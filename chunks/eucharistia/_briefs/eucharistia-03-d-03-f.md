# Translation brief: eucharistia 03-d–03-f

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/eucharistia/wyc-eucharistia-03-d.md chunks/eucharistia/wyc-eucharistia-03-e.md chunks/eucharistia/wyc-eucharistia-03-f.md` once and fix what it reports.
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

## Glossary (the 452 rows these chunks use; the full file is GLOSSARY.md)

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
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| adolescentula | young maiden | Song 1:2, 6:7 (DR "young maidens"). Ruled 2026-10-02. |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| sacramentum (the eucharist); sacramentum altaris | sacrament; the sacrament of the altar | The plain sense, against the Augustinian row (*Incarn.*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.3, 3.30). |
| hostia; hostia consecrata | host; consecrated host | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.11, 1.22). |
| panis / vinum | bread / wine | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.8). |
| corpus Christi / corpus Domini | the body of Christ / the body of the Lord | Kept apart as the Latin alternates them. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.6, 1.10). |
| novella ecclesia / antiqua ecclesia | the newer church / the ancient church | The pair of 3.3; cf. *novelli*. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 3.3). |
| claritas (of the glorified body) | clarity | The dowry of the glorified body (with agility, subtlety, impassibility); not "brightness". Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-c). |
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
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| insolubilia | insolubles | The logicians' paradoxes of self-reference. Ruled 2026-10-02 (*Eccl.* 175.11). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |
| decretum; decreta | decree; the decrees | Gratian (*in decretis*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.14, 3.24). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| respectus; respectivus | relation; relational | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
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
| descripcio | definition | Not "description" (T. p. 363). |
| glosare | to gloss | Interpret so as to remove the difficulty (T. p. 366). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| glosa | gloss | The noun beside *glosare*. Ruled 2026-10-02 (52.10). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| inobedienciarius | disobedient man | The negative of *obedienciarius*. Ruled 2026-10-02 (146.11). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |
| humanitas | the humanity | The nature the Word assumed, body and soul; with the article (*humanitas sit Christus*, "the humanity is Christ"). Not "the human nature", which is *natura humana*. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| dimittere / dimissio (*naturam*) | lay aside / the laying-aside | Letting go the assumed nature, so the union would be dissolved. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 2.23). |
| assumere / assumpcio (*naturam*) | assume / assumption | Of the nature, as in the fathers. ⚠ Kept apart from the logician's *assumptum* "the assumption" (above): C note where the logical sense occurs. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| homo assumptus | the assumed man | A term of art (the Lombard's first opinion, *Sent.* III d. 6); keep "assumed" before "man", never "the man assumed". With the agent expressed (*homo assumptus a Verbo*) "the man assumed by the Word", which cannot be misread (coordinator, 2026-10-22). Ruled 2026-10-22 (Wilson; *Incarn.* 5.15). |
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
| novelli | the newer [doctors] | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 13.7). |
| sophistice | sophistically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 15). |
| de vi vocis / de vi sermonis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| gracia unionis | the grace of union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| exinanicio / exinanire / inanicio | emptying / empty | Phil. 2:7 (Douay "emptied himself"); *inanicio* (*Incarn.* 33) the same. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| minoracio | lowering | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| humanitus | humanly | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* passim). |
| suscipere / suscepcio (of the soul, the nature) | take up / taking-up | Kept apart from *assumere* "assume". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 31). |
| suppositum | supposit | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 34.24). |
| individuum | individual | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 35.7). |
| in quantum (reduplicative) | insofar as | As *secundum quod*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37.9). |
| unio | union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 39). |
| pars qualitativa | qualitative part | Body or soul as the parts that make up a man by kind; set against *pars quantitativa*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 43.5). |
| pars discretiva | discrete part | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 46.9). |
| in effectu | in actual fact | As against in potency or in name; ⛔ not "in effect" (modern "virtually"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 47.10). |
| animare | animate | The argument turns on it (45.30–46.4). Ruled 2026-10-22 (coordinator, delegated). |
| communicacio ydiomatum | communication of idioms | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.1). |
| predicacio actualis / aptitudinalis / habitudinalis / mixtim | actual / aptitudinal / habitudinal / mixed predication | *Habitudinalis* is its own term (the four MSS at 49.6), not under *habitudo*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.5–16). |
| denominativum | denominative | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 50.30). |
| Doctor Subtilis | the Subtle Doctor | Scotus. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.24). |
| convertibilis / converti | convertible / be convertible | Of terms. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 52.29). |
| forma totalitatis | form of totality | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 50.7). |
| quantus | quantified | The adjective beside *quantitas*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.22). |
| suppositacio | suppositation | Kept apart from *supposicio* "supposition". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.31). |
| construccio synecdochica | synecdochic construction | Beside *synecdochica locucio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.5). |
| moderniores loquentes | the more modern speakers | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 59.21). |
| passio (against *accio*) | being-acted-on | The category; G note at the first occurrence in a chunk. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 60.13). |
| supposibilis | that can be supposited | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 64.14). |
| dampnificare / dampnificacio | damage / damaging | Kept apart from *dampnum* "loss" and *dampnari* "be damned"; the argument of 65–68 turns on it. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 65). |
| per se / per accidens | of itself / by accident | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a (sufficienti) divisione | the topic from sufficient likeness / from (sufficient) division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| pretericio | being past | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| libere contradictorie | freely, as between contradictories | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 76.15). |
| insolubilitas | inextricability | As *insolubiliter*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| peccabilis | able to sin | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
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
| humidum infantile / radicale | the moisture of infancy / radical moisture | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 94.9). |
| conversari | live one's life (among men) | Beside *conversacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.25). |
| esse intelligibile | intelligible being | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 99.23). |
| extraneare / extraneacio (supposicionis) | estrange / estrangement (of supposition) | *Affeccio extraneandi* "an affection of estrangement". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 98.16). |
| ministerialiter | ministerially | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 100.17). |
| res racionis | thing of reason | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| predicacio secundum essenciam / formalis | predication by essence / formal predication | Wyclif's modes of predication (cf. *predicacio secundum causam*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 115–116). |
| forma substancialis | substantial form | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| concepcio (figure) | conception | The grammatical figure. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| accidens | accident | The category; *accidit* "befalls". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| denominacio respectiva | relational naming | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 120.17). |
| figura / figuratum | figure / thing figured | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 121.23). |
| incepcio | beginning | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 121.16). |
| conversio (of a proposition) | conversion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.30). |
| humanitacio | humanation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 126.12). |
| deduccio | deduction | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.21). |
| racio (individual, personal) | account | *Racio individui / persone* "the account of an individual / a person", as *racio speciei*; not "aspect" (the row against *substancia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 8, 129–132). |
| vir (against *homo*) | man (*vir*) | Where Wyclif sets *vir* against *homo*, the Latin in parentheses. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 129.15–26). |
| univocare / univocari | make univocal / be univocal | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 131.3). |
| res secunde intencionis | things of second intention | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.25). |
| complexio | complexion | The mixture of qualities. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137–138). |
| materia proxima / remota | proximate / remote matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137.1). |
| personari | be made a person | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 134.10). |
| colorate | with colour enough | With a plausible ground (cf. *color*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 134.26). |
| res communis / res communes | the common thing / common things | The realist universal the *moderni* do not conceive (first root of their error). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 144.27). |
| distinccio racionis | distinction of reason | Beside *differencia formalis*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 145.23). |
| conversio naturarum / confusio naturarum | conversion of the natures / confusion of the natures | Kept apart from *conversio* of a proposition. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 143.9). |
| moderni (bare) | the moderns | Beside *moderni doctores* "the modern doctors". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 142.10). |
| principiare (active) | be the principle of | Beside the passive *principiari* "be constituted from principles". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 147.4). |
| assumere personale | personal assuming | The infinitive used as a noun; kept apart from *assumpcio personalis* "personal assumption". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 146.33). |
| moderniores (bare) | the more modern | Beside *moderniores doctores* "the more modern doctors". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 151.17). |
| supposicio simplex / supposicio personalis | simple supposition / personal supposition | Supposition theory. *Simpliciter / personaliter supponere* "stand with simple / personal supposition": NOT the *simpliciter / secundum quid* pair, C note where the two could be confused. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 152.5–12). |
| transsumpcio | transumption | Beside *transsumptive*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 153.28). |
| personalitas | personality | The scholastic term: what makes a person a person, not character. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 155). |
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
| augmentacio | augmentation | Growth in quantity (Aristotle's motion of increase). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 180). |
| beatificabilitas | beatifiability | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 181). |
| passionaliter | as an attribute | Beside *passio* (the proper attribute). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 181). |
| mocio / motus (paired) | motion (*mocio*) / movement (*motus*) | Only where Wyclif pairs them; otherwise "motion". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 180). |
| posicio anime | the laying-down of the soul | John 10:17–18; not the logical *posicio* "position", C note. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 183.3). |
| causancia / causacio | causing / causation | Kept apart (both at 187.30–34). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 185.16). |
| personare (active) / personacio | make a person / personation | Beside the passive *personari* "be made a person". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 188.16, 188.32). |
| peticio (principii) / petitur | begging [of the question] / is begged | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.23). |
| perfeccio simpliciter | perfection without qualification | After *simpliciter* "without qualification". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.1). |
| transsubstanciacio | transubstantiation | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.10). |
| multiplicative | multiplicatively | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 193.20). |
| in divinis | among the divine [persons] | Keeps "Godhead" for *deitas*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 196.18). |
| partes proporcionales | proportional parts | The halving division of a continuum. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 194.24). |
| multiplicacio dimensionalis | dimensional multiplication | One body in several places by its dimensions. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.6). |
| proporcio racionalis | rational proportion | The mathematical ratio. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 207.7). |
| a maiori vel pari | from the greater or from the equal | Arguments *a maiori*; cf. *locus a maiori*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 209.5). |
| sensibile commune | common sensible | Aristotle's common sensibles (number, motion, figure); the term of art, against the §D row "perceptible". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 209.23). |
| mocio progressiva / motus progressivus | progressive motion | Locomotion. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 205.28). |
| communioritas | greater commonness | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 210.15). |
| multiplicacio concomitancie | multiplication of concomitance | Cf. *gracia concomitancie*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 213.21). |
| nomen appellativum | appellative name | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 213.29). |
| assertibile | assertible | The thing a proposition asserts. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 215). |
| superioritas / inferioritas terminorum | superiority / inferiority of terms | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 215). |
| homo communis | the common man | The universal man, with *res communis*; not "the ordinary man". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 218.3). |
| moderni loquentes | the modern speakers | Beside *moderniores loquentes*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 221.20). |
| mixtim (bare) | in a mixed way | Beside *predicacio mixtim*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 230.21). |
| signum reduplicatum | the reduplicated sign | The reduplicative word (*secundum quod*, *in quantum*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 230.23). |
| supposicio | supposition | Of a term (supposition theory) or of a premiss laid down (cf. *supponitur* "it is supposed"); the English word serves both, C note where it matters. Kept apart from *suppositacio* "suppositation". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 102.8). |
| univocus | univocal | Beside *univoce*, *univocare*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 102.13). |
| lex proximitatis | the law of neighbourhood | The duty to love one's neighbour (*proximus*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 101.29). |
| negacio preposita toti | a negation placed before the whole | The negation governing a whole proposition. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 103.21). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |
| sacramentaliter | sacramentally | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| vere | truly | A mode adverb: one word each, never two merged, kept where Wyclif puts it. ⛔ Never "really" (that is *realiter*). Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| spiritualiter | spiritually | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| virtualiter | virtually | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| figurative | figuratively | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
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
| figurare | figure | Both senses: to prefigure (the lamb figured Christ) and to shape (*figurare Deum nostrum*), which Wyclif plays on; one English word keeps the pun. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-c 10; 21.29). |
| supponere pro | stand for | Supposition; with *supposicio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 24.27). |
| sensualiter | sensually | Berengar's oath word (*Ego Berengarius*); kept apart from *sensibiliter* "perceptibly". A mode adverb, one word. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 26.1, 30.24). |
| predicacio figurativa | figurative predication | A synonym of *predicacio tropica*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 35.18). |
| mixtum; mixta | mixed body; mixed bodies | The compounds of the elements. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 42.23, 44.10). |
| describere | define | The verb of *descripcio* "definition". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 48.9). |
| anichilacio; anichilare | annihilation; annihilate | The key term of ch. 3. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 03-a passim). |
| illusio | illusion | Kept apart from *decepcio* "deception". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 57.10, 57.24). |
| aliquitas | somethingness | Being a something (*aliquid*). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 60.27). |
| cedere (in) | give way (into) | Of the bread passing into the body. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 58.3, 60.9). |
| informacio; informare | informing; inform | Of a form in its subject; not "information". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 64.13). |
| linire; linitus | smear (on); smeared | The modern doctors' accidents "smeared on" the quantity. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 64.12, 64.29). |
| accidens predicamentale | accident of the categories | Kept apart from the predicable *accidens*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 64.1). |
| revera | in truth | Kept apart from *vere* "truly". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 63.4). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| magisterium | rule; of teaching, the teaching office; *quale magisterium* "what a feat of mastery" (*Incarn.* 137.14) | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| denominacio; denominare | naming; to name | The argument turns on it. Ruled 2026-10-02 (*Eccl.* 17, 391.17, 398.2). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| continuacio (of bodies, the act) / discontinuacio; continuare / discontinuare | continuation / discontinuation; make continuous / make discontinuous | The making of several bodies into one continuum (*Incarn.* ch. 12), G note at first use: not "carrying on". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.30, 211.12). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| dampnacio | CONTEXTUAL: damnation / condemnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). Of a judgement passed on a teaching (*dampnacio istius sentencie tamquam heretice*, *Pot. pape* 84.10) "condemnation"; ruled 2026-10-07. |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| univoce | univocally | Ruled 2026-10-02 (*Eccl.* 21, 514.4). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| memoriale | memorial | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
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
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). Beside *consecrare* (*consecrat et conficit*) "confect", so the pair stays two. Ruled 2026-11-07 (Wilson, "confect works"; *Euch.* 16.10). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| deliramenta | ravings | Ruled 2026-10-07 (*Pot. pape* 06-c). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| memorativa potencia | memorative power | A faculty of the soul (the "power" sense of *potencia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 219.27). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| episcopi cesarei | caesarean bishops | Extends *prelatus / sacerdos cesarius*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 331.24). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| latitudo (of a quality) | latitude | The intension/remission term. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 352.4). |
| decimacio | tithing | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 359.26). |
| decimantes | tithe-payers | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 359.24). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| coloracior | more colourable | Comparative, with the *color* / *colorabilis* rows. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 384.15). |
| ars cesarea | the caesarean art | After *papa cesareus*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| servitus ydolorum | servitude of idols | Beside *servitus laboris*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| ingeniacio | wit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 394). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| insolubiliter | inextricably | Kept apart from *insolubilia* "insolubles". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 404). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |
| nimis | exceedingly | Medieval intensive (= *valde*); "too much" only where excess is the point. Ruled 2026-10-12 (close-out R2; *Pot. pape* 169.2). |
| fingere (a miracle) | feign | "imagine". Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.11, 1.14). |
| recitare | recite | To report, rehearse. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.4, 3.10, 4.18). |

---

## Chunk 03-d: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-03-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-03-d
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "65.29–69.21"
divisions: "cap. 3 (heading 'CAPITULUM TERTIUM.' at 53.0); part 4 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "883 words; 870 confirmed by the vote; 12 runs stood by rule; 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n136–n140 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 3, part 4: [TITLE]

## ¶1 · 65.29–66.5

> [p. 65] Sed contra istud arguitur primo per hoc quod nulla quantitas potest taliter maiorari, nam vel manet quantitas que maioraretur vel non. Si manet, vel est permixta cum quantitate que advenit; et patet [p. 66] quod tunc ad omnem punctum fit nova quantitas antiqua corrupta; si vero manet inpermixta, non illa fit maior sed generaliter nova que non est sacramentum, ex quibus fit sacra et non sacra quantitas bipartita.

[ENGLISH]

## ¶2 · 66.6–66.21

> [p. 66] Secundo arguitur per hoc quod rarefacta quantitate ad omnem punctum, cum experimentum docet quod potest rarefieri, oportet quod antiqua quantitas que fuit sacramentum totaliter corrumpatur et una quantitas non sacramentum totaliter generetur. Non enim fingendum est aliquid quod consecret continue novam quantitatem; cum tamen non desinet corpus Christi esse ibi beatum accidentibus sic remanentibus sub forma panis et vini, quia aliter trepidaret christianus per quantumlibet breve tempus post consecracionem accipere sacramentum, cum ex sibi dubio calor vel aliud agens mutando subiectum fecit accidens succedere, quod non fit sacramentum, cum prius causaliter sit sacramentum sensibile quam corpus Christi sit ibi sacramentaliter, ut patet de natura confeccionis.

[ENGLISH]

## ¶3 · 66.22–66.33

> [p. 66] Tercio arguitur per hoc quod signata a terra pedali cui linitur pedalis quantitas, illa terra est et foret formaliter pedalis in illo casu possibili quo Deus anichilaret quantitatem illam sed servaret terram omnino inmotam in situ eodem; sed tunc remaneret formaliter pedalis, ergo est dare unam pedalitatem intrinsecam priorem illa linita qua formaliter est pedalis; et illa non potest per se esse, cum sit istam terram sic esse quantam; et distinccionem illius nemo potest destruere; et eadem est consideracio de qualitate quod non habet propriam raritatem, densitatem et similes qualitates distinctas a subiecto.

[ENGLISH]

## ¶4 · 67.1–67.15

> [p. 67] Item, secundum falsigraphos substancia potest manere quanta sine quantitate distincta et sic de omni respectu; nec est racio quin per idem sic senciendum est de toto genere qualitatis, ergo non est dare accidens preter substanciam; cum ergo constat ex sensu quod remanent post consecracionem res materiales, restat illis concedere quod remanent materiales substancie. Quid ergo foret istud corpus remanens nisi panis et vinum, ut dicit decretum Romane ecclesie? Cum autem hoc sit argumentum ad hominem, peto maiorem ut datam. Minor patet ex hoc quod eque ad quantitatem potest esse motus ut ad qualitatem; eque ponunt philosophi et probant raciones alia accidencia distingui ut qualitates, eque ponunt qualitates non posse separari a subiecto ut alia accidencia.

[ENGLISH]

## ¶5 · 67.16–67.24

> [p. 67] Unde hic mirantur philosophi quare theologi ponunt omnem qualitatem posse per se esse et non formam substancialem materialem, que (in quantum substancia) pocius haberet racionem per se standi et sic materia prima posset esse informis quod negant. Si dicitur quod Aristoteles vel racio illud dictat, eque vel plus dictat quod qualitas non poterit per se esse; si dicitur quod fides hoc postulat, pure petitur quod probarent.

[ENGLISH]

## ¶6 · 67.25–68.11

> [p. 67] Mirantur secundo quam graciam meruit qualitas, quam approbant posse per se esse, cum eque sicut potest salvari figuram esse figuratum et sic de pulcritudine cum naturali potencia et aliis donis Dei, sic potest probabiliter teneri de toto genere qualitatis. Et tamen paucas alias qualitates ponunt de tercia specie qualitatis, cum eque propter variacionem modi habendi substancie sine aliquo accidente quod poterit per se esse potest salvari substancia utrobique; [p. 68] nam sicut lux consequitur ad solem ut passio ad subiectum, ita consecuntur qualitates prime ad elementa; et sicut ad presenciam lucis solis cum capacitate in medio naturaliter sequitur lumen eius vel illuminacio, ita secundum varietatem mixtionis elementorum in ceteris mixtis consecuntur qualitates secunde, aliis respicientibus lucem vel factum preteritum ut calores et passiones, et aliis respicientibus figuras, mollicies et duricies, levitas et asperitas; poneret ergo sic opinans omnes qualitates quas ponunt philosophi et nullas posse per se esse vel omnes.

[ENGLISH]

## ¶7 · 68.12–69.5

> [p. 68] Mirantur tercio quod sic opinantes ponunt unionem, continuacionem, contiguacionem et substancia esse qualitates que poterunt per se esse; propter hoc principium non potest esse motus a contradictorio in contradictorium sine generacione vel corrupcione nove rei; et non dicunt sic de motu, tempore et ceteris respectibus; nam si ista tria poterunt per se esse, tunc illorum est dare unionem distinctam, et sic de continuacione et contiguacione sine fine. Non enim videtur racio quod ad continuandum A cum B sequitur continuacio que sit qualitas distincta potens per se esse, quin per idem ad continuandum continuaciones illas sequeretur alia et sic in infinitum; et posita carencia continuacionis cum inmediacione continuabilium ponitur contiguacio sine nova re denominante formaliter, que poterit per se esse; et iterum in confinio continuatorum forent infinite continuaciones superficiales, lineares vel punctuales; quod negat opinans nec dicet racionem quod anichilacio, transsubstanciacio et similia sint veritates distincte et [p. 69] sic nec substancie nec accidencia, cum poterunt per se esse, quin per idem est dare veritates alias predicamentales duodecim generum, ut olim posuerunt philosophi. Et patet quante error fictus de hoc sacramento perturbat philosophos.

[ENGLISH]

## ¶8 · 69.6–69.21

> [p. 69] Item, iuxta hanc viam non convinceretur philosophice aliqua materialis substancia, quia omnis experiencia de motu vel transmutacione subiecti aut aliquo allegando posset salvari sine tali materiali principio, ergo frustra est ponere talem inperfectam substanciam, cum nec racio nec experiencia hanc convincit. Sic enim possent sompniari infinite substancie sine racione movente. Assumptum patet iuxta sic loquentes, cum ponunt accidencia posse per se agere et pati eque efficaciter ut modo sine substrata materiali substancia. Cum ergo iuxta philosophorum principia frustra fit per plura, quod fieri potest per pauciora et natura agit breviori modo quam poterit, videtur esse phisici negare huiusmodi materialem substanciam sensibilem et ponere sufficienter ad finem nature aliqua predicamenta accidentis.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 65.29: Answer: 1. If the quantity were altered, the subject would no longer be the same.
- 66.4: 2. Such an alteration may take place through rarefaction caused by heat or other agency.
- 66.21: 3. Although the quantity be changed, the subject remains quantitative; this shews that quantity is only a condition o the subject.
- 67.1: If substance can be quantitative without distinct quantity, accident does not exist without substance; and if substance remains, why is it not of bread and wine?
- 67.10: This is merely an argumentum ad hominem, resting on a false premiss.
- 67.16: The postulates of our opponents land them in the contradiction that matter may exist without form.
- 67.25: Why is quality to be specially distinguished above other accidents?
- 68.12: Other inconsistencies as to union &c., which our opponents distinguish from the other predicaments.
- 69.6: It accidents can exist of themselves, we need not postulate substance at all.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 66: *bipartita.* (print = bt) [BT-ONLY]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 65:
2. C: per se in marg. alia manu. 3. E: ut pura; C: ut deest.
6. AB: ubi intensive. j. D: suum integrum; C in marg. in alia manu.
8, 9. C: quod multipliciter obviant. 10. D: partibus et. i3. E: ut qua.
i5. ABC: ad omnem punctum. 16. D : so = secundo. 18. D: et hostia ;
ib E: alba et. 21. D: primo deest. 22. B: Sed quia. 23. D: et alia.

p. 66:
t. E: quod deest: ib. E: sit. 3. D: sed generatur. 10. E: generatur.
n. D: continue deest. i3. AB: Christi deest; C in marg. alia manu;
ib. D: esse relativum. i5. E: quantumcunque. l5, 16. E: per conse-
cracionem. 23. E : unitur. 24. D : illo deest. 25. D: et servaret.
2S. E: unita. 3o. ABC: esse sic.

p. 67:
4, 5. C: accidais deest. 6. B: remanet. u. D: Et minor.
16. E: qualiter. 20. D: prima decst; ib. AE: possit; ib. D: negandum.
21. B: illud debeat. 28. C: potencia in marg. alia manu. 3i. D : quali-

p. 68:
1. C in marg. alia manu: ad. 4. D: consequitnr . 6. D: in cor-
poribus. 8. E: colores ; ib. ADE: et potestates. 9. ABC: mollies;
ib. D: ut levitas ; E: et levitas. i3. substancia; C in rasura: subiecta ;
recte: contiguacionem substancie. i5. E: ad contradictoria in.
18. ABC: si deest; ib. E: potuerunt. 19. ABC: illarum. 21. AB: a
continuandum. 22. D: respondetur ; ib. ABCD : quesit; C correxit: est.
24. D: requiritur. 29. ABCD : liniares ; ib. C: punctales ; correxit.

p. 69:
1. ABC: nec deest before substancie; DE: sic deest; ib. C: poterint ;
E: potuerunt. 4. AB: hoc deest. 8, 9. ABC: aut quo ; C corr. : aliquo.
9. AB: materia; C corr. in marg. i3. ABCD : argumentum patet.
18. ABCE: aget; ib. ABCD : quo. 19. B: esse deest; ib. ABCD : philoso-
pliicum; D : philosophicwn veraciter. 20. D : insensibilem ; ib. B : exponere.
21 . D : predicamenta alia. 22. ABE : ad ista ; C corr. : in isto. 23. D : quam
tantum. 20. CD: transmutacionis ; ib. B: crearet in marg. ; E: careret;
A: careret extinct. crearet in marg. 29. ABCD : argumentum; ib. C:
posito in marg. alia manu. 3o. BCDE : alienatum ; A : ali<" alimentum.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 65: quod illa. | adhuc agno subditur: Et edent carnes nocte illa assas igni. In nocte quippe agnum comedimus, quia in sacramento modo corpus dominicum accipimus, quando adhuc adinvicem consciencias nostras non | videmus. Que tamen carnes igne assande sunt, quia nimirum dissolvit carnes quas aqua coxerit, quas vero ignis sine aqua excoquit roborat. Carnes itaque agni nostri coxit ignis, quia eum ipsa vis passionis illius ad resurreccionem valenciorem reddidit atque | incorrupcionem roboravit. Qiti enim ex morte convaluerit, videlicet carnes illius ab igne duruerunt. Unde per Psalmistam eciam dicit: Exaruit velud testa virtus mea quid namque est testa ante ignem; nisi molle lutum? Sed ei ex igne agitur ut solidetur, | virtus igitur humanitatis eius velut testa exaruit, quia ab igne passionis ad virtutem incorrupcionis crevit. Sed sola redemptoris nostri percepta sacramenta ad veram sollempnitatem mentis non sufficiunt nisi eis quoque et bona opera iungantur. Quid enim pro- | dest corpus et sanguinem illius ore percipere et e perversis moribus contraire? Unde bene ad comedendum subditur: Et a^imos panes cum lactucis aggrestibus. Panes quippe sine fermento comedit qui recta opera sine corrupcione vane glorie exercet, qui man- | data misericordie sine admixtione peccati exhibet, ne perverse diripiat quod quasi recte dispensat. Hoc quoquepeccati fermentum miscuerant bone sue accioni quibus prophete voce per increpacionem Dominus | ligno sitbditur; | assumimus accipimus. | quod tamcn; | in igne. | cum ipsa. 10. incorrupcionem; | ad incorrupcionem. | videt carnes. | alias exaruerunt. | panes quidem. | qui manifesta.
p. 66: dicebat: Venite ad Bethel et impie agite. Atque post pauca: Et sacrificate de fermentato laudem. De fermentato namque laudem immolat qui Deo sacrificium de rapina parat. Lactuce vero aggrestes valde amare sunt. Carnes autem agni cum lactucis aggrestibus | sunt edende, ut cum corpus Redemptoris accipimus, nos pro peccatis nostris in fletibus affligamus, quatenus ipsa amaritudo penitencie abstergat a mentis stomacho perverse humorem vite. Ubi et subditur: Non comedetis ex eo crudum quid neque coctum | aqua. Ecce iam nos ipsa verba historie ab intellectu historiaco repellunt. Numquid, fratres karissimi, Israeliticus illepopulus in Egypto constitutus comedere agnum crudum consueverat, ut ei lex dicat, non comedetis ex eo crudum quid? Ubi et additur: Nec | coctum aqua. Sed quid aqua nisi humanam scienciam designat iuxta hoc quod per Salomonem dicitur sub hereticorum vcce: Aque furtive dulciores sunt. Qidd crude agni carnes, nisi inconsideratam ac sine reverencia cogitacionis relictam illius humanitatem. Omne | enim quod subtiliter cogitamus quasi mente coquimus. Sed agni caro nec cruda edenda est nec aqua cocta, quia redemptor noster nec purus homo estimandus est neque per humanam sapienciam qualiter Deus incarnari potuit cogitandus. Omnis enim qui redemp- | torem nostrum purum hominem credit quid iste aliud quam crudas agni carnes comedit quas videlicet coquere per divinitatis eius intelligenciam noluit? Omnis vero qui incarnacionis eius misteria iuxta humanam sapienciam discutere conatur carnes agni | cum eum. | crudi quid. | nec cruda | ut purus homo. | quas valet.
p. 67: aqua vult coquere, id est, dispensacionis eius mistevium per dissolutam vult scienciam penetrare. Qiii ergo paschalis gaudii sollempnitatem celebrare desiderat agnum nec aqua coquat nec crudum comedat, ut | neque per hurnanam sapienciam profunditatem incarnacionis illius penetrare appetat neque in eum tamquam in hominem purum credat, sed assas igne ccirnes comedat, ut dispensari omnia per Sancti Spiritus potenciam sciat. De quo adhuc recte subiungitur: | Caput cum pedibus et intestinis vorabitis, quia Redemptor noster est alpha et o, Deus videlicet ante secula et homo in fine seculorum. Et sicut iam prediximus, fratres, Paulo attestante didicimus quod caput Christi Deus; caput ergo agni vorare est divi- | nitatis illius fidem percipere, pedes vero agni vorare est vestigia humanitatis illius amando et imitando perquirere. Quid vero sunt intestina nisi verborum illius occulta et mistica mandata? Que tunc voramus, cum verba vite cum aviditate sumimus. In quo de- | voracionis verbo quid aliud quam pigricie nostre torpor deprehenditur? Qui eius verba atque misteria per nosmetipsos non requirimus et dicta ab aliis audimus inviti. Non remanebit ex eo quidquam usque mane, quia eius dicta magna sunt sollicitudine | discucienda, quatenus prius quam dies resurreccionis appareat in hac presentis vite nocte omnia mandata eius intelligendo et operando penetrentur. Sed quia valde difficile est, ut omne sacrum eloquium possit | id est | assas tantum; | assas tamen. | atque inteslinis; | caput vero; | quidquam ex eo. 26. | eius appareat; | vite voeacione communia; | omnia nocte; | vocacione omnia. | po*set.
p. 68: intelligi et omne eius misterium penetrari, recte subiungitur: Si quid remanserit, igni conburctis. Quod ex agno remanet igni cotiburimus, quando hoc quod de misterio incarnacionis eius intelligere et penetrare non possunius, potestati Sancti Spiritus humiliter | reservajjius, ut Jion superbe quis audeat vel cojitemp- Jiere vel denunciare quod non intelligit: sed hoc igjii tradat, cum Spiritui Sancto reservat. Quia igitur qualiter edendum sit pasca agnovwius, jiunc autejn a qualibus edi debeat agnoscajjius. Sequi- | tur: Sic autem cojJiedetis illiun: Renes vestros accingetis. Qiiid in renibus nisi delectacio carjiis accipitur? Unde et Psaimista postulat dicens:' Ure renes meos. Si enim voluptatem in renibus esse nesciret, eos uri minime petisset. Unde quia potestas dyaboli | in hujjiano genere jjiaxwie per luxuriam prevaluit, de illo voce dojJiinica dicitur: Potestas eius in lujjibis eius. Qui ergo pasca coniedit habere renes succinctos debet, ut qui sollempnitatem resurreccionis atque incorrupcionis agit corrupcioni iam per nulla vicia | subiaceat, voluptates edomet, carnem a luxuria restringat. Neque enim cognovit que sit sollejjipjiitas incorrupcionis qui adhuc corrupciojii per incontinenciam subiacet. Hec quibusdam dura sunt, sed angusta est via que ducit ad celuni, et habuimus iam jjiulta exempla | cojitinencium. Unde et adhuc subditur: Calceajnejita habebitis in pedibus. Quid etejiini sunt pedes nostri Jiisi opera? Quid vero calceamenta tiisi pelles mortuorum animalium; calceajjiejita autejupedes jnujiiunt. Que | videlicet qui. | fiic iam. | Nec opera. Quidenim; | nisi pedes.
p. 69: vero sunt mortua animalia, ex quorum pellibus nostri muniantur pedes, nisi antiquipatres qui nos ad eternam patriam precesserunt. Qiiorum dum exempla conspicimus, nostri operis pedes munimus. Calceamenta | ergo inpedibus habere est mortuorum vitam conspicere et nostra vestigia a peccati vulnere custodire. Tenentes baculos in manibus. Qiiid lex per baculum nisi pastoralem custodiam designat? Et notandum quod prius precipimur renes accingere, postmodum baculos lotenere, quia illi debent curam pastoralem suscipere, quia iam sciunt in suo corpore fluxa luxurie edomare, ut cum aliis forcia predicant, ipsi desideriis mollibus et voluptatibus non succumbant. Bene autem subditur: Et comedetis festinanter. | Notate, fratres, notate quod dicitur festinantes. Mandata Dei, misteria Redemptoris, celestis patrie gaudia cum festinacione cognoscite et precepta vite cum festinacione implere curate. Quia enim adhuc hodie licet bene agere scimus: utrum cras liceat igno- | ramus. Eestinantes autem pascha comedite, id est, ad sollempnitatem patrie celestis anhelate. Nemo in huius vite itinere torpeat, ne in patria locum perdat. Nemo moras ad appetenda studia innectat sed cepta perficiat, ne minime liceat implere quod inchoat. Si ad | amorem Dei pigri non sumus, adiuvat ipse quem amamus. | quibus pellibus. | illi debent | sarcinam predicant ipsi desidiis. | ad hoc. | Det Christi.
```

---

## Chunk 03-e: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-03-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-03-e
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "69.22–73.18"
divisions: "cap. 3 (heading 'CAPITULUM TERTIUM.' at 53.0); part 5 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "866 words; 856 confirmed by the vote; 10 runs stood by rule; 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n140–n144 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 3, part 5: [TITLE]

## ¶1 · 69.22–71.3

> [p. 69] Nec valet allegare in isto miracula ad colorandum quamcunque opinionem contrariam veritati; non enim fundatur fictum miraculum. Secundo quia sic accidens factum subiectum transsubstanciacionis crearet in casu et anichilaret et tamen cum sit res inanimata, non habens substanciam que sustentaret eius mutacionem, nulla una permanens qualitas posset pati vel agere. Assumptum sic arguitur: Posito quod calor per se agat in sacramento, quousque fiat alimentum [p. 70] et redeat eadem materia, patet quod diu erit antequam redibit materia panis (ut concedunt adversarii), et tota qualitas que iterum corrumperetur anichilabitur, sicut qualitas que interim producetur creabitur, cum non sit materia que suscipiat illam transmutacionem naturalem, sic quod qualitas non corrumpetur in potencia materie, sed corrumpetur in nichilum vel totaliter producitur ex nichilo, sicut agens naturale suscitat priorem materiam panis ex nichilo. Talis enim substancia non generatur ex accidente, ut patet quod, licet ecclesia sollempnizet hec signa supra substancias, sicut transfert ad contraria nomina ministrorum ecclesie, manente tamen disposicione quam Deus instituit vel variancia, non oportet quod natura rei proporcionaliter consequatur, ut posito quod anima vel quecunque forma materialis inmediate actuet huiusmodi accidens absolutum per se servatum foret substancia composita ut est modo et vel nulla creatura potest per se esse sine miraculo vel vocatum accidens potest per se esse sine novo miraculo vel fingi posset per idem miraculum. Unde tolleretur omnis descripcio creature. Sic enim fingunt sollempnes doctores quod generato verme de hostia anima sensitiva induceretur in accidencia sine materia; quare ergo non consumeretur ex tibi dubio tota materialis substancia facta generacione et motu inter talia accidencia, ymmo cum materia individuatur ab instanti sue creacionis, videtur quod nova creatur et non sic inevitabiliter antiqua sustentatur et sic quot substancie convertuntur in corpus Christi tot materie prime sunt perdite [p. 71] et nemo nostrum cognosceret huiusmodi materialem substanciam. Quomodo ergo auderet quisquam conficere vel iurare de actu materialis substancie.

[ENGLISH]

## ¶2 · 71.4–71.14

> [p. 71] Item, ecclesia non est oneranda novitate tali insolita nisi vel fides scripture vel vivax racio vel efficax sanctorum testimonium ad hoc cogat, sed quodlibet istorum trium deficit predicto errori de sacramento altaris, ergo et racio sic onerandi ecclesiam. Assumptum patet ex multis testimoniis sanctorum et veritate ac sufficiencia legis Christi. Sic enim coleretur abhominacio desolacionis, quia accidens entitatis minime, tamquam Deus, vel saltem coleretur tamquam sacrum signum mendacissime accidens loco substancie et imponeretur Deo quod sit auctor mendacii.

[ENGLISH]

## ¶3 · 71.15–71.19

> [p. 71] Quantum ad scripturam, patet in sex locis predictis de hoc sacramento tangentibus quod nec ponunt accidencia sic esse sine subiecto, nec antecedens ad hoc. Et idem est iudicium de qualibet parte scripture in qua est omnis veritas.

[ENGLISH]

## ¶4 · 71.20–71.25

> [p. 71] Quantum ad racionem, patet luce clarius quod aliena est a fundacione existencie huiusmodi accidencium sine subiecto, ymmo ut loyci instant, inpossibile est accidens esse nisi unum accidens subiectet aliud; et cum quelibet creatura sit accidens deitati, patet quod oportet esse accidens sine subiecto suo cui inhereat.

[ENGLISH]

## ¶5 · 71.26–71.30

> [p. 71] Et quantum ad testimonium doctorum, patet quod antiqui sancti testati sunt concorditer quod accidens non potest esse sine subiecto cui inhereat; tamen suffecit eis sicut philosophis ponere accidens quod est substanciam esse accidentatam.

[ENGLISH]

## ¶6 · 71.31–72.2

> [p. 71] Et quantum ad decretalem, patet quod non est forcior quam decretum pape et CXIV episcoporum [p. 72] qui diffinierunt panem et vinum remanere post consecracionem (ut sepe recitatum est).

[ENGLISH]

## ¶7 · 72.3–72.10

> [p. 72] Unde quantum ad testimonia sanctorum, reduco ex multis triplex testimonium Augustini;. primo illud dictum de Quantitate Anime capitulo IVº, ubi dicit quod corpus non potest esse sine altitudine; prorsus, inquit, non dubito corpora omnia longitudine, latitudine et altitudine carere non posse, sed numquid potest cogitari ista tria non esse nisi in corporibus? Non intelligo, inquit, quomodo alibi esse possint.

[ENGLISH]

## ¶8 · 72.11–72.27

> [p. 72] Et quoad qualitatem scribit IIº Soliloquiorum XIIº capitulo: Esse aliquid in aliquo nos non fugit duobus modis dici. Uno modo localiter ut corpus seiungi atque alibi esse possit, ut hoc lignum in hoc loco et sol in oriente. Altero autem quo ita est aliquid in subiecto, ut ab eo nequeat separari, ut in hoc ligno forma et species quam videmus, ut in sole lux, ut in igne calor et in anima disciplina et si qua sunt alia. Ista, inquit, vetustissima nobis sunt et ab ineunte adolescencia studiosissime percepta et cognita, quia non possum de hiis interrogatus, quin ea sine ulla deliberacione concedam. Et sequitur: Illud vero quod interrogasti, quis concesserit aut cui posse fieri, videatur ut id quod est in subiecto maneat ipso intereunte subiecto? Monstruosum enim et a veritate alienissimum ut id quod non esset nisi in ipso esset, eciam cum ipsum non fuerit possit esse.

[ENGLISH]

## ¶9 · 73.1–73.18

> [p. 73] Et tercio Epistola XL ad Dardanum sic loquitur Augustinus: Tolle ergo ipsa corpora qualitatibus, qualitates corporum nec erit ubi sint, et ideo necesse est ut non sint. Et idem sine retractacione sepe sentenciat, ut patet De Trinitate IXº et XIIIº, VIº De Trinitate VIº et IXº, De Trinitate IIIº et in De Moribus Ecclesie capitulo VIº. Nec valet glosare dicta sancti quod intelligit sic esse nisi fiat miraculum, tum quia nullo existente miraculo non foret aliqua creatura, tum eciam quia nemo potest mereri vel beatificari sine miraculo, ymmo maneret ubique incertitudo, quando et ubi foret miraculum, et per consequens periret certitudo de quacunque materiali substancia et sic naturalis philosophia, tum tercio quia non magis probabiliter fingitur miraculum in hoc venerabili sacramento, quam fingi posset quidquid volueris; et per istam glosam tolleretur consequenter quodlibet sanctorum testimonium vel scripture.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 69.22: The plea of miracle is ungrounded, for it is not a question of change in things, but of misuse of language.
- 70.21: . If (as in the case of a maggot bred on the host) a sensitive soul can be induced into mere accidents, we can have no knowledge of substance.
- 71.4: This error is a needless burden laid on the Church without authority
- 71.15: of scripture,
- 71.20: of reason,
- 71.26: or of the fathers.
- 72.3: Teaching of Augustine.

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference Tcaching Augustine. . . ... (72.3).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 69:
1. ABC: nec deest before substancie; DE: sic deest; ib. C: poterint ;
E: potuerunt. 4. AB: hoc deest. 8, 9. ABC: aut quo ; C corr. : aliquo.
9. AB: materia; C corr. in marg. i3. ABCD : argumentum patet.
18. ABCE: aget; ib. ABCD : quo. 19. B: esse deest; ib. ABCD : philoso-
pliicum; D : philosophicwn veraciter. 20. D : insensibilem ; ib. B : exponere.
21 . D : predicamenta alia. 22. ABE : ad ista ; C corr. : in isto. 23. D : quam
tantum. 20. CD: transmutacionis ; ib. B: crearet in marg. ; E: careret;
A: careret extinct. crearet in marg. 29. ABCD : argumentum; ib. C:
posito in marg. alia manu. 3o. BCDE : alienatum ; A : ali<" alimentum.

p. 70:
1, 2. B: patct — materia deest. 2. D: contendunt. 5. D: suscitat;
C: susciperet; ib. AB : transsubstanciacionem. 6. D: corrumperetur.
7. ABCD: corrumpitur ; ib. C in in marg. alia mann. i3. D : difftnicione ;
C correxit: disposicione ; B: diffinicione vel disposicione ; A: difftnicione
alias disposicione. 14. ABCE : variari; ib. BCE: non deest.
14, i5. D: proporcionabiliter. 16. B: quodcunque; ib. ABCE: modi
decst. 18. ABCE: nam nulla. 23. E: introduceretur. 25. D: ex
tibi in tcxtu; ex tali in marg. 29. D: antique ; ib. CD: suscitatur.

p. 71:
1. D: hic materialem; E: hniusmodi deest. 5. E: fide ; ib. E: vel in
marg. alia raanu. 7. E: isto errori. 8, 9. ABC: argwnentum.
11. C: entitatis in marg. alia manu. 21. ADE: huius) ib. ABDE: acci-
dencia. 29. E: sufficiet ; ib. C: eis in marg. alia manu. 3i. C: est
in marg. alia manu.

p. 72:
5. AB: dictnm deest; C in marg. alia manu. 8. D: sed nunquam.
9. D: possunt; ib. AB : ista d tria = ista tria. 9. Cod.: non deest.
10. C: esse in marg. alia manu; E: possent. 11. Codd. : XIII. Correxi.
i3. ABC : modo deest ; ib. B : se iungit. 14. ABC : aut alibi. i5. D : alteri.
18. CD: animo; D corr. in marg. 20. A in textu : abeunte. 21. ABCE:
possim. Recte: Quare non possum. 23. D: concessit; ib. ABCD : alicui ;
aul deest. 24. C: fieri in marg. alia manu. 25. C: ipso in marg.
alia manu; ib. E: subiecto deest. 26. ABC: illud; ib. D: non esset
deest; Codd.: est. Correxi. 18. Codd.: ipso oportet; C correxit.
4. St. Augustini Opp. tom. I, pag. 404. 11. St. Augustini
Opp. tom. I, pag. 378. 21. Aug. 1. c. cap. XIII.

p. 73:
L ABCE: Item tercio. 4. AB : idem deest; ib. ABC : retraccione.
5. ABC: De Trinitate et IX; E: et VI Trinitate. 7. D: oportet.
S. D : esse illud. 9. B: tamen ; ib. C: foret in marg. alia manu; ib. D : alia.
i3. ABCE: perieret. 14. D: tamen tercio. 16. E: possit. 17. ABC :
et deest; C in marg. alia manu: et. 20. D: plurium. 22. E: suorum
deest: ib. B: ceperant. 24. ABE : maiorum; ib. C: stulticie in marg.
alia manu. 26. C: doctoris in marg. alia manu. 27. D: et vis.
2. Aug. L c. tom. II, pag. 682. 5. Cf. Augustini Opp.
tom. VIII, pag. 833 et seqq. 6. ib. tom. I, pag. 690, 691.
26. Scil. Thomae Aquinatis.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 69: vero sunt mortua animalia, ex quorum pellibus nostri muniantur pedes, nisi antiquipatres qui nos ad eternam patriam precesserunt. Qiiorum dum exempla conspicimus, nostri operis pedes munimus. Calceamenta | ergo inpedibus habere est mortuorum vitam conspicere et nostra vestigia a peccati vulnere custodire. Tenentes baculos in manibus. Qiiid lex per baculum nisi pastoralem custodiam designat? Et notandum quod prius precipimur renes accingere, postmodum baculos lotenere, quia illi debent curam pastoralem suscipere, quia iam sciunt in suo corpore fluxa luxurie edomare, ut cum aliis forcia predicant, ipsi desideriis mollibus et voluptatibus non succumbant. Bene autem subditur: Et comedetis festinanter. | Notate, fratres, notate quod dicitur festinantes. Mandata Dei, misteria Redemptoris, celestis patrie gaudia cum festinacione cognoscite et precepta vite cum festinacione implere curate. Quia enim adhuc hodie licet bene agere scimus: utrum cras liceat igno- | ramus. Eestinantes autem pascha comedite, id est, ad sollempnitatem patrie celestis anhelate. Nemo in huius vite itinere torpeat, ne in patria locum perdat. Nemo moras ad appetenda studia innectat sed cepta perficiat, ne minime liceat implere quod inchoat. Si ad | amorem Dei pigri non sumus, adiuvat ipse quem amamus. | quibus pellibus. | illi debent | sarcinam predicant ipsi desidiis. | ad hoc. | Det Christi.
p. 70: et contemptum. | et occupaciones. | carnis et. | quin per; | vel pecuniam. | Et talis | Jesn Clirisli | iudicio, non.
p. 71: Cum Marthe | ut spiritus salvus fiat: ymmo in libris illis quibus adversarii magnam auctoritatem tribuunt. Advertant | quod dicimus ubi scriptum est apostolum | Et quantum. | quod Deus; | Sed ex; | populos in suis. | esse innuere. 16. | Notando itaque. | quod — mendacia | ad versat.
p. 72: non dubito corpora omnia longitudine, latitudine et altitudine carere non posse, sed numquid potest cogitari ista tria non esse nisi in corporibus? Non intelligo, | quomodo alibi esse possint. | Esse aliquid in aliquo nos non fugit duobus modis dici. Uno modo localiter ut corpus seiungi atque alibi esse possit, ut hoc lignum in hoc loco et sol in oriente. Altero autem quo ita est aliquid | in subiecto, ut ab eo nequeat separari, ut in hoc ligno forma et species quam videmus, ut in sole lux, ut in igne calor et in anima disciplina et si qua sunt alia. Ista, | vetustissima nobis sunt et ab ineunte adolescencia studiosissime percepta et | cognita, quia non possum de hiis interrogatus, quin ea sine ulla deliberacione concedam. | Illud vero quod interrogasti, quis concesserit aut cui posse fieri, videatur ut id quod est in subiecto maneat ipso intereunte subiecto? Monstruosum enim et aio veritate alienissimum ut id quod non esset nisi in ipso esset, eciam cum ipsum non fuerit possit esse. | Thomam inprecatum cuidam a quo palma percussus ' esset atrocissime mortis supplicium, animam tamen eius commendat ut in futuro seculo ei parceretur: cuius a leone occisi a cetero corpore discerptam manum canis intulit mensis convivarum, in quibus | convivabatur Apostolus. Cui scripture, | licet nobis non credere; non enim est in katholico canone. | interpretatiun cuidam. | a toto corpore; | scripta sacra. | cum cognomine quaniitatis. | et sic
p. 73: Tolle ergo ipsa corpora qualitatibus, qualitates corporum nec erit ubi sint, et ideo necesse est ut non sint. | Hoc est. | Deus verax est, se ipsum negare non potest. | Scrmone LY. | quia Augustinus. | substancie — impossibilitate
```

---

## Chunk 03-f: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-03-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-03-f
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "73.19–77.28"
divisions: "cap. 3 (heading 'CAPITULUM TERTIUM.' at 53.0); part 6 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "938 words; 919 confirmed by the vote; 14 runs stood by rule; 5 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n144–n148 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 3, part 6: [TITLE]

## ¶1 · 73.19–75.4

> [p. 73] Quantum ad glosas et opiniones modernorum doctorum in ista materia, patet quod ut plurimum sunt frivole; ipsi enim vix corticem verborum sanctorum suorum priorum conceperant; et ideo deficiente intelligencia hii negant et imponunt erronee sanctis stulticiam et hii ad ostensionem maioris stulticie fingunt eis glosas nimis extraneas, ut patet de glosa Doctoris Communis ad dicta Augustini de potenciis anime, quomodo memoria, racio et voluntas non sunt essencia anime inseparabiles qualitates, Augustinus [p. 74] autem ponit in utroque oppositum. Sed movet me dictum illius magni doctoris et sciencioris modernis Hugonis, IIº De Sacramentis, Parte VIIIª in cuius IXº capitulo ita scribit: Per verba sanctificacionis vera panis et vini substancia in verum corpus Christi et sanguinem convertitur, sola specie panis et vini remanente et substancia in substanciam transeunte. Conversio autem ipsa non secundum unionem sed secundum transicionem credenda est: quoniam nequaquam essencia in augmentum essencie accidit ut per id quod accedit id ad quod accedit cum illo ad quod accedit unum fiat. Nec sic in pane corpus Christi consecrari dicimus, ut de pane corpus Christi esse accipiat, nec quasi novum corpus subito factum de mutata essencia, sed in ipsum corpus verum mutatam essenciam; nec ipsam substanciam panis et vini in nichilum redactam, quia desiit esse quod fuit, sed mutatam pocius, quia incepit esse aliud quod non fuit et ipsum quod cepit esse ex ea esse non accipiat, quia panis fuit, sed ipsa eius esse accepit quando desiit esse quod fuit. Hoc expressius distinximus propter eos qui ex sua racione fidei preiudicium faciunt et sensu suo incedentes asserere nituntur vel hoc esse solum quod cernitur vel tale esse quod creditur; hoc est, quia sola panis et vini species cernitur solam ibi esse panis et vini substanciam vel quia ibi substancia corporis et sanguinis esse [p. 75] creditur possibiliter ei inesse speciem et qualitatem panis et vini que cernitur quasi non possit species apparere cuius non assit substancia vel substancia latere cuius non appareat forma.

[ENGLISH]

## ¶2 · 75.5–75.26

> [p. 75] Ista verba doctoris incusserunt michi formidinem nec video quin doctor in illis intelligit quod fidelis suscitet intellectum ad credendum quod solum corpus Christi sit post consecracionem ibi principaliter pane et vino in principalitate illa corpori Christi cedentibus, unde propter amissionem illius principalitatis dicit nec panem nec vinum remanere sed in corpus Christi converti. Accidencia autem habent ibi principalem existenciam ad expergefaciendum sensus fidelium sine subiecto suo ibi principaliter existente; verumtamen ipsa informant panem et vinum, non autem corpus Christi vel sanguinem, sed illa informacio propter presencialitatem dignioris corporis est sopita, sicut Petro tenente in domo principalitatem dominii post successionem Christi, in eadem domo cui Petrus omnino succedit in servum nomen Petri tacetur et nomen Christi in hiis que sunt dignitatis vel principalitatis ibi erigitur. Sic est quodammodo de corpore Christi et pane qui post conversionem, licet remaneat secundum essenciam, tamen esse principalitatis ab eo tollitur, cum remanet secundarie serviens superiori corpori ut figura.

[ENGLISH]

## ¶3 · 75.27–76.5

> [p. 75] Et possunt dicta verba doctoris trahi ad istam sentenciam, et per hoc potest intelligi dicta conversio vel transsubstanciacio et ecclesia novella concordari cum ecclesia antiqua, et potest labor in ista equivocacione [p. 76] colorari ex modo loquendi quo servus recipiens dominum in domum suam inferiorat se quantum sufficit, dando sibi in domo totum nomen honoris vel reverencie ac si ipse foret in huiusmodi anullatus.

[ENGLISH]

## ¶4 · 76.6–76.18

> [p. 76] Et iterum, attribuimus in aliis terminacionem actus corpori principali, accessorio dimisso, ut dicimus nos emere vel vendere equum vel asinum et non materiam eius vel formam, sicut legiste dicunt se non excommunicare propter pecuniam sed propter inobedienciam consumatam; et cadit utrimque ex equivocacione illusio, potest tamen modus loquendi fundari ex illo Joh. IVº, 42: Mulieri dicebant quia iam non propter tuam loquelam credimus, ipsi enim audivimus et scimus quia hic est vere salvator mundi, ubi oportet intelligere negacionem super principalitatem muliebris evidencie; et tales sunt multi modi loquendi in scriptura.

[ENGLISH]

## ¶5 · 76.19–77.28

> [p. 76] Sic ergo possunt concordari dicta gravium personarum ecclesie quod est melius quam invenire sensum et verba ab antiquis sanctis extranea, et ex illis ut in materia calculatoria ex falso fundamento deducere conclusiones et sentencias mundo mirabiles; que de facto sunt deliramenta fidelibus onerosa: ut adversarii concludunt in casu eis possibili quod iste homo fuit temporaliter generatus univoce et non ab animali aliquo, licet parentes eius conversantes cum eo in fide ipsum instruxerint; qui licet a Deo perpetue dampnabuntur, non possunt tamen peccare vel puniri in corpore aut anima, sicut non possunt in altero horum pati, posito quod ex duobus spiritibus [p. 77] qui possunt esse anime humane et omnibus accidentibus absolutis corporeis (que sunt in Petro et Martha) optime complexionatis constituantur duo supposita subducta in eis omni materiali substancia et quod ista que sunt A et B peccent dampnabiliter, procreando Paulum compositum ex corpore et anima, de quo Paulo verificant consequenciam; nam sicut A et B mediantibus aliquibus suis accidentibus corporeis possunt operari eque efficaciter et satis univoce, ut patet de operibus nutritivis et sensitivis: ita videtur de accionibus generacionis, et per consequens sicut A et B habent potenciam gignendi et aliter operandi secundum quascunque qualitates quas habent, sic possunt esse parentes et coniuges hominem procreantes. Et patet cum casu prima pars conclusionis; et secunda pars probatur per hoc quod nec A nec B est substancia animata sensibilis quia non corpus, ymmo pari evidencia qua foret substancia foret tam quantitas quam qualitas; et patet tercia pars ex casu cum tam A quam B potest exercere omnes operaciones tam organicas quam non organicas. Et patet quomodo tam virtus quam vicium potest inesse illis spiritibus, et sic tam A quam B potest dampnari perpetuo, cum habet libertatem flexibilitatis arbitrii, sicut ponitur de inesse. Ultima vero particula videtur per hoc, quod nec A nec B potest esse animatum sive corporeum, quia tunc foret aliene nature omnino a natura cuius est materia.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 73.19: The comments and opinions of modern doctors are frivolous.
- 74.1: The words of Hugo give us pause, since he seems to say that after consecration the substance is of the Body.
- 75.5: Perhaps he only means that the Body is the object on which our attention should be fixed.
- 76.6: Examples of such use of language.
- 76.19: It is better to strain the later doctors into agreement with the early church than to accept absurdities: e. g. that human beings may live and act without substance.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 73: *doctorum* (print = bt) [SUB]
  - 74: *VIIIª* (print = bt) [SUB]
  - 74: *panis* (print = bt) [SUB]
  - 75: *fidelis suscitet intellectum ad credendum quod solum corpus* (print = bt) [SUB]
  - 76: *non* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 73:
L ABCE: Item tercio. 4. AB : idem deest; ib. ABC : retraccione.
5. ABC: De Trinitate et IX; E: et VI Trinitate. 7. D: oportet.
S. D : esse illud. 9. B: tamen ; ib. C: foret in marg. alia manu; ib. D : alia.
i3. ABCE: perieret. 14. D: tamen tercio. 16. E: possit. 17. ABC :
et deest; C in marg. alia manu: et. 20. D: plurium. 22. E: suorum
deest: ib. B: ceperant. 24. ABE : maiorum; ib. C: stulticie in marg.
alia manu. 26. C: doctoris in marg. alia manu. 27. D: et vis.
2. Aug. L c. tom. II, pag. 682. 5. Cf. Augustini Opp.
tom. VIII, pag. 833 et seqq. 6. ib. tom. I, pag. 690, 691.
26. Scil. Thomae Aquinatis.

p. 74:
2. ABE: scienciarum; C: scienciorum ; D : scienciore ; ib. ABC : modernus.
3. E : Hugo; ib. E : IIo deest. 4- D : illa scribit; ib. ABC : veri. 5, 6. D :
substancia — vini deest. 6. C: panis in marg. alia manu. 9. Codd. :
quam. Correxi. 9, 10. D : nequaquam esse. 10. ABDE: et augmentum ;
ib. Codd.: accedit. 10, n. C: ul — accedit in marg. alia manu. 11. AB:
et id ad; ib. D: cum illud. 11, 12. adquem. 12. ABDE: vinum ftat ;
ib. B : corporis. i3. C: consecrare. i5. E: mutata subslancia sive essencia.
20. ABCD : cuius esse. 21. C: quavdo in textu : in marg. alia manu:
ante. 22. ABCE: distinccius ; C iu marg. alia manu: distinguimus.
20. ABCD : quod sola. 26. Codd.: esse deest. 27. esse; D: Christi.
3. Hugo, De Sacramentis, lib. II, pars VIII, cap. IX (ed. Mo-
guntina 16 17), pag. 463. 11, 12. Recte: ut per id quod accedit,
id ad quod accedit maius fiat.

p. 75:
3. ABCE: cuiusnam; ib. ABDE: substancialiter. Correxi. 3, 4. C:
substancia lateris; lateris in marg. alia manu. 10. Codd.: credentibus.
11. ABCD: et vinum. 1 \ E: sensum. 17. AB: propter deest.
iS. AB: tenente in dotno deest; C in marg. alia manu addit; E: in domo
deest. 19. AB: dominium; C: domus. 21. D: nomen deest; ib. ABCE :
qui sunt; C correxit: que. 22. B: ubi erigitur. 23. C: in marg.
aliamanu: consecracionem. 25. D: secundario. 25, 26. B: servientes.
28. E: novella dicta; intelligi deest. 3o. C in marg. alia manu: labor.

p. 76:
1, 2. A: recipientes. 2. ABCE: inferio\at. 3. C: sufficit in marg.
alia manu. 4. D: honoris et; ib. AB: ipse deest; C in marg. alia manu.
9. E: vel formam eius. 9—10. C: sicut — pccuniam in marg. alia manu.
H. ABDE: utrum. 11, 12. E: sub equivocacione. i3. D: in illo.
14. D: credemus. i5. ABC: audimus. 17. B: mulieris. 20. E: eccle-
sie deest. 21. AB : quod illis ex deest; ib. CE : ex deest. 22. B: ut
deest; ib. D: calculativa. 28. CDE : instruxerunt. 3o. B: vel anima.

p. 77:
I. D: in omnibns. 3. D : secunda. 4. AB: subdicta. 7. 8. H : nam
sic A. 8. D: alibus. 11, 12. B: sic A. 12. ABDE: potenciam deest;
C in marg. addit. i3, 14. D: sicut possunt. 16. C: conclusionis in
marg. alia manu. 19. E: Et hoc patet. 20. E: quod tam. 27. E: sive
deest. 28. C: est modo. Ex. 3l E: fit.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 73: Tolle ergo ipsa corpora qualitatibus, qualitates corporum nec erit ubi sint, et ideo necesse est ut non sint. | Hoc est. | Deus verax est, se ipsum negare non potest. | Scrmone LY. | quia Augustinus. | substancie — impossibilitate
p. 74: Per verba sanctificacionis vera | p an } s et vm i S ubstancia in verum corpus Christi etb sanguinem convertitur, sola specie panis et vini remanente et substancia in substanciam transeunte. Conversio autem ipsa non secundum unionem sed secundum transicionem credenda est: quoniam nequaquam essencia in augmentum essencie accidit ut per | id quod accedit id ad quod accedit cum illo ad quod accedit unum fiat. Nec sic in pane corpus Christi consecrari dicimus, ut de pane corpus Christi csse accipiat, nec quasi novum corpus subito factum de mutata essencia, sed in ipsum corpus verum | mutatam essenciam; nec ipsam substanciam panis et vini in nichilum redactam, quia desiit esse quod fuit, sed mutatam pocius, quia incepit esse aliud quod non fuit et ipsum quod cepit esse ex ea esse non accipiat, quia panis fuit, sed ipsa eius esse ac- | cepit quando desiit esse quod fuit. Hoc expressius distinximus propter eos qui ex sua racione fidei preiudicium faciunt et sensu suo incedentes asscrere nituntur vel hoc esse solum quod cernitur vel tale esse quod creditur; hoc est, quia sola panis et vini | species cernitur solam ibi esse panis et vini substanciam vel quia ibi substancia corporis et sanguinis esse | Panem nostrum supersubstancialem da nobis hodie, | Solvite templum hoc et in tribus diebus excitabo illud. Hic | possum destruere templum Dei et post triduum reedificare | ut palet in illo. | super subiectalem. | Johannis III. | cum vino.
p. 75: creditur possibiliter ei inesse speciem et quahtatem panis et vini que cernitur quasi non possit species apparere cuius non assit substancia vel substancia latere cuius non appareat forma. | si Deus voluerit. | non potuit sed non decuit y hoc est, potuit, si voluerit; | ad vcrsarium | ad hoc. | quando dicunt; | cum dicit. | non potuit,
p. 76: Mulieri dicebant quia iam ?ion propter tuam loquelam credimus, ipsi enim audivimus et scimus quia hic est vere salvator mundi, | Mandatum novum do vobis: ut diligatis invicem, sicut dilexi vos. | alia enim. | ad alia. | secundum quod sit; | ista modum. | et illa. | in primo.
p. 77: diligitis me, mandata mea servate. | Pacem relinquo vobis, pacem meam do vabis\ | quantumcunque homo mundus fuerit in baptismo, verumtamen cum in rebus humanis postea vivitur et terra pede fedata calcatur: Ipsi, | humani affectus sine quibus in hac mortalitate non vivitur quasi pedes sunt quibus lohumanis rebus afficimur, et sic afficimur quod si dixerimus quia peccatum non habemus nos ipsos seducimus et veritas in nobis non est. Ideo debemus lavare pedes mentis cotidie, cum oramus: Dimitte nobis debita nostra. | ut paulo.
```
