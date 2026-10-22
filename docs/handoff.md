# Handoff: domain-skills, 2026-10-21 (second session)

**Bottom Line:** Eight skills exist (`harvest-doc-level0`, `harvest-record-level0`, `harvest-chat-level0`, `interview-level0`, `sort-level1`, `roles-level1`, `check-level1`, `review-level1`) plus one profiler tool, and one domain folder, `domains/equity-research/`, harvested and sorted from a single source, the equity-research brief. Two skills have a hand run; six are unrun. The repo is public at https://github.com/hwang-va/domain-skills and the plugin is published as `domain@hw-skills`. The next session starts by fixing the Alpaca key pair, pulling the paper journal into `raw/`, then running `harvest-record-level0`, `interview-level0` on Hai, `roles-level1`, `check-level1`, and the first `review-level1`. Read `docs/project-spec.md`, `references/domain-bins.md`, and `docs/brief-review-level1.md` first; this page says where to begin and what was decided. Updated 2026-10-21, end of the second session.

**Origin:** This repo came out of the `product-spec-skills` session of 2026-10-21 (session `68bac1c8-c3dc-42bd-b19f-a42516ab046e`, [web](https://claude.ai/code/session_01EtJbacV359VffRPjttCASz)), where five AI-native spec sections were added and the missing input, the domain, became its own factory. The second session ([web](https://claude.ai/code/session_015G77NziMbnTy8aaSfoaVN4)) added four harvesters and the review loop. The method for building skills by conversation is in `~/learnings/meta-spec/07-building-a-spec-skill.md`.

## 1. State

| Part | Status | Where |
|---|---|---|
| Project spec | Drafted, not yet aligned; Hai confirmed the bins, charter, roles-first scope, tools, conversation, raw, exemplars, research in chat | `docs/project-spec.md` |
| Review brief | Written and committed; contract, four diff kinds, five anchors, order of work; §5 steps 3 and 5 done, steps 1, 2, 4 wait on outcome rows | `docs/brief-review-level1.md` |
| Contract | Levels, scope rule, Catalog of eleven parts (Reviews added), bin test, charter and roles registers, example rows, eleven cross-bin rules (rule 11: the outcome gate) | `references/domain-bins.md` |
| Plugin | `/domain:<skill>`, validates with one README warning, eight skills; published as `domain@hw-skills` through `tools/publish-to-skills.sh`; hand runs in chat until the plugin is reloaded | `.claude-plugin/plugin.json`, `skills/`, `tools/publish-to-skills.sh` |
| House skills | Copied from `product-spec-skills`: `comms`, `skill-micro`, `show-ascii`, `skill-refine` | `.claude/skills/` |
| Tools | `tools/render_register.py` wraps register cells to 110 columns; `tools/profile_record.py` profiles a CSV, TSV, XLSX, SQLite, or markdown table (kind, distinct, nulls, unique, range, timestamp cadence, sample), tested on a 4-row CSV | `tools/` |
| Harness | Not started; adapt `product-spec-skills/tests/harness/harness.py` | `tests/harness/` |
| Domains | `equity-research`: stub charter and three roles in `README.md`; one source in `raw/` (the brief, Reported); one candidate register; nine files sorted: 12 EN, 7 DT, 2 RU, 4 KN, 6 PR, 3 TL, 1 EX, 14 UN, 6 pains in the `roles.md` holding block; no `reviews/` yet. `domains/common/` empty | `domains/equity-research/` |
| Git | Public, `origin` = https://github.com/hwang-va/domain-skills, `main` pushed; `hw-skills` carries the plugin copy at `plugins/domain` (`978983f`) | |

## 2. Decisions Made in Chat (Hai, 2026-10-21, both sessions)

- **Separate project named `domain-skills`,** not `invest-spec-skills`: the skills are the method, a domain is a folder inside.
- **Six bins by one test, "who could make this fact false":** entity, data, rule, knowledge, process, tool.
- **Roles first:** a domain is scoped by the roles in play, never by the firm; a role added later widens by merge.
- **Charter on top:** Serves, Outcome, Yardstick; domain truth that `purpose-level1` later measures.
- **Pains stay in the role map, solutions go to the product spec.**
- **Seven source kinds:** document, feed, person, method, record, conversation (with consent), outside research on one Unknown.
- **Raw is truth, exemplars are kept.** **The folder becomes the system.** **No Level 2.**
- **Records are profiled by script,** never counted by eye, except under 30 rows with the counts stated (`harvest-record-level0`).
- **Chat consent lives in the raw file's front matter,** one `consent:` line per speaker; a speaker without one becomes a role label and yields pains only; the speaker map comes from Hai (`harvest-chat-level0`).
- **Interview runs case first, charter last,** cap 15 questions, one per turn, stop word, transcript verbatim to `raw/` with a consent line (`interview-level0`).
- **Review uses a count rule, not Brier:** three or more outcome rows move a KN confidence one step per review; Brier reported only beside a probability the journal row carries; Hai gates each diff with `applied` or `rejected`; `merge-level1` applies; never a size, order, or recommendation (`review-level1`, cross-bin rule 11).
- **Repo is public,** account `hwang-va`; the plugin ships through `hw-skills` as a regenerated copy.

## 3. Next Session, in Order

1. **Fix the Alpaca keys:** the `key_id` and `secret` under `alpaca:` in `~/.secrets/accounts.yaml` return 401 on both `paper-api.alpaca.markets` and `data.alpaca.markets`; the key id has 26 characters and the secret 43, where Alpaca issues 20 and 40. Re-copy from the paper dashboard. Then rerun the pull script (scratchpad `pull_alpaca.py` from this session, or rewrite it in ten lines: GET `/v2/orders?status=all&limit=500`, `/v2/account/activities/FILL`, write CSV) into `domains/equity-research/raw/journal-alpaca-<date>.csv`, grade Verified, add a Sources row to `README.md`. If the paper account holds no closed orders, write the first rows of `~/inv/journal.md` by hand and copy it in.
2. **Run `harvest-record-level0`** on the journal: `python tools/profile_record.py <raw path>` first, then the register.
3. **Run `interview-level0`** on Hai as the equity-research analyst; it settles UN-07, UN-08 and gives the charter yardstick that `check-level1` will otherwise fail on.
4. **Bring the other artifacts** into `raw/`: one memo of Hai's, one broker note, the PM newsletter sample; harvest with `harvest-doc-level0`; then `sort-level1` again, which now exercises merge across harvests.
5. **Run `roles-level1` and `check-level1`** by hand; expect fails on rule 7 and rule 8 unless step 3 settled them.
6. **Run `review-level1`** once on the journal; expect few or no diffs, which is correct on thin data; gate each with `applied` or `rejected`.
7. **Build the remaining skills** through `/skill-micro`, one per turn: `merge-level1` (needed before any `applied` diff lands), `harvest-feed-level0`, `harvest-method-level0`, `research-level0`.
8. **Harness:** copy `product-spec-skills/tests/harness/` and point `check` at the register renderer and the eleven cross-bin rules.
9. **After any skill change:** `bash tools/publish-to-skills.sh`, then commit and push `hw-skills`.

## 4. Rules That Bite

- `/skill-micro` is locked to user invocation; Hai types it, Claude runs the five steps in chat and stops at the one open decision.
- One skill per turn; one decision per turn; defaults in brackets.
- Never a vendor name in a bin fact; the tool bin names the tool, the fact names the role and the step.
- A wish is never a rule. A method's rules are knowledge until the firm adopts them.
- Raw PDFs are git-ignored by default; commit a raw file only with its owner's consent. The repo is public now: scan before every push.
- Worklog row at the end of every turn that changes a file.
- Registers are rendered, not typed: rows go in a `build.py` per domain and through `tools/render_register.py`.
- Every count comes from a tool: `tools/profile_record.py` for records; the model's arithmetic is dropped.
- Python heredocs with apostrophes fail in this shell; write a script file to the scratchpad and run it with `python -I`.
- Secrets: never print a value from `~/.secrets/accounts.yaml`; the permission classifier blocks it and the rule forbids it. Report length and prefix only.

## 5. Open Decisions (from the spec)

Project home confirmed as `~/projects/domain-skills`. Interview by chat script (decided, chat first). Confidence as three words (decided, count rule rests on it). One repo for all domains (standing default). Plugin name `/domain:` (yes). Still open: whether `review-level1` may also propose edits to `references/domain-bins.md` (default no, only skills and bins); whether `reviews/` files are committed to the public repo (default yes, they hold no sizes or orders by rule 11).
