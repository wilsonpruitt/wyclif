# Translation brief: incarnacione 08-b–08-d

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/incarnacione/wyc-incarnacione-08-b.md chunks/incarnacione/wyc-incarnacione-08-c.md chunks/incarnacione/wyc-incarnacione-08-d.md` once and fix what it reports.
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

## Glossary (the 314 rows these chunks use; the full file is GLOSSARY.md)

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
| predestinatus, -i | the predestinate (sg. "a predestinate [person]") | Never "the elect", which is *electi* and gets "the elect". |
| prescitus, -i | **the foreknown** | ⭐ Wyclif's technical term for those God foreknows will be damned. It is **not** "the reprobate" (*reprobi* → "the reprobate"). Explain it in a note at its first occurrence in **each work**. The English word misleads on its own and Penn explains it only once (T. p. 361 n. 12). Pilot. |
| presciencia | foreknowledge | |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| temporalia | temporal goods | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| respectus; respectivus | relation; relational | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
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
| descripcio | definition | Not "description" (T. p. 363). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| citra fidem | short of faith | The contrast with *ex fide*: held on evidence, not as faith teaches. Ruled 2026-09-28 (4 sites). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| citra Christum | short of Christ | As *citra fidem*. Ruled 2026-10-02 (45.8). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| dyameter / costa | diameter / side | The geometers' terms (the square's incommensurable diagonal). Ruled 2026-10-02 (97.21 ff.). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |
| humanitas | the humanity | The nature the Word assumed, body and soul; with the article (*humanitas sit Christus*, "the humanity is Christ"). Not "the human nature", which is *natura humana*. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| incommunicans / incommunicantes (*nature*) | that do not communicate (with one another) | None predicated of, or shared with, another (Godhead, body, soul). Not "incommunicable": keep the participle. Ruled 2026-10-22 (Wilson; *Incarn.* 1.4). |
| dimittere / dimissio (*naturam*) | lay aside / the laying-aside | Letting go the assumed nature, so the union would be dissolved. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 2.23). |
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
| ypostatice | hypostatically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 12.2). |
| Sermo (beside *Verbum*) | Speech | The divine title, capitalised; *Verbum* stays "the Word". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 16–17). |
| sophistice | sophistically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 15). |
| de vi vocis / de vi sermonis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| minoracio | lowering | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| humiliacio | humbling | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26–28). |
| immediate | without intermediary | The scholastic sense, ⛔ not "at once". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 30.30). |
| humanitus | humanly | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* passim). |
| suppositum | supposit | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 34.24). |
| individuum | individual | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 35.7). |
| in quantum (reduplicative) | insofar as | As *secundum quod*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37.9). |
| unio | union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 39). |
| universitas creaturarum | the totality of creatures | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37). |
| in effectu | in actual fact | As against in potency or in name; ⛔ not "in effect" (modern "virtually"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 47.10). |
| animare | animate | The argument turns on it (45.30–46.4). Ruled 2026-10-22 (coordinator, delegated). |
| communicacio ydiomatum | communication of idioms | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.1). |
| predicacio actualis / aptitudinalis / habitudinalis / mixtim | actual / aptitudinal / habitudinal / mixed predication | *Habitudinalis* is its own term (the four MSS at 49.6), not under *habitudo*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.5–16). |
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
| libere contradictorie | freely, as between contradictories | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 76.15). |
| ypostasis | hypostasis | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| ydemptitas ypostatica | hypostatic identity | Beside *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 84.20). |
| passionatus | subject to passion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| eiusdem / consimilis / alterius racionis | of the same / like / another kind | The species-sense of *racio*; *racio speciei* "the account of the species" (Aristotle's *logos*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.4, 87.17). |
| principiari | be constituted from principles | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.7). |
| univocacio | univocation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.27). |
| accidentatus | subject to accidents | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.4). |
| in recto / in obliquo | in the direct case / in an oblique case | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.25). |
| passibilis | passible | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.12). |
| signum / signatum | sign / thing signified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 91.2–6). |
| conveniencia / convenire (*in*) | agreement / agree | The argument of 90–91 turns on it; not "fittingness" (that is *congruencia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 90). |
| humidum infantile / radicale | the moisture of infancy / radical moisture | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 94.9). |
| conversari | live one's life (among men) | Beside *conversacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.25). |
| esse intelligibile | intelligible being | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 99.23). |
| extraneare | estrange | *Affeccio extraneandi* "an affection of estrangement". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 98.16). |
| ministerialiter | ministerially | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 100.17). |
| res racionis | thing of reason | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| universitas creata | the created totality | Beside *universitas creaturarum*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| significatum | significate | Kept apart from *signatum* "thing signified". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 111). |
| sermo vocalis | the spoken word | Against *Sermo* "Speech", the divine title. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 113). |
| predicacio secundum essenciam / formalis | predication by essence / formal predication | Wyclif's modes of predication (cf. *predicacio secundum causam*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 115–116). |
| forma substancialis | substantial form | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| concepcio (figure) | conception | The grammatical figure. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| accidens | accident | The category; *accidit* "befalls". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| conversio (of a proposition) | conversion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.30). |
| humanitacio | humanation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 126.12). |
| deduccio | deduction | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.21). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| recencius | more freshly | Pilot (*Dial.* 2.10) |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| ydiota | unlettered man | Never "idiot". Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| collacio | conferral | Of a gift or endowment; paired with *ablacio* "taking-away". Ruled 2026-10-02 (*Eccl.* 16, 385–386). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| falsarius | falsifier | The opponent's epithet. Ruled 2026-10-02 (*Eccl.* 17, 414.6). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| univoce | univocally | Ruled 2026-10-02 (*Eccl.* 21, 514.4). |
| incompossibilis | incompossible | Beside *compossibilis*. Ruled 2026-10-02 (*Eccl.* 22, 522.1). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| venia | forgiveness | Kept apart from *condonacio* "pardon". Ruled 2026-10-02 (*Eccl.* 23, 573.4). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| procuratoria potestas | proctorial power | From *procurator* "proctor". Ruled 2026-10-07 (*Pot. pape* 63.9). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| Lincolniensis | Lincoln | Robert Grosseteste, bishop of Lincoln (S note at first occurrence), as in *De ecclesia*. Ruled 2026-10-07 (*Pot. pape* 59.8). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| infundabilis; infundabiliter | without foundation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 195–196). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| carismata; carisma | CONTEXTUAL: charisms / chrism | "Charisms" (gifts; *Pot. pape* 176.1). Singular *misticum carisma* in Augustine's sense of the anointing that names Christians (*chrisma*, *Pot. pape* 312.16) "chrism", with a T note. Ruled 2026-10-08; CONTEXTUAL 2026-10-12 (coordinator, delegated). |
| primicia (virtutum) | being first (in the virtues) | Kept apart from *primatus* "primacy" and *primitas* "firstness". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 228.33). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| imperium (vicarium, autoritativum) | command (vicarial, authoritative) | The power to command (*par in parem non habet imperium*); "empire" only of the Empire. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 263.2). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| correptibilis | open to reproof | Beside *corripere* "reprove". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 301.3). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| procuratorium | proctor's mandate | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 336.11). |
| spissius (vivere) | more closely | Of living to a rule. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 338.13). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| civilitas cesarea | caesarean civil standing | After *civilitas* "civil standing" and *papa cesareus*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.31). |
| involucrum | wrapping | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 357.9). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |
| coloracior | more colourable | Comparative, with the *color* / *colorabilis* rows. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 384.15). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |

---

## Chunk 08-b: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-08-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-08-b
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "127.5–130.7"
divisions: "cap. 8 (heading 'Cap. VIII.' at 123.0); part 2 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "780 words; 776 confirmed by Fordham or the vote; 4 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n166–n169 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 8, part 2: [TITLE]

## ¶1 · 127.5–128.8

> [p. 127] Et quoad diffiniciones hominum dico quod nunquam inventa est a philosophis aliqua probabilis diffinicio sive descripcio hominis, quin illa univoce conveniat Iesu nostro. Est enim animal racionale mortale ante passionem, sicut veteres describebant hominem integrum⁴ secundum noticiam imperfectam, quam de ipso habuerant,⁵ quos⁴ sequitur Augustinus in De Qualitate⁶ Anime ca°.⁷: est iterum racionalis substancia ex corpore et anima composita tam post resurreccionem quam ante; sicut Augustinus describit hominem perfectum 15°. De Trinitate ca°. 7°.: est tercio anima racionalis habens corpus ab instanti sue concepcionis et ulterius in eternum. Et sic loquitur Augustinus de homine ut⁸ ad personam attinet, Ome. 19,⁹ exponens illud Ioh. 5. ‘Potestatem dedit ei iudicium facere, quia filius hominis est.’ ‘Ex virgine, inquit, Maria homo factus est filius hominis; sed hanc potestatem temporalem faciendi iudicium non haberet, nisi acciperet¹⁰ et esset homo prius sine hac potestate. Sed ipse filius hominis, qui et Filius Dei: herendo¹¹ enim ad unitatem persone filius hominis¹² Filius¹² Dei facta est una persona eadem Filius Dei et filius hominis. Quid autem propter¹³ quid habeat,¹³ dinoscendum est. Filius hominis habet animam, habet corpus: Filius Dei, quod est Verbum Dei, habet animam,¹⁴ tanquam anima habens corpus; et sicut anima habens corpus non facit duas personas sed unum hominem, sic¹⁵ Verbum habens hominem¹⁵ non facit duas personas sed unum Christum.’ Et sequitur. ‘Quid est homo? anima racionalis habens [p. 128] corpus. Quid est Christus? Verbum Dei habens hominem.’ Ex istis¹ patet quod supradicta sentencia est¹ beati Augustini et Hugonis de Sancto Victore cum aliis; scilicet, quod omnis homo est anima vel spiritus habens corpus. Et credo quod non est possibile hominem completum esse, nisi habeat tempore suo corpus: quia nisi assit corpus organicum, anima non creatur. Unde et Christus habuit corpus in triduo.

[ENGLISH]

## ¶2 · 128.9–129.12

> [p. 128] Quod si 4°. volumus² describere hominem in sua communitate maxima, patet quod Christus fuit univoce homo cum aliis: cum hec descripcio hominis communissima sit superior ad descripcionem triplicem supradictam. Pro quo notandus est Lincolniensis in suo Exameron de opere sexte diei, qui post exposicionem huius—‘Faciamus³ hominem ad ymaginem et similitudinem nostram’—sic³ scribit: ‘Quid autem sit homo, ex hic cognitis et auditis diffiniamus: non⁴ enim egemus mutuari⁴ diffiniciones alienas. ‘Homo, inquit, est creatura racionalis, facta ad ymaginem conditoris.’⁵ Unde exponens illud Gen. 2°. ‘spiravit in faciem eius spiraculum vite,’ ita scribit: ‘Deus verbo⁶ beneplaciti⁷ spiraculum vite id est, animam racionalem formavit, et⁷ in unitatem persone corpori formando infudit.’ Et sequitur: ‘per hoc, quod “homo factus est in animam viventem,” notatur quod homo interior est homo, et corrupto homine exteriori nichilo minus manet veritas et personalitas uniuscuiusque hominis in subsistencia hominis interioris; quod ex verbis Domini satis insinuatur, cum dicit Matt. 22°. “Ego sum Deus Abraham, Deus Ysaac, et Deus Iacob: non est Deus mortuorum sed vivencium.”’ Hec Lincolniensis. Quamvis enim Christus sit Deus mortuorum prima morte, non tamen est Deus obiective beatificans mortuos secunda morte. Et hoc sonat theos in uno sensu. Cum autem Deus tempore Moysi particulariter dixit se esse Deum illorum patriarcharum [p. 129] non solum pro lapso tempore cum hodie non daret Moysi evidenciam ad credendum Deum tunc velle iuvare semen eorum; non mirum si isto argumento Salvator imposuit silencium Saduceis de negacione resurreccionis mortuorum. Cum enim ipsi perpetuo vixerant in spiritu, nec desiderium naturale ad naturam corpoream extingui poterat¹; sequitur quod sancti patriarche non ab hoc perpetuo finaliter sint frustrandi, licet secundum quid mortui sint ad tempus. Alii autem presciti mortui sunt simpliciter morte perpetua; et ista est exposicio beati Augustini Ome. 43. super illud Ioh. 8: ‘Si quis sermonem meum servaverit, mortem non gustabit in eternum.’

[ENGLISH]

## ¶3 · 129.13–129.26

> [p. 129] Nec est negandum a sic dicentibus quin angeli sint homines, iuxta testimonium scripturarum. Quod² si obicitur scripturam dicere² angelos esse viros, et per consequens pari auctoritate concedendum esset fore distinccionem sexuum angelorum. Sed sic arguens non recolit quod ‘vir’ notat etatem, formam, sexum,³ probitatem. Concedendum est ergo sine distinccione sexuum omnem creaturam racionalem virentem virtutibus virum esse. Unde Ierem.⁴ 31. dicitur significanter de beata virgine involvendo⁵ Christum duplici matricula, ‘femina circumdabit virum’; non quod tunc fuit vir forma corporis vel etate, sed quia omni genere carismatum tunc pollebat⁶; vel quia⁷ boni angeli sic virtutibus semper virent,⁸ non mirum⁹ si⁹ scriptura sine implicacione¹⁰ distinccionis sexuum verissime tales angelos vocet ‘viros.’

[ENGLISH]

## ¶4 · 129.27–130.7

> [p. 129] Sed ulterius non est negandum quin Christus habet racionem equivocam individuantem, secundum quam est Iesus, que non potest alteri individuo convenire. Aliter enim non esset essenciale principium generis¹¹ Christiani, nisi in eo quod esset proprietatum collacio addita nature specifice per [p. 130] quam individualiter a singulis aliis distinguitur: ut dicit Anselmus in De Incarnacione 7°., ‘Quis alius, queso, est Deus et homo, et¹ ex illis principiis individuantibus temporaliter procreatus,² ex quibus efficitur noster Iesus?’ Sed³ procul hoc ad inferendum³ diversitatem specificam, quia per idem omnia que individualiter distinguuntur differrent⁴ specifice.

[ENGLISH]

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference Augustinus (127.11); reference Gen. i. 26. (128.15).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
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

p. 128:
1–1 patet supradicta sentencia que est A B C.
2 voluerimus C.
3–3 faciamus hô etc. B.
4–4 non negemus mutuari A B C; non enim egemus mutari O.
5 auditoris O.
6 verbo om. A B C.
7–7 spiraculum . . . et om. O; in om. A B C.

p. 129:
1 poterit A B C.
2–2 quod si obicitur dicere A C; quod obicitur dicere B; et si obicitur scripturam dicere O.
3 sexuum O.
4 Ezech. A B C.
5 îuoluen (an pro involvente?) O.
6 possidebat O.
7 ergo add. O.
8 vivunt super A B C; semper vivunt O; virent ex ipso textu paulo superius inventum restitui.
9–9 nimirum B.
10 multiplicacione A B C.
11 ergo A B C.

p. 130:
1 et om. C.
2 procreatus om. A B C.
3 licet procul hoc sit ad ferendum O.
4 different in rasura alter. man. A; indifferenter B.
5 personalitas A B C.
6 Christi add. A B C.
7 equivoco A.
8 Christo A B C.
9 ut O.
10 personalitas C.
11_11 argumenti . . . maior om. O; quod om. C.
12_12 sicut . . . temporalem om. A B C.
13 eternaliter O.
14 analoga A B C; anagᵃ[?] O.
15_15 in specie . . . univoce bis O.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 127: a ^ l ^ a ' le racionale | rociofialis sub- | stancia ex cor- 1 1 | pore et anima | habens corpus. | vix per rasuras distingui poiest in
p. 128: ereotura rado- | nalis facta ad m | ymaginem condi- | becatnea* u7iTg
p. 129: mortui secundvm | mortui morte | ex ipso textu paulo superius inventum restitui.
```

---

## Chunk 08-c: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-08-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-08-c
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "130.8–134.3"
divisions: "cap. 8 (heading 'Cap. VIII.' at 123.0); part 3 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "979 words; 976 confirmed by Fordham or the vote; 3 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n169–n173 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 8, part 3: [TITLE]

## ¶1 · 130.8–132.9

> [p. 130] Tercio principaliter arguitur quod Christus non sit univoce homo cum aliis eo quod non est univoce cum alio homine individuum vel persona. Nam solum personalitate⁵ eterna est persona⁶; et illa in nullo univoce⁷ convenit cum personalitate creata: ergo Christus non est univoce persona cum alia creatura. Maior patet ex hoc quod aliter, sicut dixit Nestorius, esset in ipso⁸ duplicitas personarum, quia una personalitas eterna et alia temporalis: nec⁹ dubium quin, si multiplicantur raciones personales multiplicabuntur et persone; quia unius persone una tantum est racio personalis.¹⁰ Et patet minor¹¹ argumenti ex hoc quod non est maior¹¹ conveniencia, imo tanta differencia inter personalitatem eternam et quamlibet aliam temporalem sicut¹² et inter essenciam eternam et quamlibet aliam temporalem¹²: sed quelibet essencia eterna¹³ non convenit eciam in esse univoco cum alia temporali: ergo per idem nec personalitas. Hic videtur michi probabile quod personalitas Christi sit equivoca vel analogica¹⁴ cum personalitate cuiuscunque alterius fratris sui; et tamen conveniunt summe univoce in¹⁵ specie vel natura. Ideo non sequitur, si Christus non sit univoce¹⁵ cum alio homine individuum vel persona, quod exinde non sit cum isto univoce species vel natura: quia notum est quod univocacio in superiori non arguit univocacionem in inferiori; nec equivocacio inferioris arguit [p. 131] equivocacionem communiorum,¹ ut evidet in exemplo.² Nam omnia creata per se³ in genere diverso⁴ per differencias oppositas univocantur in genere et non citra; ut substancia et accidens univocantur quodammodo in analogo transcendente, homo et asinus in genere animalis, et ita de aliis: ydiotes⁵ eciam et Hercules equivocantur in signo hominis, et tamen univocantur in genere corporis sive⁶ substancie: correspondenter Iesus et Petrus equivocantur in signo⁷ personalitatis et tamen univocantur in specie hominis, et in quolibet creato genere plus communi: quia correspondenter, ut aliquid est communius, magis⁸ univocat; et ut particularius, sic et minus: in tantum quod persona vel individuum non potest univocare secum personam aliam; ut persona Verbi non potest assumere quamlibet personam hominis, sicut nec aliquam, quia tunc persona esset summe communicabilis. Univocacio enim realis de qua nunc⁹ [est] sermo, est quando aliqua secundum eandem racionem communicant vel conveniunt in communi; ut quelibet persona hominis est eadem communis species que est homo sub illa communi racione—creatura racionalis ad ymaginem Dei facta—persona autem hominis equivoce communicatur naturis¹⁰ oppositis, cum alia sit racio vel individuandi condicio, que est hoc corpus, et alia racio vel individuandi condicio, que est hic spiritus. Et sic intelligunt illi qui dicunt personam descriptive esse¹¹ naturam racionalem¹¹ incommunicabilis¹² essencie vel¹² existencie. Nec¹³ est negandum quin sub eisdem signis licet equivoce analogicatur tam increata personalitas quam creata; ut quelibet persona divina est racionalis nature individua substancia, et quelibet persona hominis est raciocionalis nature¹⁴ individua substancia; sed nature¹⁴ sunt multum equivoce tam racionales quam essencie¹⁵ vel nature: [p. 132] Petrus eciam est multum equivoce substancia vel individuum respectu persone alterius increate. Sed utrobique est racio creata exemplata analogice in racione superiori eiusdem nominis increata. Ideo laboraverunt priores doctores ad habendum in suis descripcionibus nomina significancia simul licet equivoce tam exemplaria eterna quam eciam exemplata; ut veritas, iusticia, liberum arbitrium; et persona analogicatur¹ secundum Anselmum² et Boecium sub istis nominibus.

[ENGLISH]

## ¶2 · 132.10–132.12

> [p. 132] Sed obicitur primo per hoc quod Christus est individuum speciei humane, et preter hoc est individuum nature divine: ergo est duplex individuum sicut³ est duplex³ natura.⁴

[ENGLISH]

## ¶3 · 132.13–132.18

> [p. 132] Hic dicitur negando consequenciam sicut non sequitur, si Christus sit Filius Dei et filius hominis, quod sit duplex filius; idem enim est individuum nature humane et nature divine, sed per accidens individuum nature humane, quia secundum naturam assumptam, per se autem individuum, persona, vel suppositum nature divine.

[ENGLISH]

## ¶4 · 132.19–132.23

> [p. 132] 2°. obicitur per hoc quod universale et singulare dicuntur ad aliquid et per consequens sunt simul natura: sed Christus solum temporaliter est universale: ergo solum temporaliter est singulare; et per consequens aliqua individuatio solum temporaliter inest Christo.

[ENGLISH]

## ¶5 · 132.24–133.5

> [p. 132] Hic conceditur prima conclusio. Nam singulare et⁵ universale sunt res secunde intencionis que sese mutuo relative respiciunt ita, quod singulare, ut⁶ sic, sit individuum vel suppositum speciei. Ideo nulla persona divina est ad illum sensum⁷ quoad deitatem universalis vel singularis, ut patet in De Questionibus Veteris et Nove Legis. Questione 122; sed est⁸ individuum suppositum vel persona, Cum ista sint nomina significancia analogice extra genus, ut patet de nomine individui in⁹ descripcione Boecii De Persona. Nec est vis¹⁰ quare philosophi sic varie utuntur [p. 133] nominibus. Sicut ergo Christus solum ex tempore est singularis, sic quod singularitas a posteriori accidit sue¹ individuitati vel personalitati, sicut accidit sibi quod sit persona speciei humane: ideo individuitas vel personalitas in Christo non est singularitas que supponitur speciei.

[ENGLISH]

## ¶6 · 133.6–133.12

> [p. 133] 3°. instatur per hoc quod Christus, quia iste homo, vel in quantum iste homo, est suppositum, individuum vel² persona; ergo ista singularis humanitas est causa personalitatis in Christo, sicut est in suis fratribus, et non est causa personalitatis eterne: ergo est causa personalitatis temporalis: ergo in Christo est duplex personalitas, sicut³ duplex nativitas.

[ENGLISH]

## ¶7 · 133.13–133.28

> [p. 133] Hic negatur causalis assumpta eo quod significat circumstanciam cause.⁴ Conceditur tamen de Christo vel aliis quod, quia est iste homo, ideo est persona hominis: sed non, quia persona hominis, ideo est persona; cum habet personalitatem nature superioris quam est eius⁵ humanitas, quod nulli alii homini potest competere; cum ipse solus⁶ sit homo per accidens et cum hoc summe univoce. Est autem in Christi duplex nativitas, una eterna secundum naturam divinam, que eternaliter absolute necessario personaliter nascitur et est natus; et illi accidit alia temporalis non interpellatim⁷ sed simul adveniens, secundum quam fuit natura alia et noviter persona hominis. Non enim sequitur —Christus solum temporaliter vel noviter est persona, individuum, vel suppositum humanum: ergo⁸ sic est suppositum—cum⁸ arguitur ab inferiori ad suum superius cum impedimento habente vim negacionis.

[ENGLISH]

## ¶8 · 133.29–134.3

> [p. 133] 4°. obicitur per hoc quod Christus recenter est tam corpus quam anima, et utrumque illorum est suppositum et persona: ergo Christus recenter est suppositum vel persona: sic⁹ enim Christus⁹ est corpus et spiritus creatus: [p. 134] sed utrumque illorum est per se individuum et persona: ergo Christus est persona creata: et cum eciam sit persona increata, sequitur quod duplex personalitas inest Christo.

[ENGLISH]

## Notes

## Transcription notes
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 130:
1 et om. C.
2 procreatus om. A B C.
3 licet procul hoc sit ad ferendum O.
4 different in rasura alter. man. A; indifferenter B.
5 personalitas A B C.
6 Christi add. A B C.
7 equivoco A.
8 Christo A B C.
9 ut O.
10 personalitas C.
11_11 argumenti . . . maior om. O; quod om. C.
12_12 sicut . . . temporalem om. A B C.
13 eternaliter O.
14 analoga A B C; anagᵃ[?] O.
15_15 in specie . . . univoce bis O.

p. 131:
1 9'ore[?] A B C; coîo4 pr. man. coîorû in margine altera manu O.
2 Christo A B C; ex° pr. man. et alt. man. in marg. O.
3 p^e (i.e. persone) B.
4 diviso O.
5 ydolum A B O; ydioles (sic) C.
6 sue A B C.
7 specie A B C.
8 generalius A B C.
9 modo B C; nobis O, est supplendum censeo.
10 personis B.
11–11 naturalem racionalem O.
12 essencie vel om. O.
13 nunc O.
14–14 individua . . . nature om. O.
15 encia O.

p. 132:
1 analoga B.
2 Augustinum AB C; añs & boym O.
3–3 sicut est duplex om. A B C.
4 nature A B C.
5 et om. B.
6 ut om. A B C.
7 sensum om. C.
8 est om. A B C.
9 et O.
10 vis om. C.

p. 133:
1 suᵉi A ; sui C.
2 et C O.
3 et add. B.
4 cause om. O.
5 9is (i.e. communis) O.
6 solum A B C.
7 interpolatim A B C.
8–8 ergo sic suppositum A ; ergo sit suppositum B C.
9–9 sequitur enim quod Christus A B C.

p. 134:
1-1 d'1te A B C. 2 naturarum A B C. 3 sequitur O.
4-4 tunc . . . creatum om. B. 5 Christus om. O. 6 non A; mo̅ B C; m̊ O.
7 concederent O[?].
* 8 Totus hic locus a Quod si usque ad substancie tales (p. 136, l. 25) stellulis supra notatus in Cod. O. omittitur, sic—specificantes formas sunt multe argucie O; in margine autem alia manus deficit multum adnotavit.
9 esse add. B.
CHECK (coordinator): text figure(s) 8 have no entry read here: read the plate foot before citing.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 131: creatura racionalis ad ymaginem Dei facta | ot personality | supplendum censeo.
p. 132: per acci-
p. 134: Totus hic locus a | stellulis supra notatus in Cod. | in maryine autem alia manus
```

---

## Chunk 08-d: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-08-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-08-d
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "134.4–138.22"
divisions: "cap. 8 (heading 'Cap. VIII.' at 123.0); part 4 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1205 words; 1203 confirmed by Fordham or the vote; 1 runs stood by rule (both witnesses garbled); 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n173–n177 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 8, part 4: [TITLE]

## ¶1 · 134.4–135.15

> [p. 134] Hic dicitur quod antecedens primi argumenti est verum et consequens impossibile. Nec est verum quod aliqua creatura preter Christum est primo per se suppositum vel persona; quia in omni persona creata proprietates accidentales individuant ipsam; et sic idem est sibi personalitas et singularitas que ad ipsam consequitur, sicut passio ad subiectum: Christus autem solum personatur per se primo ex¹ divinitate,¹ et non ex proprietatibus accidentalibus ut alia singularia. Ideo non mirum, si sua personalitas recipit singularitates personarum,² ut sibi accidencia, et non ut personalitates. Due ergo nature create eciam in sancto sabato sunt simul utraque eadem persona Verbi. Si ergo persona esset per se superius ad istam naturam, sicut aliquid est ad hominem, tunc sequeretur—si³ Christus est hoc singulare creatum, tunc⁴ est ista persona creata—; sicut sequitur, quod Christus⁵ sit aliquid creatum,⁴ ex hoc quod est natura creata; et tunc foret duplex persona creata, sicut est duplex natura creata, quarum utraque est persona. Modo⁶ autem ille ambe nature, et utraque illarum, sunt eciam pro triduo separate idem individuum, suppositum, et persona: licet enim sint due essencie singulares, tamen sunt unita individua substancia nature humane. Et sophista satis colorate concederet⁷ quod illa persona, demonstrando humanitatem Christi, est persona et natura eterna. Ideo in talibus oportet ultra pronomina significancia pure essencias explicare res de quibus loquitur per terminos specificantes formas.* Quod⁸ si arguitur eo ipso quo ponitur aliqua⁹ per se [p. 135] et completa causa causabilis, sequitur illud causabile: sed natura singularis in Christo cum communi creata substancia sufficit per se et complete causare creatum suppositum: ergo illis positis et unitis, sicut est in Christo, sequitur quod oportet ponere creatam personam ex illis principiis resultantem: nam eiusdem speciei specialissime est creata natura atque substancia in Christo, cuius est in quolibet fratre suo. Sicut ergo Christus est univoce cum Petro racionalis nature individua substancia, sic cum eo univoce est persona: cui enim univocatur diffinicio eciam competit univoce diffinitum. Confirmatur ex hoc quod tractantes pollitice¹ cum Christo acceptarent univoce cum aliis personam suam in testimonium et iudicium et quodlibet aliud opus sensibile vel quodlibet personale. Nec potest fingi quod deitas impedit ista principia ad causandum personam.

[ENGLISH]

## ¶2 · 135.16–136.7

> [p. 135] Hic dicitur quod minor est falsa cum nulla creatura causat naturaliter nisi de quanto a posteriori subicitur voluntati divine prius causanti. Sed voluntas divina non potest ex istis causare creatam personam: nam assumpcio impedit, vel verius iuvat ut natura creata sit suppositum increatum. Cum enim omne recipiens denudatur a natura rei recepte, oporteret Verbum vel esse duas personas, ut dixit Nestorius; vel recipiendo personalitatem creatam personalitatem increatam dimittere; quorum utrumque cum sit summe impossibile, sequitur quod natura rei exaltantis naturam assumptam, ut quasi insorbendo, non permittat² eam habere personalitatem creatam. Et hoc intendunt loquentes de suppositacione aliena. Et dicitur quod ista natura est persona gloriosissima, sed illi non competit diffinicio persone create. Pro quo notandum quod substancia est commune in Greco ad ypostasim, usiosim, et usion: quando autem diffinitur persona per nomen substancie intelligitur ypostasis, quam alii differenter explicant per nomen subsistencie. Et sic Christus non est racionalis nature individua subsistencia vel suppositum, [p. 136] nisi suppositum nature increate. Ideo natura assumpta non est formaliter persona sed ydemptice vel ypostatice. Non enim est formaliter ypostasis vel subsistencia, sed substancia vel usion. Ideo in Christo sunt formaliter tres substancie, sed unica subsistencia, sed ille due nature create faciunt unam naturam completam, que est humanitas, non autem personam, cum deest complementum ex parte cause finalis.

[ENGLISH]

## ¶3 · 136.8–136.27

> [p. 136] Ulterius conceditur quod conversantes cum Christo putando eum esse univoce personam cum aliis hominibus ex ignorrancia sue divinitatis [acceptarent],¹ univoce personam suam in testimonium.¹ Ideo non potest iudicare² vel conversari civiliter, ut patet alibi, sed omne iudicium suum foret infinitum maioris auctoritatis quam iudicium persone create. Et ita videtur de omni actu personali quem fecit humanitus: auctoritas enim consequitur personam in dignitate et non naturam accionis pure. Et patet quod descripcio persone signata convertitur cum ista racionalis nature incommunicabilis existencia. Incommunicabilis dico quoad supposita, non naturas; et ita subsistencia est contractior quam substancia, ut sumitur ad hec tria. Et ita Trinitas commune principium et commune principatum non est persona vel subsistencia, sed persone vel subsistencie. Nec est color in illa equivocacione, quod divicie sunt substancia racionalis nature, sed substancia restricta ad subsistenciam est consequens ad omne suppositum substanciale. Tales*³ sunt multe argucie quibus decipiuntur incauti, facte pro stabilienda opinione Nestorii.

[ENGLISH]

## ¶4 · 136.28–137.8

> [p. 136] Sed 4°. principaliter arguitur contra ydemptitatem specificam Christi cum aliis ex parte materie. Nam semen decisum⁴ a diversis sexubus et commixtum est alterius speciei quam simplex semen sexus feminei: sed⁵ Christus conceptus est pure ex semine sexus feminei,⁵ omnes autem alii ex commixtis seminibus maris et feminei: ergo materia ex qua [p. 137] factus¹ est Christus est alterius speciei quam materie proxime aliorum: et cum agens semper dat formam secundum condignitatem materie, ut patet philosophis, sequitur quod Christus sit alterius speciei quam alii secundum communem cursum nature univoce² procreati. Confirmatur per Commentatorem 8vo. Physicorum 9. 46. ponentem contra Avicennam quod si homo generaretur ex terra, ipse esset homo equivoce propter extraneacionem materie.

[ENGLISH]

## ¶5 · 137.9–137.21

> [p. 137] Hic dicitur quod illud argumentum deficit in pluribus. Primo in assumpto quod semen muliebre, quod differt a menstruo, non distat a virili semine nisi secundum maius et minus; sic quod semen virile de communi cursu nature sit in substancia spissius, complexione³ calidius, et informacione virtuosius. Sed quale magisterium Deo de beata virgine complexione³ mundissima descindere⁴ semen vel sanguinem pro mensura delectationis sue humilime ex gaudio salutacionis⁵ angelice, que excedat⁶ in bonitate⁷ complexionis⁷ in proporcione multitudinis et in limitacione virtutis omnem aliam materiam, ex qua fuit persona hominis procreata? quod quia factum est, unde non daretur illi capaci⁸ organo spiritus consimilis speciei?

[ENGLISH]

## ¶6 · 137.22–137.32

> [p. 137] Deficit 2°. in sequela quando infert quod materia proxima, de qua factus est Christus, sit alterius speciei quam materie proxime aliorum. Nam⁹ si, sicut est summe⁹ possibile, Deus de lapidibus¹⁰ vel quocumque alio mixto vel simplici descidisset¹¹ materiam, et commiscendo athomos¹² in utero virginali dedisset post¹³ commixturam ydoneam formam complexionalem¹⁴ humani seminis; adhuc proxima materia, ex qua talis homo fieret, foret eiusdem racionis cum aliis, licet remota materia sit diversa: aliter enim semina hominum generata ex distinctis cibariis in specie forent eo ipso disparium specierum.

[ENGLISH]

## ¶7 · 137.33–138.22

> [p. 137] Ex istis 3°. colligitur quod non refert ex qua materia Deus [p. 138] adaptet¹ materiam proximam ad hominem producendum; dum tamen reducat eam ad temperamentum complexionis seminee,² et limitet³ successive vel subito infundendo humanum spiritum in corpus debite limitatum.⁴ Nec refert quo agente Deus ad illud officium utatur pro organo: aliter enim primi parentes, qui sunt principia humani generis, non convenirent cum suis generacionibus in specie vel natura: talis tamen error auctoris in principio †caret⁵ maximum in processu. Patet deduccio ex hoc quod Adam plasmatus est de limo terre forsitan sine⁶ ministerio creature, et Eua de costa viri ab eodem opifice est formata. Sicut ergo non refert utrum ignis ab igne, vel immediate a lumine producatur ad hoc quod sit de natura ignis univoce, et sic de aliis effectibus cuiuscumque speciei vel generis; sic facta de quacumque materia prima complexione et limitacione sufficienti ad animam subiectandam, non refert ad unionem compositi⁷ ministerio cuiuscumque agentis secundi hoc factum fuerit, ut⁸ sive immediato a Deo, sive ministerio angelorum, sive per se a constellacione celesti, sive a quocumque agente secundo corpus humanum productum fuerit; non refert data anima adesse hominis sicut nec refert a quo artifice creato ydolum vel aliud artificiale fuerit⁹ fabricatum.

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 136: *argucie* (bt arguncie; print argucie) [AGREE]
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 134:
1-1 d'1te A B C. 2 naturarum A B C. 3 sequitur O.
4-4 tunc . . . creatum om. B. 5 Christus om. O. 6 non A; mo̅ B C; m̊ O.
7 concederent O[?].
* 8 Totus hic locus a Quod si usque ad substancie tales (p. 136, l. 25) stellulis supra notatus in Cod. O. omittitur, sic—specificantes formas sunt multe argucie O; in margine autem alia manus deficit multum adnotavit.
9 esse add. B.
CHECK (coordinator): text figure(s) 8 have no entry read here: read the plate foot before citing.

p. 135:
1 pollce B; polletice C; pollitice A (pro politice=civiliter, p. 136, l. 12).
2 permittant A; permittunt B.

p. 136:
1–1 codd. A B lacunam xii litterarum exhibent: cod. C omnia post verbum divinitatis ad testimonium sine lacuna omittit. acceptarent (cf. p. 135, l. 12) pro certo supplendum est.
2 indicare C.
*3 vide supra, p. 134, n. 8.
4 decisis C.
5–5 sed . . . feminei om. A B C.
CHECK (coordinator): text figure(s) 3 have no entry read here: read the plate foot before citing.

p. 137:
1 natus B.
2 univoce om. A B C.
3 commixione A B C.
4 decindere O.
5 saluatoris O.
6 excedit A B.
7–7 materia commixionis B.
8 capiti C O.
9–9 si nam perfectum sed summe O.
10 lapide B.
11 decidisset B.
12 attomos (i.e. atomos) O.
13 n⁹ O.
14 commixionalem A B C.

p. 138:
1 adept; O.
2 seminis AB C.
3 liniet A B C ; et cod. O in rasura.
4 liniatum A B C ; lĩtatû (i.e. limitatum) O.
5 caret om. A B C : forsitan pro caret codicis O. lectione cresceret vel foret legendum.
6 tñ (tamen) A B ; cû (cum) C ; sñ (sine vel sive) O.
7 suppositi A B C.
8 ut om. A B C
9 sit A B C.
10 tamen C O.
11 est om. B.
12 linite A B C ; lĩtate O.
13 invenio A B C.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 134: Totus hic locus a | stellulis supra notatus in Cod. | in maryine autem alia manus
p. 135: ovaiov. ypostasim, usiosim,
p. 136: P men) ma
p. 137: matena proxima. | materia proxuna
p. 138: materia proxima
```
