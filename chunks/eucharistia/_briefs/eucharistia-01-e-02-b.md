# Translation brief: eucharistia 01-e–02-b

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/eucharistia/wyc-eucharistia-01-e.md chunks/eucharistia/wyc-eucharistia-02-a.md chunks/eucharistia/wyc-eucharistia-02-b.md` once and fix what it reports.
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

## Glossary (the 386 rows these chunks use; the full file is GLOSSARY.md)

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
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). Where privileges or law, not prayers, do the aiding: "to aid" (*Eccl.* 241.1; cf. *suffragium* "aid"), 2026-10-02. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| sacramentum (the eucharist); sacramentum altaris | sacrament; the sacrament of the altar | The plain sense, against the Augustinian row (*Incarn.*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.3, 3.30). |
| hostia; hostia consecrata | host; consecrated host | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.11, 1.22). |
| panis / vinum | bread / wine | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.8). |
| calix | chalice | The Douay word (1 Cor. 10:16). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.3). |
| corpus Christi / corpus Domini | the body of Christ / the body of the Lord | Kept apart as the Latin alternates them. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.6, 1.10). |
| novella ecclesia / antiqua ecclesia | the newer church / the ancient church | The pair of 3.3; cf. *novelli*. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 3.3). |
| cultores accidencium / signorum | worshippers of accidents / of signs | Wyclif's name for the defenders of the accident without a subject. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 6.15, prol-c 10.2). |
| missantes | mass-priests | Priests hired to say masses; pejorative. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 15.25). |
| species (of bread and wine) | species | The sacramental species; kept as the term, not "appearance". Distinct from the logical *species*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 13.15; 23.8). |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). Third referent, the logician's arrangement of terms in a proposition (*Incarn.* 49.10): "ordering", with a **C** note; ruled 2026-10-22 (coordinator, delegated). |
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| simonia | simony | Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| thema | theme | The scripture text of a sermon. Ruled 2026-09-28 (2 sites). |
| protestacio; protestari | declaration; to declare solemnly | ⭐ The submission formula ("if anyone can teach me this is contrary to scripture or reason, I will humbly retract"). Penn and Lahey both inverted it (T. pp. 369, 378). Render it as a retraction offer, never as defiance. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| leges ecclesie | the laws of the church | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.20, 1.23). |
| decretum; decreta | decree; the decrees | Gratian (*in decretis*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.14, 3.24). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| credulitas | credence | With *credere*, believe (*Dial.* 23.17–24.4). Ruled 2026-09-28. |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| sumitur pro | is taken for | Supposition language. Pilot. |
| simpliciter / secundum quid | **without qualification / in a certain respect** | ⛔ Always opposable. Never "simply", "wholly", "directly", "naturally" etc. (T. p. 364). |
| necessitas supposicionis / ex supposicione | necessity of supposition / necessity on supposition | Conditional necessity. Pilot (*Eccl.* 3.21); *ex supposicione* ruled 2026-10-02 (34.12, 38.22). |
| de congruo / de condigno | by congruity / by condignity | Pilot. |
| contingens ad utrumlibet | contingent either way | T. p. 364. |
| consequencia | inference | ⛔ Not "consequence" (T. p. 361 n. 13). |
| consequens / antecedens | consequent / antecedent | |
| sequitur | it follows | Introduces a stated inference, often quoted in the next words. Pilot (*Eccl.* 2.21). Not tagged where it is not an inference ("the third law follows", *Dial.* ch. 5). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| glosare | to gloss | Interpret so as to remove the difficulty (T. p. 366). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| glosa | gloss | The noun beside *glosare*. Ruled 2026-10-02 (52.10). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| suffragium (*legis, privilegii*) | aid | As *suffragium* "aid" (01-a) and *suffragium sensus*. Ruled 2026-10-02 (149.29, 152.8). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| dimittere / dimissio (*naturam*) | lay aside / the laying-aside | Letting go the assumed nature, so the union would be dissolved. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 2.23). |
| ydemptitas specifica | identity of species | That Christ and other men are of one species. Not "specific identity" (reads as "particular"). Ruled 2026-10-22 (Wilson; *Incarn.* prol, 8). |
| Verbum | the Word | Pronoun **"he"** (as Douay–Rheims John 1:3, "by him"), never "it", though the Latin is neuter; so also *Sapiencia* where Wisdom is the Word in person (*Incarn.* 7, coordinator). Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.3–4). |
| homo assumptus | the assumed man | A term of art (the Lombard's first opinion, *Sent.* III d. 6); keep "assumed" before "man", never "the man assumed". With the agent expressed (*homo assumptus a Verbo*) "the man assumed by the Word", which cannot be misread (coordinator, 2026-10-22). Ruled 2026-10-22 (Wilson; *Incarn.* 5.15). |
| secundum quod (reduplicative) | insofar as | ⛔ Never "in that" (heard as "because", which inverts the logic). Ruled 2026-10-22 (Wilson; *Incarn.* 5.29–6.24). |
| secundum deitatem / secundum humanitatem | as to the Godhead / as to the humanity | The rule of reduplication; keep it in Wyclif's place in the sentence. ⛔ Never supply "as God / as man" where the Latin has bare apposition (*ipse Deus*) or bare predication. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| natura | nature | Ruled 2026-10-22 (Wilson; *Incarn.* 3.4). |
| creatura / creator / creatus | creature / creator / created | ⛔ Never "creation" for the created thing. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| posicio / proposicio / predicacio | position / proposition / predication | Kept apart: the apparatus shows the three trading places (*Incarn.* 4.15). Ruled 2026-10-22 (Wilson). |
| sacramentum (of the incarnation, of creation) | sacrament | The Augustinian sense, "mystery" (1 Tim. 3:16): G note at the first occurrence in the chunk. Kept apart from *misterium*. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.8). |
| sancti | the saints | The fathers. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.15). |
| probabiles doctores | reputable doctors | *Probabilis*: worthy of credence (cf. *probabiliter*). Ruled 2026-10-22 (Wilson; *Incarn.* 7.1) as "approved doctors"; changed the same day (coordinator) to free "approved" for *approbati*. |
| approbati doctores | approved doctors | Kept apart from *probabiles doctores*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 13.3). |
| novelli | the newer [doctors] | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 13.7). |
| determinacio | determination | A qualifying addition to a predicate (*cum determinacione*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 14.11). |
| de vi vocis / de vi sermonis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| protervus | obstinate | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21). |
| determinaciones ecclesie | the church's determinations | Rulings of the church, not the logician's *determinacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 24). |
| nedum | not only | "Let alone" where the sense is a fortiori. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21, 24). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| gracia unionis | the grace of union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| minoracio | lowering | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| in quantum (reduplicative) | insofar as | As *secundum quod*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37.9). |
| pars qualitativa | qualitative part | Body or soul as the parts that make up a man by kind; set against *pars quantitativa*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 43.5). |
| diccio (logical) | word | A single term in a proposition. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 43.3). |
| pars discretiva | discrete part | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 46.9). |
| dos immortalitatis | dower of immortality | Of the glorified body. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 46.24). |
| in effectu | in actual fact | As against in potency or in name; ⛔ not "in effect" (modern "virtually"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 47.10). |
| communicacio ydiomatum | communication of idioms | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.1). |
| predicacio actualis / aptitudinalis / habitudinalis / mixtim | actual / aptitudinal / habitudinal / mixed predication | *Habitudinalis* is its own term (the four MSS at 49.6), not under *habitudo*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.5–16). |
| Doctor Subtilis | the Subtle Doctor | Scotus. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.24). |
| convertibilis / converti | convertible / be convertible | Of terms. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 52.29). |
| forma totalitatis | form of totality | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 50.7). |
| quantus | quantified | The adjective beside *quantitas*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.22). |
| construccio synecdochica | synecdochic construction | Beside *synecdochica locucio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.5). |
| dampnificare / dampnificacio | damage / damaging | Kept apart from *dampnum* "loss" and *dampnari* "be damned"; the argument of 65–68 turns on it. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 65). |
| peiorare / peioracio | make worse / worsening | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 65–68). |
| per se / per accidens | of itself / by accident | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a (sufficienti) divisione | the topic from sufficient likeness / from (sufficient) division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| medium (logical) | middle term | Of a syllogism; elsewhere "means" by context. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| ydemptitas ypostatica | hypostatic identity | Beside *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 84.20). |
| eiusdem / consimilis / alterius racionis | of the same / like / another kind | The species-sense of *racio*; *racio speciei* "the account of the species" (Aristotle's *logos*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.4, 87.17). |
| accidentatus | subject to accidents | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.4). |
| in recto / in obliquo | in the direct case / in an oblique case | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.25). |
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
| predicacio secundum essenciam / formalis | predication by essence / formal predication | Wyclif's modes of predication (cf. *predicacio secundum causam*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 115–116). |
| forma substancialis | substantial form | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| exclusiva | the exclusive [proposition] | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 116–117). |
| concepcio (figure) | conception | The grammatical figure. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| accidens | accident | The category; *accidit* "befalls". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| figura / figuratum | figure / thing figured | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 121.23). |
| conversio (of a proposition) | conversion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.30). |
| racio (individual, personal) | account | *Racio individui / persone* "the account of an individual / a person", as *racio speciei*; not "aspect" (the row against *substancia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 8, 129–132). |
| exemplaria / exemplata | exemplars / things exemplified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.6). |
| res secunde intencionis | things of second intention | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.25). |
| materia proxima / remota | proximate / remote matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137.1). |
| colorate | with colour enough | With a plausible ground (cf. *color*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 134.26). |
| ydemptificare / ydemptificacio | identify / identification | Make the same (*idem*); the hypostatic union as identification, not conversion or generation. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 142.19, 147.22). |
| res communis / res communes | the common thing / common things | The realist universal the *moderni* do not conceive (first root of their error). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 144.27). |
| distinccio racionis | distinction of reason | Beside *differencia formalis*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 145.23). |
| conversio naturarum / confusio naturarum | conversion of the natures / confusion of the natures | Kept apart from *conversio* of a proposition. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 143.9). |
| transsumpcio | transumption | Beside *transsumptive*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 153.28). |
| aliud / alius | another thing / another one | The neuter against the masculine (*aliud et aliud, non alius et alius*): natures against persons. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 160.1–2). |
| in quid (predicari in quid) | in quid | Kept in Latin (predication of what a thing is, as against *in quale*), glossed at first use in a chunk. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 162.22). |
| dependencia actualis / potencialis / obediencialis | actual dependence / potential dependence / obediential dependence | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 161.23–162.4). |
| substancia prima / substancia secunda | first substance / second substance | Aristotle, *Cat.* 5. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.25). |
| a simili | by likeness | Bare, as an argument form; beside *locus a simili* "the topic from likeness". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.16). |
| racio substancialis | substantial account | As *racio individui* "account". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.21). |
| doctores signorum | the doctors of signs | The logicians who reason from terms, not things. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.26). |
| sensibilis (in the definition of animal) | sentient | *Substancia animata sensibilis*: able to sense. Elsewhere the §D row "perceptible" holds; G note at first use. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 177). |
| ydemptitas numeralis | numerical identity | Beside *ydemptitas specifica* "identity of species". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 172). |
| accidens absolutum | absolute accident | Quantity and quality, against relative accidents. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 176). |
| beatificabilitas | beatifiability | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 181). |
| transsubstanciacio | transubstantiation | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.10). |
| multiplicative | multiplicatively | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 193.20). |
| remitti / intendi (of a quality, merit) | be remitted / be intensified | The intension and remission of forms; not *remissio* of sin. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 197.1–7). |
| in divinis | among the divine [persons] | Keeps "Godhead" for *deitas*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 196.18). |
| partes proporcionales | proportional parts | The halving division of a continuum. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 194.24). |
| multiplicacio dimensionalis | dimensional multiplication | One body in several places by its dimensions. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.6). |
| a maiori vel pari | from the greater or from the equal | Arguments *a maiori*; cf. *locus a maiori*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 209.5). |
| sensibile commune | common sensible | Aristotle's common sensibles (number, motion, figure); the term of art, against the §D row "perceptible". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 209.23). |
| communioritas | greater commonness | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 210.15). |
| multiplicacio concomitancie | multiplication of concomitance | Cf. *gracia concomitancie*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 213.21). |
| assertibile | assertible | The thing a proposition asserts. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 215). |
| superioritas / inferioritas terminorum | superiority / inferiority of terms | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 215). |
| homo communis | the common man | The universal man, with *res communis*; not "the ordinary man". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 218.3). |
| bonum de genere | good in its kind | Moral goodness by the kind of act. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 228.16). |
| signum reduplicatum | the reduplicated sign | The reduplicative word (*secundum quod*, *in quantum*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 230.23). |
| lex proximitatis | the law of neighbourhood | The duty to love one's neighbour (*proximus*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 101.29). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |
| sacramentaliter | sacramentally | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| realiter | really | A mode adverb: one word each, never two merged, kept where Wyclif puts it. ⛔ Never "actually". Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| vere | truly | A mode adverb: one word each, never two merged, kept where Wyclif puts it. ⛔ Never "really" (that is *realiter*). Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| spiritualiter | spiritually | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| figurative | figuratively | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| tropice | tropically | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Kept apart from *figurative*. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| ydemptice | identically | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
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
| esus / manducacio (corporalis / spiritualis) | (bodily / spiritual) eating | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.5). |
| confeccio | consecration (of the eucharist) | The noun of *conficere*, which already shares "consecrate" with *consecrare*. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 4.4). |
| locucio tropica | tropical speech | With *predicacio tropica* "tropical predication". Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 4.26). |
| Doctor Communis | the Common Doctor | Thomas; with *Doctor Subtilis*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 8.16). |
| multitudo (of one body) | multitude | Of one body's being many (ch. 8); the plain "multitude" of persons needs no row. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 8.4). |
| sensus communis | the common sense | The inner faculty; kept apart from *sensibile commune* "common sensible". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 18.31). |
| laudative; effective | by way of praise; by way of effect | Of blessing God vs. blessing a thing. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 16.24). |
| sensacio | sensation | One of the five. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 20.18). |
| figurare | figure | Both senses: to prefigure (the lamb figured Christ) and to shape (*figurare Deum nostrum*), which Wyclif plays on; one English word keeps the pun. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-c 10; 21.29). |
| conus (of the visual cone) | apex | The point of the visual triangle in the eye. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 20.21). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| insensibilis | imperceptible; of a thing that cannot feel, without sensation | Two senses by referent: what cannot be perceived / what cannot perceive (*lapis insensibilis*, *Dial.* 56.3). Kept visibly paired with *sensibilis*. Ruled 2026-09-28 (3 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
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
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| brocardicum / brogardicum | brocard | The schoolmen's stock maxim. Ruled 2026-10-02 (*Eccl.* 16, 360.9). |
| calumpnia (ponere / capere) | challenge (to lay a challenge against / to be open to challenge) | The disputant's formal objection to a premiss. Ruled 2026-10-02 (*Eccl.* 16, 363.18, 363.24, 367.11). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| quadriga diaboli | the devil's four-horse chariot | Ruled 2026-10-02 (*Eccl.* 18, 427.12). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| continuacio (of bodies, the act) / discontinuacio; continuare / discontinuare | continuation / discontinuation; make continuous / make discontinuous | The making of several bodies into one continuum (*Incarn.* ch. 12), G note at first use: not "carrying on". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.30, 211.12). |
| precaria | precarial grant | Wyclif defines it (*Eccl.* 453.21). Ruled 2026-10-02 (*Eccl.* 19). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| dampnacio | CONTEXTUAL: damnation / condemnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). Of a judgement passed on a teaching (*dampnacio istius sentencie tamquam heretice*, *Pot. pape* 84.10) "condemnation"; ruled 2026-10-07. |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| premium accidentale | accidental reward | Ruled 2026-10-02 (*Eccl.* 23, 565.6). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| remissio; remittere | remission; to remit | Headword row (cf. *condonacio* "pardon", *venia* "forgiveness"). Ruled 2026-10-02 (*Eccl.* 23). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). Beside *consecrare* (*consecrat et conficit*) "confect", so the pair stays two: PROVISIONAL 2026-11-07 (coordinator; *Euch.* 16.10), Wilson to confirm. |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| regulariter | as a rule | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 165.2). |
| quaternarius / denarius / quadragenarius | the four / the ten / the forty | Number exegesis (the 153 fishes, ch. 7). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 154–155). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| malum culpe / pene | the evil of fault / of penalty | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.19). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| eleccio passiva / activa | passive / active election | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 254.31). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| papa cesareus | caesarean pope | The pope as endowed temporal lord (chs. 10–12). Ruled 2026-10-08 (coordinator, delegated). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| correptibilis | open to reproof | Beside *corripere* "reprove". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 301.3). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| calumpniator | challenger | Under *calumpnia* "challenge". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 323.10). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| remisse (of assent) | with slackened [assent] | Opposed to full assent in the degrees of belief. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 328.18). |
| potissimus; pocior (Antichristus) | foremost; greater | Superlative and comparative kept visible as a pair. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.28, 331.12). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| episcopi cesarei | caesarean bishops | Extends *prelatus / sacerdos cesarius*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 331.24). |
| evangelizans | preacher of the gospel | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-g). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |
| coloracior | more colourable | Comparative, with the *color* / *colorabilis* rows. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 384.15). |
| diccio procuratoria | proctorial pronouncement | C note gives *dicio* "authority" as the alternative. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 386). |
| ars cesarea | the caesarean art | After *papa cesareus*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |
| sentire (the sacrament, the body) | perceive | "sense". As *sensibilis* "perceptible". Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.10, 1.17). |
| recitare | recite | To report, rehearse. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.4, 3.10, 4.18). |
| narrare | relate | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.9). |

---

## Chunk 01-e: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-01-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-01-e
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "25.19–29.24"
divisions: "cap. 1 (heading 'CAPITULUM PRIMUM.' at 11.0); part 5 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "890 words; 879 confirmed by the vote; 10 runs stood by rule; 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n96–n100 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 1, part 5: [TITLE]

## ¶1 · 25.19–27.19

> [p. 25] Et per hoc potest glosari decretum sequens: Ego Beringarius, ubi iste diaconus anathematizavit heresim qua prius fuerat irretitus; et facit protestacionem sue fidei sub hiis verbis: Consencio autem sancte Romane ecclesie et apostolice sedi, et ore et corde profiteor de sacramentis dominice mense eandem fidem me tenere quam dominus et venerabilis papa Nicholaus et hec sancta sinodus auctoritate evangelica et apostolica tenendam tradidit michique firmavit, scilicet panem et vinum que in altari ponuntur post consecracionem non solum sacramentum sed eciam verum corpus et sanguinem domini nostri Jesu Christi [p. 26] esse sensualiter, non solum sacramentaliter sed in veritate manibus sacerdotum tractari et frangi et fidelium dentibus atteri, iurans per sanctam et omousion Trinitatem et per hec sacrosancta Christi evangelia. Eos qui contra hanc fidem venerint cum dogmatibus et consecutoribus suis eterno anathemate dignos esse pronuncio. Ista tam sollempnis confessio non potest intelligi quod panis et vinum sit formaliter vel essencialiter corpus Christi et sanguis, sed figurative vel tropice, modo quo loquitur Apostolus I. Cor. Xº, 4: Bibebant autem de spirituali consequente eos petra, petra autem erat Christus. Unde glosa ordinaria intelligit per panem et vinum speciem panis et vini, modo quo loquitur perante eadem distinccio sub auctoritate Gregorii: Species et similitudo earum rerum vocabula sunt que ante fuerant, scilicet panis et vini; unde in fine cuiusdam misse oratur et dicitur: Perficiant in nobis, quesumus, Domine tua sacramenta que continent, ut que nunc sub specie panis et vini gerimus rerum veritate capiamus. Quotlibet sunt dicta sanctorum atque ecclesie que docent quod illa sacramenta sensibilia non sunt corpus Christi et sanguis sed eorum figura; et forte in isto multi sunt christiani nomine in fidelitate paganis peiores. Nam minus malum foret quod homo illud quod primo videt mane per totum residuum diei honoret ut Deum quam quod regulariter illud accidens quod videt in missa inter manus sacerdotis in hostia consecrata sit [p. 27] realiter Deus suus; et per hec est medium ad intelligendum decreta similia, ut distinccione XCVª, Ecce ego dico sub auctoritate Jeronimi sic habetur: Quid maius est Christo aut quid poterit corpori et sanguini eius anteponi? Si presbiter Christum consecrat, cum in altari sacramenta benedicat, benedicere populo non debet qui Christum consecrare non metuit? Videtur autem sanctum intelligere figurative per Christum hostiam consecratam, ita quod eadem sit consecracio qua consecrat hostiam et qua consecrare dicitur corpus Christi; hostiam tamen facit esse sacram saltem occasionaliter, dum rite facit ministerium sacerdotis, et Deus appropriate perficit quod suum est supernaturaliter alterando; quod si equivocetur in consecracione, vocando eam ostensionem rei sacre, tunc sicut laycus potest benedicere Trinitati, sic eciam consecrare, sicut laycus facit quod corpus Christi sit sacrum in isto loco vel sub isto sacramento et tamen non propterea consecrat corpus Christi.

[ENGLISH]

## ¶2 · 27.20–27.28

> [p. 27] Est ergo vera intencio sancti doctoris quod predicare, conficere et orare sunt pociora quam benedicere populo, ecclesie vel alii ornamento; ideo sicut est periculosum tam episcopo quam layco inprudenter suspendere maiorem benediccionem in presbitero sic et minorem, per quam sine simonia populus possit melius suffragari et presbiter per laxacionem potencie promereri; ideo prelatus timeret sibi in suspensionibus et laxacionibus de iniuria undequaque.

[ENGLISH]

## ¶3 · 27.29–28.6

> [p. 27] Sed arguitur quod sacerdos potest consecrare corpus Christi, quia potest benedicere deitati, potest [p. 28] ymmolare Filium Deo Patri et potest sanctificare Deum in corde suo (ut dicitur prima Petri IIIº, 15). Quodlibet autem istorum est plus quam consecrare corpus Christi; si ergo sacerdos habet potestatem in maius, habet potestatem et in minus, sicut dicit sanctus doctor linguarum peritissimus.

[ENGLISH]

## ¶4 · 28.7–28.17

> [p. 28] Hic dicitur quod benedicere potest homo tripliciter: scilicet laudative, inprecative et effective. Laudative omnis creatura benedicit Dominum, ut patet dictum in cathalogo sanctorum. Inprecative unus orans pro alio misero, ut Christus Deus noster benedicat; effective... Talem autem equivocacionem non vidi in consecrare, cum secundum grammaticos sit dare Deo vel simul sacrare; nam in veteri testamento dederunt Deo bestias et oblaciones que dicebantur Domino postea consecrate; sed quomodo consecramus corpus Christi vel sanguinem, cum sacrare sit sacrum facere?

[ENGLISH]

## ¶5 · 28.18–28.21

> [p. 28] Quantum ad secundum, dicitur quod ymmolatur sumitur equivoce pro sacrificare corporaliter et pro meritoria accione, ut verbum Dei pro aliquo interpellet; et sic non sumitur sacrare activum.

[ENGLISH]

## ¶6 · 28.22–29.9

> [p. 28] Quantum ad tercium, dicitur quod sanctificare est iterum equivocum ad facere sanctum et ad sancte colendum, ut Deus sanctificat se in homine, quando facit se sancte coli per eum; quod homo potest facere sed non corpus Domini consecrare. Nec movet sentencia beati Jeronimi ut sic equivocetur in consecrare, cum ipse videtur loqui de consecracione in signo que terminatur ad sacramentum et non ad [p. 29] Dominum, nisi dicatur quod sacerdos facit Dominum quia in signo. Equivocaciones autem que excludunt contradiccionem oportet loquentes in ista materia diligenter attendere, quia sicut conceditur quod sacerdos conficit corpus Christi, sic concederetur quod ista hostia sit corpus Christi quam loycam propter periculum est bonum suspendere et equivocacionem detegere. Et patet quod hoc sacramentum est forma panis et vini et non Christus vel pars eius.

[ENGLISH]

## ¶7 · 29.10–29.24

> [p. 29] Et quamvis omnes christiani teneantur cognoscere istam sentenciam, specialiter tamen theologi et professores legum ecclesie; leges enim ipsorum quas oportet eos defendere sunt plene ista sentencia, ut specialiter patet IIIº Decretalium, De Celebracione Missarum, Cum Marthe. Leges, inquam, iste vel sunt abrogande tanquam heretice vel defendende et docende tanquam katholice, et eo diligencius quo supra alias leges sunt de pane celesti lucrando necessarie; ideo nota infidelitatis est dicere quod ille sunt tacende et alie leges licium declarande. Dicunt enim quod sacramentum tantum et non pars Christi est hostia consecrata sed Christus insensibiliter absconsus est sub illa.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 27.1: Jerome on blessing and consecration.
- 28.7: Different kinds of blessing.
- 28.12: (We cannot not consecrate Christ's body, since that is already holy).
- 28.19: Double sense of immolate,
- 28.23: of sanctity.
- 29.10: The host is a sacrament under which Christ is insensibly hidden.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 28: *Christus* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 25:
1. E: modi deest: ib. AB : calice. 3. C: m Domini. 12. C: et
tandem. i3. complexione; AB : gxico ; C : correxit. in marg. alia manu
complexione ; E: complexionem. i5. ABE : inquientibus. 17. Recte:
Fitaue sanguis Christi merum, etsi sensus deficit. 20. D: Biringarius :
ib. CD: anathematisat. 23. ABC : sedi deest. 27. ABDE: tenenda :
17. Daniel, Thesaur. hymnol. L c I, 245. 19. Decreti
Tertia Pars, dist. II, cap. XLII.

p. 26:
1. C: ct sensnaliter. 3. 1) : atteriri ; Codd.: monstrans. Correxi.
4. AB: omousicii; C: correxit : omousion; E: omdsion. 6. suis; E: eis.
II. ABE: / deest. 12. AB : eas. 14. D : et speciem vini; ib. E: per deest;
ib. CE: distinccione. 16. D: species panis. 17. C in marg. alia manu:
eiusdem wwse. 19. E: nunc invicem; ib. AB: sub in marg. alia manu;
in textu seT. 20. E: et vini deest. 23. C: in islo in marg. alia manu.
24. D: pociores. 26. mane ; D: in die. 27. C: quod deest.
12. Cf. Glossam ord. ad vocem Panem, id est, specie panis
et vini esse sacramentum tantum. i5. Decreti Tertia Pars,
dist. II, cap. XXXIV. 17. Post common of the Mass Sabbato
Quatuor Temporum mensis Septembris.

p. 27:
1. C: per idem per hec. 2. E : ut dictum est; ib. ABCE: XXXIII;
D: XCIII; AB: distinccione cst ; C: distinccione etc. 3. C: Jeronymi
in marg. alia manu. 7. ABCE: que Christum; ib. codd. : promeruit.
11. D: esse sacramenta. 14. C: equi in marg. alia manu. 18, 19. C: et
tamen — Christi deest. 20. E : sancti deest. 24, 25. AC : sicut et.
25 AB: sine summo ; C correxit: simonia; DE: sine synonimo. 28. C: in-
iuria in marg. alia manu. ?o. E: divinitati.
2. Decreti Prima Pars, dist. XCY, cap. VL

p. 28:
ib. ABDE: Imprecacione. II. noster; D: nunc. 12. effective ; h.c ah-
quot verba excidisse apparet; tb. C: talem deest; A: tamen correx.t in
talem. i5. C: Deo in marg. al. man.; ib. C: quas dtcebantur.
16. ABC: consecrare; ib. E: lamen quomodo. 17. DJ£: sacramus.
,9. AB : sacrificatis. 22. ABCE : sacrijicare est. 24. D : sanctificatur.
26. C: corpus Christi. 27. A : beati in marg. ; ib. D: equivocetur tam.
2. I. Pctri III, 9, i5. 5. Vidc supra pag. 27, L 2.
27. In cpistola ad Hedibiam Opp., tom. II, 824.

p. 29:
5. D: concederet. 6. ABCE: ista deest; ib. C: Chrisii alia manti.
7. C: suspendere alia manu. 9. est; B : et. i3. ABC: pleni; ih. D:
ista simul. i3, 14. E: et specialiter. i5. B: ut sunt. 16. D : ab-
negande. 19. B: ideo non ; ih. B: iste. 21. C: non al. manu.
22. D: invisibililer absconditus ; E: est absconsus. 23. B: illa elc.
24. ABCE: cap. secundum deest. 28. E: beati.
i5. Decr. Greg. IX, lib. III, tit. XLI, cap. VI. 28. Gf. St.
Thomae Summa, III, quaest. LXXVf. Super Quart. Sententiarum,
dist. X, quaest. I, art. II.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 25: Qui manducant, | quod videtur panis est, et calix quod oculi renunciant, quod autem fides postulat instruenda, pdnis est corpus Christi et calix sanguis. | Corpus Christi quod sumitur de altari figura est, dum panis et vini natura extra videtur: veritas autem, dum corpus et sanguis Christi in veritate interius creditur. | panem et vinum que in altari | ponuntur remanere post consecracionem tam sacra- | mentum quam carnem Christi et sanguinem, | Ego Berengarius. | est sanguis. | sensus latencia. | cognoscere quod; | non communicancia. | et sacramentaliter;
p. 26: Qiio mihi multitudinem victimarum vestrarum? Plenus sum. | Cum extenderitis manus vestras, avertam oculos meos a vobis, et cum multiplicaveritis, oracionem non exaudiam: | Hoc est corpus | meum vel sanguis. | Fugite ab ydolorum cultura. | Calix benediccionis cui benedicimus nonne communicacio sanguinis Christi est? et panis quem frangimus | nonneparticipacio corporis Domini est? quoniam unus panis et unum corpus multi sumus; | Sed ex; | ita demonstrando. | post consecracionem benediccionem; | panem illum. | substanciam vel naturam. | in alia. | partem eorpore. | mille millia. | Argumentum patet. | minor probatur | fit cum paribus. | poncre mensuram. | argumentum palet.
p. 27: Uli qui intelligunt scripturam sacram aliter quam Spiritus Sanctus /Iagitat sunt heretici? | quod videtur panis est, sed quod creditur panis est corpus Christi, | ut quando. | tam profundus; | in probabiles.
p. 28: iste quem videtis in altari sanctificatus per verbum Dei corpus Christi est. Quod habet calix sanctificatum per verbum Dei sanguis Christi est. Per ista voluit Dominus commen- | dare corpus suum et sanguinem. Si bene accipitis, unus panis, unum corpus multi sumus, sicut exponit Apostolus. Et sic commendatur vobis in isto pane quomodo unitatem diligere debeatis. Numquid enim panis ille de uno grano factus est? ymmo multa\5 erant tritici grana? Sed antequam ad panem venirent, separata erant, per aquam coniuncta sunt et post quandam contricionem. Nisi enim molatur triticum, per aquam conspergatur et per ignem pinsatur, ad formam minime venit que panis vocatur. Sic et vos | ante ieiunii humiliacionem exorcismi sacramento quasi molebamini. Accessit baptismum; quasi aqua conspersi estis et igne karitatis cotistantes 7 ut ad formam panis veniretis. | Si unde; | tercie grana, | sistis (accessistis); | et quasi.
p. 29: Hoc est); | verborum Domini | quin sine. | vel ut — unum | ex illa
```

---

## Chunk 02-a: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-02-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-02-a
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "29.25–33.26"
divisions: "cap. 2 (heading 'CAPITULUM SECUNDUM.' at 29.0); part 1 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "864 words; 850 confirmed by the vote; 11 runs stood by rule; 3 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n100–n104 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 2, part 1: [TITLE]

## ¶1 · 29.25–30.5

> [p. 29] Premissa ista communi sentencia de isto venerabili sacramento restat scrutari quid ipsum sit realiter. In qua materia sunt tres vie: prima videtur esse sentencia sancti Thome cum suis sequacibus quod Eukaristia [p. 30] sit magnitudo de genere quantitatis, quia cum oportet ipsum esse accidens, quantitas autem est primum accidens post genus substancie, oportet illud sacramentum sensibile esse quantitatem continuam permanentem qua panis perante formaliter fuit quantus.

[ENGLISH]

## ¶2 · 30.6–31.20

> [p. 30] Secunda opinio videtur esse Scoti qui inprobat opinionem priorem per hoc quod hoc sacramentum potest rarefieri et condensari, quod non potest competere quantitati; ideo cum sit accidens consonum, videtur ipsum ponere qualitatem, cum oportet quod sit accidens absolutum. Unde aliqui istius secte dicunt quod est figura, aliqui quod est qualitas prima, et alii quod est qualitas secunda, ut color, sapor vel aliud huiusmodi sextuplex vel ex multis accidentibus aggregatum. Tercia opinio est Beringarii, et videtur esse decretum sancte sinodi. Constat quidem ex publica et sollempni confessione Beringarii posita in De Consecracione, distinccione 2ª, Ego Beringarius, quod ipse corrigendo errorem priorem confitetur panem et vinum esse hoc sensibile sacramentum. Nam (ut recitavi superius) ibi inscribitur sua confessio sub hiis verbis: Credo panem et vinum que in altari ponuntur post consecracionem non solum sacramentum sed eciam verum corpus et sanguinem domini nostri Jesu Christi esse sensualiter non solum sacramentum, sed in veritate manibus sacerdotum tractari et frangi et fidelium dentibus atteri. Ubi patet quod ille sensit quod idem panis et vinum quod ponebatur ante missam super altare remanet post consecracionem [p. 31] tam sacramentum quam corpus dominicum. Quod autem ista fuit tunc sentencia Romane ecclesie, patet ex tribus: primo quia in eodem decreto ex verbis notarii sic habetur: Hoc lecto et perlecto sponte subscripsi. Hanc confessionem sue fidei de corpore et sanguine domini nostri Jesu Christi a Beringario Rome coram centum 14ᶜⁱᵐ episcopis factam. Ex quo patet quod ecclesia tante sinodi non permitteret revocacionem prioris heresis et correpcionem suam sine vituperio sub hiis verbis nisi suam fidem tamquam katholicam approbaret. Secundo confirmatur ex eodem decreto quod ista fuit tunc Romane ecclesie sentencia. Nam ibidem sic scribitur: Misit papa Nicholaus per urbes Italie, Germanie Gallie et ad quecunque loca fama pravitatis eius pervenire ante potuit, ut ecclesie que prius doluerant de adverso atque diverso, post ea gauderent de reverso atque converso. Ex istis luculenter patet quod ecclesia tunc sensit sentenciam predictam Beringarii esse katholicam et sentenciam illi contrariam esse hereticam.

[ENGLISH]

## ¶3 · 31.21–32.4

> [p. 31] Tercio confirmatur idem per hoc quod in prima revocacione sua protestatus fuerat sub hiis verbis: Consencio autem sancte Romane ecclesie et apostolice sedi, et ore ac corde profiteor de sacramentis dominice mense eandem fidem me tenere quam dominus et venerabilis papa Nicholaus et hec sancta sinodus auctoritate evangelica et apostolica tenendam tradidit michique confirmavit. Et post confitetur sentenciam supradictam. Ex quibus colligitur quod sentenciam [p. 32] illam receperat a papa et sinodo confitendam; et patet quod olim fuit sensus ecclesie, ut de articulo fidei quod panis et vinum remanent post consecracionem Eukaristie sicut ante.

[ENGLISH]

## ¶4 · 32.5–32.9

> [p. 32] Ex quibus colligitur quod altera istarum ecclesiarum erravit in fide vel equivocavit in loyca vel significacione, vel tercio quod in tempore successit credendi varietas, sic quod illud quod tunc fuit articulus fidei iam est falsum.

[ENGLISH]

## ¶5 · 32.10–32.15

> [p. 32] Sed constat quoad hoc tercium, quod equa racione verum foret quod panis et vinum remanent post consecracionem in Eukaristia, sicut umquam fuit verum vel credendum; ideo cum equivocacio in materia fidei non excusat, videtur quod altera ecclesia erravit.

[ENGLISH]

## ¶6 · 32.16–32.32

> [p. 32] Ex quo patet primo quod Romana ecclesia potest errare in articulis fidei, cum sic fecit; patet secundo quod non oportet credere quod si Romana ecclesia quidquam katholicat vel hereticat, ergo vere; et tercio videtur probabile quod prior ecclesia sane sensit in isto et posterior oberravit; tanta namque auctoritas, tanta sanctitas et tanta sapiencia vel maior lucebat in isto papa Nicholao II° secundum cronicas et istis 114ᶜⁱᵐ episcopis, sicut in eo qui composuit decretales. Quare ergo non crederetur tante vel plus sue sentencie sicut debiliori sentencie succedenti? Ecclesia enim deteriorando quoad fidem scripture procedit. Et iterum prior sentencia plus consonat sensui, racioni, sanctis doctoribus et scripturis, igitur cum illa non sit posterius abrogata vel inprobata, videtur quod ecclesia adhuc debet illam credere sicut primo.

[ENGLISH]

## ¶7 · 33.1–33.8

> [p. 33] Quod autem plus consonat sensui et racioni patet inferius, et quod plus consonat sanctis doctoribus patet ex tribus: primo ex dicto beati Ambrosii, posito in De Consecracione, distinccione IIª Omnia quecunque: Licet figura panis et vini videatur, nichil tamen aliud quam caro Christi et sanguis post consecracionem credenda sunt. Ecce quod panis et vinum credenda sunt esse caro Christi et sanguis.

[ENGLISH]

## ¶8 · 33.9–33.19

> [p. 33] Secundo confirmatur eadem sentencia ex dicto beati Augustini eadem distinccione, Qui manducant, ubi loquens de hoc sacramento sic dicit: Quod videtur, inquit, panis est et calix quod oculi renunciant; quod autem fides postulat instruenda, panis est corpus Christi et calix est sanguis. Ista ideo dicuntur sacramenta, quia in eis aliud videtur et aliud intelligitur. Quod videtur speciem habet corporalem, quod intelligitur fructum habet spiritualem. Ecce quod iste sanctus ponit panem et vinum esse sacramentum visibile.

[ENGLISH]

## ¶9 · 33.20–33.26

> [p. 33] Tercio confirmatur ex dicto Hilarii eadem distinccione, ubi sic scribitur: Corpus Christi quod sumitur de altari figura est, dum panis et vinum extra videntur, veritas autem, dum corpus Christi et sanguis in veritate interius creduntur. Quotlibet sunt dicta similia dictis istorum trium sanctorum que expresse dicunt sentenciam quam utrobique Beringarius confitetur.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 29.25: Three opinions on the Sacrament:
- 30.1: 1. that of St. Thomas who says that it is a quantity;
- 30.6: 2. that of Scotus who says it is quality;
- 30.15: 3. that of Berengarius contained in his approved confession.
- 31.21: Our view supported by his first revocation.
- 32.16: The Roman Church may err.
- 33.1: St. Ambrose,
- 33.9: St. Augustine,
- 33.20: St. Hilary.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 31: *tamquam* (print = bt) [BT-ONLY]
  - 31: *fama* (print = bt) [SUB]
  - 31: *fuerat* (print = bt) [SUB]
- **Omitted per §3.5 / kept in the English** (margin matter): reference The Roman Church may ? • c , . . , . , (32.16); reference St. Augustioe, (33.9).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 29:
5. D: concederet. 6. ABCE: ista deest; ib. C: Chrisii alia manti.
7. C: suspendere alia manu. 9. est; B : et. i3. ABC: pleni; ih. D:
ista simul. i3, 14. E: et specialiter. i5. B: ut sunt. 16. D : ab-
negande. 19. B: ideo non ; ih. B: iste. 21. C: non al. manu.
22. D: invisibililer absconditus ; E: est absconsus. 23. B: illa elc.
24. ABCE: cap. secundum deest. 28. E: beati.
i5. Decr. Greg. IX, lib. III, tit. XLI, cap. VI. 28. Gf. St.
Thomae Summa, III, quaest. LXXVf. Super Quart. Sententiarum,
dist. X, quaest. I, art. II.

p. 30:
4. E: sensibile deest. 8. C: ABC: et deest; ib. AB : indensari;
E: vel condensari. Q, 10. D : consonum ipsum videtur. 10. B: quanti-
tatem. i3, 14. D : et huiusmodi; aliud deest; E: ut aliud ; C: aliud alia
manu. 14. C : sextuplex alia manu ; D: huiusmodi hoc vel. i5. E: aggre-
gati. 19. D: quod ipse deest. 24. C: corpus Christi. 25. Recte :
nisi in solo sacramento. Cf. Conf. Berengarii 1. c.
6. Cf. Joannis Duns Scoti De Eucharistia (Lugd. i63g) Scho-
lium III. 18. Decreti Tertia Pars, De Consecrat., dist. II,
cap. XLII.

p. 31:
4, 5. ABC: sponle scripsi. 7. factam. Cetera infra sequuntur : factam
misit papa Nicolaus pcr urbes Ilaliae, Germaniae, Galliae ad quaecunque
loca fama pravitatis eius pervenire ante potuit .... q. ABC: et con-
cepcionem. 10. C: hiis deest; ib. ABD : nec suam. 12. ABC: tuncfttit.
16. C: sive diverso. 17. AB: gaudenter ; ib. E: E.x quo. 22. re-
vocacione ; Herzberg-Franckcl legit: ralificacione ; D: renovacione.
27. ABCE: aucloritate deest; C addit in marg. alia manu; ib. D: tenenda.
i3. De Consecratione, dist. II, cap. 42 1. c.

p. 32:
1. D: ad confitendam. 8. E: illud quod deest. 12. I) : sic.
i5. D: oberravil. 16. D: potuit. 17. ABC: patet et sic. iS. E: est
credendum nobis 11011 oportet credere si ; ib. D: quod deest. 19. 1>:
ergo etc. 19, 20. AB : tercio vel probabile; C: videtur in rasura.
20. ABC: quod quod. 23. B: sciendum secundum. 24. C: istis jijim.
3i. A: di-bct in marg. alia manu. 3i, 32. ABC: sicut prime.

p. 33:
i. 2. C: phu — et quod deest. 3. E: posilo deest. 6. E: sanguis
Christi. 9. B: confirmat; ib. ABCD : beati deest. 10. DE: manducat.
12, i3. AD: quod autem panis ; BC : panis extinct. corr. : fides. 14. ABC :
Ideo ista. 22. C : de altari deest. 22. 23. D : exlra unum. 23, 24. Recte:
videtur . . . creditur. 23. ABCE: autem dicitur. 25. ABCE : qui ex-
presse. 29. ABCD : Act. XX.
4. Decreti Tertia Pars, dist. II, cap. LXXTV. Cf. Joh. Wyclif,
De Apostasia, pag. 64. 10. ib. cap. LVIIl. 21. ib. cap. LXXIX.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 29: Hoc est); | verborum Domini | quin sine. | vel ut — unum | ex illa
p. 30: Intelligendum est panem super altare positum per illa sollempnia verba in corpus mutari, nec remanere substanciam panis | et vini, speciem tamen intelligendum est remanere, scilicet formam, colorem et saporem, et secundum illa fit attricio, soricis corrosio et multiplex localis mocio, ut in ventrem trahicio, non autem secundum corpus Christi. | violari et corrodi. | et in rentrem.
p. 31: Existente namque corpore colorem 2d eius esse necesse est, et pereunte corpore colorem eius manere inpossibile est. | sit hoc sic; | officium iante; | et ad. | et decretiste.
p. 32: sancti in | quod econtra. | Et est. | et non econtra. | species specie; | ut inquiunt.
p. 33: Omnia quecunque: Licet figura panis et vini videatur, nichil tamen aliud quam caro Christi et sanguis post consecracionem credenda sunt. | Qiii manducant, | Quod videtur, | panis est et calix quod oculi renunciant; quod autem fldes postulat instruenda, panis est corpus Christi et calix est sanguis. Ista ideo dicuntur sacramenta, quia in eis aliud videtur et aliud intelligitur. Quod videtur speciem habet corporalem, quod intelligitur fructum habet spiritualem. | Corpus Christi quod sumitur de altari figura est, dum panis et vinum extra videntur, veritas autem, dum corpus Christi et sanguis in veritate interius creduntur. | Sicut ergo non dicimus tres essencias, ita non dicimus tres magnitudines. In rebus, | que participacione | magnitudinis magne sunt, quibus aliud est esse, aliud magnum esse, sicut magna domus et magnus mons et magnus animus, in hiis ergo rebus aliud est magnitudo, aliud quod ab ea magnitudine magnum est, et prorsus non hoc est magnitudo quod magna | domus, sed vera magnitudo in Deo est ipse Deus et non sibi accidens. | que ab. | sed magna. | Sed illa est vera magnitudo qua non solum magna est domus quae magna est et qua magnus est mons quisquis magnus est.
```

---

## Chunk 02-b: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-02-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-02-b
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "33.28–36.23"
divisions: "cap. 2 (heading 'CAPITULUM SECUNDUM.' at 29.0); part 2 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "641 words; 613 confirmed by the vote; 9 runs stood by rule; 19 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n104–n107 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 2, part 2: [TITLE]

## ¶1 · 33.28–34.11

> [p. 33] Quantum ad testimonium scripture patet Math. XXVIº, Marc. XIVº, Luc. XXIIº et Iª Cor. XIº, et Act. IIº [p. 34] ac Joh. VIº, ubi fit mencio de hoc sacramento et datur forma conficiendi; utrobique narratur quod Jesus accepit panem et de illo dixit: Hoc est corpus meum. Nam Luc. XXIIº, 19 sic scribitur: Et accepto pane gracias egit et fregit et dedit eis dicens: Hoc est corpus meum; ubi patet non protervo quod illum panem quem accepit postea demonstravit. Et constat quod illo manente pane non est realiter corpus Christi sed signum efficax eius. Ex istis colligitur quod confessio Beringarii et antiquum decretum ecclesie sunt undique plus consona veritati.

[ENGLISH]

## ¶2 · 34.12–34.17

> [p. 34] Sed obicitur per hoc quod secunda pars decreti repugnat priori et katholice veritati et per consequens tota confessio est infecta; ponit enim quod panis et vinum nedum sunt sacramentum post consecracionem, sed verum corpus Christi et sanguis quod frangitur et sentitur ut panis, quod est contra dicta.

[ENGLISH]

## ¶3 · 34.18–35.14

> [p. 34] Hic dico (ut supra) quod oportet omnino equivocare in isto secundo dicto, cum nec substancia panis nec illud quod fuit eius forma accidentalis sit realiter corpus Christi, sicut oportet tam antiquos quam novellos concedere; ideo dicit glosa ordinaria quod oportet confessionem Beringarii sane intelligi, quia aliter foret novissimus error peior priore ab ecclesia dampnato tanquam heretico. Hodie namque approbaretur prior Beringarii opinio secundum tres partes quas ecclesia tunc dampnavit tanquam hereticas, scilicet quod illud album manet post consecracionem solummodo sacramentum, secundo quod illud non est corpus Christi, et tercio quod per sensacionem illius [p. 35] corpus Christi non frangitur vel sentitur. In istis tribus se correxit iuxta decretum ecclesie; et revera nunc defendere quod ecclesia illa tunc erravit in fide tanquam ignara loyce que per sapienciorem ecclesiam est correcta foret inponere toti determinacioni nostre quoad materiam fidei suspectam calumpniam; per idem est dicere quod scriptura cum sanctis doctoribus defecit in istis. Sed quis tunc crederet verbis nostris, cum possumus ad nutum fidem pro pecunia variare? Oportet ergo glosare dictum utriusque ecclesie secundum regulam fidei scripture, et hoc est plus consonum et honorabilius utrobique omnino ad intelligendum scripturam, sanctos doctores et confessionem Beringarii, que fuit decretum ecclesie.

[ENGLISH]

## ¶4 · 35.15–36.23

> [p. 35] In ista materia oportet (ut supra) signanter notare distinccionem inter predicacionem ydempticam et predicacionem tropicam. Ydemptica est (ut dixi), quando predicatum ydemptice asseritur de subiecto, ut Christus est homo. Sed predicacio tropica vel figurativa est, quando unum extremum notatur figurari per reliquum, ut prius exposui: Petra autem erat Christus. Unde triplex exemplum adduco de omnibus pro hoc sensu; primum est dictum Apostoli I. Cor. Xº, 1, 4: Nolo autem vos ignorare fratres, quoniam patres nostri omnes sub nube fuerunt, et omnes mare transierunt, et omnes eundem potum spiritualem biberunt. Bibebant autem de spirituali consequente eos petra: petra autem erat Christus. Et patet quoad intellectum istius scripture et sibi similium quod oportet notare sensum figurativum vel tropicum; ad quem sensum est hoc dictum eque verum sicut alia pars scripture; omnes namque patriarche fuerunt sub proteccione [p. 36] divina, secundum quam fuit ardor vindicte Domini effugatus; omnes transierunt mundi et omnium adversancium populorum periculum; et cum fides non variatur propter fluxum temporis, patet quod nutriebantur eadem fide qua christiani postmodum sunt nutriti. Et totum hoc figuratum est per ambulacionem quadraginta annorum ad terram promissionis, sic quod nichil contigit itinerantibus de Egypto quin fuit figura futura succedentibus in peregrinacione sua ad patriam. Sicut enim populus bibebat de aqua fluente de petra quam Moyses bis percussit (ut patet Exodi XVIIº, 6), sic populus christianus bibit spiritualiter subtilitatem fidei Jesu Christi postquam populus iudaicus Christum infamiter sic percussit; et sicut secutum fuit obiurgacionis obprobrium de percussione predicta, ita consequitur iudeos obprobrium, quod Christum sic in patibulo percusserunt. Petra, inquit, erat Christus, hoc est, illa petra Christum mistice figuravit. Notandum tamen quod tales locuciones possunt dupliciter sane intelligi, scilicet quod talis figura figuravit huius figuratum, vel dimittendo litteralem sensum figure intelligere equivoce figuratum, et utrobique erit sensus katholicus absque scrupulo falsitatis.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 33.28: Witness of Scripture.
- 34.18: The modern church falls into the error that Berengarius renounced.
- 35.15: We must note when speech is figurative.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 33: *Math. XXVIº,* (print = bt) [BT-ONLY]
  - 33: *Iª* (print = bt) [SUB]
  - 34: *ubi* (print = bt) [SUB]
  - 34: *fregit* (print = bt) [SUB]
  - 35: *1,* (print = bt) [BT-ONLY]
  - 36: *vindicte Domini* (print = bt) [BT-ONLY]
  - 36: *quod nutriebantur* (print = bt) [BT-ONLY]
  - 36: *postmodum sunt* (print = bt) [BT-ONLY]
  - 36: *per ambulacionem* (print = bt) [BT-ONLY]
  - 36: *sic quod* (print = bt) [BT-ONLY]
  - 36: *quin fuit figura* (print = bt) [BT-ONLY]
  - 36: *subtilitatem* (print = bt) [BT-ONLY]
  - 36: *fuit obiurgacionis* (print = bt) [BT-ONLY]
  - 36: *predicta, ita* (print = bt) [BT-ONLY]
  - 36: *erat Christus,* (print = bt) [BT-ONLY]
  - 36: *figuravit. Notandum* (print = bt) [BT-ONLY]
  - 36: *dupliciter sane* (print = bt) [BT-ONLY]
  - 36: *figuravit huius* (print = bt) [BT-ONLY]
  - 36: *sensum figure* (print = bt) [BT-ONLY]
- **Omitted per §3.5 / kept in the English** (margin matter): reference St. Augustioe, (33.9); reference Exodi XVII0, 6), (36.11); reference Apoc. XIX0, 8: (36.24).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 33:
i. 2. C: phu — et quod deest. 3. E: posilo deest. 6. E: sanguis
Christi. 9. B: confirmat; ib. ABCD : beati deest. 10. DE: manducat.
12, i3. AD: quod autem panis ; BC : panis extinct. corr. : fides. 14. ABC :
Ideo ista. 22. C : de altari deest. 22. 23. D : exlra unum. 23, 24. Recte:
videtur . . . creditur. 23. ABCE: autem dicitur. 25. ABCE : qui ex-
presse. 29. ABCD : Act. XX.
4. Decreti Tertia Pars, dist. II, cap. LXXTV. Cf. Joh. Wyclif,
De Apostasia, pag. 64. 10. ib. cap. LVIIl. 21. ib. cap. LXXIX.

p. 34:
I. C: sacramento dccst. 4, 5. ABC: Et accepil panem. 5. E: dedit
Hlis) li: dedit di. 7. B: prnpterea. 9. B: Kt ex istis; C: Ex hiis.
11. B: plus dcest. 10. AB: cum iam. 27. B: condempnavit.
II. CJ. De Apostasia, pag. 68. 22. Cf. Glossam orJin. ad
vocem Dentibus: Nisi sane intelligas vcrha Berengarii, in maiorem
incides haeresim quam ipse habuit et ideo omnia referas ad
species ipsas, nam de Christi corpore partes non fecimus . . .

p. 35:
1. D: non dcest. 3. C: ecclesia deest. 4. D: loyca ; ib. ABDE :
que post. 7. ABC: idcm condicere; E: contradicere. S. E : deficit.
Q. A: cum possumus ad merilum : BCE: ad ritum; I>: ad votum. Corrcxi.
12. H: ubique. 20. D: reliqua. 24. ABDE : quomodo patres;
ib. ABCD: vestri. 27. B: speciali. 3o. C: et tropicum. 3i. L) : eane
unum ; ib. ABCE: sicut aliqtia. 32. ABCD: omnes inqnam.

p. 36:
8 D: si itinerantibus; ib.C: de Egypto
ib. C: Christum decst. 3i. D : Exod. XXIV.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 33: Omnia quecunque: Licet figura panis et vini videatur, nichil tamen aliud quam caro Christi et sanguis post consecracionem credenda sunt. | Qiii manducant, | Quod videtur, | panis est et calix quod oculi renunciant; quod autem fldes postulat instruenda, panis est corpus Christi et calix est sanguis. Ista ideo dicuntur sacramenta, quia in eis aliud videtur et aliud intelligitur. Quod videtur speciem habet corporalem, quod intelligitur fructum habet spiritualem. | Corpus Christi quod sumitur de altari figura est, dum panis et vinum extra videntur, veritas autem, dum corpus Christi et sanguis in veritate interius creduntur. | Sicut ergo non dicimus tres essencias, ita non dicimus tres magnitudines. In rebus, | que participacione | magnitudinis magne sunt, quibus aliud est esse, aliud magnum esse, sicut magna domus et magnus mons et magnus animus, in hiis ergo rebus aliud est magnitudo, aliud quod ab ea magnitudine magnum est, et prorsus non hoc est magnitudo quod magna | domus, sed vera magnitudo in Deo est ipse Deus et non sibi accidens. | que ab. | sed magna. | Sed illa est vera magnitudo qua non solum magna est domus quae magna est et qua magnus est mons quisquis magnus est.
p. 34: Hoc est corpns meum. | Et accepto pane gracias egit et fregit et dedit eis dicens: Hoc | est corpus meum; | ex islis. 6. | sic subslancia. | in cause. | et est. | vel actuaciones.
p. 35: Petra autem erat Christus. | Nnlo autem vos ignorare fratres, quoniam patres nostri | omnes sub nube fuerunt, et omnes mare transierunt, et omnes eundem potum spiritualem bibcrunt. Bibebant autem de spirituali consequente eos petra: pctra autem crat Christus. | et propter. | eos quod. | Quam nisi autem. | sompnii decurrentis quod quod. | sit nostris. | fundamento istius. | et virtutibus | Sicut ergo; | Deum inesse; | Deus inesse. | tam ergo.
p. 36: erat Christus, | Byssinum enim iustificaciones sunt sanctorum, | Hic calix novum testamentum est in meo sanguine; | AC: preterquam; | filios posterwres. | vobis quod ante verba Christi quod offertur panis | dicatur, sed cum verba Christi deprompta fuerint, i$ iam non panis dicitur sed corpus appellatur. | Sacramentum quidem pene omnes corpus Christi dicunt. | esse in similitudinem carnis peccati et nunc dicitur peccatum. Solet, | similitudo capere nomen rei cuius est similitudo, | elicere ars actus. | que offertur. | corpus esse dicunt.
```
