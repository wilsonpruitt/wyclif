"""Build catalog/volumes.json + volumes.tsv: one row per Wyclif Society volume.

Keyed by a work slug, NOT by archive.org item digits (latinworksNN is Princeton's shelf
order, not a Society volume number). Scan list comes from the CSV; contents were confirmed
against each Princeton scan's title page (Phase 0, 2026-09-28); Fordham coverage comes from
catalog/fordham_map.json (scripts/map_fordham.py). Queue rank + English status are editorial
judgments recorded here so there is one place to change them.
"""
import csv, json

# slug, princeton item, csv work, csv volume, contents (from the title page), queue rank, tier, english status
VOLUMES = [
    ("apostasia",        "latinworks01wycl", "De apostasia", "", "De apostasia", 7, 1, "none known"),
    ("blasphemia",       "latinworks02wycl", "De blasphemia", "", "De blasphemia", 8, 1, "none known"),
    ("incarnacione",     "latinworks03wycl", "De benedicta incarnacione", "", "De benedicta incarnacione", 16, 3, "none known"),
    ("civ-dom-1",        "latinworks04wycl", "De civili dominio", "I", "De civili dominio, liber I", 5, 1, "extracts only (Penn 2019; older selections)"),
    ("civ-dom-2",        "latinworks05wycl", "De civili dominio", "II", "De civili dominio, liber II", 11, 2, "extracts only"),
    ("civ-dom-3a",       "latinworks06wycl", "De civili dominio", "III", "De civili dominio, liber III (tome 1)", 12, 2, "extracts only"),
    ("civ-dom-3b",       "latinworks07wycl", "De civili dominio", "IV", "De civili dominio, liber III (tome 2)", 13, 2, "extracts only"),
    ("compositione",     "latinworks08wycl", "De compositione hominis", "", "De compositione hominis", 17, 3, "none known"),
    ("dominio-divino",   "latinworks09wycl", "De dominio divino", "", "De dominio divino libri tres + FitzRalph, De pauperie Salvatoris I-IV (NOT Wyclif; excluded)", 15, 2, "none known"),
    ("ecclesia",         "latinworks10wycl", "De ecclesia", "", "De ecclesia", 1, 1, "extracts only (Penn 2019; Spinka 1953)"),
    ("ente-excerpta",    "latinworks11wycl", "De ente librorum duorum (Summa de ente, excerpts)", "", "De ente librorum duorum excerpta + Fragmentum de annihilatione", 19, 3, "none known"),
    ("ente-praed",       "latinworks12wycl", "De ente praedicamentali", "", "De ente praedicamentali + Quaestiones XIII logicae et philosophicae", 18, 3, "none known"),
    ("eucharistia",      "latinworks13wycl", "De eucharistia", "", "De eucharistia tractatus maior + De eucharistia et poenitentia sive de confessione", 4, 1, "extracts only (Penn 2019; Spinka 1953)"),
    ("logica-1",         "latinworks14wycl", "Tractatus de logica", "I", "Tractatus de logica I", 21, 3, "none known"),
    ("logica-2",         "latinworks15wycl", "Tractatus de logica", "II", "Tractatus de logica II (Logicae continuatio)", 22, 3, "none known"),
    ("logica-3",         "latinworks16wycl", "Tractatus de logica", "III", "Tractatus de logica III (Logicae continuatio)", 23, 3, "none known"),
    ("mandatis",         "latinworks17wycl", "De mandatis divinis", "", "De mandatis divinis + De statu innocencie", 14, 2, "none known"),
    ("officio-regis",    "latinworks18wycl", "De officio regis", "", "De officio regis", 6, 1, "extracts only"),
    ("potestate-pape",   "latinworks19wycl", "De potestate pape", "", "De potestate pape", 3, 1, "none known"),
    ("simonia",          "latinworks20wycl", "De simonia", "", "De simonia", 26, 4, "FULL English exists (McVeigh 1992, in copyright) - verify"),
    ("veritate",         "latinworks21wycl", "De veritate sacrae scripturae", "I–III", "De veritate sacrae scripturae I-III (one scan, 1144 images)", 25, 4, "ABRIDGED English (Levy 2001, in copyright)"),
    ("dialogus",         "latinworks22wycl", "Dialogus sive Speculum ecclesie militantis", "", "Dialogus sive Speculum ecclesie militantis", 2, 1, "none known"),
    ("misc-phil-1",      "latinworks23wycl", "Miscellanea philosophica", "I", "De actibus anime, Replicacio de universalibus, De materia et forma, etc.", 20, 3, "none known"),
    ("misc-phil-2",      "latinworks24wycl", "Miscellanea philosophica", "II", "De universalibus fragmenta, notae et quaestiones variae (full De universalibus exists in English from the later Mueller ed.)", 24, 3, "overlaps Kenny/Spade 1985 (different edition)"),
    ("opera-minora",     "latinworks25wycl", "Opera minora", "", "Opera minora (incl. De servitute civili et dominio seculari)", 14.5, 2, "none known"),
    ("opus-evang-1",     "latinworks26wycl", "Opus evangelicum", "I", "Opus evangelicum I-II", 10, 1, "none known"),
    ("opus-evang-2",     "latinworks27wycl", "Opus evangelicum", "II", "Opus evangelicum III-IV = De Antichristo I-II", 10.5, 1, "none known"),
    ("polemical-1",      "latinworks28wycl", "Polemical works in Latin", "I", "Polemical works I (short tracts)", 9, 1, "none known (spot-check per tract)"),
    ("polemical-2",      "latinworks29wycl", "Polemical works in Latin", "II", "Polemical works II (short tracts, incl. De solutione Satanae, De mendaciis fratrum)", 9.5, 1, "none known (spot-check per tract)"),
    ("sermones-1",       "latinworks30wycl", "Sermones", "I", "Sermones I (Sunday gospels)", 15.1, 2, "none known"),
    ("sermones-2",       "latinworks31wycl", "Sermones", "II", "Sermones II", 15.2, 2, "none known"),
    ("sermones-3",       "latinworks32wycl", "Sermones", "III", "Sermones III (epistles)", 15.3, 2, "none known"),
    ("sermones-4",       "latinworks33wycl", "Sermones", "IV", "Sermones IV (Sermones miscellanei: XL de tempore, XXIV mixti)", 15.4, 2, "none known"),
]

rows = list(csv.DictReader(open("sources/wyclif_society_archive_org.csv", encoding="utf-8-sig")))
fmap = json.load(open("catalog/fordham_map.json"))
by_item = {}
for fn, m in fmap.items():
    by_item.setdefault(m["best"], []).append(f"{fn} (pp. {m['first_page']}-{m['last_page']})")

out = []
for rank, (slug, item, work, vol, contents, q, tier, eng) in enumerate(sorted(VOLUMES, key=lambda v: v[5]), 1):
    scans = [r for r in rows if r["work"].strip() == work and r["volume"].strip() == vol]
    base = next(r for r in scans if r["ia_identifier"] == item)
    out.append(dict(
        queue=rank, tier=tier, slug=slug, contents=contents, year=base["original_year"], editor=base["editor"],
        english=eng, fordham=by_item.get(item, []), primary_scan=item,
        primary_url=base["archive_url"],
        other_free_scans=[r["ia_identifier"] for r in scans if r["access"] == "Free" and r["ia_identifier"] != item],
    ))

json.dump(out, open("catalog/volumes.json", "w"), indent=1, ensure_ascii=False)
with open("catalog/volumes.tsv", "w") as f:
    cols = ["queue", "tier", "slug", "year", "editor", "english", "fordham", "primary_scan", "contents"]
    f.write("\t".join(cols) + "\n")
    for v in out:
        f.write("\t".join("; ".join(v[c]) if isinstance(v[c], list) else str(v[c]) for c in cols) + "\n")
print(len(out), "volumes;", sum(1 for v in out if v["fordham"]), "with Fordham text")
