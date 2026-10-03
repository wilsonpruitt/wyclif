You are checking Wyclif, De ecclesia (ed. Loserth 1886), chunks 21-d, 21-e, 21-f in ~/wyclif (pp. 502–514; 21-d starts at 502.10, 21-f ends at 514.34).
Do NOT edit any files except your report; report only. Be economical.

Plates: ~/wyclif/text/ecclesia/raw/leaves/nLLLL.jpg, LLLL = printed page + 37, 4 digits (p. 502 → n0539.jpg).
Read the image; margin line numbers are by fives. Established Latin: text/ecclesia/pNNN.la.txt (already corrected for the fixes below; the chunk files may still show the old Latin — compare against pNNN). Chunks:
chunks/ecclesia/wyc-ecclesia-{21-d,21-e,21-f}.md. Loserth's print governs; report what the print shows incl. page-foot
apparatus for the line.

Known loss mechanisms: words lost at PAGE HEADS, at LINE-END HYPHENS (short words: a, et, ex, in, sua, nec, non, sed), mid-line drops, DOUBLINGS, apparatus numerals read as letters (die¹ → diei), line numerals glued to words. Loserth's small enumerator numerals at line ends are apparatus: ignore them.
Already fixed (ignore): 503 domnino→omnino; 505 rantasiandum→fantasiandum; 510 jn→in; 512 stray *of* deleted, *4— 7:*→*4—7:*.

PLATE ITEMS (PRINT = "…", OUR = "…", ACTION):
1. 502.11–12 `non oportet ut maneat … quod iste usus`: is a *sed*/*nisi* lost (line end)? Exact print.
2. 506.1 `per inde`: print *perinde* or two words?
3. 505.28 `Ex primo … commento` (second fabrication?): print + apparatus.
4. 506.18 `doctori isti mihi et aliis`: a lost *et*?
5. 506.24–25: quote Loserth's note ("recte si ex non possibili").
6. 507.6 `revertentur`: print + apparatus (*reiterentur*?).
7. 507 ~l.13 `oditum, (ut patet`: is the comma printed?
8. 509.3 `ut patet prioris doctoris`: a lost word (*ex dictis*?)?
9. 510.12 `superius)`: is there an opening bracket earlier in the sentence, or is ")" a scar?
10. 510.25 `corrupto episcopo`; 510.28–34 (no apodosis; *circumcisione*, Loserth "rectius et intercisione"): exact print + apparatus.
11. **511.10 `reminiscere`** (does not construe; we emend to *reviviscere* in the English): what does the print show, and any apparatus? This decides a departure.
12. 513.24 `quod sacerdos celebrat`; 513.29 doubled `tantum`?; 514.14 `pars senarius`; 514.33 doubled `appreciando`?: print readings + apparatus.
13. 512.15: how does the print set the verse numbers *4—7*?
14. Italics: first and last words of every italic run on pp. 502–514; especially quotation ends at 503.1, 503.13 (*Alia possunt fieri argumenta* — inside or outside Bonaventure's quotation?), 503.31, 505.17, 506.26, 507.6, 512.18, 512.29.
15. Page feet: 503.23 (Bonaventure page — 602 or 650? which q.?), 506.32 and 509.5 (Thomas, p. 442 vs 424), 514.24 (*Trial.* page number in full).
16. Systematic: compare EVERY line of pp. 502 (from l.10)–514 word by word with pNNN.la.txt; every line-end hyphen; every page's first/last words. List only discrepancies, plus any other garbage token (stray letters/English words, line numbers, glued/broken words, numerals, lost ª/º after roman numerals, lost or stray punctuation, f read as r/t).

SOURCE ITEMS. PL TEI: ~/patrologia/sources/pl/tei/*.xml (grep -l a phrase).
A. E21d-2: Anselm, Cur Deus homo I.12 (PL 158) — confirm chapter and whether Anselm reads *deum illum* or *dominum*; give the sentence.
B. E21e-2: "Machabeorum VII°", a lie hated in the camps — check 1–2 Maccabees 7 (bible.py: `cd ~/wyclif && .venv/bin/python scripts/w3/bible.py "2 Mac 7:1"` etc.) and say whether anything fits; else "not located".
C. E21f-1: Chrysostom "Omelia prima" on the seven churches — try PL (Ps.-Chrysostom; Opus imperfectum; homilies on the Apocalypse) for *septem ecclesias*; else "not located".
D. E21e-3: Wyclif's earlier statement that some character is only temporal — grep text/ecclesia/p*.la.txt for *caracter* before p. 502.
E. E21e-4: Bonaventure IV d. 24 — anything in Loserth's feet on potestative parts? (No Bonaventure on disk expected.)

Report: numbered verdicts, PRINT/OUR/ACTION or SOURCE/WORDING/ACTION. Under 900 words. Write it to /Users/wilsonpruitt/wyclif/chunks/ecclesia/_briefs/ecclesia-21-d-21-f.CHECK-REPORT.md.
