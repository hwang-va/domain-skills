# Project Spec: Skill Factory for Domain Folders

**Bottom Line:** This repository is a second skill factory, built the way `product-spec-skills` was, pointed at a domain instead of a product. It turns a domain's scattered sources (documents, feeds, people, methods, records, conversations) into one orderly folder, `domains/<name>/`, that anyone building or judging an AI-native product in that domain reads first: a charter (whom the domain serves, for what outcome, judged how), then entities, data, rules, process, knowledge, tools, and a role map with each role's jobs and pains, closing with the Unknowns. Read top to bottom it says how this world works today, the as-is a product spec then changes. A domain is a world: the files its roles keep and the apps its roles use, bounded by the roles in scope, never by the whole firm. The domain folder is the input the spec skills were missing. Same loop, same harness idea, same authoring method.

**Status:** Draft, 2026-10-21, Hai Wang and Claude, from the Q&A that followed the AI-native spec sections. Not yet aligned; aligned when Hai confirms the Purpose Card and the five bins.

## 1. Purpose Card

```
┌─ Purpose · Domain Skills ───────────────────────────────────────────────────────────┐
│ Summary  turns a domain's scattered sources into one folder of sorted, named,       │
│          checked facts that an AI agent and a person read the same way, scoped by   │
│          the roles in play, and lists what the domain still leaves unknown          │
│ Problem  domain truth lives in heads, broker PDFs, feeds, podcasts, and journals;    │
│          every product brief restates it badly; the spec skills expect it as input  │
│          and today get prose; today: ingest-level0 grades sources per product only  │
│ Users    Domain Builder (Hai) │ Product Maker (PM, founder, solo builder who writes │
│          the brief) │ Agent (reads the folder before any task in the domain)        │
│ Non-goal no product features, tasks, or pain-point solutions (those are the spec)  │
│          · no runtime product · no domain is finished · no whole-firm harvest       │
└─────────────────────────────────────────────────────────────────────────────────────┘

 #     Measure                                                          Baseline   Target
 PU-01 % of Glossary Level 0 terms from a brief already in the folder    0 %        80 %
 PU-02 Unknowns a spec run raises that the folder could have answered    Unknown    0
 PU-03 domains whose folder passed one check and one judge               0 of 0     every domain
 PU-04 minutes for a Product Maker to write a brief with the folder open Unknown    Unknown
Rule check: 4 measures · 2 with baseline · 3 with target → 2 gaps (PU-02, PU-04)
```

**Baselines (Inferred 2026-10-21):** PU-01 is 0 because no folder exists; the equity-research brief in `product-spec-skills` is the first test. PU-03 counts folders, not skills, because a domain folder is the product of several skills together.

## 2. Structure

```
 CONTRACT                          SKILLS                            EVIDENCE
 references\domain-bins.md         skills\<source>-level<N>\         domains\<name>\
 ┌──────────────────────────┐      ┌──────────────────────────┐      ┌──────────────────────────┐
 │ six bins, one test each  │      │ harvest-doc-level0       │      │ equity-research\         │
 │ role map, jobs, pains    │─────▶│ harvest-feed-level0      │─────▶│   entities.md data.md    │
 │ roles as the scope rule  │      │ interview-level0         │      │   rules.md process.md    │
 │ file contract per bin    │      │ harvest-method-level0    │      │   knowledge.md tools.md  │
 │ cross-bin rules          │      │ harvest-record-level0    │      │   roles.md unknowns.md   │
 │                          │      │ harvest-chat-level0      │      │   exemplars.md README.md │
 │                          │      │ research-level0          │      │ raw\ (every source, graded)
 │                          │      │ sort-level1, merge-level1│      │ raw\ (sources, graded)   │
 └──────────────────────────┘      │ roles-level1, check-level1      └────────────┬─────────────┘
                                   └──────────────────────────┘                   │
                                                                                  ▼
                                                                     tests\harness\harness.py
                                                                     run · check · judge · report
```

**Reading Key:** A source kind is where domain truth comes from: a document, a feed, a person, a method, a record, a conversation, or outside research on an Unknown. A bin is where a fact lands: entity, data, rule, knowledge, process, tool. Every source is kept verbatim under `raw/` with a grade, and every bin fact points back to its raw file, so a misread harvest is repaired from the source, never from memory. A harvest skill reads one source kind and emits candidate facts, each tagged with its bin, its source, and Verified, Reported, or Inferred. The sort, merge, roles, and check skills turn candidates into the folder. The folder grows; a domain is never finished.

## 3. Charter: Whom, for What, Judged How

Every domain folder opens with three lines, before the roles. **Serves:** the people the domain exists for, internal or external: the PM, the end investor, the person managing their own health. **Outcome:** the thing the domain produces for them: an allocation decision, an equity investment, a health routine kept. **Yardstick:** how the domain itself judges that outcome, in its own terms, before any product: return against benchmark after a quarter, a thesis that held, records in one place and reminders followed. The charter is domain truth, not product; Purpose Level 1 later turns the yardstick into measures with baselines and targets. A folder with no charter has no way to say which role, tool, or pain matters most, so `check-level1` fails it.

```
 Charter · asset-allocation
 Serves     the PM, and through the PM the fund's investors
 Outcome    a weight decision across six asset classes each cycle, with its rationale
 Yardstick  allocation contribution to return against the policy benchmark, reviewed quarterly
```

## 4. Scope: Roles First

A domain is scoped by the roles in play, never by the firm. The Domain Builder names the roles first (PM, analyst, client), and the harvest covers only the nouns, verbs, files, and apps those roles touch, then stops. "A wealth management firm" is not a domain; "the PM and the client in a wealth management firm" is one that finishes in a week. A role added later widens the folder by a merge, never by a restart. The role list follows the charter in the folder's README and is the first gate of every harvest skill: a fact no role in scope touches is dropped with a note, not kept.

## 5. The Six Bins

One test per bin: who could make this fact false?

| Bin | Who could make it false | Holds | File | Example, equity research |
|---|---|---|---|---|
| entity | nobody; it is a noun with identity and a lifecycle | name, definition, identifier, states, relations | `entities.md` | Security, Memo, Signal, Decision, Portfolio, Watchlist |
| data | a vendor or a sensor | values about an entity that arrive from outside, with source and cadence | `data.md` | price, filing, estimate, news item, X post |
| rule | a regulator or the firm | a must or never that holds whatever product is built, with source, severity, jurisdiction, validity | `rules.md` | MNPI handling, position limits, the firm's long-bias AI mandate |
| knowledge | an expert; judgment that may be wrong | playbooks, theses, mental models, methods, with owner and confidence | `knowledge.md` | sector logic for semis, continuous-decision model, value investing |
| process | the firm's workflow; steps a role performs in order | ordered steps, owner per step, handoffs | `process.md` | idea, research, decision, trade, review |
| tool | the vendor, or the firm's IT; an app a role uses today | tool, roles that use it, what goes in, what comes out, which process steps it serves | `tools.md` | email, Bloomberg terminal, Excel, the broker portal, Alpaca, eMoney |

**Role Map (`roles.md`):** one row per human role with the verbs it performs, and per verb the job, the load, and the pain. A job is domain truth; it exists whether or not a product is built. The pain is where a product starts: the brief names the job, Purpose measures it, Agents assigns it. The folder records the pain and hands it on; it never designs the fix.

**Unknowns (`unknowns.md`):** every fact a harvest could not place, every conflict between two sources, every term with two meanings, one question each, with the source that would settle it.

**Why Tools Is a Bin:** an AI-native product replaces or wraps the apps a role uses today, so each tool row becomes an Interfaces row or a Product Surface screen in the spec, and the role's load on that tool is where automation pays. A tool row names no product decision; it records what is used, by whom, for which step.

**Exemplars (`exemplars.md`):** a source kept to be imitated, not only read: another fund's letter, a deck, a signal alert sample, a memo format, a skill file for a method such as DCF. One line per exemplar: artifact kind, raw path, what to keep, what to change, which entity it will become. The product's Letter or Memo entity is then born with a worked example beside it, and a method skill file is kept whole for an agent to run.

**The Folder Becomes the System:** the domain folder is the first distilled corpus of the product's Knowledge section (`KN-NN`, layer distilled). The day the system runs, its agents load the folder built by hand, and the decisions, memos, and reviews they write back flow into it through the Knowledge feedback arrows. Collecting and iterating the domain is building the system's first memory.

**What Is Not a Bin:** tasks, features, pain-point solutions, agents, screens. Those are the product spec. A harvester that hears one notes it under the role's pain and moves on.

## 6. The Loop

Same five steps as `product-spec-skills`, one skill per turn.

```
 ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
 │ 1 DEFINE     │──▶│ 2 RESEARCH   │──▶│ 3 AUTHOR     │──▶│ 4 TEST       │──▶│ 5 COMPARE    │
 │ bin or source│   │ anchors with │   │ /skill-micro │   │ harness run  │   │ harness judge│
 │ block in the │   │ Hai, searched│   │ five steps;  │   │ + check:     │   │ vs previous; │
 │ Contract     │   │ for the year │   │ validate     │   │ hard rules   │   │ better ships │
 └──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘   └──────┬───────┘
        ▲                                                                           │
        └───────────────────────────────────────────────────────────────────────────┘
```

| Step | Input | Output | Gate |
|---|---|---|---|
| 1 Define | A source kind or a bin | Block in `references\domain-bins.md`: elements, file contract, legend | Elements, test, file columns stated |
| 2 Research | Block | Five anchors, one primary, searched for the current year, confirmed with Hai | Hai confirms the primary anchor |
| 3 Author | Anchors | `skills\<name>\SKILL.md` | `claude plugin validate .` passes |
| 4 Test | SKILL.md | `tests\harness\runs\<skill>.<tag>.md` and its check | Every hard rule in Requirements passes |
| 5 Compare | Two outputs | Judge verdict and one fix each; Hai's read | Hai decides what ships |

## 7. The Skills

| Skill | Reads | Emits | Hard rules |
|---|---|---|---|
| `harvest-doc-level0` | one document: broker note, memo, research paper | candidate facts, one per line, bin, source, tag | every noun phrase placed or listed as Unknown; no fact without a page or section reference |
| `harvest-feed-level0` | a feed sample: news, X posts, podcast transcript | candidate facts, mostly data and knowledge, with cadence and author | KOL claims land in knowledge with the author, never in rules |
| `interview-level0` | a person, by a question script run in chat | candidate facts from one role, mostly knowledge and process, plus that role's jobs and pains | one question per turn; every answer tagged Reported; mental models kept in the person's words |
| `harvest-method-level0` | a published method: value investing, a strategy document | knowledge and process facts with the method as source | a method's rules are knowledge, not rules, unless the firm adopted them |
| `harvest-record-level0` | records: decision log, trade journal, watchlist, portfolio | entities with real identifiers, process as it actually ran, data cadences | every entity names its identifier; a record that contradicts a stated process is an Unknown |
| `research-level0` | one Unknown from `unknowns.md`, for a part of the domain no insider in reach knows (middle office, fund operations, a regulator's rule) | candidate facts from public sources (regulator material, industry body guides, filings of similar firms, textbooks) tagged Reported with a source grade, plus the interview questions to put to an insider | never tags Verified; every fact carries "learned, no insider has confirmed" until one does; stops at the first source that answers, lists the rest |
| `harvest-chat-level0` | a conversation: chat export (WeChat, Teams, Slack), meeting transcript, email thread, between domain people or between them and engineers | candidate facts tagged with the speaker's role and fact or wish; facts to the bins, wishes to the role's pain line, feature ideas handed to the product spec | consent asked first; a wish is never written as a rule; every pain names the speaker's role and the job it hurts |
| `sort-level1` | all candidate facts | facts placed in six files by the one test, duplicates merged | every fact in exactly one bin; a fact that fits two is split; a fact no role in scope touches is dropped with a note |
| `merge-level1` | an existing folder plus new candidates | the folder updated, conflicts listed | never silently overwrite; a conflict is an Unknown with both sources |
| `roles-level1` | process, tool, and interview facts | `roles.md`: role, verbs, jobs, load, pain, tools used | every process step has an owner role; every pain names a job; every tool names at least one role |
| `check-level1` | the folder | `README.md` with the charter, the roles in scope, counts, coverage per bin, Unknowns by kind | charter present with all three lines; the same shape for every domain, so folders compare |

**Conversation as a Source:** the richest source for the role map, because pains are said out loud in chat and nowhere else, and the weakest for rules, because people state wishes as if they were facts. The harvester separates the two by one question per line, "is this true of the domain, or wanted of the product", and keeps only the first in the bins.

**Equity Research First:** the first folder, built from three real artifacts (a memo of Hai's, one broker note, the trade journal) through `harvest-doc-level0` and `harvest-record-level0`, sorted by hand before `sort-level1` exists, so the skills encode decisions, not guesses.

## 8. Cross-Bin Rules

1. Every data row names the entity it describes; data with no entity is an entity gap.
2. Every process step names a role in `roles.md` and the entities it reads or writes.
3. Every rule names its source and severity; a rule with no source is knowledge until proven.
4. Every knowledge row names an owner and a confidence; knowledge with no owner is a feed claim, kept with its author.
5. A term used in two bins with two meanings is an Unknown; the Glossary of any product spec in the domain starts from `entities.md`.
6. Shared terms across domains (a rate decision in macro and equity research) live once in `domains/common/` and are pointed at, never copied.
7. Every tool row names at least one role and one process step; a tool no role uses is dropped; a process step with no tool and no manual note is an Unknown.
8. The charter's served people appear as roles in `roles.md`, and its outcome is an entity in `entities.md` with the yardstick as a data row about it; a charter whose outcome no process step produces is an Unknown.
9. Every bin fact names its raw file; every exemplar names the entity it will become; a bin fact from `research-level0` keeps its "no insider has confirmed" mark until an interview or a record confirms it.

## 9. How the Spec Skills Read It

`ingest-level0` copies the domain folder's README into the spec folder and grades it as a source. `purpose-level1` reads the charter first: the served people become Users, the outcome becomes the Summary, and the yardstick becomes the first measure row. `glossary-level0` harvests against `entities.md` first, so PU-01 can be measured. Every section skill's Target line gains "domain folder, if present, read first": Data Model reads entities, Interfaces reads data cadences and `tools.md` as the exchanges to wrap or replace, Product Surface reads `tools.md` for the screens a role has today, Risks reads rules by severity, Knowledge reads `knowledge.md` and the whole folder as the first distilled corpus with `raw/` as its raw layer, `lessons-level0` reads `exemplars.md` for other firms' patterns to Adopt, Adapt, or Avoid, Agents reads `roles.md` to propose one agent per job a human role wants to hand off. The role map is the bridge from domain to agent team: a role's verbs become the actions Autonomy tiers, and the pain becomes the Purpose measure.

## 10. Open Decisions

| # | Decision | Options | Owner |
|---|---|---|---|
| 1 | Project name and home | `domain-skills` at `~/projects/domain-skills` (recommended); or a folder inside `product-spec-skills` | Hai |
| 2 | Interview skill: chat script or a recorded call through `/transcript-tool` | Both, chat first | Hai |
| 3 | Confidence on knowledge rows: three words (low, medium, high) or a number | Three words | Hai |
| 4 | Where `domains/` lives: inside this repo, or one repo per domain for sharing | Inside, until a second person needs one | Hai |
| 5 | Plugin name: `/domain:<skill>` | Yes | Hai |

## 11. Definitions

- **Source kind:** where domain truth comes from: document, feed, person, method, record, conversation.
- **Wish:** a line in a conversation that asks for the product rather than describes the domain; recorded as a pain on the speaker's role, handed to the product spec, never a bin fact.
- **Bin:** where a fact lands: entity, data, rule, knowledge, process, tool, decided by who could make it false.
- **World:** a domain seen as the files its roles keep and the apps its roles use; the roles in scope bound it.
- **Charter:** three lines at the top of a domain folder: whom the domain serves, the outcome it produces for them, the yardstick it judges that outcome by; domain truth that Purpose later measures.
- **Domain folder:** `domains/<name>/` with one file per bin, a role map, an Unknowns list, and a README that opens with the charter, then the roles in scope, then the counts.
- **Role map:** one row per human role with verbs, jobs, load, and pain; the input Agents reads.
- **Exemplar:** a source kept to be imitated: a letter, deck, alert, memo, or method skill file, indexed in `exemplars.md` with what to keep and change and the entity it becomes.
- **Raw:** `domains/<name>/raw/`, every source verbatim with a grade; the raw layer of the domain as a Knowledge corpus.
- **Candidate fact:** one line a harvest skill emits: text, bin, source, tag; not yet in the folder.
- **Contract:** `references/domain-bins.md`: bins, tests, file contracts, legend, cross-bin rules.
