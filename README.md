# domain-skills

**What It Is:** A skill factory for domain folders. Give it a domain's scattered sources, documents, feeds, people, methods, records, conversations, and it produces one folder, `domains/<name>/`, that an AI agent and a person read the same way: a charter (whom the domain serves, for what outcome, judged how), the roles in scope, six bins of facts (entities, data, rules, knowledge, process, tools), exemplars to imitate, and the Unknowns the domain itself has not settled. The folder is the input the `product-spec-skills` sections read first, and the first distilled corpus of the product that is later built.

**Premise:** Domain truth lives in heads, broker PDFs, feeds, podcasts, journals, and chats, and every product brief restates it badly. Forcing each source through a fixed bin test, "who could make this fact false", sorts it and exposes what is missing. The folder is a gap-finding instrument first, a reference second.

**Status:** Project spec drafted 2026-10-21; no skill built yet. Read `docs/project-spec.md`.

## Layout

| Path | Role |
|---|---|
| `docs/project-spec.md` | Purpose, charter, roles-first scope, the six bins, the loop, the skills, cross-bin rules, how the spec skills read a folder. |
| `references/domain-bins.md` | The Contract: bins, tests, file contracts, legend, cross-bin rules. To be written. |
| `skills/<name>/SKILL.md` | One skill per source kind or folder step, run as `/domain:<name>`. |
| `domains/<name>/` | One folder per domain; `raw/` holds every source verbatim with a grade. |
| `domains/common/` | Terms shared across domains, pointed at, never copied. |
| `tests/harness/` | Runner, checker, judge, report, to be adapted from `product-spec-skills`. |
| `docs/worklog.md` | One row per step, newest last. |

## Skills Planned

`harvest-doc-level0`, `harvest-feed-level0`, `interview-level0`, `harvest-method-level0`, `harvest-record-level0`, `harvest-chat-level0`, `research-level0`, `sort-level1`, `merge-level1`, `roles-level1`, `check-level1`.

## First Domain

Equity research, long-short, AI sector: three real artifacts (a memo, a broker note, the trade journal) harvested and sorted by hand before any skill exists, so the skills encode decisions, not guesses.
