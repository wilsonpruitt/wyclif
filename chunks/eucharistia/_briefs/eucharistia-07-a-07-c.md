# Translation brief: eucharistia 07-a–07-c

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/eucharistia/wyc-eucharistia-07-a.md chunks/eucharistia/wyc-eucharistia-07-b.md chunks/eucharistia/wyc-eucharistia-07-c.md` once and fix what it reports.
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

## Glossary (the 436 rows these chunks use; the full file is GLOSSARY.md)

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
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |
| sacramentum (the eucharist); sacramentum altaris | sacrament; the sacrament of the altar | The plain sense, against the Augustinian row (*Incarn.*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.3, 3.30). |
| hostia; hostia consecrata | host; consecrated host | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.11, 1.22). |
| panis / vinum | bread / wine | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.8). |
| corpus Christi / corpus Domini | the body of Christ / the body of the Lord | Kept apart as the Latin alternates them. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.6, 1.10). |
| novella ecclesia / antiqua ecclesia | the newer church / the ancient church | The pair of 3.3; cf. *novelli*. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 3.3). |
| cultores accidencium / signorum | worshippers of accidents / of signs | Wyclif's name for the defenders of the accident without a subject. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 6.15, prol-c 10.2). |
| claritas (of the glorified body) | clarity | The dowry of the glorified body (with agility, subtlety, impassibility); not "brightness". Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-c). |
| fractio; fractura (of the host) | breaking | *Lauda Sion* *signi tantum fit fractura*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 13; 21.31). |
| species (of bread and wine) | species | The sacramental species; kept as the term, not "appearance". Distinct from the logical *species*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 13.15; 23.8). |
| sacer; sacrare | sacred; hallow | Kept apart from *sanctus / sanctificare* "holy / sanctify" and from *consecrare*; *consecrare* is "to hallow together" in the grammarians' etymology. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 27–28). |
| sacramentum tantum | a sacrament only | The *sacramentum tantum* of the Lombard's three (IV d. 8 c. 4). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 29.23). |
| conversio (eucharistic) | conversion | Of bread into the body; kept apart from *conversio* of a proposition. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 48.15). |
| decretalis | decretal | Kept apart from *decretum* "decree". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 71.31). |
| principaliter; principalitas (of the body's presence) | principally; principality | Of the body of Christ alone being in the sacrament as its principal; not the compendium's *principaliter* "as a main head". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 75.5–26). |
| transaccidentacio | transaccidentation | Wyclif's coinage beside *transsubstanciacio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 81.27). |
| transinferioracio; transsubieccio | transinferioration; transsubjection | Coinages in the same series. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 82.3). |
| baptiste signorum | baptizers of the signs | Not "Baptists". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 81.29). |
| consecracio | consecration | The noun of *consecrare*; see *confeccio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 99–100). |
| transaccidencia | transaccidents | In the *transaccidentacio* series. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 145.4). |
| corpus dominicum | the Lord's body | Kept apart from *corpus Domini* "the body of the Lord" and *corpus Christi*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 158.31, 165.3). |
| in circulo (of the host) | in a round | The round form of the host. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 161.17). |
| nominacio (baptismatis) | naming (of our baptism) | Wyclif's figure for the name the faithful bear. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 172.21). |
| sanctificacio | sanctification | Ruled 2026-11-07 (coordinator, delegated; *Euch.* 189.6). |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). Third referent, the logician's arrangement of terms in a proposition (*Incarn.* 49.10): "ordering", with a **C** note; ruled 2026-10-22 (coordinator, delegated). |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| potencia regulata racione | power regulated by reason | Pilot. |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| censura | censure | Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| possessionati | the possessioners | Endowed religious. |
| protestacio; protestari | declaration; to declare solemnly | ⭐ The submission formula ("if anyone can teach me this is contrary to scripture or reason, I will humbly retract"). Penn and Lahey both inverted it (T. pp. 369, 378). Render it as a retraction offer, never as defiance. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | CONTEXTUAL: condition / respect | "Condition": a person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). "Respect": the logical relation under which a predicate holds (*posiciones secundum habitudinem*), with a **C** note; ruled 2026-10-22 (Wilson; *Incarn.* 4.16). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| decretum; decreta | decree; the decrees | Gratian (*in decretis*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.14, 3.24). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
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
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |
| humanitas | the humanity | The nature the Word assumed, body and soul; with the article (*humanitas sit Christus*, "the humanity is Christ"). Not "the human nature", which is *natura humana*. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| ydemptitas specifica | identity of species | That Christ and other men are of one species. Not "specific identity" (reads as "particular"). Ruled 2026-10-22 (Wilson; *Incarn.* prol, 8). |
| Verbum | the Word | Pronoun **"he"** (as Douay–Rheims John 1:3, "by him"), never "it", though the Latin is neuter; so also *Sapiencia* where Wisdom is the Word in person (*Incarn.* 7, coordinator). Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.3–4). |
| homo assumptus | the assumed man | A term of art (the Lombard's first opinion, *Sent.* III d. 6); keep "assumed" before "man", never "the man assumed". With the agent expressed (*homo assumptus a Verbo*) "the man assumed by the Word", which cannot be misread (coordinator, 2026-10-22). Ruled 2026-10-22 (Wilson; *Incarn.* 5.15). |
| secundum quod (reduplicative) | insofar as | ⛔ Never "in that" (heard as "because", which inverts the logic). Ruled 2026-10-22 (Wilson; *Incarn.* 5.29–6.24). |
| secundum deitatem / secundum humanitatem | as to the Godhead / as to the humanity | The rule of reduplication; keep it in Wyclif's place in the sentence. ⛔ Never supply "as God / as man" where the Latin has bare apposition (*ipse Deus*) or bare predication. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| natura | nature | Ruled 2026-10-22 (Wilson; *Incarn.* 3.4). |
| persona | person | Ruled 2026-10-22 (Wilson; *Incarn.* 4.14). |
| creatura / creator / creatus | creature / creator / created | ⛔ Never "creation" for the created thing. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| posicio / proposicio / predicacio | position / proposition / predication | Kept apart: the apparatus shows the three trading places (*Incarn.* 4.15). Ruled 2026-10-22 (Wilson). |
| sacramentum (of the incarnation, of creation) | sacrament | The Augustinian sense, "mystery" (1 Tim. 3:16): G note at the first occurrence in the chunk. Kept apart from *misterium*. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.8). |
| sancti | the saints | The fathers. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.15). |
| abstractive | abstractively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 10.6). |
| sophistice | sophistically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 15). |
| de vi vocis / de vi sermonis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| protervus | obstinate | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21). |
| nedum | not only | "Let alone" where the sense is a fortiori. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21, 24). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| exinanicio / exinanire / inanicio | emptying / empty | Phil. 2:7 (Douay "emptied himself"); *inanicio* (*Incarn.* 33) the same. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| minoracio | lowering | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| humanitus | humanly | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* passim). |
| suscipere / suscepcio (of the soul, the nature) | take up / taking-up | Kept apart from *assumere* "assume". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 31). |
| individuum | individual | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 35.7). |
| in quantum (reduplicative) | insofar as | As *secundum quod*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37.9). |
| unio | union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 39). |
| universitas creaturarum | the totality of creatures | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37). |
| pars qualitativa | qualitative part | Body or soul as the parts that make up a man by kind; set against *pars quantitativa*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 43.5). |
| pars discretiva | discrete part | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 46.9). |
| in effectu | in actual fact | As against in potency or in name; ⛔ not "in effect" (modern "virtually"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 47.10). |
| animare | animate | The argument turns on it (45.30–46.4). Ruled 2026-10-22 (coordinator, delegated). |
| predicacio actualis / aptitudinalis / habitudinalis / mixtim | actual / aptitudinal / habitudinal / mixed predication | *Habitudinalis* is its own term (the four MSS at 49.6), not under *habitudo*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.5–16). |
| denominativum | denominative | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 50.30). |
| Doctor Subtilis | the Subtle Doctor | Scotus. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.24). |
| convertibilis / converti | convertible / be convertible | Of terms. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 52.29). |
| forma totalitatis | form of totality | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 50.7). |
| quantus | quantified | The adjective beside *quantitas*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.22). |
| carneus / carnalis | fleshy / carnal | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.21). |
| per se / per accidens | CONTEXTUAL: of itself / by accident; (spatial) apart, by itself | The spatial sense (a thing set apart, *Euch.* 104.16–17) gets a G note. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a (sufficienti) divisione | the topic from sufficient likeness / from (sufficient) division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| libere contradictorie | freely, as between contradictories | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 76.15). |
| inconsequens | inconsistency | Kept apart from *inconveniens* (an unfitting conclusion). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 78.23). |
| ydemptitas ypostatica | hypostatic identity | Beside *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 84.20). |
| capitales doctores | the chief doctors | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| eiusdem / consimilis / alterius racionis | of the same / like / another kind | The species-sense of *racio*; *racio speciei* "the account of the species" (Aristotle's *logos*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.4, 87.17). |
| principiari | be constituted from principles | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.7). |
| accidentatus | subject to accidents | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.4). |
| in recto / in obliquo | in the direct case / in an oblique case | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.25). |
| signum / signatum | sign / thing signified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 91.2–6). |
| conveniencia / convenire (*in*) | agreement / agree | The argument of 90–91 turns on it; not "fittingness" (that is *congruencia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 90). |
| predicacio synecdochica | synecdochic predication | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.27). |
| conversari | live one's life (among men) | Beside *conversacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.25). |
| esse intelligibile | intelligible being | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 99.23). |
| extraneare / extraneacio (supposicionis) | estrange / estrangement (of supposition) | *Affeccio extraneandi* "an affection of estrangement". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 98.16). |
| ministerialiter | ministerially | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 100.17). |
| res racionis | thing of reason | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| universitas creata | the created totality | Beside *universitas creaturarum*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| significatum | significate | Kept apart from *signatum* "thing signified". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 111). |
| predicacio secundum essenciam / formalis | predication by essence / formal predication | Wyclif's modes of predication (cf. *predicacio secundum causam*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 115–116). |
| forma substancialis | substantial form | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| concepcio (figure) | conception | The grammatical figure. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habitus (of the humanity) | habit | The Lombard's third opinion (*Sent.* III d. 6). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| accidens | accident | The category; *accidit* "befalls". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habitacio | habitation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 120.14). |
| denominacio respectiva | relational naming | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 120.17). |
| figura / figuratum | figure / thing figured | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 121.23). |
| conversio (of a proposition) | conversion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.30). |
| humanitacio | humanation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 126.12). |
| racio (individual, personal) | account | *Racio individui / persone* "the account of an individual / a person", as *racio speciei*; not "aspect" (the row against *substancia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 8, 129–132). |
| vir (against *homo*) | man (*vir*) | Where Wyclif sets *vir* against *homo*, the Latin in parentheses. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 129.15–26). |
| res secunde intencionis | things of second intention | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.25). |
| materia proxima / remota | proximate / remote matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137.1). |
| personari | be made a person | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 134.10). |
| colorate | with colour enough | With a plausible ground (cf. *color*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 134.26). |
| ydemptificare / ydemptificacio | identify / identification | Make the same (*idem*); the hypostatic union as identification, not conversion or generation. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 142.19, 147.22). |
| res communis / res communes | the common thing / common things | The realist universal the *moderni* do not conceive (first root of their error). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 144.27). |
| distinccio racionis | distinction of reason | Beside *differencia formalis*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 145.23). |
| conversio naturarum / confusio naturarum | conversion of the natures / confusion of the natures | Kept apart from *conversio* of a proposition. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 143.9). |
| principiare (active) | be the principle of | Beside the passive *principiari* "be constituted from principles". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 147.4). |
| concretum / abstractum | concrete [term] / abstract [term] | *Homo* the concrete, *humanitas* the abstract. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 152). |
| transsumpcio | transumption | Beside *transsumptive*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 153.28). |
| personalitas | personality | The scholastic term: what makes a person a person, not character. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 155). |
| nativitas | nativity | Christ's twofold birth. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 155). |
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
| risibilis / risibilitas | risible / risibility | The proper attribute of man. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 181). |
| mocio / motus (paired) | motion (*mocio*) / movement (*motus*) | Only where Wyclif pairs them; otherwise "motion". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 180). |
| causancia / causacio | causing / causation | Kept apart (both at 187.30–34). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 185.16). |
| personare (active) / personacio | make a person / personation | Beside the passive *personari* "be made a person". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 188.16, 188.32). |
| vicem supplere / vicis supplecio | supply the place / the supplying of a place | God supplying the place of a second cause. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 187.26). |
| perfeccio simpliciter | perfection without qualification | After *simpliciter* "without qualification". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.1). |
| transsubstanciacio | transubstantiation | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.10). |
| multiplicative | multiplicatively | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 193.20). |
| habitudo relativa | relative respect | The "respect" sense of the CONTEXTUAL *habitudo* row. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 193.19). |
| in divinis | among the divine [persons] | Keeps "Godhead" for *deitas*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 196.18). |
| partes proporcionales | proportional parts | The halving division of a continuum. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 194.24). |
| universitas creabilis | the creatable totality | Beside *universitas creaturarum* "the totality of creatures". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 199.5). |
| multiplicacio dimensionalis | dimensional multiplication | One body in several places by its dimensions. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.6). |
| habitus (= possession, *habere*) | the having | The category of having, C note; kept apart from *habitus* "habit". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.14). |
| a maiori vel pari | from the greater or from the equal | Arguments *a maiori*; cf. *locus a maiori*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 209.5). |
| sensibile commune | common sensible | Aristotle's common sensibles (number, motion, figure); the term of art, against the §D row "perceptible". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 209.23). |
| mocio progressiva / motus progressivus | progressive motion | Locomotion. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 205.28). |
| multiplicacio concomitancie | multiplication of concomitance | Cf. *gracia concomitancie*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 213.21). |
| superioritas / inferioritas terminorum | superiority / inferiority of terms | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 215). |
| homo communis | the common man | The universal man, with *res communis*; not "the ordinary man". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 218.3). |
| signum reduplicatum | the reduplicated sign | The reduplicative word (*secundum quod*, *in quantum*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 230.23). |
| lex proximitatis | the law of neighbourhood | The duty to love one's neighbour (*proximus*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 101.29). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
| sacramentaliter | sacramentally | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| vere | truly | A mode adverb: one word each, never two merged, kept where Wyclif puts it. ⛔ Never "really" (that is *realiter*). Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| virtualiter | virtually | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| figurative | figuratively | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| tropice | tropically | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Kept apart from *figurative*. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| ydemptice | identically | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| invisibiliter | invisibly | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
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
| Doctor Communis | the Common Doctor | Thomas; with *Doctor Subtilis*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 8.16). |
| multitudo (of one body) | multitude | Of one body's being many (ch. 8); the plain "multitude" of persons needs no row. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 8.4). |
| sensus communis | the common sense | The inner faculty; kept apart from *sensibile commune* "common sensible". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 18.31). |
| sensacio | sensation | One of the five. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 20.18). |
| figurare | figure | Both senses: to prefigure (the lamb figured Christ) and to shape (*figurare Deum nostrum*), which Wyclif plays on; one English word keeps the pun. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-c 10; 21.29). |
| sensualiter | sensually | Berengar's oath word (*Ego Berengarius*); kept apart from *sensibiliter* "perceptibly". A mode adverb, one word. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 26.1, 30.24). |
| sentire (an opinion: sensit quod) | hold | Of a doctor's or church's opinion; the "perceive" row is the sacrament sensed. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 30.30, 31.18). |
| predicacio figurativa | figurative predication | A synonym of *predicacio tropica*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 35.18). |
| expositorie (of preaching scripture) | by way of exposition | Not the logicians' *expositorie* "expositorily" of the expository syllogism. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 46.4). |
| aliquitas | somethingness | Being a something (*aliquid*). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 60.27). |
| cedere (in) | give way (into) | Of the bread passing into the body. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 58.3, 60.9). |
| informacio; informare | informing; inform | Of a form in its subject; not "information". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 64.13). |
| accidens predicamentale | accident of the categories | Kept apart from the predicable *accidens*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 64.1). |
| contiguacio | contiguity | Beside *continuacio* (of bodies) "continuation". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 68.12). |
| pedalitas | foot-length | *pedalis* "foot-long". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 66.27). |
| veritas predicamentalis | truth of the categories | As *accidens predicamentale* "accident of the categories". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 69.2). |
| extense loquendo | speaking in an extended sense | Cf. *large / stricte loquendo*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 82.15). |
| esse situale / intencionale / potenciale | situal / intentional / potential being | The modes of the body's being. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 84.8 ff.). |
| sensus (of words) | meaning | Kept apart from *sentencia (verborum)* "sense" (Wilson's row). The bodily *sensus* and *sensus literalis / misticus* stay "sense". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 89.22, 04-c, 04-d). |
| insensibiliter | imperceptibly | Beside *insensibilis*; the opposite of *sensibiliter* "perceptibly". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-e). |
| pertinenter | fittingly | Kept apart from *convenienter*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-e, 04-f). |
| essencialiter | essentially | A mode adverb, one word. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-g). |
| noticia confusa / distincta | indistinct / distinct knowledge | As *confuse / confusus* "indistinct(ly)". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-g). |
| ponderositas; ponderosum | heaviness; heavy | The abstract against the concrete: *hostia est ponderositas sed non est ponderosum*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-a p. 10, 110.24). |
| suscipere magis et minus | admit of more and less | Aristotle's test of a quality. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 113.32). |
| questio si est / quid est | the question whether it is / what it is | *Post. An.* II.1. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 119.18). |
| universitas sua (God's) | his universe | Beside *universitas creaturarum* "the totality of creatures". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 124.31, 129.16). |
| figuracio | figuration | Beside *figura / figurare*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 131.16). |
| neutraliter; adiective | as a neuter [noun]; as an adjective | The grammar of *accidens*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.7). |
| naturalitas obediencialis | obediential naturalness | Cf. *dependencia obediencialis*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.15–18). |
| accidentalitas | accidentality | Beside *substancialitas*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.13). |
| quantitas successiva | successive quantity | Time and motion, against permanent quantity. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.1). |
| corpus mathematicum | mathematical body | The three dimensions without matter. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 142.31). |
| ubi; ubicans | where; that which gives a where | The category of place and its cause. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 146.23–24). |
| inpossibilitare | make out as impossible | Of the *moderni*'s argument. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 149.13). |
| utrobique | on both sides | In citation formulae and argument. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 148.21). |
| conversivus | converting | As *verba sacramentalia conversiva*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 153.6, 153.25). |
| pertinencior | more fitting | The comparative of *pertinens*; cf. *pertinenter*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 153.8). |
| signum nature | instant of nature | The scholastic priority without time; kept apart from *signa* "signs". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 161.9). |
| generancia | begetting | Ruled 2026-11-07 (coordinator, delegated; *Euch.* 161.25). |
| ponderacio | weighing | Beside *ponderositas* "heaviness". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 183.17). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| insensibilis | imperceptible; of a thing that cannot feel, without sensation | Two senses by referent: what cannot be perceived / what cannot perceive (*lapis insensibilis*, *Dial.* 56.3). Kept visibly paired with *sensibilis*. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| magisterium | rule; of teaching, the teaching office; *quale magisterium* "what a feat of mastery" (*Incarn.* 137.14) | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ydiota | unlettered man | Never "idiot". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| ablacio | taking-away | Set against *restituere*/*restitucio*. Ruled 2026-10-02 (*Eccl.* 15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| denominacio; denominare | naming; to name | The argument turns on it. Ruled 2026-10-02 (*Eccl.* 17, 391.17, 398.2). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
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
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| continuacio (of bodies, the act) / discontinuacio; continuare / discontinuare | continuation / discontinuation; make continuous / make discontinuous | The making of several bodies into one continuum (*Incarn.* ch. 12), G note at first use: not "carrying on". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.30, 211.12). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
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
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). Beside *consecrare* (*consecrat et conficit*) "confect", so the pair stays two. Ruled 2026-11-07 (Wilson, "confect works"; *Euch.* 16.10). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| infundabilis; infundabiliter | without foundation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 195–196). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| neutra | neutral things | Things neither commanded nor forbidden (obedience *in neutris*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.19). |
| eleccio passiva / activa | passive / active election | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 254.31). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| correptibilis | open to reproof | Beside *corripere* "reprove". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 301.3). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| potissimus; pocior (Antichristus) | foremost; greater | Superlative and comparative kept visible as a pair. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.28, 331.12). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |
| coloracior | more colourable | Comparative, with the *color* / *colorabilis* rows. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 384.15). |
| ars cesarea | the caesarean art | After *papa cesareus*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| ingeniacio | wit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 394). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| nimis | exceedingly | Medieval intensive (= *valde*); "too much" only where excess is the point. Ruled 2026-10-12 (close-out R2; *Pot. pape* 169.2). |
| sentire (the sacrament, the body) | perceive | "sense". As *sensibilis* "perceptible". Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.10, 1.17). |
| singulariter | CONTEXTUAL: alone, only / in a singular way | "singularly" never; "in a singular way" where "alone" will not construe (*Euch.* 85.28, coordinator 2026-11-07). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 4.14). |
| fingere (a miracle) | feign | "imagine". Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.11, 1.14). |
| recitare | recite | To report, rehearse. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.4, 3.10, 4.18). |
| ex tibi dubio; ex sibi dubio | for all you know; for all he knows | Idiom: not "from doubt". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 66.15, 70.25). |
| pertinaciter | pertinaciously | Keeps "obstinate" for *protervus*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 180.29). |

---

## Chunk 07-a: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-07-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-07-a
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "189.29–193.19"
divisions: "cap. 7 (heading 'CAPITULUM SEPTIMUM.' at 189.0); part 1 of 11, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "851 words; 837 confirmed by the vote; 10 runs stood by rule; 4 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n260–n264 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 7, part 1: [TITLE]

## ¶1 · 189.29–190.12

> [p. 189] Ut autem a sacramento veritatis clarius fugetur falsitas, restat transcurrendum per alia dubia quibus scola theologie nimis inaniter accusatur, et primo de [p. 190] sentencia ydemptificacionis sacramenti in corpus Christi, qua creditur, quod nudus panis et vinum fient ydemptifice corpus Christi et sanguis. Et recitat illam Magister Sentenciarum IVᵒ, distinccione XIᵃ, capitulo primo; et habet ista sentencia pro se evidencias multas sophisticas et testimonia sanctorum sophistice intellecta. Arguitur ergo primo sic contra istam sentenciam: Panis et vinum non fient aliquid quod non erunt, sed non erunt ydemptice corpus Christi et sanguis, ergo non fient sic corpus Christi et sanguis. Si enim erunt idemptice hec partes Christi et omnia que erunt sunt, tunc sunt hec partes Christi.

[ENGLISH]

## ¶2 · 190.13–190.26

> [p. 190] Contra quod arguitur secundo per hoc quod vinum non per accidens sed per se est vinum. Sed nihil quod per se est aliquid potest esse non illud, ergo nullum vinum potest esse non vinum. Si enim corpus Christi in fine verborum conversionis erit non vinum, tunc oportet quod materia vel forma vini aut aliquid sibi equale deficiat, quia manente omni essenciali requisito ad esse vini non est tunc racio quare non remaneret vinum et per consequens non tunc erit non vinum conversum in aliud. Si tunc deficiet materia, forma vel aliquid sibi essenciale, tunc oportet quod vinum desinet esse et per consequens ipsum vinum non tunc erit aliud quam vinum, quia tunc non erit aliquid.

[ENGLISH]

## ¶3 · 190.27–191.12

> [p. 190] Item, vel erit ipsa ydemptificacio individualis per motum vel sine motu; si per motum, oportet signare aliquid quod deperdetur vel acquiretur vel utrumque; [p. 191] et signato illo quod acquiretur vel deperdetur, queritur (ut supra) utrum erit essenciale vel accidentale ydemptificando, si essenciale signatum non ydemptificatur sed destruetur. Si vero sit accidentale ydemptificando, sequitur quod non obstante illo motu manebit utrumque quidquid prefuit; non ergo ydemptificatur unum alteri, sed manebunt due res tantum essencialiter distincte sicut in principio. Si sine motu fiat ydemptificacio, tunc a neutro fiet ablacio alicuius essencialis vel accidentalis pertinens ydemptificacioni, et per consequens remanebunt tante distincta substancialiter et accidentaliter sicut in principio.

[ENGLISH]

## ¶4 · 191.13–193.10

> [p. 191] Item, posito quod Deus ydemptificet hominem cum asino vel quidlibet significandum cum alio, queratur post casum, utrum homo remanebit homo post ydemptificacionem vel asinus vel utrumque. Si utrumque, remanebunt tantum distincta in principio, si remanebit homo et asinus desinit esse vel econtra, videtur primo quod illud desinens non ydemptificatur sed corrumpitur, quod est contra concessum. Videtur secundo quod sequitur: Homo ydemptificatur asino, ergo asinus ydemptificatur homini et econtra; et ita ex casu non sequitur pocius quod remaneat homo quam asinus vel econtra. Non ergo concedendum est unum quin per idem et aliud. Et videtur idem tercio ex hoc quod illud ydemptificatum quod desinit perdit aliquid sibi essenciale ut animam asininam vel animam humanam, et per consequens illa non foret ydemptificacio sed destruccio. Et hic querunt logici de subiecto et terminis ydemptificacionis ut distingueretur ab aliis motibus et de eius celeritate ac aliis eius proprietatibus. [p. 192] Item, pono quod Deus ydemptificet quodlibet cuilibet, quod oportet concedere esse possibile, quia aliter staret Dei potencia infinita ad aliqua que non posset ydemptificare, consequens inpossibile, cum posset ydemptificare creaturas valde abiectas sibi ipsi, ut patet in materia de incarnacione tam quoad corpus Christi quam animam; quarum utrumque est verbum Dei et personaliter ipse Deus; quod videtur summe mirabile. Hoc ergo admisso videtur quod quilibet manet in sua specie ac individuacione ut mansit in principio, quia da quod non Petrus remanet ut in principio, contra quidlibet ydemptificatur Petro, ergo Petrus remanet summe multiplex. Et idem est argumentum de quolibet assignando. Si ergo tota universitas remanet in sua specie ac sua individuacione ut in principio, videtur quod utrobique tollitur ydemptificacio; nam ad omnem punctum mundi est summa diversificacio; que cum sit contraria ydemptificacioni, videtur quod tollit ydemptificacionem pro eodem tempore et subiecto. Si dicatur quod summa ydemptificacio est summa diversificacio, tunc (ut supra) debet correspondenter hoc posito variari responsio, quia repugnat quod quidquam remaneat compositum ex partibus vel accidentatum, ymmo notum est si quidlibet est, quidlibet solum Deus est. Item, stante hoc casu videtur quod quelibet pars mundi sit indivisibilis, quia ydemptificata est puncto et per consequens est punctus indivisibilis. Et videtur quod quelibet pars mundi sit in infinitum magna, quia cum quelibet pars mundi sit totus mundus, quelibet pars quantitativa mundi foret ita magna ut totus [p. 193] mundus et per consequens infinitum modica pars mundi foret ita magna ut aliquid. Ex quo cum principiis geometrie sequitur quod omnis pars mundi sit infinita, quia da quod caput tuum non sit nisi pedale, contra nasus tuus est ita magnus ut mundus, ergo caput tuum cuius nasus est pars quantitativa est maius quam pedale, cum omne totum huius est maius sua parte quantitativa capitis, ydemptificatur maxime linee, maxime superficiei et maximo tempori mundi; et tunc est nimis magna.

[ENGLISH]

## ¶5 · 193.11–193.19

> [p. 193] Nec est racio quare quelibet pars panis potest ydemptificari corpori Christi et cuilibet sue parti, quin per idem posset ydemptificari cuilibet substancie vel accidenti, cum par sit racio et multiplicacio inconveniencium utrobique, quod ex tali ydemptificacione arguunt loyci quod inpossibile sequitur ex necessario quod quilibet est et quicunque non est et quod species et genera rerum que differunt ab invicem non differunt, quia omnis differencia foret unio et non differencia.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 190.1: Of identification in the Sacrament.
- 190.13: Wine cannot be not wine, so when the form of wine is gone it ceases to be, and so cannot be the subject of change.
- 190.27: Identification must involve change or not.
- 191.1: If it involves change of the essence, that is destruction; if of an accident the substance remains. If there is no change, the substance remains.
- 191.13: Suppose God to identify a man with an ass, do both remain or either? If both, they are distinct as before; if only one, the other is destroyed, not identified.
- 192.1: No limit to + God's power of identification.
- 192.12: Absurdities that would follow from granting identification.
- 192.12: Yet identification does not take place.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 190: *IVᵒ,* (print = bt) [SUB]
  - 190: *Si* (print = bt) [BT-ONLY]
  - 192: *principio, contra quidlibet ydemptificatur Petro, ergo Petrus remanet summe multiplex. Et idem est argumentum de quolibet assignando. Si ergo tota universitas remanet in sua specie ac sua individuacione ut in principio, videtur quod utrobique tollitur ydemptificacio; nam ad omnem punctum mundi est summa diversificacio; que cum sit contraria ydemptificacioni, videtur quod tollit ydemptificacionem pro eodem tempore et subiecto. Si dicatur quod summa ydemptificacio est summa diversificacio, tunc (ut supra) debet correspondenter hoc posito variari responsio, quia repugnat quod quidquam remaneat compositum ex partibus vel accidentatum, ymmo notum est si quidlibet est, quidlibet solum Deus est. Item, stante hoc casu videtur quod quelibet pars mundi sit indivisibilis, quia ydemptificata est puncto et per consequens est punctus indivisibilis. Et videtur quod quelibet pars mundi sit in infinitum magna, quia cum quelibet pars mundi sit totus mundus, quelibet pars quantitativa mundi foret ita magna ut totus* (print = bt) [BT-ONLY]
  - 193: *ydemptificatur* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 189:
5. C : sit — sacramenti in marg. alia manu. ~. E : fit. S. E : aliguid.
l3. ABD : convcrti deest: C: in marg. alia manu. iS. AB: subiectalem.
22. D : figwraret. 2?. tantam regulam. 27. C: terrena in marg. alia
manu. 2S. CK: Cap. VII. deest. 20. B: Et ut a : ABCD: autem dcest:
ib. D: clarius dccsf; ib D: fuceretur. ?i. D: o-curitur.

p. 190:
2. E: fierent. 4. Codd.: IV Sentenciarium. /|, 5. C: cap. I in
marg. alia manu. 5. AB: ista evidencia ; C: correxit. 6. E: testimonio.
7. D: incollecta. n. ABCD: ydemptice deest. 12. ABCE: tunc sunl
deest. i5. B: non aliud. ig. ABCI) : essenciale before deficiat.
20, 21. B: non est — vinum decst. 22. B: deficil. 23. ABCD: vel aliud.
24. D : deficiet.
3. Petri Lombardi Opp. (ed. Col. iSyG) fol. 352b, 353*.
Cf. Thomae Super Quarto Sent., dist. XL, q. I, art. I, vol.
Opp. tom. X, [66.

p. 191:
i. C: quod acquiretur in marg. alia mann; ib. D: deperdereiur.
4. C: destrueretur. 6. ABCD: quidqnid quod; ib. DE: idemptificabitur.
9. D: oblacio. 16. AB : vel utrum. 17. C: v* in yrincipio. Herzberg-
Franckel rcads: videlicet; Rectius: ut. iS. ABC: desit. 20. E: sed
destruitur sive corrumpitur ; ib. D: quod essc. 25. D: quod idem.
26. D: tioc ergo; ib. D : illud decst: ib. E: non dcsinit. 3o. Codd.: et
distingueretur.

p. 192:
principio, contra quidlibet ydemptificatur- Petro, ergo
Petrus remanet summe multiplex. Et idem est argu-
identification r .
mentum de quolibet assignando. Si ergo tota univer-
sitas remanet in sua specie ac sua individuacione ut
in principio, videtur quod utrobique tollitur ydempti-
ficacio; nam ad omnem punctum mundi est summa
diversificacio; que cum sit contraria ydemptificacioni,
videtur quod tollit ydemptificacionem pro eodem
tempore et subiecto. Si dicatur quod summa ydempti-
ficacio est summa diversificacio, tunc (ut supra)
debet correspondenter hoc posito variari responsio,
quia repugnat quod quidquam remaneat compositum
ex partibus vel accidentatum, ymmo notum est si
quidlibet est, quidlibet solum Deus est.
thai Item, stante hoc casu videtur quod quelibet pars
mundi sit indivisi bilis, quia ydemptincata est puncto
et per consequens est punctus indi visibilis. Et videtur
quod quelibet pars mundi sit in infinitum magna, quia
cum quelibet pars mundi sit totus mundus, quelibet
pars quantitativa mundi foret ita magna ut totus
1. D: suppono'; ib. E: quidlibct. 3. D: ad alia. 7. ABDE: utraque.
8. C : qund ipse Deus. 9. D: dimisso. 10. ac ; C: et in marg. alia manu.
11. E: remanet Petrus in. 16. D: utrolibet. 20. ABCI£: Si dicit.
21. C: ut in marg;. alia manu. 23. E: maneat. 24. E: esl decst.
25. Deus est; C addit in marg. alia manu (incertum an ad textum pertinens):
quia quidlibet esset anima intellcctiva et per conscquens non essct com-
positum cx partibus ncc esset aliquid accidenlatum, quia quidlibet esset
Deus qui accidentatus non cst. 29. C: in deest; ib. ABC: magno.

p. 193:
5. E: sicut. 6. D: caput totum. 7. D: huius sit. \b. D: et ex ta/i;
C: quia ex tali. 17. C: quia before quilibet ; ib. D: cuiusmodicunque.
18. BC: ad invicem. 26. E: Christi deest; ib. ABCD : non tantam.
28. D : alia. 29. C: non in marg. alia manu; ib. C: tam in marg. alia manu.
3o. C: et in marg. alia manu. 3i. D: quidlitet. 33. DE: impedit.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
(none recorded)
```

---

## Chunk 07-b: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-07-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-07-b
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "193.21–197.22"
divisions: "cap. 7 (heading 'CAPITULUM SEPTIMUM.' at 189.0); part 2 of 11, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "952 words; 936 confirmed by the vote; 13 runs stood by rule; 3 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n264–n268 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 7, part 2: [TITLE]

## ¶1 · 193.21–194.5

> [p. 193] Item, plus accedendo ad difficultatem videtur quod omnis panis vel vinum transsubstanciatum in corpus et sanguinem manebit post conversionem ydemptificatum parti Christi, et cum nullam partem ex tali conversione deperdit Christus, sequitur quod post conversionem erit corpus Christi multiplicius; nam tantam partem quantus est panis aut vinum consecratus in toto mundo, Christus acquiret sine perdicione aliqua; quomodo ergo non habebit plus tam de materia quam de forma? Nam omnia ista habebit ut partes et nullam istarum iam habet; ergo quamlibet earum acquirit vel acquiret. Non enim dicetur quod ydemptificacio impediret formas syllogisticas, ita quod sequitur: [p. 194] totum istum panem et vinum Christus habebit partem suam et nullum istorum nunc habet, ergo multas partes habebit, quas nunc non habet; nam panis et vinum sunt substancialia et non accidentalia; et tunc patet consequencia.

[ENGLISH]

## ¶2 · 194.6–194.14

> [p. 194] Sed adversarius dicit quod omnes termini sunt accidentales, cum quilibet potest esse quidlibet, et ita non sequitur quidquid erit Petrus illud nunc est, sed asinus erit Petrus, ergo asinus ipse nunc est; ut in simili non sequitur: quidquid tempore nativitatis tue fuisti illud nunc es, sed infidelis ydiota tunc fuisti, ergo infidelis ydiota nunc es; et quam accidentale est tibi esse infidelem, tam accidentale est tibi esse hominem.

[ENGLISH]

## ¶3 · 194.15–194.22

> [p. 194] Sed contra istud obicitur primo per hoc quod omne quod Christus umquam habebit partem suam, illud nunc habet partem suam; sed omne quod est vel erit panis aut vinum consecrandum, Christus habebit partem suam, cum ydemptificatur parti sue, ergo omne quod est vel erit, panis aut vinum consecrandum, Christus iam habet partem suam; ista quidem forma valet in terminis accidentalibus.

[ENGLISH]

## ¶4 · 194.23–194.27

> [p. 194] Capta ergo essencia que est panis consecrandus, si hoc erit corpus Christi et hoc differt nunc essencialiter a corpore Christi, cum nunc sit aliud ab ipso, sequitur quod aliquid quod iam essencialiter differt a corpore Christi erit corpus Christi.

[ENGLISH]

## ¶5 · 194.28–195.8

> [p. 194] Similiter, data ista sentencia perirent omnia putata, quia tam substancia que foret basis omni accidenti quam eciam distinccio accidencium; nam humanitas, animalitas et omne tale signabile accidit essencie, cum illa essencia que est homo vel animal potest esse [p. 195] non animal eciam non substancia, ymmo nichil foret per se aliquid nec aliquid per se vel singulare; quomodo ergo staret genus substancie? Et per idem quantitas potest esse qualitas, et sic de omni genere accidentis; et perirent quinque universalia, scilicet genus, species et substancialis differencia et per consequens omnis sciencia et omnis forma substancialis vel accidentalis.

[ENGLISH]

## ¶6 · 195.9–195.25

> [p. 195] Similiter iuxta hanc viam periret omnis motus vel accio naturalis, quia tam fundamentum quam materia motus deficeret; si enim scirem quod homo ambulat, scirem quod homini accidit ambulacio. Sed contra pro toto tempore ambulandi ex tibi dubio hoc fit non homo sed lapis vel aliud ydemptificatum membris Christi; non ergo scitur quod homo ambulat, cum tollitur omnis sciencia de rerum quidditate, distinccione vel transmutacione. Si enim materia motus foret continue ydemptificata cuilibet, quomodo specificaretur, distingueretur vel attenderetur motus? Sed totum hoc ignoras et dubitas, cum ydemptificacio sit habitudo reciproca que potest fieri insensibiliter ignorante homine subducto quocunque motu. Nichil itaque stulcius aut irracionabilius ista sentencia, cum ydemptificatur opinioni stultissime summe heretice et maxime detestande.

[ENGLISH]

## ¶7 · 195.26–195.29

> [p. 195] Nec valet hec opinio pro fine quo fingitur, quia implicat panem et vinum remanere panem et vinum post consecracionem, ad quod evadendum fingit ydemptificacionem.

[ENGLISH]

## ¶8 · 195.30–196.3

> [p. 195] Sed pro ista via arguitur primo per hoc quod quidquid producit individuum speciei, ydemptificat [p. 196] illud nedum illi speciei sed cuilibet eius individuo, cum sit triplex ydemptitas, scilicet generalis, specialis et numeralis, est ergo ydemptificacio possibilis.

[ENGLISH]

## ¶9 · 196.4–196.22

> [p. 196] Sed pro isto non est difficultas quin talis ydemptificacio sit necessaria, sed difficultas loquitur de ydemptificacione numerali duorum individuorum que prius essencialiter et numeraliter sunt distincta, ut panis consecrandus et corpus Christi in celo sunt duo individua loco et forma multiplici distincta et virtute verborum conversionis ponitur eandem rem que prius fuit panis foret ydemptice corpus Christi; sed corpus Christi negatur fore ille panis: et hoc videtur fore difficile, cum ponitur formam substancialem panis et materiam primam ac quamlibet partem panis pro instanti conversionis desinere esse secundum se totam. Et ista foret mirabilis ydemptificacio in qua unum extremum secundum se totum destruitur et per idem non foret transitus, conversio vel transsubstanciacio panis in corpus Christi, nec corpus Christi fieret ex illo, sicut patet admittenti significaciones signorum antiquas. Et non valet baptisare terminos sic extranee et infundabiliter ad fingendum mendacium.

[ENGLISH]

## ¶10 · 196.23–196.28

> [p. 196] Conceditur tamen (ut dictum est in materia De Universalibus) quod omnis homo est idem quod quilibet, ymmo omnis substancia est idem cuilibet, non tamen propterea omnis homo est omnis homo, cum non oportet si iste homo sit idem isti homini quod sit propterea iste homo.

[ENGLISH]

## ¶11 · 196.29–197.9

> [p. 196] Secundo arguitur pro ista via per hoc quod illa sensibilis eukaristia est uni albedo sub qua videtur Christus corporali oculo et per idem est alii alia qualitas vel quantitas, secundum quod eius opinio de quidditate eukaristie variatur. Cum ergo quodlibet [p. 197] istorum sit Christus, videtur quod ydemptificacio multorum eciam diversorum in genere sit satis possibilis. Minor videtur ex hoc quod ex ultima protestacione Beringarii et confirmacione Romane ecclesie corpus Christi est in illo sacramento sensibile et de facto illud sacramentum (ut loquitur scriptura cum sanctis doctoribus). Quid ergo foret si non albedo, cum illa sit perfectissimum accidens, ibidem maxime propinquum intellectui ut sic signum?

[ENGLISH]

## ¶12 · 197.10–197.22

> [p. 197] Item, cum illud sacramentum sit visibile vel est albedo vel album, sed non est album; ergo est albedo per se visibilis, non quantitas ut magnitudo vel superficies, vel non est hoc solum, quia potest manere idem album quantitate variata, ut patet de maioracione vel minoracione sacramenti in calice, ymmo sacramentum sub forma panis, sicut potest variari in albedine, sic potest per exspiracionem variari in quantitate. Sicut ergo quantitas per se existens est quanta, sic albedo per se existens est alba, quia aliter sensus nimis deciperetur in sensacione, cum prius videt album quam albedinem in abstracto, quia hoc est virtutis abstractive discernere.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 193.21: If identification takes place, Christ must certainly be acquiring new parts.
- 194.6: Our opponent says that all terms are accidental.
- 194.15: We hold that whatever will be a part of Christ is so already.
- 194.23: In his theory something that differs now from Christ's body will be Christ's body.
- 194.28: If identity could thus be lost, all things would perish.
- 195.1: There would be no substance, no universals, no knowledge.
- 195.9: Action and change would cease, for there would be no specific thing to act; e. g. you could not say "a man walks" when the man might be a stone or any other creature.
- 195.30: Equivocation as to meaning of identification.
- 196.4: The identification we are dealing with is that of two numerically distinct bodies one is lost, in the other.
- 196.29: 2. Our opponents say: The host is a whiteness under which Christ is seen with the bodily eye;
- 197.3: for since Christ is the sacrament He must be whiteness, which is the most perfect accident.
- 197.10: We see the sacrament, and it must be either white or whiteness. But it is not white, so it must be whiteness, which indeed is white.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 197: *Beringarii* (print = bt) [SUB]
  - 197: *confirmacione Romane* (print = bt) [SUB]
  - 197: *Christi* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 193:
5. E: sicut. 6. D: caput totum. 7. D: huius sit. \b. D: et ex ta/i;
C: quia ex tali. 17. C: quia before quilibet ; ib. D: cuiusmodicunque.
18. BC: ad invicem. 26. E: Christi deest; ib. ABCD : non tantam.
28. D : alia. 29. C: non in marg. alia manu; ib. C: tam in marg. alia manu.
3o. C: et in marg. alia manu. 3i. D: quidlitet. 33. DE: impedit.

p. 194:
2. D: iam habet. 6, 7. D: termini isti accidentales. 7. ABCD : cum
quidlibet. 8. E: hoc nunc. 10. ABCD : in assimili ; ib. ABD : tempore ne-
cessitatis; A: correxit in marg. alia manu. n. C: illud deest. 12. D: et
quantum. i3. D: est after accidentale deest. i5. ABCD : obicitur deest.
19. D: idemptificabitur. 21. 22. B: aut quidem. 29. D: tam subiecto
que foret; ib. C: basis in marg. alia manu. 3i, 32. D: Et tamen illa.

p. 195:
i. D: et non. 2. se aliquid; C: addit. in marg. superiori alia
manu: quia si aliquid foret per se aliquid, tunc non posset esse non
illud; quod falsum est secundum ponentem ydemptificacionem quorum-
cunque et persona posset esse non persona, et singulariter universale,
et sic de aliis; ib. ABCD : aliquid persona. 4. C: esse in marg. alia
manu. 22. B: subducto deest. 23. B: stulticius. 24. C: Ofinioni
in marg. alia manu.

p. 196:
6. B: naturali; ib. D: duarum individuarum. 11. D: ydemptifice.
12. ABCD: fore after videtur deest. 16. ABC : illa ; ib. E: qua vini.
18. E: non deest. 19. ABC : ferret. 20. D: signaciones. 23. D: con-

p. 197:
4. ABC: et protestacione. 7. ABC: cum ilhid. 9. D: intellectu.
10. D : cum deest. i3. D : vel deest. 17. D : per exspisacionem.
25. D: Si quis. 26. D: elementales. 27. E: ut homo. 29. ABCD :
Averrois. 3o. D: principans. 32. D: variaretur. 33. E: existencia.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
(none recorded)
```

---

## Chunk 07-c: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-07-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-07-c
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "197.23–199.33"
divisions: "cap. 7 (heading 'CAPITULUM SEPTIMUM.' at 189.0); part 3 of 11, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "547 words; 535 confirmed by the vote; 10 runs stood by rule; 2 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n268–n270 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 7, part 3: [TITLE]

## ¶1 · 197.23–198.13

> [p. 197] Item, nulla alia qualitas coexistens informatur albedine, quia hoc foret potissime qualitas prima, ex qua resultat albedo. Sed quis dicit quod qualitates elementares sunt sic colorate? Tunc enim quilibet sensus perciperet qualitates tangibiles et homo videret potissime gravitatem, cum illa vel sit forma substancialis (ut placet Averroi) vel forma propinquissime principians colorem; ymmo cum color secundum philosophos non sit nisi lux incorporata dyaphano, videtur quod ad variacionem lucis varietur et color. Cum ergo coexistencia qualitatum non sufficit ut una [p. 198] informet reliquam, necesse habet hec via dicere, quomodo causatur informacio qualitatum. Non enim est color concludere quod, si qualitas resultat ex elemento, ex materia et forma, quod propterea qualificat suum principium, quia sic omnis qualitas qualificaret Deum. Videtur ergo cum hoc sacramentum non sit album quod sit albedo et per idem qualiscunque, qualitas aut quantitas, et nullomodo aggregatum ex omnibus accidentibus in hostia consecrata, cum illud non potest informari albedine, tum quia continue variatur, tum eciam quia multa sunt ibi accidencia distincta in genere que non possunt albari; sed pocius albedo denominatur ab illis.

[ENGLISH]

## ¶2 · 198.14–199.5

> [p. 198] Sicut ergo glossa ordinaria decretorum (ut supra exposui) dicit quod hoc sacramentum non est ponderosum sed ipsa ponderositas vel sibi subiectum, sic debet dicere de albedine, duricie, sapore et eis similibus; et per consequens sunt in eadem hostia infinita sacramenta distincta in genere. Non ergo foret unitas in hostia vel denominacio accidentalis; quod manifeste repugnat sensui; videmus enim quod hostia est continua, frangitur et nutrit, odorat et sapit, sonat et descendit. Numquid credimus illud quod sic demonstratur esse nichil vel unum aggregatum ex sono, odore, sapore, descensu et alia accione? Talia enim continue variantur et accidunt sacramento, sicut conficere in fermento vel azimo. Numquid credimus quod accidens illud sit fermentatum vel azimum, extensum vel fractum et cum hoc multiplicatum et non huius, quia secundum alias partes quarum quelibet est sacramentum invisibile; alias multiplicavi argumenta que [p. 199] darent fidem fidelibus quod nulla qualitas poterit per se esse et multo minus alia genera accidentis. Non enim est figura, pulcritudo, febris vel potencia anime res talis quam debemus orare, pro se colere vel timere.

[ENGLISH]

## ¶3 · 199.6–199.18

> [p. 199] Ideo quantum ad istud laudo Deum qui me liberavit ab isto scandaloso et derisibili errore de quidditate huius sacramenti. In qua materia philosophi et pagani derident nimirum nostram ficticiam de incertitudine et variacione circa quidditatem hostie consecrate. Est enim panis aut vinum quod subiectat omnia illa accidencia. Et illud sentitur sensacione multiplici cui nova accidencia non consecrata possunt accidere, que non sint pars sacramenti sicut accidencia hostie, que tamen omnia reducuntur cum tota universitate creata ad quandam unitatem in Deo cui omnia instituuntur, ut ipsum significent et omnia modo suo ipsum dicunt atque aliqua magis sacra et alia minus sacra.

[ENGLISH]

## ¶4 · 199.19–199.33

> [p. 199] Sacramentum autem altaris potest vocari, ut sepe dixi, corpus sic rite benedictum a presbitero, quelibet eciam eius pars; et quodlibet eius sensibile accidens potest vocari secundarie vel per accidens sacramentum, sicut et corpus aggregatum ex corpore consecrato et alio sibi commixto; ymmo quandoque corpus permanens vocatur sacramentum et quandoque corpus successivum. Sed inpossibile est sacrum accidens, potissime quantitatem et qualitatem, esse per se sacramentum, cum secundum Augustinum non poterit per se esse. Et patet quod nullum istorum sacramentorum est ydemptice Deus vel pars eius, sed signum efficax quod ad sensum equivocum et tropicum suscipit predicacionem partis Christi in modis loquendi sanctorum et Romane ecclesie.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 197.23: Whiteness does not inform another quality.
- 198.14: Following this line of argument we find that the sacrament is all kinds of accidents. Consequently in one host there are many sacraments. Thus we are led into endless follies.
- 199.5: Wyclif thanks God for freeing him from all this error.
- 199.9: The quiddity of the host is bread and wine.
- 199.11: In this substance the accidents unite to be all alike symbols of God.
- 199.18: The sensible accidents of the host may in a way be called the sacrament, but having no separate existence it cannot be the sacrament. A sacrament is not identically but symbolically God.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 199: *timere.* (print = bt) [BT-ONLY]
  - 199: *Christi* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 197:
4. ABC: et protestacione. 7. ABC: cum ilhid. 9. D: intellectu.
10. D : cum deest. i3. D : vel deest. 17. D : per exspisacionem.
25. D: Si quis. 26. D: elementales. 27. E: ut homo. 29. ABCD :
Averrois. 3o. D: principans. 32. D: variaretur. 33. E: existencia.

p. 198:
1. D: aliam necesse; lh. B : fiecesse est. 3. D: qualiter resultat.
3. 13: sit omnis. 6. E: quod cum. ~. ABCH: quaufactum ; ib. aut ;
B: vel; D: ac. 12. ABC: possunt deest; C in marg. alia manu addit.
14. E: Sic ergo. i5, 16. C: neque ponderositas. 17. E: et de tiiis.
19. E: in deest. 23, 24. D : denominatur. 25 C: aiia deest
27. B: et a\imo. 29. Rectius: huiusmodi.
ir. Vide supra pag, 184.

p. 199:
i. E: nulla quantitas. 3. D : est deest. ~. D : scandalo. i3. B : sun
accidere. 14. C: partes. 16. D: cum Deo. iS. ABCD : alia magis;
C in marg. aliqua ; ib. D : sacramenta. 19. ABD : vocare. 20. ABC : ritu.
22. B: potest variari. 3o. D: dominus.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
(none recorded)
```
