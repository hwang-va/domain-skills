---
name: harvest-record-level0
description: "Trigger: /domain:harvest-record-level0 or harvest a record, journal, decision log, watchlist, portfolio export, CSV, spreadsheet, table request. Outcome: ASCII candidate register, one line per fact with bin, source, tag, from one record profiled by script and the folder charter, inline."
---
# Harvest-Record-Level0
Goal: Render one record as a candidate fact register, process-mining framing (van der Aalst event log: case, activity, timestamp, resource; conformance checking against the stated process), identifiers by profile-then-verify (candidate keys counted by script, never asserted by the model; LLM-FK 2026 finding that model-guessed keys hold under 20 percent), tidy data for columns, OCEL 2.0 for rows that touch several entities, ASCII, inline.
Target: One record user points at: trade journal, decision log, watchlist, portfolio or order export, in CSV, TSV, XLSX, SQLite, or a markdown table; infer from full chat context. `domains/<name>/README.md`, if present, supplies the charter and the roles in scope; absent = ask for the role list in one line before harvesting. `domains/<name>/entities.md` and `process.md`, if present, supply existing terms and the stated steps so a known entity is cited and a contradiction is caught.
Scope: Profile first: run `python tools/profile_record.py <raw path>` and read its column lines, cadence lines, and sample before binning; a record under 30 rows may be read by eye with the counts stated. One line per fact. Entity: one per table and one per column whose values name a thing with identity (ticker, account, thesis); its identifier is the column the profile marks unique, or Unknown. Data: one per value column, with cadence from the profile's median gap and unit from the header or the values. Process: one step per distinct activity or status value, ordered by timestamp, owner from the resource column. Rule: a column that is never null or never outside a range is a rule candidate, Inferred. Tool: the app that exported the record, from the header or the file name. Tag: Verified for every count and value the profile printed, Inferred for a deduction, Reported for a free-text cell. Unknown: a record step with no match in `process.md`, a stated step the record never shows, a key the profile cannot mark unique. Cut: placing facts in folder files, merging, IDs, role map rows, product features, any count the script did not print.
Reference: `${CLAUDE_PLUGIN_ROOT}/references/domain-bins.md`: Levels, scope rule, the bin test, the register shapes; if absent, six columns: bin, fact, source, section, tag, role. `${CLAUDE_PLUGIN_ROOT}/tools/profile_record.py`: the profiler.
Output: Element list (record, rows, columns, roles in scope, profile line count), divider, candidate register grouped by bin, divider, pains and exemplar lines, divider, unknowns.

## Process
1. Scope: Read the charter and roles; a column no role in scope touches is dropped with one note line.
2. Profile: Run the profiler; keep its output in the turn as evidence; every count in a candidate line comes from it.
3. Walk: Column by column from the profile, then row by row from the sample: entities and their identifiers, data with cadence and unit, activities in timestamp order, free-text cells for knowledge and pains.
4. Bin: Apply the one test per fact; a row that touches several entities yields one line per entity; a fact that fits two bins is split.
5. Conform: Compare the activity sequence with `process.md`; each mismatch is an Unknown line naming the step and the raw row.
6. Render: ASCII register grouped by bin in Catalog order, then pains and exemplars, then unknowns. ≤ 60 lines; over = split by column group, name the groups skipped.

Requirements:
1. Every line has a bin, a source with row or column, and a tag; a line missing one is not a candidate.
2. Every entity line names its identifier column or carries an Unknown; a record is the one source that can supply a real identifier.
3. Every count, range, and cadence is one the profiler printed; a number the model computed is dropped.
4. No IDs and no folder writes: candidates are proposed, `sort-level1` places them.
5. Fits one screen: ≤ 60 candidate lines, ≤ 110 characters each.
