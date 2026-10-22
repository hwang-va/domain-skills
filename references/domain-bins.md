# Domain Bins

Shared reference for the skills under `skills\`. One `##` heading per bin or folder part. A human reads the whole file as the overall view; each skill reads Levels plus its own heading. Rows carry an ID prefix per bin (EN, DT, RU, KN, PR, TL, RO, EX, UN); cross-bin rules bind by those IDs. Facts carry one tag: Verified (seen in a record or a primary document), Reported (said by a person or a secondary source), Inferred (deduced by the harvester), and outside research adds `no insider has confirmed`.

## Levels

Level 0 harvests: one skill per source kind reads one source and emits candidate facts, one per line, each with a bin, a raw path, and a tag; nothing is placed yet. Level 1 builds the folder: sort places candidates in bins, merge updates an existing folder and lists conflicts, roles builds the role map, check writes the README. There is no Level 2: detail beyond a bin row belongs to the product spec or to the raw source itself. `Inferred`: confirm.

- Level 0 is a list of candidate lines with bins and sources, nothing more.
- Level 1 is the folder a stranger can read top to bottom and know how this world works today.

**Scope Rule:** A domain is bounded by the roles in play, never by the firm. Every harvest reads the role list in the folder README first; a fact no role in scope touches is dropped with one note line.

**Rendering:** Monospace registers, one row per fact, box-drawing glyphs only. Rows within 110 characters. Tag at the end of every row.

## Catalog

| Part | Prefix | File | Holds | Skill that writes it |
|---|---|---|---|---|
| **Charter** | none | `README.md` top | Serves, Outcome, Yardstick: three lines | `check-level1` from `interview-level0` and `harvest-doc-level0` facts |
| **Roles** | RO | `roles.md` | role, verbs, jobs, load, pain, tools used | `roles-level1` |
| **Entities** | EN | `entities.md` | noun with identity and lifecycle: name, definition, identifier, states, relations | `sort-level1` |
| **Data** | DT | `data.md` | values about an entity that arrive from outside: name, entity, source, cadence, unit | `sort-level1` |
| **Rules** | RU | `rules.md` | a must or never that holds whatever product is built: text, source, severity, jurisdiction, validity | `sort-level1` |
| **Knowledge** | KN | `knowledge.md` | judgment that may be wrong: text, owner, confidence, validity, method or view | `sort-level1` |
| **Process** | PR | `process.md` | ordered steps a role performs: step, owner role, reads, writes, tool, handoff | `sort-level1` |
| **Tools** | TL | `tools.md` | an app a role uses today: tool, roles, what goes in, what comes out, steps served | `sort-level1` |
| **Exemplars** | EX | `exemplars.md` | a source kept to imitate: kind, raw path, keep, change, entity it becomes | `sort-level1` |
| **Unknowns** | UN | `unknowns.md` | one question each, the kind of gap, the source that would settle it | every skill appends; `check-level1` dedupes |
| **Reviews** | none | `reviews\<date>.md` | one proposed diff per finding from outcome records: kind, target, raw outcome rows, Before → After, gate cell | `review-level1` writes; Hai gates; `merge-level1` applies |

**Source Kinds and Harvesters:** document (`harvest-doc-level0`), feed (`harvest-feed-level0`), person (`interview-level0`), method (`harvest-method-level0`), record (`harvest-record-level0`), conversation (`harvest-chat-level0`), outside research on one Unknown (`research-level0`).

## The Bin Test

One question decides the bin: who could make this fact false?

```
 nobody; it is a noun with an identity and a lifecycle ─────────────▶ entity     EN
 a vendor or a sensor; the value arrives from outside ──────────────▶ data       DT
 a regulator or the firm; a must or never, product or no product ───▶ rule       RU
 an expert; a judgment, view, model, or method that may be wrong ───▶ knowledge  KN
 the firm's workflow; steps a role performs in order ───────────────▶ process    PR
 the vendor or the firm's IT; an app a role uses today ─────────────▶ tool       TL
 nobody can, but it is wanted of a product, not true of the domain ─▶ not a fact: pain on a role, handed on
```

A fact that fits two bins is split into two facts. A method's rules are knowledge, not rules, unless the firm adopted them. A KOL claim is knowledge with the author as owner, never a rule.

## Charter

- **Serves.** The people the domain exists for, internal or external, named as roles.
- **Outcome.** The thing the domain produces for them, named as an entity.
- **Yardstick.** How the domain itself judges the outcome, in its own terms, named as a data row about the outcome entity.

```
 Charter · asset-allocation
 Serves     the PM, and through the PM the fund's investors                 RO-01, RO-07
 Outcome    a weight decision across six asset classes each cycle            EN-04 Decision
 Yardstick  allocation contribution to return against the policy benchmark   DT-09, quarterly
```

## Roles

- **A. Role.** `RO-NN`, one row per human role in scope, with the verbs it performs.
- **B. Jobs.** Per verb, the job in one line: the outcome the role is responsible for.
- **C. Load and Pain.** Per job, how much and how often, and what hurts, in the role's own words when a source gives them.
- **D. Tools.** The `TL-NN` rows this role uses.

```
 #     Role            Verbs                          Job                              Load          Pain                       Tools
 RO-01 PM              read, form view, decide        decide weights each cycle        daily, 2 h    too much to read, misses   TL-01, TL-03
 RO-02 Quant analyst   blend, run model, report       turn views into weights          weekly        views arrive as prose      TL-02
 RO-03 Client          read letter, ask               understand what changed and why  quarterly     letter late, jargon        TL-04
Rule check: 3 roles · 3 with a pain · 0 without tools                                                                     Reported
```

## Entities, Data, Rules, Knowledge, Process, Tools

One register per file, one row per fact, the columns the Catalog names. Every row ends with its raw path and tag.

```
 EN-01 Security      a listed instrument the fund may hold     id: ticker, ISIN    states: watch, held, exited   raw/gs-note-01.pdf  Verified
 DT-03 Price         about EN-01 │ source: market data vendor │ cadence: daily close, intraday │ unit: USD        raw/journal.csv     Verified
 RU-02 MNPI          never trade on material non-public information │ source: regulator │ severity: critical │ jurisdiction: US │ valid: always   Reported
 KN-05 Semis view    AI capex stays above trend through 2027 │ owner: RO-04 sector researcher │ confidence: medium │ valid: 2026-Q4   raw/memo-03.md  Reported
 PR-04 Blend views   owner RO-02 │ reads KN-*, DT-03 │ writes EN-05 ModelRun │ tool TL-02 │ hands to PR-05 recommend                 Reported
 TL-02 Quant model   roles RO-02 │ in: views, prices │ out: weights │ serves PR-04 │ where it runs: Unknown                              Inferred
 EX-01 Letter sample other fund's quarterly letter │ raw/letter-xyz.pdf │ keep: structure, attribution table │ change: tone │ becomes EN-08 Letter
 UN-03 Which six asset classes, by name? │ kind: entity gap │ settles: the IPS or RO-01
```

## Cross-Bin Rules

1. Every `DT` row names the `EN` it describes; data with no entity is an entity gap.
2. Every `PR` step names an owner `RO` and the `EN` it reads or writes.
3. Every `RU` names its source and severity; a rule with no source is knowledge until proven.
4. Every `KN` names an owner and a confidence; knowledge with no owner is a feed claim, kept with its author.
5. A term used in two bins with two meanings is an `UN`; a product spec's Glossary in this domain starts from `entities.md`.
6. Shared terms across domains live once in `domains\common\` and are pointed at, never copied.
7. Every `TL` names at least one `RO` and one `PR`; a tool no role uses is dropped; a step with no tool and no manual note is an `UN`.
8. The charter's served people are `RO` rows, its outcome an `EN`, its yardstick a `DT` about that `EN`; an outcome no `PR` step produces is an `UN`.
9. Every fact names its raw file; every `EX` names the `EN` it becomes; a fact from `research-level0` keeps `no insider has confirmed` until an interview or a record confirms it.
10. A wish (wanted of a product, not true of the domain) is never a bin row; it is a pain on the speaker's `RO` and is handed to the product spec.
11. A folder row changes from an outcome only through `reviews\<date>.md`: `review-level1` proposes a diff with its raw outcome rows, Hai writes `applied` or `rejected` beside it, `merge-level1` applies the applied ones; a `KN` confidence moves one step per review and never on fewer than three outcome rows; a review never holds a size, an order, or a recommendation.
