---
name: roles-level1
description: "Trigger: /domain:roles-level1 or role map, who does what, jobs and pains request. Outcome: roles.md written, one row per role with verbs, jobs, load, pain, tools, from the folder README, process, tools, and the pains block, counts inline."
---
# Roles-Level1
Goal: Write the domain role map, jobs-to-be-done (Ulwick: a job is a role's outcome stated free of any solution, pains rank it) with one owner per process step (RACI), roles as goals, never people (Cooper).
Target: `domains/<name>/README.md` supplies the charter and the roles in scope; `process.md` supplies verbs by owner; `tools.md` supplies tools by role; the pains holding block at the end of `roles.md` supplies pains; `${CLAUDE_PLUGIN_ROOT}/references/domain-bins.md` supplies the register shape and rule 8.
Scope: One `RO-NN` row per role in scope. Verbs: from the `PR` steps the role owns, one word each. Jobs: per verb, the outcome the role is responsible for, in one line, no solution words. Load: one of hourly, daily, weekly, quarterly, event-driven, plus hours when a source gives them. Pain: from the holding block, bound to a job; wished agents, tools, or systems stay inside the pain text as a note, never a row. Tools: the `TL-NN` rows the role uses. Served people from the charter are rows even when no step names them. Cut: person names, headcount, org chart, agents, product features, access rights.
Reference: `${CLAUDE_PLUGIN_ROOT}/references/domain-bins.md`: Roles register, rule 8; if absent, stop and say so.
Output: `roles.md` written, then inline: the register, counts, roles named by a source but out of scope, pains left unbound.

## Process
1. Gather: Roles from the README; verbs from `PR` owners; tools from `TL` roles; pains from the holding block.
2. Bind: Each pain to one job of its role; a pain naming a job no step covers becomes a job row with `PR: none` and one Unknown line, because a job with no step is a process gap, not a roles gap.
3. Write: One row per role, charter roles first, in the Contract shape; the holding block is removed once every pain is bound.
4. Check: Every `PR` owner is a row; every `TL` role is a row; a role a source names outside the scope is an Unknown line, never a row.
5. Report: Register inline, counts, unbound pains, out-of-scope roles.

Requirements:
1. Every role in scope has at least one job and one verb; a served role with no step (the client who only reads) still gets a row with its job, because the folder must show who the domain is for.
2. Pains carry no solution as a row: an agent, tool, or system a source wishes for stays as a note inside the pain text.
3. Creates no `PR`, `TL`, or `EN`; a missing step or tool is an Unknown line for its file.
4. Fits one screen: ≤ 10 roles, rows ≤ 110 characters via the renderer. More = split by served people.
