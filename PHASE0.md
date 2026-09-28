# Phase 0 — ingest and reconcile (2026-09-28, Opus)

Goal of the project: the **whole Wyclif Society corpus** in English, queued toward the
interesting untranslated texts first. Home: **wyclif.wrootpress.com**. PLAN.md and
CONVENTIONS.md are not written yet — those are the Fable session (see "Next" below).

## What is on disk

| Path | What | In git |
|---|---|---|
| `sources/wyclif_society_archive_org.csv` | Wilson's list: 39 work-volume rows, 147 archive.org scans (129 free) | yes |
| `sources/fordham/*.md` | 18 Fordham transcriptions, `[p. N]` page markers, as received (a derived rendering; see finding 9) | yes |
| `sources/fordham/data/data.json` | **source of record**: the site's structured data, extracted 2026-09-28 | yes |
| `sources/fordham/extract_wyclif.js` | pulls the `JSON.parse('…')` blobs out of Fordham's `main.js` into `data.json`; the data.json→.md step was not supplied | yes |
| `sources/ia-ocr/latinworksNNwycl.txt` | archive.org OCR text of all 33 Princeton volumes (~40 MB) | no — `scripts/fetch_ia_ocr.sh` |
| `catalog/volumes.json`, `.tsv` | one row per Society volume: queue, tier, contents, English status, Fordham coverage, primary + other free scans | yes |
| `catalog/fordham_map.json` | each Fordham file → its printed volume + page range | yes |

Rebuild: `python3 scripts/map_fordham.py && python3 scripts/build_catalog.py`.

## Primary witness

**The Princeton Theological Seminary set, `latinworks01wycl`–`latinworks33wycl`**, is the complete
series in one uniform scan, every item with `_djvu.txt` and hOCR. It is the primary scan for every
volume. ⚠ **The `NN` is Princeton's shelf order (roughly alphabetical), NOT a Society volume
number**, and the archive.org metadata is useless (every item says "Latin works", v.N, 1883).
Contents were confirmed from each scan's own title page. The catalog is keyed by **work slug**;
citations will be **work + Society page**, the scholarly convention.

## Findings

1. **Fordham covers 15 of 33 volumes, about 1.05M Latin words.** Every file matched one Princeton
   volume without ambiguity: the correct volume shared 32–69% of sampled 6-word runs, the next best ≤1%.
   **The full corpus is about 2.6M Latin words** (main text only; estimated from the OCR of the 18
   volumes Fordham does not cover, at Fordham's text-to-page ratio of 0.49).
2. **Fordham's header dates are wrong** (e.g. De civili dominio I "1904" = Poole 1885; De
   compositione hominis "1887" = Beer 1884). Catalog dates come from the CSV. Fordham's
   `De_Civili_Dominio_I/II` are **liber I and liber II**. Liber III (two tomes, Princeton 06–07) has
   no Fordham text.
3. **Fordham carries the main text only.** Apparatus, source notes, the English marginal
   summaries (side-notes) and the introductions are absent. That is why main text runs ~49% of each
   volume's OCR word count. The side-notes are PD English and a free navigation layer. Recover
   them from hOCR in Phase 2.
4. **Fordham is uncorrected OCR.** Seen in one page of De officio regis: `wltfacere`, `Sicul`
   (=sicut), `edifacta`. Every text gets a correction pass against the plates before translation.
5. **The page runs are complete except for 14 gaps:** De officio regis pp. 26, 66; Sermones I pp.
   67, 100, 104, 115, 117, 151, 159, 177, 197, 209; Sermones II pp. 5, 36. Each could be a blank or
   a real drop. Check against the plates.
6. **Fordham's chapter divisions are unreliable** (De civili dominio I = 105 "chapters"; De logica
   III = 4 across 227 pp). Recover structure from the plates, never from the `##` headings.
7. **Volume contents the CSV does not show** (from the title pages):
   - `dominio-divino` also prints **FitzRalph, *De pauperie Salvatoris* I–IV — not Wyclif, excluded**
     (possible later context layer). Fordham's De_Dominio_Divino stops at p. 256, before it.
   - `eucharistia` + *De eucharistia et poenitentia sive de confessione*.
   - `mandatis` + *De statu innocencie*.
   - `ente-praed` + *Quaestiones XIII* (Fordham's `XIII_Quaestiones` = pp. 223–305 of that volume).
   - `ente-excerpta` + *Fragmentum de annihilatione* (Fordham's `De_Annihilatione` = pp. 287–315).
   - `opus-evang-2` = Opus evangelicum III–IV, i.e. *De Antichristo* I–II.
   - `veritate` = all three volumes in one scan (1144 images).
8. **Rights: settled 2026-09-28.** Source: *The Latin Works of John Wyclif*,
   https://www.library.fordham.edu/wyclif/#/ (J. Patrick Hornbeck II and Christopher Adams; begun at
   Georgetown CNDLS 2003, hosted by Fordham University Libraries). Its copyright page, quoted from the
   site's `main-es2015.*.js`: *"With the exception of Wyclif's Tractatus de Trinitate, all of the
   editions of Wyclif's writings contained on this site exist in the public domain in the United
   States as well as in their country of original publication."* The one exception, Breck's 1962
   *De Trinitate* (digitised by permission), is **not in our data** and is not a Wyclif Society
   volume, so it stays out. "All rights reserved" covers **only the site design**. **Use the
   text freely and credit the project on the site** ("Latin text of the Fordham volumes from *The
   Latin Works of John Wyclif*, ed. J. P. Hornbeck II and C. Adams, Fordham University Libraries,
   corrected against the Wyclif Society plates"). English + encoding = CC BY-NC 4.0 per house policy.
9. **The source of record is now `sources/fordham/data/data.json`,** extracted by running
   `extract_wyclif.js` on the live site's JS on 2026-09-28. It holds titles, chapters, paragraphs
   (with `_order`, and `split` for paragraphs that run across a page) and pages. The zip's `.md`
   files are a derived rendering. `scripts/fordham_to_md.py SLUG` regenerates them: Dialogus,
   De compositione hominis, De dominio divino, Civ. dom. II and the XIII Quaestiones come out
   byte-identical. The rest differ only because the zip turned `<i>` into `*` and misplaced some
   chapter headings (e.g. De blasphemia p. 46 sits under a later "Capitulum Primum"). **Take
   structure from data.json, never from the zip.**
   - The live data has **no more text than the zip.** `opera-minora` has 435 page records but
     **no paragraphs**. `de-apostasia`, `de-eucharistia` and `de-ente` are empty title
     placeholders; `de-simonia` has one page. Fordham's page images (`pages_to_display/…jpg`) are
     not served at any path I could find. Use the archive.org plates.

## English landscape (quick check, 2026-09-28 — firm up in the PLAN session)

There is **no complete modern English of any major treatise in the series** except, from memory,
*De simonia* (McVeigh 1992). Otherwise:
- Stephen Penn, *John Wyclif: Selected Latin Works in Translation* (Manchester UP, 2019): extracts
  from De civili dominio, De ecclesia, De eucharistia and others. Severely criticised by Mark
  Thakkar, "Duces caecorum: On Two Recent Translations of Wyclif", *Vivarium* 58 (2020) 357–83
  (also reviews Lahey's *Trialogus*, CUP 2013). **Read Thakkar before the pilot**: it is a
  catalogue of the traps in Wyclif's Latin.
- Levy, *On the Truth of Holy Scripture* (2001): abridged.
- Spinka, *Advocates of Reform* (LCC 14, 1953): extracts.
- *De universalibus* (Kenny/Spade 1985) and *Trialogus* (Lahey 2013) are outside the series.

## The queue (judgment call, recorded in `scripts/build_catalog.py`)

**Tier 1: church, papacy, eucharist, lordship.** These are the texts that got Wyclif condemned
and that Hus took over nearly wholesale. They have extracts at most in English.
1 De ecclesia · 2 Dialogus (short, has Fordham text: the early publishable win) · 3 De potestate
pape · 4 De eucharistia · 5 De civili dominio I · 6 De officio regis · 7 De apostasia · 8 De
blasphemia · 9–10 Polemical works I–II (short tracts, good site pieces) · 11–12 Opus evangelicum
incl. De Antichristo (his last work).

**Tier 2: the rest of the dominion and ethics writings, and the sermons.** De civili dominio II–III ·
De mandatis divinis · Opera minora · De dominio divino · Sermones I–IV.

**Tier 3: philosophy.** De benedicta incarnacione · De compositione hominis · De ente
praedicamentali · De ente excerpta · Miscellanea philosophica I · De logica I–III · Misc. phil. II
(overlaps the English De universalibus).

**Tier 4: English exists.** De veritate (abridged) · De simonia (full).

⚠ **Tier 1 is mostly outside Fordham.** Only 4 of its 12 volumes have Fordham text, so the OCR
correction in Phase 2 is on the critical path from the first item.

## Next

**Superseded 2026-09-28 by `PLAN.md`** (the pilot is drafted; see M1). The list below is kept as written.

- ~~Wilson owes the Fordham URL~~: received, rights settled (finding 8).
- **Fable session:** write `PLAN.md` + `CONVENTIONS.md` + `GLOSSARY.md` and run the pilot on a
  chapter of De ecclesia (plate-read, no Fordham text) and a chapter of the Dialogus (Fordham text
  corrected against the plate). That tests both text paths and the core register. Notes numbered
  and anchored from the first chapter.
- Then Phase 2 (Opus): per-volume text preparation from hOCR + plates, in queue order, plus the
  side-note layer.
- ⚠ Before any volume translation run: a token estimate and Wilson's go (≈2.6M Latin words).
