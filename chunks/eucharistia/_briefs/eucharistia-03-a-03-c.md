# Translation brief: eucharistia 03-a–03-c

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/eucharistia/wyc-eucharistia-03-a.md chunks/eucharistia/wyc-eucharistia-03-b.md chunks/eucharistia/wyc-eucharistia-03-c.md` once and fix what it reports.
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
   every §A–C term: `[accident]{g:accidens}`; a multi-word key is lower case with hyphens, `{g:corpus-christi}`, `{g:a-simili}` (lint rejects spaces). The key must exist in GLOSSARY.md. A term that looks
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

## Glossary (the 417 rows these chunks use; the full file is GLOSSARY.md)

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
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
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
| conversio (eucharistic) | conversion | Of bread into the body; kept apart from *conversio* of a proposition. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 48.15). |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |
| decretum; decreta | decree; the decrees | Gratian (*in decretis*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.14, 3.24). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| respectus; respectivus | relation; relational | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| fallacia | fallacy | Ruled 2026-09-28. |
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
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| glosare | to gloss | Interpret so as to remove the difficulty (T. p. 366). |
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
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| citra Christum | short of Christ | As *citra fidem*. Ruled 2026-10-02 (45.8). |
| glosa | gloss | The noun beside *glosare*. Ruled 2026-10-02 (52.10). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| dulia / latria | dulia / latria | Kept as the theologians' terms, glossed once per chunk. Ruled 2026-10-02 (95.17). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| humanitas | the humanity | The nature the Word assumed, body and soul; with the article (*humanitas sit Christus*, "the humanity is Christ"). Not "the human nature", which is *natura humana*. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| dimittere / dimissio (*naturam*) | lay aside / the laying-aside | Letting go the assumed nature, so the union would be dissolved. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 2.23). |
| assumere / assumpcio (*naturam*) | assume / assumption | Of the nature, as in the fathers. ⚠ Kept apart from the logician's *assumptum* "the assumption" (above): C note where the logical sense occurs. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
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
| novelli | the newer [doctors] | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 13.7). |
| de vi vocis / de vi sermonis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| gracia unionis | the grace of union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| minoracio | lowering | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| immediate | without intermediary | The scholastic sense, ⛔ not "at once". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 30.30). |
| humanitus | humanly | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* passim). |
| suppositum | supposit | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 34.24). |
| individuum | individual | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 35.7). |
| in quantum (reduplicative) | insofar as | As *secundum quod*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37.9). |
| universitas creaturarum | the totality of creatures | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37). |
| pars qualitativa | qualitative part | Body or soul as the parts that make up a man by kind; set against *pars quantitativa*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 43.5). |
| pars discretiva | discrete part | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 46.9). |
| intransitive | intransitively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 45.28). |
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
| peiorare / peioracio | make worse / worsening | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 65–68). |
| per se / per accidens | of itself / by accident | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a (sufficienti) divisione | the topic from sufficient likeness / from (sufficient) division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| pretericio | being past | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| peccabilis | able to sin | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| Donum | the Gift | The Holy Spirit. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 78.21). |
| passionatus | subject to passion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| capitales doctores | the chief doctors | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| intricaciones sophistice | sophistical entanglements | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 82). |
| eiusdem / consimilis / alterius racionis | of the same / like / another kind | The species-sense of *racio*; *racio speciei* "the account of the species" (Aristotle's *logos*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.4, 87.17). |
| principiari | be constituted from principles | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.7). |
| univocacio | univocation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.27). |
| accidentatus | subject to accidents | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.4). |
| in recto / in obliquo | in the direct case / in an oblique case | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.25). |
| illusor | deceiver | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88). |
| passibilis | passible | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.12). |
| signum / signatum | sign / thing signified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 91.2–6). |
| conveniencia / convenire (*in*) | agreement / agree | The argument of 90–91 turns on it; not "fittingness" (that is *congruencia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 90). |
| illusivus | deceptive | Beside *illusor*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 92.9). |
| predicacio synecdochica | synecdochic predication | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.27). |
| paranymphus | paranymph | The bridegroom's friend (Gabriel). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 93.3). |
| humidum infantile / radicale | the moisture of infancy / radical moisture | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 94.9). |
| conversari | live one's life (among men) | Beside *conversacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.25). |
| esse intelligibile | intelligible being | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 99.23). |
| extraneare / extraneacio (supposicionis) | estrange / estrangement (of supposition) | *Affeccio extraneandi* "an affection of estrangement". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 98.16). |
| ministerialiter | ministerially | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 100.17). |
| mobile (noun) / primum mobile | a movable / the first movable | Against the adjective *mobilis*; ch. 7 turns on it. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 107, 116). |
| res racionis | thing of reason | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| universitas creata | the created totality | Beside *universitas creaturarum*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| significatum | significate | Kept apart from *signatum* "thing signified". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 111). |
| predicacio secundum essenciam / formalis | predication by essence / formal predication | Wyclif's modes of predication (cf. *predicacio secundum causam*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 115–116). |
| forma substancialis | substantial form | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| exclusiva | the exclusive [proposition] | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 116–117). |
| concepcio (figure) | conception | The grammatical figure. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| accidens | accident | The category; *accidit* "befalls". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| incepcio | beginning | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 121.16). |
| conversio (of a proposition) | conversion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.30). |
| humanitacio | humanation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 126.12). |
| racio (individual, personal) | account | *Racio individui / persone* "the account of an individual / a person", as *racio speciei*; not "aspect" (the row against *substancia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 8, 129–132). |
| vir (against *homo*) | man (*vir*) | Where Wyclif sets *vir* against *homo*, the Latin in parentheses. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 129.15–26). |
| univocare / univocari | make univocal / be univocal | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 131.3). |
| analogicari | be said analogically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 131.27). |
| res secunde intencionis | things of second intention | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.25). |
| materia proxima / remota | proximate / remote matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137.1). |
| res communis / res communes | the common thing / common things | The realist universal the *moderni* do not conceive (first root of their error). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 144.27). |
| distinccio racionis | distinction of reason | Beside *differencia formalis*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 145.23). |
| conversio naturarum / confusio naturarum | conversion of the natures / confusion of the natures | Kept apart from *conversio* of a proposition. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 143.9). |
| moderni (bare) | the moderns | Beside *moderni doctores* "the modern doctors". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 142.10). |
| principiare (active) | be the principle of | Beside the passive *principiari* "be constituted from principles". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 147.4). |
| assumere personale | personal assuming | The infinitive used as a noun; kept apart from *assumpcio personalis* "personal assumption". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 146.33). |
| moderniores (bare) | the more modern | Beside *moderniores doctores* "the more modern doctors". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 151.17). |
| supposicio simplex / supposicio personalis | simple supposition / personal supposition | Supposition theory. *Simpliciter / personaliter supponere* "stand with simple / personal supposition": NOT the *simpliciter / secundum quid* pair, C note where the two could be confused. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 152.5–12). |
| transsumpcio | transumption | Beside *transsumptive*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 153.28). |
| aliud / alius | another thing / another one | The neuter against the masculine (*aliud et aliud, non alius et alius*): natures against persons. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 160.1–2). |
| in quid (predicari in quid) | in quid | Kept in Latin (predication of what a thing is, as against *in quale*), glossed at first use in a chunk. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 162.22). |
| suppositari | be supposited | Verb beside *suppositum*, *suppositacio*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 161). |
| negacio (constituent of the person) | negation | The moderns' account: a person = nature + negation of dependence. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 161–162). |
| dependencia actualis / potencialis / obediencialis | actual dependence / potential dependence / obediential dependence | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 161.23–162.4). |
| substancia prima / substancia secunda | first substance / second substance | Aristotle, *Cat.* 5. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.25). |
| a simili | by likeness | Bare, as an argument form; beside *locus a simili* "the topic from likeness". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.16). |
| racio substancialis | substantial account | As *racio individui* "account". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.21). |
| doctores signorum | the doctors of signs | The logicians who reason from terms, not things. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.26). |
| sensibilis (in the definition of animal) | sentient | *Substancia animata sensibilis*: able to sense. Elsewhere the §D row "perceptible" holds; G note at first use. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 177). |
| suppositalis | of a supposit | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 176). |
| accidens absolutum | absolute accident | Quantity and quality, against relative accidents. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 176). |
| beatificabilitas | beatifiability | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 181). |
| passionaliter | as an attribute | Beside *passio* (the proper attribute). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 181). |
| mocio / motus (paired) | motion (*mocio*) / movement (*motus*) | Only where Wyclif pairs them; otherwise "motion". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 180). |
| posicio anime | the laying-down of the soul | John 10:17–18; not the logical *posicio* "position", C note. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 183.3). |
| transsubstanciacio | transubstantiation | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.10). |
| multiplicative | multiplicatively | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 193.20). |
| remitti / intendi (of a quality, merit) | be remitted / be intensified | The intension and remission of forms; not *remissio* of sin. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 197.1–7). |
| in divinis | among the divine [persons] | Keeps "Godhead" for *deitas*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 196.18). |
| partes proporcionales | proportional parts | The halving division of a continuum. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 194.24). |
| universitas creabilis | the creatable totality | Beside *universitas creaturarum* "the totality of creatures". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 199.5). |
| multiplicacio dimensionalis | dimensional multiplication | One body in several places by its dimensions. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.6). |
| a maiori vel pari | from the greater or from the equal | Arguments *a maiori*; cf. *locus a maiori*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 209.5). |
| sensibile commune | common sensible | Aristotle's common sensibles (number, motion, figure); the term of art, against the §D row "perceptible". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 209.23). |
| mocio progressiva / motus progressivus | progressive motion | Locomotion. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 205.28). |
| communioritas | greater commonness | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 210.15). |
| multiplicacio concomitancie | multiplication of concomitance | Cf. *gracia concomitancie*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 213.21). |
| assertibile | assertible | The thing a proposition asserts. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 215). |
| superioritas / inferioritas terminorum | superiority / inferiority of terms | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 215). |
| exponentes | the exponents | The propositions into which a proposition is resolved (expounded). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 216.14). |
| homo communis | the common man | The universal man, with *res communis*; not "the ordinary man". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 218.3). |
| moderni loquentes | the modern speakers | Beside *moderniores loquentes*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 221.20). |
| signum reduplicatum | the reduplicated sign | The reduplicative word (*secundum quod*, *in quantum*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 230.23). |
| supposicio | supposition | Of a term (supposition theory) or of a premiss laid down (cf. *supponitur* "it is supposed"); the English word serves both, C note where it matters. Kept apart from *suppositacio* "suppositation". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 102.8). |
| univocus | univocal | Beside *univoce*, *univocare*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 102.13). |
| lex proximitatis | the law of neighbourhood | The duty to love one's neighbour (*proximus*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 101.29). |
| negacio preposita toti | a negation placed before the whole | The negation governing a whole proposition. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 103.21). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |
| sacramentaliter | sacramentally | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| vere | truly | A mode adverb: one word each, never two merged, kept where Wyclif puts it. ⛔ Never "really" (that is *realiter*). Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| virtualiter | virtually | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| sensibiliter | perceptibly | A mode adverb: one word each, never two merged, kept where Wyclif puts it. As *sensibilis* "perceptible". Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| corporaliter | bodily | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| substancialiter | substantially | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| sentencia (verborum, scripture) | sense | The meaning of words or a text (*ad sentenciam attendendum*, against the rites, 4.9); kept out of the two-sense row *sentencia*. Ruled 2026-11-06 (Wilson; *Euch.* prol-a 4.9, review b14). |
| predicacio ydemptica / tropica | identical / tropical predication | The treatise's key pair; *tropica* kept apart from *figurative*. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.21). |
| accidens sine subiecto | accident without a subject | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 3.19). |
| remanencia (panis) | the remaining (of the bread) | Verb *manere* "remain". Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.21). |
| substancia | substance | Beside *substancia prima / secunda*. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 3.14). |
| quantitas / qualitas | quantity / quality | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.7–8). |
| esse; esse sacramentale | being; sacramental being | The bare *esse* of the modes of being. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 3.28, 3.30). |
| confeccio | consecration (of the eucharist) | The noun of *conficere*, which already shares "consecrate" with *consecrare*. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 4.4). |
| Doctor Communis | the Common Doctor | Thomas; with *Doctor Subtilis*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 8.16). |
| multitudo (of one body) | multitude | Of one body's being many (ch. 8); the plain "multitude" of persons needs no row. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 8.4). |
| sensus communis | the common sense | The inner faculty; kept apart from *sensibile commune* "common sensible". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 18.31). |
| supponere pro | stand for | Supposition; with *supposicio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 24.27). |
| sensualiter | sensually | Berengar's oath word (*Ego Berengarius*); kept apart from *sensibiliter* "perceptibly". A mode adverb, one word. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 26.1, 30.24). |
| predicacio figurativa | figurative predication | A synonym of *predicacio tropica*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 35.18). |
| describere | define | The verb of *descripcio* "definition". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 48.9). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| perplexus | perplexed | The moral-theology sense: bound to sin whichever way one turns. Ruled 2026-09-28. |
| magisterium | rule; of teaching, the teaching office; *quale magisterium* "what a feat of mastery" (*Incarn.* 137.14) | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| detegere | to expose | "wipe away" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| continuacio (of bodies, the act) / discontinuacio; continuare / discontinuare | continuation / discontinuation; make continuous / make discontinuous | The making of several bodies into one continuum (*Incarn.* ch. 12), G note at first use: not "carrying on". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.30, 211.12). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| perplexitas | perplexity | The noun beside *perplexus* "perplexed". Ruled 2026-10-02 (*Eccl.* 19, 470.3). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| univoce | univocally | Ruled 2026-10-02 (*Eccl.* 21, 514.4). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| cambium | barter | Kept apart from *commutacio* "exchange". Ruled 2026-10-02 (*Eccl.* 23, 551.24). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
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
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| trahere in consequenciam | draw into a precedent | The legal idiom; *consequencia* stays "inference". Ruled 2026-10-07 (*Pot. pape* 94.13). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| regulariter | as a rule | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 165.2). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| irregularitas | irregularity | Canonical impediment to orders or office. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 190.30). |
| infundabilis; infundabiliter | without foundation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 195–196). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| primicia (virtutum) | being first (in the virtues) | Kept apart from *primatus* "primacy" and *primitas* "firstness". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 228.33). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| malum culpe / pene | the evil of fault / of penalty | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.19). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| papa cesareus | caesarean pope | The pope as endowed temporal lord (chs. 10–12). Ruled 2026-10-08 (coordinator, delegated). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| preponderancia; dispensacio | preponderance; dispensation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 266.11, 268.4). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| potissimus; pocior (Antichristus) | foremost; greater | Superlative and comparative kept visible as a pair. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.28, 331.12). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| episcopi cesarei | caesarean bishops | Extends *prelatus / sacerdos cesarius*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 331.24). |
| prepositus (participle of *preponere*) | the one preferred | CONTEXTUAL beside *prepositi* "superiors" (the noun); untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| involucrum | wrapping | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 357.9). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| obviare; obvia (logical) | meet; meeting | Of a case or argument. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 383). |
| ars cesarea | the caesarean art | After *papa cesareus*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |
| nimis | exceedingly | Medieval intensive (= *valde*); "too much" only where excess is the point. Ruled 2026-10-12 (close-out R2; *Pot. pape* 169.2). |
| fingere (a miracle) | feign | "imagine". Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.11, 1.14). |
| narrare | relate | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.9). |

---

## Chunk 03-a: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-03-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-03-a
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "53.26–57.27"
divisions: "cap. 3 (heading 'CAPITULUM TERTIUM.' at 53.0); part 1 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "823 words; 809 confirmed by the vote; 13 runs stood by rule; 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n124–n128 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 3, part 1: [TITLE]

## ¶1 · 53.26–54.4

> [p. 53] Restat superaddere alia argumenta contra doctores novellos pro antique ecclesie sentencia et primo per hoc quod non est Dei destruere suam fabricam in auctorisando ecclesiastica sacramenta; sed sic faceret iuxta sentenciam istam noviter adinventam, ergo ipsa [p. 54] est irracionabilis. Minor patet ex hoc quod iuxta hanc viam quantum de pane et vino in toto mundo est transsubstanciatum, tantum desinit atque destruitur tam quoad materiam quam quoad formam.

[ENGLISH]

## ¶2 · 54.5–54.8

> [p. 54] Et videtur nocivum esse cambium, cum tanta substancia plus prodesset mundo quam eius horrenda transsubstanciacio; Deus ergo inepte et infundabiliter sic prodesset ecclesie.

[ENGLISH]

## ¶3 · 54.9–54.23

> [p. 54] Item, cum nec remanet materia nec forma transsubstanciati, ne corpus Christi foret nimis gravidatum novella materia, videtur iuxta concedentes possibilitatem anichilacionis quod simpliciter anichiletur natura transsubstanciata; nam possibile est secundum illos quod anichiletur tam panis quam vinum et succedant corpus Christi et sanguis sacramentaliter sub istis accidentibus, ut modo videmus, sed quomodocunque foret tunc ex parte panis aut vini est materia; ergo nunc est irrevocabiliter anichilata in consecracione. Assumptum est famosum aput illos, cum substancia potest anichilari servato accidente et econtra, ut inquiunt, nec obest quin Christus potest pro eodem instanti multiplicare corpus suum sub illis accidentibus, cum sint motus omnimode separati.

[ENGLISH]

## ¶4 · 54.24–55.8

> [p. 54] Item, anichilacio secundum sic loquentes specificatur ab esse parcium anichilati et terminatur ad simpliciter non esse; quod est in omni transsubstanciacione secundum ipsos, ergo etc. Que rogo diversitas inter annichilacionem A panis, succedente corpore Christi sub eisdem accidentibus pro instanti [p. 55] anichilacionis, et transsubstanciacionem B panis in corpus Christi sub suis accidentibus sacramentaliter succedens pro eodem instanti? Nam par est desicio atque destruccio substancie utrobique, ideo videtur quod quoad motum destruccionis sit in toto conformitas. Conformis est enim destruccio panis, sive cicius redibit materia sive maneat perpetuo corpus Christi sub sensibili subiecto.

[ENGLISH]

## ¶5 · 55.9–56.14

> [p. 55] Nec valet ficticia de transsubstanciacione vel conversione panis in corpus Christi, cum corpus Christi nec accipit materiam nec formam substancialem vel accidentalem a pane corrupto; ideo videtur non pocius converti in corpus Christi quam dies convertitur in noctem vel econtra; ideo vel irregulariter panis non convertitur in corpus Christi in confeccione eukaristie vel est ambiguum quando est talis conversio; cuius descripcio non fingetur. Et patet, licet canat ecclesia: Dogma datur christianis Quod in carnem transit panis Et vinum in sanguinem, quod natura illius transitus panis in corpus Christi et vini in sanguinem videtur esse ignorata eciam theologis, quia quilibet eorum ponit desicionem substancie secundum se totam et nescit ubi aliquid panis remaneat vel quo vadat; ideo separando illum motum ab aliis videtur secundum eos quod sit anichilacio. Aliter enim posset fingi de quolibet motu quod non sit anichilacio propter motum positum [p. 56] alium comitantem; videtur enim quod panis vertitur in nichilum, sicut est de gracia que non vertitur in peccatum, sicut nec anichilatum vertitur in corpus quod occupat locum suum; nam nichil vertitur vel transit in aliud nisi subiectet versionem vel transitum usque ad terminum ad quem est motus, non vocando illam mutacionem mirabilem ab esse panis ad eius non esse, cum non sit materia substrata, sicut nec in anichilacione, videtur illis dicendum quod sit anichilacio, cum non sciunt conversionem impedientem detegere; nam (ut inquiunt) postmodum producetur materia prima secundum se et quamlibet sui partem; de nichilo ergo in desicione sua anichilata est.

[ENGLISH]

## ¶6 · 56.15–56.25

> [p. 56] Et mirantur hic naturales quomodo irregulariter eadem materia prima in numero redit secundum se totam, cum talia individuantur ab instanti in quo producuntur; ideo sicut non redit primum instans mundi, sic nec redit eadem materia in numero. Cum ergo sit eque facile Deo producere in toto novam materiam, nec habent revelacionem, racionem vel sompnium quando sic fecit, ergo non est credendum narracioni istorum, quin creatur nova materia annichilata antiqua. In tales perplexitates involvunt ecclesiam qui extraneant ab antiquis sanctis.

[ENGLISH]

## ¶7 · 56.26–57.27

> [p. 56] Item, secundum Augustinum super Joh., Omelia XXVIᵃ, super isto Joh. VIᵒ, 56: Caro mea vere est cibus et sanguis meus vere est potus: In illis, inquit, rebus Deus commendavit nobis hoc sacramentum, [p. 57] que ad unum aliquid reducuntur ex multis. Namque ex multis granis panis conficitur, et ex multis racemis vinum confluit; nunc secundum adversarios istud foret hereticum, cum plane implicat panem et vinum post consecracionem hostie remanere; ideo non in illis rebus sed in accidentibus que ignorant dicunt quod accipimus corpus Christi. Cum ergo Deus decrevit nobis dare donum tam magnum, videtur convenire sue veritati magnifice quod dedit nobis ipsum in velamento honorifico illusionem hominis excludente. Omnis enim talis decepcio est mala, cum homo naturaliter innititur cognoscere veritatem, ideo cum sciencia veritatis sit bona et utilis, ignorancia veritatis est mala, beatitudini repugnans, ideo dicimus accidencia remanere ut sensus a decepcione immunes reddantur; sensus autem interiores iudicant de substanciis materialibus, cum sint sensibilia per accidens; ideo magis malum foret in illis decipi. Cum ergo sensus hominis tam exteriores quam interiores iudicant illud remanens esse panem et vinum rei non consecrate simillimum, videtur quod non convenit domino veritatis tantam illusionem inducere in graciose communicando donum tam dignum; non enim punit nisi citra condignum propter culpam que meruit sic puniri. Unde ergo puniret decepcione tam ignobili eciam beatum qui sacramentaliter assumeret corpus suum?

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 53.26: The modern doctrine makes God destroy His own work.
- 54.24: Cessation to exist is equivalent to annihilation.
- 55.9: The bread is not converted since Christ's body takes neither matter nor form from it.
- 56.15: It is a mere fancy to pretend that the primal matter which was in the bread returns in the Body.
- 57.7: God does not mingle deception with His great gift in the Sacrament.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 56: *VIᵒ,* (print = bt) [SUB]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Danger jliat th (53.5).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 53:
y. ABC: ydemptice dccst. 9. I): remaneret. 10. C: esse alia manu.
11. ABCIi: et revera dccst. 17. 1): quod tantum. 20. AI5CK: ut irrc-
verencius. 21, 22. ABC: sit ydemptice — accidens dccst. 23. DE: ei vini.
2 |. D : vero patet ; AB : autem dcest; C: autem patet alia manu; ib. ABC :
posterius etc. 27. B: antiqua. 3o. E: ipsa deest.

p. 54:
2. D: vel vino. 4. E: quo deest beforc ad materiam. 8. AB: pro-
desset ecclesie sic. 9. D: remaneret forma nec materia. 11. B: videt;
ib. E: contra concedentes. 12. D: adnichilacionis ; ib. C: adnichilaretur.
16. ABD : videmus deest; ib. CE: modo deest. 16, 17. ABCE: quo-
cunque foret. 17. E: etvini; ib. D: est modo. 18. B: est irret ;
E: realiter in rasura; ib. D: adnichilacio. 19. ABC: argumentum est.
22. D: multipliciter . 23. E: fuit motus. 24. ABE: Iterum.
26, 27. C: transubstanciacione in marg. alia manu. 28. C: A in marg.

p. 55:
i—3. C: annichilacionis — instanti in marg. alia manu. 4. B: ibi
videtur. 6. D: est eciam. 6, 7. D: panis sive tritici. 8. D: sensi-
bili sacramento. 10. D : cum corpus Christi deest; C in marg. alia manu.
i3. C: in corpus Christi in marg. alia manu. 17. ABE: fingeretur ;
ib. E: patet quod. 18. D: canlat. 23. AB : ignorancia. 26. ABCE :
vadit. 28, 29. ABC: Aliter — anichilacio deest.
19. E sequentia que vulgo tribuitur Thomae Aquinati de-
cantata in Festo Corporis Christi, see Daniel 1. c. II, 97.

p. 56:
1. AC: communicantem ; B: communitatem ; D: ad bene comitantem.
4. C: nichil in marg. alia manu. G. D: ct transitum. 7. ABCD: no-
tando. 10. ABC: quot; ib. ABC : sit deest. 14. D: adnichilata.
i5. C: modo mirabiliter. 16. AB: eadem dcest. lS. D : producunt.
c3. C: racioni; nar in marg. alia manu. 25. ABD : qua ; C: correxit.
27. S. Aug. Opp. tom. Iir, 2, pag. 5oo.

p. 57:
2. Codd. : ex multis deest. Addidi. 4. .13 : fores. 9. D : quod debet;
E: quoddet. 10. Codd.: illusione. 11. ABCD : Et omnis. n, 12. Codd.:
eum hoe ; C in rasura: homo. 16. B: reddeantur. 20. E: remanens
deest. 28. Codd.: modernorum; C : correxit. 29. BE : vere deest;
ib. A: vere exprimerent in marg. alia manu. 3o. D: vel fuit.
l. St. Aug. 1. c. quae ad unum aliquid rediguntur ex multis.
Namque aliud in unum ex multis granis conjit: aliud in unum
ex multis acinis conjluit.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 53: etfit quando; | ex altero.
p. 55: Dogma datur christianis -o Quod in carnem transit panis Et vinum in sanguinem,
p. 56: Caro mea vere est cibus et sanguis meus vere est potus: In illis, | rebus Deus commendavit nobis hoc sacramen- | heretici aut; | suis tcmporibus. | maxime hereticus; | quam nemo. | ad inpugnandum predictam Augwtini sancti. | sunt solute
p. 57: tum, que ad unum aliquid reducuntur ex multis. Namque ex multis granis panis conficitur, et ex muliis racemis vinum confluit\ | Scarioth autem | accepit cohortem et ministros | de Petro. | alias divino.
```

---

## Chunk 03-b: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-03-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-03-b
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "57.28–61.13"
divisions: "cap. 3 (heading 'CAPITULUM TERTIUM.' at 53.0); part 2 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "778 words; 755 confirmed by the vote; 17 runs stood by rule; 6 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n128–n132 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 3, part 2: [TITLE]

## ¶1 · 57.28–58.7

> [p. 57] Unde hic angustiantur moderni doctores, cum quibus signis vere exprimerent veritatem huius sacramenti; ut negant quod panis est, fuit vel erit corpus [p. 58] Christi, negant eciam quod panis poterit esse corpus Christi, et tercio negant quod ex pane fiet corpus Christi, cum hoc implicat panem cedere in corpus Christi et ipsum noviter generari; ideo dicunt quod panis transsubstanciabitur in corpus Christi, panis convertetur vel mutabitur in corpus Christi et (ut quibusdam placet) ex pane fiet corpus Christi.

[ENGLISH]

## ¶2 · 58.8–59.3

> [p. 58] Unde sanctus Thomas super IVᵒ, distinccione XIᵃ, articulo IIᵒ glosat beatum Ambrosium in libro suo de sacramentis et ponitur in De Consecracione, distinccione IIᵃ, Panis est in altari: Hoc est, dicit Thomas, quod est sub speciebus panis, primo fuit panis et postmodum corpus Christi. Sed Magister IVᵒ Sentenciarum, distinccione Xᵃ, capitulo IIIᵒ glosat melius talia dicta sanctorum quod utuntur tropo quodam, quo solent signa suorum signatorum sortiri vocabula. Nam ante consecracionem non fuit panis ille sic corpus Christi, sed virtute verborum Christi fit signum sic efficax; et sic intelligitur quod panis convertitur in corpus Christi, transsubstanciatur vel quocunque termino mutacionis exprimatur. Aliter tamen intelligunt moderni doctores sed non docent, ymmo se ipsos intricantes sibimet contradicunt. In omnibus enim istis angustiantur de subiecto mutacionis, cum repugnat panem et vinum expectare motum talem, ut inquiunt. Angustiantur eciam in declaracione triplicis termini supradicti et quid ponit illa conversio ultra hoc quod poneret panis anichilacio [p. 59] et corporis Christi sub illis accidentibus sacramentaliter successio. Ad tantum enim peioratur universitas corporum sensibilium utrobique.

[ENGLISH]

## ¶3 · 59.4–60.14

> [p. 59] Item, manifeste videtur secundum istos doctores quod in conversione hostie est dare duos motus natura priores, scilicet desicionem panis secundum se totam et presencie corporis Christi inchoacionem secundum se totam; et illa conversio vel est illa duo vel ad illa formaliter consequens ut passio ad subiectum; cum ergo deficit subiectum illius conversionis nec illa sit de numero accidencium que potuerunt per se esse sed naturam corruptam mutari, videtur quod illa conversio sit aggregatum ex illis duobus motibus; cum ergo prior illorum sit idem motus qui foret, si de possibili careret concomitancia aliorum, videtur quod sicut tunc panis anichilaretur sic et modo. Conversio enim cum sit mocio positiva, requirit existenciam essencie subiecti, quia aliter ipsum non plus converteretur quam anichilata essencia, cui succederet corpus novum. Sic autem (ut inquiunt) posset esse de Dei potencia absoluta, nec sompnium nec racio docet adversarios oppositum, quare ergo sic non ponunt? et cum anichilacio non sit per accidens anichilacio, videtur quod talis desicio foret anichilacio quolibet motu alio comitante; nam conversio vel presencie corporis Christi acquisicio, cum foret accidentalis illi desicioni, videtur quod non tollit sibi speciem aut quidditatem; et hoc videntur sic opinantes qui negant composicionem continui ex non quantis admittere de possibili illam desicionem panis pro uno instanti et illam conversionem immediate post succedere, quia aliter videtur quod pro [p. 60] instanti quo foret uterque motus remaneret panis nondum conversus, et per consequens conversio foret futura; sed hoc implicat duo instancia esse inmediata, sicut via que dicit quod est dare primum instans in quo angeli ceciderunt et ultimum instans in quo steterunt, sed maior pars difficultatis foret intelligibiliter declarare quod panis transit, convertitur vel cedit corpori Christi, cum iuxta hoc concedentes possibile est substanciam panis anichilari sive extra sive intra dicta accidencia; ideo preter desicionem panis et incepcionem presencie corporis Christi ponunt conversionem omnimode separatam; sed illam nesciunt omnes loquentes exponere; nec docetur in fide scripture vel simbolo ecclesie.

[ENGLISH]

## ¶4 · 60.15–61.2

> [p. 60] In natura autem, quando unum corpus convertitur in aliud corpus in quod essencia prioris corporis convertitur, manet essencialiter corpus conversum; ideo corpus sic desinens non convertitur in sua accidencia nec accidencia noviter creata, quia sic posset omnis substancia creata converti in punctum sine anichilacione, cum conversio non dicit melioritatem conversi, et tunc illo puncto anichilato totus mundus converteretur in nichilum et tamen nec ante priorem conversionem nec post; ymmo subtiliores doctores istius secte asserunt quod foret in ista transsubstanciacione anichilacio, nisi panis aliquitas remaneret in carne Christi in quam fit conversio. In cuius testimonium dicunt quod Deus potest de hostia corpus suum sacramentaliter subtrahere et ipsam in naturam eiusdem panis revertere; sed certum est quod non remaneret sic panis aliquitas, nisi remaneret quod [p. 61] panis est aliquid et sic panis, cui accidit quod corpus Christi est sacramentaliter ibi presens.

[ENGLISH]

## ¶5 · 61.3–61.13

> [p. 61] Alii autem stulte ponunt quod omne desinens convertitur in omne remanens; et sic affirmacio posset converti in negacionem et tolleretur possibilitas anichilacionis; quod negant, sicut et illi qui dicunt quod omne anichilatum convertitur in Deum secundum suum esse supremum, et omne corruptum convertitur in non esse panis aut convertitur in non esse secundum se totum, ut dicitur; nec docetur quod convertitur in corpus Christi, ex hoc quod corpus Christi succedit sub illis accidentibus ibi presens; nec verba sacramentalia illud docent, ut patebit inferius.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 57.28: Difficulty of finding language to express the modern doctrine.
- 59.4: The modern doctors require two movements: the cessation of the bread, the beginning of the presence of the Body.
- 59.10: These are separate movements, independent of each other, whereas conversion, as a positive movement, requires a subject in which it can exist continuously.
- 60.15: Some say that something of the bread (aliquitas panis) remains, so that God may withdraw His body and the host return to bread.
- 61.3: Various fancies as to what becomes of that which is annihilated.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 57: *sacramenti;* (print = bt) [SUB]
  - 58: *IVᵒ,* (print = bt) [SUB]
  - 58: *XIᵃ,* (print = bt) [SUB]
  - 58: *IIᵒ* (print = bt) [SUB]
  - 58: *IVᵒ* (print = bt) [SUB]
  - 59: *succederet* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 57:
2. Codd. : ex multis deest. Addidi. 4. .13 : fores. 9. D : quod debet;
E: quoddet. 10. Codd.: illusione. 11. ABCD : Et omnis. n, 12. Codd.:
eum hoe ; C in rasura: homo. 16. B: reddeantur. 20. E: remanens
deest. 28. Codd.: modernorum; C : correxit. 29. BE : vere deest;
ib. A: vere exprimerent in marg. alia manu. 3o. D: vel fuit.
l. St. Aug. 1. c. quae ad unum aliquid rediguntur ex multis.
Namque aliud in unum ex multis granis conjit: aliud in unum
ex multis acinis conjluit.

p. 58:
2. D : fieret. 3, 4. D : in materiam corporis Christi. 9. E: suo dcest
11, 12. B: dum Thomas. 17. A: ante in marg. alia manu; ib. E: con-
secracionem panis. 18. E: sic deest. 19. C: sic erased. 20. ABC:
vertitur ; ib. D: transsubstancialiler. 21. D: inprimitur ; ABC : e.xpri-
mitur. 22. E: tamen dicunt. 25. D: tamen ; ib. D: panem vel.
27. B: termini secundi. 28. E: quod decst.
8. S. Thomae Aquinatis Opp. tom. X, 1G7. 10. Decreti
Tertia Pars, De Cons. dist. II, cap. LV. i3. i. e. Petrus
Lombardus, Lib. IV, dist. X. (Ed. Col. 1676, foL 35 ih).

p. 59:
1, 2. D: sacramentalis. (5. D: natura peiores. 7. C: Christi deest.
11. C: stt deest. 12. ABC : naturam corpoream. i5. ABCD : possibile.
16. AB: sicut etpanis. 17. C: cum in marg. alia manu. 22. ABD : decet;
ib. AB: opponi; C: opponitur ; ib. E: qualiter ergo. 22, 23. D: igitur
non sic; E: ergo non sic. 23. ABCE: non fit. 29. A: continua.
3i. D: instanti ad. 32. DE: succedere post.

p. 60:
7. I) : vel convcrtitur. 8. ABC : Cliristo. n. C: prcsaicie dccst.
12. C: omnino despcratam. i3. C: c.xplanarc ; l) : cxprimere ; ib. C : ncc
doccre. i3, 14. D: in finc. 16. C: prioris cxtinct. 26. AB: aniclii-
lacio dccst; C in marg. alia manu; ib. E: rci mancrct. 27,28 B: esti-
monium. 28. B : Deus post. 3l. C : rcmanet.

p. 61:
2. B: sibi prcsens ; E: est ibi sacramentaliter. 6. C: quod corrcxit
in qnam. ~. I) : convertetur ; E: converteretur. (). C: in in marg.
alia manu; ib. BD: panis autcm. n, 12. B: Christi ficticet ; C: /icticet
in marg. alia manu; in textu: fic. i3. AB: illa docent ; C: illud in marg.
alia manu. 17. D: vel revelacio. 21. B: scripturis; ib. B: pertinere;
E: pertinet. 23. ABCE : debet. 24. D: movit ; C: debct in marg. alia
manu. 25. E: nec de quanto. 28. E: debemus. 29. 1) : sic enim.
19. St. Aug. Opp. tom. III, 1, 63. Cf. De Baptismo contra
Donatistas Opp. IX, q8. Cf. Trial., pag. 240.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 57: tum, que ad unum aliquid reducuntur ex multis. Namque ex multis granis panis conficitur, et ex muliis racemis vinum confluit\ | Scarioth autem | accepit cohortem et ministros | de Petro. | alias divino.
p. 58: Panis est in altari: Hoc est, | quod est sub speciebus panis, primo fuit panis et postmodum corpus Christi. | quod utuntur tropo | quodam, quo solent signa suorum signatorum sortiri vocabula, | non 20 debemus epulari in fermento veteri | sed in a\imis sinceritatis | et veritatis | virtus et Dei | ad conversacionem.
p. 59: iudicium sibi manducat et bibit | Quidquid autem gestum est in cruce Christi, in sepultura, in resurreccione tercia zodie, in ascensione in celum et in eo quod sedet ad dextram patris, ita gestum est ut hiis rebus non mistice tantum dictis sed eciam gestis configuraretur vita christiana que hic geritur. Nam propter eius crucem dictum est: Qui autem Christi sunt carnem | suam crucifixerunt cum viciis et concupiscenciis. Propter sepulturam: Consepulti enim sumus Christo per baptismum in mortem. Propter resurreccionem: Ut quemadmodum Christus resurrexit a mortuis per gloriam patris, ita et nos in novitate vite am- | bulemus. Propter ascensionem in celum sedemque ad | fidem rectam; | et bibendo. | secunditatem falsilatis; | duplicem falsitatem ; | convertit que. | Faich. LII; | tercia die | ascendit ad dextram; | alias a dextris. | Et propter. | sedens que;
p. 60: dextram Patris: Si consurrexistis cum Christo, que sursum sunt sapite, non que super terram: Mortui enim estis et vita vestra abscondita est cum Christo in Deo. | Hoc facite in meain commemoracionem; | Hec quociens- | cunque feceritis in mei memoriam facietis. | ad Deunt. | in fine | ut ut.
p. 61: Quoniam unus panis | et unum corpus multi | omnes de uno pane | prius primam; | ex secunda. | summo tribulacionis. | per graciam.
```

---

## Chunk 03-c: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-03-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-03-c
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "61.14–65.28"
divisions: "cap. 3 (heading 'CAPITULUM TERTIUM.' at 53.0); part 3 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "932 words; 910 confirmed by the vote; 21 runs stood by rule; 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n132–n136 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 3, part 3: [TITLE]

## ¶1 · 61.14–62.10

> [p. 61] Item, secundum adversarium foret possibile quod corpus Christi maneret sacramentaliter sub pane, sicut iam manet sub nudis accidentibus et nec scriptura sacra nec racio nec revelacio docet aliquem quod sit talis transsubstanciacio; ergo stultum foret talem sensum inducere. Cum enim secundum Augustinum IIIᵒ De Doctrina Christiana in fine, omnis veritas sit in scriptura sacra, pertineret prepositis perscrutari fundamentum suum ibidem, ne ex falsitate illudant et onerent ecclesiam plus quam debent; et istud movet multos, cum nemo debet credere eciam pape in materia fidei, nisi de quanto se fundaverit in scriptura. Sed nec scriptura nec racione nec revelacione potest ecclesia Avinonica fundare predictam transsubstanciacionem, ergo non pocius tenemur ipsam credere quam credidit ecclesia primitiva; sic eciam [p. 62] posset ecclesia onerari mille fallaciis tanquam fide, et posset processu temporis induci lex Antichristi; creditur, inquam, quod in edicione ultima illius decretalis De Fide catholica, capitulo Firmiter in fine, non concurrerunt papa et CXIIIᶜⁱᵐ episcopi, ut contigit in sinodo qua decretum est quod panis et vinum remanent; ideo (ut dixi superius) non est racio quare debemus eis credere plus quam illis, potissime cum fabricatores mendacii de novo subrepserant, quos creditur istam ficticiam invenisse.

[ENGLISH]

## ¶2 · 62.11–63.22

> [p. 62] Cum ergo subtiliores doctores moderni vident et asserunt quod nichil cogit hoc credere nisi predicta decretalis et ipsa non daret per se fidem fidelibus, videtur quod in isto deficit huius fidei fundamentum. Oportet enim legistas fundantes tam sollempniter novum festum baptismo dimisso aliquid novum atque mirabile inculcare. Unde omnes legiste et eorum auctores nesciunt describere transsubstanciacionem et quomodo ab anichilacione distinguitur cum annexis difficultatibus, quibus exinde ecclesia est involuta. Conceditur tamen quod accidencia illa que quidam vocant panem et vinum sunt honoranda ut signum corporis Christi et sanguinis. Sed quantum patres legis veteris cavebant colere ymagines tanquam Deum, ut patet in epistola Jeremie missa Babiloniam per Baruch, tantum debet christianus cavere ne colat illud quod moderni vocant accidens et prior ecclesia [p. 63] vocavit panem et vinum tanquam verum corpus et sanguinem Jesu Christi, quia sicut ille ymagines non poterant se iuvare vel suos cultores contra hostes, latrones vel aves, ut docet Jeremias Baruch ultimo, revera sic nec dictum accidens. Ideo illo dimisso signatum suum quod est corpus Christi et sanguis, ymmo tota Christi humanitas, quantum univoce sufficimus est colenda; et licet illud signum habeat maiorem efficaciam quam signa legis veteris et nostre ymagines (ut patebit posterius), tamen nimis magna infidelitas foret credere illud tam abiectum in natura esse Deum; ymmo sic immolans infideliter facit abhominacionem et despectum Deo sicut alii infideles ydolatre; et illud predicandum foret laycis, ne stulta pietate precipitarentur infideliter in ydolatriam. Nec videtur quod aliqua pars panis aut vini convertitur in aliquam partem corporis Christi nisi per idem in quamlibet et sic in sanguinem et animam et quelibet accidencia corporis dominici absoluta; nam racione istius conversionis sunt omnia de novo ibi presencia; et hoc sufficit ad conversionem huiusmodi, ut videtur.

[ENGLISH]

## ¶3 · 63.23–63.29

> [p. 63] Secundo principaliter arguitur de racione accidentis: nam omne accidens formaliter inherens substancie non est nisi veritas que est substanciam esse accidentaliter alicuius modi, ut hic supponitur, sed nulla talis veritas potest esse sine substancia, sicut nulla creatura potest esse sine Deo, ergo non est cumulus talium accidencium sine subiecto que sit hostia consecrata.

[ENGLISH]

## ¶4 · 64.1–64.11

> [p. 64] Item, omne accidens predicamentale est univoce accidens cum quolibet, sed aliquod accidens, ut omnis respectus in aliquo septem generum, non potest esse nisi informet subiectum suum, ergo nec aliquod; assumptum videtur ex hoc quod, sicut racio unica essendi sit et accidendi, quia aliter non cognosceretur a nobis analoga descripcio vel distinccio accidentis (nam substancia potest inesse et alias separari), ideo videtur quod analoga racio accidentis sit inesse substancie formaliter, non constituendo ipsam quid nec habendo potenciam per se esse.

[ENGLISH]

## ¶5 · 64.12–64.29

> [p. 64] Item, ponendo quantitatem et qualitatem linitas substancie adhuc oportet ponere informacionem earum qua immediate et formaliter substancia sit quanta et qualis; et illa non potest per se esse, ne sit processus in infinitum, ergo per idem nec aliquod accidens absolutum; assumptum patet eo quod informacio istorum accidencium potest suspendi ipsis manentibus (ut inquiunt), et per consequens oportet dare informacionem que sit vinculum quo substancia et tale accidens colligantur, quia aliter indubie non probabitur quantitas vel qualitas distincta a substancia, sed sufficerent partes quantitative et quidditas substancie; per hoc ergo quod substancia esset non tanta nec talis, alias autem est contrarie se habens, concludimus utrumque accidens. Et consimili argumento oportet dare informacionem distinctam que sit quantitas et qualitas, non autem ficta accidencia sic linita.

[ENGLISH]

## ¶6 · 64.30–65.17

> [p. 64] Item, cum illa accidencia non superfluunt sed subiacent tantum divine potencie, poterunt coextendi [p. 65] punctus, linea, superficies; et multo magis forma substancialis poterit per se esse; ex quo generantur mille difficultates, ut puta quod tam quantitas quam qualitas componitur ex suis partibus intensivis, quia coextensis illis et continuatis ad omnem punctum non restat quomodo componerentur, nisi intensive fuit integrum; et de quantitate ac tempore, de materia et forma suasum est alibi multipliciter quod obviant veritati. Videtur eciam contra adversarios quod continuum componitur ex suis partibus indivisibilibus, cum Deo auferente a celo extimam superficiem sine pluri foret residuum mundi finitum et habens superficiem extimam eadem racione qua prius, sicut Deus posset linire unum tale cum alio et continuare partes ad unum punctum; quibus compositis forent duo indivisibilia inmediata in eodem continuo.

[ENGLISH]

## ¶7 · 65.18–65.28

> [p. 65] Item, cum quantitas in hostia consecrata sit alba, rotunda et aliter diversimode qualificata, oportet quod illa sit subdita qualitati (ut dicit Thomas), primo quia nulla qualitas est alba vel sic qualificata, secundo quia est prioritas naturalis quantitatis ad qualitatem et ad alia accidencia que sequuntur, et tercio quia illa hostia potest alterari, ut patet ad sensum secundum valde disparem qualitatem; oportet ergo subiectum talis alteracionis esse aliud ab huius qualitate, quia secundum nullam partem potest ipsa taliter transmutari.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 61.14: Neither reason nor revelation teaches of such transsubstantiation.
- 62.11: We must be on our guard against idolatry.
- 63.4: To worship the elements is like worshipping an image.
- 63.23: An accident is only the truth that a substance is of such a sort. No collation of such accidents can be the host.
- 64.1: The accident is formally in the subject, but cannot give it quiddity nor exist by itself.
- 64.12: Quality and quantity are only accidents in forming a subject.
- 65.18: Quantity, according to St. Thomas, is the subject of qualities, which may vary in it from time to time.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 62: *subrepserant,* (print subrepserant, (bt subreperant)) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 61:
2. B: sibi prcsens ; E: est ibi sacramentaliter. 6. C: quod corrcxit
in qnam. ~. I) : convertetur ; E: converteretur. (). C: in in marg.
alia manu; ib. BD: panis autcm. n, 12. B: Christi ficticet ; C: /icticet
in marg. alia manu; in textu: fic. i3. AB: illa docent ; C: illud in marg.
alia manu. 17. D: vel revelacio. 21. B: scripturis; ib. B: pertinere;
E: pertinet. 23. ABCE : debet. 24. D: movit ; C: debct in marg. alia
manu. 25. E: nec de quanto. 28. E: debemus. 29. 1) : sic enim.
19. St. Aug. Opp. tom. III, 1, 63. Cf. De Baptismo contra
Donatistas Opp. IX, q8. Cf. Trial., pag. 240.

p. 62:
1. C: Jlagiciis tanquam ; correxit in marg. 4. Codd.: ergo firmiter ;
C in rasura: C (= capitulo) Jirmiter ; ib. D: in fine deest. 5. ABC: con-
currunt; ib. ABDE : CXIW*. 7, 8. E: qualiter debemus illis. 8. C:
cum in marg. alia manu. 9. D: surrepserant. 10. E: credere.
12. D: quod quod; ib. codd.: nichil credit ; C in rasura: cogit ; ib. D:
nisi id. i3. E: et papa non. 14. E: defecit. i5. D : fundatos.
19. D: ab deest. 23. C: corporis in marg. alia manu. 25. AB : per
deest; C in marg. alia manu addit.
4. Decret. Greg. IX, lib. I, titul. I, cap. I. 6. Cf. Decreti,
Pars 111, dist. II, De Consecracione, cap. XLII. 20. Cf. Ba-
ruch VI, 1.

p. 63:
2. E: Jesu deest. 3. D: poluerunt; ib. ABC: contra hostes contra.
7. D: totaliter ; ib. D: unite ; C in rasura : unite. 9. E: rignum.
11. BD : obiectum. 12. E: infideliter deest. 14. ABCD: foret deest.
i5. C in marg. : precopitarentur ; ib. D: ad ydolatriam. 16. D: quod
alia ; ib. E: et vini. 17. D: aliam partem ; ib. ABC: nec per idem;
D: quin per idem. 18. D: ac animam. 21. ABC : hoc ft; ib. D: huius.
26. E: esse alicuius.
4. Baruch VI, 56.

p. 64:
[. 1): commune accidcns; ib. D: predicabile. 2. E: accidens decst.
3. r>: in argumento septem; AB: aliquo modo septem. 4. E: infor-
maret. 4.) 5. ABCD : aliquod argumentum. 5,6. D: una racio unica ;
C: univoca ; ABE: unica racio unica. 6. C: essendi sic. 12. C: unitas
in marg. alia mann ; D : trinitas. i5. C : nisi sil. 17. ABCH : argumentttm
palet. iS. D: accidencia. 21. B: quia arguitur. 24, 25. D: esse nunc ;
C: esset nunc. 25. D: et talis. 29. ARDE: sit linita. 3i. E: poterint.

p. 65:
2. C: per se in marg. alia manu. 3. E: ut pura; C: ut deest.
6. AB: ubi intensive. j. D: suum integrum; C in marg. in alia manu.
8, 9. C: quod multipliciter obviant. 10. D: partibus et. i3. E: ut qua.
i5. ABC: ad omnem punctum. 16. D : so = secundo. 18. D: et hostia ;
ib E: alba et. 21. D: primo deest. 22. B: Sed quia. 23. D: et alia.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 61: Quoniam unus panis | et unum corpus multi | omnes de uno pane | prius primam; | ex secunda. | summo tribulacionis. | per graciam.
p. 62: esurit et alter | est ebrius. | nisi nobis. | essent superioris; | et faciendo. | ncc pcriuri. | magis care; | cum gaudio Christi meriantur.
p. 63: ad iudicium nobis manducamus et bibimus, | Quia morte Christi liberati sumus, huius rei memores in edendo camem et potando sanguinem eius, que pro nobis oblata sunt | necesse est ut. | nobis obligaciores | figitur; in | et amicorum. | ad summum;
p. 64: sit sanguis agni, non iam audiendo sed bibendo didicistis, qui sanguis super utrumque postem ponitur, quando non solum ore corporis sed eciam ore cordis accipitur aut hauritur. In utroquc etenim poste sanguis agni positus est, | quando sacramcntum passionis illius cum ore ad redempcionem sumitur, ad imitacioncm quoque intenta mente cogitatur. Nam qui sic redemptoris sui sanguinem accipit, ut imitari passionem illius necdum velit, in uno poste sanguinem posuit, qui eciam | in superliminaribus domorumponendus est. Qiiid enim spiritualiter domos nisi mentes Jiostras accipimus, in quibus per cogitacionem habitamus? Cuius domus superliminare est ipsa intencio que preeminet accioni. Qui igitur intencionem cogitacionis sue ad imitacionem 2? dominice passionis dirigit in superliminari domus agni sanguinem ponit. Vel certe domus nostre sunt ipsa corda in quibus quousque vivimus, habitamus et in superliminari domus agni sanguinem ponimus, quia crucem passionis illius in fronte portamus. De quo | et hauritur. | ante sacramentum. | quoque cum; | quam inlenta. | et in super. | qui mentea.
p. 65: quod illa. | adhuc agno subditur: Et edent carnes nocte illa assas igni. In nocte quippe agnum comedimus, quia in sacramento modo corpus dominicum accipimus, quando adhuc adinvicem consciencias nostras non | videmus. Que tamen carnes igne assande sunt, quia nimirum dissolvit carnes quas aqua coxerit, quas vero ignis sine aqua excoquit roborat. Carnes itaque agni nostri coxit ignis, quia eum ipsa vis passionis illius ad resurreccionem valenciorem reddidit atque | incorrupcionem roboravit. Qiti enim ex morte convaluerit, videlicet carnes illius ab igne duruerunt. Unde per Psalmistam eciam dicit: Exaruit velud testa virtus mea quid namque est testa ante ignem; nisi molle lutum? Sed ei ex igne agitur ut solidetur, | virtus igitur humanitatis eius velut testa exaruit, quia ab igne passionis ad virtutem incorrupcionis crevit. Sed sola redemptoris nostri percepta sacramenta ad veram sollempnitatem mentis non sufficiunt nisi eis quoque et bona opera iungantur. Quid enim pro- | dest corpus et sanguinem illius ore percipere et e perversis moribus contraire? Unde bene ad comedendum subditur: Et a^imos panes cum lactucis aggrestibus. Panes quippe sine fermento comedit qui recta opera sine corrupcione vane glorie exercet, qui man- | data misericordie sine admixtione peccati exhibet, ne perverse diripiat quod quasi recte dispensat. Hoc quoquepeccati fermentum miscuerant bone sue accioni quibus prophete voce per increpacionem Dominus | ligno sitbditur; | assumimus accipimus. | quod tamcn; | in igne. | cum ipsa. 10. incorrupcionem; | ad incorrupcionem. | videt carnes. | alias exaruerunt. | panes quidem. | qui manifesta.
```
