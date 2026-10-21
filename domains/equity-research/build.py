"""Rebuild the equity-research register files from the rows placed by sort-level1 on 2026-10-21.

Run: python domains/equity-research/build.py  (from the repo root). Hand-run evidence; the rows are the decisions.
"""
import io
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools"))
from render_register import render  # noqa: E402

HERE = os.path.dirname(__file__)
RAW = "Raw `brief` = `raw/brief-hai-2026-09.md`."


def write(name, title, intro, headers, widths, rows, check):
    body = render(headers, widths, rows)
    text = f"# {title} · equity-research\n\n{intro} Placed by `sort-level1`, run by hand 2026-10-21. {RAW}\n\n```\n{body}\n{check}\n```\n"
    io.open(os.path.join(HERE, name), "w", encoding="utf-8", newline="\n").write(text)


write("entities.md", "Entities", "Nouns with an identity and a lifecycle. Test: nobody could make the fact false.",
      ["#", "Entity", "Definition", "Identifier", "States", "Source · Tag"], [5, 17, 36, 14, 18, 15], [
    ["EN-01", "Sector", "a market segment with its own investment logic and data series", "name", "covered, not covered", "brief §1 · Reported"],
    ["EN-02", "Company", "a listed business the fund may research or hold", "ticker, ISIN (Unknown)", "watch, held, exited", "brief §1 · Reported"],
    ["EN-03", "Watchlist", "the fund's list of companies under coverage", "name", "Unknown", "brief §1 · Reported"],
    ["EN-04", "Investment Thesis", "the standing view on one company, held with it; synonym candidate: Viewpoint (UN-09)", "company", "current, revised, closed", "brief §1 · Reported"],
    ["EN-05", "Financials", "a company's reported figures, held with it", "company, period", "Unknown", "brief §1 · Reported"],
    ["EN-06", "Knowledge Base", "the fund's collected research and data, referred to by investors and analysts", "Unknown", "Unknown", "brief §1 · Reported"],
    ["EN-07", "Event", "a sector event, corporate event, or industry policy change", "Unknown", "new, assessed", "brief §2 · Reported"],
    ["EN-08", "Viewpoint", "the current view on a company's fundamentals, updated on events; overlap with EN-04 (UN-09)", "company, date", "current, superseded", "brief §2 · Reported"],
    ["EN-09", "Recommendation", "buy, sell, or hold at security level, with a rationale; \"hold for further research\": UN-08", "company, date", "draft, issued, acted, closed", "brief §2 · Reported"],
    ["EN-10", "Signal", "a retrieved item of new information judged to matter; relation to EN-07 (UN-10)", "Unknown", "new, researched, dismissed", "brief §2 · Reported"],
    ["EN-11", "Valuation", "the market's price level for a company, compared to fundamentals", "company, date", "Unknown", "brief §2 · Reported"],
    ["EN-12", "Report", "the output to the PM; kinds: short alert, one-page update, deep research", "Unknown", "draft, sent, read", "brief §3 · Reported"],
], "Rule check: 12 rows · 12 Reported · identifiers Unknown on 5 · relations open: UN-09, UN-10")

write("data.md", "Data", "Values about an entity that arrive from outside. Test: a vendor or a sensor could make the fact false.",
      ["#", "Data", "About", "Source", "Cadence", "Unit", "Source · Tag"], [5, 24, 12, 18, 12, 10, 15], [
    ["DT-01", "Sector investment logic (products, clients, competitive landscape)", "EN-01", "Unknown (analyst written? UN-11)", "Unknown", "text", "brief §1 · Reported"],
    ["DT-02", "Memory chip price (semi)", "EN-01", "Unknown vendor", "Unknown", "USD per unit", "brief §1 · Reported"],
    ["DT-03", "Supply-demand tracker (semi)", "EN-01", "Unknown vendor", "Unknown", "Unknown", "brief §1 · Reported"],
    ["DT-04", "Research reports", "EN-02, EN-01", "brokers, Unknown which", "Unknown", "document", "brief §1 · Reported"],
    ["DT-05", "Company financials", "EN-02", "Unknown", "quarterly", "currency", "brief §1 · Inferred"],
    ["DT-06", "Market and company news", "EN-02, EN-01", "Unknown", "daily", "item", "brief §2 · Inferred"],
    ["DT-07", "Market prices", "EN-02", "Unknown", "intraday or daily", "currency", "brief §2 · Inferred"],
], "Rule check: 7 rows · every row names an entity · sources Unknown on 7 (UN-05)")

write("rules.md", "Rules", "A must or never that holds whatever product is built. Test: a regulator or the firm could make the fact false.",
      ["#", "Rule", "Source", "Severity", "Jurisdiction", "Valid", "Source · Tag"], [5, 44, 9, 9, 12, 8, 15], [
    ["RU-01", "Reports to the PM follow the existing format", "the firm", "Unknown", "the firm", "always", "brief §3 · Reported"],
    ["RU-02", "A material discrepancy between fundamentals and valuation triggers an action recommendation (threshold: UN-03)", "the firm", "Unknown", "the firm", "always", "brief §2 · Reported"],
], "Rule check: 2 rows · 2 with a source · severity Unknown on 2 · no regulatory rule yet (UN-12)")

write("knowledge.md", "Knowledge", "Judgment that may be wrong: views, models, methods. Test: an expert could make the fact false.",
      ["#", "Knowledge", "Owner", "Confidence", "Valid", "Source · Tag"], [5, 45, 16, 10, 14, 15], [
    ["KN-01", "Sector investment logic defines the business of a sector: products, clients, competitive landscape", "research analyst", "Unknown", "until revised", "brief §1 · Reported"],
    ["KN-02", "One investment thesis per watchlist company (EN-04)", "research analyst", "Unknown", "until an event changes it", "brief §1 · Reported"],
    ["KN-03", "Events and policy changes change the outlook of a sector and its companies", "research analyst", "Unknown", "always", "brief §2 · Reported"],
    ["KN-04", "Fundamentals versus valuation is the signal for action", "the firm (should be a role: UN-13)", "Unknown", "always", "brief §2 · Reported"],
], "Rule check: 4 rows · 4 with an owner · confidence Unknown on 4")

write("process.md", "Process", "Ordered steps a role performs. Test: the firm's workflow.",
      ["#", "Step", "Owner", "Reads", "Writes", "Tool", "Next", "Source · Tag"], [5, 22, 16, 13, 12, 10, 5, 15], [
    ["PR-01", "Build the foundation: sector logic, data series, watchlist, theses", "research analyst, knowledge base owner", "DT-01 to DT-05", "EN-01, EN-03, EN-04, EN-06", "TL-03 (Unknown)", "PR-02", "brief §1 · Reported"],
    ["PR-02", "Ingest new information: news, prices, events", "research analyst (wished: agent)", "DT-06, DT-07", "EN-07, EN-10", "none noted", "PR-03", "brief §2 · Reported"],
    ["PR-03", "Update the viewpoint on a company's fundamentals", "research analyst", "EN-07, EN-10, EN-05", "EN-08", "none noted", "PR-04", "brief §2 · Reported"],
    ["PR-04", "Recommend at security level", "research analyst", "EN-08, EN-11", "EN-09", "none noted", "PR-05", "brief §2 · Reported"],
    ["PR-05", "Trigger an action on a material discrepancy", "Unknown (analyst or PM)", "EN-08, EN-11, RU-02", "EN-09", "none noted", "PR-06", "brief §2 · Reported"],
    ["PR-06", "Report to the PM in one of three formats", "research analyst", "EN-09", "EN-12", "TL-01, TL-02", "end", "brief §3 · Reported"],
], "Rule check: 6 steps · 5 with an owner role · 1 owner Unknown (PR-05) · 4 steps with no tool and no manual note (UN-14)")

write("tools.md", "Tools", "An app a role uses today. Test: the vendor or the firm's IT could make the fact false.",
      ["#", "Tool", "Roles", "In", "Out", "Serves", "Source · Tag"], [5, 26, 20, 12, 8, 6, 15], [
    ["TL-01", "Message channel", "research analyst, PM", "report", "read", "PR-06", "brief §3 · Reported"],
    ["TL-02", "Email", "research analyst, PM", "report", "read", "PR-06", "brief §3 · Reported"],
    ["TL-03", "Existing research storage (Unknown what it is: UN-02)", "research analyst", "reports, data", "Unknown", "PR-01", "brief §1 · Inferred"],
], "Rule check: 3 rows · 3 with a role and a step · 1 tool Unknown (TL-03)")

write("exemplars.md", "Exemplars", "Sources kept to be imitated.",
      ["#", "Kind", "Raw", "Keep", "Change", "Becomes", "Tag"], [5, 40, 14, 10, 10, 8, 9], [
    ["EX-01", "Report formats: short alert, one-page update, deep research (UN-04)", "not attached", "Unknown", "Unknown", "EN-12", "Unknown"],
], "Rule check: 1 row · 0 with a raw file")

write("unknowns.md", "Unknowns", "One question each, the kind of gap, and the source that would settle it. UN-01 to UN-08 from the brief harvest; UN-09 to UN-14 raised by cross-bin checks.",
      ["#", "Question", "Kind", "Settles"], [5, 62, 15, 24], [
    ["UN-01", "Which sectors are in scope beyond semiconductors, each with its own data list?", "entity gap", "the PM, the watchlist"],
    ["UN-02", "Who owns the knowledge base today, and where do reports and data live?", "tool gap", "knowledge base owner"],
    ["UN-03", "What counts as a material discrepancy, a number or a judgment, and who decides?", "rule threshold", "the PM"],
    ["UN-04", "What are the existing report formats, as samples?", "exemplar gap", "three reports into raw/"],
    ["UN-05", "Which vendors supply prices, news, memory chip prices, the supply-demand tracker?", "data source", "the analyst, contracts"],
    ["UN-06", "What is the yardstick for a recommendation: hit rate, return versus benchmark?", "charter", "the PM"],
    ["UN-07", "Is \"human investor\" in §1 the PM, or a client?", "role", "Hai"],
    ["UN-08", "Is \"hold for further research\" a fourth recommendation value or a process state?", "entity states", "Hai"],
    ["UN-09", "Are Investment Thesis (EN-04) and Viewpoint (EN-08) one entity or two?", "term conflict", "the analyst"],
    ["UN-10", "Is a Signal (EN-10) an Event (EN-07) judged to matter, or separate?", "term conflict", "the analyst"],
    ["UN-11", "Is sector investment logic (DT-01) data from outside or knowledge the analyst writes (KN-01)?", "bin", "the analyst"],
    ["UN-12", "Which regulatory rules bind research and recommendations: MNPI, research independence, record keeping?", "rule gap", "compliance, research-level0"],
    ["UN-13", "Who owns the fundamentals-versus-valuation rule (KN-04): the PM or the CIO?", "owner", "the PM"],
    ["UN-14", "Which tools serve steps PR-01 to PR-05 today, or are they manual?", "tool gap", "the analyst"],
], "Rule check: 14 questions · 8 from harvest · 6 from sort · 0 settled")

pains = render(["Role", "Job", "Pain", "Source · Tag"], [20, 30, 42, 15], [
    ["research analyst", "ingest new information daily", "too much news, research, prices to read; wants an ingesting agent and a signal retriever", "brief §2 · Reported"],
    ["research analyst", "keep sector logic and data series current", "scattered; wants one knowledge base, SQL plus vector, hybrid search", "brief §1 · Reported"],
    ["research analyst", "maintain theses and financials per watchlist company", "wants them held in the same base", "brief §1 · Reported"],
    ["research analyst", "perform research on each signal", "wants a sector agent to do it", "brief §2 · Reported"],
    ["PM", "read research", "wants the right depth, alert, one page, or deep, by message or email, in the existing format", "brief §3 · Reported"],
    ["knowledge base owner", "build and serve the base", "wants it searchable by humans and agents alike", "brief §1 · Reported"],
])
io.open(os.path.join(HERE, "roles.md"), "w", encoding="utf-8", newline="\n").write(
    "# Roles · equity-research\n\nNot yet built: `roles-level1` has not run. The role list is in `README.md`. Below is the holding block of pains copied by `sort-level1` on 2026-10-21 for `roles-level1` to place. " + RAW + "\n\n```\n Pains (holding block, from candidates/brief-hai-2026-09.md)\n" + pains + "\n```\n")
print("built")
