"""
Yayın / patent yıl penceresi — 2020’den içinde bulunulan takvim yılına kadar genişler.
Sabit 2026 tavanı yeni yılı düşürmesin.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional

START_YEAR = 2020


def current_year() -> int:
    return datetime.now(timezone.utc).year


def end_year() -> int:
    return max(int(current_year()), START_YEAR)


def year_window() -> tuple[int, int]:
    return (START_YEAR, end_year())


def last5_window() -> tuple[int, int]:
    y1 = end_year()
    return (y1 - 4, y1)


def trend_years() -> list[int]:
    y0, y1 = year_window()
    return list(range(y0, y1 + 1))


def year_tuple() -> tuple[int, ...]:
    return tuple(trend_years())


def span_label() -> str:
    y0, y1 = year_window()
    return f"{y0}–{y1}"


def last5_label() -> str:
    y0, y1 = last5_window()
    return f"{y0}–{y1}"


def format_fields() -> Dict[str, Any]:
    y0, y1 = year_window()
    l0, l1 = last5_window()
    return {"y0": y0, "y1": y1, "l0": l0, "l1": l1, "end": y1}


def should_refresh(
    *,
    complete: bool,
    fetched_at: str = "",
    year_end: Optional[int] = None,
    force: bool = False,
    running: bool = False,
    debounce_s: float = 15 * 60,
    max_stale_s: float = 6 * 60 * 60,
) -> bool:
    """Eksik, yıl penceresi büyümüş veya bayat önbellek → arka plan işi."""
    if running:
        return False
    if not complete:
        return True
    if year_end is not None and int(year_end) < int(end_year()):
        return True
    age = age_seconds(fetched_at)
    if age is None:
        return bool(force)
    if age >= max_stale_s:
        return True
    if force and age >= debounce_s:
        return True
    return False


def parse_utc(raw: str) -> Optional[datetime]:
    text = (raw or "").strip()
    if not text:
        return None
    for fmt in ("%Y-%m-%d %H:%M UTC", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d"):
        try:
            dt = datetime.strptime(text, fmt)
            return dt.replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def age_seconds(raw: str) -> Optional[float]:
    dt = parse_utc(raw)
    if dt is None:
        return None
    return max(0.0, (datetime.now(timezone.utc) - dt).total_seconds())


def read_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    blob = json.dumps(payload, ensure_ascii=False, indent=2)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(blob, encoding="utf-8")
    tmp.replace(path)
