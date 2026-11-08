# Translation brief: eucharistia 02-c–02-e

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/eucharistia/wyc-eucharistia-02-c.md chunks/eucharistia/wyc-eucharistia-02-d.md chunks/eucharistia/wyc-eucharistia-02-e.md` once and fix what it reports.
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

## Glossary (the 469 rows these chunks use; the full file is GLOSSARY.md)

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
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |
| sacramentum (the eucharist); sacramentum altaris | sacrament; the sacrament of the altar | The plain sense, against the Augustinian row (*Incarn.*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.3, 3.30). |
| hostia; hostia consecrata | host; consecrated host | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.11, 1.22). |
| panis / vinum | bread / wine | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.8). |
| calix | chalice | The Douay word (1 Cor. 10:16). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.3). |
| corpus Christi / corpus Domini | the body of Christ / the body of the Lord | Kept apart as the Latin alternates them. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.6, 1.10). |
| novella ecclesia / antiqua ecclesia | the newer church / the ancient church | The pair of 3.3; cf. *novelli*. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 3.3). |
| cultores accidencium / signorum | worshippers of accidents / of signs | Wyclif's name for the defenders of the accident without a subject. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 6.15, prol-c 10.2). |
| cognacio (Christi cum membris) | kinship | With those who do the Father's will (Matt 12:50; 314.21–22). Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-c 10.11). |
| species (of bread and wine) | species | The sacramental species; kept as the term, not "appearance". Distinct from the logical *species*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 13.15; 23.8). |
| sacer; sacrare | sacred; hallow | Kept apart from *sanctus / sanctificare* "holy / sanctify" and from *consecrare*; *consecrare* is "to hallow together" in the grammarians' etymology. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 27–28). |
| sacramentum tantum | a sacrament only | The *sacramentum tantum* of the Lombard's three (IV d. 8 c. 4). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 29.23). |

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
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| castra caynitica | Caim's castles | The friars' houses; the Wycliffite English name (CAIM = the four mendicant orders' initials). Ruled 2026-09-28 (coordinator, delegated). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| vulgares | the common people | The third estate. Not "the vulgar". Pilot. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| insolubilia | insolubles | The logicians' paradoxes of self-reference. Ruled 2026-10-02 (*Eccl.* 175.11). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |
| autenticus / autenticacio | authentic / authentication | The key term of *Eccl.* 13. Ruled 2026-10-02. |
| decretum; decreta | decree; the decrees | Gratian (*in decretis*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.14, 3.24). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| practizare | to put into practice | Ruled 2026-09-28 (coordinator, delegated) (4 sites). With *contra* + person, "practise against" (plot), *Dial.* ch. 17. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| simpliciter / secundum quid | **without qualification / in a certain respect** | ⛔ Always opposable. Never "simply", "wholly", "directly", "naturally" etc. (T. p. 364). |
| necessitas supposicionis / ex supposicione | necessity of supposition / necessity on supposition | Conditional necessity. Pilot (*Eccl.* 3.21); *ex supposicione* ruled 2026-10-02 (34.12, 38.22). |
| de congruo / de condigno | by congruity / by condignity | Pilot. |
| contingens ad utrumlibet | contingent either way | T. p. 364. |
| consequencia | inference | ⛔ Not "consequence" (T. p. 361 n. 13). |
| consequens / antecedens | consequent / antecedent | |
| propositio copulativa / disiunctiva | conjunction / disjunction | Not "copulative proposition" (T. p. 365). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| influxus / influere | inflow / flow in | The head's inflow of grace into the members; not "influence" (which renders *influencia*). Ruled 2026-10-02 (33–34). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| penaliter | in hardship | The adverb of *penalitas*. Ruled 2026-10-02 (76.29, 76.34). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| dulia / latria | dulia / latria | Kept as the theologians' terms, glossed once per chunk. Ruled 2026-10-02 (95.17). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| indispensabilis | not to be dispensed | Ruled 2026-10-02. |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |
| dimittere / dimissio (*naturam*) | lay aside / the laying-aside | Letting go the assumed nature, so the union would be dissolved. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 2.23). |
| assumere / assumpcio (*naturam*) | assume / assumption | Of the nature, as in the fathers. ⚠ Kept apart from the logician's *assumptum* "the assumption" (above): C note where the logical sense occurs. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| ydemptitas specifica | identity of species | That Christ and other men are of one species. Not "specific identity" (reads as "particular"). Ruled 2026-10-22 (Wilson; *Incarn.* prol, 8). |
| Verbum | the Word | Pronoun **"he"** (as Douay–Rheims John 1:3, "by him"), never "it", though the Latin is neuter; so also *Sapiencia* where Wisdom is the Word in person (*Incarn.* 7, coordinator). Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.3–4). |
| secundum quod (reduplicative) | insofar as | ⛔ Never "in that" (heard as "because", which inverts the logic). Ruled 2026-10-22 (Wilson; *Incarn.* 5.29–6.24). |
| secundum deitatem / secundum humanitatem | as to the Godhead / as to the humanity | The rule of reduplication; keep it in Wyclif's place in the sentence. ⛔ Never supply "as God / as man" where the Latin has bare apposition (*ipse Deus*) or bare predication. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| natura | nature | Ruled 2026-10-22 (Wilson; *Incarn.* 3.4). |
| persona | person | Ruled 2026-10-22 (Wilson; *Incarn.* 4.14). |
| creatura / creator / creatus | creature / creator / created | ⛔ Never "creation" for the created thing. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| posicio / proposicio / predicacio | position / proposition / predication | Kept apart: the apparatus shows the three trading places (*Incarn.* 4.15). Ruled 2026-10-22 (Wilson). |
| sacramentum (of the incarnation, of creation) | sacrament | The Augustinian sense, "mystery" (1 Tim. 3:16): G note at the first occurrence in the chunk. Kept apart from *misterium*. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.8). |
| misterium | mystery | Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.3). |
| moderni doctores / moderniores doctores | the modern doctors / the more modern doctors | Ockham and the *moderni*, usually unnamed. Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.1). |
| sancti | the saints | The fathers. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.15). |
| ypostatice | hypostatically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 12.2). |
| ypostaticus | hypostatic | *Unio ypostatica* "the hypostatic union". Ruled 2026-10-23 (coordinator, close-out review; *Incarn.* 220.23). |
| novelli | the newer [doctors] | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 13.7). |
| Sermo (beside *Verbum*) | Speech | The divine title, capitalised; *Verbum* stays "the Word". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 16–17). |
| sophistice | sophistically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 15). |
| de vi vocis / de vi sermonis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| gracia unionis | the grace of union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| humiliacio | humbling | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26–28). |
| suppositum | supposit | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 34.24). |
| in quantum (reduplicative) | insofar as | As *secundum quod*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37.9). |
| unio | union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 39). |
| diccio (logical) | word | A single term in a proposition. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 43.3). |
| intransitive | intransitively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 45.28). |
| in effectu | in actual fact | As against in potency or in name; ⛔ not "in effect" (modern "virtually"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 47.10). |
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
| proditor | the traitor | Judas. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 64.3). |
| dampnificare / dampnificacio | damage / damaging | Kept apart from *dampnum* "loss" and *dampnari* "be damned"; the argument of 65–68 turns on it. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 65). |
| per se / per accidens | of itself / by accident | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a (sufficienti) divisione | the topic from sufficient likeness / from (sufficient) division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| pretericio | being past | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| solvere / solucio (of the union) | loose / loosing | Except inside a Douay quotation (John 10:35 "cannot be broken"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| libere contradictorie | freely, as between contradictories | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 76.15). |
| ypostasis | hypostasis | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| insolubilitas | inextricability | As *insolubiliter*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| peccabilis | able to sin | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| medium (logical) | middle term | Of a syllogism; elsewhere "means" by context. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| ydemptitas ypostatica | hypostatic identity | Beside *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 84.20). |
| passionatus | subject to passion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| intricaciones sophistice | sophistical entanglements | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 82). |
| eiusdem / consimilis / alterius racionis | of the same / like / another kind | The species-sense of *racio*; *racio speciei* "the account of the species" (Aristotle's *logos*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.4, 87.17). |
| principiari | be constituted from principles | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.7). |
| accidentatus | subject to accidents | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.4). |
| in recto / in obliquo | in the direct case / in an oblique case | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.25). |
| passibilis | passible | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.12). |
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
| sermo vocalis | the spoken word | Against *Sermo* "Speech", the divine title. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 113). |
| predicacio secundum essenciam / formalis | predication by essence / formal predication | Wyclif's modes of predication (cf. *predicacio secundum causam*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 115–116). |
| forma substancialis | substantial form | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| exclusiva | the exclusive [proposition] | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 116–117). |
| concepcio (figure) | conception | The grammatical figure. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| accidens | accident | The category; *accidit* "befalls". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| figura / figuratum | figure / thing figured | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 121.23). |
| incepcio | beginning | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 121.16). |
| conversio (of a proposition) | conversion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.30). |
| racio (individual, personal) | account | *Racio individui / persone* "the account of an individual / a person", as *racio speciei*; not "aspect" (the row against *substancia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 8, 129–132). |
| vir (against *homo*) | man (*vir*) | Where Wyclif sets *vir* against *homo*, the Latin in parentheses. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 129.15–26). |
| exemplaria / exemplata | exemplars / things exemplified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.6). |
| res secunde intencionis | things of second intention | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.25). |
| materia proxima / remota | proximate / remote matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137.1). |
| personari | be made a person | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 134.10). |
| ydemptificare / ydemptificacio | identify / identification | Make the same (*idem*); the hypostatic union as identification, not conversion or generation. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 142.19, 147.22). |
| res communis / res communes | the common thing / common things | The realist universal the *moderni* do not conceive (first root of their error). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 144.27). |
| distinccio racionis | distinction of reason | Beside *differencia formalis*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 145.23). |
| conversio naturarum / confusio naturarum | conversion of the natures / confusion of the natures | Kept apart from *conversio* of a proposition. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 143.9). |
| moderni (bare) | the moderns | Beside *moderni doctores* "the modern doctors". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 142.10). |
| principiare (active) | be the principle of | Beside the passive *principiari* "be constituted from principles". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 147.4). |
| assumere personale | personal assuming | The infinitive used as a noun; kept apart from *assumpcio personalis* "personal assumption". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 146.33). |
| moderniores (bare) | the more modern | Beside *moderniores doctores* "the more modern doctors". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 151.17). |
| supposicio simplex / supposicio personalis | simple supposition / personal supposition | Supposition theory. *Simpliciter / personaliter supponere* "stand with simple / personal supposition": NOT the *simpliciter / secundum quid* pair, C note where the two could be confused. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 152.5–12). |
| transsumpcio | transumption | Beside *transsumptive*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 153.28). |
| filiacio | sonship | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 154–155). |
| personalitas | personality | The scholastic term: what makes a person a person, not character. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 155). |
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
| multiplicacio dimensionalis | dimensional multiplication | One body in several places by its dimensions. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.6). |
| proporcio racionalis | rational proportion | The mathematical ratio. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 207.7). |
| a maiori vel pari | from the greater or from the equal | Arguments *a maiori*; cf. *locus a maiori*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 209.5). |
| sensibile commune | common sensible | Aristotle's common sensibles (number, motion, figure); the term of art, against the §D row "perceptible". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 209.23). |
| mocio progressiva / motus progressivus | progressive motion | Locomotion. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 205.28). |
| multiplicacio concomitancie | multiplication of concomitance | Cf. *gracia concomitancie*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 213.21). |
| superioritas / inferioritas terminorum | superiority / inferiority of terms | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 215). |
| exponentes | the exponents | The propositions into which a proposition is resolved (expounded). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 216.14). |
| moderni loquentes | the modern speakers | Beside *moderniores loquentes*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 221.20). |
| bonum de genere | good in its kind | Moral goodness by the kind of act. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 228.16). |
| signum reduplicatum | the reduplicated sign | The reduplicative word (*secundum quod*, *in quantum*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 230.23). |
| supposicio | supposition | Of a term (supposition theory) or of a premiss laid down (cf. *supponitur* "it is supposed"); the English word serves both, C note where it matters. Kept apart from *suppositacio* "suppositation". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 102.8). |
| lex proximitatis | the law of neighbourhood | The duty to love one's neighbour (*proximus*). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 101.29). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |
| infirmitas (of Christ's flesh) | weakness | Ruled 2026-10-22 (Wilson; *Incarn.* 5.31–6.11). |
| sacramentaliter | sacramentally | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| vere | truly | A mode adverb: one word each, never two merged, kept where Wyclif puts it. ⛔ Never "really" (that is *realiter*). Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| spiritualiter | spiritually | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| virtualiter | virtually | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| figurative | figuratively | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
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
| locucio tropica | tropical speech | With *predicacio tropica* "tropical predication". Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 4.26). |
| Doctor Communis | the Common Doctor | Thomas; with *Doctor Subtilis*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 8.16). |
| multitudo (of one body) | multitude | Of one body's being many (ch. 8); the plain "multitude" of persons needs no row. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 8.4). |
| sensus communis | the common sense | The inner faculty; kept apart from *sensibile commune* "common sensible". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 18.31). |
| figurare | figure | Both senses: to prefigure (the lamb figured Christ) and to shape (*figurare Deum nostrum*), which Wyclif plays on; one English word keeps the pun. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-c 10; 21.29). |
| supponere pro | stand for | Supposition; with *supposicio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 24.27). |
| sensualiter | sensually | Berengar's oath word (*Ego Berengarius*); kept apart from *sensibiliter* "perceptibly". A mode adverb, one word. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 26.1, 30.24). |
| sentire (an opinion: sensit quod) | hold | Of a doctor's or church's opinion; the "perceive" row is the sacrament sensed. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 30.30, 31.18). |
| predicacio figurativa | figurative predication | A synonym of *predicacio tropica*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 35.18). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| perplexus | perplexed | The moral-theology sense: bound to sin whichever way one turns. Ruled 2026-09-28. |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| indispositus; (se) indisponere | unfit; to make (oneself) unfit | "indisposed" (now "unwell"). Ruled 2026-09-28 (8 sites). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| penalitas | hardship | "penalty". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| redempcio temporalium | redemption of the temporal goods | Chapters buying back seized goods. Ruled 2026-10-02 (*Eccl.* 15, 340.15). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| redempcio (of a sentence) | redemption | Buying off a penalty; kept apart from *redempcio temporalium*. C note at first use. Ruled 2026-10-02 (*Eccl.* 15, 352.1). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| dotes (docium) beatorum; dotes corporis | the dowries of the blessed; the dowries of the body | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| falsarius | falsifier | The opponent's epithet. Ruled 2026-10-02 (*Eccl.* 17, 414.6). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| quadriga diaboli | the devil's four-horse chariot | Ruled 2026-10-02 (*Eccl.* 18, 427.12). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| continuacio (of bodies, the act) / discontinuacio; continuare / discontinuare | continuation / discontinuation; make continuous / make discontinuous | The making of several bodies into one continuum (*Incarn.* ch. 12), G note at first use: not "carrying on". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.30, 211.12). |
| precaria | precarial grant | Wyclif defines it (*Eccl.* 453.21). Ruled 2026-10-02 (*Eccl.* 19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| indisposicio | unfitness | Noun of *indispositus*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| perplexitas | perplexity | The noun beside *perplexus* "perplexed". Ruled 2026-10-02 (*Eccl.* 19, 470.3). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| dampnacio | CONTEXTUAL: damnation / condemnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). Of a judgement passed on a teaching (*dampnacio istius sentencie tamquam heretice*, *Pot. pape* 84.10) "condemnation"; ruled 2026-10-07. |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
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
| venia | forgiveness | Kept apart from *condonacio* "pardon". Ruled 2026-10-02 (*Eccl.* 23, 573.4). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| remissio; remittere | remission; to remit | Headword row (cf. *condonacio* "pardon", *venia* "forgiveness"). Ruled 2026-10-02 (*Eccl.* 23). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). Beside *consecrare* (*consecrat et conficit*) "confect", so the pair stays two. Ruled 2026-11-07 (Wilson, "confect works"; *Euch.* 16.10). |
| licencia | licence | Permission granted; never "power". Wyclif usually sets it against *potestas*, but can also identify the two where power is defined as a grant (*illa licencia est potestas*, *Pot. pape* 21.29): render "licence" either way and let the argument show which. Ruled 2026-10-07 (*Pot. pape* 41.21); qualified 2026-10-12 (close-out R1).|
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| procuratoria potestas | proctorial power | From *procurator* "proctor". Ruled 2026-10-07 (*Pot. pape* 63.9). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| trahere in consequenciam | draw into a precedent | The legal idiom; *consequencia* stays "inference". Ruled 2026-10-07 (*Pot. pape* 94.13). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| influencia (celestis) | (celestial) influence | Astrological sense. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 172.1). |
| quaternarius / denarius / quadragenarius | the four / the ten / the forty | Number exegesis (the 153 fishes, ch. 7). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 154–155). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| memorativa potencia | memorative power | A faculty of the soul (the "power" sense of *potencia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 219.27). |
| primicia (virtutum) | being first (in the virtues) | Kept apart from *primatus* "primacy" and *primitas* "firstness". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 228.33). |
| replicatur; replicatum | it is rejoined; rejoinder | A further objection against an answer; kept apart from *respondetur* "the reply is" (so 04-b). Ruled 2026-10-08 (coordinator, delegated; conformed 10-e, 10-g). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| malum culpe / pene | the evil of fault / of penalty | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.19). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| summus sacerdos | high priest | DR; kept apart from *summus pontifex* "highest pontiff". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 265.20). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| summum sacerdocium | high priesthood | Cf. *summus sacerdos* "high priest". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-c, 11-d). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| penalis | hard, of hardship | Beside *penalitas*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 280.20). |
| demereri | to demerit | Ruled 2026-10-02 (*Eccl.* 23). |
| correptibilis | open to reproof | Beside *corripere* "reprove". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 301.3). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| remisse (of assent) | with slackened [assent] | Opposed to full assent in the degrees of belief. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 328.18). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| procuratorium | proctor's mandate | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 336.11). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| provisio (papal) | provision | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* ch. 12). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |
| diccio procuratoria | proctorial pronouncement | C note gives *dicio* "authority" as the alternative. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 386). |
| specularis prudencia | the prudence of a watchman | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| insolubiliter | inextricably | Kept apart from *insolubilia* "insolubles". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 404). |
| nimis | exceedingly | Medieval intensive (= *valde*); "too much" only where excess is the point. Ruled 2026-10-12 (close-out R2; *Pot. pape* 169.2). |
| sentire (the sacrament, the body) | perceive | "sense". As *sensibilis* "perceptible". Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.10, 1.17). |
| postponere | set aside | "put after". Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 4.8). |
| recitare | recite | To report, rehearse. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.4, 3.10, 4.18). |
| narrare | relate | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.9). |

---

## Chunk 02-c: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-02-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-02-c
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "36.24–40.26"
divisions: "cap. 2 (heading 'CAPITULUM SECUNDUM.' at 29.0); part 3 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "954 words; 930 confirmed by the vote; 12 runs stood by rule; 12 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n107–n111 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 2, part 3: [TITLE]

## ¶1 · 36.24–38.21

> [p. 36] Secundum exemplum est illud Apoc. XIXº, 8: Byssinum enim iustificaciones sunt sanctorum, ut alias diffuse exposui; et tercium exemplum est illud I. Cor. XIº, 25: Hic calix novum testamentum est in meo sanguine; figuravit enim vinum in calice novum testamentum, sicut sanguis vituli fuit signum confirmacionis veteris testamenti, ut patet Exod. XXXIVº. Sic igitur videtur sanctos ecclesie primitive et suos filios post eos intelligere per panem et vinum figurative corpus Christi et sanguinem. Unde Iª Cor. XIº, 21 narrans Apostolus quomodo Corinthi conveniebant ad manducandum cenam dominicam [p. 37] unoquoque portante secum proprium panem et vinum, sic quod unus fuit ebrius et alius esuriens post hanc cenam, increpat eos leniter in hoc facto et addit instruccionem quoad hoc sacramentum, que tunc suffecit ecclesie; videlicet quod conveniant manducantes in ecclesia ordinate vel aliter domi infirmi manducent nec alii darent scandalum fratribus in copiosis, in sumptuosis et in deliciosis preparacionibus panis et vini. Unde pro plena instruccione quoad hoc sacramentum sic loquitur: Ego enim accepi a Domino quod et tradidi vobis; quoniam dominus Jesus in qua nocte tradebatur accepit panem et gracias agens fregit et dixit: Accipite et manducate, hoc est corpus meum quod pro vobis tradetur, hoc facite in meam commemoracionem. Quocienscunque, inquit, manducabitis panem hunc et calicem bibetis, mortem Domini annunciabitis donec veniat; ubi patet quod loquitur quadrupliciter de pane et vino materiali et per consequens dicit hoc esse corpus eius et sanguinem in figura, sicut dicit hunc calicem esse novum testamentum et hoc fieri in eius commemoracionem. Quod autem alii dicuntur in medio prandii accipere instar Christi hostiam a sacerdotibus consecratam, videtur esse sompnium, sed sacramenta et ritus adiecti videntur michi esse racionabiles, sic tamen quod non sint nimium ponderati. Aliqui enim stulte plus ponderant ritus adiectos quam sentenciam Apostoli, dum sic dicit: Itaque quicunque manducaverit panem hunc vel biberit calicem Domini indigne, reus erit corporis [p. 38] et sanguinis Domini. Intelligit enim quod panis et vinum non debent sumi in memoriam corporis Christi et sanguinis nisi digne, hoc est, nisi mundo corde et pura intencione; et sic videtur michi quod nulli ritus honesti de Eukaristia debent contempni nec plus virtutibus ponderari; et utrobique videtur quod scriptura vocat hoc sacramentum panem et vinum, quomodo quidam intelligunt illud Act. IIº, 46 quod dicitur de conversis: Cotidie autem perdurantes unanimiter in templo et frangentes circa domos panem sumebant cibum cum exultacione et simplicitate cordis. Panis itaque vocatur utrobique hoc venerabile sacramentum; quod si sit verum, patet cum paribus quod graviter peccaverunt qui onerarunt ecclesiam tam speculative quam practice tot perplexitatibus quibus difficultatur circa hoc sacramentum. Manet ergo iuxta sentenciam ecclesie in Beringario, iuxta sanctos doctores et formam verborum scripture tam panis quam vinum post benediccionem et sacramentum et corpus Christi in signo et non in essencia quod sic frangitur et tractatur.

[ENGLISH]

## ¶2 · 38.22–38.29

> [p. 38] Et patet solucio obiectus quo dicitur sentenciam ecclesie in Beringario contradicere sentencie supradicte, sed replicatur secundo per hoc quod scriptura sacra in sex locis predictis vocat sacramentum Eukaristie panem, et idem dicunt sancti doctores cum decreto ecclesie in Beringario. Quare ergo non teneremus nos eandem loycam, cum non licet in materia fidei secundum loycam variare?

[ENGLISH]

## ¶3 · 38.30–40.3

> [p. 38] Hic dicitur quod sensus supradictus est satis equivocus et vulgo satis extraneus ac occasio unde multi accipiunt fidem ad credendum panem et vinum post [p. 39] consecracionem esse ydemptice corpus Christi et sanguinem: ideo sicut ecclesia variavit in aliis accidentalibus preter fidem, sic debet ex causa variare in loyca stante sentencia et sic fide. Variarunt enim observanciam sabbati a feria septima usque ad feriam quintam et abhinc usque ad feriam primam, quod hodie observat ecclesia stante fide non variata, et ita de multis similibus preter fidem; quare ergo non licet ecclesie variare in loyca, servando fidem et obserando infidelitatis aditum, sicut custos castri ex causa racionabili mutat portas, nec hoc licet nisi cum sufficienti ac racionabili decreto custodum. Aliqua ergo sunt loca in quibus expedit variare in loyca propter periculum evitandum et aliqua sunt loca in quibus non convenit variare; et patet quod non oportet, si sancti doctores ecclesie katholice sic locuntur, tunc licet cuilibet katholico ita loqui, ut beatus Bernhardus in sermone De Exaltacione sancte crucis, qui sic incipit De virga Jesse sic loquitur: Manus ille que fundaverunt celos extense sunt in cruce. Et multa similia dicunt iste sanctus et usus ecclesie que non sunt nobis generaliter trahendi in consequenciam, quia nec manus corporales Christi eterne fuerant crucifixe nec manus spirituales que sunt potencia operandi; nam manus corporales non habuit antequam fuerat incarnatus, quia tunc fuisset Deus corpus antequam fuit mundus, nec manus spirituales, quia omnes ille sunt divina essencia, et sic Trinitas que non potest extendi vel pati nisi incidatur in heresim [p. 40] Patripassianorum, quos Augustinus recitat in libro suo de heresibus dixisse naturam divinam et per consequens patrem pati.

[ENGLISH]

## ¶4 · 40.4–40.11

> [p. 40] Cum enim hec predicacio sit formalis, manus eterne Dei erant passe in cruce, patet quod consequenter concedi oportet quod virtus ymmo digitus Dei qui est Spiritus Sanctus extendebatur et paciebatur, et sic natura increata, potencia, virtus et bonitas, raciones exemplares et ydee forent palpabiles, et sic foret confusio personarum et naturarum, cum omnis natura foret sensibilis.

[ENGLISH]

## ¶5 · 40.12–40.26

> [p. 40] Item, si ex auctoritate scripture licet huiusmodi conclusiones extorquere, per idem concedendum foret quod Deus ante mundi constitucionem et sic eternaliter infinitum plus in corde de valde bono doluit quam dolere potuit aliqua creatura, quia Genes. VIº, 6 dicitur quod Deus tactus dolore cordis intrinsecus dixit quod penituit eum fecisse hominem; et sic habuisset infinita membra infinite et eternaliter dolorosa; nam sicut eternaliter novit peccatum hominis, sic eternaliter in corde doluit de eodem, quia in corde tactus fuit dolore; et cum per cor intelligitur Deus Pater iuxta illud Psalmi XLIVº, 2: Eructavit cor meum verbum bonum, videtur quod eternaliter doluit Deus Pater; et constat quod nulla creatura potest parificari sibi in dolore, sicut nec in noticia vel affeccione.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 38.30: Errors introduced by use of tropical language.
- 39.16: Example from a phrase of St. Bernard,
- 40.12: Example from Scripture.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 36: *Apoc.* (print = bt) [SUB]
  - 36: *Byssinum* (print = bt) [SUB]
  - 36: *exemplum est illud* (print = bt) [BT-ONLY]
  - 36: *testamentum est* (print = bt) [BT-ONLY]
  - 36: *et sanguinem.* (print = bt) [BT-ONLY]
  - 36: *Iª* (print = bt) [SUB]
  - 36: *cenam dominicam* (print = bt) [BT-ONLY]
  - 37: *nocte* (print = bt) [SUB]
  - 37: *fregit* (print = bt) [SUB]
  - 38: *et* (print = bt) [SUB]
  - 39: *sancti* (print = bt) [SUB]
  - 40: *6* (print = bt) [BT-ONLY]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Exodi XVII0, 6), (36.11); reference Apoc. XIX0, 8: (36.24).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 36:
8 D: si itinerantibus; ib.C: de Egypto
ib. C: Christum decst. 3i. D : Exod. XXIV.

p. 37:
2. AB: ebrius aller esurie?is; C: et alter. 8. BE: et deesl; ib. 1) :
in omitted before deliciosis. i3. C: fregit in tnarg. alia manu;
ib. C: comedite ; superscriptum : manducate. i3— 15. C: Hoc est —
commemoracionem in marg. alia manu. i5. ABC: Quociens. 16. ABCD:
manducate ; E: manducaveritis ; ib. E: biberitis. 19. E: eius deest.
22. AC: dicunt cor? ; B: dicunteorum; D : dicunt Corinthii; E: Corinthios.
Correxi. 27, 28. ABC : cum sic. 28. Codd.: panem hunc deest. Addidi.
10. I. Cor. XI, 23, 24, 26. 28. I. Cor. XI, 27.

p. 38:
2. A: swnmi. 3. A: nec digne. 7. ABC: esse panem. 8. B: qui-
dcm; C: quique. 9, 10. ABCI) : quo dicitur ; E: quod dicitur dccst.
17. 15: circa sentenciam. 20. E: non in cena. 22. ABE : solvendo
obiectus; C : solvend» crased et corr. 24. AB : secundo dccst. 3o. DE:
predictus. 3i. AB: ac ecclcsie unde.

p. 39:
additum. 12. E: custodis. i5, 16. A15 : sic sancti. 16. ACE: doctores
cciam katholice; B: ecclesie dccst. 17. ABCD: catliolice. 18. C: qui
in marg. alia manu. uj. Di De dccst. 24. E: polencie. 28. C: ille
in marg. alia manu.
19. Rectius (ut videtur): De duobus discipulis cuntibus in
Emaus. Cf. Opp., pag. i555.

p. 40:
1. E: recita. 5. C: Dei in marg. alia manu. 6. D : concedendum;
ib. C: concedi debet ; ib. AB : ymmo decst. 7. E: sic dcest. 8, 9. A:
raciones exemplares in marg. alia mann. 16. D : alia creatura ; ib. D : de VI.
17. AB : dixit deest; C in marg. alia manu; E: dixit quod penituisset.
19, 20. ABCD : si eternaliter. 23. C: meum videtur; bonum deest.
1. In libro S. Augustini De Haeresibus hic locus non extat.
Cf. Sermon LII. De verb. evang. Matth. III, Opp. tom. V, 1, 304:
Excidit nobis quosdam male intelligentes vocari Patripassianos,
qui dicunt ipsum Patrem natum ex femina, ipsum Patrem
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 36: erat Christus, | Byssinum enim iustificaciones sunt sanctorum, | Hic calix novum testamentum est in meo sanguine; | AC: preterquam; | filios posterwres. | vobis quod ante verba Christi quod offertur panis | dicatur, sed cum verba Christi deprompta fuerint, i$ iam non panis dicitur sed corpus appellatur. | Sacramentum quidem pene omnes corpus Christi dicunt. | esse in similitudinem carnis peccati et nunc dicitur peccatum. Solet, | similitudo capere nomen rei cuius est similitudo, | elicere ars actus. | que offertur. | corpus esse dicunt.
p. 37: alius esuriens | Ego enim accepi a Domino quod et tradidi vobis; quoniam dominus Jcsus in qua nocte tradebatur accepit panem et gracias agens fregit et dixit: Accipite et manducate, hoc est corpus meum quod pro vobis tradetur, Iwc facite in xbmeam commemoracionem. Quocienscunque, | manducabitis panem hunc et calicem bibetis, mortcm Domini annunciabitis donec veniat; | Itaque quicunque manducaverit panem hunc vel biberit calicem Domini indigfie, reus erit corporis | posicio que ponit substanciam panis remanere simul cum corpore Christi est incompctens, inpossibilis et heretica. Incompetens | qnidem, quia impediret veneracionem debitam huic sacramento. Ksset enim ydolatrie occasio, sisubstancia panis ibi remaneret. Esset eciam contra signijicacionem sacramenti, quia species que inducerent in verum corpus Christi signijicarent magis substanciam panis. | Esset tercio contraria huic sacramento, quia cibus iste non esset pure spiritualis sed eciam corporalis. Et quod sit inpossibilis, patet quia inpossibile est aliquid esse nunc, ubi prius non fuit nisi ipso mutato vel alio in ipsum converso; non enim posset eciam per | miraculum fieri quod esset animal racionale, mortale et non esset homo; sic ergo corpus Christi non posset aliter se habere nunc quam prius, nisi interveniat mutacio] cum ergo ex parte panis non | pono que. | remaneret eciam. | quia species non ducerent in verum corpus Christi per modum signi sed magis in substanciam panis. | Et tercio. | nisi id. | eciam per | Aliter enim se haberet nunc et prius, est idem quod moveri vel transmutari. Si ergo corpus Christi
p. 38: Cotidie autem perdurantes unanimiter in templo et frangentes circa domos | panem sumebant cibum cum exultacione et simplicitate cordis. | sa{ls | faret mutacio, nec cx parte corporis Christi, quia sic idem corpus moveretur simul et semel ad diversa loca, quod est inpossibile, cum tunc motus contrarii inessent simul eidem. Quod autem sit heretica y patet ex hot quod con- | tradicit veritati scripture. Non enim esset verum dicere: Hoc est corpus meum, sed hic est corpus meum. | sic fabule; | sed coram: | ut pio. | in eternum; | quod pius tam sanctus. | cum stultum. | alios in hoc | in hoc fuit.
p. 39: Manus ille que zofundaverunt celos extense sunt in cruce. | sit propterea. 6. | istud assumptum | de multis. \\. | ut multum; | subditos dolos.
p. 40: penituit eum fecisse hominem; | Eructavit cor meum verbum | Excidit nobis quosdam male intelligentes vocari Patripassianos, qui dicunt ipsum Patrem natum ex femina, ipsum Patrem passum | Omnia quecunque, | sicut fedati; | heretici heretica. | tamen reputant; | quam nisi. | Similiter decretum. | ibi quecunque.
```

---

## Chunk 02-d: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-02-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-02-d
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "40.27–43.29"
divisions: "cap. 2 (heading 'CAPITULUM SECUNDUM.' at 29.0); part 4 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "639 words; 633 confirmed by the vote; 4 runs stood by rule; 2 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n111–n114 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 2, part 4: [TITLE]

## ¶1 · 40.27–41.16

> [p. 40] Et quantum ad infinitatem membrorum, ut manuum, digitorum vel talium que preter personalitatem [p. 41] in Deo dicunt raciones exemplares, videtur quod non est numerus istorum, sicut non est finitus numerus omnium ydearum. Et istud considerarent canoniste qui in vulgari predicant laycis quod ille manus quibus formavit Deus celum et terram fuerant crucifixe; addiscerent, inquam, primo quot manus huiusmodi habet Deus et si manus sinistra Dei fuit in mundi inicio aliquid operata, ad excludendum Manicheos qui posuerunt Deum malum. Et infinite sunt conclusiones huiusmodi, quibus nimis oneraretur ecclesia a sophistis infidelibus, si omnia dicta figurativa scripture debent generaliter trahi in consequenciam, ut alii in toto libere loquantur conformiter; oportet ergo nos loqui plane interpretando figuras et reservando illis formas loquendi autenticas, ut docet Augustinus IVᵒ De Doctrina Christiana.

[ENGLISH]

## ¶2 · 41.17–42.7

> [p. 41] Sed tercio replicatur contra dicta per hoc quod non docetur que scriptura debet admitti et que abnui, nec in quo doctor est tenendus et in quo negandus. Ymmo videtur quod ecclesia tempore Beringarii fuit heretica vel aliter infidelis fuit ecclesia sequens illi contraria. Hic dico quod tota scriptura sacra debet admitti ut fides et detestari eius falsitas, cum ex integro sit vera et in nulla parte falsa, ut hic supponitur. Figurativas autem locuciones scripture debemus exponere et modo discipulorum dimissis figuris nostris auctoribus loqui plane. Unde solebam exponere predictam scripturam Genes. VIᵒ, ubi notato textu solebam dicere, quomodo minus bene intelligentibus textus iste videtur pretendere quod Deus prius ignorans peccatum hominum futurum, postquam in facto [p. 42] didicit hominem ex pronitate sic peccare, doluit et displicuit sibi vel quod unquam fecit hominem, vel quod fecit hominem tam fragilem; sed quod fecisset eum constantem et confirmatum ut angelum, quia tunc caruisset occupacione penali in castigando eum pro delicto; sed longe alium sensum pretendit bene intelligentibus.

[ENGLISH]

## ¶3 · 42.8–42.12

> [p. 42] Pro quo notandum quod Moyses alloquens populum valde rudem aptavit verba secundum eorum capacitatem, ut primo literaliter consencientes per fidem ascendant ad sensum alciorem, sicut utrobique facit scriptura.

[ENGLISH]

## ¶4 · 42.13–42.25

> [p. 42] Secundo secundum historiographos est notandum quod mortuo Adam Seth ex mandato patris separavit cognacionem suam a Kaym, rediens ad solum natale in quendam montem propinquum paradiso, sed post septimam generacionem fertur filios eius qui propter religiositatem vocantur filii Dei miscuisse cum filiabus Kaym que propter petulanciam vocantur filie hominum; et potuit cum hoc esse quod demones incubi qui numerantur inter filios Dei detulerunt semina hominum in matrices mulierum procreando gigantes ex industria fovendi fetus per virtutes mixtorum, et ista brutalitas cum aliis que narrat Methodius martyr fuit causa diluvii.

[ENGLISH]

## ¶5 · 42.26–43.12

> [p. 42] Tercio notandum quod Deus apud quem omnia sunt presencia, loquitur in textu predicto tanquam pius pater consolans filios volentes per penitenciam converti ad Deum; quod patet ex tribus partibus huius textus. Nam primo dicit: Non permanebit spiritus [p. 43] meus in homine in eternum, quia caro est, eruntque dies eius centum viginti annorum, quasi diceret: Spiritus vivendi non permanebit eternaliter in toto genere peccatorum perpetuo dampnato, ut dampnatur genus demonum. Et racio secunda subditur, quia fragilis est ex carne et ut sic excusabilis. Tercio vero apponitur medium medendi, dum promittitur quod dies penitencie antequam inundet diluvium erunt CXX anni; hoc enim verbum Dei fuit viginti annis antequam Noe incepit procreare, et centum annorum fuit primogenitus suus tempore diluvii.

[ENGLISH]

## ¶6 · 43.13–43.29

> [p. 43] Secundo principaliter premittitur prima noticia malicie commisse, cum dicitur: Videns autem Deus etc. Secundo subditur pronitas ad recidivandum, dum adiungitur: Et cuncta cogitacio hominis etc. Et tercio ostenditur medicinalis satisfaccio, dum dicitur: Penituit eum quod hominem fecisset in terra. Ex faccione namque hominis terreni et peccato eius contra summum bonum oportuit Christum pati et intrare cum redemptis in gloriam suam; et hoc sonat penitere, id est, penam tenere. Nec moveat quod dicitur de presenti, quia Deus semper scit se pati. Tercio principaliter tangit in generali remedium ad abscindendum peccatum hominis in futurum, dum dicitur: Precavens in futurum, nam potestas gygancium qui fuerant super terram et sterilitas terre nascencium cum serenitate et salubritate aeris fuit illis occasio bestialiter lasciviendi.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 41.17: We are to accept all Scripture as true, and explain the figurative expressions.
- 41.27: Wyclif's exposition of 'it repented the Lord'.
- 42.8: Moses adapted his words to his hearers.
- 42.13: Cause of the deluge.
- 42.26: The text is an expression of God's mercy.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 41: *IVᵒ* (print = bt) [SUB]
  - 41: *VIᵒ,* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 40:
1. E: recita. 5. C: Dei in marg. alia manu. 6. D : concedendum;
ib. C: concedi debet ; ib. AB : ymmo decst. 7. E: sic dcest. 8, 9. A:
raciones exemplares in marg. alia mann. 16. D : alia creatura ; ib. D : de VI.
17. AB : dixit deest; C in marg. alia manu; E: dixit quod penituisset.
19, 20. ABCD : si eternaliter. 23. C: meum videtur; bonum deest.
1. In libro S. Augustini De Haeresibus hic locus non extat.
Cf. Sermon LII. De verb. evang. Matth. III, Opp. tom. V, 1, 304:
Excidit nobis quosdam male intelligentes vocari Patripassianos,
qui dicunt ipsum Patrem natum ex femina, ipsum Patrem

p. 41:
6. Codd. : inquit. 9. DE : posuerant ; ib. ABCD : Et deest. 10. E : hone-
raretur. 14. ABC: reservandi ; ib. D : reservanda formam. 17. ABC:
replicatur tercio. 19. B : quo notandus. 21 . B : fuit infidelis. 25. C : autem
in marg. alia manu; ib. ABC: debent; C correxit: debemus. 27. Rectius:
auditoribus. 27, 28. C: predictam sentenciam. 29. C: bene alia manu.
i5, 16. St. Augustini Opp. tom. Ilf, 1, pag. 70.

p. 42:
1. I»: soluit. 2. li: vel quod — hominem dccst. 3. B: tam fra-
gilem dcest. 5. D: caruit. g. E: rudem valde; ib. D: apta verba.
9, 10. E: capacitatem eurum. i5. E: solium naturale. 17. C: fertur
alia manu. 18. C: tniscuisse se; sc alia mauu. 25. E : causa fuit.
3o. D : non manebit.
20. Incubi, incuboncs cf. Du Cangc III, 804. 3o. Gcn.VI, 3.

p. 43:
2. C: centum et viginti; ib. DE: dies illius. 3. I)E: Spiritus vindi-
candi. 4. D: perpetue. 5, 6. E: subscribitur. 6. D: ut sit.
7. E: TerCium. i3. D : primo ; ib. A: noticia alia manu. 14. D: dum
dicitur; ib. E: ete. docst. i5. DE: adiungitur pronitas. i5, 16. E:
cum adiungitur. 16. E: etc. deest. 17. ABC: cum. 22. D: quod est;
E: quasi est. 27. I) : fertilitas. 28. ABC: fuerit; ib. E: eis ; ib. D:
14. Gcn. VI, 5. 17. ib. 6. 25. Hic locus in Vulgate
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 40: penituit eum fecisse hominem; | Eructavit cor meum verbum | Excidit nobis quosdam male intelligentes vocari Patripassianos, qui dicunt ipsum Patrem natum ex femina, ipsum Patrem passum | Omnia quecunque, | sicut fedati; | heretici heretica. | tamen reputant; | quam nisi. | Similiter decretum. | ibi quecunque.
p. 42: Non permanebit spi-
p. 43: ritus meus in homine in eternum, quia caro est, eruntque dies eius centum viginti annorum, | Videns autem Deus | Et cuncta cogitacio hominis | Penituit eum quod hominem fecisset in terra. | Precavens in futurum,
```

---

## Chunk 02-e: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-02-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-02-e
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "44.1–48.22"
divisions: "cap. 2 (heading 'CAPITULUM SECUNDUM.' at 29.0); part 5 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "1026 words; 998 confirmed by the vote; 21 runs stood by rule; 7 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n115–n119 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 2, part 5: [TITLE]

## ¶1 · 44.1–45.29

> [p. 44] Secundo premittit eternam displicenciam, dum dicitur: Factus dolore cordis intrinsecus; non enim credendum est quod Deus habet penam secundum naturam divinam, etsi sibi mala displiceant; nec est credendum quod noviter habuit vel eternaliter elicuit displicenciam, cum fuit intrinsecus in corde; per hoc autem notatur quod finaliter specificat modum delendi occasionem ab inusu hominis ad terrestria, cum finaliter dicit: Delebo, inquit, hominem quem creavi a facie terre etc. Consumpsit enim mixta ornancia terram et aerem ac indisposuit raciones seminales, sicut pater misericors precavens petulanciam filii aufert ab eo occasionem peccandi; non enim punit Deus predestinatum ut prescitum, nisi misericorditer ad puniti demeritum; unde punicio aque preternaturaliter inundantis correspondet eorum inordinate luxurie. Corrupte vero exalaciones causantes salsedinem et indisponentes terram et aerem ut influencia celestis sit proporcionalis cremento et aure temporanee, sicut ante correspondet eorum affeccioni inordinate circa terrena violenter rapiendo. Unde pro istis duobus peccatis subditur: Corrupta est autem terra coram Deo quoad primum peccatum carnale, et repleta est iniquitate quoad secundum peccatum avaricie. Si autem placet intelligere per punicionem iustam execucionem vindicte que est finis penitudinis in potente, excludendo mocionem, passionem, inprovisionem etc., que dicunt inperfeccionem in penitente, non contradico sentencie. Sic enim intelligitur illud Psalmi VI, 2 et Psalmi XXXI: Domine ne in furore tuo arguas me, [p. 45] neque in ira tua corripias me. Furor enim sonat in vehemenciam et acceleracionem vindicte pro peccato irremissibili continuando usque ad finem vite pro quo Deus arguit insolubiliter concludens, ut patet Matth. XXVᵒ, 31: Cum venerit filius hominis. Talium enim terrenorum inventa est iniquitas ad odium perpetuum; secundo quia horrendum est incidere in manus Dei viventis ad Hebr. Xᵒ, 31; ideo petit quod non corripiatur propter lignum, fenum et stipulam in purgatorio expurgandum. Quamvis enim ira talis sit micior iuxta illud Abakuk IIIᵒ, 2: Cum iratus fueris, misericordie recordaberis, tamen utrumque est timendum, et pro supplecione tocius penitencie in via humiliter est petendum. Absit autem quod in talibus locucionibus credamus passionem vel perturbacionem in Deo accidere, cum Sap. XIIᵒ, 18 scribitur: Tu autem Domine virtutum cum tranquillitate iudicas. Et conformiter iudicandum est de austeritate et usura Dei in parabola Salvatoris Luc. XIXᵒ. Et eodem modo intelligendum est de Dei serenitate et quibuscunque aliis sibi attributis, que omnia ex equo concurrunt; ad Rom. IIᵒ scribit Apostolus: Vide ergo bonitatem et serenitatem Dei; et illud Apok. XVI, 15: Ecce venio sicut fur; beatus qui vigilat et custodit vestimenta sua. Et sic intelligendum est illud Psalmi LXXVIIᵒ, 65: Et excitatus est tanquam dormiens Dominus et tanquam potens crapulatus a vino cum quotlibet similibus, quorum particulares exposiciones continent indubie profunda misteria.

[ENGLISH]

## ¶2 · 45.30–46.12

> [p. 45] Ex istis patet quod non oportet si Deus intelligit per dolorem cordis displicenciam Dei Patris, quod nos in toto debemus loqui conformiter. Sicut enim [p. 46] dicit Augustinus quod Deus est iustus iusticia et non qualitate, sic concedendum est quod Deus est tactus dolore cordis sine passione vel penitencia dolorosa. Et patet in quibus debemus loqui conformiter ad scripturam et in quibus debemus loqui expositorie suspensis parabolis admirando eius subtilem sentenciam, ut quidam intelligunt per hoc quod Deus est tactus dolore cordis intrinsecus, quomodo eternaliter displicencia Dei Patris fecit quod misit unigenitum suum incarnandum; unio enim ypostatica fuit taccio infirmitatis filii, quia ex hoc filius qui est natura patris intrinsecus fuit nostris doloribus oneratus.

[ENGLISH]

## ¶3 · 46.13–47.9

> [p. 46] Quantum ad secundum allegatum de autenticacione doctoris, patet quod quilibet doctor est concedendus, sed nullius posterioris doctoris sentencia nisi de quanto est fundabilis ex scriptura. Credo autem quod sentencia beati Bernhardi fuit katholica sed logica eius est hodie postponenda. Sic enim facimus cum loyca ecclesie de Eukaristia, sic eciam sepe prohibet Augustinus quod defendantur vel teneantur dicta sua nisi de quanto consonant cum scriptura. Intellexit autem Bernhardus per manus, oculos et aures personaliter verbum Dei et sic posuit figurative illa organa crucifigi; hoc est signum signatum per illa organa vel secundum alium sensum nobis absconditum. Sed nos non debemus predicare taliter et specialiter in vulgari sine explanacione sensus katholici, cum sentencia heretica sic de facile surriperet in auditorio ex negligencia predicantis; [p. 47] debemus enim loqui palam populo sentencias scripture necessarias ad salutem. Nec sufficit quod nos habeamus sensum katholicum, quia sic possemus seminare quotcunque hereses adversando toti scripture, dum tamen debemus niti apciori modo quo sufficimus imprimere in auditorio katholicas et edificatorias veritates, quia aliter non sumus adiutores Dei sed dyaboli, nostrum honorem vel seculare commodum proditorie procurantes.

[ENGLISH]

## ¶4 · 47.10–47.27

> [p. 47] Ulterius credo quod utraque ecclesia tempore Beringarii et tempore novellorum doctorum fuit katholica, cum equivocarunt in terminis; nec credo quod scola illa de Eukaristia tantum intricavit ecclesiam ut moderna; hoc tamen videtur omnino quod caveamus denotando quamlibet partem sacramenti sensibilis esse corpus Christi vel sanguinem, quia vulgus et litterati viri sunt proni ad intelligendum panem post consecracionem esse ydemptice corpus Christi, ideo propter sensibilem erroris percepcionem tam in clero quam in layco debent defectus corrigi in loquendo, recolendo quomodo circa Eukaristiam fuit prima heresis in Christi discipulis abeuntibus retrorsum propter duriciam sermonis, ut patet Joh. VIᵒ, 61, 67, et meminit decretum in De Consecracione, distinccione 2ᵃ, Prima quidem heresis ex testimonio Augustini. Et hec est racio quare oportet sacerdotes qui panes offerunt omnino instrui in ista materia.

[ENGLISH]

## ¶5 · 47.28–48.7

> [p. 47] Sed tercio principaliter replicatur per hoc quod novella ecclesia ponit transsubstanciacionem panis et vini in corpus Christi et sanguinem; hoc autem non posuit ecclesia primitiva, ergo in sentencia contradicunt. Assumptum patet Iᵒ Decretalium De summa [p. 48] Trinitate et Fide katholica, Una vero: Corpus Christi, inquit, et sanguis sub speciebus panis et vini in sacramento altaris veraciter continentur transsubstanciatis pane in corpus et vino in sanguinem potestate divina. Si autem panis et vinum manent integra et· non alterata post consecracionem, quomodo sunt transsubstanciata per verba sacerdotis?

[ENGLISH]

## ¶6 · 48.8–48.22

> [p. 48] In ista materia nostri katholici, eciam decretiste, didicerunt sic describere terminum supradictum: Transsubstanciacio est transitus unius substancie secundum se totam in aliam tota accidencium multitudine remanente, ut nec materia nec forma substancialis que fuerunt in pane et vino remanent post consecracionem, sed omnis substancia materialis vel formalis que fuit in eis corrumpitur, et succedit per conversionem sub eisdem accidentibus corpus Christi, et sic non est alicuius substancie annichilacio, tum quia conversio tocius substancie in melius, tum eciam quia accidencia remanent que prius erant in pane et vino, quia ipsis remanentibus committeretur ydolatria adorando panem et vinum ut corpus dominicum et sic Deum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 44.10: The appropriateness of the deluge as a punishment.
- 46.13: Authority of doctors must rest on their agreement with Scripture.
- 46.25: Need of careful exposition to the vulgar;
- 47.10: especially with regard to the Eucharist.
- 47.28: Transubstantiation a modern invention.
- 48.8: Definition of the word.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 44: *indisposuit* (print = bt) [SUB]
  - 44: *primum* (print = bt) [BT-ONLY]
  - 44: *me,* (print = bt) [SUB]
  - 45: *XXVᵒ, 31:* (print = bt) [SUB]
  - 45: *15:* (print = bt) [SUB]
  - 46: *concedendum* (print = bt) [SUB]
  - 47: *VIᵒ, 61,* (print = bt) [SUB]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 2. Gen. VI, 6. (). ib. 7. 22. ib. 1 [. (44.31).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 44:
3. ABC : concedendum. 7. C: finaliter deest; ib. B: speclat;
ib. DE: dolendi. 8. C: ab usu ; D: ab in visu. 10. E: etc. decst.
12. C: filii alia manu. i3. D: potuit Deus. 14, i5. B: ad presenti.
i5. AB: aqua. 18. E: celestis decst. 21. BD: violente; ib. D: rapienda.
23. ABC: est decst. 25. CDE: per penitudinem ; Lb. C: iustam execu-
cionem alia manu. 27. C: etc. deest. 29. E: enim dcest.

p. 45:
3. E: irremissibilitcr : ib. D: continendo ; ib. ABC: vite sue.
5. ABC: hominis etc. 6. D : enim corporum. 9. BC: e/deest; E: vel
stipulum. 16. B: m Deo deest. 21. E: ex quo. 22. D: scritit
Apostolus Rom. XI: ib. C : scribit Apostolus deest. 22, 23. C : Yide ergo —
Apoc. XVI alia manu. 23. Dei ; ABCE: dicit. 24. D: beatms omnis.
2<. ABCE: exponentes. 32. C: uniformiter.

p. 46:
r. E: dicimus; A alia manu: dicit Augustinus. 3. D: vei pena.
4. ABC: uniformiter. |, 5. A: uniformiter — loqui alia manu.
<). C: prOmisit; in marg.: misit. 14. doctoris; C correxit: doctorum;
ib. C: quod alia manu; ib. D: quod omnis. i5. C: docloris dccst.
i6. D: de scriptura. 20. B: tueantur. 21. Codd.: consonal; ib. C: cum
alia rrianu. 22, 23. D: probabiliter verbum Dei. 24. D : hoc estfilium;
rb. E : figuratum. 27, 28. AB: tam de facili; C: tunc defacili; in
marg. : sic de fdcili.
u S. Augustini Opp. tom. V, 144, I, 63o etc. i5. Decret.
Prima Pars, dist. IX, cap. X.. Cf. Wydifs De Apostasia, pag. 66.

p. 47:
2. A: sufficit in marg. alia manu. 6. D: audito modo katholicas.
12. B: equivocaverunt. 12, i3. B: sola illa. iS. ABCD: propler decst.
24. D: Dc deest. 25. D: cst decst. 32. ABC: arg&mentwn.
24. Decreti, Tertia Pars, dist. IT, cap. XLIV. 32. Decr.
Greg. IX, lib. I, tit. T, cap. T, § 3.

p. 48:
1. ABDE: Una racio ; C corr. in una vero. 2. AB : inquit deest;
C: inquit in rasura. 9. D: tantutn tradictum. n. D: accidencia.
x3. B: remanent. i5. AB: corri 26. C: fantasiaverunt ; ib C-.falsa.
33. C correxit: hoc expressius.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 44: Factus dolore cordis intriusecus; | hominem quem creavi | a facie terre | Corrupta est autem terra coram Deo | etrepleta estiniquitate | Domine ne in furore tuo arguas me/io
p. 45: neque in ira tua corripias me. | Cum venerit filius hominis. | horrendum est incidere in manus Dei viventis | Cum iratus fueris, misericordie recordaberis, | Tu autem Domine virtutum cum tranquillitate iudicas. | Vide ergo bonitatem et serenitatem Dei; | Ecce venio sicutfur; beatus qui vigilat et custodit | vestimenta sua. | Et excitatus est tanquam dormiens Dominus et tanquam potens crapulatus a vino
p. 46: Deus est tactus dolore cordis | est tactus dolore cordis intrinsecus,
p. 47: discipulis abeuntibus retrorsum propfer duriciam | quidem heresis
p. 48: Una vero: Corpus Christi, | et sanguis sub speciebus panis et vini in sacramento altaris veraciter continentur transsubstanciatis pane in corpus et vino in sanguinem potestate divina.
```
