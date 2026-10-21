---
name: skill-refine
description: "Trigger: /skill-refine <skill>, or refine, improve, fix a skill after a harness run. Outcome: minimal SKILL.md edits from harness evidence, rerun, judged against the prior version."
---
# Skill-Refine
Goal: Improve one existing skill from evidence, not taste (Deming PDCA; anchors over instructions, per skill-micro).
Target: `skills/<section>-level<N>/SKILL.md` the user names; infer from full chat context.
Scope: Skill description, body, Requirements. Never `references/spec-sections.md`; never `examples/**/output-*.md`.
Output: State understanding, add divider, then reply.

## Process
1. Evidence: Latest `tests/harness/results/<skill>.*.json`, its run output in `tests/harness/runs/`, judge fixes, and Hai's own read of the output. No evidence = run first: `python tests/harness/harness.py run <skill> --tag vN`.
2. Diagnose: Map each failed rule or judge fix to the one skill line that caused it: missing anchor, instruction fighting the anchor, rule with no number, Cut list gap, Target naming a sibling that does not exist. One cause per symptom; symptom with no cause in the skill = brief or contract gap, say so.
3. Propose: Before → After per line, each with the symptom it removes. Cut before add. Description touched = re-audit per skill-micro compression rule.
4. Align: Show proposal; Hai confirms. One skill per turn.
5. Apply and prove: Edit; `claude plugin validate .`; harness run with the next tag; judge new against prior. Report check lines and verdict. Hai reads both outputs and decides what ships.

Requirements:
1. Every edit names the symptom it removes; no edit from taste alone.
2. Body no longer after refine, unless a hard rule needed a number.
3. Prior run and result kept; new tag every run; nothing overwritten.
