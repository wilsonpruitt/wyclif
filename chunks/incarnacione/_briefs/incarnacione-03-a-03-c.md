# Translation brief: incarnacione 03-a–03-c

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/incarnacione/wyc-incarnacione-03-a.md chunks/incarnacione/wyc-incarnacione-03-b.md chunks/incarnacione/wyc-incarnacione-03-c.md` once and fix what it reports.
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
  Hilary, the Lombard (*Sent.* III) and Grosseteste; the *moderni* are usually unnamed.

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

## Glossary (the 293 rows these chunks use; the full file is GLOSSARY.md)

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
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| regnum | kingdom | Every sense: the political state as well as the kingdom of God and scripture's kingdoms. Not "realm". Wilson, Ruled 2026-09-28 (27 sites). |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| censura | censure | Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| habitudo | CONTEXTUAL: condition / respect | "Condition": a person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). "Respect": the logical relation under which a predicate holds (*posiciones secundum habitudinem*), with a **C** note; ruled 2026-10-22 (Wilson; *Incarn.* 4.16). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| locus a maiori | the topic from the greater | The dialectical topic; for *a simili* see "the topic from likeness" (2026-09-28 row). Ruled 2026-10-02 (*Eccl.* 144.27). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| insolubilia | insolubles | The logicians' paradoxes of self-reference. Ruled 2026-10-02 (*Eccl.* 175.11). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
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
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| dyameter / costa | diameter / side | The geometers' terms (the square's incommensurable diagonal). Ruled 2026-10-02 (97.21 ff.). |
| dulia / latria | dulia / latria | Kept as the theologians' terms, glossed once per chunk. Ruled 2026-10-02 (95.17). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| subintelligere | understand as implied | Recurs through *Eccl.* 12. Ruled 2026-10-02. |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |
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
| verificari (de) | be true (of) | The logicians' sense; not "verified" (modern "checked"). Ruled 2026-10-22 (Wilson; *Incarn.* 7.6). |
| sacramentum (of the incarnation, of creation) | sacrament | The Augustinian sense, "mystery" (1 Tim. 3:16): G note at the first occurrence in the chunk. Kept apart from *misterium*. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.8). |
| moderni doctores / moderniores doctores | the modern doctors / the more modern doctors | Ockham and the *moderni*, usually unnamed. Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.1). |
| sancti | the saints | The fathers. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.15). |
| probabiles doctores | reputable doctors | *Probabilis*: worthy of credence (cf. *probabiliter*). Ruled 2026-10-22 (Wilson; *Incarn.* 7.1) as "approved doctors"; changed the same day (coordinator) to free "approved" for *approbati*. |
| approbati doctores | approved doctors | Kept apart from *probabiles doctores*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 13.3). |
| copulative (adv.) | conjunctively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 9.23). |
| ypostatice | hypostatically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 12.2). |
| Sermo (beside *Verbum*) | Speech | The divine title, capitalised; *Verbum* stays "the Word". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 16–17). |
| de vi vocis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| nedum | not only | "Let alone" where the sense is a fortiori. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21, 24). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| gracia unionis | the grace of union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| exinanicio / exinanire | emptying / empty | Phil. 2:7 (Douay "emptied himself"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| humiliacio | humbling | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26–28). |
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
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| carecter, caracter (sensibilis) | (perceptible) character | "reputation". The mark of orders. Ruled 2026-09-28 (*Dial.* 5.7). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
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
| ablatarius | the one from whom it is taken | Beside *ablacio* "taking-away". Ruled 2026-10-02 (*Eccl.* 15, 343.7). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| redempcio (of a sentence) | redemption | Buying off a penalty; kept apart from *redempcio temporalium*. C note at first use. Ruled 2026-10-02 (*Eccl.* 15, 352.1). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| denominacio; denominare | naming; to name | The argument turns on it. Ruled 2026-10-02 (*Eccl.* 17, 391.17, 398.2). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| precaria | precarial grant | Wyclif defines it (*Eccl.* 453.21). Ruled 2026-10-02 (*Eccl.* 19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| locus evidencie | topic of evidence | *locus* = dialectical topic (cf. *locus a maiori*); not "place". Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| preconium | commendation | Ruled 2026-10-02 (*Eccl.* 20, 488.20). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| dampnacio | CONTEXTUAL: damnation / condemnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). Of a judgement passed on a teaching (*dampnacio istius sentencie tamquam heretice*, *Pot. pape* 84.10) "condemnation"; ruled 2026-10-07. |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| caracter in actu | character in act | Ruled 2026-10-02 (*Eccl.* 21, 513.18). |
| univoce | univocally | Ruled 2026-10-02 (*Eccl.* 21, 514.4). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| obsequium (for the dead) | duty | Kept apart from *servicium* "service", *officium* "office". Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| remissio; remittere | remission; to remit | Headword row (cf. *condonacio* "pardon", *venia* "forgiveness"). Ruled 2026-10-02 (*Eccl.* 23). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| trahere in consequenciam | draw into a precedent | The legal idiom; *consequencia* stays "inference". Ruled 2026-10-07 (*Pot. pape* 94.13). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| preco (Dei) | herald (of God) | Ruled 2026-10-07 (*Pot. pape* 06-b, 06-d). |
| deliramenta | ravings | Ruled 2026-10-07 (*Pot. pape* 06-c). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| sessiva | seisin | So the manuscripts (Loserth 170.8, *ita cod.*); feudal possession that perfects a title. Ruled 2026-10-08 (coordinator, delegated). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| locus a simili | the topic from likeness | Dialectical topic. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 240.10). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| imperium (vicarium, autoritativum) | command (vicarial, authoritative) | The power to command (*par in parem non habet imperium*); "empire" only of the Empire. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 263.2). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| correptibilis | open to reproof | Beside *corripere* "reprove". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 301.3). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| remisse (of assent) | with slackened [assent] | Opposed to full assent in the degrees of belief. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 328.18). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| evangelizans | preacher of the gospel | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-g). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |
| ars cesarea | the caesarean art | After *papa cesareus*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| insolubiliter | inextricably | Kept apart from *insolubilia* "insolubles". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 404). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |

---

## Chunk 03-a: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-03-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-03-a
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "28.0–32.23"
divisions: "cap. 3 (heading 'Cap. III.' at 28.0); part 1 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1143 words; 1140 confirmed by Fordham or the vote; 2 runs stood by rule (both witnesses garbled); 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n67–n71 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 3, part 1: [TITLE]

## ¶1 · 28.0–28.0

<!-- the editor's bracketed argument at the chapter head: a Latin summary, then his own English
     summary in the same bracket (see the volume CARD for what is translated) -->

> [p. 28] [Ostendit quod Christus fuit homo in triduo, et obicit multipliciter et dissolvit. Christ’s humanity was not suspended during the three days’ entombment.]

[ENGLISH]

## ¶2 · 28.17–29.6

> [p. 28] Ex⁸ istis plane consequitur quod Christus fuit verus homo in triduo inter eius mortem et resurreccionem. Probatur sic. Cuiuslibet⁹ hominis tam corpus quam anima est inseparabiliter idem homo: sed tam corpus Christi quam eius anima per dictum triduum manet: ergo Christus fuit per dictum triduum verus homo. Maior patet ex dictis. Nam quomodocunque scriptura vel alii doctores catholici hoc intellexerunt sive figurative sive aliter, suppono me intelligere; sic tamen quod maneat verum de virtute¹⁰ sermonis: et sic oportet me concedere aliqua¹¹ que secuntur. Nam licet illud argumentum det michi plenam fidem ad conclusionem propositam, verumtamen pro intellectu scripture et veritatum annexarum huic [p. 29] materie cum dictis doctorum oportet illam materiam ulterius triplici medio¹ dilatare. Veritas¹² enim testatur omnimode sibi ipsi, nec aliquid ex veritate consequens offenderet pias aures. Quicquid ergo ex hoc principio perfectus² philosophus sciret deducere concedi debet tanquam catholicum, et oppositum abici³ tanquam dissonum fidei Christiane.

[ENGLISH]

## ¶3 · 29.7–29.24

> [p. 29] Ut primo sequitur ex eius opposito quod Christus non descendisset ad inferos, nec iacuisset sepultus in sepulcro, sicut tamen⁴ superius allegatur ex fide. Si enim descendit ad inferos, vel secundum deitatem vel secundum humanitatem. Non secundum⁵ deitatem, cum non secundum illam sit mobilis; et si secundum humanitatem, tunc illa fuit servata⁶ pro tunc descendens ad inferos. Nec sufficit hoc, nisi illa pro tunc fuerit sibi ypostatice copulata: quia persone non est attribuenda pars⁷ denominacionis⁸ pro tempore pro quo ipsa non est pars persone: cum tunc omne corpus racione materie foret perpetue,⁹ et omnis homo racione anime eque post mortem viveret sicut ante. Quod negant illi, quibus non sapit, quod Christus vixit humanitus in dicto triduo: unde dicunt quod est impossibile de vi vocis quod Christus fuit mortuus aut sepultus vel quod descendit ad inferos: sed sic intelligitur: corpus, quod quondam fuit Christi, sepultum est, et anima, que quondam fuit Christi, descendit ad inferos, sed non Christus,¹⁰ cum tunc non fuit ita quod Christus est.¹⁰

[ENGLISH]

## ¶4 · 29.25–30.22

> [p. 29] Sed revera ista ficticia superaddit perfidiam Iudeorum. Nam turba Iudaica Ioh. 12. dixit Iesu: ‘nos audivimus ex lege quod Christus manet in eternum’: quia Iesaie¹¹ 9° scribitur: ‘super solium David et super regnum eius sedebit, ut confirmet illud et corroboret a modo¹² et usque in sempiternum,’ id est, a tempore quo ‘puer natus est nobis.’ Probatur sic. Iesus natus est rex humanitus, ut patet Ioh. 18¹³ ‘Tu dicis quia rex sum ego: nam ego¹⁴ in hoc natus sum.’ Cum ergo per mortem non fuit intercisio regni sui, cum fuit spirituale [p. 30] a corpore independens; ergo mansit perpetuo. Confirmatur: quia Daniel 7 scribitur de humanitate Christi: ‘potestas eius eterna que non auferetur,¹ et regnum eius quod non corrumpetur.’ Non ergo potest ille Dominus eciam² secundum humanitatem perdere regnum suum: quia Michee 4^to. dicitur, ‘regnabit super eos ex hoc³ nunc et usque in seculum.’ Et patet⁴ ex hoc quod non est⁵ alia regnacio hominis interioris⁵ in Christo nisi que est⁶ regnacio Christi Dei: sed anima regnavit a principio sue creacionis continue: ergo Christus. Non enim dictus rex Israel secundum humanitatem ut corporaliter regnet sed spiritualiter super illos: ut exponit Augustinus Ome. 50⁷ exponens illud⁷ Ioh. 12 ‘Benedictus qui venit in nomine Domini, rex Israel.’ ‘Non enim,⁸ inquit Augustinus, rex Israel fuit Christus ad exigendum tributum vel ferro exercitum armandum hostesque⁹ visibiliter debellandos; sed rex Israel, quod mentes regat, quod in eternum consulat, quod in regnum celorum credentes sperantes amantesque perducat.’ Cum ergo illa¹⁰ potestas spiritualis, existens subiective in anima independenter¹¹ a corpore, non fuit spoliata ab anima Christi in morte; videtur quod eciam¹² in morte fuit humanitas vel spiritus¹³ Christi rex Israel¹⁴ sicut ante.

[ENGLISH]

## ¶5 · 30.23–31.1

> [p. 30] Unde et illud Psi. 23 ‘attollite portas etc.’¹⁵ exponitur a beato Augustino et Ieronimo de anima Christi descendente ad inferos: ac si angeli preconizantes¹⁶ Christi¹⁷ descensum¹⁸ ad inferos dicerent principibus tenebrarum; ‘O principes mundanorum! attollite¹⁹ portas vestras, et introibit rex glorie cum captivitate ducta ab inferis, portas aperiens²⁰ eternales.’ Et sic in scripturis dirigitur liberacio patrum ab inferis ad personam Christi, quod ipse humanitus immediate ipsam perficeret.²¹ Ut Luce 1°. ‘Illuminare his²² qui in tenebris et in umbra mortis sedent.’ Quod,²³ cum sequitur de [p. 31] virtute sermonis ex dicto principio, est catholice concedendum.

[ENGLISH]

## ¶6 · 31.3–32.1

> [p. 31] Item nemo sapiens et plene potens incipit opus laudabile in propria persona perficere; et, dum perfecerit¹ in propria persona rudimenta² operis,³ committit suo subdito operis complementum. Cum ergo edificacio ecclesie et liberacio patrum⁴ ab inferis sit opus summe laudabile; sequitur quod Christus in propria persona non perficiet imperfectam disposicionem, et committet spiritui creato ypostatice separato belli victoriam, que est operis complementum. Indignius namque⁵ est temptari a dyabolo, pati, et corporaliter disponere ad edificacionem ecclesie, quam⁶ potenter spoliare Tartara⁷ a dyabolo devicto. Si ergo Christus in propria persona passus fuerat et temptatus, quia in carne et⁸ anima ypostatice copulata: per idem in propria persona spoliavit infernum⁹ extrahendo patriarchas ab inferis, specialiter cum non reliquit unionem anime vel corporis quod assumpsit: dicente Augustino Ome. 47. ‘Si enim dixerimus quod Verbum Dei posuit animam suam et iterum sumpsit eam, metuendum est, ne subintret¹⁰ prava cogitacio et dicatur :—Ergo¹¹ aliquando anima illa separata est a Verbo, et aliquando Verbum illud, ex quo suscepit illam animam¹² fuit sine anima.—Video enim fuisse sine anima humana Verbum cum “in principio erat Verbum;”¹³ sed ex quo “Verbum¹³ caro factum est et habitavit in nobis;” et susceptus est¹⁴ a Verbo totus homo, id est,¹⁵ anima et caro. Quid fecit passio, quid fecit mors, nisi corpus ab anima separavit, animam vero a Verbo non separavit?’ Et sequitur. ‘Fidelis latronis animam¹⁶ non deserebat? et deserebat¹⁷ suam? Absit.’ Et quia minus intelligens potest¹⁸ ex dictis intelligere quod Verbum solum per graciam affuit illi anime et non hypostatica¹⁹ unione [p. 32] subdit¹ differenciam: ‘latronis vero¹ animam custodivit, suam vero inseparabiliter habuit.’²

[ENGLISH]

## ¶7 · 32.2–32.13

> [p. 32] Et potest illud confirmari ex hoc, quod aliter patres in limbo³ tantum tenerentur creature, que non est Deus, spoliando³ eos de manu dyaboli, sicut Christo secundum humanitatem: quod est impossibile. Cum ergo persone debetur accio, anima fuit tunc anima persone agentis.⁴ Unde sicut anima Christi non fuit⁵ spoliata gracia per mortem, et per consequens non⁶ gracia unionis; sic non fuit spoliata potestate spirituali regia, caractere,⁷ vel sacerdocio, quod est qualitas indelebilis secundum doctores. Unde sanctus Thomas concedit⁸ quod Christus fuit sacerdos secundum animam in triduo iuxta textum Apostoli ad Hebre 8. ‘Iesus autem eo quod maneat⁹ in eternum sempiternum habet sacerdocium.’

[ENGLISH]

## ¶8 · 32.14–32.23

> [p. 32] Et revera non sapit¹⁰ quod illa anima sit rex et sacerdos, nisi sit persona; quia actus huius officii sint signantissime personales. Et Doctor Subtilis vere dicit quod Christus mansit Christus in illo triduo. Sicut ergo nichil quod non est Deus sufficit genus humanum redimere, sic nichil quod non est Deus suffecit tam potenter de manu inimici patres eripere. Sed si hoc posset¹¹ in virtute Dei creatura ab eo ypostatice separata; per idem posset passio vel meritum cuiuscunque hominis a Deo personaliter seiuncti auctoritate Dei pro quocunque peccato hominis facere recompensam.

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 29: *intelligitur:* (print = bt (in | telligitur across MS-fold marker)) [SUB]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Thus, as Augustine says, ' (28.1); reference 1 Cor. xv. 53. (28.4); reference Mic. iv. 7. (30.5); reference John xii. 13. (30.12); reference Ps. xxiv. (30.23); reference Luke i. 79. (30.31); reference Johni. h. (31.23); reference Ps. lxviii. 18. (32.27).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 28:
1 immortalis om. A B C.
2 in terra A B C.
3 et C.
4 pulius O.
5 in celum om. B.
6 at A B C.
7 post om. A B C.
8 littera initialis om. ut fere semper A B C.
9 cuiuscunque O.
10 de vi sermonis A B; de Christo sermonis C.
11 alia O.

p. 29:
1 3ci A B C O. Qu. modo legendum pro medio?
2 factus O.
3 hĩti B.
4 tamen om. A B; tum C.
5 secundum om. A B C.
6 incarnata A B C.
7 partis codd. omn.
8 denominandum O.
9 perpetuo O.
10-10 cum tunc non ita quod Christus fuit B.
11 ysae O.
12 año A B C; a m° O, i.e. a modo.
13 Ioh. 18 altera manu C.
14 ego om. B.
CHECK (coordinator): entry figure(s) 18 have no figure in the transcription: read the plate foot before citing.

p. 30:
1 aufertur A B C.
2 et A B C.
3 super hoc ex hoc B.
4 quod O.
5 aliqua potestas hominis ynterioris B; aliqua A C.
6 est om. B.
7–7 exponendo O.
8 enim om. B.
9 quia A B C.
10 illa om. A B C.
11 independenter om. C cum lacuna.
12 eciam om. O.
13 pars O.
14 israhel C.
15 etc. om. O B.
16 preconisantes A B C.
17 eius B.
18 descensus A B C.
19 attolite B.
20 apperiendo A; aperiendo B C.
21 proficeret O.
22 illis B.
23 et O.

p. 31:
1 perficerit O.
2 redimenta O.
3 operis om. C.
4 parentum O.
5 nanque A; nam O.
6 quantum A.
7 creaturam A B C.
8 vel C M.
9 in infernum O.
10 subintret om. O.
11 ergo om. B.
12 utcumque O.
13–13 sed . . . verbum om. O.
14 est om. O; suscepit est B.
15 id est om. C.
16 fidelis animam latronis animam B.
17 et deserebat om. O.
18 posset O.
19 apostatica O.

p. 32:
1 dr͡am latronis. Vero A B; dr͡am latronis. Non C.
2 habuit om. O.
3_3 locus corruptus. Qu. tenerentur, tantum creatura . . . spoliante ?
4 persona agens A B C.
5 est A B C.
6 non om. A B C.
7 correctere O; nempe charactere.
8 concessit A B C.
9 manet A B C; moneat O; maneat Vulg.
10 non sapit om. B; sapit om. O.
11 potest A B C.
12 apropriate A B C.
13 descensus C.
14 "de Christo" dicente. Sola ascendisti A; de Christo solo ascendisti B; dicente de Christo: Spolia ascendisti C.
15 Illi A B C.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 28: \_Ostendit quod Christus fuit homo in triduo, et obicit multipliciter et dissolvit, Chrisfs humanity was not suspended during the three days' entombment.'] | littera mitia/is om. ut fere semper
p. 29: codd. omn.
p. 30: cum lacuna. n
p. 32: eg fc | locus corrtiptus. Qu.
```

---

## Chunk 03-b: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-03-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-03-b
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "32.24–36.14"
divisions: "cap. 3 (heading 'Cap. III.' at 28.0); part 2 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "901 words; 900 confirmed by Fordham or the vote; 1 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n71–n75 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 3, part 2: [TITLE]

## ¶1 · 32.24–33.6

> [p. 32] Unde videtur michi scripturas insolubiles appropriate¹² tribuere persone Christi descensum¹³ ad inferos et spoliacionem fidelium de potencia inimici. Nam Psalmo 67 dicitur ad litteram¹⁴ de Christo dividente spolia ‘Ascendisti¹⁴ in altum’ sed prius ‘cepisti captivitatem,’ et 3°. ‘dedisti dona hominibus.’ Cui¹⁵ sensui alludit Apostolus ad Ephes. 4. [p. 33] ‘Ascendens,¹ inquit, Christus in altum,² captivam duxit captivitatem.’ Et sequitur: ‘quod autem ascendit, quid³ est, nisi quia descendit primum ad partes inferiores terre?’ Et ut ostenderet nobis quod eadem sit persona, que hec cuncta perficiat, subiungit: ‘qui descendit ipse est et qui ascendit super omnes celos ut impleret omnia.’

[ENGLISH]

## ¶2 · 33.7–33.16

> [p. 33] Ex istis verbis Apostoli patet primo quod loquitur de Christo secundum humanitatem, secundum quam solum ascendere et descendere sibi conveniunt.⁴ 2°. probat illum hominem esse Deum, cum post ascensionem dedit spiritualia dona hominibus mittendo eis Spiritum Sanctum, ut testatur utrumque testamentum et rei eventus probaverat in effectu. 3°. intendit quod eadem persona secundum humanitatem eandem descendit et⁵ taliter⁵ ascendit. ‘Qui descendit, inquit, ipse et non alius ascendit,’ racionem autem subiungit ‘ut impleret omnia.’

[ENGLISH]

## ¶3 · 33.17–34.13

> [p. 33] Cum enim tres sint⁶ regiones mundi notabiles,⁷ in quibus oportuit Christum humanitus possessionem accipere vel sesinam,⁸ scilicet celestium, terrestrium, et infernorum; proporcionaliter⁹ descendit tripliciter benefaciens et repetens omagium de¹⁰ subiectis. Primo descendit per inanicionem secundum infirmitatem carnis, et¹¹ eum mundus infirmus sibi similis in carne¹¹ et anima eciam genus proprium non cognovit. 2°. Descendit ad patres in limbo qui erant tantum¹² in spiritu post triumphum sed proporcionaliter in anima,¹² et indubie fuit in illo triduo in sinu Abrahe per 36 horas, quibus passio¹³ continuata fuerat, non parva exaltacio capite coniuncto membris cum multitudine angelorum. Sicut enim sexto die creatum est genus humanum,¹⁴ sic sexto senario, qui est numerus perfectus ex ductu eius in se circulariter, [p. 34] fuerat recreatum; ut¹ per tantum tempus clarere² posset veritas et excludi³ ficticia mortis Chrsti. Resurrexit autem, ut confortaret ecclesiam de fide resurreccionis future, ut patet ad Cor. 15;⁴ et ut ‘primatum teneat’ ut abbas ordinis Christiani aperiendo⁵ patribus complete purgatis ianuam eternalem. Tempus autem continens purum integrum diem et duas seminoctes significat quod simpla mors Christi,⁶ que integraliter fuit lucida proporcionaliter ad vitam, fuit medium sufficiens ad nostram duplicem mortem semiplenam. Tercius vero⁷ fuit descensus⁸ corporis in sepulchro,⁹ qui nedum ostendit corpus vere mortuum anima ab eo¹⁰ elongata, sed per omnia factus nobis consimilis sanctificavit subterraneas requies beandorum.

[ENGLISH]

## ¶4 · 34.14–34.19

> [p. 34] Et correspondenter tres maneries hominum eripuit, et tres¹¹ dimisit. Extraxit enim, quasi mordens infernum, patriarchas prophetas et fideles alios, quorum peccata sunt plene purgata, relictis purgandis in purgatorio et dampnatis in inferno; sive sint infantes solis originalibus, si sit possibile, irretiti; sive adulti peccatis actualibus maculati.

[ENGLISH]

## ¶5 · 34.20–35.5

> [p. 34] Sed 3°. post privatam instruccionem apostolorum 40 diebus, ut patet Actuum 1°, ascendit gloriose in celum secundum utramque naturam summe beatus, ducens secum numerum insensibilem suo tempore captivorum; et sic tenendo primatum multiplicem inter omnia supposita humani generis, sicut est prior vel abbas omni dignitate: iuxta illud Baptiste: ‘qui post me venit ante me¹² factus est,’ Ioh. 1°. sic habuit primatum resurgencium, et virtute sui solius ascendentis omnia genera hominum ad se trahentis¹³ fuit primus celum intrancium. Nemo enim sufficit¹⁴ suo imperio portas huius¹⁵ aperire¹⁶ nisi filius hominis,¹⁷ qui notus hostiariis prius descenderat.¹⁷. Et sic indubie sicut illuminavit istas tres [p. 35] machinas sua humanitate impletas, ita suscepit omagium¹ vel obsequium utrobique: cum secundum Apostolum ad Philipp. 2°. ‘oportet quod in nomine Iesu omne² genu flectatur celestium, quos restituit, terrestrium, quos redemit, et infernorum,’ quos spoliavit.

[ENGLISH]

## ¶6 · 35.6–35.29

> [p. 35] Omnia quidem hec fecit humanitas Christi. Et ideo post tantum honorem triumphalem individui humane nature prohibuit nimirum Iohannem angelus seipsum vel³ dulia adorare, ut⁴ patet Apoc. ultimo capitulo: ante quidem satis permiserant,⁵ ut patet Gen. 18 et Iosue 5. Omnia quidem hec fecit idem filius hominis secundum eandem humanitatem continue⁶ ypostatice copulatum: qua unione habita patet quod oportet Christum esse continue creaturam et aliquid quod prius non fuerat. Sed quid, rogo, si non homo? Ipsa ergo humanitas fecit⁷ hec omnia, id est, ‘in opus ministerii, in edificacionem corporis Christi,’ ut dicit Apostolus ad Ephes. 4°., quia Ioh. 4°. dicitur: ‘meus cibus est ut faciam voluntatem eius, qui⁸ misit me, ut perficiam opus eius,’ id est,⁸ ut perfecte usque ad consummacionem faciam: inter que hoc videtur principium,⁹ descendere ad inferna et'extrahere patres captivos in limbo, sicut ante promiserat. Et huic consonat¹⁰ illud Zacharie¹¹ 9°. ubi post propheciam Messie quod veniet salvator et ipse ‘pauper et ascendens super asinam et super pullum asine’ alloquitur eundem Messiam in hec verba: ‘Tu quoque in sanguine testamenti tui emisisti vinctos tuos de lacu in quo non est aqua.’ Quod¹² exponitur ad litteram de patribus incarceratis in limbo. Et¹³ idem sonat illud Osee 13. verificatum ad litteram de Messia: ‘ero¹⁴ mors tua, o mors; ero morsus tuus, inferne.’¹⁵

[ENGLISH]

## ¶7 · 35.30–36.5

> [p. 35] Qui ergo sumus,¹⁶ ut impugnemus tenorem¹⁷ verborum fidei vel scripture,¹⁷ specialiter cum sanctioribus et approbatioribus [p. 36] doctoribus visa sit illa logica² subtilis et de virtute sermonis verissima?² Pro certo per idem possemus innovando falsificare reputacione totum corpus biblie³ scripture. Ideo expedit obstare principiis erroris⁴ ne error intollerabilis⁵ consequatur.

[ENGLISH]

## ¶8 · 36.6–36.14

> [p. 36] Item iuxta sic loquentes sequitur quod Christus bis factus fuit homo, bis eciam incarnatus. Nam semel fuit incarnatus et humiliatus⁶ in utero virginis et in morte desiit⁷ esse homo et caro, et post pro instanti⁸ resurreccionis incepit esse homo corporeus: ergo conclusio. Si enim⁹ homo pro quacunque modica¹⁰ morula reticens post loquelam reloquatur,¹¹ bis loquitur; multo evidencius persona, que 33 annis¹² est homo et post per¹³ intercisum triduum non est homo ac tercio post est homo, bis evidenter est homo.

[ENGLISH]

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference Ps. lxviii. 18. (32.27); reference Eph. iv. 8-10. (33.1); reference Jonn1, n* (33.24); reference l Cor. xv. 12. (34.4); reference Johni. 30. (34.26); reference Rev. xxii. 9. thereby exalled (35.8); reference Gen. xviii. 2. Josh. v. 14. . . (35.10); reference Hos. xiii. 14. (35.28); reference John iii. 6. (36.27).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 32:
1 dr͡am latronis. Vero A B; dr͡am latronis. Non C.
2 habuit om. O.
3_3 locus corruptus. Qu. tenerentur, tantum creatura . . . spoliante ?
4 persona agens A B C.
5 est A B C.
6 non om. A B C.
7 correctere O; nempe charactere.
8 concessit A B C.
9 manet A B C; moneat O; maneat Vulg.
10 non sapit om. B; sapit om. O.
11 potest A B C.
12 apropriate A B C.
13 descensus C.
14 "de Christo" dicente. Sola ascendisti A; de Christo solo ascendisti B; dicente de Christo: Spolia ascendisti C.
15 Illi A B C.

p. 33:
1 ascendit A B C; ascendens O.
2 et *add.* B.
3 quidem O.
4 convenit O.
5-5 taliter et A B C.
6 sint *om.* O.
7 nobiles A C; mobiles B.
8 se'suram A; sessuram B C.
9 proporcionabiliter A B C, *ut infra.*
10 a C O.
11-11 et tunc eum mundus infernus similis in carne A B C.
12-12 tamen post triumphum *om.* in spiritu O. *An ita corrigendum?*—qui erant tunc tantum in spiritu sed post triumphum proporcionaliter in anima.
13 possessio A B C.
14 humanum *om.* A C; hominum O.

p. 34:
1 et A B C O.
2 clare A, pr. manu. clarere A corr. alt. manu. B C O.
3 concludi O.
4 ad corum. 3°. O.
5 apperiendo A.
6 mors Christi simpla B; simplani—oris (sic) Christo O.
7 Tercio non C; 3°. vero O.
8 decensus O.
9 sepulcris A B.
10 a deo O.
11 et tres om. O.
12 prior add. C.
13 trahentes O.
14 suffecit A B C.
15 huiusmodi B.
16 apperire A O.
17_17 hominis hostiarius prius descenderet A B C; hominis qui notis hostiariis prius descenderat O; hostiarius pro ostiarius.
CHECK: the main text also has footnote figures 18 (after "aperire") and a second 17 (after "descenderat"), the text's figure 16 is absent where 18 is printed; the foot has no entry 18.

p. 35:
1 homagium C O.
2 Jesu omne om. B.
3 vel om. A B; se om. O.
4 ut ut C.
5 permiserat A B C; promisserant O; permiserant sc. angeli.
6 continue om. A.
7 fecit bis O.
8–8 qui . . . est om. O.
9 primum A B C.
10 et add. O.
11 zekarie O.
12 sed B.
13 ad add. O.
14 ero om. B.
15 in inferno O.
16 quum ergo nescimus O.
17–17 vel tenorem verborum scripture A B C.

p. 36:
1 approbatis A B C; approbatoribus O.
2 lingva (lingbba B) subtilis et de vi verbi sit vera A B C.
3 biblie om. O.
4 errorum A B C.
5 intellerabilis O.
6 humanitus A B C.
7 desivit O.
8 et post tempore A B C; pro Θti O, ut saepe infra.
9 ergo A B C.
10 monica B.
11 reloquendo O.
12 annis om. B.
13 per om. A B C.
14 verbi B.
15 dupliciter A B.
16 eternas B.
17 prima est B C; persone O.
18 vel instanti resurreccionis A; pro tempore sibi instanti resurrectionis B; pro Φ resurrectionis C; pro Θti resurreccionis O.
19 in A B C.
20 esset suppositum A B; esset persuppositum C.
21 ut A B C.
22 creatum (lineatum in margine) ac creata anima, anima copulata A; creatum ac creata anima copulata B; lineatum ac creata anima anima copulata C.
23 proporcionalis A B C.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 32: eg fc | locus corrtiptus. Qu.
p. 35: sc. angeli.
```

---

## Chunk 03-c: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-03-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-03-c
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "36.15–40.15"
divisions: "cap. 3 (heading 'Cap. III.' at 28.0); part 3 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1026 words; 1026 confirmed by Fordham or the vote; 0 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n75–n79 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 3, part 3: [TITLE]

## ¶1 · 36.15–37.4

> [p. 36] Sed consequens videtur¹⁴ falsum tripliciter.¹⁵ Primo ex hoc quod tunc resurreccio Christi foret eius nativitas vel generacio. Et sic Christus haberet triplicem nativitatem et generacionem multiplicem: nativitatem unam eternam et duas alias temporales.¹⁶ Nam generacio Christi prima¹⁷ in utero ideo est generacio quia est produccio a non esse hominem ad esse hominem. Cum ergo sic sit pro instanti¹⁸ resurreccionis, sequitur quod illa sit generacio, et per idem nativitas ex¹⁹ sepulcro, sicut foret posito quod semen virginis esset per se positum²⁰ in sepulcro, et²¹ successive vel subito lineatum,²² ac creata anima copulata.²² Nec est locus nativitati corporali pertinens, nisi forte racione conservacionis, sicut nec est pertinens nativitati ex spiritu, de qua Ioh. 3°., sed utrobique habita generacione renati consequitur proporcionaliter²³ [p. 37] nativitas. Oportet ergo ad resurreccionem persone quod eadem persona, que cecidit sopore mortis sive¹ intercisione humanitatis, resurgat; cum spiritus racionalis persone² sit humanitas et sic homo.

[ENGLISH]

## ¶2 · 37.5–37.19

> [p. 37] Secundo obicitur contra dictum consequens per hoc, quod mundus per mortem Christi esset quantumlibet imperfectus: quod est impossible, cum illa fuit mors iustissima preciosissima et utilissima perficiens³ totum mundum: et consequencia probatur. Christus, in quantum homo, est pars mundi, ut patet eciam modernis loquentibus, qui concedunt Christum, in quantum homo est, esse creaturam: et mundus est universitas creaturarum. Cum ergo Christum esse hominem plus perficit mundum quam totum usque⁴ celum vel quecunque alia pars mundi; videtur quod, hoc ablato, plus proporcionaliter imperficitur ille mundus: quod est impossibile; cum tanta perfeccio, quanta ad humanitatem Christi attinet, servatur in anima et corpore incorrupto. Ideo cum totum⁵ sit sue partes, patet quod mansit idem homo in triduo.

[ENGLISH]

## ¶3 · 37.20–39.9

> [p. 37] Tercio confirmatur illud ex⁶ testimonio scripture. Nam Ioh. 19 scribitur: ‘ad Iesum autem cum venissent,⁷ ut⁸ viderunt eum iam mortuum, non fregerunt eius⁹ crura; sed unus militum lancea¹⁰ latus eius¹¹ apperuit,¹² et exivit sanguis¹² et aqua: et qui vidit, inquit Iohannes, testimonium perhibuit;¹³ et verum est testimonium eius.’ Rogo, quomodo venissent ad Iesum mortuum,¹⁴ nisi ille homo mortuus esset Iesus? aut quomodo miles lancea latus eius Iesu aperiret,¹⁵ si non tunc fuerat latus Jesu? Numquid credimus quod evangelista, tam signanter asserens¹⁶ se ista vidisse ultra omnia alia¹⁶ gesta Christi, finxit mendacium? Et si dicatur quod littera occidit, sensus autem spiritualis et rectus vivificat, [p. 38] cuiusmodi est talis ?—cum venissent ad illud corpus mortuum, quod non¹ potuit esse Iesus, sed¹ prius, non tunc fuit corpus Iesu; tunc unus militum, non latus eius, nec univoce latus alicuius aperuit, sed partem unius corporis mortui, quod non tunc fuit Christus vel pars eius²; et exivit, non sanguis redempcionis et aqua baptismatis de latere Christi, quia tunc non fuit Christus. Et sic spiritus, aqua,³ et sanguis non sunt nec fuerunt testes humanitatis Christi, quia non simul fuerunt, sicut videtur Iohannes dicere I Ioh 4°. Nec est verum ad verba illud quod dicit Apostolus ad Ephes. 5°. quod ‘Christus sic dilexit ecclesiam quod tradidit semetipsum pro illa, ut sanctificaret⁴ mundans eam lavacro aque in verbo vite;’ cum ecclesia per totum triduum fuit cum sponso vel capite Christo.⁵ Nec est illud Apostoli ad Ephes 5°. verum ad verba, quando illud Gen. 2.⁶ dictum⁷ ad sensum litteralem de primo Adam et de uxore⁷ sua, exponit ad sensum misticum de Christo et ecclesia: ‘hoc, inquit textus, nunc os ex ossibus meis et caro de carne mea: propter hoc relinquet⁸ homo patrem et matrem suam et adherebit uxori sue, et erunt duo in carne una.’ ‘Sacramentum,⁸ inquit Apostolus, hoc magnum est: ego autem dico in Christo et in ecclesia.’ Illa autem exposicio Apostoli est impossibilis, scilicet quod,⁹ sicut ex costa Adam resoluti¹⁰ in soporem¹¹ edificata est sponsa eius secundum membra ossea solida et tenera, sic ex apertura¹² lateris secundi Adami edificata est ecclesia sponsa Christi secundum varietatem¹³ membrorum ecclesie. Nec reliquit¹⁴ Christus Patrem semetipsum¹⁵ exinaniendo¹⁶ et exeundo a¹⁷ Patre, ut dicitur Ioh. 16°.; et ‘matrem synagogam in qua natus’ est Isa. 50;¹⁸ et adherebit uxori sue scilicet ecclesie, ut dicitur Osee 2°. Nec erant duo coniugata in eadem natura communi tam secundum carnem¹⁹ quam [p. 39] spiritum ac¹ affeccione tam sensitiva quam intellectiva concordes; ut exponit Augustinus et alii sequentes Apostolum. Sed quelibet illarum particularum est impossibilis de vi vocis cum Christus non passus est mortem in cruce; quia pro² instanti mortis Christus non est Christus, nec fuit illud sacramentum in Christo et ecclesia: cum pro toto triduo non fuit Christus, sed sponsa exspectavit usque ad instans resurreccionis sponsalia. Deliramenta sunt ista et verbis puerorum similia.³

[ENGLISH]

## ¶4 · 39.10–39.21

> [p. 39] Unde omnes moderniores doctores, quorum scripta memini me legisse, dicunt concorditer quod in triduo corpus illud fuit corpus Christi sicut et anima fuit tunc anima Christi: quia manentibus extremis unionis⁴ Verbi ad naturam assumptam, manet eadem unio. Unde dicunt, quod est synecdochica⁵ locucio, sepelierunt Iesum, id est, corpus Iesu. Sed⁶ ego non video, quomodo foret tunc corpus Iesu,⁶ nisi Iesus tunc foret Iesus corporeus, habens omnes partes illius corporis partes suas, iuxta illam⁷ Veritatis vocem Mt 26°. ‘mittens hec unguentum⁸ hoc in corpus meum ad sepeliendum me fecit.’ Pro certo ego credo quod ipse Christus sicut et⁹ quelibet pars corporis sui sepultus est.

[ENGLISH]

## ¶5 · 39.22–40.15

> [p. 39] Ideo hoc¹⁰ concedo cum istis doctoribus in prima parte, cum sit de fide, et concedo de summa virtute sermonis Christum iacuisse in sepulcro; cum illud corpus mortuum fuit persona¹¹ Verbi: non quod¹² quelibet pars quantitativa illius corporis generaretur¹³ pro instanti mortis, sic quod Christus tunc generaretur assumendo novam naturam: sed manens continue idem¹⁴ corpus prius vivum et¹⁵ post mortuum subiectum est perpetuo¹⁶ eidem ypostatice unioni. Nam per totum triduum Christus mansit homo tam secundum corpus quam secundum¹⁷ animam; et vere passus est mortem pro [p. 40] instanti separacionis; cum caro mortua, que tunc¹ fuit Christus, passa est privacionem vite: et vere de latere Christi exierunt aqua et sanguis Christi pro mora exitus; quia Christus pro toto triduo est idem corpus mortuum, cuius sanguine et spiritibus effluentibus, ut anima naturaliter separetur, reservata est miraculose subtilior pars sanguinis cum ichore² ad sponsalia celebranda inter sponsum viventem gloriose in triduo post triumphum et corpus suum misticum, quod est ecclesia. Nam Isae 11°.³ scribitur: ‘radix Iesse⁴ in signum populorum, ipsum gentes deprecabuntur; erit sepulcrum eius gloriosum.’ Et sic intelliguntur alie scripture de Christo ad litteram tam novi quam veteris testamenti. Oportet enim interpretari⁵ scripturas de Christi humanitate secundum sensum, quem in eis sancti doctores sunt sedule scrutati.

[ENGLISH]

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference John iii. 6. (36.27); reference Eph. v. 26. (38.10); reference Eph. v. 31, 32. (38.14); reference Gen. ii. 24. (38.15); reference Johnxvi.27. (38.28); reference Hos. ii. 16, 19. (38.30); reference Matt. xxvi. 12. (39.17); reference John xii. 35. (40.21).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 36:
1 approbatis A B C; approbatoribus O.
2 lingva (lingbba B) subtilis et de vi verbi sit vera A B C.
3 biblie om. O.
4 errorum A B C.
5 intellerabilis O.
6 humanitus A B C.
7 desivit O.
8 et post tempore A B C; pro Θti O, ut saepe infra.
9 ergo A B C.
10 monica B.
11 reloquendo O.
12 annis om. B.
13 per om. A B C.
14 verbi B.
15 dupliciter A B.
16 eternas B.
17 prima est B C; persone O.
18 vel instanti resurreccionis A; pro tempore sibi instanti resurrectionis B; pro Φ resurrectionis C; pro Θti resurreccionis O.
19 in A B C.
20 esset suppositum A B; esset persuppositum C.
21 ut A B C.
22 creatum (lineatum in margine) ac creata anima, anima copulata A; creatum ac creata anima copulata B; lineatum ac creata anima anima copulata C.
23 proporcionalis A B C.

p. 37:
1 sine A B C.
2 species racionalis per se O.
3 utillissima et totum om. perficiens O.
4 usque om. A B C.
5 toum sic C.
6 ex om. B.
7 pervenissent B.
8 et A B C O, ut Vulg.
9 eius om. B.
10 lancia O.
11 eius om. O.
12_12 perforavit et sangwis C.
13 perhibet O.
14 venissent add. B.
15 apperiret (sic) A; aperuit B.
16 se vidisse omnia ista ultra omnia alia B.

p. 38:
1–1 non potuit . . . sed om. A B C.
2 eius om. O.
3 a quo B.
4 eam add. A B C.
5 Christo om. O.
6 3° A B C.
7–7 dictum . . . uxore om. O.
8–8 relinquet etc. Sacramentum B.
9 quod om. A B.
10 resoluta A B; resoluto C.
11 sopore B.
12 appertura A B C; aptura pro aptura[?] O.
13 veritatem A B C.
14 requirit O.
15 seipsum O.
16 exanimiendo A B C.
17 de O.
18 Isa. 7 A B C.
19 naturam in margine corr. carnem B.

p. 39:
1 et B; om. O.
2 per C.
3 puerorum dissimilia A B C.
4 unionibus A B C.
5 synochica A; sinodochia B; synodogica O; syndochica C. pro synecdochica i.e. per synecdochen.
6–6 sed . . . Iesu om. O.
7 illud O.
8 hec om. A B C; hunguentum B.
9 in O.
10 hoc om. A B C; ideo om. O.
11 Christi add. O.
12 quod om. O.
13 generabatur A B O.
14 continuo A B C; illud C.
15 et om. A B C.
16 perpetue B.
17 secundum om. C O.

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
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 39: i.e. per synecdochen.
```
