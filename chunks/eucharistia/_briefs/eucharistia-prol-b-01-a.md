# Translation brief: eucharistia prol-b–01-a

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/eucharistia/wyc-eucharistia-prol-b.md chunks/eucharistia/wyc-eucharistia-prol-c.md chunks/eucharistia/wyc-eucharistia-01-a.md` once and fix what it reports.
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
   every §A–C term: `[accident]{g:accidens}`. The key must exist in GLOSSARY.md. A term that looks
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

## Glossary (the 423 rows these chunks use; the full file is GLOSSARY.md)

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
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |
| sacramentum (the eucharist); sacramentum altaris | sacrament; the sacrament of the altar | The plain sense, against the Augustinian row (*Incarn.*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.3, 3.30). |
| hostia; hostia consecrata | host; consecrated host | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.11, 1.22). |
| panis / vinum | bread / wine | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.8). |
| calix | chalice | The Douay word (1 Cor. 10:16). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.3). |
| corpus Christi / corpus Domini | the body of Christ / the body of the Lord | Kept apart as the Latin alternates them. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.6, 1.10). |
| novella ecclesia / antiqua ecclesia | the newer church / the ancient church | The pair of 3.3; cf. *novelli*. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 3.3). |

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
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| brachium seculare | the secular arm | Ruled 2026-09-28 (coordinator, delegated) (7 sites). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| graduacio; graduati | CONTEXTUAL: graduation / gradation; graduates | Academic "graduation" (Dialogus, 4 sites); of rank or lordship (*graduacio dominii*, *Pot. pape* 293.33, 297) "gradation". Ruled 2026-09-28; CONTEXTUAL 2026-10-12 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| conducentes | those who hire them | Ruled 2026-09-28. |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | CONTEXTUAL: condition / respect | "Condition": a person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). "Respect": the logical relation under which a predicate holds (*posiciones secundum habitudinem*), with a **C** note; ruled 2026-10-22 (Wilson; *Incarn.* 4.16). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| franchisia | franchise | Ruled 2026-10-02 (*Eccl.* 239.22). |
| leges ecclesie | the laws of the church | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.20, 1.23). |
| decretum; decreta | decree; the decrees | Gratian (*in decretis*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.14, 3.24). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| credulitas | credence | With *credere*, believe (*Dial.* 23.17–24.4). Ruled 2026-09-28. |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
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
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| glosare | to gloss | Interpret so as to remove the difficulty (T. p. 366). |
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
| glosa | gloss | The noun beside *glosare*. Ruled 2026-10-02 (52.10). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| dulia / latria | dulia / latria | Kept as the theologians' terms, glossed once per chunk. Ruled 2026-10-02 (95.17). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| incommunicans / incommunicantes (*nature*) | that do not communicate (with one another) | None predicated of, or shared with, another (Godhead, body, soul). Not "incommunicable": keep the participle. Ruled 2026-10-22 (Wilson; *Incarn.* 1.4). |
| assumere / assumpcio (*naturam*) | assume / assumption | Of the nature, as in the fathers. ⚠ Kept apart from the logician's *assumptum* "the assumption" (above): C note where the logical sense occurs. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| ydemptitas specifica | identity of species | That Christ and other men are of one species. Not "specific identity" (reads as "particular"). Ruled 2026-10-22 (Wilson; *Incarn.* prol, 8). |
| homo assumptus | the assumed man | A term of art (the Lombard's first opinion, *Sent.* III d. 6); keep "assumed" before "man", never "the man assumed". With the agent expressed (*homo assumptus a Verbo*) "the man assumed by the Word", which cannot be misread (coordinator, 2026-10-22). Ruled 2026-10-22 (Wilson; *Incarn.* 5.15). |
| secundum quod (reduplicative) | insofar as | ⛔ Never "in that" (heard as "because", which inverts the logic). Ruled 2026-10-22 (Wilson; *Incarn.* 5.29–6.24). |
| secundum deitatem / secundum humanitatem | as to the Godhead / as to the humanity | The rule of reduplication; keep it in Wyclif's place in the sentence. ⛔ Never supply "as God / as man" where the Latin has bare apposition (*ipse Deus*) or bare predication. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| natura | nature | Ruled 2026-10-22 (Wilson; *Incarn.* 3.4). |
| creatura / creator / creatus | creature / creator / created | ⛔ Never "creation" for the created thing. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| posicio / proposicio / predicacio | position / proposition / predication | Kept apart: the apparatus shows the three trading places (*Incarn.* 4.15). Ruled 2026-10-22 (Wilson). |
| sacramentum (of the incarnation, of creation) | sacrament | The Augustinian sense, "mystery" (1 Tim. 3:16): G note at the first occurrence in the chunk. Kept apart from *misterium*. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.8). |
| moderni doctores / moderniores doctores | the modern doctors / the more modern doctors | Ockham and the *moderni*, usually unnamed. Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.1). |
| sancti | the saints | The fathers. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.15). |
| probabiles doctores | reputable doctors | *Probabilis*: worthy of credence (cf. *probabiliter*). Ruled 2026-10-22 (Wilson; *Incarn.* 7.1) as "approved doctors"; changed the same day (coordinator) to free "approved" for *approbati*. |
| approbati doctores | approved doctors | Kept apart from *probabiles doctores*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 13.3). |
| determinacio | determination | A qualifying addition to a predicate (*cum determinacione*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 14.11). |
| sophistice | sophistically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 15). |
| de vi vocis / de vi sermonis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| determinaciones ecclesie | the church's determinations | Rulings of the church, not the logician's *determinacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 24). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| gracia unionis | the grace of union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| minoracio | lowering | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| individuum | individual | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 35.7). |
| in quantum (reduplicative) | insofar as | As *secundum quod*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37.9). |
| unio | union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 39). |
| diccio (logical) | word | A single term in a proposition. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 43.3). |
| intransitive | intransitively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 45.28). |
| in effectu | in actual fact | As against in potency or in name; ⛔ not "in effect" (modern "virtually"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 47.10). |
| animare | animate | The argument turns on it (45.30–46.4). Ruled 2026-10-22 (coordinator, delegated). |
| communicacio ydiomatum | communication of idioms | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.1). |
| predicacio actualis / aptitudinalis / habitudinalis / mixtim | actual / aptitudinal / habitudinal / mixed predication | *Habitudinalis* is its own term (the four MSS at 49.6), not under *habitudo*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.5–16). |
| denominativum | denominative | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 50.30). |
| Doctor Subtilis | the Subtle Doctor | Scotus. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.24). |
| convertibilis / converti | convertible / be convertible | Of terms. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 52.29). |
| quantus | quantified | The adjective beside *quantitas*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.22). |
| carneus / carnalis | fleshy / carnal | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.21). |
| moderniores loquentes | the more modern speakers | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 59.21). |
| ampliativus | ampliative | Beside *ampliacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 57.29). |
| dampnificare / dampnificacio | damage / damaging | Kept apart from *dampnum* "loss" and *dampnari* "be damned"; the argument of 65–68 turns on it. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 65). |
| per se / per accidens | of itself / by accident | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a (sufficienti) divisione | the topic from sufficient likeness / from (sufficient) division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| pretericio | being past | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| solvere / solucio (of the union) | loose / loosing | Except inside a Douay quotation (John 10:35 "cannot be broken"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| peccabilis | able to sin | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| inconsequens | inconsistency | Kept apart from *inconveniens* (an unfitting conclusion). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 78.23). |
| ydemptitas ypostatica | hypostatic identity | Beside *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 84.20). |
| capitales doctores | the chief doctors | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| eiusdem / consimilis / alterius racionis | of the same / like / another kind | The species-sense of *racio*; *racio speciei* "the account of the species" (Aristotle's *logos*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.4, 87.17). |
| principiari | be constituted from principles | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.7). |
| accidentatus | subject to accidents | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.4). |
| in recto / in obliquo | in the direct case / in an oblique case | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.25). |
| illusor | deceiver | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88). |
| signum / signatum | sign / thing signified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 91.2–6). |
| conveniencia / convenire (*in*) | agreement / agree | The argument of 90–91 turns on it; not "fittingness" (that is *congruencia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 90). |
| illusivus | deceptive | Beside *illusor*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 92.9). |
| predicacio synecdochica | synecdochic predication | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.27). |
| humidum infantile / radicale | the moisture of infancy / radical moisture | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 94.9). |
| conversari | live one's life (among men) | Beside *conversacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.25). |
| esse intelligibile | intelligible being | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 99.23). |
| extraneare / extraneacio (supposicionis) | estrange / estrangement (of supposition) | *Affeccio extraneandi* "an affection of estrangement". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 98.16). |
| ministerialiter | ministerially | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 100.17). |
| res racionis | thing of reason | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| significatum | significate | Kept apart from *signatum* "thing signified". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 111). |
| predicacio secundum essenciam / formalis | predication by essence / formal predication | Wyclif's modes of predication (cf. *predicacio secundum causam*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 115–116). |
| concepcio (figure) | conception | The grammatical figure. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habitus (of the humanity) | habit | The Lombard's third opinion (*Sent.* III d. 6). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| accidens | accident | The category; *accidit* "befalls". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habitacio | habitation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 120.14). |
| denominacio respectiva | relational naming | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 120.17). |
| figura / figuratum | figure / thing figured | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 121.23). |
| conversio (of a proposition) | conversion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.30). |
| racio (individual, personal) | account | *Racio individui / persone* "the account of an individual / a person", as *racio speciei*; not "aspect" (the row against *substancia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 8, 129–132). |
| vir (against *homo*) | man (*vir*) | Where Wyclif sets *vir* against *homo*, the Latin in parentheses. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 129.15–26). |
| res secunde intencionis | things of second intention | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.25). |
| materia proxima / remota | proximate / remote matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137.1). |
| colorate | with colour enough | With a plausible ground (cf. *color*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 134.26). |
| ydemptificare / ydemptificacio | identify / identification | Make the same (*idem*); the hypostatic union as identification, not conversion or generation. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 142.19, 147.22). |
| res communis / res communes | the common thing / common things | The realist universal the *moderni* do not conceive (first root of their error). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 144.27). |
| distinccio racionis | distinction of reason | Beside *differencia formalis*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 145.23). |
| conversio naturarum / confusio naturarum | conversion of the natures / confusion of the natures | Kept apart from *conversio* of a proposition. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 143.9). |
| moderni (bare) | the moderns | Beside *moderni doctores* "the modern doctors". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 142.10). |
| principiare (active) | be the principle of | Beside the passive *principiari* "be constituted from principles". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 147.4). |
| assumere personale | personal assuming | The infinitive used as a noun; kept apart from *assumpcio personalis* "personal assumption". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 146.33). |
| moderniores (bare) | the more modern | Beside *moderniores doctores* "the more modern doctors". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 151.17). |
| in quid (predicari in quid) | in quid | Kept in Latin (predication of what a thing is, as against *in quale*), glossed at first use in a chunk. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 162.22). |
| dependencia actualis / potencialis / obediencialis | actual dependence / potential dependence / obediential dependence | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 161.23–162.4). |
| substancia prima / substancia secunda | first substance / second substance | Aristotle, *Cat.* 5. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.25). |
| a simili | by likeness | Bare, as an argument form; beside *locus a simili* "the topic from likeness". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.16). |
| racio substancialis | substantial account | As *racio individui* "account". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.21). |
| doctores signorum | the doctors of signs | The logicians who reason from terms, not things. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.26). |
| sensibilis (in the definition of animal) | sentient | *Substancia animata sensibilis*: able to sense. Elsewhere the §D row "perceptible" holds; G note at first use. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 177). |
| ydemptitas numeralis | numerical identity | Beside *ydemptitas specifica* "identity of species". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 172). |
| accidens absolutum | absolute accident | Quantity and quality, against relative accidents. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 176). |
| augmentacio | augmentation | Growth in quantity (Aristotle's motion of increase). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 180). |
| beatificabilitas | beatifiability | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 181). |
| posicio anime | the laying-down of the soul | John 10:17–18; not the logical *posicio* "position", C note. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 183.3). |
| causancia / causacio | causing / causation | Kept apart (both at 187.30–34). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 185.16). |
| vicem supplere / vicis supplecio | supply the place / the supplying of a place | God supplying the place of a second cause. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 187.26). |
| multiplicative | multiplicatively | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 193.20). |
| habitudo relativa | relative respect | The "respect" sense of the CONTEXTUAL *habitudo* row. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 193.19). |
| remitti / intendi (of a quality, merit) | be remitted / be intensified | The intension and remission of forms; not *remissio* of sin. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 197.1–7). |
| in divinis | among the divine [persons] | Keeps "Godhead" for *deitas*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 196.18). |
| partes proporcionales | proportional parts | The halving division of a continuum. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 194.24). |
| multiplicacio dimensionalis | dimensional multiplication | One body in several places by its dimensions. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.6). |
| habitus (= possession, *habere*) | the having | The category of having, C note; kept apart from *habitus* "habit". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.14). |
| a maiori vel pari | from the greater or from the equal | Arguments *a maiori*; cf. *locus a maiori*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 209.5). |
| sensibile commune | common sensible | Aristotle's common sensibles (number, motion, figure); the term of art, against the §D row "perceptible". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 209.23). |
| communioritas | greater commonness | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 210.15). |
| multiplicacio concomitancie | multiplication of concomitance | Cf. *gracia concomitancie*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 213.21). |
| assertibile | assertible | The thing a proposition asserts. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 215). |
| exponentes | the exponents | The propositions into which a proposition is resolved (expounded). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 216.14). |
| homo communis | the common man | The universal man, with *res communis*; not "the ordinary man". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 218.3). |
| incommunicabilis existencia | incommunicable existence | Richard of St Victor's definition of person. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 218.11). |
| moderni loquentes | the modern speakers | Beside *moderniores loquentes*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 221.20). |
| signum reduplicatum | the reduplicated sign | The reduplicative word (*secundum quod*, *in quantum*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 230.23). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |
| infirmitas (of Christ's flesh) | weakness | Ruled 2026-10-22 (Wilson; *Incarn.* 5.31–6.11). |
| sacramentaliter | sacramentally | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| realiter | really | A mode adverb: one word each, never two merged, kept where Wyclif puts it. ⛔ Never "actually". Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| vere | truly | A mode adverb: one word each, never two merged, kept where Wyclif puts it. ⛔ Never "really" (that is *realiter*). Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| spiritualiter | spiritually | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| virtualiter | virtually | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| figurative | figuratively | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| tropice | tropically | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Kept apart from *figurative*. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
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
| secta signorum | the sect of the signs | Beside *doctores signorum*. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a, card). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office; *quale magisterium* "what a feat of mastery" (*Incarn.* 137.14) | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| recencius | more freshly | Pilot (*Dial.* 2.10) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| irreligiositas | irreligion | Ruled 2026-10-02. |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| brocardicum / brogardicum | brocard | The schoolmen's stock maxim. Ruled 2026-10-02 (*Eccl.* 16, 360.9). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| denominacio; denominare | naming; to name | The argument turns on it. Ruled 2026-10-02 (*Eccl.* 17, 391.17, 398.2). |
| dotes (docium) beatorum; dotes corporis | the dowries of the blessed; the dowries of the body | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| falsarius | falsifier | The opponent's epithet. Ruled 2026-10-02 (*Eccl.* 17, 414.6). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| quadriga diaboli | the devil's four-horse chariot | Ruled 2026-10-02 (*Eccl.* 18, 427.12). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| continuacio (of bodies, the act) / discontinuacio; continuare / discontinuare | continuation / discontinuation; make continuous / make discontinuous | The making of several bodies into one continuum (*Incarn.* ch. 12), G note at first use: not "carrying on". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.30, 211.12). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| dampnacio | CONTEXTUAL: damnation / condemnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). Of a judgement passed on a teaching (*dampnacio istius sentencie tamquam heretice*, *Pot. pape* 84.10) "condemnation"; ruled 2026-10-07. |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| incompossibilis | incompossible | Beside *compossibilis*. Ruled 2026-10-02 (*Eccl.* 22, 522.1). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| memoriale | memorial | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| premium accidentale | accidental reward | Ruled 2026-10-02 (*Eccl.* 23, 565.6). |
| venia | forgiveness | Kept apart from *condonacio* "pardon". Ruled 2026-10-02 (*Eccl.* 23, 573.4). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| remissio; remittere | remission; to remit | Headword row (cf. *condonacio* "pardon", *venia* "forgiveness"). Ruled 2026-10-02 (*Eccl.* 23). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| criminosus | criminous man | Ruled 2026-10-07 (*Pot. pape* 06-c). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| quaternarius / denarius / quadragenarius | the four / the ten / the forty | Number exegesis (the 153 fishes, ch. 7). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 154–155). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| infundabilis; infundabiliter | without foundation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 195–196). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| memorativa potencia | memorative power | A faculty of the soul (the "power" sense of *potencia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 219.27). |
| discrasia | distemper | Physicians' term. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 223.1). |
| primicia (virtutum) | being first (in the virtues) | Kept apart from *primatus* "primacy" and *primitas* "firstness". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 228.33). |
| replicatur; replicatum | it is rejoined; rejoinder | A further objection against an answer; kept apart from *respondetur* "the reply is" (so 04-b). Ruled 2026-10-08 (coordinator, delegated; conformed 10-e, 10-g). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| cultus Dei | worship of God | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-d). |
| pontifex (Old Testament, unqualified) | pontiff | Kept apart from *sacerdos* "priest"; *summus pontifex* of the Jewish priesthood is "high priest" (see *summi pontifices*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* ch. 11). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| gradus (of belief) | degree | The four degrees of belief (*Pot. pape* 327.18 ff.). Ruled 2026-10-12 (coordinator, delegated). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| episcopi cesarei | caesarean bishops | Extends *prelatus / sacerdos cesarius*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 331.24). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| proventus | proceeds | Kept apart from *redditus* "revenues". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 353.25). |
| decimacio | tithing | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 359.26). |
| decimantes | tithe-payers | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 359.24). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |
| coloracior | more colourable | Comparative, with the *color* / *colorabilis* rows. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 384.15). |
| diccio procuratoria | proctorial pronouncement | C note gives *dicio* "authority" as the alternative. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 386). |
| specularis prudencia | the prudence of a watchman | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| suadere | make the case | To persuade, not to prove. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 399.2). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |
| nimis | exceedingly | Medieval intensive (= *valde*); "too much" only where excess is the point. Ruled 2026-10-12 (close-out R2; *Pot. pape* 169.2). |
| sentire (the sacrament, the body) | perceive | "sense". As *sensibilis* "perceptible". Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.10, 1.17). |
| singulariter | alone, only | "singularly". Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 4.14). |
| recitare | recite | To report, rehearse. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.4, 3.10, 4.18). |
| narrare | relate | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.9). |

---

## Chunk prol-b: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-prol-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-prol-b
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "4.26–8.29"
divisions: "prologus (heading 'PROLOGUS.' at 1.0); part 2 of 3, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "880 words; 875 confirmed by the vote; 3 runs stood by rule; 2 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n75–n79 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, prologue, part 2: [TITLE]

## ¶1 · 4.26–6.2

> [p. 4] Capitulum quintum replicat de locucione tropica secundum modernos doctores et solvit. Secundo replicat per doctores antiquiores et solvit, ita quod tangit primo Scotum, Henricum et dominum Armachanum, ubi docet tripliciter quod hoc decretum Ego Beringarius non est abrogatum. Sed post tanguntur [p. 5] alii doctores provecciores, primo Petrus Lombardus, ubi ostenditur quod ipse non repugnat huic sentencie, et tollit evidenciam Bonaventure et solvit, declarans quid concluditur ex dictis multis sanctorum et decreti quod Eukaristia est panis et vinum sacramentaliter consecrata. Secundo replicat per Anshelmum et declarat ex testimonio suo et racionibus quod accidens non potest esse sine subiecto, et ostendendo quid Augustinus sentit de quantitate declarat quomodo ista via magnificaret ulterius Dei potenciam ponendo hostiam infinitum magis gloriosam quam modo sompniat, et quomodo error istius materie induxit in multos alios errores. Quarto obicit per hoc quod multi sancti canonizati moriebantur in ista fide de Eukaristia. Et allegat sanctum Thomam probantem quod via dicens panem remanere post consecracionem est incompetens, inpossibilis et heretica, et primo tollit evidenciam ex testimonio triplici quod non probatur multos sanctos in ista fide de Eukaristia decessisse. Secundo dicitur probabiliter, quod multe sancti Thome sentencie sunt corrupte. Tercio declaratur tripliciter quod non est de substancia fidei credere quod post benediccionem non remanet substancia sacramenti et colorat concordancias decreti Nicholai IIⁱ et decretalis Innocencii IIIⁱⁱ in hac parte. Quarto infringitur trimembre argumentum per quod sanctus Thomas videtur probare incompetenciam huius sentencie. Quinto probat sextupliciter falsitatem porismatis, per quod nititur Thomas probare inpossibilitatem huius sentencie. Sexto obicitur tripliciter contra evidenciam hereticantem sentenciam [p. 6] istam et declaratur quam irreligiose procedit ista secta in condempnando sentenciam quam ignorat.

[ENGLISH]

## ¶2 · 6.3–6.29

> [p. 6] Capitulum sextum declarat quomodo .homo dignificabit se ut communicet sacramento; et primo declarat quomodo oportet quod habeat habitus et opera virtuosa. Secundo descendit ad tres virtutes theologicas quas oportet omnis habere, et narrat quomodo ipse verse sunt in vicia. Tercio descendit ad actus, narrando quod quatuordecim secundum exposicionem beati Gregorii in esu agni paschalis fuerant; quod mirabiliter prodesset fidelibus sacramentum Eukaristie memorando. Quarto obicit tripliciter et dissolvit, primo per hoc quod in legendis et lege ecclesie canitur quod sacramentum sit accidens sine subiecto; et solvendo declarat ex testimonio Augustini quomodo se homo habebit ad talia docens triplici medio, quomodo cultores accidencium reduci poterint ad ecclesiam primitivam. Secundo obicit per hoc, quod sacerdotes sunt nimis fragiles ad celebrandum nec habet hostia virtutem ad peccata tollendum ac graciam acquirendum; et solvit declarans quomodo in ista materia populus est delusus. Tercio obicit per hoc quod errantes in ista materia forent puniendi tanquam heretici, quod tamen declarative concedit, dicens quod variacio opinionum in ista materia prenosticat opiniones plurimorum criminum et virtutum, et descendit ad opinionem triplicem et usum ecclesie Anglicane et invehit contra illas ex testimonio Rabani et aliorum, eliciens quid cultores talis accidentis prenosticant.

[ENGLISH]

## ¶3 · 7.1–8.3

> [p. 7] Capitulum septimum introducit materiam de ydemptificacione; contra quam arguit septempliciter, et arguit pro ydemptificacione, primo pro idemptificacione individuorum in specie et genere, et dissolvit. Secundo replicatur per hoc quod hoc sacramentum est uni una qualitas et alii alia; et dissolvit negans illud, declarans quod qualitates non poterunt per se esse ex parte qualitatum anime. Et solvit tria argumenta, declarans multipliciter quomodo accidens varie denominat. Et tercio ostendendo quomodo Deus videtur declarat novem genera visionum. Et solvit quatuor obiectus quibus suadetur Deum videri oculo corporali. Quarto solvit tercium obiectum factum pro ydemptificacione per hoc quod panis fit corpus Christi, ubi declarando sensum istius ostendit qualis est virtus sacramenti et quomodo non sufficit facere panem esse idem corpori Christi. Et ultimo solvit quartum obiectum de inpanacione, exponendo primo et colorando posicionem; secundo narrat originem huius vie et quid sibi contingit ac quam sinistre glosantur dicta sanctorum et leges ecclesie ex ista infecta radice. Et tercio probat tripliciter quod sentencia ista de inpanacione est heretica, primo quia scriptura sacra et sancti doctores in verbis asserunt, ut allegant beatum Augustinum dicentem quod panis est corpus Christi, secundo per hoc quod quidditas panis non potest esse ydemptice quidditas carnis, et tercio per hoc quod ecclesia non est difficultata in fide sine magna racione; sed non est racio, ymmo inconvenientis multiplicis implicacio ponendo inpanacionem. Et exponit decretum ecclesie quod videtur [p. 8] contrarium narrans tres logicas in ista materia et quomodo usus earum est secundum epikeyam pro loco et tempore adaptandus.

[ENGLISH]

## ¶4 · 8.4–8.29

> [p. 8] Capitulum octavum exponendo et limitando sensum multitudinis probat sextupliciter quod nullum corpus idem in numero potest multiplicari simul et semel dimensionaliter per diversa loca. Secundo obicit tripliciter et dissolvit, primo per hoc quod multa corpora possunt esse per eundem locum, ubi docet quod corpora appropriate replent loca, secundo ex miraculo de beato Ambrosio quod dissolvit tripliciter; et tercio ex scriptura sacra triplici de multitudine corporum et de augmentacione; que omnia dissolvit exponendo illud Matth. XVᵒ: Omne quod intrat in os etc. Tercio principaliter resumendo sentenciam Doctoris Communis tractat si tempus componitur ex instantibus, arguit quadrupliciter contra ipsum in materia de tempore discreto ex vicissitudine affeccionis angelice resultante, recitando in ista materia responsivam distinccionem de duplici tempore, et arguit sextupliciter contra illam; et sic descendit ponendo quiete sentenciam triplicem, scilicet Dei, angeli et nature moralis temporalis. Quarto principaliter describendo multitudinem et distinguendo de esse in loco et esse per locum declarat quomodo corpus Christi multiplicatur in Eukaristia, et quale esse habet ibi; et concludit in quibus et qualiter credi debet ecclesie, quia in materia fidei precise de quanto se fundat efficaciter ex scriptura.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 4.26: Chapter V.
- 6.3: Chapter VI.
- 7.1: Chapter VII.
- 8.4: Chapter VIII.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 4: *Beringarius* (print = bt) [SUB]
  - 8: *XVᵒ:* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 4:
1. D: qnod quesit. 2. D: qualiter proposicio ; ib. D : et qualiter.
f>. C: et in marg. alia manu; ib. D: quo ccclesia ; ib. BCD : ccdesia que.
7. D: ritibus deest. 10. ABDE: sequitur. i3. D: qualiter Spiritus
Sanctus; ib. I) : se variavit. 14. D : et qualiter. i5. calicis; E: in aliquo.
20. D: proponit; ib. E: Romane curie. 22. AB: questionem deest.
25. ABC: sacramentis (error ut videtur legentis); ib. B: vcl de\oli.
27. C: et solvit in marg. alia manu. 20, 3o. BCD: Ardmachanum;
E: Ardmacanum. A in marg. alia manu : Armichanum.

p. 5:
r, 2. ABCD : Lumbardus. 4, 9- quid; rectius: quod. 5. D : ac vinum.
5, (5. D: sacramentaliter confectum. 9, 10. E: oslendit quomodo.
II. C: hostiam in marg. alia manu; ib. infinitum; D: in singulari.
i3. ABC: Tercio obicitur. 16 B : panem dcest; ib. D: se manere.
17. B: et incompetens. 22. B: declarat. 24. B: remaneret ; C: rema-
neat; D: manet. 27. ABCD : sanctus deest; ib. E: improbare.
28. C: tripliciter. 29. ABCE: porisomatis ; D: perisomatis ; ib. D: in-
teltigitur Thomas. 29, 3o. E: improbare. 3o. DE: obicit.

p. 6:
1. BCDE: dcclarat. 2. D: quam ignorat dccst. 3. ABC : Scxlum
capitulum. 4. A: convincct in textu; communicct in marg. 7. omncs ;
DE: omnino. 8, 9. 1): narrando quod deest; E: quod dccst.
10, 11. AB: monstrabiliter ; A in marg. alia manu: mirabilitcr. 14. ABDE:
canctur. E: homose; ib. B: habit; ib. D: triplici modo. 17. D: po-
tcrunt. 19. sunt nimis; E: ccrnimus. 20. liostia ; DE ct C in marg. :
Eukaristia. 21. C: rcquircndum. 22. D: illusus. 23. B: matcria
dccst. 23, 2|. tamquam; \i: sicut. 26. E: et criminum; virtulum dccst.
29. B : quod cultorcs.

p. 7:
2. E: arguitur. 2, 3. Codd. : septemplicitcr secundo arguit. Corrcxi.
3, 4. B: primo — ydemptificacioue dcest; D: pro ydemptificacione de
ydemptificacione. 4. E: in generc et specie. 5. E: replicat; ib. DE:
quod illud. 10, 11. D: ostendit . . . . et declarat. 12. D: abiectus.
16. AB : facere deest. 18. D : obiectum et. 18, 19. A : colorando peecatum.
20. H: quidsit; D: contingit. 24. ABCD : allegat. 27. D : ydemptifice.
29, 3o. D : inconveniens.

p. 8:
1. D: narrantis. 2. ABC : USUS corum; ib. D : epykeram. 3. D: aa
optandus; B: aptandus ; ad supra lin. 7. B : obicitur. 8. A: pcrhoc
in marg. alia manu. 12. DE: sacra dccst. i3. E: de dccst. 16. E: si
tunc. 23. moralis; ABCD : vwbilis. 24. ABC: et diccndo.
26. C: Christi in marg. alia mann; ib. 1 1 : multipliciter . 29. ABC: ex
scriptura efficaciter; D : efficaciter de scriptura. 3i. AB : in Innocen-
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 4: Ego Beringarius | \m ducaturi estis et bibituri illum sanguhiem que\ effusuri sunt Hli qui me crucifigent, | ipsum quidem et non ipsum, ipsum invisibiliter, non ipsum visibiliter; necesse est, | celebrari illud visibiliter, necesse? est tamen invisibiliter intelligi. | Siper negligenciam aliquid de sanguine stil- | laverii super terrtWl) UngM lambetur; si super tabulani, tabula radetur, sicut terra vel aliud ipsum recipiens, et igne consumetur et cinis iuxta altare | visibiliter non. | est eius. | nec sanguini commiscetur, sed accidentibus prioris vini commixtum corpori quod sub eis latet undique circumfunditur non madidans circumfusum, ipsa tamen accidencia vinum appositum videntur afficere, | quia si aqua fuerit apposita, vini saporem assumit. Contingit igitur accidencia mutare subiectum, sicut contingit subiectum accidencia permutare: cedit quippe natura miraculo et virtus supra consuetudinem operatur. | que asserit tam aquam quam vinum in Christi sanguinem transmutari. | patet pliilosophis | quod aqua; | ymmo sepe. | est calor; | quod qua solum vertitur. | in vinum convertelur. | aquam — in
p. 5: Qiiod Jit vinum sanguis Christi, Etsi sensus deficit. | Consencio autem sancte Romane ecclesie et apostolice sedi, et ore et corde projiteor de sacramentis dominice mense eandem Jidem | me tenere quam dominus et venerabilis papa Nicholaus et hec sancta sinodus auctoritate evangelica et apostolica tenendam tradidit michique firmavit, scilicet panem et vinum que in altari ponuntur post consecracionem non solum sacramentum sed eciam ooverum corpus et sanguinem domini nostri Jesu Christi | et tandem. | Fitaue sanguis Christi merum, etsi sensus deficit. | sedi deest. | flt vinum. | ad consecrandum. | in se. | forma cuius.
p. 6: esse sensualiter, non solum sacramentaliter sed in veritate manibus sacerdotum tractari etfrangi et fidelium dentibus atteri, iurans per sanctam et omousion Trinitatem et per hec sacrosancta Christi evangelia. Eos qui contra hanc fidem venerint cum | dogmatibus et consecutoribus suis eterno anathemate dignos esse pronuncio. | Bibebant autem de spirituali consequente eos petra, petra autem erat Christus. | per panem et vinum speciem panis et vini y | Species et similitudo earum rerum vocabula sunt que ante fuerant, scilicet panis et vini; unde in fine cuiusdam misse oratur et dicitur: Perficiant in nobis, quesumus, Domine tua sacramenta que continent, ut que nunc sub specie | gerimus rerum veritate capiamus. | ct sensnaliter. | et speciem vini; | species panis. | nunc invicem; | et vini | in islo | in die. | Panem, id est, specie panis et vini esse sacramentum tantum. | Hoc videtur. 2. rino; | subtilia quoquo; | vero in quo. u. | ut ut. | ul ignoranter. 2.\.
p. 7: ego dico | Quid maius est Christo aut quid poterit corpori et sanguini | eius anteponi? Si presbiter Christum consecrat, cum in altari sacramenta benedicat, benedicere populo non debet qui Christum consecrare non metuit? | per idem per hec. | ut dictum est; | distinccione cst; | que Christum; | esse sacramenta. | et tamen — Christi | sicut et. | sine summo; | sine synonimo. | secundus Benedicto eiecto, sedit in papatu annis pene duobus, cuius diebus Gallicana ecclesia plurimum perturbatur per Beringarium | Turonensem qui asserebat eukaristiam non verum corpus Christi esse sed Jiguram. Contra quem Nicholaus papa concilium celebravit in quo Beringarius errorem suum retractavit y sicut habetur in De Consecracione distinccione II a , capitulo | Lamfrancus eciam Beccensis abbas tonantem librum contra eundem edidit quem Scintiliarium intitulavit; post hec Beringarius sancte vixit et obitum suum predixit. | inutile dubitabo; | populitm perturbatur. | quarum tercia
p. 8: Omne quod intrat in os | in Innocencius. | quas dtcebantur. | lamen quomodo. | sacrijicare est. | corpus Christi. | equivocetur tam. | jbgo Benngarius, | sed non. | tamen post; | cognoscere quid. | propter procedet; | in secunda. | qui colunt. | Vix tamen; | vix aliter; | doctoribus vel complicibus. 22. tercia; | scilicet cuiusmodi est. | in niti parte. 1,
```

---

## Chunk prol-c: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-prol-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-prol-c
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "8.30–10.18"
divisions: "prologus (heading 'PROLOGUS.' at 1.0); part 3 of 3, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "350 words; 349 confirmed by the vote; 1 runs stood by rule; 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n79–n81 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, prologue, part 3: [TITLE]

## ¶1 · 8.30–10.18

> [p. 8] Capitulum nonum arguit multipliciter contra dicta, primo per hoc quod Innocencius IIIᵘˢ cum mille trecentis [p. 9] et quindecim diffinierunt hodiernam sentenciam, et respondet tripliciter, primo per hoc quod non docetur quod aliquis eorum fuit membrum ecclesie, secundo quod illorum sentencia est glosanda, et tercio quod non est credendum homini in materia fidei nisi de quanto dictum suum docuerit ex scriptura. Et narrat causam multiplicem quare diffinicio Innocencii est suspecta. Secundo arguit per hoc quod decretum Nicholai est in eadem dampnacione, et respondet assignando causam multiplicem quare testimonium illud est pocius, et declarat quomodo in materia fidei credi debet doctoribus et quomodo Augustinus ex fide scripture invexit contra Donatistas. Qua sentencia servata hodie non foret ecclesia tot creditorum novitatibus onerata. Et describit opera huius Innocencii, ut eius auctoritas plus patescat. Tercio arguit ex testimonio doctorum, legis Dei et legis ecclesie; et respondet declarando quomodo nemo debet accipi nisi ut testis veritatis. Et exhinc variantur gradus credendi hominibus adiecta causa quare non debet credi isti sentencie; et descendit ad tres evidencias Lanfranci qui videtur fuisse unus de primis cultoribus accidentis. Quarta racio obicit de multitudine sanctorum et famosorum doctorum istius sentencie et retorquet ad oppositum, quod sancciores et famosiores illis tenuerunt contrarium; quare ergo non credimus illis? Et declarat primo auctoritatem Romani episcopi et quomodo ex lege propria est infirma et quomodo pape instarent pro declaracione istius fidei, cum [p. 10] videtur scriptura vocare Eukaristiam panem et quid figurat quod cultores signorum tanquam ydolatre contendunt infundabiliter circa hoc signum. Quinto obicit sextupliciter quod corpus Christi non est quantum in Eukaristia et respondet solvendo tres obiectus narrat quomodo Deus habet esse per loca differenter a creaturis et quomodo dissonat claritati corporis Christi esse in hostia. Sexta obieccio tractat quomodo corpus Christi manducatur et movetur in hostia et recitando dictum Damasceni narrat periculum huius erroris et quomodo maius miraculum est cognacio Christi cum membris suis quam Eukaristia. Septima obieccio declarat qua adoracione est hostia adoranda et quomodo sacerdotes debent communicare bona ecclesie que iacent in manu eorum mortua ad defensionem regnorum, quod probatur tripliciter regno Anglie pertinere; et recitat tres sophisticaciones cleri in quibus populus est illusus.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 8.30: Chapter IX.

## Notes

## Transcription notes
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 8:
1. D: narrantis. 2. ABC : USUS corum; ib. D : epykeram. 3. D: aa
optandus; B: aptandus ; ad supra lin. 7. B : obicitur. 8. A: pcrhoc
in marg. alia manu. 12. DE: sacra dccst. i3. E: de dccst. 16. E: si
tunc. 23. moralis; ABCD : vwbilis. 24. ABC: et diccndo.
26. C: Christi in marg. alia mann; ib. 1 1 : multipliciter . 29. ABC: ex
scriptura efficaciter; D : efficaciter de scriptura. 3i. AB : in Innocen-

p. 9:
i. AC: qui diffiniunt; B: qui diffinierunt; CD: qui deest. 4. illo-
rum; E: eorum. 5. C: homini in marg. 6. nisi ; E: aut. 7. quare ;
DE: qualiter. 8. D: sit suspecta. 10. E: allegando; ib. D: multitudinem ;
ib. quare; DE: qualiter. i3. C: ex fide in marg. al. manu ; ib. C: scrip-
feredeest; ib. ABD : Donastistas. 14. qua ; D: quia; ib. hodie; D: hoc
modo. 19. E: debet capi ; ib. C: ex hoc. 20. E: in hominibus.
21. B: et deest. 24. A: sentencie in marg. alia manu. 25. D: opposita ;
l>E: ad documentum. 26. D: tenuere. 27. C: primo deest; ib. E :
auctoritate. 28, 29. C: et quomodo pape in marg. alia manu.

p. 10:
i. B: vacari; D : vocari. 2. B: cultoeres. 6—8. B: per loca — esse
dccst. 11. A: inanis miraculum ; ib. B: quomodo dccst; ib. B : maius
periculum; A in tcxtu pcriculum ; miraculum in marg. alia manu; ib. B:
cognicio. 11, 12. Codd.: cognacio Christi et vino (M: viam) Christi. Vide
infra: Ista quidem cognacio que ex tanta aucloritate procedit cum verbo
substandi foret lonye melior quam conficere . ... i3. C: hostia in marg.
alia manu. 14. BD: conimunicari.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 8: Omne quod intrat in os | in Innocencius. | quas dtcebantur. | lamen quomodo. | sacrijicare est. | corpus Christi. | equivocetur tam. | jbgo Benngarius, | sed non. | tamen post; | cognoscere quid. | propter procedet; | in secunda. | qui colunt. | Vix tamen; | vix aliter; | doctoribus vel complicibus. 22. tercia; | scilicet cuiusmodi est. | in niti parte. 1,
p. 9: Cum Marthe. | ista simul. | et specialiter. | ut sunt. | ideo non; | invisibililer absconditus; | est absconsus. | illa elc. | cap. secundum | ut supra | secunda potencia. | data dicione. | et dicere; | finem hostie. | monuit me. | quod mille CXIIII. | aut vinum; | cuius decet; | cuius dicte; | cuius deest cognoscere.
p. 10: Ego Beringarius, | Credo panem et vinum que in altari ponunturpost consecracionem non solum sacramentum sed eciam verum corpus et sanguinem domini nostri Jesu Christi esse sensualiter non solum sacramentum, 2? sed in veritate manibus sacerdotum tractari etfrangi etfidelium dentibus atteri. | vel condensari. | consonum ipsum videtur. | et huiusmodi; aliud | ut aliud; | huiusmodi hoc vel. | quod ipse | corpus Christi. | nisi in solo sacramento. | hoc est sacramentum, | hostia ista est ponderositas sed non est ponderosum. | sicut se ; | sic ad. | duos alios. 6. | de ipsa cognoverit. | quia hoc est. | quid hoc. | quod sit; | Si per negligenciam. | Si per ncgUgenciam | In terranx.
```

---

## Chunk 01-a: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-01-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-01-a
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "11.2–15.26"
divisions: "cap. 1 (heading 'CAPITULUM PRIMUM.' at 11.0); part 1 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "930 words; 913 confirmed by the vote; 16 runs stood by rule; 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n82–n86 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 1, part 1: [TITLE]

## ¶1 · 11.2–11.16

> [p. 11] Tractando de Eukaristia oportet premittere quedam communia plus famosa et primo utrum sacramentum altaris sit realiter corpus Christi. In qua materia dixi sepe populo quod in sacramento altaris est tria considerare, scilicet nudum sacramentum sic quod non rem sacramenti ut hostiam consecratam; secundo sacramentum et rem sacramenti ut verum corpus Christi et sanguinem; et tercio rem sacramenti et non sacramentum ut unionem Christi cum corpore suo mistico quod est ecclesia; hoc enim nusquam est sensibile et per consequens non est alicubi sacramentum. Per hanc fidem tolluntur instancie paganorum. Arguunt enim quod sus, canis vel mus potest comedere Deum nostrum, quia corpus Christi quod est Deus.

[ENGLISH]

## ¶2 · 11.17–12.2

> [p. 11] Sed respondemus eis iuxta fidem predictam quod infideliter falsum assumunt, cum tales bestie possunt comedere hostiam consecratam que est nudum sacramentum et non corpus Christi vel sanguis. Ymmo sicut leo comedens corpus hominis non comedit eius animam, licet sit ad omnem punctum illius corporis, sic intelligendum est de corpore Christi in sacramento altaris. Ipsum enim est totum sacramentaliter, spiritualiter [p. 12] vel virtualiter ad omnem punctum hostie consecrate, sicut anima est in corpore.

[ENGLISH]

## ¶3 · 12.3–12.6

> [p. 12] Secundo obiciunt per hoc quod nos sacerdotes frangimus corpus Christi et per idem caput, collum, brachia et singula eius membra; quod foret maxime horribile facere Deo nostro.

[ENGLISH]

## ¶4 · 12.7–12.17

> [p. 12] Sed nos respondemus iuxta fidem priorem quod infideliter falsum assumunt, cum frangimus sacramentum vel hostiam consecratam, non autem corpus Christi, cum distinguuntur, sicut non frangimus radium solis, licet frangamus vitrum vel lapidem cristallinum. Et hec videtur sentencia cantus ecclesie quo canitur: Fracto demum sacramento Non vacilles sed memento Tantum esse sub fragmento Quantum toto tegitur.

[ENGLISH]

## ¶5 · 12.18–12.24

> [p. 12] Cum ergo negare non possumus quin sacramentum frangatur, ut docet usus ecclesie, et sensus forent aliter illusi ex sophismate veritatis, et corpus Christi non frangitur, manifestum est quod illud sacramentum quod frangitur, non est corpus Christi, quia aliter querenti quid frangitur minus vere diceretur quod corpus Christi: quid enim querit de substancia rei.

[ENGLISH]

## ¶6 · 12.25–12.29

> [p. 12] Tercio obiciunt per hoc quod nisi corpus Christi foret hostia consecrata, nos non videremus corpus Christi nec comederemus, sicut nec dente conterimus, et per idem non assumeremus; quod foret inconveniens christianis.

[ENGLISH]

## ¶7 · 13.1–13.17

> [p. 13] Sed hic respondemus per distinccionem quod est dare duplicem visionem, duplicem esum et duplicem sumpcionem, scilicet corporalem et spiritualem; et sic concedimus quod non videmus in sacramento illo corpus Christi oculo corporali sed oculo mentali, scilicet fide per speculum in enigmate. Et sicut ymago est integra ad omnem punctum speculi, sic quod videri potest vel secundum partem vel totum ab aliquo oculo corporali alicubi posito: sic intelligendum est in parte de corpore Christi in hostia consecrata ut speculo. Et eodem modo dicitur quod non tangimus vel capimus corpus Christi tactu corporeo, sicut nec corporaliter ipsum comedimus. Et iste est sensus cantus ecclesie quo dicitur: Quod non capis, quod non vides Animosa firmat fides Preter rerum ordinem.

[ENGLISH]

## ¶8 · 13.18–13.24

> [p. 13] Nec conterimus corpus Christi dentibus sed spiritualiter integrum ipsum accipimus. Et sic intelligimus istum cantum quo dicimus: Nulla rei fit scissura, Signi tantum fit fractura Qua nec status nec statura Signati minuitur.

[ENGLISH]

## ¶9 · 13.25–14.15

> [p. 13] Sed hic obiciunt quidam de nostris quod ista non sunt dicenda laycis qui nec ipsa concipiunt nec observant, cum ex istis fidem priorem amitterent. Sed nichil obiecto isto insanius; nam tam layci quam clerici nimis multi sunt tantum infideles in ista materia quod credunt paganis deterius quod hostia [p. 14] illa consecrata sit Deus illorum; et tunc indubie concludunt predicta argumenta paganica. Ille ergo qui non concipit ista male conciperet fidem de Trinitate vel incarnacione. Nec est fides predicta layca fides qua placeretur domino veritatis, sed infidelitas pessima quia ydolatria qua creatura valde abiecta non assumpta coleretur infideliter tamquam Deus; et sic secundum istam stulticiam nunquam doceretur vel argueretur aliquis error in fide, sed ne deterius contingat christianus valde disciplinabilis in infidelitate sordesceret, ac si diceretur quod spina in pede, telum in carne vel quecunque venenosa causa morbi in corpore non debet extrahi, ne forte contingat deterius. Episcoporum itaque est destruere has hereses, quia aliter ipsi forent heretici ex consensu.

[ENGLISH]

## ¶10 · 14.16–14.18

> [p. 14] Secundo obiciunt per hoc quod promulgata laicis ista sentencia vel vilesceret vel saltem minoraretur honor et devocio populi ad hoc venerabile sacramentum.

[ENGLISH]

## ¶11 · 14.19–15.7

> [p. 14] Sed ista ficticia currit sub eadem perfidia. Nam Apostolus dicit Rom. III°, 8: Absit ut faciamus mala ut eveniant bona, ergo multo magis fidelis diceret: Absit ut committamus ydolatriam, ut ex falsa et infideli devocione populus amplius seducatur, quia revera paulo minus evidenter crederetur a populo, quod calix in quo est sanguis Christi et lignum per quod colitur crucifixus sunt realiter Deus noster. Sicut enim viso calice in tantum cultum prorumpimus sicut visa hostia consecrata, non propter ipsum calicem consecratum a pontifice sed propter sacramentum eximium in vase absconditum: sic visa [p. 15] hostia debemus credere quod ipsa non sit corpus Christi, sed ipsum corpus Christi est sacramentaliter in ipsa absconditum. Et iste sensus ecclesie est quem canit: Sub diversis speciebus, Signis tantum et non rebus, Latent res eximie.

[ENGLISH]

## ¶12 · 15.8–15.17

> [p. 15] Et patet quod destructo errore ydolatrie plus et purius coleretur Deus quam modo colitur, quia credendum est quod Christus in sacramentis illis presens absconditur. Quare ergo non coleremus Christum visa hostia, sicut facimus viso calice et sicut fideles devocius colunt maiestatem divinam visa qualibet creatura? Detecta ergo ista sentencia foret cultus verus et debitus placens Deo, ymmo iam est cultus mendacii abhominabilis Deo vero. Et ista est vera sentencia licet displiceat pontificibus ydolorum.

[ENGLISH]

## ¶13 · 15.18–15.26

> [p. 15] Tercio obiciunt per hoc quod sic vilesceret sacerdotalis potestas cum non habet potestatem consecrandi vel faciendi corpus Christi vel sanguinem, ymmo videtur quod sicut laycus videndo quamlibet creaturam videt in fide deitatem que est plus quam corpus Christi, sic videndo quamlibet creaturam fideliter sufficienter accipit corpus Christi. Sed quis tunc audiret missam, missantes care conduceret vel acciperet more ecclesie sacramentum?

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 11.2: Three things to be considered in the Sacrament: 1. The Sacrament or symbol: the host;
- 11.7: 2. the Sacrament and res sacramenti: Christ's body; 3. the res sacramenti: the union of Christ with the Church.
- 11.16: A beast may eat the host but does not eat the body.
- 12.3: Nor does the priest break Christ's body.
- 12.25: We must not confuse spiritual and bodily reception.
- 13.25: These truths may be preached to laymen to save them from heathen errors.
- 14.16: Such preaching is said to lessen the honour paid to the Sacrament.
- 14.19: We must not commit idolatry under pretence of increasing devotion.
- 15.8: We should recognize that Christ is hidden in the Sacrament.
- 15.18: This does not really lessen the priestly power.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 11: *Christi.* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 11:
2, 3. D: questiones aut communut. 5. C: altaris in marg. alia matm.
6. D: considerari ; ib. E: sicut. 8. ABE: et verum. 10. AUCE: et
unionem. 14, i5. D: vel canis. iS. E: possent. 20. B: et sanguis.
20, 2i. CE: ideo sicut. 24. C: euim in uarg. al. man.
5. Cf. Trialogum, lib. IV, cap. II, pag. 248.

p. 12:
3. AB: Et sic obiciunt. 8. B: falsum d^est: ib. D: assumant.
16. AE: fragmentis. 17. B: quanto. 19. C: frangilur. 21, 22. C:
manifestum — frangitur in marg. alia manu. 28. D: assumendum.
14 — 17. E sequentia S. Thomae de Aquino: Lauda Sion
Salvatorem. Cf. Daniel, Thes. hvmnol. II, 98. Cf. Daniel Cod.
lit. I, 122.

p. 13:
I. D: per divisionem. 5. D : oculo carnalt. g. C: oculn in marg.
alia manu. 12. B: coipore. 16. AE: animosis. iS. C: corpus in marg.
alia manu. 25. ABC: hic deest; ib. ABC: qmdem. 28. DE: obiectu.
29. E: nimis deest: D: inter.
I. Cf. Johannis Hus, De Corpore Christi, Opp. tom. I, fol. 174'.
1:. Daniel L 0

p. 14:
1. ABC: illa deest. 2. predicia; E: ilia. 4. E: de incarnacione.
6. 1): qua idolatria; ib. B: creatur; ib. D: valide. S. DE: iuxta islam.
10. B: christianis valde disciplinatis ; D: valide. 11. AB: spina in fide;
D: fide tela. 12. E: vel deest ; ib. B: tam morbi. ifi. 1>: obicit,
17. ABC: ista sentencia laicis. 20. ABCD: Rom. VI; ib. AB: male.
20, 21. \rulgate: Ft non faciamus mala, ut veniant bona.

p. 15:
2. C: Christi est in marg. alia manu. 3, 4. D: ecclesie cantas ;
E: est cantus ecclesie; ib. B: quem canis. 6. C: tantum et twn
corrigit ex: tamen sed non; ib. E: rei. 9. AB: Deus deest; C in marg.
alia manu; ib. E: quam nuuc. 10. D: in sacramento. i3. B: maiestate
divina; ib. AB: vita. 14. AB: sentencia deest; C in marg. alia mann.
i5. D: quod iam. 16. B: abhomina. 21. D: videndo fideliter.
24. D: Sed quomodn tunc ; AB: quos ante. 25. ABC : caris. 29. D:
sacerdotalis dignitas. 3o. D: quod deest.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 11: Hoc lecto et perlecto sponte | subscripsi. Hanc confessionem sue fidei de corpore et sanguine domini nostri Jesu Christi a Beringario Rome coram centum i4 cim episcopis factam. | Misit papa Nicholaus per nrbes Italie, Germanie Gallie et ad quecunque loca bfama pravitatis eius pervenire ante potuit } ut ecclesie que prius doluerant de adverso atque diverso, post ea gauderent de reverso atque converso. | Consencio autem sancte Romane ecclesie et apostolice sedi, et ore ac corde profiteor de sacramentis dominice | mense eandem fidem me tenere quam dominus et venerabilis papa Nicholaus et hec sancta sinodus auctoritate evangelica et apostolica tenendam tradidit michique confirmavit. | sponle scripsi. | factam misit papa Nicolaus pcr urbes Ilaliae, Germaniae, Galliae ad quaecunque loca fama pravitatis eius pervenire ante potuit | et concepcionem. | nec suam. | sive diverso. | Ego 20 Reringarius, | argitat false. | ad doctrinam. | inter ipsos. 16. | non possunt | vel aKqmo. }o. | sit — virtutes
p. 12: Fracto demiim sacramento Non vacilles sed memento | Tantnm esse sub fragmento Quantum toto tegitur. | ad confitendam. | illud quod | patet et sic. | est credendum nobis 11011 oportet credere si; | ergo etc. | tercio vel probabile; | quod quod. | sciendum secundum. | istis jijim. | di-bct | sicut prime. | vulgus credit nimis infideliter et 'blaspheme quod hoc signum sacramentale corporis Christi sit | realiter ipse Christus. | corpus sit; | corpus Christi sit. | vel lucri. | quam talis. | undc — alicuius | presbiter seu sacerdos; | presbyter seu | est esse debet.
p. 13: Qiiod non capis, quod non vides Animosa Jirmat fides Preter rerum ordinem. | Nulla rei Jit scissura, Signi tantum Jit fractura Qua nec status nec statura Signati minuitur. | mens equivocatur; | in de quidditate. | in celum. | uno pane. | et bonitatem; | ad bonitatem; | malum et;
p. 14: Absit ut faciamus mala | ut evemant bona, | quod res. | in sc solum. 6. | que habei. | tamquam — graciam | Domini ea quc. | super ista. | merendi sed aliis; | sed el aliis;
p. 15: Snb diversis speciebus, Signis tantum et non rebus, Latent res eximie. | inius dominus et una fides | Hoc estcorpus meum; quod | Hoc est corpus meum, | quod pro | vobis tradetur, | Caro mea vere est cibus. | Hoc est corpus meum, | mundum potum. | sed de. | hic loqui. | precepit illum. | quod hoc est.
```
