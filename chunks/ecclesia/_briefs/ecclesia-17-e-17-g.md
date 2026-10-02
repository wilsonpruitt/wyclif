# Translation brief: ecclesia 17-e–17-g

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-17-e.md chunks/ecclesia/wyc-ecclesia-17-f.md chunks/ecclesia/wyc-ecclesia-17-g.md` once and fix what it reports.
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
| presciencia | foreknowledge | |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| expropriacio | renunciation of property | Never "expropriation" (seizure). Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| regnum | kingdom | Every sense: the political state as well as the kingdom of God and scripture's kingdoms. Not "realm". Wilson, Ruled 2026-09-28 (27 sites). |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| vulgares | the common people | The third estate. Not "the vulgar". Pilot. |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| credulitas | credence | With *credere*, believe (*Dial.* 23.17–24.4). Ruled 2026-09-28. |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
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
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| glosare | to gloss | Interpret so as to remove the difficulty (T. p. 366). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| glosa | gloss | The noun beside *glosare*. Ruled 2026-10-02 (52.10). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| zizania | cockle | Douay–Rheims (Matt. 13:25). Ruled 2026-09-28. |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| impresenciarum | nowadays, at present | (T. p. 366) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| denominacio; denominare | naming; to name | The argument turns on it. Ruled 2026-10-02 (*Eccl.* 17, 391.17, 398.2). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |

---

## Chunk 17-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-17-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-17-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "402.25–406.33"
divisions: "cap. 17 (heading 'CAP. XVII.' at 388.1); part 5 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1063 words; 900 unanimous or majority-real; 149 settled by vote (R2 107, R3a 35, R5a 7); 14 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n439–n443 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 17, part 5: [TITLE]

## ¶1 · 402.25–404.26

> [p. 402] Item, iuxta hec dicta sacerdotes, prophete et reges legis veteris erant Christi ut Israel, Aaron, David, et per consequens, Israelite, Aaronite et domus David fuerant christiani, quia discipuli Christi servantes iusticiam, et ita secundum omnem descripcionem quam doctor dat de christiano, sequitur quod ante incarnacionem fuerant christiani. Et in confirmacionem illius sic scribit mihi: Qui, inquit, observant legem Christi omnes dicuntur christiani, prout notat beatus Augustinus, Epistola XLIIª, [p. 403] allegans Apostolum Romanorum XIª dicentem quod non omnes qui ex Israel sunt sunt Israelite; pocius, inquit Augustinus, christiani sunt non qui secundum Ismael filii sunt carnis, sed secundum Isaac filii sunt promissionis ad spirituale ministerium pertinentes. Ex isto processu Augustini bene notato sequitur quod patres veteris testamenti fuerant christiani et membra ecclesie; quod negatur. Omnes, inquit, viventes secundum legem Christi sunt filii Abrahe et veri christiani. Ex qua conclusione patet quod per tempus veteris testamenti fuerant christiani, vel secundo quod modo nulli sunt filii Abrahe, vel quod in sancto triduo beata virgo non fuerat christiana, quia tunc non fuit ita quod ipsa observat legem Christi, cum tunc fuit ita quod non est Christus. Unde finaliter videtur inconsequenter dictum quod fuit ecclesia catholica cuius beata virgo fuit pars pro triduo mortis Christi, primo quia, posito quod loquamur pro illo triduo, ex tibi dubio sola virgo est persona fidelis superstes, et cum ipsa non sit christiana ex tibi dubio, non est multitudo omnium christianorum. Similiter, per totam vitam Christi corpoream ante mortem non fiebat ecclesia (ut dicitur), quia solum pro tempore fluxus sanguinis et aque de suo latere, quod fuit post mortem Christi. Similiter, posito quod loquamur pro dicto triduo et arguamus a diffinicione ad diffinitum: Omnis ecclesia catholica est universalis multitudo omnium christianorum habencium ex integro rectam et eandem fidem, per Christum et suos apostolos promulgatam et postea a sanctis patribus in conciliis generalibus declaratam, sed nunc est ecclesia catholica cuius mater domini est pars, ergo nunc est universalis multitudo omnium christianorum, habencium ex integro rectam et eandem fidem per Christum et suos apostolos [p. 404] promulgatam et postea a sanctis patribus in conciliis generalibus declaratam; consequens falsum pro dicto triduo, ergo antecedens. Sed minor fuit tunc vera ut datur; ergo cum tunc fuit dicta consequencia, ut suppono, relinquitur quod tunc fuit maior falsa, que est descripcio universalis ecclesie, ut fingitur perpetuo permansura. Quod autem consequens fuit tunc falsum. patet quia dato per impossibile quod tunc fuit multitudo omnium christianorum habencium ex integro rectam et eandem fidem per Christum et suos apostolos promulgatam, adhuc non fuit tunc verum quod illa fides sit postea a sanctis patribus in conciliis generalibus declarata. Sequitur enim illa fides a sanctis patribus in conciliis generalibus declarata; ergo nec post nec ante nec unquam est a sanctis patribus in conciliis generalibus declarata; si (inquam) sufficeret quod fides illa erit a sanctis patribus in conciliis generalibus declarata tunc sequitur cum veris quod diu ante mortem Christi fuit ecclesia catholica; quod negatur. Sed male, cum tunc fuit christiana religio, eo quod tunc fuit abbas secundum regulam apostolicam, regens suum capitulum de electis apostolis. Ipsi enim observarunt tunc melius quam nos facimus religionem christianam, et ex nomine talis religionis dicto primo Retractacionum, capitulo XXII°, infertur vere res et nomen ecclesie.

[ENGLISH]

## ¶2 · 404.27–406.11

> [p. 404] In tercio argumento fert doctor graviter quod dixi descripcionis sue particulas congregatas inculte. Fateor, inquit, quod inculte, sed malo inculto sermone et absque dictamine scribere veritates quam sub fuco verborum politorum tradere falsitates. Sed constat quod descripcio data est rethorica et diffusa, [p. 405] nec solum falsitatem implicans sed errorem contrarium fidei christiane; et revera descripcionem sic diffusam et falsam non excusat color rethoricus quin sit a catholicis condempnata; descripcio autem ecclesie catholice est condicionis opposite, dum recte breviter et plane dicitur quod ecclesia catholica est universitas predestinatorum. Sed quoad materiam argumenti dicitur quod ubique assumit falsum incomprobatum, cum aliquam unam fidem qua creditur habent omnes christiani. Unam, inquit, tam genere quam specie sed non numero (ut allegatur de Augustino XIII° De Trinitate VI° et VII°), et eadem est fides que creditur aput omnes. Et placet de ista responsione: exhinc enim feci argumentum ad hominem, quia credidi doctorem posuisse ut olim quod non fuisset species vel aliquod universale nisi terminus vel conceptus; non quia credidi hoc esse verum, cum scio ex fide scripture quod una est fides que creditur, et fides qua creditur in quolibet christiano; aliter enim impertinenter diceret Apostolus Ephes. IV°, 5. Unus dominus, una fides. Et illud expresse dicit Augustinus XIII° DeTrinitate, II° cap° X. Fides (inquam), scilicet que creditur, communis est sicut dici potest omnibus hominibus facies humana communis; nam hoc ita dicitur, ut tamen singuli suas habeant. Ex una sane doctrina impressam fidem credencium cordibus singulorum qui hoc idem credunt, verissime dicimus; sed aliud sunt ea que creduntur, aliud fides qua creduntur. Illa quippe in rebus sunt que vel esse vel fuisse vel futura esse dicuntur, hec autem in animo credentis est, ei tantum conspicua cuius est, quamvis sit in [p. 406] aliis non ipsa sed similis. Non enim una est numero sed genere propter similitudinem, tamen et nullam diversitatem magis unam dicimus esse quam multas. Nam duos homines simillimos cum videmus, unam faciem habere dicimus, facilius itaque dicitur multas animas fuisse singulas utique singulorum, de quibus legitur in actibus Apostolorum quod eis fuerit anima una, quoniam, ubi dixit Apostolus: Una fides, tot eas quisquam audet dicere quot fideles. Et tamen qui dixit: 0 mulier magna est fides tua, et alteri: Modice fidei quare dubitasti? suam cuique esse signat.

[ENGLISH]

## ¶3 · 406.12–406.33

> [p. 406] Ex istis notare potest logicus quod Augustinus loquitur de fide que est multitudo habituum credendi ab uno principio inlusorum et nec de genere nec de specie logico, quia illud universale non recipit predicaciones huiusmodi peregrinas; nam ad species tales accidencium non est motus, sed ad partes quantitativas generis quod est multitudo dissimilium qualitatum sed nulla earum. Patet secundo quod fides que creditur est veritas de presenti, de preterito vel futuro et non subiective in credente, et per consequens, omnia que fuerunt vel erunt sunt pro suo tempore; aliter enim non diceret Augustinus quod ea que creduntur sunt in rebus sicut articuli preteriti et futuri. Et gaudeo tercio quod magistra et mater nostra scriptura habet testes conformes sanctis doctoribus, eius eminenciam attestantes, sic tamen quod dicant consequenter illam unam fidem habere unum subiectum quod est corpus ecclesie, et tunc oportet dicere quod illud corpus dispergitur inter patres veteris testamenti tam Hebreos quam gentiles et non artare ipsum ad tempus post mortem Christi et gentem vulgari nomine christianam.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 402.25: and according to his definition there were Christians before the Incarnation.
- 403.10: Other absurd conclusions.
- 403.25: Application of his definition to the three days;
- 404.6: during which time, it leads us to believe, the Church ceased to exist.
- 404.27: 3. We are accused of attacking mere faults of expression;
- 405.1: but our opponent's error is serious,
- 405.15: since he confuses faith with the thing believed.
- 406.12: The terms "genus" and "species" are not applicable to faith.
- 406.25: The subject in which faith exists is the body of the Church.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 402: *fuerant* [R3]
  - 402: *XLIIª* [R5]
  - 403: *Romanorum* [THIN]
  - 403: *XIª* [THIN]
  - 403: *multitudo* (2 is a margin argument numeral) [R4]
  - 404: *falsum* [R3]
  - 405: *nec* (alinea L and 185a folio mark glued) [THIN]
  - 405: *descripcionem* [R4]
  - 405: *II°* [R3]
  - 405: *futura* (30 is the line number; italic) [R4]
  - 406: *loquitur* (loqui- here, tur next line; main token holds whole word) [R3]
  - 406: *principio* (clear ri) [NW]
  - 406: *specie* (1 is a margin argument numeral) [R4]
  - 406: *∅* (cre-/ditur: main pos 148 already holds creditur, so this second-half token is empty (hyphen convention)) [R6]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 402:
3. B: Jesus deest. 5. A in marg.: Nota quando incepit ecclesia.
Prima responsio. 25. A in marg. : Secunda responsio.
33. Aug. Epistola ad Asellicum. Opp. tom. II, pag. 734.

p. 403:
1. In codd. Rom. IX. i5. A in marg.: Tercia responsio. 25. A:
litera I deest. 3i. A in marg. : Quedam diffinicio ecclesie.

p. 404:
3. B: triduo deest. 4. B: data consequencia. 12. Codd.:
consiliis; sic et in sequentibus. i3. A A,: Sequitur — declarata
deest. 16. A A,: si — declarata deest. 18. 19. B: quod
domini ante. 27. A in marg. : Tercia responsio. 28 B: districcionis.
2?. Aug. Opp. tom. I, pag. 29. 27. Cf. p. 1 1 3 . 1. 14.

p. 405:
4. B: condcmpta. 6. A in marg. : Ecclcsia quid est? 7. li:
Sed conclusio ad. i3. A in marg. : Nota dc universali reali.
21. A in marg.: Augustinus. 25. In codd. suas deest; addidi ex
textu Aug. 26. B: expressam. 2.S. A B in marg. : Fides dupkx.
12. Aug. Opp. tom. VIII, pag. 932. 22. ib. pag. 929.

p. 406:
b. 7. B: de quibus loquitur; in textu Aug.: legimus. 7. B: eis fuit.
8. 9. B: tot eas quisque audet dicere, quot fides. 19. B: fides est que.
23. 24. B: que credantur.
```

---

## Chunk 17-f: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-17-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-17-f
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "407.1–410.29"
divisions: "cap. 17 (heading 'CAP. XVII.' at 388.1); part 6 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "929 words; 782 unanimous or majority-real; 139 settled by vote (INS 1, R2 88, R3a 45, R3b 2, R5a 1, R6a 2); 8 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n444–n447 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 17, part 6: [TITLE]

## ¶1 · 407.1–408.25

> [p. 407] Ulterius asseritur falsum esse quod defective et corrupte habet multitudo christianorum fidem Christi, eo quod multitudo christianorum habet in fide quidquid est ei necessarium ad salutem credere. Sed constat quod imprudenter ex causa particulari falsum inducitur, nam iuxta sic asserentem prescitus dum est in mortali habet habitum fidei sicut et quilibet falsus christianus. Et credo quod nullus dubitat quin defective et corrupte quilibet talis habet fidem Christi defective, quia peccabiliter, sicut et habuerunt apostoli qui rogaverunt ut Christus adaugeat eis Jidem Luce XVII°, 5. Si enim Petro non deficeret gradus fidei, Christus exprobrando non ei diceret Matthei XIV°, 3 1: Modice fidei quare dubitasti? Et corrupte habent fidem qui irretiti peccatis mortalibus corrumpunt bonos mores et ex informitate fidei finaliter corrumpuntur, nam secundum Apostolum Iª. Cor. V°, 6, modicum fermentum totam massam corrumpit. Ideo oportet doctorem consequenter dicere quod aliqua multitudo christianorum habet fidem valde defective et corrupte sicut homines opinionis sue. Nec moveat evidencia doctoris: si eandem fidem habent boni christiani et mali singuli, sequitur quod mali christiani eque perfectam et integram fidem habeant ut boni. Nam pertinens est hic loqui limitate de fide qua creditur, quia de fide que creditur eque perfectam fidem habent demones et creature singule ut beate. Ideo Augustinus loquitur de genere fidei que est tota multitudo habituum fidei in corpore ecclesie. Illud autem genus fidei habet unam partem quantitativam, perfectam in uno et in alio imperfectam, sicut genus motus localis habet in celo [p. 408] unam partem quantitativam uniformem quoad subiectum et tempus, sed aliam partem quantitativam utrimque difformem. In patria autem sunt singuli fidei uniformis, cum ibi evacuabitur imperfectum. Si enim eundem habitum fidei in numero omnino simpliciter habet quilibet christianus, sequitur quod ille habitus eque perfecte denominaret subiectum suum credere ut alius quicunque. Omnis enim qualitas denominat subiectum suum primum secundum sui ultimum, quia variacio disposicionis variaret gradum habitus et sic ipsum habitum. act Et ista est sentencia Augustini, non quod idem in numero scilicet actus vel habitus fidei sit formaliter in diversis personis, quia tunc quelibet illarum personarum foret fides quelibet. Fides enim non est nisi personam credere vel disponi ad credendum. Sed fides que creditur est veritas a credentibus aliena. Et sic quamvis infidelis eciam dyabolus credat veritatem fidei catholice, verumptamen secundum partem est infidelis et racione mortalis habet fidem corruptam et informem. Nec refert quoad illam informitatem, sive fides acquisita fuerit sive infusa, ut loquitur decretalis in Clementinis De Summa Trinitate et Fide Catholica, capitulo Firmiter, dicens quod regulariter fides infunditur in baptismo; quod ego credo de omni predestinato rite baptizato.

[ENGLISH]

## ¶2 · 408.26–409.1

> [p. 408] Et si queratur quando regulariter incidit quis in infidelitatem et quando remanet fidelis filius ecclesie, dicitur quod tripliciter dicitur quis esse de ecclesia, sicut tripliciter dicitur esse ecclesia preter ecclesiam nuncupativam. Aliqua enim est convocacio fidelium secundum quid vel ad tempus vel nude secundum [p. 409] presentem iusticiam, et taliter sunt presciti de ecclesia

[ENGLISH]

## ¶3 · 409.2–410.2

> [p. 409] pro tempore quo sunt in gracia. Illa autem ecclesia non est corpus Christi nec ecclesia sancta catholica 2 nec pars eius. Secundo modo sumitur ecclesia mixtim pro predestinatis et prescitis dum sunt in gracia secundum presentem iusticiam; et ista ecclesia communicat in parte sed non in toto cum ecclesia sancta Dei. Et ista ecclesia vocatur mixtim granum et palea, frumentum et zizannia, nec non et regnum celorum de quinque fatuis virginibus et quinque prudentibus (ut patet in parabolis evangelicis); et istam ecclesiam vocavit Tyconius erronee corpus domini bipartitum (ut patet 111° De Doctrina Christiana XXXII°); non enim sunt presciti corpus domini vel pars eius! Sed tercio modo sumitur ecclesia pro convocacione predestinatorum, sive sint in gracia secundum presentem iusticiam sive non. Et isto modo ecclesia est articulus fidei, de quo loquitur Apostolus Ephes. VI°. Et sic nullus prescitus est de sancta ecclesia, licet sit in illa Correspondenter potest intelligi tripliciter personam esse de ecclesia. Primo modo nude secundum Presentem iusticiam, ut presciti sunt de ecclesia primo modo dicta; secundo modo predestinati sive presciti dum sunt ad tempus in gracia sunt de ecclesia secundo modo dicta, differenter tamen et equivoce presciti et predestinati, ut patet ex varietate tituli predestinacionis et presciencie et ex diversitate corporis Christi et corporis dyaboli. Sed tercio modo omnes predestinati, et solum tales sunt de sancta matre ecclesia, differenter tamen quando sunt in mortali cum sola predestinacionis gracia et quando cum illa sunt in gracia secundum presentem iusticiam; tunc [p. 410] enim sunt continuati corpori Christi secundum humidum fluens et secundum humidum naturale. two

[ENGLISH]

## ¶4 · 410.3–410.29

> [p. 410] Istis premissis dicitur quod omnis prescitus nunquam est de ecclesia tercio modo dicta; est autem de ecclesia primo et secundo modo dicta, quando splendet in eo lumen gracie et pro quocunque mortali veniente est extra triplicem ecclesiam, licet habuerit tantam fidem infusam, ut montes transferat; nam fides omnino informis, sive infusa sive adquisita, non sufficit constituere personam, ut sit de ecclesia, quia cum illa fidestat hominem dampnari perpetuo; fides autem cum gracia predestinacionis constituit hominem membrum ecclesie sive sit in gracia secundum presentem iusticiam, sive ad tempus iniustus tuent vel eciam infidelis. Generacio enim qua talis fit filius salvat eum, ne possit cum datis paribus peccare peccato finalis impenitencie ut prescitus, et sic nemo potest desinere esse membrum sancte ecclesie tercio modo dicte quia tunc desineret esse predestinatus; incipit autem esse membrum illius ecclesie secundum disparem racionem, nunc quando incipit esse et nunc quando incipit esse iustus (ut notat Augustinus super Johannis Omelia XLIXª). De prima autem ecclesia nunc cadunt et nunc incorporantur presciti, secundum quod accenditur vel extinguitur in eis scintilla gracie; de secunda vero ecclesia cadunt predestinati casu secundum quid, sed presciti quandoque cadunt simpliciter, illa autem ecclesia desinet esse ad diem iudicii, cum tunc desinet esse commixtio grani cum palea.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 407.1: Further, our opponent says that the mass of Christians do not hold the faith defectively.
- 407.9: Answer: Sin makes faith defective.
- 407.16: How we believe is the question;
- 407.25: as to what is believed the devils are at one with the blessed.
- 408.12: Faith is the act of believing, or the disposition to believe.
- 408.28: Three senses of Church: a) all who are nominally Christians,
- 409.4: b) all who are in present righteousness,
- 409.15: c) all the predestinate. In this last sense the Church is an article of belief.
- 409.20: A man may be in or out of the Church, according to the sense in which the word is used.
- 410.3: In the first two senses the foreknown may be members of the Church,
- 410.12: but in the third sense all the predestinate are members, and only they.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 407: *Christi* (10 is the line number) [R3]
  - 407: *Christus* [R3]
  - 407: *Iª* [R3]
  - 409: *presentem* (alinea O and 185c folio mark glued) [THIN]
  - 409: *esse* (1 is a margin argument numeral) [R3]
  - 410: *iniustus* (clear ni) [NW]
  - 410: *XLIXª* [R4]
  - 409: *secundo* (se-/cundo; output holds both halves) [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 407:
i. B in marg.: Nota quomodo quidam habent fidem defective et cor-
rupte. A in marg. : Nota qui sunt qui habent fidem corruptam et qui
defectivam. II. B in marg. : Inferius nota quod in patria sunt sin-
guli fidei uniformis; ergo sequitur ut videtur quod fides manebit in patria.
22. A A,: homines opltus. B: sue deest. 27. A in marg. : Nota.
32. A Aj: habet in celo habet partem.

p. 408:
i3. B in marg.: Nota. A B in marg.: Quid est fides. i5. A A,:
foret quelibet. 26. A in marg. : Questio. 29. B in marg. :
Solucio. AB in marg. : Nota quod triphciter dicitur quis de ecclesia sicut
tripliciter dicitur (A: capitur) ecclesia.
24. Not in Clementinis, but in Decr.Greg. IX, lib. I, tit. I, cap. L
3i. Cf. Johannis Wyclif, De Civili Dominio pag. 288.

p. 409:
4- A A,: modo deest. 12. B: 20. B in
Tripliciter aliquis est de ecclesia. marg.
18. Ephesians V. 3o-32.

p. 410:
3. A in marg.: Nola. 10. B: sufficit — dampnari deest. n. A in
marg. : Fides cum gracia predestinacionis constituunt hominem mem-
brum ecclesie. i3. A in marg. : Nota quod diversimode aliqui cadunt
de ecclesia (Above i85d without mark of reference). i3. B: sit deest.
3o. A in marg. : Quarta responsio.
```

---

## Chunk 17-g: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-17-g.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-17-g
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "410.30–412.14"
divisions: "cap. 17 (heading 'CAP. XVII.' at 388.1); part 7 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "348 words; 310 unanimous or majority-real; 33 settled by vote (INS 1, R2 16, R3a 11, R3b 1, R5a 4); 5 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n447–n449 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 17, part 7: [TITLE]

## ¶1 · 410.30–412.14

> [p. 410] Ad quartum argumentum respondetur quadrupliciter pro declaracione huius quod nec apostoli nec [p. 411] alii fideles erant de ecclesia, antequam fides fuit a sanctis patribus in conciliis generalibus declarata. Et suppono quamlibet istarum responsionum validam, cum aliter nimis superflue globarentur. Prima responsio et secundum partem validissimam dicit quod ante mortem Christi fuit doctrina fidei nostre per Christum et suos apostolos sufficienter divulgata et declarata per sanctos patres (supple per Christum et apostolos) ante mortem Christi in conciliis generalibus celebratis, et quod ista concilia ante mortem Christi habita inter Christum et apostolos cum suis discipulis de hiis que pertinent ad fidem fuerunt generalia. Patet per descripcionem concilii generalis positam in glosa Johannis XVIIª dist. cap. Generalia, ubi dicitur quod illud est generale concilium quod a papa vel eius legato aut locum eius tenente cum omnibus episcopis celebratur. Cum ergo Matthei X° dicitur quod Christus convocavit discipulos suos et, exponens eis fidem, dedit eis privilegia et multiplices potestates, videtur quod ipse celebravit tunc concilium generale; et idem patet Matthei XV° et Marci VI° et sepe ante mortem Christi, ubi loquitur discipulos convocasse. Istud autem dictum est in parte catholicum, cum tota trinitas eterno consilio decrevit decursum ecclesie consuluitque patriarchis, prophetis et capiti ecclesie domino Jesu Christo, secundum quem cursum procederet sancta mater ecclesia. Verumptamen non oportet omnes episcopos ad tale concilium congregari, nec facit per se multitudo personarum consulencium ad concilii, cum generalissimum quia principium omnibus aliis sit concilium increatum. Verumptamen in conciliis apostolorum et aliis conciliis generalibus quoad multitudinem episcoporum quatuor apostolorum [p. 412] concilia tenuerunt primatum, et post quatuor concilia principalia, de quibus XVIª dist. Omnibus, et quatuor fuerunt sollempnes sinodi (ut patet XVI. dist. Omnibus). Omnibus tamen istis hoc imperfeccionis fuit quod unusquisque tamquam ignarus consulendo quesivit ab alio. Non sic autem in concilio increato nec in concilio quod Christus cum apostolis celebravit; ipse enim omnisciens non consuluit eos in sibi ambiguis sed per se diffinivit et auctorizavit quid foret ecclesie faciendum; quod pape non potest competere. Ideo concilia posterius solempnizata non possunt nisi equivoce dici concilia vel generalia aut decreta, inter illa tamen quatuor concilia apostolorum racionabiliter habent preeminenciam dignitatis.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 410.30: 4. My opponent says
- 411.4: that there were general councils in which Christ conferred with his apostles.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 411: *alii* (alinea P and 185d folio mark glued) [THIN]
  - 411: *XVIIª* [R4]
  - 411: *illud* (15 is the line number; italic) [R4]
  - 412: *XVIª* [R4]
  - 412: *Christus* [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 410:
3. A in marg.: Nola. 10. B: sufficit — dampnari deest. n. A in
marg. : Fides cum gracia predestinacionis constituunt hominem mem-
brum ecclesie. i3. A in marg. : Nota quod diversimode aliqui cadunt
de ecclesia (Above i85d without mark of reference). i3. B: sit deest.
3o. A in marg. : Quarta responsio.

p. 411:
5. A A, : validiss.ma. 12. A in marg.: Nota de concilis genera-
hbus. 16. A m marg.: Quid est concilium generale? B in marg •
Generale concilium quid sit nota. 22. 15: ubi legitur.

p. 412:
2. B in marg. : Quatuor consilia apostolorum et quatuor fuerunt
solempnes sinodi, ut patet XVI. dist. Omnibus. 2. B: XV.
10. B: potest deest. i5. A in marg.: Contra hoc quod dicitur
quod ecclesia incepit post mortem Christi. 19. B: honorem dcest.
20. 21. A A,: sed innuitur.
2. Dist. XV vel XVI. Omnibus non extat. Cf. pp. 388, and 3g8.
```
