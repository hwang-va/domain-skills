# Candidates: `raw/brief-hai-2026-09.md`

**Harvest:** `harvest-doc-level0`, run by hand in chat 2026-10-21 (plugin not reloaded). Document: a product brief by Hai, three paragraphs, no headings; read as three sections, §1 foundation, §2 ingestion and research, §3 reporting. Roles in scope from `README.md`: PM, research analyst, knowledge base owner. Grade: Reported (a request, not a record). Tags per line.

**Elements:**
- **Sections read:** §1 foundation and knowledge base; §2 new information, viewpoints, triggers; §3 reports to the PM. None skipped.
- **Roles touched:** PM (§3 reader), research analyst (§2 actor), knowledge base owner (§1 implied). "Human investor" in §1 reads as the PM. "AI agents", "ingesting agent", "sector AI agent" are wished workers: pains, not roles.
- **Dropped as out of scope:** none; every noun touches a role in scope.
- **Wishes separated:** SQL and vector database, hybrid RAG, ingestion system, agents, delivery automation: six pain lines, no bin line.

---

```
 Bin        Fact                                                                      Source §  Tag
 entity     Sector: a market segment with its own investment logic and data series   §1        Reported
 entity     Company: a listed business the fund may research or hold                 §1        Reported
 entity     Watchlist: the fund's list of companies under coverage                    §1        Reported
 entity     Investment Thesis: the standing view on one company, held with it         §1        Reported
 entity     Financials: a company's reported figures, held with it                    §1        Reported
 entity     Knowledge Base: the fund's collected research and data, referred to by    §1        Reported
            investors and analysts
 entity     Event: a sector event, corporate event, or industry policy change         §2        Reported
 entity     Viewpoint: the current view on a company's fundamentals, updated on events §2        Reported
 entity     Recommendation: buy, sell, or hold, at security level, with a rationale   §2        Reported
 entity     Signal: a retrieved item of new information judged to matter              §2        Reported
 entity     Valuation: the market's price level for a company, compared to fundamentals §2      Reported
 entity     Report: the output to the PM; kinds: short alert, one-page update, deep    §3        Reported
            research
 data       Sector investment logic: products, clients, competitive landscape │ about  §1        Reported
            Sector │ source: Unknown │ cadence: Unknown
 data       Memory chip price │ about Sector (semi) │ source: Unknown │ cadence: Unknown §1      Reported
 data       Supply-demand tracker │ about Sector (semi) │ source: Unknown              §1        Reported
 data       Research reports │ about Company, Sector │ source: brokers, Unknown which  §1        Reported
 data       Company financials │ about Company │ source: Unknown │ cadence: quarterly  §1        Inferred
 data       Market and company news │ about Company, Sector │ source: Unknown │ daily  §2        Inferred
 data       Market prices │ about Company │ source: Unknown │ cadence: intraday or daily §2      Inferred
 rule       Reports follow the existing format │ source: the firm │ severity: Unknown  §3        Reported
 rule       A material discrepancy between fundamentals and valuation triggers an      §2        Reported
            action recommendation │ source: the firm │ threshold: Unknown
 knowledge  Sector investment logic defines the business of a sector │ owner: analyst  §1        Reported
            │ confidence: Unknown
 knowledge  An investment thesis per watchlist company │ owner: analyst │ validity:    §1        Reported
            until an event changes it
 knowledge  Events and policy changes change the outlook of a sector and its companies §2        Reported
            │ owner: analyst
 knowledge  Fundamentals versus valuation is the signal for action │ owner: the firm   §2        Reported
 process    1 build foundation: sector logic, data series, watchlist, theses │ owner:  §1        Reported
            analyst, knowledge base owner │ writes Knowledge Base
 process    2 ingest new information: news, prices, events │ owner: analyst (wished:   §2        Reported
            agent) │ reads Event, Signal
 process    3 update viewpoint on company fundamentals │ owner: analyst │ writes       §2        Reported
            Viewpoint
 process    4 recommend at security level │ owner: analyst │ writes Recommendation     §2        Reported
 process    5 trigger action on material discrepancy │ owner: Unknown (analyst or PM)  §2        Reported
 process    6 report to the PM in one of three formats │ owner: analyst │ writes Report §3        Reported
            │ tool: message, email
 tool       Message channel │ roles: analyst, PM │ in: report │ out: read │ serves 6   §3        Reported
 tool       Email │ roles: analyst, PM │ in: report │ out: read │ serves 6             §3        Reported
 tool       Existing research storage, where reports and data live today │ roles:      §1        Inferred
            analyst │ Unknown what it is
```

---

```
 Pains and exemplars
 pain       research analyst │ ingest new information daily │ too much news, research, §2        Reported
            prices to read; wants an ingesting agent and a signal retriever
 pain       research analyst │ keep sector logic and data series current │ scattered;  §1        Reported
            wants one knowledge base, SQL plus vector, hybrid search
 pain       research analyst │ maintain theses and financials per watchlist company │  §1        Reported
            wants them held in the same base
 pain       research analyst │ perform research on each signal │ wants a sector agent  §2        Reported
            to do it
 pain       PM │ read research │ wants the right depth: alert, one page, or deep, by    §3        Reported
            message or email, in the existing format
 pain       knowledge base owner │ build and serve the base │ wants it searchable by   §1        Reported
            humans and agents alike
 exemplar   Report formats: short alert, one-page update, deep research │ raw: not     §3        Unknown
            attached │ keep: Unknown │ becomes Report
```

---

**Unknowns:**
- Unknown: Which sectors are in scope beyond semiconductors, and does each have its own data series list? Settles: the PM or the watchlist.
- Unknown: Who owns the knowledge base today, and where do research reports and data live? Settles: the knowledge base owner, a records harvest.
- Unknown: What counts as a material discrepancy between fundamentals and valuation, a number or a judgment, and who decides the trigger? Settles: the PM.
- Unknown: What are the existing report formats, as samples? Settles: three real reports into `raw/`, one per kind.
- Unknown: Which data vendors supply prices, news, memory chip prices, and the supply-demand tracker? Settles: the analyst or the vendor contracts.
- Unknown: What is the yardstick for a recommendation, hit rate, return against benchmark, or something the PM uses? Settles: the PM.
- Unknown: Is "human investor" in §1 the PM, or a client? Settles: Hai.
- Unknown: Is "hold for further research" a fourth recommendation value or a process state? Settles: Hai.
