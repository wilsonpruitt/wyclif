# Translation brief: eucharistia 09-j–09-l

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/eucharistia/wyc-eucharistia-09-j.md chunks/eucharistia/wyc-eucharistia-09-k.md chunks/eucharistia/wyc-eucharistia-09-l.md` once and fix what it reports.
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

## Glossary (the 621 rows these chunks use; the full file is GLOSSARY.md)

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
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| expropriacio | renunciation of property | Never "expropriation" (seizure). Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |
| vicarius Christi | vicar of Christ | The card's ruling, now a row. Ruled 2026-10-02. |
| elemosinans | almsgiver | The participle of *elemosinare*: the donor. Ruled 2026-10-02 (*Eccl.* 13). |
| sacramentum (the Eucharist); sacramentum altaris | sacrament; the sacrament of the altar | The plain sense, against the Augustinian row (*Incarn.*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.3, 3.30). |
| hostia; hostia consecrata | host; consecrated host | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.11, 1.22). |
| panis / vinum | bread / wine | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.8). |
| corpus Christi / corpus Domini | the body of Christ / the body of the Lord | Kept apart as the Latin alternates them. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.6, 1.10). |
| cultores accidencium / signorum | worshippers of accidents / of signs | Wyclif's name for the defenders of the accident without a subject. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 6.15, prol-c 10.2). |
| cognacio (Christi cum membris) | kinship | With those who do the Father's will (Matt 12:50; 314.21–22). Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-c 10.11). |
| sumpcio | reception | Of the sacrament; *sumere* "receive". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 13.2). |
| missantes | mass-priests | Priests hired to say masses; pejorative. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 15.25). |
| pontifex (a Christian bishop, unqualified) | pontiff | As the Old Testament row; where the referent (a bishop) matters, an R note. *pontifices ydolorum* "pontiffs of idols". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 14.29, 15.17). |
| species (of bread and wine) | species | The sacramental species; kept as the term, not "appearance". Distinct from the logical *species*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 13.15; 23.8). |
| sacer; sacrare | sacred; hallow | Kept apart from *sanctus / sanctificare* "holy / sanctify" and from *consecrare*; *consecrare* is "to hallow together" in the grammarians' etymology. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 27–28). |
| sacramentum tantum | a sacrament only | The *sacramentum tantum* of the Lombard's three (IV d. 8 c. 4). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 29.23). |
| canoniste | canonists | Beside *decretiste* "decretists". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 41.3). |
| conversio (eucharistic) | conversion | Of bread into the body; kept apart from *conversio* of a proposition. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 48.15). |
| decretalis | decretal | Kept apart from *decretum* "decree". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 71.31). |
| transaccidentacio | transaccidentation | Wyclif's coinage beside *transsubstanciacio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 81.27). |
| transinferioracio; transsubieccio | transinferioration; transsubjection | Coinages in the same series. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 82.3). |
| baptiste signorum | baptizers of the signs | Not "Baptists". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 81.29). |
| concomitanter | concomitantly | Of the body present with the blood by concomitance; cf. *gracia concomitancie*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 81.23–25). |
| accepcio personarum | respect of persons | The Douay phrase. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 92.15). |
| consecracio | consecration | The noun of *consecrare*; see *confeccio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 99–100). |
| verba sacramentalia conversiva | sacramental words that convert | The *moderni*'s words of consecration as effecting conversion. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 121.1). |
| concomitancia | concomitance | With *concomitanter*, *gracia concomitancie*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 121.27). |
| provecciores doctores | more advanced doctors | Beside *moderni doctores*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 130.3). |
| ydolatrare | idolatrize | Beside *ydolatria*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 143.24). |
| transaccidencia | transaccidents | In the *transaccidentacio* series. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 145.4). |
| katholicacio | declaration as catholic | The noun of *catholicare*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 156.31). |
| pena talionis | penalty of retaliation | The accuser's penalty in canon law. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 156.4). |
| corpus dominicum | the Lord's body | Kept apart from *corpus Domini* "the body of the Lord" and *corpus Christi*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 158.31, 165.3). |
| in circulo (of the host) | in a round | The round form of the host. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 161.17). |
| nominacio (baptismatis) | naming (of our baptism) | Wyclif's figure for the name the faithful bear. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 172.21). |
| cultor; cultus (sacramenti) | worshipper; worship (of the sacrament) | Beside *cultus Dei* "worship of God" and *cultores accidencium*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 177.3–9). |
| usus (ecclesie) | use | A church's customary practice or way of speaking, and by play its liturgical Use. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 183.25 ff.). |
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
| regnum | kingdom | Every sense: the political state as well as the kingdom of God and scripture's kingdoms. Not "realm". Wilson, Ruled 2026-09-28 (27 sites). |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). Third referent, the logician's arrangement of terms in a proposition (*Incarn.* 49.10): "ordering", with a **C** note; ruled 2026-10-22 (coordinator, delegated). |
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| conducentes | those who hire them | Ruled 2026-09-28. |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| frater | friar (of the mendicants) / brother | By context. |
| possessionati | the possessioners | Endowed religious. |
| satrapa | satrap | Derogatory: church-court officials wielding delegated power (T. p. 378 n. 58). Keep the word; note it at first occurrence per work. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | CONTEXTUAL: condition / respect | "Condition": a person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). "Respect": the logical relation under which a predicate holds (*posiciones secundum habitudinem*), with a **C** note; ruled 2026-10-22 (Wilson; *Incarn.* 4.16). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| insolubilia | insolubles | The logicians' paradoxes of self-reference. Ruled 2026-10-02 (*Eccl.* 175.11). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| franchisia | franchise | Ruled 2026-10-02 (*Eccl.* 239.22). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |
| decretum; decreta | decree; the decrees | Gratian (*in decretis*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.14, 3.24). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| credulitas | credence | With *credere*, believe (*Dial.* 23.17–24.4). Ruled 2026-09-28. |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| practizare | to put into practice | Ruled 2026-09-28 (coordinator, delegated) (4 sites). With *contra* + person, "practise against" (plot), *Dial.* ch. 17. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| respectus; respectivus | relation; relational | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| fallacia | fallacy | Ruled 2026-09-28. |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
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
| propositio copulativa / disiunctiva | conjunction / disjunction | Not "copulative proposition" (T. p. 365). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| redarguere | to refute | T. p. 365. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6); the adjective (*status exproprietarius*) "propertyless", 2026-10-08 (*Pot. pape* 146.25). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| viacio | wayfaring | The state of the *viator*. Ruled 2026-10-02 (42.30). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| penaliter | in hardship | The adverb of *penalitas*. Ruled 2026-10-02 (76.29, 76.34). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| dulia / latria | dulia / latria | Kept as the theologians' terms, glossed once per chunk. Ruled 2026-10-02 (95.17). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| impetrare | obtain (by request) | Ruled 2026-10-02. |
| iugum | yoke (a pair) | Ruled 2026-10-02 (*Eccl.* 202.9 ff.). |
| humanitas | the humanity | The nature the Word assumed, body and soul; with the article (*humanitas sit Christus*, "the humanity is Christ"). Not "the human nature", which is *natura humana*. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| dimittere / dimissio (*naturam*) | lay aside / the laying-aside | Letting go the assumed nature, so the union would be dissolved. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 2.23). |
| triduum (*in triduo*) | the three days | Death to resurrection, body in the tomb (Lombard, *Sent.* III d. 22). Ruled 2026-10-22 (Wilson; *Incarn.* prol). |
| ydemptitas specifica | identity of species | That Christ and other men are of one species. Not "specific identity" (reads as "particular"). Ruled 2026-10-22 (Wilson; *Incarn.* prol, 8). |
| homo assumptus | the assumed man | A term of art (the Lombard's first opinion, *Sent.* III d. 6); keep "assumed" before "man", never "the man assumed". With the agent expressed (*homo assumptus a Verbo*) "the man assumed by the Word", which cannot be misread (coordinator, 2026-10-22). Ruled 2026-10-22 (Wilson; *Incarn.* 5.15). |
| secundum quod (reduplicative) | insofar as | ⛔ Never "in that" (heard as "because", which inverts the logic). Ruled 2026-10-22 (Wilson; *Incarn.* 5.29–6.24). |
| secundum deitatem / secundum humanitatem | as to the Godhead / as to the humanity | The rule of reduplication; keep it in Wyclif's place in the sentence. ⛔ Never supply "as God / as man" where the Latin has bare apposition (*ipse Deus*) or bare predication. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| natura | nature | Ruled 2026-10-22 (Wilson; *Incarn.* 3.4). |
| persona | person | Ruled 2026-10-22 (Wilson; *Incarn.* 4.14). |
| creatura / creator / creatus | creature / creator / created | ⛔ Never "creation" for the created thing. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| posicio / proposicio / predicacio | position / proposition / predication | Kept apart: the apparatus shows the three trading places (*Incarn.* 4.15). Ruled 2026-10-22 (Wilson). |
| sacramentum (of the incarnation, of creation) | sacrament | The Augustinian sense, "mystery" (1 Tim. 3:16): G note at the first occurrence in the chunk. Kept apart from *misterium*. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.8). |
| sancti | the saints | The fathers. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.15). |
| probabiles doctores | reputable doctors | *Probabilis*: worthy of credence (cf. *probabiliter*). Ruled 2026-10-22 (Wilson; *Incarn.* 7.1) as "approved doctors"; changed the same day (coordinator) to free "approved" for *approbati*. |
| determinacio | determination | A qualifying addition to a predicate (*cum determinacione*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 14.11). |
| Sermo (beside *Verbum*) | Speech | The divine title, capitalised; *Verbum* stays "the Word". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 16–17). |
| sophistice | sophistically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 15). |
| de vi vocis / de vi sermonis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| determinaciones ecclesie | the church's determinations | Rulings of the church, not the logician's *determinacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 24). |
| nedum | not only | "Let alone" where the sense is a fortiori. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21, 24). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| gracia unionis | the grace of union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| humanitus | humanly | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* passim). |
| suppositum | supposit | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 34.24). |
| in quantum (reduplicative) | insofar as | As *secundum quod*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37.9). |
| universitas creaturarum | the totality of creatures | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37). |
| pars qualitativa | qualitative part | Body or soul as the parts that make up a man by kind; set against *pars quantitativa*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 43.5). |
| pars discretiva | discrete part | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 46.9). |
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
| ampliativus | ampliative | Beside *ampliacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 57.29). |
| supposibilis | that can be supposited | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 64.14). |
| per se / per accidens | CONTEXTUAL: of itself / by accident; (spatial) apart, by itself | The spatial sense (a thing set apart, *Euch.* 104.16–17) gets a G note. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a (sufficienti) divisione | the topic from sufficient likeness / from (sufficient) division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| pretericio | being past | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| solvere / solucio (of the union) | loose / loosing | Except inside a Douay quotation (John 10:35 "cannot be broken"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| insolubilitas | inextricability | As *insolubiliter*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| peccabilis | able to sin | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| inconsequens | inconsistency | Kept apart from *inconveniens* (an unfitting conclusion). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 78.23). |
| ydemptitas ypostatica | hypostatic identity | Beside *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 84.20). |
| capitales doctores | the chief doctors | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| intricaciones sophistice | sophistical entanglements | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 82). |
| eiusdem / consimilis / alterius racionis | of the same / like / another kind | The species-sense of *racio*; *racio speciei* "the account of the species" (Aristotle's *logos*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.4, 87.17). |
| accidentatus | subject to accidents | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.4). |
| in recto / in obliquo | in the direct case / in an oblique case | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.25). |
| mobilis / mobilitas | movable / movability | Of Christ's humanity (ch. 7). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.11). |
| signum / signatum | sign / thing signified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 91.2–6). |
| conveniencia / convenire (*in*) | agreement / agree | The argument of 90–91 turns on it; not "fittingness" (that is *congruencia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 90). |
| predicacio synecdochica | synecdochic predication | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.27). |
| humidum infantile / radicale | the moisture of infancy / radical moisture | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 94.9). |
| conversari | live one's life (among men) | Beside *conversacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.25). |
| esse intelligibile | intelligible being | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 99.23). |
| faccio | making | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 100.6). |
| extraneare / extraneacio (supposicionis) | estrange / estrangement (of supposition) | *Affeccio extraneandi* "an affection of estrangement". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 98.16). |
| ministerialiter | ministerially | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 100.17). |
| mobile (noun) / primum mobile | a movable / the first movable | Against the adjective *mobilis*; ch. 7 turns on it. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 107, 116). |
| res racionis | thing of reason | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| universitas creata | the created totality | Beside *universitas creaturarum*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| significatum | significate | Kept apart from *signatum* "thing signified". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 111). |
| sermo vocalis | the spoken word | Against *Sermo* "Speech", the divine title. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 113). |
| predicacio secundum essenciam / formalis | predication by essence / formal predication | Wyclif's modes of predication (cf. *predicacio secundum causam*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 115–116). |
| forma substancialis | substantial form | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| redarguere / redargucio | refute / refutation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| concepcio (figure) | conception | The grammatical figure. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habitus (of the humanity) | habit | The Lombard's third opinion (*Sent.* III d. 6). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| accidens | accident | The category; *accidit* "befalls". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habicio | holding | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 119.7). |
| habitacio | habitation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 120.14). |
| figura / figuratum | figure / thing figured | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 121.23). |
| incepcio | beginning | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 121.16). |
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
| supposicio simplex / supposicio personalis | simple supposition / personal supposition | Supposition theory. *Simpliciter / personaliter supponere* "stand with simple / personal supposition": NOT the *simpliciter / secundum quid* pair, C note where the two could be confused. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 152.5–12). |
| transsumpcio | transumption | Beside *transsumptive*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 153.28). |
| personalitas | personality | The scholastic term: what makes a person a person, not character. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 155). |
| aliud / alius | another thing / another one | The neuter against the masculine (*aliud et aliud, non alius et alius*): natures against persons. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 160.1–2). |
| in quid (predicari in quid) | in quid | Kept in Latin (predication of what a thing is, as against *in quale*), glossed at first use in a chunk. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 162.22). |
| suppositari | be supposited | Verb beside *suppositum*, *suppositacio*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 161). |
| substancia prima / substancia secunda | first substance / second substance | Aristotle, *Cat.* 5. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.25). |
| a simili | by likeness | Bare, as an argument form; beside *locus a simili* "the topic from likeness". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.16). |
| racio substancialis | substantial account | As *racio individui* "account". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.21). |
| doctores signorum | the doctors of signs | The logicians who reason from terms, not things. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.26). |
| sensibilis (in the definition of animal) | sentient | *Substancia animata sensibilis*: able to sense. Elsewhere the §D row "perceptible" holds; G note at first use. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 177). |
| ydemptitas numeralis | numerical identity | Beside *ydemptitas specifica* "identity of species". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 172). |
| suppositalis | of a supposit | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 176). |
| accidens absolutum | absolute accident | Quantity and quality, against relative accidents. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 176). |
| mocio / motus (paired) | motion (*mocio*) / movement (*motus*) | Only where Wyclif pairs them; otherwise "motion". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 180). |
| yperdulia | hyperdulia | Beside *dulia / latria*; glossed once per chunk. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 183.13). |
| causancia / causacio | causing / causation | Kept apart (both at 187.30–34). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 185.16). |
| personare (active) / personacio | make a person / personation | Beside the passive *personari* "be made a person". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 188.16, 188.32). |
| peticio (principii) / petitur | begging [of the question] / is begged | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.23). |
| perfeccio simpliciter | perfection without qualification | After *simpliciter* "without qualification". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.1). |
| transsubstanciacio | transubstantiation | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.10). |
| multiplicative | multiplicatively | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 193.20). |
| habitudo relativa | relative respect | The "respect" sense of the CONTEXTUAL *habitudo* row. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 193.19). |
| remitti / intendi (of a quality, merit) | be remitted / be intensified | The intension and remission of forms; not *remissio* of sin. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 197.1–7). |
| in divinis | among the divine [persons] | Keeps "Godhead" for *deitas*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 196.18). |
| universitas creabilis | the creatable totality | Beside *universitas creaturarum* "the totality of creatures". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 199.5). |
| multiplicacio dimensionalis | dimensional multiplication | One body in several places by its dimensions. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.6). |
| habitus (= possession, *habere*) | the having | The category of having, C note; kept apart from *habitus* "habit". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.14). |
| proporcio racionalis | rational proportion | The mathematical ratio. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 207.7). |
| a maiori vel pari | from the greater or from the equal | Arguments *a maiori*; cf. *locus a maiori*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 209.5). |
| sensibile commune | common sensible | Aristotle's common sensibles (number, motion, figure); the term of art, against the §D row "perceptible". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 209.23). |
| mocio progressiva / motus progressivus | progressive motion | Locomotion. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 205.28). |
| communioritas | greater commonness | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 210.15). |
| multiplicacio concomitancie | multiplication of concomitance | Cf. *gracia concomitancie*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 213.21). |
| assertibile | assertible | The thing a proposition asserts. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 215). |
| superioritas / inferioritas terminorum | superiority / inferiority of terms | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 215). |
| exponentes | the exponents | The propositions into which a proposition is resolved (expounded). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 216.14). |
| homo communis | the common man | The universal man, with *res communis*; not "the ordinary man". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 218.3). |
| signum reduplicatum | the reduplicated sign | The reduplicative word (*secundum quod*, *in quantum*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 230.23). |
| supposicio | supposition | Of a term (supposition theory) or of a premiss laid down (cf. *supponitur* "it is supposed"); the English word serves both, C note where it matters. Kept apart from *suppositacio* "suppositation". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 102.8). |
| lex proximitatis | the law of neighbourhood | The duty to love one's neighbour (*proximus*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 101.29). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
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
| figurare | figure | Both senses: to prefigure (the lamb figured Christ) and to shape (*figurare Deum nostrum*), which Wyclif plays on; one English word keeps the pun. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-c 10; 21.29). |
| supponere pro | stand for | Supposition; with *supposicio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 24.27). |
| sensualiter | sensually | Berengar's oath word (*Ego Berengarius*); kept apart from *sensibiliter* "perceptibly". A mode adverb, one word. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 26.1, 30.24). |
| sentire (an opinion: sensit quod) | hold | Of a doctor's or church's opinion; the "perceive" row is the sacrament sensed. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 30.30, 31.18). |
| predicacio figurativa | figurative predication | A synonym of *predicacio tropica*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 35.18). |
| expositorie (of preaching scripture) | by way of exposition | Not the logicians' *expositorie* "expositorily" of the expository syllogism. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 46.4). |
| aliquitas | somethingness | Being a something (*aliquid*). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 60.27). |
| cedere (in) | give way (into) | Of the bread passing into the body. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 58.3, 60.9). |
| informacio; informare | informing; inform | Of a form in its subject; not "information". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 64.13). |
| accidens predicamentale | accident of the categories | Kept apart from the predicable *accidens*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 64.1). |
| revera | in truth | Kept apart from *vere* "truly". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 63.4). |
| contiguacio | contiguity | Beside *continuacio* (of bodies) "continuation". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 68.12). |
| veritas predicamentalis | truth of the categories | As *accidens predicamentale* "accident of the categories". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 69.2). |
| convincere; conviccio | prove conclusively; conclusive proof | Of an argument that compels assent; "convince" never; of a witness or liar shown guilty, "convict" (*Euch.* 01-c). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 78.10, 79.10–12, 85.27). |
| esse situale / intencionale / potenciale | situal / intentional / potential being | The modes of the body's being. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 84.8 ff.). |
| sensus (of words) | meaning | Kept apart from *sentencia (verborum)* "sense" (Wilson's row). The bodily *sensus* and *sensus literalis / misticus* stay "sense". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 89.22, 04-c, 04-d). |
| interpolatus; interpolacio | interrupted; interruption | Of words spoken with pauses. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 89.4, 89.18). |
| noticia confusa / distincta | indistinct / distinct knowledge | As *confuse / confusus* "indistinct(ly)". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-g). |
| ponderositas; ponderosum | heaviness; heavy | The abstract against the concrete: *hostia est ponderositas sed non est ponderosum*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-a p. 10, 110.24). |
| questio si est / quid est | the question whether it is / what it is | *Post. An.* II.1. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 119.18). |
| universitas sua (God's) | his universe | Beside *universitas creaturarum* "the totality of creatures". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 124.31, 129.16). |
| figuracio | figuration | Beside *figura / figurare*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 131.16). |
| naturalitas obediencialis | obediential naturalness | Cf. *dependencia obediencialis*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.15–18). |
| accidentalitas | accidentality | Beside *substancialitas*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.13). |
| quantitas successiva | successive quantity | Time and motion, against permanent quantity. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.1). |
| corpus mathematicum | mathematical body | The three dimensions without matter. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 142.31). |
| insolidus | unsolid | Of the modern doctors' fantasy. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 143.20). |
| ubi; ubicans | where; that which gives a where | The category of place and its cause. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 146.23–24). |
| inpossibilitare | make out as impossible | Of the *moderni*'s argument. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 149.13). |
| utrobique | on both sides | In citation formulae and argument. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 148.21). |
| localiter | locally | A mode adverb, one word; beside *dimensionaliter*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 148.29). |
| conversivus | converting | As *verba sacramentalia conversiva*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 153.6, 153.25). |
| yronice | ironically | Ruled 2026-11-07 (coordinator, delegated; *Euch.* 153.4). |
| signum nature | instant of nature | The scholastic priority without time; kept apart from *signa* "signs". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 161.9). |
| generancia | begetting | Ruled 2026-11-07 (coordinator, delegated; *Euch.* 161.25). |
| ponderacio | weighing | Beside *ponderositas* "heaviness". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 183.17). |
| ydemptifice | by identification | Kept apart from *ydemptice* "identically" (a mode adverb). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 190.3). |
| universitas (bare: tota universitas) | the whole universe | Beside *universitas sua* "his universe". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 192.14). |
| qualitas prima | first quality | Hot, cold, wet, dry. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 197.24). |
| subiectare | be the subject of | Of a substance underlying accidents. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 199.10). |
| visio corporalis / ymaginaria / intellectualis | bodily / imaginary / intellectual vision | Augustine's three kinds (*De Gen. ad litt.* XII). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 206–211). |
| diffinitive (of presence) | definitively | Of being in a place definitively, not circumscriptively. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 216.4). |
| sensus tropicus | tropical meaning | As *sensus* (of words) "meaning". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 217.22). |
| contentive / causaliter / subiective / obiective | by way of containing / causally / subjectively / objectively | The modes of being in the sacrament. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 219.17–22). |
| verba adiectiva | adjectival verbs | Grammar: set against the substantive verb *est*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 230.22). |
| multiplicacio corporis | multiplication of a body | The subject of ch. 8. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 232.5). |
| predicatum infinitum / finitum | infinite / finite predicate | Ruled 2026-11-07 (coordinator, delegated; *Euch.* 235.29). |
| qualitas secunda | second quality | Beside *qualitas prima*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 236.11). |
| non communicans (of times) | not communicating | Of times with no common part. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 241.25). |
| simultas adequacionis / inmediacionis | simultaneity of adequacy / of immediacy | Ruled 2026-11-07 (coordinator, delegated; *Euch.* 247.9–10). |
| mora | abiding | Kept apart from *duracio* "duration" and *diuturnitas* "length". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 257–258). |
| punctale (noun) | punctual | A point-like thing. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 253.10). |
| quando (the category) | the when | Beside *ubi* "where". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 260.23). |
| quandalitas | whenness | The abstract of *quando*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 268.6). |
| eviternitas | eviternity | Kept apart from *evum* "aeviternity" and *evitas* "aeveity". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 266.19). |
| punctalitas | punctuality | Beside *punctale*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 269.25). |

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
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| recencius | more freshly | Pilot (*Dial.* 2.10) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| penalitas | hardship | "penalty". Ruled 2026-09-28. |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| irreligiositas | irreligion | Ruled 2026-10-02. |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "almsman" (the 09-28 row governs; conformed 2026-10-02, *Eccl.* 16). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| dotes (docium) beatorum; dotes corporis | the dowries of the blessed; the dowries of the body | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
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
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| continuacio (of bodies, the act) / discontinuacio; continuare / discontinuare | continuation / discontinuation; make continuous / make discontinuous | The making of several bodies into one continuum (*Incarn.* ch. 12), G note at first use: not "carrying on". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.30, 211.12). |
| precaria | precarial grant | Wyclif defines it (*Eccl.* 453.21). Ruled 2026-10-02 (*Eccl.* 19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| exequie | exequies | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| memoriale | memorial | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| palliacio; palliare | cloaking; to cloak | Ruled 2026-10-02 (*Eccl.* 23, 566.27). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the Eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). Beside *consecrare* (*consecrat et conficit*) "confect", so the pair stays two. Ruled 2026-11-07 (Wilson, "confect works"; *Euch.* 16.10). |
| licencia | licence | Permission granted; never "power". Wyclif usually sets it against *potestas*, but can also identify the two where power is defined as a grant (*illa licencia est potestas*, *Pot. pape* 21.29): render "licence" either way and let the argument show which. Ruled 2026-10-07 (*Pot. pape* 41.21); qualified 2026-10-12 (close-out R1).|
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| procuratoria potestas | proctorial power | From *procurator* "proctor". Ruled 2026-10-07 (*Pot. pape* 63.9). |
| archivicarius | archvicar | Ruled 2026-10-07 (*Pot. pape* 62.20). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| criminosus | criminous man | Ruled 2026-10-07 (*Pot. pape* 06-c). |
| Lincolniensis | Lincoln | Robert Grosseteste, bishop of Lincoln (S note at first occurrence), as in *De ecclesia*. Ruled 2026-10-07 (*Pot. pape* 59.8). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| preeminencia | preeminence | Kept apart from *primatus* "primacy". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| dileccio | love | Kept apart from *caritas* "charity". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-e). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| sessiva / sesina | seisin | *Sesina* the spelling at *Incarn.* 33. So the manuscripts (Loserth 170.8, *ita cod.*); feudal possession that perfects a title. Ruled 2026-10-08 (coordinator, delegated). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| infundabilis; infundabiliter | without foundation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 195–196). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| pompare; pompacio; pompa | boast; boasting; boasting | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 204.11). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| memorativa potencia | memorative power | A faculty of the soul (the "power" sense of *potencia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 219.27). |
| discrasia | distemper | Physicians' term. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 223.1). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| primicia (virtutum) | being first (in the virtues) | Kept apart from *primatus* "primacy" and *primitas* "firstness". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 228.33). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| malum culpe / pene | the evil of fault / of penalty | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.19). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| papa cesareus | caesarean pope | The pope as endowed temporal lord (chs. 10–12). Ruled 2026-10-08 (coordinator, delegated). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| cultus Dei | worship of God | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-d). |
| pontifex (Old Testament, unqualified) | pontiff | Kept apart from *sacerdos* "priest"; *summus pontifex* of the Jewish priesthood is "high priest" (see *summi pontifices*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* ch. 11). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| penalis | hard, of hardship | Beside *penalitas*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 280.20). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| archiprepositus | arch-superior | Formed on *prepositi* "superiors". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 300.17). |
| correptibilis | open to reproof | Beside *corripere* "reprove". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 301.3). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| pallium privilegii | cloak of privilege | Kept apart from *palliacio* "cloaking". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-a). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| procuratorium | proctor's mandate | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 336.11). |
| evangelizans | preacher of the gospel | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-g). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| pagina (of a law) | page | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.13). |
| provisio (papal) | provision | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* ch. 12). |
| proventus | proceeds | Kept apart from *redditus* "revenues". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 353.25). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |
| coloracior | more colourable | Comparative, with the *color* / *colorabilis* rows. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 384.15). |
| specularis prudencia | the prudence of a watchman | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| ars cesarea | the caesarean art | After *papa cesareus*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| servitus ydolorum | servitude of idols | Beside *servitus laboris*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| ingeniacio | wit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 394). |
| cesaree (adv.) | in caesarean fashion | After *papa cesareus*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 403.25). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| insolubiliter | inextricably | Kept apart from *insolubilia* "insolubles". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 404). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |
| nimis | exceedingly | Medieval intensive (= *valde*); "too much" only where excess is the point. Ruled 2026-10-12 (close-out R2; *Pot. pape* 169.2). |
| sentire (the sacrament, the body) | perceive | "sense". As *sensibilis* "perceptible". Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.10, 1.17). |
| singulariter | CONTEXTUAL: alone, only / in a singular way / in the singular (grammatical number, *Euch.* 215.15) | "singularly" never; "in a singular way" where "alone" will not construe (*Euch.* 85.28, coordinator 2026-11-07). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 4.14). |
| fingere (a miracle) | feign | "imagine". Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.11, 1.14). |
| cognacio (family) | kindred | Seth's line apart from Cain's; kept apart from *cognacio* "kinship" (with Christ). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 42.14). |
| ex tibi dubio; ex sibi dubio | for all you know; for all he knows | Idiom: not "from doubt". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 66.15, 70.25). |
| rima | chink | Wyclif's figure for a loophole. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 216.21). |
| precavicio | precaution | Ruled 2026-11-07 (coordinator, delegated; *Euch.* 249.10). |
| secta signa colencium | the sect of those who worship signs | Beside *secta signorum*, *cultores signorum*. Ruled 2026-11-09 (coordinator, delegated; *Euch.* 278.11). |
| informacio (ecclesie) | instruction | The church's teaching; apart from the *informacio* row (a form in its subject). Ruled 2026-11-09 (coordinator, delegated; *Euch.* 284.17). |
| vertibilis | turnable | Ruled 2026-11-09 (coordinator, delegated; *Euch.* 291.6). |
| sensus vicarius | vicarial meaning | Ruled 2026-11-09 (coordinator, delegated; *Euch.* 296.12). |
| melioracio | betterment | Ruled 2026-11-09 (coordinator, delegated; *Euch.* 293.13). |
| tropare; tropicare | trope; take tropically | The verbs of *predicacio tropica*, beside *tropice*. Ruled 2026-11-09 (coordinator, delegated; *Euch.* 296.23–297.3). |
| commultiplicare | co-multiply | Of the accidents multiplied with the body. Ruled 2026-11-09 (coordinator, delegated; *Euch.* 298.13). |
| ydolatria | idolatry | Beside *ydolatrare*. Ruled 2026-11-09 (coordinator, delegated; *Euch.* 297.25). |
| signum vicarium | vicarial sign | Beside *sensus vicarius*. Ruled 2026-11-09 (coordinator, delegated; *Euch.* 303.14). |
| septipedalis; septipedalitas | seven feet long; seven-foot length | Ruled 2026-11-09 (coordinator, delegated; *Euch.* 301.7, 302.1). |
| quantificacio | quantification | Ruled 2026-11-09 (coordinator, delegated; *Euch.* 303.1). |
| esse presenciale / virtuale / actuale / propinquum | presential / virtual / actual / proximate being | The modes of one thing's being. Ruled 2026-11-09 (coordinator, delegated; *Euch.* 305.28–306.6). |
| Magister (in historiis) | the Master [of the *Histories*] | Peter Comestor, *Historia scholastica*; apart from the *Magister* row (Lombard). Ruled 2026-11-09 (coordinator, delegated; *Euch.* 306.6). |

---

## Chunk 09-j: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-09-j.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-09-j
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "307.24–311.30"
divisions: "cap. 9 (heading 'CAPITULUM NONUM.' at 272.0); part 10 of 14, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "908 words; 895 confirmed by the vote; 13 runs stood by rule; 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n378–n382 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 9, part 10: [TITLE]

## ¶1 · 307.24–309.16

> [p. 307] Quantum ad mocionem corporis Christi videtur homines in ista materia loqui dupliciter vel tropice ad sensum quo concedunt illa que contingunt sacramentum corporis Christi contingere (ut loquitur decretum Ego Beringarius) vel sine figura ydemptice, modo quo dicitur Deum esse ubique et Petrum solum esse ubi est diffinitive; et sic videtur corpus Christi post ascensionem nedum non moveri in terris nec esse, sed virtus sua est per totum mundum, cum perficit [p. 308] humanitus quamlibet creaturam. Sed propter innovacionem vel incepcionem virtutis non oportet corpus Christi correspondenter moveri, sicut non oportet regem moveri correspondenter ad motum baiuli suas litteras deferentis. Quamvis enim corpus Christi sit ubique, eciam per totum mundum sublunarem, tamen est quadam singularitate in sacramento altaris; sed sicut non alteratur vel movetur in quantitate ad motum hostie, ita non movetur localiter correspondenter ut ipsa movetur localiter, quia non acquirit sibi ex motu hostie quantitatem aut qualitatem, sicut nec ex delacione hostie sibi acquirit novum, quod sicut corpus Christi non conburitur conbusta pixide, sic nec elevatur nec submittitur presbitero hostiam sic movente. Et patet quod corpus Christi non evomitur vel screatur. Et quoad manducacionem patet ex dictis dupliciter potest intelligi, vel tropice vel ydemptice; ydemptice non manducatur corporaliter sed spiritualiter a fideli, dum mens sua pascitur ex memoria corporis Christi; et sic non potest manducari a bestia nec manducatur sic a simpliciter fideli, sed indignus manducat sacramentum et accipit corpus Christi. Unde aliud est capere, aliud manducare; nam multi accipiunt Spiritum Sanctum qui non est mobilis nec corporaliter manducabilis; aer eciam secundum sic loquentes accipit corpus Christi, sicut os hominis; intestina eciam bestiarum in tantum quod nedum corpus Christi est ad omnem punctum mundi sed sacramentaliter est in interioribus bestiarum, cum posset ab illis forma panis extrahi; et quamdiu remanet forma panis aut vini consecrata, dicunt adversarii corpus Christi eciam quantumcunque modica [p. 309] particula sacramentaliter remanere. Et isto modo videtur Thomam dicere super distinccione IX, questione IIᵃ, quod creatura irracionalis sumit corpus Christi. Wilelmus autem in De Sacramento Altaris videtur dicere quod quinque modis accipitur corpus Christi et sic mus (ut inquit) comedit corpus Christi realiter sed non sacramentaliter neque spiritualiter. Sed absit, licet omnes isti (eciam papa) dixerint, quod bestia et omne manducans hostiam manducat propterea corpus Christi, sicut exemplificatum est de anima, ymmo loyci dicunt quod, sicut fons, lacus vel bestia accipit aquam que de facto est sacramentum baptismi, et tamen non baptizatur vel accipit baptismum, sic multa accipiunt illum panem vel illa accidencia, que de facto sunt sacramentum, et tamen non accipiunt sacramentum quia non sub racione sacramenti.

[ENGLISH]

## ¶2 · 309.17–311.15

> [p. 309] Sed dimissa ista altercacione loycis concedo cum glossa communi super distinccione secunda, capitulo Non iste, quod corpus Christi non descendit in stomachum, et usque ad quem locum ducitur per gulam nescio. Unde textus vere dicit: Non iste panis est qui vadit in corpus. Tripliciter enim accipitur panis ad propositum in scriptura sacra et sanctis doctoribus, scilicet pro pane usuali quem vulgus comedit, pro pane consecrato qui est sacramentum; quem Augustinus vocat panem celestem, et pro pane ultimo figurato qui est Christus Deus noster. Et istam equivocacionem sicut equivocam istorum predicacionem oportet theologum notare. Si enim panis qui est corpus Christi [p. 310] gloriosum in celo foret in sua persona nobiscum, ut sentimus de hostia, nullus vivens hanc vitam sufficeret suffere gloriam et extasim quam inferret; nam Petrus in transfiguracione cadebat ut mortuus. Sed in pane et vino figuratur nobis corpus Christi gloriosum, ut allegavi superius Augustinum et Rabanum et Damascenum. Scribit enim iste Grecus IIIᵒ Sentenciarum suarum, capitulo VIIIᵛᵒ: Quemadmodum consuetudo est homini aqua lavari et oleo ungi quo coniuncta gracia Spiritus Sancti facit lavacrum regeneracionis, sic quia consuetudo est hominibus panem comedere, vinum et aquam bibere, coniugavit Deus ipsis sui ipsius deitatem et fecit ipsa corpus et sanguinem sui ipsius. Nec repugnat sed consonat quod dicitur eodem capitulo quod panis et vinum transit et transsubstanciatur in corpus Christi et sanguinem. Per hoc enim quod dicit Deum fecisse ea corpus suum et sanguinem, patet quod intelligit ipsa esse tropice corpus Christi et sanguinem ad modum loquendi scripture; nam ut dicit Scotus: Eodem spiritu exponende sunt scripture quo condite erant; et sic ecclesia katholica ad illum sensum exposuit ad quem docuit. [p. 311] Sed absit fidelem ex illo concludere quod si Innocencius IIIᵘˢ cum suis satrapis sic diffinit, tunc ecclesia katholica ita sensit; verumptamen (ut dixi) presumpcio est quod katholice sensierunt de transsubstancione et accidentibus modo quo supra exposui, et non contrariabantur sanctis qui dicunt quantitatem et qualitatem non posse per se esse; sed generaliter modo scripture vocant ea panem et vinum, et sic intelligunt ipsi bene per sua accidencia, quia XXV, questione prima, Sunt quidam, dicit Urbanus papa katholice: ubi vero aperte Dominus vel eius apostoli et eos sequentes sancti patres sentencialiter aliquit diffinierunt, ibi non novam legem Romanus dare potest sed pocius quod predicatum est usque ad animam et sanguinem confirmare, quia aliter nimium oberraret.

[ENGLISH]

## ¶3 · 311.16–311.30

> [p. 311] Cum ergo auctores scripture et sancti doctores concorditer vocant sacramentum panem quem dicunt esse corpus, grave esset illa verba vel sensum illum impetere; scio tamen quod pontifices eciam Romani possunt seduci ad tantum et amplius, cum possunt errare in articulo plus necessario ad viacionem ecclesie, scilicet quod expedicius et perfeccius est eis dotari cesarie quam sequi statum exproprietarium quem Christus verbo et facto docuit et servandum suis discipulis dereliquit. Iste enim error est maior quam foret credere non esse eukaristie sacramentum; et cum error unus ducit in reliquum, creditur quod in penam erroris prioris ecclesia cadebat in reliquum exponens scripturam sacram et sanctos doctores yronice per suum contradictorium.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 308.12: Christ's body is not subject to be burned, eaten or vomited.
- 308.26: According to our opponents a beast's belly receives Christ.
- 309.9: To take the elements is not to take the sacrament, unless they are taken as the sacrament.
- 311.16: We know the Roman pontiffs can err, as in the matter of endowment.

## Notes

## Transcription notes
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 307:
3. Codd.: nitllo modo. 4. E: et corporeitas. 5. D: alia.
j.Codd. : oculus. Correxi. 9.E: celi. 21.D: excitatur. 22. AC : eciam a;
ib. B: et — manducahfr deest. 27. D: corpus. 28. C:-sine in marg.
afia manu; ib. D: ydemptijice. 3i. B: movetur. 32. C: sed in marg.

p. 308:
12. ABCD: sic nec ; ib. ACDE: acquiritur. i3. ABC: ubi sicut.
i5. ABC: sub presbytero; ib. ABC: moventem. 16. D: evomit.
17. Codd.: et dictis. Corrcxit; ib. Addc: quod dupliciter. 21. ABC: nec
sic; ib. D: a simplici. 22, 23. D : el — Christi dcest. 23. E: et aliud
after capcre.. 25. ABC: corporalis. 39. ABCD: in decst.

p. 309:
1. E: sacramentaliter remanere deest. 4. D: ibi de. 11. D: locus.
i3. AB: Etsic; ABC : multi ; C: correxit. 18. C in marg. : De conse-
cracione. 19. E: Nonuste. 22. Codd.: cadit. 23. ABC: sacra deest.
24, 25. C: quem - pane in marg. alia manu. 28. ABC: sicut equivocacionem.
2. Recte dist. IX, quaest. I, Art. II 1. c. pag. i3q, 140.
3. Wilhelmus, sc. de Sancto Amore. 19. Decr. Tertia Pars,
De Consecracione, dist. II, cap. LVI. Gf. Glossam ord. ad vocem
Non iste panis. 26. Opp. tom. III, 2, 494, V, 326, 334, 33q, 344
(et passim).

p. 310:
2. D: vivus; ib. E: meam; A in textu: meam; supra scr. : vitam;
C: vitam decst. 3. B: sufficere. 6. E: et deest. 8. C: quemad-
modum in rasura. 9. ABC: hominum. 12. D: coniungavit.
i5. ABCD: capitulo scilicet. 18, 19. ABC: patet — sanguinem deest.
8. Cf. Jacobi de Misa, De vera existencia corporis Christi in
S. Coena, von der Hardt Rer. conc. Const. II, 906. Non sunt
Sentenciarum libri, sed De Fide Orthodoxa lib. IV. Opp. tom. I,
pag. 269, cap. XIII: Et sicut in baptismo, quoniam in more
hominum positum est, ut aqua laventur et unguantur oleo,
Spiritus graciam cum oleo et aqua copulavit, ut lavacrum rege-
neracionis illum faceret: consimili . modo quia hominum con-
suetudo fert ut panem edant vinumque et aquam bibant, idcirco
coniuncta cum illis sua divinitate, haec corpus et sanguinem
suum fecit, uti per usitata et naturae consentanea assurgamus
ad ea, quae supra naturam sunt. 20. Reportatorum Parisien-
sium, lib. III, dist. XXIV, schol. IV, pag. 520 (et alibi).

p. 311:
i. DE: isto. 3. E: sic sensit; ib. D: ubi tamen. 7. D : possunt ;
Codd.: ipsi si. 10. C: quidam alia manu. 10, 11. Codd. : ubi primo.
11. ABCD: apte. i3. Romanus adde: pontifex (ut in decretali super
memor.) ; ib. potest ; ABC : post. 14. E: usque deest. i5. ABCE:
oberarem. 20. C: ad tantum in marg. alia manu. 22. Codd.: sed
quod; ib. D: cesariem; ABC : cesarie. 27. ABDE: unns deest; ib.
A: reliquum; Codd.: reeum = reliquum; ib. ABC: in pena.
10. Decr. Sec. Pars, causa XXV, quaest. I, cap. VI.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 307: non corvoreis oculis | Deum in celo ultra finnamentum vidit, cum nulhus | hominis visus ullomodo usque ad celum vertinsrere | possit. Sed et concio illa in qua Stephanus stans | Christum conspexit in domo aliqua fuit cuius tecti culmen ipsius corporeus oculus minime penetrare potuit. Constat igitur, | quod nec oculo corporis sed intuitu interioris hominis Christum non in corporeo sed intellectuali celo viderit. | Ego Beringarius)
p. 309: creatura irracionalis sumit corpus Christi. | sic mus | comedit corpus Christi realiter sed non sacramentaliter neque spiritualiter. | corpus Christi non descendit in sto~ | usque ad quem locum ducitur per gulam nescio. | Non iste panis est qui vadit in corpus. | panem celestem,
p. 310: Qiiemadmodum consuetudo est homini aqua lavari et oleo ungi quo coniuncta gracia Spiritus Sancti facit lavacrum re- | generacionis, sic quia consuetudo est hominibus panem comedere, vinum et aquam bibere, coniugavit Deus ipsis sui ipsius deitatem et fecit ipsa corpus et sanguinem sui ipsius. | panis et vinum transit | et transsubstanciatur in corpus Christi et sanguinem. | Eodem spiritu ex- | ponende sunt scripture quo condite erant;
p. 311: Sunt quidam, | ubi vero aperte Dominus vel eius apostoli et eos sequentes sancti patres sentencialiter aliquit diffinierunt, ibi non novam legem Romanus dare potest sed pocius quod predicatum est usque ad animam et sanguinem coniifirmare, quia aliter nimium oberraret.
```

---

## Chunk 09-k: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-09-k.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-09-k
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "312.1–316.22"
divisions: "cap. 9 (heading 'CAPITULUM NONUM.' at 272.0); part 11 of 14, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "1068 words; 1055 confirmed by the vote; 12 runs stood by rule; 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n383–n387 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 9, part 11: [TITLE]

## ¶1 · 312.1–312.17

> [p. 312] Unde sicut fratres palliant vitam cesaream consensu multiplici, sic sophisticant in materia de accidentibus eukaristie; sed sicut sunt in signis, professione et opere contradictorii sibi ipsis, sic alternatim contradicunt in materia de accidentibus sacramenti; ideo non est conveniens in hoc testimonium eorum; et cum evidenter creditur quod facta generali sinodo plures voces haberet in utrolibet istorum articulorum pars Antichristi quam pars Christi et sic amplius seduceretur ecclesia, ideo debemus pulsare Veritatem obnixius, ut in utroque istorum, et specialiter in primo quod plus spectat ad mores reducat fideles, quia quoad paginas contra scripturam non est aliud nisi adducere corruptos satrapas qui sciant exponere veritatem scripture per eius oppositum. Et ista sentencia erit diffuse katholica et contraria proscripta tanquam heretica.

[ENGLISH]

## ¶2 · 312.18–313.17

> [p. 312] Sed fideles in veritate confidunt quod, sicut in tempore Christi inposuerunt Christo et suis gravissimum genus heresis quod est blasphemia, et post hec tiranni cruciantes martires Christi inposuerunt eis heresim ac infidelitatem non colendo deos eorum, sic necesse est quod succedat in ecclesia pestis gravior, inponens fideli heresim, quia defendit veritatem scripture. In omnibus enim istis docetur commune proverbium quod viciosus cicius impetet adversarium suum ex crimine in quo timendo redargucionem se noverit magis reum. Et in omnibus istis est fides cum karitate et paciencia optima medicina. Scimus quidem quod ante tribunal Veritatis omnes astabimus, ubi non clamor vel multitudo testimonii sed ipsa veritas facti ante oculos iudicis accusabit. Nam si vel [p. 313] propter magnificenciam nostram vel pecuniam a populo cumulandam ipsos errare facimus, peccata illorum comedimus et nos ipsos pro duplici crimine ipsorum et nostra cecitate temeraria obligamus, dicente Gregorio Omelia XVII: Debemus, inquit, sine cessacione meminisse quod de quibusdam Osee dictum est: Peccata populi mei comedunt et sunt hii qui delinquencium peccata fovent ne temporalia stipendia vel honores amittant. Sed et nos qui ex obligacione fidelium vivimus quod illi pro peccatis suis nobis conferunt, si comedimus et tacemus, procul dubio eorum peccata comedimus. Quid enim oportet infundabiliter in magnificencia sacramenti fingere nostram excellenciam sine fructu? Unde frequenter mirando movebam quid movit primos glossatores sic dicere, et cum nec racio nec testimonium, solum superest revelacio vel scriptura.

[ENGLISH]

## ¶3 · 313.18–314.3

> [p. 313] Quantum ad revelacionem, in diebus eorum fuit sermo Domini preciosus; scripturam autem cum sensu suo nesciunt allegare; et cum scriptura tam crebro vocat hostiam panem, periculosum videtur credere vel docere quod Spiritus Sanctus intellexit per panem illum non panem sed accidens aliene nature, cum sancti et racio contradicant. Non enim est racio quin panis sacratus et vinum simpliciter sint sacramentum corporis dominici, sicut aqua benedicta sit sacramentum baptismi et sic de aliis sacramentis; nec est racio quod Deus deteriorat universitatem suam, destruendo signi substanciam sine causa; nec est racio quod Veritas ordinet sacramentum tam spirituale, ut sit [p. 314] falsum tanquam insolubile puerorum, sic quod illa accidencia sensibilia significent panem vel subiectum suum ad esse, dum totaliter ibi desit.

[ENGLISH]

## ¶4 · 314.4–316.9

> [p. 314] Sed sicut false memoramur vitam Christi conversando contrarie, sic Deus permittit nos false signa concipere. Concedo tamen quod inconveniens est ecclesiam tam diu errasse in speculabilibus, sed maius inconveniens est ipsam diucius sic errasse in operabilibus et (ut credo) superiores ac inferiores huius secte discredunt quod referunt, cum nunquam vel raro celebrant, et tamen longe plus et fervencius laborant pro faccione nedum temporalium ut auri modici sed pro possessione vel habicione eorum (que est respectus debilissimus) acquirenda. Quomodo ergo credam ex opere quod talis convertit panem suum in regnum celorum, quia personaliter in corpus Christi, quod exinde credit perpetuo se habere; ymmo si credit plene evangelio, laboraret pro cognacione Christi habenda, qui Matth. XIIᵒ, 5 dicit verissime: Quicunque fecerit voluntatem patris mei qui in celis est, ipse meus frater, soror et mater est. Ista quidem cognacio que ex tanta auctoritate procedit cum verbo substandi foret longe melior quam conficere, tractare vel (ut ipsi inquiunt) facere corpus Christi. Cultum autem rectum non reprobo sed desidero et procurarem quantum sufficio, sed cultum infidelem et duplicem detestor quo adoratur sacramentum tamquam ydemptice corpus Christi. Pocius autem concederem cum Augustino, Lincolniensi et ceteris quod omne membrum Christi sit realiter et vere sed participacione quadam dominus Jesus Christus; nam quodlibet tale [p. 315] est membrum vivum Christi, ipso Christo in se loquente et faciente omnia eius viva opera tanquam quidditate intrinsecus informante, quod deficit a sacramento altaris; ideo evidencius ex racione et scriptura Christus faceret se esse quodlibet membrum suum. Aliter enim, supposita fide scripture Math. XXVᵒ, pascendo vel opus misericordie inpendendo uni in nomine Christi, sic faceret homo duobus hominibus, et sic de indigenciis eorum et toto facto foret falsum Christum tunc fuisse esurientem, sicientem aut nudum nisi fuerit eius membrum, quia posito quod scimus post ascensionem quando Christus esuriit et sic patitur, patet quod non in persona propria sic modo patitur. Et illud considerarent fingentes accidencia esse sine subiecto propter hoc quod Christus vere sed figurative dicit panem esse corpus suum. Utrumque enim dicunt simpliciter; nec convincetur ex scriptura, racione vel sanctorum testimonio plus unum quam aliud preter glossatores recentes qui ficte fabricant novam fidem; et (ut tactum est) non est maior color: Si Innocencius IIIᵘˢ sic determinat, ergo verum; quod si ipse cum complicibus determinat quod rex Anglie solvere debeat sibi et sedi sue in perpetuum nongentas marcas annuatim in partim pecunie pro commissis, tunc hoc fuit consonum racioni; utrobique enim est tanta auctoritas. Sed Anglici et cuncti fideles dicerent quod illud fuit irreligiosa cupiditas; ideo suspecta est eius assercio nisi de quanto est fundabilis in scriptura. Revera si per inpossibile Jesus noster sic sibi et suis apostolis accumulasset lucrum pro crimine, tota evangelisacio sua suspecta fuisset fidelibus, ideo sicut docemur in practica noscere istam [p. 316] fallaciam: Robertus Gibbonensis asserit sic cum suo clero, ergo verum; et secta sua tanta probabilitate negat consequenciam istam: Urbanus noster cum suis cardinalibus sic determinat, ergo verum. Sic docemur noscere has fallacias in quocunque Petri vicario et specialiter post dotacionem ecclesie. Sic enim negamus tanquam plenam fallaciam: si Johannes archipresbiter successor sancti Thome in India sic asserit, ergo verum.

[ENGLISH]

## ¶5 · 316.10–316.18

> [p. 316] Septimo dubitatur: Si eukaristia sit latria vel dulia adoranda, et videtur quod latria, quia non est adoranda nisi ut ymago Dei, nec absolute ut ymago, sed ut figurative et vicarie ipse Deus, sed ut sic est adoranda latria, ergo conclusio: Adoramus enim crucem Domini non sub racione qua truncus putridus sed sub racione qua Deus in ipsa passus fuit pro nobis. Sic enim Alexander Magnus adoravit sacerdotem Jerusalem, ut dicit magister in historia Machabeorum.

[ENGLISH]

## ¶6 · 316.19–316.22

> [p. 316] Sed contra illud videtur quod Christus quoad humanitatem adorandus est yperdulia (ut hic supponitur), ergo hostia et ymagines adorande sunt adoracione inferiori.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 312.1: Friars support falsehood on that point as on the Eucharist.
- 312.18: The faithful are charged with heresy, as were Christ and His apostles.
- 313.18: The makers of the gloss had no revelation, and Scripture is against them.
- 314.4: The prevalence of false belief is God's punishment for our evil life.
- 315.1: Identification might be asserted of the members of Christ as well as of the sacramental bread.
- 315.21: If we are to accept all Pope Innocent says, we must pay tribute as he appointed.
- 316.9: What kind of worship is to be rendered to the host.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 313: *fidelium* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 312:
1. D: cesariam. 6. ABC: et deest. 8. C: haberent in marg. alia
manu; ib. B: utroque. i3. D: paganos. i5, DE: illa. 20. C: est
in marg. alia manu. 21. D: tyrannie ; ib. D: inposuit. 27. D: de cri-
mine. 29. ABC: caritate cum; AB: et deest; C: in marg. alia manu.
3o. C: quod in marg. alia manu: ib. E: stabimus. 3i. E: non multitudo.

p. 313:
r. C in textu: tnagnitudinem ; inmarg. : magnificenciam. 6. ABCD :
in Osee. 8, 9. D : stipendiales honores. 10. In textu S. Gregorii :
Sed et nos qui cx oblacionibus fidelium vivimus, quas illi pro peccatis suis
obtulerunt. 12. DE: Qiiid ergo. 14. B: numerando. i5. ABC: movebat.
26. DE: fit. 3o. ABCD: speciale.
5. S. Gregorii, In Evangelia, lib. I, Hom. XVII, Opp. tom. I, 1490.
6. Osee IV, 8. 18. I. Reg. III, 1.

p. 314:
7. DE: speculacionibus. 11. E: et before fervencius deest.
i3. E: aut; ib. ABDE: habitacione ; ib. E: qui. 14- D: debitissimus.
19. ABC: quia. 20. ABC: celo. 27, 28. DE: ydemptifice. 29. ABC:
quod et. 3o. D: fit. 3i. D: dominus ?ioster.
29. Cf. Aug. Opp. tom. V, 1346, 1412, 1 4 1 3 ; IV, 1083, 1394
(et alibi).

p. 315:
i. ABC: ipsi; C: correxit. 4, 5. AB: et sic faceret ; C: C/iristus
in rasura. 10, 11. ABC: nec fuerit. 11. scimus; C: correxit: simus.
i3. E: sicut. i5, 16. AB : licet figurative ; B: sed supra lin.j C: sed ;
licet extinct. 16. D: Vtraque. 18. D: testimonia. 20. C: tactum in
rasura: ib. C: est betore maior in marg. alia manu. 28. ABC: est
quelibet; C: eius alia manu. 29. E: ex scriptura. 32. E: a fdelicus.

p. 316:
l. ABCE: Gillianensis ; D: Giibone?isis ; ib. D: cum sic. 3. Codd.:
negant. 10. ABC: utrum eukarisiia; E: si adoracio eukaristie.
12. D: ubi. 21. ABCE: adoranda. 23. C: homo in marg. alia manu.
7. De Johanne presbytero cf. Wyclifs Sermones III, 77.
17. Cf. Flavii Josephi Antiq. Iud. Lib. XI, Cap. VIII, 5.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 313: sine cessacione meminisse quod de quibusdam Osee dictum est: Peccata populi mei comedunt et sunt hii qui delinquencium peccata fovent ne temporalia stipendia vel honores amittant. Sed et nos qui ex obligacione lofidelium vivimus quod illi pro peccatis suis nobis conferunt, si comedimus et tacemus, procul dubio eorum peccata comedimus. | in diebus eorum fuit | sermo Domini preciosus;
p. 314: Qiiicunque fecerit voluntatem patris mei qui in celis | esty ipse meus frater, soror et mater est.
p. 316: velato capite, | et eciam.
```

---

## Chunk 09-l: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-09-l.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-09-l
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "316.23–320.22"
divisions: "cap. 9 (heading 'CAPITULUM NONUM.' at 272.0); part 12 of 14, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "913 words; 898 confirmed by the vote; 11 runs stood by rule; 4 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n387–n391 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 9, part 12: [TITLE]

## ¶1 · 316.23–317.3

> [p. 316] Confirmatur ex hoc quod omnis homo ad ymaginem Dei factus expressius representat Deum et est natura superior quam hostia consecrata. Unde quia fuit origo femine non originatus ab alio sue nature, precipit Apostolus quod oret in ecclesia velato capite, ut patet I. Cor. XIᵒ, 5. Et naturales cum mandatis Domini docent omnem hominem diligi et magnates [p. 317] precipue honorari; honoracio vero vel dileccio hostie non habet tantam auctoritatem, cum homo sit expressius sacramentum.

[ENGLISH]

## ¶2 · 317.4–317.7

> [p. 317] Hic oportet primo cognoscere quod aliquid adoratur ut signum alterius quod adoratur in ipso et aliquid in natura preeminenter adoratur ut Deus; et isto modo nemo rite adorat hostiam et specialiter si sit quantitas.

[ENGLISH]

## ¶3 · 317.9–317.29

> [p. 317] Secundo notandum quod multiplex est racio adorandi naturam racionalem, vel pro excellencia quam ex se habet qualiter solus Deus est adorandus, vel pro excellencia quam a Deo participat, sive fuerit angelus sive homo secundum excellenciam secularem sive excellenciam sacerdotalem. Unde secundum istam racionem mediam Jacob adoravit Esau fratrem suum Genes. XXXIIIᵒ. Sed tercio modo adoramus ymagines nude ut signa, Deum autem debemus quantum sufficimus adorare. Sed in adoracione creature consistit nimia religionis perturbacio ut ydolatria et personarum accepcio; quandocunque enim per se adoratur ymago creata ut Deus vel inordinate aut moroso amore committitur ydolatria. Et isto modo dicit Apostolus Ephes. Vᵒ, 5 quod avarus est ydolorum servitus. Et in isto peccato gentes quas vocamus infideles laborant, adorantes bestias vel simulacra muta tanquam ymagines Dei quem adorant et credunt finaliter. Et in ista ydolatria nos vocati christiani peccamus sepe plus barbaris adorando sanctorum ymagines, reliquias et sacramentum altaris.

[ENGLISH]

## ¶4 · 317.30–318.11

> [p. 317] Unde penes infideles fiunt plura vocata miracula, ut decipiant infideles. Religio autem christiana primeva non habuit tales ymagines nec sanctos canonisatos [p. 318] sed vixerunt perfeccius nobis in fide filii Dei, cum omnia talia signa non adiuvant nisi de quanto iuvant et excitant ad Christum sponsum ecclesie diligendum. Et hinc creditur Deum ordinasse corpus matris Domini non adorari in loco habitabilis nostre, ut nec corpus Moysi in lege veteri nec coli corpora Apostolorum tam sumptuose et splendide, sicut coluntur corpora sanctorum in Anglia. Et hinc creditur Apostolum tam crebro vocare sacramentum altaris panem. Et omnia ista sicut prohibicio ymaginum erant propter ydolatriam precavendam.

[ENGLISH]

## ¶5 · 318.12–318.29

> [p. 318] Conceditur ergo quod reliquie, ymagines et sacramenta sunt cum prudencia adoranda. Ille ergo qui sciret suspendere consideracionem signi sensibilis et appendere totam intencionem et affeccionem in creatore ymaginis, modo quo clericus suspendit scripturas concipiendo sentenciam; ille inquam adoraret latria Deum in illo signo. Sed nimis multi sunt layci et bestiales sensibilibus nimium intendentes et multi, ut loquitur Apostolus Iᵃ Cor. XIIᵒ, 2, cum adorando hostiam tanquam gentes ad simulacra muta prout ducebantur captivi euntes ad ydolatrandum sicut brutum ad iugum servilis operis. Qui autem adorat humanitatem Christi ut talem in hostia, adorat in ipsa Christum yperdulia, et nemo rite adorat ipsam sub racione propria, et sic vere concluditur quod homo sit multiplicius honorandus quam hostia et adorandus tanquam ymago Dei, vas virtutum et sic Christus, verius quam hostia consecrata.

[ENGLISH]

## ¶6 · 318.30–320.14

> [p. 318] Et sic creditur quod error circa cultum hostie dimittit caritatem in homine. Tres enim sunt cause profectus et fructus huius sacramenti scilicet ut pax et caritas in hominibus augeatur, ut memoria gratitudinis [p. 319] Christi recencius habeatur et ut vigilancius in modo conversandi misse particeps Domini exequatur; et omnium horum trium opposita contingunt populo et specialiter sacerdotibus misse qui ex officio pro istis tribus magis sollicite laborarent. Nemo enim plus perturbat pacem Christi, extinguit caritatem, minus fructuose memoratur vitam Christi, ut sequatur ipsum in moribus quam faciunt sacerdotes, et specialiter prelati qui ad hoc ex nomine plus tenentur. Debemus enim instar Christi minus intendere mundo cum suis ritibus, plus aufugere secularia desideria cum suis contencionibus, cum ipsa plus extinguunt pacem et karitatem ecclesie. Nemo minus studet, ut vivat conformiter vite Christi, ymmo nullus Antichristus magis ab ea degenerat, cum non studemus circa vitam parcam penalem et exproprietariam, quam indubie Christus vixit in terris, sed circa vitam largam, lautam, proprietariam, pompaticam et maxime secularem. Cum ergo cultus hostie maxime consistit in complexu istorum trium et in aufugio horum: ita non in preciosis vel sumptuosis ornamentis nec in ritibus inclinacionum, genuflexionum vel decapuciacionum sed in mente pura et sanctitate vite conversacioni Christi similis. Et hinc videtur quod sacerdotes quibus singulariter commissum est hoc ministerium debent in paupere vita sequi Christum et sine offensione ecclesie vel cura de propriis habere omnia in communi, ut dicit Apostolus Iᵃ Cor. Xᵒ, 17: Unus panis et unum corpus multi sumus. Unde solebam pro tempore illius perturbacionis et invasionis regni nostri asserere quod, cum bona regni in manibus religiosorum sint bona pauperum, quorum bonorum ipsi religiosi sunt procuratores [p. 320] non domini, expediret communitati regni in parliamentis constanter instare quod de bonis illis pauperum magis vacantibus regnum intrinsecus ab hostibus defendatur, servatis bonis vivis ad usus pauperum et proviso religiosis sic alleviatis de necessariis vite et ministerio eorum; quod fieret si pensata gravitate, quantitate, qualitate ipsorum limitata sit eis porcio bonorum de quibus debent racionabiliter contentari. Tota ista sentencia patet ex dictis alibi; et repetitur hic triplex sentencia, nam Wilhelmus Conquestor cepit nedum temporalia sed possessiones et vitam licite ab Anglicana ecclesia in Deum et ipsum leviter delinquente: ergo multo magis licet regi et regno micius recipere elemosinas a sua ecclesia gravius delinquente.

[ENGLISH]

## ¶7 · 320.15–320.22

> [p. 320] Secundo confirmatur idem arguendo ad hominem per hoc quod domini temporales Anglie capiunt ab ecclesia Francie nimis rigide temporalia (ut probabiliter creditur) minus quam propria ecclesia delinquente, ergo possunt licencius ex maiori causa ab ecclesiis suis hec facere. Nec dicent satrape nostri utrumque istorum fuisse illicitum, quia virtute primi tenent sua predia et ad secundum consulunt et conducunt.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 317.4: It is to be worshipped as a symbol, not as God.
- 317.9: Different kinds of adoration: 1. of God; 2. of man as sharing in God's excellence.
- 317.16: 3. of images, simply as symbols.
- 317.18: Danger of idolatry in this.
- 317.30: There were neither images nor Saints in the primitive Church.
- 318.12: We may adore relics and images, but only in fixing our mind on the Creator.
- 318.30: Error as to the host lessens charity.
- 319.5: Most of all do priests fail in carrying out the purpose of the sacrament.
- 320.1: Endowments should be usefully applied.
- 320.15: Our nobles take property from the church of France.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 316: *XIᵒ,* (print = bt) [SUB]
  - 318: *XIIᵒ,* (print = bt) [SUB]
  - 318: *Tres* (print = bt) [SUB]
  - 319: *Christi,* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 316:
l. ABCE: Gillianensis ; D: Giibone?isis ; ib. D: cum sic. 3. Codd.:
negant. 10. ABC: utrum eukarisiia; E: si adoracio eukaristie.
12. D: ubi. 21. ABCE: adoranda. 23. C: homo in marg. alia manu.
7. De Johanne presbytero cf. Wyclifs Sermones III, 77.
17. Cf. Flavii Josephi Antiq. Iud. Lib. XI, Cap. VIII, 5.

p. 317:
1. ABC: honoralo ; ib. C: hostie in marg. alia manu. b. adoratur ;
ABDE: adiutrix; C: corrcxit. 9. B: Sed notandum. 14. D: sine
secundum. 21. C: ut Deus alia manu; ih.E; inordinato. 23. E: ava-
ricia. 28. DE: in adorando.

p. 318:
2. ABC: nec de. 5. D : habitacionis. 10. D : Et deest; ib. D : ista sunt.
12. ABC : et deest. i3. ABC : Illa. i5. ABC : apprendere. IQ.E: nimis.
21. C: w^alia manu. 23. E: adorant. *5. D: adorat quantam; ib. ABC:
ipsum. 27. ABCD : quam bestia. 28. ABCE: virgo Dei. 32, 33. C : pax
augeaiur et caritas in hominibus. 33. C: et in marg. alia manu.

p. 319:
I. B: Christi deest. 2. B: participes ; E: participe ; ib. ABC: Do-
minum. 3. AB : opposita dcest; C: in marg. alia manu add. 7. E: eum.
12. ABCE: extinguit. 14. AB: magis deest: C: in marg. alia manu.
16. B: pertam. 20. D : caufugi. 21. 22. ABC: inclinacionem, genit-
fLexionem vel decapuciacionem et in; E: capuciacionum. 23. ABC: con-
versacionem. 25. E: dicunl. 3o. Codd.: regis.

p. 320:
4. vivis; ABCD: wius ; ib. E: adversits pauperum; ib. ABC: provisio.
6. D : gravitate deest. 6, 7. D : et qualitate. 7. D : de quo. 10. Wil-
helmus; A in textu: voluis ; in marg. alia manu: Wilhel. i3. C: et in
marg. alia manu. 22. D: ad eum. 24. D: prolem delicto. 25. C: pre-
latorum iu marg. alia manu. 26. D: evidenter. 27. AB : illum.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 316: velato capite, | et eciam.
p. 317: avarus est ydolorum servitus.
p. 318: tanquam gentes ad simulacra muta prout ducebantur captivi euntes
p. 319: Unus panis et unum corpus multi sumus.
```
