"""Count variable roles in jorma markdown tables embedded in files."""

import re
import sys
from collections import Counter
from pathlib import Path

# Matches a table data row (not a header or separator line).
# Captures the last non-empty cell, which is the role column in both
# static tables (Scope | Variable | Role | Location) and dynamic tables
# (Variable | Scope | Role).
_ROW = re.compile(r"^\|[^|]+\|[^|]+\|([^|]+)\|")

# Header words that appear in the role column — skip these rows.
_HEADER_WORDS = {"role", "location"}


def count_in_file(path: Path) -> Counter:
    counts: Counter = Counter()
    for line in path.read_text(encoding="utf-8").splitlines():
        m = _ROW.match(line.strip())
        if not m:
            continue
        cell = m.group(1).strip().lower().lstrip(":")
        if cell in _HEADER_WORDS or set(cell) == {"-"}:
            continue
        counts[cell] += 1
    return counts


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} FILE [FILE ...]", file=sys.stderr)
        sys.exit(1)

    totals: Counter = Counter()
    for arg in sys.argv[1:]:
        path = Path(arg)
        if not path.exists():
            print(f"Warning: '{path}' not found", file=sys.stderr)
            continue
        totals.update(count_in_file(path))

    if not totals:
        print("No roles found.")
        return

    width = max(len(role) for role in totals)
    for role, count in sorted(totals.items()):
        print(f"{role:<{width}}  {count}")


if __name__ == "__main__":
    main()
