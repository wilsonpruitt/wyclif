# Translation brief: ecclesia 16-d–16-f

You translate these 3 chunk(s) of Wyclif's *Tractatus de ecclesia* in a single pass. Everything you need is in this file:
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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-16-d.md chunks/ecclesia/wyc-ecclesia-16-e.md chunks/ecclesia/wyc-ecclesia-16-f.md` once and fix what it reports.
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

# TRANSLATOR CARD — one *De ecclesia* chunk

This card replaces reading CONVENTIONS, the pilot and Thakkar in full: it is their working core.
Adapted from `chunks/dialogus/CARD.md` (2026-10-01). Read it, then `GLOSSARY.md`, then your
scaffold (or your brief, which carries all three). Consult CONVENTIONS.md only when the card sends
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

*Tractatus de ecclesia*, ed. Johann Loserth (Wyclif Society, 1886), from the plates of archive.org
`latinworks10wycl` (**leaf = page + 37**). Written 1378–79, after Gregory XI's bulls against *De
civili dominio*, as the Schism opened. A **treatise**, not a dialogue: Wyclif speaks in the first
person, states conclusions, raises objections against them (*instatur*, *obicitur*, *arguitur*) and
answers them (*dicitur*, *respondetur*). Its subject is what the church *is* (the number of the
predestinate), and from that, headship, membership, the pope, endowment and sanctuary.

**Sigla** (Loserth): **A** Vienna, ÖNB Cod. Pal. 1294 (his base); **A₁** Vienna 3929 ("almost wholly
valueless"); **B** Prague, University Library X.D.11, whose early reader's marginal glosses Loserth
prints ("B in marg: …"); **D** Dublin, TCD C.1.23 (chapter 7 only). Cite variants with these sigla.

**The page foot** (in your brief as "apparatus", by page) has two blocks, both keyed to the line:
the variants (`26. AA₁: tamen ex.`) and Loserth's source references (`27. Decret. Unam sanctam.
Extrav. comm. lib. I, tit. VIII, cap. I.`). The OCR of it is rough: read it for sense, not letter by letter.

## The job

The Latin in your scaffold is **established and frozen** (three-witness vote + plate reading). Fill
`[TITLE]` (short, lower case: "headship: the pope is not head of the church"), each `[ENGLISH]`, the
notes and the transcription notes; set `status: translated`; lint; report.

- **Headings:** keep `## ¶k · range` exactly. **Never change a range; never split a paragraph.**
  (The pilot headed its paragraphs with Loserth's alinea letters A, B, C; the scaffolds do not
  carry them, so leave the ¶ numbers.)
- **Never alter the Latin.** A word that looks wrong: read the apparatus for that line first; then,
  if still doubtful, the plate (`text/ecclesia/raw/leaves/nLEAF.jpg`, LEAF = page + 37 padded to four digits: p. 1 = `n0038.jpg`). A variant
  that gives the sense → translate it + **T** note citing the siglum; a compelling emendation →
  translate it + **T** note "(our emendation)"; neither → translate the print and flag it. Never
  smooth nonsense into sense. Report every such case. **Loserth's printed text governs** (ruled
  2026-10-02): translate it, his own emendations included, unless it will not construe; a manuscript
  reading is chosen only then, and **A₁ alone never outweighs the print**; every departure gets a T note
  giving both readings. Open flags for this volume:
  `text/ecclesia/PLATE-FLAGS.md` (read it if your pages are listed there).
- **English layout:** `[N]` at the same word as `[p. N]` in the Latin (the chunk's first `[p. N]` is
  implicit). Supplied words in `[brackets]`, sparingly. Quotations in quotation marks: Loserth
  italicises quotations, but the scaffold does not carry italics (`italics: none`), so find quoted
  matter by sense and by the source references at the page foot.
- **Formulae of the disputation** (GLOSSARY §C, ruled 2026-10-01), rendered the same way throughout: *instatur* "it is objected" ·
  *obicitur* "it is objected" · *arguitur* "it is argued" (with *per*: GLOSSARY) · *dicitur* "it is
  said" (in an answer: "the answer is") · *respondetur* "the reply is" · *conclusio* "conclusion" ·
  *antecedens / consequens* "antecedent / consequent" · *consequencia* "inference", ⛔ never
  "consequence" (GLOSSARY §C).

## The four error classes (Thakkar) — check every sentence

1. **Terms:** GLOSSARY.md governs, one term one rendering. Tag the **first occurrence in the chunk**
   of every §A–C term: `[quiddity]{g:quiditas}`. The key must exist in GLOSSARY.md. A term that looks
   technical but has no row: render it sensibly, untagged, and propose it in your report.
   **CONTEXTUAL** rows hold two senses English splits: choose by context and write a **C** note at
   the first occurrence in the chunk and wherever it leans to the other sense (the dikaiosune rule,
   CONVENTIONS §6).
   Key rulings for this volume: *ecclesia* church (**lower-case**) · *ecclesia militans / triumphans /
   dormiens* the church militant / triumphant / sleeping · *quiditas* quiddity · *caput* head ·
   *membrum* member · *predestinati* the predestinate · *presciti* the foreknown · *papa* pope ·
   *vicarius Christi* vicar of Christ · *sponsa* bride · *caritas* charity (never love) · *dominium*
   lordship · *viator* wayfarer · *patria* homeland · *ex fide* as faith teaches (with a genitive:
   "from the faith of scripture") · *sentencia* teaching · *evidencia* evidence (the rest: GLOSSARY).
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
   | per idem | by the same token | "in the same way" |
   | ymmo | indeed, rather (correcting upward) | (omitted) |
   | patet; constat | it is clear; it is evident | |

   "Now" is reserved for the minor premiss, or the step that brings a new premiss to bear (*Illos
   autem parentes debemus …*, 1.17). An *autem* that only extends the same step is "and" (*Illis autem
   cultis …*, 1.19).
3. **Ordinary words with a medieval sense:** GLOSSARY §D; look up any word whose classical and
   Wyclifite senses may differ, and propose additions.
4. **Syntax:** construe before rendering (main verb, subject, what every relative and genitive
   hangs on). Keep quantifier order where it is meaning (*nullus papa … caput*; *quilibet papa*).
   Keep Wyclif's long periods where English tolerates them. **A doubtful construal is never chosen
   silently:** translate the likelier reading and write a **C** note giving the alternative.

## Scripture

`python3 scripts/w3/bible.py "Luc 17:23"` (Vulgate + Douay–Rheims; psalms in Vulgate numbering) or
`python3 scripts/w3/bible.py --find "nolite ire neque sectemini"`. Where Wyclif's Latin agrees with the
Clementine Vulgate, use the **Douay–Rheims wording**. Where he departs, translate *his* Latin and write
an **S** note giving the Vulgate. Modern references in the English (Luke 17:23). The chapter numbers
are Wyclif's, the verse numbers Loserth's (the headnote says so once).

## Notes

- `[^n]` from 1, the marker placed in the same edit as its note, each opening with a type letter:
  **T** text · **C** construal · **G** glossary (passage-specific only; otherwise a tag) · **S** source ·
  **R** reception/context (e.g. a B marginal gloss that shows how an early reader construed the text,
  CONVENTIONS §4; Hus's reuse where Loserth notes it: "cf. Hus, De eccl.").
- **Density: about one note per 70–100 Latin words**, fewer where the text is plain. Short, factual,
  says what the Latin does and stops. No modern theology, no evaluation.
- **Every identification** other than scripture checked with bible.py gets a ledger row in your
  report with a status: `editor` (Loserth's source reference at the page foot), `to-verify` (from
  memory: every patristic or canon-law identification you did not read in this session), `verified`
  (you read the source text this session: say where; local PL at `~/patrologia/sources/pl/tei/`).
  ⛔ Never pass memory off as verified. Id `E<chunk>-<n>` (`E02a-1`), cited in the note:
  "(LEDGER E02a-1)". Loserth's references to the *Corpus iuris canonici* (Decretum, Extravagantes)
  are `editor`; give them in modern form (*Extrav. comm.* 1.8.1) and say the form is ours.

## The pilot (`pilots/wyc-ecclesia-01a.md`, pp. 1.1–5.13)

A reviewed model of register and note style, read for that. Two cautions: its Latin was established
before the re-extraction (**your scaffold's Latin governs**), and it predates some GLOSSARY rulings
(**GLOSSARY governs**: e.g. the pilot's "by faith" for *ex fide* becomes "as faith teaches"). Its
ledger rows are V-01…V-19 in `LEDGER.md`. **Chunks 01-a and 01-b** fall inside the pilot's pages:
start from the pilot's English and notes for those pages, bring them into line with your Latin, the
card and GLOSSARY, keep its ledger ids, and say in your report what you changed. **01-a** also fills
`## Headnote` from the pilot's headnote, keeping each `[verify]` until its ledger row is verified.

## Side-notes

Already read against the plates (WORKFLOW 5; 1,293 notes, `text/ecclesia/sidenotes.fixed.tsv`) and
placed in your scaffold's section. ⛔ Do not edit them. One that is plainly wrong (garbled, or at
the wrong line): report it under Latin doubts as `side-note page.line`.

## Finish

1. `status: translated` in the front matter (nothing else changes there).
2. `.venv/bin/python scripts/w3/lint.py chunks/ecclesia/<your chunk>.md` until clean.
3. The four-class check above, sentence by sentence.
4. ⛔ Edit **only your chunk(s)**. No git, no other files. Everything shared goes in your report.

## Report (≤ 200 words per chunk, exactly these heads)

- **Chunk:** id, Latin words, notes.
- **Ledger rows:** in LEDGER.md's table format `| id | chunk / note | claim | status | how / next step |`.
- **Glossary proposals:** Latin · proposed English · where · why.
- **Latin doubts:** page.line · printed · suspicion · settled on the plate?

## Glossary (the 188 rows these chunks use; the full file is GLOSSARY.md)

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
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| expropriacio | renunciation of property | Never "expropriation" (seizure). Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |
| vicarius Christi | vicar of Christ | The card's ruling, now a row. Ruled 2026-10-02. |
| elemosinans | almsgiver | The participle of *elemosinare*: the donor. Ruled 2026-10-02 (*Eccl.* 13). |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| regnum | kingdom | Every sense: the political state as well as the kingdom of God and scripture's kingdoms. Not "realm". Wilson, Ruled 2026-09-28 (27 sites). |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| familia | household | A great man's retinue. Ruled 2026-09-28. |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| ditare | to enrich | Kept apart from *dotare*, endow. Ruled 2026-09-28 (coordinator, delegated) (21 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| brachium seculare | the secular arm | Ruled 2026-09-28 (coordinator, delegated) (7 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| patronus | patron | Of a benefice. Ruled 2026-09-28 (coordinator, delegated) (13 sites). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| legalitas | legal standing | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| citare; citacio | to cite; citation | Summons to a church court. Ruled 2026-09-28 (coordinator, delegated) (12 sites). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| conducentes | those who hire them | Ruled 2026-09-28. |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| insolubilia | insolubles | The logicians' paradoxes of self-reference. Ruled 2026-10-02 (*Eccl.* 175.11). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| franchisia | franchise | Ruled 2026-10-02 (*Eccl.* 239.22). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |
| autenticus / autenticacio | authentic / authentication | The key term of *Eccl.* 13. Ruled 2026-10-02. |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| practizare | to put into practice | Ruled 2026-09-28 (coordinator, delegated) (4 sites). With *contra* + person, "practise against" (plot), *Dial.* ch. 17. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
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
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| laureola | aureole | The theologians' special crown (of virgins, martyrs, doctors). Ruled 2026-10-02. |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| cautela | wile | Not "caution"; *cautela diaboli*, the devil's wile. Ruled 2026-09-28 (8 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| impresenciarum | nowadays, at present | (T. p. 366) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| ditarius | almsman | The one enriched by the alms (cf. *ditare*, §B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "almsman" (the 09-28 row governs; conformed 2026-10-02, *Eccl.* 16). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| redempcio temporalium | redemption of the temporal goods | Chapters buying back seized goods. Ruled 2026-10-02 (*Eccl.* 15, 340.15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| ablatarius | the one from whom it is taken | Beside *ablacio* "taking-away". Ruled 2026-10-02 (*Eccl.* 15, 343.7). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| legii | lieges | Ruled 2026-10-02 (*Eccl.* 15, 343–344). |
| redempcio (of a sentence) | redemption | Buying off a penalty; kept apart from *redempcio temporalium*. C note at first use. Ruled 2026-10-02 (*Eccl.* 15, 352.1). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |

---

## Chunk 16-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-16-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-16-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "368.29–372.1"
divisions: "cap. 16 (heading 'CAP. XVI.' at 359.5); part 4 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "713 words; 655 unanimous or majority-real; 48 settled by vote (R2 31, R3a 8, R5a 8, R6a 1); 10 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n405–n409 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 16, part 4: [TITLE]

## ¶1 · 368.29–370.14

> [p. 368] Si, inquam, cum talibus exhortacionibus evangelicis securius procurasset Silvester pro futura ecclesia, tunc verisimilius plus profuisset utrique parti, sicut beatus Leonardus plus profuit regi Francie retrahendo ipsum ab affeccione mundana per hoc quod renuit officium [p. 369] presulatus, quam fecisset in retinendo illud officium procurando a rege dimidium regni sui. Ideo fecit conformius ad evangelium et (sicut credo) utilius utrique parti ecclesie, quam fecit beatus Silvester recipiendo illam cartam a cesare, sicut innuit cronica de voce angeli dicentis quod in die illius dotacionis diffusum est venenum in ecclesia sancta Dei. Nec est carta cesaris magis credibilis quam ista cronica, ymmo evidencius est ex fide scripture et lege ecclesie quod Nabuchodonosor qui destruxit synagogam et sacerdotes Jerusalem sit salvatus, quam quod Constantinus salvabitur, quia primum asserit decretum cum Augustino ex testimonio scripture, sed secundum relinquitur insuasum. Sed arguit doctor quod Silvester tenebatur de necessitate salutis recipere dotacionem predictam cesare eo quod spolians christianos bonis suis tenebatur eis restituere. Sed si evidencia ista procederet, moveret primo credere quod Constantinus propter defectum plene satisfaccionis fuit dampnabilis, secundo cum beatus Silvester debuit sub pena mortalis restitucionem illam recipere, sequitur quod totum imperium principaliter debebatur Romano pontifici, et per idem, extincto quolibet seculari capitali domino cuiuslibet regni, episcopus debet esse eius civilis dominus capitalis, ut deductum est et improbatum priori capitulo. Tercio sequitur quod Christo et cuilibet eius vicario debetur principaliter dominacio secularis, cum aliter posset cesar renunciasse toti civilitati et distribuisse bona pauperibus, sicut fecerunt sanctus Thomas apostolus et sanctus Laurencius; nam dato opposito non oportuit quod cesar resignasset Silvestro imperium, et per consequens non oportuit sub pena mortalis beatum Silvestrum illam dotacionem a cesare recepisse. [p. 370] Unde ego credo quod meritorius fuisset utrique parti quod distributa fuissent bona pauperibus, et ordinatum per laycos ministerium continuum in subsidium egenorum; tunc enim posset clerus stare in suo gradu vivendo exproprietarie sicut primo, et ablata confederacione, assecuracione et occupacione cum mundo cresceret undique fructus cleri. Nec est credendum quod ad satisfaccionem tyranni requiritur ut det clero dominacionem civilem, sed oportet quod satisfaciens capitali domino iuvet suam ecclesiam, aliis ut egentibus conferendo, et superhabundantibus vel abutentibus subtrahendo. Sic enim dicitur Nabuchodonosor ex maiori evidencia quam nostrum cesarem meruisse.

[ENGLISH]

## ¶2 · 370.15–370.29

> [p. 370] Quinto arguitur per deducens ad familiare inconveniens scilicet: Si beatus Silvester peccavit in recipiendo dotacionem ecclesie in perpetuum, sequitur a pari quod collegia nostre universitatis verisimiliter peccarent in recipiendo temporalia pro sustentacione perpetua pauperum clericorum; et ita sequitur quod tam clerici domini Wyntoniensis quam alii collegiati tenentur non perpetuari, et per consequens monere patronos ad dissolvendum privilegia perpetua, ut est de privilegiis perpetuis concessis universitati nostre a rege, et sic de cantariis et aliis elemosinis perpetuis. Revocetur, inquit, ista heresis, cum extingueret devocionem populi, elemosinas perpetuas clericorum, et per consequens cederet ad detrimentum maximum pauperibus in futurum.

[ENGLISH]

## ¶3 · 370.30–372.1

> [p. 370] Hic dico primo quod consequencia non procedit, cum homo potest facere nedum bonum de genere, sed bene moraliter et tamen cum hoc et in hoc peccare venialiter, ut ista pars habet dicere in familiariori [p. 371] exemplo. Nam dominus Symon Hyslep archiepiscopus Cantuariensis fundavit unum collegium in Oxonia plus pia intencione, ut evidencius creditur quam de fundacione cuiuscunque abbathie in Anglia, et ordinavit quod in ea sub forma laudabili studeant ad utilitatem ecclesie pure clerici seculares, quod et factum est. Et cum ipso mortuo symoniace cum commentis mendacii eversum est tam pii patroni propositum et illis expulsis pauci alii non egentes sed diviciis affluentes irregulariter introducti contra decretum captum ex dictis beati Jeronimi, positum XIIª q. II: Gloria episcopi est pauperum opibus providere, ignominia sacerdotis est propriis studere diviciis. Et cum pretextu illius fuci sophistici episcopus et suum capitulum sunt una persona a qua non licet alienare bona illius ecclesie, ista persona vendicat bona illius collegii proprietarie possidere. Unde consulendum videtur domino Wyntoniensi ut caveat hanc cautelam. Credo autem quod dictus Symon peccavit fundando dictum collegium, sed non tantum quantum Antisymon qui ipsum dissolverat, sed ut credo nunquam fuit ecclesia appropriata in Anglia vel possessio in perpetuam elemosinam mortificata quin appropriacio sapuit peccatum altrinsecus. Ulterius pro materia argumenti affectarem, si Deus decreverit quod non foret in regno nostro talis ecclesiarum appropriacio vel reddituum temporalium mortificacio, sed quod totus clerus vivendo pure exproprietarie de decimis, oblacionibus et privatis elemosinis sit contentus; quamvis enim illud non dixerim per modum conclusionis, sed per viam condicionis et [p. 372] imprecacionis, tamen eius racionabilitas suaderi potest

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 369.1: St. Leonard's example is better than Silvester's.
- 369.15: The doctor argues that Silvester was bound to accept restitution from Constantine.
- 369.24: This implies imperfect restitution on Constantine's part,
- 369.29: and a duty in the Pope to bear civil sway.
- 370.15: Objection: 5. If perpetual alms are wrong our colleges ought to be dissolved.
- 370.30: Answer: An act may be good, yet touched with venial sin.
- 371.1: Example of Archbishop Islip and his college,
- 371.19: dissolved by Archbishop Langham.
- 371.25: I should be glad to see all appropriations and endowments come to an end.
- 372.1: 1. The clergy 1 would then live as Christ t ordered.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 369: *presulatus* (180b folio mark and H alinea letter are not text) [R3]
  - 369: *defectum* (2 is the margin argument numeral) [R4]
  - 370: *arguitur* [R3]
  - 370: *cum* [R3]
  - 370: *in* [R3]
  - 371: *XIIª* [R3]
  - 371: *foret* [R3]
  - 372: *imprecacionis* [R3]
  - 371: *exemplo* (180c folio mark glued) [THIN]
  - 371: *et* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 368:
i3. A: reduplicacione sive reduplicative. 21. B: mundanos in
proprietatem. 29. A in marg. : Nota defectus beati Silvestri (Above
iSob without mark of reference).

p. 369:
„ . . . _ , • Nabuchodonosor.
2. B: pro crcando. 10. A in marc. : Salvacio <~ _ . .

p. 370:
3. B: continuum deest. 6. B: et assecuracione. II. 12. B:
ab utentibus trahendo. i5. A in marg. : Quinta racio 22. B:
tenentur velle non. 24. 25. B: nostri a rege. 26. extigueret
in codJ. 3o. A in marg : Responsio.

p. 371:
io. B: irregulari introducti. 25. A in marg. : Conchisio. Contra
dotacionem (lielow i8oc without mark of reference).
i. Comp. Lechlcr, Johann von Wlclif tom. I, pp. 204, 3o3.
12. Decreti II pars, causa XII, q. II, cap. LXXI.

p. 372:
i3. A in marg. : Augustinus. 19. B: Hmitando eque. 24. A
XXII cap. corr. in marg. 26. B: populua. 27. B: Tercio
conlirmatur cx.
```

---

## Chunk 16-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-16-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-16-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "372.2–376.28"
divisions: "cap. 16 (heading 'CAP. XVI.' at 359.5); part 5 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1112 words; 993 unanimous or majority-real; 95 settled by vote (R2 58, R3a 33, R5a 4); 24 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n409–n413 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 16, part 5: [TITLE]

## ¶1 · 372.2–375.2

> [p. 372] Primo per hoc quod ecclesia cleri vixit sic expropnetane ex ordinacione Christi et apostolorum usque ad dotacionem cesaream; sed et usque hodie in plus religiosis clericis remanet illa vita, et illam conversacionem declaravi superius esse plus autenticam, plus meritoriam et securam. Secundo ex hoc quod stat minando destruccionem regni superhabundare multitudinem clericorum, ut docet Apostolus I, Cor. XII°, in exemplo de corpore humano, quod foret nimis monstruosum, si totum, medietas vel tercia foret oculus. Cum ergo omne utile ad regimen rei publice secundum Augustinum, II° De Doctrina Christiana, in fine, sit reperibile in scriptura, videtur quod in scriptura fundabilis sit regula secundum quam in populo proporcionaliter sit de clero, nec inveniet homo regulam reccius directivam quam ministrando clero secundum formam quam ecclesia primitiva instituit, et limitando eis officium quod tunc gessit. Ergo hoc foret conveniens racioni. Si enim in veteri testamento, quando sacerdotes et Levite onerati erant importabiliter cum disposicionibus bestiarum ad victimas, limitati sunt ad istam porcionem triplicem (ut dixi superius XIII° cap.), multo magis in tempore legis gracie, quando clerus alleviatus ab oneribus legis debet esse? pauperior, et populus ad relevandum est prompcior. Tercio arguitur ex precavicione inconvenientis multiplicis quod taliter tolleretur; primo, inquam, non aspiraret tanta multitudo ad sacerdocium plus propter affeccionem ad seculum quam ad sacerdotale ministerium. Secundo non foret tanta mercacio symoniaca nec tanta contencio et vulpina confederacio sicut modo, et ista conturbant regna plurimum. Tercio brachium seculare non tantum necessitaretur pugnare [p. 373] pro bonis fortune ut modo, tum quia ex uno latere universitas temporalis dominii saciaret, tum eciam quia clerus vivens apostolice eorum tyrannidem mitigaret. Quarto quia seculares sic magis disponerentur ad magis ordinate imperciendum elemosinas magis dignis et plus paterent discolorum latebre que hodie in evestimentis ovium sunt occulte. Quinto quia elemosine limitate clero ad distribuendum pauperibus forent in manu layca equius distribute. Notet, inquam, speculator primo bona regni devoluta ad manum mortuam, notet secundo subtraccionem partis eorum proporcionalem numero et vite procuratorum pauperum et notet tercio quomodo residuum est expensum. Dicitur enim quod fratres peregrini et alii egentes tantam elemosinam recipiunt de exteris ut de illis. f Sexto quia secularibus occupantibus illa bona iam incarcerata tamquam suis (ut convenit) foret terra magis fructifera, plus habundans bestiis et aliis bonis fortune et ad defensionem regni ac augmentum exercitus christiani amplius populosa. Sic enim contigit ante dictam dotacionem, et racio probabilis sumpta ex facto cum eius circumstanciis contestatur. Deus enim non fundit aquam pluvie differenter per gurgites sed guttatim et roride facit ad nutrimentum terre nascencium pluviam distillare, docens nos per hoc indubie omnia genera bonorum nostrorum sine personarum accepcione prudenter dispergere, et sic (si non fallor) ista expropriacio excitaret devocionem populi, prepararet ad elemosinas perpetuas cleri Christi, et per consequens cederet in relevaminis pauperum notabile incrementum. Unde quod ecclesie et redditus regni sic sunt appropriata collegiis, error appropriacionis ecclesiarum abbathiis illud fecit; ex hinc enim tollebantur rectores et eorum clerici qui augerent [p. 374] universitates et clerimoniam regni nostri, eo quod vel divise sunt ecclesie vel cognatis et familiaribus patronorum clericorum infideliter distribute, sic quod nisi Deus reliquisset nobis semen in fundacione collegiorum ex licencia regum Anglie quoad clerimoniam quasi Sodoma fuissemus; melius tamen foret quod quilibet collegiatus aptus ad regimen animarum haberet ecclesiam que iam appropriatur monasterio cui pastum spiritualem et sacramenta debite ministraret. Tunc enim prosperaretur regnum in corporalibus et spiritualibus et cresceret universitas nostra tam numero quam virtute; in cuius signum ante catheclismum appropriacionis huiusmodi erant in Oxonia sexaginta milia scolarium, ubi hodie non sunt tria. Universitas eciam plus crescit hodie per presbiteros mobiliter conducticios, quam crescit per perpetuas cantarias, nec oporteret habere tot privilegia a rege nisi quia ob defectum sacerdotum et supplantacionem privilegiorum laycorum per clericos layci eis propter sensacionem iniurie oppido sunt infesti. Olim autem non fuit sentencia ista heretica ante dotacionem ecclesie, quando in ea floruerunt catholice veritates. Ymmo (si non fallor) sonaret ad emendacionem ecclesie et ad stabilimentum regni et ad profectum cuiuscunque membri ecclesie tam vivi quam mortui quod proviso cuilibet clerico secundum ordinem suum de necessario [p. 375] nutrimento et tegumento ista conclusio sit paulative et provide practizata.

[ENGLISH]

## ¶2 · 375.3–375.20

> [p. 375] Sexto arguitur, sumendo quod principes et domini temporales licite et absque peccato vendunt terras et tenementa sua viris ecclesiasticis et suis successoribus in perpetuum, ergo a forciori conferrent eis temporalia in perpetuum; et assumptum probatur, ponendo quod aliquis dominus secularis sit constitutus in extrema necessitate, sicut sunt milites nostri capti ab hostibus in partibus transmarinis, nec habeat dictus dominus unde se ipsum redimat nisi alienando in perpetuum suum manerium, et cum hoc suppono quod nullus sit qui velit emere dictum manerium nisi collegium nostrum vel aliud ei simile, tunc datum Collegium tenetur relevare dictum militem in extrema necessitate positum, et hoc sub pena peccati mortalis; sed non potest ipsum relevare nisi emat ab eo manerium, ergo tenetur in casu sub pena peccati mortalis emere a dicto milite pro perpetuo suum manerium.

[ENGLISH]

## ¶3 · 375.21–375.34

> [p. 375] Iste casus foret michi nimis difficilis, nec video colorem quomodo foret possibilis nisi forte dictum collegium fuerit per dominum huius seculi vinculis, insolubilibus mammone iniquitatis adeo cathenatum quod ex induracione necessario dampnabili non possit dictum militem misericorditer relevare, sed necesse habeat eum de hereditate paterna dampnabiliter spoliare. Sed nec casum illum libenter admitterem nec aliud relevamen militis omnino excluderem; tale enim collegium si foret esset summe dyabolicum, quia (ut innuitur) non posset per elemosinam sed non nisi per sacrilegium dictum militem relevare, et revera Deus non posset salvare tale collegium de sua potencia absoluta.

[ENGLISH]

## ¶4 · 376.1–376.25

> [p. 376] Debet ergo miles ire ad dominum terre et narrare sibi condiciones talis collegii, et totum regnum teneretur collegium tale venenosum expellere et cum bonis que talis legio occuparet, si fuerit elemosina, militem relevare. Et patet quod hoc fieri posset legaliter ex dicto beati Ambrosii posito in decretis XIIª, q. IIª, Aurum. Aurum, inquit, habet ecclesia non ut servet sed ut eroget et subveniat in necessitatibus. Quid est opus custodire quod nihil adiuvat? An ignoramus quantum auri atque argenti de templo domini Assirii sustulerunt? Nonne melius conflat sacerdos propter alimoniam pauperum, si aliqua subsidia desunt, quam si sacrilegus contaminat et asportat hostis? Nonne dicturus est dominus: Cur passus es tot inopes fame mori? Et certe habebas aurum, unde ministrasses alimoniam. Cur tot captivi in commercium ducti nec redempti ab hoste occisi sunt? Melius fuerat ut vasa vivencium servares quam metallorum; hiis non posset responsum deferri. Quid enim diceres: Timui ne templo Dei ornatus deesset? Aurum, inquit, sacramenta non querunt, neque auro placent que auro non emuntur. Ornatus sacrorum est redempcio captivorum, et vere sunt illa vasa preciosa que redimunt animas a morte. Ille verus est thesaurus domini qui operatur quod sanguis eius operatus est.

[ENGLISH]

## ¶5 · 376.26–376.28

> [p. 376] Ex istis verbis huius doctoris sanctissimi et decreti videtur, primo quod regi licet in tempore necessitatis multiplicis auferre nedum localia cleri sui superflua sed

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 372.7: 2. The excessive number of clergy would be lessened.
- 372.27: 3. There would be less worldliness and simony among the clergy and less fighting among the laity.
- 373.5: 4. The laity would be more careful in giving alms,
- 373.8: 5. and the alms would be better distributed.
- 373.17: 6. The earth would be more fruitful.
- 373.32: Evil of appropriations,
- 374.1: which injure both universities and parishes,
- 374.12: so that the numbers at Oxford have fallen greatly.
- 375.3: Objection: 6. Why may not ecclesiastics accept what they may buy?
- 375.10: Example.
- 375.21: Answer: In the case supposed the college ought to give, not to buy;
- 376.1: and a college so buying ought to be suppressed.
- 376.7: Judgment of Ambrose.
- 376.26: These words show that the King may use church treasure to redeem captives,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 372: *Primo* [R3]
  - 372: *∅* (print has exproprietarie once; it is already pos 14, pos 15 duplicates it) [DEL]
  - 372: *II°* [R3]
  - 372: *populo* (15 after it is the line number) [NW]
  - 372: *∅* (plicis is the tail of multi-/plicis, already whole at pos 197; print: plicis quod taliter) [INS?]
  - 372: *Tercio* (e at the edge is the margin alinea letter) [R4]
  - 373: *pro* (180d folio mark and L alinea letter are not text) [R3]
  - 373: *elemosine* (the following 5. is the side-note numeral) [R4]
  - 373: *enim* (print has Dici-/tur enim quod; 3 in margin is a numeral) [INS?]
  - 373: *foret* [R3]
  - 373: *Christi* [R3]
  - 374: *∅* (coordinator: universitates printed whole on line 1; held at pos 0 (OVERRIDE, part99)) [THIN]
  - 374: *appropriacionis* [R4]
  - 375: *foret* [R3]
  - 375: *forte* (clear f) [NW]
  - 375: *vinculis* (English side-note "give" glued) [R4]
  - 376: *XIIª* [R3]
  - 376: *IIª* [R3]
  - 376: *sed ut* (print: servet / sed ut eroget; main lacks sed ut) [INS?]
  - 376: *ministrasses* (15 is the line number) [R4]
  - 376: *in* [R3]
  - 376: *superflua* [R4]
  - 372: *XII°,* [OVERRIDE-VERSE]
  - 374: *universitates* (print: universitates whole on line 1 (agent 9); the scan split it uni | uersitates) [OVERRIDE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 372:
i3. A in marg. : Augustinus. 19. B: Hmitando eque. 24. A
XXII cap. corr. in marg. 26. B: populua. 27. B: Tercio
conlirmatur cx.

p. 373:
23. A in marg. : Nota.

p. 374:
4 Binmarg. : Approbat ut videtur collegium universitatum. 6. 7. B:
quod quibus collegiatus. 8. B: que tam appropriatur. 14. B:
sexaginta sex millia. A in marg. : Sexaginta millia scolarium fucrunt
Oxonic, vidc supra (Below 181" without mark of reference). 23. AA,:
Et — ecclesie deest.
i3. There is a passage in Fitz Ralph's Defensio Curatorum
on the numbers at Oxford. He says that parents are afraid to
send their children Iest the friars should get hold of them „et
sic fit quod ubi in studio Oxoniensi adhuc meo tempore erant
triginta millia studentium non reperiuntur sex millia his diebus".
Brown's Fasciculus II, 473. Apud Goldast, Monarchia II, 1 3q8

p. 375:
3. A in marg. Sexta racio 5. B: et per tencmenta. 9. A in
marg. : Casus. 21. A in marg.: Kesponsio.

p. 376:
5. A in marg.: Ambrosius. 7. A in marg.: Aurum habet ecclesia.
i5. B: aurum aurum. 16. B in marg. : Pro redempcionc captivorum
exponenda sunt vasa ecclesie. 17. A: Melius fuerant.
6. Ambrosius lib. II, De Qfficiis, c. XXVIII and Decreti sec.
pars, causa XII, q. II, cap. LXX.
```

---

## Chunk 16-f: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-16-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-16-f
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "376.29–380.30"
divisions: "cap. 16 (heading 'CAP. XVI.' at 359.5); part 6 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "921 words; 801 unanimous or majority-real; 106 settled by vote (DEL 1, INS 2, R2 61, R3a 34, R5a 7, R6a 1); 14 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n413–n417 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 16, part 6: [TITLE]

## ¶1 · 376.29–377.20

> [p. 376] et calices et preciosa tumbarum et ecclesie ornamenta, ut puta, si aliunde vel oportunius regnum non sufficit redimere captivos qui in defensione regni [p. 377] legitime militarunt: et nro iterata defensione regni necessarii sunt. Secundo, si regnum pro sua defensione necessaria non habeat aliunde vel congruencius unde militantibus pro defensione regni ministraret stipendia. Et tercio, si vulgus per taxas gubernacioni regni necessarias ad nimiam pauperiem sit reductus. Rac beati Ambrosii stat in isto: Melius est quod regnum religiose defendatur per propria quam quod in penam peccati sui depredetur de hiis que inutiliter et avare retinuit a gente sacrilega aliena. Sic enim Nabugodonosor ex peccato sacerdotum fecit templum in Jerusalem spoliari (ut patet Regum XX. et Daniel V°), sed quid propter superbiam qua plus timemus hostes cognoscere nostram egenciam, quam Deum offendere per nostram arroganciam, et quid per evidencias sophisticas et partem quam facit clerus potentibus lamentabiliter pauperes sunt predati? Et ista creditur una causa quare thesaurus ecclesie et cleri Francie fuit per nostros in Angliam transportatus, sed Felix quem faciunt aliena pericula cautum.

[ENGLISH]

## ¶2 · 377.21–378.4

> [p. 377] Et patet quod dictum collegium debet dare dicto pauperi militi elemosinam de bonis pauperum ad hoc datis, non autem ad hereditarie conquirendum dominium seculare, quia sic posset clerus conquirere omnia regna mundi, cum (ut inquiunt) possunt infinite adquirere, sed nichil alienare vel perdere, et sic videretur quod talis adquisicio omnium regnorum mundi foret monstrum abhominabile Antichristi, de quo Daniel IX°, 27: Erit in templo abhominacio desolacionis; cui dicto Christus alludit Matthei XXIV, 15 Cum inquit, videritis abhominacionem desolacionis que [p. 378] dicta est a Daniele propheta stantem in loco sancto, velut dicitur Marci XIII, 14, stantem ubi non debet: qui legit, inquit, intelligat. Sed credo quod non veniet desolacio ad hunc gradum.

[ENGLISH]

## ¶3 · 378.5–378.15

> [p. 378] Septimo principaliter sic arguitur: Domini temporales libere transferunt ius quod habent ad sua dominabilia nunc in certam communitatem et nunc in unam personam, quia translacio iuris temporalis est libertatis creature, nolentis uti vel esse particeps alterius talis iuris, sed in certam personam transferunt absque peccato sua dominia, ergo per idem possunt absque peccato in communitate transferre iura huiusmodi. Sed translato iure in communitatem pro suo perpetuo consequitur tam perseverans dominacio, ergo stat communitatem habere perpetuo tale dominium.

[ENGLISH]

## ¶4 · 378.16–380.5

> [p. 378] Hic dico, primo quod conclusio deducta est concedenda de communitate civili que est capax civilis dominii, ut patet de multis communitatibus civium que licite civiliter dominantur. Sed procul hoc ad inferendum quod clerico (in quantum huiusmodi) licet dominari civiliter, et multo periculosius foret communitatem cleri dominari civiliter, cum error ille vix foret extinguibilis, sed tamquam cancer serperet ampliandoque procederet, quousque magnam partem regnorum inficeret. Satis ergo est nobis habere usum moderatum temporalium pro nostris propriis necessitatibus et aliorum pauperum relevandis vel extincta eorum dominacione civili vel in manus capitalis domini derelicta, ut notat Hugo libro secundo De Sacramentis, parte secunda, cap. 111° et VII°. Layci, inquit, quia terrena et terrene vite necessaria tractant, pars corporis Christi sinistra sunt. Clerici vero, [p. 379] quoniam ea que ad spiritualem vitam pertinent dispensant quasi dextera pars sunt corporis Christi. Et post interpretando utrumque terminum sic infert Clericus nisi Deum et ea que ad Deum spectant habere non debet, cui statutum est decimis et oblacionibus que Deo offeruntur sustentari. Laicis vero christianis fidelibus terrena possidere conceditur, sed clericis spiritualia committuntur, sicut fuit in veteri testamento. Et cap. VII° declarat quomodo quedam ecclesie Christi devocione fidelium conceduntur salvo iure terrene potestatis, ne fiat confusio, cum nihil inordinatum approbare potest Deus. Unde quandoque concedunt principes terreni nudum usum ecclesie, et quandoque usum et potestatem exercende iusticie, quod clericus per ecclesiasticas personas aut individua clericalia exercere non potest. Potest tamen habere personas laycas ministros ad illud officium, sic tamen, inquit, ut id ipsum quod potestatem habet a principe terreno se habere cognoscat et ipsas possessiones nunquam ita a regia potestate elongari posse intelligat, quin si racio postulaverit aut necessitas, illi ipse possessiones debeant in necessitate obsequium, quia, sicut regia potestas patrocinium quod debet alteri alienare non debet, sic ipsa possessio eciam ab ecclesiasticis personis obtenta obsequium quod regie potestati pro patrocinio debetur iure negare non potest. ji Iste profundus doctor non admitteret quod clericus haberet in se civilitatem, nec emeret vel caperet in se sive papa sive alius summum dominium seculare, sed regens laycos et dominaciones suas spiritualiter recipere posset titulo elemosine fructum possessionis vel potestatis terrene, sic tamen quod seculare dominium [p. 380] remaneat aput dominum secularem. Ulterius sicut doctor concedit quod est de libertate dominorum secularium quod possunt transferre ius et possessiones in alios, sic concederet evidencius hoc de clero, cum laico sit magis cognata secularis possessio. of

[ENGLISH]

## ¶5 · 380.6–380.16

> [p. 380] Item, non dubium quin clero potest nocere terre-2 norum habicio, si ergo non liceret sibi tunc ipsa relinquere, ipse foret contra legem Dei ipsis diabolice copulatus; Christus enim precepit suis apostolis mundana relinquere. Paulus cum potuit habuisse vite necessaria de Corinthiis, non usus fuit illa potestate, sed et Augustinus rogavit cives suos recipere possessiones quas sibi donaverant. Quare ergo non potuit papa et quilibet alius cleri dotatus capitaneus sic fecisse; illi enim utilius procurarunt pro genere cleri postero quam Silvester.

[ENGLISH]

## ¶6 · 380.17–380.30

> [p. 380] Item, non ex dotacione cesarea constituitur novus ordo cleri qui sine dotacione huiusmodi non fuisset; quilibet ergo ordo cleri potuit fuisse sine dotacione huiusmodi cum tanta religiositate ordinis sicut modo. Ex quo sequitur quod dotacio talis quecunque est ordini cleri impertinens; aliter enim in spoliacionibus domorum religiosarum et in conquestibus terrarum destruerentur proporcionaliter possessionatorum ordines, et sic variarentur ordines illi proporcionaliter, ut dotacio variatur, quod dementis est dicere. Sicut ergo in prima dotacione sua potuit religiosus possessiones oblatas relinquere, sic modo post possessionem, quod si generaliter voluntarie fieret, maneret idem ordo perfeccior quam est modo.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 377.1: or to defend the realm,
- 377.5: or to avoid oppressive taxation.
- 377.14: Now the clergy prey upon the poor.
- 378.5: Objection: 7. Men may transfer their rights to other men; why not to a society?
- 378.16: Answer: They may, to a civil society that has the right to hoid property, but not to a Clerical community.
- 379.3: Hugh of St. Victor
- 379.28: declares that secular power must rest in secular hands.
- 380.6: Falseness of the rule that the clergy may not part with their endowments.
- 380.12: Example of Paul and Augustine.
- 380.17: All orders could exist as well without endowment and may therefore relinquish it.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 377: *per* [R3]
  - 377: *pauperi* (181c folio mark glued) [R4]
  - 377: *15* (print: Matthei XXIV, 15: (main token 1 covers 15)) [R3]
  - 378: *iuris* [R3]
  - 378: *civili* [NW]
  - 379: *quoniam* (alinea Q and 181c folio mark glued; italic) [THIN]
  - 379: *a* (181d folio mark glued; italic a) [R3]
  - 379: *dominium* (do- here, minium at top of p.380; main token holds whole word) [THIN]
  - 380: *remaneat* (p.380 l.1 reads minium remaneat; minium folded into p.379 pos 232) [THIN]
  - 380: *∅* (inserted run is the end of p.379 already in the main scan; p.380 begins minium remaneat aput) [INS?]
  - 380: *fuisset* [R3]
  - 380: *fuisse* [R3]
  - 378: *∅* (second half of tempo-rales; neighbour 36 already temporales) [DELX]
  - 378: *que* (glued bold 4 is margin numeral) [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 376:
5. A in marg.: Ambrosius. 7. A in marg.: Aurum habet ecclesia.
i5. B: aurum aurum. 16. B in marg. : Pro redempcionc captivorum
exponenda sunt vasa ecclesie. 17. A: Melius fuerant.
6. Ambrosius lib. II, De Qfficiis, c. XXVIII and Decreti sec.
pars, causa XII, q. II, cap. LXX.

p. 377:
1. B: illata defensione. 5. 6. B: regni necessitas.
20. Vulgo iactatus versus; in eandcm sentenciam ap. Plautum:
Feliciter sapit qui alieno periculo sapit.

p. 378:
5. A in marg.: Septima racio. i3. B: translacio. i5. A in
marg.: Responsio. 28. A in marg : Hugo. In Hugonis De Sacram.
1. c. leges: Laici qui.
29. Hugonis de S. Victore Opp. pars II, De Sacramentis,
lib. II, pars II (ed. Migne), pp. 417 et 420 mutatis aliquot verbis

p. 379:
8. Ainmarg.: Contra dominacionem civilcm clcri (Below 181= witliont
mark ot' refcrence). i5. B: pcrsonas ac individua. 19. 15 in
marg.: Nota, tantuni clongantur temporalia data clericis a brachio scculari,

p. 380:
1. A in marg.: Nota. 6. 7. B: tcrrenorum non abicio. 25. A:
proporcionabiter.
```
