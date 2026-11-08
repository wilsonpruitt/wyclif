# Translation brief: eucharistia 08-h–08-j

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/eucharistia/wyc-eucharistia-08-h.md chunks/eucharistia/wyc-eucharistia-08-i.md chunks/eucharistia/wyc-eucharistia-08-j.md` once and fix what it reports.
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

## Glossary (the 480 rows these chunks use; the full file is GLOSSARY.md)

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
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| sacramentum (the eucharist); sacramentum altaris | sacrament; the sacrament of the altar | The plain sense, against the Augustinian row (*Incarn.*). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.3, 3.30). |
| hostia; hostia consecrata | host; consecrated host | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.11, 1.22). |
| panis / vinum | bread / wine | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 2.8). |
| corpus Christi / corpus Domini | the body of Christ / the body of the Lord | Kept apart as the Latin alternates them. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.6, 1.10). |
| novella ecclesia / antiqua ecclesia | the newer church / the ancient church | The pair of 3.3; cf. *novelli*. Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 3.3). |
| cultores accidencium / signorum | worshippers of accidents / of signs | Wyclif's name for the defenders of the accident without a subject. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-b 6.15, prol-c 10.2). |
| pontifex (a Christian bishop, unqualified) | pontiff | As the Old Testament row; where the referent (a bishop) matters, an R note. *pontifices ydolorum* "pontiffs of idols". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 14.29, 15.17). |
| species (of bread and wine) | species | The sacramental species; kept as the term, not "appearance". Distinct from the logical *species*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 01-a 13.15; 23.8). |
| sacer; sacrare | sacred; hallow | Kept apart from *sanctus / sanctificare* "holy / sanctify" and from *consecrare*; *consecrare* is "to hallow together" in the grammarians' etymology. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 27–28). |
| sacramentum tantum | a sacrament only | The *sacramentum tantum* of the Lombard's three (IV d. 8 c. 4). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 29.23). |
| peregrinacio | pilgrimage | The church's way to the *patria*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 36.9). |
| conversio (eucharistic) | conversion | Of bread into the body; kept apart from *conversio* of a proposition. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 48.15). |
| principaliter; principalitas (of the body's presence) | principally; principality | Of the body of Christ alone being in the sacrament as its principal; not the compendium's *principaliter* "as a main head". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 75.5–26). |
| transaccidentacio | transaccidentation | Wyclif's coinage beside *transsubstanciacio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 81.27). |
| transinferioracio; transsubieccio | transinferioration; transsubjection | Coinages in the same series. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 82.3). |
| divinitus | divinely | The pair of *humanitus* "humanly". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 84.19). |
| consecracio | consecration | The noun of *consecrare*; see *confeccio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 99–100). |
| verba sacramentalia conversiva | sacramental words that convert | The *moderni*'s words of consecration as effecting conversion. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 121.1). |
| transaccidencia | transaccidents | In the *transaccidentacio* series. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 145.4). |
| corpus dominicum | the Lord's body | Kept apart from *corpus Domini* "the body of the Lord" and *corpus Christi*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 158.31, 165.3). |
| in circulo (of the host) | in a round | The round form of the host. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 161.17). |
| nominacio (baptismatis) | naming (of our baptism) | Wyclif's figure for the name the faithful bear. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 172.21). |
| sanctificacio | sanctification | Ruled 2026-11-07 (coordinator, delegated; *Euch.* 189.6). |
| eukaristia | the Eucharist | PROVISIONAL capital (Wilson to rule; the volume has ~110 *Eucharist*, 36 *eucharist* in the English, not yet conformed); kept apart from *sacramentum (altaris)*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 196.29). |
| secta signorum | the sect of the signs | Wyclif's name for the *moderni*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 220.13). |

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
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| graduacio; graduati | CONTEXTUAL: graduation / gradation; graduates | Academic "graduation" (Dialogus, 4 sites); of rank or lordship (*graduacio dominii*, *Pot. pape* 293.33, 297) "gradation". Ruled 2026-09-28; CONTEXTUAL 2026-10-12 (coordinator, delegated). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| possessionati | the possessioners | Endowed religious. |
| protestacio; protestari | declaration; to declare solemnly | ⭐ The submission formula ("if anyone can teach me this is contrary to scripture or reason, I will humbly retract"). Penn and Lahey both inverted it (T. pp. 369, 378). Render it as a retraction offer, never as defiance. Also of Berengar's sworn confession (*Euch.* 197.4, coordinator 2026-11-07). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| locus a maiori | the topic from the greater | The dialectical topic; for *a simili* see "the topic from likeness" (2026-09-28 row). Ruled 2026-10-02 (*Eccl.* 144.27). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |
| leges ecclesie | the laws of the church | Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 1.20, 1.23). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| respectus; respectivus | relation; relational | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
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
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| citra fidem | short of faith | The contrast with *ex fide*: held on evidence, not as faith teaches. Ruled 2026-09-28 (4 sites). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| citra Christum | short of Christ | As *citra fidem*. Ruled 2026-10-02 (45.8). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| dyameter / costa | diameter / side | The geometers' terms (the square's incommensurable diagonal). Ruled 2026-10-02 (97.21 ff.). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
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
| approbati doctores | approved doctors | Kept apart from *probabiles doctores*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 13.3). |
| novelli | the newer [doctors] | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 13.7). |
| sophistice | sophistically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 15). |
| de vi vocis / de vi sermonis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| protervus | obstinate | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| gracia unionis | the grace of union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| exinanicio / exinanire / inanicio | emptying / empty | Phil. 2:7 (Douay "emptied himself"); *inanicio* (*Incarn.* 33) the same. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| suppositum | supposit | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 34.24). |
| individuum | individual | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 35.7). |
| in quantum (reduplicative) | insofar as | As *secundum quod*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37.9). |
| universitas creaturarum | the totality of creatures | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37). |
| pars qualitativa | qualitative part | Body or soul as the parts that make up a man by kind; set against *pars quantitativa*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 43.5). |
| pars discretiva | discrete part | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 46.9). |
| intransitive | intransitively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 45.28). |
| in effectu | in actual fact | As against in potency or in name; ⛔ not "in effect" (modern "virtually"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 47.10). |
| animare | animate | The argument turns on it (45.30–46.4). Ruled 2026-10-22 (coordinator, delegated). |
| communicacio ydiomatum | communication of idioms | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.1). |
| denominativum | denominative | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 50.30). |
| Doctor Subtilis | the Subtle Doctor | Scotus. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.24). |
| convertibilis / converti | convertible / be convertible | Of terms. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 52.29). |
| forma totalitatis | form of totality | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 50.7). |
| quantus | quantified | The adjective beside *quantitas*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.22). |
| suppositacio | suppositation | Kept apart from *supposicio* "supposition". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.31). |
| moderniores loquentes | the more modern speakers | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 59.21). |
| supposibilis | that can be supposited | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 64.14). |
| per se / per accidens | CONTEXTUAL: of itself / by accident; (spatial) apart, by itself | The spatial sense (a thing set apart, *Euch.* 104.16–17) gets a G note. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a (sufficienti) divisione | the topic from sufficient likeness / from (sufficient) division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| pretericio | being past | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| inconsequens | inconsistency | Kept apart from *inconveniens* (an unfitting conclusion). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 78.23). |
| capitales doctores | the chief doctors | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| intricaciones sophistice | sophistical entanglements | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 82). |
| eiusdem / consimilis / alterius racionis | of the same / like / another kind | The species-sense of *racio*; *racio speciei* "the account of the species" (Aristotle's *logos*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.4, 87.17). |
| principiari | be constituted from principles | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.7). |
| accidentatus | subject to accidents | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.4). |
| in recto / in obliquo | in the direct case / in an oblique case | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.25). |
| mobilis / mobilitas | movable / movability | Of Christ's humanity (ch. 7). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.11). |
| signum / signatum | sign / thing signified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 91.2–6). |
| conveniencia / convenire (*in*) | agreement / agree | The argument of 90–91 turns on it; not "fittingness" (that is *congruencia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 90). |
| conversari | live one's life (among men) | Beside *conversacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.25). |
| esse intelligibile | intelligible being | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 99.23). |
| extraneare / extraneacio (supposicionis) | estrange / estrangement (of supposition) | *Affeccio extraneandi* "an affection of estrangement". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 98.16). |
| ministerialiter | ministerially | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 100.17). |
| mobile (noun) / primum mobile | a movable / the first movable | Against the adjective *mobilis*; ch. 7 turns on it. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 107, 116). |
| immobilis / immobilitas | immovable / immovability | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| res racionis | thing of reason | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| universitas creata | the created totality | Beside *universitas creaturarum*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| predicacio secundum essenciam / formalis | predication by essence / formal predication | Wyclif's modes of predication (cf. *predicacio secundum causam*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 115–116). |
| forma substancialis | substantial form | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| concepcio (figure) | conception | The grammatical figure. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| accidens | accident | The category; *accidit* "befalls". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| denominacio respectiva | relational naming | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 120.17). |
| conversio (of a proposition) | conversion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.30). |
| deduccio | deduction | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.21). |
| racio (individual, personal) | account | *Racio individui / persone* "the account of an individual / a person", as *racio speciei*; not "aspect" (the row against *substancia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 8, 129–132). |
| vir (against *homo*) | man (*vir*) | Where Wyclif sets *vir* against *homo*, the Latin in parentheses. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 129.15–26). |
| exemplaria / exemplata | exemplars / things exemplified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.6). |
| res secunde intencionis | things of second intention | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.25). |
| materia proxima / remota | proximate / remote matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137.1). |
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
| aliud / alius | another thing / another one | The neuter against the masculine (*aliud et aliud, non alius et alius*): natures against persons. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 160.1–2). |
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
| risibilis / risibilitas | risible / risibility | The proper attribute of man. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 181). |
| mocio / motus (paired) | motion (*mocio*) / movement (*motus*) | Only where Wyclif pairs them; otherwise "motion". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 180). |
| posicio anime | the laying-down of the soul | John 10:17–18; not the logical *posicio* "position", C note. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 183.3). |
| causancia / causacio | causing / causation | Kept apart (both at 187.30–34). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 185.16). |
| vicem supplere / vicis supplecio | supply the place / the supplying of a place | God supplying the place of a second cause. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 187.26). |
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
| homo communis | the common man | The universal man, with *res communis*; not "the ordinary man". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 218.3). |
| moderni loquentes | the modern speakers | Beside *moderniores loquentes*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 221.20). |
| supposicio | supposition | Of a term (supposition theory) or of a premiss laid down (cf. *supponitur* "it is supposed"); the English word serves both, C note where it matters. Kept apart from *suppositacio* "suppositation". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 102.8). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
| sacramentaliter | sacramentally | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| vere | truly | A mode adverb: one word each, never two merged, kept where Wyclif puts it. ⛔ Never "really" (that is *realiter*). Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| spiritualiter | spiritually | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| virtualiter | virtually | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| sensibiliter | perceptibly | A mode adverb: one word each, never two merged, kept where Wyclif puts it. As *sensibilis* "perceptible". Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| corporaliter | bodily | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| substancialiter | substantially | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| dimensionaliter | dimensionally | A mode adverb: one word each, never two merged, kept where Wyclif puts it. Ruled 2026-11-06 (Wilson; *Euch.* prol-a, review b3). |
| sentencia (verborum, scripture) | sense | The meaning of words or a text (*ad sentenciam attendendum*, against the rites, 4.9); kept out of the two-sense row *sentencia*. Ruled 2026-11-06 (Wilson; *Euch.* prol-a 4.9, review b14). |
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
| supponere pro | stand for | Supposition; with *supposicio*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 24.27). |
| sensualiter | sensually | Berengar's oath word (*Ego Berengarius*); kept apart from *sensibiliter* "perceptibly". A mode adverb, one word. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 26.1, 30.24). |
| describere | define | The verb of *descripcio* "definition". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 48.9). |
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
| interpolatus; interpolacio | interrupted; interruption | Of words spoken with pauses. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 89.4, 89.18). |
| quintimembris | fivefold | Cf. *trimembris*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 91.11). |
| locus a maiori | the topic from the greater | The dialectical topic. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-e). |
| essencialiter | essentially | A mode adverb, one word. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-g). |
| noticia confusa / distincta | indistinct / distinct knowledge | As *confuse / confusus* "indistinct(ly)". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-g). |
| opinative | as an opinion | Kept apart from *opinio* "opinion" (noun). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 04-g). |
| ponderositas; ponderosum | heaviness; heavy | The abstract against the concrete: *hostia est ponderositas sed non est ponderosum*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* prol-a p. 10, 110.24). |
| relacio ydemptitatis | relation of identity | The grammatical relative of identity. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 116.6). |
| questio si est / quid est | the question whether it is / what it is | *Post. An.* II.1. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 119.18). |
| universitas sua (God's) | his universe | Beside *universitas creaturarum* "the totality of creatures". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 124.31, 129.16). |
| naturalitas obediencialis | obediential naturalness | Cf. *dependencia obediencialis*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.15–18). |
| accidentalitas | accidentality | Beside *substancialitas*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.13). |
| quantitas successiva | successive quantity | Time and motion, against permanent quantity. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 134.1). |
| corpus mathematicum | mathematical body | The three dimensions without matter. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 142.31). |
| ubi; ubicans | where; that which gives a where | The category of place and its cause. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 146.23–24). |
| inpossibilitare | make out as impossible | Of the *moderni*'s argument. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 149.13). |
| localiter | locally | A mode adverb, one word; beside *dimensionaliter*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 148.29). |
| conversivus | converting | As *verba sacramentalia conversiva*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 153.6, 153.25). |
| generancia | begetting | Ruled 2026-11-07 (coordinator, delegated; *Euch.* 161.25). |
| ponderacio | weighing | Beside *ponderositas* "heaviness". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 183.17). |
| universitas (bare: tota universitas) | the whole universe | Beside *universitas sua* "his universe". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 192.14). |
| qualitas prima | first quality | Hot, cold, wet, dry. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 197.24). |
| subiectare | be the subject of | Of a substance underlying accidents. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 199.10). |
| visio corporalis / ymaginaria / intellectualis | bodily / imaginary / intellectual vision | Augustine's three kinds (*De Gen. ad litt.* XII). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 206–211). |
| visio intuitiva / abstractiva / enigmatica | intuitive / abstractive / enigmatic vision | The schools' kinds of cognition; *enigmatica* after 1 Cor 13:12. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 206–211). |
| locus a completa similitudine | the topic from complete likeness | Beside *locus a maiori*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 214.31). |
| diffinitive (of presence) | definitively | Of being in a place definitively, not circumscriptively. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 216.4). |
| sensus tropicus | tropical meaning | As *sensus* (of words) "meaning". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 217.22). |
| contentive / causaliter / subiective / obiective | by way of containing / causally / subjectively / objectively | The modes of being in the sacrament. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 219.17–22). |
| verba adiectiva | adjectival verbs | Grammar: set against the substantive verb *est*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 230.22). |
| multiplicacio corporis | multiplication of a body | The subject of ch. 8. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 232.5). |
| predicatum infinitum / finitum | infinite / finite predicate | Ruled 2026-11-07 (coordinator, delegated; *Euch.* 235.29). |
| qualitas secunda | second quality | Beside *qualitas prima*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 236.11). |
| infinicies | infinitely many times | Ruled 2026-11-07 (coordinator, delegated; *Euch.* 237.10). |
| non communicans (of times) | not communicating | Of times with no common part. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 241.25). |
| simultas adequacionis / inmediacionis | simultaneity of adequacy / of immediacy | Ruled 2026-11-07 (coordinator, delegated; *Euch.* 247.9–10). |
| principative | principatively | Beside *principaliter*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 247.21). |
| situaliter | situally | The adverb of *esse situale*. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 247.2). |
| evum | aeviternity | The measure of angels, between time and eternity. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 255.9 ff.). |
| evitas | aeveity | Kept apart from *evum* "aeviternity". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 258.20). |
| vicissitudo | alternation | Of discrete angelic time. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 251.5, 255). |
| mora | abiding | Kept apart from *duracio* "duration" and *diuturnitas* "length". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 257–258). |
| punctale (noun) | punctual | A point-like thing. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 253.10). |
| argumentum temptativum | tentative argument | Aristotle's *peirastic* argument. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 256.4). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office; *quale magisterium* "what a feat of mastery" (*Incarn.* 137.14) | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| detegere | to expose | "wipe away" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| ablatarius | the one from whom it is taken | Beside *ablacio* "taking-away". Ruled 2026-10-02 (*Eccl.* 15, 343.7). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| adequata ecclesia | the adequate church | C note at use. Ruled 2026-10-02 (*Eccl.* 17, 393). |
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
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| continuacio (of bodies, the act) / discontinuacio; continuare / discontinuare | continuation / discontinuation; make continuous / make discontinuous | The making of several bodies into one continuum (*Incarn.* ch. 12), G note at first use: not "carrying on". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.30, 211.12). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| locus evidencie | topic of evidence | *locus* = dialectical topic (cf. *locus a maiori*); not "place". Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| rectiloqui | those who speak correctly | Ruled 2026-10-02 (*Eccl.* 19, 468.15). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). Beside *consecrare* (*consecrat et conficit*) "confect", so the pair stays two. Ruled 2026-11-07 (Wilson, "confect works"; *Euch.* 16.10). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| deliramenta | ravings | Ruled 2026-10-07 (*Pot. pape* 06-c). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| relacio racionis | relation of reason | Scholastic term (a relation in the mind only). Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 3.7). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| sessiva / sesina | seisin | *Sesina* the spelling at *Incarn.* 33. So the manuscripts (Loserth 170.8, *ita cod.*); feudal possession that perfects a title. Ruled 2026-10-08 (coordinator, delegated). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| primicia (virtutum) | being first (in the virtues) | Kept apart from *primatus* "primacy" and *primitas* "firstness". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 228.33). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| locus a simili | the topic from likeness | Dialectical topic. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 240.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| pontifex (Old Testament, unqualified) | pontiff | Kept apart from *sacerdos* "priest"; *summus pontifex* of the Jewish priesthood is "high priest" (see *summi pontifices*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* ch. 11). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| gradus (of belief) | degree | The four degrees of belief (*Pot. pape* 327.18 ff.). Ruled 2026-10-12 (coordinator, delegated). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| latitudo (of a quality) | latitude | The intension/remission term. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 352.4). |
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
| singulariter | CONTEXTUAL: alone, only / in a singular way / in the singular (grammatical number, *Euch.* 215.15) | "singularly" never; "in a singular way" where "alone" will not construe (*Euch.* 85.28, coordinator 2026-11-07). Ruled 2026-11-06 (coordinator, delegated; *Euch.* prol-a 4.14). |
| ex tibi dubio; ex sibi dubio | for all you know; for all he knows | Idiom: not "from doubt". Ruled 2026-11-07 (coordinator, delegated; *Euch.* 66.15, 70.25). |
| cordatus | stout-hearted | Not "wise" (C note where it leans). Ruled 2026-11-07 (coordinator, delegated; *Euch.* 180.6). |
| rima | chink | Wyclif's figure for a loophole. Ruled 2026-11-07 (coordinator, delegated; *Euch.* 216.21). |

---

## Chunk 08-h: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-08-h.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-08-h
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "259.19–263.13"
divisions: "cap. 8 (heading 'CAPITULUM OCTAVUM.' at 232.0); part 8 of 10, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "903 words; 895 confirmed by the vote; 6 runs stood by rule; 2 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n330–n334 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 8, part 8: [TITLE]

## ¶1 · 259.19–260.7

> [p. 259] Confirmatur ex hoc quod idem homo intuens coloratum vel lucidum motum celeriter variat continue visionem et sic intuicionem, ergo multo magis sic potest angelus qui est celerior ad mutandum intuicionem in proprio genere et affeccionem, quamvis enim ponitur quod Deus et angelus semper intuetur in verbo omnia preterita et futura, non tamen intuentur illa angeli in proprio genere nisi dum sunt, quia aliter dyabolus semper intueretur casum suum; et quomodocunque sit de hoc, Deus sicut in uno instanti potest mutare affeccionem angeli, ita continue in quocunque. [p. 260] Nec est dubium isti secte, si sic faciat, quo facto mora affeccionis talis angeli foret mensura continua tocius mundi sensibilis et tempus compositum ex instantibus, ita quod nullum argumentum fieret contra composicionem continui ex non quantis, quin eque procederet contra illud; quod tamen negat hec secta esse possibile.

[ENGLISH]

## ¶2 · 260.8–260.18

> [p. 260] Item (ut sepe assumpsi) forent simul iuxta hanc sectam multa tempora non communicancia nec pars alicuius temporis tercii; quod est inpossibile, quia posito quod quelibet creatura permanens habeat tempus proprium sibi inexistens formaliter, ut conceditur de evo quoad angelos, tunc cum veris sequitur quod tempus componitur ex suis partibus coextensis et omne permanens duraret per infinitum magnum tempus, et quodlibet foret in quolibet, et infinitum maior foret in casu pars quantitativa suo toto, et periret omnis certitudo de mora temporis mensurantis.

[ENGLISH]

## ¶3 · 260.19–262.3

> [p. 260] Prima istarum quinque conclusionum videtur ex hoc quod omnis rei temporalis duracio potest esse tempus sed omnis talis rei duracio est quidquid potest esse, ergo omnis rei talis duracio est tempus. Assumptum patet per hoc quod tempus et quando sunt accidencia diversorum generum, sic quod omne tempus per se primo est tempus, sicut omnis homo est per se homo, et sic de quando; posito ergo de quacunque re permanente quod per se foret successive durans, tunc eius duracio foret tempus, quod sic opinans dicit esse contingencium; sive ergo fuerit forma sive materia sive accidens per se positum, ipsum posset per se subiectare tempus; ymmo tempus cum sit quantitas poterit per se esse; quod est magis quam posse informare quamcunque substanciam permanentem; ideo non negabit ista secta possibilitatem assumpti. Nec [p. 261] valet allegari Aristoteles vel Averrois quod tempus solum sequitur motum primi mobilis in quo est solummodo subiective, quia illi negant accidens per se esse; ideo miror qua fronte ipsi allegarent istos pro sua sentencia, cum tantum discordant in principiis. Isti enim dicunt quod Deus non potest facere quod incipiat esse tempus, cum non potest (ut inquiunt) creare mundum nec potest movere aliquam partem mundi nisi mediante motu primi mobilis; quorum quodlibet est summe hereticum, ideo est baculus nimis arundineus accipere sentencias istas hereticas ad stabiliendum subiectum temporis. Ideo iuxta sentenciam Augustini, XII Confessionum, totus mundus est subiectum temporis, cum quiescente toto celo et mota rota figuli foret idem tempus quod modo; cum ergo tempus non potest migrare de subiecto in subiectum, manifestum est quod tempus individuatur et subiectatur in mundo; nam quiescente quacunque parte mundi non subiectaret tempus et per idem nec modo. Et istam sentenciam consideraret hec secta, antequam dixisset tot sentencias hereticas in materia de sacramento altaris. Ponit enim quod inpossibile est panem remanere post consecracionem (ut dictum est quinto capitulo) et fundatur super isto principio summe heretico: Nichil potest esse ubi prius non fuit, nisi vel moveatur illuc localiter vel aliud convertatur in ipsum; quod indubie destrueret totam fidem, quia tunc Deus non posset creare celum vel aliquid nec dominus Jesus Christus posset crescere corporaliter (ut deductum est ibidem) nec Spiritus Sanctus posset elevare hominem ad conversandum in celo, nisi moveat illuc localiter corpus suum. Que tria destruerent [p. 262] totam fidem. Oportet ergo fidelem rimari aliud fundamentum ad stabiliendum subiectum temporis a quo ipsum dependeat.

[ENGLISH]

## ¶4 · 262.4–262.8

> [p. 262] Et patet prima istarum conclusionum ex opinione, quia capto uno corpore inanimato per se durante cuiuslibet sue partis duracio foret tempus et coextensis materia et forma substanciali et accidentali forent duraciones tempora coextensa.

[ENGLISH]

## ¶5 · 262.9–262.13

> [p. 262] Et patet secunda conclusio, quia omne durans per tempus duraret per infinita tempora non communicancia, quorum quodlibet foret tantum ut hec hora, ut patet de partibus intensivis vel quantitativis date substancie vel de lineis vel superficiebus equalibus.

[ENGLISH]

## ¶6 · 262.14–262.17

> [p. 262] Et tercia conclusio, scilicet quod quidlibet foret in quolibet, videtur ex hoc, quod quidlibet foret in tempore cuiuslibet, sed nichil est in tempore subiecti, nisi fuerit in ipso; ergo quidlibet foret in quolibet.

[ENGLISH]

## ¶7 · 262.18–262.27

> [p. 262] Unde sollempniores doctores novelli dicunt quod nullum sublunare foret in tempore primi celi, nisi quia omne corpus sublunare habet dependenciam ordinis causalis ad ipsum, sicut dicimus omne temporale se habere ad mundum. Nec dubium quin omne temporale coexistens cuicunque tempori est in eodem, quia est cum tempore illo in quo potest esse; et hoc sufficit ad aliquid esse in illo; sic enim due quantitates eiusdem speciei possunt informare idem subiectum, sicut est de qualitatibus.

[ENGLISH]

## ¶8 · 262.28–263.13

> [p. 262] Et quarta conclusio, scilicet quod infinitum maior est de possibili pars quantitativa quam suum integrum, patet capiendo A pedale cum sua duracione, et pono quod Deus annichilet secundam medietatem A cum sua [p. 263] duracione conservando residuum duracionis perpetuo, et tunc videtur quod medietas quantitativa temporis A est ita longa et per consequens ita magna ut tempus aliquid et totum tempus sicut et suum subiectum nunc desinit esse. Sic enim foret dare temporis primum instans et ultimum; et sic videtur quod positis infinitis temporibus omnino equalibus quoad molem infinitum minus est aliquod quoad duracionem, et ut unum est relacio minus quoad molem, est ipso maius quoad duracionem. Ex quibus sequuntur inconveniencia, dato quod sequitur tempus est sic magnum quoad molem vel duracionem, ergo tempus est sic magnum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 261.1: Our opponents have thrown over Aristotle and Averrhoes.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 259: *motum* (print = bt) [SUB]
  - 261: *modo;* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 259:
[. D: continuitatem. 2. AB: corporis; C: temporis in rasura.
3. E: sit. 5, 7. 8. D: continuo. 8. C: novam deest. 8,9. D: Sicut
tuitus. 10. D: sequitur illud. 11. AB : illa ut. 14. D: que ita ut ;
ib. ABCD : substancia et. i5. Sed ; D: secundum. 17. C: simul deest.
21. D: intelleccionem ; ib. ABC: sic deest. 22. D: est deest. 23. D:
quam nisi. 27. E: quia alias. 28. C: sicut in marg. alia manu.

p. 260:
1. D: ldeo est. 6. D: contra illa. 9. D: nec partes. 16. D: quid-
libet. 17. C: et in marg. alia manu. 22, 23. ABCD: Argumentum patet.
29. ABC: contingentivum 3i. D: lioc tempus; ymmo dcest.

p. 261:
i. ABDE: allegare. 4. A in tcxtu: ideo minor ; miror in marg. alia
manu. 9. AB : quarum. 10, 11. ABC: arundeneus. i5. D : ut modo.
20. A: sentenciam in marg. alia manu. 26. ABC: vel before moveatur
dcest. 27. D : quod non.
i3. S. Augustini Opp. tom. I, pag. 210.

p. 262:
1. C: totam fidem in marg. alia manu. 5. D: pro se. 7. D: in
materia; ib. D: ac accidentali. 11. D: liec est. i3. D: aut super-
Jiciebus; ib. A: equalibus in marg. alia manu. 14. ABC: quod quodlibet.
14, i5. E: in quodlibet. i5, 16. D: videtur — cuiuslibet deest. 19. AB : in
parte. 21, 22. D: esse temporale. 23. ABC: circuique tempori.
25. DE: aliquid deest; ib. C: Sicut; ib. D: secunde. 3o. pedale ;
A: possibi/e. 3i. D: annicliilaret.

p. 263:
8. ABC: aliquid. 8 10. ABCE: et ul unum — duracionem decst.
12, i3. C quoad — magnum in marg. alia manu. 17. D: quanlumcunque
diu. i^. ABDE: qualibet. 22. A: diuturnitas in marg. alia manu.
?4. ABC: linias. 27. D: superficiales ; ib. D: vel tempus. 3i. I): elposl.
32. BD : vocant; ib. ABC: liniam; D : literam.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
(none recorded)
```

---

## Chunk 08-i: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-08-i.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-08-i
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "263.14–267.22"
divisions: "cap. 8 (heading 'CAPITULUM OCTAVUM.' at 232.0); part 9 of 10, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "1005 words; 993 confirmed by the vote; 12 runs stood by rule; 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n334–n338 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 8, part 9: [TITLE]

## ¶1 · 263.14–265.19

> [p. 263] Et ex eodem patet quinta conclusio, scilicet quod periret omnis certitudo de mora temporis, quia quantumcunque breve tempus, eciam instans, potest servari quantumlibet diu, ideo diuturnitas et brevitas forent accidencia separabilia a tempore sicut a quolibet permanente, quia aliter non posset tempus per se esse vel prorogari, cum tamen tempus inter omnia accidencia minime dependeat a subiecto. Et patet confusio respondendi, cum diuturnitas temporis vel sit ipsum tempus vel accidens quod poterit per se esse; de quo non est nobis certitudo; et sic (ut sophiste arguunt) capiendo lineas infinitas girativas quarum quelibet infinitum diu durat, sicut est infinitum magna quoad molem, tunc videtur quod superficies, numerus vel respectus qui est per illa tempora (quantumcunque brevis fuerit) est per infinita tempora non communicancia, quorum quodlibet est dupliciter infinitum; et ita foret de omni corpore racione suarum parcium; et patet incertitudo atque confusio. Unde sophiste notant unam lineam girativam [p. 264] circumgirantem versus orientem in infinitum A columpnam cuius cingulum sit pedale, et ponatur quod A et tota superficies sua annichiletur servato B per se et quod una superficies rotunda appropinquet ab oriente quousque tangat B in C instanti, et tunc patet quod B fuit finitum in utroque extremo et quod fuit dare ultimam eius partem proporcionalem que fuit superficialis quod est dare maximum gradum curvedinis in circumgiracione; que omnia negat hec secta esse possibilia, ideo valde inconvenienter est sibi ipsi contraria; nam dato puncto extremali linee vel est dare pedale illius linee terminatum ad illum punctum vel linea non est tanta, sicut patet ablato illo puncto sine pluri vel rectificata illa linea secundum illud extremum vel fluente puncto uniformiter super illam incipiendo ab illo extremo vel fluente reliquo extremo in infinitum continuum et directum manente isto extremo fixo vel veniente ab oriente superficie rotunda, cuius dyameter sit pedalis. Et patet, sicut unus punctus illius superficiei tangit A datum punctum extremalem qui exempli gracia sit punctus ultimus illius diametri, sic quilibet alius punctus eiusdem circuli incipit vel incipiet tangere aliquem punctum illius linee girative; et ponatur quod Deus ex omnipotencia sua aptet sic motum dati circuli quod quilibet eius punctus eque primo tangat punctum sibi oppositum de linea girativa et secundum principia illius secte negare aliquem talem casum est condicio blasphemi, Dei omnipotenciam negantis. Et conformiter dicitur de tempore et instanti quod repugnaret Dei omnipotencie quod ipse non potest servare instans [p. 265] vel tempus per se quantumcunque sibi libuerit et per consequens Deus potest infinita tempora infinitum magna in instanti producere et quam cito sibi placuerit annichilare, sicut potest instans vel infinitum modicum tempus infinitum diu per se servare; et cum nullus nostrum sit consiliarius Domini noscens si sic facit, patet quod isti secte est ambiguum de quantitate duracionis cuiuslibet creature, vel Deus potest facere (ut inquiunt) quod et instans duret per infinitum multa tempora non communicancia quorum quodlibet sit infinitum magnum et potest facere quod omne sempiternum non duret nisi per instans vel horam ad maximum, quia Deus potest servare horam per se in perpetuum, secundum se totam; quia si oporteret aliquam partem eius umquam labendo deficere, tunc necesse foret quod in tempore finito tota hora deficeret, nec Deus posset servare tempus vel motum ultra suam naturalem periodum nec citra ipsum corrumpere.

[ENGLISH]

## ¶2 · 265.20–266.4

> [p. 265] Nec valet in ista materia allegare diffiniciones Aristotelis in hac parte, quia iuxta hanc sectam oportet dicere quod Aristoteles cum secta peripatetica et Augustinus cum multis sanctis diffiniendo accidencia blasfemarunt, ut ipsi asserunt quod nullum accidens habet esse aliud preter formaliter substancie inherere; terna dimensio corporis quod est longitudo, latitudo et profunditas, vel ipsa substancie magnitudo aut corporeitas non potest per se esse. Ista autem secta dicit quod hoc est hereticum, cum ista quantitas sit per se necessario sacramentum, et sic verecundaretur hec secta ex testimonio Aristotelis vel sanctorum doctorum quidquam describere vel aliquam per se [p. 266] differenciam assignare, ymmo nescit si de communi cursu nature Deus sic ordinavit, cum noviter ponit quidditatem et miraculum sacramenti altaris quod nec scriptura nec sancti doctores cognoverant.

[ENGLISH]

## ¶3 · 266.5–266.14

> [p. 266] Sed dimissis istis deliramentis sectivagis notandum quod eternitas, evitas et tempus sic differunt: Eternitas est permanencia Dei in se, quam Boetius describit quod est interminabilis vite possessio tota simul, et illa est prima mensura possibilis; unde denominat non solum naturam divinam, sed omnes relaciones in Deo, omnes ydeas et omnes eternas veritates in Deo ad intra, cum secundum racionem et non essencialiter distinguuntur a Deo; et ideo sunt eterna, quia sunt natura que est sine principio vel fine suo.

[ENGLISH]

## ¶4 · 266.15–267.3

> [p. 266] Secunda est mensura angelorum que vocatur evum vel evitas; et videtur michi quod quelibet tam spiritualis quam materialis essencia habet evitatem perpetuam, que est eius permanencia ante tempus. Angelus tamen quia habet visionem in verbo et in genere proprio que est permanens supra tempus, ideo habet secundum quandam excellenciam nomen evi. Unde quia angelus est primum perpetuum emanans ab eternitate divina, ideo eius permanencia vocatur eviternitas, et quot sunt angeli tot et plura sunt eva, cum alia sit evitas mensurans esse angeli et alia mensurans accionem eius intrinsecam secundum numerum speciei accionum que insunt angelis permanenter, sicut aliud est evum mensurans permanenciam hominis et cuiuscunque materialis essencie et aliud est tempus vel quando suum fundamentum in successiva [p. 267] transmutacione; et patet quod multa sunt eva que omnia reducuntur ad unum in specie non numero propter defectum unius subiecti in numero.

[ENGLISH]

## ¶5 · 267.4–267.22

> [p. 267] Tercia mensura est tempus quod est mensura certissima, quia numerus instancium mensurancium secundum prius et posterius motum mundi; quod est idem quod mundi duracio successiva; ipsum autem est ad omnem punctum mundi. Instans vero est mensura partis indivisibilis motus mundi; et sic tempus consequitur motum mundi in communi (ut sonant verba philosophi), Deus autem ex immensitate eternitatis est ante omne instans temporis et post omne instans et presens cuilibet instanti preterito vel futuro; tempus autem a mundi inicio usque ad finem mensurat ipsum per se primo quoad successionem et quandamlitatem que est mensura alterius generis quamlibet eius partem. Quando enim est illud quod derelinquitur ex adiacencia temporis (ut hic supponitur), et sic post diem iudicii erit idem evum mundi sine tempore; quod evum licet sit modo, tamen consideracione eius sopita attendimus ad tempus nobis magis sensibile.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 266.5: Definition of
- 266.6: 1. Eternity, which belongs only to God.
- 266.15: 2. Endlessness, (aevitas) the measure of angels.
- 267.4: 3. Time, the measure of the world.

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference 3. Time, the measurc of thc (267.4).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 263:
8. ABC: aliquid. 8 10. ABCE: et ul unum — duracionem decst.
12, i3. C quoad — magnum in marg. alia manu. 17. D: quanlumcunque
diu. i^. ABDE: qualibet. 22. A: diuturnitas in marg. alia manu.
?4. ABC: linias. 27. D: superficiales ; ib. D: vel tempus. 3i. I): elposl.
32. BD : vocant; ib. ABC: liniam; D : literam.

p. 264:
1. D: circumgirante ; ib. ABCD : oriens; ib. ABC: in decst.
3. D: tota species ; ib. D: annichilaretur. 5. D: D in tempore.
(3. E: D decst. 17. E: in deest; ib. A: manifeste ; alias manente in marg.
alia manu; BDE: manifeste; C: manente in rasura. 20. AC: diclum.
21. D:fit 23. D: incipiat 28. D : istius. 29. B: omnipotenlis :
ib. D : denegantis.

p. 265:
1. ABC: vel tempus deest. 3. D: instancia. 6. C: Domini deest.
9. DE: quod eciam; A: quod sequitur lacuna. 11. E: est ; ib. D: quan-
tum magnum. 12. D : quod esse. 17. ABC: scilicet tempus; C: erased.
18. D: nec circa. 21, 22. B: in hac — Aristoteles deest. 22. E: ponere
et dicere. 25. ABCD : esse aliquod. 26. C: est in marg. alia manu.
3o. E: per se et; ib. ABC: vendicaretur.

p. 266:
5. ABD: sectingis; E: secctanigis. 7, 8. E: diffinit. 9. C: est
in marg. alia manu. 10. B: revelaciones. i3. AB: et deest; C: alia
manu add. 18. C: est proprie. 21. C: secundum in marg. alia manu.
23, 24. A in textu eternitas extinct.; eviternitas in marg. alia manu.
25. C : mensurans essenciam.
7. Boethii, De Consol. lib. V, 6: Aliud interminabilis vitae
totum pariter complexam esse pcaesentiam . . .

p. 267:
1. AB: transsubslanciacione ; C: corrcxit. 3. proptcr ; A: semper
extinct. propter in marg. ; ib. B: sibi deest. 6. ABC: prius et per con-
scquens. i5, 16. ABC: quandalitatcm. 17. C: est alia manu.
18. ABC : cx iaccncia. 23. AB : non deest ; ib. ABC : essc ; ib. AB : fuisse;
C: correxit. 25. A: Deus alia mauu; ib. C: vcl alia manu. 3i. AB:
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 267: sicut cst.
```

---

## Chunk 08-j: write to `/Users/wilsonpruitt/wyclif/chunks/eucharistia/wyc-eucharistia-08-j.md`

### Scaffold

````markdown
---
chunk_id: wyc-eucharistia-08-j
work_la: Tractatus de eucharistia
work_en: On the Eucharist
volume_slug: eucharistia
editor: Johann Loserth
year: 1892
pages: "267.23–272.11"
divisions: "cap. 8 (heading 'CAPITULUM OCTAVUM.' at 232.0); part 10 of 10, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against the vote)
witnesses: [iohanniswyclifd00losegoog, iohanniswyclifd01losegoog, iohanniswyclifde12wycl, latinworks13wycl]
check: "1172 words; 1162 confirmed by the vote; 10 runs stood by rule; 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks13wycl, leaves n338–n343 (printed p. = leaf − 71)"
status: draft
---

# *De eucharistia*, chapter 8, part 10: [TITLE]

## ¶1 · 267.23–268.9

> [p. 267] Ulterius notandum quod non esset fuisse vel fore nisi racione temporis et per consequens subducto omni tempore Deus non fuit vel erit sed est absolute necessario. Et sic in eternitate non est formaliter hec differencia, et per consequens cum Deus et sua eternitas, angelus et sua evitas fuerunt et erunt, oportet quod capiant illas denominaciones eis accidentales a tempore et sic habent quando; quod non presupponit in eis naturalem periodum sicut creature naturaliter [p. 268] corruptibiles, et ita Deus equivoce fuit et erit in comparacione ad naturas corruptibiles, sicut alia respectiva accidencia equivoce sibi insunt. Idem ergo tempus in numero mensurat eternitatem Dei, evitatem angeli et sic de aliis supra tempus quoad denominacionem respectivam qua tempore mensurantur Et ita videtur quod non propterea tempus aliud sed alia quandalitas sine mutacione essencie est ponenda. Ista autem hic sufficiunt.

[ENGLISH]

## ¶2 · 268.10–271.24

> [p. 268] Sed redeundo post digressionem ad difficultatem tactam de multiplicacione videtur quod secunda sentencia sit tenenda; cum enim inpossibile sit idem corpus multiplicari situaliter vel dimensionaliter per diversa loca et tam fides de eukaristia quam eciam communis philosophia docet esse multiplicacionem substancie, patet veritas secunde sentencie. Vocatur autem multiplicacio, quando eadem res creata est simul in tempore per multa loca secundum se totam, ut anima, universalia et instancia; tempus autem non sic multiplicatur, cum omni loco pro quocunque instanti partes sue defuerint ut partes preterite et future; potest tamen extense loquendo concedi multiplicari, quia secundum multas partes suas est per diversa loca et sic commune lumen, communis species, vel similitudo rei multiplicatur, quia per unum magnum situm est et per quamlibet eius partem secundum aliquod eius suppositum, sicut universale et ubicunque habuerit aliquod singulare. Si autem quodlibet tale singulare habuerit esse per quamlibet partem dati situs, tunc et illud singulare multiplicatur per situm eundem, sicut ponitur de speciebus visibilis. [p. 269] Deus autem non potest multiplicari, quia necessario est secundum se totum ubique; nec potest aliquo loco vel tempore diffinire vel secundum motum sui alicubi esse; ideo ex parte sui non contingit multiplicacio vel secundum tempus diffinicio. Nam secundum sanctos non est in eo formaliter multitudo, alia autem licet sint ubique scilicet mundus, tempus et universalia quorum individua sunt, ubique tamen dispariter a Deo; nam mundus non secundum se totum est ubique, quia non quelibet eius pars quantitativa ubique distenditur, nec quelibet pars subiectiva generis corporis vel universalis huius est ubique, nec tempus habet omnes partes suas simul pro eodem instanti, sed quadam dependencia ex motu aliter est in celo et aliter in terra. Deus autem secundum immensitatem suam primo et per se replet omnem locum et secundum eternitatem suam primo et per se est per omne tempus; non potest contingere variacio ex parte sui in essendo per locum vel tempus sed oportet quod sit variacio in substancia creata; cuius variacio vocatur accidens, ut Deus per se efficienter replet omnem locum et corpus, vel eius principium per se formaliter replet locum, sic quod punctale materialis essencie cum non possit maiorari vel minui est per se punctale, cuius punctalitas est punctus; et sic de quantitate corporis que consequitur ad suum primum subiectum, sicut risibilitas ad hominem et secundum racionem qua Deus immobilis ponit substanciam materialem secundum racionem immobilem, cuius situacio vel locacio est situs vel locus quem Aristoteles vocat inmobile primum. Deus enim non posset movere illam racionem secundum primum motum qui est motus localis. Et hec est prima racio immobilitatis sensibilis qua ascendimus ad cognoscendum inmobilitatem [p. 270] ultimam Dei nostri; et cum videmus rem moveri de loco ad locum ex ordinacione Dei, vocamus illam vicissitudinem motus tempus vel duracionem, et individuamus locum et tempus a genere substancie vel motus cum aliis circumstanciis individuantibus quas Deus ad hoc ordinat. Et sic videmus dominum nostrum in omni vicissitudine creature. Et sicut Deus est primo magnus et immensus per se efficaciter et finaliter replens locum, ita est primo per se durans et eternus, per se finaliter mensurans omnium temporalium vices, et sic inmensitas et eternitas Dei non sunt accidencia vel divisibiles (ut hic supponitur); et sicut cum Deus non potest esse alius Deus, ita per eundem situm punctalem non potest esse simul alius punctus vel materialis essencia, cum tota capacitas sua repletur, quia non est aliud nisi illam materialem essenciam situari vel saltem aliam tantam aut tantam speciem quantitatis. Cum autem forma substancialis aut accidentalis non sit nisi talem essenciam informari, patet quod non exinde multiplicatur situs replecio. Loquor autem de situ vel loco (ut supra), ut dicit materialem essenciam situari. Et patet logicis quod aliud est Petrum esse in loco sibi adequato et aliud est ipsum esse per locum sibi adequatum. Cum enim sint mille loca inter ipsum et celum sibi equalia, quia ut sunt laciora sunt magis tenua, et omnia ipsum undique circumstancia, patet quod est in totidem locis sibi equalibus et per consequens adeo sibi adequatis, et tamen per nullum illorum locorum est, cum per nullam partem talis loci sit aliqua pars Petri cum a quolibet tali distat, ideo longe aliud est Petrum esse in multis locis sibi adequatis et aliud est ipsum [p. 271] esse per multa loca sibi adequata. Est enim per locum, quando ad aliquam partem illius loci signati est aliqua pars sui, sicut omnis materialis substancia per locum diffunditur, qualiter repugnat idem corpus in numero per distancia loca simul distendi; potest tamen distendi in uno loco et habere aliud esse spirituale in alio tamquam in signo aut virtute, sicut dictum est de rege. Et sic patet de corpore Christi, quod est dimensionaliter in celo et virtualiter in hostia ut in signo. Sed in isto est magna dissensio de modo essendi corporis Christi in hostia: Quidam enim dicunt quod corpus Christi est tantum secundum essenciam suam ibi presens; quod tantum diffinitur loco hostie quod posset esse illo modo ibidem et alibi nusquam esse, sed alii admittunt hoc, quia foret Deo longe facilius quam servare accidens sine subiecto, ideo super illos iacet difficultas, quomodo multiplicatur cum corpore Christi quantitas et alia accidencia committantur. Super nos autem non iacet difficultas ista: Esto quod corpus Christi sit in sacramento panis, aut virtus et non corpus Christi quod in celo extenditur, sic quod corpus Christi non est non corpus, sed est non corpus Christi ibi; et est illud quod ibi extenditur sed non ibi extenditur.

[ENGLISH]

## ¶3 · 271.25–272.11

> [p. 271] Et iste est tercius punctus in quo vario a modernis, verumptamen (ut sepe protestatus sum) volo parate obedire docto quod quantum ad veritatem illius materie fuero sive superfluus, sive parcus. Miratur autem mundus quomodo post dotacionem ecclesie vel variaretur sacramentum vel innotesceret nostris plus a Christo extraneis vel racio vel fieret revelacio plus quam Paulo et sanctis prioribus. Sic enim tanquam domini leges Christi possent extraneare totam fidem [p. 272] catholicam. Nec dubium quin veritas catholica fuit per auctores scripture sufficienter edocta, licet officium ecclesie peregrinantis cui Deus dedit scienciam sit detegere fidem in scriptura implicita, quando pullulant errores circa eius sensum. Et nunquam est per illos aliquod novum fidei catholice fabricandum; et hinc Deus semper ordinat aliquos qui intendant loyce et sensui scripture, cum tamen debet credi cuicunque pontifici in istis, de quanto validius adduxerit testimonium scripturarum; et notum est eos post dotacionem ecclesie in isto sicut in moribus defecisse.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 267.23: Past and future are founded in time. God neither was nor will be, but is eternally.
- 268.10: Multiplication is a thing's being as a whole in many places at once.
- 269.1: It cannot be predicated of God, who is necessarily every where.
- 271.8: How Christ is present in the host.

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference 3. Time, the measurc of thc (267.4).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 267:
1. AB: transsubslanciacione ; C: corrcxit. 3. proptcr ; A: semper
extinct. propter in marg. ; ib. B: sibi deest. 6. ABC: prius et per con-
scquens. i5, 16. ABC: quandalitatcm. 17. C: est alia manu.
18. ABC : cx iaccncia. 23. AB : non deest ; ib. ABC : essc ; ib. AB : fuisse;
C: correxit. 25. A: Deus alia mauu; ib. C: vcl alia manu. 3i. AB:

p. 268:
I. C: corporales in textu ; corruptibiles in marg. alia manu; ib. AB:
sic ita ; ib. C: vel erit. 4. E: eviternitatem. i3. C: situaliter in marg.
alia manu; D: signanter. i5. D: multitudinem. 16. A: substancie in
textu extinct. ; in marg. : sentencie. 17. D : quod eadem. 19. ABCE: et
deest. 21. ABC: defuerunt. 24. D: sic racione luminum ; ib. E: gravis
syeciei. 27. D: tempus suppositum ; ib. ABC: est ubicunque. 3o. D : sin-
gulariter.

p. 269:
2. A : ubique in marg. alia manu. 4. D : aliter esse. 18. ABC : varia-
cionem. 21. D : efficaciler. 28. E: immaterialem. 3i. B: monere deest.
33. E: prima causa.

p. 270:
l. ABD: videmus removeri. 2. E: ad locum deest. 4. E: vel
individuamm ; ib. D: et deest. 7. E: Et sic. 8. ABC: efficienter.
i3. C: ita alia manu. 14. E: punctualem. 17. E: vel tantam.
19. DE: vel. 21. ABCD : Loquitur. 22. ABCE: loycis. i3. AB: sibi
deesl. 20. C: ut deest; ib. D: lociora ; ib. AB : tenuia. 3i. C: a \\\
marg. alia manu: ib. ABC: Petrus. 32. D: est deest.

p. 271:
2. D: aliam. 8. ABC : Et sic. 9. B: vel in. 10. ABC : ista.
14. C: esse in marg. alia manu; ib. DE : isto esse. 19. C: committanter ;
ib. ABC: ant non; E: autem deest. 20. DE: Esto deest; ib. DE: quia ;
ib. DE: est. 27, 28. E: materie sim. 29, 3o. E: varietur. 32. E:
tamquam diu.

p. 272:
2. ABC: satis edocta. 4. E: protegere. 9, 10. E: in testimonium.
18. ABDE: decretales; C: correxit. 19. D: CCCXV. 23. ABCE: gravis.
24. ABD: primo ; ib. E: que deest. 26. ABCD : quod deest. 29. D:
19. Gf. Martini Chronicon Monum. German. Scriptorcs
tom. XXII, 438: In quo fuit . . . summa prelatorum i3i5.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 267: sicut cst.
p. 270: Et sic videmus dominum nostrum in omni vicissitudine creature.
p. 272: tali dubio.
```
