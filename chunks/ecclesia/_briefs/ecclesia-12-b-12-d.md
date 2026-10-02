# Translation brief: ecclesia 12-b–12-d

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-12-b.md chunks/ecclesia/wyc-ecclesia-12-c.md chunks/ecclesia/wyc-ecclesia-12-d.md` once and fix what it reports.
6. Final message: per chunk, the ledger rows (table: id | chunk / note | claim | status | how / next step),
   glossary proposals, Latin doubts, and a one-line note of anything the coordinator must decide.


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

## Glossary (the 161 rows these chunks use; the full file is GLOSSARY.md)

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
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
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
| autorizare | authorize | Ruled 2026-09-28 (6 sites). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| legalitas | legal standing | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| indulgencie | indulgences | Ruled 2026-09-28 (7 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| conducentes | those who hire them | Ruled 2026-09-28. |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| possessionati | the possessioners | Endowed religious. |
| satrapa | satrap | Derogatory: church-court officials wielding delegated power (T. p. 378 n. 58). Keep the word; note it at first occurrence per work. |
| vulgares | the common people | The third estate. Not "the vulgar". Pilot. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| curia romana | the Roman curia | Ruled 2026-09-28 (*Dial.* 7.8; 5 sites). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| locus a maiori / a simili | the topic from the greater / from the like | The dialectical topics. Ruled 2026-10-02 (*Eccl.* 144.27). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| facinus | misdeed | Wyclif equates it with "felony" (239.13, 239.21). Ruled 2026-10-02. |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| fallacia | fallacy | Ruled 2026-09-28. |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
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
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| insensibilis | imperceptible; of a thing that cannot feel, without sensation | Two senses by referent: what cannot be perceived / what cannot perceive (*lapis insensibilis*, *Dial.* 56.3). Kept visibly paired with *sensibilis*. Ruled 2026-09-28 (3 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| illabi | to flow into | Ruled 2026-09-28. |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| sciolus | knowing, wise | "smatterer" (the classical sense). Neutral in Wyclif. Pilot (*Eccl.* 5.8) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| recencius | more freshly | Pilot (*Dial.* 2.10) |
| prevaricator; prevaricancia | transgressor; transgression | Ruled 2026-09-28. *Basali prevaricancia* (*Dial.* 9.24) is doubtful: see its C note. |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| prevaricari | to transgress | The verb of *prevaricator*. Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |

---

## Chunk 12-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-12-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-12-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "254.24–258.22"
divisions: "cap. 12 (heading 'CAP. XII.' at 250.17); part 2 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "943 words; 838 unanimous or majority-real; 86 settled by vote (DEL 1, R2 55, R3a 23, R5a 6, R6a 1); 19 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n291–n295 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 12, part 2: [TITLE]

## ¶1 · 254.24–258.7

> [p. 254] Unde vani sunt casus quibus ponitur Deum auferre a justo graciam vel adnichilare hominem sine suo demerito; hoc enim derogaret omnipotencie et supremo dominio Dei nostri. Ideo cum notum sit quod Deus, si sic faceret juste faceret, non restat nisi expectare in fide predicta, quousque probatum fuerit, si poterit, quod Deus possit sic facere; nichil itaque repugnat potencie adnichilandi cum illa non potest esse, et ista exemplaris iusticia in Deo debet esse exemplar cuilibet eius vicario, tam pape quam regi, ut non faciat [p. 255] iniuriam alicui. Unde blasphemant quidam extollentes papam sophistice super omne quod dicitur Deus, qui dicunt quod licet sibi auferre beneficium a subdito non demerente nec facta debita recompensacione aliunde; hoc enim non est Deo licitum et si Antichristus illud presumpserit, tunc Christus faceret humiliter pacienti iniuriam recompensam. Et eodem modo dicitur de dominis temporalibus; non enim licet eis spoliare sanctam matrem ecclesiam, nisi prius deliquerit abutendo elemosinis datis pauperibus, et multo magis non licet regi concedere membris diaboli licenciam iniuste oblata a sancta matre ecclesia perpetuo detinendi, quia hoc foret maior iniuria. Unde notare potest indifferens quomodo sum specialior procurator pro conservandis privilegiis et bonis sancte ecclesie, quam illi qui dicunt quod licet dominis temporalibus concedere latronibus ut sine restitucione retineant quecunque bona sancte ecclesie. Et si obicitur quod volenti non fit iniuria, sed totum regnum est virtualiter congregatum in parliamento, ergo consenciente parliamento ad aliquid non fit regno iniuria, licet scelerati habuerint in ecclesia privilegium supradictum, patet quod consequencia non procedit. Nam stat quod signando volenti fiat manifesta iniuria, ut posito quod quis velit peccare et habeat excitatorem et fautorem criminis, hinc primo peccatori volenti fit iniuria a proximo culpabiliter excitante. Ymmo quandocunque prepositus omittit debitam correpcionem propter falsam pietatem volentis sordescere, iniuriatur eidem, ut Hely dampnabiliter iniuriatus est filiis suis Ophni et Finees, quam iniuriam ipsi dampnabiliter voluerunt. Et multo magis fovens hominem in peccato propter pecuniam, iniuriatur [p. 256] eidem, et ita generaliter quandocunque quis consentit culpabiliter temptatori; nec est hic sophisma: Petrus vult id quod de facto est peccatum vel formaliter antecedens ad illud, sed non vult peccatum, sicut sophiste dicunt quod formaliter vult percutere Petrum scit quod ille est sacerdos, et tamen non vult percutere sacerdotem. Nam sophisma istud est impossibile (sicut alias declaravi); tunc enim non foret volucio vel concessio implicita, quia si homo vult particulare per accidens implicitum in universali per se primo volito, multo magis vult implicite formaliter consequens ad per se volitum, ut si rex vult quod Petrus clericus habeat dictum privilegium, quia vult quod omnis clericus regni sui habeat dictum privilegium, et Petrus est aliquis talis clericus, multo magis vult omne formaliter sequens ad illud. Unde necessitas cogit eciam avaros concedere hanc logicam, cum aliter non participarent privilegiis vel elemosinis principum, nisi in concessione vel volucione generali, notata in cartis illis, implicite sit concessa participacio elemosine generalis. Et isto modo concedunt catholici quod in Petro procuratore ecclesie concessa est a Christo generaliter in quodam involucro potestas ordinis cuilibet sacerdoti sequenti. Cum ergo peccatum patenter sequitur ex actibus volitis cum suis circumstanciis, videtur quod volens illud antecedens vult saltem implicite peccatum consequens. Sic enim dicit Augustinus quod omne peccatum est voluntarium, et fides scripture sepe dicit quod homo vult et diligit multa mala, et tamen notum estquod nonvult ipsa explicite secundum racionem qua mala. Et hec racio quare necesse est dominos temporales in quacunque concessione generalis privilegii vel elemosine perpetue subintelligere [p. 257] condicionem dignitatis persone capacis (ut dictum est XX° cap. libri proximi et sepe alias). Unde (ut dixi hic) Deus non potest subintelleccionem talis condicionis pretermittere, et curia Romana declarat in omni concessione sua de privilegio condicionem debere subintelligi (ut in proximo capitulo allegatur decretum pape XXVª q. I, Ideo permittente). Absit itaque ut imponamus dominis temporalibus tantam blasphemiam quod ipsi non sint Deo subiecti subintelligentes condicionem, si Deo placuerit, cum Jacobi IV° docetur tota christiana religio de cunctis operibus futuris exprimere vel saltem subintelligere si Deus voluerit; aliter enim posset discolus vendicare elemosinas principum stante maxima discolia; et sic inficerentur elemosine (ut dictum est XXIV cap. libri proximi). Unde Archidiaconus dicit quod tales discoli non sunt illi quibus elemosine sunt concesse. Attenderemus ergo ad dictum Dei, 1° Regum II°, 30, concedentis Hely etsuo generi sacerdocium perpetuum: Loquens, inquit, locutus sum, ut domus tua et domus patris tui ministraret in conspectu meo usque in sempiternum. Nunc autem dicit Dominus: Absit hoc a me, sed quicunque honorificaverit me, glorificabo eum, qui autem contempnunt me, erunt ignobiles; non potest blaspheme intelligi quod Deus sit contrarius sibi ipsi, cum secundum Apostolum se ipsum negare non potest, sed quia subintellexit condicionem de Hely et suo genere quantum ad sacerdocium perpetuum, quam condicionem ipsi peccando diruperant, necesse fuit ex iusto iudicio veritatis, ut transferretur ab illo ad alium per donum Dei. Aliter enim Deus foret auctor iniurie. Ideo sepe dedi clericis nostris [p. 258] consilium quod honorarent scripturam sacram, tam verbo quam opere, quia sine conservacione huius est quodmaneat dignitas ad privilegium vel aliquod bonum gratuitum capiendum. Alie autem carte prosunt quandoque per accidens, sed nunquam nisi in virtute testamenti domini principaliter observati.

[ENGLISH]

## ¶2 · 258.8–258.22

> [p. 258] Tercio principaliter obicitur per hoc quod privilegium regum est pie et misericorditer interpretandum, ymmo necessitante casu ad aliquod inconveniens fugiendum est maius inconveniens et inconveniens minus tollerandum. Non ergo sequitur: dato privilegio sequitur inconveniens, ergo ipsum est impium vel tollendum, cum tunc evangelium, passio Christi et omne bonum foret tollendum, cum occasione male accepta malum ex illo provenit. Et istum obiectum clamant tam scolastici quam vulgares in tantum quod unus iuridicus dixit michi nullam esse legem universalem humanam, quin sepe in casu necesse sit ex illa sequi iniusticiam iudicando. Ideo attendendo ad maius bonum fructus quam malum defectus, debet malum nedum permitti sed fieri propter bonum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 254.24: It is therefore useless to put cases in which God is supposed to do so;
- 255.1: and what God cannot do the Pope cannot do rightly,
- 255.8: nor can secular lords.
- 255.13: I (Wyclif) am the real advocate of Church privileges.
- 255.19: 3. It is said that the realm, through parliament, has consented and is therefore not injured; Answer: We may do injury to a willing man a) in helping him to sin,
- 255.27: b) in not punishing him for sin,
- 255.31: c) still more in taking money to
- 256.1: abet him in his sin
- 256.27: There is implicit sin In acts that lead to sin, even when that result is not intended.
- 257.3: Hence all grants shoald be conditional on worthiness in the grantee.
- 257.18: Even God's promises are thus conditional.
- 258.1: Hence Wyclif's warnings that the clergy may forfeit their privileges.
- 258.8: 3. It is objected that a) the king's grant should be interpreted mercifully;
- 258.14: and that b) a privilege is not proved to be evil by an occasional wrong.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 254: *demerito* (hyphenated de-/merito; main token holds whole word) [R3]
  - 254: *repugnat* (30 is the line number) [R3]
  - 255: *iniuriam* (C 164ᶜ margin alinea + folio mark) [R3]
  - 255: *aliunde* (5 is the line number) [R3]
  - 255: *regnum* [R4]
  - 255: *congregatum* [R3]
  - 255: *parliamento* (hyphenated parlia-/mento; main token holds whole word) [R3]
  - 255: *privilegium* (164ᵈ folio mark glued in other scans) [R4]
  - 255: *fiat* [R3]
  - 255: *manifesta* (bold argument numeral 1 glued) [R4]
  - 256: *∅* (inserted run is the end of p.255 (already in p.255 main); print line begins eidem, et ita) [INS?]
  - 256: *consentit* (3 D after it is margin numeral + alinea letter) [R4]
  - 256: *volitum* [NW]
  - 256: *volitis* [NW]
  - 257: *itaque* (165ª folio mark glued) [R4]
  - 257: *Regum* [R3]
  - 257: *II°* [R3]
  - 258: *tam* ('may' in other scans is English side-note text) [R4]
  - 257: *condicionem* (164d folio mark glued) [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 254:
6. B: Vel per. i3. A A,: confiscancia. i5. equininiiter in
codd. 19. A in marg. : Conclusio. 23. tribuet in codd.
24. A in marg. : Deus non potest iniuste auferre nec potest annichilare
(Above 164' without mark of reference).

p. 255:
8. A A,: dicetur. II. A Ax: membro. 12. A: detenendi.
19. A in marg : Obieccio. Maleria super voluntate peccati (Above
■64d without mark of reference). 23. A in marg. : Conclusio.
27 li in marg. : Volentia lit iniuria.

p. 256:
2. A in marg. : Sophisma. 6. B; cum non vult. 10. B in
marg. : Volucio duplex implicita scilicet et explicita. 27. A in marg. :
Augustinus. 3i. A in marg. : Conclusio.

p. 257:
16. A in marg.: Archidiaconus. 20. A in marg. : Deus donat sub
condicione. 3o. Codd.: transterreretur.
7. Causa XXV, q. I, cap. XVI. 26. II. Timoth. II, i3.

p. 258:
1. A B in marg. : Consilium bonum. 8. A in marg. : Contra.
Tercia obieccio. 12. B: Non ergo — tollendum cum decst in tcxtu;
cxtat in marg. inf. 23. A in marg. : Responsio. 29. A in marg. :
```

---

## Chunk 12-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-12-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-12-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "258.23–263.26"
divisions: "cap. 12 (heading 'CAP. XII.' at 250.17); part 3 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1152 words; 1046 unanimous or majority-real; 89 settled by vote (R2 51, R3a 28, R3b 1, R5a 8, R6a 1); 17 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n295–n300 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 12, part 3: [TITLE]

## ¶1 · 258.23–263.26

> [p. 258] istum obiectum. respondeo concedendo assumptum. seci nec lex Dei nec aliqua lex justa necessitat ad aliquid culpabiliter faciendum, ideo necesse est?. leges tales habere prudentes interpretes secundum sensum sacre scripture, ut tam privilegiantes quam privilegiati active et passive participant meritorium fructum privilegii, salvato semper iure cuiuslibet et postposita generaliter iniuria undequaque. Unde non est possibile legem rectam statui et casum contingere, quin secundum regulam sacre scripture tolli potest inconveniens peccati, quia ad minimum non existente [p. 259] fuga alia tolli debet statutum aut privilegium vel suspendi, nec fallat inscios ignorancia illius veritatis quam Anselmus declarat primo, Cur deus homo, XXI°, quod nec propter salvacionem tocius mundi vel infinitorum, si fuerint, non debet committi peccatum aliquod eciam veniale, quia tunc peccatum esset non peccatum, cum non sit possibile ut quis peccet in quantum facit ut debet, quia tunc debet peccare et prima iusticia exigit ut sic peccet. Sed revera iusticia dispensaret in casu huiusmodi, ut non peccet. Oportet ergo privilegia huiusmodi habere interpretes ad discernendum condicionem que debet subintelligi in tali privilegio, ut si quis proditorie occiderit regem, notorie molitus fuerit regni prodicionem, vel corporaliter aut spiritualiter superinduxerit simul vel paulative depopulatores regni, refugium ecclesie non ad illum. Unde recoleremus statutum nefandum Danielis VI°, 7, ubi dicitur satrapas consuluisse Dario, ut extinguerent Danielem, quod omnis qui peciverit aliquam peticionem a quocunque Deo et homine usque ad triginta dies nisi a rege Dario mittatur in lacum leonum, sed postquam compertum est Danielem tribus temporibus in die adorare Dominum versus Jerusalem, sinistri interpretes regem seduxerant, ut Daniel in lacum leonum mitteretur; sed iniquum iudicium probavit eventus miraculi. Et utinam satrape nostri non seducant principes ex insana interpretacione decreti regii. Nam vel est quodcunque tale decretum illicitum, vel oportet quod solum intelligatur in ipso quod nullius sapit [p. 260] iniuriam, quia iuxta dicta in proximo argumento oportet subintelligere in omni tali generali statuto beneplacitum prime iusticie. Oportet ergo secundum regulas scripture docere quod implecio privilegii generalis in casu posito sit consona legi Dei. Et si consiliarii sapientes mundialiter exigunt ex verbis privilegii tamquam concessum omne quod sciverint sophistice palliare, exacta est cum satrapis Medorum blasphema peticio; ipsi enim exigunt concessum a principe omne quod sophistice inferre possunt ex verbis privilegii, sive iustum fuerit sive iniustum, seu parti privilegianti aut privilegiate meritorium fuerit aut demeritorium, et ita sive Deus illud voluerit sive noluerit. Sed in istam blasphemiam non potest princeps seculi nec eciam Deus ipse, ideo instruendi sunt religiose domini seculares, ne ex ignorancia condicionis privilegii et interpretacionis eius participent tali blasphemie; videntur enim cecis secundum formam talem concedere sed non possunt. Sicut autem non possunt concedere quod manifeste vergeret ad destruccionem regni sui vel Dei iniuriam, sic non possunt concedere privilegium quod inferret per se alicui iniuriam vel quod occasione data suis subditis sit dampnosum. Concessio enim talis subdola non est concessio, sicut nec luciferina promissio Matthei IV°, 9, qua Jesu nostro false promiserat quod omnia regna mundi sibi daret, si cadens ipsum adoraverit, non fuisset donacio, nec fas est dogmatizare istam blasphemiam, ut eo ipso quo princeps terrenus decreverit sic esse, sequitur quod sit iustum, quia sanctus Nabuchodonosor qui fuit unus de potencioribus monarchis a mundi principio non potuit vendicare istam potenciam, cum soli Deo sit propria. Et dico ipsum [p. 261] sanctum, quia decret. XXIIIª, q. IV. Nabuchodonosor ex testimonio Augustini reputat eum sanctum. Ex istis colligitur quod concessio privilegiorum principum non minus dependet a privilegiandis qui ipsis participent quam ab ipsis principibus. Patet ex hoc quod non foret illis privilegium, nisi supposita capacitate ex vita meritoria participio talis privilegii forent digni; cum ergo talis dignitas essencialiter dependet ab illis privilegiandis et non ab illis privilegiantibus, patet conclusio. Ymmo cum privilegiacio passiva potest inferri ab aliis quam a datis principibus, (non autem potest inesse nisi insit ex dignitate quam privilegiatus perficit in se ipso), videtur quod talis passiva concessio vel privilegiacio prius natura dependet a privilegiandis quam ab istis privilegiantibus a quibus solum causatur per accidens. Concessio vero eciam activa dominorum, secundum racionem qua foret isti clerico privilegium, dependet essencialiter ab eodem clerico, quia si non meruerit, tunc dominus in concessione generali non concessit privilegium illud sibi, ideo (sicut dixi in solucione proximi argumenti) optimum medium conservandi privilegia est ut privilegiandus conformet se sacre scripture, quia (ut dicitur Matthei V°) eo ipso quo ipsam habuerit adversarium perdit privilegium, quia vitam propriam, in qua vivificata per Christum privilegium fundaretur. Conceditur ergo quod pie et misericorditer racione privilegii principum agendum est cum talibus fugitivis, sed (ut dixi proximo capitulo) cavenda est falsa pietas et misericordia iniusta. Ipsam autem declarat decretum sub auctoritate beati Ambrosii in libro suo De Officiis, [p. 262] ut recitatur XXIIIª, q. IV, ubi dicitur: Est iniusta misericordia. Denique scriptum est de quodam: Non misereberis illius, Deuteronomii XIX°, 13, et in libris Regum legitur quod Saul contraxit offensam, quia misertus est Agag regem hostium quem prohibuit divina sentencia servari, I° Regum XV°. Itaque si quis latronem filiis deprecantibus motus et lacrimis coniugis eius inflexus absolvendum putat, cui adhuc latrocinandi aspiret affectus, nonne innocentes tradet exicio qui sic liberat multorum exicia cogitantem? Certe si gladium domini reprimit, vincula dissolvit, laxat exilium, cur latrocinandi qua potest clemenciori via non eripit facultatem qui voluntatem extorquere non potuit? Deinde inter duos, hoc est, accusatorem et reum, pari periculo de capite decertantes, alterum si non probasset, alterum si esset ab accusatore convictus, si non id quod iusticie est iudex exequatur, sed miseretur alterius, aut dampnabit probantem aut dum accusatori favet, quod probare non possit, addicet innoxium. Non potest ergo hec dici iusta misericordia. In ipsa ecclesia, ubi maxime quis misereri debet, teneri autem quam maxime debet forma iusticie, ne quis a consorcio criminacionis abstractus brevi lacrimula atque ad tempus parata vel eciam uberioribus fletibus communionem, quam plurimis debet postulare temporibus, a facilitate sacerdotis extorqueat. Nonne cum uni indulget indigno, ad prolapcionis contagium provocat universos? Facilitas enim venie incentivum tribuit delinquendi. [p. 263] Quotlibet enim sunt tales leges cum racione docentes quod iudex debet secundum leges punire, faciendo utrique parti iusticiam. Princeps ergo precludens cursum talis iusticie est omnino reus iniune; si enim antedictum privilegium fuit iustum de multis quod non obstante tali aufugio subirent penam legalem, quomodo excusat peccatum principis, quin dimissis magis induratis in suo facinore iniuriaretur Deo et partibus? Non enim facit regis concessio ut sic varietur iusticia quoad Deum, secura ergo via misericordie est dare tali criminoso quadraginta dies penitencie et post punire vel dimittere secundum disposicionem persone culpabilis, quia secundum illam misericordia vel crudelitas est taxanda. Et utinam hoc privilegium in recentibus criminosis observaretur per totam Angliam, aliis sceleratis deprehensis post correpcionem terciam secundum legem evangelii Matthei XVIII°, castigatis scilicet vel ociosis in casu quo probabiliter credatur illos intoxicare plus sancte matris ecclesie in futurum, vel aliter proscriptis in casu quo credatur illis prodesse profugis. Tale enim opus ex caritate procedens servaret undique misericordiam et (quantum est in homine) libertatem. Quantum ad secundam difficultatem in qua quidam instant fortiter, quod pro execucione et observacione legis debet iudex facere eciam scienter iniuriam, patet

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 258.23: Answer: a) We grant the assumption, but the interpretation must be wise.
- 259.1: A statute or privilege may need to be suspended.
- 259.18: Instance of the law made by Darius.
- 260.4: The privilege must in each case be used in accordance with God's law;
- 260.19: nor may rulers grant what is injurious to their subjects or to individual rights.
- 261.3: The concession of privileges depends as much on the grantee as the granter.
- 261.27: We must beware of false mercy,
- 262.1: against which we are warned by St. Ambrose.
- 263.3: A prince who interrupts the course of justice is guilty of wrong.
- 263.24: b) That a judge is to do wrong in obedience to law is contrary to the catholic faith.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 258: *∅* ('the' is English side-note text (We grant the); print: Ad istum obiectum) [INS?]
  - 258: *lex* [R4]
  - 258: *Dei* [R3]
  - 258: *ad* [R3]
  - 259: *fuga* (F alinea + 165ᵇ folio mark glued) [R3]
  - 259: *veritatis* [R3]
  - 261: *sanctum* (G alinea + 165ᶜ folio mark in margin) [R3]
  - 261: *privilegii* [R3]
  - 262: *recitatur* [THIN]
  - 262: *XXIIIª* [THIN]
  - 262: *Denique* [R3]
  - 262: *I°* (full-height capital I with degree sign) [R3]
  - 263: *facere* [NW]
  - 263: *iniuriam* [NW]
  - 263: *patet* [R3]
  - 261: *XXIIIª* [THIN]
  - 263: *XVIII°,* (line-final; next line starts castigatis, no verse) [OVERRIDE-VERSE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 258:
1. A B in marg. : Consilium bonum. 8. A in marg. : Contra.
Tercia obieccio. 12. B: Non ergo — tollendum cum decst in tcxtu;
cxtat in marg. inf. 23. A in marg. : Responsio. 29. A in marg. :

p. 259:
3. A in marg. : Anselmus. Priyilegia principum sunt prudenter inter-
pretanda (Above i(i5b wiiliout mark of reference). 3. primo scil.
libro. 8. B: ncc debet. 8. B: non debct. 2(5. B: probant.
3. Anselmi Opp. pag. 84 — 85.

p. 260:
8. B: exacta cum. 14. non potest. sc. incidere. 17. 18. talis
blasphcmie in codd. 19. A in marg. : Conclusio. 26. B:
contra Jesu; qui; addc: diabolus. 28. A in marg. : Conclusio.

p. 261:
1. B in marg. : Nabugodonosor est beatus. 3. A in marg. : Corre-
larium. 22. B: observandi. 3o. A in marg.: Nota contra falsam
pietatem ct iniustam misericordiam (Below i65c without mark of re-
ference).
1. Decr. sec. pars, causa XXIII, q. IV, c XXII.

p. 262:
I. In codd.: Est iniusta mirericoidia, cst ct iusta. Denique. Correxi e
dccrct sup. mcmor. 4. 5. In decr. : miscratus est ; rcgis : in codd. 6. ib.
Ita si quis. 7. A A, : latronis coniugis. 10. A At: libcrtat.
11. 12. In codd.: laxat cxicium. Correxi e decr. 14. B in marg.:
Iudcx nulli auferret complcmcntum iusticie motus favore aut pictatc aut
favore (sic). 19. probari in codd. corr. e decr. 26. ib.: facultate.
corr. e dccr. 28. B: prolacionis.

p. 263:
16. AB: deprehensus.
```

---

## Chunk 12-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-12-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-12-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "263.27–267.34"
divisions: "cap. 12 (heading 'CAP. XII.' at 250.17); part 4 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1020 words; 913 unanimous or majority-real; 75 settled by vote (R2 41, R3a 27, R3b 2, R5a 2, R6a 3); 32 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n300–n304 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 12, part 4: [TITLE]

## ¶1 · 263.27–264.32

> [p. 263] quod hoc est contra fidem catholicam ut patet Rom. III° et VII°, ubi docet apostolus quod non sunt faciendo mala culpe, ut bona eveniant, nam cum tales casuum circumstancie sint casuales, patet quod tunc contingeret ut per maiorem partem duracionis date legis iudicaretur secundum ipsam iniustum iudicium, et tunc foret indubie lex iniusta et nunquam permittenda. Quoad terciam difficultatem super qua clamant scolastici, oportet distinguere (sicut facit Apostolus) [p. 264] inter occasionem datam et occasionem acceptam ex lege ad committendum iniuriam: datur autem occasio a lege iniusta ad iniuriam perpetrandum, quando secundum sensum eius cum veris infertur iniuria, ut sensus vendicatur competere dicto privilegio quod omnis fugitivus ad illum locum, sive fuerit dignus sive indignus, habebit ibi omnimodam libertatem; quod declaratum est repugnare divine iusticie. Si autem dicatur quod solum pro dignis vendicatur libertas, tunc vel oportet docere quod fugitivi libertandi sunt digni, vel dicere quod eo ipso quo rex sic concedit, quicunque illuc fugiens erit dignus; dato primo, tunc docto per consilium regis quod datus fugitivus non sit dignus habere refugium, nichil sibi et privilegio libertanti. Si secundum detur, tunc blaspheme extollitur princeps privilegians supra Deum. Deus enim non sic privilegiat locum vel naturam peccabilem, quin ponit in libertate sui arbitrii quod possit reddere se indignum ad percipiendum fructum privilegii concessi. Nec valet deduccio quod tunc iudicium secundum leges humanas foret sepe iniustum cum non attendunt iusticiam quoad Deum: verum concluditur, cum solum lex domini est immaculata convertens animas. Et ita si secundo obicitur quod in Anglia sunt multa privilegia tam iniqua, patet quod improbatio huius privilegii non solvitur sed gravatur, cum multiplicare inconveniens non sit solvere; ymmo manifestior, generalior et contrarior iniusticia verbis, et intencioni privilegii plus dissonaret illi loco et ordini quam alibi in Anglia in manu secularium, ubi communiter non tanta iniuria est commissa.

[ENGLISH]

## ¶2 · 264.33–264.34

> [p. 264] Quarto principaliter obiciunt tam scolastici quam vulgares: Multi, inquiunt, sancti reges, episcopi, clerici

[ENGLISH]

## ¶3 · 265.1–265.8

> [p. 265] vulgares approbarunt hoc privilegium, quando regnum processit prospere; qua ergo fronte nos minus sancti, minus scioli vel potentes usurpare audemus violacionem sancte matris ecclesie, cum domini et partes quibus iniuriatum est possunt (quantum in eis est) remittere satisfaccionem et penam recommendando Deo vindictam? Sic enim alique civitates in Anglia sunt servis in perpetuum refugium.

[ENGLISH]

## ¶4 · 265.9–266.31

> [p. 265] Hic dicitur quod falsum assumitur ad mentem obiectus, nam nec potest esse sanctitas neque prudencia defendere hoc privilegium ad nudum sensum expositum, unde quicunque hunc sensum approbaverant vel fructuose penituerant vel aliter sunt dampnati; nec docetur qui sancti vel approbati viri approbaverant istum sensum. Sed sinistre extortum est ut privilegium ultra fines iusticie contra iuramentum regis et prosperitatem regni, ideo tam excessivo abusui necesse est apponi novum remedium. Et hec racio quare regnum non potens ulterius tollerare crementum iniune apposuit nunc remedium pocius quam perante. Nam semistultus percipit et impugnat manifestam iniuriam, postquam sciolus insensibilem iniuriam pretermittit. Nec est verbum nisi stultorum dicere quod basilica ut lignum et lapides sit sancta mater ecclesia. Nam spiritus quos Deus vocat ad coronam desponsans in via, sunt sancta mater ecclesia; cuius domus est talis basilica cui in nomine sponsi et sponse est reverencia ymaginis tribuenda; quod fit potissime observata pro illo loco iusticia. Nam sanctitas vite et observacio iusticie plus honoraret locum ecclesie, quam totum aurum vel omnia iocalia corporalia huius mundi, sicut minimum peccatum plus ipsum inficeret in oculis sponsi, [p. 266] quam omnes turpitudines vel polluciones corporales possibiles. Nam Deus cuilibet creature quantumlibet turpi illabitur, ipsam causans, quem amorem non potest habere ad peccatum, unde (quantum ego concipio) domini temporales insteterunt prudenter pro loci reverencia et honore ecclesie. Nam sentencia domini mei, domini ducis, fuit quod conservaretur in eis quodcunque privilegium quod in honestatem loci sonuerit, quod utilitatem monachorum intulerit, quod ad veram misericordiam et pietatem fugitivis pertinuerit, quod honor regis ac iuramentum suum de conservando cuicunque legio suo iusticiam permiserit, in tantum quod audivimus eum dicere quod tollerabile foret ut profugi haberentibi refugium in causa alicuius speciei criminis lese regie maiestatis. Defloracio, inquit, filie regis est una species criminis lese regie maiestatis, sed longe hoc a prodicione regni, a defensione iniurie Dei et proximi, et eciam a dampnacione anime incolentis locum illum ex defensione sceleris fugitivi. Ipse autem animose stetit singulariter pro istis iusticiis in tantum quod docuit ubi, per quam et quando oblate sunt sibi mille libre ad procurandum vel promittendum dictos fugitivos cum suo captivo ad terras inimicorum accedere, quod quia visum fuit sibi et regis consilio ipsis confederatis cum hostibus ad periculum regni vergere, noluit assentire. Unde omnino est irreligiositatis condicio invidorum auribus prurientibus de homine ficta scandalosa mendacia et graviter ferre de eo commenta laudabilia que per multos centenarios hominum sunt audita.

[ENGLISH]

## ¶5 · 266.32–267.34

> [p. 266] Pars autem adversa visa est nobis omnino stare pro contrario; cum enim domum Dei decet sanctitudo tempore synagoge, quanto magis tempore legis gracie [p. 267] Christo eiciente vendentes et ementes de templo et dicente Matthei XXI°, 13: Domus mea domus oracionis vocabitur, vos autemfecistis illam speluncam latronum Qualis ergo religio est intra ecclesiam defendere sceleratos, eciam licet evidencia probabili fuerint indurati? Aut qualis utilitas est monacho parare domum conductivam eciam induratis latronibus fugitivis, quamvis in fine vite eorum abbathia habuerit omnia latrocinia que apportant? Aut qualis religio est tercio tueri sceleratos sub pallio false pietatis ad dampnacionem anime eorum et infeccionem ecclesie Anglicane, ubi extra illam speluncam positi parendo iuri communi forent verisimiliter salubriter castigati? Vel quomodo staret quarto cum iuramento regis in recipiendo regni gubernacula, quod stat ut patet ex iuramento regis observacione iusticie cuicunque, ut veneno privilegii foveat eciam membra diaboli ad intoxicacionem et iniuriam regni sui? Nonne Ecclesiastici X°, 8, scribitur: Regnum de gente in gentem transfertur propter iniusticias atque iniurias? Sicut enim nichil plus facit ad stabilimentum regni quam observare cuicunque iusticiam et per punicionem prevaricatorum severam, sic nichil plus minatur ruinam regno quam constanter fovere iniurias. Et si obicitur quod iuxta istam sentenciam rex puniret homicidia inibi perpetrata, lateor, sed rectus ordo exigit, ut gravior iniusticia cicius corrigatur: modo vero ex inhabitacione sceleratorum in sanctuario, ex occisione religiosi intra ecclesiam, ex fraccione capitis religiosi eciam graduati intra ecclesiam per unum de suis confratribus, cum similibus que sonant cum habitantibus ecclesiam maioris peccati gravedinem, plus polluunt locum quam effusio sanguinis vel seminis in qua non tanta gravedo criminis est fundata.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 264.1: We must distinguish between occasion given and occasion taken.
- 264.24: The existence of other false privileges cannot protect this one.
- 264.33: 4. Objection: The privilege
- 265.1: has been approved by great authorities.
- 265.9: Answer: It is not certain that it was approved in the sense now put upon it;
- 265.19: and the need of remedy is not felt till mischief arises.
- 265.24: It is foolish to confuse a material building with holy Church.
- 266.7: The Duke's wish was to preserve every reasonable privilege.
- 266.16: He would have tolerated even insult to the king, but not danger to the kingdom.
- 266.27: It is a sign of irreligion to love scandal.
- 267.4: What religion is there in defending scoundrels, or in keeping a hired house for thieves,
- 267.9: or in saying scoundrels from the punishment that might amend them,
- 267.14: or can the king give unjust privileges?
- 267.25: If the king had to punish within the monastery there would be the Jess crime there.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 263: *catholicam* (box is inside catholicam; one printed word) [R4]
  - 263: *III°* [R4]
  - 264: *inter* [R3]
  - 264: *∅* (inserted run is the end of p.263; print line begins inter occasionem, nothing between) [INS?]
  - 264: *a* (print: occasio a lege iniusta; main lacks a) [INS?]
  - 264: *iniuriam* [R4]
  - 264: *tunc* (bold argument numeral 1 glued) [R4]
  - 264: *iniqua* [NW]
  - 264: *privilegii* [R3]
  - 265: *reg-* (print reg-/num; main holds num separately at pos 6; 'has' is English side-note) [R4]
  - 265: *iocalia* [NW]
  - 266: *conservaretur* [THIN]
  - 266: *in* (main split in into i + n) [THIN]
  - 266: *∅* (n is the tail of in (pos 46); no separate word) [THIN]
  - 266: *dicere* [THIN]
  - 266: *quod tollerabile foret* (main's one token covers three printed words) [THIN]
  - 266: *regni* [NW]
  - 267: *Christo* (L alinea + 166ᵇ folio mark in margin) [R3]
  - 267: *mea domus* (main's one token covers two printed words) [R4]
  - 267: *que* (bold argument numeral 3 in margin) [R4]
  - 267: *staret* (bold argument numeral 4 glued) [R4]
  - 267: *observacione* (166ᶜ folio mark in margin) [R3]
  - 267: *inibi* [NW]
  - 267: *sanctuario* [R3]
  - 267: *fundata* [R3]
  - 266: *omnes* [THIN]
  - 263: *∅* (duplicate: quod already at 184) [DELX]
  - 263: *∅* (duplicate: catholicam already at 189) [DELX]
  - 265: *∅* (second half of reg-num; JOIN onto 5 reg- -> regnum) [DELX]
  - 267: *∅* ('atos' already inside neighbour 64 sceleratos) [DELX]
  - 265: *regnum* (print: reg-/num (agent 13); scan split, side-note "has" glued) [OVERRIDE]
  - 265: *∅* (joined at 5) [OVERRIDE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 263:
16. AB: deprehensus.

p. 264:
i. A A, : et accionem. 6. A A,: sive fuerit dignus sive fuerit.
i3. A A, : Dato premio. 25. 26. A: pravilegia . . . pravilegii. 33. A
in marg. : Contra Quarta obieccio.

p. 265:
9. A in marg. : Rcsponsio. 29. B: et lit. 3o. AA, : sanc-
titas vita. A in marg. : Conclusio. Contra prctensam immunitatem eccle-
siarum (Above 160'' without mark of reference).

p. 266:
2. A in marg. : Nota. 3. B: quam amorcm. 16. 17. A A,:
Detioracio — maiestatis deest.

p. 267:
2. A in marg. : Nota. 6. 7. A A,: conducticiam. 16. A:
pravilegii. 25. A in marg. : Obieccio. 29. B:intra — maioris
```
