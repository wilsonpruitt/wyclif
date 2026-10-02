# Translation brief: ecclesia 15-f–15-h

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-15-f.md chunks/ecclesia/wyc-ecclesia-15-g.md chunks/ecclesia/wyc-ecclesia-15-h.md` once and fix what it reports.
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

## Glossary (the 182 rows these chunks use; the full file is GLOSSARY.md)

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
| viator | wayfarer | One still on the road, not yet in the homeland. Loserth: "a traveller on earth". Pilot. |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| corpus Christi misticum | the mystical body of Christ | |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| expropriacio | renunciation of property | Never "expropriation" (seizure). Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |
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
| autorizare | authorize | Ruled 2026-09-28 (6 sites). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| ditare | to enrich | Kept apart from *dotare*, endow. Ruled 2026-09-28 (coordinator, delegated) (21 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| brachium seculare | the secular arm | Ruled 2026-09-28 (coordinator, delegated) (7 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| coactivus; cohercere, cohersitivus | coactive; coerce, coercive | Kept apart: *potencia coactiva* "coactive power" (the ruler's), *cohercere* "coerce". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| frater | friar (of the mendicants) / brother | By context. |
| possessionati | the possessioners | Endowed religious. |
| satrapa | satrap | Derogatory: church-court officials wielding delegated power (T. p. 378 n. 58). Keep the word; note it at first occurrence per work. |
| vulgares | the common people | The third estate. Not "the vulgar". Pilot. |
| protestacio; protestari | declaration; to declare solemnly | ⭐ The submission formula ("if anyone can teach me this is contrary to scripture or reason, I will humbly retract"). Penn and Lahey both inverted it (T. pp. 369, 378). Render it as a retraction offer, never as defiance. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| curia romana | the Roman curia | Ruled 2026-09-28 (*Dial.* 7.8; 5 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| perquisitum | acquisition | Property acquired, not inherited (the legal term). Ruled 2026-10-02 (*Eccl.* 215.4). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| credulitas | credence | With *credere*, believe (*Dial.* 23.17–24.4). Ruled 2026-09-28. |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
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
| redarguere | to refute | T. p. 365. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| glosare | to gloss | Interpret so as to remove the difficulty (T. p. 366). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| glosa | gloss | The noun beside *glosare*. Ruled 2026-10-02 (52.10). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| indispensabilis | not to be dispensed | Ruled 2026-10-02. |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| impresenciarum | nowadays, at present | (T. p. 366) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| laude digni | worthy of praise | (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| indispositus; (se) indisponere | unfit; to make (oneself) unfit | "indisposed" (now "unwell"). Ruled 2026-09-28 (8 sites). |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| prevaricator; prevaricancia | transgressor; transgression | Ruled 2026-09-28. *Basali prevaricancia* (*Dial.* 9.24) is doubtful: see its C note. |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| prevaricari | to transgress | The verb of *prevaricator*. Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| ditarius | almsman | The one enriched by the alms (cf. *ditare*, §B). Ruled 2026-10-02 (*Eccl.* 13). |
| pseudomonachus | false monk | Kept apart from *pseudofrater* if it appears. Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "one given alms". Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| ydiota | unlettered man | Never "idiot". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| subdominans | holding lordship under | Beside *dominari*. Ruled 2026-10-02 (*Eccl.* 15, 339.6). |
| redempcio temporalium | redemption of the temporal goods | Chapters buying back seized goods. Ruled 2026-10-02 (*Eccl.* 15, 340.15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| legii | lieges | Ruled 2026-10-02 (*Eccl.* 15, 343–344). |

---

## Chunk 15-f: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-15-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-15-f
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "348.24–352.16"
divisions: "cap. 15 (heading 'CAP. XV.' at 328.26); part 6 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "872 words; 783 unanimous or majority-real; 65 settled by vote (DEL 5, R2 31, R3a 21, R3b 1, R5a 7); 24 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n385–n389 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 15, part 6: [TITLE]

## ¶1 · 348.24–349.16

> [p. 348] Secundo obicitur per hoc quod oportet partes ecclesie habere suam iurisdiccionem et ordinem impermixtum; sed clerus est seculari parte superior, ideo supposito delicto debet corrigi per se ipsum. Confirmatur per hoc quod sic est in celesti ierarchia in qua oportet exemplari omne officium ecclesiastice ierarchie. [p. 349] Ad illud sepe dixi quod falsum assumitur; oportet enim utrumque brachium corporis ecclesie iuvare reliquum, nec est in isto confusio, sed secundum Apostolum Iª Cor. XII° caritativa connexio. Ulterius sepe dictum est quod, sicut clerus stans in suo ordine est seculari superior, sic nominetenus clericus degenerans est inter omnes viatores abieccior. Unde (ut sepe dixi) nobis stantibus in nostro ordine non debemus contemptibiliter esse subiecti principibus, unde glosa ordinaria super XCVIª dist. dicitur quod episcopus est super imperatorem, non tamen si facit contra religionem, nam in illo casu posset a quocunque redargui, ut patet XLª dist., Si papa, vel eciam si scisma faceret, XXIII, q. V, De Liguribus. Et plures sunt casus in quibus layci habent iurisdiccionem super clericos ut dixi; inquit XXIII, q. Vª, Principes.

[ENGLISH]

## ¶2 · 349.17–350.11

> [p. 349] Unde miror quomodo quidam innituntur exemp de celesti ierarchia, putando quod clerici non debent corrigi a laycis, nam stabilito ordine militantis ierarchie, sicut est in ierarchia celesti, procederet racio similitudine quod clerici non forent subiecti laicis, sed si deficit eis virtus illuminandi et expurgandi, sic quod sint ceciores et criminosiores quam layci, quomodo staret in illis perturbantibus ordinem ecclesie exemplum ierarchie celestis? Ideo in defectu illorum stat quod pervertitur ordo ecclesiasticie ierarchie; ordo dico non simpliciter sed ordo individuus qui foret in illis. Non enim est fas fideli credere quod datus clerus servabit ordinem superiorem in ecclesia quantumcunque peccaverit, cum primus angelus cum suis complicibus propter apostasiam ab ordine deiectus [p. 350] est de ecclesia triumphante (ut notatur Is. XIV°). Viator ergo extra ordinem debet habere subsidium a fratre inferioris ordinis, cum pes iuvat oculum, eciam utroque servante integritatem corporis. Et ita videtur Lincolniensi quod angelus superioris ordinis illuminatur ab angelo inferioris ordinis, cum omnes beati spiritus sese iuvant reciproce, ymmo (ut alias dixi): Michael et omnes angeli inferioris ordinis confirmati pugnarunt contra draconem Luciferum et contra complices suos apostatantes, quare ergo non debet esse proporcionaliter in ecclesiastica ierarchia?

[ENGLISH]

## ¶3 · 350.12–351.19

> [p. 350] Sed alias insteti per hoc quod nulla potestas puni- tiva civilis se extendit ad amplius quam potestas civiliter dominandi, sed non licet civili domino dominari civiliter super clerico, cum clericus cui foret licitum servire civiliter posset coloracius civiliter dominari. Sed hic sepe dixi quod de lege nature et de lege evangelii qua astringimur ad correpcionem fraternam debet rex Anglie corripere clerum suum, nec video quin stat clericum servire civiliter eo quod dominari civiliter dicit superbiam. Sed servire civiliter potest esse sine peccato. Nec oportet quod sic homo servit civiliter quod sit servus civilis, cum omnis dominus Anglie sub rege servit sibi civiliter, cum sit eius servitor tenens de rege in capite per servicia suo domino debita et consueta. Servus autem civilis est omnino expers libertatis civilis, et sic serviunt clerici regi libere, qui tenent de illo in capite; et sic videtur mihi quod rex noster habet super clerum suum legium quoad bona nature et bona fortune secundum quid [p. 351] civile dominium. Si autem viverent vitam omnino exproprietariam, sicut vixerunt Christus et Baptista, non forent sic subiecti, et sic racione bonorum fortune et bonorum nature in casu quo contingat in eis abusus vel contemptus notabilis licet regi eos civiliter cohercere, non in quantum sacerdotes, sed in quantum regis elemosinarii vel homines eius legii contempnentes. Et sic regi suo in corpore et bonis multipliciter sunt subiecti. Econtra autem rex debet esse eis subiectus in hiis que sunt ad Deum, ut sit sic mutua connexio caritatis et ordinis utrobique. Tercio arguitur per hoc quod clerus nunquam debet castigari per laicum nisi in defectu spiritualis prepositi, et per consequens nunquam antequam papa defecerit, oportet ergo subditum corripi per diocesanum, secundo per metropolitanum, et si illi defecerint, tunc per papam. Et non est presumendum quod in hiis tribus signis ecclesia Christi deficiet.

[ENGLISH]

## ¶4 · 351.20–352.16

> [p. 351] Hic dicitur quod assumptum est verum, quia ut sepe dixi) clericus nunquam castigari debet per laicum nisi auctoritate ecclesie in defectu spiritualis prepositi et in casu quo clericus fuerit a fide devius. Unde posito de possibili quod omnes episcopi regni nostri deficiant in suis correccionibus post vel ante, racione cuius defectus invalescat peccatum ad regni periculum, regum autem est sub gravi periculo clerum suum corripere quoad corpus vel substanciam cleri, in quibus potestati regie est subiectus; quod si clerus devenit ad tantam profunditatem malicie, spiritualis prepositus omnimode est in causa. Nec est prudentis asserere quod rex expectaret correccionem cleri, quousque papa [p. 352] super isto decreverit, propter multa. Primo quia stat quod in curia redempcio sit venalis, sic quod cum thesauris regni proditor defendat ibidem peccatum suum contra Deum, regem et regnum. Secundo quia stat quod papa et sui cardinales sint acceptores personarum coniuncti hostibus regni nostri. Tercio quia stat eos esse ignaros legis scripture cecatosque tradicionibus hominum propter questum. Quarto quia stat longitudinem et discrimina itineris esse tanta quod nec persone regni nostri haberent illuc securum accessum, nec rex et regnum expectarent tantundem propter regni periculum. Quinto quia Romanus pontifex non habet illam iurisdiccionem in Anglia, nisi vel ex lege Christi, quod limitatur de quanto dicit eis humilius et sanccius legem Christi, vel ex decreto cesaris, ut notatur XCVIª dist. Constantinus.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 348.24: Objection: 2. The clergy, as superior to the laity, should judge itself.
- 349.1: Answer: The assumption is false; all parts of the Church owe mutual help.
- 349.17: As to the pattern of the celestial hierarchy, it is already forsaken when the clergy are wicked.
- 350.12: Objection: If the clergy cannot have dominion, neither can they serve Civilly.
- 350.18: This does not follow.
- 351.4: They are subject not as clergy, but as almsmen and liegemen.
- 351.12: 3. The laity ought to act only in default of the spiritual authorities.
- 351.20: Answer: True; but the King is not to wait for the Pope's action, for many reasons;
- 352.1: 1. because the curia is venal;
- 352.4: 2, Pope and Cardinals are in league with our enemies; 3. they are blinded by avarice;
- 352.8: 4. they are too far away;
- 352.12: 5. the Roman pontiff has no such jurisdiction in England.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 349: *iuvare* (print: corporis ecclesie iuvare) [NW]
  - 349: *Iª* [R3]
  - 349: *XCVIª* [R3]
  - 349: *XLª* [R4]
  - 349: *Vª* [R4]
  - 350: *Lincolniensi* [R4]
  - 350: *per* (descender p) [R3]
  - 350: *puni-* (first half of puni-/tiva (tiva is pos 84); Q is the alinea letter) [R4]
  - 350: *tiva* (second half of puni-/tiva) [R6]
  - 350: *dominari* (print domi- / nari; main token holds the whole word) [R3]
  - 350: *foret* (15 after it is the line number) [R3]
  - 350: *∅* (not is the English side-note (This does not follow); print: dominari. Sed) [R6]
  - 350: *legium* (30 after it is the line number) [NW]
  - 351: *Christus* [R3]
  - 351: *defectu* [R3]
  - 351: *spiritualis* [R5]
  - 351: *diocesanum* [NW]
  - 351: *ut* (print: quia (ut sepe dixi)) [R3]
  - 351: *defectu* (f clear) [R3]
  - 351: *fuerit* [R3]
  - 352: *super* [R3]
  - 352: *stat* (1 and R are margin numeral and alinea letter) [R3]
  - 352: *regni* [R3]
  - 352: *XCVIª* [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 348:
i. in decret: quoniam peccator. 2. B: Episcopus in quantum. A in
marg. : Nota decrctum quantum nocet malus episcopus, papa ctc. (Bclow
I77b without mark ot' refercnce). 4. A B: Ista itaque iura. B in
marg. : Episcopus omittens subditos corrigere dicendus est canis impu-
dicus. 9. A in marg. : Accusator quomodo dcbet se habcrc.
22. singularia. A, addit: nomina.
9. Dec. II pars, causa V, q. V, c. V.

p. 349:
1. A in marg. : Rcsponsio. 5. B: ordinis. 11. A in marg. :
Clerus potest corrigi per laicum. B in marg. : Quod prelati delinquentes
a regibus sunt corrigendi, ut est dignum. 10. A A,: nam — ierarcliic
10. Vid, glossam ad cap. X, dist. XCVI. Duo sttnt. t3. Cap.
tUtt. i5. Cap. XX.

p. 350:
I. B in marg.: Ad tantum potest clericus delinquere, quod non est
credendum eum servare suum ordincm. i3. A in marg. : Instancia.
18. A tn marg.: Racio. 21. B in marg. : Dominari civiliter dicit
superbiam. 23. A in marg.: Condiciones servi civilis. 27. B in
marg. : Servus civilis. 3o. A in marg. : Rex habet civile dominium
super clerum.

p. 351:
8. B in marg. : Sub qua racione re\ potest sacerdotes civiliter cohercere.
10. B in marg. : In hiis que ad Deum perinent rex est subiectus saccr-
dotibus. 12. A in marg. : Clericus nunquam debet castigari per
laicum nisi in defcctu spirituali prepositi, scd non oportct ut papc cor-
reccio cxpectetur. 19. A in marg. : Rcsponsio. 20. A in marg.:
Conclusio notanda. 21. 22. A A, : prepositi in casu. 28. A A, :
quod — omnimode est deest. 3i. A B in marg.: Ficcio.

p. 352:
4. B: Deum et legem. 32. 33. B: istorum et in Gregorio.
```

---

## Chunk 15-g: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-15-g.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-15-g
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "352.17–356.16"
divisions: "cap. 15 (heading 'CAP. XV.' at 328.26); part 7 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1009 words; 922 unanimous or majority-real; 74 settled by vote (R2 41, R3a 22, R3b 1, R5a 9, R6a 1); 13 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n389–n393 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 15, part 7: [TITLE]

## ¶1 · 352.17–354.19

> [p. 352] Sed quantum ad iurisdiccionem istam cesaream vel primatum, patet, cum regnum nostrum sit exemptum a iurisdiccione cesarea, quod nec iurisdiccio coactiva sui episcopi astringit nos nisi de quanto est fundabilis ex sacra scriptura. Sed volvat et revolvat adversarius fidem scripture et non inveniet iurisdiccionem talem. Sed quicunque sacerdos expressius docuerit legem Christi, Christo est in illo obediendum devocius, cum talis primatus introductus est ex ritu cesareo, sic quod, sive prepositus fuerit ydoneus sive non, populus fidelis Christo obediat. Si ergo nos Anglici gratis tantum obedimus papa nostro Urbano VI tamquam humili servo Christi, sicut scismatici obediunt Clementi propter dominium et potenciam secularem, quis dubitat quin ut sic habemus racionem meriti amplioris? Et possibilitatem omnium istorum quinque in Gregorio XI et suis complicibus oculata fide poterimus conspexisse. Dicitur enim quod ipse cum suis pseudocardinalibus dampnavit quatuor veritates [p. 353] catholicas et approbavit quatuor hereses cardinales, sicut vidi notatum in quadam epistola maledicta ab homine, sed a nemine reprobata. Nec horreamus malediccionem huiusmodi, cum veritas ipsa est maledicta pendens in cruce (ut notat Apostolus Gall. III°, et exponit Ambrosius epistola XXXVIIIᵛᵃ). Nam a multis dicitur catholicum per eum quod eo ipso quo ipse vel alius papa Romanus pretendit se quovismodo solvere vel ligare, eo ipso sic solvit vel ligat, cum eius oppositum tamquam sceleratissimum sit dampnatum. Et audeo dicere quod a tempore prime fundacionis Romane ecclesie non fuit tam manifesta antichristiana heresis tam publice proclamata; nam nedum scriptura sacra sed leges papales testantur quod Petrus et omnes successores sui errare poterant, tam in execucione clavium quam eciam in via morum, quod si dictus Gregorius non potest, ipse blaspheme extollitur super omne quod dicitur Deus. Nec video ad quid foret illud tamquam novus articulus fidei divulgandum nisi propter fastum et questum episcopo Scarioth adquirendum. Nam dato illo articulo ipse posset eciam invito Deo liberare omnes animas tam de purgatorio quam inferno, cum in tantam vesaniam posset incidere quod pretendat se ista facere, sicut loquuntur illi qui dicunt quod est Deus in terris. Et quantum ad questum, patet quod isto articu catholicato posset faciliter perquirere omnia regna mundi, quia (da oppositum de regno Anglie) contra, si pretendit se ligare regem nostrum et regnum in partem salutaris penitencie, ut det perpetuo totum fructum regni nostri tenendo episcopo Romano in capite tamquam supremo domino seculari, tunc eo ipso sic ligantur; sed sic potest pretendere se ligare: ergo virtute illius potestatis clavium potest faciliter [p. 354] acquirere regnum nostrum. Et idem est iudicium de omnibus aliis regnis mundi. Et possibilitas minoris patet tripliciter: Primo ex hoc quod taliter ligatus est rex Johannes cum regno (ut dicitur) quoad mille marcas, et idem iudicium est de toto. Secundo per hoc quod multi credunt papam debere dominari seculariter et capitaliter toti mundo, nec verti debet in dubium quin rex et regnum possent obligare se ad tantam elemosinam perpetuam. Sed cui si non pape qui potest absolucionem et dispensacionem super isto soli Romano pontifici reservare? Sic enim dicit se posse restringere potestates clavium de plenitudine potestatis. Tercio confirmatur per hoc quod ipse habet potestatem incomprehensibilem, cui non licet fines ponere, quia tunc formidandus esset, si excedit limites potestatis, et titubaret fides de potestate clavium, et manifeste sequeretur oppositum articuli noviter catholicati, scilicet quod non eo ipso quo pretendit se quovismodo solvere vel ligare, eo ipso sic solvit vel ligat.

[ENGLISH]

## ¶2 · 354.20–356.16

> [p. 354] In tales insanias inducuntur ignari episcopi et doctores facientes ydiotam credere quod potest tantum facere in ecclesia sicut Christus. Unde episcopus Roffensis dixit mihi in publico parlamento stomachante spiritu quod conclusiones mee sunt dampnate, sicut testificatum est sibi de curia per instrumentum notarii. Et visum est multis quod fuit assercio indiscreta, primo quia vergebat ad curie Romane defamacionem, secundo quia implicabat regis nostri et regni scandalizacionem, et tercio quia ostendebat sui et fratrum suorum consentaneam suspicionem. Non enim tam signanter mitterent fratres eius sibi dictam dampnacionem, nisi applaudendo de facto cuius utraque pars foret auctor vel fautor, nec dubium quin stante iusticia dicte dampnacionis cum facto [p. 355] regis et iure quod vendicat, rex et regnum forent expresse heretici, et sic iuxta leges ecclesie nedum exheredandi, sed a toto christianismo funditus destruendi. Nam hoc est hereticatum ut dampnatissimum quod aliqui domini temporales possunt auferre temporalia ab ecclesia delinquente. Unde videtur zelantes pro dampnacione ista intendere quod papa debet super regno nostro imperatorie civiliter dominari (ut sepe tetigi), primo quia procurarunt quod inconsulto rege vel suo consilio virtute bullarum papalium legius homo regis ubicunque in Anglia non convictus super pravitate heretica arrestetur et papali carceri mancipetur, et (ut videtur prudentibus) non posset esse evidencius signum capitalis civilis dominii pape super Angliam. Secundo quia dampnavit ex procuracione quorundam qui videntur esse de nostris quod alique carte humanitus adinvente sunt impossibiles, et per consequens catholicavit oppositum, et cum impossibile et necessarium dicantur condicionaliter et simpliciter (ut patet XXIII, q. IVª, Due sunt) necessitates, sequitur cum veris quod catholicavit omnes cartas cleri Anglie de elemosina perpetua, et per consequens non foret necesse ad regem recurrere pro ratificacione cartarum huiusmodi, cum sint per superiorem dominum nedum confirmate sed catholicate. Et tercio potissime, quia vendicat quod non liceat regi punire clerum suum legium quantumcunque in regnum deliquent nec subtrahere elemosinas cleri quantumcunque contempserit nisi petita ab eo licencia et obtenta, et cum hoc non habet ex lege Christi (sicut patet scrutanti), ab omnibus eius fautoribus relinquitur quod hoc habet a cesare. X Unde vellem quod rex faceret diligenter inquiri a clero suo legio istas quatuor questiones: primo si [p. 356] rex licite potest auferre temporalia a clero suo legio pro contemptu; secundo si rex dominatur capitaliter super regno Anglie et papa sic civiliter subdominans vel econtra; tercio si forme dampnacionum et factorum Romani pontificis hic recitate sint iuri divino consone, et si clericus regis qui vel expresse vel mutescendo consenserit videtur in contemptum regis et regni incidere; quarto autem queritur a plano parliamento regis, cum propter maiorem contemptum sit contemptor gravius puniendus, utrum defendens ista expresse vel tacite contra regem et regnum debeat cum hoc participare elemosinis regni nostri. Videtur enim quod, si susurrones huiusmodi non expectant nisi subdole premittendo preambulam horam illis congruam, quando expulsis secularibus dominis possint dominari ex integro toti regno.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 352.27: How far such jurisdiction can be trusted we may see in the case of Gregory XI.
- 353.1: who approved four cardinal heresies.
- 353.7: Many say it is of faith that the Pope can bind or loose as he will;
- 353.13: but this is a heresy.
- 353.26: Otherwise he might make the realm pay him all its revenue.
- 354.2: This is evident for 1. his predecessor did get 1000 marks from John;
- 354.7: 2. the supreme lordship of the world is claimed for him;
- 354.13: 3, any limitation of his powers would be fatal to the original claim.
- 354.23: Assertion of the bishop of Rochester.
- 355.1: The Pope's bull was directly opposed to English law,
- 355.9: 1. in ordering the arrest of the King's subject without conviction of heresy;
- 355.15: 2. IN asserting the authority of all charters;
- 355.25: 3. above all in declaring that the King may not punish a clergyman however delinquent.
- 356.1: The King should enquire into this.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 353: *partem* (30 is the line number) [R4]
  - 354: *regno* [R4]
  - 354: *mille* [R3]
  - 354: *et* (V is the margin alinea letter) [NW]
  - 355: *consilio* [NW]
  - 355: *alique* [R3]
  - 355: *IVª* [R4]
  - 355: *legium* [NW]
  - 355: *contempserit* (178c is the folio mark) [R4]
  - 353: *catholicas* (178a folio mark glued) [THIN]
  - 355: *regis* (178b folio mark glued) [THIN]
  - 353: *XXXVIIIᵛᵃ).* (superscript va) [OVERRIDE-MARK]
  - 353: *III°,* (line-final; next line starts et, no verse) [OVERRIDE-VERSE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 352:
4. B: Deum et legem. 32. 33. B: istorum et in Gregorio.

p. 353:
ii. A in marg. : Heresis. Papa non semper quando pretendit absolvit.
2i. A in marg. : Prima racio. 26. A in marg. : Secunda racio.
27. B: facilitcr deest.

p. 354:
1. B: idem iudicium. i5. 16. B: Potestatis titubaret. 24. A A,:
stomachando. 33. A in marg. : Conclusio.

p. 355:
3. B: exhedandi. 6. A in marg. : Nota tria. i5. A At:
quia deest. 27. B: dclinqucrit. 33. AB in marg. : Nota quatuor
questiones.

p. 356:
i3. B: si omttted. 17. A in marg. : Pro dominacione civili cleri
fundamentum. 21. A A,: extensior.
```

---

## Chunk 15-h: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-15-h.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-15-h
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "356.17–359.4"
divisions: "cap. 15 (heading 'CAP. XV.' at 328.26); part 8 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "658 words; 590 unanimous or majority-real; 58 settled by vote (DEL 1, R2 34, R3a 17, R5a 4, R6a 2); 10 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n393–n396 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 15, part 8: [TITLE]

## ¶1 · 356.17–358.18

> [p. 356] Innuunt quidam quod habent potestatem ad hoc, quam potestatem vocant dominium, et cum illa immediate sit data a Christo qui dat singulis suis sacerdotibus affluenter, illa potestas est prior, principalior et extencior quam potestas iure hereditario carnali, conquestu vel titulo mundano seculari domino acquisita. Et ad hoc vadunt quotquot conclusiones quas false contra scripturam discipuli Antichristi innuunt ad perturbacionem regnorum et diminucionem religionis christiane, in tantum quod illi Antichristi discipuli sunt capitales inimici illis quibus videntur carnaliter affici, quia dyabolus et omnia membra sua, sicut in imitando sibi ipsis continue sese dampnificant, sic obsunt vere paci aliorum quibus videntur proficere. Allegant autem illud Apostoli Roman. VIII°, 32: Proprio filio suo non pepercit, sed pro nobis omnibus tradidit illum. Quomodo non cum ipso omnia nobis donavit? Et Ia Corinth. III°, 22 [p. 357] Omnia vestra sunt, et Marci X°, 29, dicit Christus quod quicunque reliquerit mundum et carnem propter nomen suum, accipiet cencies tantum. Et in hoc mundo sacerdos (inquiunt) et specialiter religiosus habet ius quod est dominium ad toti mundo seculariter dominandum, et sic Christus docuit eos mundum relinquere, ut secularius conversentur. Sed quesito si layci relinquentes cuncta pro Christo erunt eis participes, si unus excludens alium facit sibi iniuriam, cum aliis que concernunt civile dominium, paciuntur angustias. Ideo defendunt unum capitaneum quem papam nominant sub cuius umbra infideliter sunt protecti. Y Et si obicitur quod curia Romana extinguit multos errores, dicitur quod de tanto est laudabilis et suis satrapis est parendum. Si autem vulpes parvule que demoliuntur particulares vineas habent inibi foveas in quibus convoluti criminibus callidius et constancius defendantur, quis dubitat quin nidus ille foret fons veneni ex cuius rivulis scateat toxica in fidelem ecclesiam militantem? Scutum autem et velamentum huius toxice videntur esse congregacio ista perversa et triplex velum quo mentes fidelium sunt cecate. Nam appellante pecunioso ad illam curiam, quid per mendacia, quid per mala exempla sceleris ibi capta et quid per tradiciones callidas tam de nostris quam de aliis inibi adinventas inductum est scutum infidelitatis ad membrum dyaboli contra regna et sanctam ecclesiam defendendam? Velum autem trimembre statuit inprimis principium quod non licet christiano dictum vel factum eorum discernere, cum sint dii subterranei quibus donata est potestas clavium par cum Christo, qui possunt scripturam sacram statuere, [p. 358] corrigere et mutare, et cum solum convincerentur ex scriptura sacra et factis propriis, patet quod non restat in eos medium accusandi. Secunda pars veli consequenter adicit quod subdi illis tamquam capiti sancte matris ecclesie quomodocunque vixerint est cuilibet christiano de necessitate salutis, et per consequens implere quidquid preceperint, cum non stat (ut inquiunt) quod eorum aliquis sit dampnandus. Tercia pars veli dyaboli est ficta plenitudo potestatis qua exterrent mundum cum pretensa legacione et excommunicacione sic quod, si quidquam decreverint in altera ecclesia faciendum, eo ipso oportet ut fiat; et quia reservarunt sibi cum istis armis potestatem conferendi beneficia ecclesie et superiores ac graviores persone ecclesie extere appetunt symoniace fastum et commodum temporale, ideo propter multitudinem, propter famam et propter terrorem istorum satellitum exterriti sunt pauci simplices dicere veritatem.

[ENGLISH]

## ¶2 · 358.19–359.4

> [p. 358] Sed benedictus sponsus ecclesie qui occidit Gre- z gorium XI. et dispersit suos complices quorum scelera per Urbanum VI. ecclesie sunt detecta, et qualitas veneni ex divisione eorum est quodammodo mitigata. Et utinam placeret sponso ecclesie perficere quod quidam prenosticant et alii imprecantur, scilicet quod numerus undenarius infamis et sterilis, prevaricans in totum decalogum, imponat finem numero pseudoprepositorum dicencium: Hereditate, civilitate et gladio possideamus Dei sanctuarium et Christi patrimonium. Ipse, inquiunt, crucifixus est ligno et apostolus mundo, ut nos occidamus gladio et nobis rebelles crucifigamus in patibulo, quia quam necessaria, inquiunt, fuit in primitiva ecclesia potestas faciendi miracula, tam necessaria est hodie potestas corporalis acquirendi et defendendi temporalia. Scimus tamen quod una potestas infinitum excedit aliam, et quod vita exproprietaria est vita seculari perfeccior et quod tam necessaria erant temporalia clero in primitiva [p. 359] ecclesia sicut modo et quod necessarior foret modo eorum subtraccio et suspensio rapine bonorum cum gaudio, quam tunc fuit, nec est illa ficta defensio fundabilis ex scriptura sacra.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 356.17: Some of the clergy suggest that they have a right above all civil powers;
- 357.10: and their head is the Pope.
- 357.14: The court of Rome is a nest of mischievous foxes.
- 357.27: It has invented for itself a triple shelter:
- 357.30: 1. that it is above all human judgments;
- 358.3: 2. that every Christian is bound to obey all commands of the Curia;
- 358.9: 3. that the Curia has the right of ruling other churches.
- 358.19: God in mercy has taken away Gregory XI;
- 358.27: and we trust he will be the last of these false pontiffs.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 356: *illi* [R3]
  - 356: *Corinth* [R4]
  - 356: *III°* [R5]
  - 357: *Christus* [R3]
  - 357: *toxice* [NW]
  - 357: *factum* [R3]
  - 358: *vixerint* [NW]
  - 358: *Gre-* (first half of Gre-/gorium (gorium is pos 136); Z is the alinea letter) [R3]
  - 358: *gorium* (second half of Gre-/gorium) [NW]
  - 357: *∅* (second half of infideli-tatis; neighbour 197 already infidelitatis) [DELX]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 356:
i3. B: si omttted. 17. A in marg. : Pro dominacione civili cleri
fundamentum. 21. A A,: extensior.

p. 357:
14. A in marg. : Obieccio. 16. A in marg. : Solucio 21. A in
marg.: Scutum et velum dcfenrtencia dominacionem civilem cleri (Above
i-8<i without mark of refercncc). 15: scutum et.

p. 358:
(none)

p. 359:
2. B : subtraccio et suscepcio. 4. scriptura sacra ; A : Scquuntur lingua
Boliemica aliquot verba: Lecz na kawczye horze v Prahy est fundata
newyem. Id est: Si in monte apud Pragam est fundata nescio. 6. A in
marg. : Nota bene istam totam columpnam, quia ponuntur fundamenta pro
dominacion ecivili cleri (Below iy8d without mark of reference). i5. A in
marg.: Prima racio. Nota argumenta pro dominacione cum solucionibus
(Above 179" without mark of reference). 14. B : qui licite. i5. AA, :
pro — elemosinas deest. 20. Codd.: quin a pari.
```
