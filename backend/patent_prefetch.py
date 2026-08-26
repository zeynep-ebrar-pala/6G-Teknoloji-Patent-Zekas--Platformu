"""
Lens sayımlarını arka planda doldurur. Streamlit betiği bitince menü serbest kalır.
"""

from __future__ import annotations

import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from data.patents import SPEC_COMPANIES, TECHNOLOGY_DOMAINS

from backend.years import end_year, read_json, trend_years, write_json

_ROOT = Path(__file__).resolve().parents[1]
_STATUS = _ROOT / "data" / "cache" / "patent_prefetch_status.json"
_ROWS = _ROOT / "data" / "cache" / "patent_vendor_rows.json"
_lock = threading.Lock()
_work_lock = threading.Lock()
_threads: Dict[str, threading.Thread] = {}


def _years() -> tuple[int, ...]:
    return tuple(trend_years())


def _job_key(topic: Optional[str], companies: Tuple[str, ...]) -> str:
    return f"{topic or 'all'}|{'|'.join(companies)}"


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    write_json(path, payload)


def _read_json(path: Path) -> Dict[str, Any]:
    return read_json(path)


def _status_set(**fields: Any) -> None:
    data = _read_json(_STATUS)
    data.update(fields)
    data["at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    _write_json(_STATUS, data)


def _queries(topic: Optional[str], companies: Tuple[str, ...]) -> List[str]:
    from backend.patent_apis import _applicant_clause, lens_assignee_dsl, lens_explorer_dsl, lens_topic_dsl

    names = [c for c in companies if c]
    axes = [topic] if topic else list(TECHNOLOGY_DOMAINS)
    dsl = lens_topic_dsl(topic) if topic else lens_explorer_dsl()
    applicant_or = " OR ".join(_applicant_clause(n) for n in names)
    out: List[str] = []
    out.append(dsl)
    for name in names:
        out.append(f"{dsl} AND {_applicant_clause(name)}")
    for axis in axes:
        out.append(f"{lens_topic_dsl(axis)} AND ({applicant_or})")
    for axis in TECHNOLOGY_DOMAINS:
        for name in names:
            out.append(lens_assignee_dsl(axis, name))
    for name in names:
        for year in _years():
            out.append(f"{dsl} AND {_applicant_clause(name)} AND year_published:{year}")
    return out


def _work(topic: Optional[str], companies: Tuple[str, ...]) -> None:
    from backend.config import reload_env
    from backend.patent_apis import (
        _applicant_clause,
        _lens_count,
        _rows_from_lens,
        lens_search,
        lens_topic_dsl,
    )
    from backend.patent_service import _company_match, _from_lens

    with _work_lock:
        reload_env()
        done = 0
        total = 1
        try:
            queries = _queries(topic, companies)
            total = len(queries) + (1 if topic else len(TECHNOLOGY_DOMAINS))
            _status_set(running=True, done=0, total=total, error="", job=_job_key(topic, companies))
            for q in queries:
                _lens_count(q, force=True)
                done += 1
                _status_set(running=True, done=done, total=total)
                time.sleep(0.08)
            names = [c for c in companies if c]
            applicant_or = " OR ".join(_applicant_clause(n) for n in names)
            topics = [topic] if topic else list(TECHNOLOGY_DOMAINS)
            rows_out: List[Dict[str, Any]] = []
            seen: set = set()
            for axis in topics:
                data = lens_search(f"{lens_topic_dsl(axis)} AND ({applicant_or})", size=100)
                done += 1
                _status_set(running=True, done=done, total=total)
                time.sleep(0.12)
                for raw in _rows_from_lens(data or {}):
                    company = _company_match(raw.get("assignee") or "")
                    if not company:
                        continue
                    payload = dict(raw)
                    payload["assignee"] = company
                    rec = _from_lens(payload, axis)
                    if not rec:
                        continue
                    pub = rec.get("publication_number") or ""
                    if not pub or pub in seen:
                        continue
                    seen.add(pub)
                    rows_out.append(rec)
            blob = _read_json(_ROWS)
            key = _job_key(topic, tuple(SPEC_COMPANIES))
            if rows_out:
                blob[key] = rows_out
                _write_json(_ROWS, blob)
            _status_set(
                running=False,
                done=total,
                total=total,
                fetched_at=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
                year_end=end_year(),
            )
        except Exception as exc:
            _status_set(running=False, error=str(exc)[:240], done=done, total=total)


def ensure_prefetch(topic: Optional[str], companies: Tuple[str, ...], *, force: bool = False) -> None:
    from backend.years import should_refresh

    key = _job_key(topic, companies)
    snap = snapshot(topic, companies)
    st = _read_json(_STATUS)
    stored = st.get("year_end")
    try:
        stored_end = int(stored) if stored is not None else None
    except (TypeError, ValueError):
        stored_end = None
    with _lock:
        alive = _threads.get(key)
        if alive is not None and alive.is_alive():
            return
        if not should_refresh(
            complete=bool(snap.get("complete")),
            fetched_at=str(st.get("fetched_at") or ""),
            year_end=stored_end,
            force=force,
            running=False,
        ):
            return
        _status_set(running=True, done=0, total=max(int(snap.get("total") or 1), 1), error="", job=key)
        t = threading.Thread(target=_work, args=(topic, companies), daemon=True, name=f"lens-{key[:24]}")
        _threads[key] = t
        t.start()


def _topic_year_work(topic: str) -> None:
    from backend.config import reload_env
    from backend.patent_apis import _lens_count, lens_topic_year_query

    reload_env()
    for year in _years():
        _lens_count(lens_topic_year_query(topic, int(year)), force=True)
        time.sleep(0.05)
    st = _read_json(_STATUS)
    stamps = st.get("topic_years") if isinstance(st.get("topic_years"), dict) else {}
    stamps[topic] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    _status_set(topic_years=stamps, year_end=end_year())


def ensure_topic_year_prefetch(topic: str, *, force: bool = False) -> None:
    """Teknoloji sayfası: konu × yıl Lens total. Firma süzgeci yok."""
    from backend.years import should_refresh

    name = (topic or "").strip()
    if not name:
        return
    from backend.config import get_lens_token
    from backend.patent_apis import peek_topic_year_counts

    if not get_lens_token():
        return
    years = _years()
    counts = peek_topic_year_counts(name, years)
    complete = all(isinstance(n, int) for n in counts.values())
    key = f"ty|{name}"
    with _lock:
        alive = _threads.get(key)
        if alive is not None and alive.is_alive():
            return
        fetched = ""
        stamps = _read_json(_STATUS).get("topic_years")
        if isinstance(stamps, dict):
            fetched = str(stamps.get(name) or "")
        stored_end = _read_json(_STATUS).get("year_end")
        try:
            year_end = int(stored_end) if stored_end is not None else None
        except (TypeError, ValueError):
            year_end = None
        if not should_refresh(
            complete=complete,
            fetched_at=fetched,
            year_end=year_end,
            force=force,
            running=False,
        ):
            return
        t = threading.Thread(target=_topic_year_work, args=(name,), daemon=True, name=f"lens-year-{name}")
        _threads[key] = t
        t.start()


def load_vendor_rows(topic: Optional[str]) -> List[Dict[str, Any]]:
    blob = _read_json(_ROWS)
    key = _job_key(topic, tuple(SPEC_COMPANIES))
    rows = blob.get(key)
    if isinstance(rows, list):
        return [r for r in rows if isinstance(r, dict)]
    return []


def snapshot(topic: Optional[str], companies: Tuple[str, ...]) -> Dict[str, Any]:
    from backend.patent_apis import (
        _applicant_clause,
        lens_assignee_dsl,
        lens_explorer_dsl,
        lens_topic_dsl,
        peek_lens_count_map,
    )

    cached = peek_lens_count_map()

    def _n(query: str) -> Optional[int]:
        hit = cached.get(query)
        return int(hit) if isinstance(hit, int) else None

    names = [c for c in companies if c]
    dsl = lens_topic_dsl(topic) if topic else lens_explorer_dsl()
    applicant_or = " OR ".join(_applicant_clause(n) for n in names)
    axes = list(TECHNOLOGY_DOMAINS)
    firm = {n: _n(f"{dsl} AND {_applicant_clause(n)}") for n in names}
    topics = {axis: _n(f"{lens_topic_dsl(axis)} AND ({applicant_or})") for axis in axes}
    matrix: Dict[str, Dict[str, Optional[int]]] = {}
    for name in names:
        matrix[name] = {axis: _n(lens_assignee_dsl(axis, name)) for axis in axes}
    years: Dict[str, Dict[int, Optional[int]]] = {}
    for name in names:
        years[name] = {
            y: _n(f"{dsl} AND {_applicant_clause(name)} AND year_published:{y}")
            for y in _years()
        }
    st = _read_json(_STATUS)
    queries = _queries(topic, companies)
    pending = sum(1 for q in queries if _n(q) is None)
    rows = load_vendor_rows(topic)
    complete = pending == 0 and bool(rows)
    return {
        "running": bool(st.get("running")),
        "done": int(st.get("done") or 0),
        "total": int(st.get("total") or max(len(queries), 1)),
        "error": str(st.get("error") or ""),
        "firm": firm,
        "topics": topics,
        "matrix": matrix,
        "years": years,
        "rows": rows,
        "complete": complete,
        "year_list": list(_years()),
    }


def frames_from_snapshot(
    snap: Dict[str, Any], companies: List[str]
) -> Tuple[Dict[str, int], Dict[str, int], Any, Any, Any]:
    import pandas as pd

    names = [c for c in companies if c]
    firm = {n: int(v) for n, v in (snap.get("firm") or {}).items() if isinstance(v, int) and n in names}
    topics = {k: int(v) for k, v in (snap.get("topics") or {}).items() if isinstance(v, int)}
    matrix = snap.get("matrix") or {}
    dens_rows: List[Dict[str, Any]] = []
    for comp in names:
        row: Dict[str, Any] = {"Company": comp}
        ok = True
        for axis in TECHNOLOGY_DOMAINS:
            n = (matrix.get(comp) or {}).get(axis)
            if not isinstance(n, int):
                ok = False
                break
            row[axis] = n
        if ok:
            dens_rows.append(row)
    df_density = pd.DataFrame(dens_rows)
    years = snap.get("years") or {}
    year_list = list(snap.get("year_list") or _years())
    ready = [
        comp
        for comp in names
        if all(isinstance((years.get(comp) or {}).get(y), int) for y in year_list)
    ]
    if ready:
        trend: Dict[str, List[int]] = {"Years": [int(y) for y in year_list]}
        for comp in ready:
            trend[comp] = [int((years.get(comp) or {}).get(y) or 0) for y in year_list]
        df_trends = pd.DataFrame(trend)
    else:
        df_trends = pd.DataFrame()
    records = []
    if not df_density.empty:
        axes = [c for c in df_density.columns if c != "Company"]
        for _, row in df_density.iterrows():
            comp = str(row["Company"])
            for axis in axes:
                n = int(row.get(axis) or 0)
                if n <= 0:
                    continue
                records.append({"company": comp, "domain": axis, "n": n})
    df_tree = pd.DataFrame(records)
    return firm, topics, df_density, df_trends, df_tree
