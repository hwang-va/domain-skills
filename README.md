# domain-skills

**What It Is:** A skill factory for domain folders. Give it a domain's scattered sources, documents, feeds, people, methods, records, conversations, and it produces one folder, `domains/<name>/`, that an AI agent and a person read the same way: a charter (whom the domain serves, for what outcome, judged how), the roles in scope, six bins of facts (entities, data, rules, knowledge, process, tools), exemplars to imitate, and the Unknowns the domain itself has not settled. The folder is the input the `product-spec-skills` sections read first, and the first distilled corpus of the product that is later built.

**Premise:** Domain truth lives in heads, broker PDFs, feeds, podcasts, journals, and chats, and every product brief restates it badly. Forcing each source through a fixed bin test, "who could make this fact false", sorts it and exposes what is missing. The folder is a gap-finding instrument first, a reference second.

**Status:** Project spec 2026-10-21. Eight skills authored and validated (`harvest-doc`, `harvest-chat`, `harvest-record`, `interview`, `sort`, `roles`, `check`, `review`), run by hand with the owner gating each output. One domain folder, `domains/equity-research/`, at stub stage from one source. Contract extended 2026-11-06 with `starts on` per step and `authority` per role verb. Read `docs/project-spec.md`.

## Layout

| Path | Role |
|---|---|
| `docs/project-spec.md` | Purpose, charter, roles-first scope, the six bins, the loop, the skills, cross-bin rules, how the spec skills read a folder. |
| `docs/human-ai-cowork.md` | The one-line action model (actor, trigger, verb, thing, right) behind `starts on` and `authority` in the contract; the process row as the line, the bins as its lookups; a sketch on a paper investing loop. |
| `references/domain-bins.md` | The Contract: bins, tests, file contracts, legend, cross-bin rules. To be written. |
| `skills/<name>/SKILL.md` | One skill per source kind or folder step, run as `/domain:<name>`. |
| `domains/<name>/` | One folder per domain; `raw/` holds every source verbatim with a grade. |
| `domains/common/` | Terms shared across domains, pointed at, never copied. |
| `tests/harness/` | Runner, checker, judge, report, to be adapted from `product-spec-skills`. |
| `docs/worklog.md` | One row per step, newest last. |

## Skills Planned

`harvest-doc-level0`, `harvest-feed-level0`, `interview-level0`, `harvest-method-level0`, `harvest-record-level0`, `harvest-chat-level0`, `research-level0`, `sort-level1`, `merge-level1`, `roles-level1`, `check-level1`.

## Domains It Fits

**General by Design:** the six bins and the test "who could make this fact false" are not about investing. Any professional domain sorts the same way: a lab result is data, a prescribing rule is a rule, intake then exam then treatment is process. The tool captures how a profession works today, in the words its roles use, for a person and an agent to read alike.

**Best Fit:** knowledge work with well digitised documentation and applications that expose an API. Where the records already exist as files, feeds and app data, the harvest is reading rather than interviewing, and each row in the tools bin is an interface the product can later wrap.

**Candidate Domains:** an investment platform and its parts (equity research, analytics, order management), and outside finance, health management or any other role-bounded professional practice.

**First Domain:** equity research, long-short, AI sector: three real artifacts (a memo, a broker note, the trade journal) harvested and sorted by hand before the skills, so the skills encode decisions, not guesses.
