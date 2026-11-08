# Translation brief: eucharistia 07-d–07-f

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/eucharistia/wyc-eucharistia-07-d.md chunks/eucharistia/wyc-eucharistia-07-e.md chunks/eucharistia/wyc-eucharistia-07-f.md` once and fix what it reports.
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

## Glossary (the 509 rows these chunks use; the full file is GLOSSARY.md)

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
| viator | wayfarer | One still on the road, not yet in the homeland. Loserth: "a traveller on earth". Pilot. |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| sacramentum (the eucharist); sacramentum altaris | sacrament; the sacrament of the altar | The plain sense, against the Augustinian row (*Incarn.*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.3, 3.30). |
| hostia; hostia consecrata | host; consecrated host | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.11, 1.22). |
| panis / vinum | bread / wine | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.8). |
| corpus Christi / corpus Domini | the body of Christ / the body of the Lord | Kept apart as the Latin alternates them. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.6, 1.10). |
| cultores accidencium / signorum | worshippers of accidents / of signs | Wyclif's name for the defenders of the accident without a subject. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 6.15, prol-c 10.2). |
| claritas (of the glorified body) | clarity | The dowry of the glorified body (with agility, subtlety, impassibility); not "brightness". Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-c). |
| missantes | mass-priests | Priests hired to say masses; pejorative. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 15.25). |
| species (of bread and wine) | species | The sacramental species; kept as the term, not "appearance". Distinct from the logical *species*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 13.15; 23.8). |
| sacer; sacrare | sacred; hallow | Kept apart from *sanctus / sanctificare* "holy / sanctify" and from *consecrare*; *consecrare* is "to hallow together" in the grammarians' etymology. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 27–28). |
| sacramentum tantum | a sacrament only | The *sacramentum tantum* of the Lombard's three (IV d. 8 c. 4). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 29.23). |
| decretalis | decretal | Kept apart from *decretum* "decree". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 71.31). |
| principaliter; principalitas (of the body's presence) | principally; principality | Of the body of Christ alone being in the sacrament as its principal; not the compendium's *principaliter* "as a main head". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 75.5–26). |
| transaccidentacio | transaccidentation | Wyclif's coinage beside *transsubstanciacio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 81.27). |
| transinferioracio; transsubieccio | transinferioration; transsubjection | Coinages in the same series. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 82.3). |
| concomitanter | concomitantly | Of the body present with the blood by concomitance; cf. *gracia concomitancie*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 81.23–25). |
| divinitus | divinely | The pair of *humanitus* "humanly". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 84.19). |
| consecracio | consecration | The noun of *consecrare*; see *confeccio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 99–100). |
| concomitancia | concomitance | With *concomitanter*, *gracia concomitancie*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 121.27). |
| transaccidencia | transaccidents | In the *transaccidentacio* series. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 145.4). |
| corpus dominicum | the Lord's body | Kept apart from *corpus Domini* "the body of the Lord" and *corpus Christi*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 158.31, 165.3). |
| in circulo (of the host) | in a round | The round form of the host. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 161.17). |
| nominacio (baptismatis) | naming (of our baptism) | Wyclif's figure for the name the faithful bear. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 172.21). |
| sanctificacio | sanctification | Ruled 2026-11-07 (coordinator, delegated; *Euch.* 189.6). |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| temporalia | temporal goods | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| simonia | simony | Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| pencio annua | yearly pension | Ruled 2026-09-28 (3 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| possessionati | the possessioners | Endowed religious. |
| satrapa | satrap | Derogatory: church-court officials wielding delegated power (T. p. 378 n. 58). Keep the word; note it at first occurrence per work. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | CONTEXTUAL: condition / respect | "Condition": a person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). "Respect": the logical relation under which a predicate holds (*posiciones secundum habitudinem*), with a **C** note; ruled 2026-10-22 (Wilson; *Incarn.* 4.16). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| decretum; decreta | decree; the decrees | Gratian (*in decretis*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.14, 3.24). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| credulitas | credence | With *credere*, believe (*Dial.* 23.17–24.4). Ruled 2026-09-28. |
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
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| glosare | to gloss | Interpret so as to remove the difficulty (T. p. 366). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
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
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| glosa | gloss | The noun beside *glosare*. Ruled 2026-10-02 (52.10). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| impetrare | obtain (by request) | Ruled 2026-10-02. |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |
| humanitas | the humanity | The nature the Word assumed, body and soul; with the article (*humanitas sit Christus*, "the humanity is Christ"). Not "the human nature", which is *natura humana*. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| assumere / assumpcio (*naturam*) | assume / assumption | Of the nature, as in the fathers. ⚠ Kept apart from the logician's *assumptum* "the assumption" (above): C note where the logical sense occurs. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| ydemptitas specifica | identity of species | That Christ and other men are of one species. Not "specific identity" (reads as "particular"). Ruled 2026-10-22 (Wilson; *Incarn.* prol, 8). |
| homo assumptus | the assumed man | A term of art (the Lombard's first opinion, *Sent.* III d. 6); keep "assumed" before "man", never "the man assumed". With the agent expressed (*homo assumptus a Verbo*) "the man assumed by the Word", which cannot be misread (coordinator, 2026-10-22). Ruled 2026-10-22 (Wilson; *Incarn.* 5.15). |
| secundum quod (reduplicative) | insofar as | ⛔ Never "in that" (heard as "because", which inverts the logic). Ruled 2026-10-22 (Wilson; *Incarn.* 5.29–6.24). |
| secundum deitatem / secundum humanitatem | as to the Godhead / as to the humanity | The rule of reduplication; keep it in Wyclif's place in the sentence. ⛔ Never supply "as God / as man" where the Latin has bare apposition (*ipse Deus*) or bare predication. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| natura | nature | Ruled 2026-10-22 (Wilson; *Incarn.* 3.4). |
| persona | person | Ruled 2026-10-22 (Wilson; *Incarn.* 4.14). |
| creatura / creator / creatus | creature / creator / created | ⛔ Never "creation" for the created thing. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| posicio / proposicio / predicacio | position / proposition / predication | Kept apart: the apparatus shows the three trading places (*Incarn.* 4.15). Ruled 2026-10-22 (Wilson). |
| sacramentum (of the incarnation, of creation) | sacrament | The Augustinian sense, "mystery" (1 Tim. 3:16): G note at the first occurrence in the chunk. Kept apart from *misterium*. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.8). |
| misterium | mystery | Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.3). |
| sancti | the saints | The fathers. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.15). |
| probabiles doctores | reputable doctors | *Probabilis*: worthy of credence (cf. *probabiliter*). Ruled 2026-10-22 (Wilson; *Incarn.* 7.1) as "approved doctors"; changed the same day (coordinator) to free "approved" for *approbati*. |
| abstractive | abstractively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 10.6). |
| determinacio | determination | A qualifying addition to a predicate (*cum determinacione*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 14.11). |
| Sermo (beside *Verbum*) | Speech | The divine title, capitalised; *Verbum* stays "the Word". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 16–17). |
| sophistice | sophistically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 15). |
| de vi vocis / de vi sermonis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| determinaciones ecclesie | the church's determinations | Rulings of the church, not the logician's *determinacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 24). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| gracia unionis | the grace of union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| humanitus | humanly | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* passim). |
| suppositum | supposit | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 34.24). |
| individuum | individual | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 35.7). |
| in quantum (reduplicative) | insofar as | As *secundum quod*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37.9). |
| diccio (logical) | word | A single term in a proposition. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 43.3). |
| intransitive | intransitively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 45.28). |
| in effectu | in actual fact | As against in potency or in name; ⛔ not "in effect" (modern "virtually"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 47.10). |
| animare | animate | The argument turns on it (45.30–46.4). Ruled 2026-10-22 (coordinator, delegated). |
| communicacio ydiomatum | communication of idioms | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.1). |
| predicacio actualis / aptitudinalis / habitudinalis / mixtim | actual / aptitudinal / habitudinal / mixed predication | *Habitudinalis* is its own term (the four MSS at 49.6), not under *habitudo*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.5–16). |
| denominativum | denominative | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 50.30). |
| Doctor Subtilis | the Subtle Doctor | Scotus. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.24). |
| forma totalitatis | form of totality | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 50.7). |
| quantus | quantified | The adjective beside *quantitas*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.22). |
| suppositacio | suppositation | Kept apart from *supposicio* "supposition". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.31). |
| carneus / carnalis | fleshy / carnal | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.21). |
| passio (against *accio*) | being-acted-on | The category; G note at the first occurrence in a chunk. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 60.13). |
| supposibilis | that can be supposited | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 64.14). |
| illacio (*mali*) | bringing-on | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 66). |
| per se / per accidens | CONTEXTUAL: of itself / by accident; (spatial) apart, by itself | The spatial sense (a thing set apart, *Euch.* 104.16–17) gets a G note. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a (sufficienti) divisione | the topic from sufficient likeness / from (sufficient) division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| pretericio | being past | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| libere contradictorie | freely, as between contradictories | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 76.15). |
| ydemptitas ypostatica | hypostatic identity | Beside *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 84.20). |
| passionatus | subject to passion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| capitales doctores | the chief doctors | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| intricaciones sophistice | sophistical entanglements | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 82). |
| eiusdem / consimilis / alterius racionis | of the same / like / another kind | The species-sense of *racio*; *racio speciei* "the account of the species" (Aristotle's *logos*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.4, 87.17). |
| principiari | be constituted from principles | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.7). |
| accidentatus | subject to accidents | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.4). |
| in recto / in obliquo | in the direct case / in an oblique case | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.25). |
| passibilis | passible | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.12). |
| signum / signatum | sign / thing signified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 91.2–6). |
| predicacio synecdochica | synecdochic predication | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.27). |
| paranymphus | paranymph | The bridegroom's friend (Gabriel). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 93.3). |
| humidum infantile / radicale | the moisture of infancy / radical moisture | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 94.9). |
| esse intelligibile | intelligible being | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 99.23). |
| ministerialiter | ministerially | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 100.17). |
| res racionis | thing of reason | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| significatum | significate | Kept apart from *signatum* "thing signified". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 111). |
| sermo vocalis | the spoken word | Against *Sermo* "Speech", the divine title. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 113). |
| predicacio secundum essenciam / formalis | predication by essence / formal predication | Wyclif's modes of predication (cf. *predicacio secundum causam*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 115–116). |
| forma substancialis | substantial form | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| exclusiva | the exclusive [proposition] | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 116–117). |
| concepcio (figure) | conception | The grammatical figure. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habitus (of the humanity) | habit | The Lombard's third opinion (*Sent.* III d. 6). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| accidens | accident | The category; *accidit* "befalls". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habitacio | habitation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 120.14). |
| denominacio respectiva | relational naming | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 120.17). |
| figura / figuratum | figure / thing figured | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 121.23). |
| humanitacio | humanation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 126.12). |
| racio (individual, personal) | account | *Racio individui / persone* "the account of an individual / a person", as *racio speciei*; not "aspect" (the row against *substancia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 8, 129–132). |
| vir (against *homo*) | man (*vir*) | Where Wyclif sets *vir* against *homo*, the Latin in parentheses. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 129.15–26). |
| exemplaria / exemplata | exemplars / things exemplified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.6). |
| res secunde intencionis | things of second intention | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.25). |
| materia proxima / remota | proximate / remote matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137.1). |
| personari | be made a person | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 134.10). |
| colorate | with colour enough | With a plausible ground (cf. *color*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 134.26). |
| ydemptificare / ydemptificacio | identify / identification | Make the same (*idem*); the hypostatic union as identification, not conversion or generation. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 142.19, 147.22). |
| res communis / res communes | the common thing / common things | The realist universal the *moderni* do not conceive (first root of their error). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 144.27). |
| distinccio racionis | distinction of reason | Beside *differencia formalis*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 145.23). |
| principiare (active) | be the principle of | Beside the passive *principiari* "be constituted from principles". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 147.4). |
| assumere personale | personal assuming | The infinitive used as a noun; kept apart from *assumpcio personalis* "personal assumption". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 146.33). |
| supposicio simplex / supposicio personalis | simple supposition / personal supposition | Supposition theory. *Simpliciter / personaliter supponere* "stand with simple / personal supposition": NOT the *simpliciter / secundum quid* pair, C note where the two could be confused. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 152.5–12). |
| concretum / abstractum | concrete [term] / abstract [term] | *Homo* the concrete, *humanitas* the abstract. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 152). |
| transsumpcio | transumption | Beside *transsumptive*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 153.28). |
| personalitas | personality | The scholastic term: what makes a person a person, not character. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 155). |
| nativitas | nativity | Christ's twofold birth. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 155). |
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
| causancia / causacio | causing / causation | Kept apart (both at 187.30–34). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 185.16). |
| personare (active) / personacio | make a person / personation | Beside the passive *personari* "be made a person". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 188.16, 188.32). |
| perfeccio simpliciter | perfection without qualification | After *simpliciter* "without qualification". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.1). |
| transsubstanciacio | transubstantiation | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.10). |
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
| superioritas / inferioritas terminorum | superiority / inferiority of terms | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 215). |
| exponentes | the exponents | The propositions into which a proposition is resolved (expounded). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 216.14). |
| homo communis | the common man | The universal man, with *res communis*; not "the ordinary man". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 218.3). |
| signum reduplicatum | the reduplicated sign | The reduplicative word (*secundum quod*, *in quantum*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 230.23). |
| supposicio | supposition | Of a term (supposition theory) or of a premiss laid down (cf. *supponitur* "it is supposed"); the English word serves both, C note where it matters. Kept apart from *suppositacio* "suppositation". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 102.8). |
| lex proximitatis | the law of neighbourhood | The duty to love one's neighbour (*proximus*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 101.29). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |
| sacramentaliter | sacramentally | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
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
| substancia | substance | Beside *substancia prima / secunda*. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 3.14). |
| quantitas / qualitas | quantity / quality | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.7–8). |
| esse; esse sacramentale | being; sacramental being | The bare *esse* of the modes of being. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 3.28, 3.30). |
| Doctor Communis | the Common Doctor | Thomas; with *Doctor Subtilis*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 8.16). |
| multitudo (of one body) | multitude | Of one body's being many (ch. 8); the plain "multitude" of persons needs no row. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 8.4). |
| sensus communis | the common sense | The inner faculty; kept apart from *sensibile commune* "common sensible". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 18.31). |
| laudative; effective | by way of praise; by way of effect | Of blessing God vs. blessing a thing. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 16.24). |
| sensacio | sensation | One of the five. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 20.18). |
| figurare | figure | Both senses: to prefigure (the lamb figured Christ) and to shape (*figurare Deum nostrum*), which Wyclif plays on; one English word keeps the pun. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-c 10; 21.29). |
| supponere pro | stand for | Supposition; with *supposicio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 24.27). |
| sensualiter | sensually | Berengar's oath word (*Ego Berengarius*); kept apart from *sensibiliter* "perceptibly". A mode adverb, one word. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 26.1, 30.24). |
| sentire (an opinion: sensit quod) | hold | Of a doctor's or church's opinion; the "perceive" row is the sacrament sensed. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 30.30, 31.18). |
| predicacio figurativa | figurative predication | A synonym of *predicacio tropica*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 35.18). |
| loyca (of speaking about the sacrament) | logic | The manner of speaking, as against the teaching (*sentencia*); the argument of ch. 2 turns on it. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 38.28, 47). |
| describere | define | The verb of *descripcio* "definition". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 48.9). |
| expositorie (of preaching scripture) | by way of exposition | Not the logicians' *expositorie* "expositorily" of the expository syllogism. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 46.4). |
| aliquitas | somethingness | Being a something (*aliquid*). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 60.27). |
| cedere (in) | give way (into) | Of the bread passing into the body. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 58.3, 60.9). |
| informacio; informare | informing; inform | Of a form in its subject; not "information". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 64.13). |
| linire; linitus | smear (on); smeared | The modern doctors' accidents "smeared on" the quantity. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 64.12, 64.29). |
| accidens predicamentale | accident of the categories | Kept apart from the predicable *accidens*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 64.1). |
| pedalitas | foot-length | *pedalis* "foot-long". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 66.27). |
| veritas predicamentalis | truth of the categories | As *accidens predicamentale* "accident of the categories". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 69.2). |
| armatura | armament | Both weapon and armour. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 78.6). |
| extense loquendo | speaking in an extended sense | Cf. *large / stricte loquendo*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 82.15). |
| esse situale / intencionale / potenciale | situal / intentional / potential being | The modes of the body's being. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 84.8 ff.). |
| sensus (of words) | meaning | Kept apart from *sentencia (verborum)* "sense" (Wilson's row). The bodily *sensus* and *sensus literalis / misticus* stay "sense". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 89.22, 04-c, 04-d). |
| interpolatus; interpolacio | interrupted; interruption | Of words spoken with pauses. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 89.4, 89.18). |
| quintimembris | fivefold | Cf. *trimembris*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 91.11). |
| organisare | form (sounds) with the organs | Of speech. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 92.9). |
| insensibiliter | imperceptibly | Beside *insensibilis*; the opposite of *sensibiliter* "perceptibly". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-e). |
| pertinenter | fittingly | Kept apart from *convenienter*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-e, 04-f). |
| essencialiter | essentially | A mode adverb, one word. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-g). |
| noticia confusa / distincta | indistinct / distinct knowledge | As *confuse / confusus* "indistinct(ly)". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-g). |
| ponderositas; ponderosum | heaviness; heavy | The abstract against the concrete: *hostia est ponderositas sed non est ponderosum*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-a p. 10, 110.24). |
| relacio ydemptitatis | relation of identity | The grammatical relative of identity. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 116.6). |
| questio si est / quid est | the question whether it is / what it is | *Post. An.* II.1. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 119.18). |
| bonificacio | bettering | Of the bread made better, not destroyed. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 129.14). |
| figuracio | figuration | Beside *figura / figurare*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 131.16). |
| neutraliter; adiective | as a neuter [noun]; as an adjective | The grammar of *accidens*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.7). |
| naturalitas obediencialis | obediential naturalness | Cf. *dependencia obediencialis*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.15–18). |
| actuacio | actuation | Of a form actuating matter. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.25). |
| accidentalitas | accidentality | Beside *substancialitas*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.13). |
| quantitas successiva | successive quantity | Time and motion, against permanent quantity. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.1). |
| corpus mathematicum | mathematical body | The three dimensions without matter. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 142.31). |
| fantasiare | fancy | The verb beside *fantasia* "imagination". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 143.16). |
| ubi; ubicans | where; that which gives a where | The category of place and its cause. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 146.23–24). |
| localiter | locally | A mode adverb, one word; beside *dimensionaliter*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 148.29). |
| fasciculus accidentis | bundle of accident | Wyclif's mockery of the accident without subject. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 154.12). |
| pertinencior | more fitting | The comparative of *pertinens*; cf. *pertinenter*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 153.8). |
| signum nature | instant of nature | The scholastic priority without time; kept apart from *signa* "signs". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 161.9). |
| generancia | begetting | Ruled 2026-11-07 (coordinator, delegated; *Euch.* 161.25). |
| ponderacio | weighing | Beside *ponderositas* "heaviness". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 183.17). |
| ydemptifice | by identification | Kept apart from *ydemptice* "identically" (a mode adverb). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 190.3). |
| qualitas prima | first quality | Hot, cold, wet, dry. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 197.24). |
| subiectare | be the subject of | Of a substance underlying accidents. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 199.10). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| insensibilis | imperceptible; of a thing that cannot feel, without sensation | Two senses by referent: what cannot be perceived / what cannot perceive (*lapis insensibilis*, *Dial.* 56.3). Kept visibly paired with *sensibilis*. Ruled 2026-09-28 (3 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| magisterium | rule; of teaching, the teaching office; *quale magisterium* "what a feat of mastery" (*Incarn.* 137.14) | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ydiota | unlettered man | Never "idiot". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| ablatarius | the one from whom it is taken | Beside *ablacio* "taking-away". Ruled 2026-10-02 (*Eccl.* 15, 343.7). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| denominacio; denominare | naming; to name | The argument turns on it. Ruled 2026-10-02 (*Eccl.* 17, 391.17, 398.2). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| quadriga diaboli | the devil's four-horse chariot | Ruled 2026-10-02 (*Eccl.* 18, 427.12). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
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
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
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
| premium accidentale | accidental reward | Ruled 2026-10-02 (*Eccl.* 23, 565.6). |
| casus calculatorii | calculatory cases | Ruled 2026-10-02 (*Eccl.* 23, 574.32). |
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
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| deliramenta | ravings | Ruled 2026-10-07 (*Pot. pape* 06-c). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| relacio racionis | relation of reason | Scholastic term (a relation in the mind only). Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 3.7). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| fantasia | imagination | The faculty (scholastic *phantasia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 147.11). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| quaternarius / denarius / quadragenarius | the four / the ten / the forty | Number exegesis (the 153 fishes, ch. 7). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 154–155). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| infundabilis; infundabiliter | without foundation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 195–196). |
| fantasticus | imaginary | Cf. *fantasia* "imagination". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 203.4). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| memorativa potencia | memorative power | A faculty of the soul (the "power" sense of *potencia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 219.27). |
| primicia (virtutum) | being first (in the virtues) | Kept apart from *primatus* "primacy" and *primitas* "firstness". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 228.33). |
| replicatur; replicatum | it is rejoined; rejoinder | A further objection against an answer; kept apart from *respondetur* "the reply is" (so 04-b). Ruled 2026-10-08 (coordinator, delegated; conformed 10-e, 10-g). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| neutra | neutral things | Things neither commanded nor forbidden (obedience *in neutris*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.19). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| eleccio passiva / activa | passive / active election | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 254.31). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| imperium (vicarium, autoritativum) | command (vicarial, authoritative) | The power to command (*par in parem non habet imperium*); "empire" only of the Empire. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 263.2). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| precellencia | pre-excellence | Kept apart from *preeminencia* "preeminence". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 274.33). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| bonificare | make good | Ruled 2026-10-02 (*Eccl.* 23). |
| precellenter | pre-excellently | Adverb beside *precellencia* "pre-excellence". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 291.2). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| episcopi cesarei | caesarean bishops | Extends *prelatus / sacerdos cesarius*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 331.24). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| spissius (vivere) | more closely | Of living to a rule. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 338.13). |
| evangelizans | preacher of the gospel | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-g). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |
| coloracior | more colourable | Comparative, with the *color* / *colorabilis* rows. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 384.15). |
| diccio procuratoria | proctorial pronouncement | C note gives *dicio* "authority" as the alternative. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 386). |
| specularis prudencia | the prudence of a watchman | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| ars cesarea | the caesarean art | After *papa cesareus*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| precellere | excel | Verb beside *precellencia* "pre-excellence"; not "pre-excel". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 399.28). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |
| sentire (the sacrament, the body) | perceive | "sense". As *sensibilis* "perceptible". Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.10, 1.17). |
| fingere (a miracle) | feign | "imagine". Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.11, 1.14). |
| pius pater | loving father | *pius* of a father: not "pious". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 42.27). |
| ex tibi dubio; ex sibi dubio | for all you know; for all he knows | Idiom: not "from doubt". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 66.15, 70.25). |
| cordatus | stout-hearted | Not "wise" (C note where it leans). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 180.6). |
| pertinaciter | pertinaciously | Keeps "obstinate" for *protervus*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 180.29). |
| exsufflare | blow out | The exorcism gesture. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 189.25). |

---

## Chunk 07-d: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-07-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-07-d
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "200.1–204.32"
divisions: "cap. 7 (heading 'CAPITULUM SEPTIMUM.' at 189.0); part 4 of 11, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "1072 words; 1056 confirmed by the vote; 14 runs stood by rule; 2 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n271–n275 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 7, part 4: [TITLE]

## ¶1 · 200.1–202.8

> [p. 200] Sed limitatum est nobis pro fugandis heresibus quod loquamur de predicacione ydemptica, et illam oportet scire distinguere a predicacione tropica ad intelligendum sanctos. Scribit enim Jeronimus in epistola ad Helbidiam De XII Questionibus questione IIᵃ: Nos, inquit, audiamus panem quem fregit Dominus deditque discipulis suis esse corpus Domini salvatoris, ipso dicente ad eos: Accipite et comedite; hoc est corpus meum. Ecce quod iste sanctus cui mille doctores et pape non equiparantur in fide scripture asserit quod panis demonstratur pronomine, et usque hodie omnes eciam infideles satrape non audebant hereticare huius sancti sentenciam. Unde Augustinus exponit eam expressius epistola XII ad Bonifacium episcopum: Si, inquit sacramenta quandam similitudinem rerum earum quarum sacramenta sunt non haberent, omnino sacramenta non essent. Ex hac autem similitudine plerumque eciam ipsarum rerum nomina accipiunt; sicut ergo secundum quendam modum sacramentum corporis Christi corpus Christi est, sacramentum sanguinis Christi sanguis Christi est, ita et sacramentum fidei fides est. Ideo docet Augustinus Sermone LV° quomodo non debemus contemptibiliter vel irracionabiliter accipere sacramentum propter suum signatum: Non tibi videatur vile, inquit, quod vides; quod vides transit, sed quod signatur in ipso visibili non transit sed permanet; ecce signum accipitur, comeditur, consumitur: numquid [p. 201] corpus Christi consumitur? Absit. Distinguunt enim sancti inter hoc signum et corpus Christi ut inter Deum et creaturam signantem, nec umquam sciverunt concipere quod qualitas sit sine subiecto, ita quod omnes vires anime plene virtute, beatitudine et gracia sint per se in patria adorande tanquam considerantes et compacientes de nostra miseria si tamen per se forent, pocius hoc facerent qualitates: fides, spes, karitas, felicitas, virgines quas oramus, quia de sua natura haberent perfecciones, quas per accidens accomodant sanctis quasi fines suarum perfeccionum, quas in se habent perfeccius, cum nichil accomodat alteri perfeccionem ulteriorem quam ex se habeat; virtus autem talis cum sit intuitiva, abstractiva et quomodocunque natura humana est secundum animam operativa, foret valde perfecta ex illa operacione sibi propria et advocatrix valde compaciens et miseri iuvativa. Nec dicetur racio quare qualitates corporee possunt per se habere omnem accionem quam possunt habere in corpore quin a pari vel evidencius qualitates anime ita possunt; nec est facile fingere quomodo possunt communicare acciones suas corporibus quibus per accidens sunt linite, quin evidencius Deus posset communicare potenciam creandi et omnem accionem suam ad intra cuilibet creature; et ita sicut ille qualitates anime insensibiles communicant corpori denominaciones quas per se sibi retinent, ita possent de Dei omnipotencia communicare ligno vel lapidi, et sic omnis materialis substancia foret de Dei omnipotencia intellectiva subtilissime et beatificabilis de obedienciali potencia. Ille enim qui potest [p. 202] suspendere informacionem qua qualitas spiritualis informat corpus et alias facere quod informet eciam efficacius corpus ex natura sua minus dispositum, ipse posset extendere potenciam informativam virtutis et potenciam passivam subiecti; et sic quelibet materialis substancia foret de Dei potencia quomodocunque activa et per consequens nulla foret substancialis differencia.

[ENGLISH]

## ¶2 · 202.9–202.19

> [p. 202] Sed deliramenta sunt ista, cum nulla qualitas sit nisi substanciam esse qualem, nec aliqua forma est nisi illa que est substanciam esse formatam vel formosam; ideo idem est ponere quod qualitas sit per se sine substancia et ponere quod sit ista quod substancia sit qualis sine hoc quod sit substancia; et sic includit formalem contradiccionem quod sit accidens sine substancia subiecta, in tantum quod forma substancialis qua corpus hominis est formaliter vivum est vita que est accidentalis tam corpori quam illi spiritui. Et illi uniuntur in eadem persona hominis, ut hic supponitur.

[ENGLISH]

## ¶3 · 202.21–202.28

> [p. 202] Quantum ad triplicem evidenciam tactam in principio argumenti patet quod decretum loquitur tropice quod panis sacramentaliter fiat corpus Christi et non ydemptice quod natura panis sit natura corporis Christi, et sic licet albedo sit sacramentum, non tamen est per se sacramentum, sed sacramento illi inherens; et illud subiectum est infinitum perfeccius quam quantitas vel albedo.

[ENGLISH]

## ¶4 · 202.29–202.30

> [p. 202] Quantum ad secundum argumentum patet quod illud sacramentum est album quia natura panis.

[ENGLISH]

## ¶5 · 202.31–203.17

> [p. 202] Ulterius pro denominacione accidentis notandum quod triplex est denominacio, scilicet subiectiva, [p. 203] respectiva et intrinseca. Prima denominacione sola substancia denominatur, cum omne accidens sit substanciam esse accidentatam, ita quod nichil est subiectum accidentis nisi substancia; accidens autem est fundamentum et causa alteri sed non subiectum. Denominacio autem respectiva non exigit denominatum illud esse subiectum accidentis denominantis, quod satis est quod sit fundamentum ad quod accidens absolutum respiciat, causando in ipso habitudinem respectivam, ut patet de septem respectibus fundatis in quantitate et qualitate. Et isto modo dicunt Augustinus V De Trinitate in fine et Anshelmus in Monologion XXVII quod Deus est fundamentum habitudinis relative, que quia non requirit fundamentum suum per eius acquisicionem moveri, vocatur ab aliquibus relacio racionis. Non enim requirit in illius subiecto fundamentum esse accidens absolutum.

[ENGLISH]

## ¶6 · 203.18–204.8

> [p. 203] Tercia autem denominacio intrinseca est qua idem denominat se per se, quod potest esse multipliciter; nam Deus per se excludendo omnem aliam causam denominat se sapientem, iustum, potentem etc.: ideo ista non sunt in Deo accidencia. Quantitas eciam dicitur per se quanta, licet equivoce a substancia; sic eciam albedo alba et ita de aliis accidentibus eciam respectivis. Aliter enim foret processus in infinitum, ut qualitas foret distincta intensione intensa, et sic in infinitum, nisi foret dare unum per se intensum. Non tamen video quod quantitas denominatur subiective albedine vel econtra, sed sicut superficies est alba vel albata, ut locuntur philosophi, ita qualitas [p. 204] est mole magna, ita quod neutrum istorum accidencium est subiectum alterius, sed denominant se reciproce respective, quia unum concomitatur reliquum in eodem subiecto, ut quia albedo est per partem substancie superficialem aut tenuem; ideo dicitur albedo superficialis, et quia qualitas est per pedalem quantitatem subiecti, ideo dicitur pedalis, sic quod nec quantitas subiectat qualitatem nec econtra.

[ENGLISH]

## ¶7 · 204.9–204.12

> [p. 204] Sed qualitas multiplicius denominatur intensa, activa, quanta etc., quam denominatur ipsa quantitas, licet sit secundum speciem et non individuum fundamentum et basis in subiecto qualitati corporee.

[ENGLISH]

## ¶8 · 204.13–204.32

> [p. 204] Sacramentum autem est per se subiectum tam quantitati quam qualitati, cum adversarii concedunt quod accidente albi vini infuso in accidens rubei vini consecrati utraque quantitas et qualitas movetur, cum sacramentum erit maius et alterum; ideo necesse est ponere ibi subiectum prius quantitate et qualitate, quia certum est quod fasciculus accidencium est posterius utroque; et patet in parte quomodo accidencia in denominacione sese respiciunt. Et per hec patet responsio ad tercium argumentum. Nam qualitates secunde denominant qualitates primas, materiam et formam, eciam Deum denominacione respectiva. Sed denominacione subiectiva solum denominant materialem substanciam per quam extenduntur. Denominacionem autem respectivam facit accidens in quantumcunque distante in quo non est subiective, ut albedo Petri Rome facit ipsum esse similem Johanni Anglie, ideo causat ad omnem punctum propinquitatem atque distanciam et quodammodo facit quod Deus est causa eius.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 200.1: -We must distinguish between identical and tropical statements.
- 201.1: If qualities could exist separately, we ought to pray to the virtues rather than to the Saints.
- 201.27: Intelligence might house itself in a log of wood.
- 202.9: This is mere madness: neither quality nor form can exist without substance.
- 203.1: Three kinds of naming: 1. Subjective, which applies only to substance.
- 203.7: 2. Respective, which does no require the thing named to be the subject of the accident.
- 203.18: 3. Intrinsic, which applies in many ways.
- 204.13: The sacrament a subject for both quality and quantity.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 200: *fregit* (print = bt) [SUB]
  - 202: *natura* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 200:
5. A: Albidiam; in marg. alia manu: Helbidiam; B : Albidiam alias
Helbidiam. 7. ABDE : snis deest. 9. D : meum deest; ib. E : quod deest.
12. D: et infideles. i3. D: istius sancti. 14. D: in epistola. 22. E:
Christi deest. 24. D: irregulariter. 26—28. ABC: transit — comeditur
deest; C in marg. alia manu addit. 27. Recte: significatur.
6. S. Hieronymi, Ep. ad. Hedibiam vol. I, 824. Cf.Trialog. 200,
Serm. II, ^53; III, 278. i5. S. Augustini Ep. ad Bonifacium
XCVIII. Opp. II, 267. 23. Non Sermone LV, sed LXXXIII
De Diversis; Nov.: Serm. CCXXVII. In die Paschae IV, Opp.V, 973.

p. 201:
1. C: Distinguebant. 4. B : qnantitas. 5, 6. ABCE: et beatitndine.
7, 8. C: nisi tamen; correxit in marg. alia manu. 8. D: pro se;
ih. ABC : facerent qualitas; DE: quain fides. 10 D: profecciones.
12. AB : habet. i3. D : utiliorem. 16. D : operativam. 18. E : qualiter.
19. E : operacionem sive accionem. 21. ABCE : ista possunt. 24. AB : Deus
deest; C in marg. alia manu addit; ib. B: credandi. 28. D: posset.

p. 202:
1. B: specialis. 3. ABC: corpus deest. 10. D: alia. 12, i3. D :
qualitas — quod deest. i3. C: ista — sit deest; ib. qualis; C in marg.
alia manu : qualitas. i5. B : substancia twice ; sutiecta deest. 16. D : et
tantum. 19. C: persona huius ; in marg. correxit. 23. ABCD: figurat.
23—2?. C: et sic — Cliristi deest. 24. A: quod natura in marg. alia
manu. 27. D: in infinitum; est deest.

p. 203:
3. D: coaccidentatam. 5. C: causa est. S. quod; C in marg. alia
manu addit. : accidens respectivum respiciat accidens absolutum. 10. E:
septem deest. i3. ABC: Deus deest; C in marg. alia manu addit.
16. D: in illo. 17. C: esse deest; ib. D: aklatum. 19. C: per se
deest. 22. E: eciam deest. 24. D: ita deest. 26. C: quantitas.
27. C: unum deest. 28. E: videtur ; in marg. correxit.
12. S. Augustini DeTrinitate, lib.V, cap. XVI, Opp. VUI, 8^3;
ib. S. Anselmi Opp. (ed. Maur.), pag. 14. Monologium, cap. XXVIII.

p. 204:
1. D: illa; ib. C: neutrorum. 3. ABCD : quod wium; ib. D: reliqua.
8. ABC: nec deest; ib. C : non subiectat ; non alia manu. 12. AB: quan-
titati; C: correxit. i5. B: infusio. 18. ABC: et qualitate deest.
23. ABC: denominat. 24. AC : eciam nedum; C in marg. correxit : Deum ;
ib. B: subiectiva. 25. A: subiectiva in marg. alia manu. 28. in quo ;
B: iniquo; ib. ABCD : est deest. 3o. D: ymmo causat.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 200: audiamus panem quem fregit Dominus deditque discipulis suis esse corpus Domini salvatoris, ipso dicente ad eos: Accipite et comedite; hoc est corpus meum. | sdcramenta quan- | dam similitudinem rerum earum quarum sacramenta sunt non haberent, omnino sacramenta non essent. Ex hac autem similitudine plerumque eciam ipsarum rerum nomina accipiunt; sicut ergo secundum quendam modum sacramentum corporis Christi corpus | Christi est, sacramentum sanguinis Christi sanguis Christi est, ita et sacramentum Jidei fides est. | Non tibi videatur ih vile, | quod vides; quod vides transit, sed quod signatur in ipso visibili non transit sed permanet; ecce signum accipitur, comediiur, consumitur: num-
p. 201: qiud corpus Christi consumitur? Absit.
```

---

## Chunk 07-e: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-07-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-07-e
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "205.1–209.23"
divisions: "cap. 7 (heading 'CAPITULUM SEPTIMUM.' at 189.0); part 5 of 11, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "1050 words; 1025 confirmed by the vote; 18 runs stood by rule; 7 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n276–n280 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 7, part 5: [TITLE]

## ¶1 · 205.1–205.5

> [p. 205] Ideo oportet primo sopire istam stulticiam qua creditur quod omne ens in quantum adquirit sibi accidens movetur. Oportet enim omnem motum subiectari in substancia mota per acquisicionem vel deperdicionem false quantitatis aut qualitatis.

[ENGLISH]

## ¶2 · 205.6–205.10

> [p. 205] Secundo oportet distinguere inter denominaciones respectivas et subiectivas, inter denominacionem efficientem et formalem ut albedinem que denominat formaliter Petrum album denominat efficienter Paulum quantumcunque distantem esse Petro similem.

[ENGLISH]

## ¶3 · 205.11–205.20

> [p. 205] Et tercio oportet notare divisiones et descripciones predictas ad tollendum sophismata et errores. Ad tantum enim desipiunt quidam magni, quod credunt accidens denominare subiectum quantumcunque extrinsecum sine aliqua denominacione accidentis eciam respectivi in illo sic denominato, ut exemplificat de visione, de tempore, de motu. Sed illi parum ponderant visionem passivam que est videri predicamentum ubi et quando causatum a tempore cum denominacione formali et effectuali.

[ENGLISH]

## ¶4 · 205.21–206.2

> [p. 205] Sed redeundo replicatur (ut tactum est) quod homo videndo quodcunque videt Deum oculo corporali, quia omne sensibile vel insensibile ipsum significat. Et confirmatur ex testimonio scripture multiplicis, nam Genes. XXXII, 30 dicitur quod Jacob vidit Dominum facie ad faciem; et Ysaie VI, 1 dicit quod vidit Dominum sedentem super solium excelsum et elevatum. Et Joh. VIIIᵛᵒ, 56 dicit Christus quod Abraham pater Iudeorum exultavit, ut videret diem Messie, vidit et gavisus est; et sic de multis similibus. Si ergo homo, potest tractare et tangere corpus Christi in hostia, [p. 206] multo magis videre potes ipsum ibidem, cum visus sit sensus subtilissimus et supremus.

[ENGLISH]

## ¶5 · 206.3–207.10

> [p. 206] Hic oportet cognoscere equivocaciones pro veritatis scripture misteriis cognoscendis. Est enim visio corporalis, visio ymaginaria et visio intellectualis. Visio corporalis est qua vigil sentit visibile secundum figuram forme visibilis in organo sensus visus. Unde ut loquar clarius in ista materia exprimo quod nemo videt ibidem corpus Christi oculo corporali, quod debet fidelibus esse certum. Unde Doctor Sollempnis primo quodlibeto, questione VIᵗᵃ, dubitando si fidelis videt corpus Christi in hostia oculo corporali declarat quod non, eciam quod oculus Christi in hostia non videt se ibidem propter limitacionis carenciam tam in visibili quam in specie visibilis quam in virtute visiva. Et idem dicit lex ecclesie satis sepe, ut III Decretalium, De Celebracione missarum, capitulo Cum Marthe dicitur quod forma visibilis panis et vini est sacramentum sed non res sacramenti; et aliud est quod creditur quam cernitur, quia bene corpus Christi creditur et cernitur eius species que est solummodo sacramentum. Unde mirantur multi qua fronte infundabiliter quis audet dicere quod videt corpus Christi in hostia oculo corporali. Non enim sequitur: Petrus intellectu vel fide videt Deum in hostia per corporalem oculum, quia per eius ministerium, ergo videt Deum ibidem oculo corporali. Sic enim arguunt sophiste quod homo videt per talum, per digitos et [p. 207] cetera organa inpertinencia visui Deum et omne sensibile vel insensibile, quia illa sunt in casu instrumenta movencia, ut mente concipiat noscibile quod absconditum est ab omni materiali veritate; sed vident quod ista est argucia deridenda, cum sic dicto: Petrus videt hoc oculo corporali, notatur quod oculus corporalis informatur virtute visiva apprehendente hoc per eius speciem naturalem, quomodo solum color, lux vel eius subiectum aut horum privacio videtur, sicut patet philosopho noscenti limites visionis.

[ENGLISH]

## ¶6 · 207.11–207.18

> [p. 207] Secunda maneries visionis vocatur visio ymaginaria que est visio qua secundum virtutem ymaginativam est visibile formaliter apprehensum; et differt a visione priori in tribus: Primo in hoc quod omnis visio corporalis sive per rectam intuicionem sive per reflexionem sive per refraccionem fit per limitacionem speciei presentis visibilis in organo sensus visus; non sic autem visio ymaginaria, cum sepe fit in obiecti absencia.

[ENGLISH]

## ¶7 · 207.20–207.28

> [p. 207] Secunda differencia est quod visio corporalis solum inest videnti dum vigilat, sed visio ymaginaria inest tam dormienti quam vigili, nam in sompnis fiunt quecunque sompnia in visione ymaginaria, sicut multe prophecie inperfecte fiunt in vigili per misterium visionis ymaginarie, ut patet in Daniele qui tam vigil quam dormiens vidit visione ymaginaria sompnium Nabuchodonosor et per hoc vidit prophetice ultra regem interpretacionem sompnii, ut patet Daniel. IIᵒ.

[ENGLISH]

## ¶8 · 207.29–208.28

> [p. 207] Tercio differunt in hoc quod visio ymaginaria est tam quoad obiectum quam tempus visione corporali extensior. Nemo enim videt corporaliter nisi colorem aut lucem presentem vel subiectum aut eorum privacionem, [p. 208] sed homo videt ymaginarie illa, que non habent existenciam, ut montem aureum et multa ymaginabilia que nunquam existunt. Sepe eciam videt homo ymaginarie pro dando signo temporis illa que tunc non existunt sed post vel ante; primo modo legitur Act. Xᵒ, 11 12, quomodo Petrus vidit in mentis excessu celum apertum et descendens vas quoddam velud lintheum quatuor iniciis submitti de celo in terram in quo erant omnia quadrupedia et serpencia terre et volatilia celi; que scriptura est verissima ad sensum positum. Secundo modo loquitur scriptura Act. IX, 11 quod Ananias ex mandato Domini alloqueretur Paulum: Vade, inquit, in vicum qui vocatur Rectus et quere in domo Jude Saulum nomine Tharsensem. Ecce enim orat. Et vidit virum Ananiam nomine introeuntem et inponentem sibi manus ut visum recipiat. Ecce quod Paulus vidit ymaginarie futurum factum Ananie, ut videtur probabiliter ex textu. Et ista visione vidit Heliseus Gesi valde distantem localiter, quomodo recepit simoniace a Naaman munera propter graciam spiritualem quam Deus contulit Heliseo (ut patet IVᵒ Reg. Vᵒ). Et ita videtur quod triplex sit visio ymaginaria, sicut triplex est visio corporalis, scilicet visio ymaginabilis non existentis preteriti vel futuri, visio ymaginabilis non existentis sed visui possibilis, et visio cuiuscunque estimabilis sicut apprehensio estimative fantastice vel memorative organice.

[ENGLISH]

## ¶9 · 208.29–209.3

> [p. 208] Sed tercia est visio intellectualis, qua primo intellectu videtur visibile; et est in beatis pura sine visione inferiori corporali vel tardante ymaginaria. In nobis [p. 209] autem sunt iste tres visionum species comitantes, ut simul video hiis tribus virtutibus sacramentum sensibile triplici visione.

[ENGLISH]

## ¶10 · 209.4–209.23

> [p. 209] Est autem triplex visio intellectualis, scilicet intuitiva, abstractiva et enigmatica. Prima visione vident Deum beati in patria, sicut vident angelos et sensibilia, et cum actus specificantur ab obiectis, ponitur quod iste sunt tres species intuicionum, sicut aliter intuetur beatus sensibile et aliter viator. Intuicio autem intellectualis habet hanc racionem quod per se causatur ex capacitate intellectus et presencia rei vise, ut posito visibili cum sua applicacione que exprimitur per presenciam et sufficienti capacitate intellectus consequitur intuicio. Sed sic non est de visione abstractiva, quia ad illam requiritur discursus racionis, sicut philosophi naturaliter noverunt Deum ex effectibus (ut dicit Apostolus Rom. Iᵒ). Et illam dicunt doctores requiri ad actuale meritum viantis, et hanc neminem posse mereri in primo instanti in quo incipit preter Christum. Oportet enim tale meritum procedere a voluntate libere mota per racionem ad meritorie operandum quod requirit tempus in quolibet alio preter Christum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 205.1: 1. Acquiring an accident need not always cause change.
- 205.6: 2. We must distinguish between subjective and respective naming.
- 205.11: 3. We must keep these distinctions in mind to avoid error.
- 205.21: Our adversary's reply: Scripture shews that we see God in the host.
- 206.3: Three kinds of seeing: bodily, imaginative, intellectual.
- 206.11: I. Bodily. We cannot by bodily sight see the body of Christ.
- 206.20: We see the host with the eye; we see God there by faith; it does not follow that we see God with the eye.
- 207.11: 2. Imaginitive. This differs from bodily sight,
- 207.14: a) In applying to absent things;
- 207.20: 6) in acting during sleep;
- 207.29: c) in applying to things that do not exist,
- 208.3: or to things, past or future.
- 208.29: 3. Intellectual vision.
- 209.4: Three kinds of intellectual vision: a) Intuitive, as the blessed see God.
- 209.14: b) Abstractive, the result of reasoning; as the philosophers by nature know God.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 205: *VIIIᵛᵒ,* (print = bt) [SUB]
  - 206: *Est* (print = bt) [SUB]
  - 206: *infundabiliter* (print = bt) [SUB]
  - 207: *IIᵒ.* (print = bt) [SUB]
  - 207: *presentem* (print = bt) [SUB]
  - 207: *subiectum* (print = bt) [SUB]
  - 208: *IVᵒ* (print = bt) [SUB]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 17. Rom. I, i<), 20. (209.33).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 205:
2. ABC: adqtarit deest; C in marg. addit. 4. DE: aut. 5. D: per-
dicionem. S. C: albedinem corrigere vult in : albedo ; ib. AB : qui.
q. E: denominant. 10. ABC: distanter. 11. D: et ideo. i5. D: alia.
16, 17. E: de visione, tempore et motu. iS. D: videre; ib. C: predicatum.
19. D: tantum a iempore. 21. C: respondendo. 23. D: signat.
27. C : super celum.

p. 206:
i. D : videtur ; ib. ibidem; B : Vdem. 4. B: Et enim. 5, 6. C : risio —
corporalis in marg. alia manu. 8. ABCE: loquatur. 9. E: ibi ;
ib. E: in ocitlo. 11, 12. D: fideles vident. 14. B: literacionis ; E: limi-
tacionem; C in marg. alia manu : limacionis. 17. ABDE: De Celebracione
Missarum deest. 19. ABC: et non. 21. D : cuius. 25. D: et fide.
27. C: enim deest. 28. E: per collum per.
10. Doctor Solemnis, i. e. Henricus de Gandano. Cf. Wilhelmum
Widefordum adversus Joh. Wiclephum Anglum in Fasciculo rer.
expet., fol. 97. Cf. De Ecclesia, pag. 317; De Apostasia, pag. jo.
17. Decr. Gregor. lib. III, tit. XLI, cap. VI.

p. 207:
4. C: videt. 5. D: dico. 11. C: Secunda in marg. alia manu.
12. ABE: que secundum. 16. D: sive per refraccionem deest.
17. D: sensibilis. 24. DE: vigile ; ib.D: ministerium. 26. D: viiionem
imaginariam. 27. D: et philosopho vidit; ib. C: ultra in marg. alia manu.
28. D : interpretaciones. 29. C quia visio.

p. 208:
6. BCE: Act. i. 7. B : celum deest. 9. ABC : in qita.
10. B: scripta alia manu. 11. D: positi. 14. C: nomine deest.
17. E: ymaginarie deest. 18, 19. ABC: et illa. 19. E: Eli\eus.
20. D: Anaaman. 22. E: Eli\eo. 23. B: visio — est deest. 25. B: pre-
teriti— exislentis deest. 27. D : sic; ib. B : estimacione. 3i. D : tarditate.

p. 209:
2. D: videre. 7. ABCD : specificatur. 9. B: beatus deest.
10. E : habet — racionem deest. 14. B: sicut. i5. D: sequitur ;
E: extgitur. 24. D : enigmata. 25. E : puro. 32. I) : Sic enim.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 205: vidit Dominum facie ad faciem; | vidit Dominum sedentem super solium excelsum et elevatum. | Abraham pater Iudeorum exultavit, ut videret diem Messie, vidit et Sogavisus est;
p. 206: si fidelis | videt corpus Christi in hostia oculo corporali | no?i, eciam quod oculus Christi in hostia non videt se ibidem propter limitacionis carenciam tam in visibili quam in specie visibilis quam in virtute | Cum Marthe | forma visibilis panis et vini est sacramentum sed non res sacramenti; et aliud est | quod creditur quam cernitur. quia bene corpus | Christi creditur et cernitur eius species que est solum- | modo sacramentum.
p. 208: vidit in mentis excessu celum apertum et descendens vas quoddam velud lintheum quatuor iniciis submitti de celo in terram in quo erant omnia quadrupedia et serpencia terre et volatilia celi; | in vicum qui vocatur Rectus et quere in domo Jude Saulum nomine Tharsensem. Ecce enim orat. Et vidit virum Ananiam | nomine introeuntem et inponentem sibi manus utvisum recipiat.
p. 209: Videmus nunc per speculum in enigmate, tunc autem facie adfaciem.
```

---

## Chunk 07-f: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-07-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-07-f
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "209.24–213.20"
divisions: "cap. 7 (heading 'CAPITULUM SEPTIMUM.' at 189.0); part 6 of 11, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "905 words; 879 confirmed by the vote; 19 runs stood by rule; 7 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n280–n284 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 7, part 6: [TITLE]

## ¶1 · 209.24–210.8

> [p. 209] Tercia autem visio intellectualis est enigmatica, que est de pure credito infusa obscura noticia, modo quo loquitur Apostolus I. Cor. XIIIᵒ, 12: Videmus nunc per speculum in enigmate, tunc autem facie ad faciem. Et noticiam istius modi habent tam boni quam mali in quolibet inicio noticie rei insensibilis, sic quod quandoque simul currunt iste tres noticie. Et communiter precedit visio enigmatica, cum oportet nos procedere ab imperfecto ad perfectum. Sic ergo novem modis satis equivoce sumitur visio in scriptura. [p. 210] Quandoque autem sumitur visio aggregative pro multis visionibus; unde in Deo distinguitur visio intuicionis qua Deus videt existencia presencia, preterita et futura. Omnia enim illa intuetur, cum existunt sibi presencia, sed possibilia que non existunt videt Deus noticia simplicis apprehensionis. Unde quamvis oporteat illa esse, non tamen oportet illa existere (sicut patet alibi diffuse).

[ENGLISH]

## ¶2 · 210.9–210.17

> [p. 210] Et per istam distinccionem potest intelligi scriptura que videtur contradicere sibi ipsi. Nam Exodi XXXIIIᵒ, 20 capitulo dicit Deus: Non me videbit homo et vivet, hoc est, non tunc vivet vitam naturalem, dum deitatem fuerit intuitus, ut fuit de Moyse et Paulo in raptibus, et ut evenit de beatis; vivunt enim tunc aliam vitam spiritualem mortificati mundo. Et hec est racio quare debemus mundum relinquere et non implicare nos terrestribus sed spiritualibus inhiare.

[ENGLISH]

## ¶3 · 210.18–211.20

> [p. 210] Et sic intelligitur illud Johannis Iᵒ, 18: Deum nemo vidit unquam. Et illud Apostoli I. Cor. IIᵒ, 9: Nec oculus vidit nec auris audivit nec in cor hominis ascendit cum eis similibus. Notandum tamen quod tales negative quandoque excedunt claram intuicionem divine essencie et quandoque equalitatem visibilitatis divine. Quamvis enim beati clare videbunt divinam essenciam, non tamen secundum ultimum sue visibilitatis, cum hoc soli Deo sit proprium. Necesse itaque est tales distincciones cognoscere, nam propter talem ignoranciam et alias malicias dicitur Manassen regem Juda impetere Isaiam super heretica pravitate et ipsum usque ad mortem serrare. Dicit enim (ut supra [p. 211] exposui): Vidi dominum sedentem super solium excelsum. Et Deus dicit Moysi: Non videbit me homo et vivet. Sed concordantur per hoc quod propheta vidit Dominum visione abstractiva cum visione alia quam habuit de ymagine vel figura; per hoc enim quod Ysaias vidit talem ymaginem oculo corporali et visio deitatis fuit sibi infusa cum visione abstractiva quam Deo movente elicuit, Deum super alios intellexit, et sic generaliter in lege veteri, quando dicitur quod videt vel audit Dominum, intelligitur de sensacione in signo cum noticia abstractiva divine essencie, non quod tunc intuitus est Deum, ut sepe declarat Augustinus et specialiter in libro Sermonum Sermone primo: Apparere, inquit, per substanciam suam, sicuti est, nonnisi mundis cordibus dignatur, ut dicit evangelium; oculis autem corporalibus sanctorum. Si quando Deus voluit apparere, non per se ipsum, sed per creaturam sensibilem, quantum ista carne sentiri potest apparuit. Et post diffuse declarat istam sentenciam.

[ENGLISH]

## ¶4 · 211.21–212.6

> [p. 211] Et patet quod sicut nemo sufficit Deum videre oculo corporali, sic nec corpus Christi in hostia consecrata, quia si sufficeret videre sic illud corpus ibi, sufficeret videre sic illud corpus esse ibi, et discernere cuiusmodi est ibi, quod est contra experienciam et determinacionem Urbani quinti cum suis cardinalibus. Videt, inquam, fide et intellectu corpus Christi in hostia consecrata, et sic per istam distinccionem de visione intelligende sunt alie scripture ut Math. Vᵗᵒ, 8, ubi promittitur pro finali premio beati mundo corde quoniam ipsi Deum videbunt. [p. 212] Ibi patet quod loquitur de intuicione in patria. Sed Joh. XIVᵒ, 9 dicit: Philippe, qui videt me, videt et patrem meum; ubi videtur loqui de visione abstractiva et visione infusa. Qui enim videt Dei filium naturalem sub racione qua talis, videt abstractive Deum patrem; et illa visio Christi pertinet ad fidelem supra bestiam.

[ENGLISH]

## ¶5 · 212.7–212.16

> [p. 212] Sed replicatur contra istud primo per hoc quod oculus corporalis est causa visionis Dei a nobis, ergo nos videmus Deum oculo corporali. Sed sic arguens remittendus est ad grammaticos pro cognoscendo regimine ablativi casus, ut dixi sepius. Illi enim talo et pedibus senciunt et intelligunt quidquid apprehenderint sicut fingunt; ideo oportet volentes loqui in ista materia notare grammaticam, loycam et philosophiam cum distinccione visionis predicta, et aliter sunt a disputacione istius materie exsufflandi.

[ENGLISH]

## ¶6 · 212.17–212.19

> [p. 212] Secundo replicatur per hoc quod iuxta sepe dicta hostia consecrata est corpus Christi, et illa ibi videtur oculo corporali, ergo et corpus Christi.

[ENGLISH]

## ¶7 · 212.20–212.28

> [p. 212] Sed patet quod concedentes recte assumptum sunt sic glosandi: Hostia sacra figurat sacramentaliter corpus Christi; sed supposito quod ecclesia admittat loycam istam ut olim, patet quod propter equivocacionem perit illacio, cum sic arguitur: Hostia figurat corpus Christi et ipsa sentitur ibidem, ergo et corpus Christi. Sic enim argueretur quod deitas sit sensibilis quolibet quinque sensuum quandocunque aliquid sentiretur, omnis namque creatura figurat et dicit deitatem.

[ENGLISH]

## ¶8 · 212.29–213.16

> [p. 212] Tercio replicatur per hoc quod nulla substancia videtur oculo corporali nisi quia suum accidens videtur oculo corporali per se, cum ergo indumentum vel [p. 213] armatura corporis Christi per se videtur in hostia, videtur quod corpus Christi videbitur consequenter. Confirmatur ex predicta sentencia Augustini dicentis quod Deus in ista carne potest sentiri oculis corporalibus, sicut dicimus parietem colorari et videri per spissas picturas parieti collinitas. Istam autem arguciam magnificant ydiote, asserentes quod solum accidens vere sentitur. Sed ignorant philosophiam quomodo nullum accidens potest sentiri nisi in virtute substancie sustentantis, cum nullum accidens sit nisi substanciam accidentari, hoc est, modus accidentalis substancie. Accidens tamen videtur per se et subiectum per accidens; cum ergo nullum accidens corporis Christi in hostia videtur oculo corporali, manifestum est quod ipsum non videtur sic per accidens sed ipsa hostia.

[ENGLISH]

## ¶9 · 213.17–213.20

> [p. 213] Et quantum ad Augustinum, patet quod ipse extendit sensacionem ad omnem noticiam intuitivam, iuxta illud Apostoli Rom. XIᵒ, 34: Quis enim cognovit sensum Domini?

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 209.24: c) Enigmatic, as by faith we see God.
- 209.28: This kind is prior to the others.
- 210.1: God has intuition of all things, past, present and future, but apprehension of possible things that do not exist.
- 210.9: These distinctions explain apparent contradictions in Scripture;
- 210.19: e. g. as to man seeing God.
- 211.21: As no man car see God with the bodily eye, so neither can he see the body of Christ in the host.
- 212.7: Grammatical quibbles.
- 212.29: It is said that no substance is visible except by its accidents,
- 213.1: and that in seeing the accidents of the host we see Christ's body.
- 213.12: But the accidents that we see are not accidents of Christ's body.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 210: *IIᵒ,* (print = bt) [SUB]
  - 211: *Christi* (print = bt) [SUB]
  - 211: *sufficeret* (print = bt) [SUB]
  - 211: *Vᵗᵒ,* (print = bt) [SUB]
  - 212: *corpus* (print = bt) [BT-ONLY]
  - 213: *Christi* (print = bt) [SUB]
  - 213: *XIᵒ,* (print = bt) [SUB]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 17. Rom. I, i<), 20. (209.33).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 209:
2. D: videre. 7. ABCD : specificatur. 9. B: beatus deest.
10. E : habet — racionem deest. 14. B: sicut. i5. D: sequitur ;
E: extgitur. 24. D : enigmata. 25. E : puro. 32. I) : Sic enim.

p. 210:
1. C: Quandocunque ; ib. C: aggregaliva. 5. C: existunt in textu;
sunt in marg. alia manu. 7. C: oporteat. 12. D: vitam animalem ;
ib. B: cum. i3. ABCE: et raptibus. 14. C: eveniet. i5. E: spiri-
tualem deest; ib. D: mortificato ; ib. DE: est deest. 22. E: visionem;
C: visionem in marg. alia manu. 27. C: cognoscere deest; agnoscere
in marg. 3o. D : sarrare.
20. IS. VI, I.

p. 211:
4. A: cum in textu; in marg. alia manu: tamen. 7. ABC: sibi deest.
8. ABC: eliciunt; E: deest. 17. ABCE : Sed quando ; C: Debet quando
voluerit; ib. C: se deest. 19. ABC: sentire. 23. D: sicut. 2 \. E:
ibi — corpus deest. 3o. ABCE: ut deest; ib. ABCD : ubi deest.
2. Exod. XXXIII, 20. 14. Recte XVII De Diversis =
Sermn VI, De eo quod apparuit Dominus, Opp. tom. V, ^4.

p. 212:
2. ABCD: Joh. XIV quando ; ib. ABC: Philippo. 3, 4. B : abstrac-
tiva — visione deest. 4. AB: Quandoenim; Ccorrexit; ib. AC: videret ;
BE : vidit. 12, i3. ABCD : apprehenderunt. i5. D : Enim aliter.
i5, 16. D: de disputacione. 16. E: huius materie. 20. D : assensum.
25, 26. C: et ipsa — Christi in marg. alia manu. 25. C: et before
corpus deest. ?o, 3r. ABC: nisi — corporali deest. 3i. ABCD: rudi-

p. 213:
1. C: per se deest. 9. E: ullum. 12. E: et deest. 14. D: in
eucaristia. i5. AbC: est deest; ib. D: sic videtur ; ib. E: stc deest.
19. AbC: Rom. V: ib. C: enim deest. 22. C: camalibus. 26. D : visio.
28. E: et illo. 3i. Ab: candem corporalem eandem. 3i, 32. E : ymaginem.
3. Gf. S. Augustini Opp. tom. V, 34, 3 1 3 ; VIII, 866 et al.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 209: Videmus nunc per speculum in enigmate, tunc autem facie adfaciem.
p. 210: Non me videbit homo et vivet, | Deum nemo | vidit unquam. | Nec oculus vidit nec auris audivit nec in cor hominis
p. 211: Vidi dominum sedentem super solium excelsum. | Non videbit me homo et vivet. | per substanciam | suam, sicuti est, nonnisi mundis cordibus dignatur, ut dicit evangelium; oculis autem corporalibus sanctorum. Si quando Deus voluit apparere, non per se ipsum, sed per creaturam sensibilem, quantum ista carne sentiri potest apparuit. | beati mundo corde quoniam ipsi Deum videbunt.
p. 212: Philippe, qui videt me, videt et patrem meum;
p. 213: Deus in ista carne potest sentiri oculis cor- | Quis enim cognovit sen- | sum Domini? | apparere oculis corporalibus
```
