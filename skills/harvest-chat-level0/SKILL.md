---
name: harvest-chat-level0
description: "Trigger: /domain:harvest-chat-level0 or harvest a chat export, Teams, Slack, WeChat thread, meeting transcript, email thread request. Outcome: ASCII candidate register, one line per fact with bin, speaker role, source, tag, wishes as pains, consent checked first, from one conversation and the folder charter, inline."
---
# Harvest-Chat-Level0
Goal: Render one conversation as a candidate fact register, each line sorted first by speech act (Searle: assertive is a fact for a bin, directive or expressive is a wish for a pain line), turn as unit (ISO 24617-2 dialogue acts, one act per segment), pains in the speaker's words (in vivo coding) bound to the job they hurt (Ulwick), consent and data minimisation before any reading (GDPR Art. 5 and 6), ASCII, inline.
Target: One conversation user points at: chat export (WeChat, Teams, Slack), meeting transcript, email thread, under `domains/<name>/raw/`; infer from full chat context. `domains/<name>/README.md`, if present, supplies the charter and the roles in scope; absent = ask for the role list in one line. A speaker map, `name = role`, given by the user in one line before the harvest; the harvester never guesses a role.
Scope: Consent first: the raw file opens with a front-matter block, one `consent: <name>, <date>, <scope>` line per consenting speaker; block absent = stop with one line asking for it. A speaker without a consent line is replaced by a role label (`PM-2`) in the raw copy and in every candidate line, and that speaker's words appear only as a pain fragment, never as a bin fact. Then one question per segment, "true of the domain, or wanted of the product": true = bin by the one test, entity, data, rule, knowledge, process, tool; wanted = pain line on the speaker's role naming the job it hurts, in the speaker's words; a feature idea = one handoff line to the product spec, never a bin line. A turn that carries both is split. Tag: Reported for every line (a person said it), Inferred for a deduction across turns; never Verified from chat alone. Source: raw path plus turn number or timestamp. Unknown: a term two speakers use differently, a claim one speaker contradicts, a role named that the scope lacks. Cut: placing facts in folder files, merging, IDs, role map rows, product features, any rule that comes from a wish.
Reference: `${CLAUDE_PLUGIN_ROOT}/references/domain-bins.md`: Levels, scope rule, the bin test, the register shapes, cross-bin rule 10; if absent, seven columns: bin, fact, speaker role, source, turn, tag, job.
Output: Element list (conversation, turns, speakers with consent state, speaker map, roles in scope), divider, candidate register grouped by bin, divider, pain lines by role and handoff lines, divider, unknowns.

## Process
1. Consent: Read the front matter; stop if absent; mark each speaker consented or role-only.
2. Scope: Read the charter, roles, and the speaker map; a turn from a role out of scope is dropped with one note line.
3. Walk: Turn by turn; segment a turn into acts; ask the one question per segment.
4. Bin: Apply the one test per fact; a method a speaker cites is knowledge with that speaker as owner; a must the speaker states is a rule only when the speaker names who enforces it, else knowledge.
5. Pains: One line per wish: role, job it hurts, the speaker's words in quotes, turn; a feature idea gets one handoff line.
6. Render: ASCII register grouped by bin in Catalog order, then pains and handoffs, then unknowns. ≤ 60 lines; over = split by speaker, name the speakers skipped.

Requirements:
1. No consent block, no harvest; the stop line names the file and the block shape.
2. Every line has a bin or a pain mark, a speaker role, a source with turn, and a tag.
3. A wish is never a bin line and never a rule; the test question is answered per segment, not per turn.
4. Pains quote the speaker; a paraphrased pain is Inferred and says so.
5. No IDs and no folder writes: candidates are proposed, `sort-level1` and `roles-level1` place them.
6. Fits one screen: ≤ 60 candidate lines, ≤ 110 characters each.
