# Translation brief: ecclesia 17-b–17-d

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-17-b.md chunks/ecclesia/wyc-ecclesia-17-c.md chunks/ecclesia/wyc-ecclesia-17-d.md` once and fix what it reports.
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
| presciencia | foreknowledge | |
| viator | wayfarer | One still on the road, not yet in the homeland. Loserth: "a traveller on earth". Pilot. |
| viare; vians | to be a wayfarer; [one] on the way | The verb of *viator*; tag `g:viator`. Ruled 2026-09-28 (8 sites). |
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
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |

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
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| legalitas | legal standing | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| conducentes | those who hire them | Ruled 2026-09-28. |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| locus a maiori | the topic from the greater | The dialectical topic; for *a simili* see "the topic from likeness" (2026-09-28 row). Ruled 2026-10-02 (*Eccl.* 144.27). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |
| autenticus / autenticacio | authentic / authentication | The key term of *Eccl.* 13. Ruled 2026-10-02. |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| insinuativus | implied | Paired with *expressus*, express. Ruled 2026-09-28. |
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
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| autonomatice / antonomastice | by antonomasia (pre-eminently) | Pilot (*Eccl.* 1.16) |
| in necessitatis articulo | at the point of need | Pilot |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| redempcio temporalium | redemption of the temporal goods | Chapters buying back seized goods. Ruled 2026-10-02 (*Eccl.* 15, 340.15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| redempcio (of a sentence) | redemption | Buying off a penalty; kept apart from *redempcio temporalium*. C note at first use. Ruled 2026-10-02 (*Eccl.* 15, 352.1). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| legalia | the legal precepts | Of the old law, beside *cerimonialia* "ceremonial precepts". Ruled 2026-10-02 (*Eccl.* 17, 389.2–3). |

---

## Chunk 17-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-17-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-17-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "390.12–394.23"
divisions: "cap. 17 (heading 'CAP. XVII.' at 388.1); part 2 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1061 words; 916 unanimous or majority-real; 125 settled by vote (R2 80, R3a 34, R3b 1, R5a 10); 20 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n427–n431 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 17, part 2: [TITLE]

## ¶1 · 390.12–394.23

> [p. 390] Ex istis dictis notari possunt notabilia. Primo quia christiana religio secundum formam quam ipse instituit est perfectissima et securissima; secundo quod ipsa durat per tempus utriusque testamenti, licet ante incarnacionem non sit vocata christiana religio, et tercio sequitur quod ecclesia fuit a mundi inicio, ut dicit Crisostomus et decretum Augustini, positum XXXIIª q. IVª. Recurrat. Et hoc debet attendere doctor allegans hoc dictum Augustini, non enim hic loquitur de ecclesia sub nomine ecclesie, sed loquitur de religione christiana, dicens quod fuit a mundi inicio. Ecclesiam ergo vocat sub nomine religionis que hodie dicitur christiana. Et patet quod non sequitur: si ante incarnacionem non vocabatur christiana religio, ergo ante incarnacionem non fuit ecclesia vel christiana religio, quin pocius sequitur quod a mundi inicio fuit ecclesia; quia notum est quod nunquam fuit religio fidelium predestinatorum nisi quando fuit ecclesia. Ideo sicut a mundi inicio fuit illa religio, sic a mundi inicio fuit ecclesia; et ad hoc sunt quotlibet testimonia sanctorum. Nam Augustinus (ut allegavi [p. 391] superius) sic scribit super Psalmo CXLII°: Ecclesia que est mulier antiqua, civitas Dei et corpus Christi, habet inicium ab Abel, sicut mala civitas a Caym. Unde in libro De Questionibus veteris et nove legis q. IIIa declarat quomodo fides ecclesie successit per ordinem in electis. Ab inicio, inquit, genus est christianorum, priores ergo homines quotquot fidem habuerunt unius Dei iure christiani dicendi sunt. Unde sicut non sequitur: per tempus veteris testamenti non fuit vocata religio christiana, ergo tunc non fuit religio, ita non sequitur: tunc non fuit vocata ecclesia christiana, ergo tunc non fuit ecclesia. Sicut ecclesia Romana, cum sit universalis ecclesia, diu fuit ecclesia, antequam fuit ecclesia Romana, quia quemcunque locum mundi incoluerit semper manet ecclesia, cum fides et predestinacio non dependent a loco corporeo. Ideo oportet notare quomodo accidit ecclesie denominacio a loco et denominacio a natura creata sub nomine tali, sed per se inest sibi denominacio a capite, quod nunc est Christus, Deus et homo; fuit autem caput ecclesie antequam fuit homo. Ideo foret nephandum sophisma concedere quod tunc non fuit ecclesia, licet ecclesia fuerit tunc per locum a simili quod ecclesia Romana vel christiana fuit, quando ipsa non fuit Romana vel vocata christiana. Oportet enim distinguere inter per se et per accidens. Ecclesia enim non potest desinere esse ecclesia, sicut nec aliqua creatura potest desinere esse membrum Christi mistici (ut declarat Augustinus III°, De Doctrina Christiana XXXII°). Unde quod ecclesia vocata est sub nomine ecclesie pro tempore veteris testamenti, patet scrutanti [p. 392] scripturas tam in libris legalibus quam prophetalibus, in libris historialibus et sapiencialibus. Unde frequencius (si non fallor) fit mencio in lege veteri de matre nostra sub nomine ecclesie quam in nova. Unde quia liber Psalmorum est valde autenticus, quia domino allegatus et communius in ore presbyteri exclamatus, notaremus illud Psalmi XXIª, 26. Aput te laus mea in ecclesia magna, et Psalmo XXXIV°, 18, dicitur: Confitebor tibi in ecclesia magna, et Psalmo CXLIX°, 1: Laus eius in ecclesia sanctorum. Et sic exponit Augustinus maiorem partem Psalmorum, dictam de ecclesia vel in persona ecclesie, sicut loquuntur libri alii veteris testamenti. Unde beatus Gregorius, Omelia XIXª, exponens illud Matthei XX, i: Simile est regnum celorum homini patrifamilias qui exiit primo mane conducere operarios in vineam suam, declarat quomode paterfamilias est conditor noster qui in magna domo sua regit singula, sed specialiter suam ecclesiam. Ipse, inquit, habet vineam, scilicet universam ecclesiam que ab Abel iusto usque ad ultimum electum qui in fine mundi nasciturus est quot sanctos protulit tot palmites misit. Et post prosequitur quomodo dicta ecclesia mane hora tercia, sexta, nona et undecima habuit cultores vinee ecclesie quos vocavit et excitavit ad colendum ecclesiam et vicia extirpandum. Illas autem quinque horas limitat iste sanctus papa per quinque etates mundi. Modo non dubium vel ceco logico, si vinea dicti patrisfamilias sit ad sensum misticum sancta ecclesia [p. 393] que ab Abel iusto usque ad novissimum electum sic fructificavit, tunc ilia est extencior in etate quam pro hora undecima. Sequitur enim: Deus habet illam ecclesiam, ergo illa est ecclesia, et sequitur: Ab Abel iusto usque ad novissimum electum illa taliter germinavit, ergo per tantumdem temporis ipsa fuit. Et eandem sentenciam dicunt Augustinus, Crisostomus et decretum ex fide scripture (ut ostendi superius); et revera abbreviare etatem sancte matris ecclesie quod non fuit in veteri testamento foret presumptuosus error et periculosus merito revocandus; quod ego statim facerem, si (quod absit) illam assercionem temerariam presumpsissem. Nec valet dicere quod ecclesia fuit per istas quatuor etates ante incarnacionem, sed tunc non fuit ecclesia, primo quia tam literaliter quam mistice vocatur ecclesia pro tempore veteris testamenti, sicut patet in parabolis Christi quibus vocavit fideles ad nupcias et ad laborandum in vinea (ut patet Mat. XXII° et Mat. XX°), et secundum peritos linguarum ecclesia dicitur convocacio fidelium, synagoga autem congregacio fidelium. Ideo prius dicta est ecclesia, antequam fuerat vocata synagoga. Et quoad sensum literalem, patet quod sepe vocata est ecclesia pro tempore veteris testamenti. Similiter, si ecclesia fuit in prima etate mundi, tunc vel illud quod est ecclesia vel illud quod fuit ecclesia. Primum negabitur et dato secundo oportet cum veris dicere quod illa adequata ecclesia que fuit in prima etate mundi fuit in illa etate ecclesia, et cum illa etas lapsa est per multa millia annorum ante incarnacionem Christi, sequitur quod per tantum temporis ante incarnacionem fuit ecclesia; quod ego credo esse de fide ecclesie. Similiter modo est ecclesia triumphans que fuit in prima etate mundi, [p. 394] et cum nulla sit ecclesia triumphans nisi que prius fuit militans (ut declarabitur inferius), sequitur quod illa ecclesia triumphans que fuit pro prima etate mundi fuit tunc ecclesia militans. Non enim est fas dicere quod nunc non sit ecclesia triumphans nec erit ante diem resurreccionis finalis, nec fas est dicere quod solum Christus vel alia persona humana, si iam sit beata in corpore et anima, sit modo ecclesia triumphans. the Ex istis videtur mihi quod post hereses de trinitate et incarnacione non fuit heresis periculosior quam pertinaciter defendere quod per totum tempus veteris testamenti non fuit ecclesia sancta catholica; tunc enim deficeret fidelibus tam viantibus quam triumphantibus solempnis articulus fidei, immediate sequens post articulum de spiritu sancto, quod est contra fidem scripture, contra sanctos doctoreset iura ecclesie, que dicunt concorditer quod fidelis debet credere in spiritum sanctum, sanctam ecclesiam catholicam. Ideo tam clerici quam laici debent constanter consurgere ad istum articulum defendum, scilicet quod ecclesia sancta catholica fuit a mundi principio cuius pars triumphans est spiritus celestis (ut dixi superius).

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 390.12: but he teaches that a) the Christian religion is best and safest; b) it lasts through both testaments;
- 390.17: c) it existed from the beginning of the world.
- 390.23: The Christian religion is another name for the Church.
- 391.17: The name is accidental; the essential is that the Church is joined to her head,
- 391.25: and cannot cease to be, except by falling away from him.
- 392.1: The name of "Church" used throughout the O. T.
- 392.15: Parable of the labourers in the vineyard,
- 393.1: The Church does not exist only for the eleventh hour.
- 393.33: The Church which existed in the first ages as militant is now triumphant,
- 394.10: In denying the previous existence of the Church we reject an article of the Creed.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 390: *incarnacionem* [R4]
  - 390: *IVª* [R4]
  - 390: *ergo* [R3]
  - 390: *allegavi* (alle- here, gavi at top of p.391 with 183b folio mark; main token holds whole word, p.391 pos 0 is superius)) [THIN]
  - 391: *fidem* (italic) [R3]
  - 391: *III°* [R3]
  - 392: *scripturas* [THIN]
  - 392: *in* [THIN]
  - 392: *legalibus* [THIN]
  - 392: *XXIª* [R4]
  - 392: *1* (verse number, short old-style 1) [R3]
  - 392: *XIXª* [R4]
  - 392: *quomode* (print reads quomode) [NW]
  - 393: *que* (alinea C and 183c folio mark glued) [THIN]
  - 393: *literalem* (clear e) [NW]
  - 393: *testamenti* (2 is a margin argument numeral) [R4]
  - 393: *triumphans* [R5]
  - 393: *in* [THIN]
  - 393: *prima* [THIN]
  - 394: *defendum* (print reads defendum) [NW]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 390:
II. A in marg.: Nota. 20. A in marg. : Ecclesia incepit habere
nomen ecclesie in novo testamento, sed utique ipsa prius fuit (Below
i83»without mark of reference). 26. B: vel fuit. 28. A A, :
quia — ecclesia deest. 32. A in marg. : Augustinus.
18. Decret. sec. pars, causa XXXII, q. IV, cap. II.

p. 391:
i. 2. A in marg.: Ecclesia. 16. A in marg. : Nota. 17. B in
marg. : Denominacio accidit ecclcsie tripliciter. 29. A in marg.:
Augustinus.
1. Opp. Aug. tom. IV, pars II, pag. 1 58g. 5. Ibid.
tom. III, Append. pag. 44.

p. 392:
4. A in marg.: Ecclesia vocata est sub nomine ecclesie pro tempore
veteris testamenti (Below i83b without mark of reference). 6. B. :
communicus in ore. Binmarg. : Frcquenter in lege veten tit mencio de
ecclesia sub nomine ecclesie. 12. i3. In codd.: ecclesia. Correxi.
14. A in marg.: Gregorius. 20. B: que Abel iusto. A in marg. :
Ecclesia sunt omnes electi qui sunt et palmites in Christo qui est vitis.
23. B: quomodo dunca (sic) ecclesia.
14. Sancti Gregorii XL Homil. in evang. lib. I, hom. XIX.
Opp. tom. I, i5io.

p. 393:
2. A: extensior. 12. i3. B: presumpsisse. A in marg.: Kiccio.
21. A: congrcgacio fidelium. A, add. Iudeorum.

p. 394:
4. A: Non enim fas. 10. A in marg. : Conclusio. c5. A in
marg. : Augustinus. 25. 26. A B in marg. : Apprehendent septem mu-
lieres virum de ecclesia intelligitur (Above iSj»1 without mark of reference).
2?. Aug. Quaestiones ex veteri test. cap. XLVII. Opp. tom. III,
Append. pag. 60.
```

---

## Chunk 17-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-17-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-17-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "394.24–398.26"
divisions: "cap. 17 (heading 'CAP. XVII.' at 388.1); part 3 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "951 words; 829 unanimous or majority-real; 109 settled by vote (DEL 2, INS 1, R2 64, R3a 32, R3b 2, R5a 5, R6a 3); 13 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n431–n435 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 17, part 3: [TITLE]

## ¶1 · 394.24–398.1

> [p. 394] Unde in De Questionibus veteris et nove legis cap. XLVII°, Augustinus exponens illud Isaie IV°,: 1 Apprehendent septem mulieres virum unum in die illa dicentes: Panem nostrum comedemus et vestimentis nostris operiemur: tantummodo invocetur nomen tuum super nos, aufer obprobrium nostrum, primo dicit quod propheta loquitur de die gracie et muliere septemplici, scilicet ecclesia que est mulier [p. 395] fortis, de qua Prov. XXXI: Per septem mulieres, inquit, septem ecclesias dico esse significatas que quamvis una sit tamen septiformis dicitur, ut unum corpus septemplici numero constat membrorum Non solum, inquit, nos sed eciam superni cives ecclesie membra sunt cuius caput est Christus. Sive ergo una sive septem dicantur ecclesie, non discrepat, quia tota universitas ecclesiarum que est septem ecclesie propter septem dona spiritus sancti et simul omnes unum corpus sunt Christi ex quo omnia in celis et in terra habent originem. Unde in hac militante ecclesia omnium ecclesiarum facta est mencio, quia cum huic sacramentum creatoris predicatur, eciam celestibus insinuatur doctrina. Inferioribus enim cum insinuatur necesse est ut audiant et superni. Unde Apostolus Ephesiorum III°: Michi autem omnium sanctorum minimo data est gracia in gentibus evangelizare investigabiles divicias gracie Christi et illuminare omnes, que sit dispensacio sacramenti absconditi a seculis in Deo qui omnia creavit, ut innotescat principibus et potestatibus in celestibus per ecclesiam multiformis sapiencia Dei. Ecce quod iste sanctus apostolus in thabernaculo hoc mortali positus illuminavit cives ierarchie celestis et indubie expurgavit Petrum ac perfecit sanctam matrem ecclesiam, sicut quilibet christianus debet facere et specialiter ierarchia ecclesie militantis. Non enim est distinccio primatuum quoad illud, sed quodcunque membrum ecclesie secundum datum sibi lumen intelligencie tenetur communicare tres actus ierarchicos membris singulis matris sue; sicut enim lux corporalis illuminat intellectum, sic membra Ghristi viancia [p. 396] illuminant beatos in patria, dum faciunt eos cognoscere noticia in proprio genere fructus lucis. Unde non est credendum quod in triumphante ecclesia remanent sordes peccati purgandi (ut docetur Ephesiorum VI°), sed purgacio est expulsionis sordium continuacio, sic quod intellectus et affectus civium illuminantur et purgantur per obiectivam presentacionem docium suorum concivium. Et ex istis sequitur quod multitudo civium beatorum sicut et plena eorum beatitudo per actus suos coalternos perficitur, ymmo cum verbum sit in medio omnium membrorum suorum omnibus diebus usque ad consummacionem seculi, non dubium quin cives celestes vident in ipso et audiunt quicquid conservi sui faciunt ad edificacionem ecclesie. Sic enim unum membrum corporis sentit iuvamentum et nocumentum alterius virtute sensus capitis. Hec ergo septiplex ecclesia alloquitur sponsum Christum qui est vir, de quo Jeremie XXXI°, 22, scribitur quod femina circumdabit virum; ipsum autem apprehendit modo novo in sponsum, quando accepit sacramenta tamquam cartas sue redempcionis in effluxu sanguinis et aque in sui latere dormientis in cruce (ut notat Apostolus Ephes. VI°). Et sic hec septiplex ecclesia ante incarnacionem rogat salvatorem, factum hominem, ut auferat obprobrium sue sterilitatis. Panem, inquiunt, nostrum comedemus, quia in verbis legis que in fidem unius Dei instruunt convivemus, nam Hebreorum X°, 38, scribitur: Iustus ex fide vivit, et vestimentis nostris operiemur, quia ex fide creacionis et spe recreacionis cognoscimur quales sumus. Et isto modo loquitur Apostolus, Galat. III°, 27: Omnes qui in Christo baptizati estis Christum induistis. Membra enim Christi non sunt nuda virtutibus, sed induunt armaturam suam saltem in spe, imitando ipsum imperfecte, si [p. 397] sunt de suo exercitu. Sic ergo panem et vestimenta habuerunt patres veteris testamenti, sed sicut non in solo pane vivit homo (ut dicitur Matthei IV°, 4), sic spes confunderet relinquereturque tota vita obprobriosa et sterilis nisi caritas consummans ut potus et edulium data fuerit per dominum Jesum Christum; aliter enim non deleretur peccatum humani generis, nec procrearetur operacio vitalis digna beatitudine, sed remaneret in singulis viatoribus sempiternum obprobrium ut dampnatis. Aufer, inquiunt, obprobrium nostrum, quia remanebimus perpetuo tamquam abortivi vel colobon, nisi tu dans vestem nupcialem et domicilium fueris incarnatus. Nam victus et vestitus non sufficiunt homini sine ultimo stabili tegumento quod est caritas patrie non excidens, data per dominum Jesum Christum. Invocetur ergo super nos nomen Christi, ut dicamur actualiter christiani. Unde istam deprecacionem dicit Augustinus redundare in ecclesiam triumphantem; quamquam, inquit, spirituales sint et celestes potencie, obprobrio tamen subiacent, si a creatore suo fuerint aliene et nec membra erunt corporis que caput suum non cognoscentes oberrant. Vult dicere quod toti ecclesie beatitudo deficeret nisi Christus merito sue passionis redempcionem hominis consummasset. Sed hic videtur dubium: Si patres veteris testamenti fuerant christiani, et videtur Augustinum in ista sentencia contradicere sibi ipsi. Sed notandum quod homines possunt dici tripliciter christiani, scilicet in figura, in effectu et in fructu. In figura vero dicti sunt omnes sancti legis veteris christiani. Si enim dieta dicitur sana propter sanitatem futuram cuius [p. 398] est effectiva, quanto magis patriarche dicuntur pro suo

[ENGLISH]

## ¶2 · 398.2–398.12

> [p. 398] tempore christiani, cum Christus eos denominat membra sua? Christus enim manet in eternum secundum naturam divinam et creatus est a principio mundi nedum in causis secundis communibus, sed in materiali essencia singulari; non tamen assumpsit illam ypostatice, antequam assumens animam fuit homo. In actu autem secundum nomen expressum Christi dicebantur tempore gracie populi christiani et talem nominis denominacionem invocant patres legis veteris super illos; quod et habuerunt, antequam ducti SUnt cum Christo ad celum. Sed post diem iudicii habebunt

[ENGLISH]

## ¶3 · 398.13–398.16

> [p. 398] omnia membra sancte ecclesie nomen christiani in fructu perpetuo. Et patet in parte quod non obstantibus istis declarativis sentenciis remanet prima raciuncula non soluta.

[ENGLISH]

## ¶4 · 398.17–398.26

> [p. 398] Secunda responsio ad secundam raciunculam negat consequenciam; sed videtur, si nulla sit ecclesia nisi multitudo christianorum, sed Christus non est christianus, tunc Christus non est pars vel membrum ecclesie. Concedit itaque quod Christus Deus noster est christianus, nec sequitur, inquit, si a Christo dicitur quilibet christianus, quod Christus ille non sit christianus: sic a creatore dicitur quelibet creatura, Christus est creator et sic ab eo dicitur quelibet creatura et tamen ipsemet est creatura, ut ego assero. to.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 395.23: St. Paul's example teaches us that we must enlighten our brethren.
- 396.9: The whole body of the blest and their bliss are perfected by mutual aid,
- 396.15: and each through the head is sensible of the help or default of others.
- 397.1: The O. T. Church had faith and hope: Christ brought charity.
- 397.26: Men may be called Christians in three ways;
- 398.1: a) in figure, as the O. T. Saints;
- 398.8: b) in fact, as those who live in the time of grace;
- 398.12: c) in fruit, as all members of the Church after the day of judgment.
- 398.17: 2. We said that by our opponent's definition Christ was not a part of the Church.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 394: *1* (print: Isaie IV°, 1: Appre-; short old-style 1, main lacks it) [INS?]
  - 395: *fortis* (alinea E and 183d folio mark glued) [R5]
  - 395: *intelligencie* (30 is the line number) [NW]
  - 396: *beatorum* (alinea F glued) [R4]
  - 396: *perficitur* [R4]
  - 396: *iuvamentum* (print reads iuvamentum) [NW]
  - 396: *Christum* [R3]
  - 397: *sunt* (alinea F and 184a folio mark glued) [THIN]
  - 397: *fuerant* [R3]
  - 398: *suo* (print: pro / suo tempore christiani; main lacks suo) [INS?]
  - 398: *populi* [NW]
  - 398: *∅* (that is the English side-note (We said that)) [INS?]
  - 395: *III°:* (italic, degree sign) [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 394:
4. A: Non enim fas. 10. A in marg. : Conclusio. c5. A in
marg. : Augustinus. 25. 26. A B in marg. : Apprehendent septem mu-
lieres virum de ecclesia intelligitur (Above iSj»1 without mark of reference).
2?. Aug. Quaestiones ex veteri test. cap. XLVII. Opp. tom. III,
Append. pag. 60.

p. 395:
2. In codd.: signa.as; correxi e textu Aug. 0. A m marg. : Que
sunt septem ecclesie designate per septem mulieres et que sunt septem
membra qu.bus eorpus constituitur. 3,. A in marg.: Sicut enim
lux corporahs .Hum.natintellectum, sic membra Christi viancia illuminant
beutos ,n patr.a. B in marg. : Viatores illuminant beatos in patr.a.

p. 396:
9. B: Et omitted. 19. In codd.: Jer. XXI.

p. 397:
11. A in marg. : Passio Christi perfecit nos et omnia. 18. A in
marg.: Augustinus. 26. A B in marg.: Dubium. 29. A in
marg.: Nota quod homines dicuntur tripliciter christiani. 15 in marg. :
Homines dicuntur chnstiani tripliciter.
7. Augustinus quaestio XLVII 1. c.

p. 398:
4. B in marg.: Christus fuit creatus a principio mundi. 9. B:
docebantur. A iri marg.: Utrum patres veteris testamenti fuerant christiani
(Below 184» without mark of reference). 17- A in marg. : Secunda
responsio. 3i. A in marg.: Cristus non est cristianus.
17. Compare pag. 112, 1. 3o.
```

---

## Chunk 17-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-17-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-17-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "398.27–402.24"
divisions: "cap. 17 (heading 'CAP. XVII.' at 388.1); part 4 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "891 words; 763 unanimous or majority-real; 118 settled by vote (INS 2, R2 64, R3a 31, R5a 19, R6a 2); 10 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n435–n439 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 17, part 4: [TITLE]

## ¶1 · 398.27–400.14

> [p. 398] Hic primo notandum quod, si locus a simili (quantumcunque fuerit similitudo insufficiens) valeat ad probandum intentum, periret omnis consequencia et foret omne signabile concedendum, eo quod omnes creature sunt similiores ad invicem, quam natura divina est similis nature create. Ideo necesse est [p. 399] arguentem vel respondentem per locum a simili docere sufficienciam similitudinis quantum attinet ad propositum. Secundo notandum quod Ghristus est simul creator et creatura, nec posset esse ista nisi esset simul duarum naturarum utraque, sic quod secundum naturam divinam est creator et secundum humanitatem est creatura; correspondenter ad propositum, si ipse simul esset Christus et christianus, tunc essent due nature, secundum quarum unam esset Cristus et secundum aliam christianus, sed nec secundum deitatem est Christus pars ecclesie; cum secundum illam non potest parcialiter quicquam componere, nec secundum humanitatem est ipse christianus sed caput omnium christianorum dicente Augustino super Johannem, Sermone CXXIII°, quod super petram que erat Christus fundata est ecclesia; a qua petra Petrus figurans ecclesiam nomen accepit: Non enim a Petro petra sed Petrus a petra, sicut non Christus a christiano sed christianus a Christo vocatur. Sed modo secundum istam ficticiam a christiano et Petro eque dicitur Christus, sicut econtra, cum verbum Dei sit christianus, ut false fingitur. Ulterius declaratur tam per grammaticos quam doctores ex testimonio scripture quod multi erant Christi in veteri testamento, quia reges, sacerdotes et prophete qui crismate erant uncti. Illud autem gratanter accepto cum modificacione tamen quod intelligatur de unccione spirituali qua anima ungitur gracia predestinacionis; solum enim membrum Christi unitum gracia predestinacionis et omne huiusmodi est proprie christianus. Non enim unccio corporalis [p. 400] facit per se christianum, eo quod tunc utraque barba Aaron scilicet superior et inferior foret cum suis partibus christianus. Nec sequitur quod Jesus Christus sit christianus, licet Deus unxit illum oleo leticie pre consortibus suis (ut dicitur Psalmo XLIV°, 8), quia non est membrum Christi, sed caput tocius ecclesie. Unde vere dicitur quod Christus est nomen appellativum, autonomatice conveniens Jesu nostro; ideo propter illam spiritualem unccionem derivatam a Jesu nostro dicimur Christiani et non Jesuani. Omnes enim convenimus cum eo in unccione secundum graciam predestinacionis a qua veste dicimur christiani, non autem sumus sic Christo conformiter salvatores, ideo non dicimur Jesuani.

[ENGLISH]

## ¶2 · 400.15–400.23

> [p. 400] Arguit tamen doctor tripliciter quod dominus Jesus Christus fuit vere christianus. Primo quia christianus dicitur quasi crismate unctus; quod spiritualiter automatice sibi competit. Secundo per hoc quod christianus dicitur quasi observans legem Christi, quod iterum Jesu nostro summe competit; et tercio per hoc quod Remus et Romulus dicuntur Romani, Israel Israelita, et Arrius Arrianus; quare ergo non dicetur Jesus, principium nostre secte vel generis, christianus?

[ENGLISH]

## ¶3 · 400.24–402.4

> [p. 400] Ad primum patet quod non plus sequitur quam si lapis dicitur quasi ledens pedem, et gladius ledit pedem, ergo gladius ille est lapis: Non enim omnis interpretacio est diffinicio. Et per hoc tollitur secunda argucia; nam tota trinitas et angeli, ymmo quelibet substancia creata observat legem Christi, et tamen non pocius quam apostema unctum crismate prescitus dicitur christianus. Quoad tercium dicitur quod, admisso [p. 401] isto triplici assumpto, quod tamen non probatur, non exinde sequitur per locum a simili quod Jesus principium secte nostre sit christianus, quia in dictis generibus fuit unum principium ante predictos, sed non potest esse homo prior dignitate prius principians genus nostrum, quam fuit dominus Jesus Christus; nam fuit ante Jacob unus vir clarius videns Deum, fuit ante Romulum unus homo principium generis Romanorum, et fuit ante Arrium unus heresiarcha qui pertinaciter asseruit Jesum nostrum fuisse solummodo creaturam, ut patet de dyabolo et principibus sacerdotum. Sed fundamentum aliud ecclesie vel generis christiani nemo potest ponere preter id quod positum est Christus Jesus. Ideo secundum Augustinum super Johannem, Omelia ultima, non a christiano dicitur Christus sed econtra; aliquid enim oportet nomen christiani addere super Christum, sicut oportet residuum domus presupponere fundamentum. Unde (si non fallor) non habetur testimonium a sanctis doctoribus quod Jesus Christus fuerat christianus. Non enim sequitur hoc ex sensu Crisostomi, Omelia LIIª Operis Imperfecti, dicentis quod ex hoc dicitur aliquis christianus, quod servat iusticiam, nam intencio sua est dicere quod solum membrum Christi, sive militans sive triumphans, est proprie christianus; aliter enim diceret quod trinitas et omne membrum dyaboli, ymmo quelibet creatura foret christianus, cum omne tale modo suo servat iusticiam. Nam de qualibet creatura iustum est quod se habeat ut Deus ipsam decreverit se habere. Nec sequitur: Porphirius dicit quod genus quandoque sumitur pro generacionis [p. 402] principio et quandoque pro ipsa generacione, ergo Christus Deus noster est christianus. Sed colorate infertur quod Jesus Christus noster sit genus christianorum, quia illius generacionis principium.

[ENGLISH]

## ¶4 · 402.5–402.24

> [p. 402] Sed finaliter colligitur ex dictis quomodo ista sentencia obviat sibi ipsi. Nam respondendo ad primum articulum dicitur conclusionaliter quod vel ante incarnacionem erat ecclesia catholica, et adiungitur una alia conclusio gloriosa, scilicet quod ista ecclesia que incepit in morte Christi per effluxum sanguinis et aque a corpore eius diu fuit ante incarnacionem Christi, sed nunquam ante dictam incarnacionem fuit ipsa ecclesia, sed synagoga. Mirantur logici quo sensu diceretur ista conclusio tamquam logica, cum ista ecclesia cepit esse, antequam fuit synagoga, et per consequens, antequam fuit ecclesia. Ista ergo ecclesia non cepit hora mortis Christi, cum ante incarnacionem fuit synagoga; nec potest hoc pertinenter verificari de aggregato ex talibus personis et forma a qua denominatur ecclesia, quia illud nec fuit ante incarnacionem nec fuit synagoga nec incepit per dictum effluxum, cum pro tunc secundum istam opinionem non fuit Christus, eo quod ex fide scripture Johannis XX° Christus tunc fuit mortuus.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 398.27: He tries to prove that Christ is a christian,
- 399.4: but by a parallel which does not hold.
- 400.15: The doctor gives three reasons why Christ was a christian,
- 400.24: none of which are valid.
- 402.5: Our opponent contradicts himself;

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 400: *automatice* (auto- here, matice next line; main token holds whole word) [R4]
  - 400: *admisso* (ad- here, misso at top of p.401 with 184c folio mark; main token holds whole word, p.401 pos 0 is isto) [THIN]
  - 401: *Christus* [R3]
  - 401: *Christum* [R4]
  - 401: *Christus* [R3]
  - 401: *LIIª* [R4]
  - 401: *Christi* [R3]
  - 402: *Christi* [R3]
  - 402: *per* (15 is the line number) [R3]
  - 400: *∅* (second half of christi-anus; neighbour 128 already christianus) [DELX]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 398:
4. B in marg.: Christus fuit creatus a principio mundi. 9. B:
docebantur. A iri marg.: Utrum patres veteris testamenti fuerant christiani
(Below 184» without mark of reference). 17- A in marg. : Secunda
responsio. 3i. A in marg.: Cristus non est cristianus.
17. Compare pag. 112, 1. 3o.

p. 399:
1. 2. 13 : simili dicere. 12. B: Cliristus vel pars. B: ut secundum.
l5. A in marg. : Augustinus; in codd. serm. CXXIII recte CCLXX (alias
XIII) vide Opp. tom V, pars I, pag. 4 15. 24. B in marg.: Nota
quod solum predestlnatus est propric christianus. 26. B in marg.:
Nota proprie christianus. 27. B: modificacione deest. 27. B:
tamen deest. 3i. A in marg. : Nota quod solum predestinatus est
propric christianus.

p. 400:
4. B: unxerit. 7. A B in marg. : Christus est nomcn appella-
cionem. 8. Autonomastice in codd. 10. B in marg. : Nota bene
quare dicuntur Christiani et non Jesuani. 20. B: summo competit.
26. A B in marg. : Triplex responsio. B in marg.: Christus non est
christianus. 3i. Ainmarg.: Arguitur quod Christus sit christianus
et solvitur (Above i84c without mark of reference). B in marg.: Prescitus
non est christianus.

p. 401:
18 — 20. B : Unde — fuerat deest. 14. A in marg. : Augustinus. 21. A
in marg. : Crisostomus. 25. A in marg. : Qui est proprie christianus.
i5. Aug. In Joh. Ev. cap. XXI. Tract. CXXIV. Opp. tom. III,
pars II, pag. 822. 22. Opus Imperfectum 1 c. pag. CCXVIIl.

p. 402:
3. B: Jesus deest. 5. A in marg.: Nota quando incepit ecclesia.
Prima responsio. 25. A in marg. : Secunda responsio.
33. Aug. Epistola ad Asellicum. Opp. tom. II, pag. 734.
```
