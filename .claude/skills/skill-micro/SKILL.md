---
name: skill-micro
description: "Trigger: /skill-micro"
disable-model-invocation: true
---
# Skill-Micro
Goal: Write precise, narrow skill through information anchors, not specificity.
Target: New or Existing Skill.md.
Scope: SKILL.md and bundled files.
Output: State understanding, add divider, then reply.

## How To Create A Micro Skill
Output each step in chat:
1. Align Goal Outcome: Determine desired agent outcome.
2. Align Anchor: Map 5 best-in-class anchors. Chose highest leverage reference point that anchors agent to that outcome.
3. Refine: Ask user high-leverage unknowns about Goal Outcome, through lens of highest-leverage anchors clustered near it.
4. Align: Show proposal.
5. Write

## How To Write Skill Definition
description: "Trigger: <minimum_triggers>. Outcome: <minimum_caveman_outcome>."
Compression Rule: Ruthlessly minimize. Count every description word; per word (excluding labels `Trigger`, `Outcome`), write one sentence proving word MUST exist or agents misjudge when to trigger or what skill does. Word whose justification fails to name concrete misfire it prevents gets cut. Present per-word audit, then surviving description

## How To Write Skill Body

### Writing
Writing Register: 100% faithful Telegraphic Style.
Writing Structure: Label, colon, sentence.
Writing Style: Prefer short, direct, researched references to specific academic/industry processes/concepts.

Major Risk: Describing how anchor works; risks directly fighting agent's contextually aware knowledge of anchor, could force over-emphasis of irrelevant or immaterial anchor sub-elements.

#### Defaults
Add if unspecified:
- Goal: {{ PRIMARY ANCHOR every skill line revolves around. Infer from full chat context. }}
- Target: Infer from full chat context.
- Scope: Infer from full chat context.
- Output: State understanding, add divider, then reply.

### Examples

Good Example:
```
Goal: Rewrite target in 100% faithful telegraphic style.
Target: Infer from full chat context.
Scope: Infer from full chat context.
Output: State understanding, add divider, then reply.
```

Bad Example:
```
# comms-telegraphic

Identify target from context: file, selection, or text user points at. Ambiguous target = ask one line ("Target = `<path>`?"), then translate.

## Transform (Lossless)

Telegraphic = lossy *grammar*, lossless *content*. Compress form only; every fact survives.

**Drop:**
- Articles (a/an/the).
- Copulas and auxiliaries where meaning holds ("is the default" = "default").
- Conjunctions: collapse to slashes or commas ("browser, web, or UI" = "browser / web / UI").
- Gerund noun phrases to bare verbs ("opening a site" = "open site").

**Keep verbatim, always:**
- Paths, code, commands, flags, Machine Strings in backticks.
- Numbers, names, ordering, every listed item.
- Negations and scope words (never, only, all, before): dropping these flips meaning.

**Never:** summarize, merge list items, or cut a clause. Content cut = summarization, not telegraphic. The tell: After version missing a fact the Before version states.

## Output

Show translation in fenced block matching source format. Editing file in place only when user says so; default = display only. Close with one line: what grammar dropped, confirmation content intact.
```
.
