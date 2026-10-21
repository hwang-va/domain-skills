# Handoff: domain-skills, 2026-10-21

**Bottom Line:** The project is defined and scaffolded, no skill is built, no domain folder exists. The next session starts with a hand harvest of three equity-research artifacts into `domains/equity-research/`, sorted by the bin test without any skill, so the first skill, `harvest-doc-level0`, encodes decisions seen in a real folder. Read `docs/project-spec.md` and `references/domain-bins.md` first; this page says where to begin and what was decided.

**Origin:** This repo came out of the `product-spec-skills` session of 2026-10-21 (session `68bac1c8-c3dc-42bd-b19f-a42516ab046e`, [web](https://claude.ai/code/session_01EtJbacV359VffRPjttCASz)), where five AI-native spec sections were added and the missing input, the domain, became its own factory. The method for building skills by conversation is in `~/learnings/meta-spec/07-building-a-spec-skill.md`.

## 1. State

| Part | Status | Where |
|---|---|---|
| Project spec | Drafted, not yet aligned; Hai confirmed the bins, charter, roles-first scope, tools, conversation, raw, exemplars, research in chat | `docs/project-spec.md` |
| Contract | Written: Levels, scope rule, Catalog of ten parts, bin test, charter and roles registers, example rows, ten cross-bin rules | `references/domain-bins.md` |
| Plugin | `/domain:<skill>`, validates with warnings, zero skills | `.claude-plugin/plugin.json`, `skills/` |
| House skills | Copied from `product-spec-skills`: `comms`, `skill-micro`, `show-ascii`, `skill-refine` | `.claude/skills/` |
| Harness | Not started; adapt `product-spec-skills/tests/harness/harness.py` when the first skill exists | `tests/harness/` |
| Domains | None; `domains/common/` is an empty folder | `domains/` |
| Git | One commit, `4679d4d`, on `main`, no remote | |

## 2. Decisions Made in Chat (Hai, 2026-10-21)

- **Separate project named `domain-skills`,** not `invest-spec-skills`: the skills are the method, a domain is a folder inside.
- **Six bins by one test, "who could make this fact false":** entity, data, rule, knowledge, process, tool. Tools was added after Hai's "a domain is a world of files and apps".
- **Roles first:** a domain is scoped by the roles in play, never by the firm; a role added later widens by merge.
- **Charter on top:** Serves, Outcome, Yardstick; domain truth that `purpose-level1` later measures.
- **Pains stay in the role map, solutions go to the product spec:** a job is domain truth; the product is the choice to take it on.
- **Seven source kinds:** document, feed, person, method, record, conversation (chat exports, with consent), outside research on one Unknown (`research-level0`, Reported, "no insider has confirmed").
- **Raw is truth, exemplars are kept:** every source verbatim under `raw/` with a grade; samples to imitate indexed in `exemplars.md` with the entity each becomes.
- **The folder becomes the system:** it is the product's first distilled Knowledge corpus; agents load it and write decisions back.
- **No Level 2:** detail beyond a bin row belongs to the product spec or the raw source.
- **Tested across domains in chat:** equity research, macro research, wealth management, insurance sales, personal health, personal tax, family assistant, asset allocation. The bins held; health added a severity column to rules, tax added jurisdiction and validity, family made consent the top rule.

## 3. Next Session, in Order

1. **Collect three artifacts** from Hai into `domains/equity-research/raw/`: one memo of Hai's, one broker research note, the trade journal (CSV or Markdown). Add the PM newsletter sample if at hand. Grade each: Verified for records and primary documents, Reported for other firms' material.
2. **Write the charter and role list by hand** at the top of `domains/equity-research/README.md`: Serves, Outcome, Yardstick; roles PM, analyst, trader, and any the artifacts name.
3. **Harvest by hand:** run `/spec:glossary-level0` from `product-spec-skills` on each artifact to lift noun phrases, then sort every term with the bin test into the nine files, one row each in the Contract's register shape, raw path and tag on every row. Write every unplaced term and every conflict to `unknowns.md`.
4. **Read the folder top to bottom** and note what the hand sort decided that the Contract did not say. Those notes are the Scope and Requirements of `harvest-doc-level0`.
5. **Hai types `/skill-micro harvest-doc-level0`.** Anchors to search for the current year before proposing: information extraction and entity typing practice, domain-driven design's ubiquitous language (Evans) for entities and terms, data catalog practice for the data bin, regulatory taxonomy for rules, jobs-to-be-done (Christensen, Ulwick) for the role map. Three unknowns with defaults in brackets; Hai answers "use defaults" or picks.
6. **Run the new skill on the same three artifacts,** diff against the hand sort, log the differences in the worklog, refine once.
7. **Then** `harvest-record-level0` (the journal), `roles-level1`, `check-level1`; `sort-level1` and `merge-level1` only once two harvests exist to sort and merge. `interview-level0` needs a question script written with Hai as the first interviewee, on how a view forms and dies.

## 4. Rules That Bite

- `/skill-micro` is locked to user invocation; Hai types it, Claude runs the five steps in chat.
- One skill per turn; one decision per turn; defaults in brackets.
- Never a vendor name in a bin fact; the tool bin names the tool, the fact names the role and the step.
- A wish is never a rule. A method's rules are knowledge until the firm adopts them.
- Raw PDFs are git-ignored by default; commit a raw file only with its owner's consent.
- Worklog row at the end of every turn that changes a file.

## 5. Open Decisions (from the spec)

Project home confirmed as `~/projects/domain-skills`. Still open: interview by chat script or recorded call through `/transcript-tool` (both, chat first); confidence as three words or a number (three words); one repo for all domains or one per domain (one, until a second person needs theirs); plugin name `/domain:` (yes). Each is Hai's call in the next session; the bracketed default stands until then.
