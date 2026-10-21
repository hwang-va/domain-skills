---
name: sort-level1
description: "Trigger: /domain:sort-level1 or sort candidates, place facts, build the domain files request. Outcome: domain files written, one row per fact with ID, sources, tag, duplicates merged, conflicts to unknowns, from candidate registers and the folder README, counts inline."
---
# Sort-Level1
Goal: Place candidate facts into the domain folder files, entity resolution and golden-record practice for merging the same fact from several sources (Fellegi-Sunter record linkage; Evans's ubiquitous language, one name per concept), IDs per the Contract.
Target: `domains/<name>/candidates/*.md` user points at, all of them unless one is named; `domains/<name>/README.md` supplies the charter and roles; existing bin files, if present, are read so a fact already placed is cited, not duplicated; `${CLAUDE_PLUGIN_ROOT}/references/domain-bins.md` supplies prefixes, columns, and cross-bin rules.
Scope: Place: every candidate line into one file by its bin; a line whose bin fails the test is re-tested, placed, and noted. Merge: the same fact from several harvests becomes one row listing every source; the surviving tag is the best grade, Verified over Reported over Inferred; a merged-away line's wording is kept as a synonym on the row. IDs: `EN`, `DT`, `RU`, `KN`, `PR`, `TL`, `EX`, `UN`, numbered in placement order, never reused. Conflict: two candidates that contradict each other, or a term meaning two things, become one `UN` row with both sources; the test decides the bin, never a coin flip. Pains: copied to a holding block at the end of `roles.md` for `roles-level1`; never a bin row. Cut: writing the role map, the charter, the README counts, judging whether a fact is true.
Reference: `${CLAUDE_PLUGIN_ROOT}/references/domain-bins.md`: Catalog, the bin test, register shapes, cross-bin rules; if absent, stop and say so.
Output: Files written, then inline: counts per file, merged pairs, conflicts, placed-and-noted lines, divider, unknowns added.

## Process
1. Gather: Read every candidate register and every existing bin file; list candidates with their bin, source, tag.
2. Resolve: Group candidates that name the same fact across harvests and files; one survivor per group with all sources, best tag, synonyms kept, because two rows for one noun is the drift the folder exists to stop.
3. Place: Write each survivor as one row in its bin file with the next ID; rows in the Contract's register shape, raw path and tag on every row, ≤ 110 characters.
4. Check: Apply cross-bin rules 1 to 4 and 7; a row that fails gets its gap as an `UN` row, never a silent fix.
5. Report: Counts per file, merged pairs, conflicts, notes; the unknowns added.

Requirements:
1. Every candidate line ends in exactly one place: a bin row, a synonym on a row, a pain in the holding block, or an `UN` row; none dropped silently, so a harvest can be audited against the folder.
2. IDs are assigned here only, in placement order, never reused or renumbered; a later sort appends.
3. A row keeps every source it merged and the best tag; Inferred never overwrites Reported, Reported never overwrites Verified.
4. No row is written without a raw path and a tag; a candidate lacking either goes to unknowns.
