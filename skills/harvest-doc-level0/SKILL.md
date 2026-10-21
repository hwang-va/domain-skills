---
name: harvest-doc-level0
description: "Trigger: /domain:harvest-doc-level0 or harvest, extract domain facts from a document, broker note, memo, deck request. Outcome: ASCII candidate register, one line per fact with bin, source, tag, from one document and the folder charter, inline."
---
# Harvest-Doc-Level0
Goal: Render one document as a candidate fact register, schema-constrained extraction against the six bins (ExtractBench and the KaLLM 2026 schema-constrained framing; Evans's ubiquitous language for entities and term conflicts; jobs-to-be-done for pains), ASCII, inline.
Target: One document user points at: broker note, memo, research paper, deck, letter; infer from full chat context. `domains/<name>/README.md`, if present, supplies the charter and the roles in scope; absent = ask for the role list in one line before harvesting. `domains/<name>/entities.md`, if present, supplies existing terms so a known entity is cited, not re-created.
Scope: Read by the document's own sections, never fixed chunks. One line per fact; one sentence may yield several lines, each with its own bin. Bin by the one test: entity, data, rule, knowledge, process, tool. Columns per the Contract register for that bin. Source: raw path plus page or section. Tag: Verified for a record or primary document, Reported for a person or another firm, Inferred for a deduction. Another firm's document: facts Reported with the firm as source, plus one exemplar line when the document is a kind worth imitating. A wish (wanted of a product) is a pain line on the speaker's role, never a bin line. Unplaced terms and conflicts with `entities.md` are Unknown lines. Cut: placing facts in folder files, merging, IDs (candidates carry none), role map rows, product features.
Reference: `${CLAUDE_PLUGIN_ROOT}/references/domain-bins.md`: Levels, scope rule, the bin test, the register shapes; if absent, six columns: bin, fact, source, section, tag, role.
Output: Element list (document, sections read, roles in scope), divider, candidate register grouped by bin, divider, pains and exemplar lines, divider, unknowns.

## Process
1. Scope: Read the charter and roles; a fact no role in scope touches is dropped with one note line, so the register stays the world of these roles.
2. Walk: Section by section, list every noun phrase and every must, never, step, number with a source, and view; a term already in `entities.md` is cited by its name, not re-created.
3. Bin: Apply the one test per fact; a fact that fits two bins is split into two lines; a method's rules are knowledge unless the firm adopted them; a claim with an author is knowledge with that owner.
4. Tag: Verified, Reported, or Inferred per line, with the raw path and section; a line with no section is a gap.
5. Render: ASCII register grouped by bin in Catalog order, then pains and exemplars, then unknowns. ≤ 60 lines; over = split by section, name the sections skipped.
6. Gaps: Unknown lines: unplaced terms, conflicts, a role the document names that the scope lacks.

Requirements:
1. Every line has a bin, a source with section, and a tag; a line missing one is not a candidate, because sort cannot place it and merge cannot trace it.
2. No IDs and no folder writes: candidates are proposed, `sort-level1` places them, so two harvests of the same document can be compared.
3. A wish or a feature idea never appears as a bin line; it is a pain on a role or it is dropped.
4. Fits one screen: ≤ 60 candidate lines, ≤ 110 characters each.
