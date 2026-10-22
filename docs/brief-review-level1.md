# Brief: `review-level1`, the Skill That Closes the Loop

**Bottom Line:** The folder today is a reference. Nothing reads outcomes back into it: all four `knowledge.md` rows carry confidence Unknown and no skill changes them. `review-level1` is the skill that reads what happened (trade journal rows, weekly review notes, a thesis that held or broke) and proposes diffs to the folder and to the harvest skills. Hai approves every diff. That turns the folder into a system that improves its own future output, with external knowledge as the substrate instead of model weights. Written 2026-10-21 by Hai Wang and Claude, from the Altman and Schmidt talks of the same day (`~/learnings/talks/README.md`).

## 1. Why This Skill, Why Now

- **The Loop Is Open:** §6 of `docs\project-spec.md` improves the skills (judge against the previous version). Nothing improves the knowledge. A domain whose knowledge never updates from outcomes is a glossary, not a domain.
- **Investing Has a Slow, Noisy Signal:** tens of outcomes a year, luck mixed in, markets that change when exploited. A loop on that signal must be slow, gated, and process-first. It must never touch sizing or order submission.
- **Recursive Self-Improvement Without Weights (Inferred):** RSI means a system's output raises its own future capability with a signal to tell better from worse. Where the improvement is stored is a substrate choice. Here it is stored in `knowledge.md`, `rules.md`, `exemplars.md`, and `skills\*\SKILL.md`. The ceiling is the base model's reasoning; the gain is how right the model is in this domain, which is where investing edge lives.

## 2. Contract

| Element | Value |
|---|---|
| Reads | `domains\<name>\raw\` records tagged as outcomes: trade journal rows with a close, weekly review notes, a thesis marked held or broken; plus the current folder and the skill that harvested each fact |
| Emits | `domains\<name>\reviews\<date>.md`: one proposed diff per finding, each tagged with its target (a KN confidence, a new RU, a new EX, a SKILL.md edit, a new UN), the outcome rows that justify it, and a Before → After line |
| Never emits | a position size, an order, a buy or sell recommendation, a change applied without Hai's line |
| Hard rules | one outcome row is never enough to change a confidence (minimum three, say so); a loss that repeats twice becomes a rule candidate, not a rule; a thesis that held becomes an exemplar candidate; a fact the trade needed that no harvest produced becomes a SKILL.md edit candidate naming the skill; every diff names its raw outcome rows; the skill writes the review file and stops |
| Gate | Hai approves each diff by writing `applied` or `rejected` next to it; `merge-level1` applies the approved ones |

## 3. Four Diff Kinds

```
 Kind            Trigger in the outcomes                          Target file            Example
 confidence      3+ outcomes agree or disagree with a KN row      knowledge.md           KN-04 Unknown → Low (3 of 4 signals
                                                                                         false positives, raw journal rows 7, 9, 12)
 rule candidate  the same loss pattern twice                      rules.md as Inferred   never enter on a thesis older than the
                                                                                         last earnings event
 exemplar        a thesis held through its yardstick window       exemplars.md           memo brief-hai-2026-09 §3, held 1 quarter
 skill edit      the trade needed a fact no harvest produced      skills\<name>\SKILL.md harvest-record-level0 misses the exit
                                                                                         reason column
 unknown         an outcome contradicts a PR step or a RU row     unknowns.md            journal shows an exit with no review step
```

## 4. Anchors to Research (Step 2 of the Loop)

Candidates for `/skill-micro`, to be confirmed with Hai and searched for 2026:

1. **Decision journals and calibration:** Tetlock, Superforecasting; Brier score per thesis as the confidence update rule.
2. **Post-mortem practice:** blameless post-mortems (Google SRE), one lesson per incident, action item with an owner.
3. **Deliberate practice:** Ericsson; the loop Altman names at Stanford GSB: run experiments, reflect, update the model, not random flailing.
4. **Reflexion and self-refine (2023 onward):** agents that store verbal feedback in memory instead of weights; the closest published shape of this skill.
5. **Kelly and Thorp on noisy edges:** why a small sample never moves a confidence far.

## 5. Order of Work

1. Bring the trade journal into `domains\equity-research\raw\` (already the first step in `docs\handoff.md`). Without outcome rows the skill has nothing to read.
2. Run `harvest-record-level0` on it so the journal's exit and outcome columns are known.
3. Author `review-level1` via `/skill-micro` with the anchors above.
4. Hand-run it once on the journal. Expect few diffs; a review that proposes nothing on thin data is correct.
5. Add the `reviews\` folder and the `applied` or `rejected` gate to `references\domain-bins.md` as cross-bin rule 11.

## 6. Guardrails That Stay

- Paper account only until the L6 edge test in `~/learnings/daily-practice/money-map.md` passes.
- The agent proposes, Hai decides. No diff is applied without Hai's line, no order is ever submitted by an agent.
- Numbers come from tools (FMP, Alpaca, SQLite), never from the model.
