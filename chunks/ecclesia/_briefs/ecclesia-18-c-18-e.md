# Translation brief: ecclesia 18-c–18-e

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-18-c.md chunks/ecclesia/wyc-ecclesia-18-d.md chunks/ecclesia/wyc-ecclesia-18-e.md` once and fix what it reports.
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

## Glossary (the 186 rows these chunks use; the full file is GLOSSARY.md)

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
| presciencia | foreknowledge | |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| iuvencula | young girl | The church militant as Christ's young bride; kept apart from the Song's *adolescentula* "young maiden" (DR). Ruled 2026-10-02 (*Eccl.* pp. 23, 37, 94.27). |
| adolescentula | young maiden | Song 1:2, 6:7 (DR "young maidens"). Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| expropriacio | renunciation of property | Never "expropriation" (seizure). Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |
| vicarius Christi | vicar of Christ | The card's ruling, now a row. Ruled 2026-10-02. |

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
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| potencia regulata racione | power regulated by reason | Pilot. |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| franchisia | franchise | Ruled 2026-10-02 (*Eccl.* 239.22). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
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
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| ingratitudo | ingratitude | Toward a person. Ruled 2026-10-02 (156.8). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| philargiria | love of money | 1 Tim. 6:10 *radix omnium malorum cupiditas*. Ruled 2026-10-02. |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| cautela | wile | Not "caution"; *cautela diaboli*, the devil's wile. Ruled 2026-09-28 (8 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| ingratus | displeasing (to God) | *Ingratus deo*: unpleasing to God. "Ungrateful" only where a person is ungrateful to someone. Ruled 2026-09-28 (5 sites). |
| indebitare se | to make oneself a debtor | Sense doubtful; C note (*Dial.* 85.15). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| detegere | to expose | "wipe away" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| pseudomonachus | false monk | Kept apart from *pseudofrater* if it appears. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| ablacio | taking-away | Set against *restituere*/*restitucio*. Ruled 2026-10-02 (*Eccl.* 15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| ablatarius | the one from whom it is taken | Beside *ablacio* "taking-away". Ruled 2026-10-02 (*Eccl.* 15, 343.7). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| legii | lieges | Ruled 2026-10-02 (*Eccl.* 15, 343–344). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| pseudoprepositi | false superiors | Ruled 2026-10-02 (*Eccl.* 15, 358.24). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| collegiatus | collegiate | Ruled 2026-10-02 (*Eccl.* 16, 16-d/16-e). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| ficcio | fiction | As *ficticia*; Wyclif numbers six *ficciones*. Ruled 2026-10-02 (*Eccl.* 16, 385.7). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| raciuncula | little argument | The opponent's ten arguments. Ruled 2026-10-02 (*Eccl.* 17, 398.15). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| denominacio; denominare | naming; to name | The argument turns on it. Ruled 2026-10-02 (*Eccl.* 17, 391.17, 398.2). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| falsarius | falsifier | The opponent's epithet. Ruled 2026-10-02 (*Eccl.* 17, 414.6). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |

---

## Chunk 18-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-18-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-18-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "422.19–426.30"
divisions: "cap. 18 (heading 'CAP. XVIII.' at 415.8); part 3 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "995 words; 847 unanimous or majority-real; 136 settled by vote (INS 1, R2 92, R3a 33, R5a 7, R6a 3); 12 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n459–n463 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 18, part 3: [TITLE]

## ¶1 · 422.19–424.10

> [p. 422] Ad octavam raciunculam conceditur quod universalis ecclesia est diffusa per totum orbem terrarum, cum corpus Christi quod est ecclesia sit diffinitum loco, et allegatur Augustinus XVIII° De Civitate Dei, cap. L°, et XXII° De Civitate Dei, cap. XXVIII°. Hic miror quare de virtute sermonis ex auctoritate Augustini conceditur quod ecclesia est diffusa per totum orbem terrarum et tamen non conceduntur alia que eque asserit Augustinus de ipsa ecclesia; nam per maiorem partem orbis terrarum non est aliquis christianus, nullibi est ecclesia [p. 423] nisi ubi est aliquis christianus, ergo per maiorem partem orbis terrarum non est ecclesia. Et si dicitur quod est ibi secundum potestatem, sic revera quelibet persona sancte matris ecclesie est ubique, et sic concederet cum beato Augustino quod tam ecclesia militans quam triumphans est pars tocius ecclesie. Hoc enim persepe dicunt sancti doctores, licet mendacissime dicatur quod nullibi dicit aliquis doctor unam esse ecclesiam ex istis. Nam (ut sepe allegavi) Augustinus, Encheridion LXIV° cap. ponit illud et in De Questionibus veteris et nove legis cap. XLVII° sic scribit: Non solum autem nos sed et superni cives ecclesie membra sunt. Aliter enim ipsa non esset corpus vel sponsa Christi et persona manens Continue una a principio mundi usque in eternum. Non enim est racio quare ex omnibus christianis quantumcunque localiter distantibus componitur unum corpus, quin per idem ex beatis et viantibus; nec potest colorari racio, quomodo ex tota multitudine fidei christianorum, licet fuit valde disparis speciei, resultat una fides que est formale quo constituitur ecclesia, quin a pari ex omnibus predestinatis sit una sponsa Christi. Sic enim ex beatis viantibus et dampnatis fit unum genus humanum, unde quod dicitur ecclesiam militantem non esse circumscriptive alicubi falsum est, cum sit corpus habens unum locum circumscribentem, sicut habet unam fidem, et sic est corpus animatum racionale, nam est corpus sensibile exercens actus vitales, sicut multitudinis credencium erat cor unum et anima una, ut dicitur Act. IV° 32. Ideo valde remota est dissimilitudo ad probandum quod non est animata, licet vivat, sicut spiritus vivunt, et non sunt animati. Si enim spiritus forent organici [p. 424] sensibiles et gressibiles, sicut sunt militantes ecclesie, tunc oporteret concedendo ipsos vivere consequenter concedere quod sunt animati, sed hoc concedit doctor de ecclesia. Dicit enim in responsione ad novam raciunculam quod ecclesia est aliquid, quia substancia, cum totum sit sue partes, et habet dicta ecclesia tam partes quantitativas quam qualitativas, nec fingetur habere partes qualitativas, si non animas, et per consequens, sicut ecclesia est vivens multis vitis, sic est animata multis animabus. that

[ENGLISH]

## ¶2 · 424.11–426.30

> [p. 424] Ulterius quando negatur dyabolum caput esse membrorum suorum, expresse contradicitur sanctis doctoribus, cum beatus Gregorius, Omelia XVIª, super illud Matthei IV°, 1: Ductus est Jesus in desertum a spiritu, ita scribit: Certe iniquorum omnium dyabolus caput est, et huius capitis membra sunt omnes iniqui. An non dyaboli membrum fuit Pylatus? Sicut ergo est corpus iniquorum, sic est caput eorum, sicut multi qui censentur summi pontifices sunt capita particularium membrorum diaboli; nullus autem prescitus est caput sancte matris ecclesie nec alicuius membri eius, sed sicut Petrus gessit typum omnium predestinatorum pastorum ipsum sequencium post Christum, sic Scarioth gessit typum omnium episcoporum prescitorum ipsum sequencium post dyabolum, non quod ante istos non erant priores in sancta matre ecclesia quorum ipsi erant filii nati pro patribus, sed quod in tempore novi testamenti isti erant capitales post caput ecclesie et principem huius [p. 425] mundi. Differencia autem est inter istos capitaneos, quia boni siciunt precipue virtutes subditorum et lucra animarum suarum, mali autem econtra precipue siciunt temporalia subditorum. Unde Scarioth maximus symoniacus et proprietarius ferens loculos dixit, quasi continuando avariciam pontificum veteris testamenti: Quid vultis mihi dare et ego eum vobis tradam, Matthei XXVI°, 15. Nec dubium quin avaricia quam pontifices habebant circa lucrum templi fecit eos intendere mortem Christi; Johannis XI°, 47, 48, sic scribitur: Collegerunt pontifices et pharisei consilium adversus Jesum et dicebant: Quid faciemus, quia hic homo multa signa facit? si dimittimus eum sic, omnes credent in eum et venient Romani et tollent locum nostrum et gentem. Super quo Augustinus Omelia XLIXª notat primo quomodo invalescente avaricia sacerdotum tempore Christi fuit officium venale nedum pluribus existentibus sacerdotibus simul, ut elicit de Zacharia, Luce I, sed eodem anno per circumvencionem avaram versati fuerunt summi pontifices, et ista avaricia excecavit et excitavit eos ad blaspheme conspirandum in mortem domini. Plus, inquit Augustinus, perditi homines cogitabant quomodo nocerent ut perderent, quam quomodo sibi consulerent ne perirent; ideo collegerunt consilium contra salutem anime sue, quia contra signa veritatis salutaris seviebant. Secundo notat Augustinus quomodo timor perdicionis questus templi fuit causa precipua mortis Christi: Temporalia, inquit, perdere timuerunt et vitam eternam non cogitaverunt et sic utrumque amiserunt. [p. 426] Hec autem timuerant ne, si omnes homines in Christum crederent, nemo remaneret qui adversus Romanos civitatem et templum defenderet. Conceperant enim Christum esse hostem templi et ministrorum eius, et per consequens inimicum ecclesie capitalem, eo quod tradiciones avaricie detexit (Matthei XV°), contra scelera eorum multiplex ve invexit (Matthei XXIII°), ymmo de templo eorum instrumenta avaricie dominanter evexit (Matthei XXI°, 12 et Johannis II° II° Ideo accusarunt eum reportacione falsa de potestate ruine templi minata, quod potuit destruere templum illud et in tribus diebus reedificare illud (ut patet Matthei XXVI° ex dicto Christi Johannis II°, 19: Solvite templum hoc et in tribus diebus excito illud). Unde tamquam habentes hoc plus cordi inproperabant domino crucifixo: Vach, inquiunt, qui destruit templum Dei et in tribus diebus reedificat illud, Matthei XX VII°, 40. Contra templum, inquit Augustinus, et contra suas paternas leges esse totam doctrinam Christi temere senciebant, et ideo iusto Dei iudicio evenit eis finis quem prepostere sic timebant. Nam quadragesimo secundo anno post ascensionem domini per Tytum et Vespasianum tam gentem quam locum perpetuo deperdebant, et sic verificatum est de eis illud Matthei VIII°, 12: Filii autem regni huius eicientur in tenebras exteriores. Unde imposuerunt sibi horribiliorem speciem heresis que est blasphemia, per quam coloracius possent eum extinguere. Johannis XIX°, 7 scribitur: Nos legem habemus et secundum legem debet mori, quia filium Dei se fecit. De lege autem occidendi blasphemum patet Levitici XXIV°, 16.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 422.19: 8. My opponent grants that the Church is spread throughout the world, and cites Augustine.
- 423.5: Why does he not admit with Augustine that militant are triumphant and one Church?
- 423.24: The militant Church is circumscribed as to place.
- 424.4: g. My opponent allows that the Church has substance and parts.
- 424.11: In denying that the devil is head of his members, he goes against holy doctors.
- 424.24: Iscariot is the type of foreknown bishops, as Peter is of the predestinate.
- 425.15: Augustine remarks that it was avarice that led the High Priests to conspire against Christ;
- 426.20: and to bring about the ruin that they feared.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 422: *diffusa* [R4]
  - 423: *nisi* (folio mark 187ᵇ glued, reading is the Latin word) [THIN]
  - 423: *cum* [R3]
  - 424: *esse* (alinea letter H glued) [NW]
  - 424: *1* (x-height old-style arabic 1 (verse number after IV°)) [R3]
  - 425: *mundi* (folio mark 187ᶜ glued) [THIN]
  - 425: *15* (main token i. covers printed 15.) [R3]
  - 425: *XLIXª* [R4]
  - 425: *fuit* [R3]
  - 426: *II°* (print has Johannis II°). before Ideo) [INS?]
  - 426: *II°* (print has Johannis II°). before Ideo) [INS?]
  - 426: *II°* [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 422:
3. B: tres nature sed. 5. A in marg.: Anselmus. 7. A A,:
vel substancie. g. A in marg. : Bernhardus. 14. In codd.: per-
sonis; A in marg. : persona, ut habetur in textu. S. Bernhardi. 19. A in
marg. : Tercia responsio. 25. A in marg. : Ecclesia est diffusa per
totum orbem et per maiorem partem orbis non est ecclesia.
5. Anselmi, De Fide Trinitatis Opp. pag. 479 Bernhardi
in vigilia Natalis Domini. Sermo III. Opp. 1. c. pag. 41.
19. Compare p. 11 5, 1. 1.

p. 423:
2?. B in marg. : Ecclesia est corpus animatum racionale.
Aug Opp. tom. [II, Append. pag. 6o.

p. 424:
4. A in marg. : Quarta responsio. 11. A in marg. : Diabolus est
caput omnium suorum membrorum (B : omnium iniquorum). i3. A
in marg. : Gregorius. 22. A in marg. : Sicut Petrus gessit typum
omnium predestinatorum pastorum, sic Judas omniutn prescitorum
pastorum ipsum in avaricia sequencium. B in marg. : Petrus gessit ty-
pum pastorum predestinatorum et Scariolh pastorum iniquorum. 25. B:
prescitorum deest.
4. Compare p. 11 5,1. i3. i3. XL Homiliarum in Evangelia
lib. I. Homil. XVI, 1. OpP- tom- I> Pag- '492-

p. 425:
2. A: sciciunt. 4. A: sciciunt ; correctum in marg. : siciunt.
8. A in marg. : Avaricia sacerdotum fecit mortem Cristi. 9. B: lucra.
l5. A in marg. : Augustinus. 18. B in marg. : Nota bene quare
pontifices et pharisci Christum fuerant persecuti. 20. B : variati
fuerunt. 3o. B: utraque.
i5. 23. Aug. in Joh. Evang. tract. XLIX, 27. Opp. III, pars
II, pag. 629.

p. 426:
9. A: Ideo accusarunt — potestate: addit. in ultima linea huius pa-
ginae; et B illum textum in margine ponit. 10. B : de potestate deest.
i5. B in marg. : de potestate. 22. A A,: Vaspasianum. B: Vaspesianum.
26. A in marg.: Christo fuit imposita blasphemia et heresis, ut cicius
extingueretur. 3i. A in marg. : Contra avariciam cleri.
```

---

## Chunk 18-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-18-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-18-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "426.31–430.31"
divisions: "cap. 18 (heading 'CAP. XVIII.' at 415.8); part 4 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "904 words; 815 unanimous or majority-real; 73 settled by vote (R2 37, R3a 23, R3b 3, R5a 9, R6a 1); 16 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n463–n467 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 18, part 4: [TITLE]

## ¶1 · 426.31–428.7

> [p. 426] Et ex isto consolati sunt fideles equanimiter tolerare obprobria heresis a pseudocardinalibus et [p. 427] discipulis Scarioth ad hoc promoventibus propter defensionem veritatis evangelice, cum Christus propter persecucionem humiliter ita tulit. Et utinam pontifices templi, scribe et pharisei non haberent hodie cum Scarioth in ecclesia discipulos imitantes. Si enim sunt hodie seculares sacerdotes tamquam pontifices et religiosi possessionati tamquam pharisei qui secundum apparenciam religionis a populo sunt divisi et tercio doctores tradicionis humane tamquam scribe ac quarto profitentes evangelicam paupertatem cum Scarioth qui omnes nitantur impugnare evangelicam veritatem, non mirum si in ista quadriga diaboli Christi ecclesia perturbatur. Signum autem perversionis persone prime partis proprietarie foret, si plus fureret propter audicionem ablacionis suorum temporalium quam propter quantumcunque gravem lapsum ecclesie in peccatum; tunc enim plus afficeretur temporalibus quam honori Dei vel utilitati ecclesie verbi gracia. Si clerus Anglie magis timet amissionem dotacionis regie quam peccatum regni invadendo regnum francie, non video quin philargiria sit seductus; utrumque nempe istorum potest bene fieri, sed indubie primum est propinquius potestati et facilitati humane, ut absque periculo anime fiat iuste. Quis (inquam) dubitat quin facilius foret regem et regnum ponere clerum nostrum in statu primevo qui foret isto statu perfeccior servando undique caritatem et evacuando pompam, rancorem ac avariciam quam exercitum Anglie invadendo Franciam, propter caritatem ad hostes, ipsos temporalibus spoliando et propter amorem eos generaliter occidendo. Et tamen ad hoc secundum consulimus ex isto colore quod potest fieri meritorie in casu possibili quoad Deum et possibilitatem primi [p. 428] tamquam venenum abnuimus contra fidem scripture et sanctorum testimonium. Nam beatus Jeronimus libro II° super Osee, exponens illud Osee IX°, 14: Da eis ubera arencia, ita scribit: Si hiis que pro benediccione donavit male abutamur et in contrarium quam ab eo data sunt convertantur, expedit ut auferantur a nobis.

[ENGLISH]

## ¶2 · 428.8–430.31

> [p. 428] Nec credo esse meliorem medicinam contra abusum huiusmodi quam bonum abusum per eum cuius interest amoveri, nec dubium quin rex penes quem oportet residere capitale dominium (ut ostendit Hugo II° De Sacramentis, parte secunda, cap. VII°) habet precipuum interesse. Unde in desidiam regum monet Deus nunc gentem exteram ad predandum, nunc eventum aeris vel bestie ad vastandum (ut patet Joelis 1°, 5). Ululate, inquit propheta, omnes qui bibitis vinum in dulcedine, quoniam periit ab ore vestro vel (ut habent septuaginta) ablatum est ab ore vestro. Super quo Jeronimus: Sepe quippe fit Dei providencia ut qui non cognoverant eum in prosperis cognoscent in adversis, et qui diviciis male abusi sunt ad vicia, ad virtutes penuria corrigantur. Et talem abusum temporalium reor esse causam bellorum et perturbacionis tocius ecclesie militantis; quibus enim servus Christi abutitur irregulariter in hiis punitur; quod si animus cleri inordinate afficitur istis bonis, nemo in ecclesia magis nocet, eo quod sub colore religionis palliat perseverancius et forcius abusum temporalium et plus inficit residuum ecclesie (ut ostendit Crisostomus, Omelia XXXIª Operis Imperfecti). Unde Augustinus tractatu [p. 429] quarto super Psalmo XXX: Maxime illi persecuntur ecclesiam qui christiani nolunt bene vivere; per hos enim obprobrium habet ecclesia et ab hiis inimicicias sustinet; quando corripiuntur, quando male vivere non permittuntur, quando cum eis vel verbo agitur, ipsi mala in suis cordibus meditantur et erumpendi occasionem exquirunt. Tales declarat beatus Gregorius, 1° Pastoralium, esse sacerdotes malos. Et hec est racio quare Christus et sancti doctores invexerunt tam acute contra huiusmodi sacerdotes. Nam, ut ait Gregorius, Omelia XVII, nullum puto fratres carissimi maius preiudicium tolerat Deus quam a sacerdotibus. Ideo ad vindicandum illam Dei iniuriam debent christiani magis animose, aspere et unite consurgere, quia secundum Crisostomum, Omelia XVIIIª Operis Imperfecti, non est verus discipulus qui non imitatur magistrum nec est imago qui non est similis auctori. Et quoad discipulos Scariothis consideremus, si sunt aliqui professores vite expropnetane, quin vel impugnant vel sophisticant vel tacent indebite evangelicam veritatem. Omnes enim illi sunt cum Scarioth proditores veritatis evangelice que est Christus, ut declarat Crisostomus, Omelia XLIXⁿᵃ Operis Imperfecti et parcialiter ponitur in decretis XIª, q. IIIa: Nolite, inquit, timere eos qui occidunt corpus, ne forte propter timorem mortis non libere dicatis quod audistis nec fiducialiter predicetis omnibus quod in aure soli audistis. Sic ergo ex hiis verbis ostenditur quod non [p. 430] solum ille est proditor veritatis qui transgrediens veritatem palam pro veritate loquitur mendacium, sed eciam ille qui non libere pronunciat veritatem quam libere pronunciare oportet aut qui non libere veritatem defendit quam libere defendere convenit, proditor est veritatis. Nam sicut sacerdos debitor est, ut veritatem quam audivit a Deo predicet, sic laicus debitor est, ut veritatem quam audivit a sacerdotibus probatam quidem in scripturis fiducialiter defendat. Quod si non fecerit, prodidit veritatem. Ex istis dictis cum explanatis alibi et statu ecclesie patet quod nimisl multi sunt vicarii Scariothis, non solum qui pro ecclesia vel fama impugnant, sophisticant vel tacent evangelicam veritatem, nec solum qui portantes loculos furtive ut Scarioth ineque parciuntur patrimonium Crucifixi cum fratribus bona pauperum dominative in uxoribus, in filiis, in pompa seculi consumendo, sed tercio qui propter desidiam aut timorem mortis pro loco et tempore congruis obmutescunt. not Nec valet ficcio qua dicimus inimicos evangelii exasperatos esse ex veritatis preconio magis segnes, quia iuxta hunc fucum caput martirum et sui milites nunquam sic pro publicacione veritatis usque ad mortem meritorie decertarent. Sed audi Augustinum super Johannis Omelia XXVII exponentem illud Johannis VI°, 7: Ex hoc multi discipulorum eius abierunt retro, dicentem: Hoc factum ad nostram consolacionem quoniam aliquando contingit ut dicat quis verum et quod dicit non capiatur, sed quod scandalizentur qui audiunt et discedant. Penitet enim hominem quandoque dixisse quod verum est; dicit enim aput seipsum:

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 427.18: Avarice makes our clergy dread the loss of endowments more than the sin of a war with France.
- 428.8: An abuse of this kind can be best remedied by removing the thing abused.
- 429.18: The friars, who profess poverty, neglect to preach the truth.
- 430.20: We ought not to be silent for fear of offending the enemies of the gospel.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 427: *Franciam* [R4]
  - 428: *II°* [R3]
  - 428: *a* (print has a nobis.) [INS?]
  - 428: *huiusmodi* [R4]
  - 428: *XXXIª* [THIN]
  - 429: *quarto* (folio mark 188ª glued) [THIN]
  - 429: *persecuntur* (print spelling) [NW]
  - 429: *Christus* [R3]
  - 429: *iniuriam* [R4]
  - 429: *impugnant* [R4]
  - 429: *XLIXⁿᵃ* [R4]
  - 429: *XIª* [R4]
  - 430: *Quod* [R3]
  - 430: *veritatis* [R3]
  - 430: *scandalizentur* [R4]
  - 429: *XVIIIª* (no comma; followed by Operis) [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 426:
9. A: Ideo accusarunt — potestate: addit. in ultima linea huius pa-
ginae; et B illum textum in margine ponit. 10. B : de potestate deest.
i5. B in marg. : de potestate. 22. A A,: Vaspasianum. B: Vaspesianum.
26. A in marg.: Christo fuit imposita blasphemia et heresis, ut cicius
extingueretur. 3i. A in marg. : Contra avariciam cleri.

p. 427:
5. A in marg.: Condicionalis. 14. B: urerent. 28. B in
marg. : Inferius nota textum Jeronymi satis pugnantem pro ablacione
tcmporalium. 3o. B in marg : Nota bene ambas columpnas.

p. 428:
2. A in marg. : Dc ablacione temporalium. 4. A in marg. : Jero-
nymus. 4. 5. In codd.: per benediccionem ; Correxi e textu Hieronymi,
Comment. in Oseam prophetam, Iib. II, cap. IX; ibid. quod ab eo data;
iterum correxi. 25. A in marg.: contra avariciam clcri bona cor-
reccio. 3o. A in marg.: Augustinus.
29. Chrysostomus in Opere Imperfecto 1. c. pag. CXXX.

p. 429:
1. B in marg. Nota que faciunt clerici, quando corripiuntur i. In
codd.: Psalmo XX; recte: tractatu tertio, Ps. XXX, pars II, sermo III.
2. A A,: per hoc. II. A in marg.: Gregorius. i3. A in marg. :
Qui non pronunciat veritatem est proditor eius et similiter qtii ipsam non
defendit. i5. A in marg: Crisostomus. In homilia XVIII hic locus
non habetur; pocius XXVIII, vide Op. Imp. 1. c. pag. CXIX. 22. B: qui
est; Christus deest. 23. A in marg. : Crisostomus.
5. Aug. Opp. tom. IV, pars I, pag. 162. 8. cap. II.
11. Greg. XL. Hom. in Evang. lib. I. Hom. XVII, 14. 1. c. p. i5o3.
23. Dec. sec. pars, causa XI, q. III, cap. LXXXVI.

p. 430:
8. B: probatam quid. 17. B: pompa simili. 20. A: dicius;
in marg. correctum : dicimus. Hic verbum excidisse videtur. 25. A in
marg. : Nota Augustinum bene. 25. Codd. : exponens.
25. Aug. in ,Ioh. Evang. tract. XXVII. Opp. tom. III, pars. II,
pag. 5o5.
```

---

## Chunk 18-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-18-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-18-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "431.1–435.25"
divisions: "cap. 18 (heading 'CAP. XVIII.' at 415.8); part 5 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1135 words; 1049 unanimous or majority-real; 71 settled by vote (DEL 4, R2 25, R3a 34, R5a 6, R6a 2); 15 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n468–n472 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 18, part 5: [TITLE]

## ¶1 · 431.1–433.23

> [p. 431] Non debui sic dixisse; sed ecce domino contigit: dixit et perdidit multos; solacium itaque in domino habeamus et tamen caute verba dicamus. Non dicit omnimode taceamus vel veritatem dicentibus resistamus, quia revera sic prodere sermonem Dei, qui est veritas et lex Christi, foret ipsum prodere, cum sit idem. Unde videtur quod nostri pretensi de parte dextera sponse Christi qui sic produnt veritatem in membris suis habent racionem maioritatis peccati super ambos proditores Christi tam novi quam veteris testamenti. Nam plura beneficia tam corporalia quam spiritualia a Christo receperant, maiorem veritatis noticiam tam ex lege Christi quam ex factis suis habuerant. Et ideo racione maioris ingratitudinis et peccandi sciencie videtur, si fuerint in maiori gracia secundum presentem iusticiam, quod maiorem culpam incurrant; et istam materiam tangit beatus Gregorius, Omelia XVIIIª super illud Johannis VIII°, 46: Si veritatem dico, quare non creditis mihi? Multi, inquit, sunt hodie qui Judeorum duriciam detestantur, quia predicacionem domini audire noluerant et tamen quales illos arguunt fuisse ad Jidem, tales ipsi sunt ad operacionem. Precepta Dei audiunt, miracula cognoscunt, sed converti a pravitatibus suis renuunt. Ad decimam raciunculam respondetur, concedendo quod ecclesia est virgo. Et allegantur ad hoc decreta ecclesie, et sic dicitur iuvenescere, senescere, et multa alia predicata suscipit quorum racionem oportet distinguere; alia, inquit, dicuntur proprie de ecclesia, ut quod habet temporalia, privilegia et regulam vivendi, alia autem dicuntur de ecclesia improprie, methaforice et [p. 432] transsumptive, ut quod ecclesia sit virgo, vetula, sponsa et mater cum denominacionibus huiusmodi. Omnia ista dicuntur de ecclesia transsumptive, mistice et improprie. Inprimis suppono quod sequitur: Ecclesia est improprie virgo, mater, sponsa Christi etc, ergo ipsa est ecclesia, est virgo, mater et sponsa Christi. Patet tripliciter: Primo ex hoc quod doctor sepe concedit huiusmodi proposiciones simpliciter; secundo ex hoc quod aliter non satisfaceret alicui tali proposicioni, dicendo utrum debet concedi simpliciter vel negari. Si enim iste terminus improprie sit terminus distrahens, tunc negaretur maior pars dictorum sanctorum de ecclesia et maior pars scripture sacre ac modi loquendi, que tamen bene concessa sunt. Scribit enim Augustinus in De Verbis Domini super Joh., Sermone L°, ecclesie: Concessit Christus in spiritu quod mater eius habuit in corpore, ut et mater et virgo sit. Et hoc est proprium Deo nostro, ut de corrupta possit facere virginem, sicut homo contra de virgine facit corruptam, dicente Jeronimo, libro primo, super illo Osee II°, 19: Sponsabo te mihi in sempiternum et sponsabo te in iusticia et iudicio et misericordia et miseracionibus et sponsabo te mihi in fide. Super quo sic loquitur sanctus doctor; O quanta clemencia Dei, meretrix que cum multis amatoribus fornicata est et ob hoc crimen bestiis tradita, postquam revertitur ad virum, nequaquam ei reconciliari dicitur sed desponderi. Et vide quid sit inter Dei coniunccionem et hominum; homo cum uxorem acceperit, de virgine mulierem facit, id est, non virginem; Deus autem meretricibus copulatus [p. 433] eas mutat in virgines iuxta illud, quod adultere dicitur per Jeremiam: Non ut dominum me invocasti aut patrem aut principem virginitatis tue. Unde et Apostolus post fornicacionem et ydolorum cultum credentibus Corinthiis loquitur: Despondi vos uni viro virginem castam exhibere Christo. Et post exponit Jeronimus quare Deus desponsacionem ecclesie tripliciter repeciit: Primo, inquit, despondit eam in Abraham sive in Egipto, ut uxorem habeat sempiternam. Secundo in monte Synay, dans ei in sponsalibus legis iusticiam. Et tercio veniente Dei filio domino Jesu Christo fuit desponsata in fide perfecta, dum videndo filium vidit et patrem, Johannis XIV°, 10, 11. Sic ergo sancti doctores concedentes ista simpliciter non sunt ausi asserere quod auctor scripture dicit ista improprie et false. Sed videtur mihi quod doctor loquitur improprie vocando ecclesiam vetulam vel post eius incepcionem dicendo ipsam iuvenescere. Non enim memini me legisse ista de sancta matre ecclesia, sed synagoga sathane, ecclesia malignancium et meretrix cuius dyabolus est caput, quam doctor dicit partem sancte matris ecclesie, potest racionabiliter dici vetula turpissima.

[ENGLISH]

## ¶2 · 433.24–435.25

> [p. 433] Ponit enim doctor quod prescitus eciam dum fuerit in mortali, si habuerit fidem infusam, est membrum sancte matris ecclesie, et indubie tunc est membrum sathane et dyabolus caput eius (ut dicit beatus Gregorius). Dicitur autem sancta mater ecclesia proprie senescere et florere virtutibus, cum Psalmo XCI°, 11, sic loquitur propheta: Senectus mea in misericordia uberi; nam in tercia desponsacione quando sponsa Christi est mulier antiqua et tamquam senex persecucionibus membrorum diaboli tribulata, habet uberiorem [p. 434] misericordiam quam in tempore sue adolescencie, et sic vere vocatur vidua propter elongacionem sponsi ab ea peregrinante ad patriam, dum Psalmo CXXXI°, 5, dicit sponsus: Viduam eius benedicens benedicam. Ulterius foret Opus doctole detegere quid proprie et quid improprie ac figurative conveniat sancte matri ecclesie, quia nimis suspectum verbum et carnale est dicere quod ecclesia proprie habet possessiones et privilegia Constantini, sed improprie est mater vel sponsa Christi. Primo (inquam) querendum esset quid proprie foret ecclesia, si aliquid; non superest quid foret nisi substancia, et ulterius descendendo (ut sepe tetigi) oporteret concedere quod ecclesia sit substancia corporea et sic corpus animatum racionabile, et sic proprie foret homo, et per consequens desponsanda. Confirmatur, ecclesia est proprie privilegiata et possessionata (ut dicitur); quod non foret nisi posset uti privilegiis et vesci possessionibus. Ergo ecclesia posset comedere et actus humanos consimiles exercere, et per consequens ecclesia foret substancia animata que generaret omnem hominem, et sic cum foret individuum eiusdem speciei specialissime cum omni homine univoce generans hominem, foret homo (ut sepe dicunt sancti). Et certum est quod improprie foret homo, cum haberet propriam individuacionem, propriam racionabilitatem et propriissimam perfeccionem humanam; nam nisi foret substancia, potens exercere actus racionales, ut actus promerendi, contemplandi et gaudendi, aliter indignius quam sacerdotes Baal comederet tantum cibum. Si dicitur quod ecclesia proprie nichil est sed est aliqua, tunc concedendum foret simpliciter quod ecclesia nichil est. Si enim illa simpliciter conceduntur [p. 435] de ecclesia que improprie sibi conveniunt, multo magis forent predicata de ecclesia simpliciter concedenda que proprie sibi conveniunt. Si ergo proprie sit nichil, sequitur simpliciter quod sit nichil, et per consequens non est aliquid, et tunc non haberet partem qualitativam aut quantitativam, sicut concedetur, et per consequens nulla denominacio partis foret sibi proprie vere et proprie attributa. Ex quo sequitur quod ecclesia catholica non sit cesaree privilegiata nec seculariter possessionata, quia non secundum se totam (tum quia est indivisibilis, tum eciam quia multis de ecclesia non convenit hoc privilegium vel ista dotacio) nec eciam secundum partem que foret pars illius ecclesie, eo quod spiritus beati qui sunt de illa ecclesia sunt indivisibiles; et sic ecclesia non haberet partem vel partes, et per consequens papa non foret proprie caput ecclesie, cum ipsa proprie semper foret acephala, quia gens sine capite. Caput enim non proprie dicitur nisi in comparacione ad corpus capitatum, sed ecclesia (ut dicitur) non proprie est corpus, quia sic proprie foret homo, ergo non est proprie capitata; et cum proprie est, sequitur quod sit proprie incapitata, et per consequens est incapitata, et per idem quelibet abbathia sive religio non foret proprie antiqua vel iuvenis,

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 431.25: 10. My opponent allows the Scriptural names of the Church but says they are used figuratively.
- 432.3: Still they are used and are therefore applicable.
- 433.14: My opponent uses terms that are not warranted by Scripture.
- 434.5: It would be a fitting work for the doctor to shew what language is figurative and what literal;
- 434.11: e. g. as to whether the Church is a person.
- 434.29: If the Church is only figuratively something, it is literally nothing,
- 435.3: and so has no parts,
- 435.15: and no head;
- 435.24: likewise no religious corporation could be or do anything;

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 431: *sit idem* (main token covers two printed words) [R3]
  - 431: *Unde* [R3]
  - 431: *Christi* (line number 10 glued) [R4]
  - 431: *XVIIIª* [R3]
  - 431: *alia* [R3]
  - 432: *II°* [R3]
  - 432: *O* [R3]
  - 433: *eas* (folio mark 188ᶜ glued) [THIN]
  - 433: *10* [R3]
  - 433: *11* [R3]
  - 433: *11* [R3]
  - 433: *Christi* [R3]
  - 434: *proprie* (alinea letter Q glued) [R4]
  - 434: *ut* [R3]
  - 434: *foret* [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 431:
8. A A,: perdunt. 14. A A,: peccandi scire. 17. A in marg.:
Gregorius. 25. A in marg.: Quinta responsio. Ecclesia est virgo,
mater, vetula et sponsa etc. 28. 29. A: distinguere.
18. Gregor. XL Homiliarum in evang. lib. I, Hom. XVIII, 5.
2C1. Compare p. ii5. 1. 23.

p. 432:
2. B: huius. Omnia. 7. B: concedit huius. 20. A in marfi. :
Jeronymus. 21. A in marg.: Christi desponsacio facit ex meretrice
virginem. Vide supra. 24. B: S. Thomas. 28. coniunctos in
codd. Correxi e textu Hieronymi.
i5. Aug. Opp. tom. V, pag. '75. 24. Hieronymi Com-
ment. in Oseam prophet. lib. I, cap. II. Opp. VI (ed. Migne) 881.

p. 433:
1. adulteris in codd. : correxi e textu Hieron. 2. B : non dominum.
11. B: Sed tercio. 24. A in marg. : Opinio. 25. A in marg. :
Quomodo ccclesia est vetula, vidua et virgo. 27. I?: ut dum beatus.

p. 434:
3. B: peregrinantem. 5. A,: doctorem. 16. A A,; et deest.
19. B : humanos sensibiles. 21. 22. B : foret iudicium eiusdem. 25. risi-
bilitatem in codd. 3o. A in marg. : Responsio quedam. Nota si ecclesia
est proprie corpus et que predicata sibi proprie conveniant, vide modicum
ante (Above lSS^without marlc of rcference). 32. B: Si est illa.

p. 435:
3. 4. B : Si ergo sit proprie, sequitur. 10. AA,: cesarea; B: cesarie.
29. A Aj! doctorum fiddium.
```
