---
name: check-level1
description: "Trigger: /domain:check-level1 or check the folder, coverage, is the domain complete request. Outcome: README written with charter, counts, coverage per bin, unknowns by kind, pass or fail, from every folder file, rule failures added as unknowns."
---
# Check-Level1
Goal: Write the domain folder README as a data quality report (DAMA DMBOK dimensions: completeness, consistency, uniqueness, validity; referential integrity for every pointer), same shape for every domain so folders compare.
Target: Every file in `domains/<name>/`: `README.md` (charter, roles, sources), the six bin files, `roles.md`, `exemplars.md`, `unknowns.md`, `raw/`; `${CLAUDE_PLUGIN_ROOT}/references/domain-bins.md` supplies the ten cross-bin rules and the charter block.
Scope: Charter: three lines present, Serves as `RO` rows, Outcome as an `EN`, Yardstick as a `DT` (rule 8). Integrity: every `EN`, `DT`, `RU`, `KN`, `PR`, `TL`, `RO`, `EX`, `UN` pointer resolves to a row (rules 1, 2, 7, 9). Uniqueness: no two rows for one noun, no duplicate `UN` question. Validity: every row has a raw path and a tag; rules carry a source and a severity; knowledge carries an owner. Coverage: per bin, rows with no `Unknown` cell, as n of m. Counts: rows per file, sources in `raw/` with grades. Unknowns by kind, deduped, `UN` IDs kept. Verdict: pass when every rule holds, fail with the list. Cut: rewriting any bin row, the charter, or the role list; judging whether facts are true; scoring the domain.
Reference: `${CLAUDE_PLUGIN_ROOT}/references/domain-bins.md`: Catalog, charter, cross-bin rules; if absent, stop and say so.
Output: `README.md` written, then inline: verdict, rule failures, counts, coverage per bin.

## Process
1. Read: Every file; list rows per file, pointers per row, Unknown cells per row.
2. Rules: Apply the ten cross-bin rules; each failure becomes one `UN` row with the rule number, appended, never silently fixed, because a check that edits facts hides what the harvest got wrong.
3. Dedupe: `UN` rows asking the same question merge into one, lowest ID kept, the others listed as merged.
4. Write: README in fixed order: charter, roles in scope, sources with grades, counts per file, coverage per bin, Unknowns by kind, verdict with date; a charter missing a line is a fail, written as the first Unknown.
5. Report: Verdict, failures, counts, coverage inline.

Requirements:
1. Changes no row in any bin file, `roles.md`, or the charter; its only writes are the README and appended `UN` rows.
2. Verdict is pass only when every rule holds; a folder can pass with many Unknowns, because Unknowns are the product, failures are broken structure.
3. Same README order for every domain, so two folders compare line by line.
4. Counts and coverage are computed from the files, never typed; a count that disagrees with a file is a fail.
