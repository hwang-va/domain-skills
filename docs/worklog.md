# Worklog

**Bottom Line:** One row per step of the skill loop, newest last, appended by Claude at the end of every turn that changes a file, runs the harness, or records a decision. Hai reads it to see what happened; an agent reads it to resume.

**Columns:** When, Skill or file, Step (Define, Research, Author, Test, Compare, Decide, Ship, Tooling, Docs), What happened, Evidence, Next.

| When | Skill or file | Step | What happened | Evidence | Next |
|---|---|---|---|---|---|
| 2026-10-21 | `docs\project-spec.md` | Docs | Project spec drafted in chat with Hai: charter, roles-first scope, six bins by the "who could make it false" test, seven source kinds, raw and exemplars, ten skills, nine cross-bin rules. Repo scaffolded with the house skills copied from `product-spec-skills`. | file present; `claude plugin validate .` | Define the Contract `references\domain-bins.md`; first harvest by hand on three equity-research artifacts. |
| 2026-10-21 | `references\domain-bins.md` | Define | Wrote the Contract: Levels (0 harvest, 1 folder, no Level 2), scope rule, Catalog of ten folder parts with prefixes EN, DT, RU, KN, PR, TL, RO, EX, UN, the bin test diagram, charter block, roles register, one example row per bin, ten cross-bin rules. | file present | Hand harvest of three equity-research artifacts into `domains\equity-research\`; then `/skill-micro harvest-doc-level0`. |
| 2026-10-21 | `docs\handoff.md` | Docs | Handoff for the next session: state table, decisions made in chat, seven ordered next steps starting with a hand harvest of three equity-research artifacts, rules that bite, open decisions with defaults. | file present | Next session: collect the three artifacts into `domains\equity-research\raw\`. |
| 2026-10-21 | `skills\harvest-doc-level0\SKILL.md` | Author | Authored `harvest-doc-level0` via `/skill-micro` (primary anchor schema-constrained extraction, ExtractBench and KaLLM 2026; Evans ubiquitous language; jobs-to-be-done; DCAT; ingest-level0 grading; header-aware reading per a January 2026 chunking study). Defaults: one line per fact, other firms as Reported plus an exemplar line, cap 60 split by section. | `claude plugin validate .` passed. | Hand-run on `product-spec-skills\examples\equity-research\brief.md` with a stub charter and role list; diff against a hand sort. |
