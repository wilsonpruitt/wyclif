# Boundaries audit: *De ecclesia*, 58 stopless ¶ and chunk ends

Source list: `text/ecclesia/boundaries.tsv`. Each row was checked on the plate (`raw/leaves/n{page+37}.jpg`).
The page.line is the printed line where the print continues, or where it has the stop. The line numbers in our ¶ headers are sometimes one line off from the print (e.g. 514.30–32); the numbers below follow the print.

| # | chunk | ¶ | verdict | page.line | detail |
|---|---|---|---|---|---|
| 1 | 02-f | ¶1 | TRUE | 43.23/24 | Print reads `capitulo —).`: a blank chapter number and a close-paren, with a stop. 43.24 `Ex istis patet secundo` is indented. No word is lost, but our text ends at bare `capitulo` and is missing `—).` |
| 2 | 02-f | ¶4 | FALSE-BREAK | 46.24 | `superiores nostri / plus exigunt`: no indent, so merge ¶4+¶5. *plus* has already been restored. |
| 3 | 02-f | ¶5 | **LOST** | 47.5 | Print: `supplantacio legis / ⁵Christi etc.` Missing: **Christi etc.** The chapter ends there (rule, then CAP. III), so the end itself is TRUE. |
| 4 | 03-d | ¶1 | FALSE-BREAK | 60.5 | `esse / membra Christi in potencia`. The break came from a side-note ("Others receive it…"). |
| 5 | 04-d | ¶4 | FALSE-BREAK | 84.11 | `domini, / sed continue membra diaboli`. Side-note. |
| 6 | 05-a | ¶4 | **LOST** | 95.2 | Print: `est independens / C 141ᶜ a regimine* pape`. Missing: **a** (our ¶5 starts with `regimine`). Also, the print's real new paragraph is at 95.1 (indent + alinea C before `Regnum ergo`), so the ¶ break belongs before `Regnum`, not after `independens`. |
| 7 | 05-b | ¶2 | VERSE/HEADING | 97.5 | `Rex Salomon fecit templum`: verse line. |
| 8 | 05-b | ¶3 | VERSE/HEADING | 97.6 | Verse line. |
| 9 | 05-b | ¶5 | VERSE/HEADING | 97.8 | Verse line. |
| 10 | 05-b | ¶7 | VERSE/HEADING | 97.11 | Verse line. |
| 11 | 05-b | ¶8 | VERSE/HEADING | 97.12 | Verse line. |
| 12 | 06-e | ¶3 | TRUE (shifted) | 133.25/26 | Print: `spiritualiter virgo.` then an indented `Q Sed dubium est` at 133.26. Nothing is lost, but `Sed` sits on the wrong side of the chunk end: move it to the start of 06-f. |
| 13 | 08-d | ¶1 | FALSE-BREAK | 169.29 | `de matre / filiorum Zebedei`. Side-note. |
| 14 | 08-d | ¶3 | TRUE | 170.20/21 | Print: `vanitas est.` then an indented `Tercio notandum`. Ours has a comma; the print has a stop. |
| 15 | 09-e | ¶2 | VERSE/HEADING | 199.11 | Hymn verse. |
| 16 | 09-e | ¶3 | VERSE/HEADING | 199.12 | Hymn verse. |
| 17 | 09-e | ¶4 | VERSE/HEADING | 199.13 | Hymn verse. |
| 18 | 12-c | ¶1 | CHUNK-SPLIT | 263.33 | Ends at 263.26 `patet / quod hoc`. The next stop is `nunquam permittenda.` at 263.33. 263.34 `Quoad terciam` is an indented paragraph that our 12-d ¶1 merges. |
| 19 | 12-d | ¶2 | **LOST** | 265.1 | Print: `clerici / K 166ᵃ et vulgares approbarunt`. Missing: **et** (our ¶3 starts with `vulgares`). The break is also false: an alinea letter at the page turn. |
| 20 | 14-e | ¶2 | FALSE-BREAK | 317.1 | `quod / N 173ᵇ in hiis tribus locis`. Alinea letter at the page turn. |
| 21 | 15-a | ¶2 | FALSE-BREAK | 330.31 | `quam / regnum processit prospere`. Side-note ("3. The realm…"). Our ¶2 already holds `regnum`. |
| 22 | 15-c | ¶1 | FALSE-BREAK | 338.12 | `ipsam / dotare ad enervacionem`. Side-note. |
| 23 | 16-d | ¶3 | **LOST** | 372.2 | Print: `suaderi potest 180ᶜ L / tripliciter. Primo per hoc`. Missing: **tripliciter.** (16-e ¶1 starts with `Primo`). The stop for the chunk end is right after it, at 372.2. |
| 24 | 16-e | ¶5 | CHUNK-SPLIT | 377.2 | Ends `superflua / sed et calices` (376.28/29). The next stop is `necessarii sunt.` at 377.2. |
| 25 | 16-g | ¶4 | FALSE-BREAK | 382.17 | `emere / sibi beatitudinem`. Side-note. |
| 26 | 16-g | ¶5 | FALSE-BREAK | 384.1 | `inquiri / quantum de bonis regni` (182ᵇ V). Alinea letter at the page turn. |
| 27 | 17-c | ¶1 | FALSE-BREAK | 398.2 | `pro / suo tempore christiani` (184ᵃ G). Alinea letter and side-note. |
| 28 | 17-c | ¶2 | FALSE-BREAK | 398.13 | `habebunt / omnia membra`. Side-note "c)". |
| 29 | 17-f | ¶2 | FALSE-BREAK | 409.2 | `de ecclesia / pro tempore`. Alinea letter O at 409.1. |
| 30 | 18-a | ¶1 | CHUNK-SPLIT | 418.6 | Ends `sanctorum / et ecclesia` (418.1/2). The next stop is `cap. XLVII°.` at 418.6. |
| 31 | 18-e | ¶2 | CHUNK-SPLIT | 435.28 | Ends `iuvenis, / nec ipsa` (435.25/26). The next stop is `vel de ecclesia.` at 435.28. |
| 32 | 18-f | ¶3 | VERSE/HEADING | 438.19 | Hymn verse. |
| 33 | 18-f | ¶4 | VERSE/HEADING | 438.20 | Hymn verse. |
| 34 | 18-f | ¶5 | VERSE/HEADING | 438.21 | Hymn verse. |
| 35 | 19-b | ¶3 | TRUE | 449.15/16 | Print: `vulneratus sanet.` then an indented `H 2 Item, iudex`. Ours has a comma; the print has a stop. |
| 36 | 19-c | ¶1 | FALSE-BREAK | 450.5 | `necessaria / instrumenta` within one line. Side-note. |
| 37 | 19-c | ¶3 | FALSE-BREAK | 450.29 | `predicta / scit si alius`, mid-line. |
| 38 | 19-c | ¶4 | FALSE-BREAK | 451.1 | `nec iudex / I 190ᵈ ex quacunque`. Alinea letter at the page turn. |
| 39 | 19-d | ¶4 | CHUNK-SPLIT | 458.5 | Ends `conficiendo / vel absolvendo` (457.29/30). The next stop is `sive catholica.` at 458.5. |
| 40 | 19-g | ¶2 | CHUNK-SPLIT | 469.1 | Ends `a regulis / X 193ᵇ et iudiciis prime iusticie.` The stop is at 469.1. |
| 41 | 20-b | ¶2 | FALSE-BREAK | 476.15 | `fertiliter dotata / a viro`. Side-note "Verse 12". |
| 42 | 21-b | ¶2 | FALSE-BREAK | 498.8 | `dupliciter / potest intelligi`. Side-note. |
| 43 | 21-f | ¶3 | FALSE-BREAK | 514.21 | `secundo / quod sicut res`. Side-note. |
| 44 | 21-f | ¶4 | FALSE-BREAK | 514.24 | `Nam / oportet recipientem`. Side-note. |
| 45 | 21-f | ¶5 | FALSE-BREAK | 514.30 | `appreciando / intendimus`, mid-line. Side-note. |
| 46 | 21-f | ¶6 | CHUNK-SPLIT | 515.2 | Ends `magis / T 199ᵇ attendimus ad folia`. The next stop is `vilescere.` at 515.2. 515.3 `U Sic enim` is an indented paragraph that our 21-g ¶1 merges. |
| 47 | 21-g | ¶1 | FALSE-BREAK | 515.11 | `sacramentalium, / sed veritas`, mid-line. Side-note. |
| 48 | 21-g | ¶2 | FALSE-BREAK | 515.13 | `sacerdotalem / caracterem nec habent`. Side-note. 515.15 `Ex istis tercio` is an indented paragraph that our ¶3 merges. |
| 49 | 21-g | ¶3 | FALSE-BREAK | 515.19 | `et post / ascensionem tempore apostolorum`, mid-line. |
| 50 | 22-b | ¶1 | FALSE-BREAK | 523.1 | `pene, / C 200ᵃ in paradiso`. Alinea letter at the page turn. 523.3 `D Quintum et ultimum` is an indented paragraph that our ¶2 merges. |
| 51 | 22-d | ¶1 | FALSE-BREAK | 530.2 | `pro eis / tunc efficacia`. Alinea letter I and side-note. |
| 52 | 22-d | ¶2 | CHUNK-SPLIT | 532.27 | Ends `vel / quoad voluntatem` (532.20/21). The next stop is `persona ecclesie.` at 532.27. 532.19 `Et ad primam confirmacionem` is an indented paragraph that our ¶2 merges. |
| 53 | 22-f | ¶2 | CHUNK-SPLIT | 538.18 | Ends `De exequiis vero / et aliis` (538.13/14). The next stop is `mala moraliter.` at 538.18. |
| 54 | 23-c | ¶9 | FALSE-BREAK | 558.23 | `conclusio, / sed non credamus`. Side-note. |
| 55 | 23-c | ¶10 | CHUNK-SPLIT | 558.26 | Ends `pro debito / illius ad salutem` (558.23/24). The next stop is `iuxta opera sua.` at 558.26. |
| 56 | 23-e | ¶3 | FALSE-BREAK | 564.23 | `in preteritum / cum omnibus`. Side-note. |
| 57 | 23-i | ¶4 | FALSE-BREAK | 576.2 | `curato / licenciam indulgendi`. Side-note. |
| 58 | 23-i | ¶5 | CHUNK-SPLIT | 576.8 | Ends `quia / tunc nunquam` (576.2/3). The next stop is `potenciam indulgendi.` at 576.8. |

## Counts

| verdict | n |
|---|---|
| FALSE-BREAK | 28 |
| CHUNK-SPLIT | 11 |
| VERSE/HEADING | 11 |
| TRUE | 4 (incl. 1 shifted: #12) |
| LOST | 4 |
| **total** | **58** |

### Lost words
- **47.5** `Christi etc.`: after `supplantacio legis`, at the end of cap. II.
- **95.2** `a`: `independens a regimine pape`. The ¶ break also belongs before `Regnum` (95.1).
- **265.1** `et`: `clerici / et vulgares approbarunt`.
- **372.2** `tripliciter.`: `suaderi potest / tripliciter. Primo per hoc`.

### Punctuation only
- 43.23: print `capitulo —).`, ours `capitulo`.
- 170.20: print `vanitas est.`, ours `est,`.
- 449.15: print `sanet.`, ours `sanet,`.

### Seen in passing (outside the 58): indented print paragraphs that our ¶s merge
263.34, 515.3, 515.15, 523.3, 532.19.
