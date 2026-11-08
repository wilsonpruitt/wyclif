# Translation brief: eucharistia 06-c–06-e

You translate these 3 chunk(s) of Wyclif's *Tractatus de eucharistia* in a single pass. Everything you need is in this file:
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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/eucharistia/wyc-eucharistia-06-c.md chunks/eucharistia/wyc-eucharistia-06-d.md chunks/eucharistia/wyc-eucharistia-06-e.md` once and fix what it reports.
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

# TRANSLATOR CARD — one *De eucharistia* chunk

This card replaces reading CONVENTIONS, the pilot and Thakkar in full: it is their working core.
Adapted from `chunks/potestate-pape/CARD.md` (Loserth's other volume) with the B+ lessons of
`chunks/incarnacione/CARD.md` (2026-11-06; **reviewed 2026-11-06** on `prol-a`: `_review/REVIEW-prol-a.md`). Read it, then `GLOSSARY.md`,
then your scaffold (or your brief, which carries all three). Consult CONVENTIONS.md only when the card sends
you there. Work in `~/wyclif`. Wyclif is approached with **daggers drawn**: the most recent English
versions were "worse than useless" because of four error classes (below). Your English must survive
a hostile reader with the Latin open.

## Work lean (cost is per tool call: each call re-sends your whole context)

1. One call reading what you need (the brief, or CARD + GLOSSARY + scaffold).
2. **One** `bible.py` call with every scripture reference you need (it takes many refs).
3. Plates **only** for a Latin doubt the print plus apparatus cannot settle.
4. Write each finished chunk in **one** Write of the whole file (Latin blocks copied unchanged).
5. Lint once; fix; done. Draft in your head, not in the file.

## The volume

*Tractatus de eucharistia* and *Tractatus de penitencia sive de confessione*, ed. Johann Loserth (Wyclif
Society, 1892), from the plates of archive.org `latinworks13wycl` (**leaf = page + 71**; leaf images in
`text/eucharistia/raw/leaves/`). Three texts:

Chunk ids: `prol-a … prol-c` the compendium, `01-a … 09-n` the nine chapters, `pen01 … pen06` *De
penitencia*, `quest` the *Questio*.

- **pp. 1–10, the compendium** (*Sentencia tractatus de Eukaristia in compendio*, under "Prologus"): a
  medieval summary of the nine chapters that came down with the work. Translate it like the text.
- **pp. 11–326, the *Tractatus de eucharistia* (maior)**, nine long chapters. Written in Wyclif's last
  years, before 1382–83 (Loserth, Introd. §4: it shares passages word for word with *Sermones* III, and
  it avoids the words *substancia* and *materialis* of the bread, which Wyclif says in *Sermo* III.54 he
  has stopped using). Wyclif's case against the "modern" doctrine: that the consecrated host is in its
  nature bread and wine and sacramentally, figuratively, the body and blood of Christ; that an accident
  without a subject is impossible; that the decree *Ego Berengarius* (*De cons.* D. 2 c. 42) is the
  faith of the ancient Roman church; against the friars, Thomas, Scotus and "the sect of the signs".
  A **treatise**: Wyclif speaks in the first person, states conclusions, raises objections and answers
  them. The tractatus minor (the *Confessio*) is NOT in this volume (Shirley, *Fasc. Ziz.*).
- **pp. 327–348, *De eucharistia et penitencia sive de confessione*** in six chapters (only ch. 1 is on
  the eucharist; the rest is penance and auricular confession), then the short ***Questio ad fratres de
  sacramento altaris*** (pp. 347–348, its first part only: Loserth notes that the rest of the
  manuscript's text is not on the sacrament, and is Hus's).

**Sigla. ⚠ They differ between the two works.** *De eucharistia* (Introd. §5): **A** Vienna 3927;
**B** Vienna 3932; **C** Vienna 1387 ("the best of the three" Vienna MSS, correcting A and B); **D** Prague
Univ. IV D 22 (1404–05, Andreas of Kouřim); **E** Prague Univ. XI E 3 (1460; Loserth: "the best and most
reliable text of all the five"). Loserth's lettering "does not in any way refer to their respective
value". The Vienna MSS are one group, the Prague MSS another. *De penitencia* (Introd. §6): **A** Vienna
3927; **B** Bautzen, Gersdorf Library M. St. 80.7; **C** Vienna 1337; **D** Prague Univ. III G 11; **E**
Vienna 3980; **F** Vienna 4527. Cite variants with the sigla of the work you are in. Marginal notes in the
manuscripts that Loserth prints ("F in marg.", "DB in marg.") are reception: an **R** note where they
show how a reader took the text.

**The page foot** (in your brief as "apparatus", by page) has two blocks, both keyed to the **line**:
the variants (`19. C: ecclesie in marg. alia manu.`) and Loserth's source references. The OCR of it is
rough: read it for sense, not letter by letter, and read the plate foot where a variant matters.

## The job

The Latin in your scaffold is **established and frozen** (blind transcription of the plates, checked word
by word against a four-scan vote; residue read on the plate). Fill `[TITLE]` (short, lower case: "the
three opinions on the quiddity of the host"), each `[ENGLISH]`, the notes and the transcription notes;
set `status: translated`; lint; report.

- **Headings:** keep `## ¶k · range` exactly. **Never change a range; never split a paragraph.**
- **Never alter the Latin.** A transcription error you find (a stray mark, a broken word, a side-note
  word in the text) is REPORTED, never repaired in your file: the coordinator repairs the transcription
  (`text/eucharistia/bt/pNNN.txt`) and refreshes the chunk's Latin. A word that looks wrong: read the
  apparatus for that line first; then, if still doubtful, the plate (`text/eucharistia/raw/leaves/nLEAF.jpg`,
  LEAF = page + 71 padded to four digits: p. 1 = `n0072.jpg`). A variant that gives the sense → translate
  it + **T** note citing the siglum; a compelling emendation → translate it + **T** note "(our
  emendation)"; neither → translate the print and flag it. Never smooth nonsense into sense. Report every
  such case. **Loserth's printed text governs** (ruled 2026-10-02 for Loserth's volumes; the
  manuscripts-outrank-the-print rule is Harris's volumes only): translate it, his own emendations
  included, unless it will not construe; a manuscript reading is chosen only then, or where the source
  Wyclif quotes, read this session, agrees with it. Every departure gets a T note giving both readings.
- **The compendia (`prol-a … prol-c`) summarise chapters whose Latin is already established** in this
  directory. Where the compendium's ellipsis leaves a construal open (whose argument, which *per* phrase is a
  ground and which a means), grep the chapter's `>` blocks, follow them, and cite the page in the **C** note:
  that is construal, not source verification, and one call. (`prol-a` 2.1–5: the three decrees are the
  objections' grounds, ch. 1 pp. 24, 25, 28.)
- **English layout:** `[N]` at the same word as `[p. N]` in the Latin (the chunk's first `[p. N]` is
  implicit). Supplied words in `[brackets]`, sparingly, ⛔ never in italics. **Quotations** in quotation
  marks. Your brief carries Loserth's **italic runs** per page where the scan's OCR gives them (rough;
  ⚠ page numbers drift: a run not in your page's Latin belongs to a neighbouring page): they are
  the editor's judgement of where a quotation runs, not the manuscript's: follow them by default, depart
  where the source shows otherwise (say so in a note). Reviews do not check quotation bounds against the
  italics. Italicised scripture inside indirect speech is quoted too; where quoting would garble the
  sentence, leave it unquoted and give the reference in an **S** note.
- **Ordinals:** a degree-sign ordinal can print or OCR like a two-digit number (*30 et 10* = 3° and 1°).
  Read both forms the same way, and check the plate when a citation looks impossible.
- **Formulae of the disputation** (ruled 2026-10-01; fixed renderings, tagged only where GLOSSARY has a
  row): *instatur* "it is objected" · *obicitur* "it is objected" · *arguitur* "it is argued" (with
  *per*: GLOSSARY) · *dicitur* "it is said" (in an answer: "the answer is") · *respondetur* "the reply is"
  · *conclusio* "conclusion" · *antecedens / consequens* "antecedent / consequent" · *consequencia*
  "inference", ⛔ never "consequence" · *patet* "it is clear" · *supponitur* "it is supposed" ·
  *probatur* "proof:" or "it is proved" · *confirmatur* "this is confirmed" · *solvit / dissolvit* (an objection) "resolves", both (never "answers", which belongs to *respondetur / dicitur*).
- **A source note says only what the Latin says about the source** (who narrates, which book, which work)
  and leaves the rest to the ledger: never supply a story the Latin rules out (*narratum a beato Gregorio*:
  Gregory narrates).
- **Citation formulae:** *ubi supra* "in the place cited above" (⛔ never a claim about where a passage
  stands), *ut supra* "as above", *infra* "below". *Utrobique* "on both sides / in both places".

## The four error classes (Thakkar) — check every sentence

1. **Terms:** GLOSSARY.md governs, one term one rendering. Tag the **first occurrence in the chunk** of
   every §A–C term: `[accident]{g:accidens}`; a multi-word key is lower case with hyphens, `{g:corpus-christi}`, `{g:a-simili}` (lint rejects spaces); never nest brackets inside a tag (`[form [sounds] with]{g:k}` breaks the site): tag the bare word. The key must exist in GLOSSARY.md. A term that looks
   technical but has no row: render it sensibly, untagged, and propose it in your report.
   **CONTEXTUAL** rows hold two senses English splits: choose by context and write a **C** note at the
   first occurrence in the chunk and wherever it leans to the other sense (the dikaiosune rule,
   CONVENTIONS §6).
   Rows that already exist and bear on this volume: *accidens* "accident" · *accidens absolutum*
   "absolute accident" · *transsubstanciacio* "transubstantiation" · *conficere* "consecrate (the
   eucharist)" · *figura / figuratum* "figure / thing figured" · *res sacramenti* "reality of the
   sacrament" · *sacramentalia* "sacramentals" · *quantus* "quantified" · *per se / per accidens* "of
   itself / by accident" · *sensibile commune* "common sensible" · *ecclesia* church (**lower-case**) ·
   *caritas* charity · *sentencia* teaching (and *sentencia verborum* "sense", a separate row) · *ex fide* as faith teaches ·
   *opinio* opinion · *novelli* the newer [doctors] · *sancti* the saints · *concludere* infer ("conclude" only where a
   conclusion is literally drawn) · *deduccio* deduction · *maneries* kind · *principaliter* as a main head ·
   *sensibilis* perceptible · *declarare / ostendere* make clear / show · *ecclesia* is tagged at its first
   occurrence in every chunk.
   **This volume's vocabulary is now ruled (2026-11-06, `prol-a` review):** *sacramentum* (the eucharist) ·
   *hostia* host · *panis / vinum* bread / wine · *calix* chalice · *corpus Christi / Domini* kept apart ·
   *remanencia* the remaining · *accidens sine subiecto* · *substancia · quantitas · qualitas* · *esse /
   esse sacramentale* being / sacramental being · *esus / manducacio* eating · *confeccio* consecration ·
   *secta signorum* · *novella / antiqua ecclesia* · *predicacio ydemptica / tropica* identical / tropical
   predication. **The mode adverbs, one word each, never merged, each tagged at first occurrence:**
   *sacramentaliter* sacramentally · *realiter* really (never "actually") · *vere* truly (never "really") ·
   *spiritualiter* spiritually · *virtualiter* virtually · *figurative* figuratively · *tropice* tropically ·
   *ydemptice* identically · *invisibiliter* invisibly · *sensibiliter* perceptibly · *corporaliter* bodily ·
   *substancialiter* substantially · *dimensionaliter* dimensionally. A term still missing a row (*ydemptificacio*,
   *conversio*, *fractio*, *confessio auricularis*, *absolucio*, *claves* …): render it sensibly, untagged, and
   propose it. *Ego Berengarius* stays as the decree's title (Wyclif's spelling *Beringarius* in the Latin;
   "Berengar" for the man in the English). In ch. 1, *res sacramenti* "reality of the sacrament" is a ruled
   row: the compendium's *de rebus huius sacramenti* (1.3) is the three-membered distinction the chapter sets
   out, so keep its *res* consistent with that row.
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
   it is "now".
3. **Ordinary words with a medieval sense:** GLOSSARY §D; look up any word whose classical and
   Wyclifite senses may differ, and propose additions.
4. **Syntax:** construe before rendering (main verb, subject, what every relative and genitive hangs
   on). Keep quantifier order where it is meaning. Keep Wyclif's long periods where English tolerates
   them. **A doubtful construal is never chosen silently:** translate the likelier reading and write a
   **C** note giving the alternative.
   ⚠ **Predication is the matter here, as in *De incarnacione*.** *Hoc est corpus meum*, *panis est
   corpus Christi*, *hoc sacramentum est panis*: Wyclif argues about what the pronoun demonstrates and
   in what mode the predicate holds. Keep subject and predicate in his order, keep *est* as "is" (never
   "exists", "becomes" or "represents" unless the Latin says so), and keep the mode adverb where he puts
   it (*est sacramentaliter corpus Christi* "is sacramentally the body of Christ"). ⛔ Never soften "is"
   into "signifies" or harden "figuratively" into "really": the difference is the treatise's matter.
   Demonstrative pronouns (*hoc*, *istud*) under discussion: render "this", and keep their gender
   visible in a C note where the argument turns on it (*hoc* neuter against *hic*, 348).
   **Propositions in indirect speech** whose sense is under discussion: render as the quoted proposition
   ("who say 'this is an accident without a subject'"), not "who say that …", which asserts it.

## Scripture

`python3 scripts/w3/bible.py "I Cor 10:16"` (Vulgate + Douay–Rheims; psalms in Vulgate numbering) or
`python3 scripts/w3/bible.py --find "panis quem frangimus"`. Where Wyclif's Latin agrees with the
Clementine Vulgate, use the **Douay–Rheims wording**. Where he departs, translate *his* Latin and write
an **S** note giving the Vulgate. Modern references in the English (1 Cor. 10:16). The chapter numbers
are Wyclif's, the verse numbers Loserth's (the headnote says so once).

## Notes

- `[^n]` from 1, the marker placed in the same edit as its note, each opening with a type letter **with a
  full stop** (`**C.**`; the site strips only that form): **T** text · **C** construal · **G** glossary
  (passage-specific only; otherwise a tag) · **S** source · **R** reception/context (a manuscript's
  marginal note Loserth prints; Hus's or the Hussites' reuse where Loserth notes it). A note that does two
  jobs takes the combined code (`**S/T.**`, `**C/S.**`; lint accepts it). The first occurrence of a CONTEXTUAL
  row in each chunk (*sentencia*, *inconveniens*) always gets its **C** note.
- **Density: about one note per 70–100 Latin words**, fewer where the text is plain. Short, factual,
  says what the Latin does and stops. No modern theology, no evaluation, ⛔ no judgement on whose
  eucharistic doctrine is right.
- **Every identification** other than scripture checked with bible.py gets a ledger row in your report
  with a status: `editor` (Loserth's source reference at the page foot), `to-verify` (from memory: every
  patristic, scholastic or canon-law identification you did not read in this session), `verified` (you
  read the source text this session: say where; local PL at `~/patrologia/sources/pl/tei/`). ⛔ Never
  pass memory off as verified. Id `K<chunk>-<n>` (`K01a-1`; ⚠ `K`, since `E` is *De ecclesia*, `P`
  *De potestate pape*, `I` *De incarnacione*), cited in the note: "(LEDGER K01a-1)". Loserth's references
  to the *Corpus iuris canonici* are `editor`; give them in modern form (*De cons.* D. 2 c. 42) and say
  the form is ours. Expect above all: Gratian *De consecratione* D. 2 (*Ego Berengarius*, c. 42;
  Augustine and Ambrose there), Augustine (*In Ioh.*, *De civ. Dei*, sermons), Ambrose *De sacramentis*
  and *De mysteriis*, Hilary, Jerome, Bernard, Thomas (*ST* III qq. 73–83; *In IV Sent.*), Scotus,
  the Lombard *Sent.* IV d. 8–13, Grosseteste.

## Model of register

`pilots/wyc-ecclesia-01a.md` (De ecclesia pp. 1–5) is a reviewed model of register and note style: read
it for that only (it predates some GLOSSARY rulings; **GLOSSARY governs**). **The first chunk, `prol-a`** (the compendium), carries
the `## Headnote` for the whole volume; `pen01` carries a short headnote for *De penitencia* and `quest` one for the
*Questio* (date, sigla, Loserth's remarks on the text). The headnote ⛔ is **not** the card's thesis paragraph: "The move" is how the compendium *builds* the case, chapter by chapter, and names no adversary the chunk does not name; the date is given as Loserth's evidence plus the modern dating, each `[verify]`. The headnote (CONVENTIONS §12 order: occasion, text, the work's move, where it is answered; date,
editor, the two works and their sigla, the compendium, the *Questio*), each unverified claim marked
`[verify]`.

## Transcription notes

The variant list is either complete against the page-foot apparatus or headed "selected"; none that affects the
English may be left out. Plate readings and fixes to the Latin (stray stops that were ink flecks) are recorded
there.

## Side-notes

Already read against the plates (WORKFLOW 5, `text/eucharistia/sidenotes.fixed.tsv`) and placed in your
scaffold's section. ⛔ Do not edit them. One that is plainly wrong (garbled, or at the wrong line):
report it under Latin doubts as `side-note page.line`.

## Finish

1. `status: translated` in the front matter (nothing else changes there).
2. `.venv/bin/python scripts/w3/lint.py chunks/eucharistia/<your chunk>.md` until clean.
3. The four-class check above, sentence by sentence.
4. ⛔ Edit **only your chunk(s)**. No git, no other files. Everything shared goes in your report.

## Report (≤ 200 words per chunk, exactly these heads)

- **Chunk:** id, Latin words, notes.
- **Ledger rows:** in LEDGER.md's table format `| id | chunk / note | claim | status | how / next step |`.
- **Glossary proposals:** Latin · proposed English · where · why.
- **Latin doubts:** page.line · printed · suspicion · settled on the plate?

## Glossary (the 535 rows these chunks use; the full file is GLOSSARY.md)

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
| presciencia | foreknowledge | |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| apocrifa; apocrifus | apocrypha; apocryphal | Wyclif applies it to the saints' chronicles as well as to books outside the canon. Ruled 2026-09-28 (6 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| elemosinans | almsgiver | The participle of *elemosinare*: the donor. Ruled 2026-10-02 (*Eccl.* 13). |
| sacramentum (the eucharist); sacramentum altaris | sacrament; the sacrament of the altar | The plain sense, against the Augustinian row (*Incarn.*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.3, 3.30). |
| hostia; hostia consecrata | host; consecrated host | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.11, 1.22). |
| panis / vinum | bread / wine | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.8). |
| corpus Christi / corpus Domini | the body of Christ / the body of the Lord | Kept apart as the Latin alternates them. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.6, 1.10). |
| novella ecclesia / antiqua ecclesia | the newer church / the ancient church | The pair of 3.3; cf. *novelli*. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 3.3). |
| cultores accidencium / signorum | worshippers of accidents / of signs | Wyclif's name for the defenders of the accident without a subject. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 6.15, prol-c 10.2). |
| missantes | mass-priests | Priests hired to say masses; pejorative. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 15.25). |
| species (of bread and wine) | species | The sacramental species; kept as the term, not "appearance". Distinct from the logical *species*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 13.15; 23.8). |
| sacer; sacrare | sacred; hallow | Kept apart from *sanctus / sanctificare* "holy / sanctify" and from *consecrare*; *consecrare* is "to hallow together" in the grammarians' etymology. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 27–28). |
| sacramentum tantum | a sacrament only | The *sacramentum tantum* of the Lombard's three (IV d. 8 c. 4). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 29.23). |
| peregrinacio | pilgrimage | The church's way to the *patria*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 36.9). |
| canoniste | canonists | Beside *decretiste* "decretists". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 41.3). |
| conversio (eucharistic) | conversion | Of bread into the body; kept apart from *conversio* of a proposition. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 48.15). |
| decretalis | decretal | Kept apart from *decretum* "decree". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 71.31). |
| principaliter; principalitas (of the body's presence) | principally; principality | Of the body of Christ alone being in the sacrament as its principal; not the compendium's *principaliter* "as a main head". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 75.5–26). |
| transaccidentacio | transaccidentation | Wyclif's coinage beside *transsubstanciacio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 81.27). |
| transinferioracio; transsubieccio | transinferioration; transsubjection | Coinages in the same series. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 82.3). |
| baptiste signorum | baptizers of the signs | Not "Baptists". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 81.29). |
| divinitus | divinely | The pair of *humanitus* "humanly". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 84.19). |
| dies artificialis | the artificial day | Sunrise to sunset, against the natural day. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 95.2). |
| consecracio | consecration | The noun of *consecrare*; see *confeccio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 99–100). |
| commenta scripture | commentaries on scripture | Kept apart from *commentum (mendacii)* "fabrication". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 116.28). |
| verba sacramentalia conversiva | sacramental words that convert | The *moderni*'s words of consecration as effecting conversion. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 121.1). |
| transaccidencia | transaccidents | In the *transaccidentacio* series. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 145.4). |
| katholicacio | declaration as catholic | The noun of *catholicare*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 156.31). |
| pena talionis | penalty of retaliation | The accuser's penalty in canon law. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 156.4). |
| corpus dominicum | the Lord's body | Kept apart from *corpus Domini* "the body of the Lord" and *corpus Christi*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 158.31, 165.3). |
| in circulo (of the host) | in a round | The round form of the host. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 161.17). |

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
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| temporalia | temporal goods | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| citare; citacio | to cite; citation | Summons to a church court. Ruled 2026-09-28 (coordinator, delegated) (12 sites). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | CONTEXTUAL: condition / respect | "Condition": a person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). "Respect": the logical relation under which a predicate holds (*posiciones secundum habitudinem*), with a **C** note; ruled 2026-10-22 (Wilson; *Incarn.* 4.16). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| perquisitum | acquisition | Property acquired, not inherited (the legal term). Ruled 2026-10-02 (*Eccl.* 215.4). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| facinus | misdeed | Wyclif equates it with "felony" (239.13, 239.21). Ruled 2026-10-02. |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |
| leges ecclesie | the laws of the church | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.20, 1.23). |
| decretum; decreta | decree; the decrees | Gratian (*in decretis*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.14, 3.24). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
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
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
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
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| ingratitudo | ingratitude | Toward a person. Ruled 2026-10-02 (156.8). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| indispensabilis | not to be dispensed | Ruled 2026-10-02. |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |
| humanitas | the humanity | The nature the Word assumed, body and soul; with the article (*humanitas sit Christus*, "the humanity is Christ"). Not "the human nature", which is *natura humana*. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| dimittere / dimissio (*naturam*) | lay aside / the laying-aside | Letting go the assumed nature, so the union would be dissolved. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 2.23). |
| triduum (*in triduo*) | the three days | Death to resurrection, body in the tomb (Lombard, *Sent.* III d. 22). Ruled 2026-10-22 (Wilson; *Incarn.* prol). |
| ydemptitas specifica | identity of species | That Christ and other men are of one species. Not "specific identity" (reads as "particular"). Ruled 2026-10-22 (Wilson; *Incarn.* prol, 8). |
| homo assumptus | the assumed man | A term of art (the Lombard's first opinion, *Sent.* III d. 6); keep "assumed" before "man", never "the man assumed". With the agent expressed (*homo assumptus a Verbo*) "the man assumed by the Word", which cannot be misread (coordinator, 2026-10-22). Ruled 2026-10-22 (Wilson; *Incarn.* 5.15). |
| secundum quod (reduplicative) | insofar as | ⛔ Never "in that" (heard as "because", which inverts the logic). Ruled 2026-10-22 (Wilson; *Incarn.* 5.29–6.24). |
| secundum deitatem / secundum humanitatem | as to the Godhead / as to the humanity | The rule of reduplication; keep it in Wyclif's place in the sentence. ⛔ Never supply "as God / as man" where the Latin has bare apposition (*ipse Deus*) or bare predication. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| natura | nature | Ruled 2026-10-22 (Wilson; *Incarn.* 3.4). |
| creatura / creator / creatus | creature / creator / created | ⛔ Never "creation" for the created thing. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| posicio / proposicio / predicacio | position / proposition / predication | Kept apart: the apparatus shows the three trading places (*Incarn.* 4.15). Ruled 2026-10-22 (Wilson). |
| sacramentum (of the incarnation, of creation) | sacrament | The Augustinian sense, "mystery" (1 Tim. 3:16): G note at the first occurrence in the chunk. Kept apart from *misterium*. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.8). |
| misterium | mystery | Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.3). |
| moderni doctores / moderniores doctores | the modern doctors / the more modern doctors | Ockham and the *moderni*, usually unnamed. Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.1). |
| sancti | the saints | The fathers. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.15). |
| probabiles doctores | reputable doctors | *Probabilis*: worthy of credence (cf. *probabiliter*). Ruled 2026-10-22 (Wilson; *Incarn.* 7.1) as "approved doctors"; changed the same day (coordinator) to free "approved" for *approbati*. |
| Sermo (beside *Verbum*) | Speech | The divine title, capitalised; *Verbum* stays "the Word". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 16–17). |
| sophistice | sophistically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 15). |
| de vi vocis / de vi sermonis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| nedum | not only | "Let alone" where the sense is a fortiori. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21, 24). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| gracia unionis | the grace of union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| humiliacio | humbling | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26–28). |
| humanitus | humanly | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* passim). |
| suscipere / suscepcio (of the soul, the nature) | take up / taking-up | Kept apart from *assumere* "assume". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 31). |
| suppositum | supposit | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 34.24). |
| in quantum (reduplicative) | insofar as | As *secundum quod*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37.9). |
| diccio (logical) | word | A single term in a proposition. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 43.3). |
| intransitive | intransitively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 45.28). |
| dos immortalitatis | dower of immortality | Of the glorified body. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 46.24). |
| in effectu | in actual fact | As against in potency or in name; ⛔ not "in effect" (modern "virtually"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 47.10). |
| animare | animate | The argument turns on it (45.30–46.4). Ruled 2026-10-22 (coordinator, delegated). |
| communicacio ydiomatum | communication of idioms | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.1). |
| predicacio actualis / aptitudinalis / habitudinalis / mixtim | actual / aptitudinal / habitudinal / mixed predication | *Habitudinalis* is its own term (the four MSS at 49.6), not under *habitudo*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.5–16). |
| Doctor Subtilis | the Subtle Doctor | Scotus. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.24). |
| convertibilis / converti | convertible / be convertible | Of terms. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 52.29). |
| quantus | quantified | The adjective beside *quantitas*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.22). |
| suppositacio | suppositation | Kept apart from *supposicio* "supposition". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.31). |
| construccio synecdochica | synecdochic construction | Beside *synecdochica locucio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.5). |
| carneus / carnalis | fleshy / carnal | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.21). |
| moderniores loquentes | the more modern speakers | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 59.21). |
| ampliativus | ampliative | Beside *ampliacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 57.29). |
| passio (against *accio*) | being-acted-on | The category; G note at the first occurrence in a chunk. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 60.13). |
| supposibilis | that can be supposited | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 64.14). |
| proditor | the traitor | Judas. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 64.3). |
| per se / per accidens | CONTEXTUAL: of itself / by accident; (spatial) apart, by itself | The spatial sense (a thing set apart, *Euch.* 104.16–17) gets a G note. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a (sufficienti) divisione | the topic from sufficient likeness / from (sufficient) division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| pretericio | being past | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| solvere / solucio (of the union) | loose / loosing | Except inside a Douay quotation (John 10:35 "cannot be broken"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| peccabilis | able to sin | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| inconsequens | inconsistency | Kept apart from *inconveniens* (an unfitting conclusion). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 78.23). |
| ydemptitas ypostatica | hypostatic identity | Beside *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 84.20). |
| passionatus | subject to passion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| capitales doctores | the chief doctors | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| eiusdem / consimilis / alterius racionis | of the same / like / another kind | The species-sense of *racio*; *racio speciei* "the account of the species" (Aristotle's *logos*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.4, 87.17). |
| principiari | be constituted from principles | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.7). |
| accidentatus | subject to accidents | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.4). |
| in recto / in obliquo | in the direct case / in an oblique case | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.25). |
| passibilis | passible | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.12). |
| signum / signatum | sign / thing signified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 91.2–6). |
| conveniencia / convenire (*in*) | agreement / agree | The argument of 90–91 turns on it; not "fittingness" (that is *congruencia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 90). |
| predicacio synecdochica | synecdochic predication | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.27). |
| humidum infantile / radicale | the moisture of infancy / radical moisture | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 94.9). |
| conversari | live one's life (among men) | Beside *conversacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.25). |
| esse intelligibile | intelligible being | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 99.23). |
| extraneare / extraneacio (supposicionis) | estrange / estrangement (of supposition) | *Affeccio extraneandi* "an affection of estrangement". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 98.16). |
| ministerialiter | ministerially | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 100.17). |
| mobile (noun) / primum mobile | a movable / the first movable | Against the adjective *mobilis*; ch. 7 turns on it. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 107, 116). |
| res racionis | thing of reason | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| significatum | significate | Kept apart from *signatum* "thing signified". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 111). |
| sermo vocalis | the spoken word | Against *Sermo* "Speech", the divine title. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 113). |
| predicacio secundum essenciam / formalis | predication by essence / formal predication | Wyclif's modes of predication (cf. *predicacio secundum causam*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 115–116). |
| concepcio (figure) | conception | The grammatical figure. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habitus (of the humanity) | habit | The Lombard's third opinion (*Sent.* III d. 6). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| accidens | accident | The category; *accidit* "befalls". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habitacio | habitation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 120.14). |
| conversio (of a proposition) | conversion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.30). |
| humanitacio | humanation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 126.12). |
| racio (individual, personal) | account | *Racio individui / persone* "the account of an individual / a person", as *racio speciei*; not "aspect" (the row against *substancia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 8, 129–132). |
| vir (against *homo*) | man (*vir*) | Where Wyclif sets *vir* against *homo*, the Latin in parentheses. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 129.15–26). |
| exemplaria / exemplata | exemplars / things exemplified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.6). |
| res secunde intencionis | things of second intention | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.25). |
| materia proxima / remota | proximate / remote matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137.1). |
| colorate | with colour enough | With a plausible ground (cf. *color*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 134.26). |
| ydemptificare / ydemptificacio | identify / identification | Make the same (*idem*); the hypostatic union as identification, not conversion or generation. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 142.19, 147.22). |
| res communis / res communes | the common thing / common things | The realist universal the *moderni* do not conceive (first root of their error). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 144.27). |
| distinccio racionis | distinction of reason | Beside *differencia formalis*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 145.23). |
| conversio naturarum / confusio naturarum | conversion of the natures / confusion of the natures | Kept apart from *conversio* of a proposition. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 143.9). |
| moderni (bare) | the moderns | Beside *moderni doctores* "the modern doctors". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 142.10). |
| principiare (active) | be the principle of | Beside the passive *principiari* "be constituted from principles". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 147.4). |
| moderniores (bare) | the more modern | Beside *moderniores doctores* "the more modern doctors". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 151.17). |
| supposicio simplex / supposicio personalis | simple supposition / personal supposition | Supposition theory. *Simpliciter / personaliter supponere* "stand with simple / personal supposition": NOT the *simpliciter / secundum quid* pair, C note where the two could be confused. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 152.5–12). |
| transsumpcio | transumption | Beside *transsumptive*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 153.28). |
| aliud / alius | another thing / another one | The neuter against the masculine (*aliud et aliud, non alius et alius*): natures against persons. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 160.1–2). |
| in quid (predicari in quid) | in quid | Kept in Latin (predication of what a thing is, as against *in quale*), glossed at first use in a chunk. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 162.22). |
| suppositari | be supposited | Verb beside *suppositum*, *suppositacio*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 161). |
| dependencia actualis / potencialis / obediencialis | actual dependence / potential dependence / obediential dependence | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 161.23–162.4). |
| substancia prima / substancia secunda | first substance / second substance | Aristotle, *Cat.* 5. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.25). |
| a simili | by likeness | Bare, as an argument form; beside *locus a simili* "the topic from likeness". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.16). |
| racio substancialis | substantial account | As *racio individui* "account". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.21). |
| doctores signorum | the doctors of signs | The logicians who reason from terms, not things. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.26). |
| sensibilis (in the definition of animal) | sentient | *Substancia animata sensibilis*: able to sense. Elsewhere the §D row "perceptible" holds; G note at first use. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 177). |
| ydemptitas numeralis | numerical identity | Beside *ydemptitas specifica* "identity of species". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 172). |
| suppositalis | of a supposit | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 176). |
| accidens absolutum | absolute accident | Quantity and quality, against relative accidents. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 176). |
| beatificabilitas | beatifiability | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 181). |
| passionaliter | as an attribute | Beside *passio* (the proper attribute). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 181). |
| posicio anime | the laying-down of the soul | John 10:17–18; not the logical *posicio* "position", C note. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 183.3). |
| causancia / causacio | causing / causation | Kept apart (both at 187.30–34). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 185.16). |
| vicem supplere / vicis supplecio | supply the place / the supplying of a place | God supplying the place of a second cause. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 187.26). |
| transsubstanciacio | transubstantiation | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.10). |
| multiplicative | multiplicatively | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 193.20). |
| habitudo relativa | relative respect | The "respect" sense of the CONTEXTUAL *habitudo* row. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 193.19). |
| remitti / intendi (of a quality, merit) | be remitted / be intensified | The intension and remission of forms; not *remissio* of sin. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 197.1–7). |
| in divinis | among the divine [persons] | Keeps "Godhead" for *deitas*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 196.18). |
| partes proporcionales | proportional parts | The halving division of a continuum. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 194.24). |
| multiplicacio dimensionalis | dimensional multiplication | One body in several places by its dimensions. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.6). |
| habitus (= possession, *habere*) | the having | The category of having, C note; kept apart from *habitus* "habit". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.14). |
| proporcio racionalis | rational proportion | The mathematical ratio. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 207.7). |
| a maiori vel pari | from the greater or from the equal | Arguments *a maiori*; cf. *locus a maiori*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 209.5). |
| sensibile commune | common sensible | Aristotle's common sensibles (number, motion, figure); the term of art, against the §D row "perceptible". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 209.23). |
| communioritas | greater commonness | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 210.15). |
| multiplicacio concomitancie | multiplication of concomitance | Cf. *gracia concomitancie*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 213.21). |
| assertibile | assertible | The thing a proposition asserts. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 215). |
| superioritas / inferioritas terminorum | superiority / inferiority of terms | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 215). |
| homo communis | the common man | The universal man, with *res communis*; not "the ordinary man". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 218.3). |
| moderni loquentes | the modern speakers | Beside *moderniores loquentes*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 221.20). |
| bonum de genere | good in its kind | Moral goodness by the kind of act. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 228.16). |
| mixtim (bare) | in a mixed way | Beside *predicacio mixtim*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 230.21). |
| signum reduplicatum | the reduplicated sign | The reduplicative word (*secundum quod*, *in quantum*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 230.23). |
| supposicio | supposition | Of a term (supposition theory) or of a premiss laid down (cf. *supponitur* "it is supposed"); the English word serves both, C note where it matters. Kept apart from *suppositacio* "suppositation". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 102.8). |
| lex proximitatis | the law of neighbourhood | The duty to love one's neighbour (*proximus*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 101.29). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |
| sacramentaliter | sacramentally | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| vere | truly | A mode adverb: one word each, never two merged, kept where Wyclif puts it. ⛔ Never "really" (that is *realiter*). Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| spiritualiter | spiritually | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| virtualiter | virtually | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| ydemptice | identically | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| sensibiliter | perceptibly | A mode adverb: one word each, never two merged, kept where Wyclif puts it. As *sensibilis* "perceptible". Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| corporaliter | bodily | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| substancialiter | substantially | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| dimensionaliter | dimensionally | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| solvere / dissolvere (an argument, an objection); solucio | resolve; resolution | Synonyms in Wyclif, not an opposable pair (both in one sentence for one act, 2.1–5); "answer" is left to *respondetur / dicitur*. Ruled 2026-11-06 (Wilson; *Euch.* prol-a 1.4–2.5, review b1). |
| sentencia (verborum, scripture) | sense | The meaning of words or a text (*ad sentenciam attendendum*, against the rites, 4.9); kept out of the two-sense row *sentencia*. Ruled 2026-11-06 (Wilson; *Euch.* prol-a 4.9, review b14). |
| predicacio ydemptica / tropica | identical / tropical predication | The treatise's key pair; *tropica* kept apart from *figurative*. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.21). |
| accidens sine subiecto | accident without a subject | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 3.19). |
| remanencia (panis) | the remaining (of the bread) | Verb *manere* "remain". Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.21). |
| substancia | substance | Beside *substancia prima / secunda*. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 3.14). |
| quantitas / qualitas | quantity / quality | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.7–8). |
| esse; esse sacramentale | being; sacramental being | The bare *esse* of the modes of being. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 3.28, 3.30). |
| esus / manducacio (corporalis / spiritualis) | (bodily / spiritual) eating | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.5). |
| Doctor Communis | the Common Doctor | Thomas; with *Doctor Subtilis*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 8.16). |
| multitudo (of one body) | multitude | Of one body's being many (ch. 8); the plain "multitude" of persons needs no row. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 8.4). |
| sensus communis | the common sense | The inner faculty; kept apart from *sensibile commune* "common sensible". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 18.31). |
| supponere pro | stand for | Supposition; with *supposicio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 24.27). |
| sensualiter | sensually | Berengar's oath word (*Ego Berengarius*); kept apart from *sensibiliter* "perceptibly". A mode adverb, one word. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 26.1, 30.24). |
| inprecative | by way of imprecation | The third mode beside *laudative / effective*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 28.8). |
| sentire (an opinion: sensit quod) | hold | Of a doctor's or church's opinion; the "perceive" row is the sacrament sensed. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 30.30, 31.18). |
| predicacio figurativa | figurative predication | A synonym of *predicacio tropica*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 35.18). |
| mixtum; mixta | mixed body; mixed bodies | The compounds of the elements. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 42.23, 44.10). |
| describere | define | The verb of *descripcio* "definition". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 48.9). |
| elicere | elicit | Of an act of will or judgement. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 44.5). |
| aliquitas | somethingness | Being a something (*aliquid*). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 60.27). |
| accidens predicamentale | accident of the categories | Kept apart from the predicable *accidens*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 64.1). |
| revera | in truth | Kept apart from *vere* "truly". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 63.4). |
| contiguacio | contiguity | Beside *continuacio* (of bodies) "continuation". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 68.12). |
| veritas predicamentalis | truth of the categories | As *accidens predicamentale* "accident of the categories". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 69.2). |
| convincere; conviccio | prove conclusively; conclusive proof | Of an argument that compels assent; "convince" never; of a witness or liar shown guilty, "convict" (*Euch.* 01-c). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 78.10, 79.10–12, 85.27). |
| esse situale / intencionale / potenciale | situal / intentional / potential being | The modes of the body's being. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 84.8 ff.). |
| sensus (of words) | meaning | Kept apart from *sentencia (verborum)* "sense" (Wilson's row). The bodily *sensus* and *sensus literalis / misticus* stay "sense". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 89.22, 04-c, 04-d). |
| interpolatus; interpolacio | interrupted; interruption | Of words spoken with pauses. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 89.4, 89.18). |
| famosius | as best known | The adverb of *famosior*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 90.15). |
| insensibiliter | imperceptibly | Beside *insensibilis*; the opposite of *sensibiliter* "perceptibly". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-e). |
| noticia confusa / distincta | indistinct / distinct knowledge | As *confuse / confusus* "indistinct(ly)". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-g). |
| ponderositas; ponderosum | heaviness; heavy | The abstract against the concrete: *hostia est ponderositas sed non est ponderosum*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-a p. 10, 110.24). |
| suscipere magis et minus | admit of more and less | Aristotle's test of a quality. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 113.32). |
| questio si est / quid est | the question whether it is / what it is | *Post. An.* II.1. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 119.18). |
| mistice | mystically | A mode adverb, one word; kept apart from *figurative*, *tropice*, *sacramentaliter*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 128.24). |
| naturalitas obediencialis | obediential naturalness | Cf. *dependencia obediencialis*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.15–18). |
| actuacio | actuation | Of a form actuating matter. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.25). |
| accidentalitas | accidentality | Beside *substancialitas*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.13). |
| quantitas successiva | successive quantity | Time and motion, against permanent quantity. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.1). |
| corpus mathematicum | mathematical body | The three dimensions without matter. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 142.31). |
| ubi; ubicans | where; that which gives a where | The category of place and its cause. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 146.23–24). |
| inpossibilitare | make out as impossible | Of the *moderni*'s argument. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 149.13). |
| utrobique | on both sides | In citation formulae and argument. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 148.21). |
| conversivus | converting | As *verba sacramentalia conversiva*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 153.6, 153.25). |
| signum nature | instant of nature | The scholastic priority without time; kept apart from *signa* "signs". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 161.9). |
| generancia | begetting | Ruled 2026-11-07 (coordinator, delegated; *Euch.* 161.25). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| insensibilis | imperceptible; of a thing that cannot feel, without sensation | Two senses by referent: what cannot be perceived / what cannot perceive (*lapis insensibilis*, *Dial.* 56.3). Kept visibly paired with *sensibilis*. Ruled 2026-09-28 (3 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| vecors; vecorditer; vecordia | faint-hearted; faint-heartedly; faint-heartedness | The medieval sense, not classical "senseless". Ruled 2026-09-28 (5 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| ingratus | displeasing (to God) | *Ingratus deo*: unpleasing to God. "Ungrateful" only where a person is ungrateful to someone. Ruled 2026-09-28 (5 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| monita | admonitions | Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office; *quale magisterium* "what a feat of mastery" (*Incarn.* 137.14) | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| laude digni | worthy of praise | (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| indispositus; (se) indisponere | unfit; to make (oneself) unfit | "indisposed" (now "unwell"). Ruled 2026-09-28 (8 sites). |
| prevaricator; prevaricancia; prevaricacio | transgressor; transgression; transgression | Ruled 2026-09-28 (*prevaricacio* 2026-10-08, *Pot. pape* 155.10). *Basali prevaricancia* (*Dial.* 9.24) is doubtful: see its C note. |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| prevaricari | to transgress | The verb of *prevaricator*. Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "almsman" (the 09-28 row governs; conformed 2026-10-02, *Eccl.* 16). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). Inside a DR quotation of Titus 1:7, DR's "steward" (2026-10-08). |
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
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| collegiatus | collegiate | Ruled 2026-10-02 (*Eccl.* 16, 16-d/16-e). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| ficcio | fiction | As *ficticia*; Wyclif numbers six *ficciones*. Ruled 2026-10-02 (*Eccl.* 16, 385.7). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| dotes (docium) beatorum; dotes corporis | the dowries of the blessed; the dowries of the body | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| continuacio (of bodies, the act) / discontinuacio; continuare / discontinuare | continuation / discontinuation; make continuous / make discontinuous | The making of several bodies into one continuum (*Incarn.* ch. 12), G note at first use: not "carrying on". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.30, 211.12). |
| precaria | precarial grant | Wyclif defines it (*Eccl.* 453.21). Ruled 2026-10-02 (*Eccl.* 19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| indisposicio | unfitness | Noun of *indispositus*. Ruled 2026-10-02 (*Eccl.* 19). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
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
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| memoriale | memorial | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
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
| remissio; remittere | remission; to remit | Headword row (cf. *condonacio* "pardon", *venia* "forgiveness"). Ruled 2026-10-02 (*Eccl.* 23). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). Beside *consecrare* (*consecrat et conficit*) "confect", so the pair stays two. Ruled 2026-11-07 (Wilson, "confect works"; *Euch.* 16.10). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| negociatores | dealers | Kept apart from *mercantes* "traders" (*Eccl.*); the servants of the talents parable (Matt. 25). Ruled 2026-10-07 (*Pot. pape* 101.7). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| criminosus | criminous man | Ruled 2026-10-07 (*Pot. pape* 06-c). |
| deliramenta | ravings | Ruled 2026-10-07 (*Pot. pape* 06-c). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dileccio | love | Kept apart from *caritas* "charity". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-e). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| regulariter | as a rule | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 165.2). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| quaternarius / denarius / quadragenarius | the four / the ten / the forty | Number exegesis (the 153 fishes, ch. 7). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 154–155). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| negociacio | dealing | Pairs with *negociatores* "dealers". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 194.5). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| memorativa potencia | memorative power | A faculty of the soul (the "power" sense of *potencia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 219.27). |
| primicia (virtutum) | being first (in the virtues) | Kept apart from *primatus* "primacy" and *primitas* "firstness". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 228.33). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| malum culpe / pene | the evil of fault / of penalty | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.19). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| eleccio passiva / activa | passive / active election | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 254.31). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| preponderancia; dispensacio | preponderance; dispensation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 266.11, 268.4). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| precellencia | pre-excellence | Kept apart from *preeminencia* "preeminence". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 274.33). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| cultus Dei | worship of God | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-d). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| pastor cesareus | caesarean shepherd | The *papa cesareus* family. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 290.24). |
| precellenter | pre-excellently | Adverb beside *precellencia* "pre-excellence". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 291.2). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| evangelizans | preacher of the gospel | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-g). |
| prepositus (participle of *preponere*) | the one preferred | CONTEXTUAL beside *prepositi* "superiors" (the noun); untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| latitudo (of a quality) | latitude | The intension/remission term. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 352.4). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |
| coloracior | more colourable | Comparative, with the *color* / *colorabilis* rows. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 384.15). |
| diccio procuratoria | proctorial pronouncement | C note gives *dicio* "authority" as the alternative. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 386). |
| servitus ydolorum | servitude of idols | Beside *servitus laboris*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| precellere | excel | Verb beside *precellencia* "pre-excellence"; not "pre-excel". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 399.28). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |
| nimis | exceedingly | Medieval intensive (= *valde*); "too much" only where excess is the point. Ruled 2026-10-12 (close-out R2; *Pot. pape* 169.2). |
| sentire (the sacrament, the body) | perceive | "sense". As *sensibilis* "perceptible". Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.10, 1.17). |
| singulariter | CONTEXTUAL: alone, only / in a singular way | "singularly" never; "in a singular way" where "alone" will not construe (*Euch.* 85.28, coordinator 2026-11-07). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 4.14). |
| recitare | recite | To report, rehearse. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.4, 3.10, 4.18). |
| ex tibi dubio; ex sibi dubio | for all you know; for all he knows | Idiom: not "from doubt". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 66.15, 70.25). |

---

## Chunk 06-c: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-06-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-06-c
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "165.17–169.26"
divisions: "cap. 6 (heading 'CAPITULUM SEXTUM.' at 158.0); part 3 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "901 words; 885 confirmed by the vote; 13 runs stood by rule; 3 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n236–n240 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 6, part 3: [TITLE]

## ¶1 · 165.17–168.8

> [p. 165] Sed sola redemptoris nostri percepta sacramenta ad veram sollempnitatem mentis non sufficiunt nisi eis quoque et bona opera iungantur. Quid enim prodest corpus et sanguinem illius ore percipere et e perversis moribus contraire? Unde bene ad comedendum subditur: Et azimos panes cum lactucis aggrestibus. Panes quippe sine fermento comedit qui recta opera sine corrupcione vane glorie exercet, qui mandata misericordie sine admixtione peccati exhibet, ne perverse diripiat quod quasi recte dispensat. Hoc quoque peccati fermentum miscuerant bone sue accioni quibus prophete voce per increpacionem Dominus [p. 166] dicebat: Venite ad Bethel et impie agite. Atque post pauca: Et sacrificate de fermentato laudem. De fermentato namque laudem immolat qui Deo sacrificium de rapina parat. Lactuce vero aggrestes valde amare sunt. Carnes autem agni cum lactucis aggrestibus sunt edende, ut cum corpus Redemptoris accipimus, nos pro peccatis nostris in fletibus affligamus, quatenus ipsa amaritudo penitencie abstergat a mentis stomacho perverse humorem vite. Ubi et subditur: Non comedetis ex eo crudum quid neque coctum aqua. Ecce iam nos ipsa verba historie ab intellectu historiaco repellunt. Numquid, fratres karissimi, Israeliticus ille populus in Egypto constitutus comedere agnum crudum consueverat, ut ei lex dicat, non comedetis ex eo crudum quid? Ubi et additur: Nec coctum aqua. Sed quid aqua nisi humanam scienciam designat iuxta hoc quod per Salomonem dicitur sub hereticorum voce: Aque furtive dulciores sunt. Quid crude agni carnes, nisi inconsideratam ac sine reverencia cogitacionis relictam illius humanitatem. Omne enim quod subtiliter cogitamus quasi mente coquimus. Sed agni caro nec cruda edenda est nec aqua cocta, quia redemptor noster nec purus homo estimandus est neque per humanam sapienciam qualiter Deus incarnari potuit cogitandus. Omnis enim qui redemptorem nostrum purum hominem credit quid iste aliud quam crudas agni carnes comedit quas videlicet coquere per divinitatis eius intelligenciam noluit? Omnis vero qui incarnacionis eius misteria iuxta humanam sapienciam discutere conatur carnes agni [p. 167] aqua vult coquere, id est, dispensacionis eius misterium per dissolutam vult scienciam penetrare. Qui ergo paschalis gaudii sollempnitatem celebrare desiderat agnum nec aqua coquat nec crudum comedat, ut neque per humanam sapienciam profunditatem incarnacionis illius penetrare appetat neque in eum tamquam in hominem purum credat, sed assas igne carnes comedat, ut dispensari omnia per Sancti Spiritus potenciam sciat. De quo adhuc recte subiungitur: Caput cum pedibus et intestinis vorabitis, quia Redemptor noster est alpha et o, Deus videlicet ante secula et homo in fine seculorum. Et sicut iam prediximus, fratres, Paulo attestante didicimus quod caput Christi Deus; caput ergo agni vorare est divinitatis illius fidem percipere, pedes vero agni vorare est vestigia humanitatis illius amando et imitando perquirere. Quid vero sunt intestina nisi verborum illius occulta et mistica mandata? Que tunc voramus, cum verba vite cum aviditate sumimus. In quo devoracionis verbo quid aliud quam pigricie nostre torpor deprehenditur? Qui eius verba atque misteria per nosmetipsos non requirimus et dicta ab aliis audimus inviti. Non remanebit ex eo quidquam usque mane, quia eius dicta magna sunt sollicitudine discucienda, quatenus prius quam dies resurreccionis appareat in hac presentis vite nocte omnia mandata eius intelligendo et operando penetrentur. Sed quia valde difficile est, ut omne sacrum eloquium possit [p. 168] intelligi et omne eius misterium penetrari, recte subiungitur: Si quid remanserit, igni conburetis. Quod ex agno remanet igni conburimus, quando hoc quod de misterio incarnacionis eius intelligere et penetrare non possumus, potestati Sancti Spiritus humiliter reservamus, ut non superbe quis audeat vel contempnere vel denunciare quod non intelligit: sed hoc igni tradat, cum Spiritui Sancto reservat.

[ENGLISH]

## ¶2 · 168.9–169.13

> [p. 168] Quia igitur qualiter edendum sit pasca agnovimus, nunc autem a qualibus edi debeat agnoscamus. Sequitur: Sic autem comedetis illum: Renes vestros accingetis. Quid in renibus nisi delectacio carnis accipitur? Unde et Psalmista postulat dicens: Ure renes meos. Si enim voluptatem in renibus esse nesciret, eos uri minime petisset. Unde quia potestas dyaboli in humano genere maxime per luxuriam prevaluit, de illo voce dominica dicitur: Potestas eius in lumbis eius. Qui ergo pasca comedit habere renes succinctos debet, ut qui sollempnitatem resurreccionis atque incorrupcionis agit corrupcioni iam per nulla vicia subiaceat, voluptates edomet, carnem a luxuria restringat. Neque enim cognovit que sit sollempnitas incorrupcionis qui adhuc corrupcioni per incontinenciam subiacet. Hec quibusdam dura sunt, sed angusta est via que ducit ad celum, et habuimus iam multa exempla continencium. Unde et adhuc subditur: Calceamenta habebitis in pedibus. Quid etenim sunt pedes nostri nisi opera? Quid vero calceamenta nisi pelles mortuorum animalium; calceamenta autem pedes muniunt. Que [p. 169] vero sunt mortua animalia, ex quorum pellibus nostri muniantur pedes, nisi antiqui patres qui nos ad eternam patriam precesserunt. Quorum dum exempla conspicimus, nostri operis pedes munimus. Calceamenta ergo in pedibus habere est mortuorum vitam conspicere et nostra vestigia a peccati vulnere custodire. Tenentes baculos in manibus. Quid lex per baculum nisi pastoralem custodiam designat? Et notandum quod prius precipimur renes accingere, postmodum baculos tenere, quia illi debent curam pastoralem suscipere, quia iam sciunt in suo corpore fluxa luxurie edomare, ut cum aliis forcia predicant, ipsi desideriis mollibus et voluptatibus non succumbant.

[ENGLISH]

## ¶3 · 169.14–169.26

> [p. 169] Bene autem subditur: Et comedetis festinanter. Notate, fratres, notate quod dicitur festinantes. Mandata Dei, misteria Redemptoris, celestis patrie gaudia cum festinacione cognoscite et precepta vite cum festinacione implere curate. Quia enim adhuc hodie licet bene agere scimus: utrum cras liceat ignoramus. Festinantes autem pascha comedite, id est, ad sollempnitatem patrie celestis anhelate. Nemo in huius vite itinere torpeat, ne in patria locum perdat. Nemo moras ad appetenda studia innectat sed cepta perficiat, ne minime liceat implere quod inchoat. Si ad amorem Dei pigri non sumus, adiuvat ipse quem amamus.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 169.26: Fitness to receive the host consists in love to Christ and God.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 166: *vero* (print = bt) [SUB]
  - 167: *nocte* (print = bt) [SUB]
  - 169: *amamus.* (print = bt) [BT-ONLY]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 6. Exod. XII, 1 1. 14. Ibid. (169.30).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 165:
1. B: ligno sitbditur; ACDE: signo ; C in marg. correxit: agno.
2. AB: quippe deest; C in marg. addit.; E: qnidem. 3. modo ; Codd.:
nostro; C: fiostro in marg. alia mann; ib. E: assumimus accipimus.
4. Codd.: abinvicem. 5. D: quod tamcn ; ib. C: in igne. 8. E: ipsum ;
ABC: cum ipsa. 10. incorrupcionem ; C in alia manu; in marg. ad;
E: ad incorrupcionem. 11. Codd. : videt carnes. Correxi ; ib. Codd. :
dirruerunt ; E: alias exaruerunt. 12. E: aruit. 20. ABCD: eis.
21. C: bene in marg. alia manu. 23. E: panes quidem. 24, 25. B: qui
manifesta. 25. C: exhiberet. 2S. Codd.: Dominus deest; C in marg.
in rasura addit.
1. ExoJ. XII, 8. 12. Psalm. XXI, 16. 22. Exodi XII, 8.

p. 166:
2. C: fermento; ib. AB: De deest. 3. E: laudis. 5. D: agni
dcest; ib. D: cum eum. 6. D: comedende. 10. B: crudi quid.
i |. C: agnunt in marg. alia manu; ib. D: eius. 17. C: hoc in marg.
alia manu. 19. Codd. : inconsiderata. 22. C: nec cruda in marg. alia
manu. 23. D: ut purus homo. 27. D: quos; ib. ABC: quas valet.
28. C: coquere in marg. alia manu; ib. E: voluit.
1. Amos IV, 4, 5. 9. Exod. XII, 9. 18. Prov. IX, 17.

p. 167:
1. ABC: id est deest. 2. C: sapienciam ; correxit in marg. alia manu.
7. A: assas tantum; B: assas tamen. 8. Codd.: dispensare Correxi e
textu S. Gregorii. 10. E: Etcaput; ib. E: atque inteslinis ; ib. E: vorabis.
12. Codd.: et before sicut deest. Addidi. i3. ABCE: quia. 14. C: caput
in marg. alia manu; ib. B: caput vero ; C: vero in textu. Corr. supr. lin.
14, i5. D: divinitatis dcest. 16. ABDE: illius deest; C in marg. alia
manu. 19. ABC: vite deest; ib. D: sumamus. 23. E: quidquam ex eo.
26. C: eius appareat ; ib. ABE: vite voeacione communia ; C correxit iu
marg. : omnia nocte ; D: vocacione omnia. 27. D: illius. 28. ABCE :
10. ExoJ. XII, 9. 23. ib. 10.

p. 168:
10. D: quolibet. 11. D: aut. 12. D: deleclacio. i5. ABCE: urere.
18. D: cius deest. 19. C: videlicet qui. 20— 23. C: corrupcioni —
corrupcionis in marg. sup. alia manu. 21. E: voluptas; ib. ABC: edomat.
22. D: etenitn. 25. D: fiic iam. 27. ABCE: nostri deest. 28. E: Nec
opera. Quidenim; ib. D: nisi pedes.
2. Exod. XII, 10. 11. ib. 11. 14. Psalm. XXV, 2.
17. Job XL, 11, 20. S. Gregorii I. c. pag. 1 536, i53j*
24. Matth. VII, i3. 26. Exod. XII, 11.

p. 169:
1. B: quibus pellibus. 10. A in textu : ille ; supra lin.: illi ; ib. C:
illi debent in marg. alia manu. 11. C: fluxum. 12. ABCE: sarcinam
predicant ipsi desidiis. i5. E: festinanter. 18. ABC : ad hoc.
20. B: medite. 23. E: studia deest. 28. D: stet. 28, 29. B: Det
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
(none recorded)
```

---

## Chunk 06-d: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-06-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-06-d
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "169.27–173.29"
divisions: "cap. 6 (heading 'CAPITULUM SEXTUM.' at 158.0); part 4 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "920 words; 906 confirmed by the vote; 12 runs stood by rule; 2 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n240–n244 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 6, part 4: [TITLE]

## ¶1 · 169.27–171.11

> [p. 169] Sic ergo tota disposicio hominis ad comedendum hostiam stat in sincera et grata dileccione Christi et Dei. Est, inquam, sincera dileccio, quando amor Dei supereminet et amor cuiuslibet creature in ordine ad ipsum supponitur. Qui enim plus diligit aliquid [p. 170] Domino est ingratus et per consequens non ipso dignus. Omnes autem istam dileccionem sed nimis mendaciter profitemur; quod discerni potest ex hoc quod nos sacerdotes misse a summo usque ad infimum statim post missam propter superbiam, carnem vel similia dimittimus Christi servicium, legem suam, monita sua, et conversacionem suam abicimus in contemptum. Quis, inquam, nostrum nedum post missam, sed in missa non plus nititur servire mundo vel homini quam auctori? Inclinaciones autem, occupaciones et operaciones istud diiudicant, cum nedum facillime possemus ad delectaciones corporis vel commodi offendere veritatem sed de facto sic facimus: ut, inquam, dimittam maiora facinora, quis nostrum non est tam fragilis quin propter affeccionem carnalem sive pecuniam diceret testimonium contra veritatem vel prorumpat in assercionem sentencie, antequam secundum Dei regulas examinet veritatem, vel tercio ubi ad honorem Dei posset prodesse ecclesie, taceat vecorditer veritatem? Et omnium istorum causa est preponderans dileccio terrenorum. Et talis indigne capit corpus Christi et sanguinem Jesu Christi; et nisi hoc esset sacerdotes Christi non occuparentur in seculari negocio, non aspirarent ad temporalia sed pauper vita Christi foret eis amena; nec dimittendo certum et melius prorumperent in verba et opera minus utilia. Et bene esset illi sacerdoti qui sciret ab ista macula triplici se servare. Oportet enim quod ob amorem Christi quem comedit moderet intellectum, quia aliter prandium istud quod ordinatum est propter hanc medicinam, foret tam sumenti quam toti ecclesie venenosum; quanto magis si demonium meridianum [p. 171] commixtum fuerit in istis ministerio sacerdotum? Utile quidem foret ecclesie non habere elemosinarios sic celebrantes dotatos nec ypocritas proditores veritatis super falso fundamento religionis et ficcione mendacii sic orantes, sed evangelisacione Christi plus in suis iustis operibus confidentes. Tunc enim digne manducarent corpus Christi et sanguinem eius biberent, que in celis sunt, subducto omni conversante nobiscum presbytero celebrante. Ymmo efficacius et verius forent corpus Christi et sanguis tam in corpore nostro quam anima hic nobiscum.

[ENGLISH]

## ¶2 · 171.12–171.19

> [p. 171] Sed obicitur primo per hoc quod nedum in legendis et serviciis huius festi accidencia asseruntur esse sine subiecto, sed decretalis libro III hoc videtur expresse innuere, ut patet De Celebracione Missarum, capitulo Cum Marthe et in Clementinis capitulo... de hoc festo dicuntur multa similia. Negando itaque hoc posse fieri contradiceretur decretis et glosse ecclesie sed blaspheme contradiceretur divine potencie.

[ENGLISH]

## ¶3 · 171.20–172.7

> [p. 171] Quantum ad legendas patet quod nedum sunt collecta apocrifa sed sepe mendacia. Unde Augustinus in De Sermone Domini in Monte libro primo declarans quomodo Petrus et Paulus excommunicaverunt homines pro amore, sicut patet Act. V°, 3 de Anania et Saphira, et prima Cor. V°, 5, quem Paulus tradidit Sathane, ut spiritus salvus fiat: ymmo in libris illis quibus adversarii magnam auctoritatem tribuunt. Advertant inquit, quod dicimus ubi scriptum est apostolum [p. 172] Thomam inprecatum cuidam a quo palma percussus esset atrocissime mortis supplicium, animam tamen eius commendat ut in futuro seculo ei parceretur: cuius a leone occisi a cetero corpore discerptam manum canis intulit mensis convivarum, in quibus convivabatur Apostolus. Cui scripture, inquit, licet nobis non credere; non enim est in katholico canone.

[ENGLISH]

## ¶4 · 172.8–172.13

> [p. 172] Ex isto testimonio Augustini patet quod omnia talia extra fidem scripture licet vera, non oportet fidelem credere explicite; multo magis non oportet aliquomodo credere legendas que dicunt in sacramento altaris accidens esse sine subiecto, cum sint contrarie sanctis doctoribus et racioni.

[ENGLISH]

## ¶5 · 172.14–173.29

> [p. 172] Quantum ad decretales, videtur primo ex dicto Augustini quod non oportet ipsas credere, cum non sint in katholico canone, sed (ut sepe glossavi) potest dici quod per accidencia panis et vini intelliguntur panis et vinum, ut ecclesia sepe per signa intelligit sua signata. Sicut ergo scriptura sacra, sancti doctores et leges ecclesie vocant illa que dicimus accidencia panem et vinum, sic nos ad imitacionem eorum vocamus ea panem et vinum; nec habent auctoritatem vel evidenciam ad impugnandum nominacionem nostri baptismatis pocius quam econtra. Nec probare possunt quod interim sit miraculosa variacio pocius quam fuit tempore istorum auctorum. Sed maiori auctoritate vel evidencia licuit eis vocare illum panem et vinum accidencia quantitatis cum cognomine. Nec dubium quin Apostolus vocavit illam rem panem prima Cor. X et XI°, sicut generaliter scriptura et beatus Ambrosius, ut patet de consecracione, distinccione IIᵃ, [p. 173] Panis est, et Augustinus eadem distinccione, Hoc est, et Sermone XXVI (ut sepe recitavi); et pari evidencia qua glossatores glossant eos quod intelligunt per panem et vinum non substanciam sed accidencia, nos econtra glossamus eos quod non intelligunt per accidencia aliquas res novem generum accidentis, quia nemo scit quam; sed intelligunt per accidencia substanciam panis et vini et non accidens, quia (ut testatur Augustinus in isto katholicus) nullum accidens poterit per se esse. Nec videtur quod ecclesia sit oneranda ut fide eorum testimonio, cum cotidie fiant ista miracula que Augustinus dicit non posse fieri, sicut tempore Augustini Spiritus Sanctus noluit onerari ecclesiam dictis suis vel alterius preter auctores scripture tanquam fide katholica (ut sepe testatur iste sanctus); quomodo ergo oneretur contra dicta sanctorum et contra racionem, ut credat accidens esse ibi sine subiecto? Nec in isto contradicitur divine potencie, sicut nec Apostolus contradixit IIᵃ Thym. II°, quando asseruit Deus verax est, se ipsum negare non potest. Quid ergo obest quod longitudo, latitudo et profunditas materialis substancie (sicut Augustinus testatur) non poterunt per se esse? Leges itaque quotlibet constituit Deus in natura quarum opposita implicant contradiccionem, in quam Deus non potest, cum tunc foret contrarius sibi ipsi, cuiusmodi est lex de inpossibilitate substancie sine accidente; et sic de inpossibilitate ydemptificacionis generum, specierum et differenciarum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 170.4: Yet we set worldly delights above them.
- 171.12: Objections from the language of legends, services and decretals.
- 171.20: Some legends are false, as Augustine says.
- 172.14: Decretals are not of full authority; and even if they were could be glossed in our sense.
- 173.10: No reason why the Church should be burdened with additions to the faith of Scripture.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 173: *per se esse. Nec* (print = bt) [SUB]
  - 173: *IIᵃ* (print = bt) [SUB]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 6. Exod. XII, 1 1. 14. Ibid. (169.30).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 169:
1. B: quibus pellibus. 10. A in textu : ille ; supra lin.: illi ; ib. C:
illi debent in marg. alia manu. 11. C: fluxum. 12. ABCE: sarcinam
predicant ipsi desidiis. i5. E: festinanter. 18. ABC : ad hoc.
20. B: medite. 23. E: studia deest. 28. D: stet. 28, 29. B: Det

p. 170:
2. E: nimis deest. 5. B: statum; ib. C: propter in marg. alia manu.
("). J): similium. 7, 8. B: et contemptum. 9. E: non deest.
10, 11. ABC: et occupaciones. 12. BD: facilem; ib. D : carnis et.
1.4. I) : dimitlat. i5. BD: quin per ; ib. D: corporalem. 16. E: vel
pecuniam. 21. C: Et talis in rharg. alia manu. 22. E: Jesn Clirisli deest.
24. A13CE: iudicio, non. 2K. D: Oporterel.

p. 171:
1. ABC: fucrat. 5. E: Sed ex ; ib. ABDE: populos in suis.
i3. ABDE : asseritur. i5. B: esse innuere. 16. Inicium huius capituli
excidisse apparet. 17. D : Notando itaque. 18. ABCD : glossa.
20. B : Et quantum. 20. 21. C: quod — mendacia deest. 21. D: in
deest; ib B: De deest. 22. A: declarnans. 27. AB : ad versat.
28. AB: quod Deus ; C: correxit.
16. Decret. Greg. lib. III, tit. XLI. De Cel. Missarum, cap. VI.
21. S. Augustini De Serm. Domini in Monte, lib. I, cap. XX (65),
Opp. tom. III, 2, 194.

p. 172:
I. AliE: interpretatiun cuidam. 4. CE: a toto corpore ; ib. 13: de-
scriptam. 5. D: convivorum. 7. C: non before credere alia manu.
14. D: dictis. i5. E: ipsos. 19. B: scripta sacra. 24. C: pocius
alia manu; ib. C: possunt alia manu. 28. D: cum cognomine quaniitatis.
jo. L) : et sic after scriptura.
3j. Decreti Tcrtia Pars, De Cons., dist. II, cap. LV.

p. 173:
2. ABCE: Scrmone LY. 12, i3. E: quia Augustinus. 14. E: eccle-
siam deest. 17. D: oneraretur. 25. D : quorum. 27. ABCE: contra-
dictorius. 28, 20. ABCD : substancie — impossibilitate deest.
1. Decreti Tertia Pars, De Cons., dist. II, cap. XLVIII et LXIII,
e tractatu XXVI ad cap. VI Johannis. 21. Rect. Rom. III, 4,
and II. Tim. II, 1 3.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
(none recorded)
```

---

## Chunk 06-e: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-06-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-06-e
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "174.1–178.30"
divisions: "cap. 6 (heading 'CAPITULUM SEXTUM.' at 158.0); part 5 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "1116 words; 1098 confirmed by the vote; 14 runs stood by rule; 4 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n245–n249 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 6, part 5: [TITLE]

## ¶1 · 174.1–174.32

> [p. 174] Ideo fabulantes talia sompnia viderent primo quomodo sancti et philosophi loquuntur de descripcione et de distinccione substancie et accidentis. Multi enim locuntur de signis huiusmodi sine sensu, et multi iudaice fabricant allegaciones corruptas, ut allegant fundacionem transubstanciacionis sue in illo Math. VI°, 11: Panem nostrum supersubstancialem da nobis hodie, sed hii non minus delirant quam falsi reportatores Christi qui loco istius dicti Johannis II°, 19: Solvite templum hoc et in tribus diebus excitabo illud. Hic dixit, inquiunt, possum destruere templum Dei et post triduum reedificare illud Math. XXVI°, 61. Nam longe plus differunt panis ille substancialis et sua transubstanciacio quam differant solvere et destruere, excitare et reedificare. Pictores autem vocant colores corpora liquida que illiniunt corporibus solidis, que debent ex hoc colorari. Et ita videtur decretalem grosse loqui de accidentibus vocando grave liquidum inebriatum generativum vini quod inmiscet se vino aut aqua post consecracionem accidenter; quod alii specificant per quantitatem quam dicunt ternam dimensionem que potest esse vanum. Que quantitas foret eque activa ut vinum, sive fuerit per se sive in subiecto. Sed philosophi non sic locuntur de quantitate quod sit de genere activorum racione qualitatis active quod subiectet, sicut nec qualitates prime agunt acciones qualitatis secunde quam causant, nec potest quantitas secundum diffinicionem Augustini sic per se variari; nec umquam conceperunt priores sancti illud insensibile cotidianum miraculum, ymmo pocius vocatur irracionabilis Dei crudelitas sanctificare per se accidencia destruendo substanciam.

[ENGLISH]

## ¶2 · 175.1–175.5

> [p. 175] Et sic quantum ad omnes allegandos in contrarium, est triplex solucio. Prima quod sunt grossi pictores mendacii intelligentes per accidencia ipsas substancias quas scriptura sacra et sancti doctores intellexerunt per panem et vinum.

[ENGLISH]

## ¶3 · 175.6–175.10

> [p. 175] Secunda solucio est quod intelligunt quod accidens est sine subiecto ibi principaliter in suo genere existente; nam corpus Christi est ibi principalius quam panis aut vinum; cui corpori suspensa consideracione signorum est precipue attendendum.

[ENGLISH]

## ¶4 · 175.11–175.24

> [p. 175] Tercia solucio est quod omnes adversarii veritatis intelligunt accidens esse sine subiecto condicionaliter, si Deus voluerit. Et illam condicionem oportet adversarium (ut docet beatus Jacobus) velit nolit intelligere. Nec habet dictum eorum in hoc efficacius testimonium, nam si per inpossibile Deus posset sic facere, adhuc non dicetur per hoc sic esse de facto; nec displiceret illis dicta glossa sancti Apostoli, cum sic glossatur Augustinus in dicto suo ad maximum hereticum, quando dicit quod Deus filius potuit produxisse ad intra alium filium. Non, inquit, non potuit sed non decuit, hoc est, potuit, si voluerit; et sic non plus quam sancti primitive ecclesie contradicimus in hoc divine potencie.

[ENGLISH]

## ¶5 · 175.25–176.2

> [p. 175] Secundo obicitur contra dicta de fragilitate indisponente hominem ad celebrandum hoc venerabile sacramentum. Nemo, inquam, capit hoc venerabile sacramentum quin sit infinitum fragilis et positus in adopcione bonum temporale ante virtutem eligeret; satis est igitur quod homo non sit mortali actualiter [p. 176] maculatus, licet oporteat quod pedes lavet (ut dicitur Joh. XIII°, 14).

[ENGLISH]

## ¶6 · 176.3–176.22

> [p. 176] Hic sunt multa dicenda; aliqua enim indisponunt hominem simpliciter et aliqua secundum quid, ut communicet cum infidelibus in sacramento altaris; nam peccatum mortale vel infidelitas presciti indisponit eum simpliciter et peccata venialia indisponunt secundum quid; unde quia quilibet nostrum debet presupponere quod sit predestinatus, debet supponere quod hoc sacramentum sibi proficiet, et licet sit indispositus secundum quid per veniale peccatum, tamen est simpliciter dispositus per graciam predestinacionis et per triplicem graciam consequentem (ut notatum est in principio huius VIᵗⁱ capituli). Loquor autem de veniali peccato ut alias; sine cuius noticia vanum est dubitare in ista materia; et sic nemo est infinitum fragilis, cum non attenditur penes hoc quod cicius ant facilius homo posset peccare. Sed multi positi in adopcione eligerent virtutem dimisso vicio; et ita non sufficit carencia mortalis peccati actualis cum malus habitus nimis indisponit hominem ad cultum huius sacramenti.

[ENGLISH]

## ¶7 · 176.23–178.30

> [p. 176] Tria ergo sunt disponencia, scilicet Christi dileccio, pax cum proximo et actualis devocio; que tria exprimuntur in illo magno sermone Christi post dacionem huius sacramenti a capitulo XIII Joh. usque ad capitulum XVIII. Quoad dileccionem Christi et pacem proximi dicit Joh. XIII°, 34: Mandatum novum do vobis: ut diligatis invicem, sicut dilexi vos. Et quia illa dileccio convertitur cum dileccione et pace proximi, ideo capitulo XIV°, 21 explicat hanc dileccionem: [p. 177] Si, inquit, diligitis me, mandata mea servate. Et sequitur: Pacem relinquo vobis, pacem meam do vobis; ubi non dubium dat doctrinam tenerrimam ad colendum hoc sacramentum quod paulo ante dedit apostolis: Oportet, inquam, cultorem huius sacramenti radicari et fundari in caritate, sic quod habitualiter Deum amet pre omnibus et omnia in ordine ad ipsum. Unde nimis indisponitur qui peccato invidie, peccato avaricie vel carnis proponunt inordinate creaturas diligere; nam cultus eukaristie nocet tali et facit iniuriam cuilibet creature. Unde in signum plene mundicie observancie huius sacramenti creditur Christum post eius ministerium lavisse humillime pedes discipulorum quod significat mundiciam affeccionum. Unde Augustinus Omelia LVI dicit quod quantumcunque homo mundus fuerit in baptismo, verumtamen cum in rebus humanis postea vivitur et terra pede fedata calcatur: Ipsi, inquit, humani affectus sine quibus in hac mortalitate non vivitur quasi pedes sunt quibus humanis rebus afficimur, et sic afficimur quod si dixerimus quia peccatum non habemus nos ipsos seducimus et veritas in nobis non est. Ideo debemus lavare pedes mentis cotidie, cum oramus: Dimitte nobis debita nostra. Qui ergo est mundus totus secundum partes superiores anime carens mortali crimine indiget ut pedes lavet, cum solum beati sine macula sive ruga qui non calcant hanc terram peregrinancium et incolunt terram vivencium laverunt pedes simpliciter, ut dicitur Cant. Vᵗᵒ, 3. Valet ergo usus eukaristie ad memorandum gesta Christi, ut sit efficacius imitatus, sic quod quicunque celebrat missam vel [p. 178] audit cum oleo devocionis ungit devote corpus Christi cum Magdalena. Unde signanter dicit Christus Matth. XXVI°, 10 contra imitatores Scarioth qui remurmurant contra devotos quos vocant paplardos vel ypocritas, quod poterunt apcius prodesse pauperibus. Quid, inquit, molesti estis huic mulieri? Opus enim bonum operata est in me. Et sequitur: Amen dico vobis, ubicunque predicatum fuerit hoc evangelium, in toto mundo dicetur quod et hoc fecit in memoriam eius. Quicunque, inquam, sic ungit Dominum in sacramento altaris. Nichil debet esse in mundo quoad actus nostros famosius quam quod hoc debet facere in memoriam imitatoriam Jesu Christi; nam subvenire pauperibus est opus predicto inferius, ad quod semper est oportunitas temporis, dum hic vivitur. Sed oportet captare tempus ad sic singulariter celebrandum, quia solum dum est dolor ingratitudinis precedentis et devocio ad colendum corpus Christi pro nobis sic passi mortui et sepulti. Et hec racio quare nostri dicunt quod requiritur intencio consecrandi; requiritur, inquam, devota intencio ad memorandum sic sacramentaliter Salvatorem, quod si defuerit, est Christi irrisio et despectiva super Christum humoris fetentis infusio. Digne ergo manducatum corpus Christi valet pro vivis et mortuis, ut pena pro peccatis debita remittatur, ut vivus ex devocione amplius mereatur, et ut sanctum merendi propositum et per consequens ut gracia firmius et perseverancius habeatur, et sic utrobique delentur culpe tam veniales quam mortales occasione huius sacramenti.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 174.1: False arguments for transsubstantiation.
- 175.1: Three solutions of objections: I. Our opponents call accidents what Scripture calls bread and wine.
- 175.6: 2. Bread and wine are said not to exist in the sense that we need not care tor them.
- 175.11: 3. We do not limit God's power, but say that the acts ascribed to Him are contrary to His nature.
- 175.25: II. As to the disposition needed for the celebrant. (Cf. 163, 12.)
- 176.3: Not only actual mortal sin may indispose us, but a bad habit.
- 176.23: The right disposition is given by: 1. Love of Christ. 2. Peace with our neighbour. 3. Devoutness.
- 177.5: He who would communicate rightly must love God above all things and all things in relation to Him.
- 178.26: Great profit of the sacrament when rightly taken.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 174: *11:* (print = bt) [SUB]
  - 176: *VIᵗⁱ* (print = bt) [SUB]
  - 177: *meam* (print = bt) [SUB]
  - 178: *Christus* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 174:
4. Codd.: modi deest. 6. E: ut palet in illo. 7. ABCD: super
subiectalem. 9. Codd.: Johannis III. Correxi. 14. D: diffcrat.
19. D: generalum ; ib. D: inmisceret; ib. ABCD: cum vino. 20. D: acci-
dens ; CE: occidere. 21. D: per deest; ib. D: trinam. 26. D: primo.
3i. D : irractonalis.

p. 175:
2. E: Primo. 10. Codd.: signum. i3, 14. C: dicioncm — ad
vcrsarium alia mann. i3. D: oportet dcest. 17. ABC: ad hoc.
18. E: cis. 20. AB: quando dicunt; CE: cum dicit. 22. D: non potuit,
25, 26. ABCE: indisposite. 27. ABCE: vcncrabilc deest.
14. Jacob. IV, 1 5.

p. 176:
3. D : alia enim. 4. D : ad alia. 8. AB : quia deest.
8. 9. AHCD: supponere. 10. E: proftciat. n. B: secundum quod sit ;
ib. DE: peccatum deest. 12, i3. B: predestinacionis — praciam deest.
16. D: in deest; ib. D: ista modum. 20. D: et illa. 23. A: tercia in
textu; correxit supra hneam. 24. A: actualis in marg. a ia manu; in
textu : aciis. 25. D: in primo. 26 — 28. C: usque — mandatum in
marg. alia manu. 3i. C: ideo in marg. alia manu; ib. E: replicat.

p. 177:
3. E: temerariam. 4. AB: ut paulo. 17. ABCE: et deest;
ib. C: pede alia manu. 21. ABDE : peccata. 23. E: pedes dcest.
2. Joh. XIV, 27. i5. S. Augustini In Joh. Evang. Tract. LVI,
Opp. tom. III, 2, pag. 656, 6^7.

p. 178:
1. ABC: debite corpns. 4. C: murmurant. 5. D: sire ypocritas;
ib. B: poterant. 7. B: Et sequitur deest. 18. C: colendum in marg.
alia manu. 3i. ABDE: Sed non per se.
7-10. Matlh. XXVI, \3.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
(none recorded)
```
