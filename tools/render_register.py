"""Render a register as fixed-width ASCII rows, wrapping cells so no line exceeds WIDTH.

Usage inside a script: render(headers, widths, rows) -> str. A row is a list of cell strings.
ponytail: plain textwrap per cell, no alignment of wrapped lines beyond the column start.
"""
import textwrap

WIDTH = 110


def render(headers, widths, rows):
    assert sum(widths) + len(widths) - 1 <= WIDTH, sum(widths)
    out = []

    def line(cells):
        wrapped = [textwrap.wrap(c, w) or [""] for c, w in zip(cells, widths)]
        n = max(len(x) for x in wrapped)
        for i in range(n):
            parts = []
            for col, w in zip(wrapped, widths):
                parts.append((col[i] if i < len(col) else "").ljust(w))
            out.append((" " + " ".join(parts)).rstrip())

    line(headers)
    for r in rows:
        line(r)
    return "\n".join(out)


if __name__ == "__main__":
    s = render(["#", "Name"], [5, 20], [["X-01", "a " * 30]])
    assert all(len(l) <= WIDTH for l in s.split("\n"))
    print("ok")
