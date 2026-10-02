# Translation brief: ecclesia 14-e–14-g

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-14-e.md chunks/ecclesia/wyc-ecclesia-14-f.md chunks/ecclesia/wyc-ecclesia-14-g.md` once and fix what it reports.
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

## Glossary (the 171 rows these chunks use; the full file is GLOSSARY.md)

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
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). Where privileges or law, not prayers, do the aiding: "to aid" (*Eccl.* 241.1; cf. *suffragium* "aid"), 2026-10-02. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| regalia | regality | The king's royal right. Ruled 2026-10-02 (*Eccl.* 148.3, 151.12, 152.12). |
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
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| brachium seculare | the secular arm | Ruled 2026-09-28 (coordinator, delegated) (7 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| coactivus; cohercere, cohersitivus | coactive; coerce, coercive | Kept apart: *potencia coactiva* "coactive power" (the ruler's), *cohercere* "coerce". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| censura | censure | Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| locus a maiori / a simili | the topic from the greater / from the like | The dialectical topics. Ruled 2026-10-02 (*Eccl.* 144.27). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| insolubilia | insolubles | The logicians' paradoxes of self-reference. Ruled 2026-10-02 (*Eccl.* 175.11). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Ruled 2026-10-02 (*Eccl.* 13). |
| autenticus / autenticacio | authentic / authentication | The key term of *Eccl.* 13. Ruled 2026-10-02. |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| credulitas | credence | With *credere*, believe (*Dial.* 23.17–24.4). Ruled 2026-09-28. |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| sumitur pro | is taken for | Supposition language. Pilot. |
| simpliciter / secundum quid | **without qualification / in a certain respect** | ⛔ Always opposable. Never "simply", "wholly", "directly", "naturally" etc. (T. p. 364). |
| necessitas supposicionis / ex supposicione | necessity of supposition / necessity on supposition | Conditional necessity. Pilot (*Eccl.* 3.21); *ex supposicione* ruled 2026-10-02 (34.12, 38.22). |
| de congruo / de condigno | by congruity / by condignity | Pilot. |
| consequencia | inference | ⛔ Not "consequence" (T. p. 361 n. 13). |
| consequens / antecedens | consequent / antecedent | |
| propositio copulativa / disiunctiva | conjunction / disjunction | Not "copulative proposition" (T. p. 365). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| suffragium (*legis, privilegii*) | aid | As *suffragium* "aid" (01-a) and *suffragium sensus*. Ruled 2026-10-02 (149.29, 152.8). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "one given alms". Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |

---

## Chunk 14-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-14-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-14-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "314.28–318.26"
divisions: "cap. 14 (heading 'CAP. XIV.' at 299.9); part 5 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "877 words; 751 unanimous or majority-real; 108 settled by vote (R2 73, R3a 25, R3b 1, R5a 8, R6a 1); 18 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n351–n355 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 14, part 5: [TITLE]

## ¶1 · 314.28–316.10

> [p. 314] Intelligo autem per utrumque gladium ad sensum misticum potenciam castigandi, priorem potenciam [p. 315] castigandi spiritualiter tam filios ecclesie quam eciam inimicos, et secundum gladium potestatem corporaliter cohercendi. Et cum iste due partes ecclesie sicut omnia eius membra in omnibus que habent communicant, patet quod utraque istarum parcium habet modo suo utrumque gladium, modo quo loquitur Apostolus II Corinthiorum II°, 3: Meum gaudium omnium vestrum est. Sacerdos itaque habet gladium spiritualem in se formaliter et sue iurisdiccioni subiectum, ut regulet eius usum. Sed ad hoc requiritur noticia utriusque testamenti, ut sciat docere quomodo et qualiter est ille gladius exercendus; aliter enim non daret Deus gladium illum in manus ydiote, frenetici sive litargici, qui non sciat uti ipso, ad defensionem ecclesie secundum regulas pugnandi quas Christus instituit, sed omnino ad dampnum vel perturbacionem ecclesie. Habet ergo secularis gladium temporalem in se subiective ad illud officium exequendum; sacerdos autem habet, si sciverit, illum gladium obiective ad eius officium regulandum, et sic utraque pars ecclesie comparticipat fructu gladii utriusque. Christus autem fuit simul rex et sacerdos, habens in se subiective utrumque gladium, modo quo impossibile fuit ut Petro vel eius vicario communicetur, eo quod principium generis et exemplar oportet esse perfectius, habens simplicius omnes raciones tocius generis christiani. Unde oportet quod post illud caput sive principium tocius christiani generis sint duo rami disparis vicarie, scilicet laicorum et clericorum; et in illis ramis fundatis in eadem vite sunt quoad subiectacionem impermixte due maneries potestatum. Nec sufficit aliquis Christi vicarius sine peccato plene exercere unam illarum potestatum; multo magis ipsis confuse commixtis. Unde ad figurandum [p. 316] illas potestates precipit Christus gladios eius virtutibus et diffinivit sufficienciam in duobus. Et (ut notat beatus Bernardus ad papam Eugenium) per hoc quod precipit Petro ponere gladium in vaginam, prohibuit clero in persona vel causa sua execucionem gladii corporalis. Christus autem servans inseparabiliter summum gradum innocencie, scivit sine defectu vel confusione utrumque gladium regulare et utriusque status honores accipere (ut alias explanavi), nec potuit cum istis statibus civiliter dominari.

[ENGLISH]

## ¶2 · 316.11–316.29

> [p. 316] Et si queratur ubi scriptura prohibet clerum civi- liter dominari, interrogo sic querentem unam aliam questionem: Cum omne privilegium ecclesie sit fundabile in scriptura, ubi in scriptura fundatur clero potestas vel utilitas taliter dominandi? Nam secundum Augustinum, II° De Doctrina Christiana, in fine: Si aliquid utile est, ibi invenitur; sed nulla talis cleri dominacio ibi invenitur, ergo nulla talis cleri dominacio est utilis. Maior istius racionis est assercio archidoctoris Augustini qui multum horrebat mendacium; que maior vel est necessaria vel summe heretica, quod non dicetur ob reverenciam tanti sancti. Et pro minori huius argumenti est plana induccio per singulas partes alterius testamenti; vel si non sit plana induccio, dicat falsigraphus ubi fundatur clero Christi taliter dominativa possessio. Nam tam necessarium et tam notabile privilegium foret ab auctore scripture et capite ecclesie alicubi expressatum. Sed ego non reperi, nisi dicatur yronice vel per antifrasim quod

[ENGLISH]

## ¶3 · 317.1–318.3

> [p. 317] hiis tribus locis fundatur dominacio civilis cleriacorum. Primo in illo Luce XXII°, 25, 26: Reges gencium dominantur eorum, vos autem non sic; ubi notum est quod Christus approbavit dominacionem secularem regum gentilium, ut patet de Job, de Nabuchodonosor et de aliis regibus tam preteritis quam futuris. Sed iuxta beatum Bernardum interdixit eam suis apostolis. Secundus locus scripture in quo taliter fundaretur seculare dominium clericorum foret preceptum Christi Matthei X°, 9: Nolite possidere aurum neque argentum; iuxta quod locutus est Petrus ceco, ut legitur Actorum III, 6°, dicens: Argentum et aurum non est mihi, quod autem habeo hoc tibi do. Et hinc tradit pro regula, V° capitulo sue prime epistole, quod non simus dominantes in clero sed forma facti gregis ad deserendum mundum et eius concupiscencias, non coacte et invite, sed sponte et ex animo. Tercius locus scripture est dictum Apostoli, Iª Tim. VI°, 8, dicentis: Habentes ergo alimenta et quibus tegamur, hiis contenti simus. Ille autem non est contentus alimento et tegumento qui ultra hec exigit nedum temporalium superaffluenciam ad ministrandum sed ad dominandum, nec solum clericaliter sed seculariter. Unde contendimus instancius circa iurisdiccionem et secularem dominacionem tamquam nobis privilegium requisitum, quod tangit Doctor Solempnis, VI° quolibeto q. XXIIIª, sed cum formidine; quod, inquit, ecclesiastici temporalium habeant jurisdiccionem forte non multum expedit et erat forte venenum [p. 318] quod legitur cecidisse in ecclesia Dei tempore Constantini qui in iurisdiccione sua dotavit ecclesiam, sed

[ENGLISH]

## ¶4 · 318.4–318.26

> [p. 318] Iste autem doctor reprobatus fuit acute, quia tractavit de potestate pape, ideo innuit cum formidine quod debuit constanter asserere, ut docet Hugo de Sancto Victore, libro II° De Sacramentis, parte II°, capitulis III° et VII°. Nam quod amplius est quam liber usus fructus in clero, vergens ad ritum mundanum, malum est, quia sacerdotalis officii tardativum. Cum ergo in istis locis scripture non fundatur clero civilitas sed plane contrarium, nec est scriptura sibi ipsi contraria, utinam illud dominium esset suspensum a clero, quousque in scriptura sacra eius invenerit fundamentum, et vellem si Deo placeret quod nullus sacerdos haberet primatum vel privilegium ecclesie quousque cartam illius invenerit in scriptura. Cum enim nemo debet privilegium appetere nisi sibi utile, et secundum Augustinum si utile est, ibi invenitur, videtur quod ad clericum privilegiandum pertinet quod cartam tam autenticam inveniat in scriptura; tunc enim laboraremus circa eius noticiam, niteremurve in deposicione sic nobis adversaria ex deformitate vite nostre ad cartam illam. Et tercio non acceptaremus tantum onus nisi quasi nolentes ad magnam instanciam populi pro spirituali suffragio nos urgentis.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 315.7: The spiritual sword is formally committed to the priest,
- 315.18: with an indirect control of the secular sword, which is in the hands of the laity.
- 315.26: The powers which were in Christ the vine are divided between the branches.
- 316.11: If it is asked where in Scripture rule is forbidden to the clergy, we reply by asking where it is allowed.
- 317.2: Three texts that might do if they could be taken ironically.
- 317.27: Opinion of Henry de Gandano.
- 318.4: who was very mild in his expressions,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 315: *cum* [R3]
  - 315: *gladium* (20 is the line number) [R3]
  - 315: *Christus* [R3]
  - 315: *generis* [R3]
  - 315: *vicarie* [R3]
  - 316: *Christus* [R3]
  - 316: *interrogo* [R4]
  - 316: *questionem* (English side-note words glued in other scans) [R4]
  - 316: *II°* [R4]
  - 317: *Iª* [R3]
  - 317: *XXIIIª* [R4]
  - 318: *∅* ('very' is the English side-note; main already has Iste at 15) [INS?]
  - 318: *II°* [R3]
  - 318: *II°* [R3]
  - 318: *III°* [R3]
  - 318: *cecidisse* [THIN]
  - 318: *ecclesia* [THIN]
  - 315: *noticia* (glued margin mark dropped) [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 314:
10. A in marg. : Responsio. 12. B: ius deest. 14. B in marg. :
Si Christus habuit potestatem cohercendi homines corporali racione sue
regalie, unde est quod sibi competere dominari civiliter denegatur.
22. A B in marg. : Nota qualiter ecclesia habct duos gladios (A: Below
173» without mark of reference). 28. B in marg. : Quid signant duo
gladii ecclesie. B: ad sensum — gladium potestatem deest.
18. Aug. In Joh. Ev. cap. I, tract. V. Opp. tom. III, pars II,
pag. 323.

p. 315:
27. B: Unde oportet — christiani generis deest. 3o. A A, : cleri-
corum; in illis.

p. 316:
1. A: gladios eius; A,: gladios virtutibus. B: gladios enis (sic)
virtutibus. 3. A in marg. : Bernhardus. Nota. 11. A in marg. : Vide
cap. XXII. huius ; que verba in textum codicis A, inciderunt. 14. AA,:
tundatur deest. B: fundabatur. Aj corr. in marg. : datur. 16. A in
marg. : Augustinus. 17. A in marg.: Nota racionem. 29. A B in
marg. : Nota quod dominacio civilis cleri non est fundabilis nisi yronice.
3. Bernhardi de Consideracione lib. IV. Opp. pag. io36.
[5. cap. XI. II. Rec. 63. Opp. tom. III, pars I, pag. 44.

p. 317:
7. 8. B: eam apostolis. i5. A: sub forma. 17. B: et vite.
18. A: apostoli apostoli. 27. A B in marg. : Henricus (B addit:
hereticus) deGandano; hereticus — hec distinccio non ad Henricum sed
ad Johannem de Gandavo pertinet.
27. Doctor Solemnis. This is the distinguishing name of Hen-
ricus de Gandano (f 120,5); comp. Jocher, Gelehrtenlexicon, II,
i5o3; Kabricius, Bibl. lat. III, 200.

p. 318:
12. i3. A A,: sibi ipsa. 29. A in marg.: Nota. 3o. B: tunc
sonaret. 33. A in marg.: Quomodo debet defcndi ct teneri scriptura
sacra. Ritus. B in marg.: Contendcndum non cst contra ritus dum topicc
fundantur in scriptura.
```

---

## Chunk 14-f: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-14-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-14-f
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "318.27–322.4"
divisions: "cap. 14 (heading 'CAP. XIV.' at 299.9); part 6 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "784 words; 689 unanimous or majority-real; 84 settled by vote (INS 1, R2 51, R3a 23, R3b 1, R5a 8); 11 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n355–n359 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 14, part 6: [TITLE]

## ¶1 · 318.27–320.27

> [p. 318] Si autem arguitur per locum a simili quod ritus nostri non valent, cum non sint fundabiles in scriptura, dico quod docto hoc de quocunque ritu est conclusio concedenda, quia tunc non sonaret ritus talis pietatem vel religionem Christi. Unde pro illis que non expresse docentur in scriptura sacra, si quadam evidencia topica suadentur, non debemus [p. 319] multum contendere sed conclusiones expressas ipsius scripture omnibus modis defendere. Et error huius sentencie fecit divinam theologiam contempni et leges exteras exaltari; de quo conqueritur dominus per prophetam Osee VIII°, 12: Scribam, inquit, ei multiplices leges meas que velut aliene computate sunt. Et revera rex et lex sua sese in dileccione et odio consequuntur. Et hec est causa tocius confusionis ecclesie, quod claudicat plus intendens legi humanitus superaddite quam divine. Et si queratur ubi in scriptura fundatur lex supradicta fundans dotacionem ecclesie, dicitur quod fundacio proporcionaliter ad eius necessitatem fundatur implicite in illo Luce XVI°, 9: Facite vobis amicos de mammona iniquitatis, et in illo Ia Tim. VI°, 17: Divitibus huius seculi precipe non sublime sapere, nec sperare in merito diviciarum, sed facile tribuere, et in illo Luce X°, 5, 7: In quamcunque domum intraveritis ibi manete edentes et bibentes que aput illos sunt: dignus est enim operarius mercede sua. Nunquam autem fundari potest in scriptura quod sacerdocio Christi conveniat dominacio civilis et sicut non est contendendum circa sequelam tante dotacionis ex scripturis cum merito clericorum, sic non est contendendum circa ablacionem eius si eveniat, nisi forte de quanto docetur ex scriptura quod auferens excedit regulam caritatis vel quod occupacio illorum bonorum per clerum foret sancte ecclesie utilior. Tercio arguitur per hoc quod dominacio civilis est perrecta tam a Christo quam a philosophis approbata; perfecciori ergo parti ecclesie debet potestas illa infundi per Christum a quo est omnis potestas. [p. 320] Sicut ergo beatus Silvester non accepit illam partem imperii a Constantino, sic nec aliquis sacerdos cuiusquam terreni principis accepit ab eo dominacionem huiusmodi secularem sed immediate a Christo; prius enim tempore vel natura fuit beatus Silvester dignus habere dominacionem illam imperii quam cesar sibi diviserat, et per consequens prius fuit data a Deo, quam cesar ipsam sibi resignaverat, et cum eque digni fuerunt prius alii Christi vicarii, videtur quod eciam illis infuit potestas taliter dominandi. Et ista videtur sentencia cuiusdam Nicolai Putanensis super epistolam ad Romanos, qui vocat episcopos ex hinc miseros, quod volunt se subicere in onere tributi et aliis serviciis exactis a brachio seculari. Et fundat se super dicto Apostoli Hebreis VII°: Omnimodo maior est ille qui benedicit, quam ille cui benedicitur, et per hoc probat Apostolus quod Melchisedech rex Salem qui gessit typum Christi fuit maior quam Abraham cui benedixit (ut legitur Gen. XIV°). Sicut ergo sacerdocium est dignius imperio, sic oportet Romanum pontificem esse digniorem imperatore accipiente imperium ab illo pontifice, et per consequens, oportet conferentem habere illud imperium, et non esse subiectum suo elemosinario, quia tunc non foret papa omnimode ipso maior, sed secundum eandem racionem qua benedicit et confert sibi spirituale imperium foret ipso subieccior.

[ENGLISH]

## ¶2 · 320.28–322.4

> [p. 320] In isto puncto sunt nimis multi maniaci, putantes nedum maiores sacerdotes sed minores singulos debere [p. 321] super omnes reges et principes seculariter dominari, in tantum quod iste Nicolaus dicit quod reges debent esse advocati sacerdotum, quia si ipsi eque immediate haberent potestatem illam cum sacerdotibus, ecclesia non servaret monadem, eo quod forent duo capita eque primo. Et in istam blasphemiam ex defectu intellectus scripture incidunt multi iuriste facientes suos prepositos insanire. Conceditur ergo quod dominacio civilis sit quodammodo perfecta et necessaria perfecte supposito ad dominandum tam clericos quam laycos insolentes. Sapit tamen (in quantum talis) veniale peccatum: ideo non potuit Christo competere, nec auctonzatur in Christo et evangelio expresse sed innuitive, et ideo inferiori parti ecclesie quam Apostolus Ia Cor. VI°, 4, vocat contemptibilem debet competere. Illa ergo dominacio non pure capit complecionem suam a Christo, sicut spiritualis dominacio vel potestas, sed completur ut sic per ritus humanos. Unde pro tali complecione et legum aggregacione dicit Augustinus super Joh., Omelia VIª (ut recitavi superius) quod non iure Dei sed imperatoris dicimus quod hec villa vel domus est mea, non quod ius Dei sit omnino alienum a constitucione civilis dominii, cum oportet legem Dei dare graciam que est civilis dominii fundamentum, sed non secundum illam culpam quam contrahit est a Deo. Et sic intelligo Augustinum in Epistola XXXVII ad Macedonium sic dicentem: Inter mundanos quedam iura constituuntur que appellantur civilia, non quod hinc fiat ut bene utentes sint, sed ut male utentes minus molesti sint. Quando autem hec iura consonant legi Dei que est per se iusta, tunc [p. 322] evenit quod sunt iusta, et quando deficiunt ab eius regulacione sunt iniusta. Ideo dicit veritas Matthei V°, 20: Nisi habundaverit iusticia vestra plus quam scribarum et phariseorum, non intrabitis in regnum celorum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 318.27: All ceremonies should likewise be grounded in Scripture.
- 319.11: Scriptural authorities for the true law of endowment
- 319.30: Objection: 3. Rule is a perfection and so belongs to the more perfect part of the Church.
- 321.1: Extravagant rights of rule are often claimed for priests.
- 321.12: All civil rule smacks of sin.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 318: *∅* ('in' is the English side-note (grounded in); main already has nostri at 198) [INS?]
  - 319: *Christo* [R4]
  - 319: *perfecciori* (print perfecciori; ff ligature) [NW]
  - 319: *infundi* [R3]
  - 320: *subieccior* [NW]
  - 321: *super* (173d folio mark) [R3]
  - 321: *laycos* (print has y; 174a folio mark) [R4]
  - 321: *VIª* [R3]
  - 321: *sint* [R3]
  - 322: *evenit* [R3]
  - 319: *multum* (173c folio mark glued) [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 318:
12. i3. A A,: sibi ipsa. 29. A in marg.: Nota. 3o. B: tunc
sonaret. 33. A in marg.: Quomodo debet defcndi ct teneri scriptura
sacra. Ritus. B in marg.: Contendcndum non cst contra ritus dum topicc
fundantur in scriptura.

p. 319:
ii. A in marg. : Questio. Nota fundacionem dotacionis cx lege Dei.
23. B: non est concedendum. 25. B: concedendum circa abla-
cionem si. 3o. A in marg.: Tercia obieccio.

p. 320:
6. 7. B: sihi dimiserat. 8. A A, : ipsam deest. II. A in
marg.: Nicolaus Putanensis. 28. A in marg. : Responsio. Arguitur
pro dominacione civili sacerdotum et dissolvitur (Below 1734 without mark
of reference).
i5. Verba apostoli ad Heb. VII, 7: Sine ulla autem con-
tradiccione, quod minus est a meliori benedicilur.

p. 321:
io. B: perfccta et intra. ib. domandum in codd. II. B in marg. :
Dominacio civilis sapit peccatum in quantum talis. i3. A A,: Christo
in evangclio. 18. A in marg. : Augustinus. 21. B: scd iurc
imperatoris.
21. See above pag. 3oi.

p. 322:
2. B: sunt iniusta — ideo dicit vcritas deest 3. A: vestra quam plus
5. A in marg. : Responsio. 32. A in marg. : An benedicens univer-
saliter sit dignior benedicto (Helow 174» without mark of reference).
21. Dec. I pars, dist. XCVI, c. XIV. 28. Matth. XXII, 21.
```

---

## Chunk 14-g: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-14-g.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-14-g
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "322.5–326.31"
divisions: "cap. 14 (heading 'CAP. XIV.' at 299.9); part 7 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1173 words; 1011 unanimous or majority-real; 137 settled by vote (DEL 1, R2 79, R3a 34, R3b 4, R5a 16, R6a 3); 25 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n359–n363 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 14, part 7: [TITLE]

## ¶1 · 322.5–323.10

> [p. 322] Falsum ergo assumitur quod sacerdos Christi acci- pit dominacionem civilem a Christo, sicut nec Silvester accepit a cesare, sed elemosinam accepit ab eo. Prius ergo tempore et natura habuit Silvester omnia bona imperii, immo fuit dominus super astra et omnia inferiora homine in natura, sed non titulo civili, ymmo titulo gracie quo iusti sunt omnia; sed post accepit in usum corporalem titulo elemosine post donacionem cesaris, et adhuc in illa elemosinacione cesaris prius naturaliter sed non prius tempore egit Deus. Unde nec Constantinus nec Deus ipse potuit donasse dominacionem civilem beato Silvestro stante puro ordine clericali, ideo cum illa non habet auctoritatem a scriptura sacra, et cum secundum Augustinum si sit utilis, in scriptura sacra invenitur, manifesta patet quod non ad sensum catholicum intelligitur illa carta Constantini, posita in decretis, XCVIª d., Constantinus, quod resignavit sibi ibidem dominacionem civilem, sed elemosinam vocatam perpetuam vel stante civili dominio apud cesarem vel extincto. his Et quantum ad dictum Nicolai Putanensis, patet quod equivocat vel blasphemat. Nam Christus facto et verbo precepit et docuit clericos suos subdi principibus, sic enim precepit Petro Matthei XVII°, 25, quod solveret didragmam cesari pro Christo et Petro figurante suam ecclesiam, et interrogatus si licet dare censum cesari, ostenso sibi denario cuius imago et superscripcio erat cesaris, sic subiungit: Reddite ergo [p. 323] que? sunt cesaris cesari et que sunt Dei Deo. Et Petrus ex ista doctrina precepit suis (quod et facto docuit) ut sint subiecti regibus et ducibus eciam discolis (ut patet prima Petri II°, 18). Et Apostolus docet Rom. XIII°, 7, quomodo debemus obedire principibus, cui tributum dantes tributum, et cui vectigal vectigal, et multo magis nos qui sumus elemosinarii secularium principum debemus esse subiecti nostris elemosinantibus, cum tam graves et sancti apostoli non sic dotati a principibus ita fecerunt.

[ENGLISH]

## ¶2 · 323.11–324.16

> [p. 323] Ulterius conceditur quod sacerdocium est dignius civili imperio, et sic minimus sacerdos (in quantum talis) est maior quam temporalis dominus (in quantum talis), cum potestas spiritualis sit prestancior corporali. Sed notandum (ut supra dixi) quod est dare duplicem dignitatem et maioritatem, scilicet quoad iudicium Dei secundum leges suas vel quoad iudicium mundi secundum suas leges. Quoad iudicium Dei secundum suas leges diffinit Christus Matthei XI°, 11 quod inter natos mulierum non surrexit maior Johanne Baptista, nam persona humilior et ad utilitatem ecclesie ministrativior est quoad Deum maior( ut patet Luce XXII°, 27). Secundo modo ille qui secundum leges humanas habet primatum in reputacione eorum superiorem vocatur apud mundum maior et dignior, licet sit aput Deum indignior; et isto modo constituit Constantinus quod episcopus Romanus sit dignior aliis, ut patet XCVIª d., non respiciens sive fuerit dignior sive indignior quoad Deum. Unde nec imperator nec cardinales habent potestatem constituendi hominem in tali dignitate, nec licet fideli asserere quod, eo ipso quo isti sic decreverunt vel elegerunt, oportet Deum [p. 324] assistere dando constituto in tali primatu dignitatem et maioritatem simpliciter quoad Deum, quia illud sacramentum non est fundabile ex scriptura sacra. Istis premissis patet quod Christi sacerdocium et clericatus in exproprietariis sortis sue est dignius dominacione civili, sed summa stulticia foret ex istis concludere quod omnis sacerdos debet excellencius dominari civiliter. Nam iuxta istam vesaniam sequeretur quod Deus et omnes angeli excellencius quam papa dominarentur civiliter. Iste ergo dignitates in papa et imperatore sunt disparium specierum nec sunt compossibiles in eadem persona simplici propter imperfeccionem quam sapit civile dominium. Unde passiva elemosinacio est perfeccior quam civilis dominacio, et (ut alias dixi) vocata civilitas in mixto clerico facit subiectum imperfeccius, quam foret pure clericus ceteris paribus.

[ENGLISH]

## ¶3 · 324.17–325.21

> [p. 324] Et quantum ad auctoritatem apostoli, Hebreorum VIIª 7, dicitur quod (sic habet textus noster) sine ulla autem contradiccione quod minus est a meliori benedicitur; quod intelligendum de benediccione auctoritativa, non positiva obice in benedicente. Nam omnia opera domini benedicunt creatori, et sacerdos, membrum diaboli, benedicit predestinato, carissimo filio Dei. Ideo maneat quicunque sacerdos sine hoc quod contradicat suo ordini et est melior layco (in quantum huiusmodi) cui potestative benedicit. Sed longe hoc ad inferendum quod clericus debet dominari civiliter, cum racione maioritatis infertur oppositum. Clericus ergo debet aufugere primatum, gloriam et excellenciam quoad mundum, et in hoc consistit eius maioritas quoad Deum. Nec video quomodo fundabitur pure ex fide scripture quod oportet imperatorem accipere imperium a suo pontifice. Consonum tamen est quod benedicat electo tamquam superior quoad [p. 325] Deum, sed non oportet si confirmaverit imperatorem quod ipse sit excellencius imperator, quia tunc foret coniugatus et omnis ordinis. Sicut ergo Deus potest conferre alteri denominacionem creatam, licet in se non habeat hanc vel talem, sed habet in se virtutem excellenciorem, sic est de prepositis ecclesie. Nec movet consideracio de monade, quia solus Christus est caput universalis ecclesie, sanccior in clero militante, ad cuius ducatum maior pars militantis ecclesie ambulat vias domini, est caput militantis ecclesie quoad Deum. V Sed ille in quem militans ecclesia consenserit ut primatem est caput militantis ecclesie quoad mundum. In alio autem genere primatus est imperator, et sic tam papa quam imperator uterque alteri subiectus, sed papa simpliciter superior si non ponat contradiccionem in nomine. Et sicut materia prima et forma sunt duo genera causarum quarum est dare materiam causam primam in suo genere, et formam causam primam in suo genere, et mundum primum ex eis compositum utroque genere perfeccionum, sic est in elementari composicione militantis ecclesie.

[ENGLISH]

## ¶4 · 325.22–326.11

> [p. 325] Unde absit fidelem credere quod quilibet sacerdos Christi (in quantum huiusmodi) sit superior in dominacione civili quam aliquis rex vel dominus secularis, ut dicit doctor predictus. Si tamen papa haberet dominacionem illam immediate a Christo et non ex titulo elemosine cesaris, non video quin oporteret concedere quod papa et totum genus sacerdotum dominaretur seculariter super singulos reges terre, ita quod sicut quelibet superficies dicitur infinitum maior quam linea, sic quelibet sacerdotis dominacio civilis foret infinitum maior quam aliqua dominacio principis secularis Et potest hoc confirmari, cum sacerdos et [p. 326] specialiter papa potest iniungere cuicunque principi virtute potestatis clavium quod renunciando toti dominacioni sue det ecclesie in perpetuam elemosinam cuncta que possidet. Vicarius ergo Christi potest virtute clavium habere quotquot bona voluerit ex privilegio concesso Petro Matthei XVI°. Sed (ut dixi superius) nec tenetur secularis pandere sibi peccata, quantumcunque restrinxerit potestatem clavium, nec talem penam acceptare sive consilium pro salutari penitencia nisi gratis voluerit, et si vicarius Christi inordinate urgeat, tenetur resistere.

[ENGLISH]

## ¶5 · 326.12–326.26

> [p. 326] Nec moveat quod Gregorius XI fuerit in genere secularis dominii capitalis dominus regni nostri, ex hoc quod potuit catholicare omnes cartas religiosorum possessionatorum in Anglia, quo facto fuissent exempti a iurisdiccione regali. Item, potuit arrestare per bullas suas quemcunque hominem legium regis nostri eciam infra regnum nostrum, non petita licencia a rege, et tercio (quod maximum est) ipse potest hereticare quod domini temporales possunt auferre temporalia ab ecclesia delinquente, et per consequens catholicare eius oppositum. Ista, inquiunt quidam, fecit de facto satis legitime. Sed deliramenta sunt ista, quia sic rex Anglie teneret de utroque archiepiscopo in capite, non econtra; sicut enim papa se habet ad cesarem, sic archiepiscopus noster se habet ad regem quoad illud genus dominii.

[ENGLISH]

## ¶6 · 326.27–326.31

> [p. 326] Item, tunc omnes fratres ex vi potestatis clavium dominarentur seculariter toti mundo, quod est contra professionem eorum et (ut ipsi vere credunt) contra legem Christi. Sic enim quilibet dominus secularis iniuriaretur presbitero detinendo sua temporalia.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 322.5: Silvester accepted alms, not civil authority,
- 322.15: which would have been inconsistent with his orders.
- 322.25: Christ bade his clergy be subject to princes.
- 323.11: Priesthood is nobler than civil rule,
- 323.15: but with a nobleness that depends on service, not on position,
- 324.4: Nor does it follow that priesthood includes the right to rule.
- 324.24: That the Emperor is blessed by the Pope does not make the Pope an Emperor,
- 324.34: or by the same rule he would be married.
- 325.11: Pope and Emperor have each a primacy but in different ways.
- 325.22: According to the claims made for the clergy every priest would be civilly above the King;
- 326.1: and competent to make him yield up his kingdom.
- 326.12: So the chief rule in England was claimed for Gregory XI.
- 326.22: Such claims are insane.
- 326.25: Supreme power might as well be claimed for every friar,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 322: *acci-* (acci-/pit; main token holds first half (R is margin letter)) [NW]
  - 322: *pit* (second half of acci-/pit) [NW]
  - 322: *XCVIª* [R3]
  - 322: *Christus* [R3]
  - 323: *II°* [R3]
  - 323: *18* (old-style 1 at x-height + 8) [R3]
  - 323: *11* (leaf zoom: old-style 11 after XI°) [R3]
  - 323: *XCVIª* [R3]
  - 324: *∅* ('it' is the English side-note (Nor does it); main already has Istis at 21) [INS?]
  - 324: *patet* [R3]
  - 324: *subiectum* [R3]
  - 325: *habeat* (174c folio mark) [R4]
  - 325: *superior* [NW]
  - 325: *cum* [R3]
  - 326: *XI* (print 'Gregorius XI. fuerit'; main lacks XI between Gregorius and fuerit) [INS?]
  - 326: *dominii* [NW]
  - 326: *capitalis* [NW]
  - 326: *dominus* [R3]
  - 326: *regni* [R4]
  - 326: *nostri* [R3]
  - 326: *legium* [NW]
  - 326: *quod* (print (quod; 3 is a margin argument numeral) [R4]
  - 326: *hereticare* [NW]
  - 323: *que* (174a folio mark glued; italic que) [THIN]
  - 325: *∅* (second half of mun-dum; neighbour 93 already mundum.) [DELX]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 322:
2. B: sunt iniusta — ideo dicit vcritas deest 3. A: vestra quam plus
5. A in marg. : Responsio. 32. A in marg. : An benedicens univer-
saliter sit dignior benedicto (Helow 174» without mark of reference).
21. Dec. I pars, dist. XCVI, c. XIV. 28. Matth. XXII, 21.

p. 323:
5. in codd. Rom XII. u. A in marg.: Responsio. i5. A in
marg. : Dnplex dignitas et maiorilas. i5. A: dare dcest. 17. B:
quoad — leges deest. 22. B: minislracior. 27. A A,: epi-
scopus suus. 29. imperator; incodd.: A B: ~~~~r; A, 1 pr. 3o. B:

p. 324:
16. A: ceteris pauperibus; A, correxit; scd peribus iam extat. 23. In
codd.: membra. 32. B in marg. : Accepcio imperii non fundatur in
(idc aut scriptura.

p. 325:
6. AB in marg. : Nota de triplici capitc. 7. monade, id est: unitatc.
11. B in marg. : Nota bene caput ccclcsie mililantis. 22. A in marg. : Nota
quomodo Christus, quomodo papa et quomodo imperator suntcapita cccIchc
(Abovc i74,: without mark of rcferencc). 33. A in marg. : Nota racionem.

p. 326:
12. A in marg.: Triplcx obiectus. 16. B: biillas suas quidcunque.
22. A in marg. : Responsio. 27. A in marg. : Conlra dominacionem
civilem cleri (Below 174« without mark ot reference).
```
