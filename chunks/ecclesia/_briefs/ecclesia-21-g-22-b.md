# Translation brief: ecclesia 21-g–22-b

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-21-g.md chunks/ecclesia/wyc-ecclesia-22-a.md chunks/ecclesia/wyc-ecclesia-22-b.md` once and fix what it reports.
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

## Glossary (the 207 rows these chunks use; the full file is GLOSSARY.md)

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
| sponsa / sponsus | bride / bridegroom | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). Where privileges or law, not prayers, do the aiding: "to aid" (*Eccl.* 241.1; cf. *suffragium* "aid"), 2026-10-02. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
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
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| legalitas | legal standing | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| indulgencie | indulgences | Ruled 2026-09-28 (7 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |
| autenticus / autenticacio | authentic / authentication | The key term of *Eccl.* 13. Ruled 2026-10-02. |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| respectus; respectivus | relation; relational | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
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
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| viacio | wayfaring | The state of the *viator*. Ruled 2026-10-02 (42.30). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| suffragium (*legis, privilegii*) | aid | As *suffragium* "aid" (01-a) and *suffragium sensus*. Ruled 2026-10-02 (149.29, 152.8). |
| indoles | promise | The natural promise of a thing (the midwives' argument, *Eccl.* 163.18, 164.1–12; Comestor reads *de dolo*). Ruled 2026-10-02. |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| laude digni | worthy of praise | (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| recencius | more freshly | Pilot (*Dial.* 2.10) |
| carecter, caracter (sensibilis) | (perceptible) character | "reputation". The mark of orders. Ruled 2026-09-28 (*Dial.* 5.7). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "almsman" (the 09-28 row governs; conformed 2026-10-02, *Eccl.* 16). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| redempcio temporalium | redemption of the temporal goods | Chapters buying back seized goods. Ruled 2026-10-02 (*Eccl.* 15, 340.15). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| redempcio (of a sentence) | redemption | Buying off a penalty; kept apart from *redempcio temporalium*. C note at first use. Ruled 2026-10-02 (*Eccl.* 15, 352.1). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| ficcio | fiction | As *ficticia*; Wyclif numbers six *ficciones*. Ruled 2026-10-02 (*Eccl.* 16, 385.7). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| legalia | the legal precepts | Of the old law, beside *cerimonialia* "ceremonial precepts". Ruled 2026-10-02 (*Eccl.* 17, 389.2–3). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| quadriga diaboli | the devil's four-horse chariot | Ruled 2026-10-02 (*Eccl.* 18, 427.12). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| habilis / habilitas | qualified / qualification | The positive of *inhabilis* "unqualified". Ruled 2026-10-02 (*Eccl.* 19, 469.4). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| dampnacio | damnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| caracter in actu | character in act | Ruled 2026-10-02 (*Eccl.* 21, 513.18). |

---

## Chunk 21-g: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-21-g.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-21-g
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "515.1–517.26"
divisions: "cap. 21 (heading 'CAP. XXI.' at 491.1); part 7 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "654 words; 551 unanimous or majority-real; 58 settled by vote (DEL 8, INS 7, R2 26, R3a 12, R3b 1, R5a 4); 45 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n552–n554 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 21, part 7: [TITLE]

## ¶1 · 515.1–515.11

> [p. 515] ad folia quam ad fructus creditur facere in oculis Dei sacramenta nostra vilescere. V Sic enim fuit tempore cessacionis legalium multipliciter ritibus humanitus adinventis, et patet via ad solvendum difficultatem qua queritur utrum, dyacono recipiente ab episcopo potestatem absolvendi et non conficiendi vel econtra per mortem aut infirmitatem episcopi vel causam aliam, utrum sit plene sacerdos. Dicitur enim communiter quod non imprimitur caracter sacerdocii ante complecionem verborum sacramentalium

[ENGLISH]

## ¶2 · 515.12–515.13

> [p. 515] sed veritas est quod ignoramus quando et qualiter Deus imprimit sacerdotalem caracterem

[ENGLISH]

## ¶3 · 515.14–515.19

> [p. 515] nec habent evidencie facte ex legibus ecclesie et scriptura vix corticem coloris (ut patet alibi). Ex istis tercio potest convinci quomodo interpolata celebracio sacramenti ordinis potest sive bene fieri sive male Nam in primitiva ecclesia Christus immediate fecit apostolos. suos sacerdotes, hoc est, episcopos, et post ascensionem

[ENGLISH]

## ¶4 · 515.20–516.12

> [p. 515] tempore apostolorum constituerunt dyaconos, nec alios ordines clerici seorsum exhibitos legi illas columpnas ecclesie celebrasse. Et Deus scit utrum ritus ille foret hodie solempnior, facilior et ecclesie Christi utilior. Omnia enim que faciunt clerici inferioris ordinis possunt clerici ex vi potestatis sacerdotalis perficere et a probabili efficacius et humilius quam fiunt modo. Christus enim summus sacerdos exercuit omnia ista officia (ut alias explanavi). Ideo videri posset quod foret ad alleviamen eccle- sie non habere tot ritus sacramentales et tot leges de clericis ordinatis per saltum, cum hoc quod toret ecclesie efficacius et brevius ministratum. Ex alio autem latere posset contingere quod episcopi postposito fastu de excellencia sui ordinis et cupiditate questus de sua preeminencia et necessitate ad regulandum [p. 516] ecclesiam in oculo puro et simplici considerent quod sincerius ministraretur ecclesie ordinatis clericis paulative. Sic enim foret examinacio discrecior, examinati appropriacio ex conversacione experta securior et omnino expulsio persone inhabilis et acceptacio persone habilis ad utilitatem ecclesie foret facilior. Illam autem potestatem ordinandi habent superiores prepositi ex dicto Apostoli, Romanorum XIV°, 19: Que edificacionis sunt invicem custodiamus. Debet autem supponi in istis prepositorum discrecio et per consequens acceptari eorum ordinacio, nisi fuerit ad oppositum vehemens suspicio.

[ENGLISH]

## ¶5 · 516.13–517.26

> [p. 516] Quarto ex predictis potest colligi quomodo nomen clerici superaddit caracterem ordinis conversacionem exproprietariam. Nam habentes ordines inferiores coniugati et conversantes seculariter sunt laici, licet ex favore regni nostri habeant privilegium clericatus, et per consequens non sunt simul cum hoc clerici, cum status illi ex opposito distinguuntur (ut docet Hugo, De Sacramentis, libro secundo parte septima). Et potest confirmari ex decreto beati Jeronimi posito XIIª, q. I. Clericus, et infra, et Iª, q. II. Si quis et Sacerdos, cum multis legibus eis similibus. Et valet ad idem testimonium beati Bernardi libro ad papam Eugenium et testimonia sanctorum alibi sepius allegata. Sed efficacissime videtur mihi valere quadruplex testimonium de clericis veteris testamenti allegatum XIII° capitulo huius libri. Nec valet fingere quod leges veteris testamenti non obligant nos in novo; primo quia ille qui venit non legem solvere sed! implere, cuius factum est optimus interpres quomodo vetus testamentum debet intelligi et servari, docuit [p. 517] quomodo ipse, sui apostoli et eorum vicarii debent vivere pauperem vitam exproprietarie; quod duravit per trecentos annos et amplius usque ad venenosam dotacionem cesaream, ad cuius crementum proporcionaliter decrevit possessionata ecclesia in virtute. Secundo confirmatur ex hoc quod omnia moralia iudicialium vel cerimonialium legis veteris sunt pro tempore legis gracie observanda; cum ergo conversacio pauper et exproprietaria sit moralis, videtur quod post Christum pauperem debet a suis clericis observari; sicut enim mater ecclesia est senior, sic debet esse specialiter in clero religiosior, et per consequens deserendo mundum sponso proprinquior. Tercio confirmatur per deducens ad inconveniens vel per locum a simili; nam decimas et illa que sonant in lucrum clericis accipimus non expressa auctoritate legis nove sed veteris; cum ergo amplectimus minus religiosum legis veteris, videtur sequi quod magis religiosum sit servandum nobis ex integro vel minus religiosum sic racionabiliter auferendum. Non enim licet nobis modo paganico colare nobis placitum de utroque testamento et abicere quod visum est nobis durum, per quod ut clavem Christi religio servaretur et potissime periclitante mundo per venenum avaricie. Sic enim introducta est ex consilio Sergii monachi secta nepharia Machometi.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 516.9: and should not be distrusted without reason.
- 516.13: It is a "character" of the clergy to live in poverty.
- 516.26: This is proved by the Old Testament as interpreted by Christ's acts.
- 517.6: The moral laws of the O. T. are binding,
- 517.15: and we assert them for our tithes.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 515: *in oculis* (print: in oculis Dei; main has no tokens for in oculis) [INS?]
  - 515: *legalium* [THIN]
  - 515: *multipliciter* (print multi-|pliciter; main has multi- here and no pliciter token (pos 17 is the English side-note Question), missing half appended) [THIN]
  - 515: *∅* (English side-note word "Question") [THIN]
  - 515: *solvendum* (main token is the English side-note "ordination"; print at this slot has 5 solvendum) [R4]
  - 515: *∅* (English side-note word "bishop") [DEL]
  - 515: *∅* (English side-note word "is") [DEL]
  - 515: *sacramentalium* (print: verborum / sacramentalium, sed; main has no token) [INS?]
  - 515: *ignoramus* [R5]
  - 515: *quando* (main token is the English side-note "We"; print at this slot has quando (next line)) [R3]
  - 515: *∅* (English side-note word "not") [R6]
  - 515: *et* (print: ecclesie et scriptura; main has no et token) [INS?]
  - 515: *∅* (main "it" is English side-note; matt "5" is the line number 15) [R3]
  - 515: *Ex* (main token is English side-note "would"; print at this slot has Ex) [R4]
  - 515: *istis* (main token is English side-note "be"; print at this slot has istis) [R3]
  - 515: *male* (main token is English side-note "have"; print has sive / male.) [R3]
  - 515: *Nam* (main token is English side-note "no"; print has Nam) [R3]
  - 515: *apostolos* (main token is English side-note "Scripture."; print has apostolos) [R3]
  - 515: *ascensionem* (print: et post ascensionem tempore; main has no token) [INS?]
  - 515: *nec alios* (print: dyaconos, nec alios ordines; main has no tokens) [INS?]
  - 515: *illas* (print: legi illas columpnas; main has no token) [INS?]
  - 515: *ritus ille* (print: utrum ritus ille foret; main has no tokens) [INS?]
  - 515: *Christi* (print: ecclesie Christi utilior; main has no token) [INS?]
  - 515: *perficere* (print per-|ficere et a probabili; main token perprobabili fuses per- with probabili, ficere et a lost; slot = perficere, rest in GAP pos 168) [R3]
  - 515: *et a probabili* (print l.25: ficere et a probabili efficacius) [GAP]
  - 515: *ista officia* (print: omnia / ista officia (ut; main has no tokens) [INS?]
  - 515: *eccle-* (hyphen half, line ends eccle-) [THIN]
  - 515: *sie* (English side-note "This" in slot of Latin sie (second half of eccle-sie)) [THIN]
  - 515: *non* (English side-note "would" in slot of Latin non) [THIN]
  - 515: *∅* (English side-note "relief") [THIN]
  - 515: *de* (English "to" in slot of Latin de (line begins 30 de clericis)) [THIN]
  - 515: *clericis* (English "the" in slot of Latin clericis) [THIN]
  - 515: *∅* (English side-note "bishops") [THIN]
  - 515: *ecclesie* (English "may" in slot of Latin ecclesie (line begins ecclesie efficacius)) [THIN]
  - 515: *efficacius* [THIN]
  - 515: *alio* [R4]
  - 515: *fastu* (print: posito fastu de excellencia) [INS?]
  - 516: *Iª* (superscript a; comma dropped per superscript rule) [R3]
  - 517: *quomodo* (199c is the glued folio mark) [THIN]
  - 517: *Secundo* (2 is the margin argument numeral) [R4]
  - 517: *cerimonialium* [NW]
  - 516: *sed* (199ᶜ folio mark and 1 margin numeral dropped) [OVERRIDE-MARK]
  - 515: *∅* (English side-note "has" (agent 11)) [OVERRIDE]
  - 515: *∅* (English side-note "do" (agent 11)) [OVERRIDE]
  - 515: *sive* (English side-note "which" glued on (agent 11)) [OVERRIDE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 515:
marg. : Questio. 14. B: corticem colorum. i5. A in
conclusio. 25. 26. B: fuit raodo. 3i. A A, : mini-
32. A: continguere.

p. 516:
10 Codd.: debent. i3. A in marg.: Quarta conclusio. i3. 14. B:
quomodonullaclerici. 28. A : 22 cap. corr. : i3. 3o. A in marg. : F.ccio.
22. Decr. sec. pars, c. V, C. XII, qu. I, cap. V. 22. ibid.
causa I, q. II, c VIII et IX. 28. Vide supra pag. 284

p. 517:
3o. Cf. Decr. sec. pars, causa XIII, q. II, c. XXII. Animae.
```

---

## Chunk 22-a: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-22-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-22-a
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "517.28–520.14"
divisions: "cap. 22 (heading 'CAP. XXII.' at 517.27); part 1 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "562 words; 535 unanimous or majority-real; 23 settled by vote (R2 11, R3a 8, R5a 3, R6a 1); 4 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n554–n557 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 22, part 1: [TITLE]

## ¶1 · 517.28–519.13

> [p. 517] Quartum mendacium est ficcio testimonii Hostiensis in Summa de oracionis suffragio pro dampnatis. Scribit enim in libro V°, De Penitenciis et Remissionibus, [p. 518] capitulo Quibus mortuis suffragia ecclesia prosunt, quod quatuor beneficiis specialiter adiuvantur, scilicet missarum celebracionibus, sanctis oracionibus, amicorum elemosinis et ieiuniis cognatorum. Sed quibus mortuis prosunt hec suffragia scolastici varie opinantur. Quidam enim dicunt quod nullis qui sunt in inferno prosunt penitus vivorum suffragia, sed tantum hiis qui sunt in purgatorio. Secundi dicunt quod prosunt omnibus regeneratis qui dum viverent meruerunt ut eis mortuis prodessent suffragia; et quia non sufficimus discernere qui meruerunt et qui non, qui decesserunt in mortali et qui non, ideo oramus generaliter pro omnibus regeneratis. Et valet eciam pro dampnatis quodammodo, cum pro valde bonis sunt graciarum acciones, pro mediocriter bonis et malis sunt propiciaciones, pro valde malis prosunt ut tollerabilior sit eis dampnacio. Prima autem est opinio theologorum et secunda doctorum canonum; que licet sit magis pia, prima tamen est magis catholica. Hugucius tamen dicit quod opinio theologorum parum distat ab heresi, cum de quatuor generibus defunctorum eundem constituat simul et semel bonum et malum. Ideo dicunt decretiste quod Augustinus intellegit in illa divisione quadrimembri per excellenter bonos eos qui sunt in celo, per mediocriter bonos salvandos ad tempus spectantes in purgatorio, per mediocriter malos dampnatos leviter in inferno, et per excellenter malos dampnatos gravius. Et duobus [p. 519] generibus prosunt suffragia in tantum quod Judas in die dominico quievit a pena, licet non sit valde autenticum. Et sic nunquam dimittitur dampnatis pena simpliciter, sed proporcionaliter secundum partem cotam non quantam, et sic glossant dicta sanctorum quod dampnatis non prosunt suffragia, scilicet excellenter malis. Et post sequitur Hostiensis sentencia in hec verba: Non est mihi tanta copia ut ista diffiniam quid debeat teneri precise. Nec Innocencius III. qui tantus erat voluit diffinire sed reliquit disputacioni et discrete investigacioni (ut patet in De Celebracione misse, Cum Marthe). Tamen sentencia theologorum est celebrior et verior videtur.

[ENGLISH]

## ¶2 · 519.14–520.14

> [p. 519] Volve itaque et revolve sentenciam huius doctoris magni in iure canonico et vide si sit testis ydoneus ad confirmandum quod sunt facienda suffragia pro dampnatis ad penam perpetuam. Unde videtur mihi quod totum genus humanum debet concorditerdetestari huiusmodi mendacia et dampnare istam blasphemiam quod licitum est mentiri. Cum enim mentiri sit ex equo peccare (ut dicunt sancti), si licet mentiri, sic licitum est peccare, sed dare illam licenciam non subest potestati divine. Quis ergo blasphemus extolleret se super omne quod dicitur Deus, quod ipse habet privilegium vel licenciam menciendi? Unde graviter fert doctor cum suis quod irridebam istam sentenciam dicendo me nescire quam laudem talis mentitor egregius reportaret, nisi forte ut pre omnibus aliis ferat cotem. Cum enim Deus non potest per se vel alium facere tam solempne mendacium, videtur quod omnes discipuli veritatis debent acui [p. 520] contra illos, et cum ille qui habitat in celis irridebit eos omnes, sui debent irrisione, exprobracione vel racione, ut Deus donaverit confundere istam scolam. Sic enim legitur III° Regum XVIII° quod Helias canus irrisit quadringentos sacerdotes Baal qui seduxerunt populum suis mendaciis; nam illis paciscentibus cum consensu populi quod credatur illi Deo qui fecerit ignem descendere super bovem divinitus comburendum, et cum prophete Baal invocassent nomen Baal de mane usque ad meridiem, et non erat vox que eis responderet, post meridiem illudebat eis Helias dicens: Clamate voce maiori: Deus enim vester est et forsitan cum alio loquitur, aut in diversorio est, aut in itinere, aut certe dormit, ut excitetur.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 517.28: The fourth false quotation, of Hostiensis.
- 518.1: What the teaching of Hostiensis really is. He recites two opposed views;
- 518.10: a) of the theologanis, b) of the canonists,
- 519.6: and declares himself unable to decide;
- 519.11: but leans to the theologians.
- 519.26: The doctor is angry because I have laughed at him.
- 520.4: I have the precedent of Elijah;

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 517: *CAP. XXII.* [HEAD]
  - 518: *ieiuniis* [R4]
  - 519: *Et* [R3]
  - 520: *III°* [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 517:
3o. Cf. Decr. sec. pars, causa XIII, q. II, c. XXII. Animae.

p. 518:
3. B: sacris oracionibus. b. A in marg. : Oracionum suffragia
an dampnatis prosunt (Below 199= without mark of reference). 17. In
codd.: prima inquit. 20. A in marg.: Hugucius.
20. De Hugutio glossatore vid. supra pag. 225 et Fabricii
Bibliothecam latinam VI, pag. 283. Cf. Schulte, Geschichte der
Quellen und Literatur des Canonischen Rechts I, p. 1 56 — 170.
De Hostiensi, ib. II, p. 1 23 — 129. 23. Augustinus in Enchi-
ridio de fide spe et caritate cap. CIX. (Opp. tom. VI, pag. 238)
and c. XXIII, causa XIII, q. II. Tempus.

p. 519:
5. cotam, id est quotam. A, : totam. 7. A in marg. : Hosticnsis.
14. A A,: Volve ct rcvolve itaque. 23. A in marg. : Nota quomodo
mendaces sunt irridendi.
10. Decret. Innocenti! III. Quntn Marthae; Decret. Greg. IX,
lib. III, tit. XLI, cap. VI.

p. 520:
5. A in marg.: Quomodo irrisit Elias quadringentos sacerdotes Baal.
20. A: inscidant. 29. A B: octiplici. 32. A B: deus peries.
27. Vide supra pag. 1 63, 164.
```

---

## Chunk 22-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-22-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-22-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "520.15–524.17"
divisions: "cap. 22 (heading 'CAP. XXII.' at 517.27); part 2 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1008 words; 932 unanimous or majority-real; 61 settled by vote (R2 38, R3a 13, R5a 8, R6a 2); 15 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n557–n561 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 22, part 2: [TITLE]

## ¶1 · 520.15–522.31

> [p. 520] Et correspondenter potest dici doctori mendacii cum omnibus suis complicibus quod scrutetur testimonia omnium scripturarum, ut lumen sciencie et fervor caritatis descendat ut ignis ad istam sentenciam mendacii illustrandam, et certus sum quod licet incidant se cultris et lanceolis quantumcunque super cotem acutis, donec perfundantur sanguine, ut ibi dicitur de sacerdotibus Baal, non invenient conveniens testimonium ad suum mendacium colorandum, solum jn quantum unum adductum testimonium ex Psalmo V°, 7: Perdes omnes qui loquuntur mendacium. Et quia testimonium illud non est conveniens, ideo in dolo allegatur Augustinus pro indole (ut alias diffuse exposui). Sic eciam Jesus noster exprobrat scribas et phariseos Ve octuplici verbis asperis et irrisoriis, ut patet Matthei XXII°, ex cuius doctrina sumpsit Apostolus disciplinam ad dicendum principi sacerdotum: Percuciet te Deus, paries dealbate Act. XXIII°, 3, unde utile foret introducere et docere [p. 521] artem irridendi et exprobrandi, cum in illo homo potest nunc superhabundare, nunc deficere et nunc tenere medium virtuosum; non sic autem in arte mendacii. Quando autem quis ex caritate ad vindicandum Dei iniuriam et ad excludendum errores a sancta ecclesia prorumpit in verba exprobratoria et irrisoria subducto zelo vindicte et laudis proprie, fit opus laudabile quod si integre sensero in me ipso, dicerem ironice cum Apostolo, IIª Corinth. XII° cap., i: Donate mihi istam iniuriam. Quantum ad exprobracionem Hugucii, patet quod fuit ignarus logice, philosophie et veritatis fidei, ideo non mirum si intulit contumelias veritatis catholice professori. Unde Hostiensis respondet ad obiectum suum fatuum: Hii, inquit, qui sunt in purgatorio possunt dici boni et mali diversis respectibus. Boni vero sunt qui salvabuntur, mali autem sunt qui mala sustinent. Nec dubium theologo quin idem in numero sit simul bonum bonitate nature et malum malicia culpe. Ymmo eadem persona est bona bonitate purgacionis sive iusticie et cum hoc mala malicia pene. Unde Augustinus Enchiridion XIV°, 17°: Quapropter in hiis contrariis que bona et mala vocantur illa dialecticorum regula deficit qua dicunt nulli rei simul inesse duo contraria. Cum, inquit, bona et mala nullus ambigat esse contraria, non solum simul esse possunt, sed eciam mala omnino sine bonis et nisi in bonis esse non possunt, quamvis econtra bonum poterit sine malo. Constat quidem philosophis quod bonum et malum nunc dicuntur analogice, nunc equivoce et nunc contrarie, privative aut positive. Unde illi fuerunt ignari dyalectici de secta Manichei de quibus loquitur Augustinus. Contingit [p. 522] enim specialiter sic sumere bonum et malum quod sint sibi ipsis contraria incompossibilia, ut loquitur propheta Isaie V° cap., 20: Ve qui dicunt bonum malum et malum bonum. Illi enim qui dicunt in facto bonitatem moralem esse maliciam viciosam sunt in illa malediccione prophetica. Item, Hostiensis infra, De Remissionibus, capitulo Quibus prosunt, loquens de indulgenciis episcoporum dicit quod mortuis in purgatorio caritate continuatis corpori Christi prosunt ad suffragia merita militantis ecclesie, sed non secundum racionem absolvendi. Potestas, inquit, clavium non habet ibi locum, nec obstat quod ecclesia post mortem ligat et solvit XXIVª, q. IIª. Sane. Nam ibi fit absolucio ad consolacionem vivorum fidelium et confusionem infidelium, et ut ecclesia oret pro mortuo absoluto, sic et equivoce absolvitur mortuus, id est, antequam morietur, absolutus fuisse contricione monstratur, et sic quoad mortuos nihil iam operatur. Nam ubi te invenero, ibi te iudicabo, et sive arbor cadat ad austrum sive ad aquilonem, ibi erit; sed ecclesia militans sepe fallit et fallitur, ut dicit decretalis, De Sentencia Excommunicacionis, A nobis. Nam non mortuos sed vivos astringit potestas clavium, cum solum illi subsunt ecclesie militanti; et sequitur in fine tituli diffinicio doctoris. In inferno vero nihil operantur iste indulgencie, quia ibi nulla est redempcio. Non enim est ibi aliquod bonum quoad penam sed omne malum. Ibi enim non est pena meritoria nec purgatoria nec transitoria sed tantum punitoria et eterna. Hugucius tamen dicit quod ibi est alleviacio pene,

[ENGLISH]

## ¶2 · 523.1–524.17

> [p. 523] paradiso autem nihil operantur, quia anime ibi existentes non egent nostris suffragiis sed econtra. Quintum et ultimum mendacium est accepc testimonii Augustini de refrigerio dampnatorum et primo per illud Enchiridion CX°, ubi dicit quod mediocriter malis qui sunt dampnati prosunt suffragia, et glossa exponit istam quadrimembrem divisionem quod non est orandum pro valde bonis nec valde malis; non pro valde bonis, quia statim advolant et io(ut dicitur libro III°, De Celebracionibus Missarum, Cum Marthe) iniuriam facit martiri qui orat pro martire; nec pro valde malis, quia non meruerunt sic iuvari. Mediocriter vero bonis prosunt, ut cicius liberentur ab igne purgatorio et mediocriter malis prosunt ut micius puniantur, nunquam tamen liberabuntur. Ex quo patet quod orandum est specialiter pro illis qui decesserunt in mortali, dummodo non sint valde mali vel summe mali. Sed dictum est superius in quarto commento mendacii quomodo doctores tam theologi quam iuris canonici exponunt utrumque membrum mediocriter bonorum et malorum de predestinatis in purgatorio penitenciam expectantibus. Quamvis enim omnes illi sint tam boni quam mali et ad penam temporalem dampnati, tamen alia est racio qua sunt boni, et alia racio qua sunt mali, sicut alia est racio qua simpliciter liberantur et alia racio qua micius puniuntur. Nec valet dicta logica glosse communis, cum nihil sit summe malum nisi peccatum, vel forte primus apostata cum omnibus membris suis; quod si non sit orandum pro istis, non est orandum pro prescito; et idem apparet in eadem questione cap. Pro obeuntibus, ubi sub auctoritate beati Gregorii decretum sic loquitur: Congruit ut pro mortuis catholicis sacerdos memoriam faciat et [p. 524] intercedat, non tamen pro impiis (quamvis christiani fuerint) tale quid agere licebit. Super quo dicit eadem glossa: Si est evidens aliquem decessisse in mortali, ut cum QUIS suspendit se vel precipitat aut alio modo se interficit, pro eo non est orandum, ut XXIIIª, q. V°, Placuit, et q. VIIIª, Quicunque clericus. Secus est, si est dubium: unde pro occiso in ebrietate non oratur (ut Extra., De Reliquiis, Audivimus). Quomodo queso ordinarentur tot leges ad non orandum pro mortuo in mortali secundum suspicionem fallibilem, si debemus specialiter orare pro illo quem scimus dampnatum perpetuo? vel quomodo specificaret ecclesia oracionem pro mortuis in missa dicendo: Memento domine famulorum tuorum qui nos precesserunt cum signo fidei et dormiunt in sompno pacis, si generaliter orandum est pro illis quibus pax ex perpetuitate vermis consciencie est incompossibilis

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 520.15: and, like Elijah, I challenge my opponent to shew the Divine sanction for his teaching,
- 520.23: for God never approves lies.
- 521.11: The objection of Hugucius is of no weight.
- 522.7: Hostiensis tells us that indulgences cannot absolve in purgatory,
- 522.23: since the power of the keys extends only to the militant Church.
- 523.3: The fifth and last false allegation is of Augustine.
- 524.1: The decretal forbids praying for suicides, and even for those slain when drunk.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 521: *artem* (199d is the glued folio mark) [THIN]
  - 521: *irrisoria* (200a is the glued folio mark) [R4]
  - 521: *IIª* [R3]
  - 521: *Hugucii,* [R4]
  - 521: *17°* (degree sign; colon dropped per superscript rule) [R3]
  - 522: *loquitur* [R3]
  - 522: *∅* (English side-note "tells"; Latin Item, is the next token) [R4]
  - 522: *caritate* [R3]
  - 522: *XXIVª* [R3]
  - 522: *IIª* [R4]
  - 523: *CX°* [R4]
  - 524: *interficit,* [R3]
  - 524: *XXIIIª* [R3]
  - 524: *VIIIª,* (italic) [OVERRIDE-MARK]
  - 520: *XXII°,* [OVERRIDE-VERSE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 520:
5. A in marg.: Quomodo irrisit Elias quadringentos sacerdotes Baal.
20. A: inscidant. 29. A B: octiplici. 32. A B: deus peries.
27. Vide supra pag. 1 63, 164.

p. 521:
11. A in marg. : An dampnatis prosunt sufiragia (Above 200* without
mark of reference). 20. persona (?) in codd: pe. 22. In codd.:
Enchiridion XVII. A in marg. : Augustinus. 29. U ia marg.:
Iionum accipitur tripliciter.

p. 522:
17. B: moriretur. 23. A in marg.: Ecclesia militans sepe fallit
et fallitur. 3i. A in marg. : Hugucius.
14. Decr. sec. pars, causa XXIV, q. II, cap. VI. 20. Comp.
Eccles. XI, 3. 23. Decr. Greg. IX. lib. V, tit. XXXIX, c. XXVIII.

p. 523:
4. A in marg. : Augustinus. 5. In codd.: Enchirid. CXXIV.
3i. Decr. sec. pars, causa XIII, q. II, cap. XXI.

p. 524:
2. In codd.: tale in quid. 3. In codd.: glossa. Est evidens.
Correxi e textu glossae (Pro impiis) ad caus. XIII, q. II. Pro obeuntibus.
ibid.: suspendat. Correxi e textu glossae. Vide Decretum Gratiani una cum
glossis (Venet. iCo5) pag. 97! 18. A in marg.: Argumentum pro
salvacione omnium. 18. In codd.: XXII de civitate Dei cap. XXIII.
23. In codd.: orabat.
18. Aug. Opp. tom. VII, pag. 641, 642.
```
