# Translation brief: incarnacione 08-e–09-b

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/incarnacione/wyc-incarnacione-08-e.md chunks/incarnacione/wyc-incarnacione-09-a.md chunks/incarnacione/wyc-incarnacione-09-b.md` once and fix what it reports.
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

## Glossary (the 341 rows these chunks use; the full file is GLOSSARY.md)

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
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
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
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| autorizare | authorize | Ruled 2026-09-28 (6 sites). |
| magnates | magnates | Ruled 2026-09-28. |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| temporalia | temporal goods | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| graduacio; graduati | CONTEXTUAL: graduation / gradation; graduates | Academic "graduation" (Dialogus, 4 sites); of rank or lordship (*graduacio dominii*, *Pot. pape* 293.33, 297) "gradation". Ruled 2026-09-28; CONTEXTUAL 2026-10-12 (coordinator, delegated). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| thema | theme | The scripture text of a sermon. Ruled 2026-09-28 (2 sites). |
| possessionati | the possessioners | Endowed religious. |
| protestacio; protestari | declaration; to declare solemnly | ⭐ The submission formula ("if anyone can teach me this is contrary to scripture or reason, I will humbly retract"). Penn and Lahey both inverted it (T. pp. 369, 378). Render it as a retraction offer, never as defiance. |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| quiditas | quiddity | Kept. Explain at first use per work ("what a thing is"). |
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| practizare | to put into practice | Ruled 2026-09-28 (coordinator, delegated) (4 sites). With *contra* + person, "practise against" (plot), *Dial.* ch. 17. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| respectus; respectivus | relation; relational | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
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
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
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
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |
| humanitas | the humanity | The nature the Word assumed, body and soul; with the article (*humanitas sit Christus*, "the humanity is Christ"). Not "the human nature", which is *natura humana*. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| incommunicans / incommunicantes (*nature*) | that do not communicate (with one another) | None predicated of, or shared with, another (Godhead, body, soul). Not "incommunicable": keep the participle. Ruled 2026-10-22 (Wilson; *Incarn.* 1.4). |
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
| misterium | mystery | Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.3). |
| moderni doctores / moderniores doctores | the modern doctors / the more modern doctors | Ockham and the *moderni*, usually unnamed. Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.1). |
| sancti | the saints | The fathers. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.15). |
| probabiles doctores | reputable doctors | *Probabilis*: worthy of credence (cf. *probabiliter*). Ruled 2026-10-22 (Wilson; *Incarn.* 7.1) as "approved doctors"; changed the same day (coordinator) to free "approved" for *approbati*. |
| approbati doctores | approved doctors | Kept apart from *probabiles doctores*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 13.3). |
| copulative (adv.) | conjunctively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 9.23). |
| ypostatice | hypostatically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 12.2). |
| sophistice | sophistically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 15). |
| de vi vocis / de vi sermonis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| protervus | obstinate | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21). |
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
| moderniores loquentes | the more modern speakers | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 59.21). |
| passio (against *accio*) | being-acted-on | The category; G note at the first occurrence in a chunk. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 60.13). |
| supposibilis | that can be supposited | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 64.14). |
| per se / per accidens | of itself / by accident | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a divisione | the topic from sufficient likeness / from division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| pretericio | being past | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| solvere / solucio (of the union) | loose / loosing | Except inside a Douay quotation (John 10:35 "cannot be broken"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| ypostasis | hypostasis | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| peccabilis | able to sin | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| medium (logical) | middle term | Of a syllogism; elsewhere "means" by context. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| ydemptitas ypostatica | hypostatic identity | Beside *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 84.20). |
| passionatus | subject to passion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| intricaciones sophistice | sophistical entanglements | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 82). |
| eiusdem / consimilis / alterius racionis | of the same / like / another kind | The species-sense of *racio*; *racio speciei* "the account of the species" (Aristotle's *logos*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.4, 87.17). |
| principiari | be constituted from principles | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.7). |
| accidentatus | subject to accidents | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.4). |
| in recto / in obliquo | in the direct case / in an oblique case | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.25). |
| mobilis / mobilitas | movable / movability | Of Christ's humanity (ch. 7). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.11). |
| passibilis | passible | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.12). |
| conveniencia / convenire (*in*) | agreement / agree | The argument of 90–91 turns on it; not "fittingness" (that is *congruencia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 90). |
| predicacio synecdochica | synecdochic predication | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.27). |
| humidum infantile / radicale | the moisture of infancy / radical moisture | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 94.9). |
| conversari | live one's life (among men) | Beside *conversacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.25). |
| esse intelligibile | intelligible being | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 99.23). |
| faccio | making | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 100.6). |
| extraneare | estrange | *Affeccio extraneandi* "an affection of estrangement". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 98.16). |
| ministerialiter | ministerially | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 100.17). |
| mobile (noun) / primum mobile | a movable / the first movable | Against the adjective *mobilis*; ch. 7 turns on it. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 107, 116). |
| immobilis / immobilitas | immovable / immovability | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| res racionis | thing of reason | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| universitas creata | the created totality | Beside *universitas creaturarum*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| significatum | significate | Kept apart from *signatum* "thing signified". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 111). |
| predicacio secundum essenciam / formalis | predication by essence / formal predication | Wyclif's modes of predication (cf. *predicacio secundum causam*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 115–116). |
| forma substancialis | substantial form | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| concepcio (figure) | conception | The grammatical figure. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| accidens | accident | The category; *accidit* "befalls". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| figura / figuratum | figure / thing figured | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 121.23). |
| conversio (of a proposition) | conversion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.30). |
| humanitacio | humanation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 126.12). |
| quiditativus | quidditative | Beside *quiditas*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 126.24). |
| deduccio | deduction | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.21). |
| racio (individual, personal) | account | *Racio individui / persone* "the account of an individual / a person", as *racio speciei*; not "aspect" (the row against *substancia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 8, 129–132). |
| vir (against *homo*) | man (*vir*) | Where Wyclif sets *vir* against *homo*, the Latin in parentheses. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 129.15–26). |
| analogicari | be said analogically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 131.27). |
| exemplaria / exemplata | exemplars / things exemplified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.6). |
| res secunde intencionis | things of second intention | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.25). |
| complexio | complexion | The mixture of qualities. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137–138). |
| materia proxima / remota | proximate / remote matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137.1). |
| personari | be made a person | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 134.10). |
| colorate | with colour enough | With a plausible ground (cf. *color*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 134.26). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |
| epilogus / epilogare | recapitulation / recapitulate | Ruled 2026-10-22 (Wilson; *Incarn.* 3.25, prol 2.14). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office; *quale magisterium* "what a feat of mastery" (*Incarn.* 137.14) | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
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
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| falsarius | falsifier | The opponent's epithet. Ruled 2026-10-02 (*Eccl.* 17, 414.6). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| incompossibilis | incompossible | Beside *compossibilis*. Ruled 2026-10-02 (*Eccl.* 22, 522.1). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| palliacio; palliare | cloaking; to cloak | Ruled 2026-10-02 (*Eccl.* 23, 566.27). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| remissio; remittere | remission; to remit | Headword row (cf. *condonacio* "pardon", *venia* "forgiveness"). Ruled 2026-10-02 (*Eccl.* 23). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| discrasia | distemper | Physicians' term. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 223.1). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| eleccio passiva / activa | passive / active election | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 254.31). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| imperium (vicarium, autoritativum) | command (vicarial, authoritative) | The power to command (*par in parem non habet imperium*); "empire" only of the Empire. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 263.2). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| precellencia | pre-excellence | Kept apart from *preeminencia* "preeminence". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 274.33). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| precellenter | pre-excellently | Adverb beside *precellencia* "pre-excellence". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 291.2). |
| correptibilis | open to reproof | Beside *corripere* "reprove". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 301.3). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| pallium privilegii | cloak of privilege | Kept apart from *palliacio* "cloaking". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-a). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| remisse (of assent) | with slackened [assent] | Opposed to full assent in the degrees of belief. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 328.18). |
| gradus (of belief) | degree | The four degrees of belief (*Pot. pape* 327.18 ff.). Ruled 2026-10-12 (coordinator, delegated). |
| potissimus; pocior (Antichristus) | foremost; greater | Superlative and comparative kept visible as a pair. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.28, 331.12). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| coloracior | more colourable | Comparative, with the *color* / *colorabilis* rows. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 384.15). |
| specularis prudencia | the prudence of a watchman | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| servitus ydolorum | servitude of idols | Beside *servitus laboris*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| ingeniacio | wit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 394). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| precellere | excel | Verb beside *precellencia* "pre-excellence"; not "pre-excel". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 399.28). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |
| nimis | exceedingly | Medieval intensive (= *valde*); "too much" only where excess is the point. Ruled 2026-10-12 (close-out R2; *Pot. pape* 169.2). |

---

## Chunk 08-e: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-08-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-08-e
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "138.23–142.9"
divisions: "cap. 8 (heading 'Cap. VIII.' at 123.0); part 5 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "908 words; 906 confirmed by Fordham or the vote; 2 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n177–n181 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 8, part 5: [TITLE]

## ¶1 · 138.23–140.21

> [p. 138] Et si dicatur quod Deus, non potest per se, nec cum tam disparibus secundis agentibus, tales effectus producere; tum,¹⁰ quia nec est¹¹ auctenticum nec expertum; sed raciones seminales forent superflue limitate¹²: quoad illud videtur michi quod talis contencio de Dei persona sit satis superflua, ubi non evidenter scimus racionem pro vel contra producere: unde leve verbum multorum est et satis inevidens—‘ego non sum expertus hoc, vel ego non inveni¹³ hoc scriptum in historiis michi auctenticis: ergo non est verum’.—Et ex [p. 139] alio latere sollicitando fingere quod agens secundum potest naturaliter in talia¹ inexperta excedit limites philosophi naturalis. Sed inter alia opera, que de Deo credimus, partus virginis tenet locum satis probabilem in lumine² naturali; cum in multis aliis speciebus animalium narrantur femelle sine commixtione³ seminis vel tactu maris concipere. Sed admiracio ineffabiliter nobis mirabilis est quod post limitacionem⁴ subitam corporis capti⁵ de pura virgine copulatus sit Deus⁶ pro instanti generacionis⁶ nature complete, et hoc ypostatica unione. Ideo⁷ hoc oportet nos ex fide supponere credendo quod nullum aliud tale novum potest fieri, licet hoc fuerit in natura creata analogice exemplatum de ypostatica unione⁷ mentis cum corpore. Et hinc tam sepe exemplificat Augustinus cum simbolo Athanasii quod ‘sicut anima racionalis et caro unus est homo, ita⁸ Deus et homo unus est⁸ Christus.’ Decuit enim auctorem nature specialiter post peccatum hominis remissibile per talem assumpcionem viri⁹ ex femina speciem hominis innovare: ut, sicut primo formatus est mas ex non- homine, secundo¹⁰ femina ex homine¹⁰ sed ex mare solummodo, tercio autem ex his sexubus commixtis sunt alii communiter procreati; sic quarto pro complemento iusticie¹¹ per se stantis in quatuor¹¹ compleat Deus virum celestem pure ex femina; cuius necessitas patet alibi. Nec sequitur ex illis superfluitas limitacionis racionis seminalis diversis mixtorum generibus, ut experiencia philosophorum testatur, quod multa genera animalium, in quibus est distinccio sexuum, tam ex putrefaccione quam ex semine procreantur. Et tamen, cum hoc dicunt philosophi quod nec sexuum distinccio, nec racionis seminalis limitacio est aliquo modo superflua; sic¹² latet in visceribus nature, quid Deus disposuit secundum potenciam obediencialem creature sue per se facere, et quid agens [p. 140] creatum a seculis multis absconditum sufficit preter communem cursum nature producere. Et circa¹ possibilitatem talium sollicitantur multi superflue: ut illi, quod demones² possunt in aspectu placido celi, mediantibus virtutibus mixtorum sicut herbarum et lapidum, mirabilia vulgo inopinabilia per se efficere: illi quod celum secundum diversas figuras et aspectus astrorum per se³ potest in talia: et hi quod homines possunt cum iuvamine demonum et constellacione celestium mirabilia inopinata producere. Et in speculacione talium theologizant speculativi inaniter. In practica vero mathematici consumunt tempus figuras celi superflue prestolantes, et demones periculosius consulentes. Sufficit ergo pio theologo quod sciat in genere talia mirabilia ab agente secundo posse fieri: 2° quod sciat istis agentibus secundis a Deo, a quo est omnis potencia, terminos secundum maximum et minimum limitari; nec⁴ creaturam aliquam posse in aliquid, nisi secundum eius ordinacionem et benevolenciam limitantem: et 3°. quod Deus ex condicione omnipotencie⁵ facit eo ipso quodlibet dandum opus quo vult ipsum a quoquam fieri, et istam condicionem potencie non potest communicari alteri.

[ENGLISH]

## ¶2 · 140.22–141.15

> [p. 140] Quantum ad testimonium Commentatoris patet quod dictum Averrois⁶ non debet esse alicui philosopho, et minus theologo, testis auctenticans, cum tam in philosophia quam fide presumptive⁷ vel invide sepius⁷ deviavit. Fautor autem Commentatoris, cui placeret⁸ dictum suum palliare, posset fingere ipsum de Avicenna concipere; quod posset esse homo, cuius proxima materia subiecta anime foret terra, et per consequens corpus alterius speciei quam mixtum organicum⁹ a sibi simili in specie procreatum; et cum forme dantur secundum disposicionem materie, si haberet¹⁰ animam, ipsa foret ab humanitate nostra disparis racionis. Nam in tam [p. 141] vilem materiam non inducit natura formam¹ simee vel pigmee:¹ vel 2°. quod natura plus ingenians² circa produccionem hominis quam animalis alterius imperfecti, quod corpus sicut et anima³ non posset produci naturaliter nisi a racionali supposito producatur. Ideo non sequitur—animal imperfectum potest ex putrefaccione produci: ergo homo— qui est finis uniuscuiusque alterius animalis, quia effectum preciosiorem virtus regitiva universitatis plus curat. Unde figuracionem embrionis oportet fieri a virtute informativa ab anima hominis per species triplices dirivata, per fomentum caloris consimilis in matrice, et per nutricionem concepti de sanguine menstruo parientis. Quod si alius sit modus producendi quoad corpus hoc est auctori nature specialiter reservatum. Sed totum illud vix moveret protervum ad credendum possibilitatem negative que petitur.

[ENGLISH]

## ¶3 · 141.16–142.9

> [p. 141] Tercii autem dicunt quod nemo post primum parentem potest produci nisi materialiter⁴ producatur ab homine propter amorem humani generis nutriendum. Nam racione stipitis et cognacionis oportet nutriri amorem inter homines ultra bruta, quia aliter fuisset facile post peccatum Adam totam suam generacionem sicut genus Caim⁵ exstinguere et aliud genus hominum ex disparato principio⁶ procreare⁶ sine hoc quod Christus paciatur pro salvanda specie. Et tunc esset homo species imperfecta, sine qua mundus posset existere; cum, nullo homine existente, celum posset ut vermes hominem⁷ de novo producere; †et multo magis elementum⁸ quod est⁹ gracia hominis tamquam finis non esset de substancia universali;¹⁰ et, sicut¹¹ situs spere¹² corruptibilium posset vacuus a corpore.†¹³ Sed cum iste tractatus multum¹⁴ distat a puncto proposito, redeundo dicitur quod philosophicum et facile est catholicum sustinere quod primus homo fiebat de terra, secundus sexus [p. 142] ab illo, et tercius ab ambobus; et sic gradatim de genere consequente quousque novus homo atque novissimus eiusdem speciei cum aliis fiebat ex femina; et quinto¹ omnis homo secundum animam fit ab illo circulariter a quo ultimate reficitur: quinarius autem et senarius sunt numeri circulares. Non enim credo quod species humana peribit, vel quod possit sub tanto auctore eciam quoad perfeccionem illam² deficere.

[ENGLISH]

## Notes

## Transcription notes
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
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

p. 139:
1 talis O.
2 lı̃me A B C.
3 commixione A B C.
4 liniacionem A B C.
5 capi O.
6-6 deus per generacionem A B; deus per generacionis C.
7-7 ideo . . . unione om. A B C.
8-8 ita . . . est om. O.
9 utri O.
10-10 secundo . . . homine om. O; secundo ex femina ex homine C.
11-11 persone stantis in quarto A B C.
12 sicut A B C.

p. 140:
1 ita O.
2 denoıacōes (i.e. denominaciones) O.
3 per se om. C.
4 et sic C; ut O.
5 oıpoe A B C.
6 aūois A B; auctoris C; aūoȳs O.
7–7 p̃supue ve inde septus O.
8 placet B.
9 tamen add. A B C.
10 sed haberent O.

p. 141:
1 symee vel pigmei A B C.
2 ingenias (pro ingeniãs) B.
3 animans B.
4 naturaliter prima manu correctum e materialiter A.
5 cayn A B C.
6-6 principio provocare A; principio hominum provocare B.
7 hominem in margine alia manu suppletum A.
8 elementum om. A B C.
9 est om. A C.
10 universi A B C.
11 sicut om. O.
12 spere (i.e. sphaerae) codd. omn.
13† hic locus corruptus videtur.
14 membrum O.
CHECK (coordinator): text figure(s) 13 have no entry read here: read the plate foot before citing.

p. 142:
1 ergo A B C.
2 secundam A B C; illam (an pro ullam?) O.
3 ẏdẽptıte O (an Christi ydemptitate legendum?).
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 138: materia proxima
p. 141: prima manu correctum e | in margine alia manu suppletum | codd. omn. | hic locus corruptus videtur.
p. 142: \_Epilogat posicionem de humanitate; et, narrando tres radices causantes modernorum discrepancias, dissolvit tres obiectus eorum per ordinem. | Gives a summary of the aathor's position concerning the humanity of Christ. | Explains the three sources from which the modern divsrsities of opinion have arisen. | Deals with three principal objections to the author f s positio7i.~\ | assumed by the | word is perfect | man composed of .. . . .. . | body and a | and by hypol | staticunion iden- , , . , tified with the | Word in person, notinnature.
```

---

## Chunk 09-a: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-09-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-09-a
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "142.0–146.24"
divisions: "cap. 9 (heading 'Cap. IX.' at 142.0); part 1 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1135 words; 1128 confirmed by Fordham or the vote; 4 runs stood by rule (both witnesses garbled); 3 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n181–n185 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 9, part 1: [TITLE]

## ¶1 · 142.0–142.0

<!-- the editor's bracketed argument at the chapter head: a Latin summary, then his own English
     summary in the same bracket (see the volume CARD for what is translated) -->

> [p. 142] [Epilogat posicionem de humanitate; et, narrando tres radices causantes modernorum discrepancias, dissolvit tres obiectus eorum per ordinem. I. Gives a summary of the author’s position concerning the humanity of Christ. II. Explains the three sources from which the modern divsrsities of opinion have arisen. III. Deals with three principal objections to the author’s position.]

[ENGLISH]

## ¶2 · 142.10–142.12

> [p. 142] Consequens est iuxta ponere sentenciam illam sentenciis modernorum, ut diversitas summe veritatis magis appareat et obiectus, quos adversantes invehunt, planius dissolvantur.

[ENGLISH]

## ¶3 · 142.13–142.13

> [p. 142] Primo ergo danda est posicio in quodam compendio.

[ENGLISH]

## ¶4 · 142.14–142.15

> [p. 142] 2°. declarende sunt radices ex quibus oritur discrepancia modernorum.

[ENGLISH]

## ¶5 · 142.16–142.16

> [p. 142] Et 3°. commixtim solventur instancie.

[ENGLISH]

## ¶6 · 142.17–143.8

> [p. 142] Stat itaque posicio in hoc—Quod humanitas assumpta a Verbo sit perfectus homo ex corpore et anima racionali compositus, et per ypostaticam unionem ydemptificatus Verbo in persona non natura—.Et sic non est aliud suppositum, individuum, ypostasis, vel persona in Christo ydemptice³ quam persona eterna Dominus Iesus Christus; [p. 143] cum tam corpus, quam anima, quam¹ eciam¹ humanitas completa sit persona eterna, quamvis sint inter² se nature solummodo temporales distincte plurimum ab invicem,³ et a divinitate⁴ a natura, et a substancia vel essencia divina. Et sic⁵ cavendum est specialiter de his tribus. Primo ne credatur aliquam illarum naturarum esse aliud suppositum a Verbo, quod est simul Filius Dei eternus et filius hominis temporalis.

[ENGLISH]

## ¶7 · 143.9–143.23

> [p. 143] 2°. oportet cavere ne credatur conversio⁶ vel confusio naturarum; cum manet plene natura divina⁷ cum duabus naturis incommunicantibus sed creatis constituentibus humanitatem perfectam, omnes⁸ et singule eadem persona in numero. Si autem esset conversio tunc natura conversa pro mensura conversionis⁹ non maneret; ut lignum conversum in ignem pro mensura conversionis desinit, nova forma inducta et veteri desinente; quod non potest esse de tribus formis incommunicantibus¹⁰ supra dictis. Si autem esset confusio naturarum, tunc forent reciproce quelibet eadem cuilibet, vel omnis vel aliqua incompleta, sicut est de elementis et¹¹ mixtis integraliter componentibus ipsum mixtum.¹² Modo autem manent tres incommunicantes nature, quelibet plene incommunicans cuilibet; sed utraque creatura per unionem personalem idem ypostatice Verbo Dei.

[ENGLISH]

## ¶8 · 143.24–144.24

> [p. 143] 3°. oportet cavere ne¹³ credatur ex humanitate et deitate fieri unum aggregative, ut est cumulus lapidum, vel accidens et subiectum. Nam unio ypostatica, que est ydemptitas¹⁴ personalis facit quod quelibet istarum trium incommunicancium naturarum est plene eadem communis persona; licet inter se naturaliter distinguantur per totum ex multis sanctorum testimoniis supradictis, ut Augustini, Gregorii, et Anselmi. Unde istam sentenciam colligit¹⁵ venerabilis Anselmus in De Incarnacione Verbi ca°. 7. sub his verbis: [p. 144] ‘Sicut, inquit, in Deo una natura est plures persone, et plures persone sunt una natura; sic in Christo una persona est plures nature, et plures nature sunt una persona. “Quemadmodum enim¹ Pater est Deus, Filius Deus et Spiritus sanctus Deus; et² non tamen tres dii, sed unus Deus;”² ita in Christo Deus est persona, et homo est persona, non tamen due persone sed una persona.’ Intelligit autem iste doctor per Deum et hominem deitatem et humanitatem, quia aliter esset similitudo impertinens, et verba sequencia nimis falsa. ‘Non, inquit, alius Deus alius homo in Christo, quamvis aliud sit Deus, aliud homo, sed idem ipse Deus qui et homo.’ Quando ergo dicit cum beato Augustino, Ieronimo, Gregorio et aliis quod aliud Deus in Christo et aliud homo, intelligit quod alia natura est deitas et alia humanitas, sed utraque non alia sed eadem persona; quia homo, ut dicit, solum naturam significat, et illum assumptum hominem dicit postea esse Iesum, et eandem personam cum Verbo. Unde non dubium quin per assumptum hominem intelligit naturam humanam assumptam. ‘Verbum, inquit, naturam aliam assumpsit, non aliam personam.’ Et ita generaliter intendunt sancti quando dicunt ‘aliud Deus, aliud homo; sed non alius,’ quod alia natura sit deitas et alia natura³ humanitas, non autem persona alia sed eadem.

[ENGLISH]

## ¶9 · 144.25–145.3

> [p. 144] Pro 2°.⁴ notandum quod in tribus radicibus stat modernorum variacio ab antiquis. Primo in hoc quod non concipiunt res communes. Noticia quidem⁵ universalium secundum Anselmum in De Incarnacione ca° 1°. est medium ad cognoscendum misterium Trinitatis, misterium incarnacionis, et multa alia fidei sacramenta. Sicut enim natura vel forma⁶ divina est communis ad tria supposita, sic omnis natura vel forma specifica universalis in actu est communis ad omnia eius singularia; et persona Verbi⁷ communis ad [p. 145] naturam divinam et alias duas contingenter extranee ypostatice copulatas: et tolluntur¹ hinc inde¹ sophistica argumenta conformiter.

[ENGLISH]

## ¶10 · 145.4–145.15

> [p. 145] 2ª radix est methaphisica de forma substanciali compositi. Quelibet enim talis forma substancialis compositi est eius² quiditas, idem essencialiter vel personaliter cum formato; ut quelibet anima animati, cum sit ipsum vivere et per consequens ipsum esse; et eius essencia, ex 2° De Anima, est idem essencialiter vel personaliter cum composito et subiecto; ut anima intellectiva hominis, que est eius humanitas, est eadem persona cum homine sic formato; igneitas est idem suppositum cum igne, et ita de ceteris: et per consequens, cum alique forme sint separabiles a materia que non accidentaliter³ sunt persone, patet⁴ quod personalitas manet cum forma a materia separata.

[ENGLISH]

## ¶11 · 145.16–146.16

> [p. 145] 3ª radix est abieccio predicacionis secundum essenciam, ut⁵ recte admittentes predicacionem secundum essenciam concedunt cum Anselmo De Incarnacione 7 quod quelibet universalis forma est idem cum omnibus et singulis eius suppositis, et correspondenter de aliis rebus communibus: concedunt eciam quod tam in creatore quam eciam⁶ in qualibet creatura omne esse est essencia et e contra, licet in omnibus istis sit formalis differencia vel distinccio racionis. Cum ergo moderniores variant in istis tribus radicibus, non mirum si variant in germine consequente. Ponunt enim quod non est possibile⁷ plures naturas vel res alias⁸ singulas esse unam. Ponunt 2° quod omnis forma substancialis compositi est distincta essencialiter a subiecto, in tantum quod aliqui dicunt omnem formam materialem substancie posse a natura separari. Et 3° dicunt⁹ quod in omni creatura est dare essenciam, que non est esse, sed eius causa, sicut lux luminis vel¹⁰ lucere. Ex istis dicunt consequenter [p. 146] quod non est possibile multas naturas esse personam Verbi. Dicunt eciam quod in quolibet homine esse suum et essencia et per consequens ipse homo ac sua humanitas distinguantur, sic quod omnis homo vel non est humanitas, vel humanitas solum est homo per accidens: unde Christus ut dicunt non suscepit hominem, sed humanitatem, que non potest esse idem ypostatice Verbo Dei. In istis ergo tribus radicibus et aliis ex eis consequentibus stat modernorum variacio ab antiquis. Magnam¹ quidem vim habent principia, cum eorum variacio dilatat distinccionem multiplicem posterius dicendorum. Oportet igitur supponere res communes: quod idem est forma substancialis cuiuslibet et formatum; ac demum, admittendo² predicacionem secundum essenciam, quod sicut in omni creato vel increato omne esse est essencia et e contra; sic omnis humanitas vel³ esse hominis est homo sive assumpta sive suppositacione propria terminata.

[ENGLISH]

## ¶12 · 146.17–146.24

> [p. 146] Quibus suppositis restat 3° tollere evidencias ex adverso. Videtur enim primo quod Verbum personam assumpsit, quia humanitatem assumpsit, que quidem humanitas est persona. Nec valet nude negare consequenciam, cum arguitur ordinate ab inferiori ad suum superius. Et talis deduccio a Deo approbatur quod conceditur exinde Verbum sumpsisse aliquid quod prius non fuerat. Et istam racionem Nestorianorum recitat Anselmus in De Incarnacione in principio ca° 7.

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 144: *in Christo* (print = bt) [SUB]
  - 144: *Iesum,* (print = bt) [SUB]
  - 144: *‘Verbum,* (print = bt) [SUB]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Augustine, Jeroine, o Gregory; (144.12).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 142:
1 ergo A B C.
2 secundam A B C; illam (an pro ullam?) O.
3 ẏdẽptıte O (an Christi ydemptitate legendum?).

p. 143:
1–1 quantum vel O.
2 in se O.
3 ab ı̂ A B C.
4 directe A B C.
5 sic *om.* O.
6 conversio *om.* A B C.
7 divina *om.* O.
8 omnis A B C.
9 conversacionis O.
10 formis communicantibus A; formis et communicantibus O.
11 in A B C.
12 mixtum *om.* C.
13 vel O.
14 unio B.
15 tollit O.

p. 144:
1 enim om. A B C.
2–2 et non . . . deus om. B.
3 natura om. sit add. O.
4 pro quo A B C.
5 quidem noticie O.
6 vel forma om A B C.
7 videtur A.

p. 145:
1–1 collinitur in O.
2 eius *om.* A B C.
3 accidenter O.
4 ᵽ (*i.e.* per) O.
5 nec O.
6 eciam *om.* A B C.
7 impossibile O.
8 aliquas A B C.
9 dicunt *om.* A B C.
10 et A B C.

p. 146:
1 Vaguani O.
2 dimitendo A B.
3 est A B C.
4 tamen O.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 142: \_Epilogat posicionem de humanitate; et, narrando tres radices causantes modernorum discrepancias, dissolvit tres obiectus eorum per ordinem. | Gives a summary of the aathor's position concerning the humanity of Christ. | Explains the three sources from which the modern divsrsities of opinion have arisen. | Deals with three principal objections to the author f s positio7i.~\ | assumed by the | word is perfect | man composed of .. . . .. . | body and a | and by hypol | staticunion iden- , , . , tified with the | Word in person, notinnature.
```

---

## Chunk 09-b: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-09-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-09-b
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "146.25–150.24"
divisions: "cap. 9 (heading 'Cap. IX.' at 142.0); part 2 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1055 words; 1050 confirmed by Fordham or the vote; 5 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n185–n189 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 9, part 2: [TITLE]

## ¶1 · 146.25–147.18

> [p. 146] Hic dicitur quod consequencia non valet, cum idem sit ac si sic argueretur—Verbum fecit se esse hominem, et esse hominem est esse personam: ergo Verbum fecit se esse personam—ubi constat quod antecedente existente necessario consequens est impossibile; cum tantum⁴ una persona, que absolute necessario est Verbum, poterit esse Verbum, et per consequens cum Verbum non potest se facere illam personam, patet quod Verbum non potest facere se personam. Sed pro ulteriori declaracione notandum quod assumere personale, de quo scriptura cum sanctis doctoribus in proposito loquitur, [p. 147] est duas naturas personaliter unire, id est,¹ duas naturas facere esse unum suppositum vel² personam, et ideo vocatur² unio personalis. Et potest secundum³ tres gradus active intelligi. Primo pro active principiare unionem huiusmodi: et sic tota Trinitas assumpsit naturam humanam de quanto univit⁴ eam ypostatice Verbo Dei. 2° striccius pro activa⁵ causancia principali unientis, ut ipsum fiat eadem persona cum natura unita; et sic natura divina univit vel assumpsit in supposito Verbi⁶ naturam hominis; quia fecit naturam hominis esse eandem personam non eandem naturam cum persona divina. 3° strictissime dicitur assumere personale pro causancia persone quia fecit⁷ naturam creatam⁸ esse idem personaliter sibi ipsi. Et illo modo solum Verbum assumpsit hominem. Ex istis patet, cum⁹ nulla assumpcio ypostatica sit eterna, quod oportet assumptum esse solummodo creaturam, quia nec alia persona, nec alia natura est Christi humanitas; licet sit creator, quia persona Verbi, que secundum deitatem non secundum ipsam creat omnia.

[ENGLISH]

## ¶2 · 147.19–148.2

> [p. 147] 2° patet, quod non potest esse personalis assumpcio nisi persona naturam assumpserit non personam.¹⁰ Oportet enim personam assumere, quia aliter non esset unio personalis, nisi persona ydemptificaret sibi naturam. Et quod oportet personam assumentem naturam assumere non personam, patet ex hoc quod personarum personalis¹¹ ydemptificacio vel naturarum essencialis ydemptificacio est impossibilis, ut nullum unum suppositum potest esse aliud, nec una natura fieri potest alia. Sed sicut persone maxime entitatis uniuntur in suprema essencia vel natura, sic nature maxime distantes ydemptificantur in eodem supposito vel persona. Et patet quod natura divina non potest primo sibi assumere naturam aliam vel personam. Patet ex hoc quod non potest esse alia natura vel persona quam est ab intrinseco necessario absolute, et nullius talis potest esse assumpcio. Oportet [p. 148] ergo naturam divinam unire¹ Verbo non nature primo quam sumpsit.²

[ENGLISH]

## ¶3 · 148.3–149.9

> [p. 148] 3° patet quod assumpcio ypostatica, unio, vel incarnacio, aut quomodocunque³ aliter nominetur,³ nec est generacio, nec conversio, nec alteracio, sed ydemptificacio; et si est mutacio, tunc est potissima mutacio dextere excelsi. Non enim est generacio, licet⁴ generacio⁴ ad ipsam consequatur:⁵ sicut motus localis ad motum augmentacionis, cum omnis generacio temporalis sit a non-esse ad esse produccio: assumpcio⁶ autem⁶ videtur esse subsistencie⁷ summe minoracio, cum Verbum ex incarnacione minoratum est paulo minus ab angelis, ut exponit Apostolus ad Hebre. 2° illud Psalmi 8ⁱ; ‘minuisti eum paulo minus ab angelis.’ Nec est conversio, cum subsistencia Verbi manet summa secundum omnes eius proprietates non composita⁸ cum aliquo. Nec est alteracio, tum quia humanitas assumpta non est inherens accidens; tum eciam quia persona secundum naturam precedentem humanitatem assumptam est omnino immobilis eo quod illi nature non potest accidens, ad quod est motus, formaliter inherere. Ex istis colligitur⁹ racio quare sequitur quod Verbum assumendo humanitatem assumpsit essenciam, substanciam, aliquid, et naturam; et non assumendo illam humanitatem assumpsit individuum, suppositum, vel personam. Nam¹⁰ illa¹⁰ humanitas est per se inferius ad aliquid, essenciam, vel naturam; cum sit per se quiditas singularis in specie humana; persona autem¹¹ cum sit extra racionem generis creati est solum accidentaliter superius ad substanciam, aliquid et¹² quodcunque genus creatum. Cum ergo persona Verbi sit equivoce Verbum respectu humanitatis, patet quod non sequitur, si Verbum illam humanitatem assumpsit, que non primo per [p. 149] se sed a Deo equivoce est persona, quod exinde assumpsit personam: ut in exemplo non sequitur—Petrus fecit se septipedalem, album, patrem,et sic de ceteris generibus accidencium: ergo Petrus fecit se esse aliquid—; quia est aliquid extra racionem quanti, vel qualis etc. Correspondenter Verbum esse personam est tanquam longe prius extra racionem humanitatis, sed esse aliquid est racio per se humanitatis; cum Christus, in quantum homo, est aliquid eciam quod prius non fuerat: ideo assumendo hominem assumpsit aliquid non personam.

[ENGLISH]

## ¶4 · 149.10–149.28

> [p. 149] Et si arguatur ex illo sequi quod Christus assumpsit personam hominis, sicut fecit se esse personam hominis: dicitur quod non hoc sed oppositum sequitur ex predictis; cum assumpcio non sit nisi nature per se possibilis, et, nulla¹ inherente accidente,¹ mutacio est assumpcio. Non enim quelibet faccio, sed solum faccio, qua natura racionalis fit Deus, est assumpcio vel ypostatica unio; et per conquens solum ydemptificacio est assumpcio.² Et patet quod sicut Christus fecit se esse hominem, animal, corpus, substanciam, et aliquid; sic assumpsit hec omnia in illa substancia singulari. Unde idem aliquid, quod fuit eternaliter est equivoce ad³ illud aliquid quod³ assumpsit. Ideo sicut albefactum sit⁴ ut sic⁴ coloratum et quale, licet perante fuerat coloratum, quia aliter non esset alteracio possibilis: sic in proposito per incarnacionem Christus fit aliquid licet prius fuit aliquid. Sicut enim sufficit ad alteratum, quod ipsum sit alterum secundum gradum quam prius; sic sufficit ad alietatem Christi quod aliquid aliud sit Christus quam prius fuerat.

[ENGLISH]

## ¶5 · 149.29–150.16

> [p. 149] Et patet quod non est assumpcio nisi substancie; et per consequens nullius forme inherentis est assumpcio: ut Christus non assumpsit ypostatice se pati, mori, vel ascendere, quamvis se fecit huiusmodi; quia tunc ydemptificasset passionem, mortem, et ascensionem ypostasi Verbi, sicut fecit [p. 150] humanitatem; quod est impossibile. Et sic quelibet nature racionalis accidentalis transmutacio esset assumpcio; quod repugnat supradictis. Persona ergo Verbi accidentaliter est persona hominis. Ergo sicut non assumpsit dominium¹ in mundi principio, nec filium hominis pro instanti incarnacionis; sic nec personam hominis, cum non assumpsit personam. Sed assumendo ‘formam servi’ fecit se esse personam hominis; licet nullam personam se fecerit, sed illam naturam, quam assumpsit, se fecerit:² cum sophisma illud non habet hic locum—Christus fecit se esse hominem, sed nullum hominem—; cum illam³ humanitatem, et per consequens hoc aliquid se fecit, quod prius non fuerat. Unde si correspondenter esset persona hominis, que tunc et non prius⁴ fuit Verbum Dei; tunc concedendum esset quod personam hominis assumpsit: sed assumptum est impossibile.

[ENGLISH]

## ¶6 · 150.17–150.24

> [p. 150] 2° principaliter obicitur per hoc quod videtur esse distinccio inter humanitatem, naturam, vel formam hominis et personam hominis; cum humanitatem, naturam, et formam hominis Verbum assumpsit,⁵ non personam: et hoc sufficit ad inferendum distinccionem. Oppositum tamen dicit posicio, cum dicit naturam assumptam esse personam Verbi; et sic non videtur quod Verbum hominem assumpsit,⁶ cum omnis homo sit persona, et nullam personam assumpserit.⁶

[ENGLISH]

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference Heb. ii. (148.12); reference Ps.Tiii. (148.13).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 146:
1 Vaguani O.
2 dimitendo A B.
3 est A B C.
4 tamen O.

p. 147:
1 id est *om.* O.
2_2 personam non vocatur B.
3 secundum *om.* O.
4 vîcit (*i.e.* vincit) O. *corr. alia manu in margine* univit.
5 causa *add.* O.
6 videtur C.
7 facit C.
8 creata O.
9 quod A B.
10 nec *add.* O.
11 personarum *iterum* O.

p. 148:
1 unisi (sic) A; uniri B.
2 sumpserit A; assumpsit B M; naturam quam sumpsit O.
3 quomodolibet alio nominetur A; quomodolibet nominetur B.
4-4 licet generacio om. O.
5 consequitur O.
6-6 assumpcio enim A B; assumptum autem O.
7 sbê (i.e. substancie) O.
8 componens A B C; compos ad extremum lineae, -ita in initio sequentis om. O.
9 tollitur A B C.
10-10 n̊lr̃ (i.e.) naturaliter O.
11 p̶sori (i.e. personari) B.
12 substanciam aut eciam quodcunque A B C.

p. 149:
1-1 natura inherente accidente A B; natura [?] ente accidente C; nulla inherente in accidente O.
2 est assumpcio om. O.
3-3 ab illo quod; in marg. corr. ob illud A; ab illo quod B; ab illud [al?]iquid quod C.
4-4 sit ut sit C; tit ut sic O; fit ut sic M.

p. 150:
1 doñ (i.e. donum) O.
2 fecerat A B C.
3 itaȝ (pro istam) O.
4 plus C.
5 assumpserit A B C.
6 assumpserat O.
7 quod O.
8 distinguitur A B C.
9 et om. A C O.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 147: sonai union. | unio personalis.
p. 149: ° h \ r \ n { orma in ~
p. 150: De Trinitate,
```
