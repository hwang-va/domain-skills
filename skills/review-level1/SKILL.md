---
name: review-level1
description: "Trigger: /domain:review-level1 or review outcomes, close the loop, what did the journal teach, update confidence from results request. Outcome: reviews/<date>.md, one proposed diff per finding (confidence, rule candidate, exemplar, skill edit, unknown) with target, raw outcome rows, Before → After, gated by the owner's applied or rejected; never a size, order, or recommendation."
---
# Review-Level1
Goal: Turn outcome records into gated proposals, calibration from scored outcomes (Tetlock: small updates, never from one case; a noisy edge needs a long sample, Kelly and Thorp), one lesson per incident with a target and an owner (blameless post-mortem, Google SRE), feedback on the process not the result (Ericsson), verbal feedback stored in the folder instead of weights (Reflexion, with a human gate), on disk.
Target: `domains/<name>/raw/` records marked as outcomes: journal rows with a close, weekly review notes, a thesis marked held or broken; plus the current folder (`knowledge.md`, `rules.md`, `process.md`, `exemplars.md`, `unknowns.md`) and the harvest skill that produced each fact (`skills/<name>/SKILL.md`). Infer the domain from full chat context. Counts and P&L come from the record or `tools/profile_record.py`, never from the model.
Scope: One review file, `domains/<name>/reviews/<date>.md`, one diff per finding, five kinds. Confidence: three or more outcomes that agree with a KN row move its confidence one step up (Unknown, Low, Medium, High), three or more that disagree move it one step down, one step per review, fewer than three = no diff and the review says so; Brier reported next to the count only when the journal row carries a probability, never used alone. Rule candidate: the same loss pattern twice, written to `rules.md` as Inferred, never as a rule. Exemplar: a thesis that held through its yardstick window. Skill edit: a fact the trade needed that no harvest produced, naming the skill and the line. Unknown: an outcome that contradicts a PR step or a RU row. Each diff: kind, target ID or file, raw outcome rows, Before → After, one line. Gate: the owner writes `applied` or `rejected` beside each diff; `merge-level1` applies; this skill writes nothing outside `reviews/`. Cut: a position size, an order, a buy or sell, a confidence moved on fewer than three rows or by more than one step, a rule from a wish, a change applied, a P&L the model computed, a review of an outcome row already cited by an earlier review.
Reference: `${CLAUDE_PLUGIN_ROOT}/references/domain-bins.md`: the bin test, the Knowledge and Rules shapes, cross-bin rules; `${CLAUDE_PLUGIN_ROOT}/tools/profile_record.py`: counts.
Output: Element list (outcome records read, rows with a close, KN rows checked, earlier reviews), divider, the review file rendered inline (diffs grouped by kind, each with a blank gate cell), divider, findings with no diff and why (sample too small, process sound), divider, raw path written.

## Process
1. Gather: List outcome records and earlier `reviews/*.md`; a row cited before is out.
2. Count: Profile the records by script; per KN row, count outcomes that agree and disagree; per loss, name its pattern.
3. Judge: Process before result: a loss with the stated process followed is no rule candidate; a win with a step skipped is an Unknown.
4. Propose: One diff per finding with its rows and Before → After; fewer than three rows = a finding with no diff.
5. Trace: For each diff, name the harvest skill whose output the trade used or lacked; a lack is a skill edit candidate.
6. Write: `reviews/<date>.md`, gate cell empty, then stop.

Requirements:
1. Every diff names its raw outcome rows and its target; a diff without rows is not a diff.
2. A confidence moves at most one step per review and never on fewer than three rows; the review states the count.
3. Nothing is applied, sized, ordered, or recommended; the review proposes and stops.
4. Every number in the review comes from a record or the profiler; the model's arithmetic is dropped.
5. Fits one screen: ≤ 40 diff lines, ≤ 110 characters each; over = split by kind, name the kinds skipped.
