# Translation brief: dialogus 02–14

You translate these 2 chunk(s) of Wyclif's *Dialogus sive Speculum ecclesie militantis* in a single pass. Everything you need is in this file:
the working card, the glossary rows these chunks use, and for each chunk its scaffold and the editor's
apparatus for its pages. Work so as to use few tool calls:

1. Read this brief once (it is the only file you need to read).
2. For each chunk, write the COMPLETE chunk file ONCE with the Write tool to its path (given in the chunk's
   header below): the scaffold with `status: translated`, the title, the English after every Latin block,
   headings renamed per the card, the side-notes corrected, Notes, and Transcription notes, in the card's
   layout. Never alter the Latin. Do not make a series of small edits.
3. Use the apparatus given here for variants (the card's rule: a variant that gives the sense is translated
   with a T note citing the siglum; otherwise translate the print and flag it). Open a plate image only if a
   word cannot be construed at all from the print plus the apparatus; otherwise flag it as a Latin doubt.
4. Scripture: quote the Douay-Rheims as you know it. At the END, check every reference you quoted in ONE
   command: `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/bible.py "Ref 1" "Ref 2" ...` and fix any wording
   that differs, in the same chunk file (this is the one allowed round of edits).
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/dialogus/_pilot/brief-test/wyc-dialogus-02.md chunks/dialogus/_pilot/brief-test/wyc-dialogus-14.md` once and fix what it reports.
6. Final message: per chunk, the ledger rows (table: id | chunk / note | claim | status | how / next step),
   glossary proposals, Latin doubts, and a one-line note of anything the coordinator must decide.


## The working card

# TRANSLATOR CARD — one *Dialogus* chunk, one agent

This card replaces reading CONVENTIONS, the pilot and Thakkar in full: it is their working core.
Read it, then `GLOSSARY.md` (all of it; it is short), then your scaffold. Consult CONVENTIONS.md
only when the card sends you there. Work in `~/wyclif`. Wyclif is approached with **daggers drawn**:
the two most recent English translations were "worse than useless" because of four error
classes (below). Your English must survive a hostile reader with the Latin open.

## Work lean (cost is per tool call: each call re-sends your whole context)

Aim for **about 10 tool calls** in all:
1. One call reading CARD + GLOSSARY + your scaffold together (`cat` them).
2. **One** `bible.py` call with every scripture reference you need (it takes many refs).
3. Plates **only** for a Latin doubt or a side-note you cannot fix by the OCR rules below.
   Not to "check" the side-notes generally.
4. Write the finished chunk in **one** Write of the whole file (Latin blocks copied unchanged).
5. Lint once; fix; done. Draft in your head, not in the file.

## The job

The Latin in your scaffold is **established and frozen**. Fill: `[TITLE]` (short, lower case: "the
first law: Numbers 18"), each `[ENGLISH]`, the notes, the side-notes, the transcription notes; set
`status: translated`; lint; report.

- **Headings:** rename `## ¶k · range` to the speaker(s): `## Truth · 5.13–7.10`, `## Falsehood · …`,
  `## Truth and Falsehood · …`. VERITAS = Truth, MENDACIUM = Falsehood. **Never change a range; never
  split a paragraph.**
- **Never alter the Latin.** A word that looks wrong: open the plate (`text/dialogus/raw/leaves/nLEAF.jpg`,
  LEAF = page + 31; if missing, `curl -sL -o text/dialogus/raw/leaves/n0LEAF.jpg https://archive.org/download/latinworks22wycl/page/nLEAF.jpg`),
  read the apparatus at the page foot, and then: a variant that gives the sense → translate it + **T**
  note citing the siglum; a compelling emendation → translate it + **T** note "(our emendation)"; neither →
  translate the print and flag it. Never smooth nonsense into sense. Report every such case.
- **English layout:** speech opens `TRUTH.` / `FALSEHOOD.`. `[N]` at the same word as `[p. N]` in
  the Latin (the chunk's first `[p. N]` is implicit). Supplied words in `[brackets]`, sparingly.
  Quotations in quotation marks (italics are `none` in this volume; find quoted matter by sense).

## The four error classes (Thakkar) — check every sentence

1. **Terms:** GLOSSARY.md governs, one term one rendering. Tag the **first occurrence in the chunk**
   of every §A–C term: `[lordship]{g:dominium}`. The key must exist in GLOSSARY.md. A term that looks
   technical but has no row: render it sensibly, untagged, and propose it in your report.
   **CONTEXTUAL** rows (e.g. *inconveniencia*: absurdity / troubles) hold two senses English splits:
   choose the English by context, and write a **C** note at the first occurrence in the chunk and
   wherever it leans to the other sense (the dikaiosune rule, CONVENTIONS §6).
   Key rulings: *caritas* charity (never love) · *dominium* lordship · *presciti* the foreknown ·
   *predestinati* the predestinate · *viator* wayfarer · *patria* homeland · *ex fide* as faith teaches
   (with a genitive: "from the faith of scripture") · *limitare* assign (noun *limites* limits) ·
   *indispositus* unfit · *liberum arbitrium* free choice · *sensibilis* perceptible · *sentencia* teaching ·
   *evidencia* evidence · *reditus* revenue(s) · *conversacio* manner of life (the rest: GLOSSARY).
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

   "Now" is reserved for the minor premiss. *Quia autem vellem* opening a speech is "And because I
   wished", not "Now because".
3. **Ordinary words with a medieval sense:** GLOSSARY §D; look up any word whose classical and
   Wyclifite senses may differ, and propose additions.
4. **Syntax:** construe before rendering (main verb, subject, what every relative and genitive
   hangs on). Keep quantifier order where it is meaning. Keep Wyclif's long periods where English
   tolerates them. **A doubtful construal is never chosen silently:** translate the likelier reading
   and write a **C** note giving the alternative.

## Scripture

`python3 scripts/w3/bible.py "Num 18:20-24"` (Vulgate + Douay–Rheims; psalms in Vulgate numbering)
or `python3 scripts/w3/bible.py --find "maledicti qui declinant"`. Where Wyclif's Latin agrees with the
Clementine Vulgate, use the **Douay–Rheims wording**. Where he departs, translate *his* Latin and
write an **S** note giving the Vulgate. Modern references in the English (Num. 18:20); the verse
numbers are Pollard's.

## Notes

- `[^n]` from 1, the marker placed in the same edit as its note, each opening with a type letter:
  **T** text · **C** construal · **G** glossary (passage-specific only; otherwise a tag) · **S** source ·
  **R** reception/context.
- **Density: about one note per 70–100 Latin words**, fewer where the text is plain. Short, factual,
  says what the Latin does and stops. No modern theology, no evaluation.
- **Every identification** other than scripture checked with bible.py gets a ledger row in your
  report with a status: `editor` (Pollard's margin reference, listed in the scaffold's Transcription
  notes), `to-verify` (from memory: every patristic or canon-law identification you did not read in
  this session), `verified` (you read the source text this session: say where). ⛔ Never pass memory
  off as verified. Id `D<chunk>-<n>` (`D12-1`), cited in the note: "(LEDGER D12-1)".

## Worked example (chapter 3, batch A, reviewed)

> VERITAS. Quia autem vellem quod ista lex et cleri specialiter esset recencius memorata, feci illam
> scribi sepius in duplici testamento. Et sicut nemo potest excusari quin noscat in gradum qui sibi
> pertineat legem dei, sic nemo potest excusari quin noscat quodammodo matrem suam.

TRUTH. And because I wished that this law, and the clergy's especially, should be remembered the
more freshly, I had it written more than once in the twofold testament. And as no one can be
excused from knowing [God's law]{g:lex-dei} in the degree that pertains to him, so no one can be
excused from knowing, in some manner, his mother.[^1]

[^1]: **C/T.** *In gradum qui sibi pertineat*: "in the degree that pertains to him", with *qui*
    agreeing with *gradum*. B, C omit *in gradum* and read *quid*: "knowing what pertains to him
    according to God's law".

## Side-notes

The scaffold's list is a machine OCR draft. Keep only notes whose page.line falls **inside your
range**. Fix unambiguous OCR confusions (i/l, 0/o, rn/m, stray digits); for anything else read the
plate. Pollard's wording verbatim, no paraphrase. Join a note split over two draft lines. Delete the
`OCR DRAFT` comment.

## Finish

1. `status: translated` in the front matter (nothing else changes there).
2. `.venv/bin/python scripts/w3/lint.py chunks/dialogus/<your chunk>.md` until clean.
3. The four-class check above, sentence by sentence.
4. ⛔ Edit **only your chunk**. No git, no other files. Everything shared goes in your report.

## Report (≤ 200 words, exactly these heads)

- **Chunk:** id, Latin words, notes.
- **Ledger rows:** in LEDGER.md's table format `| id | chunk / note | claim | status | how / next step |`.
- **Glossary proposals:** Latin · proposed English · where · why.
- **Latin doubts:** page.line · printed · suspicion · settled on the plate?

## Glossary (the 82 rows these chunks use; the full file is GLOSSARY.md)

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
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
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
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| possessionati | the possessioners | Endowed religious. |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| simpliciter / secundum quid | **without qualification / in a certain respect** | ⛔ Always opposable. Never "simply", "wholly", "directly", "naturally" etc. (T. p. 364). |
| necessitas supposicionis | necessity of supposition | Conditional necessity. Pilot (*Eccl.* 3.21). |
| de congruo / de condigno | by congruity / by condignity | Pilot. |
| consequencia | inference | ⛔ Not "consequence" (T. p. 361 n. 13). |
| consequens / antecedens | consequent / antecedent | |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| citra fidem | short of faith | The contrast with *ex fide*: held on evidence, not as faith teaches. Ruled 2026-09-28 (4 sites). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| illabi | to flow into | Ruled 2026-09-28. |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| indispositus; (se) indisponere | unfit; to make (oneself) unfit | "indisposed" (now "unwell"). Ruled 2026-09-28 (8 sites). |
| limitare; limites | to assign (an office); limits | "to limit" for the verb. The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| carecter (sensibilis) | (perceptible) character | "reputation". The mark of orders. Ruled 2026-09-28 (*Dial.* 5.7). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |

---

## Chunk 02: write to `/Users/wilsonpruitt/wyclif/chunks/dialogus/_pilot/brief-test/wyc-dialogus-02.md`

### Scaffold

````markdown
---
chunk_id: wyc-dialogus-02
work_la: Dialogus sive Speculum ecclesie militantis
work_en: Dialogue, or The Mirror of the Church Militant
volume_slug: dialogus
editor: Alfred W. Pollard
year: 1886
pages: "3.15–5.11"
divisions: "cap. 2 (heading 'CAPITULUM 2m.' at 3.14)"
latin_source: three-witness
witnesses: [11663460bsb, dialogussivespec00wycl, fordham, iohanniswycliff00wyclgoog, iohanniswycliffe05wycl, latinworks22wycl]
check: "385 words; 370 unanimous or majority-real; 14 settled by vote (R2 9, R3a 5); 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks22wycl, leaves n34–n36 (printed p. = leaf − 31)"
status: draft
---

# *Dialogus*, chapter 2: [TITLE]

## ¶1 · 3.15–4.2

> [p. 3] VERITAS. Correspondenter ad vitas et officia istarum trium parcium ordinavi illis regulas vivendi, ne in suis officiis confundantur. Clerum autem, qui debet esse supremus et celo propinquissimus, ordinavi a causis mundialibus et mundi sollicitudinibus maxime sequestratum, et sic non dominaret seculariter sed deberet esse pauper, similis statui innocencie instar mei. Et sic debuit docere duas partes alias mundum deserere tam opere quam sermone. Et ista vita similis aquiline est ad similitudinem vite angelice contemplativa [p. 4] perfeccior quam activa. Et qui est indispositus hanc vitam vivere est indispositus clericari.

[ENGLISH]

## ¶2 · 4.3–4.7

> [p. 4] Secunda autem pars ecclesie debet dominari seculariter et esse in temporalibus opulenta, quia hoc est instrumentum necessarium suo officio quod isti parti ecclesie limitavi. Sic enim deitas cohercet homines dando illis rerum affluenciam, et immiscet quodammodo potentiam coactivam.

[ENGLISH]

## ¶3 · 4.8–5.11

> [p. 4] Terciam autem partem et infimam volo in labore corporali vivere et circa lucrum temporalium se cum moderamine ocupare; et sic omnes has tres partes ecclesie volo, tam in spirituali quam in temporali quantum racio exigit, ad suum officium habundare. Et sicut in trinitate increata est summa concordia, sic volo in hiis tribus partibus ecclesie esse amoris concordiam, controversia expulsa secundum virtutis regulas, cum ecclesia sit corpus liberi arbitrii quod per Christi capitis influencias reguletur. Disponat ergo se corpus ecclesie, et specialiter suprema pars que secundum augustinum debet esse montes, ut influencie hujus capitis coaptetur, et tunc bene regulabitur secundum graciam jhu Christi. Sicut enim pars bassior in qua vigent terre nascencia recipit influenciam suam a solari lumine, sic pars inferior terrene ecclesie recipit influenciam suam derivatam per clerum a sole justicie. Et nichil sensibilius conturbat ecclesiam vel inducit in eam morbidam discrasiam quam quod una ejus pars accipiat ministeria alterius, et correspondenter officia et per consequens dimittat officia sibimet limitata. Nec est possibile Christum deficere officium et statum parti ecclesie limitare, nisi illi [p. 5] parti deficiat influxa gracia ex peccato proprio, que se ad recipiendum dictam graciam indisponit. Nec omnia membra istarum parcium eque perficiunt officium quod statui suo attinet, sed unum magis et aliud minus, secundum quod radius gracie cum ipso homine operatur. Alia autem membra diaboli que seminantur in ecclesia non sunt proprie partes ejus, licet habeant carecterem sensibilem et nomen quoad famas hominum pupplicatum, quia verum officium quod deus requirit de persona status ecclesie est signum evidencius quam signum humanitus introductum. Ideo dicit Christus jo 10 operibus credite.

[ENGLISH]

## Pollard's side-notes (PD, verbatim; not our translation)

<!-- OCR DRAFT, grouped by machine: correct every note against the plate (leaf images in
     text/dialogus/raw/leaves/ or archive.org/download/latinworks22wycl/page/nLEAF.jpg), fix the
     page.line where a note is misplaced, and delete this comment. -->

- 3.1: These three parts must be knit by love-
- 3.3: B1. 150 b The ciergy must
- 3.3: set a good
- 3.6: The temporai lords must promote Christian welfare. * A
- 3.9: The Pe0pie must serve clergy and L J
- 3.10: B. lc. io
- 3.10: J0^- a*™j;™dbyers
- 3.15: 1 Each order has
- 3.15: its own rule of Kfe.
- 3.17: The ciergy by their life of Poverty and contemPlation must teach the othe;" orders to forsake
- 3.20: 2o the world-
- 4.1: Eise they are no true clergy.
- 4.3: The temporai lords must be nch and powerfui.
- 4.8: The peopie must work for their lmng.
- 4.13: Thethreeorders must live in the harmonyof love.
- 4.15: For the church is a body of free judgment which b. ld.
- 4.16: dispose
- 4.17: openSthe^nhead" °f lts
- 4.20: The goodness of the other orders r ^ ° depends on that 01 the clergy. ' r
- 4.23: Nothing more C. 2 a. disturbs the Church than for
- 4.25: anotheJkand
- 4.26: leave its own.
- 5.2: 98' Not aii members
- 5.2: of these orders have the same fitness for their * work-
- 5.5: But members of the devil living "> *he Church are not members of the Church.
- 5.10: These may be known by their
- 5.15: Men are °°und to know and 1 1 x
- 5.16: La^andthe
- 5.22: ignorance of Chnst and the r

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 3: *CAPITULUM 2m.* [HEAD]
- **Omitted per §3.5 / kept in the English** (margin matter): MS mark Bl. 150 c. (5.1); reference Johnx. 38. works. (5.11).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 3:
i. tres, al. man. in marg. B. 2. ipsis, al. man. inter lin. B. om. Bl.
3. rubr. in marg. Clerus, B, c. autem, om. c. 5. eos docere, ord.
inv. c. 6. promerendam corr. al. man. ex promerendum, b. 7. in
marg. rubr. Domini temporales, B, c. 8. personas sed al. man.
partes, B. pas =personas, sed al. man. in marg. partes, Bl. alter-
natas, B. 9. consequendam, B, B1, C. in marg. rubr. Volgares,
B, C. 10. autem, pro vero, B, Bl. 11. sup. du., ord. inv. b, b1.
13. in am. hil., ord. inv. B1. 14. rubr. Veritas declarat materiam
inceptam. In marg. Cam. 2™. C. 15. Veritas declarat 3™. B. 17.
in marg. rubr. Regula cleri, c. 19. sequitur rubr. ecce sacerdos
veritas, id est Christus, de te ordinat ut sis in tuis conversacionibus
abstractus a curis mundanis, et tu vis utique ad oppositum, C. sic ut
non dominaretur, ut al. man. b. sic non dominaretur, B1. sic ut non
dominaretur, c 23. est aquiline, ord. inv. B.

p. 4:
3. in marg. rubr. Secularium regula, B. Regula secularium, c.
4. in, al. man. B. om. B1. 5. isti, corr. ex recti, B. 8. in marg.
rubr. Laborancium regula, B. Regula laborancium, c. et, om.
B, Bl, c. nolo,/r^ volo, B. 10. tam temporalibus quam
spiritualibus, b, b1. tam spiritualibus quam temporalibus, c. 13.
am. esse, ord. inv. c. 14. virtutum, B, b1, c. 18. montes, sed in
marg. al. man. innocens, C 19. regulam, pro graciam, b1. in
marg. rubr. officia, b, c. 24. instrumenta, pro minist., B, b1, c.
25. consequenter, b, b1, c. et officia, om. B, B1, c. 26. unum,
at. man. Christum, B. 27. parti, om. B, B1, c. militantes, sed al.
man. limitare B. al. man. sub limitare. militanti, B1.

p. 5:
1. ecclesise post parti, al. man. add. b. se, om. B, Bl, c. 2. indispo-
nunt, b. 3. in marg. rubr. mebra ecclesia, c. eque al. man., B, B1.
secundum officium, B1, B. 4. magis aliquod minus, B. magis aliud
minus, B1. maius aliquod minus, c. 5. m,pro cum, B. homine, al.
man. B ; om. B1. in marg. rubr. hic loquitur monachus, C 7-
caracterum, B, B1, c. 11. 16, B, B1. 12. sequitur rubr. Veritas
continuit in hoc capitulo vetus testamentum Num. 18 ponens quam
vitam debent sacerdotes vivere probacio paupertatis. In marg. rubr.
Cm. 3™. c. 13. Veritas, 4m. B. 14. michi, pro in, B. 15. testi-
monio, sed al. man. in. marg. testamento, B1. sic; pro sicut, B1. 15-1 7.
quin . . . excusari, om. b1. 16. in gradum, om. B, c. quid. pro qui
B,c. secundum legem, B, c; sed secundum al. man. B. dei int. lin.al.
man., C. 18. serv. opor., ord. inv. C. caput est, ord. inv. C. 19.
matrem suam, B, B1. 21. suam, om. B, b1. secundum (add.) humani-
tatem suam (add.), B, b1.
```

---

## Chunk 14: write to `/Users/wilsonpruitt/wyclif/chunks/dialogus/_pilot/brief-test/wyc-dialogus-14.md`

### Scaffold

````markdown
---
chunk_id: wyc-dialogus-14
work_la: Dialogus sive Speculum ecclesie militantis
work_en: Dialogue, or The Mirror of the Church Militant
volume_slug: dialogus
editor: Alfred W. Pollard
year: 1886
pages: "26.28–28.30"
divisions: "cap. 14 (heading 'CAPITULUM 14m.' at 26.27)"
latin_source: three-witness
witnesses: [11663460bsb, dialogussivespec00wycl, fordham, iohanniswycliff00wyclgoog, iohanniswycliffe05wycl, latinworks22wycl]
check: "502 words; 473 unanimous or majority-real; 24 settled by vote (DEL 2, R2 9, R3a 12, R3b 1); 5 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks22wycl, leaves n57–n59 (printed p. = leaf − 31)"
status: draft
---

# *Dialogus*, chapter 14: [TITLE]

## ¶1 · 26.28–28.30

> [p. 26] MENDACIUM. Iterum manifeste innuis non esse ut fidem [p. 27] credendum illos esse sanctos qui in missis, in letaniis, et aliis ecclesie serviciis inseruntur; ad quid ergo diceremus de illis nisi crederemus quod in patria suntbeati? cum spes meriti super fide stabili in credentibus est fundanda. VERITAS. Hic dictum est sepius quod de sanctis quos canonizat ecclesia supponimus, sed non ut fidem credimus, quod sunt beati in patria. Undecim tamen apostolos cum paulo, magdalene et ceteris quos fides scripture implicat esse sanctos, credendum est ut fidem esse beatos, et alios, quantumcunque magna sanctitate in celis prepolleant, credimus esse in beatitudine, verumtamen citra fidem. Et ideo ordinavit ecclesia quod quecumque oracio porrecta ad sanctum ad deum principaliter dirigatur. Et sic quelibet talis oracio implicat tacite condicionem, si et quatenus placet deo per talis sancti meritum nobis miseris suffragari. Et ut videtur multis nulla oracio porrecta specialiter sancto Christi est laudabilis, nisi de quanto acuit devocionem in Christum, sic quod si omnes intenciones et oraciones uniri possent in Christum, sincerius directe unite in Christum, esset utilius Christiano omnes oraciones specialiter Christo porrigere. Nec valet false credere quod Christus propter celsitudinem sui dominii non potest a nobis miseris faciliter exorari; ideo est necessarium habere alias personas mediantes; Christus enim assistens pontifex immediate illabitur viatori et cum hoc immediate conjungitur deitati. Ideo nullus sanctus est misericordius aut facilius auditivus miseri quam est Christus. Nec valent oraciones aliorum sanctorum, nisi de quanto Christus prius ex sua gracia has acceptat. Ideo dicunt quidam quod porrecciones oracionum ad istos sanctos sepe [p. 28] sunt superflue vel nocive. Conceditur ergo quod non est articulus fidei appropriare cuilibet sancto de quo dicimus specialem articulum fidei sed beatitudinem illorum supponimus secundum majorem evidenciam vel minorem. Unde absit quod omnes legende sanctorum in ecclesiam introducte sint fides catholica, cum in festo corporis Christi de sancto sanctorum scribitur quod accidencia sunt in eucaristia sine subjecto, quod non fuit fides tempore augustini. Ideo dicit in de sermone Domini in monte quod multa vera, licet in legendis talibus inserantur non sunt fides catholica; sicut exemplificat de ministro convivii cujus unum brachium a cane rapido est abstractum. Sufficit ergo ad tales oraciones secundarias habere probabilem supposicionem, et de Christo qui fundamentaliter oratur habere cum aliis virtutibus firmam fidem; et patet solucio. In ista tamen materia dicunt scolastici quod aliqua est fides explicita vel expressa et aliqua est fides implicita sive tacita. Fidem autem implicitam dicunt esse quamcunque veritatem juxta illud apostoli prima cor. Caritas omnia credit, et tamen infinite sunt veritates de quibus non oportet nos hic habere fidem explicitam; cum sufficit fideli quod credat quamcunque veritatem secundum gradum et formam qua deus vult ipsum hanc credere. Ut carnis resurreccionis est articulus fidei cuilibet Christiano, et tamen non oportet de qualibet persona hominis habere expressum articulum fidei quod resurget. Sed deus vult quod per istam fidem generalem sua militans ecclesia excusetur. Non enim vult quod sua ecclesia cum veritatibus inutiliter oneretur. Communis autem carnis resurreccio erit tempore sempiterno adhuc futura, et postmodum tempore suo presens; sed post diem judicii est elapsa.

[ENGLISH]

## Pollard's side-notes (PD, verbatim; not our translation)

<!-- OCR DRAFT, grouped by machine: correct every note against the plate (leaf images in
     text/dialogus/raw/leaves/ or archive.org/download/latinworks22wycl/page/nLEAF.jpg), fix the
     page.line where a note is misplaced, and delete this comment. -->

- 26.1: And with letters of fraternity.
- 26.6: Aii our hope should be m r Christ.
- 26.11: As to contracts, they are usually °
- 26.12: sTnfuToath? by
- 26.15: Astoinheritances, paternity A shouidnotbedisputed except at God's wiii.
- 26.24: And about these
- 26.25: feessbetter t0 Care
- 26.28: Mend. objects
- 27.2: You thus deny that the sanctity saints to whom address we faruhers is °f
- 27.5: Ver. answers :
- 27.6: we do not hoid of faith the as sanctity of any but Scripture saints-
- 27.11: Prayers are addressed me-
- 27.12: djri^te\y5?ontS' God-
- 27.17: And are only . good, lf at all, m sofar asthey. quicken devotion r Christ-
- 27.25: 25 Who is more
- 27.25: ready to hear than any saint.
- 27.28: Prayers to saints often harmful. are
- 28.3: The sanctity of saints is to be beiieved or not according to the
- 28.5: ThdrTegends arenotoffaith. In primo
- 28.7: nocturno, ... . . . . ...
- 28.7: just as the ex- Lectio II. istence of accidents without a substance in the jt Eucharistisa doctnnal De accre-
- 28.10: tion- Serni. Dei
- 28.11: So are many of in Monte, these 1. 05. legends.
- 28.13: it is enough to believe tentativeiy in prayers to saints, absoluteiy in Christ. *5
- 28.16: Expiicit (or specific) differs from impiicit (or in- B1. 153 b. definite) faith. ^
- 28.22: We must beiieve in the resurrection of the body, but not separ-
- 28.24: thfs orlha?1 °f
- 28.25: man'sbody.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 26: *CAPITULUM 14m.* [HEAD]
  - 27: *∅* (side-note "to Christ") [R4]
  - 28: *fides* [R3]
  - 28: *scribitur* [R4]
  - 28: *in* [R4]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Aug (28.10); reference 1 Cor.xiii. (28.18).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 26:
7. dei, pro Xti, B, B1, c. 8. concipiendum, pro percipiendum,
B, B1, c. istius, pro illius, B, B1, c. 14. hec, pro hoc, B, b1.
15. patrum corr. ex patribus, B, B1. patrum, c. 22. magna,
pro magis, B, B1, c. 23. speculativi, B, B1, c. 24. practici,
B, B1, c. multum, pro multi, B, Bl, c. 25. contencionis,
B, B1, C.

p. 27:
1. in, antc letaniis, om. b1, c. 2. horarum officia, diceremus,
add. B, c, scd B, al. man. in marg. 8. Magdalena, B, c. 9. qua-
cunque corr. cx quantumcunque, B. quacunque, C. 14. et si, ord.
inv. B, b1, C. placeat, B, B1, c. 19. sup. Xtum al. man. scilicet
sanctum, B ; ipsum corr. cx Xtum, B1 ; ipsum, ct int. lin. al. man.
sanctum, c. est, pro esset, Bl, c. 20. ad Christum, pro Xto,
B, B1, c. 23. pers. al., ord. inv. B, B1, c. 25. sanctus, om. B, Bl, c.
26. aut audacius, pro auditivus, B, b1, c. misereri, b, c. miserere, B1.
28. &e,pro ex, B, B1, c.

p. 28:
1. sunt, om. b, Bl, c. nocive fiunt, B, b1, C. 2. appropriate,
B, B1, c. oras dicimus, B, B1, c. 3. adaptare quod in patria
sit beatus, post fidei, add. B, B1, c. 6. facto,/ro festo, B, c. 12.
rabido, pro rapido, B, B1, C. enim, pro ergo, b, b1. raciones corr.
ex oraciones, B, B1. 13. contrarias, pro secundarias, b1, c. 18.
esse, 07ii. B, B1, C. 23. resurreccionem et alios, articulos, B, Bl. 28.
est in, pro erit, B, b1, c.
```
