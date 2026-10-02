# LEDGER — source identifications and factual claims

*Every source identification and dated fact in a chunk has a row here (CONVENTIONS §11–12). A chunk
with an open `to-verify` or a `[verify]` tag is not publishable.*

**Status:** `verified` (checked against a text; how and when) · `editor` (the Society editor's own
identification, carried over) · `to-verify` (from memory or secondhand; not yet checked) ·
`untraced` (looked for, not found; the note says so).

| id | chunk / note | claim | status | how / next step |
|---|---|---|---|---|
| V-01 | ecclesia-01a headnote; ecclesia-01-a headnote | *De ecclesia* composed early 1378–early 1379 | verified | SEP "John Wyclif", fetched 2026-09-28 |
| V-02 | ecclesia-01a n16; ecclesia-01-a n13 | Augustine, *Enchiridion* 56 | verified | augustinus.it Latin text, 2026-09-28 |
| V-03 | ecclesia-01a headnote; ecclesia-01-a headnote | Loserth, *Hus und Wiclif: Zur Genesis der hussitischen Lehre* (1884), argued Hus's *De ecclesia* depends on Wyclif's (the pilot had the title as *Wiclif und Hus*) | verified | Loserth's introduction to *De ecclesia* (§1, the English translation printed with the edition): Hus's book "is only a meagre abridgment of Wyclif's 'De Ecclesia'"; the title as Loserth cites it in his own apparatus (sources/ia-ocr/latinworks10wycl.txt l. 23653). Read 2026-10-01 |
| V-04 | ecclesia-01a n32, headnote; ecclesia-01-a headnote | Constance, Hus art. 1 = *Unica est sancta universalis ecclesia, quae est praedestinatorum universitas* | to-verify | Denzinger (DS 1201); check the wording and number |
| V-05 | ecclesia-01a n8; ecclesia-01-a n7 | *credere in Deum* vs *credere ecclesiam*: Rufinus, *Commentarius in symbolum apostolorum* 36 (the pilot had §37) | verified | local PL 21 (`~/patrologia/sources/pl/tei/7119.xml`), §36, col. 373A–B: *in praepositio non additur … sanctam Ecclesiam credendam esse, non ut Deum*; read 2026-10-01 |
| V-06 | ecclesia-01a n18 | "Augustine": the church as *summa creatura* | untraced | Loserth gives nothing. Try the Augustine corpus for *summa creatura* + *ecclesia* |
| V-07 | ecclesia-01a n11; ecclesia-01-a n9 | *APo* I.1 71a11–17; II.1–2 | to-verify | Bekker lines against a text of the *Posterior Analytics* |
| V-08 | ecclesia-01a n22; ecclesia-01-b n6 | Augustine, *De doctrina christiana* III.31.44, III.32.45 (*erit*, *simulato*) | verified | PL 34:82–83 (local PL): *vero atque simulato*; *quod cum illo non erit in aeternum*; Wyclif *manebit* for *erit*. Read 2026-10-01 |
| V-09 | ecclesia-01a n25 | *Tract. in Ioh.* 25.12, *crede, et manducasti* | to-verify | augustinus.it, *In Ioh. ev. tr.* 25–26 |
| V-10 | ecclesia-01a n26 | *Conf.* VII.10.16, *nec tu me in te mutabis* | to-verify | our identification, not Loserth's; check the text |
| V-11 | ecclesia-01a n28 | bestiary lion reviving its cubs on the third day | to-verify | *Physiologus* ch. 1, or a standard bestiary text |
| V-12 | ecclesia-01a n30 | Te Deum, *Te per orbem terrarum sancta confitetur Ecclesia* | verified | standard liturgical text |
| V-13 | dialogus-01 n7 | "Augustine" on the king as vicar of the Godhead (also *Off. reg.* 13) | verified (corrected) | Ps.-Augustine (Ambrosiaster), *Quaestiones Veteris et Novi Testamenti*, local PL TEI 7317.xml (PL 35). q. 91: *Rex enim adoratur in terris quasi vicarius Dei* (PL 35:2284). q. 106: *habens imperium Dei quasi vicarius ejus; quia omnis rex Dei habet imaginem* (PL 35:2319). q. 35: *Dei enim imaginem habet rex, sicut et episcopus Christi* (PL 35:2234). This is exactly the *De officio regis* 13 form (king = image of God, bishop = image of Christ). q. 106 passed into Gratian under Augustine's name: C.33 q.5 c.13 *Vir est caput mulieris*, "Idem in Quaestionibus Veteris et Novi Testamenti … c. 106" (PL 187:1654A, TEI 21354.xml). It is also in Ivo, *Decretum* (PL 161:603D). That circulation explains *sepe meminit Augustinus*. Read 2026-09-29. |
| V-14 | dialogus-01 n10 | Lombard, *Sent.* I d.17: charity = the Holy Spirit | verified | house pilot, `~/wroot-press/sentences` (I d.17) |
| V-15 | dialogus-01 headnote | *Dialogus* written "some time in 1379" | editor | Pollard, intro pp. xvi–xvii (read from OCR, 2026-09-28) |
| V-16 | dialogus-01 headnote | Pollard's sigla B, B¹, C = Vienna 1387 / 3930 / 4505 (order) | verified (corrected) | Pollard, intro pp. xxii–xxiii (OCR `sources/ia-ocr/latinworks22wycl.txt` ll. 879–928): "Vienna, 3930 … Cited as B"; "Vienna, 1387 … Cited as B¹"; "Vienna, 4505 … Cited as C". Also "Vienna, 1338 … Cited as D" (used in the Epilogus). The headnote's order 1387/3930 → B/B¹ is reversed. Read 2026-09-29. |
| V-17 | dialogus-01 headnote | Prague lecture ban 1408; first in 1410 condemnation list | editor | Pollard p. v n. 1, citing Loserth, *Wiclif and Hus* (Eng. ed.) pp. 105, 115 |
| V-18 | both pilots | DR (Challoner) wordings: John 6:54; Jer. 31:3; 1 Cor. 13:8; Prov. 31:10; Isa. 61:10; John 14:6; 8:44 | verified | `scripts/w3/bible.py` DR text for all 7 verses, compared with the quoted wordings in `pilots/wyc-ecclesia-01a.md` (ll. 121, 182–183, 192, 196, 278) and `pilots/wyc-dialogus-01.md` n3 (= chunk 01 n3). All match. The only difference is a trivial comma: the pilot reads "the Son of man, and drink" where DR has "the Son of man and drink". Read 2026-09-29. |
| V-19 | ecclesia-01a headnote; ecclesia-01-a headnote | De ecclesia MSS: A = Vienna 1294, A₁ = Vienna 3929, B = Prague X.D.11, D = TCD C.1.23 (cap. 7 only) | editor | Loserth, intro (read from OCR, 2026-09-28) |
| D02-1 | dialogus-02 n1 | The eagle, gazing at the sun, as a medieval figure of contemplation and of John the Evangelist | verified | Augustine, *Tract. in Ioh.* 36.5 (PL 35:1666, TEI 7323.xml): *Restat aquila: ipse est Joannes, sublimium praedicator, et lucis internae atque aeternae fixis oculis contemplator*, followed by the eaglets held up *radiis solis*. See also 40.1, *aquilae comparatum: nulla quippe avis volare altius perhibetur* (PL 35:1686). Read 2026-09-29. |
| D02-2 | dialogus-02 n3 | Augustine reads the Psalms' *montes* as the great men of the church (apostles, preachers): *En. in Ps.* 71.5, 120.4 | verified | *En. in Ps.* 71.5 (PL 36:903–904, TEI 7329.xml): *Excellenti ergo sanctitate eminentes in Ecclesia, montes sunt; qui idonei sunt et alios docere*. *En. in Ps.* 120.4 (PL 37:1607, TEI 21385.xml): *Jam illuminati sunt montes … Jam ortus est sol justitiae, jam ab Apostolis praedicatum est Evangelium … ipsi montes non a se lucent … Montes possunt intelligi, homines magni*. This matches the Dialogus's *montes* receiving influence from the *sol*. Read 2026-09-29. |
| D02-3 | dialogus-02 n5 | John 10:38 at 5.11 | editor | Pollard's margin reference *John x. 38* (plate n36); text checked with bible.py |
| D03-1 | dialogus-03 n2 | "First commandment of the second table" = Honour thy father and mother; the Augustinian division counts it fourth and Wyclif follows it; Pollard's "fifth" is the Protestant count | verified | Augustine, *Quaest. in Hept.* II.71 (PL 34:620–621, TEI 7312.xml) gives both divisions (4+6, *quorum primum est, Honora patrem et matrem*; or 3+7) and prefers 3+7: *Mihi tamen videtur congruentius accipi tria illa, et ista septem*. Wyclif, *De mandatis divinis* c. 15 (ed. Loserth, p. 152; OCR latinworks17 ll. 13852–13890) speaks of the *tria mandata prime tabule* and notes *Augustinus ponit septem mandata in secunda tabula*. Also c. 12: *iniuriando matri ecclesie contra primum mandatum secunde tabule*, the same application as the Dialogus. Pollard's side-note at p. 6 reads "The fifth commandment" (latinworks22 l. 1515). Read 2026-09-29. |
| D03-2 | dialogus-03 n4 | Truth's voice changes after chapter 3 | editor | Pollard, intro p. vi (as cited in the pilot, n. 3) |
| D03-3 | dialogus-03 n7 | Matt. 21:2 at 7.10 | editor | Pollard's margin reference *Mat. xxi. 2* (plate n38); text checked with bible.py |
| D04-1 | dialogus-04 n2 | *Concessio stulta cesaris* = the imperial endowment; the *Dialogus* calls it *ista stulta donacio* (p. 18) and blames Constantine for it (p. 72) | verified | Read this session in `text/dialogus/p018.la.txt` (*stulta donacio … capitale dominium supra cesarem*) and `p072.la.txt` (*dicitur constantinum anglicum istam vesaniam diabolicam presumpsisse*). Line numbers not yet taken from the plates |
| D05-1 | dialogus-05 n7 | *Pauperes … sacerdotes* anticipates the "poor priests", the preachers associated with Wyclif | verified (corrected) | Pollard, intro pp. xiv–xv (latinworks22 ll. 485–540) quotes this very sentence (p. 10, l. 23 sqq.) and discusses it as a reference to "measures against the 'Poor Priests'". He concludes that the Poor Priests "must have both begun their work, and met with resistance" earlier than supposed. His chronology dates their activity from 1378 (p. xiii n.). His index, s.v. "Poor Priests (pauperes et fideles sacerdotes), persecuted, 10, 23". So the passage *refers to* the poor priests, and "anticipates" is wrong. Read 2026-09-29. |
| D05-2 | dialogus-05 n7 | In canon law the secular arm carried out the church's sentences on heretics | verified | Lucius III, *Ad abolendam* (Verona 1184), PL 201:1298C–1299A (ep. 171, TEI 11606.xml). A convicted cleric *saecularis relinquatur arbitrio potestatis, animadversione debita puniendus*; a layman *saecularis judicis arbitrio relinquatur, debitam recepturus … ultionem*; relapsed heretics *saeculari judicio … decernimus relinquendos*. The X 5.7.9 number was not checked (no Liber Extra locally); the note does not cite it. Read 2026-09-29. |
| D07-1 | 07 / n4 | *pertinaciter*: pertinacity makes error heresy in the canonists' definition (Gratian C.24 q.3 c.31, from Augustine) | verified (corrected) | Gratian, PL 187:1306C–1307B (TEI 21354.xml). The "pertinacity" text is **c.29** (Augustine, ep. 43, inscribed "epist. CLXII"): those who defend a false opinion *nulla pertinaci animositate* … *nequaquam sunt inter haereticos deputandi*. **c.31** (Augustine, inscribed *contra Manichaeos*) gives the positive form: *si correpti … resistunt contumaciter … haeretici fiunt*. The ledger reference should read "C.24 q.3 cc.29, 31". Read 2026-09-29. |
| D08-1 | 08 / n2 | *patrimonium crucifixi* a current name for church goods held by the clergy as stewards of the poor | verified | Phrase attested widely in PL (16 files). Examples: ps.-Bernard, *Ad pastores in synodo* (PL 184:1092B), *abutimini eleemosynis pauperum? De patrimonio Crucifixi non facitis codices…*; Joannes de Deo (canonist), *Poenitentiale* excerpts (PL 99:1107A), clergy who give to hunters and jesters *quam pauperibus de patrimonio Crucifixi … contra ecclesiasticas sanctiones*; Peter of Blois, *Compendium in Job* (PL 207:799A); John of Salisbury, *Epistolae* (PL 199). Read 2026-09-29. |
| D08-2 | 08 / n5 | the "three hundred years" run to the Constantine/Sylvester endowment, treated elsewhere as the poison entering the church | verified | Dialogus p. 16 (`text/dialogus/p016.la.txt`): *lex Christi … per trecentos annos tantummodo observata*. Wyclif, *De potestate pape* c. 9 (ed. Loserth, p. 198; OCR latinworks19 ll. 14524–14540): *hostis antiquus facta per Constantinum hac publica largicione ecclesiis legitur publice in aere proclamasse 'hodie infusum est venenum in ecclesia'* (MS margin: *venenum infusum est in ecclesiam Dei*). The next lines speak of a heretic pope *tercius post Silvestrum*. Read 2026-09-29. |
| D09-1 | 09 / n9 | chief lord's leave for a grant compared with mortmain (Statute of Mortmain 1279) | verified | *Statutum de viris religiosis*, 7 Edw. I (1279), Statutes of the Realm translation via Wikisource "Mortmain Act 1279". The recital: religious men "should not enter into the Fees of any without Licence and Will of the chief Lord, of whom such Fees be holden immediately". On alienation into mortmain, "it shall be lawful to us and other chief Lords of the Fee immediate, to enter into the Land so aliened, within a Year". Read 2026-09-29. |
| D10-1 | 10 / n6 | Augustine: "Si Christus hoc asserit ve illi qui non credit" (20.17) | verified (corrected) | Augustine, *En. in Ps.* 66.1 (PL 36:802, TEI 7329.xml; the TEI lacks a col. 802 anchor, and the passage stands immediately before `<pb n="0803"/>`): *Si ego dico, nemo credat: si Christus dicit, vae qui non credit*. Wyclif quotes freely (*asserit*, *ve illi*). Read 2026-09-29. |
| D11-1 | 11 / n6 | *duo pape … electi* = the double election of 1378 (Urban VI / Clement VII), start of the Great Schism | verified | Dialogus p. 22: *si duo pape ex seminacione sathane electi fuerint … ex tali scismate*. Pollard's chronology, intro p. xiii n. 1 (latinworks22 ll. 455–463): "Protests of Cardinals against Urban's election, July — … Clement VII elected Anti-Pope, Sept. 20". Pollard dates the Dialogus by this "fresh scandal" (pp. xvi–xvii). Nuance: Clement was elected at Fondi and settled at Avignon only in 1379. "Clement VII at Avignon" names his seat and is acceptable. Read 2026-09-29. |
| D12-1 | 12 / n1 (now n2) | *litere fraternitatum* = friars' letters granting lay benefactors a share in the order's prayers | verified | Dialogus p. 23: *literis fraternitatum de suffragio spiritali*. Pollard, index s.v. "Fraternity, letters of (promising their purchasers the prayers of the brother[hood])" and intro p. [x] ("letters of bishops and of fraternity"); latinworks22 ll. 206–208, 9305. Friars: the Dialogus p. 26 (*literas fraternitatum*, sold by those "who do not know whether they are … foreknown") is in the anti-friar context of ch. 13 n7. Read 2026-09-29. |
| D12-2 | 12 / n4 (now n5) | Boethius, "whatever opinion anyone holds is faith to him" | untraced | Searched Boethius in local PL 64 (TEI 7781 *De diff. top.*, 7778 *In Top. Cic.*) for *fides*/*opinio*. Nearest candidate: the definition *Argumentum est ratio rei dubiae faciens fidem* (*De diff. top.* I, PL 64:1174C; *In Top. Cic.* I, PL 64:1156D), where *fides* is the conviction any probable argument produces. *De diff. top.* I (PL 64:1180–81, TEI l. 529ff.) speaks of *fides* resting *in opinione hominum*. Not found as Wyclif's wording. Next: Aquinas / Lombard-commentators on *credere* taken *large* "secundum Boethium" (e.g. Aquinas, *In III Sent.* d.23; *De veritate* q.14 a.1–2); Wyclif's own logic works on *credere*. The note already says "unidentified", so no text change is needed. |
| D12-3 | 12 / n5 (now n6) | the "childish principle" (grant, deny, doubt) = the respondent's rule in *de obligationibus* | verified | Dialogus p. 24: *famosum puerile principium quod omnis proposicio proposita sit concedenda, neganda, vel dubitanda*. Standard reference: Uckelman, Maat & Rybalko, "The Art of Doubting in *Obligationes Parisienses*" (ILLC preprint 2008, eprints.illc.uva.nl/id/document/791), on "the tripartite answering scheme (concede, deny, doubt)" of obligational disputation, with the Latin rules for *dubitatio*. SEP "Medieval Theories of Obligationes" treats grant/deny as the main responses and doubt as a third. Burley's own text was not read (Green's edition is not online); if a primary is wanted, Burley, *De obligationibus*, ed. Green, or Spade's translation. Read 2026-09-29. |
| D13-1 | 13 / n3 | Wyclif dates the loosing of Satan (Apoc. 20:7) to c. 1000 | verified | Wyclif, *De solutione Satanae* c. 1 (Polemical Works, ed. Buddensieg, II p. 395; OCR latinworks29 ll. 988–990): *quod erit post mille annos ad literam post ascensionem domini, tunc sathanas est solutus*. On p. 392 he discusses the friars' "first millennium / second millennium" argument. Dialogus p. 25: *nec in alicujus pape sapiencia antequam satanas est solutus*. Read 2026-09-29. |
| D13-2 | 13 / n6 | a bishop's indulgence limited to 40 days (Lateran IV c. 62) | verified | Lateran IV c. 62 *Cum ex eo* (Schroeder trans., Fordham Medieval Sourcebook, sourcebooks.fordham.edu/basis/lateran4.asp): "on the occasion of the dedication of a church an indulgence of not more than one year be granted … and on the anniversary of the dedication the remission granted for penances enjoined is not to exceed forty days. We command also that in each case this number of days be made the rule in issuing letters of indulgences". Dialogus p. 25: *literis episcopalibus concedentibus 40 dies venie*. (The one-year allowance at a church's dedication is the exception.) Read 2026-09-29. |
| D14-1 | 14 / n7 | Corpus Christi office, 1st nocturn, lesson 2: accidents without a subject | editor | Pollard margin "In primo nocturno, Lectio II."; wording to-verify against the breviary |
| D14-2 | 14 / n8 | Aug., *De serm. Dom. in monte* I.20.65: the apocryphal story of Thomas, the servant and the dog | verified | Augustine, *De sermone Domini in monte* I.20.65 (cap. XX begins at §62), PL 34:1262–1263 (TEI 7307.xml): *in illis libris … ubi scriptum est apostolum Thomam imprecatum cuidam, a quo palma percussus esset … cujus a leone occisi … discerptam manum canis intulit mensis in quibus convivabatur Apostolus. Cui scripturae licet nobis non credere; non est enim in catholico canone*. This matches the note. Augustine tells the same story in *Contra Adimantum* 17.2 (PL 42:158, TEI 21356.xml). Read 2026-09-29. |
| D15-1 | 15 / n8 | Cyprian "si solus Christus" = *Ad Caecilium* §14 (Ep. 63), cited through Gratian D.8 (B, B¹, C "decimo capitulo") | verified | Cyprian, Ep. 63 *Ad Caecilium* §14, PL 4:385A (TEI 130.xml; the heading reads "EPISTOLA LXIII … AD CAECILIUM", with Erasmus's numbering II, 3): *Quare, si solus Christus audiendus est, non debemus attendere…*. Gratian, D.8 **c.9** *Dei veritatem, non hominum consuetudinem sequi oportet*, "Idem lib. II, ep. 3, ad Caecilium", PL 187:48B (TEI 21354.xml). In PL 187 the text before c.9 is an unnumbered excerpt, *Idem in epistola ad Jubaianum*. A count that treats it as a separate chapter makes *Si solus* the tenth, which explains the MSS' *decimo capitulo* and Pollard's supplement [*decimo*]. The note gives no canon number, so no change is needed. If one is wanted: D.8 c.9 (PL 187:48B). Read 2026-09-29. |
| D15-2 | 15 / n10 | Possidius, *Vita Augustini*: Augustine willing to give Hippo's possessions back to its citizens | verified (corrected) | Possidius, *Vita Augustini* c. 23, PL 32:53 (TEI 7297.xml): *paratum se esse illis cedere … Sed nunquam id laici suscipere voluerunt*. Wyclif tells the story again in the Epilogue, Pollard p. 88 (latinworks22 ll. 6878–6886), where Pollard's margin reads "Possidius Vita Aug. c 23". The note has no chapter; add "23". Read 2026-09-29. |
| D15-3 | 15 / n10 | Jerome refusing possessions, life outside the cloister, clerical estates | untraced | Pollard gives no reference at p. 31 (latinworks22 ll. 3370–3380). *extraclaustral-* occurs nowhere else in the Wyclif OCR. The nearest Jerome texts, read in PL 22 (TEI 7132.xml): Ep. 52.5 to Nepotian, where the cleric whose portion is the Lord *nihil extra Dominum habere potest … si possessiones … Dominus pars ejus fieri non dignabitur* (PL 22:531); and Ep. 58.5 to Paulinus, *Sin autem cupis esse … Monachus, id est, solus, quid facis in urbibus?* (PL 22:582–583). No text found in which Jerome himself refuses possessions. The claim is probably Wyclif's own summary of these letters. Next: Wyclif, *De civili dominio* and *De ecclesia* on Jerome; Gratian C.12 q.1 (Jerome excerpts). The note should say it is untraced (see the D15-2 correction). |
| D17-1 | 17 / n1 | "fourth commandment" = honour father and mother (Exod. 20:12) in the Augustinian count | verified | Augustine, *Quaest. in Hept.* II.71, PL 34:620–621 (TEI 7312.xml), gives both divisions and prefers 3 + 7 (*Mihi tamen videtur congruentius accipi tria illa, et ista septem*). On that count *Honora patrem et matrem*, the first of the second table, is the fourth. Wyclif follows it: *De mandatis divinis* c. 22 opens *redeundum est ad primum mandatum secunde tabule, quod est: Honora patrem tuum et matrem tuam* (latinworks17 ll. 25112–25115). The Dialogus text reads *ex quarto mandato decalogi* (p. 33). Exod. 20:12 checked with bible.py. Read 2026-09-29. |
| D19-1 | 19 / n1 | *quatuor sectas cleri* = endowed secular clergy, monks, canons, friars | verified | Wyclif, *De quattuor sectis novellis* c. 1 (Polemical Works I, ed. Buddensieg, p. 243; latinworks28 ll. 18745–18790): *Sacerdos autem cesareus … intelliguntur … dotati presbiteri, quicunque seculares clerici … dotati*. The MS marginal note there reads *Secte quatuor: Sacerdos cesareus, Monachus, Canonicus, Frater*. See also *De Christo et suo adversario Antichristo* c. 2 (Pol. Works II p. 656; latinworks29 ll. 12879–12887): *Sunt autem iste secte quatuor, ut sepe dictum est, clerus cesareus, monachi, canonici atque fratres*. That text says the Caesarean clergy's *patronus* is the pope, which fits the Dialogus's *curie romane* (p. 37). Read 2026-09-29. |
| D19-2 | 19 / n1 | *quatuor sectas fratrum* = Franciscans, Dominicans, Carmelites, Austin friars | verified | Pollard, index (latinworks22 ll. 9339–9342): "Friars, the four sects of (Carmelites, Augustinians, Jacobites or Dominicans, and Franciscans), 37, 27; 48, 6". Here 37, 27 is this very passage. His index s.v. CAIM (ll. 8912–8920) quotes Wyclif, *Trialogus* IV.33: *C. Carmelitas, A. Augustinenses, I. Iacobitas et M. Minores significat*. Buddensieg quotes the same passage (latinworks28 ll. 8550–8556). Read 2026-09-29. |
| D20-1 | 20 / n1 | black canons = Augustinian, white = Premonstratensian; *boni homines* = the English Bonshommes | verified | Pollard gives nothing. *Catholic Encyclopedia*, "Canons and Canonesses Regular" (newadvent.org/cathen/03288a.htm): "AUGUSTINIAN CANONS, BLACK CANONS"; "The Premonstratensians wear a white habit". VCH Derbs. II, Beauchief (british-history.ac.uk/vch/derbs/vol2/pp63-69): "for Premonstratensian or White Canons". VCH Bucks. I, Ashridge (british-history.ac.uk/vch/bucks/vol1/pp386-390): "The College of Bonhommes at Ashridge, was founded in 1283 … It was the only house of this order in England, except the small college at Edington in Wiltshire". The brethren were professed to the rule of St Augustine. VCH Wilts. III, Edington (…/vch/wilts/vol3/pp320-324): converted into a house of Bonhommes in March 1358. Fetched 2026-09-29. |
| D20-2 | 20 / n5 | *istas 8 species* = the eight kinds of religious listed at 39.4–8 | verified | Pollard pp. 39–40 (latinworks22 ll. 3918–3992). The list at 39.4–8 runs: *canonici regulares, nigri* (1) *et albi* (2); *fratres hospitales* (3); *monachi cartusienses* (4); *fratres boni homines* (5); *sanctimoniales* (6); *sororisse* (7); *cum anacoritis et ceteris inclusis* (8). That makes exactly eight if black and white canons count separately and anchorites and other recluses count as one class, as *ceteris* suggests. The note's hedge ("does not count out to eight unambiguously") is fair but could be replaced by this count. p. 40 l. 1: *per istas 8 species*. Read 2026-09-29. |
| D20-3 | 20 / n6 | John 8:46 | editor | Pollard margin; text via bible.py |
| D20-4 | 20 / n7 | the church's three parts = the three estates | verified | Dialogus cap. 1, p. 2 (`text/dialogus/p002.la.txt`): *Dividebam autem meam militantem ecclesiam in tres partes quarum prima foret clerus meus … Secunda pars … forent domini temporales … Tercia autem pars militantis ecclesie sunt vulgares*. The same point recurs at p. 3 (*has tres partes … Media autem pars que est domini temporales*). p. 40 (*sectam unicam militantem et ipsam habere tres partes*) refers back to it. Read 2026-09-29. |
| D21-1 | 21 / n1 | *Regula quam fecit papa gregorius*: Gregory I (Dial. II, life of Benedict), credited by Wyclif with the monks' rule | verified (corrected) | Pollard, index: "Gregory the Great … his rule, 41, 16; 42, 26" (latinworks22 ll. 9362–9364). Wyclif makes the same ascription elsewhere, *De Christo et suo adversario Antichristo* c. 2 (Pol. Works II p. 656; latinworks29 ll. 12883–12885): *Secunda secta dicitur esse monachi … cuius patronus dicitur esse Benedictus, et regula, quam ex eius sentencia beatus Gregorius compilavit*. So the identification is Wyclif's own, and "presumably" can go. Read 2026-09-29. |
| D23-1 | 23 / n9 | *justorum sunt omnia* ← Augustine, Ep. 93 | verified (corrected) | Augustine, Ep. 93.12.50 (to Vincentius), PL 33:345 (TEI 7300.xml; the heading reads "EPISTOLA XCIII"): *res quaeque terrena non recte a quoquam possideri possit, nisi vel jure divino, quo cuncta justorum sunt, vel jure humano*. Replace "(from memory)" with the reference. Read 2026-09-29. |
| D23-2 | 23 / n10 | Prov. 1:28, Isa. 1:11–15, Mal. 1:7–8 | editor | Pollard margin 47.26–28 |
| D23-3 | 23 / n11 | Gregory, *Reg. past.* I.10 | editor | Pollard margin 47.29 |
| D23-4 | 23 / n11 | Gratian C.3 q.7, *Si quis in gravibus* | verified (corrected) | Gratian, C.3 q.7 **c.5** *Gravatus criminibus judicare non valet*, inscribed "Gregorius praefationis in Job", PL 187:694A (TEI 21354.xml; Causa III at l. 27157, q. VII at l. 28185). Incipit: *In gravibus peccatis quis positus, dum suis premitur, aliena non diluit. § 1. Cuncti enim liquido novimus, quia, quum is displicet, qui ad intercedendum mittitur, irati animus proculdubio ad deteriora provocatur*. This is the same Gregory sentence the Dialogus has just quoted (relevant to D23-3). The canon's incipit is *In gravibus*; Wyclif's *si quis* is loose. Read 2026-09-29. |
| D23-5 | 23 / n12 | Augustine, *En. in Ps.* 148.2 (paraphrase + *vinolencia*) | verified (corrected) | The quotation is **146.2**, not 148.2. *En. in Ps.* 146.2, PL 37:1899–1900 (TEI 21385.xml; the heading "IN PSALMUM CXLVI" at l. 61342) reads: *et cibus tuus et potus tuus laudat Deum: si vero modum naturae debitum immoderatione voracitatis excedas, et vinolentia te ingurgites; quantaslibet laudes Dei lingua tua sonet, vita blasphemat*. The preceding sentences give the paraphrase (praise by works; *opere tuo laudas Deum*). *En. in Ps.* 148.2 (PL 37:1938) makes the same general point (*Non cesset bene vivere, et semper laudat Deum … lingua tua tacet, vita tua clamat*) but has no *vinolentia* sentence. Read 2026-09-29. |
| D23-6 | 23 / n13 | "four sects" = Wyclif's usual count of the orders | verified (corrected) | Pollard indexes this passage (*plures oratores de hiis sectis 4or*, p. 48 l. 6) under "Friars, the four sects of (Carmelites, Augustinians, Jacobites or Dominicans, and Franciscans), 37, 27; 48, 6" (latinworks22 ll. 9339–9342). Wyclif's usual "four sects" (*ut sepe dictum est*) are the Caesarean clergy, monks, canons and friars (*De Christo et suo adversario Antichristo* c. 2; *De quattuor sectis novellis* c. 1; see D19-1). The note's "count of the orders" is ambiguous between the two readings; name both. Read 2026-09-29. |
| D24-1 | 24 / n5 | *dotacione ecclesie presumpta per cesarem* (49.17) = Constantine's endowment | verified | Dialogus p. 49: *cum hoc nomen papa sit terminus extra fidem scripture, videtur quod in dotacione ecclesie presumpta per cesarem est inventum*. p. 72 uses the same verb of Constantine: *dicitur constantinum anglicum istam vesaniam diabolicam presumpsisse*. See also p. 18 *stulta donacio* (D04-1). Pollard's intro p. xiv (latinworks22 ll. 648–654) discusses p. 49 and notes that the Pope's pre-eminence "is traced to the interference of Constantine (pp. 82, 83)". His index, s.v. "Constantine, Donation of, 63, 12; 72, 14". Read 2026-09-29. |
| D26-1 | 26 / n2 | Falsehood's eucharistic "heresy" (53.19–20) = the controversy in which Wyclif's teaching was condemned at Oxford, 1381 | verified (corrected) | Pollard, intro p. vi (latinworks22 ll. 121–125): Mendacium "is content to use such very Wyclifite language as *ut patet de heresi in eucharistia et aliis similibus que in fine temporum diabolus spissius seminavit*". So Pollard reads the "heresy" as the doctrine Wyclif calls heresy: the host as *accidens … sine subjecto*, which Truth names at 54.23–25 (*ut reserant nove secte*). Pollard pp. xix–xx (ll. 721–803) calls p. 53 l. 19 an "unimportant reference" and dates the *Dialogus* to 1379. It therefore predates the Oxford condemnation by Chancellor William Berton's council. Pollard p. xix n. 1 even doubts the *Fasciculi zizaniorum* date of summer 1381 for the twelve theses, noting the Confessio heading altered to 1380. So the note cannot be right that Falsehood refers to the condemnation of 1381. At most, read in character, he refers to Wyclif's teaching, already in dispute. Replacement text is below. Read 2026-09-29. |
| D29-1 | 29 / n1 | *in manum mortuam* = mortmain; land to the church only by licence (Statute of Mortmain 1279) | verified | *Statutum de viris religiosis*, 7 Edw. I (1279), Statutes of the Realm translation (Wikisource "Mortmain Act 1279 (unsourced)"). It recites that religious men "should not enter into the Fees of any without Licence and Will of the chief Lord". It enacts that no one "buy or sell any Lands or Tenements … whereby such Lands or Tenements may any wise come into Mortmain", under pain of forfeiture. The statute forbids alienation outright; licensing was the practice that followed. That practice is the subject of P. Brand, "The Mortmain Licensing System, 1280–1307" (title and abstract seen, not read). "Only by licence" is therefore right in substance. Fetched 2026-09-29. |
| D30-1 | 30 / n6 | *castra caynitica* = "Caim's castles", CAIM the initials of the four mendicant orders | verified | Pollard, index s.v. "Castra caynitica, of the friars' houses … 65, 11" (latinworks22 ll. 8903–8920). He suggests the true reading is *Caimitica* and quotes Wyclif, *Trialogus* IV.33: *Alii autem fingunt quod in Caym fuerunt istae sectae quattuor inchoatae. Et in testimonium istorum quattuor litterae huius nominis Caim inchoant hos quattuor ordines … ita quod C. Carmelitas, A. Augustinenses, I. Iacobitas et M. Minores significat*. Pollard's side-note 65.12 reads "'Caim's Castles'". *Trialogus* (ed. Lechler) itself was not read; the passage is Pollard's verbatim quotation. Optional improvement: the note could add "(Wyclif, *Trialogus* IV.33, quoted by Pollard, index s.v. *Castra*)". Read 2026-09-29. |
| D30-2 | 30 / n20 | an English king seized a bishop's goods for keeping royal office instead of residing | untraced | Pollard does not identify it. His side-note 68.14 says only "according to the precedent of an English king", and his index has only "Confiscation of Endowments, 68, 14". Searched all 33 Wyclif Society OCR volumes for *confiscass-/confiscavit* (only this passage) and for Winchester/Wykeham (nothing relevant). Wykeham (temporalities seized Nov. 1376; convocation of Feb. 1377 resisted) fits *cum cleri repugnancia* but not the stated ground, non-residence while in royal office. Stratford (1340–1) fits neither well. Next: Wyclif's *De officio regis* and *De civili dominio* on "Caesarean clergy"; ODNB Wykeham; Holmes, *The Good Parliament*. The note already says "not identified", so no change is needed. |
| D30-3 | 30 / n22 | John XXII, *Cum inter nonnullos* (1323), against the absolute poverty of Christ | verified | Latin text, Franciscan Archive (franciscan-archive.org/bullarium/qinn-l.html): *assertionem huiusmodi pertinacem … erroneam fore censendam et haereticam*, i.e. the assertion that Christ and the apostles had nothing *in speciali* or *in communi*. Dated *II Idus Novembris* 1323 (12 Nov.). Extrav. Ioann. XXII tit. 14 c. 4/5 *De verborum significatione*. Read 2026-09-29. |
| D31-1 | 31 / n2 | Ireland to Henry II; Spain to Henry of Trastámara | editor | Pollard side-note 70.1 |
| D31-2 | 31 / n12 | "Augustine": king = vicar of the Godhead, priest = vicar of Christ's humanity | verified (corrected) | Same source as V-13 (ch. 01 n7), confirmed against the ch. 31 wording. Ambrosiaster, *Quaest. VNT*, local TEI 7317.xml (PL 35). q. 35: *Dei enim imaginem habet rex, sicut et episcopus Christi* (PL 35:2234). q. 106: *habens imperium Dei quasi vicarius ejus; quia omnis rex Dei habet imaginem* (PL 35:2319). q. 91: *Rex enim adoratur in terris quasi vicarius Dei* (PL 35:2284). Gratian C.33 q.5 c.13 carries q. 106 under Augustine's name (V-13). Ch. 01 (Pollard p. 4, latinworks22 ll. 1212–1222) gives the same pairing: *sepe meminit augustinus quomodo rex est vicarius deitatis. Sacerdos autem … vicarius humanitatis domini jhu Christi*. Ambrosiaster pairs king/God with bishop/Christ; the "humanity" is Wyclif's sharpening. Remove "probably" and cite as in ch. 01 n7. Read 2026-09-29. |
| D31-3 | 31 / n14 | English Constantine = Constantine the Great, British-born in legend | verified | Geoffrey of Monmouth, *Historia regum Britanniae* V.6–7 (Giles trans., *Six Old English Chronicles*, en.wikisource "Geoffrey's British History/Book 5"). After Coel's death Constantius became king and "married the daughter of Coel, whose name was Helena"; their son Constantine was born of this marriage. Constantius "died at York, and bestowed the kingdom upon his son". V.8: Constantine takes Rome and the empire. Pollard's index lists 72.14 (this line) under "Constantine, Donation of". Latin text not read; the translation was. Read 2026-09-29. |
| D31-4 | 31 / n15 | "half the empire" = the Donation of Constantine | verified | *Constitutum Constantini* in Gratian D.96 c.14 (Palea), PL 187:464A–B (TEI 21354.xml): *tam palatium nostrum … quam Romanam urbem, et omnes Italiae seu occidentalium regionum provincias … Silvestro universali Papae contradimus atque relinquimus*. § 7: the emperor moves his own rule *in orientalibus … regionibus* to Byzantium. So the West went to the pope and the East stayed with the emperor: half the empire. Also D.96 c.13: *coronam, et omnem regiam dignitatem in urbe Romana, et in Italia, et in partibus occidentalibus Apostolico concessit*. Pollard, index s.v. "Constantine, Donation of, … 72, 14" (the same passage, 72.14–22). Read 2026-09-29. |
| D31-5 | 31 / n16 | King John's tribute of 1,000 marks, withheld from 1366 | verified (corrected) | 1,000 marks is correct: John's concession, 15 May 1213 (Henderson, *Select Historical Documents* pp. 430–431, via Fordham Medieval Sourcebook source/john1a.asp). The Roman church is to receive "yearly a thousand marks sterling … seven hundred, namely, for the kingdom of England, and three hundred for the kingdom of Ireland". "Withheld from 1366" is wrong: payment had already lapsed about 1333. In 1366 Urban V demanded the arrears ("thirty-three years in arrear") and Parliament refused and repudiated the tribute (*Catholic Encyclopedia*, "Edward III", newadvent.org/cathen/05321a.htm). Rot. Parl. ii (40 Edw. III) not read; if a primary is wanted, read it there. Pollard, index s.v. "Edward III, detention of pope's tribute in reign of, 72, 29". Read 2026-09-29. |
| D32-1 | 32 / n7 | Augustine asks Hippo to take back estates: Possidius, *Vita Aug.* 23 | editor | Pollard margin 75.20 (with D15-2) |
| D32-2 | 32 / n15 | *clerus* from κλῆρος "lot" (Jerome, Ep. 52.5) | verified | Jerome, Ep. 52 *Ad Nepotianum* c. 5, PL 22:531 (TEI 7132.xml): *Si enim κλῆρος Graece, sors Latine appellatur: propterea vocantur Clerici, vel quia de sorte sunt Domini, vel quia ipse Dominus sors, id est, pars Clericorum est*. The passage also stands in Gratian C.12 q.1 c.5 (PL 187:884A) and Isidore, *De eccl. off.* II.1. The chunk note itself does not cite Jerome; nothing needs changing. Read 2026-09-29. |
| D35-1 | 35 / n4 | *medietatem imperii* (83.2) = the Donation of Constantine | verified | As D31-4 (Gratian D.96 c.14, PL 187:464A–B). The context confirms it: Pollard p. 83 (latinworks22 ll. 7555–7562), *qui habet … potestatem a petro scit optime regere romam et medietatem imperii*, where "Rome and half the empire" answers the Constitutum's *Romanam urbem et omnes … occidentalium regionum provincias*. Read 2026-09-29. |
| D35-2 | 35 / n4 | *patrimonium crucifixi* plays on "patrimony of St Peter" | verified (corrected) | The papal lands were called "patrimony of St Peter": Paschal II, *Ep.*, PL 163:423C (TEI 10794.xml), *patrimonium beati Petri, quae potuit occupavit*; also the Alexandrine cardinals to Frederick I (TEI 11591.xml). *Patrimonium crucifixi* is not Wyclif's coinage, though. D08-1 found it current for church goods held for the poor (ps.-Bernard PL 184:1092B, Peter of Blois PL 207:799A). Wyclif's point (83.3–5) is that papal lordship is called *patrimonium crucifixi* "as if by hereditary right". The note's "turns the name … onto the crucified Christ" credits him with the substitution. Reword. Read 2026-09-29. |
| DEA-1 | epil-a / n8 | the devil sent Pilate's wife's dream | verified | Paschasius Radbertus, *Expositio in Matthaeum* XII, PL 120:937D–938A (TEI 9114.xml): *nonnulli dicunt hanc visionem a diabolo immissam, et ab eo ipsam flagellatam, sentiens jam forte passione Christi se superari, ac mundum salvari. Idcirco egerit arte sua ut Christus liberaretur per mulierem*. It then gives the alternative view, *Alii vero dicunt bonitate Dei factum fuisse*. This is exactly Wyclif's reading, the devil fearing the Passion would save the faithful. Read 2026-09-29. |
| DEA-2 | epil-a / n10 | the king revokes grants made in his minority | untraced | The minority rule was not traced to a text. The context is **prescription** (*sic non potest currere efficax et salubris prescripcio coram deo. Quia ut dicunt de privilegiis regis Anglie, quod sit semper iuxta etatem potens iustificare iniuriam prius factam*). That points first to the royal privilege that time does not run against the king: Bracton, *De legibus*, ed. Woodbine–Thorne ii. 58 (amesfoundation.law.harvard.edu, Latin v2 p. 58), *nec in primo casu nec in isto currit tempus contra regem* (royal franchises such as wreck and treasure). *Iuxta etatem* stays obscure: "at every age"? or the nonage rule? Next: Henry III's 1227 declaration voiding charters issued in his minority (Roger of Wendover s.a. 1227). A note revision is recommended (see below). Read 2026-09-29. |
| DEA-3 | epil-a / n12 | Aristotle, *Eth.* VI.2, Agathon | verified | *EN* VI.2, 1139b8–11 (Perseus canonical-greekLit tlg0086.tlg010.perseus-grc2): *τὸ δὲ γεγονὸς οὐκ ἐνδέχεται μὴ γενέσθαι· διὸ ὀρθῶς Ἀγάθων· μόνου γὰρ αὐτοῦ καὶ θεὸς στερίσκεται, ἀγένητα ποιεῖν ἅσσʼ ἂν ᾖ πεπραγμένα*. The verse begins at Bekker line 10, so "1139b10" is right. Read 2026-09-29. |
| DEA-4 | epil-a / n14–15 | Magna Carta c.1, coronation oath, excommunications, Becket | verified | (1) Magna Carta 1297 c. 1 (legislation.gov.uk aep/Edw1cc1929/25/9/section/I): "the Church of England shall be free, and shall have all her whole Rights and Liberties inviolable". (2) Coronation oath of 1308 (text via thehistoryofengland.co.uk, no edition named; standard text Statutes of the Realm i. 168): "preserve to God and Holy Church … entire peace" and the "liberties granted to the clergy and people by … the sainted Edward". (3) Excommunication of infringers: *Confirmatio Cartarum* 1297 c. 4 (constitution.org): "all archbishops and bishops shall pronounce the sentence of excommunication against all those that … do contrary to the foresaid charters", published twice yearly. The "beyond the sea" sentences (papal) were not separately traced. (4) Becket: Alexander III to Thomas, praising the constancy *quem pro libertate Ecclesiae tuae conservanda induisse dignosceris* (Ep. 772, PL 200:710C, TEI 11589.xml). His canonization bull *Redolet Anglia* (PL 200:901D–902A) speaks of his *martyrio*. Read 2026-09-29. |
| DEA-5 | epil-a / n16 | Solomon / Abiathar, 1 Kings 2:27 | editor | Pollard margin (print "3 Reg. 3°"; the story is ch. 2) |
| DEA-6 | epil-a / n18 | mortmain licence | verified | Rests on the reading of the Statute of Mortmain done for D09-1 and D29-1 (7 Edw. I, 1279, Statutes of the Realm translation). The recital requires the "Licence and Will of the chief Lord". The enacting clause forbids alienation into mortmain outright, and royal licensing was the practice that followed. So "required the king's licence" is right in substance, with the same nuance recorded in D29-1. The note's "probably" is appropriately hedged. Not re-read this batch (per instructions); cross-checked 2026-09-29. |
| DEA-7 | epil-a / n28 | *Metaph.* X.1, the measure of a genus | verified | *Metaph.* X (Iota).1, 1052b18–24 (Perseus canonical-greekLit tlg0086.tlg025, Tredennick trans.): "to be one means … especially to be the first measure of each kind [γένους], and above all of quantity; for it is from this that it has been extended to the other categories. Measure is that by which quantity is known". The schoolmen's *primum in unoquoque genere est mensura omnium* rests on this text. Read 2026-09-29. |
| DEA-8 | epil-a / n32 | Averroes: truth self-consonant; truth rubbed, fragrant | untraced | The Aristotle cross-reference is confirmed: *EN* I.8, 1098b11–12, *τῷ μὲν γὰρ ἀληθεῖ πάντα συνᾴδει τὰ ὑπάρχοντα* (Perseus grc2). *APr.* I.32 (47a8) was not read; no text was reachable. No Averroes locus found. Wyclif uses the same dictum without naming Averroes: *veritas secundum philosophos testatur sibi ipsi omnibus modis* (*Sermones* I, latinworks30 l. 5982; also latinworks27 l. 18772, latinworks32 l. 38550), and Loserth gives no source. A web search reports a Wyclif *Trialogus* instance naming Averroes (not seen). The "rubbed truth grows fragrant" figure was not found in PL (searched *fricat-* near *redolet/fragr-/odor*). Next: Averroes, *In Ethic.* I (Latin, Juntine vol. 3), comment on 1098b11; *Trialogus* (Lechler). The note's "cf." wording already hedges it, so no change is needed. |
| DEB-1 | epil-b / n9 | *stultorum infinitus est numerus* = Eccl. 1:15 | editor | Pollard margin |
| DEB-2 | epil-b / n10 | "Tersites numerum auxit…", *de bello clavo* | untraced | Pollard's apparatus (latinworks22 l. 8430) gives *tersites* C, *sersites* B¹, and the index has only "Thersites, 94, 28". No hit for *numerum auxit* + Thersites in PL (the only hit is William of Tyre, unrelated) or in the Wyclif Society OCR. Dziewicki on *De apostasia* p. 195 (latinworks01 ll. 19061, 19122) notes another Thersites allusion (*prelati apponuntur ad augendum numerum, ut tersites*) and calls Thersites "a general scholastic term for anything worthless". The *Ilias Latina* was not checked (the Latin Library page did not load). Next: Walther, *Proverbia sententiaeque*; *Ilias Latina*; Joseph of Exeter, *De bello Troiano* (*clavo* may be a corruption of *troiano*?). The note already says "not identified", so no change is needed. |
| E01b-1 | ecclesia-01-b / n20 | Augustine, *Enarr. in Ps.* 131 (Maurist *Opp.* IV.2, 1477) | verified | PL 37:1721–22, §13: *Ille enim ad domum Dei pertinet … compaginatus lapidibus vivis* |
| E01b-2 | ecclesia-01-b / n23; 01-c / n2 | Augustine, *Enarr. in Ps.* 131 (*Itaque … domus Dei*; *Ne aliquis minaretur*) | verified | PL 37:1722 §13 (*Itaque, fratres, in his est domus Dei …*; Augustine reads *pedes*, not *sedes*); PL 37:1725 §20 (*Sed ne aliquis quasi minaretur*). Loserth's Maurist p. 1480 fits §20 (inference) |
| E01c-1 | ecclesia-01-c / n1 | David = "strong of hand" (Jerome, *Liber interpretationis hebraicorum nominum*) | verified | PL 23:847A: *David, desiderabilis, sive manu fortis* (also 23:840, 855) |
| E01c-2 | ecclesia-01-c / n3 | *Tota ecclesia una vidua est*: Augustine on Ps. 131:15 | verified | PL 37:1726, §23: *Ergo tota Ecclesia una vidua est* |
| E01c-3 | ecclesia-01-c / n4 | Augustine, *Enarr. in Ps.* 120 (Maurist *Opp.* IV, 1381) | verified | PL 37:1615, §12: *Quisquis rursus putaverit Ecclesiam in una parte esse … a luna uritur* |
| E01c-4 | ecclesia-01-c / n6 | *Ipsa caro Christi est caput ecclesie*: Augustine | verified | PL 37:1615, *Enarr.* 120.12 (same passage as n4): *quia ipsa caro Christi caput Ecclesiae est* |
| E01c-5 | ecclesia-01-c / n7, n17; 01-d / n8 | *Unam sanctam* = *Extrav. comm.* 1.8.1; the wordings quoted | verified | Friedberg II, 1245–46 (archive.org BD1141952), read 2026-10-02; Wyclif omits *et unicae* and paraphrases *nec … nec* |
| E01c-6 | ecclesia-01-c / n9 | Aristotle, *De caelo* I.1, 268a ("all" of three) | editor | Loserth; *Phys.* III.6, 207a (*totum … perfectum*) to-verify |
| E01c-7 | ecclesia-01-c / n10 | triple fraction: Amalarius; Gratian, *De cons.* D.2 c.22 *Triforme* | to-verify | Gratian verified: PL 187:1740A, *Triforme est corpus Domini* (inscribed Sergius papa). Amalarius not checked |
| E01c-8 | ecclesia-01-c / n16 | Decr. C.24 q.1 c.5; Leo I, *Serm.* 4.3 | verified | Gratian PL 187:1266C–1267A; Leo *Serm.* IV (al. III) 3, PL 54:151A–B: *Manet ergo Petri privilegium …* |
| E01c-9 | ecclesia-01-c / n19 | Augustine, *Enarr.* II in Ps. 21 (Maurist *Opp.* IV, 98) | verified | PL 36:176, §21: *latrant caecis oculis*; *contra viantes*, *licet velint eis proficere* are Wyclif's |
| E01d-1 | ecclesia-01-d / n12 | Decr. C.23 q.7 c.4, from Augustine, *De correctione Donatistarum* (*Ep.* 185) 9.42 (the agent had *Ep.* 93) | verified | Gratian PL 187:1244C; Augustine PL 33:811 §42: *Quemadmodum enim membrum si praecidatur ab hominis vivi corpore …* (coordinator re-read) |
| E01d-2 | ecclesia-01-d / n13 | Decr. C.24 q.1 c.27, Bede homily on Matt. 16 | verified | Gratian PL 187:1278B–C; Bede *Hom.* XVI in natale Petri et Pauli, PL 94:223B (*illius* for Gratian's *Petri apostoli*) |
| E01d-3 | ecclesia-01-d / n14 | Decr. C.24 q.1 c.24; the words are 2 John 9 | verified | Gratian PL 187:1275C–1276A (*Beda super epistolam Joannis secundam*); Bede *In II Ioh.* PL 93:122A–B, *Filium et Patrem* |
| E01d-4 | ecclesia-01-d / n19 | Bernard, *De consideratione* IV.3.7 (Wyclif says book II) | verified | PL 182:776B–C, IV.3 §7: *Uterque ergo Ecclesiae … gladius* |
| E01d-5 | ecclesia-01-d / n20 | Decr. C.23 q.5 c.20 *Principes*; Isidore, *Sententiae* III.51.4 | verified | Gratian PL 187:1223C–1224A (inscribed *lib. III Sent. … c. 55*); Isidore PL 83:723B |
| E01d-6 | ecclesia-01-d / n22 | Johannes de Deo, canonist at Bologna | editor | Loserth, citing *Trialogus* ed. Lechler p. 251 |
| E01e-1 | ecclesia-01-e / n1 | last sentence of *Unam sanctam*, *humanae creaturae* | verified | Friedberg II, 1245–46 (archive.org BD1141952), read 2026-10-02 |
| E01e-2 | ecclesia-01-e / n5 | *Bellus Mons* = Beaumont palace, north suburb of Oxford | editor | Loserth, after Wood |
| E01e-3 | ecclesia-01-e / n6 | Gratian D.22 c.2 *Sacrosancta* | verified | PL 187:123A: names Rome, Antioch, Alexandria; Constantinople in the dictum and cc. 3–4; Jerusalem not there |
| E01e-4 | ecclesia-01-e / n12 | *derelictum* also in Hus, *De eccl.*, Opp. I fol. 208 | editor | Loserth p. 16 |
| E01f-1 | ecclesia-01-f / n9 | Augustine, *Sermo* 9, §§3 and 11 (Loserth's "9" = §11) | verified | PL 38:77, 83–84 |
| E01f-2 | ecclesia-01-f / n10 | *Dole … precipucium*, abridged from *Sermo* 9.11 | verified | PL 38:83–84: *Dole; sed ipsum noli imitari … eunt ambo per praeceps* |
| E01g-1 | ecclesia-01-g / n4 | Gregory, *Moralia* XXIII.1.2 | verified | PL 76:251C–D |
| E01g-2 | ecclesia-01-g / n4 | quotation wording; Gregory *cum sancta Ecclesia* | verified | PL 76:251C–D; Wyclif *cum sua* |
| E01g-3 | ecclesia-01-g / n5 | *Mor.* XIX.9 and IV.9 (Wyclif) | untraced | not at those places; doctrine at XIX.14.22, PL 76:110C |
| E01g-4 | ecclesia-01-g / n6 | *Unam sanctam*: *non duo capita, quasi monstrum* | verified | Friedberg II, 1245–46 (archive.org BD1141952), read 2026-10-02 |
| E01g-5 | ecclesia-01-g / n8 | FitzRalph, *Summa de quaestionibus Armenorum* VII.6 | editor | person Loserth p. 21; book/chapter to-verify |
| E01h-1 | ecclesia-01-h / n3 | *Moralia* XIX.12 (Maurist; Wyclif cap. 8) | verified | PL 76:108A |
| E01h-2 | ecclesia-01-h / n4 | *Universe quippe … adolescentule vocantur* | verified | PL 76:108B, wording identical |
| E01h-3 | ecclesia-01-h / n5 | lion and lioness = *Mor.* XVIII.35.56 (Wyclif XXVIII.11 wrong) | verified | PL 76:68C–69A (coordinator re-read 68D) |
| E01h-4 | ecclesia-01-h / n9, n10 | Gregory, *Hom. in Ev.* I.19 (vineyard, Matt. 20); the "mouth" = *Mor.* XVIII.35.56 | verified | PL 76:1154B; 76:68D. Job as "mouth" untraced |
| E01h-5 | ecclesia-01-h / n11 | *Moralia* IV: patriarchs' virtues | to-verify | nearest found: Preface 6.13, PL 75:524B–C (lacks David, Elijah); Book IV not searched in full |
| E01h-6 | ecclesia-01-h / n18 | Hus, *De eccl.* capp. 1–3 draws on cap. 1 | editor | Loserth p. 25 |
| E02a-1 | ecclesia-02-a / n1 | *Unam sanctam* under *De maioritate et obedientia*, *Extrav. comm.* 1.8.1 | verified | Friedberg II, 1245, Tit. VIII rubric |
| E02a-2 | ecclesia-02-a / n3 | *Christus videlicet et Christi vicarius Petrus, Petrique successor* | verified | Friedberg II, 1245–46 (archive.org BD1141952), read 2026-10-02 |
| E02b-1 | ecclesia-02-b / n5 | Gregory, *Hom. in Ev.* 19.1, *ab Abel … usque ad ultimum electum* (MSS *XXIII Moral. cap. I*; Loserth corrects to *XIX Homiliarum*) | verified | PL 76:1154B, as E01h-4 (read 2026-10-02 by the wave-2 verifier) |
| E02b-2 | ecclesia-02-b / n14 | *septima conclusio capituli proximi* = 19.18 | editor | Loserth |
| E02c-1 | ecclesia-02-c / n4 | Clement V, *Meruit*, *Extrav. comm.* 5.7.2 | verified | Friedberg II, 1299–1300 |
| E02c-2 | ecclesia-02-c / n3 | the apostle Thomas evangelized India | to-verify | from memory (tradition: *Acta Thomae*) |
| E02c-3 | ecclesia-02-c / n10 | Celestine V pope 5 July – Dec. 1294 | editor | Loserth's footnote reads "Dec. i" (OCR; 1 or 13?); the resignation is usually dated 13 Dec. 1294: to-verify before the note gives a day |
| E02c-4 | ecclesia-02-c / n11 | Boniface VIII: *intrabit ut vulpes …* tradition | to-verify | from memory |
| E02d-1 | ecclesia-02-d / n1 | Augustine on Matt. 24:5: *Sermo* 292, *in natali Ioannis Baptistae* (Opp. V.2, 1172) | verified | PL 38:1323, §6: *Multi venient in nomine meo dicentes, Ego sum Christus … nullum audivimus dicentem* (coordinator, 2026-10-02) |
| E02d-2 | ecclesia-02-d / n5 | Urban VI elected 8 April 1378; crowned Easter Sunday, 18 April | editor | Loserth "Easter-Sunday"; the date 18 April is the agent's, to-verify |
| E02e-1 | ecclesia-02-e / n3 | Theban legion; Bordier, *Dissertation critique…* (Amsterdam 1705) | editor | Loserth 39.9 |
| E02e-2 | ecclesia-02-e / n6 | Jerome, *Comm. in Michaeam* II on Mic. 7:5–7 | verified | PL 25:1221C–1222B; Loserth's 1281 = 1221, his 1180 wrong; *dicamus scriptum de haereticis* is Jerome's |
| E02e-3 | ecclesia-02-e / n7 | *ast uxor nati dicitur esse nurus*, a school pentameter | to-verify | source unidentified |
| E02e-4 | ecclesia-02-e / n8 | *Tulit me mater mea …* = Gospel of the Hebrews in Jerome on Mic. 7:6 | verified | PL 25:1221D–1222A, *Modo tulit me mater mea, sanctus Spiritus …* |
| E02f-1 | ecclesia-02-f / n2 | Augustine, *De Trin.* XIII.2.5–3.6 | verified | PL 42:1016–1017; two senses (*quae* / *qua creditur*), not three |
| E02f-2 | ecclesia-02-f / n6 | *libro sexto, tractatu de mendacio* = *De veritate S. Scripture* (B *quinto*) | to-verify | Loserth's conjecture |
| E02f-3 | ecclesia-02-f / n9 | the church's judgment *fallere … et falli* = *X* 5.39.28 *A nobis est saepe quaesitum* (Loserth: 5.39.21) | verified | Friedberg II, 899–900; coordinator re-read (Cap. XXVIII); Loserth's 5.39.21 is another *A nobis* |
| E02f-4 | ecclesia-02-f / n12 | *libro sexto, sexto capitulo*: the signs of Antichrist (B *quinto*) | untraced | unidentified |
| E02f-5 | ecclesia-02-f / n18 | Hus, *De eccl.* fol. 199a ff.; Kenmerton in Walsingham II, 307 | editor | Loserth p. 47 |
| E03a-1 | ecclesia-03-a / n2 | *lib. VI, cap. …* (lacuna in the text) | untraced | unidentified |
| E03a-2 | ecclesia-03-a / n3 | *Decretum* C.8 q.1 c.19 (form ours) | editor | Loserth 47.24 |
| E03a-3 | ecclesia-03-a / n3 | Augustine, *In Ioh. tr.* 46.5 on John 10:12 | verified | PL 35:1729, *temporalia commoda consectantes* |
| E03a-4 | ecclesia-03-a / nn5, 10, 11, 13 | Gregory, *Moralia* XXXI | verified | PL 76:583D–585C, §§19–21 (Migne capp. XII–XIII); *austerna* clause is Wyclif's paraphrase of 584B |
| E03a-5 | ecclesia-03-a / n9 | Augustine, *Conf.* XIII.9.10, *pondus meum amor meus* | verified | PL 32:849 |
| E03a-6 | ecclesia-03-a / n12 | the maxim *dolor amissi et amor habiti …* | untraced | unidentified |
| E03b-1 | ecclesia-03-b / n2, n4, n8–12 | Gregory, *Moralia* XXXI.12–13 §§20–23 (Wyclif "cap. X" = Migne *Vet. X*) | verified | PL 76:584D–586B (agent read 8054.xml) |
| E03b-2 | ecclesia-03-b / n3 | Augustine, *In Ioh. tr.* 6: goods left for Christ still had | untraced | not in tr. 6 (PL 35:1425–37 searched); source may be another work |
| E03b-3 | ecclesia-03-b / n10 | *sicut alias ostendi*: lower members may sue for goods | untraced | perhaps *De civili dominio* |
| E03c-1 | ecclesia-03-c / n1–2 | Gregory, *Moralia* XXXI.13 §24 | verified | PL 76:586C–D |
| E03c-2 | ecclesia-03-c / n6 | Gregory on the fifth penitential psalm | untraced | not found in PL 79:601D–630C (Ps. 101 exposition) |
| E03c-3 | ecclesia-03-c / n8 | Gregory, *Reg. past.* I.2; *Decretum* D.83 c.2 | verified | PL 77:16A; PL 187:400C; Wyclif paraphrases |
| E03c-4 | ecclesia-03-c / n9 | Aquinas, *ST* III q.8 a.3 (Venice 1774, V, 51) | editor | content to-verify (not local) |
| E03c-5 | ecclesia-03-c / n12 | *ut alias diffuse exposui*: faith, hope, charity against the Trinity | untraced | |
| E03d-1 | ecclesia-03-d / n2–3 | *ST* III q.8 a.3: potential members; 1 Tim. 4:10, 1 John 2:2 | to-verify | not local |
| E03d-2 | ecclesia-03-d / n4 | Thomas: Christ head "even of the devil" as to natural being (cf. q.8 aa.7–8) | to-verify | not local |
| E03d-3 | ecclesia-03-d / n5 | Augustine, *In Ioh. tr.* 12.8–9 (John 3:13) | verified | PL 35:1488–89 |
| E03d-4 | ecclesia-03-d / n4 | *ut alias declaravi* | untraced | |
| E03e-1 | ecclesia-03-e / n6 | Aristotle, *Meteor.* I.12, 348b: hot water freezes faster (Wyclif "I, cap. VI") | editor | Loserth: Bekker p. 348 |
| E03e-2 | ecclesia-03-e / n11 | Augustine: those excluded are not members (*proporcionalia*) | untraced | |
| E03e-3 | ecclesia-03-e / n12 | John Damascene, *De fide orth.* (Loserth 4.11): natural knowledge of God | editor | probably I.1/I.3; PG, not local |
| E03e-4 | ecclesia-03-e / n13 | Augustine: *credere in* = believing by loving | verified | *In Ioh. tr.* 29.6, PL 35:1631 |
| E03e-5 | ecclesia-03-e / n14 | Augustine, *In Ioh. tr.* 12.12, *Novit dominus …* | verified | PL 35 (7323.xml) |
| E03f-1 | ecclesia-03-f / n1–3 | Augustine, *In Ioh. tr.* 5.7 (power of baptism: *potuit … et noluit*; Wyclif *non potuit*) and 6.4 (*oscula columbarum*) | verified | PL 35:1417; 35:1427 |
| E03f-2 | ecclesia-03-f / n7 | *Quinto … ex dictis beati Augustini* | to-verify | unidentified |
| E03g-1 | ecclesia-03-g / n1 | *Faustinus* = *tr.* 6.25; *Ep.* 187.37 for *unum corpus … unum caput* | verified | PL 35:1436; PL 33:846 |
| E03g-2 | ecclesia-03-g / n2, n4 | Bernard, *Super Cant.* 12.11, 13.9 (*minime audet*) | verified | PL 183:832B–833D; 838D–839A |
| E03g-3 | ecclesia-03-g / n8 | Guido de Baysio (the Archdeacon), *Rosarium* on D.44 | editor | not local |
| E03g-4 | ecclesia-03-g / n8 | *Decretum* C.8 q.1 c.19 *Sunt in ecclesia* (form ours); "allegatum … in principio huius capituli" | editor | the earlier citation to-verify (03-a n3 cites C.8 q.1 c.19) |
| E03g-5 | ecclesia-03-g / n9 | Augustine, *Civ. Dei* XIX.19, *nomen est operis, non honoris* | verified | PL 41:647 |
| E03g-6 | ecclesia-03-g / n9 | *libro sexto, tractatu de heresi* | untraced | |
| E04a-1 | ecclesia-04-a / n3 | Augustine, *Enchiridion* 29 | verified | PL 40:246 |
| E04a-2 | ecclesia-04-a / n5 | Aquinas, *ST* III q.8 a.3 (Wyclif "conclusione octava") | editor | not local |
| E04a-3 | ecclesia-04-a / n6–7 | *Opus imperfectum in Matth.*, hom. 46 as printed (MSS XXIX; Loserth hom. 45, Montfaucon VI, cxciii E) | editor | where the quotation ends: to-verify (PG 56; not local) |
| E04a-4 | ecclesia-04-a / n8 | the two cities: Augustine, *Civ. Dei* XIV.28 (also I.35); Gregory untraced | verified | PL 41:436; 41:46 |
| E04b-1 | ecclesia-04-b / n2, n5 | Richard of St Victor, *De pot. lig. et solv.* 19–20 | verified | PL 196:1172A–1173A; ends *concorporatus fuit* |
| E04b-2 | ecclesia-04-b / n6 | Augustine, *De doctr. christ.* III.32.45, the *Ypocrite* sentence | verified | PL 34:82 |
| E04b-3 | ecclesia-04-b / n7 | *Opus imperfectum*, hom. 9 (Montfaucon VI, lxi E) | editor | not local |
| E04b-4 | ecclesia-04-b / n8–9 | *ut patet cap. X*; *ut dixi superius* | to-verify | John 10, or this book's ch. 10? |
| E04b-5 | ecclesia-04-b / n14 | *de necessitate salutis* echoes *Unam sanctam* | verified | Friedberg II, 1245–46 (as E01e-1) |
| E04c-1 | ecclesia-04-c / n4 | Thomas and Richard at 77.11 (Loserth "loc. cit."): *ST* III q.8 a.3; Richard, *De pot. lig. et solv.* | to-verify | Richard: PL 196; Thomas not local |
| E04c-2 | ecclesia-04-c / n10; 04-e / n18 | *ST* III q.8 a.3 ad 2 (Wyclif "concl. VIII, art. III"); Thomas *perducimur* | editor | not local |
| E04c-3 | ecclesia-04-c / n13 | Augustine, *De Trin.* (Wyclif "VI, 27"; Loserth XIV.18) | untraced | XIV.18 (PL 42:1055) lacks the claim; "VI, 27" not found |
| E04c-4 | ecclesia-04-c / n14 | Bradwardine, *De causa Dei* I.23, corollary | to-verify | not local |
| E04d-1 | ecclesia-04-d / n1 | John XXII denied the church is a body wherever the faithful are | untraced | |
| E04d-2 | ecclesia-04-d / n3 | Augustine, *Enarr. in Ps.* 142.3 | verified | PL 37:1846, paraphrased |
| E04d-3 | ecclesia-04-d / n5 | *Enchiridion* 56 (Loserth's correction of MSS XLI) | verified | as V-02 |
| E04d-4 | ecclesia-04-d / n8, n10 | *Decretum* C.32 q.4 c.2 *Recurrat*, inscribed Augustine, *In Ioh. tr.* XI | verified | Migne PL 187:1476C–1477C (not Friedberg) |
| E04d-5 | ecclesia-04-d / n13 | *De doctr. chr.* III.32 and the seventh rule | verified | PL 34:82, 88; paraphrase |
| E04d-6 | ecclesia-04-d / n16 | *Unam sanctam*; C.24 q.1 c.18 *Loquitur* (Cyprian, *De unit.*) | verified | Friedberg II, 1245–46; PL 187:1271B |
| E04e-1 | ecclesia-04-e / n3 | "cap. III … Gregory" = this work's ch. 3 | to-verify | 03-a/03-b cite *Moralia* XXXI |
| E04e-2 | ecclesia-04-e / n5 | Augustine, *Ep.* 187 (Wyclif cap. XI) | verified | PL 33:846, cap. XII §37: *filios Dei … congregaret* |
| E04e-3 | ecclesia-04-e / n6 | Isidore, *Sent.* I.16.6 (MSS XVI; Loserth XIX wrong); Hugh, *De sacr.* II.2.2 | verified | PL 83:572; PL 176:416D–417A |
| E04e-4 | ecclesia-04-e / n7 | D.21 c.3 *Quamvis* reads *nullis synodicis constitutis*; Wyclif *multis* | verified | Friedberg I (BD1141951), D.21 c.3: *nullis sinodicis constitutis*, no *multis* in the apparatus (coordinator re-read 2026-10-02); PL 187:119B; PL 59:159B; PL 161:1183A; *nonnullis* PL 13:374B |
| E04e-5 | ecclesia-04-e / n8, n10 | ordinary gloss to D.21 c.3 and C.24 q.1 c.9 | to-verify | not local |
| E04e-6 | ecclesia-04-e / n9–11 | C.24 q.1 cc.6, 9, 14; C.7 q.1 c.7; D.19 c.9; D.40 c.6; *De cons.* D.1 c.8 *Ecclesia* | editor | c.8 located: PL 187:1708B (Nicholas I); the rest Loserth's |
| E04e-7 | ecclesia-04-e / n13 | D.22 c.1 *Omnes* (Nicholas II); *Liber Sextus* 5.2 | verified (Omnes) | PL 187:122C; Sext title to-verify |
| E04e-8 | ecclesia-04-e / n15 | Canon of the mass, *Te igitur*: *adunare*; Wyclif *adiuvare* | to-verify | missal |
| E04e-9 | ecclesia-04-e / n17 | *De pen.* D.1 c.70 and its gloss | editor | gloss to-verify |
| E04f-1 | ecclesia-04-f / n1 | *Forte*, *Hec autem vita* = C.23 q.4 cc.11, 15 | verified | PL 187; Friedberg I ~901–904 |
| E04f-2 | ecclesia-04-f / n2 | *Recurrat* = C.32 q.4 c.2 | verified | as E04d-4 (PL 187:1476C) |
| E04f-3 | ecclesia-04-f / n2 | *Recurrat* opens with *In Ioh. tr.* 11.8; *Itaque sive intus … caro est caro est* = *De baptismo* I.17.26 | verified | PL 35 (tr. 11); PL 43 (7461) |
| E04f-4 | ecclesia-04-f / n3 | *Vasis ire* = C.23 q.4 c.23 | verified | PL 187; Friedberg I ~907–908 |
| E04f-5 | ecclesia-04-f / n10 | Hugh, *De sacr.* II.2.2: the eye that sees for the whole body | verified (partial) | PL 176 (11082); the bridegroom/bride wording not found |
| E04f-6 | ecclesia-04-f / n12 | Hus reuses ch. 4 | editor | Loserth p. 92 |
| E05a-1 | ecclesia-05-a / n1 | *Ardmacanus* = FitzRalph, *De pauperie Salvatoris*, to Innocent VI (MS note: *ad instanciam Clementis VI*) | editor | dedication to-verify (not local) |
| E05a-2 | ecclesia-05-a / n7 | Augustine, *Ep.* 187 §§20, 37 | verified | PL 33, *unum caput est Christus*; sense, not verbatim |
| E05a-3 | ecclesia-05-a / n7 | FitzRalph's emperor/pope two-heads example | to-verify | not local |
| E05a-4 | ecclesia-05-a / n10 | Gregory, *Reg. past.* II.6, wine and oil | verified | PL 77 |
| E05a-5 | ecclesia-05-a / n10 | the Commentator = Averroes, *Phys.* III prologue (poison simile) | editor | locus to-verify (not local) |
| E05b-1 | ecclesia-05-b / n2 | *ecclesia ab Abel* | to-verify | cf. Gregory, *Hom. in Ev.* 19.1 (PL 76:1154B, E01h-4); Aug. *Enarr.* 142.3 (E04d-2) |
| E05b-2 | ecclesia-05-b / n3 | sequence *Rex Salomon* (Daniel, *Thes. hymnol.* V, 106); Adam of St Victor | editor | ascription to-verify |
| E05b-3 | ecclesia-05-b / n10 | Grosseteste on Micah 7 | to-verify | not local |
| E05b-4 | ecclesia-05-b / n11 | Bernard "above": *Super Cant.* 12 (*ubera … vino*), quoted in 03-g | verified (partial) | PL 183 (11258); no vine in Serm. 12–13 |
| E05c-1 | ecclesia-05-c / n1 | Aristotle, *Cat.* 7: squaring the circle knowable, not yet known | to-verify | not local |
| E05c-2 | ecclesia-05-c / n3 | "one of the 24 prophets" = *Liber XXIV philosophorum* prop. 2 | to-verify | not local |
| E05c-3 | ecclesia-05-c / n5 | John of Howden (d. 1275); the verse's poem | editor | poem to-verify |
| E05c-4 | ecclesia-05-c / n12 | Augustine, *De natura boni*: passage not extant there (lacuna in codd.) | editor | Loserth |
| E05c-5 | ecclesia-05-c / n14 | *De doctr. chr.* III.32, Tyconius's second rule | verified | PL 34:82 (as V-08, E04b-2) |
| E05c-6 | ecclesia-05-c / n16 | heat gathers like, separates unlike (*De gen. et corr.* II.2) | to-verify | not local |
| E05c-7 | ecclesia-05-c / n17 | "cap. XLIII tercii libri" | untraced | work not identified |
| E05c-8 | ecclesia-05-c / n18 | Gregory, *Moralia* IV.11 (codd. IX) | verified | PL 75:647B–C; Wyclif omits *isdem*, adds *inquit* |
| E05d-1 | ecclesia-05-d / n2 | *Categories* 6, the common boundary | editor | Loserth 104.27 |
| E05d-2 | ecclesia-05-d / n8 | *Physics* VII.1, mover and moved together | editor | Bekker 243 |
| E05d-3 | ecclesia-05-d / n14 | Wis. 18:15 as in the introit *Dum medium silentium* | to-verify | missal |
| E05d-4 | ecclesia-05-d / n15 | the inn "between two streets", the two animals | untraced | |
| E05e-1 | ecclesia-05-e / n1 | *Eth. Nic.* II.7, 1107 | editor | |
| E05e-2 | ecclesia-05-e / n4 | Bernard, *De consid.* V.8.18: the eight unities | verified | PL 182:799C–D, near verbatim |
| E05e-3 | ecclesia-05-e / n6 | Bernard, *Serm. de div.* 80, *unitas principalis* | verified | PL 183:698D–699A |
| E05e-4 | ecclesia-05-e / n12 | Augustine to Boniface: David and Peter = *Ep.* 185.45–46 | verified (partial) | PL 33:812–813; Loserth's XXXIII / Opp. II 263 unconfirmed |
| E05e-5 | ecclesia-05-e / n12 | *De octo Dulcitii quaestionibus* q. 5: David | verified | PL 40:167–169 |
| E05e-6 | ecclesia-05-e / n15 | Isidore, *Sent.* I.19 (codd. XVI) | verified | I.16.6, PL 83:572 (E04e-3): the MSS' XVI is right |
| E05f-1 | ecclesia-05-f / n1 | the *quidam doctor* whose definition is attacked (112.10) | untraced | |
| E05f-2 | ecclesia-05-f / n3 | *Unam sanctam* | verified | Friedberg II, 1245–46 (E01c-5) |
| E05f-3 | ecclesia-05-f / n15 | *in principiis … obstare*: Ovid, *Rem. am.* 91 *principiis obsta* | to-verify | not local |
| E05f-4 | ecclesia-05-f / n15 | cf. Hus, *De eccl.* fol. 205 | editor | Loserth 115.33 |
| E06a-1 | ecclesia-06-a / n3 | "head" a relative term: Aristotle, *Cat.* 7 | to-verify | not local |
| E06a-2 | ecclesia-06-a / n5 | the divine nature does not generate: Lateran IV, *Damnamus* (*X* 1.1.2) | to-verify | Friedberg II (archive.org offline) |
| E06a-3 | ecclesia-06-a / n5 | cf. Hus, *De eccl.*, Opp. I fol. 198 (OCR "iqS*") | editor | folio uncertain |
| E06a-4 | ecclesia-06-a / n19 | Tyconius's second rule = *De doctr. chr.* III.32 | verified | PL 34:82 (V-08) |
| E06b-1 | ecclesia-06-b / n2 | *De doctr. chr.* III.32 | verified | as E06a-4 |
| E06b-2 | ecclesia-06-b / n2 | cf. Hus, *De eccl.* fol. 206b | editor | Loserth 120.22 |
| E06b-3 | ecclesia-06-b / n3 | Christ and his body one person = Tyconius's first rule, III.31.44 | verified | PL 34:82 (V-08: rule 1 = §44) |
| E06b-4 | ecclesia-06-b / n3 | Wyclif's quotation *non … sic debuit appellari … vero atque simulato* | verified | PL 34:82–83 (V-08) |
| E06b-5 | ecclesia-06-b / n4 | *De cons.* D.2 c.63 *Hoc sacramentum pietatis* (Aug. *In Ioh.* 26); *Hunc itaque cibum* is its § 1 | verified | PL 187:1762A |
| E06b-6 | ecclesia-06-b / n5 | *De pen.* D.4 c.8 *Si ex bono in malum deficiente* (Aug. *De corr. et gr.* 8–9) | verified | PL 187:1620A |
| E06b-7 | ecclesia-06-b / n10 | *decretum … in fine XIII cap.* | untraced | |
| E06b-8 | ecclesia-06-b / n12 | heresy = understanding scripture otherwise than the Spirit demands: C.24 q.3 c.27 (Jerome) | verified | PL 187:1306B |
| E06b-9 | ecclesia-06-b / n12 | heresy to impute vice to the Roman church: perhaps D.22 c.1 | to-verify | cf. E04e-7 (PL 187:122C) |
| E06c-1 | ecclesia-06-c / n1 | cf. Hus, *De eccl.*, Opp. I, 198b | editor | Loserth |
| E06c-2 | ecclesia-06-c / n1 | cf. Wyclif, *De benedicta incarnacione* c. 5, p. 67 | editor | Loserth; the phrase it attaches to to-verify |
| E06c-3 | ecclesia-06-c / n3 | *dux et legifer noster*: the antiphon *O Emmanuel* | to-verify | breviary |
| E06c-4 | ecclesia-06-c / n4 | *terrena despicere et amare celestia*: an Advent postcommunion | to-verify | missal |
| E06c-5 | ecclesia-06-c / n7 | *ut canit ecclesia*: office of the dedication of a church | to-verify | breviary |
| E06d-1 | ecclesia-06-d / n3 | consecrating during the triduum (cf. Aquinas *ST* III q.81 a.4) | to-verify | not local |
| E06d-2 | ecclesia-06-d / n3 | the place in Wyclif's *De incarnacione* | untraced | |
| E06d-3 | ecclesia-06-d / n4 | Jerome to Paula and Eustochium | to-verify | not Ep. 46 (PL 22:483); Ep. 30, 31 unread |
| E06d-4 | ecclesia-06-d / n7 | Augustine, *De Gen. ad litt.* X.19.34: Christ not in Abraham's loins as to soul | verified | PL 34:423 |
| E06d-5 | ecclesia-06-d / n7 | Anselm, *De conceptu virginali* 11 (Loserth) | untraced | not in c. 11 (PL 158:445A–446C); nearest *Omnis homo aut Adam est, aut de Adam* (446C) |
| E06d-6 | ecclesia-06-d / n19 | *De vita christiana* 6 | verified | PL 40:1036–37 |
| E06d-7 | ecclesia-06-d / n19 | *De vita christiana* not Augustine's | verified | PL 40:1031–46, *auctor incertus* |
| E06e-1 | ecclesia-06-e / n1 | the canons: the church "shaken but not overcome" | untraced | |
| E06e-2 | ecclesia-06-e / n2 | *Decretum* D.40 c.2 *Non est facile* (Jerome to Heliodorus) | verified | PL 187:213C–214B |
| E06e-3 | ecclesia-06-e / n4 | "human laws" on payment to a false proctor | untraced | |
| E06e-4 | ecclesia-06-e / n8 | doctors expounding Matt. 19:5 of Christ | untraced | |
| E06e-5 | ecclesia-06-e / n9 | antiphon *quod fuit permansit, et quod non erat assumpsit* | to-verify | breviary |
| E06e-6 | ecclesia-06-e / n17 | C.27 q.1 c.41 *Nuptiarum*, from Augustine *De bono viduitatis* 10.13 | verified | PL 187:1388B–1390A; PL 40:438 |
| E06f-1 | ecclesia-06-f / n4 | Bernard's eight unities = *De consid.* V.8.18 | verified | PL 182:799C–D (E05e-2) |
| E06f-2 | ecclesia-06-f / n6 | C.24 q.1 c.6 *Quodcumque* (Aug. *In Ioh.* 50: Peter signifies the church); C.7 q.1 c.7 *Scire debes* (Cyprian) | verified | PL 187:1267A–B, 746B; Friedberg I ~968, ~326 |
| E06f-3 | ecclesia-06-f / n11 | Augustine, *De vera religione* §91 (Wyclif "XCI") | verified (loose) | PL 34:163 |
| E06f-4 | ecclesia-06-f / n14 | *in materia De Ideis* = Wyclif's *De ideis* (*Summa de ente*) | to-verify | not local |
| E06g-1 | ecclesia-06-g / n1 | *De cons.* D.2 c.36 *Quia passus*, inscribed *Item Augustinus* | verified | PL 187:1746C–1747A; Friedberg I ~1340 n. 455 |
| E06g-2 | ecclesia-06-g / n1 | Augustine, *In Ioh.* tract. 26 | verified | PL 35:1612–1615 (tract. 27 unread) |
| E06g-3 | ecclesia-06-g / n2 | the ordinary gloss on the canon | to-verify | not local |
| E06g-4 | ecclesia-06-g / n2 | *ut dicam alibi* = *De eucharistia* | to-verify | not local |
| E06g-5 | ecclesia-06-g / n6 | doctor profundus = Bradwardine, *De causa Dei* I.23 corollary (MSS XXXII) | editor | not local |
| E06g-6 | ecclesia-06-g / n9 | C.23 q.4 c.23 *Vasis ire* (print *XXXIIIª*) | verified | Migne PL 187 (E04f-4) |
| E06g-7 | ecclesia-06-g / n10 | cf. Hus, *De eccl.*, Opp. I, 200 | editor | Loserth |
| E06g-8 | ecclesia-06-g / n15 | *De cons.* D.1 c.8 *Ecclesia* | verified | PL 187:1708B (E04e-6) |
| E07a-1 | ecclesia-07-a / n1 | the 1378 Westminster sanctuary case; autumn 1378 parliament | to-verify | |
| E07a-2 | ecclesia-07-a / n2 | *Eulogium* continuation (Haule killed; Shakell); Rolls of Parliament III | editor | Loserth p. 142 |
| E07a-3 | ecclesia-07-a / n2 | *comes de Dene* = count of Denia | to-verify | |
| E07a-4 | ecclesia-07-a / n10 | classes excluded from sanctuary | verified (partial) | *X* 3.49.6, 3.49.10, Friedberg II ~656–658; no source gives four |
| E07a-5 | ecclesia-07-a / n13 | a person presumed good until the contrary is proved | to-verify | |
| E07b-1 | ecclesia-07-b / n5 | a prince's general grant does not reach a special case | to-verify | civil/canon law |
| E07b-2 | ecclesia-07-b / n7 | he who can amend and neglects shares the crime = Gratian D.86 c.3 (John VIII) | verified | PL 187:406 |
| E07b-3 | ecclesia-07-b / n8 | *alias ostensum est* (monastery privilege = corruption) | untraced | earlier Wyclif |
| E07c-1 | ecclesia-07-c / n1 | Augustine, *Ep.* 153.20: *non remittetur peccatum nisi restituatur ablatum* | verified | PL 33:662; Wyclif *dimittitur* |
| E07c-2 | ecclesia-07-c / n4 | *Frustra invocat legis auxilium* (the canonists' maxim) | verified | *X* 3.49.10 etc. (Friedberg II); wording Wyclif's |
| E07c-3 | ecclesia-07-c / n5 | Augustine: the adversary = God's word/law: *Sermo* 9.3; *Sermo* 251.8 | verified | PL 38:76; PL 38:1171 (column less certain) |
| E07c-4 | ecclesia-07-c / n7 | disobeying princes "a kind of sacrilege" | to-verify | nearest Gratian C.17 q.4, PL 187:1071A–B; try *Cod.* 9.29 |
| E07c-5 | ecclesia-07-c / n10 | Gregory: whoever loves the king loves his law | untraced | |
| E07d-1 | ecclesia-07-d / n1 | excommunications after the Westminster killing | to-verify | historical |
| E07d-2 | ecclesia-07-d / n5 | blood or semen pollutes a church | verified | *X* 3.40.10, Friedberg II, 636; no canon on spittle |
| E07d-3 | ecclesia-07-d / n10 | privilege = *lex privata* | verified | Isidore *Etym.* V.18.1, PL 82:202A–B; Gratian D.3 c.3, PL 187:34B |
| E07d-4 | ecclesia-07-d / n14 | signification after 40 days; writ *de excommunicato capiendo* | to-verify | English law |
| E07d-5 | ecclesia-07-d / n14 | *Privilegium omnino meretur amittere …* = C.11 q.3 c.63 (Gregory) | verified | PL 187:862 (also D.74, 364B) |
| E07e-1 | ecclesia-07-e / n2 | adapts *optima legum interpres consuetudo* (*Dig.* 1.3.37) | to-verify | not local |
| E07e-2 | ecclesia-07-e / n5 | A's Czech margin and Loserth's Latin rendering | editor | Loserth p. 157 |
| E08a-1 | ecclesia-08-a / n1 | the *infamis casus* = the Westminster sanctuary violation, Aug. 1378 | to-verify | |
| E08a-2 | ecclesia-08-a / n2 | *iuxta dicta XVⁱ cap.*: which work | untraced | no ch. 15 precedes |
| E08a-3 | ecclesia-08-a / n3 | *Phys.* II.2, 194a | editor | |
| E08a-4 | ecclesia-08-a / n4 | "supra pag. 1": honour father and mother | editor | 01-a |
| E08a-5 | ecclesia-08-a / n7 | doctors heard before the council, Gloucester parliament, Oct. 1378 | to-verify | |
| E08a-6 | ecclesia-08-a / n9 | *tractatus De mendacio*: Augustine's or Wyclif's | to-verify | |
| E08a-7 | ecclesia-08-a / n10 | virtue: *Trialogus* III.1 (Lechler 128); *EN* II.6, 1106b36 | editor | |
| E08a-8 | ecclesia-08-a / n11 | Wyclif's "Eth. IV c. IV" = *EN* IV.7, 1127a28–30 | to-verify | not local |
| E08a-9 | ecclesia-08-a / n12 | Augustine, *De lib. arb.* II.19.50 (virtues, great goods), quoted in *Retract.* | verified | PL 32:1267–68; 597 |
| E08b-1 | ecclesia-08-b / n7 | *metam redargucionis*: the sophist's goals (*Soph. el.*) | to-verify | not local |
| E08b-2 | ecclesia-08-b / n10; 08-c / n1, n9 | Augustine, *Enarr. in Ps.* 5: *non re, sed indole laudantur* | verified | PL 36:85 (has *non*) |
| E08b-3 | ecclesia-08-b / n11 | Augustine on the midwives' lie | verified | *Contra mend.* 15.31–32, PL 40:539–40; *De mend.* PL 40:491–92; *Quaest. in Hept.* II.1, PL 34:597 |
| E08b-4 | ecclesia-08-b / n12 | Comestor, *Hist. schol.* Exod. 3, *De dolo obstetricum* | verified | PL 198:1142B–1143A |
| E08b-5 | ecclesia-08-b / n12 | Gregory, *Moralia* XVIII.3, the midwives | verified | PL 76:41A–B |
| E08c-1 | ecclesia-08-c / n2 | Aquinas, *ST* II-II q.110 (article; *indole*?) | editor | not local |
| E08c-2 | ecclesia-08-c / n4 | gloss *indolem vocat profectum* in Wyclif's Augustine | untraced | |
| E08c-3 | ecclesia-08-c / n5 | *necessarium atque felix* (Gregory) = the Exsultet | to-verify | missal |
| E08c-4 | ecclesia-08-c / n5 | Augustine calls Adam's sin *expediens* | untraced | *Civ.* XIV.13 says *utile* (PL 41:422) |
| E08c-5 | ecclesia-08-c / n5 | *De civ. Dei* XIV.13 | verified | PL 41:422 |
| E08c-6 | ecclesia-08-c / n13 | privilege = private law: Isidore, *Etym.* V.18 / D.3 c.3 | verified | as E07d-3 |
| E08c-7 | ecclesia-08-c / n15 | *uti / frui* | verified | *De doctr. chr.* I.3–4, PL 34:20 |
| E08d-1 | ecclesia-08-d / n11 | Ps.-Chrysostom, *Opus imperf.* hom. 35 (Montfaucon CLII E) | editor | not local |
| E08d-2 | ecclesia-08-d / n11 | FitzRalph, *Defensio curatorum* (Goldast, *Monarchia* II.ii, 1403) | editor | not local |
| E08d-3 | ecclesia-08-d / n12 | *honor fugientem se sequitur* | untraced | analogue *Vita Bernardi* III, PL 185:304A |
| E08d-4 | ecclesia-08-d / n13 | *Desiderium primatus …* in the same homily | to-verify | not local |
| E08d-5 | ecclesia-08-d / n17 | the doctors on twofold martyrdom (*affeccione / passione*) | untraced | |
| E08e-1 | ecclesia-08-e / n2 | *Opus imperf.* hom. 35 (CLIII C) | editor | not local |
| E08e-2 | ecclesia-08-e / n4 | Augustine, *De doctr. chr.* II.42.63 | verified | PL 34:65; *scripturam sacram* is Wyclif's |
| E08e-3 | ecclesia-08-e / n4 | Augustine's "fourth letter to Volusianus" | untraced | not in *Ep.* 132, 135, 137 (PL 33) |
| E08e-4 | ecclesia-08-e / n8, n14 | *Decretum* C.11 q.3 c.63 | verified | PL 187:862 (E07d-5) |
| E08e-5 | ecclesia-08-e / n10 | "the case which lately befell" = Westminster | to-verify | context |
| E08e-6 | ecclesia-08-e / n19 | *Sext* 5.12.3 *Exiit* | verified | Friedberg II; *perfectissimus* is Wyclif's |
| E08e-7 | ecclesia-08-e / n21 | Gregory, *Moralia* XXXI.13 (Loserth "ch. 12" for ch. 3) | verified | PL 76:583D–585C (E03a-4) |
| E08f-1 | ecclesia-08-f / n7 | *maliciam venenosam*: the "poison poured into the church" at the Donation | to-verify | |
| E08f-2 | ecclesia-08-f / n16 | Gregory passage cited at pp. 52–54 = *Moralia* XXXI | verified | E03b-1 |
| E08f-3 | ecclesia-08-f / n17 | *De vera rel.* 92 | verified | PL 34:163 |
| E08f-4 | ecclesia-08-f / n18 | ch. 6, sixth argument = pp. 136–138 | editor | |
| E08f-5 | ecclesia-08-f / n19 | *De vera rel.* 93 *perfecta iusticia* | verified | PL 34:163–64 |
| E09a-1 | ecclesia-09-a / n7 | *ecclesia canit … privilegio amoris Johannem dilexit*: office of St John the Evangelist | to-verify | breviary |
| E09a-2 | ecclesia-09-a / n10 | *Lincolniensis* (Grosseteste) on exemptions | to-verify | not local |
| E09a-3 | ecclesia-09-a / n12 | Augustine, *De ordine* II ("cap. XVIII (?)") | untraced | PL 32 Bk II searched; II.18 (1016) a different topic |
| E09a-4 | ecclesia-09-a / n14 | Augustine, *De agone christiano* 7 (Loserth "IV") | verified | PL 40:295 |
| E09a-5 | ecclesia-09-a / n15 | baptismal renunciation "of Satan and all his pomps" | to-verify | rite |
| E09a-6 | ecclesia-09-a / n16 | C.24 q.1 c.33 *Pudenda* (Pelagius) | verified | Friedberg I, 979–80 |
| E09a-7 | ecclesia-09-a / n16 | the Augustine inside c.33 | untraced | unnamed in Gratian and Friedberg |
| E09a-8 | ecclesia-09-a / n17 | *execratus … non consecratus* in c.33 | verified | Friedberg I, 980 |
| E09a-9 | ecclesia-09-a / n18 | *Non est facile* = D.40 c.2 | verified | PL 187:213C–214B (E06e-2) |
| E09b-1 | ecclesia-09-b / n1 | *ex cap. VI°* = this work's ch. 6 | to-verify | |
| E09b-2 | ecclesia-09-b / n2 | *De cons.* D.5 c.24 *Non mediocriter* (Jerome) | verified | Friedberg I, 1418 |
| E09b-3 | ecclesia-09-b / n2 | *libro V°, cap.* [blank] | untraced | |
| E09b-4 | ecclesia-09-b / n5 | *ut alias exemplificavi de Augustino* | untraced | |
| E09b-5 | ecclesia-09-b / n7 | C.11 q.1 c.29 *Te quidem*, from Clement to James | verified | Friedberg I, 634; Peter speaks to Clement within it (c.30) |
| E09b-6 | ecclesia-09-b / n11 | John turns branches and stones into gold and gems | to-verify | legend (*Virtutes Iohannis*) |
| E09c-1 | ecclesia-09-c / n3 | C.25 q.2 c.2, Leo to Marcian | verified | Friedberg I, 1011–12 |
| E09c-2 | ecclesia-09-c / n4 | C.25 q.1 c.3, Leo to Anatolius | verified | Friedberg I, 1007–08 |
| E09c-3 | ecclesia-09-c / n7 | *X* 3.50.7 *Relatum* (Alexander III) | verified | Friedberg II, 659–60 |
| E09c-4 | ecclesia-09-c / n10 | Aristotle, *Ethics* I.2–3 | editor | |
| E09d-1 | ecclesia-09-d / n11 | the rule at the end of ch. 8 | verified | 08-f, pp. 181–82 |
| E09d-2 | ecclesia-09-d / n13 | Augustine, *Enarr. in Ps.* 36 s.1, *olera prati* | verified | PL 36:357–58; the cabbage gloss is not Augustine's |
| E09d-3 | ecclesia-09-d / n13 | the *naturales* on cabbage as a melancholic herb | untraced | |
| E09e-1 | ecclesia-09-e / n2 | Bede on James 1:10–11: Naboth's vineyard | verified | PL 93:13A |
| E09e-2 | ecclesia-09-e / n3 | "chapter 4 of book 6" (Wyclif's cross-reference) | untraced | |
| E09e-3 | ecclesia-09-e / n4 | Sarum antiphon, St Thomas (Procter–Wordsworth I, ccli) | editor | not local |
| E09e-4 | ecclesia-09-e / n8 | "end of chapter 6" = 06-g | verified (substance) | 06-g end; not verbatim |
| E09e-5 | ecclesia-09-e / n9 | Gregory, *Privilegium omnino meretur amittere* = C.11 q.3 c.63 | verified | PL 187:862 (E07d-5); the gloss to-verify |
| E09e-6 | ecclesia-09-e / n12 | C.23 q.4 c.15 (Gregory, *Hec autem vita*) | verified | Friedberg I ~903 (E04f-1) |
| E09e-7 | ecclesia-09-e / n13 | *Omnis iniquus bonorum est inimicus* = Gratian, d.p.c.15, C.23 q.4 | verified | PL 187:1178C–1179A |
| E09e-8 | ecclesia-09-e / n15 | Augustine, *Enarr.* 36 s.1, field / mill / bed | verified | PL 36:356–57 |
| E09f-1 | ecclesia-09-f / n3 | *Quantus arrogancie tumor* = C.23 q.4 c.14 (Aug. *De bapt.* IV.12, quoting Cyprian *Ep.* 55), not Loserth's c.15 | verified | PL 187:1178; Friedberg I, 904–05 |
| E09f-2 | ecclesia-09-f / n8 | *de qua materia patet alibi* | untraced | |
| E10a-1 | ecclesia-10-a / n2 | Edgar's charter ≈ Kemble, *Cod. dipl.* II, 366 | editor | not local |
| E10a-2 | ecclesia-10-a / n5 | Edward's charter = Kemble IV no. 825, p. 181 | editor | not local |
| E10a-3 | ecclesia-10-a / n5 | *alia carta* = Kemble IV, p. 186 | editor | not local |
| E10a-4 | ecclesia-10-a / n6 | the bull "of Nicholas III" in the diploma (Kemble p. 183); Nicholas II? | to-verify | not local |
| E10a-5 | ecclesia-10-a / n1; 10-c / n3 | the *contencio* = the Westminster sanctuary violation, Aug. 1378 | to-verify | |
| E10b-1 | ecclesia-10-b / n7 | Gregory, *Hom. in Ev.* 38 = C.23 q.4 c.16 (Gratian *in ore*, Gregory *iure gladii*) | verified | PL 76; PL 187; Friedberg I |
| E10b-2 | ecclesia-10-b / n8 | *a terrenis desideriis innitentes* (Gregory *enitentes*, Gratian *innitentes*) | verified | PL 76; PL 187 |
| E10b-3 | ecclesia-10-b / n15 | C.23 q.4 *Hec autem* | verified | = c.15 *Hec autem vita* (E04f-1) |
| E10b-4 | ecclesia-10-b / n15 | *recitatur proximo capitulo* = ch. 9 | to-verify | 09-e cites c.15 |
| E10b-5 | ecclesia-10-b / n17 | Peter / Paul / Linus: cf. *De civili dominio* p. 37 | editor | not local |
| E10c-1 | ecclesia-10-c / n2 | Archidiaconus = Guido de Baysio, *Rosarium* | to-verify | not local |
| E10c-2 | ecclesia-10-c / n2 | *Excommunicatorum* = C.23 q.5 c.47 (Urban II) | verified | Friedberg I, 945; PL 187 |
| E10c-3 | ecclesia-10-c / n4 | Augustine, *De serm. Dom.* II.8.28 (Wyclif "c. 10") | verified | PL 34:1281–82 |
| E10c-4 | ecclesia-10-c / n1, n4 | *alias diffuse exposui* | untraced | |
| E10c-5 | ecclesia-10-c / n13 | *libri sexti* = book 6 of Wyclif's *Summa*? | to-verify | |
| E10c-6 | ecclesia-10-c / n15, n17 | Gregory, *Moralia* XXI.4.8 | verified | PL 76 (col. not read) |
| E10c-7 | ecclesia-10-c / n8 | *ut alias dixi* | untraced | |
| E10d-1 | ecclesia-10-d / n3 | cardinals robbed in Durham: Walsingham I, 151 | editor | not local |
| E10d-2 | ecclesia-10-d / n3 | the 1317 attack on the two legates | to-verify | not local |
| E10d-3 | ecclesia-10-d / n5 | *libro III° cap°.* (number missing) | untraced | |
| E10d-4 | ecclesia-10-d / n8 | the coronation-oath clause on doing justice | to-verify | not local |
| E10d-5 | ecclesia-10-d / n12 | Wyclif's thesis condemned by Gregory XI (1377) | to-verify | |
| E10e-1 | ecclesia-10-e / n4, n7 | the writ for taking an excommunicate after 40 days | to-verify | cf. E07d-4 |
| E10e-2 | ecclesia-10-e / n10 | second conclusion of ch. 8 = p. 173 | editor | Loserth |
| E10e-3 | ecclesia-10-e / n10 | ch. 7 on cities of refuge = p. 147 | editor | Loserth |
| E10e-4 | ecclesia-10-e / n12 | *Inter alia* = *X* 3.49.6 | verified | Friedberg II ~656 (E07a-4) |
| E10e-5 | ecclesia-10-e / n13 | *De homicidio* = *X* 5.12.1 (Exod. 21:14) | verified | Friedberg II ~791 |
| E10f-1 | ecclesia-10-f / n1 | fifth case = *X* 3.49.10 | verified | Friedberg II ~658 (E07a-4) |
| E10f-2 | ecclesia-10-f / n1, n7 | *frustra legis auxilium invocet qui committit in legem* | verified | *X* 3.49.10 (Friedberg II, 658); also *X* 1.6.23, 5.19.14, 5.39.45 |
| E10f-3 | ecclesia-10-f / n2 | C.17 q.4 c.9 *Reum ad ecclesiam fugientem* | verified | Friedberg I ~818 |
| E10f-4 | ecclesia-10-f / n2, n5 | the gloss on *X* 3.49.10 | editor | not local |
| E10f-5 | ecclesia-10-f / n2 | Huguccio (Savigny V, 425) | editor | not local |
| E10f-6 | ecclesia-10-f / n5 | D.38 c.10 *Qui ea* (Gregory, *Moralia*) | verified | Friedberg I, 144 |
| E10f-7 | ecclesia-10-f / n6 | *collacio tercia* of the *Authenticum*: which novel | to-verify | not local |
| E10f-8 | ecclesia-10-f / n6 | C.23 q.4 = p. 201 | editor | Loserth |
| E10f-9 | ecclesia-10-f / n9 | *privilegium … amittere qui permissa abutitur potestate* | verified | C.11 q.3 c.63, PL 187:862 (E07d-5) |
| E11a-1 | ecclesia-11-a / n2 | C.25 q.1 c.16 (Leo) and Gratian's dictum after it (§§1–4); *X* 5.39.31 | verified | Friedberg I, 1010–12; II, 901–02 |
| E11a-2 | ecclesia-11-a / n4 | D.20 c.3; C.25 q.1 c.6 *Sunt quidam* (Urban) | verified | Friedberg I, 66; 1008 |
| E11a-3 | ecclesia-11-a / n4 | the five degrees are the canon's words (ascribed to Innocent I) | verified | Friedberg I, 66 |
| E11a-4 | ecclesia-11-a / n5 | Aristotle, *Phys.* II.3 | editor | |
| E11a-5 | ecclesia-11-a / n6 | the bull "of Nicholas III" to Westminster | to-verify | as E10a-4 |
| E11a-6 | ecclesia-11-a / n7 | Gregory: more benefits, greater obligation | to-verify | PL 76 (*Hom. in Ev.* 9?) |
| E11a-7 | ecclesia-11-a / n10 | the canonists: a privilege must be contrary to common law | to-verify | |
| E11a-8 | ecclesia-11-a / n11 | C.25 q.2 c.10 (Gregory): *consacerdotibus* / editions *cum sacerdotibus* | verified | Friedberg I, 1014 |
| E11a-9 | ecclesia-11-a / n14 | C.25 q.1 c.8 *Omne quod*; Wyclif quotes §1 | verified | Friedberg I, 1009 |
| E11b-1 | ecclesia-11-b / n3 | *EN* V, equity (Loserth c. 14) | editor | |
| E11b-2 | ecclesia-11-b / n6 | D.83 c.3 *Error cui non resistitur* | verified | Friedberg I, 293 |
| E11b-3 | ecclesia-11-b / n9 | *Sext* 3.23.2 *Decet* (Gregory X, Lyons II) | verified | Friedberg II, 1061; no psalm cited |
| E11b-4 | ecclesia-11-b / n10 | the gloss on *Sedicionem*; Hostiensis | to-verify | not local |
| E11c-1 | ecclesia-11-c / n1 | Gregory, *Moralia* XXI.4.8 | verified | PL 76:193A–B |
| E11c-2 | ecclesia-11-c / n2, n3 | C.23 q.4 c.24 *Ipsa pietas* (Augustine to Boniface) | verified | Friedberg I, 909–10 |
| E11c-3 | ecclesia-11-c / n2 | C.5 q.5 cc.1–2 (print q.4 wrong) | verified | Friedberg I, 549 |
| E11c-4 | ecclesia-11-c / n4 | C.23 q.4 c.25 *Quid faciet* | verified | Friedberg I, 910–11 |
| E11c-5 | ecclesia-11-c / n7 | "book 6, cap. 25" | untraced | |
| E11c-6 | ecclesia-11-c / n8 | *immunis* (Isidore) | verified (partial) | PL 82:350, 382A, 524B; not *ab in et munium* |
| E11c-7 | ecclesia-11-c / n11 | *De his qui ad ecclesias confugiunt*, *lex finalis* (Cod. 1.12); Loserth *X* 3.49.6 | editor | Code not local |
| E11c-8 | ecclesia-11-c / n13 | C.23 q.4 c.50 | verified | Friedberg I, 926 |
| E11c-9 | ecclesia-11-c / n15 | *X* 3.19.8 *Quum universorum* | verified | Friedberg II, 524 |
| E11c-10 | ecclesia-11-c / n17 | C.23 q.4 c.52: *non* = pre-Correctores reading | verified | Friedberg I, 927–28 |
| E11d-1 | ecclesia-11-d / n5 | 25 Edward III (1351–52): sanctuary for debt | to-verify | statutes |
| E11d-2 | ecclesia-11-d / n6 | C.11 q.3 c.100 (Isidore), *Qui consentit* | verified | Friedberg I, 671 |
| E11d-3 | ecclesia-11-d / n6 | *Si quis peccantem defendit*; *Si quis alterius errori consentit* (inside c.100) | verified | Friedberg I, 671 |
| E11d-4 | ecclesia-11-d / n9 | forty days, coroner, abjuration: English sanctuary law | to-verify | not local |
| E11d-5 | ecclesia-11-d / n13 | C.25 q.1 c.16 *Ideo permittente* | verified | E11a-1 |
| E11d-6 | ecclesia-11-d / n13 | *privilegia quasi privatae leges* = Isidore, *Etym.* V.18 | verified | PL 82:202 (E07d-3) |
| E11d-7 | ecclesia-11-d / n13 | Gregory *Si hoc neque consuetudine generali* = Gratian d.p.c.16 §2, C.25 q.1 | verified (place) | Friedberg I, 1011–12; letter untraced |
| E11d-8 | ecclesia-11-d / n14 | C.19 q.2 c.2 *Due sunt* | verified | Friedberg I, 839 |
| E11e-1 | ecclesia-11-e / n3 | public law *a sanctis Patribus scriptis … confirmata* = C.19 q.2 c.2 | verified | Friedberg I, 839 |
| E11e-2 | ecclesia-11-e / n5 | *opera trinitatis ad extra indivisa* (Augustine) | to-verify | |
| E11e-3 | ecclesia-11-e / n7 | *removens prohibens*: *Phys.* VIII.4 | to-verify | not local |
| E11e-4 | ecclesia-11-e / n8 | *ut dixi proximo capitulo*: Rechabites in ch. 10 | to-verify | 10-* |
| E11e-5 | ecclesia-11-e / n13 | A's two Czech lines after 250.16 | editor | Loserth app. |
| E12a-1 | ecclesia-12-a / n2 | C.22 q.5 c.20 (Ambrose) | verified | Friedberg I, 887–88 |
| E12a-2 | ecclesia-12-a / n3 | Isidore, *Sent.* III.42.3 *servum se esse plebis* | verified | PL 83:711C |
| E12a-3 | ecclesia-12-a / n4 | C.16 q.1 c.68 (Jerome to Damasus) | verified | Friedberg I, 783–84 |
| E12a-4 | ecclesia-12-a / n5 | C.11 q.3 c.55 (Gregory, *Ep.* XI.2; Jaffé 4351) | verified | Friedberg I, 657–58 |
| E12a-5 | ecclesia-12-a / n5 | *Inter verba* = incipit of c.55 | verified | Friedberg I, 657 |
| E12a-6 | ecclesia-12-a / n6 | *lavare laterem* (Terence, *Phormio* 186) | to-verify | not local |
| E12a-7 | ecclesia-12-a / n8 | the Westminster killing, 1378 | to-verify | |
| E12a-8 | ecclesia-12-a / n12 | justice defined (Justinian, *Inst.* 1.1 pr.; Wyclif adds *divina*) | to-verify | not local |
| E12b-1 | ecclesia-12-b / n4 | *Scienti et consentienti non fit iniuria* = *Sext* 5.12 reg. 27 | verified | Friedberg II; *Dig.* 47.10.1.5 not checked |
| E12b-2 | ecclesia-12-b / n9 | Augustine, *De vera rel.* 14.27 (sin voluntary) | verified | PL 34; paraphrase |
| E12b-3 | ecclesia-12-b / n10 | *liber proximus* chs. 20, 24 | untraced | |
| E12b-4 | ecclesia-12-b / n11 | C.25 q.1 c.16 *Ideo permittente* | verified | E11a-1 |
| E12b-5 | ecclesia-12-b / n12 | Archidiaconus (Guido de Baysio), *Rosarium* | to-verify | not local |
| E12c-1 | ecclesia-12-c / n3 | Anselm, *Cur Deus homo* I.21 | verified | PL 158; Anselm *quamlibet parvum*, not *veniale* |
| E12c-2 | ecclesia-12-c / n9 | C.23 q.4 c.22 *Nabuchodonosor penitenciam* | verified | Friedberg I |
| E12c-3 | ecclesia-12-c / n9 | ascribed to Aug. *De praedest. et gratia* 15 (not Augustine's) | verified | Friedberg I n. 284 |
| E12c-4 | ecclesia-12-c / n12 | Matt. 5:25 adversary = scripture | verified | Aug. *Serm.* 9.3, 251.8 (E07c-3) |
| E12c-5 | ecclesia-12-c / n13 | C.23 q.4 c.33 *Est iniusta misericordia* = Ambrose, *In Ps. 118* s. 8.25 | verified | Friedberg I; PL 15 |
| E12c-6 | ecclesia-12-c / n15 | forty days before abjuring the kingdom | to-verify | not local |
| E12d-1 | ecclesia-12-d / n6 | serfs freed by residence in privileged towns | to-verify | |
| E12d-2 | ecclesia-12-d / n8 | the remedy = Gloucester parliament 1378 | to-verify | |
| E12d-3 | ecclesia-12-d / n11 | *dominus dux* = John of Gaunt | to-verify | |
| E12d-4 | ecclesia-12-d / n12 | the fugitives = Hauley and Shakell with their hostage | to-verify | |
| E12d-5 | ecclesia-12-d / n15 | the coronation oath's promise of justice | to-verify | |
| E12d-6 | ecclesia-12-d / n17 | the monk killed in 1378 | to-verify | |
| E12e-1 | ecclesia-12-e / n1 | D.8 c.3: Friedberg *celerrime*, MSS F G *celeberrime* | verified | Friedberg I, 13–14 |
| E12e-2 | ecclesia-12-e / n2 | D.8 c.4 *Veritate manifestata* = Libosus of Vaga, quoted in Aug. *De bapt.* III | verified | Friedberg I, 13–14 |
| E12e-3 | ecclesia-12-e / n7 | the dedication rite: God calls the church his bride | to-verify | not local |
| E12e-4 | ecclesia-12-e / n10 | C.14 q.6 c.1 (Aug. to Macedonius) | verified | Friedberg I, 741–42 |
| E12e-5 | ecclesia-12-e / n14, n24 | the Westminster prophecy; the 1378 killing; the king's knights | to-verify | |
| E12e-6 | ecclesia-12-e / n18 | collect *Nulla ei nocebit adversitas …* | to-verify | missal |
| E12e-7 | ecclesia-12-e / n24 | "first argument of the seventh chapter" | to-verify | 07-a |
| E12f-1 | ecclesia-12-f / n7 | C.23 q.1 c.1 *Nisi bella* (Gratian "Gregorius"; = Origen, *Hom. in Ios.* 16.1) | verified | Friedberg I, 889–90 |
| E12f-2 | ecclesia-12-f / n4 | the legend of St Peter consecrating Westminster | to-verify | not local |
| E12f-3 | ecclesia-12-f / n6 | the abbey excommunicated members of the king's household | to-verify | |
| E13a-1 | ecclesia-13-a / n1 | "the teaching I stated above" | untraced | |
| E13a-2 | ecclesia-13-a / n2 | *elemosina perpetua* = frankalmoign | to-verify | |
| E13a-3 | ecclesia-13-a / n7 | *XI° capitulo de privilegiis* (B XX) | to-verify | ch. 11 |
| E13a-4 | ecclesia-13-a / n13 | *ut alias declaravi* (*De civili dominio*?) | untraced | |
| E13a-5 | ecclesia-13-a / n14, n15 | Edgar, Edward the Confessor; William's transfers | to-verify | |
| E13a-6 | ecclesia-13-a / n16 | "declared in the last chapter": Heli's condition | to-verify | ch. 12 |
| E13b-1 | ecclesia-13-b / n3 | Gratian D.83 c.3 (Loserth; cf. p. 235) | to-verify | = E11b-2 |
| E13b-2 | ecclesia-13-b / n3 | *Regem Anglie semper esse infra etatem*, maxim of English law | untraced | |
| E13b-3 | ecclesia-13-b / n11 | Augustine, *Enarr. in Ps.* 148 (*In tuo arbitrio Deus te esse voluit*) | to-verify | |
| E13b-4 | ecclesia-13-b / n13 | *Par in parem non habet imperium*, canonists' maxim | verified | X 1.6.20; Clem. 5.11.1 |
| E13b-5 | ecclesia-13-b / n14 | King John's tribute of 1213 as the *obligacio regis* | to-verify | |
| E13b-6 | ecclesia-13-b / n15 | writ *ad quod damnum* (mortmain inquiry) | to-verify | |
| E13b-7 | ecclesia-13-b / n6 | *iuxta dicta proximo capitulo* → ch. 12 | to-verify | |
| E13b-8 | ecclesia-13-b / n17 | *ut dixi superius* (alms withdrawn from the unruly) | untraced | |
| E13c-1 | ecclesia-13-c / n1 | *libro III° cap. …* (gap in MSS) | untraced | |
| E13c-6 | ecclesia-13-c / n1 | Henry of Ghent (p. 317) and Thomas on tithes | to-verify | |
| E13c-2 | ecclesia-13-c / n1 | Lev. 6–7, Exod. 27 "perpetual" ordinances | to-verify | |
| E13c-3 | ecclesia-13-c / n7 | Josh. 21 *et ultimo* | to-verify | |
| E13c-4 | ecclesia-13-c / n8 | *Exodi XIX°* (Exod. 29 meant?) | editor | print XIX° uncommented; hedge kept |
| E13c-5 | ecclesia-13-c / n16 | *iusti sunt omnia* (Wyclif's lordship of the just) | to-verify | |
| E13d-1 | ecclesia-13-d / n6 | Gratian D.22 c.1 applied to Christ's privilege of poverty | to-verify | = E04e-7 |
| E13d-2 | ecclesia-13-d / n13 | Sergius III, Gregorovius III 242 (Loserth) | to-verify | |
| E13d-3 | ecclesia-13-d / n13 | *hodie* = 1378, *duos pseudomonachos* = Urban VI, Clement VII | to-verify | |
| E13e-1 | ecclesia-13-e / n10 | the Commentator (Averroes), star added to the heaven (*De caelo* II?) | to-verify | |
| E13f-1 | ecclesia-13-f / n9 | C.1 q.1 c.28 *Fertur* (Gregory I) | editor | Loserth 295.28 |
| E13f-2 | ecclesia-13-f / n10 | C.1 q.1 c.5 *Quisquis* | editor | Loserth 296.3 |
| E13f-3 | ecclesia-13-f / n11 | X 3.24.2 *Fraternitatem* | editor | Loserth 296.11 |
| E13f-4 | ecclesia-13-f / n12 | C.16 q.7 c.3 *Pervenit ad nos* (Gregory VII, not I) | verified | Loserth 296.19 |
| E13f-5 | ecclesia-13-f / n12 | Hus repeats the misattribution (*Opp.* I, 194) | editor | Loserth 296.19 |
| E13f-6 | ecclesia-13-f / n15 | *libro VI°, cap. XX–XXIII*: which book of the *Summa* | untraced | |
| E13f-7 | ecclesia-13-f / n16 | C.4 q.1 c.2 *Quod autem* (Nicholas I) | editor | Loserth 298.3–4 |
| E13f-8 | ecclesia-13-f / n17 | gloss on C.4 q.1 c.2: every excommunicate a heretic | to-verify | |
| E13f-9 | ecclesia-13-f / n17 | *Ipsa pietas* (C.23 q.4), *Illi* (C.24 q.3): capitula | verified | C.23 q.4 c.24; C.24 q.3 c.25 |
| E13f-10 | ecclesia-13-f / n19 | Roman church's privilege, cf. D.22 c.1 *Omnes* | to-verify | cf. E04e-7 |
| E13f-11 | ecclesia-13-f / n21 | X 2.24.4 *Ego episcopus* (Wyclif: book III) | editor | Loserth 298.30 |
| E14a-1 | ecclesia-14-a / n5 | *ius poli* / *ius fori*, Augustine's pair | verified | *Sermo* 355.4.5, PL 39.1572 |
| E14a-2 | ecclesia-14-a / n7 | Bede, *In Lucam* II (*Quid me propter divicias*) | verified | PL 92.460, book III (Wyclif: II) |
| E14a-3 | ecclesia-14-a / n8 | Jerome on Matt. 8:20 | verified | PL 26.52–53; Bede borrows it |
| E14a-4 | ecclesia-14-a / n9 | *de Evangelista*: which evangelist offered possession | untraced | |
| E14a-5 | ecclesia-14-a / n11 | D.8 c.1 *Quo iure* = Aug. *Tract. in Ioh.* 6.25 | verified | Loserth 301.16 |
| E14a-6 | ecclesia-14-a / n11 | *reticeamus* (print) vs *recitemus* | verified | Friedberg and PL 35 read *recitemus* |
| E14a-7 | ecclesia-14-a / n12 | D.96 c.14 *Constantinus* | editor | Loserth 301.28 |
| E14b-1 | ecclesia-14-b / n3 | *dominus Ardmacanus* = FitzRalph, *De pauperie Salvatoris* | to-verify | |
| E14b-2 | ecclesia-14-b / n4 | Aug. *De doctr. christ.* IV: necessary things said more plainly | untraced | not in IV; cf. II.9.14, III.26.37 |
| E14b-3 | ecclesia-14-b / n7 | Gregory, *Moralia* XXIII.1.2 (print XXXIII) | verified | |
| E14b-4 | ecclesia-14-b / n15 | Aug. Ep. 153.6.20 *non remittitur peccatum nisi restituatur ablatum* | verified | Loserth 304 foot |
| E14b-5 | ecclesia-14-b / n16 | *materia De Privilegiis* = *De eccl.* chs. 8–9 | to-verify | |
| E14b-6 | ecclesia-14-b / n17 | second Macedonius quotation, Ep. 153.21 | verified | |
| E14b-7 | ecclesia-14-b / n18 | Westminster sanctuary affair, Aug. 1378 | to-verify | |
| E14c-1 | ecclesia-14-c / n8 | *ut dixi proximo capitulo* = p. 296 ff. | editor | Loserth 308.8 |
| E14c-2 | ecclesia-14-c / n17 | the antipope = Robert of Geneva (Clement VII) | editor | Loserth 309.26 |
| E14d-1 | ecclesia-14-d / n2 | Aug. Ep. 153 quoting Prov. 17:6 LXX | verified | 153.26, PL 33.665; letter per Loserth 311.4 |
| E14d-2 | ecclesia-14-d / n2 | *Romanorum VIII* = 8:32 | to-verify | |
| E14d-3 | ecclesia-14-d / n5 | *in fine proximi capituli* = p. 297 | editor | Loserth 311.18 |
| E14d-4 | ecclesia-14-d / n12 | C.12 q.1 c.5 *Clericus* | verified | Loserth 313.17 |
| E14d-5 | ecclesia-14-d / n16 | Bernard, *De consid.* IV.3.7, two swords | verified | PL 182.776 |
| E14d-6 | ecclesia-14-d / n16 | *iura canonica*: *Unam sanctam*, Extrav. comm. 1.8.1 | to-verify | |
| E14d-7 | ecclesia-14-d / n19 | Aug. *In Ioh.* tr. 5, power of baptism | verified | 5.7, 9, 11; Loserth 314.18 |
| E14d-8 | ecclesia-14-d / n19 | Wyclif's *Omelia VIª* | untraced | |
| E14e-1 | ecclesia-14-e / n6 | Bernard, *De consid.* IV.3.7 | verified | = E14d-5 |
| E14e-2 | ecclesia-14-e / n8 | Aug. *De doctr. christ.* 2.42.63 *si utile est, ibi invenitur* | verified | |
| E14e-3 | ecclesia-14-e / n11 | Bernard, *De consid.* 2.6.10–11, apostles forbidden lordship | verified | |
| E14e-4 | ecclesia-14-e / n16 | Henry of Ghent, *Quodl.* 6 q. 23 | to-verify | |
| E14e-5 | ecclesia-14-e / n16 | the *venenum* voice at Constantine's donation | untraced | not in PL |
| E14e-6 | ecclesia-14-e / n18 | Hugh of St Victor, *De sacr.* 2.2.3, 2.2.7 | verified | two powers = 2.2.4 |
| E14f-1 | ecclesia-14-f / n9 | "Nicholas Putanensis" on Romans (A's margin) | untraced | |
| E14f-2 | ecclesia-14-f / n15 | Aug. *In Ioh.* 6.25–26, *iure imperatoris* | verified | = E14a-5 |
| E14f-3 | ecclesia-14-f / n16 | Aug. "Ep. 37" = Ep. 153.26 | verified | = E14d-1 |
| E14g-1 | ecclesia-14-g / n1 | D.96 c.14 *Constantinus* | verified | |
| E14g-2 | ecclesia-14-g / n6 | *XCVIª d.* at 323.27 = D.96 c.14 | to-verify | |
| E14g-3 | ecclesia-14-g / n18 | the claims answer Gregory XI's bulls of 1377 | to-verify | |
| E14g-4 | ecclesia-14-g / n19 | conclusion on lords taking from a delinquent church condemned 1377 | to-verify | |
| E14h-1 | ecclesia-14-h / n1 | Matthew's *Dic bufo crati* = ME proverb "quoth the toad to the harrow" | to-verify | |
| E14h-2 | ecclesia-14-h / n3 | D.96 c.14 *Constantinus* | verified | = E14g-1 |
| E14h-3 | ecclesia-14-h / n8 | Aug. *In Ioh.* 6 (*Quo iure*) | verified | 6.25, = E14a-5 |
| E14h-4 | ecclesia-14-h / n8 | D.8 c.1 *Quo iure* | verified | = E14a-5 |
| E14h-5 | ecclesia-14-h / n8 | Bernard, *De consid.* II, *Esto ut alia ratione* | verified | II.6.10, PL 182.748 |
| E15a-1 | ecclesia-15-a / n2 | C.23 q.4 c.22 *Nabuchodonosor* | verified | |
| E15a-2 | ecclesia-15-a / n5 | *mortui vel divisi* = the Schism of 1378 | to-verify | |
| E15a-3 | ecclesia-15-a / n7 | *Error cui non resistitur approbatur* = D.83 c.3 | verified | Innocent; cf. E11b-2 |
| E15a-4 | ecclesia-15-a / n10 | William Bateman, Norwich (Walsingham I, 262) | editor | |
| E15a-5 | ecclesia-15-a / n11 | John Grandisson, Exeter (Walsingham I, 309; Rot. Parl. II, 245) | editor | |
| E15a-6 | ecclesia-15-a / n11 | Thomas de Lisle, Ely (Walsingham I, 285) | editor | |
| E15a-7 | ecclesia-15-a / n12 | French possessioners = alien priories (Rot. Parl. III, 22b) | to-verify | identification ours |
| E15a-8 | ecclesia-15-a / n6 | "chapter 12" = p. 265 | editor | |
| E15b-1 | ecclesia-15-b / n2 | D.40 c.12 from *Opus imperfectum in Matth.* hom. 43 | verified | |
| E15b-2 | ecclesia-15-b / n5 | Sergius the monk who instructed Muhammad | to-verify | |
| E15b-3 | ecclesia-15-b / n7 | the pseudo-pope = Clement VII | to-verify | |
| E15b-4 | ecclesia-15-b / n8 | Hus, *De ablacione bonorum temporalium* (Nuremberg 1558, I, 122ᵛ) | editor | |
| E15c-1 | ecclesia-15-c / n1, n7, n10 | Hus, *De ablacione bonorum temporalium* fol. 121ʳ, 123ʳ; Hus's reuse at 338.10, 338.27; Loserth, *Hus und Wiclif* pp. 199–208 | editor | Loserth, feet of pp. 336–338 |
| E15c-2 | ecclesia-15-c / n12 | *primi fructus* = papal annates claimed in 14th-c. England | to-verify | |
| E15c-3 | ecclesia-15-c / n15 | *comitive depopulatrices* = the free companies; cf. Walsingham I, 302 | editor | Loserth, foot of p. 339 |
| E15c-4 | ecclesia-15-c / n16 | regalian right to temporalities in vacancy; presentation; licence to elect and assent | to-verify | |
| E15d-1 | ecclesia-15-d / n3 | cross-reference "end of chapter 13" (A *XXII* corr. *XIII*) | verified | 13-f ends with abusers of church goods as heretics |
| E15d-2 | ecclesia-15-d / n5 | *Qui emendare potest et negligit* ~ D.86 c.3 | verified | Gregory to Brunhild (PL 77); D.86 c.3 is John VIII, loose parallel only |
| E15d-3 | ecclesia-15-d / n6 | Gregory, *Registrum* XI.29 (Wyclif's numbering); the earlier citation | to-verify | |
| E15d-4 | ecclesia-15-d / n7 | *Privilegium* = C.11 q.3 c.63 (Gregory), *meretur amittere* | verified | Friedberg: *meretur*; Wyclif *debet* |
| E15d-5 | ecclesia-15-d / n8 | maxim *eius est interpretari cuius est condere* | verified (roots) | Cod. 1.14.12; C.25 q.1 §2 dictum; exact maxim not located in law |
| E15d-6 | ecclesia-15-d / n5 | Hus parallels fol. 123 (341.22, 341.25) | editor | Loserth, foot of p. 341 |
| E15e-1 | ecclesia-15-e / n4 | "in materia De Symonia" = Wyclif, *De simonia* | to-verify | |
| E15e-2 | ecclesia-15-e / n7 | "superius tractatu De Privilegiis" = *Eccl.* chs. 8–9 | to-verify | |
| E15e-3 | ecclesia-15-e / n9 | cross-reference to ch. 13 (A *XXII*, corr. in margin) | verified | see E15d-1 |
| E15e-4 | ecclesia-15-e / n10 | Bernard: Abelard's sin uncertain until his followers are known | to-verify | |
| E15e-5 | ecclesia-15-e / n11 | essential and accidental perfection of alms, scholastic commonplace | to-verify | |
| E15e-6 | ecclesia-15-e / n15 | English king's reputed healing touch and taming of lions | to-verify | |
| E15e-7 | ecclesia-15-e / n19 | C.23 q.4 *Nimium*, *Ipsa pietas*, *Quid faciet*; ch. 11 cross-ref (B XX) | verified | Friedberg c.37, c.24, c.23 |
| E15e-8 | ecclesia-15-e / n20–21 | C.5 q.5 c.1–2 (Augustine); Augustine reads *innocentes non estis, si* | verified | c.1 Aug. Ep. 211; c.2 Ep. 93; Wyclif conflates |
| E15e-9 | ecclesia-15-e / n24 | Augustine to Macedonius (Loserth Opp. II 532; Wyclif "37") = Ep. 153 | verified | PL 33 Ep. 153; *Quis nos* is Ep. 93, not 153 |
| E15e-10 | ecclesia-15-e / n27 | D.83 c.2 | editor | |
| E15e-11 | ecclesia-15-e / n29 | C.5 q.5 c.5 *Qui ambulat* | editor | |
| E15e-12 | ecclesia-15-e / n11, n15, n17, n24 | Hus parallels 343.15, 343.30, 345.3, 345.24 (fol. 133), 347.4–11 | editor | Loserth, feet of pp. 343–347 |
| E15e-13 | ecclesia-15-e / n28 | *palea* plays on the *paleae* of the Decretum | to-verify | reader's judgment |
| E15f-1 | ecclesia-15-f / n2 | ordinary gloss on D.96 c.10 *Duo sunt* | editor | p. 349 foot, l. 10 |
| E15f-2 | ecclesia-15-f / n3 | D.40 c.6 *Si papa* (OCR "Cap. tUtt") | verified | Friedberg; Loserth gives no ref (n13 is De Liguribus), so ours |
| E15f-3 | ecclesia-15-f / n3 | C.23 q.5 c.43 *De Liguribus* | editor | foot-note 13 *Cap. XLIII*; Friedberg |
| E15f-4 | ecclesia-15-f / n4 | C.23 q.5 c.20 *Principes* | verified | foot-note 15 *Cap. XX*; Friedberg |
| E15f-5 | ecclesia-15-f / n5 | Ps.-Dionysius, *Cel. Hier.* 3: purging and illuminating | to-verify | |
| E15f-6 | ecclesia-15-f / n7 | Grosseteste: higher angel illuminated by a lower | to-verify | |
| E15f-7 | ecclesia-15-f / n18 | D.96 c.14 *Constantinus* | verified | Friedberg; c.13 also begins *Constantinus*, noted |
| E15g-1 | ecclesia-15-g / n2 | Urban VI elected April 1378, Clement VII Sept. 1378; England for Urban | checked | no error found (Sonnet, memory) |
| E15g-2 | ecclesia-15-g / n4 | Gregory XI's 1377 condemnation; the "four truths"/"four heresies" | to-verify | |
| E15g-3 | ecclesia-15-g / n5 | Ambrose "epistola XXXVIII" on Gal. 3:13 | to-verify | Maurist Ep. 38 does not fit; Ep. 21 §25 closest; Wyclif's numbering unknown |
| E15g-4 | ecclesia-15-g / n6 | Wyclif's condemned conclusion on binding and loosing | to-verify | |
| E15g-5 | ecclesia-15-g / n7 | "papal laws" that Peter's successors could err (D.40 c.6?) | to-verify | |
| E15g-6 | ecclesia-15-g / n10 | King John's 1213 surrender and 1000-mark render | checked | no error found (Sonnet, memory) |
| E15g-7 | ecclesia-15-g / n12 | bishop of Rochester = Thomas Brinton OSB; which parliament | checked | Brinton OSB, Rochester 1373–89; parliament still open |
| E15g-8 | ecclesia-15-g / n13–14 | condemned conclusion: lords may take a delinquent church's temporals | to-verify | |
| E15g-9 | ecclesia-15-g / n15 | the 1377 bulls ordering arrest | to-verify | |
| E15g-10 | ecclesia-15-g / n16 | condemned conclusion on charters "humanly devised" | to-verify | |
| E15g-11 | ecclesia-15-g / n17 | C.23 q.4 *Due sunt* (or D.96 c.10 *Duo sunt*?) | verified | Gratian d.p.c.23 *Duae sunt necessitates* (Boethius, *Cons.* V pr. 6) |
| E15h-1 | ecclesia-15-h / n7 | *de necessitate salutis* echoes *Unam sanctam* (Extrav. comm. 1.8.1) | to-verify | |
| E15h-2 | ecclesia-15-h / n9 | Gregory XI d. 27 March 1378; Urban VI's breach with the cardinals | checked | no error found (Sonnet, memory) |
| E15h-3 | ecclesia-15-h / n10 | eleven generations transgressing the decalogue: Aug. *De civ. Dei* 15.20 | verified | PL 41, *De civ.* 15.20 |
| E15h-4 | ecclesia-15-h / n14 | A's Czech gloss after *scriptura sacra* (359.4) | editor | p. 359 foot |
| E16a-1 | ecclesia-16-a / n11 | D.96 c.14 *Constantinus* | verified | Loserth 361 foot *c. XIV*; Friedberg |
| E16a-2 | ecclesia-16-a / n13 | D.95 c.5 *Olim* | verified | Friedberg |
| E16a-3 | ecclesia-16-a / n13 | the *Olim* saying is Jerome on Titus 1:5 | verified | Friedberg inscription *Ieronimus supra epistolam ad Titum* |
| E16a-4 | ecclesia-16-a / n14 | the Greeks' letter to John XXII and its closing clause | to-verify | no source in Loserth |
| E16a-5 | ecclesia-16-a / n15 | *si quid utile est, in scriptura sacra invenitur* ≈ Aug. *De doctr. christ.* 2.42.63 | verified | paraphrase of *De doctr. christ.* 2.42.63 (PL 34); note says cf. |
| E16a-6 | ecclesia-16-a / n16 | "epistola VIII ad Jeronymum" = Aug. Ep. 82 (codd. *nona*) | probable | by content (Ep. 82.3); Loserth *Opp. II, pag. 45*; codd. *nona* |
| E16c-1 | ecclesia-16-c / n1 | Nicholas the deacon shared his wife (patristic story) | verified | Aug. *De haer.* 5 (PL 42) |
| E16c-2 | ecclesia-16-c / n2 | *clerus*/*sors* pun = Jerome Ep. 52.5 | verified | PL 22 |
| E16c-3 | ecclesia-16-c / n6 | Gregory XI: nephew Raymond's marriage to the heiress of "Bolonia", brother's ransom, the killings | to-verify | print *Bolonie*; Boulogne likely (Raymond de Turenne m. Marie of Boulogne, memory) |
| E16c-4 | ecclesia-16-c / n6 | Aug. Sermo 9 *De decem chordis* | editor | Loserth 366 foot |
| E16c-5 | ecclesia-16-c / n8 | Aug. *De natura et gratia* 66 | editor | Loserth 367 foot |
| E16c-6 | ecclesia-16-c / n8 | Aug. *De perfectione iustitiae hominis* | editor | Loserth 367 foot |
| E16c-7 | ecclesia-16-c / n12 | Constantine healed of leprosy at baptism by Silvester | to-verify | *Actus Silvestri* / *Constitutum* |
| E16d-1 | ecclesia-16-d / n1 | St Leonard of Noblac refused a bishopric offered by the Frankish king | to-verify | from memory |
| E16d-2 | ecclesia-16-d / n2 | Angel's voice at the donation (*hodie diffusum est venenum*) | untraced | not in PL TEI; commonplace (Jacopo della Lana *diffusum*); note says so |
| E16d-3 | ecclesia-16-d / n3 | Decree "with Augustine" on Nebuchadnezzar's salvation = C.23 q.4 c.22 | verified | Friedberg; PL 187 1182D |
| E16d-4 | ecclesia-16-d / n5 | Thomas the apostle gave the king's money to the poor (*Acts of Thomas*) | to-verify | from memory |
| E16d-5 | ecclesia-16-d / n5 | Laurence distributed the church's treasure (Ambrose, *De off.* 2.28) | verified | PL 16 (6974.xml) *Hos thesauros demonstravit Laurentius* |
| E16d-6 | ecclesia-16-d / n7 | Lord of Winchester = William of Wykeham; New College 1379 | to-verify | from memory |
| E16d-7 | ecclesia-16-d / n10 | Islip founded Canterbury Hall; Langham expelled the seculars; Wyclif warden | to-verify | Loserth cites Lechler I 204, 303 |
| E16d-8 | ecclesia-16-d / n10 | *Gloria episcopi* = C.12 q.2 c.71, from Jerome | verified | Loserth 371; modern form ours |
| E16e-1 | ecclesia-16-e / n2 | Aug. *De doctr. christ.* 2.42.63 | verified | wording matches; *regimen rei publice* is Wyclif's gloss |
| E16e-2 | ecclesia-16-e / n8 | FitzRalph, *Defensio curatorum*, numbers at Oxford | editor | Loserth 374 |
| E16e-3 | ecclesia-16-e / n13 | Ambrose, *De off.* 2.28 = C.12 q.2 c.70 | verified | Loserth 376; modern form ours |
| E16f-1 | ecclesia-16-f / n4 | *Felix quem faciunt aliena pericula cautum*, proverb; cf. Plautus | editor | Loserth 377 |
| E16f-2 | ecclesia-16-f / n8 | Hugh of St Victor, *De sacr.* 2.2.3 and 2.2.7 | verified | PL 176 417C–D, 420A–C; quote bounds checked |
| E16f-3 | ecclesia-16-f / n10 | Augustine asked his citizens to take back possessions given him | to-verify | from memory (Possidius / sermons) |
| E16g-1 | ecclesia-16-g / n2, n8 | *unius non apostoli* = Silvester; *Cesar* = Constantine | to-verify | our inference from ch. 16 usage |
| E16g-2 | ecclesia-16-g / n3 | *Deus malus … Deum bonum* alludes to the Manichees' two gods | verified | standard reference |
| E16g-3 | ecclesia-16-g / n4 | Condemning "the laws of our kingdom" before the curia = delation of Wyclif's conclusions, Gregory XI's bulls 1377 | to-verify | our inference |
| E16h-1 | ecclesia-16-h / n4 | Augustine's "37th" letter to Macedonius = Ep. 153.6.20 | verified | by content; Wyclif's number unmatched (Gratian: LIV) |
| E16h-2 | ecclesia-16-h / n4 | *Si res* = C.14 q.6 c.1 | verified | Loserth; modern form ours |
| E16h-3 | ecclesia-16-h / n5 | *Commentator* = Averroes on those who deny that creatures act | to-verify | from memory; not located in a quick search |
| E17a-1 | ecclesia-17-a / n1 | The ten arguments at the end of ch. 5 (cf. p. 112.18) | editor | Loserth 388 |
| E17a-2 | ecclesia-17-a / n6 | Aug. *De doctr. christ.* 3.6.10 | verified | PL 34 68–69 |
| E17a-3 | ecclesia-17-a / n8 | Aug. *Retract.* 1.13.3, on *De vera religione* 10.19 | verified | PL 32 603–604 |
| E17b-1 | ecclesia-17-b / n1 | Augustine's text in C.32 q.4 c.2 | verified | Friedberg: canon *Recurrat*, Aug. *In Ioh.* 11 |
| E17b-2 | ecclesia-17-b / n1 | Chrysostom: the church was from the beginning of the world | untraced | not in PL TEI |
| E17b-3 | ecclesia-17-b / n3 | Aug. on Ps. 142: *Ecclesia que est mulier antiqua … ab Abel* | verified | PL 37 1846; paraphrase |
| E17b-4 | ecclesia-17-b / n3 | *Quaest. vet. et novi test.* q. 3: *Ab inicio genus est christianorum* | verified | PL 35 2219 |
| E17b-5 | ecclesia-17-b / n3 | *Quaestiones* now ascribed to Ambrosiaster | to-verify | from memory |
| E17b-6 | ecclesia-17-b / n6 | *De doctr. christ.* 3.32 = Tyconius's rule of the Lord's twofold body | verified | PL 34 82 |
| E17b-7 | ecclesia-17-b / n8 | Gregory, *Hom. in evang.* 1.19, the vineyard | verified | PL 76 1154–5 |
| E17b-8 | ecclesia-17-b / n8 | Gregory's hours = ages of the world | verified | PL 76 |
| E17b-9 | ecclesia-17-b / n11 | *ecclesia* = convocation, *synagoga* = congregation (Augustine, Isidore) | to-verify | from memory |
| E17c-1 | ecclesia-17-c / n1, n10 | Ps.-Aug. *Quaest. vet. et novi test.* 47 on Isa. 4:1 | verified | PL 35 2247–8; *significatas* confirms Loserth |
| E17c-2 | ecclesia-17-c / n4 | Dionysian purging, illuminating, perfecting (*Cel. Hier.*) | to-verify | from memory |
| E17c-3 | ecclesia-17-c / n15 | Loserth compares p. 112.30 | editor | Loserth 398.17 |
| E17d-1 | ecclesia-17-d / n3 | "Super Johannem, Sermone CXXIII": Loserth reads Sermo 270 (alias 13) | editor | Loserth 399.15, Opp. V.1 415 |
| E17d-2 | ecclesia-17-d / n3 | *Non enim a Petro petra … a Christo vocatur* = *Tract. in Ioh.* 124.5 | verified | PL 35, verbatim |
| E17d-3 | ecclesia-17-d / n4 | Grammarians derive *Christus* from *chrisma* (Isidore) | verified | Etym. 7.2.2 |
| E17d-4 | ecclesia-17-d / n8 | *lapis quasi ledens pedem*: Isidore, *Etym.* 16.3.1 | verified | Etym. 16.3.1 verbatim |
| E17d-5 | ecclesia-17-d / n10 | Israel = *vir videns Deum* (Jerome) | verified | Jerome, PL 23 |
| E17d-6 | ecclesia-17-d / n11 | Aug. *In Ioh.* tract. 124, the last homily | editor | Loserth 401.15: Opp. III.2 822 |
| E17d-7 | ecclesia-17-d / n12 | *Opus imperfectum* hom. 52 | editor | Loserth 401.22: p. CCXVIII |
| E17d-8 | ecclesia-17-d / n12 | *Opus imperfectum* is not Chrysostom's | to-verify | from memory |
| E17d-9 | ecclesia-17-d / n13 | Porphyry, *Isagoge*, on the senses of *genus* | to-verify | from memory |
| E17e-1 | ecclesia-17-e / n2 | Ep. "XLII" = Aug. ad Asellicum (Opp. II 734) | editor | Loserth 402.33 |
| E17e-2 | ecclesia-17-e / n2 | = Ep. 196 modern; wording | verified | PL 33, Ep. 196 §12; paraphrase |
| E17e-3 | ecclesia-17-e / n7 | Retract. I (Opp. I 29); cf. Eccl. 113.14 | editor | Loserth 404 |
| E17e-4 | ecclesia-17-e / n7 | = Retract. 1.13.3 | verified | PL 32 603 |
| E17e-5 | ecclesia-17-e / n12 | De Trin. XIII (Opp. VIII 932, 929) | editor | Loserth 405.12, 405.22 |
| E17e-6 | ecclesia-17-e / n12 | quotation = De Trin. 13.2.5 | verified | PL 42; loose quotation, Aug. *quam* |
| E17f-1 | ecclesia-17-f / n9 | "Firmiter" = X 1.1.1, not Clementines | verified | Friedberg X 1.1.1 |
| E17f-2 | ecclesia-17-f / n9 | faith infused in baptism = Clem. 1.1.un. *Fidei catholicae* | verified | Friedberg Clem. 1.1.un. |
| E17f-3 | ecclesia-17-f / n10 | cf. De civ. dom. p. 288 | editor | Loserth 408.31 |
| E17f-4 | ecclesia-17-f / n12 | Tyconius rule 2 = De doctr. 3.32.45 | verified | PL 34 |
| E17f-5 | ecclesia-17-f / n13 | "Ephes. VI" = Eph 5:30–32 | editor | Loserth 409.18 |
| E17f-6 | ecclesia-17-f / n18 | Aug. "super Johannis Omelia XLIX" (Tract. 45.12?) | probable | Tract. 49.27; not word for word |
| E17g-1 | ecclesia-17-g / n3 | Joh. Teutonicus gloss, D.17 c. *Generalia*, general council | to-verify | Glossa ord. |
| E17g-2 | ecclesia-17-g / n6 | "Dist. XV vel XVI. Omnibus non extat" | editor | Loserth 412.2 |
| E17g-3 | ecclesia-17-g / n6 | four councils as four gospels = D.15 c.2 *Sicut sancti evangelii* | verified | Friedberg D.15 c.2 |
| E17h-1 | ecclesia-17-h / n6 | Aug. *Enchiridion* "64", Loserth corrects to 57 (church in the angels) | verified | PL 40, Ench. 56–57 |
| E18a-1 | ecclesia-18-a / n2 | cf. p. 114.23 | editor | Loserth |
| E18a-2 | ecclesia-18-a / n3 | Aquinas, *In III Sent.* d.13 q.2, solutio | to-verify | Loserth: Opp. IX 156; article and wording |
| E18a-3 | ecclesia-18-a / n5 | Aquinas, same place, ad 3 (hand to be cut off) | to-verify | |
| E18a-4 | ecclesia-18-a / n6 | Aug. *De doctr. christ.* 3.32.45 | verified | PL 34 (brief 35, E17f-4) |
| E18a-5 | ecclesia-18-a / n6 | "Ep. 32 ad Bonifacium" = Ep. 98 (alias 23) | verified | PL 33, Ep. 98.5 |
| E18a-6 | ecclesia-18-a / n6 | Wyclif, *De civ. dom.* 1.2, p. 15 | editor | Loserth |
| E18a-7 | ecclesia-18-a / n7 | Aug. *Tract. in Ioh.* 45 (codd. 49), *secundum predestinationem dicta sunt* | verified | PL 35, Tract. 49.27 (codd. right) |
| E18a-8 | ecclesia-18-a / n8 | Richard of St Victor, *De pot. ligandi* 2.20 | verified | PL 196, c. 20 |
| E18a-9 | ecclesia-18-a / n10 | cf. p. 114.31 | editor | Loserth |
| E18a-10 | ecclesia-18-a / n11 | Aug. to Boniface, *sine macula vel ruga* | verified | PL 33, Ep. 185 §§38–40; paraphrase |
| E18b-1 | ecclesia-18-b / n1 | Aug. *Ench.* 64, 65, 69 | verified | PL 40 |
| E18b-2 | ecclesia-18-b / n1 | *Quaest. VNT* 47 | verified | PL 35 2247–8 (brief 34, E17c-1) |
| E18b-3 | ecclesia-18-b / n6, n12, n14 | Johannes Monachus, gloss on VI 1.6.17 *Fundamenta* | editor | modern form ours; wording to check |
| E18b-4 | ecclesia-18-b / n6 | Savigny VI.103; Jöcher II.1933 | editor | Loserth |
| E18b-5 | ecclesia-18-b / n8 | Aug. *Tract. in Ioh.* 124.5 *in aeternitate mansionis* (grounds for emendation) | verified | PL 35; emendation supported |
| E18b-6 | ecclesia-18-b / n9 | *De pen.* D.1 c. *Ecclesia* (Loserth's "C. XXIII q.3 c.70", read XXXIII) | verified | Friedberg I 1180 |
| E18b-7 | ecclesia-18-b / n10 | *Dig.* 23.2.4 *Minorem* | editor | modern form ours |
| E18b-8 | ecclesia-18-b / n16 | Hugh, *De sacr.* 2.1.11 | verified | PL 176 |
| E18b-9 | ecclesia-18-b / n17 | Wyclif's own *De anima* | to-verify | |
| E18b-10 | ecclesia-18-b / n18 | Anselm, *Ep. de incarn. Verbi* c. 7 | verified | PL 158, ch. 6 (Migne) |
| E18b-11 | ecclesia-18-b / n18 | Bernard, *In vig. Nat. Dom.* serm. 3 | verified | PL 183, §8 |
| E18c-1 | ecclesia-18-c / n1 | Aug. *De civ. Dei* 18.50 and 22.28 | verified | PL 41, 18.50; 22.28 does not fit |
| E18c-2 | ecclesia-18-c / n3 | Aug. *Enchiridion* 64 | verified | PL 40 (brief 36, E18b-1) |
| E18c-3 | ecclesia-18-c / n3 | Ambrosiaster, *Quaest. VNT* 47 | verified | PL 35 2247–8 (E17c-1) |
| E18c-4 | ecclesia-18-c / n7 | Gregory, *Hom. in Ev.* 1.16.1 | verified | PL 76 |
| E18c-5 | ecclesia-18-c / n11, n14 | Aug. *Tract. in Ioh.* 49.27 | verified | PL 35 (E18a-7) |
| E18d-1 | ecclesia-18-d / n6 | Jerome, *In Osee* 2, on 9:14 | verified | PL 25; Loserth corrections confirmed |
| E18d-2 | ecclesia-18-d / n8 | Hugh, *De sacr.* 2.2.7 | verified | PL 176; paraphrase |
| E18d-3 | ecclesia-18-d / n9 | Jerome, *In Ioelem* on 1:5 | verified | PL 25 |
| E18d-4 | ecclesia-18-d / n10 | *Op. imperf.* hom. 31 | editor | Loserth p. CXXX |
| E18d-5 | ecclesia-18-d / n11 | Aug. *Enarr. in Ps.* 30, II, s. 3 | verified | PL 36 |
| E18d-6 | ecclesia-18-d / n12 | Gregory, *Reg. past.* 1.2 | editor | |
| E18d-7 | ecclesia-18-d / n12 | Gregory, *Hom. in Ev.* 1.17.14 | editor | Loserth 1503 |
| E18d-8 | ecclesia-18-d / n12 | *Op. imperf.* hom. 18, rather 28 | editor | Loserth p. CXIX |
| E18d-9 | ecclesia-18-d / n13 | *Op. imperf.* hom. 49 | untraced | PG 56 not on disk; Friedberg gives hom. 25 |
| E18d-10 | ecclesia-18-d / n13 | C.11 q.3 c.86 | verified | Friedberg I |
| E18d-11 | ecclesia-18-d / n16 | Aug. *Tract. in Ioh.* 27 | verified | PL 35 |
| E18e-1 | ecclesia-18-e / n1 | Aug. *Tract. in Ioh.* 27 (cont.) | verified | PL 35 |
| E18e-2 | ecclesia-18-e / n3 | Gregory, *Hom. in Ev.* 1.18.5 | editor | |
| E18e-3 | ecclesia-18-e / n6 | Aug. *De verbis Domini*, serm. 50 | verified | PL 38, Sermo 138.9 |
| E18e-4 | ecclesia-18-e / n7 | Jerome, *In Osee* 1, on 2:19 | verified | PL 25 |
| E18e-5 | ecclesia-18-e / n10 | "ut dicit Gregorius" = *Hom.* 1.16.1 | verified | PL 76 |
