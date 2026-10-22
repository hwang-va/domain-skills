---
name: interview-level0
description: "Trigger: /domain:interview-level0 or interview me, ask me about my role, question script, talk to a person in the domain request. Outcome: one question per turn, cap 15, then transcript verbatim to raw/ and an ASCII candidate register, one line per fact with bin, source, tag, mostly knowledge, process, jobs, pains, charter, from one person in one role, inline."
---
# Interview-Level0
Goal: Elicit one role's knowledge and process from one person by the Critical Decision Method (Klein: one recent concrete decision told whole, then fixed probes by phase, order flexible), past behaviour only (Fitzpatrick's Mom Test: never an opinion on a product), files and apps named as used (contextual inquiry), jobs and pains per verb (Ulwick), terms in the person's words (Evans), one question per turn, ASCII register, inline.
Target: One person in one role, in chat; infer the role from full chat context or ask in one line. `domains/<name>/README.md`, if present, supplies the charter and roles in scope; absent = this interview seeds them. `domains/<name>/entities.md` and `process.md`, if present, supply existing terms and steps so a conflict is caught, not re-created.
Scope: Question budget 15, one per turn, the person may say stop at any turn; the register renders from what was answered. Order: one recent decision told whole; probes by phase: what you saw, what you read, what you did, whom you handed to, what could have gone wrong; jobs and pains; files and apps; terms; charter last: whom this work serves, what it produces, how you judge it worked. A probe answered already by the story is skipped, never re-asked. Every answer tagged Reported; a deduction across answers tagged Inferred. A wish (wanted of a product) is a pain line on this role naming the job it hurts, in the person's words, never a bin line. Transcript: at the end, written verbatim to `domains/<name>/raw/interview-<role>-<date>.md`, consent line on top (`consent: <name>, <date>, this interview`), grade Reported; register lines cite it by question number. Unknown: a term that conflicts with `entities.md`, a step that conflicts with `process.md`, a question not reached. Cut: placing facts in folder files, merging, IDs, role map rows, product features, leading questions, two questions in one turn, the model's own domain knowledge as an answer.
Reference: `${CLAUDE_PLUGIN_ROOT}/references/domain-bins.md`: Levels, scope rule, the bin test, the Charter and Roles shapes; if absent, six columns: bin, fact, source, question, tag, role.
Output: Per turn: one question, question number, nothing else. At the end: element list (person as role, questions asked, stop reason), divider, candidate register grouped by bin, divider, charter lines and jobs, pains, tools for this role, divider, unknowns, divider, raw path written.

## Process
1. Open: Name the role, state the cap and the stop word, ask for consent in the same line; no consent = no interview.
2. Story: Ask for one recent decision in this role, told whole; do not interrupt.
3. Probe: One phase probe per turn from the fixed set; skip any the story answered; follow a cue the person gave rather than the script order.
4. Round out: Jobs and pains, files and apps, terms, then the three charter questions.
5. Bin: Apply the one test per answer; a method the person uses is knowledge with the person as owner; a must is a rule only when the person names who enforces it.
6. Render: Transcript to `raw/`, then the ASCII register grouped by bin in Catalog order, then charter, jobs, pains, tools, then unknowns. ≤ 60 lines; over = split by phase, name the phases skipped.

Requirements:
1. One question per turn, numbered; a turn with two questions or with the model's own answer is a broken turn.
2. Every line has a bin or a pain mark, a source with question number, and a tag; nothing is Verified from an interview alone.
3. Pains and mental models are quoted; a paraphrase is Inferred and says so.
4. The transcript is verbatim and written before the register; a register with no raw path is not a result.
5. No IDs and no folder writes beyond `raw/`: `sort-level1`, `roles-level1`, and `check-level1` place the rest.
6. Fits one screen: ≤ 60 candidate lines, ≤ 110 characters each.
