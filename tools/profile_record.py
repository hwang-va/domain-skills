"""Profile one record file for harvest-record-level0.

Usage: python tools/profile_record.py <path> [--table NAME] [--sample N]

Reads CSV, TSV, XLSX (first sheet or --table), SQLite (--table), or a markdown
table. Prints one line per column: name, kind, distinct, nulls, unique,
min, max; then the median gap between timestamps for every date column;
then the first N sample rows (default 20). Counts come from here, never from
the model.
"""
import csv
import re
import sqlite3
import statistics
import sys
from datetime import datetime
from pathlib import Path

DATE_FORMATS = ("%Y-%m-%d", "%Y-%m-%d %H:%M", "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S",
                "%m/%d/%Y", "%d.%m.%Y", "%Y%m%d")


def load(path, table):
    p = Path(path)
    ext = p.suffix.lower()
    if ext in (".csv", ".tsv", ".txt"):
        with p.open(newline="", encoding="utf-8-sig") as f:
            rows = list(csv.reader(f, delimiter="\t" if ext == ".tsv" else ","))
        return rows[0], rows[1:]
    if ext in (".db", ".sqlite", ".sqlite3"):
        con = sqlite3.connect(str(p))
        if not table:
            names = [r[0] for r in con.execute("select name from sqlite_master where type='table'")]
            sys.exit("sqlite needs --table; tables: " + ", ".join(names))
        cur = con.execute(f'select * from "{table}"')
        return [d[0] for d in cur.description], [list(r) for r in cur.fetchall()]
    if ext in (".xlsx", ".xlsm"):
        import openpyxl  # installed on this machine; stdlib has no xlsx reader
        wb = openpyxl.load_workbook(str(p), read_only=True, data_only=True)
        ws = wb[table] if table else wb.worksheets[0]
        rows = [list(r) for r in ws.iter_rows(values_only=True)]
        return [str(h) for h in rows[0]], rows[1:]
    if ext in (".md", ".markdown"):
        lines = [l for l in p.read_text(encoding="utf-8").splitlines() if l.strip().startswith("|")]
        cells = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines]
        cells = [r for r in cells if not all(re.fullmatch(r":?-+:?", c) for c in r)]
        return cells[0], cells[1:]
    sys.exit(f"unsupported extension {ext}")


def parse_date(v):
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(str(v).strip(), fmt)
        except ValueError:
            pass
    return None


def kind_of(values):
    if not values:
        return "empty"
    if all(parse_date(v) for v in values):
        return "date"
    try:
        [float(str(v).replace(",", "")) for v in values]
        return "number"
    except ValueError:
        return "text"


def profile(header, rows):
    n = len(rows)
    print(f"rows: {n}  columns: {len(header)}")
    print(f"{'column':<24}{'kind':<8}{'distinct':>9}{'nulls':>7}{'unique':>8}  min .. max")
    dates = {}
    for i, name in enumerate(header):
        col = [r[i] if i < len(r) else None for r in rows]
        vals = [v for v in col if v not in (None, "", "NULL", "null", "NA", "n/a")]
        kind = kind_of(vals)
        distinct = len(set(map(str, vals)))
        unique = "yes" if vals and distinct == n else "no"
        lo = hi = ""
        if kind == "date":
            ds = sorted(parse_date(v) for v in vals)
            dates[name] = ds
            lo, hi = ds[0].date(), ds[-1].date()
        elif kind == "number":
            nums = [float(str(v).replace(",", "")) for v in vals]
            lo, hi = min(nums), max(nums)
        print(f"{name[:23]:<24}{kind:<8}{distinct:>9}{n - len(vals):>7}{unique:>8}  {lo} .. {hi}")
    for name, ds in dates.items():
        gaps = [(b - a).total_seconds() / 86400 for a, b in zip(ds, ds[1:]) if b != a]
        if gaps:
            print(f"cadence {name}: median gap {statistics.median(gaps):.1f} days over {len(ds)} stamps")


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    table = args[args.index("--table") + 1] if "--table" in args else None
    sample = int(args[args.index("--sample") + 1]) if "--sample" in args else 20
    header, rows = load(args[0], table)
    profile(header, rows)
    print(f"sample {min(sample, len(rows))} of {len(rows)} rows")
    print(" | ".join(header))
    for r in rows[:sample]:
        print(" | ".join("" if v is None else str(v) for v in r))


if __name__ == "__main__":
    main()
