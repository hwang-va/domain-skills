# Skill Set Co-Building: From One Concrete Problem to a Shipped Skill Set

_Method note, 2026-11-06, from one day of building this repo with Claude Code: a mental model, two contract columns, two rebuilt skills, one new skill, five commits. Method only; the craft of a single skill is `/skill-micro`, the contract is `references\domain-bins.md`, the model behind the columns is `docs\human-ai-cowork.md`, the pictures are `docs\diagrams-essentials\`._

## 0. BLUF

A skill set is a contract, the skills, a harness, and real domain folders. Building one with an agent is a conversation with a fixed shape: start from one concrete problem, abstract it until the essence fits one sentence, write the sentence into the contract, then into the skill, run the skill on a real source, judge, publish. Three principles carry the whole thing: **concrete to abstract**, **anchor, never instruct**, **only the specific goes in**.

## 1. The Loop in One Picture

```
 purpose ──▶ mental model ──▶ contract ──▶ skill ──▶ run on a real source ──▶ judge ──▶ publish
 a felt gap   one line, one    a rule or    SKILL.md   a folder the skill       diff against  marketplace,
 or question  example that     column in    ≤ 1 screen wrote, raw path on       the previous  worklog row
              survives a test  references/             every row                version
```

Every arrow leaves an artifact behind. A turn that leaves none was talk.

## 2. Three Principles

**Concrete to Abstract:** start from one specific problem in one domain (the trader's fills, the LP's letter, the PM's missed filings). Draw it as one example. Lift it one level at a time until the essence is a sentence that would hold in a clinic or a law firm; that sentence goes into `SKILL.md`, the example stays in the contract as the register sample. The test of the abstraction: it lands the trader case and a health case without a special clause. `Verified` on 2026-11-06: the one-line action model came from an investing loop and mapped onto the six bins with two columns, no new bin.

**Anchor, Never Instruct:** the agent already knows more methods than any one person. Name the method and whose (Fitzpatrick's Mom Test, Ulwick's opportunity score, BPMN 2.0 start events) and stop. Writing the steps out fights what the agent knows, lengthens the file, and overweights whichever sub-step happened to be written. Search the anchor for the current year before naming it, so a successor is not missed; record the search in the worklog, not in the skill. A short `SKILL.md` costs less context and reads in a minute.

**Only the Specific Goes In:** what belongs in the file is what the agent would not do by default: the cell format (`starts on`: kind first, then words, then the cited row), the default under uncertainty (`Unknown`, never `alone`), what never closes without evidence (a raw file), the cut list, the counts to report. Those are Scope, Requirements, and the cross-bin rules. Everything else is the anchor's job.

## 3. Roles in the Room

| Who | Brings | Decides |
|---|---|---|
| The person | purpose, domain truth, the concrete case, the gate | which abstraction, which default, when it ships |
| The agent | anchors, drafts, mechanics, the repo's rules kept in mind | nothing alone: proposes, writes on a yes |
| The repo | contract, worklog, validator, register examples | what counts as done: one run on a real source |

## 4. The Turn Shape

Mirror the purpose in parts before acting. One decision per turn, stated first. An example on request, never a lecture. ASCII before any other format; a format is chosen once the picture is right. "Do you understand me?" is the checkpoint. When the work drifts, the person restates the purpose and the agent turns it into a mechanism: the problem-finding purpose became `collect-level1` in one turn.

## 5. Worked Trace: 2026-11-06

| Move | Concrete start | Abstraction | Artifact |
|---|---|---|---|
| 1 | a dashboard of schedulers | actor + trigger + verb + thing + right | `docs\human-ai-cowork.md` |
| 2 | the paper investing loop | the process row is the line; the bins are its lookups | contract: `starts on`, `authority`, rules 2 and 12 |
| 3 | "kind first", explained with one row | the start cell: kind, words, cited row | `sort-level1` rebuilt |
| 4 | memo sign-off; the trader's `submit` | authority sourced, or `Unknown`, never `alone` | `roles-level1` rebuilt |
| 5 | the fills nobody mentioned | four detectors; every ask is a past instance | `collect-level1`, rule 13 |
| 6 | six chat diagrams | one PDF in learning order | `docs\diagrams-essentials\` |

Each move: proposal, one question, write, `claude plugin validate .`, worklog row, scan of added lines for names, commit.

## 6. Rules and Where They Live

| Rule | Lives in |
|---|---|
| Contract first, skill second | `references\domain-bins.md`, then `skills\<name>\SKILL.md` |
| One skill per turn; validate before commit | `CLAUDE.md`; `claude plugin validate .` |
| Written is not built: built means one run on a real source | `CLAUDE.md`, "Evidence Over Text" |
| Worklog every turn; never rewrite a row | `docs\worklog.md` |
| No company or person name in a public skill; scan before commit | `tools\publish-to-skills.sh` block list; grep of the added lines |
| `Unknown` is a value, a guess is not | contract rules 2, 12, 13 |

## 7. Checklists

**Start a skill set:** one concrete domain and three real artifacts; the charter; the contract's parts and their one test; a harness that runs a skill on a fixed source; a worklog from day one.

**Add a skill:** outcome in one line; five anchors searched for the year, one chosen; one question to the owner; the proposal as a diff; write; validate; worklog; run on a real source; commit.

**Rebuild a skill:** change the contract first; touch only the lines the change needs; keep IDs and register shapes; put the "why" in the worklog row.

**Close a session:** commit, push, scan, worklog, and the one next step named in the last row.

## 8. Glossary

- **Contract:** the shared reference every skill reads: parts, tests, columns, rules (`references\domain-bins.md`).
- **Anchor:** a named method by a named author that fixes the agent to an outcome without spelling out steps.
- **Bin:** where a fact lands, decided by one test: who could make this fact false.
- **Line:** one action with every slot filled: actor, trigger, verb, thing, right; in the folder, a process row.
- **Detector:** a rule that turns the folder into a collection row: coverage, conformance, yardstick, unknown.
- **Level 0 and 1:** harvest one source into candidate lines; build the folder from candidates.
- **Built versus written:** written is a validated `SKILL.md`; built is a folder that skill produced from a real source.
