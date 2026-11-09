# Translation brief: eucharistia 09-a–09-c

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/eucharistia/wyc-eucharistia-09-a.md chunks/eucharistia/wyc-eucharistia-09-b.md chunks/eucharistia/wyc-eucharistia-09-c.md` once and fix what it reports.
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
  implicit). Supplied words in `[brackets]`, sparingly, ⛔ never in italics. **Quotations** (a quotation running on across ¶s or into the next chunk opens each ¶ with a double quote and closes only at its end; quotations inside it take single quotes) in quotation
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
   every §A–C term: `[accident]{g:accidens}`; a multi-word key is lower case with hyphens, `{g:corpus-christi}`, `{g:a-simili}` (lint rejects spaces); never nest brackets inside a tag (`[form [sounds] with]{g:k}` breaks the site): tag the bare word. The key must exist in GLOSSARY.md. ⛔ A `(LEDGER …)` reference goes only in a note, never in the English running text. A term that looks
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

## Glossary (the 545 rows these chunks use; the full file is GLOSSARY.md)

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
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |
| sacramentum (the Eucharist); sacramentum altaris | sacrament; the sacrament of the altar | The plain sense, against the Augustinian row (*Incarn.*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.3, 3.30). |
| panis / vinum | bread / wine | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.8). |
| corpus Christi / corpus Domini | the body of Christ / the body of the Lord | Kept apart as the Latin alternates them. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.6, 1.10). |
| novella ecclesia / antiqua ecclesia | the newer church / the ancient church | The pair of 3.3; cf. *novelli*. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 3.3). |
| cultores accidencium / signorum | worshippers of accidents / of signs | Wyclif's name for the defenders of the accident without a subject. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 6.15, prol-c 10.2). |
| sumpcio | reception | Of the sacrament; *sumere* "receive". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 13.2). |
| missantes | mass-priests | Priests hired to say masses; pejorative. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 15.25). |
| pontifex (a Christian bishop, unqualified) | pontiff | As the Old Testament row; where the referent (a bishop) matters, an R note. *pontifices ydolorum* "pontiffs of idols". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 14.29, 15.17). |
| species (of bread and wine) | species | The sacramental species; kept as the term, not "appearance". Distinct from the logical *species*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 13.15; 23.8). |
| sacer; sacrare | sacred; hallow | Kept apart from *sanctus / sanctificare* "holy / sanctify" and from *consecrare*; *consecrare* is "to hallow together" in the grammarians' etymology. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 27–28). |
| sacramentum tantum | a sacrament only | The *sacramentum tantum* of the Lombard's three (IV d. 8 c. 4). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 29.23). |
| decretalis | decretal | Kept apart from *decretum* "decree". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 71.31). |
| principaliter; principalitas (of the body's presence) | principally; principality | Of the body of Christ alone being in the sacrament as its principal; not the compendium's *principaliter* "as a main head". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 75.5–26). |
| transaccidentacio | transaccidentation | Wyclif's coinage beside *transsubstanciacio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 81.27). |
| transinferioracio; transsubieccio | transinferioration; transsubjection | Coinages in the same series. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 82.3). |
| baptiste signorum | baptizers of the signs | Not "Baptists". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 81.29). |
| accepcio personarum | respect of persons | The Douay phrase. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 92.15). |
| consecracio | consecration | The noun of *consecrare*; see *confeccio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 99–100). |
| transaccidencia | transaccidents | In the *transaccidentacio* series. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 145.4). |
| katholicacio | declaration as catholic | The noun of *catholicare*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 156.31). |
| corpus dominicum | the Lord's body | Kept apart from *corpus Domini* "the body of the Lord" and *corpus Christi*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 158.31, 165.3). |
| in circulo (of the host) | in a round | The round form of the host. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 161.17). |
| cultor; cultus (sacramenti) | worshipper; worship (of the sacrament) | Beside *cultus Dei* "worship of God" and *cultores accidencium*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 177.3–9). |
| sanctificacio | sanctification | Ruled 2026-11-07 (coordinator, delegated; *Euch.* 189.6). |
| eukaristia | the Eucharist | Capital as the sacrament's name; the adjective *eucharistic* lower case. Ruled 2026-11-07 (Wilson, "i agree"; conformed through the volume); kept apart from *sacramentum (altaris)*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 196.29). |
| secta signorum | the sect of the signs | Wyclif's name for the *moderni*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 220.13). |
| glossa; glossator | gloss; glossator | The ordinary gloss on the canon law and its authors. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 07-j passim). |

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
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| potencia regulata racione | power regulated by reason | Pilot. |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| temporalia | temporal goods | |
| prelatus | prelate | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| censura | censure | Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| citare; citacio | to cite; citation | Summons to a church court. Ruled 2026-09-28 (coordinator, delegated) (12 sites). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| possessionati | the possessioners | Endowed religious. |
| satrapa | satrap | Derogatory: church-court officials wielding delegated power (T. p. 378 n. 58). Keep the word; note it at first occurrence per work. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | CONTEXTUAL: condition / respect | "Condition": a person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). "Respect": the logical relation under which a predicate holds (*posiciones secundum habitudinem*), with a **C** note; ruled 2026-10-22 (Wilson; *Incarn.* 4.16). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| franchisia | franchise | Ruled 2026-10-02 (*Eccl.* 239.22). |
| facinus | misdeed | Wyclif equates it with "felony" (239.13, 239.21). Ruled 2026-10-02. |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |
| autenticus / autenticacio | authentic / authentication | The key term of *Eccl.* 13. Ruled 2026-10-02. |
| leges ecclesie | the laws of the church | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.20, 1.23). |
| decretum; decreta | decree; the decrees | Gratian (*in decretis*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.14, 3.24). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| credulitas | credence | With *credere*, believe (*Dial.* 23.17–24.4). Ruled 2026-09-28. |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| sumitur pro | is taken for | Supposition language. Pilot. |
| famosior | best-known [sense] | Pilot. |
| simpliciter / secundum quid | **without qualification / in a certain respect** | ⛔ Always opposable. Never "simply", "wholly", "directly", "naturally" etc. (T. p. 364). |
| necessitas supposicionis / ex supposicione | necessity of supposition / necessity on supposition | Conditional necessity. Pilot (*Eccl.* 3.21); *ex supposicione* ruled 2026-10-02 (34.12, 38.22). |
| de congruo / de condigno | by congruity / by condignity | Pilot. |
| contingens ad utrumlibet | contingent either way | T. p. 364. |
| consequencia | inference | ⛔ Not "consequence" (T. p. 361 n. 13). |
| consequens / antecedens | consequent / antecedent | |
| sequitur | it follows | Introduces a stated inference, often quoted in the next words. Pilot (*Eccl.* 2.21). Not tagged where it is not an inference ("the third law follows", *Dial.* ch. 5). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
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
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| iugum | yoke (a pair) | Ruled 2026-10-02 (*Eccl.* 202.9 ff.). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |
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
| approbati doctores | approved doctors | Kept apart from *probabiles doctores*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 13.3). |
| novelli | the newer [doctors] | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 13.7). |
| determinacio | determination | A qualifying addition to a predicate (*cum determinacione*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 14.11). |
| sophistice | sophistically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 15). |
| de vi vocis / de vi sermonis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| determinaciones ecclesie | the church's determinations | Rulings of the church, not the logician's *determinacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 24). |
| nedum | not only | "Let alone" where the sense is a fortiori. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21, 24). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| minoracio | lowering | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| humiliacio | humbling | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26–28). |
| immediate | without intermediary | The scholastic sense, ⛔ not "at once". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 30.30). |
| humanitus | humanly | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* passim). |
| suscipere / suscepcio (of the soul, the nature) | take up / taking-up | Kept apart from *assumere* "assume". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 31). |
| in quantum (reduplicative) | insofar as | As *secundum quod*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37.9). |
| universitas creaturarum | the totality of creatures | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37). |
| diccio (logical) | word | A single term in a proposition. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 43.3). |
| in effectu | in actual fact | As against in potency or in name; ⛔ not "in effect" (modern "virtually"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 47.10). |
| predicacio actualis / aptitudinalis / habitudinalis / mixtim | actual / aptitudinal / habitudinal / mixed predication | *Habitudinalis* is its own term (the four MSS at 49.6), not under *habitudo*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.5–16). |
| Doctor Subtilis | the Subtle Doctor | Scotus. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.24). |
| forma totalitatis | form of totality | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 50.7). |
| quantus | quantified | The adjective beside *quantitas*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.22). |
| construccio synecdochica | synecdochic construction | Beside *synecdochica locucio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.5). |
| moderniores loquentes | the more modern speakers | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 59.21). |
| dampnificare / dampnificacio | damage / damaging | Kept apart from *dampnum* "loss" and *dampnari* "be damned"; the argument of 65–68 turns on it. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 65). |
| per se / per accidens | CONTEXTUAL: of itself / by accident; (spatial) apart, by itself | The spatial sense (a thing set apart, *Euch.* 104.16–17) gets a G note. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a (sufficienti) divisione | the topic from sufficient likeness / from (sufficient) division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| pretericio | being past | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| solvere / solucio (of the union) | loose / loosing | Except inside a Douay quotation (John 10:35 "cannot be broken"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| peccabilis | able to sin | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| medium (logical) | middle term | Of a syllogism; elsewhere "means" by context. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| capitales doctores | the chief doctors | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| eiusdem / consimilis / alterius racionis | of the same / like / another kind | The species-sense of *racio*; *racio speciei* "the account of the species" (Aristotle's *logos*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.4, 87.17). |
| principiari | be constituted from principles | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.7). |
| accidentatus | subject to accidents | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.4). |
| in recto / in obliquo | in the direct case / in an oblique case | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.25). |
| signum / signatum | sign / thing signified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 91.2–6). |
| predicacio synecdochica | synecdochic predication | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.27). |
| humidum infantile / radicale | the moisture of infancy / radical moisture | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 94.9). |
| esse intelligibile | intelligible being | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 99.23). |
| extraneare / extraneacio (supposicionis) | estrange / estrangement (of supposition) | *Affeccio extraneandi* "an affection of estrangement". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 98.16). |
| ministerialiter | ministerially | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 100.17). |
| mobile (noun) / primum mobile | a movable / the first movable | Against the adjective *mobilis*; ch. 7 turns on it. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 107, 116). |
| res racionis | thing of reason | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| universitas creata | the created totality | Beside *universitas creaturarum*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| significatum | significate | Kept apart from *signatum* "thing signified". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 111). |
| predicacio secundum essenciam / formalis | predication by essence / formal predication | Wyclif's modes of predication (cf. *predicacio secundum causam*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 115–116). |
| forma substancialis | substantial form | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| concepcio (figure) | conception | The grammatical figure. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habitus (of the humanity) | habit | The Lombard's third opinion (*Sent.* III d. 6). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| accidens | accident | The category; *accidit* "befalls". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habitacio | habitation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 120.14). |
| figura / figuratum | figure / thing figured | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 121.23). |
| incepcio | beginning | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 121.16). |
| exceptiva | exceptive [proposition] | Beside *exclusiva*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.31). |
| humanitacio | humanation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 126.12). |
| racio (individual, personal) | account | *Racio individui / persone* "the account of an individual / a person", as *racio speciei*; not "aspect" (the row against *substancia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 8, 129–132). |
| vir (against *homo*) | man (*vir*) | Where Wyclif sets *vir* against *homo*, the Latin in parentheses. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 129.15–26). |
| exemplaria / exemplata | exemplars / things exemplified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.6). |
| res secunde intencionis | things of second intention | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.25). |
| complexio | complexion | The mixture of qualities. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137–138). |
| materia proxima / remota | proximate / remote matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137.1). |
| colorate | with colour enough | With a plausible ground (cf. *color*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 134.26). |
| res communis / res communes | the common thing / common things | The realist universal the *moderni* do not conceive (first root of their error). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 144.27). |
| distinccio racionis | distinction of reason | Beside *differencia formalis*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 145.23). |
| moderni (bare) | the moderns | Beside *moderni doctores* "the modern doctors". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 142.10). |
| principiare (active) | be the principle of | Beside the passive *principiari* "be constituted from principles". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 147.4). |
| assumere personale | personal assuming | The infinitive used as a noun; kept apart from *assumpcio personalis* "personal assumption". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 146.33). |
| moderniores (bare) | the more modern | Beside *moderniores doctores* "the more modern doctors". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 151.17). |
| transsumpcio | transumption | Beside *transsumptive*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 153.28). |
| in quid (predicari in quid) | in quid | Kept in Latin (predication of what a thing is, as against *in quale*), glossed at first use in a chunk. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 162.22). |
| dependencia actualis / potencialis / obediencialis | actual dependence / potential dependence / obediential dependence | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 161.23–162.4). |
| substancia prima / substancia secunda | first substance / second substance | Aristotle, *Cat.* 5. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.25). |
| a simili | by likeness | Bare, as an argument form; beside *locus a simili* "the topic from likeness". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.16). |
| racio substancialis | substantial account | As *racio individui* "account". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.21). |
| doctores signorum | the doctors of signs | The logicians who reason from terms, not things. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.26). |
| accidens absolutum | absolute accident | Quantity and quality, against relative accidents. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 176). |
| beatificabilitas | beatifiability | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 181). |
| posicio anime | the laying-down of the soul | John 10:17–18; not the logical *posicio* "position", C note. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 183.3). |
| perfeccio simpliciter | perfection without qualification | After *simpliciter* "without qualification". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.1). |
| transsubstanciacio | transubstantiation | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.10). |
| multiplicative | multiplicatively | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 193.20). |
| habitudo relativa | relative respect | The "respect" sense of the CONTEXTUAL *habitudo* row. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 193.19). |
| remitti / intendi (of a quality, merit) | be remitted / be intensified | The intension and remission of forms; not *remissio* of sin. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 197.1–7). |
| in divinis | among the divine [persons] | Keeps "Godhead" for *deitas*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 196.18). |
| partes proporcionales | proportional parts | The halving division of a continuum. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 194.24). |
| universitas creabilis | the creatable totality | Beside *universitas creaturarum* "the totality of creatures". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 199.5). |
| multiplicacio dimensionalis | dimensional multiplication | One body in several places by its dimensions. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.6). |
| habitus (= possession, *habere*) | the having | The category of having, C note; kept apart from *habitus* "habit". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.14). |
| a maiori vel pari | from the greater or from the equal | Arguments *a maiori*; cf. *locus a maiori*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 209.5). |
| multiplicacio concomitancie | multiplication of concomitance | Cf. *gracia concomitancie*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 213.21). |
| assertibile | assertible | The thing a proposition asserts. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 215). |
| superioritas / inferioritas terminorum | superiority / inferiority of terms | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 215). |
| exponentes | the exponents | The propositions into which a proposition is resolved (expounded). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 216.14). |
| homo communis | the common man | The universal man, with *res communis*; not "the ordinary man". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 218.3). |
| moderni loquentes | the modern speakers | Beside *moderniores loquentes*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 221.20). |
| congruencia | fittingness | The reasons of fittingness for the Son's incarnation. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 225.6). |
| bonum de genere | good in its kind | Moral goodness by the kind of act. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 228.16). |
| lex proximitatis | the law of neighbourhood | The duty to love one's neighbour (*proximus*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 101.29). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |
| sacramentaliter | sacramentally | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| realiter | really | A mode adverb: one word each, never two merged, kept where Wyclif puts it. ⛔ Never "actually". Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| vere | truly | A mode adverb: one word each, never two merged, kept where Wyclif puts it. ⛔ Never "really" (that is *realiter*). Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| spiritualiter | spiritually | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| figurative | figuratively | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
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
| sensus communis | the common sense | The inner faculty; kept apart from *sensibile commune* "common sensible". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 18.31). |
| laudative; effective | by way of praise; by way of effect | Of blessing God vs. blessing a thing. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 16.24). |
| figurare | figure | Both senses: to prefigure (the lamb figured Christ) and to shape (*figurare Deum nostrum*), which Wyclif plays on; one English word keeps the pun. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-c 10; 21.29). |
| sensualiter | sensually | Berengar's oath word (*Ego Berengarius*); kept apart from *sensibiliter* "perceptibly". A mode adverb, one word. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 26.1, 30.24). |
| sentire (an opinion: sensit quod) | hold | Of a doctor's or church's opinion; the "perceive" row is the sacrament sensed. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 30.30, 31.18). |
| predicacio figurativa | figurative predication | A synonym of *predicacio tropica*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 35.18). |
| expositorie (of preaching scripture) | by way of exposition | Not the logicians' *expositorie* "expositorily" of the expository syllogism. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 46.4). |
| desicio | ceasing | Kept apart from *destruccio* "destruction" and *corrupcio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 54.25, 55.21). |
| aliquitas | somethingness | Being a something (*aliquid*). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 60.27). |
| informacio; informare | informing; inform | Of a form in its subject; not "information". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 64.13). |
| accidens predicamentale | accident of the categories | Kept apart from the predicable *accidens*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 64.1). |
| revera | in truth | Kept apart from *vere* "truly". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 63.4). |
| contiguacio | contiguity | Beside *continuacio* (of bodies) "continuation". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 68.12). |
| veritas predicamentalis | truth of the categories | As *accidens predicamentale* "accident of the categories". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 69.2). |
| esse situale / intencionale / potenciale | situal / intentional / potential being | The modes of the body's being. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 84.8 ff.). |
| sensus (of words) | meaning | Kept apart from *sentencia (verborum)* "sense" (Wilson's row). The bodily *sensus* and *sensus literalis / misticus* stay "sense". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 89.22, 04-c, 04-d). |
| interpolatus; interpolacio | interrupted; interruption | Of words spoken with pauses. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 89.4, 89.18). |
| famosius | as best known | The adverb of *famosior*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 90.15). |
| quintimembris | fivefold | Cf. *trimembris*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 91.11). |
| pertinenter | fittingly | Kept apart from *convenienter*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-e, 04-f). |
| essencialiter | essentially | A mode adverb, one word. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-g). |
| noticia confusa / distincta | indistinct / distinct knowledge | As *confuse / confusus* "indistinct(ly)". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-g). |
| ponderositas; ponderosum | heaviness; heavy | The abstract against the concrete: *hostia est ponderositas sed non est ponderosum*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-a p. 10, 110.24). |
| suscipere magis et minus | admit of more and less | Aristotle's test of a quality. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 113.32). |
| questio si est / quid est | the question whether it is / what it is | *Post. An.* II.1. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 119.18). |
| dogmatisare | teach as dogma | Of the *moderni*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 120.13, 124.2). |
| universitas sua (God's) | his universe | Beside *universitas creaturarum* "the totality of creatures". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 124.31, 129.16). |
| mistice | mystically | A mode adverb, one word; kept apart from *figurative*, *tropice*, *sacramentaliter*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 128.24). |
| figuracio | figuration | Beside *figura / figurare*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 131.16). |
| neutraliter; adiective | as a neuter [noun]; as an adjective | The grammar of *accidens*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.7). |
| naturalitas obediencialis | obediential naturalness | Cf. *dependencia obediencialis*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.15–18). |
| accidentalitas | accidentality | Beside *substancialitas*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.13). |
| quantitas successiva | successive quantity | Time and motion, against permanent quantity. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.1). |
| corpus mathematicum | mathematical body | The three dimensions without matter. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 142.31). |
| fantasiare | fancy | The verb beside *fantasia* "imagination". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 143.16). |
| ubi; ubicans | where; that which gives a where | The category of place and its cause. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 146.23–24). |
| inpossibilitare | make out as impossible | Of the *moderni*'s argument. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 149.13). |
| utrobique | on both sides | In citation formulae and argument. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 148.21). |
| yronice | ironically | Ruled 2026-11-07 (coordinator, delegated; *Euch.* 153.4). |
| pertinencior | more fitting | The comparative of *pertinens*; cf. *pertinenter*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 153.8). |
| generancia | begetting | Ruled 2026-11-07 (coordinator, delegated; *Euch.* 161.25). |
| ponderacio | weighing | Beside *ponderositas* "heaviness". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 183.17). |
| universitas (bare: tota universitas) | the whole universe | Beside *universitas sua* "his universe". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 192.14). |
| qualitas prima | first quality | Hot, cold, wet, dry. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 197.24). |
| subiectare | be the subject of | Of a substance underlying accidents. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 199.10). |
| visio corporalis / ymaginaria / intellectualis | bodily / imaginary / intellectual vision | Augustine's three kinds (*De Gen. ad litt.* XII). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 206–211). |
| diffinitive (of presence) | definitively | Of being in a place definitively, not circumscriptively. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 216.4). |
| sensus tropicus | tropical meaning | As *sensus* (of words) "meaning". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 217.22). |
| contentive / causaliter / subiective / obiective | by way of containing / causally / subjectively / objectively | The modes of being in the sacrament. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 219.17–22). |
| multiplicacio corporis | multiplication of a body | The subject of ch. 8. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 232.5). |
| predicatum infinitum / finitum | infinite / finite predicate | Ruled 2026-11-07 (coordinator, delegated; *Euch.* 235.29). |
| qualitas secunda | second quality | Beside *qualitas prima*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 236.11). |
| immediatus; immediacio | immediate; immediacy | With nothing between; the adjective and noun of *immediate* "without intermediary". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 240.14, 247.6). |
| infinicies | infinitely many times | Ruled 2026-11-07 (coordinator, delegated; *Euch.* 237.10). |
| non communicans (of times) | not communicating | Of times with no common part. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 241.25). |
| simultas adequacionis / inmediacionis | simultaneity of adequacy / of immediacy | Ruled 2026-11-07 (coordinator, delegated; *Euch.* 247.9–10). |
| principative | principatively | Beside *principaliter*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 247.21). |
| argumentum temptativum | tentative argument | Aristotle's *peirastic* argument. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 256.4). |
| quando (the category) | the when | Beside *ubi* "where". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 260.23). |
| quandalitas | whenness | The abstract of *quando*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 268.6). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| perplexus | perplexed | The moral-theology sense: bound to sin whichever way one turns. Ruled 2026-09-28. |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| indebitare se | to make oneself a debtor | Sense doubtful; C note (*Dial.* 85.15). Ruled 2026-09-28 (coordinator, delegated). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office; *quale magisterium* "what a feat of mastery" (*Incarn.* 137.14) | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| detegere | to expose | "wipe away" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| recencius | more freshly | Pilot (*Dial.* 2.10) |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| irreligiositas | irreligion | Ruled 2026-10-02. |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| ydiota | unlettered man | Never "idiot". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| calumpnia (ponere / capere) | challenge (to lay a challenge against / to be open to challenge) | The disputant's formal objection to a premiss. Ruled 2026-10-02 (*Eccl.* 16, 363.18, 363.24, 367.11). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| raciuncula | little argument | The opponent's ten arguments. Ruled 2026-10-02 (*Eccl.* 17, 398.15). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| falsarius | falsifier | The opponent's epithet. Ruled 2026-10-02 (*Eccl.* 17, 414.6). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| continuacio (of bodies, the act) / discontinuacio; continuare / discontinuare | continuation / discontinuation; make continuous / make discontinuous | The making of several bodies into one continuum (*Incarn.* ch. 12), G note at first use: not "carrying on". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.30, 211.12). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| perplexitas | perplexity | The noun beside *perplexus* "perplexed". Ruled 2026-10-02 (*Eccl.* 19, 470.3). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| dampnacio | CONTEXTUAL: damnation / condemnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). Of a judgement passed on a teaching (*dampnacio istius sentencie tamquam heretice*, *Pot. pape* 84.10) "condemnation"; ruled 2026-10-07. |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| palliacio; palliare | cloaking; to cloak | Ruled 2026-10-02 (*Eccl.* 23, 566.27). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| iurisdiccio | jurisdiction | Cf. *potestas iurisdiccionis*. Ruled 2026-10-07 (*Pot. pape* 23.17). |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the Eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). Beside *consecrare* (*consecrat et conficit*) "confect", so the pair stays two. Ruled 2026-11-07 (Wilson, "confect works"; *Euch.* 16.10). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| trahere in consequenciam | draw into a precedent | The legal idiom; *consequencia* stays "inference". Ruled 2026-10-07 (*Pot. pape* 94.13). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| preeminencia | preeminence | Kept apart from *primatus* "primacy". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| fantasia | imagination | The faculty (scholastic *phantasia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 147.11). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| Cestrensis | the Chester [chronicler] | Ranulf Higden, *Polychronicon* (S note at first occurrence in a chunk). Ruled 2026-10-08 (coordinator, delegated; conformed in 06-h … 09-b). |
| infundabilis; infundabiliter | without foundation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 195–196). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| fantasticus | CONTEXTUAL: imaginary / phantastic (of the faculty) | Cf. *fantasia* "imagination". "Phantastic" where it names the power (*estimative fantastice … organice*, *Euch.* 208.27, coordinator 2026-11-07). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 203.4). |
| extollencia | exaltation | Self-exaltation of the proud. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.5). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| carismata; carisma | CONTEXTUAL: charisms / chrism | "Charisms" (gifts; *Pot. pape* 176.1). Singular *misticum carisma* in Augustine's sense of the anointing that names Christians (*chrisma*, *Pot. pape* 312.16) "chrism", with a T note. Ruled 2026-10-08; CONTEXTUAL 2026-10-12 (coordinator, delegated). |
| primicia (virtutum) | being first (in the virtues) | Kept apart from *primatus* "primacy" and *primitas* "firstness". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 228.33). |
| replicatur; replicatum | it is rejoined; rejoinder | A further objection against an answer; kept apart from *respondetur* "the reply is" (so 04-b). Ruled 2026-10-08 (coordinator, delegated; conformed 10-e, 10-g). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| neutra | neutral things | Things neither commanded nor forbidden (obedience *in neutris*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.19). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| papa cesareus | caesarean pope | The pope as endowed temporal lord (chs. 10–12). Ruled 2026-10-08 (coordinator, delegated). |
| imperium (vicarium, autoritativum) | command (vicarial, authoritative) | The power to command (*par in parem non habet imperium*); "empire" only of the Empire. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 263.2). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| precellencia | pre-excellence | Kept apart from *preeminencia* "preeminence". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 274.33). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| pontifex (Old Testament, unqualified) | pontiff | Kept apart from *sacerdos* "priest"; *summus pontifex* of the Jewish priesthood is "high priest" (see *summi pontifices*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* ch. 11). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| pastor cesareus | caesarean shepherd | The *papa cesareus* family. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 290.24). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| precellenter | pre-excellently | Adverb beside *precellencia* "pre-excellence". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 291.2). |
| correptibilis | open to reproof | Beside *corripere* "reprove". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 301.3). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| calumpniator | challenger | Under *calumpnia* "challenge". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 323.10). |
| pallium privilegii | cloak of privilege | Kept apart from *palliacio* "cloaking". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-a). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| potissimus; pocior (Antichristus) | foremost; greater | Superlative and comparative kept visible as a pair. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.28, 331.12). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| episcopi cesarei | caesarean bishops | Extends *prelatus / sacerdos cesarius*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 331.24). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| spissius (vivere) | more closely | Of living to a rule. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 338.13). |
| evangelizans | preacher of the gospel | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-g). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| pagina (of a law) | page | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.13). |
| civilitas cesarea | caesarean civil standing | After *civilitas* "civil standing" and *papa cesareus*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.31). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |
| gravandi | those to be charged | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 360.24). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |
| coloracior | more colourable | Comparative, with the *color* / *colorabilis* rows. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 384.15). |
| diccio procuratoria | proctorial pronouncement | C note gives *dicio* "authority" as the alternative. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 386). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| precellere | excel | Verb beside *precellencia* "pre-excellence"; not "pre-excel". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 399.28). |
| cesaree (adv.) | in caesarean fashion | After *papa cesareus*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 403.25). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |
| nimis | exceedingly | Medieval intensive (= *valde*); "too much" only where excess is the point. Ruled 2026-10-12 (close-out R2; *Pot. pape* 169.2). |
| sentire (the sacrament, the body) | perceive | "sense". As *sensibilis* "perceptible". Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.10, 1.17). |
| singulariter | CONTEXTUAL: alone, only / in a singular way / in the singular (grammatical number, *Euch.* 215.15) | "singularly" never; "in a singular way" where "alone" will not construe (*Euch.* 85.28, coordinator 2026-11-07). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 4.14). |
| recitare | recite | To report, rehearse. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.4, 3.10, 4.18). |
| narrare | relate | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.9). |
| pius pater | loving father | *pius* of a father: not "pious". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 42.27). |
| ex tibi dubio; ex sibi dubio | for all you know; for all he knows | Idiom: not "from doubt". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 66.15, 70.25). |
| cordatus | stout-hearted | Not "wise" (C note where it leans). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 180.6). |
| pertinaciter | pertinaciously | Keeps "obstinate" for *protervus*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 180.29). |
| rima | chink | Wyclif's figure for a loophole. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 216.21). |
| sollempnior (of doctors) | more eminent | The medieval sense of *sollempnis*; not "more solemn". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 262.18). |

---

## Chunk 09-a: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-09-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-09-a
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "272.12–276.20"
divisions: "cap. 9 (heading 'CAPITULUM NONUM.' at 272.0); part 1 of 14, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "916 words; 907 confirmed by the vote; 5 runs stood by rule; 4 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n343–n347 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 9, part 1: [TITLE]

## ¶1 · 272.12–272.22

> [p. 272] Pro complemento huius operis transcurrendum est per septem obiectus, ut fides de eukaristia plus patescat. Et primo notandum quod moderni ferunt graviter quod panis post consecracionem remaneat vel quod sacramentum non sit accidens sine subiecto. Primo ergo arguitur per hoc quod decretalis Innocencii tercii ad cuius edicionem fuerunt mille CCC et XV prelati dicit oppositum. Cum ergo secundum Augustinum nullus crederet evangelio nisi prius credat ecclesie, sequitur quod omnis eatholicus debet credere isti decreto tam gravi ecclesie.

[ENGLISH]

## ¶2 · 272.23–273.4

> [p. 272] Hic sunt multe instancie; prima loycorum que dicit quod non docetur efficaciter quod ista fuit sentencia dicti Innocencii cum tot prelatis. Secunda quod non docetur quod ipse vel illi fuerunt membra ecclesie, nam solum predestinatus est membrum ecclesie, sed ex tibi dubio nullus istorum fuit predestinatus, ergo [p. 273] ex tibi dubio nullus istorum fuit membrum ecclesie. Qualis ergo racio: Si homo debet credere ecclesie, ergo illis? De ista materia, quomodo fides data ecclesie iniciat fidem catholicam, patet alibi.

[ENGLISH]

## ¶3 · 273.5–273.13

> [p. 273] Tercia instancia est quod transsubstanciacio est, quando una substancia transit in aliam, ut panis fit corpus Christi ad sensum expositum. Et quantum ad illud de existencia accidencium sine subiecto, dictum est quomodo multipliciter potest vere intelligi; et si replicetur quod dicta ecclesia non sic sentit, dicitur quod hoc docto consenciendum est veritati quod dogma foret nimis difficile; ideo hoc habito dicitur quod non est credendum in hoc illi ecclesie.

[ENGLISH]

## ¶4 · 273.14–274.4

> [p. 273] Unde quarta instancia vere dicit quod nulli ecclesie vel angelo de celo credendum est in materia fidei, nisi de quanto super racione se fundaverit vel fide scripture. Cum ergo sensus ab adversariis expositus neutro istorum modorum fundatur, sequitur quod ille sensus propter nullam ecclesiam est credendus. Nam nullus istorum fuit subtilior quam sancte pagine professor notabiliter errans in ista materia. Quis ergo color, si omnes illi prelati fuerunt sacre pagine professores vel episcopi, quod decretum eorum carebat calumpnia? Nonne Sarraceni, Tartari, ymmo Asiani plures quam mille millia consenciunt in oppositum dicte sentencie, et sicut nos dicimus quod habemus fidem rectam nobisque est credendum, ita dicunt Asiani de se ipsis et contrarium de nobis; ymmo hodie possent colligi multa millia episcoporum et doctorum cum episcopo Avinonico que in ista materia forent contraria veritati; itaqae non est color, si tot congregati sic diffinierant, ergo verum et verecundum [p. 274] est illis asserere quod oportet Deum eis assistere sic quod non errent in fide, cum continue sic faciunt et fecerunt. Sic enim fantasiarunt Donatiste coloracius et multi alii infideles.

[ENGLISH]

## ¶5 · 274.5–276.8

> [p. 274] De ista materia dixi alibi; ideo si verum est quod dicit Doctor Subtilis quod nichil cogit sic dicere nisi decretales epistole supradicte, nimis vacuus est baculus arundineus cui adversarii innituntur. Unde doctor quidam dubitat quare tantum innituntur moderni isti decretali dimissa scriptura sacra cum quatuor sanctis doctoribus; et respondet quod oportet populum plus in errore et malicia profundari; ideo argumentum Sathane cecantis sordentes est quod debent inniti sentencie huius pape, credendo istam blasphemiam, quia ipse inter omnes papas maxime stetit secundum scripturas pro dignitate ecclesie; ideo magnificemus ut evangelium scripta sua. Quo contra fidelis dicit ecclesie et specialiter regibus quod iste inter omnes papas maxime palliavit scripturas ad subtrahendum honorem et dominia secularium dominorum et accumulando sibi et clero suo contra religionem Christi primatus seculi, ut primo decretalium De Maioritate et Obediencia, capitulo Solite, habetur, quomodo respondendo ad litteram imperatoris palliavit dictum pape Petri quo dicit prima Petri IIᵒ, 13: Subditi estote omni humane creature propter Deum sive regi etc., quod hoc debet intelligi de simplici populo subiecto Petro et non de sacerdotibus qui sunt excellenciores quam aliqui domini [p. 275] seculares (ut diffuse exposui in tractatu de Rege capitulo VIᵗᵒ); et ista sentencia pervertendo sensum scripture molitur a clero evertere subieccionem et obedienciam in qua fovetur religio christiana, ut patet XI, questione prima, Si tributum, et capitulo Magnum quippe, et XXIII, questione VIII De episcopis. Unde sic loquitur decretum: Medium magnum quippe est et spirituale documentum quod christiani viri sublimioribus potestatibus docentur debere esse subiecti, ne quis constitucionem terreni regis putet esse solvendam. Si enim censum Filius Dei solvit, quis tu tantus es qui non putas esse solvendum? Et sequitur in decreto sentencia beati Ambrosii et beatus Petrus apostolus generaliter omnibus fidelibus scribit: Estote subditi dominis vestris. Que sentencia cum racione videtur contraria glosse pape. Quomodo ergo non plus crederetur in isto beato Ambrosio quam sibi iuxta capitulum primum distinccione XX? Secundo idem papa in eadem decretali exponit idem Matth. XVI: Nobis, inquit, in beato Petro sunt oves commisse dicente Domino: Pasce oves meas, non distinguens inter has oves et alias ut alienum demonstraret a suo ovili, qui Petrum et successores eius magistros non recognosceret et pastores, ut illud tanquam notissimum omittamus quod Dominus dixit ad Petrum et in Petro dixit ad omnes successores ipsius: Quodcunque ligaveris super terram, nichil excipiens, quando [p. 276] dixit: Quodcunque. Ecce quam cece et presumptuose concluditur cuicunque Romano pontifici pertinere universalem preeminenciam super tota ecclesia et sic sibi. Multi namque sunt fideles qui multos Romanos pontifices nec cognoscunt pastores eorum nec membra ecclesie, quia ipsis degenerantibus a Petro alii episcopi magis proficiunt toti ecclesie militanti (ux exposui in tractatu de papa).

[ENGLISH]

## ¶6 · 276.9–276.20

> [p. 276] Ulterius vero considera quo tendit exposicio huius sententie: Quodcunque ligaveris super terram erit ligatum et in celo, nedum quod intelligitur singulariter de Petro, de ipso, et quocunque Romano pontifice, sed quod sit excepcio de quocunque quod ipse in temporalibus vel spiritualibus decreverit faciendum. Quod si per inpossibile sit verum, quilibet Romanus pontifex extollitur super omne quod dicitur Deus, cum sit Deus in terris et inpeccabilis Antichristus. Et inde dictus papa modificat quomodo imperator dominatur laycis et non clericis qui a iurisdiccione Cesaris simpliciter sunt exempti.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 272.13: The moderns will not allow that the bread remains.
- 272.18: They urge the decree of Innocent III.
- 273.5: 3.Transsubstantiation has many meanings.
- 273.14: 4. We may not credit church or angel except as Scripture and reason bid: but this decree is against both.
- 273.24: Professors of divinity and bishops may err.
- 274.5: These decrees are a very hollow reed to lean on.
- 274.17: Of all popes this was he who most disguised the Scriptures in order to snatch power from the laity.
- 276.9: The Pope's false gloss on 'Whatsoever those should bind etc.';

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 273: *doctorum* (print = bt) [SUB]
  - 274: *IIᵒ, 13:* (print = bt) [SUB]
  - 275: *contraria* (print = bt) [SUB]
  - 276: *sententie:* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 272:
2. ABC: satis edocta. 4. E: protegere. 9, 10. E: in testimonium.
18. ABDE: decretales; C: correxit. 19. D: CCCXV. 23. ABCE: gravis.
24. ABD: primo ; ib. E: que deest. 26. ABCD : quod deest. 29. D:
19. Gf. Martini Chronicon Monum. German. Scriptorcs
tom. XXII, 438: In quo fuit . . . summa prelatorum i3i5.

p. 273:
I. D: tali dubin. 2. C: racio in marg. alia manu. 9. C: vere in
marg. alia manu. 10. ABCD: sensit. 12. ABCD : ymmo hoc.
14. C: vere deesr. 20. D: nullus sanctorum. 21. D: in illa. 23. D: ut
episcopi. 24. DE: Nonne racione Saraceni. 25. ABC : sencinnt.
2'">. ABC: nos deest. AB: se deest. 29. D: hoc die.

p. 274:
3. ABCD: Sic autem; ib. D : dogmatiste. 5. E: in ista; ib. D: ideo
scilicet. 8. D : tantnm adversarii. 10. E: dimissis. 12. D: populum
commune. i3. B: cecitantis. i5. B: ipse deest; ib. C: ipse est.
18. D: fideles. 10. D: scripturam. 20. D: subtrahendo. 25. AB : quod
dicil. 26. ABCE: subiecti. 27. C: propter Deum deest; ib. C: etc. deest.
28. C: populo in marg. alia manu; ib. ABCE: de deest before sacerdotibus.
6. Duns Scotus cf. lib. IV, dist. VIII, q. II. 23. Decret.
Greg. lib. I, tit. XXXIII, cap. VI.

p. 275:
1. Codd.: in deest. 3. AB: evertetur. 6. B: et deest.
7. DE: Meum magnum; ib. C: est deest; A: est in marg. alia manu.
9. D: subditi. i3. ABC: sentencia deest; E: sancti; ib. E : et Bernhardi.
i5. B: subiecti; ib. B: domini; ib. B: cum deest. 20. D: a beato.
23. AB : eius deest; C: alia manu add.; ib. AB : magislros suos.
25. ABDE: amittamus ; C: admittamus. Correxi ; ib. ABCE: Qiiod enim;
Dominus deest. 26. D : et deest; ib. A: ad in marg. 27. E: ligaveris etc.
1. Cf. Wyclifs, De Officio Regis, cap.VI, pag. i3q. 5. Decr.
Sec. Pars, Caus. XI, quaest. I, cap. XXVII; ib. cap. XXVIII.
6. ib. Causa XXIII, q. VIII. 18. Dist. XX, II Pars, § 1.
19. In eadem decretali, i. e. Solitae ; ib. § VI.

p. 276:
1. C: sumptuose ; pre alia manu add. 3. ABC: eminenciam ; Codd : de
papa in tractatu. 12. ABC : et de. i3. C: fit excepcio. 14. ABCE: ipsi;
ib. ABCE: decreverunt. i5, 16. B: quibus Romanus. 17, 18. C: Anti-
chrisius in marg. alia manu. 21. D: ex isto. 25. AB: quia omnia.
26. ABC : si sunt. 29, 3o. ABDE: et de calice bibat deest.
9. Rectius (ut videtur) De Potestate pape (inprinted).
16. I. Thess. H, 4. 24. Cf. De Maioritate et Obed. cap. Solitae
et InnoCcntii III. ep. lib. I, ep. 401.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 272: tali dubio.
p. 274: Subditi estote omni humane creature propter Deum sive regi etc. }
p. 275: Si tributum, | Magnum quippe, | De episcopis. | Medium magnum quippe est et spirituale documentum quod christiani viri sublimioribus potestatibus docentur debere esse subiecti, | ne quis constitucionem terreni regis putet esse solvendam. Si enim censum Filius Dei solvit, quis tu tantus es qui non putas esse solvendum? | et beatus Petrus apostolus generaliter omnibus Jidelibus scribit: Estote losubditi dominis vestris. | in beato Petro sunt oves commisse dicente Domino: Pasce oves meas, non distinguens inter has oves et alias ut alienum demonstraret a suo ovili, qui Petrum et successores eius magistros non recognosceret et pastores, ut illud tanquam no- | tissimum omittamus quod Dominus dixit ad Petrum et in Petro dixit ad omnes successores ipsius: Quodcunque ligaveris super terram, nichil excipiens, quando
p. 276: dixit: Quodcunque. | Quodcunque ligaveris suver terram erit m | ligatum et in celo, | extollitur super omne quod dicitur Deus, | Fecit Deus duo luminaria. luminare maius, ut preesset diei et luminare minus ut preesset nocti, | Probet autem se ipsum homo et sic de pane illo edat et de calice bibat.
```

---

## Chunk 09-b: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-09-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-09-b
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "276.21–280.16"
divisions: "cap. 9 (heading 'CAPITULUM NONUM.' at 272.0); part 2 of 14, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "864 words; 842 confirmed by the vote; 17 runs stood by rule; 5 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n347–n351 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 9, part 2: [TITLE]

## ¶1 · 276.21–277.14

> [p. 276] Tercio vero extorquet ex illo Gen. Iᵒ, 16: Fecit Deus duo luminaria, luminare maius, ut preesset diei et luminare minus ut preesset nocti, quomodo Spiritus Sanctus per illud intenderat ipsum et omnes Romanos pontifices super omnes cesares preeminere. Que omnia si sint vera, quomodo pendebit sensus scripture derivandus toti ecclesie a tali capite? Unde solebam sciscitari a satrapis sensum huius Iᵃ Cor. XI, 28: Probet autem se ipsum homo et sic de pane illo edat et de calice bibat. Manifestum (inquam) videtur quod loquitur [p. 277] de hoc sacramento corporis et sanguinis Domini, sicut ante: Panis quem frangimus, nonne participacio corporis Domini est? Et quocienscunque manducabitis panem hunc etc. Quicunque manducaverit panem vel biberit calicem etc. Omnia enim ista intelliguntur de pane in cena Domini manducato. Non autem audemus asserere illum esse sensum Spiritus Sancti: De pane illo edat, hoc est, de accidentibus illis edat, frangimus vel quod panis quem frangimus, hoc est, accidencia que frangimus hoc figurant, quia oporteret specificare illa accidencia quod nesciunt; nam securius est loqui vocando illud panem, ut facit evangelium Apostoli, quousque habuerimus revelacionem vel racionem de sensu extraneo.

[ENGLISH]

## ¶2 · 277.15–277.29

> [p. 277] Et confirmacio illius est quod beatus Augustinus sepe respondet in talibus quod ideo sic loquitur, quia sacra scriptura sic loquitur. Quare ergo debemus nos pocius quam doctores sancti modum loquendi scripture sacre deserere? Et specialiter propter tam extraneam sentenciam ex aliis lapsibus tam suspectam. Unde inter alia valde suspectum est quod decretalis nec racionem nec scripturam sacram allegat pro sensu quem exprimit. Ideo cum testificacio non sit maior quam quatuor magnorum doctorum, ut docet decretum, illi autem prohibuerunt credi dictis suis, nisi de quanto scriptura sacra vel racio ipsa docent, que ergo racio credendi vel capiti in hoc parte? Honorare tamen debemus et glossare dicta papalia quantum permittit religio christiana.

[ENGLISH]

## ¶3 · 278.1–278.24

> [p. 278] Nec contendo quod iste Innocencius irreligiose subiugavit sibi Angliam obligacione nimis civili in nongentis marcis solvendis curie annuatim, seminavit discordiam inter Angliam et Franciam, contra imperatorem et alios seculares dominos, contra abbatem Joachim et alios irreligiose processit, ut narrat Cestrensis libro septimo, capitulo XXIV et infra; temporeque suo duo ordines Fratrum inceperant, sed multa mala passa fuit ecclesia quod figuratum est portento multiplici. Nam crescente secta signa colencium ultra religionem quam Christus instituit crescere oportet irreligiositatem fictam in signis. Multa autem opera insignia dereliquit, ut tractatum De Miseria condicionis humane et magnam partem sentencie quinque librorum decretalium; sed non ceperunt auctoritatem ab eo, cum successit post eum Honorius tercius qui dicitur confirmasse ordines fratrum Predicatorum et Minorum, et post eum successit Gregorius IX qui quinque libros decretalium per fratrem Raymundum dicitur compilasse. Et utrobique dicuntur opera eius laudanda primo de quanto consonant legi Dei. Nec dicet aliquis quod dicta sua (in quantum sua) sunt magis autentica quam glossa Innocencii quarti quam ecclesia per se acceptat, in quantum consonat veritati.

[ENGLISH]

## ¶4 · 278.25–279.10

> [p. 278] Quinta autem responsio in qua senex fideliter potest quiescere stat in isto quod, cum videtur esse scrupulus in determinacione ecclesie, quiescendum est humiliter in sentencia antiqua magis probabili, quousque ecclesia declaraverit veritatem. Ponit enim synodus sub Nicholao IIᵒ expresse quod panis et vinum que in altari [p. 279] ponuntur sunt post consecracionem non solum sacramentum sed corpus Christi et sanguis. In nulla autem decretali sequenti tam expresse ponitur quod post consecracionem non remanet panis aut vinum eukaristia, et interim volo parate acquiescere racioni, quia scio quod in nullius pape potestate est cum millesies mille satrapis determinare quidquam de fide katholica, nisi quod reperire poterunt in scriptura, quia aliter indubie foret Antichristus et plus quam Deus, potens totam fidem quam credit christianismus subvertere.

[ENGLISH]

## ¶5 · 279.11–279.17

> [p. 279] Secundo arguitur contra dicta per hoc, quod potissima racio cui via ista innititur est Nicholai IIⁱ testimonium et sinodus quam ipse congregavit pro ista materia (ut patet De Consecracione, distinccione IIᵃ, Ego Beringarius). Cum ergo hoc argumentum sit in eadem dampnacione qua testimonium decretalis quod spernitur, videtur quod ista sentencia sit suspecta.

[ENGLISH]

## ¶6 · 279.18–279.30

> [p. 279] Hic dictum est quod decretum Nicholai IIⁱ est probabilius, non solum quia ibi fuerunt plures episcopi, vel quia fuit antiquius, fonti fidei christiane propinquius, sed eo potissime quod fonti fidei scripture est similius et sanctis doctoribus conformius. Unde non propter loquelam illius synodi sed propter veritatem fidei scripture debet pocius credi priori sentencie; nec solum debet credi cuicunque parti scripture plus quam millies mille episcopis eciam Romanis vel Avinonicis sub racione qua tales, verum eciam plus beato Augustino et aliis sanctis doctoribus quoad materiam fidei quam papis et cardinalibus qui non sunt in fide scripture adeo approbati.

[ENGLISH]

## ¶7 · 279.31–280.16

> [p. 279] In hiis autem que concernunt leges quas fabricant sunt boni iudices, quia ut dicit Jeronimus, quod medicorum [p. 280] est medici tractant, fabrilia fabri. Et ista est sentencia legis ecclesie distinccione XXᵃ in principio. Si autem simea in tecto se simulat scire quod nescit, bonum est temptare, si opere, vita et auctoritate scripture confirmat quod fingit; lex namque nature quam philosophi detegunt immediate et testimonia Augustini et aliorum sanctorum recitata superius satis docent quod accidencia de quibus loquebantur philosophi non possunt esse sine subiecto. Qua ergo presumpcione seminarent isti contrariam infidelitatem quam nec sciunt colorare racionibus nec scriptura? Quo ergo colore debet fidelis hoc credere? Cum ergo secundum Augustinum credere non potest nisi volens, patet quod preceptum eciam Romani pontificis non est ad hoc efficax nisi supra preceptum adduxerit in testem vel naturalem evidenciam vel scripturam.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 276.21: and on the two lights.
- 276.25: What a head to draw doctrine from!
- 277.15: Let us follow Augustine in holding by Scripture.
- 277.22: The decretal alleges neither Scripture nor reason on its behalf.
- 278.1: Shortcomings of Innocent III.
- 278.25: 5. There is an older decree opposed to this; and where the utterance of the Church is doubtful we must rest on reason.
- 279.11: Our opponents say that we are only setting one decree against another.
- 279.18: We reply that we prefer it a) as earlier and nearer the fountain head, but far more b) because it agrees with Scripture,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 277: *illi* (print = bt) [SUB]
  - 278: *IIᵒ* (print = bt) [SUB]
  - 279: *IIⁱ* (print = bt) [SUB]
  - 279: *IIⁱ* (print = bt) [SUB]
  - 280: *XXᵃ* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 276:
1. C: sumptuose ; pre alia manu add. 3. ABC: eminenciam ; Codd : de
papa in tractatu. 12. ABC : et de. i3. C: fit excepcio. 14. ABCE: ipsi;
ib. ABCE: decreverunt. i5, 16. B: quibus Romanus. 17, 18. C: Anti-
chrisius in marg. alia manu. 21. D: ex isto. 25. AB: quia omnia.
26. ABC : si sunt. 29, 3o. ABDE: et de calice bibat deest.
9. Rectius (ut videtur) De Potestate pape (inprinted).
16. I. Thess. H, 4. 24. Cf. De Maioritate et Obed. cap. Solitae
et InnoCcntii III. ep. lib. I, ep. 401.

p. 277:
I. B: de sacro ; ib. ABDE: et sanguinis deest. 3. C: est etc.
4. D: Et quicunque. 5. ABDE: calicem deest. 6. D: audeo.
7. D : istum. 8. C: illo etc; ib. edat deest. 10. C: oportet.
II. D: Xon securius. 12. A: quod vocat evangelium. i3. B: vel
relacionem deest. 16. D: quia. 18. E: modo. 20. AB: lapsis ;
C: correxit. 23. B: non fil. 25. E: nec de. 26. B: ita docent ; ita
in marg. 28. AB: dicta probabilia ; C: probabilia in textu; papalia in
marg. alia manu.

p. 278:
5. D: abbothem. 14. C: quinque in marg. alia manu. 20. D: lauda-
bilia. 21. DE: dicit ; C: dubitet in marg. alia manu. 22. ABCE: dicta
sentencia; ib. C: sit. 23. per se ; D: prime. 24. D: acceperat;
ib. D: de quanto. 26. dicitur in tcxtu; videtur in marg.
2. Cf. Wyclifs Sermones II, 424. 6. De abbate Joachimo
de Flora (in Calabria) cf. Jocher, Gelehrten-Lexikon (II, i8o3),
Fabricius, Bibl. lat. med. act. IV, 328. 3o. Decret. Tert. Pars,
De Consecr. dist. II, cap. XLII.

p. 279:
4, 5. B: eucaristie. 6. D: et cum. 8. ABCE: poterit.
i3. ABCE: quem. i5. DE: assumptum. 17. ABCD : est. 19. ABCE:
sunt. 24. C: fideim marg. alia manu. 25. C: partixn marg. alia manu.
26. D: millesies. 32. AB: quia dicit; C in marg. alia manu: videlicet.
14. Decr. Tert. Pars, De Gons. dist. II, cap. XLII.

p. 280:
1. E: promittunt medici tractant. 2. C: legis in marg. alia manu.
4. ACDE: temperare; ib. si; ABE: scilicet ; C: corr. in marg. ; ib. E:
opere et. 6. Codd.: quo (C: ymo) mediante est. 8. E: loquebantur
per hoc. 9. ABCE: quam. 10. C: sumpcionem; pre in marg. add.:
ABCE: presumpcionem ; ib. AB : contra; C in marg. alia manu: contraria.
12. E: fideles; C: fidelis in marg. alia manu. i5. B: adduxerint.
22. C: in ecclesia in marg. alia manu. 23. A: concludit in marg. alia
manu; in textu : eoniungit; BDE: coniungit.
2. Dist. XX, L pars: Decretales itaque epistolae canonibus
conciliorum pari iure exaequantur. Nunc autem quaeritur de
exposicionibus sacrae scripturae. An exaequentur: .... Unde
nonnullorum pontificum constitutis Augustini, Hieronvmi ....
dicta videntur esse praeferenda. i3. Cf. Opp. X, 118 et seqq.
III, 2, 006. II, 676. 22. Eph. IV, 11.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 276: dixit: Quodcunque. | Quodcunque ligaveris suver terram erit m | ligatum et in celo, | extollitur super omne quod dicitur Deus, | Fecit Deus duo luminaria. luminare maius, ut preesset diei et luminare minus ut preesset nocti, | Probet autem se ipsum homo et sic de pane illo edat et de calice bibat.
p. 277: Patiis quem frangimus, nonne participacio corporis Domini est? | quocienscunque manducabitis panem hunc | Qidcunque manducaverit panem vel Sbiberit calicem | De pane illo edat,
p. 278: panis et vinum que in altari
p. 279: ponuntur sunt post consecracionem non solum sacramentum sed corpus Christi et sanguis. | Ego Berin- | quod me-
p. 280: dicorum est medici tractant, fabrilia fabri. | sint simul pastores et doctores
```

---

## Chunk 09-c: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-09-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-09-c
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "280.17–284.31"
divisions: "cap. 9 (heading 'CAPITULUM NONUM.' at 272.0); part 3 of 14, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "992 words; 966 confirmed by the vote; 21 runs stood by rule; 5 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n351–n355 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 9, part 3: [TITLE]

## ¶1 · 280.17–281.17

> [p. 280] Quod si obicitur necessario aliquos esse qui autentice doceant sensum scripture et alias veritates katholicas quas scriptura non exprimit, ut patet de beato Augustino contra Donatistas et multis aliis articulis fidei adiectis: hic dicitur quod necesse est aliquos esse preeminentes in ecclesia qui sint simul pastores et doctores (ut concludit Apostolus) et illis oportet credere non tanquam auctoribus sed tanquam doctoribus. Quod si prelati errant in pastu et circa mundana [p. 281] solliciti christiane fidei sunt ignari: quomodo curremus in isto ad ipsos ut capita ydolorum? Quod si desunt tales, melius est quiescere in fide explicita quam habemus quam suscitare novam sentenciam; ymmo ignoto sensu mistico vel litterali secundario melius est pausare in sensu rudi, relinquendo Spiritui Sancto cum sanctificacione vite sensum alium quam infundabiliter sculpere novum sensum. Unde quia secure possumus vocare eucaristiam panem, ut notat fides scripture cum sanctis doctoribus, debemus ad imitacionem eorum illud eligere et ambiguum de corpore isto vel alio accidente ignoto respuere nisi forte declaretur revelacione. Sed Deus non tardaret revelare fidem istam carioribus eius discipulis; nec credo Augustinum vel alios sanctos innovare quidquam credendum ecclesie nisi elaboratum ex fide scripture.

[ENGLISH]

## ¶2 · 281.18–281.30

> [p. 281] Unde utinam nostri considerarent fundamentum Augustini contra Donatistas. Nam evangelium precipit homines baptisari, non precipiendo baptismi iteracionem. Sic nec lex Christi nec eius cerimonie debent gravari sine auctoritate scripture: ergo iugum difficultacionis ecclesie non est sibi inponendum multiplicando baptismum. Tota ista sentencia patet ex fide scripture et sic occasione male data ab emulis sollicitabant se sancti ultra expressionem fidei ecclesie primitive. Et observata perfecte ista sentencia nunquam oneraretur ecclesia ad credendum quod eukaristia sit quantitas sacra. Et ita dicitur generaliter de omni fide a sanctis doctoribus noviter expressata.

[ENGLISH]

## ¶3 · 281.31–281.33

> [p. 281] Tercio arguitur contra hoc per glossas decretorum et famosos doctores qui scripserant contrarium super illa materia: illis ergo oportet credere plus quam nobis.

[ENGLISH]

## ¶4 · 282.1–283.17

> [p. 282] Hic dicitur quod nulli pure creature credendum est nisi ut testi, non ut domino veritatis, in tantum quod Christus venit in mundum humanitus, ut testimonium perhibeat veritati et cum omnis veritas sit in scriptura (ut dicit Augustinus), patet quod nulli creature credendum est nisi de quanto fundaverit se in scriptura; quanto magis nos testes abiecti debemus dolere de errore in falsitate et testificare quantum ex fide scripture sufficimus veritatem et docto errore nostro humiliter revocare. In testem autem veritatis non debet accipi nisi qui habuerit eius noticiam, in tantum quod in veritate facti humani non debet secundum poleticos capi in testem nisi qui de ipso noticiam habuerit, quia aliter testis foret necessitatus mentiri. Et in isto inpugnatur quedam lex Anglie, que necessitare videtur testem asserere quod vel distincte scit vel non scit quis commisit facinus perpetratum. Et hec est racio quare leges ecclesie quoad fidem scripture plus credunt quatuor sanctis doctoribus et specialiter Augustino quam aliis quos credunt nec ex dono Dei nec ex studio humano tantum de veritate fidei cognovisse. In ambiguis tamen credendum est illis evidencia topica, exspectando inspiracionem auctoris fidei a quo est omnis noticia nostra veritatis; de veritate autem et sufficiencia scripture non licet ambigere. Ideo cum nullibi docet, vel quod eukaristia sit aliquid de novem generibus accidentis vel quod potest ipsum permittere per se esse, sed periciores sancti dixerunt oppositum, videtur stultum recentes diffinire sic esse de facto et cum illo ut fide onerare [p. 283] ecclesiam. Stetit enim sponsa Christi in floribus (ut creditur) circiter mille annos, antequam fuerit onerata ista perfidia, quia usque ad indebitos cultores. Et patet quod doctores legum hominum sunt valde suspecti in ista materia, cum spissim ex ignorancia seminant hereticos sensus. In ambiguis autem extra fidem scripture solent periti silere vel ipsa abicere curiosis, concedentes quod expedit nobis nedum multa ignorare sed nec cogitare, cuiusmodi sunt impertinencia fidei. Itaque quantum ad glossatores, patet ex dictis quod non debet credi illis et specialiter in ista materia nisi de quanto se fundaverint in racione vel scriptura autentica. Unde propter perplexitatem illius materie datam a nostris novellis doctoribus glossatores decretorum titubant et discordant; ideo dictum eorum in ista materia non est argumentum nisi ad hominem.

[ENGLISH]

## ¶5 · 283.18–284.4

> [p. 283] Quantum ad doctores legis, dicit primus, et precipuus videtur esse Lanfrancus abbas Beccensis in libello suo contra Beringarium De Sacramento Altaris, ubi videtur inpugnare quod panis et vinum remanent post consecracionem sed in consecracione desinunt. Iste autem Lanfrancus, licet fuerit sanctus, aliunde tamen in sua inveccione inartificiose procedit, quia sine evidencia nunc contendit modo quo abbas solet alloqui suos novicios et nunc simulat falsa contra que arguit. Non enim invenit homo in toto scripto suo (si non fallor) nisi evidenciam triplicem: Prima si panis remanet, tunc sacramentum parvi panis indignius est quam manna. Secunda racio est quod prophecia veteris testamenti figurans corpus Christi de futuro foret sollempnius quam nostrum sacramentum quod habet [p. 284] nudam efficaciam ad signandum corpus Christi de preterito; quod cum non sit prophecia sed veritas de preterito, ydiota sciret ostendere. Et tercia racio stat super decretis ecclesie que allegat.

[ENGLISH]

## ¶6 · 284.5–284.14

> [p. 284] Quantum ad primum, patet quod racio militat (ut dixi) sepius contra ipsum, cum secta ista ponit quoad essenciam sacramentum illud vel unum nichil vel unum abiectissimum in natura quia accidens infinitum inperfeccius quam est panis et per consequens infinitum abieccius quam est manna quod de celo descendit; ideo nemo inveniet colorem efficacem ad illud nisi loquendo yronice dicatur quod est irreligiose propter devocionem populi menciendum (de qua materia dixi diffuse alibi).

[ENGLISH]

## ¶7 · 284.15–284.31

> [p. 284] Quoad secundum patet quod false assumitur professio Beringarii, cum decretum de ipso recitat quod confessus fuit secundum informacionem ecclesie, quod panis est post consecracionem nedum sacramentum, ut in errore suo confessus est, sed verum corpus Christi, hoc est figurat efficaciter, ut sacramentum nove legis, verum corpus Christi sacramentaliter ibi presens. Nec plus dicit adversarius; unde creditur Lanfrancum arguere contra eum pro dictis suis hereticis ante suam correccionem. Sed quid hoc ad nos? vel quod metu et non fide Beringarius ista dixit in sinodo? et sic sacramentum eukaristie non solum dicit veritatem corporis Christi de preterito sed facit quod verum corpus Christi sit vere et realiter ibi presens; quod non fecerunt sacramenta legis veteris. Nec ad hoc pertinet desicio nature panis vel eius destruccio.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 280.17: It is said there must be authority somewhere to expound Scripture.
- 281.2: If we have no competent prelates we had best keep to the literal sense of Scripture.
- 281.18: Augustine's ground against the Donatists was that rites ought not to be imposed without scriptural authority.
- 281.31: 3. We are confronted with doctors of more weight than we.
- 282.1: Creatures can be but witnesses, not lords of truth. They must rest on Scripture and must know what they witness.
- 283.5: There are many doubtful things which we need not care about.
- 283.10: The glosses contradict each other so much that they count for nothing.
- 283.17: Of doctors of law the chief is Lanfranc, but he never really meets the question.
- 284.5: He says, we honour the host insufficiently, but our opponents degrade it to a mere accident.
- 284.15: On the point of Berengarius' confession, he does not touch us, for his attack is against the error renounced.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 281: *curremus* (print curremus (bt currremus)) [SUB]
  - 282: *Christus* (print = bt) [SUB]
  - 283: *Christi* (print = bt) [SUB]
  - 283: *impertinencia fidei. Itaque* (print = bt) [SUB]
  - 284: *celo* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 280:
1. E: promittunt medici tractant. 2. C: legis in marg. alia manu.
4. ACDE: temperare; ib. si; ABE: scilicet ; C: corr. in marg. ; ib. E:
opere et. 6. Codd.: quo (C: ymo) mediante est. 8. E: loquebantur
per hoc. 9. ABCE: quam. 10. C: sumpcionem; pre in marg. add.:
ABCE: presumpcionem ; ib. AB : contra; C in marg. alia manu: contraria.
12. E: fideles; C: fidelis in marg. alia manu. i5. B: adduxerint.
22. C: in ecclesia in marg. alia manu. 23. A: concludit in marg. alia
manu; in textu : eoniungit; BDE: coniungit.
2. Dist. XX, L pars: Decretales itaque epistolae canonibus
conciliorum pari iure exaequantur. Nunc autem quaeritur de
exposicionibus sacrae scripturae. An exaequentur: .... Unde
nonnullorum pontificum constitutis Augustini, Hieronvmi ....
dicta videntur esse praeferenda. i3. Cf. Opp. X, 118 et seqq.
III, 2, 006. II, 676. 22. Eph. IV, 11.

p. 281:
3. DE: non fidc. 9. AB: eucaristiam deest; C: alia manu.
14. D: istam dcest. 19. DE: precepit. 21. ABCD: sed nec.
24. D : totum. 25. E: sic dcest ; ih. ABC: male ; ib. AC: sollicitarent.
32. ABC: contraria; D: eontrariam; ib. ABD : supra. 33. B: plus decst.

p. 282:
8. D : testijicari. 11. ABDE : eius decst ; C : alia manu. 12. AB : facti
hic materia; C : humani in rasura. i3. poleticos ; ADE: polites ib. E: ipsa.
16. ABC: vel quod; ib. ABDE: disiuncte ; C: dislincte in rasura.
18. DE: est deest. 21. AB : e.x omitied beforc studio. 23. ABC: tropica ;
ib. E: revelacionem. 28. AB: potest deest; C: alia manu addit.
4. S. Augustini Contra Faustum XIII, 5, Opp. VIII, 2:4, De
Baptismo contra Donatistas II, 3, Opp. IX, 98.

p. 283:
6. D: sensum hereticos; E: sensus hereticos; ib. ABC: autem deest;
E: aut. 7. E: soluciones periti. 9. D: ignorari. l3. D: in quanto.
i5. D: a deest. 22. D: desinit. 23. E: fuit. 24. D: invocacione.
20. Lanfranci Opp. ed. Giles II, i63

p. 284:
5. D: Quia racio. 8. B: unum adiectum. 10. DE: est deest.
20. E: est deest. 22. ABC: ut plus; ib. C: dicit alia manu. 26. E: sic
decst; ib. AB : non solum non. 29. C: Jecerunt alia manu.
28. Cf. De Apostasia, pag. 164.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 280: dicorum est medici tractant, fabrilia fabri. | sint simul pastores et doctores
p. 282: omnis ventas sit in scnptura
p. 284: panis est post consecracionem nedum sacramentum, | sed verum corpus Christi,
```
