# Translation brief: incarnacione 03-d–04-a

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/incarnacione/wyc-incarnacione-03-d.md chunks/incarnacione/wyc-incarnacione-03-e.md chunks/incarnacione/wyc-incarnacione-04-a.md` once and fix what it reports.
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
  neither → translate the print and flag it. Never smooth nonsense into sense. **Harris's printed text
  governs** (the standing rule of this edition): translate it unless it will not construe; a manuscript
  reading is chosen only then, and a single manuscript's reading never outweighs the print without
  cause; every departure gets a T note giving both readings. ⚠ Harris is a 19th-century editor of a
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

## Glossary (the 324 rows these chunks use; the full file is GLOSSARY.md)

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
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| possessionati | the possessioners | Endowed religious. |
| vulgares | the common people | The third estate. Not "the vulgar". Pilot. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | CONTEXTUAL: condition / respect | "Condition": a person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). "Respect": the logical relation under which a predicate holds (*posiciones secundum habitudinem*), with a **C** note; ruled 2026-10-22 (Wilson; *Incarn.* 4.16). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| quiditas | quiddity | Kept. Explain at first use per work ("what a thing is"). |
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
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
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| ingratitudo | ingratitude | Toward a person. Ruled 2026-10-02 (156.8). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |
| humanitas | the humanity | The nature the Word assumed, body and soul; with the article (*humanitas sit Christus*, "the humanity is Christ"). Not "the human nature", which is *natura humana*. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| incommunicans / incommunicantes (*nature*) | that do not communicate (with one another) | None predicated of, or shared with, another (Godhead, body, soul). Not "incommunicable": keep the participle. Ruled 2026-10-22 (Wilson; *Incarn.* 1.4). |
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
| approbati doctores | approved doctors | Kept apart from *probabiles doctores*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 13.3). |
| copulative (adv.) | conjunctively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 9.23). |
| ypostatice | hypostatically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 12.2). |
| Sermo (beside *Verbum*) | Speech | The divine title, capitalised; *Verbum* stays "the Word". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 16–17). |
| sophistice | sophistically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 15). |
| de vi vocis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| paralogismus | paralogism | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| nuncupative | nuncupatively | "By name only". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21). |
| nedum | not only | "Let alone" where the sense is a fortiori. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21, 24). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| gracia unionis | the grace of union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| exinanicio / exinanire / inanicio | emptying / empty | Phil. 2:7 (Douay "emptied himself"); *inanicio* (*Incarn.* 33) the same. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| minoracio | lowering | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| humanitus | humanly | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* passim). |
| suppositum | supposit | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 34.24). |
| individuum | individual | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 35.7). |
| in quantum (reduplicative) | insofar as | As *secundum quod*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37.9). |
| unio | union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 39). |
| synecdochica locucio | synecdochic locution | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 39.14). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| cautela | wile | Not "caution"; *cautela diaboli*, the devil's wile. Ruled 2026-09-28 (8 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| ingratus | displeasing (to God) | *Ingratus deo*: unpleasing to God. "Ungrateful" only where a person is ungrateful to someone. Ruled 2026-09-28 (5 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| calumpnia (ponere / capere) | challenge (to lay a challenge against / to be open to challenge) | The disputant's formal objection to a premiss. Ruled 2026-10-02 (*Eccl.* 16, 363.18, 363.24, 367.11). |
| collegiatus | collegiate | Ruled 2026-10-02 (*Eccl.* 16, 16-d/16-e). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| denominacio; denominare | naming; to name | The argument turns on it. Ruled 2026-10-02 (*Eccl.* 17, 391.17, 398.2). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| falsarius | falsifier | The opponent's epithet. Ruled 2026-10-02 (*Eccl.* 17, 414.6). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
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
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| incompossibilis | incompossible | Beside *compossibilis*. Ruled 2026-10-02 (*Eccl.* 22, 522.1). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| exequie | exequies | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| venia | forgiveness | Kept apart from *condonacio* "pardon". Ruled 2026-10-02 (*Eccl.* 23, 573.4). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| trahere in consequenciam | draw into a precedent | The legal idiom; *consequencia* stays "inference". Ruled 2026-10-07 (*Pot. pape* 94.13). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| quaternarius / denarius / quadragenarius | the four / the ten / the forty | Number exegesis (the 153 fishes, ch. 7). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 154–155). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| discrasia | distemper | Physicians' term. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 223.1). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| neutra | neutral things | Things neither commanded nor forbidden (obedience *in neutris*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.19). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| imperium (vicarium, autoritativum) | command (vicarial, authoritative) | The power to command (*par in parem non habet imperium*); "empire" only of the Empire. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 263.2). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| correptibilis | open to reproof | Beside *corripere* "reprove". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 301.3). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| calumpniator | challenger | Under *calumpnia* "challenge". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 323.10). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |
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
| cesaree (adv.) | in caesarean fashion | After *papa cesareus*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 403.25). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |
| nimis | exceedingly | Medieval intensive (= *valde*); "too much" only where excess is the point. Ruled 2026-10-12 (close-out R2; *Pot. pape* 169.2). |

---

## Chunk 03-d: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-03-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-03-d
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "40.16–44.26"
divisions: "cap. 3 (heading 'Cap. III.' at 28.0); part 4 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1146 words; 1143 confirmed by Fordham or the vote; 3 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n79–n83 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 3, part 4: [TITLE]

## ¶1 · 40.16–42.2

> [p. 40] Et si⁶ obiciatur,⁷ quod ista posicio, vocando ‘hominem’ corpus mortuum et animam separatam, sequitur sentenciam plebeiorum,⁸ et per consequens est erronea, ut multa alia dicta vulgaria; dicitur quod non est color in consequencia; cum dicta vulgaria a prima veritate communitati⁹ hominum inspirata non possunt in toto esse falsa. Unde Salvator Ioh. 12°. approbat turbe¹⁰ sentenciam, que dixit: ‘Nos audivimus ex lege quod Christus manet in eternum. Adhuc, inquit, modicum lumen in vobis est; ambulate dum lucem habetis, ut¹¹ non tenebre vos comprehendant; dum lucem habetis,¹¹ credite in lucem, ut filii lucis¹² sitis.’ Quasi diceret¹² iuxta exposicionem beati Augustini Ome. 52. ‘Verum est principium quod de Christo concipitis, scilicet quod ipse eternaliter manet humanitus cognoscendo. Sed oportet ultra procedere, quod non obest eundem hominem¹³ esse mortuum corporaliter et cum hoc mente vivere. Ambulate, inquit Augustinus, attendite et totum intelligite tam moriturum¹⁴ Christum quam [p. 41] victurum in eternum. Cum aliquid, inquit, verum habetis, non sitis comprehensi tenebris ignorancie¹ contempnendo mortuum et occisum² hinc trahentem ad se omnia, et sic offendatis in lapidem offensionis et petram scandali.’ Unde Ome. 78³ super istud⁴ Ioh. 14. ‘non turbetur cor vestrum:⁵ declarando Christum esse duplicem formam, scilicet humanitatem et deitatem, subdit de eius humanitate. ‘Non, inquit, homo Christus, non dixit⁶ ‘‘Filius Dei,’’ quod eciam sola caro eius in sepulcro meruit appellari?’ Probat. ‘Cum,⁷ inquit, credimus in Dei Filium qui sepultus est, profecto et Filium Dei dicimus carnem que sola sepulta est.’ Et post declarando quomodo ad verba est⁸ verum, ‘Pater⁸ maior me est,’ per hoc quod est duarum formarum utraque, ita subdit: ‘Quid ergo, heretice?⁹ cum Christus sit Deus et homo, loquitur ut homo; et tu calumpniaris Deo?¹⁰ Ille in se commendat naturam humanam; et tu in illo audes deformare divinam? Infidelis, ingrate,¹¹ nonne tu minuis eum qui te fecit, quia ille dicitur factus¹² sic¹² propter te? Equalis enim Patri est Filius per quem factus est homo; ut minor esset Patre, factus est homo; quod¹³ nisi fieret, quid esset homo?¹³ agnoscamus, inquit, geminam substanciam Christi: divinam¹⁴ scilicet, qua equalis est Patri; et humanam, qua minor est Patre. Utrumque autem simul; non duo, sed unus est Christus, ne sit quaternitas non Trinitas Deus.¹⁵ Sicut enim unus est homo, anima racionalis et caro, Christum, inquit, in omnibus istis et¹⁶ singulis confitemur. Probat hoc. Quis est ergo, per quem factus est mundus? Christus Iesus; sed in forma Dei. Quis est sub Poncio Pilato crucifixus? Iesus Christus; sed in forma servi. Item de singulis ex quibus¹⁷ homo constat. Quis non¹⁸ derelictus est in inferno? Christus [p. 42] Iesus; sed in anima sola. Quis resurrecturus in triduo iacuit in sepulcro? Christus Iesus; sed in carne sola.’

[ENGLISH]

## ¶2 · 42.3–42.15

> [p. 42] Hec sentencia huius sancti que, sicut non potest dissolvi, sic non cognosci, nisi viso quod Christus est trium naturarum incommunicancium quelibet. Qui ergo voluerit illam materiam¹ verissimam de virtute sermonis infringere, incipiat communicacionem persone² Christi multis naturis, non multis personis, ut deitas, improbare. Parcant igitur emuli huic vie quod naturali instinctu a vulgo sit cognita; quod a scriptura sacra et sanctis doctoribus sit tam assidue declarata; et quod mentes fidelium substrata sentencia non fallaci sed veridica excitat pro cura mortuorum, ut sepultura cum aliis exequiis devocius peragenda. Eadem enim persona hominis, que heri viva conversata est cum proximis, deportatur hodie mortua ad ecclesiam, et deponitur in sepulcro.

[ENGLISH]

## ¶3 · 42.16–42.27

> [p. 42] Nec oportet timere ampullosas³ instancias sophisticas quibus nituntur istam sentenciam impugnare dicendo, quod frivolum est credere racione corporum mortuorum vel personarum sanctarum in celo Deum facere miracula: cum, ut false garriunt, non est corpus sancti mortuum,⁴ nec sunt reliquie sanctorum, nec est possibile Petrum Iacobum vel Iohannem ante resurreccionem orare, sicut in letaniis⁵ canit illusa ecclesia per ignoranciam logice⁶ minus caute. Quicunque ergo sophista logicus⁷ vel naturalis vel methaphisicus vere voluerit ista defendere vel probare, si dicta factis compensat,⁸ est simul excellencior⁹ philosophus et objector¹⁰ quam Deus hucusque dignatus est sensibus mortalium propalare.⁹

[ENGLISH]

## ¶4 · 42.29–43.16

> [p. 42] Nec credo sophistam ad tantum desipere quod credat, si sola caro Christi fuit Christus in sepulcro et sola anima fuit Christus in inferno, quod¹¹ tunc sola caro vel sola anima fuit [p. 43] Christus. Ac si sic¹ argueretur solus Petrus est homo² in domo ista: ergo solus Petrus est homo² alicubi tenendo quidem diccionem exclusive, sicut facit Augustinus quando dicit³ quod nec sola caro nec sola anima fuit Christus, sed humanitas completa, que differt a parte qualitativa: patet decepcio sophistica introducta; et sicut dixi superius, quando Augustinus dicit quod pars qualitativa non est homo, exponit se ipsum quod non est completus homo, id est, natura composita⁴ ex corpore et anima: et sic intelligit 17⁵ de Trinitate ca. 7. exponens se ipsum quod intelligit ‘hominem’ ut veteres diffinierunt⁶ per ‘animal racionale mortale,’ vel iuxta descripcionem suam ‘substanciam racionalem constantem ex corpore et anima.’ Et⁷ per hoc distinguit inter triplicitatem naturarum in homine et trinitatem anime ac Trinitatem increatam. Affirmative itaque sue sunt concedende et negative modificande.

[ENGLISH]

## ¶5 · 43.17–44.6

> [p. 43] Ulterius si queratur, utrum verum sit in triduo quod hoc est corpus Christi et hec anima Christi pro nunc; dicitur⁸ quod sic: cum⁹ Christus vere sit tam corpus quam anima pro triduo, quo simul iacet mortuus et descendit vivus ad inferos, et sic persona viva est mortua secundum diversas naturas. Et movent me tria. Primo auctoritas scripture et exposicio beati Augustini superius recitata.¹⁰ Secundo quod aliter non esset concedendum quod Christus sit homo per illud triduum, quod nimis invaderet fidem meam. Et tercio quod doctores tam priores sapienciores quam moderniores capaciores¹¹ dicunt concorditer quod Christus nichil de humana natura dimisit quod¹² assumpsit, sed mansit per triduum unitus tam carni¹³ quam anime sicut ante. Cum igitur unione ypostatica, que non est per accidens unio ypostatica, fuerat antea copulatus;¹⁴ sequitur quod per illud triduum manet tam caro quam anima sicut prius. Unde [p. 44] dicunt loquentes nostri temporis concorditer quod sacerdos conficiens pro illo triduo conficeret dicendo verba sacramentalia corpus mortuum. Sed quomodo, queso, per verba falsissima¹ quibus diceret ‘hoc est corpus meum’ vere conficeret, nisi corpus confectum pro tunc fuerit corpus Christi?

[ENGLISH]

## ¶6 · 44.7–44.26

> [p. 44] Unde sanctus Thomas de Christo ca°. 50 videtur dicere² quod idem sit corpus Christi mortuum³ pro illo triduo quod⁴ fuit corpus Christi post et ante; et hoc racione unionis ad Verbum; licet quelibet pars quantitativa⁵ illius corporis racione forme substancialis substancialiter variatur. Teneo igitur⁶ primam partem huius sentencie et vario in 2ᵃ.; cum oportet formas substanciales esse subordinatas anime, ut patet ex dictis De Anima. Nec video quin, si ad omnem punctum corporis Christi generata sit nova forma⁷ substancialis preter quamcunque formam substancialem que infuit Christo vivo, foret aliud novum corpus mortuum secundum quamlibet eius partem quantitativam quam fuerat corpus vivum. Nec video 2°. quomodo illud esset tunc corpus Christi, nisi⁸ tunc Christus esset Christus, et⁸ esset illi novo⁹ corpori nova unione ypostatice copulatus.¹⁰ Nec video 3°. quomodo illud corpus sit mortuum, cum sit per totum noviter generatum, et nunquam antea fuit vivum. Dico ergo quod idem corpus in numero tam secundum materiam quam secundum¹¹ formam corporis, quod prius participative vixit, est in triduo corpus mortuum et cum hoc Christus Deus noster.

[ENGLISH]

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference John xii. 35. (40.21); reference Augustine explains thig . . ..... . , (41.1); reference 5 John xiv. l. (41.5); reference John xiv.28. (41.12); reference Augustinus (43.7).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 40:
1 que tunc *bis* O.
2 iecore A B C; ycore O.
3 7° A B C.
4 qui stat *add.* A B C
5 impleri A B C O.
6 si *om.* O.
7 obicitur A.
8 plebeorum A B C; plebiorum O.
9 communitate C; a primis veritate communicati hominem O.
10 turpe O.
11–11 etc. et A B C.
12 sitis lucis q. d. iuxta B; scitis O.
13 eundem hominem *bis* O.
14 mortuum O.
CHECK: the figure 11 appears twice in the main text and has a single combined entry "11–11"; the figure 12 appears twice in the main text and has a single entry.

p. 41:
1 et add. O.
2 ocasum C.
3 Unde act. 78 B.
4 istud om. O.
5 etc. add. A B.
6 dixit om. A B C.
7 probat tamen A B C.
8–8 est vero non pater C.
9 heretici O.
10 ut deo B.
11 infidelis vel ingrate A B; infideliter, Nonne C.
12–12 factus est homo ut minor esset patre sic O.
13–13 quod . . . homo om. B.
14 divinarum O.
15 deus om. O.
16 et om. O.
17 de singulis quibus O.
18 enim A B C.

p. 42:
1 sentenciam O.
2 persone *om.* A B C.
3 Nac . . . appullosas B; ampulosas O.
4 mortuorum A B C.
5 letariis B; lataniis C.
6 loyce C.
7 loytus C.
8 dictis facta compenset O.
9_9 excellencior vel abiectior philosophia (philosophus C) quam deus unquam hucusque sensibus mortalium voluit propalare A B C.
10 abicôr O. abiectior *non* abieccior A B C.
11 quod *om.* O.

p. 43:
1 sic om. C.
2–2 in domo . . . homo om. O.
3 dicitur O.
4 complesita O.
5 19 O.
6 definierunt O.
7 et om. C.
8 christi. Pronunc dicitur A B C.
9 quod B.
10 recita O.
11 capciosiores A B C.
12 quam C O.
13 corpori A B C.
14 perante copulata A B C; añtea copulatus O.

p. 44:
1 falsisima O.
2 dicere om. B.
3 quod add. C.
4 quam O.
5 quantitativa om. A B C.
6 itaque O.
7 formȝ O.
8–8 nisi christus tunc esset christo et A; nisi illud tunc esset christus et C.
9 novi B.
10 computatus O.
11 quam secundum om. O.
12–12 sit . . . mortuum om. O.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 44: De Anima:
```

---

## Chunk 03-e: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-03-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-03-e
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "44.27–48.33"
divisions: "cap. 3 (heading 'Cap. III.' at 28.0); part 5 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1165 words; 1165 confirmed by Fordham or the vote; 0 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n83–n87 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 3, part 5: [TITLE]

## ¶1 · 44.27–45.13

> [p. 44] Sed contra illud obicitur. Videtur primo quod corpus mortuum¹² sit corpus vivum; quia Christus, qui est corpus mortuum¹² in dicto triduo, est corpus vivum post et ante: et sic, cum corpus animatum et corpus inanimatum distinguuntur in specie, videtur quod illa non sunt idem corpus in numero, cum differencia specifica presupponit differenciam [p. 45] numeralem.¹ Hic dicitur quod corpus vivum et animatum est idem corpus in numero mortuum et inanimatum, licet non simul et semel; nec differt corpus in quantum² animatum specifice ab inanimato² corpore. Pro quo notandum quod dupliciter³ dicitur corpus animatum, scilicet, ab extrinseco participative, vel ab intrinseco qualitative⁴; ut corpus compositum ex corpore et anima est animatum anima, que est eius forma et quiditas, et illud non potest esse inanimatum: sed corpus, quod est altera pars qualitativa hominis, est animatum participacione anime; que, cum non sit forma eius intrinseca, potest abesse a corpore manente eodem in numero; sicut homines, qui participative dicuntur dii possunt manere iidem⁵ Deo absente ab eis per graciam.

[ENGLISH]

## ¶2 · 45.14–45.18

> [p. 45] 2°. obicitur sic. Si Christus in dicto triduo habet corpus et animam,⁶ tunc Christus est animatus; et per consequens tam corpus quam anima⁶ est pars⁷ Christi; et per consequens Christus in illo triduo componitur ex corpore et anima; et per consequens non iacet mortuus in sepulcro.

[ENGLISH]

## ¶3 · 45.19–46.5

> [p. 45] Hic dupliciter⁸ dicitur. Primo quod tam⁹ corpus quam anima⁹ eius¹⁰ est pars Christi, sed non in dicto triduo; quia non tunc qualitative componunt Christum, sed alias pro suo tempore. Unde posito quod essemus in dicto triduo, vere sciremus quod hec¹¹ anima que nunc est anima Christi, sed non nunc pars Christi, est pars Christi optima post et ante; et correspondenter de corpore. Ex quo patet quod hec non est synecdochica¹² locucio: ‘hoc corpus’ vel ‘hec anima est nunc Christus:’ sed, sicut homo est essencia substancia vel quiditas sua intransitive intelligendo, sic Christus est tunc hoc corpus et hec anima, que sunt sua ad¹³ sensum intransitivum, ut supra. Unde hec anima, licet non nunc animat corpus illud quod iacet mortuum, animat tamen Filium Dei; [p. 46] sicut caput¹ denominat hominem capitatum: et patet quod² animare est equivocum ad corpus subiectum vivificare et ad denominare personam cui copulatur ypostatice habentem³ animam, quam⁴ per se animat, cum ad invicem⁵ consequuntur⁶ vires inferiores sicut passio ad subiectum.

[ENGLISH]

## ¶4 · 46.6–46.16

> [p. 46] Secunda responsio dicit quod tam corpus quam anima Christi est in triduo vere pars Christi, sed nec qualitativa nec quantitativa, cum non tunc⁷ componuntur ad idem,⁷ sed est pars discretiva. Et sic intelligit Damascenus, quod Christus descendit totus ad inferos, sicut totus iacuit in sepulcro, sed non totum; quia persona fuit homo in utroque loco, sed non secundum ambas naturas; et sic in triduo habuit omnes partes⁸ quas habuit⁸ post resurreccionem, sed⁹ tunc defecit unio vel¹⁰ composicio. Sed nullum absolutum¹¹: nec pono vim in illa variacione, quia utraque sentencia est satis¹² catholica ad sensus equivocos.¹³

[ENGLISH]

## ¶5 · 46.17–46.25

> [p. 46] Sed 3°. obicitur ex hoc, quod Christus in illo triduo nec est homo immortalis nec homo¹⁴ mortalis; et omnis homo est mortalis vel immortalis: ergo Christus pro illo triduo non est homo. Maior patet eo quod Christus tunc passus est mortem: ergo iuxta Apostolum ‘mors illi ultra¹⁵ non dominabitur.’ Et quod non sit homo immortalis videtur ex hoc quod iacet mortuus in sepulcro et nondum consecutus est dotem¹⁶ immortalitatis, sed primo in resurreccione sequente iuxta communem doctorum sentenciam.¹⁷

[ENGLISH]

## ¶6 · 46.26–47.13

> [p. 46] Hic dicitur quod Christus pro hoc¹⁸ triduo est tam homo mortalis quam eciam¹⁹ homo immortalis. Est homo mortalis quia corpus, quod moritur et²⁰ iacet mortuum in sepulcro. Pro quo notandum quod mori, cum sit privari vita, vel potest intelligi ut dicit subitum actum privacionis vite a corpore, vel ut dicit absolute²¹ carenciam vite a corpore prius²² vivificato. [p. 47] Primo modo¹ est mors Christi subita non possibilis iterari licet Christus eternaliter potest mori. 2°. modo est² mors triduana, sicut corpus incorruptibile per triduum caret vita, sicut aer habet tenebram triduanam, et sicut pater semper gignit³ filium, sol semper producit lumen et medium per tempus privatur lumine, licet quodlibet istorum complete continue sit⁴ productum. Sic Christus ad sensum expositum⁵ continue moritur per istud triduum et habet simplam mortem triduanam, sicut dampnati habent mortem perpetuam. Est ergo Christus mortalis pro illo triduo cum moritur in effectu: non potest tamen nisi solummodo semel mori. Est eciam immortalis pro illo triduo⁶ quia est spiritus Iesus,⁷ qui nec potest mori corporaliter nec spiritualiter.

[ENGLISH]

## ¶7 · 47.14–48.2

> [p. 47] Et si obicitur quod hic predicatur oppositum de opposito; homo mortalis pro hoc instanti⁸ est homo immortalis; dicitur quod verum est. Ideo conclusio est impossibilis. Nec est color in isto paralogismo :—ergo homo mortalis est homo immortalis— iste homo Dominus Iesus est nunc homo mortalis, et iste idem homo est nunc homo immortalis;— Non enim sequitur, si persona que est commune ad ambas naturas illas est utraque illarum, quod ex hoc una sit reliqua; sicut non oportet, licet tantum sit unus Deus et ille sit copulative⁹ tam Deus genitus quam Deus ingenitus, quia tam Pater quam Filius, quod exinde Pater sit Filius vel Deus genitus sit Deus ingenitus, quod est idem. Nec sequitur, si Petrus sapiens et salvatus sit natura humana specifica, et Paulus insipiens et dampnatus sit eadem natura specifica, quod Petrus sapiens et salvatus sit Paulus insipiens¹⁰ et dampnatus. Et patet¹¹ ex simili modo¹¹ nutritis in rectis principiis. Sicut enim natura divina est trium personarum quelibet, et species humana personarum hominum quelibet; et tamen tantum est una natura divina sive [p. 48] species¹ humana:¹ sic persona Verbi Dei est trium naturarum quelibet et tamen una persona Verbi.

[ENGLISH]

## ¶8 · 48.3–48.28

> [p. 48] Quod autem Magister Distinctione 22 aliter loquitur cum modernis est propter equivocacionem, cum non admittit aliquid pro quacunque mensura esse hominem, nisi tunc componatur ex corpore et anima. Nos autem sequentes² scripturam non ficte sed philosophice³ dicimus quod eadem persona Petri vel cuiuscunque sancti prioris, que conversata est hic corporaliter in terris, manet iam beata in celis; et ubicunque est spiritus ille creatus sive in corpore sive extra corpus est idem homo in numero, et solum, ubi est corpus vel anima, est persona humanitus. Ut patet Ep. 40 ad Dardanum. Et cum certum sit quod Christus pro illo triduo non componitur qualitative⁴ ex corpore et anima, eo quod unio illorum dissolvitur; patet quod tunc nec est sic homo mortalis nec homo immortalis, quia non ad illum⁵ sensum tunc est homo. Si autem vocatur⁶ vere corpus et anima separata utrumque homo, sicut vocat Hugo de sancto Victore sequendo Augustinum, scripturas, et philosophicas raciones; tunc respondendum est sicut superius ad obiectus. Nam anima est per se homo et corpus nuncupative; et sic utrumque non duo homines, sed unus tantum. Si autem Magister intelligit hominem collective pro⁷ duabus naturis ad⁸ invicem et Verbo ypostatice copulatis, non est color quod tunc sit homo nisi utraque natura sit homo: et sic esset homo immortalis sicut anima fuit a sua⁹ origine immortalis; et per consequens partim mortalis, quia mortuus, et partim immortalis, quia anima. Hoc autem concedendum est de quolibet alio homine.

[ENGLISH]

## ¶9 · 48.29–48.33

> [p. 48] Mansit ergo Christus pro triduo minor patre quidquid fuit ante et sic suppositum humane speciei licet non tunc componebatur qualitative ex anima et corpore. Unde tunc complevit obedienciam Trinitati¹⁰ ministrando secundum naturam assumptam.

[ENGLISH]

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference Rom. vi. 9. (46.21).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 44:
1 falsisima O.
2 dicere om. B.
3 quod add. C.
4 quam O.
5 quantitativa om. A B C.
6 itaque O.
7 formȝ O.
8–8 nisi christus tunc esset christo et A; nisi illud tunc esset christus et C.
9 novi B.
10 computatus O.
11 quam secundum om. O.
12–12 sit . . . mortuum om. O.

p. 45:
1 materialem A B C.
2–2 inanimatum specifice ab animato A B; inamimatum specifice abianimato (*sic*) C.
3 dur O.
4 quiditative O.
5 idem A B C.
6–6 tunc Christus . . . quam anima *bis* A.
7 corpus O.
8 duplicitur A; communiter O.
9–9 anima quam corpus B.
10 eius *om.* A B C.
11 licet A B C.
12 sinodica A B C; synodogica O, cf. p. 39, n. 5.
13 ad *om.* O.

p. 46:
1 capud B C.
2 quomodo A B C.
3 habente B.
4 quomodo O.
5 inbicem C; mentem O.
6 consequitur A B C.
7–7 componunt ad invicem O.
8–8 sicut A B C.
9 et A B C.
10 seu A C; sive B.
11 abtū=absolutum A B C.
12 satis *om.* A B.
13 equivoces O.
14 homo *om.* O.
15 ultra *om.* A B.
16 dotem & mortalitatis O.
17 sentencias C.
18 per hec O.
19 quan et C.
20 et *om.* A B.
21 absolute *om.* O.
22 prius *om.* A B C.

p. 47:
1 modo om. C.
2 est om. A B.
3 gnignit O.
4 sit om. A B.
5 secundam exposicionem O.
6 pro illo triduo om. C O.
7 Iesu A B C.
8 per hoc instans A B C.
9 copulate C.
10 incipiens O.
11–11 similitudo A B C; ex silido O.

p. 48:
1_1 specifica humana C ; specifica *om.* humana O.
2 consequentes A B C.
3 sophistice B.
4 q̄le^te3[?] O.
5 ad id' =idem C ; illum *om.* O.
6 vocentur O.
7 per O.
8 ab O.
9 suo A B C.
10 trinitati *cum lacuna om.* C.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 44: De Anima:
```

---

## Chunk 04-a: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-04-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-04-a
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "49.0–53.27"
divisions: "cap. 4 (heading 'Cap. IV.' at 49.0); part 1 of 4, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1223 words; 1216 confirmed by Fordham or the vote; 6 runs stood by rule (both witnesses garbled); 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n88–n92 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 4, part 1: [TITLE]

## ¶1 · 49.0–49.0

<!-- the editor's bracketed argument at the chapter head: a Latin summary, then his own English
     summary in the same bracket (see the volume CARD for what is translated) -->

> [p. 49] [Iuxta ponit sentencias modernorum doctorum ut veritas plus lucescat. The opinions of Bonaventura, Duns Scotus, and St. Anselm, as to the nature of Christ during the three days’ entombment, examined.]

[ENGLISH]

## ¶2 · 49.1–49.3

> [p. 49] Sed ut magis appareat, quomodo communicacio ydiomatum pro triduo Christo conveniat, iuxta posite sunt sentencie modernorum.

[ENGLISH]

## ¶3 · 49.4–49.23

> [p. 49] Scribit enim Bonaventura super Distinccionem 12.¹ 3ⁱⁱ Sentenciarum, quod triplex² est predicacio, scilicet actualis, aptitudinalis,³ et mixtim. Actualis, quando subiectum est ens actu et forma predicati sibi inest; ut cum dicitur homine existente ‘homo est animal.’ Predicacio secundum puram aptitudinem est, quando nec subiectum nec forma predicati est in actu, sed necessaria⁴ est ordinacio unius ad alterum fundata super principia nature; sicut nulla rosa existente ‘rosa est flos.’ Quando subiectum autem est in actu, et forma predicati non inest sibi actualiter sed secundum necessariam ordinacionem fundatam super principia nature, tunc est predicacio mixtim, id est, partim actualis et partim aptitudinalis. Et sic concedit quod Christus fuit homo in triduo, quia subiectum, quod est Verbum Dei, tunc fuit in actu, et forma humanitatis servata fuit in aptitudine coniunccionis anime ad corpus. Nec vidi planiorem sentenciam alicuius doctoris in illa materia; quia indubie, quicunque concedit quod corpus et anima fuerunt partes Christi in triduo, habet concedere consequenter quod Christus habet correspondenter esse hominis ex eisdem.

[ENGLISH]

## ¶4 · 49.24–50.21

> [p. 49] Sed Doctor Subtilis dilatat⁵ ibidem⁶ amplius istam materiam. Dicit enim quod in triduo fuit ita; quod ‘Christus est Christus, et quod Verbum habet tam corpus quam animam [p. 50] sibi unitam, et tamen non tunc fuit ita quod Christus est homo; quia humanitas dicit ultra naturas imperfectas et ultra unionem respectivam unitatem¹ absolutam, sicut est in numeris. Et illa unitas non componit cum aliis; quia tunc esset² processus in infinitum. Et sic in triduo corruptum est aliquid absolutum, quia humanitas; sic quod nulla pars eius remanserat, cum sit³ forma totalitatis³ non habens partes quantitativas vel qualitativas. Racio autem quare non sequitur—Christus est Christus: ergo Christus est homo—est ista. Christus secundum Damascenum ca°. 49 est nomen ypostaticum⁴ duarum naturarum⁵ completarum singulatim,⁶ scilicet humanitatis et deitatis. Cum ergo oportet racionem subiecti talis esse in se veram, antequam aliquid de eo enuncietur; quia aliter esset hec vera—maius Deo⁷ est— quod est falsum,⁸ cum subiectum includit repugnanciam: patet quod hec—Christus est homo—⁹ formata pro triduo⁹ foret falsa; quia humanitas non tunc infuit Verbo Dei. Ideo, sicut,¹⁰ nullo homine existente, homo albus¹¹ est homo albus,¹² nec ex hoc sequitur quod homo sit homo albus¹²: sic pro triduo Christus est Christus; sicut Deus-homo est¹³ Deus-homo, et tamen Deus non est tunc homo.’

[ENGLISH]

## ¶5 · 50.22–51.5

> [p. 50] Ulterius quo ad denominacionem Verbi ab illis partibus ita scribit: ‘Verbum, inquit, quamvis in triduo habuit¹⁴ corpus et animam sibi unitam a quibus potuit denominari: non placuit tamen doctoribus quod denominetur ab eis, et forte non sine causa: cum partes non denominant, nisi ut subsistunt naturaliter in suo toto. Sed tunc defuit humanitas: ideo non denominavit eum carneum vel carnalem.¹⁵ Verumptamen si essent¹⁵ nomina imposita, posset denominari ab illis; sed¹⁶ oporteret quod essent denominativa, que non saperent vicium.¹⁷ Unde sicut substancia¹⁷ non sufficit denominari¹⁸ alba ab albedine,¹⁸ nisi mediante subiecto: sic [p. 51] nec Christus denominari carnalis, nisi mediante humanitate: ut, si Christus assumpsisset solum quantitatem, adhuc¹ non esset quantus propter defectum subiecti materialis.’ Hoc Latinum huius doctoris est michi² et forte aliis difficilius quam³ sentencia Augustini.³

[ENGLISH]

## ¶6 · 51.6–51.15

> [p. 51] Sed pro eius intellectu notandum quod ipse admisit predicacionem secundum habitudinem⁴ sicut Doctor alius.⁵ Et illud antiquitus est famosum,⁶ ut: ‘Quandocunque predicatur idem de se vel per se superius⁷ de suo per se⁸ inferiori⁹ est predicacio vera,⁹ licet neutrum extremum sit in actu. Ut verum est, dicit Doctor, quod—Cesar est homo—eciam nullo homine existente.’ Sed quando predicatur formaliter res alterius generis, tunc limitat ad predicacionem actualem; ut, ‘si homo est qualis,¹⁰ quantus, pater, agens, et cetera; tunc est actu.’

[ENGLISH]

## ¶7 · 51.16–51.26

> [p. 51] Et cum illo concordat Anselmus in De Concordia 5° ca°. ita dicens: ‘Quippe non idem est, rem esse preteritam, et, rem preteritam esse preteritam; aut,¹¹ rem esse presentem, et, rem presentem esse presentem; aut,¹¹ rem esse futuram, et, rem futuram esse futuram: sicut non est idem, rem esse albam, et, rem albam esse albam: lignum enim non¹² de necessitate semper est album, quia¹³ aliquando antequam fieret album, potuit non fieri album; et¹⁴ postquam fieret album,¹⁴ potest fieri non album: sed lignum album de necessitate semper est album, quia non potest¹⁵ fieri, ut album simul sit non album.’

[ENGLISH]

## ¶8 · 51.27–52.12

> [p. 51] Volunt ergo isti doctores quod necessaria sit predicacio aptitudinalis secundum esse possibile in causis secundis, quandocunque predicatur idem de se vel per se superius de suo per se inferiori. Nec ex hoc concluditur existencia talis rei. Nec contendo multum circa hanc logicam, cum nescio¹⁶ [p. 52] eam efficaciter impugnare. Sed considero quod si moderni dignarentur¹ attendere ad scripturas patrum priorum, non tantum mirarentur de hoc quod dico: Omne preteritum vel futurum esse pro suo tempore: quia ex illo dicto sequitur nedum omne preteritum vel futurum sed eciam omne possibile esse² pro semper. Et sic videtur quod infiniti homines, sicut quelibet signanda individua, sunt ubique; nam mille homines sunt mille homines, et sic infinitum,³ nullo homine existente. Nec videtur racio quare semper, quin⁴ per idem ubique et sic quilibet⁵ infinitum bonus foret infinitum bonus, et sic de quacunque denominacione possibili.

[ENGLISH]

## ¶9 · 52.13–52.27

> [p. 52] Sed dimittendo istud argumentum, ad propositum quod sequitur: Christum fuisse⁶ hominem in triduo. Nam Christus est per se in specie humana, ut patet posterius: ergo est per se homo: et per consequens, si est Christus, tunc est homo. Confirmatur. Sicut conceditur quod Christus est Christus, sic concedi debet quod iste homo est iste homo, demonstrando Iesum.⁷ Sed impossibile est istum hominem esse istum hominem, nisi iste homo sit⁸ homo. Ergo concesso quod Christus est Christus pro triduo, concedendum est ipsum esse hominem pro eodem. Unde dicit Doctor quod,†⁹ ‘si hec esset per se Christus est homo et sufficiens quod causet inherenciam predicati ad subiectum, sine hoc quod subiectum dicat compositum unum hoc Christus est homo fuisset semper vera. Sed magis, inquit, credo quod requiritur hoc et plus.’⁹†

[ENGLISH]

## ¶10 · 52.28–53.14

> [p. 52] Item sicut conceditur quod pro triduo ille homo est ille homo, ita concedi debet ut convertibile per se, quod ille [p. 53] homo componitur ex hoc corpore et hac anima. Ex quo plane sequitur quod ille homo sit homo, sicut ille homo est Deus-homo. Nam Christus et Deus-homo convertuntur¹ simpliciter et ex equo:¹ et per consequens, sicut conceditur quod Christus est Christus, sic concedi debet quod Deushomo est Deus-homo. Sicut ergo conceditur quod rosa est flos propter possibilitatem² licet nulla existat; sic evidencius videtur concedendum quod hec persona est homo, posito quod essemus in triduo cum sit nedum remota potencia, sed disposicio propinqua et necessaria, ut resurgat. Unde propter essenciam materialem perpetuam videtur Ieronimus³ in Ep. ad Paulam et Eustochium concedere quod Christus a principio seculi erat Christus: sed Doctor ille concedit ad sensum alium.

[ENGLISH]

## ¶11 · 53.15–53.27

> [p. 53] Item cum Christus secundum illum doctorem habet omnes partes⁴ quas habet post resurreccionem, non deficit ad hoc quod tunc⁵ sit homo nisi unio respectiva: sed nullum tale respectivum est de essencia substancie ut patet alibi De Continuacione: ergo corpus et anima unita Verbo pro triduo sufficiunt⁶ denominare ipsum esse hominem. Minor patet ex hoc: quod addita unione illa ad alia principia existencia⁷ pro illo triduo,⁷ foret consequens formaliter, quod Christus sit homo: ergo tunc non deficit⁸ nisi⁹ dicta unio; nec valet dicere quod humanitas deficit;⁸ quia humanitas est quod ipse est homo: ergo non est previe requisita¹⁰ ad hoc quod ipse sit homo, quia tunc idem esset previe requisitum ad se ipsum.

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 50: *ideo* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 49:
1 22 O.
2 duplex O.
3 habitudinalis codd. omn. Quae sequuntur lectionem in textu confirmant.
4 nata O.
5 dilitat O.
6 ibi B.

p. 50:
1 humanitatem A B C.
2 est C.
3_3 totalitas A B C.
4 ypostasis O.
5 coniunctaturum *add.* B.
6 significancium A B C.
7 de eo A B C.
8 factum O.
9_9 pro triduo formata A B C.
10 sicut *om.* O.
11 aʒ⁹ O.
12_12 nec . . . albus *om.* B.
13 est *om.* O; *sed in margine adnotatur* hô ê de⁹.
14 habet A B C.
15_15 verumptamen esset O.
16 si O.
17_17 *bis* O.
18 alba albedine C O.

p. 51:
1 ad hoc A B C.
2 michi *add. in margine* B.
3–3 quam ê aug⁹ sen^as O.
4 *An potius legendum* aptitudinem ? *cf. p.* 49 *passim.*
5 alius doctore A B C
6 famosus A B C.
7 vel *add.* A B C.
8 pe C.
9–9 est . . . vera *om.* A B C.
10 est equalis C.
11–11 rem . . . aut *om.* O.
12 non *in margine* C.
13 quoniam A B.
14–14 postquam est album A B C; postquam fieret est album O.
15 poterit O.
16 nequeo B.

p. 52:
1 dedignarentur O.
2 est O.
3 infinito O.
4 quando C.
5 cuilibet A (prima manu) B C; quelibet A (altera manu).
6 esse B.
7 îhς O.
8 iste add. A B.
9–9 Locus difficillimus et valde corruptus, ut crebrae rasurae et variae lectiones codicum indicant. Edidi supra lectionem codd. A B C; hic codicis O lectio subjungitur. Si hic esset per se Christus est homo et sufficiat quod causet inherenciam predicati ad subiectum cum hoc quod subiectum dicat conceptum unum hic Christus est homo fuisset semper vera sed magis inquit credo quod requiritur hoc et plus.

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
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 49: [Iuxtaponit sentencias modernorum doctorum ut veritas plus lucescat. The opinions of Bonaventnra, Duns Scotus, ancl Sf. Anselm, as to the nature of Christ during the three days 1 entombment, examined.~\
p. 52: Locus difficillimus et valde corruptus, ut crebrae rasurae et variae lectiones codicum indicant. Edidi supra lectionem codd.
```
