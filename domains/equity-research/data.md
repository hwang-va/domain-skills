# Data · equity-research

Values about an entity that arrive from outside. Test: a vendor or a sensor could make the fact false. Placed by `sort-level1`, run by hand 2026-10-21. Raw `brief` = `raw/brief-hai-2026-09.md`.

```
 #     Data                     About        Source             Cadence      Unit       Source · Tag
 DT-01 Sector investment logic  EN-01        Unknown (analyst   Unknown      text       brief §1 ·
       (products, clients,                   written? UN-11)                            Reported
       competitive landscape)
 DT-02 Memory chip price (semi) EN-01        Unknown vendor     Unknown      USD per    brief §1 ·
                                                                             unit       Reported
 DT-03 Supply-demand tracker    EN-01        Unknown vendor     Unknown      Unknown    brief §1 ·
       (semi)                                                                           Reported
 DT-04 Research reports         EN-02, EN-01 brokers, Unknown   Unknown      document   brief §1 ·
                                             which                                      Reported
 DT-05 Company financials       EN-02        Unknown            quarterly    currency   brief §1 ·
                                                                                        Inferred
 DT-06 Market and company news  EN-02, EN-01 Unknown            daily        item       brief §2 ·
                                                                                        Inferred
 DT-07 Market prices            EN-02        Unknown            intraday or  currency   brief §2 ·
                                                                daily                   Inferred
Rule check: 7 rows · every row names an entity · sources Unknown on 7 (UN-05)
```
