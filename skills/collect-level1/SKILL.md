---
name: collect-level1
description: "Trigger: /domain:collect-level1 or what to collect next, what to ask whom, coverage, unknown unknowns request. Outcome: collect.md written, one row per gap with evidence, what to get, from whom, the question, what it unblocks, status, plus a question sheet per stakeholder, from the whole folder and one outside search per step, counts inline."
---
# Collect-Level1
Goal: Turn the folder into the next stakeholder visit, run the way a founder runs customer discovery: Fitzpatrick's Mom Test (a specific past instance, never an opinion, never a pitch), Blank's customer development (get out of the building; records and observation beat interviews), Torres's continuous discovery (story-based interviews, weekly), Maurya's problem interview before any solution interview, Ulwick's opportunity score (importance and satisfaction) to rank; coverage as a traceability matrix (every role, step and served person traced to a raw source); process mining conformance checking (the record beats the story; a log needs case id, activity, timestamp); the profession's own yardstick per step, searched outside (transaction cost analysis for execution, hit rate for recommendations).
Target: The whole `domains/<name>/` folder: README charter and roles, every bin file, `roles.md`, `unknowns.md`, the `raw/` listing, an existing `collect.md` if present (rows updated, never renumbered); web search, one query per `PR` step, for the field's standard measure of that step; `${CLAUDE_PLUGIN_ROOT}/references/domain-bins.md` supplies the Collect register and rule 13.
Scope: Four detectors, one `CO-NN` row each. Coverage: a role, step or served person with no raw source behind it. Conformance: a `PR` chain with no record (case id, activity, timestamp) to check it against, or a stated step a record contradicts. Yardstick: per `PR` step, the field's standard measure found by search versus the `DT` rows present; a missing measure is a hidden problem candidate, tagged `no insider has confirmed`. Unknown: every open `UN` row, grouped by who settles it. Per row: evidence (row IDs), get (source kind and the exact artifact: fields, period), from (an `RO`, or a system `TL`), ask (one line about a specific past instance or artifact), unblocks (a problem statement for a step, a charter yardstick, an authority cell, a `UN`), priority (the step's load times the size of the gap; a served person's step first), status (`open`, `asked`, `received: raw/<file>`). Question sheet: per stakeholder, their asks in priority order, five per visit, opening with the last time it happened. Cut: solutions, agents, features, judging whether a fact is true, closing a row without a raw file.
Reference: `${CLAUDE_PLUGIN_ROOT}/references/domain-bins.md`: Collect register, rule 13; if absent, stop and say so.
Output: `collect.md` written, then inline: the register, counts per detector, the question sheet per stakeholder, divider, rows closed since the last run.

## Process
1. Gather: Read the folder and the `raw/` listing; list roles, steps, served people, `DT` rows, open `UN` rows, existing `CO` rows with status.
2. Cover: For each role, step and served person, find the raw files that mention it; none = a coverage row naming the cheapest source, a record before an interview, an interview before a document.
3. Conform: For each `PR` chain, name the record that would check it; none = a conformance row asking for the log with case id, activity, timestamp.
4. Measure: For each `PR` step, one web search for the field's standard measure; compare with the `DT` rows; missing = a yardstick row, the search hit as evidence, tagged `no insider has confirmed`.
5. Triage: Group open `UN` rows by `settles`; one row per group, the questions rewritten to a past instance.
6. Rank and write: Priority by load times gap, served people first; write `collect.md`, update statuses from `raw/` arrivals, write the question sheet.
7. Report: Register, counts per detector, the sheet, rows closed.

Requirements:
1. Every ask names a specific past instance or artifact ("the last three fills", "the memo you sent in March"); an ask containing "would you", "do you think" or a product idea is rewritten or dropped.
2. A row closes only when `status` names a raw file; a conversation is not a closure.
3. A yardstick row names its search source and keeps `no insider has confirmed` until a `DT` row computes the measure from a record.
4. No row names a solution; a hidden problem is stated as a missing measure or a missing record, never as what an agent could do.
5. Five asks per stakeholder per visit; more = a second visit row, because a long list gets opinions, a short one gets stories.
