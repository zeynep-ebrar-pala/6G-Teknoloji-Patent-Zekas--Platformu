"""Development/CI check: TR/EN translation key parity."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from i18n.check import run_all  # noqa: E402


def main() -> int:
    problems = run_all()
    if problems:
        print(f"{len(problems)} i18n problem(s):")
        for line in problems:
            print(f"  - {line}")
        return 1
    print("i18n OK: UI catalogs, beginner copy, expert depth, tech overlay, glossary.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
