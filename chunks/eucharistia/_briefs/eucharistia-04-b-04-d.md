# Translation brief: eucharistia 04-b–04-d

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/eucharistia/wyc-eucharistia-04-b.md chunks/eucharistia/wyc-eucharistia-04-c.md chunks/eucharistia/wyc-eucharistia-04-d.md` once and fix what it reports.
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

## Glossary (the 458 rows these chunks use; the full file is GLOSSARY.md)

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
| viare; vians | to be a wayfarer; [one] on the way | The verb of *viator*; tag `g:viator`. Ruled 2026-09-28 (8 sites). |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |
| sacramentum (the eucharist); sacramentum altaris | sacrament; the sacrament of the altar | The plain sense, against the Augustinian row (*Incarn.*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.3, 3.30). |
| hostia; hostia consecrata | host; consecrated host | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.11, 1.22). |
| panis / vinum | bread / wine | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.8). |
| calix | chalice | The Douay word (1 Cor. 10:16). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.3). |
| corpus Christi / corpus Domini | the body of Christ / the body of the Lord | Kept apart as the Latin alternates them. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.6, 1.10). |
| novella ecclesia / antiqua ecclesia | the newer church / the ancient church | The pair of 3.3; cf. *novelli*. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 3.3). |
| sumpcio | reception | Of the sacrament; *sumere* "receive". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 13.2). |
| missantes | mass-priests | Priests hired to say masses; pejorative. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 15.25). |
| pontifex (a Christian bishop, unqualified) | pontiff | As the Old Testament row; where the referent (a bishop) matters, an R note. *pontifices ydolorum* "pontiffs of idols". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 14.29, 15.17). |
| species (of bread and wine) | species | The sacramental species; kept as the term, not "appearance". Distinct from the logical *species*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 13.15; 23.8). |
| sacer; sacrare | sacred; hallow | Kept apart from *sanctus / sanctificare* "holy / sanctify" and from *consecrare*; *consecrare* is "to hallow together" in the grammarians' etymology. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 27–28). |
| sacramentum tantum | a sacrament only | The *sacramentum tantum* of the Lombard's three (IV d. 8 c. 4). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 29.23). |
| conversio (eucharistic) | conversion | Of bread into the body; kept apart from *conversio* of a proposition. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 48.15). |
| decretalis | decretal | Kept apart from *decretum* "decree". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 71.31). |
| principaliter; principalitas (of the body's presence) | principally; principality | Of the body of Christ alone being in the sacrament as its principal; not the compendium's *principaliter* "as a main head". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 75.5–26). |
| concomitanter | concomitantly | Of the body present with the blood by concomitance; cf. *gracia concomitancie*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 81.23–25). |
| divinitus | divinely | The pair of *humanitus* "humanly". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 84.19). |

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
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | CONTEXTUAL: condition / respect | "Condition": a person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). "Respect": the logical relation under which a predicate holds (*posiciones secundum habitudinem*), with a **C** note; ruled 2026-10-22 (Wilson; *Incarn.* 4.16). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |
| decretum; decreta | decree; the decrees | Gratian (*in decretis*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.14, 3.24). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
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
| sequitur | it follows | Introduces a stated inference, often quoted in the next words. Pilot (*Eccl.* 2.21). Not tagged where it is not an inference ("the third law follows", *Dial.* ch. 5). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| propositio copulativa / disiunctiva | conjunction / disjunction | Not "copulative proposition" (T. p. 365). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |
| humanitas | the humanity | The nature the Word assumed, body and soul; with the article (*humanitas sit Christus*, "the humanity is Christ"). Not "the human nature", which is *natura humana*. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| dimittere / dimissio (*naturam*) | lay aside / the laying-aside | Letting go the assumed nature, so the union would be dissolved. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 2.23). |
| ydemptitas specifica | identity of species | That Christ and other men are of one species. Not "specific identity" (reads as "particular"). Ruled 2026-10-22 (Wilson; *Incarn.* prol, 8). |
| Verbum | the Word | Pronoun **"he"** (as Douay–Rheims John 1:3, "by him"), never "it", though the Latin is neuter; so also *Sapiencia* where Wisdom is the Word in person (*Incarn.* 7, coordinator). Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.3–4). |
| homo assumptus | the assumed man | A term of art (the Lombard's first opinion, *Sent.* III d. 6); keep "assumed" before "man", never "the man assumed". With the agent expressed (*homo assumptus a Verbo*) "the man assumed by the Word", which cannot be misread (coordinator, 2026-10-22). Ruled 2026-10-22 (Wilson; *Incarn.* 5.15). |
| secundum quod (reduplicative) | insofar as | ⛔ Never "in that" (heard as "because", which inverts the logic). Ruled 2026-10-22 (Wilson; *Incarn.* 5.29–6.24). |
| secundum deitatem / secundum humanitatem | as to the Godhead / as to the humanity | The rule of reduplication; keep it in Wyclif's place in the sentence. ⛔ Never supply "as God / as man" where the Latin has bare apposition (*ipse Deus*) or bare predication. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| persona | person | Ruled 2026-10-22 (Wilson; *Incarn.* 4.14). |
| creatura / creator / creatus | creature / creator / created | ⛔ Never "creation" for the created thing. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| posicio / proposicio / predicacio | position / proposition / predication | Kept apart: the apparatus shows the three trading places (*Incarn.* 4.15). Ruled 2026-10-22 (Wilson). |
| sacramentum (of the incarnation, of creation) | sacrament | The Augustinian sense, "mystery" (1 Tim. 3:16): G note at the first occurrence in the chunk. Kept apart from *misterium*. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.8). |
| misterium | mystery | Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.3). |
| sancti | the saints | The fathers. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.15). |
| probabiles doctores | reputable doctors | *Probabilis*: worthy of credence (cf. *probabiliter*). Ruled 2026-10-22 (Wilson; *Incarn.* 7.1) as "approved doctors"; changed the same day (coordinator) to free "approved" for *approbati*. |
| approbati doctores | approved doctors | Kept apart from *probabiles doctores*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 13.3). |
| novelli | the newer [doctors] | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 13.7). |
| Sermo (beside *Verbum*) | Speech | The divine title, capitalised; *Verbum* stays "the Word". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 16–17). |
| de vi vocis / de vi sermonis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| nedum | not only | "Let alone" where the sense is a fortiori. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21, 24). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| gracia unionis | the grace of union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| humanitus | humanly | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* passim). |
| suppositum | supposit | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 34.24). |
| in quantum (reduplicative) | insofar as | As *secundum quod*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37.9). |
| unio | union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 39). |
| diccio (logical) | word | A single term in a proposition. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 43.3). |
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
| carneus / carnalis | fleshy / carnal | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.21). |
| passio (against *accio*) | being-acted-on | The category; G note at the first occurrence in a chunk. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 60.13). |
| supposibilis | that can be supposited | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 64.14). |
| dampnificare / dampnificacio | damage / damaging | Kept apart from *dampnum* "loss" and *dampnari* "be damned"; the argument of 65–68 turns on it. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 65). |
| per se / per accidens | of itself / by accident | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a (sufficienti) divisione | the topic from sufficient likeness / from (sufficient) division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| pretericio | being past | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| peccabilis | able to sin | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| ydemptitas ypostatica | hypostatic identity | Beside *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 84.20). |
| passionatus | subject to passion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| capitales doctores | the chief doctors | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| eiusdem / consimilis / alterius racionis | of the same / like / another kind | The species-sense of *racio*; *racio speciei* "the account of the species" (Aristotle's *logos*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.4, 87.17). |
| principiari | be constituted from principles | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.7). |
| accidentatus | subject to accidents | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.4). |
| in recto / in obliquo | in the direct case / in an oblique case | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.25). |
| passibilis | passible | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.12). |
| signum / signatum | sign / thing signified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 91.2–6). |
| conveniencia / convenire (*in*) | agreement / agree | The argument of 90–91 turns on it; not "fittingness" (that is *congruencia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 90). |
| predicacio synecdochica | synecdochic predication | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.27). |
| conversari | live one's life (among men) | Beside *conversacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.25). |
| esse intelligibile | intelligible being | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 99.23). |
| mobile (noun) / primum mobile | a movable / the first movable | Against the adjective *mobilis*; ch. 7 turns on it. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 107, 116). |
| res racionis | thing of reason | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| significatum | significate | Kept apart from *signatum* "thing signified". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 111). |
| sermo vocalis | the spoken word | Against *Sermo* "Speech", the divine title. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 113). |
| predicacio secundum essenciam / formalis | predication by essence / formal predication | Wyclif's modes of predication (cf. *predicacio secundum causam*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 115–116). |
| forma substancialis | substantial form | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| concepcio (figure) | conception | The grammatical figure. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habitus (of the humanity) | habit | The Lombard's third opinion (*Sent.* III d. 6). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| reputacio | estimation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| accidens | accident | The category; *accidit* "befalls". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habitacio | habitation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 120.14). |
| figura / figuratum | figure / thing figured | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 121.23). |
| conversio (of a proposition) | conversion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.30). |
| humanitacio | humanation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 126.12). |
| racio (individual, personal) | account | *Racio individui / persone* "the account of an individual / a person", as *racio speciei*; not "aspect" (the row against *substancia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 8, 129–132). |
| vir (against *homo*) | man (*vir*) | Where Wyclif sets *vir* against *homo*, the Latin in parentheses. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 129.15–26). |
| analogicari | be said analogically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 131.27). |
| exemplaria / exemplata | exemplars / things exemplified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.6). |
| res secunde intencionis | things of second intention | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.25). |
| complexio | complexion | The mixture of qualities. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137–138). |
| materia proxima / remota | proximate / remote matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137.1). |
| personari | be made a person | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 134.10). |
| ydemptificare / ydemptificacio | identify / identification | Make the same (*idem*); the hypostatic union as identification, not conversion or generation. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 142.19, 147.22). |
| res communis / res communes | the common thing / common things | The realist universal the *moderni* do not conceive (first root of their error). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 144.27). |
| distinccio racionis | distinction of reason | Beside *differencia formalis*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 145.23). |
| conversio naturarum / confusio naturarum | conversion of the natures / confusion of the natures | Kept apart from *conversio* of a proposition. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 143.9). |
| principiare (active) | be the principle of | Beside the passive *principiari* "be constituted from principles". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 147.4). |
| supposicio simplex / supposicio personalis | simple supposition / personal supposition | Supposition theory. *Simpliciter / personaliter supponere* "stand with simple / personal supposition": NOT the *simpliciter / secundum quid* pair, C note where the two could be confused. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 152.5–12). |
| personalitas | personality | The scholastic term: what makes a person a person, not character. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 155). |
| in quid (predicari in quid) | in quid | Kept in Latin (predication of what a thing is, as against *in quale*), glossed at first use in a chunk. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 162.22). |
| suppositari | be supposited | Verb beside *suppositum*, *suppositacio*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 161). |
| substancia prima / substancia secunda | first substance / second substance | Aristotle, *Cat.* 5. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.25). |
| a simili | by likeness | Bare, as an argument form; beside *locus a simili* "the topic from likeness". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.16). |
| racio substancialis | substantial account | As *racio individui* "account". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.21). |
| doctores signorum | the doctors of signs | The logicians who reason from terms, not things. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.26). |
| ydemptitas numeralis | numerical identity | Beside *ydemptitas specifica* "identity of species". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 172). |
| suppositalis | of a supposit | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 176). |
| accidens absolutum | absolute accident | Quantity and quality, against relative accidents. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 176). |
| beatificabilitas | beatifiability | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 181). |
| passionaliter | as an attribute | Beside *passio* (the proper attribute). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 181). |
| mocio / motus (paired) | motion (*mocio*) / movement (*motus*) | Only where Wyclif pairs them; otherwise "motion". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 180). |
| posicio anime | the laying-down of the soul | John 10:17–18; not the logical *posicio* "position", C note. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 183.3). |
| causancia / causacio | causing / causation | Kept apart (both at 187.30–34). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 185.16). |
| personare (active) / personacio | make a person / personation | Beside the passive *personari* "be made a person". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 188.16, 188.32). |
| vicem supplere / vicis supplecio | supply the place / the supplying of a place | God supplying the place of a second cause. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 187.26). |
| perfeccio simpliciter | perfection without qualification | After *simpliciter* "without qualification". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.1). |
| multiplicative | multiplicatively | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 193.20). |
| habitudo relativa | relative respect | The "respect" sense of the CONTEXTUAL *habitudo* row. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 193.19). |
| remitti / intendi (of a quality, merit) | be remitted / be intensified | The intension and remission of forms; not *remissio* of sin. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 197.1–7). |
| in divinis | among the divine [persons] | Keeps "Godhead" for *deitas*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 196.18). |
| partes proporcionales | proportional parts | The halving division of a continuum. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 194.24). |
| multiplicacio dimensionalis | dimensional multiplication | One body in several places by its dimensions. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.6). |
| habitus (= possession, *habere*) | the having | The category of having, C note; kept apart from *habitus* "habit". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.14). |
| proporcio racionalis | rational proportion | The mathematical ratio. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 207.7). |
| a maiori vel pari | from the greater or from the equal | Arguments *a maiori*; cf. *locus a maiori*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 209.5). |
| mocio progressiva / motus progressivus | progressive motion | Locomotion. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 205.28). |
| communioritas | greater commonness | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 210.15). |
| multiplicacio concomitancie | multiplication of concomitance | Cf. *gracia concomitancie*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 213.21). |
| nomen appellativum | appellative name | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 213.29). |
| imposicio primaria | primary imposition | Of a term's first assignment to signify. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 214). |
| assertibile | assertible | The thing a proposition asserts. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 215). |
| superioritas / inferioritas terminorum | superiority / inferiority of terms | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 215). |
| homo communis | the common man | The universal man, with *res communis*; not "the ordinary man". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 218.3). |
| congruencia | fittingness | The reasons of fittingness for the Son's incarnation. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 225.6). |
| signum reduplicatum | the reduplicated sign | The reduplicative word (*secundum quod*, *in quantum*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 230.23). |
| supposicio | supposition | Of a term (supposition theory) or of a premiss laid down (cf. *supponitur* "it is supposed"); the English word serves both, C note where it matters. Kept apart from *suppositacio* "suppositation". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 102.8). |
| lex proximitatis | the law of neighbourhood | The duty to love one's neighbour (*proximus*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 101.29). |
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
| corporaliter | bodily | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| substancialiter | substantially | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| sentencia (verborum, scripture) | sense | The meaning of words or a text (*ad sentenciam attendendum*, against the rites, 4.9); kept out of the two-sense row *sentencia*. Ruled 2026-11-06 (Wilson; *Euch.* prol-a 4.9, review b14). |
| predicacio ydemptica / tropica | identical / tropical predication | The treatise's key pair; *tropica* kept apart from *figurative*. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.21). |
| accidens sine subiecto | accident without a subject | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 3.19). |
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
| figurare | figure | Both senses: to prefigure (the lamb figured Christ) and to shape (*figurare Deum nostrum*), which Wyclif plays on; one English word keeps the pun. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-c 10; 21.29). |
| supponere pro | stand for | Supposition; with *supposicio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 24.27). |
| sensualiter | sensually | Berengar's oath word (*Ego Berengarius*); kept apart from *sensibiliter* "perceptibly". A mode adverb, one word. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 26.1, 30.24). |
| sentire (an opinion: sensit quod) | hold | Of a doctor's or church's opinion; the "perceive" row is the sacrament sensed. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 30.30, 31.18). |
| predicacio figurativa | figurative predication | A synonym of *predicacio tropica*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 35.18). |
| expositorie (of preaching scripture) | by way of exposition | Not the logicians' *expositorie* "expositorily" of the expository syllogism. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 46.4). |
| aliquitas | somethingness | Being a something (*aliquid*). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 60.27). |
| cedere (in) | give way (into) | Of the bread passing into the body. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 58.3, 60.9). |
| accidens predicamentale | accident of the categories | Kept apart from the predicable *accidens*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 64.1). |
| contiguacio | contiguity | Beside *continuacio* (of bodies) "continuation". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 68.12). |
| veritas predicamentalis | truth of the categories | As *accidens predicamentale* "accident of the categories". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 69.2). |
| convincere; conviccio | prove conclusively; conclusive proof | Of an argument that compels assent; "convince" never; of a witness or liar shown guilty, "convict" (*Euch.* 01-c). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 78.10, 79.10–12, 85.27). |
| esse situale / intencionale / potenciale | situal / intentional / potential being | The modes of the body's being. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 84.8 ff.). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| magisterium | rule; of teaching, the teaching office; *quale magisterium* "what a feat of mastery" (*Incarn.* 137.14) | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). Inside a DR quotation of Titus 1:7, DR's "steward" (2026-10-08). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| dotes (docium) beatorum; dotes corporis | the dowries of the blessed; the dowries of the body | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| continuacio (of bodies, the act) / discontinuacio; continuare / discontinuare | continuation / discontinuation; make continuous / make discontinuous | The making of several bodies into one continuum (*Incarn.* ch. 12), G note at first use: not "carrying on". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.30, 211.12). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
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
| ordo per accidens | order by accident | Ruled 2026-10-02 (*Eccl.* 21, 514.29). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| memoriale | memorial | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| remissio; remittere | remission; to remit | Headword row (cf. *condonacio* "pardon", *venia* "forgiveness"). Ruled 2026-10-02 (*Eccl.* 23). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). Beside *consecrare* (*consecrat et conficit*) "confect", so the pair stays two. Ruled 2026-11-07 (Wilson, "confect works"; *Euch.* 16.10). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| criminosus | criminous man | Ruled 2026-10-07 (*Pot. pape* 06-c). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| preeminencia | preeminence | Kept apart from *primatus* "primacy". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| regulariter | as a rule | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 165.2). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| memorativa potencia | memorative power | A faculty of the soul (the "power" sense of *potencia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 219.27). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| malum culpe / pene | the evil of fault / of penalty | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.19). |
| neutra | neutral things | Things neither commanded nor forbidden (obedience *in neutris*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.19). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| imperium (vicarium, autoritativum) | command (vicarial, authoritative) | The power to command (*par in parem non habet imperium*); "empire" only of the Empire. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 263.2). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| summus sacerdos | high priest | DR; kept apart from *summus pontifex* "highest pontiff". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 265.20). |
| preponderancia; dispensacio | preponderance; dispensation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 266.11, 268.4). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| precellencia | pre-excellence | Kept apart from *preeminencia* "preeminence". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 274.33). |
| summum sacerdocium | high priesthood | Cf. *summus sacerdos* "high priest". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-c, 11-d). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| pontifex (Old Testament, unqualified) | pontiff | Kept apart from *sacerdos* "priest"; *summus pontifex* of the Jewish priesthood is "high priest" (see *summi pontifices*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* ch. 11). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| pastor cesareus | caesarean shepherd | The *papa cesareus* family. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 290.24). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| precellenter | pre-excellently | Adverb beside *precellencia* "pre-excellence". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 291.2). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| remisse (of assent) | with slackened [assent] | Opposed to full assent in the degrees of belief. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 328.18). |
| potissimus; pocior (Antichristus) | foremost; greater | Superlative and comparative kept visible as a pair. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.28, 331.12). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| evangelizans | preacher of the gospel | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-g). |
| prepositus (participle of *preponere*) | the one preferred | CONTEXTUAL beside *prepositi* "superiors" (the noun); untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| provisio (papal) | provision | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* ch. 12). |
| decimacio | tithing | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 359.26). |
| decimantes | tithe-payers | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 359.24). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |
| diccio procuratoria | proctorial pronouncement | C note gives *dicio* "authority" as the alternative. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 386). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| precellere | excel | Verb beside *precellencia* "pre-excellence"; not "pre-excel". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 399.28). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |
| nimis | exceedingly | Medieval intensive (= *valde*); "too much" only where excess is the point. Ruled 2026-10-12 (close-out R2; *Pot. pape* 169.2). |
| sentire (the sacrament, the body) | perceive | "sense". As *sensibilis* "perceptible". Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.10, 1.17). |
| postponere | set aside | "put after". Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 4.8). |
| singulariter | CONTEXTUAL: alone, only / in a singular way | "singularly" never; "in a singular way" where "alone" will not construe (*Euch.* 85.28, coordinator 2026-11-07). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 4.14). |
| narrare | relate | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.9). |
| pius pater | loving father | *pius* of a father: not "pious". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 42.27). |
| ex tibi dubio; ex sibi dubio | for all you know; for all he knows | Idiom: not "from doubt". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 66.15, 70.25). |

---

## Chunk 04-b: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-04-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-04-b
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "87.29–90.22"
divisions: "cap. 4 (heading 'CAPITULUM QUARTUM.' at 83.0); part 2 of 9, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "619 words; 614 confirmed by the vote; 4 runs stood by rule; 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n158–n161 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 4, part 2: [TITLE]

## ¶1 · 87.29–88.2

> [p. 87] Tres, inquam, inter multas erant figure huius sacramenti in veteri testamento; prima erat agnus pascalis qui nedum figuravit agnum Dei qui tollit peccata mundi Joh. Iº, 29 sed ipsummet sacramentum; et [p. 88] hec racio quare debuit cessare esus agni paschalis post institucionem huius sacramenti signati pocioris.

[ENGLISH]

## ¶2 · 88.3–88.8

> [p. 88] Secunda figura huius sacramenti fuit fluxus aque de lapide (de quo Exodi XIIº); hoc enim significat secundum Apostolum bibicionem spiritualem sanguinis petre Christi: Omnes, inquit, spiritualem potum eundem biberunt, bibebant autem de spirituali consequente eos petra; petra autem erat Christus.

[ENGLISH]

## ¶3 · 88.9–88.26

> [p. 88] Tercia figura erat manna (de quo Exod. XVIº); unde Christus Joh. VIº, 59 complectens excellenciam huius sacramenti et rei sue super hoc manna: Non, inquit, sicut manducaverunt patres vestri manna et mortui sunt. Qui manducat hunc panem vivet in eternum. Nam secundum exposicionem beati Augustini Omelia XXVI licet commune sit nobis et illis mori, tamen illi manducantes manna corporaliter et remurmurantes contra Dominum mortui sunt corporaliter et in mente dampnabiliter, sed qui manducat spiritualiter panem Christum vivet spiritualiter in eternum, cum iuxta dicta ille rite manducat corpus Christi spiritualiter qui assimilatur sibi ut membrum glutino caritatis perpetue. Quamvis autem multi comedentes manna fideliter erant incorporati ecclesie, tamen illo sacramento non meruerunt presencialiter sed valde distanter apercionem ianue. Et patet in parte responsio ad dubium motum in capite huius capituli.

[ENGLISH]

## ¶4 · 88.27–89.3

> [p. 88] Sed pro declaracione ulteriori sunt tria plus declaranda: primo de veritate et virtute verborum huius sacramenti, secundo quid et qualiter de hoc sacramento [p. 89] in compendio est credendum, et tercio quomodo ad dignitatem recipientis huius sacramenti debet homo disponi.

[ENGLISH]

## ¶5 · 89.4–89.20

> [p. 89] Quoad primum dicitur quod verba ipsa successiva et interpolata non habent ex se efficaciam convertendi, sed sermo Dei assistens in cuius persona dicuntur facit opera; et creditur quod placet verbo Dei operari per verba vocalia, ut vel sic discamus quod ipsum facit opera et inproprie atque equivoce eius instrumenta. Summus enim artifex operatur per valde abiecta et debilia instrumenta. Si queratur quando talis proposicio sacramentalis incipit esse vera, dicitur quod non quando desinit esse per remocionem de presenti, cum tunc non est, et quod non est, non est verum, sed pro ultimo instanti esse sui, cum sit dare composicionem continui ex non quantis, et cum omnia que fuerunt vel erunt sunt, interpollacio non impedit proposicionem esse vel secundum unam partem vel aliam, sed pro tempore interpolacionis desinit taliter esse; que omnia hic suppono ex alibi declaratis.

[ENGLISH]

## ¶6 · 89.21–90.3

> [p. 89] Et videtur michi modo quod panis demonstratur pronomine, et sic est proposicio vera ad suum sensum, sicut videtur Augustinum concedere, hoc est Christus, demonstrata quacumque creatura, ut patet super Johanne Omelia XIII. Sed in demonstrando hoc sacramentum est quedam singularis efficacia et significacio a Christo imposita, ideo theologus debet notare quomodo ista est singulariter concedenda. In casu autem quo intelligatur proposicio non figurative sed effective, tunc per pronomen demonstratur sub habitudine accidencium illud in celo quod est realiter [p. 90] corpus Christi. Si autem intelligatur proposicio figurative, sicut videtur historiam evangelii intelligere, tunc intelligi et demonstrari debet pronomine panis ille.

[ENGLISH]

## ¶7 · 90.4–90.12

> [p. 90] Sed quantum ad formam verborum declarat dominus Armachanus IXº De Questionibus Armenorum per multa capitula quomodo nulla forma verborum quoad linguas et nomina est generaliter requisita, cum autores varie scripserant quoad linguas, ut Mattheus in Hebraico, Marcus in Ytalico, Lucas in Siro et Paulus in Greco. Et cum usque hodie secundum istas linguas et plures iuxta doctrinam fidei scripture in diversis contratis conficiunt, patet conclusio.

[ENGLISH]

## ¶8 · 90.13–90.22

> [p. 90] Unde licet sacerdos in Anglico et aliis linguis barbaris posset conficere, tamen peccaret inde ex presumpcione postponendo latinum vel linguam quam famosius quoad locum, gentem et tempus approbat sua ecclesia, linguam quoad talem consecracionem contra loci consuetudinem commiscendo; circa limites vero huius difficultatis de gravedine peccati facti in ipsam est infructuosa contencio, cum homo debet nisi urgente magna causa et racionabili se consuetudini laudabili loci quem incolit conformare.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 87.29: The old law had three types of this sacrament:
- 87.31: I. the paschal lamb,
- 88.3: 2. the water from the rock,
- 88.9: 3. the manna.
- 89.4: The words spoken are but instruments; it is God's word that effects the change.
- 89.21: 'This' refers to the bread,
- 90.4: The evangelists used different languages.
- 90.13: In consecrating it is right to follow the established use.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 89: *esse* (print = bt) [BT-ONLY]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 87:
1 — 3. C: sentencie — scribencium in marg. alia manu. \. E: quantum
dicitur. 4., 5. I>: excellit. 6. ABDE : distabant. 8. A: comitative ;
B: concomitate. 9. ABE: destitit; C: desit. 12. B: comitative.
14. B: efficaciter. 16. ABCD : comitantem. 18. D: divise. 18, 19. A :
sacramentum alia manu add. 19. D : sic nisi; ib. E : sunt. 21. B : reduntur.
23. ABC : rei sui. 25. Codd. : excessit. 29. E:multa. 32. D : met deest.

p. 88:
1. E: qualiter ; ib. E: cessare agnus. 3. E: Secunda causa.
7. D: bibunt. 9. ABD : fuit manna. 11. ABC : sui ; ib. C: hoc in
marg. alia manu. 12. E: vestri dcest; ib. D: manna in deserto.
i5. B: et illis dccst. 22. D: quam nisi. 23. C: manna in marg. alia
manu. 24. C: principaliter extinct. ; in marg. alia manu : presencialiter.
27, 28. D: declaranda per ordinem.
6. L Cor. X, 4. 14. S. Augustini In Johannis Evang.,
cap. VI, tract. XXVI, Opp. tom. III, pars 2, pag. 408.

p. 89:
1. 2. B: quo ; C: quomodo in marg. 2. D: recepcionis. 4. AB: ipsa
deest; C in marg. addit; ib. E: successive. 5. B: efficacem. 12. B: in-
cipit. 18. D: in secunda. 25. E: de Omelia. 28. E: est deest.
29. C: quo in marg. alia manu. 3i. D: illud intelligo.
2 5. St. Augustini In Joh. Evang., cap. III, tract. XIII. Opp.
tom. III, 2, 390.

p. 90:
3. D: declarari. 5. D: Ordmacanus ; E: Ardmacamm ; ib. D : et per.
6. D: capitula in illa. 8. ABC: ut dcest. 12. D: contractis (contrattis).
i5. D: quamquam. iG. D: aproperat. 17. C: Iinguam in niarg. alia
manu. 19. D: difficilitalis. 21. C: magna in marg. alia manu ; ib. se;
D: seu. 25. H : alia. 33. BCD : effundetur.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 87: rr rr ■ | agnum Dei qui tollit peccata | Aliud est sacramentum, aliud virtus sacramenti; sacramentum enim ore percipitur, virtute sacramenti | homo interior saciatur; igitur quia panis corpus confirmat, ideo ille corpus Christi congruenter nuncupatur; vinum autem quia sanguinem operatur in carne y ideo ad sanguinem Christi refertur; hec autem dum sunt visibilia sanctificata per Spiritnm Sanctum, \5in sacramentum divini corporis transeunt. | Maluit enim Dominus corporis et sanguinis sacramenta fidelium ore percipi et in partem eorum redigi, ut per visibile opus invisibilis ostenderetur effectus. | vel reprobant. | est virtns.
p. 88: sjpiritualempotum eundem biberunt, bibebant autem de spirituali consequente eos petra; petra autem erat Christus. | sicut manducaverunt patres vestri manna et mortui sunt. Qui manducat hunc panem vivet in eternum. | cum sit splendor patris et figura substancie eius. | quod dicit. | quod ille. | ab eo. | beatorum prelatorum; | parare et.
p. 89: sit — sacramenti | tantam regulam. | Cap. VII. | Et ut a :
p. 90: Hic est enim sanguis meus novi testamenti qui pro multis effun- | detur in remissionempeccatorum; | Hic est calix novum testamentum in meo sanguine qui pro vobis fundetur.
```

---

## Chunk 04-c: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-04-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-04-c
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "90.23–94.28"
divisions: "cap. 4 (heading 'CAPITULUM QUARTUM.' at 83.0); part 3 of 9, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "934 words; 923 confirmed by the vote; 11 runs stood by rule; 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n161–n165 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 4, part 3: [TITLE]

## ¶1 · 90.23–93.20

> [p. 90] Ulterius quoad formam verborum in lingua latina in qua Romana ecclesia habet fidem scripture, videtur quod non sit aliqua forma verborum ad confeccionem eukaristie generaliter requisita; nam usus ecclesie nostre variat ab omnibus illis quatuor, sicut et omnes illi variant ab invicem plus vel minus. Nam Mattheus XXVIº, 28 habet ista verba consecracionis vini: Hic est enim sanguis meus novi testamenti qui pro multis effundetur in remissionem peccatorum; Lucas vero XXIIº, 20 ponit sic: Hic est calix novum testamentum in meo sanguine qui pro vobis fundetur. Marcus vero XIVº, 24 [p. 91] varians a Mattheo dimittit enim et in remissionem peccatorum. Paulus vero tradens nobis sentenciam quam accepit a Domino I. Cor. XI° sic loquitur: Hic calix novum testamentum est in meo sanguine; hoc facite quocienscunque biberitis in meam commemoracionem. Sed ab omnibus istis variat usus nostre ecclesie, ut patet tercio decretalium Cum Marthe, titulo De Celebracione Missarum. Cum ergo secundum has quinque formas contingit vere conficere, patet conclusio. Per hanc itaque variacionem quintimembrem docemur preponderanter ad sensum attendere et quod talis variacio verborum non est de substancia sacramenti; nam contingit (sicut de facto contigit) per verba istarum quinque formarum conficere, quia aliter ante istam ordinacionem quintam ex defectu scripture deficerent ecclesie sollempnes, ymmo forent ydolatre decipientes se ipsos et populum ex falsitate scripture, et sic ex narracione evangelistarum tocius et omnium titubaret auctoritas, et per consequens superflue laboraret Augustinus per totum librum De Concordia Evangelistarum. Nec valet dicere quod quintus ordo est necessarius post publicacionem usus ecclesie Romane et non ante, quia sic liceret pape contra evangelium dispensare, eius errores corrigere et per consequens novum evangelium de toto condere; quod suppono hic a iuribus fidelium esse horribile, cum decreta Romanorum pontificum in fide sepius titubaverunt, ut patet distinccione XVI, capitulo VI. Sinodus, prima distinccione, capitulo I, De Penitencia [p. 92] quasi per totum et specialiter in ista materia. Quando enim quis peccando mortaliter deficit in moribus deficit et in fide, ideo inprovida et nimis levis videtur diffinicio eorum qui dicunt quod dimittendo verbum vel quamcunque aliam formam qua utitur ecclesia Romana sacerdos non conficit, quia diverse lingue habent diversum modum sonandi eciam latinum, ut patet in sonacione huius littere ‘C’; ymmo oportet diversimode organisantes secundum disposicionem figure celestis diversimode sonare; ideo idem foret dicere quod oportet omnem sacerdotem vel populum istam formam sonorum in confeccione huius sacramenti attendere et dicere quod oportet omnem salvandum esse istius complexionis et plage, quod foret infidelis accepcio personarum; ideo (ut dicit doctor) satis est quod fideles concordent in sentencia ante linguam, ut quod panis figurative est corpus Christi et vinum eius sanguis; et sic salvantur dicti quatuor evangeliste a mendacio, quando asserunt Dominum sic dixisse, hoc est, dixisse istam sentenciam sive sensum. Concordare tamen debet sacerdos cum patria et usu ecclesie in istis et ritibus similibus stante substancia sentencie ut in neutris. Unde usus ecclesie quem habemus licet sit colatus ex scriptura sacra, non est melior quam quilibet quatuor usuum evangelistarum; et Deus scit utrum sapuit peccatum illa varietas introducta. Teneamus ergo sentenciam requisitam; illud autem reputamus requisitam sentenciam in qua omnis isti quatuor evangeliste concordant et illam in qua variant esse necessariam ad [p. 93] mores, sed preter essenciam sacramenti; et utinam nimis observantes Judayce ritus et consuetudines hominum quos ultra veritatem Dei colunt attenderent ad istam sentenciam, nam phariseice colant culicem et degluciunt camelum, exigentes quod populus sequatur ritus et precepta et mores eorum; sed dicunt stultum esse attendere ad consilia Christi, ad vitam vel conversacionem Christi ac Petri, cum oportet propter distanciam et variacionem temporis nunc observare contrarium, et sic observantes paleam dimittimus granum purum; ideo oportet quod nos vertiginosi non excuciamus religionem quam Christus instituit, quia Eccli. XIX°, i dicitur: Qui spernit modica paulatim decidet; debemus ergo postponendo ritus novellos observare mores Christi et opera, quia secundum Gregorium I° Pastoralium III° idcirco Jesus in carne venerat ut non solum nos per passionem in carne redimeret, verum eciam per conversacionem doceret; ideo ve nobis, si latemus in tenebris vel retrocedendo vel declinando ipsum non sequimur.

[ENGLISH]

## ¶2 · 93.21–93.24

> [p. 93] Sed contra istud instatur tripliciter; videtur primo, cum Christus instituit et precepit capi hoc sacramentum in cena, quod nos debemus ipsum sequi et apostolos eius celebrando post prandium.

[ENGLISH]

## ¶3 · 93.25–93.29

> [p. 93] Hic dicitur quod conclusio est vera; sed pro materia notandum est quod, sicut Christus cum apostolis sumpsit hoc sacramentum ieiunus a crimine, sic oportet nos in hoc sacramento eorum discipulos sequi ipsos.

[ENGLISH]

## ¶4 · 93.30–94.15

> [p. 93] Sed quia in nobis ex cibario causatur communiter ventris ingluvies, ideo pia religione ieiuni corpore [p. 94] sacramentum istud accipiamus; et ne paulativa declinacio inducat periculum, statuimus nobis pro regula quod omnino ieiuni in corpore celebramus et nimis prepostere plus ponderamus illud quam imitacionem Christi in ieiunio a peccato, et sic de ritu quoad locum et tempus ac alias observancias circa hoc sacramentum racionabiliter ordinatas. Illas autem laudo sed preponderancias earum et nimietatem detestor; unde cecitas pharisaica est qua putamus Christum pocius sequendum in ritibus quam virtute, ut licet Christus sic prandebat cum duodecim quorum unus fuit traditor et sic de infinitis circumstanciis: non tamen oportet nos illas attendere, cum non per se dicant virtutes secundum imitacionem Christi quoad genus virtutum omnimode conservare.

[ENGLISH]

## ¶5 · 94.16–94.28

> [p. 94] Tres autem assignant homines causas quare Christus secundum hunc ordinem sacramentum istud instituit; prima quia oportuit esum agni paschalis, cum fuit figura huius sacramenti, precedere; secunda ut Christus doceat nos ordinaciones futuras imitacione sua in moribus minus attendere; et tercia ut legislator et auctor doceat ex ista varietate in ipso esse preeminenciam potestatis; ideo cum debemus sequi Christum, non precedere vel ex equo viare cum ipso, debemus gaudere de privilegio quod habet ut Deus et ut primogenitus ex vi gracie unionis et utrobique sequi ipsum vel proporcionaliter vel similiter secundum moralem congruenciam nostri status.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 90.23: The exact words of consecration are not essential, since they differ in Scripture.
- 91.20: The use of the Roman Church cannot make one form essential.
- 92.6: There are different pronunciations even of Latin.
- 92.16: What we have to attend to is the sense, in which the evangelists agree, although they differ in the words.
- 93.21: Christ did not ordain fasting communion.
- 93.25: It is more important to fast from sin, but to communicate fasting is a good practice.
- 94.16: Three reasons why Christ did not ordain us to fast before communion.

## Notes

## Transcription notes
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 90:
3. D: declarari. 5. D: Ordmacanus ; E: Ardmacamm ; ib. D : et per.
6. D: capitula in illa. 8. ABC: ut dcest. 12. D: contractis (contrattis).
i5. D: quamquam. iG. D: aproperat. 17. C: Iinguam in niarg. alia
manu. 19. D: difficilitalis. 21. C: magna in marg. alia manu ; ib. se;
D: seu. 25. H : alia. 33. BCD : effundetur.

p. 91:
1. B: variantes; ib. C: et decst. 6. E: nostre deest. 8. titulo ;
B: i5o ; ib. Codd.: misse. 9. C: vere in marg. alia manu. 12. A: non
est in marg. alia manu. o. B: istam deest. 21. B: per conversacionem
dicere ; A: per conversacionem in marg. alia manu. 26. B: omne hor-
ribile. 29. prima; Codd. : XXXI.
7. Decret. Greg. IX, lib. III, tit. XLI, cap. VI. 28. Decreti
Prima Pars, dist. XVI, cap. VI. Habeo librum. 29. Decreti
Secunda Pars, De Penitencia, dist. I, cap. I.

p. 92:
[. C: t'g'a in marg. alia manu. 2. E: moraliter. 4. AB : verbum
deest; C in marg. addit. 7. C: loquendi cxtinct.; in marg. corrcxit:
sonandi. 10. D: diversimode deest. 12. C: comecracione in textu
extinct. ; confeccione in marg. alia manu. 17. D: panis est figurative.
23, 24. ABC: Unde sensum quem; C correxit: usus ecclesie ; D: Unde
sensus quem. 25. C: est in marg. alia manu. 26. C : dominus in
marg. alia manu. 28. AB: putamus ; C correxit.

p. 93:
t. AB: et utinam deest; C addit in marg. 4. nam; E: orant :
ib. D: colunt. 6. E: sequitur. 7. E: vel vitam. 7, 8. D: ad con-
secrata Christi; ib. D: vel versacionem. 11. D: ideoque. 14. D: decidit.
18. D: conversionem. 23. B: sed nos debemus. 27. E: cepit hoc ;
ib. crimine; D: anime.
16. St. Gregorii Regulae Pastoralis I, 3. Opp. tom. II, pag. 4, 5.

p. 94:
1. E: accipimus. 4. ABD : meus prepostere ; C: modo prepostere.
10. B: et ritus. 12. B: totaliter traditor. 14. DE: sed imitacionem;
14. D: aut quo. 16, 17. AB: quare secundum hunc ordinem Christus.
18. E: primum; ib. C in marg. alia manu: esum. 20. D: in imitacione.
22. AB: varietatem; C correxit. 20. D: excipiatur. 3i. C: devotus
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 90: Hic est enim sanguis meus novi testamenti qui pro multis effun- | detur in remissionempeccatorum; | Hic est calix novum testamentum in meo sanguine qui pro vobis fundetur.
p. 91: in remisswnem peccatorum. | Hic calix novum testamentum est in meo sanguine; | hoc facite quocienscunque biberitis in meam commemoracionem. | Cum Marthe,
p. 93: Qui spernit modicd paulatim decidet; | idcirco Jesus in carne venerat ut non solum nos per passionem in carne redimeret, verum eciam per conversacionem doceret;
```

---

## Chunk 04-d: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-04-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-04-d
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "94.29–98.14"
divisions: "cap. 4 (heading 'CAPITULUM QUARTUM.' at 83.0); part 4 of 9, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "771 words; 760 confirmed by the vote; 10 runs stood by rule; 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n165–n169 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 4, part 4: [TITLE]

## ¶1 · 94.29–95.7

> [p. 94] In isto autem exemplatur infirmo vel in alia necessitate posito quod licet sibi prandenti accipere corpus Christi; cum devotus audiens missam post gentaculum melius sepe accipit quam sacerdos suus [p. 95] qui celebrat: Melius eciam celebraret in casu sacerdos eadem die artificiali post nonam et prandium quam institutis humanitus quantumcunque ordinata apparencia celebrando, sicut melius in casu comederet tam clericus quam laycus corpus Christi, predicando vel opus meritorium faciendo quam conficiendo, quia copiosius haberet Christum in anima.

[ENGLISH]

## ¶2 · 95.8–95.14

> [p. 95] Secundo obicitur per hoc quod Mattheus et Marcus narrant quomodo Christus accepit panem, benedixit fregit et dixit: Accipite et comedite, hoc est corpus meum, ubi videtur benediccio Christi nobis abscondita precedere verba que nos ponimus consecracionis; aliter enim non sequeremur Christum frangendo post confeccionem hostiam consecratam.

[ENGLISH]

## ¶3 · 95.15–97.28

> [p. 95] Hic dicitur quod benedicere accipitur in proposito pro gracias agere, modo quo omnis creatura sed precipue racionalis benedicit Deum. Unde in confirmacionem istius sentencie, ubi Mattheus et Marcus dicunt benedixit Lucas et Paulus dicunt: Gracias egit vel gracias agens fregit, et in isto nos sacerdotes Christum sequimur modo nostro; debemus enim in omnibus operibus nostris sequi Christum; vel quadam propinqua similitudine, ut quoad opera humanitatis sue vel quadam analoga proporcione ut quoad opera divinitatis et primogeniture sue, et diversi debent sequi eum diversimode secundum quod Christus debet esse regula status sui, ut posito duce exercitus qui errare non poterit et quem severe iniunctum est quodlibet membrum exercitus sequi modo suo, patet quod aliqui sequerentur uno incessu et aliqui alio, [p. 96] secundum differenciam qua post ipsum sunt positi. Aliqui eciam sequerentur ipsum propinquius et alii distancius secundum quod in calore et virtute secundum locum motiva et organis variantur; sic dispari incessu secuntur fideles Christum secundum disparitatem statuum et gracie quibus capitaneus illos vocat. Omnes tamen salvandos oportet sequi hunc ducem (ut docet Crisostomus In Imperfecto Omelia VII°), quia ipse est via sine qua nemo potest celestem civitatem attingere. Unde ait supra: Triplex ponitur causa, quare quatuor evangeliste qui sunt organa Spiritus Sancti tantum in istis verbis sacramentalibus variabant; potuit enim facillime facere omnes illos quatuor similime concordare; sed ista variacio fuit magis conveniens, primo ut doceret per hoc predictam veritatem katholicam quomodo totus christianus exercitus debet dispariter sequi Christum; sicut istorum quatuor evangelistarum discipuli quadam varietate decenti sub variis formis conficiunt sacramentum, et omnes sequuntur Christum; secundo ut iste subtilis et realis philosophus ostendat se habere curam parvam de signis sed principaliter attendere ad sentenciam designatam, et tercio ut lex sua in varietate verborum que sunt nobis exercicia sit gravidata multiformi sentencia. Non enim est aliqua istorum evangelistarum quantumcunque parva varietas, quin trahit secum notandam subtilitatem sentencie, ut in sacramento sanguinis singulariter fit mencio de testamento, quamvis tam consecracio panis quam calicis ad novum testamentum pertineat; cuius misterium credo esse quod [p. 97] liquor solet effundi in lege veteri in testimonium contracti federis, in signum quod sanguis eius effundi debeat qui fedus illud diruperit, ut patet; Christus autem authonomatice effudit sanguinem suum preciosum in testimonium federis inter sponsum et ecclesiam et pene dissipancium legem suam, et sic effusione sanguinis Christi testamentum suum confirmatum est. Cui sentencie videtur Zachariam alludere, dum IX° capitulo sic alloquitur Jesum nostrum: Tu quoque in sanguine testamenti tui eduxisti vinctos tuos de lacu in quo non est aqua. Istud autem misterium non sic pertinenter exprimeretur faciendo cum verbis sacramenti panis memoriam testamenti. Sed notandum ulterius quod evangelium Luc. XXII°, 20 habet sic: Hic est calix novum testamentum in meo sanguine. Evangelium autem Apostoli I. Cor. XI°, 25 habet simpliciter: Hic calix novum testamentum est in meo sanguine, ubi patet primo quod accipitur methonomatice contentum pro continente. Et patet secundo quod loquitur figurative et non ydemptice, quando dicit quod calix est novum testamentum, ut vel sic manuducamur ad intelligendum sensum verborum quibus eukaristia est confecta; unde Math. XXVI°, 28 sic loquitur: Hic est sanguis meus novi testamenti. Et eandem seriem habet Marc. XIV°, 24, ubi utrobique demonstratur vinum in calice; et sic verborum istorum quatuor evangelistarum diversitas plena est misterio.

[ENGLISH]

## ¶4 · 97.29–98.14

> [p. 97] Et patet tercio quod non obest sed consonat, ut dicit decretalis Cum Marthe, quod in hoc sacramento [p. 98] sint simul veritas et figura; sacramentum enim figurat Christum et unionem cum ipso atque ecclesia; et vere facit atque figurat presenciam Christi sacramentalem ultra figuras alias. Unde sicut vane convincitur heresis super hoc quod Christus est creatura, quia Arrius illud dixit, sic nude et stulte arguitur sentenciam illam esse hereticam que dicit locucionem istam esse tropicam: Hoc est corpus meum, et quod illa hostia est figura ex hoc quod heretici illud dicunt. Illi enim non attendunt ad modum ac intencionem dicendi cum aliis superadditis, sed ad veritatem quam fatetur omnis hereticus quam diffamant, et tamen scitur quod in moribus est modus operis maxime attendendus.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 94.29: In case of weakness or other need we may communicate after eating.
- 95.8: Objection: Christ blessed the bread before He used the words of consecration.
- 95.15: This blessing was (as Luke and Paul say) a giving of thanks.
- 96.9: Why the evangelists vary in reporting Christ's words.
- 97.29: In the sacrament are both truth and figure.
- 98.4: It does not follow that language is heretical, because it has been used by a heretic.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 97: *Christi* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 94:
1. E: accipimus. 4. ABD : meus prepostere ; C: modo prepostere.
10. B: et ritus. 12. B: totaliter traditor. 14. DE: sed imitacionem;
14. D: aut quo. 16, 17. AB: quare secundum hunc ordinem Christus.
18. E: primum; ib. C in marg. alia manu: esum. 20. D: in imitacione.
22. AB: varietatem; C correxit. 20. D: excipiatur. 3i. C: devotus

p. 95:
5. C: prandendo. 9. E: narrat. 12. D: pre ceteris verba.
i3, 14. ABCE: aliter — consecralam deest. i5. D : in dcest.
17. ABD : racionalis deest; C in marg. alia manu add.; ib. E: Et inde.
19. D: dicunt deest. 22. AB : nostris dcest; C addit in marg.
24. E: et quoad. 25. Codd.: progeniture. 28. ABCE: et errare.
29. D : non suo. 3o. ABE : insequerentur.
q. Matth. XXVI, 26.

p. 96:
2. AB: el aliqui; C corr. alii. 3. AB: calore et deest; C in marg.
alia manu addit. 4. D : dispersi. 8. ABCD: Omelia XXVIII.
ii. E: qualiter. i3. DE: istos. 24. D: ad exercicium ; C: sit guida.
25. D : alia. 3o. AB : crede.
8. S. Chrysostomi Opus Imperfectum in Matthaeum Opp.
tom. VI (ed. Paris. altera), pag. 785.

p. 97:
I, 2. C: in lege — effundi in marg. i. 13: in iestamento. 7. ABC;
testimonium. 9. E : sic deest. 16. AB: /. Cor. VI. 17. E: Hoc
novum. Codd.: calix decst. Addidi. 19. AP>: methavorice ; C in tcxlu
methaforice ; in marg. alia manu: metanomatice. 10, 20. ABC: patet
tercio. 20. D: legitur. 29. B: Et placet.
II. Zach. IX, 11. 3o. Decr. Gregor. IX, lib. III, titul. XLT,
De Celebratione Missarum, cap. VI.

p. 98:
6. CE: dixit illud; ib. B: sicut. 8. C: et in marg. alia manu.
l3. D: intelligitur. iG. DE: posset confici; ib. C: potest; ib. D: perfici.
18. E: et a-{imis. 24, 25. ABCD : quod est ostendit se. 25. D: aliud
quod.
3i. Cf. Wyclif, De Ecclesia, pag. 457.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 95: accepit panem, benedixit | \ofregit et dixit: Acapite et comedite, hoc est corpus | gracias agens fregit,
```
