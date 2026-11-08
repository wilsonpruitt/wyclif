# Translation brief: eucharistia 05-k–06-b

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/eucharistia/wyc-eucharistia-05-k.md chunks/eucharistia/wyc-eucharistia-06-a.md chunks/eucharistia/wyc-eucharistia-06-b.md` once and fix what it reports.
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

## Glossary (the 486 rows these chunks use; the full file is GLOSSARY.md)

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
| presciencia | foreknowledge | |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| orator | CONTEXTUAL: bedesman / advocate / suppliant | Plural *oratores* "bedesmen" (Dialogus ruling); of one who pleads the church's cause (*orator ecclesie*, *Eccl.* 165.25, 166.4) "advocate", with a **C** note. Ruled 2026-10-02. Of one who prays to God himself (*devotus Dei orator*, *Pot. pape* 68.17) "suppliant", with a **C** note; ruled 2026-10-07. |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |
| sacramentum (the eucharist); sacramentum altaris | sacrament; the sacrament of the altar | The plain sense, against the Augustinian row (*Incarn.*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.3, 3.30). |
| hostia; hostia consecrata | host; consecrated host | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.11, 1.22). |
| panis / vinum | bread / wine | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.8). |
| corpus Christi / corpus Domini | the body of Christ / the body of the Lord | Kept apart as the Latin alternates them. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.6, 1.10). |
| novella ecclesia / antiqua ecclesia | the newer church / the ancient church | The pair of 3.3; cf. *novelli*. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 3.3). |
| cultores accidencium / signorum | worshippers of accidents / of signs | Wyclif's name for the defenders of the accident without a subject. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 6.15, prol-c 10.2). |
| missantes | mass-priests | Priests hired to say masses; pejorative. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 15.25). |
| pontifex (a Christian bishop, unqualified) | pontiff | As the Old Testament row; where the referent (a bishop) matters, an R note. *pontifices ydolorum* "pontiffs of idols". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 14.29, 15.17). |
| species (of bread and wine) | species | The sacramental species; kept as the term, not "appearance". Distinct from the logical *species*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 13.15; 23.8). |
| sacer; sacrare | sacred; hallow | Kept apart from *sanctus / sanctificare* "holy / sanctify" and from *consecrare*; *consecrare* is "to hallow together" in the grammarians' etymology. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 27–28). |
| sacramentum tantum | a sacrament only | The *sacramentum tantum* of the Lombard's three (IV d. 8 c. 4). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 29.23). |
| conversio (eucharistic) | conversion | Of bread into the body; kept apart from *conversio* of a proposition. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 48.15). |
| decretalis | decretal | Kept apart from *decretum* "decree". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 71.31). |
| transaccidentacio | transaccidentation | Wyclif's coinage beside *transsubstanciacio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 81.27). |
| transinferioracio; transsubieccio | transinferioration; transsubjection | Coinages in the same series. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 82.3). |
| baptiste signorum | baptizers of the signs | Not "Baptists". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 81.29). |
| divinitus | divinely | The pair of *humanitus* "humanly". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 84.19). |
| accepcio personarum | respect of persons | The Douay phrase. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 92.15). |
| consecracio | consecration | The noun of *consecrare*; see *confeccio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 99–100). |
| curia Avinonica | the Avignon curia | Beside *curia romana*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 107). |
| commenta scripture | commentaries on scripture | Kept apart from *commentum (mendacii)* "fabrication". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 116.28). |
| pseudofrater; pseudofratres | false friar; false friars | Kept apart from *pseudomonachus* "false monk". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 139.13). |
| transaccidencia | transaccidents | In the *transaccidentacio* series. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 145.4). |

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
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| temporalia | temporal goods | |
| prelatus | prelate | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| oratores | bedesmen | Those bound or paid to pray for a benefactor; Pollard's side-note word. Not "those who pray". Ruled 2026-09-28 (5 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| conducentes | those who hire them | Ruled 2026-09-28. |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| vulgares | the common people | The third estate. Not "the vulgar". Pilot. |
| protestacio; protestari | declaration; to declare solemnly | ⭐ The submission formula ("if anyone can teach me this is contrary to scripture or reason, I will humbly retract"). Penn and Lahey both inverted it (T. pp. 369, 378). Render it as a retraction offer, never as defiance. |
| curia romana | the Roman curia | Ruled 2026-09-28 (*Dial.* 7.8; 5 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | CONTEXTUAL: condition / respect | "Condition": a person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). "Respect": the logical relation under which a predicate holds (*posiciones secundum habitudinem*), with a **C** note; ruled 2026-10-22 (Wilson; *Incarn.* 4.16). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| decretum; decreta | decree; the decrees | Gratian (*in decretis*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.14, 3.24). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
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
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| ingratitudo | ingratitude | Toward a person. Ruled 2026-10-02 (156.8). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| humanitas | the humanity | The nature the Word assumed, body and soul; with the article (*humanitas sit Christus*, "the humanity is Christ"). Not "the human nature", which is *natura humana*. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| dimittere / dimissio (*naturam*) | lay aside / the laying-aside | Letting go the assumed nature, so the union would be dissolved. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 2.23). |
| homo assumptus | the assumed man | A term of art (the Lombard's first opinion, *Sent.* III d. 6); keep "assumed" before "man", never "the man assumed". With the agent expressed (*homo assumptus a Verbo*) "the man assumed by the Word", which cannot be misread (coordinator, 2026-10-22). Ruled 2026-10-22 (Wilson; *Incarn.* 5.15). |
| secundum quod (reduplicative) | insofar as | ⛔ Never "in that" (heard as "because", which inverts the logic). Ruled 2026-10-22 (Wilson; *Incarn.* 5.29–6.24). |
| secundum deitatem / secundum humanitatem | as to the Godhead / as to the humanity | The rule of reduplication; keep it in Wyclif's place in the sentence. ⛔ Never supply "as God / as man" where the Latin has bare apposition (*ipse Deus*) or bare predication. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| natura | nature | Ruled 2026-10-22 (Wilson; *Incarn.* 3.4). |
| persona | person | Ruled 2026-10-22 (Wilson; *Incarn.* 4.14). |
| posicio / proposicio / predicacio | position / proposition / predication | Kept apart: the apparatus shows the three trading places (*Incarn.* 4.15). Ruled 2026-10-22 (Wilson). |
| verificari (de) | be true (of) | The logicians' sense; not "verified" (modern "checked"). Ruled 2026-10-22 (Wilson; *Incarn.* 7.6). |
| sacramentum (of the incarnation, of creation) | sacrament | The Augustinian sense, "mystery" (1 Tim. 3:16): G note at the first occurrence in the chunk. Kept apart from *misterium*. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.8). |
| sancti | the saints | The fathers. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.15). |
| probabiles doctores | reputable doctors | *Probabilis*: worthy of credence (cf. *probabiliter*). Ruled 2026-10-22 (Wilson; *Incarn.* 7.1) as "approved doctors"; changed the same day (coordinator) to free "approved" for *approbati*. |
| approbati doctores | approved doctors | Kept apart from *probabiles doctores*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 13.3). |
| Sermo (beside *Verbum*) | Speech | The divine title, capitalised; *Verbum* stays "the Word". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 16–17). |
| de vi vocis / de vi sermonis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| protervus | obstinate | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| gracia unionis | the grace of union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| exinanicio / exinanire / inanicio | emptying / empty | Phil. 2:7 (Douay "emptied himself"); *inanicio* (*Incarn.* 33) the same. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| humanitus | humanly | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* passim). |
| suscipere / suscepcio (of the soul, the nature) | take up / taking-up | Kept apart from *assumere* "assume". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 31). |
| suppositum | supposit | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 34.24). |
| machina (*mundi*) | frame | "The frame of the world". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 35.1). |
| in quantum (reduplicative) | insofar as | As *secundum quod*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37.9). |
| universitas creaturarum | the totality of creatures | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37). |
| dos immortalitatis | dower of immortality | Of the glorified body. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 46.24). |
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
| ampliativus | ampliative | Beside *ampliacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 57.29). |
| passio (against *accio*) | being-acted-on | The category; G note at the first occurrence in a chunk. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 60.13). |
| supposibilis | that can be supposited | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 64.14). |
| proditor | the traitor | Judas. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 64.3). |
| dampnificare / dampnificacio | damage / damaging | Kept apart from *dampnum* "loss" and *dampnari* "be damned"; the argument of 65–68 turns on it. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 65). |
| per se / per accidens | CONTEXTUAL: of itself / by accident; (spatial) apart, by itself | The spatial sense (a thing set apart, *Euch.* 104.16–17) gets a G note. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a (sufficienti) divisione | the topic from sufficient likeness / from (sufficient) division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| pretericio | being past | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| solvere / solucio (of the union) | loose / loosing | Except inside a Douay quotation (John 10:35 "cannot be broken"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| libere contradictorie | freely, as between contradictories | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 76.15). |
| peccabilis | able to sin | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| passionatus | subject to passion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| capitales doctores | the chief doctors | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| eiusdem / consimilis / alterius racionis | of the same / like / another kind | The species-sense of *racio*; *racio speciei* "the account of the species" (Aristotle's *logos*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.4, 87.17). |
| univocacio | univocation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.27). |
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
| universitas creata | the created totality | Beside *universitas creaturarum*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| significatum | significate | Kept apart from *signatum* "thing signified". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 111). |
| sermo vocalis | the spoken word | Against *Sermo* "Speech", the divine title. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 113). |
| predicacio secundum essenciam / formalis | predication by essence / formal predication | Wyclif's modes of predication (cf. *predicacio secundum causam*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 115–116). |
| forma substancialis | substantial form | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| concepcio (figure) | conception | The grammatical figure. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habitus (of the humanity) | habit | The Lombard's third opinion (*Sent.* III d. 6). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| accidens | accident | The category; *accidit* "befalls". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habitacio | habitation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 120.14). |
| figura / figuratum | figure / thing figured | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 121.23). |
| conversio (of a proposition) | conversion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.30). |
| humanitacio | humanation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 126.12). |
| racio (individual, personal) | account | *Racio individui / persone* "the account of an individual / a person", as *racio speciei*; not "aspect" (the row against *substancia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 8, 129–132). |
| vir (against *homo*) | man (*vir*) | Where Wyclif sets *vir* against *homo*, the Latin in parentheses. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 129.15–26). |
| univocare / univocari | make univocal / be univocal | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 131.3). |
| res secunde intencionis | things of second intention | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.25). |
| materia proxima / remota | proximate / remote matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137.1). |
| personari | be made a person | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 134.10). |
| res communis / res communes | the common thing / common things | The realist universal the *moderni* do not conceive (first root of their error). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 144.27). |
| distinccio racionis | distinction of reason | Beside *differencia formalis*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 145.23). |
| conversio naturarum / confusio naturarum | conversion of the natures / confusion of the natures | Kept apart from *conversio* of a proposition. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 143.9). |
| supposicio simplex / supposicio personalis | simple supposition / personal supposition | Supposition theory. *Simpliciter / personaliter supponere* "stand with simple / personal supposition": NOT the *simpliciter / secundum quid* pair, C note where the two could be confused. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 152.5–12). |
| transsumpcio | transumption | Beside *transsumptive*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 153.28). |
| personalitas | personality | The scholastic term: what makes a person a person, not character. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 155). |
| nativitas | nativity | Christ's twofold birth. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 155). |
| in quid (predicari in quid) | in quid | Kept in Latin (predication of what a thing is, as against *in quale*), glossed at first use in a chunk. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 162.22). |
| suppositari | be supposited | Verb beside *suppositum*, *suppositacio*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 161). |
| dependencia actualis / potencialis / obediencialis | actual dependence / potential dependence / obediential dependence | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 161.23–162.4). |
| substancia prima / substancia secunda | first substance / second substance | Aristotle, *Cat.* 5. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.25). |
| a simili | by likeness | Bare, as an argument form; beside *locus a simili* "the topic from likeness". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.16). |
| racio substancialis | substantial account | As *racio individui* "account". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.21). |
| doctores signorum | the doctors of signs | The logicians who reason from terms, not things. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.26). |
| sensibilis (in the definition of animal) | sentient | *Substancia animata sensibilis*: able to sense. Elsewhere the §D row "perceptible" holds; G note at first use. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 177). |
| suppositalis | of a supposit | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 176). |
| accidens absolutum | absolute accident | Quantity and quality, against relative accidents. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 176). |
| passionaliter | as an attribute | Beside *passio* (the proper attribute). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 181). |
| posicio anime | the laying-down of the soul | John 10:17–18; not the logical *posicio* "position", C note. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 183.3). |
| causancia / causacio | causing / causation | Kept apart (both at 187.30–34). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 185.16). |
| personare (active) / personacio | make a person / personation | Beside the passive *personari* "be made a person". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 188.16, 188.32). |
| vicem supplere / vicis supplecio | supply the place / the supplying of a place | God supplying the place of a second cause. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 187.26). |
| transsubstanciacio | transubstantiation | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.10). |
| multiplicative | multiplicatively | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 193.20). |
| habitudo relativa | relative respect | The "respect" sense of the CONTEXTUAL *habitudo* row. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 193.19). |
| remitti / intendi (of a quality, merit) | be remitted / be intensified | The intension and remission of forms; not *remissio* of sin. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 197.1–7). |
| in divinis | among the divine [persons] | Keeps "Godhead" for *deitas*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 196.18). |
| universitas creabilis | the creatable totality | Beside *universitas creaturarum* "the totality of creatures". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 199.5). |
| multiplicacio dimensionalis | dimensional multiplication | One body in several places by its dimensions. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.6). |
| habitus (= possession, *habere*) | the having | The category of having, C note; kept apart from *habitus* "habit". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.14). |
| a maiori vel pari | from the greater or from the equal | Arguments *a maiori*; cf. *locus a maiori*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 209.5). |
| sensibile commune | common sensible | Aristotle's common sensibles (number, motion, figure); the term of art, against the §D row "perceptible". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 209.23). |
| communioritas | greater commonness | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 210.15). |
| multiplicacio concomitancie | multiplication of concomitance | Cf. *gracia concomitancie*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 213.21). |
| nomen appellativum | appellative name | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 213.29). |
| imposicio primaria | primary imposition | Of a term's first assignment to signify. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 214). |
| assertibile | assertible | The thing a proposition asserts. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 215). |
| superioritas / inferioritas terminorum | superiority / inferiority of terms | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 215). |
| exponentes | the exponents | The propositions into which a proposition is resolved (expounded). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 216.14). |
| homo communis | the common man | The universal man, with *res communis*; not "the ordinary man". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 218.3). |
| congruencia | fittingness | The reasons of fittingness for the Son's incarnation. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 225.6). |
| signum reduplicatum | the reduplicated sign | The reduplicative word (*secundum quod*, *in quantum*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 230.23). |
| supposicio | supposition | Of a term (supposition theory) or of a premiss laid down (cf. *supponitur* "it is supposed"); the English word serves both, C note where it matters. Kept apart from *suppositacio* "suppositation". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 102.8). |
| univocus | univocal | Beside *univoce*, *univocare*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 102.13). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |
| infirmitas (of Christ's flesh) | weakness | Ruled 2026-10-22 (Wilson; *Incarn.* 5.31–6.11). |
| sacramentaliter | sacramentally | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| vere | truly | A mode adverb: one word each, never two merged, kept where Wyclif puts it. ⛔ Never "really" (that is *realiter*). Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| spiritualiter | spiritually | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| virtualiter | virtually | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| figurative | figuratively | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| sensibiliter | perceptibly | A mode adverb: one word each, never two merged, kept where Wyclif puts it. As *sensibilis* "perceptible". Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| corporaliter | bodily | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| substancialiter | substantially | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
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
| confeccio | consecration (of the eucharist) | The noun of *conficere*, which already shares "consecrate" with *consecrare*. Where set against *consecracio* (as the verbs at 16.10), "confecting", following Wilson's "confect" (2026-11-07). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 4.4). |
| Doctor Communis | the Common Doctor | Thomas; with *Doctor Subtilis*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 8.16). |
| multitudo (of one body) | multitude | Of one body's being many (ch. 8); the plain "multitude" of persons needs no row. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 8.4). |
| figurare | figure | Both senses: to prefigure (the lamb figured Christ) and to shape (*figurare Deum nostrum*), which Wyclif plays on; one English word keeps the pun. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-c 10; 21.29). |
| supponere pro | stand for | Supposition; with *supposicio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 24.27). |
| sentire (an opinion: sensit quod) | hold | Of a doctor's or church's opinion; the "perceive" row is the sacrament sensed. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 30.30, 31.18). |
| predicacio figurativa | figurative predication | A synonym of *predicacio tropica*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 35.18). |
| veraciter | verily | Kept apart from *vere* "truly"; *Firmiter*'s word. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 48.3). |
| elicere | elicit | Of an act of will or judgement. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 44.5). |
| aliquitas | somethingness | Being a something (*aliquid*). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 60.27). |
| informacio; informare | informing; inform | Of a form in its subject; not "information". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 64.13). |
| accidens predicamentale | accident of the categories | Kept apart from the predicable *accidens*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 64.1). |
| contiguacio | contiguity | Beside *continuacio* (of bodies) "continuation". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 68.12). |
| veritas predicamentalis | truth of the categories | As *accidens predicamentale* "accident of the categories". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 69.2). |
| esse situale / intencionale / potenciale | situal / intentional / potential being | The modes of the body's being. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 84.8 ff.). |
| interpolatus; interpolacio | interrupted; interruption | Of words spoken with pauses. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 89.4, 89.18). |
| quintimembris | fivefold | Cf. *trimembris*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 91.11). |
| pertinenter | fittingly | Kept apart from *convenienter*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-e, 04-f). |
| noticia confusa / distincta | indistinct / distinct knowledge | As *confuse / confusus* "indistinct(ly)". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-g). |
| opinative | as an opinion | Kept apart from *opinio* "opinion" (noun). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-g). |
| suscipere magis et minus | admit of more and less | Aristotle's test of a quality. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 113.32). |
| questio si est / quid est | the question whether it is / what it is | *Post. An.* II.1. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 119.18). |
| dogmatisare | teach as dogma | Of the *moderni*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 120.13, 124.2). |
| universitas sua (God's) | his universe | Beside *universitas creaturarum* "the totality of creatures". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 124.31, 129.16). |
| mistice | mystically | A mode adverb, one word; kept apart from *figurative*, *tropice*, *sacramentaliter*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 128.24). |
| figuracio | figuration | Beside *figura / figurare*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 131.16). |
| naturalitas obediencialis | obediential naturalness | Cf. *dependencia obediencialis*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.15–18). |
| accidentalitas | accidentality | Beside *substancialitas*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.13). |
| quantitas successiva | successive quantity | Time and motion, against permanent quantity. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.1). |
| corpus mathematicum | mathematical body | The three dimensions without matter. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 142.31). |
| ubi; ubicans | where; that which gives a where | The category of place and its cause. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 146.23–24). |
| inpossibilitare | make out as impossible | Of the *moderni*'s argument. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 149.13). |
| conversivus | converting | As *verba sacramentalia conversiva*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 153.6, 153.25). |
| pertinencior | more fitting | The comparative of *pertinens*; cf. *pertinenter*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 153.8). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| cautela | wile | Not "caution"; *cautela diaboli*, the devil's wile. Ruled 2026-09-28 (8 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| ingratus | displeasing (to God) | *Ingratus deo*: unpleasing to God. "Ungrateful" only where a person is ungrateful to someone. Ruled 2026-09-28 (5 sites). |
| globus | band | Derogatory collective (*globus reprobus*, *globos claustralium*). Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of things (*globus temporalium*): "mass", untagged with a note (2026-10-02). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office; *quale magisterium* "what a feat of mastery" (*Incarn.* 137.14) | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| sciolus | knowing, wise | "smatterer" (the classical sense). Neutral in Wyclif. Pilot (*Eccl.* 5.8) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| detegere | to expose | "wipe away" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| pseudomonachus | false monk | Kept apart from *pseudofrater* if it appears. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). Inside a DR quotation of Titus 1:7, DR's "steward" (2026-10-08). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| redempcio temporalium | redemption of the temporal goods | Chapters buying back seized goods. Ruled 2026-10-02 (*Eccl.* 15, 340.15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| redempcio (of a sentence) | redemption | Buying off a penalty; kept apart from *redempcio temporalium*. C note at first use. Ruled 2026-10-02 (*Eccl.* 15, 352.1). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| pseudoprepositi | false superiors | Ruled 2026-10-02 (*Eccl.* 15, 358.24). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| dotes (docium) beatorum; dotes corporis | the dowries of the blessed; the dowries of the body | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
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
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| pseudocardinales | pseudo-cardinals | Ruled 2026-10-02 (*Eccl.* 18, 426.32). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| continuacio (of bodies, the act) / discontinuacio; continuare / discontinuare | continuation / discontinuation; make continuous / make discontinuous | The making of several bodies into one continuum (*Incarn.* ch. 12), G note at first use: not "carrying on". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.30, 211.12). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| habilis / habilitas; habilitare | qualified / qualification; to qualify | The positive of *inhabilis* "unqualified". Ruled 2026-10-02 (*Eccl.* 19, 469.4). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
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
| pseudoclerici | false clerics | Cf. *pseudomonachus*. Ruled 2026-10-02 (*Eccl.* 21, 511.17). |
| univoce | univocally | Ruled 2026-10-02 (*Eccl.* 21, 514.4). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| memoriale | memorial | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| copia / habundancia | plenty / abundance | Ruled 2026-10-02 (*Eccl.* 23, 553.15, 555.20). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| palliacio; palliare | cloaking; to cloak | Ruled 2026-10-02 (*Eccl.* 23, 566.27). |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| pseudochristus | false christ | Matt. 24:24 (DR "false Christs"). Ruled 2026-10-07 (*Pot. pape* 28.32). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). Beside *consecrare* (*consecrat et conficit*) "confect", so the pair stays two. Ruled 2026-11-07 (Wilson, "confect works"; *Euch.* 16.10). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| procuratoria potestas | proctorial power | From *procurator* "proctor". Ruled 2026-10-07 (*Pot. pape* 63.9). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| preeminencia | preeminence | Kept apart from *primatus* "primacy". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| Pseudo (as a noun) | the Pseudo | Wyclif's name for the false pope of the eleven conditions (ch. 6). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-e). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| regulariter | as a rule | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 165.2). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| sessiva / sesina | seisin | *Sesina* the spelling at *Incarn.* 33. So the manuscripts (Loserth 170.8, *ita cod.*); feudal possession that perfects a title. Ruled 2026-10-08 (coordinator, delegated). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| pseudopapa | pseudo-pope | Cf. *pseudocardinales*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 180.33). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| connexio | conditional (proposition) | Logic: the "if … then" proposition. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 189.1). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| memorativa potencia | memorative power | A faculty of the soul (the "power" sense of *potencia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 219.27). |
| discrasia | distemper | Physicians' term. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 223.1). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| preponderancia; dispensacio | preponderance; dispensation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 266.11, 268.4). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| precellencia | pre-excellence | Kept apart from *preeminencia* "preeminence". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 274.33). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| pontifex (Old Testament, unqualified) | pontiff | Kept apart from *sacerdos* "priest"; *summus pontifex* of the Jewish priesthood is "high priest" (see *summi pontifices*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* ch. 11). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| precellenter | pre-excellently | Adverb beside *precellencia* "pre-excellence". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 291.2). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| inhabilitas | lack of qualification | Beside *inhabilis* "unqualified". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 316.9). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| pallium privilegii | cloak of privilege | Kept apart from *palliacio* "cloaking". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-a). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| pseudopontifices | false pontiffs | Cf. *pseudoclerici*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 335.1). |
| procuratorium | proctor's mandate | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 336.11). |
| evangelizans | preacher of the gospel | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-g). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| provisio (papal) | provision | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* ch. 12). |
| involucrum | wrapping | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 357.9). |
| inhabilitare | disqualify | Beside *inhabilis* "unqualified", *inhabilitas*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.4). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| refrigescentia arma | arms that grow cold | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 388.29). |
| specularis prudencia | the prudence of a watchman | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| precellere | excel | Verb beside *precellencia* "pre-excellence"; not "pre-excel". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 399.28). |
| cesaree (adv.) | in caesarean fashion | After *papa cesareus*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 403.25). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |
| nimis | exceedingly | Medieval intensive (= *valde*); "too much" only where excess is the point. Ruled 2026-10-12 (close-out R2; *Pot. pape* 169.2). |
| sentire (the sacrament, the body) | perceive | "sense". As *sensibilis* "perceptible". Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.10, 1.17). |
| recitare | recite | To report, rehearse. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.4, 3.10, 4.18). |
| ex tibi dubio; ex sibi dubio | for all you know; for all he knows | Idiom: not "from doubt". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 66.15, 70.25). |

---

## Chunk 05-k: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-05-k.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-05-k
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "155.16–158.10"
divisions: "cap. 5 (heading 'CAPITULUM QUINTUM.' at 115.0); part 11 of 11, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "635 words; 623 confirmed by the vote; 12 runs stood by rule; 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n226–n229 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 5, part 11: [TITLE]

## ¶1 · 155.16–157.14

> [p. 155] Hic dicitur quod multi sunt heretici, aliqui cogniti et aliqui ignoti, omnes enim presciti sunt heretici, sed aliqui sunt heretici in actu et alii in habitu, licet sint in gracia secundum presentem iusticiam. Aliqui eciam sunt heretici ad tempus solum secundum presentem iusticiam ut predestinati in mortali, et sic de multis divisionibus cum suis declaracionibus quas hic suppono, sed notum est quod stat multos homines tenere sentenciam hereticam sine hoc quod ipsi sint tunc heretici, quia multi opinative vel condicionaliter tenent multas sentencias parati ad revocandum docto opposito; et certum est quod nulli tales sunt ut sic heretici, quia tunc Doctor Communis fuisset nimis crebro hereticus. Unde videtur quod illi dogmatisantes qui deficientibus argumentis defamant universitatem in vulgari propter dicta scolastica et sanctorum sentencias sint publice puniendi; hoc autem optarem, [p. 156] cum ipsi sint manifeste heretici nisi probaverint quod divulgant aut quod non accipiant dignitatem in Oxonia antequam docuerint heresim quam imponunt; nam de natura accusacionis heretice est quod accusator obligat se ut sic ad penam talionis, cum credit katholicum eius contradictorium quod inpugnat; et idem est iudicium de toto capitulo quod consentit. Sic ergo multi sancti preterierunt istum articulum de sacris accidentibus tamquam fidei contrarium a nullis sciolis sui temporis attemptatum, ut patet de antiquis sanctis doctoribus. Et videtur quod ecclesia Avinonica ponens transsubstanciacionem non exhinc implicat substanciam panis destrui vel corrumpi. Sed conformiter ad antiquum decretum Romane ecclesie permittit panis substanciam remanere; unum tamen credo quod quicunque pertinaciter crediderit quod non remanent panis et vinum in hostia consecrata, sed quod ipsa est globus sacrorum accidencium sine subiecto, est manifeste hereticus a qualibet universitate fidelium expellendus. Contradicit eciam fidei quam magnus Augustinus confessus est cum Romana ecclesia. Nec usque hodie scivit fidelis vel infidelis inpugnare istam sentenciam Augustini. Sentencia autem ista que sancto Thome ascribitur est tam infirma et debilis quod nemo scit illam defendere vel probare; et credo quod non fient efficaciores argucie ad hereticandum predictam Augustini sentenciam quam in nomine Communis Doctoris recitate et patule sunt solute. Non enim consonat fidei Christi, quod vel sine causa aut ordine accusetur persona de heresi, vel quod eatur ad curiam mendaciter procurando katholicacionem [p. 157] omnium que scripsit sanctus Thomas. Primum non quia in hoc differt secta Machometi a secta Christi quod hic pseudo legem suam iubet defendi non racione sed gladio; Christus autem mandat in Petro quod de omni fide sua debent discipuli eius discrete, modeste et pacifice reddere racionem. Scarioth autem excitatus a dyabolo accepit cohortem et ministros pontificum, sed caute in tenebra, ut deprimeret veritatem, ut patet Joh. XVIIIᵒ, 3, sed pseudo Scariotis discipuli agitati a demonio meridiano publice in sermonibus incitant populum in vulgari, ut destruant tamquam hereticos simplices discipulos veritatis. Nec mirum quia eodem spiritu in fratres proprios tanquam Roberti discipuli magis callide machinantur.

[ENGLISH]

## ¶2 · 157.15–158.10

> [p. 157] Quantum ad secundum patet quod multe sentencie heretice sunt scriptis sancti Thome imposite; patet quod idem foret in tali involucro approbare totam sentenciam sancti Thome et in equivocacionem tocius evangelii et fidei katholice inducere dogmata Antichristi. Inponitur enim sibi Secunda Secunde, questione LXVII, articulo IIᵒ, quod asserit iudicem debere sentenciare secundum allegata et probata, licet sciverit illa esse falsa et iudicio divino contraria, quod est manifeste hereticum, pallians Pylati iudicium contra Christum. Ideo idem foret defendere istam sentenciam et defendere quod propter tradiciones humanas licet peccando facere contra Deum. Cum ergo beatus Augustinus et alii sancti doctores qui plus sciverunt quam mille tales doctores nunquam vendicarunt sed [p. 158] reprobarunt quod credatur de eis si hoc asserunt, ergo verum, qua fronte vendicarent fratres viciantes sic scripta Thome si ipse sic asserit, ergo verum? Nam Doctor Subtilis cui plus credendum est in speculacionibus quam sibi in pluribus plane detegit errores quos seminat. Cum ergo plane infirmate sunt raciones predicte, facile est tollere alias fiendas contra sentenciam Augustini et Romane ecclesie. Non ergo sequitur: Si Thomas hoc asserit, ergo hoc est populo predicandum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 155.16: A man may hold an heretical opinion without being a heretic.
- 156.21: Augustine is on our side and is of much more weight than a saying ascribed to St. Thomas;
- 157.15: to whom many heretical opinions are ascribed.

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference 2 5. F. Cor. V, 8. (158.31).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 155:
8. E: videlur sequi ; ib. D: ex istis. io. B : el quod. 10—12. C:
papa — religiosorum in inferiori marg. alia manu. 14. Uli; B: ibi.
17. AC: et alii. 18. E: et deest. 20. ABD : solum deesl; C in marg.
addit. 24. E: sunt. 28. D: fierct.
28. Doctor Communis, i. e. Thomas Aquinas.

p. 156:
[. ABCE: heretici aut; ib. ABC: probaverunt. 2. ABDE: aut dccst.
3. D: docucrant. 4. ABD : accionis ; C in marg. correxit. 8. sancti ;
AB: sunt. 10. E: suis tcmporibus. 19. E: maxime hereticus ; ib. C:
fidelium in marg. alia manu. 20. CD : contradicit enim. 24, 25. D: quam
nemo. 2(">. D : fiercnt. 26, 27. E: ad inpugnandum predictam Augwtini
sancti. 28. E: recilative ; ib. A: sunt solute in marg. alia manu.

p. 157:
1. E: scripserit. 4. D: de Petro. 5. E: omni dcost. 10 ABC:
publico. 11. D: concitant. 16— 18. C: imposite — Tliome in marg. alia
manu. 18. D: ennmeracionem. 21. DE: asserat. 23. divino ;
AD: omnino ; B: correxit in marg. ; A in marg. alia manu alias divino.
29. ABCD: doctores deest; ib. ABC: vendicaverunt.
21. Divi Thomae Aquinatis Summa theol. (ed. Venet. 1774),
tom. III, pag. 291, Art. II: Utrum iudici liceat iudicare contra
veritatem quam novit.

p. 158:
1. 13: probaveruttt; ib. C: asseruunt. 2. Codd.: vicinantes.
7. C: alias in marg. alia manu; \b.fiendas ; rcctius: ficticias. 19. C: virtus
et Dei supra lin. script. 23. D: ad conversacionem. 24. AB: quidem.
3i. I ) : recipiendum.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
(none recorded)
```

---

## Chunk 06-a: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-06-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-06-a
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "158.12–161.13"
divisions: "cap. 6 (heading 'CAPITULUM SEXTUM.' at 158.0); part 1 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "670 words; 661 confirmed by the vote; 5 runs stood by rule; 4 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n229–n232 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 6, part 1: [TITLE]

## ¶1 · 158.12–158.31

> [p. 158] Sed dimissa ista contenciosa materia superest videre (ut tactum est superius) quomodo christianus debet disponi ad ministrandum et recipiendum hoc sacramentum. Iste enim foret fructus tractatus scolastici istius materie quoad dignitatem conficiencium et recipiencium hoc sacramentum; patet quod oportet digne sumentem ipsum habere actus et habitus virtuosos, cum oportet quod Dei virtus et Dei sapiencia sit munde secundum habitus et opera quoad humanitatem suam undique ministrata; oportet, inquam, digne sumentem hoc sacramentum habere tres virtutes theologicas et conversacionem virtuosam imitatoriam capitis sui Christi; quod quidam intelligunt ex verbis Apostoli prima I. Cor. Vᵒ, quando docet quod non debemus epulari in fermento veteri quoad maculam peccati sed in azimis sinceritatis quoad virtutes que sunt disposicio ad recipiendum lumen gracie et operis virtuosi et veritatis vite qua fidelis servus Christi ostenditur in opere. Et hec est plena disposicio ad digne accipiendum corpus dominicum.

[ENGLISH]

## ¶2 · 159.1–159.11

> [p. 159] Quoad virtutes theologicas oportet omnino habere fidem sanctam de humanitate et deitate Christi et de concernentibus hoc sacramentum, quia inpossibile est infidelem in istis placere Deo manducando vel bibendo hoc sacramentum in memoriam Christi, cum ipse sit veritas odiens duplicitatem falsitatis; ideo infidelis ut sic vertit dorsum mentis in Dominum et ostendit sibi arma peccati Deo summe odibilia, convertit se ad patrem mendacii proditorie et derisorie, ideo talis iudicium sibi manducat et bibit secundum Apostolum.

[ENGLISH]

## ¶3 · 159.12–160.14

> [p. 159] Habita autem dignitate ex fundamento fidei necesse est quod erigatur spes in Domino omnipotente, omnisciente et benivolente, qui tantam gratitudinem nobis sibi ingratis ostendit humanitus paciendo, moriendo, ascendendo et sacramentum illud in memoriam istorum et aliorum mirabilium tribuendo. Unde Augustinus Enchiridion LIIIᵒ: Quidquid autem gestum est in cruce Christi, in sepultura, in resurreccione tercia die, in ascensione in celum et in eo quod sedet ad dextram patris, ita gestum est ut hiis rebus non mistice tantum dictis sed eciam gestis configuraretur vita christiana que hic geritur. Nam propter eius crucem dictum est: Qui autem Christi sunt carnem suam crucifixerunt cum viciis et concupiscenciis. Propter sepulturam: Consepulti enim sumus Christo per baptismum in mortem. Propter resurreccionem: Ut quemadmodum Christus resurrexit a mortuis per gloriam patris, ita et nos in novitate vite ambulemus. Propter ascensionem in celum sedemque ad [p. 160] dextram Patris: Si consurrexistis cum Christo, que sursum sunt sapite, non que super terram: Mortui enim estis et vita vestra abscondita est cum Christo in Deo. Ecce quomodo iste sanctus connectit ex fide scripture istam figuram nostram quintuplicem et rem gestam ad nostram doctrinam in moribus. Et totum istud debemus secundum usum ecclesie in sacramento eukaristie specialiter memorari, cum Christus precipiat pro istis Luc. XXᵒ, 19: Hoc facite in meam commemoracionem; et addit ecclesia: Hec quocienscunque feceritis in mei memoriam facietis. Et patet quomodo dignitas manducacionis huius sacramenti requirit quod ipsum digne accipiens per spem ad Dominum erigatur.

[ENGLISH]

## ¶4 · 160.15–161.2

> [p. 160] Et quoad caritatem patet quod nullum sacramentum notat expressius caritatem et pacem habendam cum Deo et homine quam hoc signum. Exhinc enim Christus tradens apostolis hoc sacramentum finaliter commendat tam crebro et specialiter in fine (ut patet Joh. XXᵒ) pacem apostolis. Hinc eciam secundum usum ecclesie datur signum pacis, antequam sacerdos vel laycus manducat hanc hostiam. Debet enim habere pacem cum fratre et per consequens cum Deo qui vult digne recipere sacramentum, ymmo secundum maximum signum caritatis debet attendi per hoc sacramentum ad ponendum tam corpus quam animam pro amicis, ut supra dictum est per Augustinum. Ex hinc Deus posuit sacramentum huius rei in illis naturis que ad unum aliquid reducuntur. Oportet enim quod recipiens digne simpliciter istam hostiam sit originatus predestinacione tamquam spiritualiter generatus univoce a grano frumenti quod cadens in [p. 161] terram mortuum est afferens multum fructum (ut dicitur Joh. XIIº).

[ENGLISH]

## ¶5 · 161.3–161.13

> [p. 161] Nec sufficit ista predestinacio nisi granum abiecto furfure molitum sit et tritum a Deo, que causaliter prevenit promerentem. Oportet enim predestinatum post primam graciam simul tempore presenciali labore mereri secundam graciam; et sic simul tempore post istam disposicionem oportet tercio quod sit gracia cooperans ad formam panis prandendi in patria, sic quod in isto tercio signo nature homo ex duplici gracia priori incipiat meritorie operari; que quidem gracia ex opere persone meritorie inpastans disponit ad graciam ampliorem.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 158.12: How we should receive Christ's body.
- 158.15: Need of good life and of the three theological virtues.
- 159.1: 1. Faith,
- 159.12: 2. Hope,
- 160.15: 3. Charity.
- 161.3: 2. Ground and bolted by God.
- 161.8: 3. Kneaded in good works.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 158: *Christi;* (print = bt) [SUB]
  - 160: *XXᵒ,* (print = bt) [SUB]
  - 160: *XXᵒ)* (print = bt) [SUB]
  - 161: *afferens* (print = bt) [SUB]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 2 5. F. Cor. V, 8. (158.31); reference I. Col. III, [. (160.32).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 158:
1. 13: probaveruttt; ib. C: asseruunt. 2. Codd.: vicinantes.
7. C: alias in marg. alia manu; \b.fiendas ; rcctius: ficticias. 19. C: virtus
et Dei supra lin. script. 23. D: ad conversacionem. 24. AB: quidem.
3i. I ) : recipiendum.

p. 159:
2. D: fidem rectam; ib. D: divinitate. 5, 6. E: et bibendo. f>. D : se-
cunditatem falsilatis; B: duplicem falsitatem ; C: convertit que. i3. D:
species. iG. D : & illud. 18. ABCE: Faich. LII; D : LV. Correxi
iq. B: Ckristi deest. 19, 20. C: tercia die in marg. alia manu.
20. E: ascendit ad dextram ; A: alias a dextris. 26. C: Et propter.
28. B: mrrexit. 3o. AB: sedens que; C: que in marg. alia manu.
10. I. Cor. XI, 2Q. 18. Opp. tom. VI, pag. 216.
24. Gal. V, 24. 26. Rom. VI, 4. 28. ib.

p. 160:
1. ABCD: dexteram. 5. AB : nostram dccst; C in marg. addit.
12. E: qualiter; ib. E: manducandi. i\. C: ad Deunt. 10. C: in fine
in marg. alia mano. 22. D: hanc dcest. 27. Codd.: ut ut. 29. A in
marg. : Nota. 3i. ABD: specialiter.

p. 161:
4. D: casaaliter. 6. Codd.: prius primam; ib. ABCD : principali
10. ABC: ex secunda. 12. E: meritoria ; ib. DE: disponat. i5. ABDE:
summo tribulacionis. 21. ABD: de deest. 25. ABCE: per graciam.
27. ABD: vitem ; C: correxit. 3j. D: egent.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
(none recorded)
```

---

## Chunk 06-b: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-06-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-06-b
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "161.14–165.16"
divisions: "cap. 6 (heading 'CAPITULUM SEXTUM.' at 158.0); part 2 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "893 words; 885 confirmed by the vote; 6 runs stood by rule; 2 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n232–n236 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 6, part 2: [TITLE]

## ¶1 · 161.14–163.12

> [p. 161] Et oportet quarto quod persona salvanda recipiat formam panis que imposita furno tribulacionis recipiat ex fervore caritatis quam habet ad Deum duriciem gracie consumate, et sic per ignem caritatis incorporabitur finaliter in circulo pani vivo et verificabitur illud Apostoli 1. Cor. Xº, 17: Quoniam unus panis et unum corpus multi sumus. Nam omnes de uno pane et de uno calice participamus. Et sic intelligunt de triplici gracia, scilicet preveniente quantum ad meritoriam passionem; nam pati et recipere precedit in nobis naturaliter meritoriam accionem, ad quam requiritur gracia cooperans. Et tercio post graciam predestinacionis requiritur ad generanciam et continuacionem gracia consumans. Oportet enim vitam veram dare nobis graciam calidam confuse informantem; unde signum infallibile est quod manducamus hunc panem indigne quod inter omnes gentes pro temporalibus magis contendimus et refrigescente caritate multorum ex superhabundante frigiditate temporalium preoccupancium mentem egeni in spiritualibus [p. 162] sequelam Christi magis contempnimus, dum tercio tempus et studium circa avidam conquisicionem, improvidam dispensacionem et avaram retencionem temporalium occupamus, sic quod ubi nobis sacerdotibus secundum regulam Christi omnia debent esse communia, unus manducans hunc panem esurit et alter est ebrius. Et inter omnes sacerdotes illi superiores qui efficacius imitarentur Christi vestigia in faciendo istud officium magis contemptibiliter quia plus Christo dissimiliter celebrant vel audiunt missas suas, in tantum quod ut periuri ad sui dispendium memorantur et nominant nomen Dei, sic et isti memorantur in sacramento eukaristie vite Christi; ideo tollerabilius et minus nocivum foret eis et populo quod non facerent talem falsam memoriam Salvatoris. Et sic ubi domini temporales care conducunt huiusmodi, ut eos habeant dignos et assiduos oratores, habent eos precipuos proditores. Nec mirum, quia contra legem Christi et racionem sacerdotalis ministerii dissolvendo statum primevum, onerant eos ac inhabilitant ad implendum suum ministerium. Ideo oportet quod racio militet contra utrumque membrum ecclesie sic protervum. Hoc enim sacramentum significaret quoscunque qui ipsum digne suscipiunt paratos ut pro Christo et causa legis Christi moriantur cum gaudio sed signata obmittimus. Ad signa autem que ritum et fastum sapiunt tamquam generacio adultera nimis attendimus; in tantum quod superiores persone ecclesie signis istis sensibilibus sic cecantur quod Samaritanis et paganis dampnabilius adorant (ut Christus dicit Joh. IVº capitulo) quod ignorant. Numquid credimus [p. 163] quod congregatis omnibus prelatis cesariis omnes sciunt quid est hostia consecrata? et errante intellectu necesse est quod erret affectus, cum cecitas oculi precipitat ambulantem. Cum igitur accipimus hoc sacramentum gracia gratitudinis Domini memorande, patet quod ad iudicium nobis manducamus et bibimus, quia remanemus post tam sollempnem memoriam Domino tam ingrati. Unde decretum Augustini positum in de Consecracione distinccione II sic loquitur: Quia morte Christi liberati sumus, huius rei memores in edendo carnem et potando sanguinem eius, que pro nobis oblata sunt nos obligaciores signamus.

[ENGLISH]

## ¶2 · 163.13–164.3

> [p. 163] Et patet quomodo fides, spes, caritas sunt necessaria celebranti; sed hodie est nobis nimis sinistra perversio, dum fides infigitur in signo, spes in mundo et caritas in infimo. Ponimus enim plus quam generacio phariseorum adultera fidem huius sacramenti in signo et in perfidis circumstanciis signorum, quia circa illorum observancias est nostra sollicitudo, nostra disputacio et nostra religio. Quoad spem patet quod ipsam ponimus in temporalium possessione, in amicorum confederacione et in prosperitatis mundane perseveracione. Et quoad caritatem patet quod ipsa sequitur in transformacione duas sorores priores, dum illos fratres quos exaltamus ad fimum mundi et honorem seculi, fingimus nos caritative diligere; illum sexum quem appetimus illecebris carnis confundere fingimus nos amare. Et quoad caritatem Dei ille fingitur plus [p. 164] Deum diligere qui superius aspirat vivere, quia (ut inquiunt) Deo similius. Et certum est quod quodlibet istorum est odium.

[ENGLISH]

## ¶3 · 164.4–165.16

> [p. 164] Quantum ad secundum, scilicet conversacionem virtuosam unitatoriam Jesu Christi patet ex dictis quod gracia huius constituitur hoc sacramentum. Unde inaniter celebrant qui pretereunt hoc figuratum. Figuratur autem nobis hec imitacio conversandi Exod XIIº, 7, ubi precipitur quod in esu agni paschalis ista 14ᶜⁱᵐ observentur, ut exponit Gregorius Super Evangelia Omelia XII: Quis, inquit, sit sanguis agni, non iam audiendo sed bibendo didicistis, qui sanguis super utrumque postem ponitur, quando non solum ore corporis sed eciam ore cordis accipitur aut hauritur. In utroque etenim poste sanguis agni positus est, quando sacramentum passionis illius cum ore ad redempcionem sumitur, ad imitacionem quoque intenta mente cogitatur. Nam qui sic redemptoris sui sanguinem accipit, ut imitari passionem illius necdum velit, in uno poste sanguinem posuit, qui eciam in superliminaribus domorum ponendus est. Quid enim spiritualiter domos nisi mentes nostras accipimus, in quibus per cogitacionem habitamus? Cuius domus superliminare est ipsa intencio que preeminet accioni. Qui igitur intencionem cogitacionis sue ad imitacionem dominice passionis dirigit in superliminari domus agni sanguinem ponit. Vel certe domus nostre sunt ipsa corda in quibus quousque vivimus, habitamus et in superliminari domus agni sanguinem ponimus, quia crucem passionis illius in fronte portamus. De quo [p. 165] adhuc agno subditur: Et edent carnes nocte illa assas igni. In nocte quippe agnum comedimus, quia in sacramento modo corpus dominicum accipimus, quando adhuc adinvicem consciencias nostras non videmus. Que tamen carnes igne assande sunt, quia nimirum dissolvit carnes quas aqua coxerit, quas vero ignis sine aqua excoquit roborat. Carnes itaque agni nostri coxit ignis, quia eum ipsa vis passionis illius ad resurreccionem valenciorem reddidit atque incorrupcionem roboravit. Qui enim ex morte convaluerit, videlicet carnes illius ab igne duruerunt. Unde per Psalmistam eciam dicit: Exaruit velud testa virtus mea quid namque est testa ante ignem; nisi molle lutum? Sed ei ex igne agitur ut solidetur, virtus igitur humanitatis eius velut testa exaruit, quia ab igne passionis ad virtutem incorrupcionis crevit.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 161.14: 4. Baked in the oven of tribulation and by the fire of charity.
- 161.22: Three kinds of grace: 1. Prevenient, 2. Cooperant, 3. Perfecting.
- 161.28: We priests shew our unworthiness by our care for worldly things.
- 162.7: The higher clergy are the worst.
- 162.23: To communicate should be a sign that we are willing to
- 162.26: Now we care only for the sign and not for the thing signified.
- 162.26: die tor Christ.
- 163.13: Faith, hope and charity are all misplaced.
- 164.4: The sacrament is appointed for the sake of virtuous life uniting us to Christ.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 163: *disputacio* (print = bt) [SUB]
  - 164: *poste* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 161:
4. D: casaaliter. 6. Codd.: prius primam; ib. ABCD : principali
10. ABC: ex secunda. 12. E: meritoria ; ib. DE: disponat. i5. ABDE:
summo tribulacionis. 21. ABD: de deest. 25. ABCE: per graciam.
27. ABD: vitem ; C: correxit. 3j. D: egent.

p. 162:
4. D: nisi nobis. 7. AB: essent superioris; A: esscnt in marg. alia
manu; C: extinxit essenl. 8. D: et faciendo. n. ABE: ncc pcriuri.
14. D: nocuum. i(i. E: magis care ; ib. ABCD: modi decst. 23. D: sig-
naret. 25. D: cum gaudio Christi meriantur. 27. ABCD: gcncra.
3i. E: capitulo deest.
(>. I. Cor. XI, 2 1. 3l, Joh. IV, 22.

p. 163:
i. C: omnibus in marg. alia manu. 3. E: necesse est ut. 4. D: ergo.
6. C : nobis in marg. alia manu. 8, 0. E : positum deest. 12. ABCE : nobis.
In Decreto haec duo verba: nobis obligaciores desunt. 14. ACDE: nobis
deest. i5. C: figitur; in erased. 16. D: genera. 21, 22. D : et ami-
corum. 24. CD : consequitur ; ib. C: duas in marg. alia manu. 25. C : quos
in marg. alia manu; ib. AB : ad summum; CDE: finium. 27. AB : ille-
cebras ; C: correxit.
5. I. Cor. XI, 29. 9. Decreti Tertia Pars, De Cons.,
dist II, cap. I.. Non est Augustini sed Ambrosii ad, e. XI,
primae ad Cor.

p. 164:
1. C: vivcre in marg. alia manu. 7. D: signatum; ABC: figurativum.
10. CD: observantur. 12. C: quis in rasura. i3, 14. C: quando —
hauritur in marg. alia manu. 14. D: et hauritur. i5. E: enim.
if>. D: ante sacramentum. 17. AB : quoque cum; D: quasi; E: quam
inlenta. 19. E: eius. 20, 21. ABCE: et in super. 22. C: qui mentea.
27. ABDE: aqui decst. 28. D: corpora. 3o. E: eius.
8. S. Gregorii In Evangcl. lib. II, Hom. XXII, Opp. tom. I,
pag. 1 533 — 1535.

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
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
(none recorded)
```
