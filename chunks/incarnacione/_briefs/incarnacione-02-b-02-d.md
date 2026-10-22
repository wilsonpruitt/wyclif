# Translation brief: incarnacione 02-b–02-d

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/incarnacione/wyc-incarnacione-02-b.md chunks/incarnacione/wyc-incarnacione-02-c.md chunks/incarnacione/wyc-incarnacione-02-d.md` once and fix what it reports.
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
  carries Harris's **italic runs** per page (from the scan's OCR, rough; his quotation bounds and the
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

- `[^n]` from 1, the marker placed in the same edit as its note, each opening with a type letter:
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

## Glossary (the 278 rows these chunks use; the full file is GLOSSARY.md)

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
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
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
| autorizare | authorize | Ruled 2026-09-28 (6 sites). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| temporalia | temporal goods | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| censura | censure | Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| thema | theme | The scripture text of a sermon. Ruled 2026-09-28 (2 sites). |
| possessionati | the possessioners | Endowed religious. |
| protestacio; protestari | declaration; to declare solemnly | ⭐ The submission formula ("if anyone can teach me this is contrary to scripture or reason, I will humbly retract"). Penn and Lahey both inverted it (T. pp. 369, 378). Render it as a retraction offer, never as defiance. |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| simpliciter / secundum quid | **without qualification / in a certain respect** | ⛔ Always opposable. Never "simply", "wholly", "directly", "naturally" etc. (T. p. 364). |
| necessitas supposicionis / ex supposicione | necessity of supposition / necessity on supposition | Conditional necessity. Pilot (*Eccl.* 3.21); *ex supposicione* ruled 2026-10-02 (34.12, 38.22). |
| de congruo / de condigno | by congruity / by condignity | Pilot. |
| consequencia | inference | ⛔ Not "consequence" (T. p. 361 n. 13). |
| consequens / antecedens | consequent / antecedent | |
| sequitur | it follows | Introduces a stated inference, often quoted in the next words. Pilot (*Eccl.* 2.21). Not tagged where it is not an inference ("the third law follows", *Dial.* ch. 5). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| propositio copulativa / disiunctiva | conjunction / disjunction | Not "copulative proposition" (T. p. 365). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| glosare | to gloss | Interpret so as to remove the difficulty (T. p. 366). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| citra fidem | short of faith | The contrast with *ex fide*: held on evidence, not as faith teaches. Ruled 2026-09-28 (4 sites). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| citra Christum | short of Christ | As *citra fidem*. Ruled 2026-10-02 (45.8). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| glosa | gloss | The noun beside *glosare*. Ruled 2026-10-02 (52.10). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |
| humanitas | the humanity | The nature the Word assumed, body and soul; with the article (*humanitas sit Christus*, "the humanity is Christ"). Not "the human nature", which is *natura humana*. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| incommunicans / incommunicantes (*nature*) | that do not communicate (with one another) | None predicated of, or shared with, another (Godhead, body, soul). Not "incommunicable": keep the participle. Ruled 2026-10-22 (Wilson; *Incarn.* 1.4). |
| assumere / assumpcio (*naturam*) | assume / assumption | Of the nature, as in the fathers. ⚠ Kept apart from the logician's *assumptum* "the assumption" (above): C note where the logical sense occurs. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| triduum (*in triduo*) | the three days | Death to resurrection, body in the tomb (Lombard, *Sent.* III d. 22). Ruled 2026-10-22 (Wilson; *Incarn.* prol). |
| ydemptitas specifica | identity of species | That Christ and other men are of one species. Not "specific identity" (reads as "particular"). Ruled 2026-10-22 (Wilson; *Incarn.* prol, 8). |
| Verbum | the Word | Pronoun **"he"** (as Douay–Rheims John 1:3, "by him"), never "it", though the Latin is neuter. Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.3–4). |
| homo assumptus | the assumed man | A term of art (the Lombard's first opinion, *Sent.* III d. 6); keep "assumed" before "man", never "the man assumed". Ruled 2026-10-22 (Wilson; *Incarn.* 5.15). |
| secundum quod (reduplicative) | insofar as | ⛔ Never "in that" (heard as "because", which inverts the logic). Ruled 2026-10-22 (Wilson; *Incarn.* 5.29–6.24). |
| secundum deitatem / secundum humanitatem | as to the Godhead / as to the humanity | The rule of reduplication; keep it in Wyclif's place in the sentence. ⛔ Never supply "as God / as man" where the Latin has bare apposition (*ipse Deus*) or bare predication. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| natura | nature | Ruled 2026-10-22 (Wilson; *Incarn.* 3.4). |
| persona | person | Ruled 2026-10-22 (Wilson; *Incarn.* 4.14). |
| creatura / creator / creatus | creature / creator / created | ⛔ Never "creation" for the created thing. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| posicio / proposicio / predicacio | position / proposition / predication | Kept apart: the apparatus shows the three trading places (*Incarn.* 4.15). Ruled 2026-10-22 (Wilson). |
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
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). Inside a DR quotation of Titus 1:7, DR's "steward" (2026-10-08). |
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
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| rectiloqui | those who speak correctly | Ruled 2026-10-02 (*Eccl.* 19, 468.15). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| univoce | univocally | Ruled 2026-10-02 (*Eccl.* 21, 514.4). |
| incompossibilis | incompossible | Beside *compossibilis*. Ruled 2026-10-02 (*Eccl.* 22, 522.1). |
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
| premium accidentale | accidental reward | Ruled 2026-10-02 (*Eccl.* 23, 565.6). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
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
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| regulariter | as a rule | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 165.2). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| memorativa potencia | memorative power | A faculty of the soul (the "power" sense of *potencia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 219.27). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| imperium (vicarium, autoritativum) | command (vicarial, authoritative) | The power to command (*par in parem non habet imperium*); "empire" only of the Empire. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 263.2). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| preponderancia; dispensacio | preponderance; dispensation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 266.11, 268.4). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| pontifex (Old Testament, unqualified) | pontiff | Kept apart from *sacerdos* "priest"; *summus pontifex* of the Jewish priesthood is "high priest" (see *summi pontifices*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* ch. 11). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| calumpniator | challenger | Under *calumpnia* "challenge". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 323.10). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| remisse (of assent) | with slackened [assent] | Opposed to full assent in the degrees of belief. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 328.18). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| episcopi cesarei | caesarean bishops | Extends *prelatus / sacerdos cesarius*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 331.24). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| evangelizans | preacher of the gospel | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-g). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| provisio (papal) | provision | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* ch. 12). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |
| coloracior | more colourable | Comparative, with the *color* / *colorabilis* rows. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 384.15). |
| servitus ydolorum | servitude of idols | Beside *servitus laboris*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |
| nimis | exceedingly | Medieval intensive (= *valde*); "too much" only where excess is the point. Ruled 2026-10-12 (close-out R2; *Pot. pape* 169.2). |

---

## Chunk 02-b: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-02-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-02-b
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "17.20–21.22"
divisions: "cap. 2 (heading 'Cap. II.' at 13.0); part 2 of 4, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1040 words; 1033 confirmed by Fordham or the vote; 3 runs stood by rule (both witnesses garbled); 4 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n56–n60 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 2, part 2: [TITLE]

## ¶1 · 17.20–18.5

> [p. 17] Secundo stetit¹¹ error Arrianorum in hoc quod dicunt Christum sine anima solam carnem suscepisse¹²; ut meminit Augustinus libro suo De Heresibus Heresi 49. 'Arriani, inquit, dicti ab Arrio in eo sunt notissimi¹³ errore, quo Patrem et Filium et Spiritum Sanctum nolunt esse eiusdem substancie vel nature; sed Filium dicunt creaturam, Spiritum vero creaturam creature; hoc est, ab ipso Filio creatum¹⁴ volunt. In eo autem quod dicunt Christum sine anima solam carnem sumpsisse minus noti sunt. Sed hoc verum esse¹⁵ Epifanius¹⁶ non tacuit, et ego ex eorum scriptis et collocucionibus certissime comperi.' Et in hoc conveniunt cum Appollinaristis¹⁷; de quibus scribit Augustinus Heresi 55 [p. 18] quod de anima Christi ab ecclesia catholica¹ differunt² dicentes, sicut Arriani, Dominum³ Jesum Christum sine anima carnem suscepisse,³ et Verbum fuisse pro anima: et sic glosant scripturas loquentes de anima Christi et Verbum in carnem⁴ fuisse conversum, non carnem sumpsisse de virgine.

[ENGLISH]

## ¶2 · 18.6–18.20

> [p. 18] Et illam heresim⁵ elegantissime destruit Augustinus Ep. 127⁶ et duabus sequentibus ad Pascencium episcopum Arrianum; cuius dicta utinam hodierni atttenderent! Scribit enim capcioso heretico, non puto⁷ quidquam inprovide de quo calumpniam formidaret.⁸ 'Quia, inquit, Dei Patris unigenitus Filius Dominus et Deus noster Jesus Christus, postquam ''venit plenitudo temporis'' opportune⁹ ''formam servi suscepit'' ad diem salutis nostre¹⁰; de illo multa¹⁰ in scripturis sacris¹¹ secundum ''formam Dei'' dicuntur, multa secundum ''formam servi'': quorum exempli gracia duo commemoro,¹² ut singula ad singula referantur.¹³ Secundum formam Dei ait ''ego et Pater unum sumus'': secundum autem¹⁴ servi ipse de se ait ''Pater maior me est.''' Nescivit¹⁵ enim ille¹⁶ sanctus negare scripturas illas¹⁷ de virtute sermonis, cum personam¹⁷ Filii concedit¹⁸ esse multorum quodlibet.

[ENGLISH]

## ¶3 · 18.21–19.4

> [p. 18] Et ponit ad hoc consequenter duplicia exempla quibus Deus hucusque non¹⁹ dignatus est ostendere hominibus meliora, per que tam in noticiam Trinitatis quam eciam incarnacionis posset²⁰ hereticus manuduci. Primum sic. 'Cum corpus, inquit, et anima sunt unus homo, quamvis corpus et anima non sunt²¹ unum; cur non multo magis Pater et Filius sunt unus Deus? cum Pater et Filius sunt unum secundum illam Veritatis vocem ''ego et Pater unum sumus.'' Cum, inquit, homo exterior et interior homo non sunt unum, neque eiusdem nature est exterior cuius [p. 19] est interior¹; quia exterior cum corpore nuncupato¹ dicitur homo; interior autem sola anima racionali² intelligitur; utrumque tamen illorum simul non³ duo homines sed unus dicitur: quanto magis Pater et Filius unus Deus est?'

[ENGLISH]

## ¶4 · 19.5–19.25

> [p. 19] Secundum exemplum est de natura universali. 'Homines, inquit, per consorcium et communionem⁴ unius eiusdem nature qua omnes homines unum erant, et si aliquando secundum diversitates voluntatum et sentenciarum opinionum et morum dissimilitudines⁵ non erant unum, erunt⁶ tamen perfecte pleneque unum⁶ cum perventum fuerit ad eum finem ut sit ''Deus omnia in omnibus.'' Et sic non est possibile homines esse unum in caritate vel alio accidente, nisi prius sint unum in substancia vel natura: ut declarat libro primo et⁷ 3° contra Maximinianum 22° capitulo. Quod autem multi homines sint unum in substancia vel natura⁸ probat⁹ per illud Apostoli ad Cor. 3° dictum¹⁰ de Paulo et Appollo ''qui plantat et qui rigat unum sunt.'' Unde Veritas Joh. 17.¹¹ ''Non¹² (dixit) rogo ut ipsi et nos unum simus;''¹² sed ''ut ipsi unum sint, sicut et nos unum sumus¹³:'' non solum natura quod iam erat verum, sed et perfecte¹³ caritatis atque iusticie¹⁴ pro sue¹⁵ capacitate nature, quantum¹⁶ in Dei regno esse poterit,¹⁷ ut sic ipsi summe unum sint in natura sua, sicut Pater et Filius summe unum sunt incomparabiliter¹⁸ meliori natura. Nunquam, inquit, de aliquibus rebus legimus quod unum sunt, nisi sint eiusdem substancie vel nature.'

[ENGLISH]

## ¶5 · 19.26–20.13

> [p. 19] Et indubie¹⁹ in illo errore de universalibus cecati sunt Arrius, Sabellius, et quam plures heretici. Ideo Anselmus De Incarnacione primo vocat²⁰ negantes universalia ex parte rei extra signa²¹ dialectice hereticos. Unde Pascencius Arrianus postquam [p. 20] vocaverat¹ Augustinum succensum errore tanquam aqua cenosa se ingurgitantem et ut arborem curvam et nodosam que nichil rectitudinis in se habet, scribit quid moveat² eum ad depravandum sentenciam Augustini confitentis sibi in³ scriptis fidem suam. Nam⁴ inter alia beatus Augustinus scripsit sibi Patrem et Filium et Spiritum sanctum esse unum Deum, 'Quis, inquit, Pascencius e⁵ tribus personis est unus Deus? an forte una est persona triformis que hoc nomine nuncupetur?' Si iste hereticus cognovisset quomodo⁶ unica⁷ communis humanitas est quelibet persona hominis; vidisse potuisset⁸ faciliter quomodo unica deitas, essencia, substancia, vel natura divina, est tres persone et quelibet earundem.

[ENGLISH]

## ¶6 · 20.14–20.20

> [p. 20] Sabellius eciam si vidisset quod cum unitate nature stat distinccio personarum, sic quoque⁹ non fuisset cecatus¹⁰ in isto turpissimo paralogismo—Petrus¹¹ est natura specifica: Paulus est eadem natura specifica: ergo Petrus est Paulus— vidisset quod non oportet quod Pater sit Filius, quamvis utrumque sit eadem simplicissima substancia. Et sic de aliis heresibus pullulantibus propter defectum logice scripturarum.

[ENGLISH]

## ¶7 · 20.22–21.22

> [p. 20] Multi enim¹² cupiunt autorizare novam logicam extraneam a scriptura et hinc dicunt¹³ se ipsam corrigere tamquam impossibilem¹⁴ de vi vocis. Et illud meminit Augustinus contra dictum Pascencium. Nam¹⁵ contra¹⁵ negantes scripturas de Christo sic loquitur: 'Homines, inquit, minus intelligentes quid propter quid dicaturprecipitesvolunt habere sentencias: et scripturis non diligenter scrutatis arripiunt defensionem¹⁶¹⁷ cuiuscumque¹⁸ opinionis¹⁶ et ab ea vel¹⁹ nunquam vel de difficili deflectuntur, dum docti atque sapientes magis putari quam esse cupiunt. Ea quippe, que propter formam²⁰ servi [p. 21] dicta sunt, volunt transferre ad formam Dei. 'Hoc, inquit, nomen Jesus Christus ex dispensacione misericordie¹ suscepteque² humanitatis assumptum est, quia ipse Filius Dei factus est filius hominis, non mutando quod erat, sed³ assumendo quod non erat.' Et probat diffuse ex scripturis⁴ quod tam Christus quam Spiritus Sanctus⁵ est idem Deus cum Patre et specialiter per illud Apostoli ad Cor. 8. 'Scimus quoniam nullus Deus nisi unus: nam etsi sunt qui dicantur dii⁶ multi et domini multi, nobis tamen unus Deus Pater ex quo omnia et nos in illo: et unus Dominus⁷ Jesus Christus per quem omnia et nos per illum.' Ex isto plane sequitur non protervo quod Christus sit idem Deus cum Patre. Unde dicunt periti scripture quod deus et dominus per se sumptus⁸ dicitur authonomatice de Deo et Domino dominorum. Scio tamen quod protervus potest,⁹ ut hodie, negare quamlibet partem scripture de virtute sermonis, et dicere quod Deus erat verbum nuncupative, et quod per Christum non sunt omnia facta sed omnia citra ipsum, et¹⁰ sic est Deus ac animatus,¹⁰ sed nec Deus deorum nec animatus¹¹ nobiscum univoce. Sed non sic sophisticati sunt eciam heretici, non sic negantes¹² scripturam ut hodie, quia melius fundati in logica et methaphisica quam nostrates.

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 18: *de* (print = bt (de se ait, next line)) [SUB]
  - 19: *Maximinianum* (print = bt (next line)) [BT-ONLY]
  - 19: *verum, sed* (print = bt) [SUB]
  - 19: *summe unum* (print = bt (next line)) [BT-ONLY]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Johnx. 30. (18.17); reference Johnxiv.28.de (18.18); reference Johnx. 30. (18.29); reference ad Cor. 3° (19.18).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 17:
1–1 deus et per consequens homo non solum A B C.
2 deificus *codd. omnes.*
3 hic *om.* A B C.
4 sermonem B; sermo dei factus C.
5 ab B.
6–6 tunc . . . dii *om.* B.
7 salutarii O.
8–8 oportet ergo sermo quo O; oportet ergo quod sermo primo quo A.B.
9 blasfemant C.
10 excidarant B.
11 stat B M.
12 suscipere O M.
13 notissimo A B C.
14 esse *add.* B.
15 Et hoc utrumque esse A C; et hoc utrumque est B.
16 Ephifanius O.
17 Apolinaristis B.

p. 18:
1 katholica C, ut saepe.
2 discesserunt A B C; disserunt O.
3–3 deum christum sine anima carnem suam sumpsisse A B C.
4 verbum in carne A B, verbum carnem fuisse C.
5 eresym B.
6 Ep 21 vel 5 O.
7 heretico. Non puto A B C.
8 formidarem A B C.
9 oportune A B C.
10–10 nostre. Multa de istis A B C.
11 sanctis A C.
12 comemoro O.
13 referuntur O.
14 formam add. O.
15 Restitit B.
16 iste sanctus negare istas istas (sic) scripturas O.
17 persona A B C.
18 concedat O.
19 non om. A B.
20 potest A B C.
21 sint O.

p. 19:
1–1 interior cum corpore nuncupato A B, interior comunia (? *quia*) exterius cum corpore nuncupato C.
2 racionabiliter A B C, racionali O.
3 sunt *add.* B.
4 et communionem *om.* B.
5 dissimiles O.
6 erant A B C; erant . . . unum *om.* O.
7 23° A B C.
8 vel natura *om.* A B C.
9 probatur O.
10 est *add.* O.
11 Joh. 11°. O.
12–12 Non dicit ut et nos unum sumus A B; simus C; sumus O.
13–13 sumus. Sumus enim non solum unum natura quod verum est iam sed et perfecte A B C.
14 iusticia O.
15 sua A B C.
16 quod A B C.
17 esse potuerunt A B C.
18 comparabiliter A B.
19 dubie O.
20 vocant B.
21 signum O.

p. 20:
1 vacaverant vacaverant (sic) O.
2 movet O.
3 in om. O.
4 nam om. A B C.
5 a O.
6 quomodo om. B.
7 una A B C.
8 posset O.
9 quod omnes codd.
10 cecitatus O.
11 Peraloysmo A B.
12 autem A B C.
13 dicunt om. B.
14 impossibile O.
15-15 nam consequenter contra A B C; nam consequenter O.
16-16 defensionem cuiuscunque opinionis om. B; defensionem add. iterum C.
17 defencionem O.
18 oppinionis A.
19 vel om. A B.
20 formam om. B.

p. 21:
1 nunc B; mĩe A C O, i.e. misericordie.
2 suscepte quia A B C.
3 et B.
4 scripture O.
5 sanctus om. A B.
6 sive in celo et in terra siquidem sunt dii add. A B C.
7 deus A B C.
8 sumpti B.
9 posset O.
10_10 ac om. sed in loco habet rasuram duarum litterarum A; et sic . . . animatus om. B.
11 anima O.
12 mutantes A B C.
13 sequentur A B C.
14 puta A B C; pũ O.
15 nedum non A B C.
16 mortuus passus B.
17 consernentibus O.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 17: gaudium, sicut, infirmius, faciliter, purus, racionaliter, suhstancialihus | De Incarnatione
p. 18: De Incarnatione, | {De Sacerdotio) | De Incarnatione | lervantand^hax | in the form of
p. 19: W. cle incarnatione Vbi
p. 21: om. sed in loco habet rasuram duarum litterarum
```

---

## Chunk 02-c: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-02-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-02-c
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "21.23–24.31"
divisions: "cap. 2 (heading 'Cap. II.' at 13.0); part 3 of 4, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "837 words; 833 confirmed by Fordham or the vote; 3 runs stood by rule (both witnesses garbled); 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n60–n63 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 2, part 3: [TITLE]

## ¶1 · 21.23–22.2

> [p. 21] Tercio antem stat opinio Arrii in his que ex predictis erroribus sequuntur¹³: ut puta¹⁴ quod Christus nedum¹⁵ est univoce homo cum aliis sed non est homo simpliciter, cum non potest esse homo si non sit anima intellectiva; et per consequens non est passus¹⁶ mortuus aut sepultus, et sic de quibuscunque predicatis humanitatem Christi concernentibus.¹⁷ Quamvis enim dici possit quod angelus, coniunctus nature corporee tanquam motrix, sit homo; verumtamen est alterius speciei quam totus vel completus homo, id est, [p. 22] natura integra ex corpore et anima composita: homo enim est racione spiritus eiusdem speciei cum angelis et non racione nature corporee.

[ENGLISH]

## ¶2 · 22.3–24.3

> [p. 22] Et per hoc patet quod quidam minus intelligentes Augustinum putant ipsum contradicere sibi ipsi, quando dicit quod anima non completus aut totus¹ homo: nam² verum dicit ad sensum³ expositum. Unde Epistola 40 ad Dardanum solvendo questionem de dicto Salvatoris⁴ Luc. 23 quo⁵ promisit latroni quod foret secum illo die in paradiso; 'antequam, inquit, sciatur utrum secundum deitatem⁶ vel⁷ secundum humanitatem intelligatur promissio Veritatis, oportet videre quomodo sit loquendum de homine. Non, inquit Augustinus, sicut quidam heretici dicunt, Verbum Dei⁸ et carnem sine anima humana⁹ suscepit, sic quod Verbum esset carni pro anima; vel Verbum Dei carnem et animam sine mente, ut Verbum Dei esset anime¹⁰ pro mente. Sed accipis, inquit ad Dardanum, hominem Christum; sicut¹¹ superius aisti quod Christum Deum non crederes nisi perfectum hominem credidisses. Profecto, inquit, cum dicis hominem, perfectam totam illic naturam humanam vis intelligere. Non est¹² autem homo perfectus si vel anima carni vel anime ipsi mens¹³ humana defuerit.'¹⁴ Et illam naturam complete ex anima et corpore compositam vocat super Joh. Ome. 47¹⁵ totum hominem: quam¹⁶ notum est ex dictis De Anima distingui tam a corpore quam anima¹⁷ licet omnia ista tria sint eadem persona hominis. Sic ergo¹⁸ intelligendus est Augustinus quandocunque videtur dicere quod corpus vel anima non est homo; id est, non est¹⁹ tota vel completa natura ex corpore et anima composita. Sed pro solucione Dardani questionis videtur Augustino catholicum quod promissio facta latroni intelligatur secundum [p. 23] humanitatem Christi:¹ sed cum corpus Christi¹ sepultum sit solum in orto, ut patet Ioh. 19,² relinquitur quod sue anime in parasceue erant simul; quia modicum felicitatis fuisset animam latronis fuisse cum solo corpore Christi mortuo in sepulcro. Et cum vera mors fuit in Christi corpore, cum aliter non fuisset vera resurreccio; querendum est—quo devenit anima³ Christi in illo triduo? Quod cum evangelium non reserat, supplet⁴ beatus Petrus Actuum 2° probans ex illo Psalmi 15 dicto de Christo ‘quoniam non⁵ derelinques animam meam in inferno, nec dabis sanctum tuum videre corrupcionem,’ quod anima Christi descendit in illo triduo ad limbum patrum, quem Veritas Luc. 16. vocat ‘sinum Abrahe,’ ubi patres veteris testamenti feliciter quieverunt.⁶ Quamvis enim dictum psalmiste sit negativum, impertinenter tamen menti prophetice diceretur, nisi intenderet Messiam secundum mentem visitare inferos et statim sine media incarceracione corpori reuniri.⁶ Et hinc fundatus est de Christo articulus fidei, quod ‘descendit ad inferos.’ Cum ergo paradisus generale nomen est ubicunque feliciter⁷ vivitur, quid obest animam latronis fuisse cum anima Christi in regione quiescencium congaudendo et non in regione inferiori dolencium,⁸ inter quas est ‘magnum chaos’ secundum veritatem evangelicam interceptum?⁹ Redeundo¹⁰ ergo ad propositum patet ex dictis quantum differt ista posicio ab heresi Arriana. Ideo est michi verisimile quod doctores moderni¹¹ cum non ydemptificarent que minus intelligunt,¹² locuntur michi temptative, yronice, vel iocose. Yronice quidem, quia Arrius negavit Verbum Dei esse idem substancialiter Deo Patri, sed creatum esse secundum supremam substanciam, que est Christus. Ego autem dico [p. 24] quod Christus absolute necessario¹ est eadem deitas que est Pater,² nec posse secundum supremam naturam, que est Christus, creari vel fieri.

[ENGLISH]

## ¶3 · 24.4–24.8

> [p. 24] 2° autem dixit Arrius quod Christus non habet animam sed pure carnem; spiritu illo creato³ supplente vicem anime non ypostatice, sed ut motrice, corpori copulato. Ego autem dico quod Christus nedum habet animam, sed est anima, nec posset⁴ carni nisi mediante anima ypostatice copulari.

[ENGLISH]

## ¶4 · 24.9–24.13

> [p. 24] 3° ubi posuit⁵ Christum non esse hominem nisi equivoce, nec proprie passum⁶ esse, mortuum, et sic de aliis que fides evangelica de Christo predicat. Ego autem⁷ dico Christum esse⁸ verissime, completissime, et univoce hominem cum quolibet fratre suo; et vere de virtute sermonis conversatum esse in terris, ut canit processus evangelicus.

[ENGLISH]

## ¶5 · 24.14–24.21

> [p. 24] Et sic, ubi Arrius peccavit in deitate Christi negando eum verum Deum⁹ eundem cum Patre; ubi eciam peccavit in humanitate Christi negando ipsum esse verum hominem; ego utrumque¹⁰ pleno corde confiteor non confundendo naturas nec¹¹ distinguendo personas in Christo. Et patet quod non, quia dixit Christum esse creaturam, censetur hereticus¹²; sed, quia dixit Christum esse puram¹³ creaturam meliorem homine; et non hominem passum abiectum et ab hominibus reprobatum.

[ENGLISH]

## ¶6 · 24.22–24.31

> [p. 24] Et utinam nostri loquentes attenderent ad regulam Augustini ‘quid propter quid de Christo dicitur,’ allegando complete scripturam vel determinaciones ecclesie non truncate. Ut primo libro contra Maximinianum ca° 11. ‘Audi, inquit, Maximiniane, auctoritatem synodice¹⁴ locucionis: Si quis ex nichilo Filium dicit non ex Deo Patre, anathema sit.’ Quis ergo color, si dico—Christus est creatura—sed et Arrius dixit Christum esse creaturam, quod coincido in heresim Arrianam? Vere non plus quam sequitur, si uterque nostrum dicat Christum esse aliquid¹⁵ sive Deum.

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 21: *antem* (plate: print = antem (Harris misprint for autem); the Latin keeps the print, the English notes it (Opus coordinator)) [AGREE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Acts u. 31. xvi- 10- . . . . . Ps- (23.8); reference Luke xvi. 22, 26. (23.12).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 21:
1 nunc B; mĩe A C O, i.e. misericordie.
2 suscepte quia A B C.
3 et B.
4 scripture O.
5 sanctus om. A B.
6 sive in celo et in terra siquidem sunt dii add. A B C.
7 deus A B C.
8 sumpti B.
9 posset O.
10_10 ac om. sed in loco habet rasuram duarum litterarum A; et sic . . . animatus om. B.
11 anima O.
12 mutantes A B C.
13 sequentur A B C.
14 puta A B C; pũ O.
15 nedum non A B C.
16 mortuus passus B.
17 consernentibus O.

p. 22:
1 totus aut completus O.
2 non O.
3 sermonem A B C.
4 salvatore O.
5 quo̅ = quomodo A C.
6 divinitatem O.
7 aut B.
8 dc͠a O.
9 humana *om.* A B C.
10 anima C.
11 sicud A B C.
12 est *om.* O.
13 meus O.
14 deseruit O.
15 40 A B C.
16 quanquam O.
17 anima *om.* O.
18 igitur A C.
19 non est *in margine* C.

p. 23:
1 sed . . . Christi *om.* O.
2 29 O.
3 deveniet Christi B, *om.* anima.
4 suplet O.
5 non *om.* O.
6–6 quamvis enim dictum psalmiste sit negatum impertinenter tamen diceretur menti prophetice nisi intenderet Messiam visitare inferos ac statim sine mera incarnacione corpori uniri A B C. *Cod.* O. *habet* quam enim dictum . . . incineracione corporis veniri; *cetera ut supra in textu.*
7 bene B.
8 dolencium *om.* A B C.
9 interceptum *codd. omn. Qu. interseptum?*
10 respondendo A.
11 mei B C *om.* O.
12 intelligunt minus O.

p. 24:
1 intus O.
2 eadem deitas cum patre B.
3 increato M A; creato B C O.
4 potest A; oportet C.
5 ut possuit B.
6 proprie ~~posse~~ esse (*sic*) A; tibi posset esse B; posset esse C.
7 autem *om.* A B O.
8 ipsum esse A C; esse *om.* B.
9 verbum domini A B C.
10 utraque B.
11 non B.
12 esse Christum censetur creaturam hereticus B.
13 pure O.
14 sinodice O, *ut saepe post.*
15 aliud C.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 21: om. sed in loco habet rasuram duarum litterarum
p. 22: De Anima | Ue Anima
p. 23: chv\eVs | cetera ut supra in textu.
```

---

## Chunk 02-d: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-02-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-02-d
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "25.1–28.15"
divisions: "cap. 2 (heading 'Cap. II.' at 13.0); part 4 of 4, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "910 words; 909 confirmed by Fordham or the vote; 1 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n64–n67 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 2, part 4: [TITLE]

## ¶1 · 25.1–26.3

> [p. 25] Sed obicitur quod dico horribilius Arrianis, quia ipsi dixerunt Christum esse primam et optimam creaturam; ego autem dico Christum esse materiam primam, et sic¹ abiectissimam creaturam. Hic dicitur quod non sequitur. Nam Christus est optimus homo possibilis, inter omnes creaturas particulares optima, in tantum quod est melior angelo²; et per consequens melior² illa creatura, si esset, quam³ finxit Arrius nimis stolide esse⁴ primam creaturam Dei, mediante qua⁵ Deus creavit Spiritum Sanctum et consequenter alias creaturas. Nam illa creatura non foret melior creato angelo: de Christo autem dicit Apostolus ad Hebr. 1° quod ‘est tanto melior angelis effectus quanto differencius pre illis nomen hereditavit.’ Et si obicitur per illud Ps. 8⁶ dictum de Christo ad litteram⁷ ‘minuisti eum paulo minus ab angelis’; dicitur quod Christus, sicut est natura increata et natura creata, sic secundum naturam creatam est simul⁸ tam natura corporea quam natura incorporea;⁹ secundum autem naturam corpoream⁹ est ‘paululum minoratus ab angelis,’ sicut¹⁰ sentenciat satis¹¹ psalmus; et secundum creatum spiritum per graciam unionis angelos¹² antecellit. Conceditur tamen¹³ quod abiectissima creatura que est Christus Deus, licet sit natura inferior quam angelus vel anima humana, est tamen optima et suprema persona possibilis: cum omnis natura que est filius¹⁴ Marie virginis hominis¹⁵ est et¹⁶ Filius Dei; et e contra omnis natura, que est Filius¹⁴ Dei, est filius hominis; quia natura divina est filius hominis, ut patet ex confessione beati Petri Mat. 16. querente Veritate, ‘Quem dicunt¹⁷ homines esse filium hominis?’ et respondente Petro de eadem humanitate que est Christus, de qua fit questio. ‘Tu es, inquit, Filius Dei vivi,’ intelligens indubie filium naturalem. Unde Veritas [p. 26] approbando responsionem¹ adiunxit premium, et monet eum:² ‘Beatus es, inquit, Symon Bariona, quia caro et sanguis non revelavit tibi, sed Pater meus.’

[ENGLISH]

## ¶2 · 26.4–28.15

> [p. 26] Et per hoc destruitur heresis Nestoriana arguens ex diversitate naturarum in Christo quod sit diversitas personarum. Nesciunt enim quomodo humanitas assumpta et natura divina tam dispares sunt utraque³ eadem persona cum Verbo Dei, ut ostendit Anselmus de Incarnacione Verbi cap. 6.⁴ et sic posuit alium esse filium hominis et alium Filium Dei; sicut aliud est filius hominis et aliud Filius Dei; sicut dicit superius Augustinus. Et patet quantum differt ista posicio ab heresi Arriana et Nestoriana, cum quibus videretur minus intelligentibus maxime concordare. Et si obicitur quod non tollitur, quin Christus sit creatura⁵ et abiectissima, quod⁵ non posuit Arrius; concedo conclusionem. Unde inter alia, que accenderent⁶ virtutes theologicas in nobis⁷ viantibus, maxime videtur mihi debere gignere⁸ illa summa minoracio, illa summa exinanicio, illa summa⁹ obediencia vel humiliacio qua¹⁰ Verbum, manens substancialiter complete et eternaliter quod erat, assumpsit ypostatice quod prius non erat. ‘Nusquam¹¹ enim angelos apprehendit’ secundum Apostolum ad Hebr. 2°. sicut ficte garriunt Arriani; sed ‘semen Abrahe’¹² tam secundum naturam corruptibilem quam secundum¹³ naturam immortalem ‘ut fieret per omnia fratribus similis’: dicente Apostolo ubi supra, ‘non confunditur¹⁴ fratres eos vocare, dicens “narrabo nomen tuum fratribus meis”’: et sequitur ‘nusquam enim angelos apprehendit, sed semen Abrahe apprehendit: unde debuit per omnia fratribus similari, ut misericors fieret et fidelis pontifex ad Deum.’ Ex quo textu patet quod fides nostra viresceret ex hoc quod naturam nostram fragilem non pure angelicam dignatur [p. 27] suscipere. 2° cum non¹ potest frustrari, patet quod ex assumpcione nostre nature, quos vocat¹ fratres suos passus et temptatus² ad nobis auxiliandum, invalesceret spes³ humana. Et 3° visa humiliacione qua Dei Patris primogenitus naturalis dignatus est naturam nostram fragilem et abiectam assumere fortificaretur caritas ad ipsum et fratres suos in ipso⁴ carius diligendum. Non ergo iniuriatur nobis nec debet vilescere quod nos sic univit, non angelos; nec ab honore Patris degenerat, nec⁵ fundatur in ipso⁶ remissior nobis diligendi racio.⁷ Sed per omnia e converso. Unde Ioh. 14. vere dicit, ‘si diligeretis me, gauderetis utique quia vado ad Patrem.’ Pro cuius declaracione suppono: primo quod Christus, hoc dicens⁸ secundum humanitatem assumptam,⁹ sit eiusdem nature nobiscum. 2° suppono¹⁰ quod apostoli, quibus locutus est et alii sermones eius servantes sint nedum servi Domini sed amici. Patet per¹¹ illud Ioh. 15¹² ‘Vos amici mei estis si feceritis que precipio vobis: iam non dicam vos servos etc.’ 3° suppono quod de racione amicicie sit, cum amicus sit alter ipse, congratulari de prosperis coamici, specialiter si exinde¹³ speratur amicicie fructus uberior. Patet per Aristotelem 8 Ethic 5.¹⁴ Ex istis sic arguitur. Quilibet amicus debet gaudere de eventu prospero coamici amiciciam confirmante; sed Christo amico apostolorum ascendente in celum et collocato a dextra¹⁵ Dei Patris advenit summa felicitas: ergo de eius transitu fuit apostolis congaudendum.¹⁶ Et hinc dicit apostolus ad Hebr. 7 ‘quod¹⁷ Iesus accedit per semet ipsum ad Deum, semper vivens ad interpellandum pro nobis.’ Cui conformiter scribitur prima¹⁸ Ioh. 2° ‘sed et si quis peccaverit¹⁹ advocatum habemus apud²⁰ Patrem, Iesum Christum.’ Unde Augustinus super illo textu Omelia 78 sic scribit: ‘humane nature congratulandum [p. 28] est eo, quod assumpta est a Verbo ut immortalis¹ constitueretur in celo, atque ita fieret² terra sublimis, ut³ incorruptibilis pulvis⁴ sedeat ad dextram Patris; et sic Christum ire ad Patrem et recedere a nobis est mortale, quod ex nobis suscepit, levare in celum⁵ et facere immortale. Quis ergo non hinc gaudeat ut et suam naturam iam immortalem gratuletur in Christo, ac⁶ illud se speret esse futurum per Christum? Nec dubito, quin omnes moderni scholastici nescirent impugnare istas logicas de vi vocis. Et sic intelligit Jeronimus et alii rectiloqui quod tota spes et consolacio nostra est in summa humiliacione Christi, qua naturam nostram assumendo et nobis exemplum conversacionis tribuendo fecit se non angelum vel naturam alienam ab homine, sicut fabulantur heretici, sed verissime et univoce fratrem nostrum, ut post⁷ declarabitur.

[ENGLISH]

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference Hebr. 1° (25.12); reference illud Ps. 8 (25.14); reference Matt. xvi. 13, 16. (25.28); reference Matt. xvi. 17. (26.2); reference and Augustine show. (26.11); reference Heb. ii. 11, 12. (26.25); reference Thus, as Augustine says, ' (28.1); reference 1 Cor. xv. 53. (28.4).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 25:
1 sic *om.* A B C.
2 angelo . . . melior *om.* O.
3 qm̃ A B O.
4 esset A B C.
5 quam B.
6 dictum 8 *om.* A B C.
7 ad litteram *om.* B.
8 filius B.
9–9 secundum . . . corpoream *om.* O.
10 sicut *om.* O.
11 sacer O.
12 angelos *om.* A.
13 tamen *om.* C.
14–14 Marie . . . filius *om.* B.
15 virginis *om.* O M; *forsitan aut* virginis *aut* hominis *omittendum.*
16 et *om.* A.
17 ducunt O.

p. 26:
1 confirmando questionem B.
2 et monentem codd. omn.
3 utrumque O.
4 6. codd. omn.
5 est abiectissima quomodo A B C.
6 attenderent A B C.
7 nube A B C.
8 ginguere O.
9 sublima A B; om. C. cum lacuna.
10 quia A C; quam B.
11 nunquam O; nusquam A B C ut in Vulg.
12 habrahe O.
13 secundum om. O.
14 confundetur O; confunditur A B C ut in Vulg.
CHECK: the main-text list gives figure 5 twice, but the foot has only one entry for 5.

p. 27:
1–1 potest . . . vocat *om.* O.
2 temperatus O.
3 species B C O; spes *cum rasura supra* A.
4 in ipso *om.* C.
5 vel O.
6 in nobis A B C.
7 pō (*potencia*) O.
8 hic docens O.
9 assumptam *om.* A B C.
10 supponantur O.
11 per *om.* A B C.
12 *lacuna in loco numeri* C.
13 inde B.
14 11° A B C.
15 dextris A B C.
16 con- *om.* A B C.
17 hebre qui O; 7 *om.*
18 scribitur prima *om.* O.
19 peciaverit O.
20 aput A B.

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
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 28: \_Ostendit quod Christus fuit homo in triduo, et obicit multipliciter et dissolvit, Chrisfs humanity was not suspended during the three days' entombment.'] | littera mitia/is om. ut fere semper
```
