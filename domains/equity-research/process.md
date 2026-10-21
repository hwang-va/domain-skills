# Process · equity-research

Ordered steps a role performs. Test: the firm's workflow. Placed by `sort-level1`, run by hand 2026-10-21. Raw `brief` = `raw/brief-hai-2026-09.md`.

```
 #     Step                   Owner            Reads         Writes       Tool       Next  Source · Tag
 PR-01 Build the foundation:  research         DT-01 to      EN-01,       TL-03      PR-02 brief §1 ·
       sector logic, data     analyst,         DT-05         EN-03,       (Unknown)        Reported
       series, watchlist,     knowledge base                 EN-04, EN-06
       theses                 owner
 PR-02 Ingest new             research analyst DT-06, DT-07  EN-07, EN-10 none noted PR-03 brief §2 ·
       information: news,     (wished: agent)                                              Reported
       prices, events
 PR-03 Update the viewpoint   research analyst EN-07, EN-10, EN-08        none noted PR-04 brief §2 ·
       on a company's                          EN-05                                       Reported
       fundamentals
 PR-04 Recommend at security  research analyst EN-08, EN-11  EN-09        none noted PR-05 brief §2 ·
       level                                                                               Reported
 PR-05 Trigger an action on a Unknown (analyst EN-08, EN-11, EN-09        none noted PR-06 brief §2 ·
       material discrepancy   or PM)           RU-02                                       Reported
 PR-06 Report to the PM in    research analyst EN-09         EN-12        TL-01,     end   brief §3 ·
       one of three formats                                               TL-02            Reported
Rule check: 6 steps · 5 with an owner role · 1 owner Unknown (PR-05) · 4 steps with no tool and no manual note (UN-14)
```
