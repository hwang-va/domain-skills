# CLAUDE.md: domain-skills

**What This Repo Is:** A skill factory for domain folders, the sister of `product-spec-skills`. One skill per source kind or folder step, tested by a harness, producing `domains\<name>\`: charter, roles, six bins, tools, exemplars, unknowns. Read `docs\project-spec.md` first; it is the alignment between Hai and Claude and the reference when the thread is lost.

## House Skills (Dev Only, in `.claude\skills\`)

| Skill | When | Strength |
|---|---|---|
| `/comms` | Every written output: docs, bins, plans, prompts, commit messages, and replies longer than a line. Casual chat with Hai stays plain. | Strong preference |
| `/skill-micro` | Every new or rebuilt `skills\<name>\SKILL.md`. Hai invokes it; Claude runs all five steps in chat: align outcome, align anchor (searched for the current year), refine with Hai, propose, write. | Preference |
| `/show-ascii` | Any visual for the terminal. | Preference |
| `/skill-refine` | An existing skill after a harness run or judge. | Preference |

## Working Rules

- **Skill Loop:** Define in `references\domain-bins.md`, research anchors with Hai, author via `/skill-micro`, validate with `claude plugin validate .`, run by hand on a real source, judge against the previous version. One skill per turn.
- **Roles First:** A domain is scoped by the roles in play, never by the firm. The charter and the role list open every folder README.
- **Bins by One Test:** entity (nobody could make it false), data (a vendor could), rule (a regulator or the firm could), knowledge (an expert could), process (the firm's workflow), tool (the vendor or the firm's IT). A fact that fits two bins is split; a fact no role in scope touches is dropped with a note.
- **Domain, Not Product:** Tasks, features, agents, screens, and solutions never enter a bin. A wish heard in a source is a pain on the speaker's role, handed to the product spec.
- **Raw Is Truth:** Every source is kept verbatim under `domains\<name>\raw\` with a grade; every bin fact points to its raw file. Outside research (`research-level0`) is Reported and marked "no insider has confirmed" until one does.
- **Evidence Over Text:** A skill is judged by the folder it produces on a real source, not by how its SKILL.md reads. Never claim a skill was run when a script rendered the output.
- **Validation:** `claude plugin validate .` prints `✔ Validation passed` before any skill commit.
- **Commits:** One commit per skill or per harness change. Never commit a raw source whose owner has not consented; `domains\*\raw\*.pdf` is ignored by default.
- **Worklog:** Append one row to `docs\worklog.md` at the end of every turn that changes a file, runs a skill, or records a decision. Never rewrite earlier rows.
- **Pace:** Mirror Hai's purpose in two to four parts before acting, one step and one decision per turn, unless Hai says "keep doing without asking". Follow `/answer-concise` when it is on.

## Paths

- Plugin: `.claude-plugin\plugin.json`, skills run as `/domain:<skill>`.
- Contract: `references\domain-bins.md`.
- Domains: `domains\<name>\` with `raw\`, `charter` in `README.md`, `roles.md`, `entities.md`, `data.md`, `rules.md`, `knowledge.md`, `process.md`, `tools.md`, `exemplars.md`, `unknowns.md`; shared terms in `domains\common\`.
- Harness: `tests\harness\` (to be built from the `product-spec-skills` harness; `runs\` and `results\` are working files).
