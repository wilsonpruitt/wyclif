# Opus translation prompt — reuse per brief (swap the brief name and the E-id prefixes)

*Rebuilt for brief 40 (2026-10-02) from the M5-RESUME loop notes; the brief-39 prompt was not saved.*

---

Read /Users/wilsonpruitt/wyclif/chunks/ecclesia/_briefs/<BRIEF>.md and follow it exactly. It is the only file you need. Write each of the three chunk files ONCE in full, then make the one allowed round of edits (bible.py check, lint).

Standing rules: never alter the Latin. Do not search the Patrologia or other sources (a checker does that later); use "to be checked" with a fresh LEDGER id (<E-id prefixes, e.g. E19h-1, E20a-1 …>). Do not commit anything to git. Give each scar token exactly as it appears in the Latin, including attached punctuation (the coordinator looks tokens up by exact text).

Traps to watch (each one has bitten recent briefs):
- Incipits and case: a capital after a comma may be a concession or a continuation rather than a new sentence. A word that is lower case in the print stays lower case.
- Line-end and page-head/foot short-word losses (a, et, ex, nec, sua …): wherever a sentence does not construe at a line or page boundary, flag the page.line and the suspected lost word. Also flag DOUBLED words (a word repeated across a line end) and LOST brackets (a closing ")" with no opening one).
- Loserth's enumerator numerals and ordinals: ª/º lost after roman numerals (I → Iª, 111° → IIIº), line numerals read as letters (5 → s) or glued to words (2in, ?odist.), apparatus numerals read as letters (die1 → diei), folio marks glued into words (e.g. 190ᶜ → "igoc"). List each one as a scar.
- OCR f read as r or t (roret/foret, tortem/fortem): if a word construes better with f, list it as a scar.
- Stray English words or margin letters (*the*, *N*, *Y*) and leftover brackets from folio marks: list as scars.
- Before proposing any glossary row, grep /Users/wilsonpruitt/wyclif/GLOSSARY.md for the lemma. If a row already exists, follow it; the earlier frozen row wins. Propose only genuinely new terms.
- Print italics mark where a quotation ends. The scaffold carries no italics: place quotation ends by sense and list every quotation end you are unsure of as a Latin doubt for the plate check.
- If you supply a word in brackets, the T note must say "our supply" (the print may well have no loss).

When done, write your full final report (the brief's step 6 content, laid out like /Users/wilsonpruitt/wyclif/chunks/ecclesia/_briefs/ecclesia-19-b-19-d.REPORT.md: per chunk the ledger table, glossary proposals, Latin doubts, scars in the print, and anything for the coordinator, plus plates opened) to /Users/wilsonpruitt/wyclif/chunks/ecclesia/_briefs/<BRIEF>.REPORT.md. Your final message should be the same report.
