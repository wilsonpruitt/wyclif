# Translation brief: ecclesia 14-h–15-b

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-14-h.md chunks/ecclesia/wyc-ecclesia-15-a.md chunks/ecclesia/wyc-ecclesia-15-b.md` once and fix what it reports.
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

## Glossary (the 144 rows these chunks use; the full file is GLOSSARY.md)

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
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| regalia | regality | The king's royal right. Ruled 2026-10-02 (*Eccl.* 148.3, 151.12, 152.12). |
| forisfacere | commit forfeiture | Ruled 2026-10-02 (152.13). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| expropriacio | renunciation of property | Never "expropriation" (seizure). Ruled 2026-10-02 (*Eccl.* 9). |
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
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| ditare | to enrich | Kept apart from *dotare*, endow. Ruled 2026-09-28 (coordinator, delegated) (21 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| citare; citacio | to cite; citation | Summons to a church court. Ruled 2026-09-28 (coordinator, delegated) (12 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| possessionati | the possessioners | Endowed religious. |
| vulgares | the common people | The third estate. Not "the vulgar". Pilot. |
| protestacio; protestari | declaration; to declare solemnly | ⭐ The submission formula ("if anyone can teach me this is contrary to scripture or reason, I will humbly retract"). Penn and Lahey both inverted it (T. pp. 369, 378). Render it as a retraction offer, never as defiance. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| curia romana | the Roman curia | Ruled 2026-09-28 (*Dial.* 7.8; 5 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| locus a maiori | the topic from the greater | The dialectical topic; for *a simili* see "the topic from likeness" (2026-09-28 row). Ruled 2026-10-02 (*Eccl.* 144.27). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| franchisia | franchise | Ruled 2026-10-02 (*Eccl.* 239.22). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Ruled 2026-10-02 (*Eccl.* 13). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| practizare | to put into practice | Ruled 2026-09-28 (coordinator, delegated) (4 sites). With *contra* + person, "practise against" (plot), *Dial.* ch. 17. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
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
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| irreligiositas | irreligion | Ruled 2026-10-02. |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| ditarius | almsman | The one enriched by the alms (cf. *ditare*, §B). Ruled 2026-10-02 (*Eccl.* 13). |
| pseudomonachus | false monk | Kept apart from *pseudofrater* if it appears. Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "one given alms". Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |

---

## Chunk 14-h: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-14-h.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-14-h
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "326.32–328.25"
divisions: "cap. 14 (heading 'CAP. XIV.' at 299.9); part 8 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "428 words; 366 unanimous or majority-real; 52 settled by vote (R2 34, R3a 11, R5a 7); 10 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n363–n365 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 14, part 8: [TITLE]

## ¶1 · 326.32–328.6

> [p. 326] Item, quilibet simplex sacerdos habet parem potestatem ordinis cum papa, et ad illam potestatem ordinis consequitur essencialiter proporcionalis potestas secularis dominii; [p. 327] ergo quilibet simplex sacerdos habet titulum de iure ad dominandum seculariter toti mundo. Sed dic buphotracti maledicti tot dominati; tunc enim nec foret ordo nec civilis dominacio, nec oporteret sacerdotes acquirere sibi titulos in suscipiendo ordines, cum illo titulo ordinum excellunt seculariter quemlibet regem mundi. Item, parem potestatem dominandi seculariter habet quilibet presbiter regni nostri, sicut haberet supposito quod ipse solus foret sacerdos in Anglia et rex noster conquireret quotquot regna, sed tunc foret secularis dominus capitaliter omnium bonorum regni nostri. Ergo et modo de iure. Aliter enim sequeretur quod civilis dominacio pape dependeret ab integritate dominacionis imperii, et per consequens, papa nitendo destruere imperium, destrueret proprium civile dominium, vel si ipse debet dominari seculariter super omnes naciones iam infideles, per idem quilibet sacerdos habet ius ad taliter dominandum. Item, tunc superflueret carta cesaris tamquam impossibilis et heretica, non ergo incorporanda foret in canone tamquam paris auctoritatis cum dictis sanctorum doctorum, ut patet XCVIª d. Constantinus; ibi enim dicitur quod Constantinus quarto die sui baptismi contulit privilegium Romano pontifici et ordinavit ut, sicut ipse imperat aliis regibus, sic eius episcopus aliis sacerdotibus, unde iudicat et discernit quod episcopus Romanus habeat potestatem utendi insigniis regalibus, unde et sanccivit, dixit et consuluit quod ditavit ac sua largitate concessit et ex imperiali potestate statuit et confirmavit ut usque in finem mundi dona [p. 328] sua et privilegia maneant illibata. Et multa alia verba ibi inseruit que iuxta succedentem superbiam sonarent in heresim, quia innuerent papam esse elemosinarium cesaris, et per consequens ipsum posse revocare donatum condicione dirupta, cum dicit se ordinare ut per manus beati Silvestri et successorum eius omnia disponantur.

[ENGLISH]

## ¶2 · 328.7–328.25

> [p. 328] Et credo, si ista carta relicta fuerit, non invenirenty cartam aliam in scriptura. In tales infinitas vesanias antichristinas inducitur populus in ecclesia propter reliccionem evangelii, propter oblivionem paupertatis Christi et candentem cupiditatem ad fastum seculi. Vidit enim quod, si beatus Silvester recepit secundum dictam formam dominium illud a cesare, tunc cesar habens integrum imperium, tam large benedicens pape foret quoad seculum ipso maior, cum partem sue magnificencie impertitus fuisset elemosinario suo pape. Ideo querunt mendaciter alias minas hereticas et blasphemas, dicentes quod Christus, Petrus et alii dominati sunt civiliter toti mundo, et illo iure, non iure cesaris gaudent suo dominio. Idem est expresse contra Augustinum super Joh., Omelia VIª, et contra decretum distinccione VIIIª, Quo iure, et contra beatum Bernardum, libro II ad papam Eugenium: Esto, inquit, ut alia racione tibi vindices dominatum sed non iure apostolico, quod probat efficaciter ex scriptura.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 326.32: or simple priest;
- 327.7: who indeed on the theory would be chief lord of all our goods.
- 327.19: Moreover on the same theory the donation of Constantine was impossible and heretical.
- 328.7: And if that were put aside nothing to the same effect would be found in scripture.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 327: *ergo* (print p.327 l.1 '174d ris dominii; ergo') [R3]
  - 327: *destruere* (15 is the line number) [R4]
  - 327: *XCVIª* [R3]
  - 328: *et* [R4]
  - 328: *∅* (print p.328 begins 'sua et privilegia'; the inserted run is the end of p.327) [INS?]
  - 328: *VIª* [R3]
  - 328: *VIIIª* [R4]
  - 326: *essencialiter* [THIN]
  - 326: *secularis dominii* (secula- here, 174d ris dominii at top of p.327; main token covers both words) [THIN]
  - 328: *maneant* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 326:
12. A in marg.: Triplcx obiectus. 16. B: biillas suas quidcunque.
22. A in marg. : Responsio. 27. A in marg. : Conlra dominacionem
civilem cleri (Below 174« without mark ot reference).

p. 327:
2. A A,: Scd dum; hic aliqua verba cxcidissc vidciitur. Quid sibi vult
hoc vcrbum buphotracli? Verisimilitcr legendum : Dic bufo crati: male-
dicti tot domiiiati (Matthew). 12. A: modo dematrc; A, dc matre cor-
rexitin: dominatur. 24. B : contulcrit. 27. B in marg.: Hic probat
quod papa habet aactoritatem dominandi civilitcr a ccsare sed non a Deo.
23. Hic memorata c decretali Constantinus mutatis tamen
aliquot verbis deprompta sunt.

p. 328:
12. B: Vidcnt. 14. B: intcgrum jominium. 24. In codd. :
vcndiccns. Correxi e textu s. Bernhardi. 2?. A: scriptura. Sequuntur
verba: ti racz .• Id cst: Domine velis adiuvare
Hospodyne pomoc psati.
scribcntcm. A,: cap. XVI in textu. 27. A in marg. : Alateria de
ablacionc temporalium clcri (Abovc 1 75™ without mark of refcrencc).
2;. Decr. I pars, dist. VIII, c. I. 23. Bernhardi, De Con-
sideracione lib. sec. (Opp. pag. 102 1).
```

---

## Chunk 15-a: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-15-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-15-a
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "328.27–332.19"
divisions: "cap. 15 (heading 'CAP. XV.' at 328.26); part 1 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "886 words; 785 unanimous or majority-real; 64 settled by vote (R2 41, R3a 18, R3b 2, R5a 2, R6a 1); 37 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n365–n369 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 15, part 1: [TITLE]

## ¶1 · 328.27–330.12

> [p. 328] Secundum dubium est, si rex Anglie a clero suo legio potest legitime auferre temporalia donata ecclesie [p. 329] pro cleri sui abusu elemosine vel contemptu. Et est dubium istud necessariissimum ad tractandum, quia multis et magnis de regno nostro videtur quod pars affirmativa conclusionis sit satis catholica, aliis autem pinguioribus regis elemosinariis videtur quod conclusio sit omnino heretica. Et indubitanter assero quod, si conclusio ista sit heretica, supposito facto regali regum Anglie, vel totum regnum vel maior pars eius est exhinc infectum heretica pravitate: et cum sacerdotes et specialiter episcopi et scolastici regni nostri tenentur predicere regi et regno suo periculum, patet quod ipsi specialiter et regnum communiter tenentur in isto puncto cognoscere veritatem. Non enim sunt rex et regnum adeo indurati quin, docto quod dogma illud foret hereticum, ipsum non amplius practizarent, sed ad vocem multitudinis cleri sui concito revocarent. Sic enim ad predicacionem Jone Ninivite salubriter penitebant (ut patet Jone III° et Matthei XII°), sic eciam Nabugodonozor conversus est ab infidelitate et salvatus finaliter virtute Dei et prudencia Danielis (ut patet in canone XXIII, q. IV. Nabuchodonosor ex historia prophete et testimonio Augustini); et revera videtur maior disposicio in regno nostro et eius principibus quam fuit in predicto populo infideli. Quomodo ergo foret fidelis vel caritative diligens regem suum qui videret ipsum ex ignorancia super oram baratri paratum ad precipicium sempiternum et assistente revocandi noticia in sepe conversionis ex negligenti desidia permitteret tam gravem populum in corpore et anima perpetuo interire, specialiter si ad speculandum et prenarrandum regis et regni pericula sit pinguiter premiatus? Nonne dicit Deus prophete [p. 330] Ezechielis XXXIII°, 7, 8: Et tu fili hominis speculatorem dedi te domui Israel, audiens ergo ex ore meo sermonem annunciabis eis ex me. Si me dicente ad impium: Impie, morte morieris, non fueris locutus, ut custodiat se impius a via sua, ipse impius in iniquitate sua morietur, sanguinem autem eius de manu tua requiram. Et multo magis in tempore legis gracie, quando debemus ex lege Christi habere ampliorem noticiam et amorem et insuper habemus a rege temporalem retribucionem amplius quam habuit Ezechiel vel quam propheta alius veteris testamenti. Dampnabilis ergo foret nostra segnicies.

[ENGLISH]

## ¶2 · 330.13–330.30

> [p. 330] Nec valet ista triplex infamis instancia, prima qual dicitur quod rex et regnum forent exhinc exasperati ad auferendum temporalia que habemus. Ista enim accusans obieccio indicat quod plus diligimus nostra temporalia quam datorem, cum irreligiose plus timemus amissionem nostrorum temporalium quam amissionem perpetuam corporis et anime regis nostri. Secunda instancia dicit quod ista materia ventilata est et decisa in Romana curia coram papa. Revera non credo sed, supposito quod sic, illi quibus illud est cognitum sunt accusabiles tamquam proditores qui sic celant istud periculum. Nam infinitum plus est periculi quam si quotlibet corporales hostes ex scitu celantis invaderent et destruerent funditus regnum nostrum, et insuper cum tales dampnantes istam materiam sunt mortui vel divisi, stultum foret expectare publicacionem decisionis eorum in tanto periculo. Tercia instancia dicit quod tam rex quam regnum

[ENGLISH]

## ¶3 · 330.31–331.16

> [p. 330] processit prospere, quando clerus noster a tractatu talis materie supersedit. Ista ficticia destructa [p. 331] est superius XII. cap.; et in proposito inficit se ipsam. Quomodo, inquam, regno nostro inesset prosperitas, quando a rege et capitalibus eius tam prelatis quam dominis defenderetur tanta iniquitas. Error enim cui non resistitur approbatur; sed altera istarum est nedum error sed heresis pro qua dignum esset ut rex et totum suum sacerdocium destruatur. Ideo non dubium rex et domini seculares sed specialiter prelati regni facerent in isto diligenter inquirere veritatem et excitarent defenderentque theologos hoc tractantes, cum eis incumbit errores tales discutere et de periculo regem et regni incolas premunire. Et revera ex utraque parte contradiccionis sequitur grande periculum, eo quod, sive sit hereticum sive non sit hereticum, supposito facto magna pars regni nostri ex adhesione, ex defensione vel omissione inficitur heretica pravitate.

[ENGLISH]

## ¶4 · 331.17–332.19

> [p. 331] Intendo ergo isto modo procedere: primo narrare factum regum Anglie m hac parte, secundo recitare opiniones doctorum in materia, et tercio obicere contra illas. Quantum ad primum, patet legenti cronicas regni nostri quomodo Willelmus conquestor multas elemosinas regum Saxonum de abbatiis, de episcopatibus et aliis dotacionibus sub nomine perpetue elemosine pro perpetuo variavit, nunc subtrahendo, nunc transferendo et nunc loco cleri prioris extraneos inducendo. Nec valet fingere sompnia quod vel a papa habuit licenciam plus ad ista quam ad conquestum regni de iure sibi debiti. Et sic de sompnio quo fingitur ipsum post restituere omnes ablatarios clericos, sicut nec restituit heredes Saxonum rebellantes; et revera hereticare ipsum finaliter, cum totum ius regni fuit ab ipso ad omnes reges medios successione hereditaria usque hodie derivatum, foret minis infectiva presumpcio. Infectiva dico, quia hereticaret reges clerum et populum interim succedentes; [p. 332] sed dimissis destruccionibus Templariorum et ablacionibus privatis que interim contigerunt, recolamus de ablacionibus talibus que diebus nostris per illustrem regem Edwardum tercium erant facte. Nam temporalia domini Willelmi Bathman Norwycensis capta sunt in manus regis et tenta duodecim annis continuis pro contemptu. Et idem contigit de domino Johanne Gransoni Exoniensi, de fratre Thoma de Lyle, episcopo Heliensi, et sic de multis ablacionibus quas diebus nostris cognovimus. Ymmo Ricardus rex noster sicut avus suus practizat hoc annuatim in religiosis possessionatis de Francia; nec super isto consulunt curiam Romanam, quia ut constanter defendunt ista potestas directe pertinet ad coronam. Nec recolo quod temporalia mobilia ablata restituunt, cum contemptus vel forisfactura elemosinariorum regis requirit ut gravius puniantur, nisi quod rex misericorditer eos respicit, sicut in possessionem elemosinarum regni sui eos misericorditer introduxit.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 328.27: A second doubt is whether the king may withdraw Church temporalties on account of abuse, or when the clergy are in contempt.
- 329.9: Many think he may, and that the clergy should tell the king so.
- 330.13: Three futile reasons for not warning:
- 330.15: 1. The king would take away our temporalties.
- 330.20: 2. The matter has been decided in the Papal Court.
- 330.30: 3. The realm goes on well while the clergy is silent.
- 331.7: Such a serious, question ought to be settled.
- 331.17: History of the question. William I. rearranged many foundations or transferred them.
- 331.33: Suppression of the Templars.
- 332.3: Recent examples of temporalties seized.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 328: *CAP. XV.* [HEAD]
  - 329: *III°* (print 'Jone III° / et Matthei'; main lacks III° after Jone) [INS?]
  - 330: *non* [THIN]
  - 330: *fueris* [THIN]
  - 330: *locutus* (whole word printed at line start; main dropped lo) [THIN]
  - 330: *in* [R3]
  - 330: *regnum* (print: regnum processit; regnum opens the line) [INS?]
  - 331: *primum* [NW]
  - 331: *hereticare* [NW]
  - 331: *hereticaret* [NW]
  - 332: *Willelmi* (letterspaced name; main split into letters) [THIN]
  - 332: *∅* (i is part of Willelmi (pos 27)) [THIN]
  - 332: *∅* (ll is part of Willelmi (pos 27)) [THIN]
  - 332: *∅* (e is part of Willelmi (pos 27)) [THIN]
  - 332: *∅* (l is part of Willelmi (pos 27)) [THIN]
  - 332: *∅* (m is part of Willelmi (pos 27)) [THIN]
  - 332: *∅* (i is part of Willelmi (pos 27)) [THIN]
  - 332: *Bathman* (letterspaced name; main split into letters) [THIN]
  - 332: *∅* (a is part of Bathman (pos 34)) [THIN]
  - 332: *∅* (t is part of Bathman (pos 34)) [THIN]
  - 332: *∅* (h is part of Bathman (pos 34)) [THIN]
  - 332: *∅* (m is part of Bathman (pos 34)) [THIN]
  - 332: *∅* (a is part of Bathman (pos 34)) [THIN]
  - 332: *∅* (n is part of Bathman (pos 34)) [THIN]
  - 332: *Norwycensis* (letterspaced name; main split into letters) [THIN]
  - 332: *∅* (o is part of Norwycensis (pos 41)) [THIN]
  - 332: *∅* (r is part of Norwycensis (pos 41)) [THIN]
  - 332: *∅* (w is part of Norwycensis (pos 41)) [THIN]
  - 332: *∅* (y is part of Norwycensis (pos 41)) [THIN]
  - 332: *∅* (c is part of Norwycensis (pos 41)) [THIN]
  - 332: *∅* (e is part of Norwycensis (pos 41)) [THIN]
  - 332: *∅* (n is part of Norwycensis (pos 41)) [THIN]
  - 332: *∅* (s is part of Norwycensis (pos 41)) [THIN]
  - 332: *∅* (i is part of Norwycensis (pos 41)) [THIN]
  - 332: *∅* (s is part of Norwycensis (pos 41)) [THIN]
  - 331: *est* (175b folio mark glued) [THIN]
  - 331: *interim* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 328:
12. B: Vidcnt. 14. B: intcgrum jominium. 24. In codd. :
vcndiccns. Correxi e textu s. Bernhardi. 2?. A: scriptura. Sequuntur
verba: ti racz .• Id cst: Domine velis adiuvare
Hospodyne pomoc psati.
scribcntcm. A,: cap. XVI in textu. 27. A in marg. : Alateria de
ablacionc temporalium clcri (Abovc 1 75™ without mark of refcrencc).
2;. Decr. I pars, dist. VIII, c. I. 23. Bernhardi, De Con-
sideracione lib. sec. (Opp. pag. 102 1).

p. 329:
5. 13: rcgis — vidctur dcest. 17. I! : concicio revocarcnt. 22. A in
marg.: Nabuchodonosor salvatus cst. 27. 15: ad precipucium.
28. A A^: in sepe conversionis. 3o. B: intcrirc deest.
21. Decr. II pars, causa XXIII, q. IV, c. XXII.

p. 330:
1. A in marg. : Mate (verbum Bohemicum) id cst: habctis (sivc habete).
4. A A, : Impie dcest. 12. A A, : signicies. B: singulcics. i3. A in
marg. : Triplcx instancia. 20. B: vcntulata.
32. Vide stipra pag. 265.

p. 331:
ii. Codd.: iu crrorcs. 17. A in marg. : Nota tria. 20. A in
marg.: Nota quomodo practisata cst ablacio temporalium. 32. B:
succcssivc. 34. B: internum succedentes.

p. 332:
1. A B: templaziorum. 2. B: privatis deest. 8. A A,: Oxo-
niensis. B: Exoniensis. 9. A: Hyle. 11. B: hoc amicatuum in.
20. A in marg. : Tres conclusiones.
5. Willelmus Bateman: Walsingham. Hist. Angl. I, p. 262.
He was bishop not quite 11 years (1844— 1 3 5 5) and during that
time he was frequently employed in embassjes abroad and must
have been in the favour of the King. It is possible however
that Wyclif does not refer to a deprivation of all his temporali-
ties, but to some one estate of which he was deprived by the
King's courts in the course of a lawsuit (Matthew). 8. Jo-
hannes Graunson ap. Walsingham 1. c. pag. 3og. Cf. Rolls of
Parliament II, 245". 8. 9. Thomas de Lyle see Walsingham
l, 285. 10. Cf. Rolls of Parliament III, 22b.
```

---

## Chunk 15-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-15-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-15-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "332.20–336.16"
divisions: "cap. 15 (heading 'CAP. XV.' at 328.26); part 2 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "839 words; 755 unanimous or majority-real; 75 settled by vote (R2 49, R3a 18, R3b 5, R5a 2, R6a 1); 9 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n369–n373 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 15, part 2: [TITLE]

## ¶1 · 332.20–334.3

> [p. 332] In ista materia est quidam doctor qui sui gracia misit mihi in scriptis tres conclusiones huic materie pertinentes. Prima, describendo heresim, dicit quodl posicio sive assercio heretica est error periculosus, pertinaciter defensatus, directe repugnans catholice veritati. Secunda, non est possibile reges Anglie [p. 333] legitime posse auferre simpliciter temporalia cleri sui. Tercia. Tercia, ii domini reges temporalia a clero suo nunquam legitime abstulerunt, sicut nec ceteris paribus poterunt m futurum. In ista materia suppono quod loquatur de clero communiter, ut includit quemcunque habentem caracterem sacerdotalis ordinis. Si autem loquatur laxius, tantum placet. Ex quo patet quod omnes sacerdotes conversantes in Anglia sub proteccione regis, sive seculares sive religiosi, possessionati vel exproprietarii, sunt clerus legius regis Anglie, sic enim loquuntur multa decreta, nunc de clerico re et nomine, nunc autem de clerico nudo nomine, ut XLª d. sub auctoritate Chrisostomi dicit Canon: Multi sunt sacerdotes et pauci sunt sacerdotes, multi in nomine, pauci in opere, quia non locus vel cathedra facit sanctum sacerdotem sed econtra. Abiecta itaque ista signacione difficile foret scire quis esset clericus vel sacerdos. Secundo suppono quod clericus tam in Anglia quam alibi posset quantumcunque enormiter peccare quocunque genere peccatorum; patet de episcopo Scarioth, de religioso Sergio et multis aliis sacerdotibus, de quibus scriptura sacra et cronice faciunt mencionem, ymmo cotidiana experiencia idem docet. Non enim habet clericus (in quantum huiusmodi) titulum sue confirmacionis a domino, sed ex testimonio sanctorum doctorum habemus quod racione dignitatis ordinis et dyabolice temptacionis plus aspere peccant communiter gravius quam vulgares, sicut oculata fide conspicimus [p. 334] de pseudopapa et suis pseudocardinalibus qui ex cupidine fastus et questus, non autem ex cupidine meritorii profectus conturbant sanctam matrem ecclesiam.

[ENGLISH]

## ¶2 · 334.4–334.11

> [p. 334] Tercio suppono facta regum Anglie superius memorata et perseveranciam regis et regni ad defendendum hanc potestatem tamquam legitimam et regis Anglie precipuam regaliam. Ex quo sequitur quod ipsi supponunt hoc regis privilegium non esse catholice veritati dissonum sed consonum, cum (ut dicunt) sit fundabile in scriptura in qua omnis veritas et non nisi veritas catholica est contenta.

[ENGLISH]

## ¶3 · 334.12–335.22

> [p. 334] Ex istis sic arguo: Reges Anglie sepe abstulerunt temporalia simpliciter a clero suo, ut patet ex supposicione tercia, et nec unquam abstulerunt sic legitime, nec potuerunt legitime sic auferre, ut patet ex secunda conclusione et tercia doctoris. Ergo in hoc fecerunt qualiter non potuerunt legitime facere. Ex quo sequitur ultra quod in hoc fecerunt qualiter non potuerunt meritorie vel de lege Dei facere, et cum omne opus humanum ex deliberacione sua precedens sit legitimum vel illegitimum, meritorium vel demeritorium, sequitur quod illegitime et demeritorie sic fecerunt, et ultra sequitur quod inciderunt ut sic in errorem periculosum, quia tam corporis quam anime dampnabiliter perditivum. Et supposito errore isto in facto, patet quod est pertinaciter defensatus, quia rex et regnum constanter defendunt hanc potestatem tamquam legitimam eciam usque ad mortem cum gladio si oportet. Et quod error iste sit directe contrarius catholice veritati, patet tripliciter ex datis. Primo, quia rex sic faciendo fecit quod non licuit nec licere potuit, ut sequitur ex datis. Secundo, quia iniuste [p. 335] abstulit aliena contra mandata secunde tabule, et tercio, quia fecit ista non in caritate contra veritatem catholicam Apostoli, I°, Cor. XVI°, 14: Omnia vestra in caritate fiant. Totum antecedens est ab adversario concedendum. Ex quibus ultra colligitur quod reges Anglie in sic faciendo sunt heretici, et cum illud usque ad mortem defenderant, sequitur quod decesserunt heretici et dampnati; et revera religiosus possessionatus qui credit hec omnia vel remisse vel nullo modo oraret pro dictis regibus iam defunctis et cum ex titulo sic orandi tenet a rege suas elemosinas temporales. Nec valet dicere quod nunquam simpliciter abstulit rex temporalia clericorum, quia certum est quod abstulit ab eis tam mobilia quam immobilia sine hoc quod unquam eis restituit et talem ablacionem vocant scriptura et communitas ablacionem simpliciter, vel si vocetur ablacio solum secundum quid, quia solum a parte ecclesie, non contendo sed scripturam et mundum in testes invoco quod tanta confiscacio qualis memoratur facta per reges Anglie fuit notabilis ablacio temporalium.

[ENGLISH]

## ¶4 · 335.23–335.31

> [p. 335] Nec valet sompniare quod post ablacionem perceperunt fructum eorum ex titulo caritatis, qua omnia sunt lustis communia, quia multi amaro animo et cum murmure ferunt ablacionem huiusmodi, nec sunt in capitulo cum illis quibus ait Apostolus quod rapinam bonorum suorum cum gaudio susceperunt, ymmo quomodocunque dicatur, sequitur contra secundam conclusionem doctoris quod reges Anglie possunt in casu auferre simpliciter temporalia cleri sui.

[ENGLISH]

## ¶5 · 336.1–336.16

> [p. 336] Nec valet dicere quod merendo talem ablacionem homo desinit esse clerus, tum quia hoc est contra primam supposicionem, cum caracter ordinis sit indelebilis, tum quia sic pauci vel nulli clerici possessionati docerent legitime quod gauderent privileg vel possessione ex titulo clericatus, quod nimis preiudicaret ordini nostro. Nec est mihi verisimile quod doctor stabit in isto, cum conclusio sua tercia dicit quod nulli reges Anglie temporalia a clero suo unquam legitime abstulerunt, et cum aliquis ex dubio fuit pro aliquo tempore fidelis clericus regis et tamen postea decidens a clericatu meritorio et fidelitate regis meruit post ut per regem sua temporalia auferantur. Sic enim fuit de Scarioth quoad Christum et sic notum est quosdam clericos alienigenas promotos in Anglia coniunctos cum hostibus post regem Anglie defidasse.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 332.20: Three conclusions laid down by a doctor: 1. a definition of heresy;
- 332.25: 2. denial of the King's right to deprive
- 333.1: of temporalties;
- 333.2: 3. denial of such right both in past and future.
- 333.5: In answer we suppose a) that clergy includes all men in orders;
- 333.19: b) that it is possible for the clergy to sin grossly,
- 334.2: as is evident of the false Pope and his supporters; c) that the English Kings believe they have the right thus denied.
- 334.15: On the doctor's supposition the Kings have acted wrongfully;
- 334.28: end contrary to the Catholic faith;
- 335.5: and are therefore obstinate heretics who ought not to be prayed for.
- 335.13: It is a mere evasion to say that the deprivation was qualified;
- 335.23: or that the clergy still profit by them, since the righteous possess all things;
- 336.1: or that the clergy cease to be such by deserving punishment.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 332: *gracia* (2 and D are margin numeral and alinea letter) [R4]
  - 333: *futurum* [R3]
  - 334: *profectus* (print: torii profectus conturbant) [R3]
  - 334: *∅* (to is the English side-note (contrary to)) [INS?]
  - 335: *abstulit* (175d folio mark and E alinea letter are not text) [R3]
  - 335: *tercio* (3 is the margin argument numeral) [R4]
  - 335: *I°* (capital I with degree sign: I°, Cor.) [R3]
  - 336: *dubio* (print: ex dubio; 10 after it is the line number) [NW]
  - 334: *pseudopapa* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 332:
1. A B: templaziorum. 2. B: privatis deest. 8. A A,: Oxo-
niensis. B: Exoniensis. 9. A: Hyle. 11. B: hoc amicatuum in.
20. A in marg. : Tres conclusiones.
5. Willelmus Bateman: Walsingham. Hist. Angl. I, p. 262.
He was bishop not quite 11 years (1844— 1 3 5 5) and during that
time he was frequently employed in embassjes abroad and must
have been in the favour of the King. It is possible however
that Wyclif does not refer to a deprivation of all his temporali-
ties, but to some one estate of which he was deprived by the
King's courts in the course of a lawsuit (Matthew). 8. Jo-
hannes Graunson ap. Walsingham 1. c. pag. 3og. Cf. Rolls of
Parliament II, 245". 8. 9. Thomas de Lyle see Walsingham
l, 285. 10. Cf. Rolls of Parliament III, 22b.

p. 333:
5. A in marg. : Tres supposiciones. B in marg. : Nota tres supposiciones.
11. 1 5. A m marg.: _ . "> sacerdotes. i5. In canone: multi nomine.
16. ibid: facit sacerdotcm sed sacerdos cathedram. 20. B: enor-
mitcr precare. 22. A, in marg. : Et Johanne papa XXIII. qui pro
heretico et diabolo incarnato est condcmpnatus in Constancia.
i3. Decreti prima pars, dist. XL, c. XII sub auctoritate auctoris
Operis Imperfecti in Matth. hom. 43, cap. 23.

p. 334:
12. A in marg. : Prima racio. 23. B: ut in errorem. 3o. A, :
corrigit: ex dictis.
12. Comp. Joannis Hus. De ablacione bonorum temporalium
a clericis. (Opera ed. Norinbergensis 1 5 58, tom. I, fol. CXXII".)

p. 335:
8. B: erant herelici. i3. A in marg. : Ficcio. 16. B: quod
nuiiqiiani. 16. B: restituit talem. 23. A in marg. : Ficcio.
24. B: contra omnia quia. 26. B: ablacionem — cum gaudio deest.
28. B: cum gladio susceperunt.
27. Hebr. X, 34.

p. 336:
1. A in marg. : Ficcio. 17. A in marg. : Secunda racio. 21. In
codd : simus. 29. A: adiciendo quantumcunque ; volucrint —
honestam deest.
17. Comp. Hus, De ablacione bonorum temporalium I. c. fol.
cxxir.
```
