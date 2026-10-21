# Handoff: domain-skills, 2026-10-21

**Bottom Line:** Four skills exist (`harvest-doc-level0`, `sort-level1`, `roles-level1`, `check-level1`) and one domain folder, `domains/equity-research/`, is harvested and sorted from a single source, the equity-research brief. Two skills have a hand run, two are unrun because the only raw source on this machine is that brief. The next session starts by bringing real artifacts into `raw/`, then runs `roles-level1` and `check-level1`, then builds the remaining harvesters. Read `docs/project-spec.md` and `references/domain-bins.md` first; this page says where to begin and what was decided. Updated 2026-10-21, end of the first session.

**Origin:** This repo came out of the `product-spec-skills` session of 2026-10-21 (session `68bac1c8-c3dc-42bd-b19f-a42516ab046e`, [web](https://claude.ai/code/session_01EtJbacV359VffRPjttCASz)), where five AI-native spec sections were added and the missing input, the domain, became its own factory. The method for building skills by conversation is in `~/learnings/meta-spec/07-building-a-spec-skill.md`.

## 1. State

| Part | Status | Where |
|---|---|---|
| Project spec | Drafted, not yet aligned; Hai confirmed the bins, charter, roles-first scope, tools, conversation, raw, exemplars, research in chat | `docs/project-spec.md` |
| Contract | Written: Levels, scope rule, Catalog of ten parts, bin test, charter and roles registers, example rows, ten cross-bin rules | `references/domain-bins.md` |
| Plugin | `/domain:<skill>`, validates with warnings, four skills; none callable as `/domain:` until the plugin is reloaded, hand runs in chat until then | `.claude-plugin/plugin.json`, `skills/` |
| House skills | Copied from `product-spec-skills`: `comms`, `skill-micro`, `show-ascii`, `skill-refine` | `.claude/skills/` |
| Harness | Not started; adapt `product-spec-skills/tests/harness/harness.py`. One check exists: `tools/render_register.py` wraps register cells so no line exceeds 110 columns, and `domains/equity-research/build.py` holds the sorted rows as data and renders the nine files | `tests/harness/`, `tools/` |
| Domains | `equity-research`: stub charter and three roles in `README.md`; one source in `raw/` (the brief, Reported); one candidate register; nine files sorted: 12 EN, 7 DT, 2 RU, 4 KN, 6 PR, 3 TL, 1 EX, 14 UN, 6 pains in the `roles.md` holding block. `roles-level1` and `check-level1` not run. `domains/common/` empty | `domains/equity-research/` |
| Git | Eight commits on `main`, last `7978061`, no remote | |

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

1. **Bring real artifacts** into `domains/equity-research/raw/`: one memo of Hai's, one broker research note, the trade journal, the PM newsletter sample. Grade each: Verified for records and primary documents, Reported for other firms' material. Add a row per file to the Sources table in `README.md`.
2. **Settle the fourteen Unknowns you can:** read `unknowns.md`; UN-07, UN-08 are yours; UN-09, UN-10, UN-11 are bin decisions an analyst makes; write answers as rows or as merged entities in `build.py`, rerun it, and mark the UN settled.
3. **Run `roles-level1` by hand:** bind the six pains in the `roles.md` holding block to jobs, one `RO` row per role, charter roles first.
4. **Run `check-level1` by hand:** rewrite the README in the fixed order with counts computed from the files; expect a fail on rule 8 (the yardstick is Unknown) and on rule 7 (four steps with no tool), both already UN rows.
5. **Harvest the new artifacts** with `harvest-doc-level0` (memo, broker note, letter) and, once written, `harvest-record-level0` (the journal); then `sort-level1` again, which now exercises merge across harvests. Compare the second sort with the first: what merged, what conflicted.
6. **Build the remaining skills** through `/skill-micro`, one per turn, searching anchors only where the field moved in the last year: `harvest-record-level0`, `harvest-chat-level0` (consent first), `harvest-feed-level0`, `harvest-method-level0`, `interview-level0` (question script, Hai as first interviewee), `merge-level1`, `research-level0` (web search on one Unknown, Reported only).
7. **Harness:** copy `product-spec-skills/tests/harness/` and point `check` at the register renderer and the ten cross-bin rules, so a skill run is scored, not read.

## 4. Rules That Bite

- `/skill-micro` is locked to user invocation; Hai types it, Claude runs the five steps in chat.
- One skill per turn; one decision per turn; defaults in brackets.
- Never a vendor name in a bin fact; the tool bin names the tool, the fact names the role and the step.
- A wish is never a rule. A method's rules are knowledge until the firm adopts them.
- Raw PDFs are git-ignored by default; commit a raw file only with its owner's consent.
- Worklog row at the end of every turn that changes a file.
- Registers are rendered, not typed: rows go in a `build.py` per domain and through `tools/render_register.py`; hand-typed tables broke the 110-column rule in 45 lines on the first try.
- Python heredocs with apostrophes fail in this shell; write a script file to the scratchpad and run it.

## 5. Open Decisions (from the spec)

Project home confirmed as `~/projects/domain-skills`. Still open: interview by chat script or recorded call through `/transcript-tool` (both, chat first); confidence as three words or a number (three words); one repo for all domains or one per domain (one, until a second person needs theirs); plugin name `/domain:` (yes). Each is Hai's call in the next session; the bracketed default stands until then.
