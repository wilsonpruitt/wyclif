# Translation brief: incarnacione 04-b–04-d

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/incarnacione/wyc-incarnacione-04-b.md chunks/incarnacione/wyc-incarnacione-04-c.md chunks/incarnacione/wyc-incarnacione-04-d.md` once and fix what it reports.
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
  summary) never outweighs it without cause. Every departure gets a T note giving both readings. ⚠ Harris is a 19th-century editor of a
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
  Hilary, the Lombard (*Sent.* III) and Grosseteste; the *moderni* are usually unnamed. ⚠ Thomas's "many men" (one person with several humanities; ch. 12) is the *Scriptum super Sent.* III d. 1 q. 2 a. 5, ⛔ not *ST* III q. 3 a. 7, which concludes "one man" (LEDGER Iprol-3). ⚠ Wyclif counts the Maximinus works as **three books** "contra Maximinianum": his book 1 = the *Collatio cum Maximino* (PL 42, 709–42), books 2–3 = *Contra Maximinum* I–II (his "book 3, c. 22" = II.22); his quotations from book 1 may be Maximinus speaking, not Augustine (LEDGER I01a-9, I02b-4, I02c-5).

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

## Glossary (the 301 rows these chunks use; the full file is GLOSSARY.md)

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
| viator | wayfarer | One still on the road, not yet in the homeland. Loserth: "a traveller on earth". Pilot. |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
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
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| thema | theme | The scripture text of a sermon. Ruled 2026-09-28 (2 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| habitudo | CONTEXTUAL: condition / respect | "Condition": a person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). "Respect": the logical relation under which a predicate holds (*posiciones secundum habitudinem*), with a **C** note; ruled 2026-10-22 (Wilson; *Incarn.* 4.16). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

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
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| respectus; respectivus | relation; relational | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| famosior | best-known [sense] | Pilot. |
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
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
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
| sacramentum (of the incarnation, of creation) | sacrament | The Augustinian sense, "mystery" (1 Tim. 3:16): G note at the first occurrence in the chunk. Kept apart from *misterium*. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.8). |
| moderni doctores / moderniores doctores | the modern doctors / the more modern doctors | Ockham and the *moderni*, usually unnamed. Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.1). |
| sancti | the saints | The fathers. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.15). |
| probabiles doctores | reputable doctors | *Probabilis*: worthy of credence (cf. *probabiliter*). Ruled 2026-10-22 (Wilson; *Incarn.* 7.1) as "approved doctors"; changed the same day (coordinator) to free "approved" for *approbati*. |
| copulative (adv.) | conjunctively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 9.23). |
| ypostatice | hypostatically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 12.2). |
| Sermo (beside *Verbum*) | Speech | The divine title, capitalised; *Verbum* stays "the Word". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 16–17). |
| sophistice | sophistically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 15). |
| de vi vocis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| nedum | not only | "Let alone" where the sense is a fortiori. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21, 24). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| gracia unionis | the grace of union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| minoracio | lowering | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| humanitus | humanly | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* passim). |
| spoliare / spoliacio | despoil / despoiling | Of hell. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 31–32). |
| suppositum | supposit | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 34.24). |
| individuum | individual | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 35.7). |
| in quantum (reduplicative) | insofar as | As *secundum quod*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37.9). |
| unio | union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 39). |
| synecdochica locucio | synecdochic locution | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 39.14). |
| universitas creaturarum | the totality of creatures | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37). |
| pars qualitativa | qualitative part | Body or soul as the parts that make up a man by kind; set against *pars quantitativa*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 43.5). |
| pars discretiva | discrete part | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 46.9). |
| intransitive | intransitively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 45.28). |
| in effectu | in actual fact | As against in potency or in name; ⛔ not "in effect" (modern "virtually"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 47.10). |
| animare | animate | The argument turns on it (45.30–46.4). Ruled 2026-10-22 (coordinator, delegated). |
| communicacio ydiomatum | communication of idioms | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.1). |
| predicacio actualis / aptitudinalis / habitudinalis / mixtim | actual / aptitudinal / habitudinal / mixed predication | *Habitudinalis* is its own term (the four MSS at 49.6), not under *habitudo*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.5–16). |
| denominativum | denominative | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 50.30). |
| Doctor Subtilis | the Subtle Doctor | Scotus. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.24). |
| convertibilis / converti | convertible / be convertible | Of terms. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 52.29). |
| previe requisitum | required beforehand | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 53.25). |
| forma totalitatis | form of totality | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 50.7). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |
| infirmitas (of Christ's flesh) | weakness | Ruled 2026-10-22 (Wilson; *Incarn.* 5.31–6.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| recencius | more freshly | Pilot (*Dial.* 2.10) |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| redempcio temporalium | redemption of the temporal goods | Chapters buying back seized goods. Ruled 2026-10-02 (*Eccl.* 15, 340.15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| ablatarius | the one from whom it is taken | Beside *ablacio* "taking-away". Ruled 2026-10-02 (*Eccl.* 15, 343.7). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| redempcio (of a sentence) | redemption | Buying off a penalty; kept apart from *redempcio temporalium*. C note at first use. Ruled 2026-10-02 (*Eccl.* 15, 352.1). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| denominacio; denominare | naming; to name | The argument turns on it. Ruled 2026-10-02 (*Eccl.* 17, 391.17, 398.2). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| casus calculatorii | calculatory cases | Ruled 2026-10-02 (*Eccl.* 23, 574.32). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| remissio; remittere | remission; to remit | Headword row (cf. *condonacio* "pardon", *venia* "forgiveness"). Ruled 2026-10-02 (*Eccl.* 23). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| trahere in consequenciam | draw into a precedent | The legal idiom; *consequencia* stays "inference". Ruled 2026-10-07 (*Pot. pape* 94.13). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| deliramenta | ravings | Ruled 2026-10-07 (*Pot. pape* 06-c). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| relacio racionis | relation of reason | Scholastic term (a relation in the mind only). Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 3.7). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| discrasia | distemper | Physicians' term. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 223.1). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
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
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| precellenter | pre-excellently | Adverb beside *precellencia* "pre-excellence". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 291.2). |
| correptibilis | open to reproof | Beside *corripere* "reprove". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 301.3). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| remisse (of assent) | with slackened [assent] | Opposed to full assent in the degrees of belief. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 328.18). |
| potissimus; pocior (Antichristus) | foremost; greater | Superlative and comparative kept visible as a pair. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.28, 331.12). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| involucrum | wrapping | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 357.9). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |
| ars cesarea | the caesarean art | After *papa cesareus*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| precellere | excel | Verb beside *precellencia* "pre-excellence"; not "pre-excel". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 399.28). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |
| nimis | exceedingly | Medieval intensive (= *valde*); "too much" only where excess is the point. Ruled 2026-10-12 (close-out R2; *Pot. pape* 169.2). |

---

## Chunk 04-b: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-04-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-04-b
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "53.28–57.6"
divisions: "cap. 4 (heading 'Cap. IV.' at 49.0); part 2 of 4, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "843 words; 840 confirmed by Fordham or the vote; 3 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n92–n96 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 4, part 2: [TITLE]

## ¶1 · 53.28–54.16

> [p. 53] Item vel est dicta unio causa humanitatis vel e contra; cum distinguuntur ut absolutum et respectivum, et non sunt impertinencia. Si humanitas sit causa dicte unionis tanquam¹¹ passionis que consequitur ad subiectum: tunc [p. 54] unio non requiritur ad humanitatem, et e contra pro¹ dicto triduo sunt omnes cause posite, que requiruntur ad humanitatem Christi;¹ et per consequens tunc est homo. Si e contra unio sit causa dicte humanitatis, hoc² videtur tripliciter esse falsum. Primo per³ hoc quod continuacio per idem foret causa corporis; quod improbatum est alibi. 2°. per hoc quod unio illa, cum dependeat ab extremis, non est essenciale principium hominis, eo quod posset manere idem homo variato corpore vel ablata eius parte quantitativa. Non ergo est illa unio causa beatitudinis, sciencie et aliorum⁴ accidencium⁴ hominis que insunt racione anime;. et multo minus est causa⁵ humanitatis, que est prior illis accidentibus. 3°. per hoc quod illa unio nedum dependet ab illis extremis absolute, sed ut copulantur qualitative ad invicem; et per consequens presupponit perfectum hominem: et sic non est previe requisita sed accessoria.

[ENGLISH]

## ¶2 · 54.17–54.24

> [p. 54] Tales multas evidencias feci alias cum testimoniis sanctorum, quod tota humanitas et personalitas servatur in anima; aliter enim nimis esset mundus peioratus per deperdicionem absolute humanitatis Christi succedente⁶ loco illius iocalis⁷ preciosissimi sola morte. Oportet ergo plenam perfeccionem humanitatis Christi servari⁸ in composito discretive ex corpore et anima, quod plus sic perficit mundum quam prius perficit qualitative compositum, sicut contingit de Sampsone.

[ENGLISH]

## ¶3 · 54.25–55.6

> [p. 54] Ulterius quoad denominacionem Verbi pro illo triduo ex corpore et anima resultantem, videtur responsio multum literalis, quando dicit quod' non placuit doctoribus ipsum denominari ab illis.' Nam semper⁹ Spiritui sancto auctori¹⁰ scripture placuit quod denominetur pro illo triduo' descendens ad inferos'¹¹ secundum animam, et' iacens in sepulcro' secundum corpus: et sic de sepultura et aliis ministeriis¹² ad sepulturam pertinentibus, ut condimento mixture mirre et aloes, involucione in sindone, posicione in monumento. [p. 55] Et racione anime denominatus est' rex spolians tartara,'¹ regens spiritualiter suum exercitum pacificando rebelles tam intraneos quam extraneos:² et sic de omnibus actibus regiminis, que ad regem spiritualem pertinent, longe efficacius quam antea fecit vivus³: tunc enim habuit exercitum plus unitum.

[ENGLISH]

## ¶4 · 55.7–55.16

> [p. 55] Item cum tam corpus Christi quam anima fuerunt secundum Doctorem tunc partes Christi, et nichil dicitur pars, nisi in comparacione ad aliquod totum: videtur quod fuit unum totum continuum vel discretum, cuius erant partes, ut dictum est superius: et illud discretum, cum non deficit in aliquo substanciali quod fuit in humanitate, quando affuit qualitativa composicio: videtur quod tunc,⁴ sicut mediante⁵ illo toto et unione sufficiunt partes ille⁶ denominari partes Christi, sic sufficiunt denominare Christum denominacionibus naturaliter⁷ consequentibus ex eodem.

[ENGLISH]

## ¶5 · 55.17–55.24

> [p. 55] Et quantum ad⁸ exemplum Doctoris de albedine dependente a subiecto ut causante et non substantivante⁹: patet quod ymaginacio¹⁰ est ficta ex falso principio, scilicet quod albedo potest primo¹¹ esse ad omnem¹² punctum subiecti sui informans;¹³ 2°. conservata¹³ ab eo sine hoc, quod informat; et 3°. nec informans nec conservata ab eodem. Albedo enim, cum sit subiectum esse album, non potest esse sine subiecto.

[ENGLISH]

## ¶6 · 55.25–56.12

> [p. 55] Item de hoc quod dicit Christum posse denominari ab illis partibus ut sic' Si essent nomina imposita;' miror de istis verbis tam realis philosophi et subtilis, cum constat¹⁴ quod denominacio rei extra est impertinens imposicioni¹⁵ nostrorum nominum, ut albedo eque denominaret¹⁶ simplum¹⁷ album, nullo signo artificiali hominum¹⁸ existente; sicut quotlibet talibus positis secundum varia ydiomata. Unde denominaciones, quas Augustinus, Hugo de Sancto Victore, [p. 56] et alii precedentes Magistrum Sentenciarum imposuerunt Verbo Dei secundum illas¹ partes pro illo triduo, scilicet quod est caro, quod est anima, et sic de ceteris, non sonuerunt in vicium. Nec valet dicere quod ille denominaciones sunt synecdochice²; quia, ut patet alibi, construccio synecdochica³ est, quando parti quantitative attribuitur primo denominacio accidentalis, et consequentur toti secundum illam partem ut ;—homo est⁴ albus faciem et sanus thoracem.⁵ Cum ergo nec corpus nec anima Christi sit pars eius quantitativa; sequitur quod hic non est construccio synecdochica—Christus⁶ est anima—sicut nec—Hic homo est tibia.

[ENGLISH]

## ¶7 · 56.13–57.6

> [p. 56] Item si pro dicto triduo corpus et anima sunt partes Christi, tunc denominant⁷ ipsum habere partes illas tanquam partes suas: quia constat quod non sequitur —Hec⁸⁹ res est mea et est pars; ergo est pars mea—quia quelibet pars creature esset pars Trinitatis increate; et, ut sophiste¹⁰ arguunt, homo¹¹ monstruose haberet multa capita asinina. Ideo concedit doctor¹² quod Christus potest vere denominari pro illo triduo habens partes illas ut partes suas, sed non carneus vel carnalis: ut si solum¹³ assumpsisset¹⁴ quantitatem, adhuc¹⁵ non¹⁶ esset quantus propter defectum subiecti materialis: sic licet habeat carneam partem suam, adhuc¹⁷ non est carneus, eo quod deest humanitas. Sed miror de ista similitudine propter tria. Primo cum impossibile sit quantitatem per se esse. 2°. cum hoc posito per impossibile Verbum esset quantum per ypostaticam unionem. Non enim est unio vel assumpcio personalis sine communicacione ydiomatum nature specifice assumpte¹⁸ Verbo vel persone assumenti: assumptum enim ypostatice oportet terminari suppositacione¹⁹ aliena et non esse suppositum proprie speciei, [p. 57] ut eciam¹ dicit doctor. 3°. videtur similitudo² impertinens; cum natura illa non dependet ab humanitate, cum manet naturaliter sine illa, et posset fuisse assumpta sine assumpcione humanitatis. Si enim Verbum posset pure assumere quantitatem, multo evidencius carnem mortuam per se de natura possibilem.

[ENGLISH]

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference Judges xvi. 30. (54.24).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 53:
1-1 ex equo simpliciter B; simpliciter et e contrario O.
2 possibilem O.
3 Ieronimum A B C.
4 personas B; ptes (sic) C.
5 tunc om. B.
6 faciunt A B C.
7-7 om. B.
8-8 nisi . . . deficit om. C.
9-9 nec O.
10 requisita codd. omn. sc. unio.
11 tanquam bis O.

p. 54:
1–1 pro . . . Christi *om.* A B C.
2 hoc *om.* O.
3 ex O.
4–4 rerum accedencium A B C.
5 sunt cause O.
6 sic sedente O.
7 vitalis A B C.
8 servare A B C.
9 semper *om.* A B C.
10 auctore C.
11 ad inferna B.
12 misteriis *pro* mȋsteriis O.

p. 55:
1 tarthara A B.
2 externos A B C.
3 vivus om. A B C; vn⁹ O.
4 tunc om. A B C.
5 mediate A B C.
6 ille om. A B C.
7 naturalibus A B C.
8 2ᵐ· add. O.
9 subiectante O M.
10 ymago O.
11 primo potest A B C.
12 hominem O.
13 2° conservatum O.
14 cum stat A B C.
15 imposicionem A B C.
16 denominari O.
17 ipsum A B C.
18 hominem O.

p. 56:
1 alias O.
2 sinodochice A B C; sýnodotice O; cf. p. 39, n. 5.
3 sinodochica A B C; synodotica O.
4 est sec. man. A; om. B.
5 serenus thoracem A B C; sanus secundum thoracem O.
6 sinodochica A B C; sýnodogica O; cf. n. 2 supra.
7 denominat A B C.
8 sequitur om. O.
9 hoc A B C.
10 sophistice A B C; soᵗᵉ O.
11 hoî O.
12 doctor om. C.
13 solus B.
14 sumpsisset A B C.
15 ad hoc C.
16 non om. O.
17 ad hoc C O.
18 assumpti O.
19 suppōne A B C.

p. 57:
1 eciam om. A B C.
2 illa add. C.
3 per C.
4-4 pedes et capud B.
5 quantitative om. B.
6 quantitative om. A B C.
7 componit O ut om..
8 magis B; mag° O.
9 sit om. C.
10 verissimilem O.
11 colton A; carton B; cantori C; cowtonus O.
12-12 sed . . . mortuus om. O.
13 et B.
14-14 et . . . mortuum om. O.
15 ampleatiō ï O.
16 est (sic) sit in marg. A.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 56: (nara avveKm m
```

---

## Chunk 04-c: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-04-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-04-c
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "57.7–61.20"
divisions: "cap. 4 (heading 'Cap. IV.' at 49.0); part 3 of 4, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1183 words; 1182 confirmed by Fordham or the vote; 1 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n96–n100 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 4, part 3: [TITLE]

## ¶1 · 57.7–58.12

> [p. 57] Item pari³ evidencia, qua Christus habet corpus mortuum tanquam partem suam pro illo triduo, habet quamlibet partem illius corporis partem suam, ut latus, caput,⁴ et pedes,⁴ sicut scriptura sacra patenter asserit. Sed concesso consequente, cum non possunt poni nisi partes quantitive Christi, cum sint partes quantitative corporis, sequitur quod sunt partes quantitative Christi. Et cum omnis pars quantitativa rei componit ut sic quantitative⁵ omne totum cuius est pars, sequitur quod dicte partes quantitative componunt Christum quantitative,⁶ et per consequens sic componunt,⁷ ut sit maius⁸ sua parte quantitativa. Sequitur quod Christus sit⁹ pro triduo mole magnus, ut puta septipedalis, in tumulo, cum ibi habeat partes extra partes: et cum nichil sit quantum nisi substancia materialis, sequitur quod Christus fuit pro dicto triduo substancia corporea; et per hoc est verisimile¹⁰ Doctorem debere concedere, cum dicit quod Christus potest denominari pro illo triduo homo mortuus a tota natura, cui discrete copulatur. Et abreviator suus Cowtonus¹¹ dicit quod fuit pro illo triduo homo mortuus¹² sed¹³ non homo. Sed videtur michi quod si quis est homo mortuus,¹² tunc est animal et corpus mortuum¹⁴ et sic corpus, quamvis enim mortuum¹⁴ per se circumlocutum cum verbo equivaleat verbo ampliativo. Ita¹⁵ quod non sequitur—ista bestia nunc est mortua; ergo illa nunc est—Tamen si ista bestia nunc sit¹⁶ bestia mortua, ista nunc est bestia, que moritur [p. 58] aut¹ moriebatur. Si ergo res sit mortua secundum partem quantitativam ut² manum aridam³ vivente residuo, quanto magis erit mortua per totum, si quelibet pars quantitativa sui sit mortua? Patet ergo quod si Christus unquam⁴ fuit mortuus,⁵ hoc fuit in triduo, et indubie tunc fuit persona mortua: et cum oportet dare⁶ naturam unitam, secundum quam passus est mortem, que natura subiectet mortem; patet quod tunc fuit corpus sibi unitum sicut subtiliter⁷ dicit Doctor. Non enim fuisset mortuus, si pro primo instanti non-actuacionis corporis post vitam Christi tam corpus quam anima adnichilata⁸ fuerunt; quia tunc omnis mors esset adnichilacio.⁸

[ENGLISH]

## ¶2 · 58.13–59.20

> [p. 58] Item omnis anima, in quantum huiusmodi,⁹ animat, ut patet 2° De Anima. Si ergo ille spiritus creatus fuit pro illo triduo anima Christi, tunc animavit; et, cum non animavit tunc corpus, relinquitur¹⁰ quod tunc animavit Christum¹¹; et per consequens ipse fuit tunc animatus ad sensum expositum. Et cum¹² non secundum naturam divinam pocius quam¹³ in mundi principio: ergo servata est unio nature create precedens animam, que non potest fingi nisi humanitas. Non enim sortiretur¹⁴ animacionem cum illo creato spiritu, nisi ypostatice uniretur; sicut habet denominacionem humanitatis propter ypostaticam unionem. Confirmatur. Si Christus uniretur ypostatice primo illi spiritui separato tunc esset aliquid quod prius non fuerat, cum fieret alicuius speciei in genere substancie, cum aliter non esset unio personalis. sed modo unitus est eadem unione qua tunc uniebatur¹⁵: ergo manet Christus illud pro triduo. Minor patet ex hoc, quod alterius racionis fuit unio, qua¹⁶ Christus uniebatur spiritui suo pro triduo, quam¹⁷ unio non ypostatica¹⁸ solum per graciam: eo quod aliter non denominaretur Christus tunc habere animam, descendere ad¹⁹ infernum, [p. 59] et ministrare Patri ut sibi subditus, pocius quam Spiritus Sanctus dicitur minor Patre secundum columbam; quod est contra Augustinum primo Contra Simplicianum. Sicut ergo Christus fuisset tunc spiritus create speciei, ita est modo propter consimilem unionem: et cum ille spiritus non esse¹ potest nisi humane speciei, quia tunc posset transire de specie ad speciem, et sic species solum per accidens sibi inexistens foret sibi non species: nam² corrupto omni corpore et servatis spiritibus illis, qui quondam erant anime, forent ipsi individua racionalis nature; quia per se denominati agere acciones personales; et per consequens individua speciei non alterius quam humane, ut olim fuerant: ergo relinquitur quod forent homines: haberent enim unam³ naturam communem, in qua convenirent pari evidencia qua⁴ alia supposita speciei, et talis communis natura, cum sit prima quiditas⁵ illorum individuorum, foret illis species specialissima. Et illud facit michi evidenciam quod humanitas servatur in anima; cum individuum non potest exuere formam specificam, et olim fuit in specie humana non solum indirecte,⁶ sed habuit propriam quiditatem.

[ENGLISH]

## ¶3 · 59.21–59.30

> [p. 59] Propter tales evidencias declinant moderniores loquentes⁷ superficialiter more⁷ legis ab istis principiis dicentes quod Christus non habuit in dicto triduo corpus vel animam; et sic nec fuit mortuus nec mortem passus, cum nulla fuit mors Christi; nec iacuit sepultus, nec descendit ad inferos; et per consequens, cum tunc non fuit unio ypostatica Christi ad naturam creatam, Christus non liberavit in persona propria patres de limbo, sicut nec Pater; cum tunc fuit secundum⁸ omnem naturam⁸ tunc habitam equalis⁹ Patri et non minister.

[ENGLISH]

## ¶4 · 59.31–60.21

> [p. 59] Nec intelligende sunt dicte¹⁰ locuciones¹⁰ synecdochice,¹¹ cum Christus tunc non habuit partem: et non est synecdochica¹² [p. 60] locucio tocius per partem nisi pro mensura pro qua¹ est pars propter inconsequencia,² que secuntur. Sed hos deliros a scriptura a fide et a sanctis doctoribus vocat Magister Sentenciarum Distinccione 21' hostes veritatis.' Nec inveni in scriptis³ alicuius doctoris probabilis istam⁴ sentenciam; sed fingunt eam recentissimi correctores. Unde doctor Bonaventura⁵ putat super Distinccione 21. 3ⁱⁱ Sentenciarum quod sit de substancia fidei credere quod tam corpus quam anima fuerunt in triduo partes Christi; et allegat⁶ ad hoc tam Augustinum quam Iohannem Damascenum dicentes⁷:' Anathema sit, qui dicit Verbum deposuisse quod semel assumpsit.' Unde consequenter declarando quod triplex⁸ est unio, scilicet accio agentis, passio uniti vel unitorum, et 3°. unitorum relacio, dicit quod eadem⁹ unione activa continue unitum est⁹ Verbum carni et anime sicut eadem tencione tenemus equum et frenum. Unde et sanctus Thomas super Dᵉ. 21 dicit quod deitas fuit coniuncta in dicto triduo tam corpori quam anime; non quod Verbum fuit tunc corpus vel anima, sed quod tunc fuit corpus Christi [corpus]¹⁰ et anima eius anima, et solum¹¹ talis fuit unio ypostatica post et ante.

[ENGLISH]

## ¶5 · 60.22–60.30

> [p. 60] Arguitur¹² autem de racione supposita fide catholica ad probandum propositum. Nam, supposito quod essemus in triduo, patet quod corpus Christi iacet in sepulcro et anima descendit ad inferos: nam hoc iacet in sepulcro et hoc est corpus Christi post et ante hoc triduum; ut patet ampliantibus presens tempus: ergo corpus Christi iacet in sepulcro. Et idem est argumentum de anima. Ex quo videtur quod¹³ dicte partes sunt partes Verbi in triduo, quia¹⁴ Verbum habet in triduo illas partes.

[ENGLISH]

## ¶6 · 60.31–61.20

> [p. 60] Sed quia non omnes conveniunt in illo principio, ideo [p. 61] arguitur 3° sic. Eo ipso quod persona manet¹ per tempus et² habet per idem tempus omnes³ subiectas partes³ sibi proprie servatas, que erunt postmodum⁴ partes⁵ sue, habet pro illo tempore partes illas: sed sic fuit de corpore et anima Christi pro dicto triduo: ergo tunc fuerunt⁶ partes sue. Maior patet eo quod aliter manus arida vel membrum mortuum non esset pars persone: quod est contra scripturam et communem modum loquendi. Imo, ut patet in De Anima, partes extreme⁷ longe cicius moriuntur ipso corde: et sic in⁸ media vita est dare aliquas partes mortuas mixtas cum vivis.⁹ Ad cuius conformitatem locuntur Morales, quod¹⁰ membrum corporis Christi mistici¹¹ per privacionem gracie mortuum, non exinde desinit esse membrum, cum tunc omnis¹² expers gracie foret ut sic¹³ infidelis. Et confirmacio illius est, quod tunc continuacio non est de essencia substancie materialis. Ex quo videtur quod manus abscisa ab homine supervivente remanet quodammodo manus sua. Et per idem, cum persona Filii Dei mansit per totum triduum habens a proprietate¹⁴ et specialiter idem corpus aliter quam alia, videtur quod¹⁵ tunc fuerat corpus suum.

[ENGLISH]

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference AugusSne68 band John of Damas- (60.10).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 57:
1 eciam om. A B C.
2 illa add. C.
3 per C.
4-4 pedes et capud B.
5 quantitative om. B.
6 quantitative om. A B C.
7 componit O ut om..
8 magis B; mag° O.
9 sit om. C.
10 verissimilem O.
11 colton A; carton B; cantori C; cowtonus O.
12-12 sed . . . mortuus om. O.
13 et B.
14-14 et . . . mortuum om. O.
15 ampleatiō ï O.
16 est (sic) sit in marg. A.

p. 58:
1 ac A B C.
2 aut *codd. omn.*
3 aridum O.
4 nunquam C.
5 per totum *add.* A C.
6 dari B.
7 subiecti O.
8 anichilata anichilacio A.
9 modi *om.* O C.
10 requiritur O.
11 Christum *om.* O.
12 cum *om.* O C.
13 quoniam A C.
14 sortitiretur O.
15 uniretur A B C.
16 quam C.
17 quoniam A.
18 ypostaica O.
19 in A B C.
CHECK: the main-text figure list has 8 twice, but the foot has only one entry for 8 ("anichilata anichilacio A."), so the second 8 has no separate entry.

p. 59:
1 esset O.
2 a *add.* O.
3 unam *om.* B.
4 quum B.
5 deitas B; quantitas C.
6 indircem A C.
7-7 superficienter nr̅e (nostre) O.
8-8 seme̅ m̃n̄ (*Qu.* semen et naturam ?) O.
9 essencialis C.
10 de vi locucionis A B; de e̅e̅ (esse) locucionis C.
11 synodochice A B C; sẏnodotica O; *cf. p.* 39, *n.* 5.
12 synodochica A B C; sẏnodotica O *ut saepissime.*

p. 60:
1 mensura que om. pro O.
2 inconveniencia O.
3 scripturis O.
4 illam scienciam A B C.
5 bonaventure O.
6 alligat O.
7 dicentes om. O.
8 z^x (duplex) B.
9 unione (acciva vix legitur in rasura) unitum A; unione anima quo unitum B; unione acc͡a 9° (activa conclusio) C.
10 corpus in codd. omnibus omissum restitui.
11 solam B.
12 aliter O.
13 cum O.
14 et quod A B C.

p. 61:
1 nmqȝ (Qu. pro nmhȝ = naturam habet ?) O.
2 ut A B C.
3_3 substancias O.
4 postmodo C.
5 parte O.
6 fuerant O.
7 extere O.
8 in om. O.
9 cum vivus C.
10 quia A B C.
11 mixti A B C; mistici (i.e. mystici) O.
12 omnis om. O.
13 sit O.
14 appropriate A B C.
15 quantum O.
16 loyce A B C ut fere semper.
17 solus A C.
18 sic add. B.
19_19 mortuus licet non sit homo ut conceditur de specie humana tunc filius dei est homo mortuus ergo O.
20 tenere om. O C.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 58: De Anima.
p. 60: in codd, omnibus omissum restitui.
p. 61: De Anima, | ut fere semper.
```

---

## Chunk 04-d: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-04-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-04-d
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "61.21–65.17"
divisions: "cap. 4 (heading 'Cap. IV.' at 49.0); part 4 of 4, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "993 words; 992 confirmed by Fordham or the vote; 0 runs stood by rule (both witnesses garbled); 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n100–n104 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 4, part 4: [TITLE]

## ¶1 · 61.21–62.11

> [p. 61] Item logice¹⁶ potest deduci illud, posito quod solum¹⁷ Christus¹⁸ sit¹⁹ mortuus de specie humana: tunc Filius Dei est mortuus, licet non sit homo ut conceditur¹⁹: ergo Filius Dei est persona mortua. Consequencia videtur tenere,²⁰ eo quod persona est superius ad hominem secundum tenentes istam sentenciam, et in talibus eodem distrahente addito conformiter utrobique tenet consequencia, ut: Si Petrus est homo mortuus, tunc est animal mortuum et corpus mortuum. Si ergo Christus sit persona mortua, cum non superest que persona nisi persona Verbi, sequitur quod sit persona Verbi [p. 62] mortua; et per consequens est persona Verbi, que moriebatnr; et sic persona Verbi est Christus. Si enim caput pedes et alia derelicta pro triduo sint partes hominis mortui, et solum Filius Dei sit homo mortuus; sequitur quod sunt¹ partes Filii Dei. Unde propter istam unionem ypostaticam Verbi ad² illud sanctum corpus sepultum in triduo dicit Doctor Solempnis 12° Quodlibeto: quod illud servatum est nedum incorruptum sed incorruptibile iuxta illud Psalmi 15' Non dabis sanctum tuum videre corrupcionem.' Nec video quomodo esset naturaliter inditum³ homini timere mortem, nisi poterit pati mortem. Non enim ordinat natura hominem timere eventum, qui⁴ non potest sibi accidere.

[ENGLISH]

## ¶2 · 62.12–63.4

> [p. 62] Item si anima Christi desiit esse anima Verbi Dei, cum tunc et ante scivit omnia, sequitur quod hoc scivit continue. Queritur⁵ utrum voluntarie⁶ reliquit corpus in morte vel non. Quod sic patet: quia fuit obediens usque ad mortem inclusive et post perpetuo. Nec illud debet verti in dubium⁷ cum scivit hoc esse de necessario Dei beneplacito ad exaltacionem sui et sui generis. Unde Augustinus Ome. 119.⁸' Quis, inquit, ita dormivit quando voluit sicut Christus?⁸ Oblatus est enim, quia voluit, ut dicitur Isᵉ. 52. Si volens⁹ fuerit ypostatice⁹ separata, cum ex hoc perdidit graciam unionis; sequitur quod sic volendo peccavit, quia voluntarie defecit a gracia; quod nephas¹⁰ est dicere. Et consequencia videtur ex hoc¹⁰: quod anima propior¹¹ est Deo, cum est anima Dei, quam foret ab eo ypostatice separata: quia aliter esset possibile Deo¹³ plus vel tantum diligere ipsam animam alterius sicut suam: quod non puto. Cum ergo anima Iesu gratis elongavit se a Verbo postquam fuit sibi carior ypostatice copulata: sequitur quod de tanto graciam perdidit et per consequens sic peccavit. Nam nulli dubium, quin maxima gracia possibilis creature est quod sit pars qualitativa [p. 63] vel humanitas Dei sui. Si enim magna gracia est quod Deus velit¹ adoptare hominem in filium et heredem, longe maior est quod velit creaturam eternaliter predestinare in suam propriam animam vel humanitatem.

[ENGLISH]

## ¶3 · 63.5–64.15

> [p. 63] Item iuxta sepe dicta et diffusius declarata impossibile est aliquam substanciam esse² materiam vel³ formam vel ex eis compositam, nisi sit singularis essencia vel persona per se supposita speciei: sed tam corpus Christi quam eius anima fuit pro illo⁴ triduo individua substancia: igitur⁵ fuit essencia vel persona per se supposita speciei: et cum nullum suppositum potest manere aliud⁶ suppositum, sequitur quod utraque illarum naturarum manet idem suppositum quod fuit,⁷ anima et corpore, copulatum:⁷ sed⁸ tunc fuit suppositum hominis,⁸ cum cuiuslibet hominis personalitas sit supposicio utriusque partis qualitative: igitur⁵ utraque natura manet adhuc idem⁹ suppositum hominis, et per consequens eadem persona Verbi. Et illa racio foret evidens cuicumque cui assumptum principium est famosum: ‘Unde quia de virtute sermonis’: sequitur ex hoc principio cum veritate fidei quod tam corpus Christi quam eius anima quantumlibet a se invicem¹⁰ separata sint, utrumque¹¹ eadem persona hominis, que fuerant,¹² copulata. Ideo concedendum est quod pro triduo ypostatice sint unita et patet quomodo Verbum non potest assumere corpus mortuum, nisi mediante assumcione anime naturaliter precedente. Nec alteram illarum naturarum potest assumere,¹³ nisi faciat se esse¹⁴ illam naturam, cum nulla tali distinguit¹⁵ essencialiter vel specialiter suppositacio a natura. Et patet 3°. quod Verbum non posset assumere corpus et animam separata, nisi faceret se esse¹⁴ eandem personam que fuerunt tam corpus [p. 64] quam anima copulata. Ideo non sollicitor quid sequeretur,¹ si Verbum assumeret unione² ypostatica tam corpus quam animam proditoris et dimitteret ipsa³ suppositacioni proprie in finali resurreccione. Nam certum videtur michi⁴ quod peccatum inde foret penitus deletum, eo quod ypostatica assumcio esset⁵ efficacius medium ad tergendum peccatum quam lavacrum baptismale: sed istud delet omne peccatum suppositi vel nature: ergo multo magis personalis assumcio. Et ex alio latere puto me esse securum quod peccatum finalis impenitencie⁶ subiectatum in anima proditoris⁷ non potest deleri, vel⁸ post eius incorrupcionem⁸ redire. Ideo non superest nisi fugere tales casus. Nec est negandum, quin illud corpus mortuum⁹ sit suppositum, sicut et spiritus; cum utrumque¹⁰ habet supposibilem operacionem secundum idem suppositum;⁹ quia persona Filii est utrumque.¹⁰

[ENGLISH]

## ¶4 · 64.16–65.17

> [p. 64] Et si obiciatur quod pie aures abhorrent quod Deus universitatis¹¹ sit corpus vel cadaver mortuum; dicitur quod Deus non est cadaver, cum non sit mortuum corpus et putidum¹² sed ad sensum proprium incorruptum. Quamvis enim laceratum sit lancea et flagellis causantibus solucionem¹³ continuitatis, non tamen crura eius fracta per milites, nec carnes eius canibus¹⁴ aut avibus¹⁴ laniate; quia Exod. 12 mistice est preceptum; ‘os non comminuetis ex eo.’ Nec horreret, sed accenderet pias mentes¹⁵ quod Dominus celi et terre, qui¹⁶ dignatus est nasci parvulus, vagiens in cunabulis,¹⁷ ac reponi coram bestiis in presepe, dignatus¹⁸ est idem et non alius iacere mortuus in sepulcro. Sed quia putrefaccio et incineracio corporis mortui non profuisset suo generi, cum corpus mortuum non mereretur¹⁹ sibi vel aliis: ideo inconsonum et superfluum fuisset quod dictas infirmitates [p. 65] post completam victoriam assumpsisset. Nec auderem¹ dicere quod corpus mortuum foret Deus, nisi scriptura sacra tam patenter illud assereret, Ioh. 19: nec crederem² capiti meo de exposicione sensus litteralis eius scripture, nisi Augustinus, Hugo de Sancto Victore, et ceteri superiores doctores illud patenter assererent: nec diligerem Verbum Dei pro tunc ut Deum meum, nisi pro tunc esset spiritus descendens ad inferos et cum hoc natura divina gubernans omnia.³ Nec video quomodo posset sumpsisse naturam⁴ porci, serpentis,⁴ vel alterius creature quam hominis, ut patet posterius. Nam si aliquid potuisset⁵ esse monstrum, potissime fuisset⁶ chimera vel tragelaphus habens caput asininum, caudam equinam, pectus leoninum.⁷ Et sic⁸ esset veracissime⁸ de Iesu nostro in casu, quo omnem naturam aliam⁹ assumeret et post assumpcionem continuaret. Vacuum ergo¹⁰ et periculosum est raciones tales asserere.

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 62: *moriebatnr;* (plate: print = moriebatnr (turned u; misprint for moriebatur); kept as printed (Opus coordinator)) [AGREE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Ps. xvi. n. (62.8); reference Exod. xii. 46. (64.23); reference 5 Augustinus, (65.5).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 61:
1 nmqȝ (Qu. pro nmhȝ = naturam habet ?) O.
2 ut A B C.
3_3 substancias O.
4 postmodo C.
5 parte O.
6 fuerant O.
7 extere O.
8 in om. O.
9 cum vivus C.
10 quia A B C.
11 mixti A B C; mistici (i.e. mystici) O.
12 omnis om. O.
13 sit O.
14 appropriate A B C.
15 quantum O.
16 loyce A B C ut fere semper.
17 solus A C.
18 sic add. B.
19_19 mortuus licet non sit homo ut conceditur de specie humana tunc filius dei est homo mortuus ergo O.
20 tenere om. O C.

p. 62:
1 sunt *om.* C.
2 ubi *add.* B.
3 ruditum B.
4 que C.
5 ergo *add.* O.
6 volupta^e O.
7 indubie B.
8–8 quod inquit ideo (cita C) dormivit quando voluit sicud (sic B) Christus AB C.
9–9 ypostatice fuerat B.
10–10 est . . . hoc *om.* B.
11 prior B O.
12 deum O.
CHECK: the foot has an entry 12 (deum O.), but 12 is not in the list of figures in the main text; the main text figure 13 (after "Deo") has no entry at the foot.
CHECK (coordinator): text figure(s) 13 have no entry read here; entry figure(s) 12 have no figure in the transcription: read the plate foot before citing.

p. 63:
1 vult A C.
2 esse om. C.
3 sive A B C.
4 illo om. A B C.
5 ergo O.
6 illud B.
7–7 anima in corpore copulantis O.
8–8 sed . . . hominis suppletum in marg. A.
9 adhuc om. O.
10 inbicio C.
11 utraque C.
12 fuerat O.
13 assumpnere B.
14–14 illam . . . esse om. A B C.
15 An distinguitur legendum?

p. 64:
1 sequitur A B C.
2 unionem O.
3 ipsam A B C.
4 michi, om. B.
5 est O.
6 impunie A B C.
7 prodicoris A.
8–8 vel post eius corrupcionem A B C; post eius om.
9–9 sit suppositum . . . suppositum om. A B C.
10 utraque O.
11 pietatis add. A B C.
12 putridum A B C.
13 sollucionem A B.
14–14 aut avibus om. A B C.
15 aures B.
16 qui om. A B C.
17 cunibulis O.
18 quia add. A B C.
19 non om. A B C; meretur O.

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
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 61: De Anima, | ut fere semper.
p. 65: [_Supponendo quod Verbum non dimisit humanitatem pro triduo, probat quod nec potuit dimittere naturam quam assumpsit. Assuming as already proved that the Word did not as a matter of fact in the three days lay aside the human nature which he had taken up; it is here proved to be impossible that he should so lay it aside.~\
```
