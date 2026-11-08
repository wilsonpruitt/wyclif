# Translation brief: eucharistia 05-b–05-d

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/eucharistia/wyc-eucharistia-05-b.md chunks/eucharistia/wyc-eucharistia-05-c.md chunks/eucharistia/wyc-eucharistia-05-d.md` once and fix what it reports.
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

## Glossary (the 487 rows these chunks use; the full file is GLOSSARY.md)

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
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
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
| sacer; sacrare | sacred; hallow | Kept apart from *sanctus / sanctificare* "holy / sanctify" and from *consecrare*; *consecrare* is "to hallow together" in the grammarians' etymology. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 27–28). |
| sacramentum tantum | a sacrament only | The *sacramentum tantum* of the Lombard's three (IV d. 8 c. 4). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 29.23). |
| conversio (eucharistic) | conversion | Of bread into the body; kept apart from *conversio* of a proposition. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 48.15). |
| decretalis | decretal | Kept apart from *decretum* "decree". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 71.31). |
| principaliter; principalitas (of the body's presence) | principally; principality | Of the body of Christ alone being in the sacrament as its principal; not the compendium's *principaliter* "as a main head". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 75.5–26). |
| transaccidentacio | transaccidentation | Wyclif's coinage beside *transsubstanciacio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 81.27). |
| transinferioracio; transsubieccio | transinferioration; transsubjection | Coinages in the same series. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 82.3). |
| baptiste signorum | baptizers of the signs | Not "Baptists". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 81.29). |
| concomitanter | concomitantly | Of the body present with the blood by concomitance; cf. *gracia concomitancie*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 81.23–25). |
| accepcio personarum | respect of persons | The Douay phrase. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 92.15). |
| consecracio | consecration | The noun of *consecrare*; see *confeccio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 99–100). |
| commenta scripture | commentaries on scripture | Kept apart from *commentum (mendacii)* "fabrication". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 116.28). |

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
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| graduacio; graduati | CONTEXTUAL: graduation / gradation; graduates | Academic "graduation" (Dialogus, 4 sites); of rank or lordship (*graduacio dominii*, *Pot. pape* 293.33, 297) "gradation". Ruled 2026-09-28; CONTEXTUAL 2026-10-12 (coordinator, delegated). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| protestacio; protestari | declaration; to declare solemnly | ⭐ The submission formula ("if anyone can teach me this is contrary to scripture or reason, I will humbly retract"). Penn and Lahey both inverted it (T. pp. 369, 378). Render it as a retraction offer, never as defiance. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| decretum; decreta | decree; the decrees | Gratian (*in decretis*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.14, 3.24). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| credulitas | credence | With *credere*, believe (*Dial.* 23.17–24.4). Ruled 2026-09-28. |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| sumitur pro | is taken for | Supposition language. Pilot. |
| simpliciter / secundum quid | **without qualification / in a certain respect** | ⛔ Always opposable. Never "simply", "wholly", "directly", "naturally" etc. (T. p. 364). |
| necessitas supposicionis / ex supposicione | necessity of supposition / necessity on supposition | Conditional necessity. Pilot (*Eccl.* 3.21); *ex supposicione* ruled 2026-10-02 (34.12, 38.22). |
| de congruo / de condigno | by congruity / by condignity | Pilot. |
| consequencia | inference | ⛔ Not "consequence" (T. p. 361 n. 13). |
| consequens / antecedens | consequent / antecedent | |
| sequitur | it follows | Introduces a stated inference, often quoted in the next words. Pilot (*Eccl.* 2.21). Not tagged where it is not an inference ("the third law follows", *Dial.* ch. 5). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| propositio copulativa / disiunctiva | conjunction / disjunction | Not "copulative proposition" (T. p. 365). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| humanitas | the humanity | The nature the Word assumed, body and soul; with the article (*humanitas sit Christus*, "the humanity is Christ"). Not "the human nature", which is *natura humana*. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| dimittere / dimissio (*naturam*) | lay aside / the laying-aside | Letting go the assumed nature, so the union would be dissolved. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 2.23). |
| ydemptitas specifica | identity of species | That Christ and other men are of one species. Not "specific identity" (reads as "particular"). Ruled 2026-10-22 (Wilson; *Incarn.* prol, 8). |
| Verbum | the Word | Pronoun **"he"** (as Douay–Rheims John 1:3, "by him"), never "it", though the Latin is neuter; so also *Sapiencia* where Wisdom is the Word in person (*Incarn.* 7, coordinator). Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.3–4). |
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
| abstractive | abstractively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 10.6). |
| Sermo (beside *Verbum*) | Speech | The divine title, capitalised; *Verbum* stays "the Word". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 16–17). |
| de vi vocis / de vi sermonis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| protervus | obstinate | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| gracia unionis | the grace of union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| humiliacio | humbling | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26–28). |
| humanitus | humanly | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* passim). |
| in quantum (reduplicative) | insofar as | As *secundum quod*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37.9). |
| unio | union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 39). |
| universitas creaturarum | the totality of creatures | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37). |
| diccio (logical) | word | A single term in a proposition. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 43.3). |
| in effectu | in actual fact | As against in potency or in name; ⛔ not "in effect" (modern "virtually"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 47.10). |
| animare | animate | The argument turns on it (45.30–46.4). Ruled 2026-10-22 (coordinator, delegated). |
| communicacio ydiomatum | communication of idioms | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.1). |
| predicacio actualis / aptitudinalis / habitudinalis / mixtim | actual / aptitudinal / habitudinal / mixed predication | *Habitudinalis* is its own term (the four MSS at 49.6), not under *habitudo*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.5–16). |
| Doctor Subtilis | the Subtle Doctor | Scotus. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.24). |
| convertibilis / converti | convertible / be convertible | Of terms. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 52.29). |
| previe requisitum | required beforehand | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 53.25). |
| forma totalitatis | form of totality | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 50.7). |
| quantus | quantified | The adjective beside *quantitas*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.22). |
| construccio synecdochica | synecdochic construction | Beside *synecdochica locucio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.5). |
| carneus / carnalis | fleshy / carnal | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.21). |
| moderniores loquentes | the more modern speakers | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 59.21). |
| dampnificare / dampnificacio | damage / damaging | Kept apart from *dampnum* "loss" and *dampnari* "be damned"; the argument of 65–68 turns on it. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 65). |
| per se / per accidens | CONTEXTUAL: of itself / by accident; (spatial) apart, by itself | The spatial sense (a thing set apart, *Euch.* 104.16–17) gets a G note. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a (sufficienti) divisione | the topic from sufficient likeness / from (sufficient) division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| peccabilis | able to sin | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| ydemptitas ypostatica | hypostatic identity | Beside *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 84.20). |
| capitales doctores | the chief doctors | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| eiusdem / consimilis / alterius racionis | of the same / like / another kind | The species-sense of *racio*; *racio speciei* "the account of the species" (Aristotle's *logos*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.4, 87.17). |
| principiari | be constituted from principles | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.7). |
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
| universitas creata | the created totality | Beside *universitas creaturarum*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| significatum | significate | Kept apart from *signatum* "thing signified". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 111). |
| sermo vocalis | the spoken word | Against *Sermo* "Speech", the divine title. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 113). |
| predicacio secundum essenciam / formalis | predication by essence / formal predication | Wyclif's modes of predication (cf. *predicacio secundum causam*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 115–116). |
| forma substancialis | substantial form | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| concepcio (figure) | conception | The grammatical figure. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| accidens | accident | The category; *accidit* "befalls". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| figura / figuratum | figure / thing figured | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 121.23). |
| conversio (of a proposition) | conversion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.30). |
| humanitacio | humanation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 126.12). |
| racio (individual, personal) | account | *Racio individui / persone* "the account of an individual / a person", as *racio speciei*; not "aspect" (the row against *substancia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 8, 129–132). |
| vir (against *homo*) | man (*vir*) | Where Wyclif sets *vir* against *homo*, the Latin in parentheses. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 129.15–26). |
| exemplaria / exemplata | exemplars / things exemplified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.6). |
| res secunde intencionis | things of second intention | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.25). |
| complexio | complexion | The mixture of qualities. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137–138). |
| materia proxima / remota | proximate / remote matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137.1). |
| personari | be made a person | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 134.10). |
| colorate | with colour enough | With a plausible ground (cf. *color*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 134.26). |
| ydemptificare / ydemptificacio | identify / identification | Make the same (*idem*); the hypostatic union as identification, not conversion or generation. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 142.19, 147.22). |
| res communis / res communes | the common thing / common things | The realist universal the *moderni* do not conceive (first root of their error). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 144.27). |
| distinccio racionis | distinction of reason | Beside *differencia formalis*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 145.23). |
| conversio naturarum / confusio naturarum | conversion of the natures / confusion of the natures | Kept apart from *conversio* of a proposition. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 143.9). |
| moderni (bare) | the moderns | Beside *moderni doctores* "the modern doctors". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 142.10). |
| principiare (active) | be the principle of | Beside the passive *principiari* "be constituted from principles". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 147.4). |
| moderniores (bare) | the more modern | Beside *moderniores doctores* "the more modern doctors". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 151.17). |
| concretum / abstractum | concrete [term] / abstract [term] | *Homo* the concrete, *humanitas* the abstract. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 152). |
| transsumpcio | transumption | Beside *transsumptive*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 153.28). |
| personalitas | personality | The scholastic term: what makes a person a person, not character. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 155). |
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
| mocio / motus (paired) | motion (*mocio*) / movement (*motus*) | Only where Wyclif pairs them; otherwise "motion". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 180). |
| posicio anime | the laying-down of the soul | John 10:17–18; not the logical *posicio* "position", C note. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 183.3). |
| causancia / causacio | causing / causation | Kept apart (both at 187.30–34). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 185.16). |
| personare (active) / personacio | make a person / personation | Beside the passive *personari* "be made a person". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 188.16, 188.32). |
| peticio (principii) / petitur | begging [of the question] / is begged | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.23). |
| perfeccio simpliciter | perfection without qualification | After *simpliciter* "without qualification". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.1). |
| transsubstanciacio | transubstantiation | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.10). |
| multiplicative | multiplicatively | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 193.20). |
| remitti / intendi (of a quality, merit) | be remitted / be intensified | The intension and remission of forms; not *remissio* of sin. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 197.1–7). |
| in divinis | among the divine [persons] | Keeps "Godhead" for *deitas*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 196.18). |
| partes proporcionales | proportional parts | The halving division of a continuum. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 194.24). |
| universitas creabilis | the creatable totality | Beside *universitas creaturarum* "the totality of creatures". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 199.5). |
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
| exponentes | the exponents | The propositions into which a proposition is resolved (expounded). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 216.14). |
| moderni loquentes | the modern speakers | Beside *moderniores loquentes*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 221.20). |
| mixtim (bare) | in a mixed way | Beside *predicacio mixtim*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 230.21). |
| signum reduplicatum | the reduplicated sign | The reduplicative word (*secundum quod*, *in quantum*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 230.23). |
| lex proximitatis | the law of neighbourhood | The duty to love one's neighbour (*proximus*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 101.29). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |
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
| sentencia (verborum, scripture) | sense | The meaning of words or a text (*ad sentenciam attendendum*, against the rites, 4.9); kept out of the two-sense row *sentencia*. Ruled 2026-11-06 (Wilson; *Euch.* prol-a 4.9, review b14). |
| predicacio ydemptica / tropica | identical / tropical predication | The treatise's key pair; *tropica* kept apart from *figurative*. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.21). |
| accidens sine subiecto | accident without a subject | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 3.19). |
| remanencia (panis) | the remaining (of the bread) | Verb *manere* "remain". Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.21). |
| substancia | substance | Beside *substancia prima / secunda*. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 3.14). |
| quantitas / qualitas | quantity / quality | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.7–8). |
| esse; esse sacramentale | being; sacramental being | The bare *esse* of the modes of being. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 3.28, 3.30). |
| esus / manducacio (corporalis / spiritualis) | (bodily / spiritual) eating | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.5). |
| confeccio | consecration (of the eucharist) | The noun of *conficere*, which already shares "consecrate" with *consecrare*. Where set against *consecracio* (as the verbs at 16.10), "confecting", following Wilson's "confect" (2026-11-07). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 4.4). |
| locucio tropica | tropical speech | With *predicacio tropica* "tropical predication". Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 4.26). |
| Doctor Communis | the Common Doctor | Thomas; with *Doctor Subtilis*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 8.16). |
| multitudo (of one body) | multitude | Of one body's being many (ch. 8); the plain "multitude" of persons needs no row. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 8.4). |
| sensus communis | the common sense | The inner faculty; kept apart from *sensibile commune* "common sensible". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 18.31). |
| laudative; effective | by way of praise; by way of effect | Of blessing God vs. blessing a thing. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 16.24). |
| figurare | figure | Both senses: to prefigure (the lamb figured Christ) and to shape (*figurare Deum nostrum*), which Wyclif plays on; one English word keeps the pun. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-c 10; 21.29). |
| sensualiter | sensually | Berengar's oath word (*Ego Berengarius*); kept apart from *sensibiliter* "perceptibly". A mode adverb, one word. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 26.1, 30.24). |
| sentire (an opinion: sensit quod) | hold | Of a doctor's or church's opinion; the "perceive" row is the sacrament sensed. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 30.30, 31.18). |
| predicacio figurativa | figurative predication | A synonym of *predicacio tropica*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 35.18). |
| aliquitas | somethingness | Being a something (*aliquid*). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 60.27). |
| cedere (in) | give way (into) | Of the bread passing into the body. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 58.3, 60.9). |
| informacio; informare | informing; inform | Of a form in its subject; not "information". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 64.13). |
| accidens predicamentale | accident of the categories | Kept apart from the predicable *accidens*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 64.1). |
| veritas predicamentalis | truth of the categories | As *accidens predicamentale* "accident of the categories". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 69.2). |
| extense loquendo | speaking in an extended sense | Cf. *large / stricte loquendo*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 82.15). |
| esse situale / intencionale / potenciale | situal / intentional / potential being | The modes of the body's being. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 84.8 ff.). |
| sensus (of words) | meaning | Kept apart from *sentencia (verborum)* "sense" (Wilson's row). The bodily *sensus* and *sensus literalis / misticus* stay "sense". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 89.22, 04-c, 04-d). |
| interpolatus; interpolacio | interrupted; interruption | Of words spoken with pauses. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 89.4, 89.18). |
| pertinenter | fittingly | Kept apart from *convenienter*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-e, 04-f). |
| essencialiter | essentially | A mode adverb, one word. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-g). |
| noticia confusa / distincta | indistinct / distinct knowledge | As *confuse / confusus* "indistinct(ly)". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-g). |
| ponderositas; ponderosum | heaviness; heavy | The abstract against the concrete: *hostia est ponderositas sed non est ponderosum*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-a p. 10, 110.24). |
| bonitas naturalis / moralis | natural / moral goodness | Of the host. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 113.29). |
| locucio effectiva | effective speech | The words of institution that do what they say. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 115.10). |
| questio si est / quid est | the question whether it is / what it is | *Post. An.* II.1. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 119.18). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| idiota | unlearned man | Not "idiot". Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office; *quale magisterium* "what a feat of mastery" (*Incarn.* 137.14) | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| recencius | more freshly | Pilot (*Dial.* 2.10) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| ficcio | fiction | As *ficticia*; Wyclif numbers six *ficciones*. Ruled 2026-10-02 (*Eccl.* 16, 385.7). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| falsarius | falsifier | The opponent's epithet. Ruled 2026-10-02 (*Eccl.* 17, 414.6). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
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
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| memoriale | memorial | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
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
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| trahere in consequenciam | draw into a precedent | The legal idiom; *consequencia* stays "inference". Ruled 2026-10-07 (*Pot. pape* 94.13). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| preeminencia | preeminence | Kept apart from *primatus* "primacy". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| fantasia | imagination | The faculty (scholastic *phantasia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 147.11). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| regulariter | as a rule | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 165.2). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| infundabilis; infundabiliter | without foundation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 195–196). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| fantasticus | imaginary | Cf. *fantasia* "imagination". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 203.4). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| memorativa potencia | memorative power | A faculty of the soul (the "power" sense of *potencia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 219.27). |
| replicatur; replicatum | it is rejoined; rejoinder | A further objection against an answer; kept apart from *respondetur* "the reply is" (so 04-b). Ruled 2026-10-08 (coordinator, delegated; conformed 10-e, 10-g). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| papa cesareus | caesarean pope | The pope as endowed temporal lord (chs. 10–12). Ruled 2026-10-08 (coordinator, delegated). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| preponderancia; dispensacio | preponderance; dispensation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 266.11, 268.4). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| precellencia | pre-excellence | Kept apart from *preeminencia* "preeminence". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 274.33). |
| cultus Dei | worship of God | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-d). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| demereri | to demerit | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| bonificare | make good | Ruled 2026-10-02 (*Eccl.* 23). |
| precellenter | pre-excellently | Adverb beside *precellencia* "pre-excellence". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 291.2). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| gradus (of belief) | degree | The four degrees of belief (*Pot. pape* 327.18 ff.). Ruled 2026-10-12 (coordinator, delegated). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| episcopi cesarei | caesarean bishops | Extends *prelatus / sacerdos cesarius*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 331.24). |
| evangelizans | preacher of the gospel | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-g). |
| prepositus (participle of *preponere*) | the one preferred | CONTEXTUAL beside *prepositi* "superiors" (the noun); untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| proventus | proceeds | Kept apart from *redditus* "revenues". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 353.25). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| coloracior | more colourable | Comparative, with the *color* / *colorabilis* rows. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 384.15). |
| obviare; obvia (logical) | meet; meeting | Of a case or argument. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 383). |
| diccio procuratoria | proctorial pronouncement | C note gives *dicio* "authority" as the alternative. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 386). |
| servitus ydolorum | servitude of idols | Beside *servitus laboris*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| precellere | excel | Verb beside *precellencia* "pre-excellence"; not "pre-excel". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 399.28). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |
| nimis | exceedingly | Medieval intensive (= *valde*); "too much" only where excess is the point. Ruled 2026-10-12 (close-out R2; *Pot. pape* 169.2). |
| sentire (the sacrament, the body) | perceive | "sense". As *sensibilis* "perceptible". Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.10, 1.17). |
| recitare | recite | To report, rehearse. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.4, 3.10, 4.18). |
| narrare | relate | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.9). |
| ex tibi dubio; ex sibi dubio | for all you know; for all he knows | Idiom: not "from doubt". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 66.15, 70.25). |

---

## Chunk 05-b: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-05-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-05-b
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "119.27–123.28"
divisions: "cap. 5 (heading 'CAPITULUM QUINTUM.' at 115.0); part 2 of 11, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "908 words; 889 confirmed by the vote; 15 runs stood by rule; 4 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n190–n194 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 5, part 2: [TITLE]

## ¶1 · 119.27–120.28

> [p. 119] Sed super istos recentes sunt antiquiores et graviores persone que videntur inpugnare sensum scripture de locucione figurativa in verbis Domini, per que sacramentum istud conficitur. Scribit enim Magister Sentenciarum IVᵒ, distinccione Xᵃ in principio: Sunt [p. 120] item alii precedencium insaniam transcendentes, qui Dei virtutem iuxta modum naturalium rerum mecientes audacius et periculosius veritati contradicunt, asserentes in altari non esse corpus Christi vel sanguinem nec substanciam panis et vini in substanciam carnis et sanguinis converti, sed ita Christum dixisse: Hoc est corpus meum, sicut Apostolus dixit: Petra autem erat Christus. Dicunt enim corpus Christi ibi esse tantum in sacramento, id est in signo, et tantum in signo manducari a nobis. Qui errandi occasionem sumunt a verbis Veritatis Joh. VIᵒ. Et illud recitant ut heresim posteriores doctores, scribentes super Lumbardi sentencias et specialiter Thomas et Bonaventura. Cum ergo nos dogmatisamus eandem sentenciam, videtur quod incidimus in caribdim, et quia modicam evidenciam facit assercio istorum doctorum, attendendum est ad eorum evidenciam pro qua asserunt quod faciunt tam racio quam scriptura; decet enim Christum dominum nostrum ex maiori miraculo, pietate et gracia procedere in novo testamento quoad sacramentum finale in quo sit memoriale suorum mirabilium consumatum. Sed in veteri testamento fuit corpus Christi in manna et ceteris figuris ut signo; oportet ergo quod in isto sacramento sit humanitas Christi efficacius quam in signo, quia aliter laycus vel avis faceret in voce corpus Christi esse eque efficaciter in signo, ut est in hostia consecrata.

[ENGLISH]

## ¶2 · 120.29–121.2

> [p. 120] Quantum ad auctoritatem scripture, videtur quod Paulus qui accepit suam sentenciam a Domino et tres alii evangeliste narrant quoad hoc sacramentum [p. 121] verba sacramentalia conversiva, cum aliter forent inpertinencia sive falsa.

[ENGLISH]

## ¶3 · 121.3–121.8

> [p. 121] Sed patet ex dictis proximo capitulo quod ista evidencia non obviat nostre sentencie; omnis enim katholicus concordat cum heretico in quibusdam. Primo itaque dicendum est de veritate et diversitate nostre sentencie ab ista sentencia reprobata. Et secundo respondendum est obiectibus.

[ENGLISH]

## ¶4 · 121.9–121.24

> [p. 121] Quantum ad primum, videtur quod Christus sit in hostia ut in signo, quia aliter non foret hostia sacramentum, non tamen est sic in signis quin sit ibi realiter et vere secundum totam humanitatem; et sic conceditur quod Christus non est ibi solummodo ut in signo, est tamen ibi efficacius quam in signo; nec repugnat sed consonat quod idem sit veritas et figura vel signum, cum secundum Augustinum Enchiridion capitulo LII mors Christi, resurreccio et ascensio erant figure mortis nostre, resurreccionis et ascensionis spiritualis, et tamen erant veritas rei geste. Quamdiu itaque sumus viantes, oportet nos uti signis et vivere in velamento fidei et figuris, et sic cum in signis sint gradus multiplices, patet quod nos tempore legis gracie habemus signa efficaciora quam habebant patres veteris testamenti.

[ENGLISH]

## ¶5 · 121.25–122.8

> [p. 121] Et patet quod nec error predictus nec racio facta contra illum errorem contrariatur nostre sentencie, nam signum nostrum habet concomitanciam corporis Christi signati, cum sit signum presens ultra signa veteris testamenti et verba signorum habent coefficienciam ut corpus Christi sit taliter ibi presens, et utrumque istorum deficit in lege veteri. Ideo signanter Christus docet istam preeminenciam Joh. VIº, 49, 52, [p. 122] dum dicit: Patres vestri manducaverunt manna et mortui sunt; qui manducat hunc panem non morietur in eternum. Unde Augustinus libro Sermonum, Sermone VIIIº, notat quomodo patres legis veteris eandem escam spiritualem manducaverunt, sicut dicit Apostolus I. Cor. Xº, 3, quia patres illi fideles per manna Christum intellexerunt quem nobiscum spiritualiter comederunt.

[ENGLISH]

## ¶6 · 122.9–123.28

> [p. 122] Ulterius quantum ad verba sacramentalia, videtur probabile domino Armachano libro nono capitulo 5ᵗᵒ De Questionibus Armenorum, quod Christus confecit hoc sacramentum pura voluntate, antequam protulit illa verba, quia ut narrant Mathaeus et Marcus Jesus accepit panem, benedixit et fregit deditque discipulis suis et ait illis: Accipite et manducate, hoc est corpus meum; ubi notata serie verborum, cum uniformiter demonstravit panem quem consecratum precepit eis comedere erantque ante ista verba benediccio, fraccio et manducandi precepcio, videtur quod erat ante ista verba hoc est corpus meum panis consecracio, videtur secundo sibi probabile iuxta fidem scripture quod verba consecratoria intelligunt de pane et vino, cum omnes predicti quatuor apostoli notant quod Jesus accepit panem materialem in manus suas, quem fregit, manducari precepit et esse corpus suum asseruit; et idem iudicium est de vino. Quid enim planius quam textus Marci XIVº, 23, 24, ubi dicitur: Accepto calice gracias agens dedit eis et biberunt ex eo omnes et ait illis: Hic est sanguis meus, ubi patet quod vocat vinum contentum in [p. 123] calice sanguinem suum; et idem patet Math. XXVIº, 26. Ex quibus videtur consonancius quam dicit magister quod talis locucio sit tropica et quodammodo sed non essencialiter conversiva vini in sanguinem, cum sensus tropicus sit verus sed demonstrando panem et vinum foret falsum quoad predicacionem ydempticam quod hoc est corpus Christi vel sanguis. Si autem demonstratur pronomine panis aut vinum in principio et in fine fit conversio, tunc proposicio in sua successione foret falsa vel conversioni inpertinens, nisi sompnietur quod Deus instituit proposicionem talem ad habendum efficaciam taliter convertendi; quod non fundabitur. Si demonstretur pronomine corpus Christi, tunc nichil novi constituitur, ut sit Christi carnis effectivum. Si autem pronomen connotat quod hoc sub istis accidentibus non subiectatis est corpus Christi, petitur infundabiliter contra scripture ordinem sompniatum; et sensum istius scripture vellem illos attendere qui fantasiant ex isto textu quod est dare conversionem sine essencia differente; videtur ergo utrobique in verbis sacramentalibus esse locucionem tropicam efficaciorem quam in ista: Petra autem erat Christus, cum illa verba faciunt occasionaliter quod humanitas Christi sit realiter sed sacramentaliter ad omnem punctum hostie consecrate, et sic est illa hostia signum efficacius quam panis benedictus a layco et secundum formam aliam a presbitero benedictus.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 120.1: Peter Lombard, St. Thomas and Bonaventura are against us;
- 121.3: but their evidence does not overthrow our opinion.
- 121.9: A thing may be real and yet also a figure.
- 121.25: This figure outdoes all those of the O. T. since Christ is present with it.
- 122.9: Christ had consecrated before saying: 'This is my body'.
- 123.8: Force of the pronoun (hoc).
- 123.21: The sacramental words are the occasion of Christ's sacramental presence, and they are of more efficacy than ordinary blessing.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 119: *IVᵒ,* (print = bt) [SUB]
  - 120: *alii* (print = bt) [SUB]
  - 120: *VIᵒ.* (print = bt) [SUB]
  - 121: *Christus* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 119:
i. ABCD: noscibile. 3. E: esse noscibile; ib. ABE: latebris ; C in
rasura: latebre. 4. B: sicut ; ib. BC: ignoraverunt. 8. DE: Ard-
machanus. 10. D: aliam responsionem. i3. D: et deest. 16. DE: sit.
18. AB: apericior. 22. ABCD : alia. 24. C: et sacramentum ; ib. C:
necessarium. 27. D: supra ; ib. D: scienciores ; in marg. : ssuores.
3i. Cf. Petrum Lombardum dist. X, De haeresi aliorum qui
dicunt corpus Christi non esse in altari nisi in signo.

p. 120:
2, 3. Codd.: mencicntcs. 4, 5. E: et sanguinem. 5. B: vel sub-
stanciam. 6. D : ita Jesum. 7. D : dicit. 8, 9. ABC : ibi corpus
esse corpus Christi; D: ibi esse corptis. 10. C: ct — signo docst.
11. E: verbis Domini. 19. ABC: docet ; ib. E: Dcum. 22. ABC: fit.
23. AB: fuit Clvistus. 26. AB : vel a veris. Rectius lcgcndum: vel anus.
3o. D: accipit.

p. 121:
1. CE: vcrba conversiva (vcrba twice) ; lb. AB : foret. 6. AB : dicendum
est decst. 14. 1) : ut deest. 14. ABC : non tamen est. 14, i5. D : non —
signo decst. 18. ABCD: figura. 19. C: spiritualiter. 22. D: figure.
25. ABCE: predictis. 28. CD : signo. 29, 3o. D: coefficaciam.
16. St. Augustini Opp. tom. VI, pag. 21 5.

p. 122:
S. C: commanducaverunt. 10. D: Ardmachano ; E: Ardmacano.
11. ABD: Arimenorum. 17. E: quem deest. 18. anie ; B: Domini.
18—20. C: benediccio — verba in marg. alia manu. 19. C: et deest.
23. cum; D: tantum. 27. C: textus in marg. alia manu. 29. E: eis.
4. Rectius sermone De utilitate agende penitencie Opp.
tom. V. 2. 1864. 11. Armachani, Summa in Quaestionibus
Armenorum, ed. Paris i5ii. i3. Matth. XXVI, 26.

p. 123:
2. A: magister in marg. aliamanu; in textu : Marcus ; ib. D: quanlum
dicit. 6. D: esset falsum. i5. D: corporis ; ib. B: convocat.
17. C: petitur in marg. alia manu. 18. C in marg. alia manu: illius;
in textu deest. 19. B: texto. 20. D: esse differente; ABCE : deferente.
23. ABD : autem dcest. 23, 24 ABD : non occasionaliter ; C: non extinxit.
24. B: humanitus, 26. E: in illa hostia. 3o. D: illis vel.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
(none recorded)
```

---

## Chunk 05-c: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-05-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-05-c
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "123.29–127.14"
divisions: "cap. 5 (heading 'CAPITULUM QUINTUM.' at 115.0); part 3 of 11, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "783 words; 769 confirmed by the vote; 13 runs stood by rule; 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n194–n198 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 5, part 3: [TITLE]

## ¶1 · 123.29–124.19

> [p. 123] Nec credo quod plus excellencie sacramenti huius potest dici ex racionibus vel scriptura. Unde stulte multiplicant quidam argumenta in ista materia quod ad magnificandum Dei potestatem et graciosam pietatem, [p. 124] ac ad augendum nostram meritoriam credendi difficultatem sunt talia ardua ac difficilia credenda de hostia, ut scola hodie dogmatisat quia lex Christi debet esse patens et facilis secundum formam scripture et non difficultata ultra eius limites; ymmo infinitum honorabilius posset credi de hoc sacramento, cum posset credi et baptismatis signis ac logice defendi magis extranee istorum opposita ac magis difficilia; illa ergo propter causas consimiles sunt credenda. Posset enim fingi quod forma substancialis per se sine quantitate vel qualitate supplet officium in hostia cuiuscunque experiencie quam sentimus; quod minus claudicaret a veritate quam hodierna ficticia: ideo ne blasphememus, oportet quod secure teneamus nos in illis limitibus quos sancti ex scriptura sacra posuerant, ne forte ponamus blaspheme Deum auctorisare mendacium, quod non potest; quod creditur fieri in multis quoad hoc sacramentum infundabiliter adinventis.

[ENGLISH]

## ¶2 · 124.20–125.2

> [p. 124] Et si queratur quomodo fundabitur quod panis et vinum remanent hostia consecrata, dicitur (ut sepe superius) quod ad hoc movent sensus et racio sanctorum, doctorum testificacio et fidei scripture informacio. Nam eque certe movet sensus ad credendum ibi esse panem et vinum, sicut movet ad credendum ibi esse quantitatem aut qualitatem, sicut prior est illorum sensitiva noticia. Racio autem videtur triplex: prima quod omnes disposiciones previe requisite ad formas elementi vel mixti sunt posite, sicut et omnes potencie agendi ex quibus naturalis concluderet formas tales, et tercio quod Deus non sine causa necessaria [p. 125] dampnificaret suam universitatem subtrahendo naturam substancie.

[ENGLISH]

## ¶3 · 125.3–125.9

> [p. 125] Triplex autem ponitur testificacio sanctorum secundum dicta superius. Primum est dictum Augustini positum in De Consecracione, distinccione IIª, Qui manducant, ubi sic dicitur: quod videtur panis est, et calix quod oculi renunciant, quod autem fides postulat instruenda, panis est corpus Christi et calix sanguis.

[ENGLISH]

## ¶4 · 125.10–125.14

> [p. 125] Item, eadem distinccione ex dicto Hilarii sic habetur: Corpus Christi quod sumitur de altari figura est, dum panis et vini natura extra videtur: veritas autem, dum corpus et sanguis Christi in veritate interius creditur.

[ENGLISH]

## ¶5 · 125.15–127.14

> [p. 125] Item, sanctus papa Nicholaus cum multis episcopis declarat ut fidem panem et vinum que in altari ponuntur remanere post consecracionem tam sacramentum quam carnem Christi et sanguinem, ut patet distinccione IIª Ego Berengarius. Et ex istis credo diffinicionem Urbani nostri cum suis episcopis tenere antiquam fidem Romane ecclesie, licet Robertus cum suis teneat ficticiam Avinone de transsubstanciacione; nec videtur alter eorum dignus in papam recipi, nisi declarare sciverit istam fidem, cum docere fidem katholicam sit precipuum illorum officium. Unde quidam credunt quod non concordabunt caritative antequam per alterum eorum hoc efficaciter sit edoctum, quia propter huius defectum et ipsi et eorum subditi sunt ydolatre et blasphemi, sic quod de sic errantibus in hiis signis potest dici illud [p. 126] Ysaie Iº, 11: Quo mihi multitudinem victimarum vestrarum? Plenus sum. Et sequitur: Cum extenderitis manus vestras, avertam oculos meos a vobis, et cum multiplicaveritis, oracionem non exaudiam: Quomodo ergo excusabuntur in isto peccato, qui ex officio tenentur in isto docere ecclesiam? Et ex fide scripture videtur quod panis et vinum post benediccionem remaneant sacramentum; nam (ut sepe repecii) quatuor evangeliste narrant quomodo Christus accepit panem et vinum et illa demonstrando dixit: Hoc est corpus meum vel sanguis. Secundo confirmatur ex evangelio Apostoli Iº, Cor. Xº, 14, 16, 17, ubi primo precipit: Fugite ab ydolorum cultura. Et adiungit: Calix benediccionis cui benedicimus nonne communicacio sanguinis Christi est? et panis quem frangimus nonne participacio corporis Domini est? quoniam unus panis et unum corpus multi sumus; ubi manifeste patet quod loquitur de pane et vino materialibus, que post benediccionem sunt hoc sacramentum; et iterum manifestum est quod hic utitur predicacione tropica et non ydemptica, dum intelligit panem et vinum figurare unionem ecclesie cum Christo qui est res huius sacramenti. Et patet quanta cecitate percutitur ecclesia que dimisso evangelio et sanctis doctoribus regulatur per stultam heresim decretistarum, qui tradunt pro regula quod generaliter in hiis dictis per panem et vinum intelliguntur accidencia non substancia vel natura. Numquid credimus sanctum Apostolum intelligere appropriate per panem quem frangimus illa accidencia que nescimus? Nonne beatus Hilarius explicat sensum quod sunt natura panis et [p. 127] vini? Nonne secundum decretum beati Jeronimi illi qui intelligunt scripturam sacram aliter quam Spiritus Sanctus flagitat sunt heretici? Et tam detestanda et iners est glossa quam dant dictis sanctorum; et quando Augustinus dicit superius quod videtur panis est, sed quod creditur panis est corpus Christi, glossant per oppositum; quod videtur non est panis sed accidens per se quod fuit in pane; sed certum est quod tam subtilis logicus, tam profundus methaphisicus et tam prudens theologus non sic oneraret verba fidei tam aliena sentencia, specialiter cum expresse tam crebro asserit quod accidens non potest esse sine subiecto, ut exemplificat de quantitate et qualitate.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 123.29: To ask more belief than this is to raise needless difficulties.
- 124.20: Our senses bear witness of the bread and Wine as surely as of quantity or quality.
- 125.3: Authority of the Saints.
- 125.15: We believe the right faith is in Urban, although Robert at Avignon holds the fiction of transsubstanciation.
- 126.23: The Gospel is set aside now-a-days for the fiction of the decretists.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 126: *11: Quo* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 123:
2. A: magister in marg. aliamanu; in textu : Marcus ; ib. D: quanlum
dicit. 6. D: esset falsum. i5. D: corporis ; ib. B: convocat.
17. C: petitur in marg. alia manu. 18. C in marg. alia manu: illius;
in textu deest. 19. B: texto. 20. D: esse differente; ABCE : deferente.
23. ABD : autem dcest. 23, 24 ABD : non occasionaliter ; C: non extinxit.
24. B: humanitus, 26. E: in illa hostia. 3o. D: illis vel.

p. 124:
i. E: augendi. 4. D: compatcns. 7. E: baptisalis ; ib. AB : logico;
C: correxit; D: logica. 8. opposita ; D : argumenta; E: opposito.
9. E: ille ; ib. C: e>go in marg. alia manu. 14. ideo nc ; B: racione.
18. E: quo dcest. 21, 22. C: hostia — movent in marg. alia manu.
21 — 24. AB: et racio sanctorum — movet sensus twice. 24. D: manet;
ib. ABC: mnvent ; C: corrcxit. 25. D: movet decst. 26, 27. D: istoruvi
sensitiva. 27. E: primo. 3i. E: Deus non deest.

p. 125:
3. D: testimonium. 6. CE: manducat. Q. ABC : est sanguis.
12. ABDE: aut; correxi ; C: deest. i5. AB: multis deest; C in marg.
addit. 19. E: Beringarius ; ib. CE: Et deest. 20. D: nostri deest.
22. D : Avinonie. 23. D : dignus deest. 26. B : concordabant.
6. Decreti Tertia Pars, De Cons., dist. II, cap. LVIII.
11. ib. cap. LXXIX. 19. ib. cap. XLII.

p. 126:
5. B: excusabunt. 6. ABD: Sed ex ; C: Et in rasura. 10. D: ita
demonstrando. 19. AB: post consecracionem benediccionem ; C: con-
secracionem extinxit. 21. ACD : panem illum. 22. ABE: signare.
25. C: regulatur in marg. alia manu. 27. ABCE: intelligunt.
28. C : substanciam vel naturam. 29. B : a proprietate.
2. Is. I, 1 5. 3i. Vide supra pag. 1 25.

p. 127:
3. A: Jlagigat. 4. DE: inhers; ib. B: est deest. 4, 5. D: ut quando.
9. D: tam profundus ; ib. ABDE: logicus. 10. D : auderei. 16. C: prin-
cipia in marg. alia manu. 21. ABC: Gillianensis ; E: Gilbanensis.
22. D: ut deest. 23. C: ecclesie in marg. alia manu. 24. D: in pro-
babiles. 27. C: ignotum correxit in : ignoratum.
1. Decreti Secunda Pars, Causa XXIV, Quaestio III, cap. XXVII.
5. Yide supra pag. 12 5.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
(none recorded)
```

---

## Chunk 05-d: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-05-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-05-d
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "127.15–131.13"
divisions: "cap. 5 (heading 'CAPITULUM QUINTUM.' at 115.0); part 4 of 11, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "855 words; 846 confirmed by the vote; 8 runs stood by rule; 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n198–n202 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 5, part 4: [TITLE]

## ¶1 · 127.15–128.4

> [p. 127] Consolacio itaque contra istos doctores est quod iuxta propria principia non debet credi alicui eorum et specialiter in materia theologica, nisi de quanto se fundaverit (quod non poterit) in hac glossa. Et sic patet quod panis et vinum sunt hoc venerabile sacramentum; verumptamen protestor publice quod, si Robertus Gilbonensis vel quicunque de suis fautoribus doceat contrarium, paratus sum ut fidelis filius ecclesie ad credendum. Sed credo quod Robertus cum omnibus suis complicibus non faciet ita probabiles evidencias ad credendum quod hoc sacramentum non est essencialiter panis aut vinum, sed unum accidens ignotum. Necesse est tamen has hereses esse ad puniendum eos in penam peccati qui phariseice ponderant nimis signa. Exhinc, inquam, occupatur scola circa falsas et vanas ficticias, dimissa doctrina [p. 128] veritatis fidei necessaria ad salutem; et oportet omnino ex hoc consequi contemptum cultus Dei et animum attentum ad cultum dyaboli ad profundacionem infinitam in vanitate signorum seculi.

[ENGLISH]

## ¶2 · 128.5–129.11

> [p. 128] Unde Augustinus libro Sermonum, Sermone LV, promittit narrare populo quid sit hoc sacramentum quod fideles accipiunt: Panis, inquit, iste quem videtis in altari sanctificatus per verbum Dei corpus Christi est. Quod habet calix sanctificatum per verbum Dei sanguis Christi est. Per ista voluit Dominus commendare corpus suum et sanguinem. Si bene accipitis, unus panis, unum corpus multi sumus, sicut exponit Apostolus. Et sic commendatur vobis in isto pane quomodo unitatem diligere debeatis. Numquid enim panis ille de uno grano factus est? ymmo multa erant tritici grana? Sed antequam ad panem venirent, separata erant, per aquam coniuncta sunt et post quandam contricionem. Nisi enim molatur triticum, per aquam conspergatur et per ignem pinsatur, ad formam minime venit que panis vocatur. Sic et vos ante ieiunii humiliacionem exorcismi sacramento quasi molebamini. Accessit baptismum; quasi aqua conspersi estis et igne karitatis constantes, ut ad formam panis veniretis. Nec dubium quin illum panem sic artificiatum quem sanctus doctor dicit esse essencialiter sacramentum mistice manducandum non vocat accidens ignotum sed realiter panem communem verbo Domini consecratum; nec umquam concepit iste vel aliquis ex hoc sanctus quod benediccione et [p. 129] virtute verborum Domini panis consumitur usque ad fundamenta in eo vel corrumpitur secundum se totum sed pocius melioratus remanet figurans nobis secundum proprietates predictas sensum misticum, scilicet allegoricum, anagogicum et moralem. Non enim pinsavit Deus unam pastam monstruosam accidencium per se existencium, ut tam varia in naturis figurent veritatem summe unam, nec epistolatus est aliquis secundum illam fidem in azimis veritatis, sed contra deitatem ac humanitatem Christi in fermento erroris nimis veteri.

[ENGLISH]

## ¶3 · 129.12–130.2

> [p. 129] Deus enim non posset destruere tantam substanciam partem mundi sine recompensacione facta aliunde, nisi iniuste dampnificet quamlibet partem mundi. Sed constat quod illa accidentalis existencia humanitatis Christi in hostia non equivalet bonificacioni quam creatura haberet ex substancia desinente, tum quia Christus tantum benefacit universitati sue, pausando limitate in celo et essendo virtualiter in creatura quam perficit, tum eciam quia blasphema ficcio falsitatis de Deo qui est veritas effugiens ficcionem, perfeccionem accidentalem abstrahit a creatis. Quomodo ergo consonat Deo bono quod sine demerito dampnificet eciam bonos ex subtraccione perfeccionis mundi, de quo antea congaudebat? Sic ergo potest fidelis colligere quod sacramentum eukaristie sit realiter panis et vinum, vel (ut alii intelligunt) sacramentum est unum aggregatum ex illa substancia et corpore Christi (ut innuit Augustinus De Consecracione, distinccione secunda, Hoc est); quod autem aggregatum [p. 130] ex benediccione Domini vel virtute, sic quod nec panis nec vinum in hoc sacramento destruitur.

[ENGLISH]

## ¶4 · 130.3–130.21

> [p. 130] Tercio replicatur per provecciores doctores contra predictam sentenciam. Scribit enim Anshelmus in libro suo De Corpore Christi, quomodo sub forma panis et vini datur nobis tota humanitas Christi, sic quod panis fieret corpus Christi et vinum eius anima, cum sanguis generatus ex vino sit secundum philosophos sedes anime, ymmo cum corpus Christi sit inviolabile et incorruptibile; et videtur quandoque hostiam violare et a soricibus comedi et corrodi. Tollendo istam difficultatem sic loquitur secundum diffiniciones sanctorum patrum: Intelligendum est panem super altare positum per illa sollempnia verba in corpus mutari, nec remanere substanciam panis et vini, speciem tamen intelligendum est remanere, scilicet formam, colorem et saporem, et secundum illa fit attricio, soricis corrosio et multiplex localis mocio, ut in ventrem trahicio, non autem secundum corpus Christi. Es istis videtur hunc sanctum sentire nudum accidens per se remanere, ut dicunt moderni.

[ENGLISH]

## ¶5 · 130.22–131.13

> [p. 130] Sed pro isto notandum quod Anshelmus et alii sancti laboraverant non ad honorem illius signi sed ad veneracionem corporis Christi signati et sic Christi; et sic nitebantur quod quidditas substancie signantis sopiatur quoad consideracionem hominis, et tota devota intencio coiligatur in Christum, ad quod per se movent signa per se sensibilia et non sic materialis substancia. Sic enim in presencia maioris vel preponderacioris obiecti sopitur appreciacio inferioris, ut patet de elementis inmixtis que multi propter latenciam [p. 131] ponunt non esse; de frigore latente in ferro candente et omnino de litteris quarum essencias et figuram clericus non attendit, cum hoc sit officium idiote, avis vel bestie; sed quantum potest consideracione tali suspensa respicit ad signatum. Sic facit fidelis quoad signum sacramentale et suum signatum; et sic conceduntur ille materiales essencie post consecracionem a quibusdam minus bene intelligentibus simpliciter nusquam esse, decretiste vero dicunt quod panis et vinum remanent, sed nescitur ubi sunt. Sed tercii dicunt quod convertuntur in corpus Christi et sanguinem; quod potest tam bene quam male intelligi.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 127.15: I will believe with Robert of Geneva if he will prove his belief.
- 128.5: Augustine's teaching.
- 129.12: God could not injure the world by such destruction of substance.
- 130.3: Anselm quoted against us, who says that what the mice eat is only the appearance.
- 130.22: He means that we need not regard the bread and wine.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 127: *scola* (print = bt) [SUB]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Augustine's teaching. . . .... (128.5).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 127:
3. A: Jlagigat. 4. DE: inhers; ib. B: est deest. 4, 5. D: ut quando.
9. D: tam profundus ; ib. ABDE: logicus. 10. D : auderei. 16. C: prin-
cipia in marg. alia manu. 21. ABC: Gillianensis ; E: Gilbanensis.
22. D: ut deest. 23. C: ecclesie in marg. alia manu. 24. D: in pro-
babiles. 27. C: ignotum correxit in : ignoratum.
1. Decreti Secunda Pars, Causa XXIV, Quaestio III, cap. XXVII.
5. Yide supra pag. 12 5.

p. 128:
10, 11. A: communkare in marg. ; in textu: commendare; BCD : com-
municare. n. ABDE: Si unde ; C correxit: bene. 14. E: veritatem;
ib. AB : enim deest; C in marg. addit alia manu. 16. A: tercie grana,
20. E: nos. 21. Recte: humiliacione. Cf. August. I. c. 22. C: accessit
in textu; in marg. alia manu: sistis (accessistis) ; ib. ABCE: et quasi.
5. St. Augustini Sermo CCXXVII, In die Pasche IV, Ad In-
tantes de Sacram., Opp. tom. V, 973. CJ. et 1 io3. Decreti Tertia
Pars, dist. II, cap. XXXVI.

p. 129:
1. C: verborum Domini in marg. alia manu. 2. D: fundamentum.
3. D: pocius deest; ib. ABDE: melioratur. 5. C: anagogicum in
marg. alia manu; ib. C: pinsuit. 9. B: istam. 10. D: humilitatem.
19. C: limitate deest. 23. E: quin sine. 25*. E: anteea; ib. B : Sicut.
27, 28. B: vel ut — unum deest. 28— 3o. ABCE: ex illa — aggregatum
29. Decreti Tertia Pars, De Cons. dist II, cap. XLVIII.

p. 130:
7. E: figurat; D: figuret. 8. D : fit. n. E: violari et corrodi.
19. E: et in rentrem. 21. ABC: manere. 23. C: laboraverunt.
29. ABC: Similiter; D: Sic.
4. Sancti Anselmi Epistolarum Lib. IV, Ep. CVII. De Corp.
Christi, pag. 462, 453.

p. 131:
3. ABC : sit hoc sic; ib. ABE: officium iante; C corr. : idiote.
6. D : et ad. 8. B: bene deest. q. B: et decretiste. 16, 17. D: mem-
brorum. 17. AB : figuram; C correxit. 21. ABCD : sensibilem.
23. C: in in marg. alia manu. 24. E: sic. 25. DE: esse deest;
ib C: pereunte in marg. ; in textu : perempto. 3o. C: a signo.
24. Sancti Anselmi Dial. De veritate pag. 114 (ed. Gerberon).
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
(none recorded)
```
