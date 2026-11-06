# Human and AI Co-Work: One Line per Action

_Copied 2026-11-06 from the owner's learning notes, names and personal paths made neutral. Kept here because the contract implements §2 of this note: `starts on` on every `PR` step and `authority` on every `RO` verb (`references\domain-bins.md`, rules 2 and 12). Changes to the model land here first._

**BLUF:** a domain where people and agents work together is a list of lines, one per action, all in the same shape: **actor + trigger + verb + thing + right**. Nouns say what is there. Actors are the nouns that act. Verbs are what actors do to things. Every verb has a trigger (what wakes it) and a right (may the actor do it alone). Read the list and the humans are wherever a right says *propose*. Started 2026-11-06 from a conversation about an agents dashboard. Exploratory: not yet run on a real domain end to end. `Draft`

## 1. Where It Came From

**The Starting Point:** in a loop or a running system there are things and there are actors. The noun part is what is there. The verb part is what actors do, on what. This is the same split a docs map uses: Components are nouns, Drive is verbs. `Convention`

**Two Additions:**

1. **Actors Are a Kind of Noun:** a human, an agent and a plain script all act on things. What separates them is not what they can touch but what they may do without asking. So the right sits on the line, not on the actor: the same agent acts alone on one verb and proposes on another.
2. **Verbs Need a Trigger:** no verb fires by itself. Each starts from a clock, an event or a person. The trigger is the "running" part of a running system, and it is what an engineer builds.

## 2. The Line

| Slot | Question | Values |
|---|---|---|
| **Actor** | who acts | human, agent, script |
| **Trigger** | what wakes it | in the domain: a clock, an arriving data row, a handoff, a role's ask, a threshold. In the product spec: user turn, after run, background, scheduled, review (the five agent triggers of `/spec:agents-level1`) `Verified` |
| **Verb** | what it does | one verb, present tense |
| **Thing** | on what | one noun from the domain's noun list |
| **Right** | may it act alone | **alone** / **propose** (a named human approves) / **never** (this actor cannot do this verb) |

**Example Line:** Research agent, on a new filing, drafts a tear sheet, propose, the owner approves.

**Reading a Domain from Its Lines:**

- the set of Things is the data model;
- the set of Actors is the agents register plus the people;
- lines with right = propose are where humans sit (the gates);
- lines with right = alone are the ones that need an evaluation and a kill switch;
- the same verb on two triggers is two lines, built and tiered separately.

## 3. How the Domain Folder Holds the Line

**The Process Row Is the Line:** a `PR` row already named its owner `RO` (Actor), its verb, and the `EN` it reads or writes (Thing). Two columns complete it: `starts on` (Trigger, in domain words) and, on the owner's `RO` row, `authority` per verb (Right: `alone`, or the `RO` that signs). So `process.md` is the design table; `roles.md`, `entities.md`, `data.md`, `rules.md`, `knowledge.md` and `tools.md` are what its cells point into.

**Why Not One Merged Document:** a harvest meets facts one at a time with no action attached (a price cadence, a mandate). Bins catch those by the test "who could make this fact false". A line is a design row across the bins. Two views, one set of facts; merging them loses the sorting test.

**Why Unknown Is Never Alone:** when a verb moves from a human role to an agent, the agent starts at the tier the human's authority gives and never a looser one. An authority nobody sourced would let an agent act alone by accident, so it stays `Unknown` until a rule, a step or an interview settles it.

## 4. How It Maps to the Product Spec

| This Model | Existing Place | Note |
|---|---|---|
| Thing | `/spec:data-model-level1` | nouns only, no actors |
| Actor (agent) | `/spec:agents-level1`, one row per worker | an actor appears once; its lines are many |
| Trigger | the five triggers in `/spec:agents-level1` | the domain's `starts on` is mapped onto them |
| Right | `/spec:autonomy-level1`, one row per action; the tier question (A suggest, B do the work with review, C run alone) | alone ≈ Tier C action, propose ≈ Tier A or B, never = a human-only verb `Inferred` |
| Trigger at runtime | an agents dashboard's three states: scheduled, sleeping, running | scheduled = clock trigger waiting, sleeping = event trigger waiting, running = mid-verb `Inferred` |

**What the Line Adds:** the spec sections hold the same facts in four places. The line puts one action's facts side by side, so a domain fits on one page and a missing gate is visible as a blank Right cell.

## 5. Worked Sketch: A Paper Investing Loop

**Rules the Sketch Must Honour** (the loop's guardrails): paper account only; an agent proposes, the owner decides; no agent submits an order without the owner's journal line; numbers come from tools, never from the model.

| Actor | Trigger | Verb | Thing | Right |
|---|---|---|---|---|
| Market data script | scheduled, after the close | fetches | prices, filings | alone |
| Scout agent | after run: fetch done | ranks | candidate names | alone (output is a list, no side effect) |
| Research agent | user turn | drafts | research memo | propose, the owner approves |
| The owner | review, Thursday | decides | trade | alone |
| Order script | after run: the owner's journal line written | submits | paper order | alone, gated by its trigger |
| Reviewer agent | review, weekly | writes | review note | alone (a file the owner reads) |

**One Thing the Sketch Shows:** a human gate can live in two slots. Research memo puts it in Right (propose). Paper order puts it in Trigger (after the owner's journal line). Both are gates; the second one is also a record, because the journal line exists whether or not the order runs. `Plausible`

## 6. Open Questions

1. **Gate as Trigger or as Right:** when the human's decision leaves an artifact, is the trigger form always better, since the artifact doubles as the log?
2. **A Sixth Slot, Check:** a long-running agent needs a check it cannot fake. Does Check belong on the line, or on the actor? Not added yet; add when a line fails silently.
3. **Scripts versus Agents:** a script has no judgment, so its Right is always alone or never. Is that a rule, or just what the sketch happened to show?

## 7. Next Step

Write every line for the paper investing loop as it is today, not as planned, and count the gates. If the count is zero, the guardrails are not in the system yet.
