# Entities · equity-research

Nouns with an identity and a lifecycle. Test: nobody could make the fact false. Placed by `sort-level1`, run by hand 2026-10-21. Raw `brief` = `raw/brief-hai-2026-09.md`.

```
 #     Entity            Definition                           Identifier     States             Source · Tag
 EN-01 Sector            a market segment with its own        name           covered, not       brief §1 ·
                         investment logic and data series                    covered            Reported
 EN-02 Company           a listed business the fund may       ticker, ISIN   watch, held,       brief §1 ·
                         research or hold                     (Unknown)      exited             Reported
 EN-03 Watchlist         the fund's list of companies under   name           Unknown            brief §1 ·
                         coverage                                                               Reported
 EN-04 Investment Thesis the standing view on one company,    company        current, revised,  brief §1 ·
                         held with it; synonym candidate:                    closed             Reported
                         Viewpoint (UN-09)
 EN-05 Financials        a company's reported figures, held   company,       Unknown            brief §1 ·
                         with it                              period                            Reported
 EN-06 Knowledge Base    the fund's collected research and    Unknown        Unknown            brief §1 ·
                         data, referred to by investors and                                     Reported
                         analysts
 EN-07 Event             a sector event, corporate event, or  Unknown        new, assessed      brief §2 ·
                         industry policy change                                                 Reported
 EN-08 Viewpoint         the current view on a company's      company, date  current,           brief §2 ·
                         fundamentals, updated on events;                    superseded         Reported
                         overlap with EN-04 (UN-09)
 EN-09 Recommendation    buy, sell, or hold at security       company, date  draft, issued,     brief §2 ·
                         level, with a rationale; "hold for                  acted, closed      Reported
                         further research": UN-08
 EN-10 Signal            a retrieved item of new information  Unknown        new, researched,   brief §2 ·
                         judged to matter; relation to EN-07                 dismissed          Reported
                         (UN-10)
 EN-11 Valuation         the market's price level for a       company, date  Unknown            brief §2 ·
                         company, compared to fundamentals                                      Reported
 EN-12 Report            the output to the PM; kinds: short   Unknown        draft, sent, read  brief §3 ·
                         alert, one-page update, deep                                           Reported
                         research
Rule check: 12 rows · 12 Reported · identifiers Unknown on 5 · relations open: UN-09, UN-10
```
