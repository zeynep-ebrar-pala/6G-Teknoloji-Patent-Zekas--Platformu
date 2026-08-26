"""
Avrupa MNO yayın sayımı — Springer Nature Meta metin «6G {firma} {ülke}».
Bağlılık facet değildir. Sayı gelmezse None; uydurulmaz.
Sayfa diskten açılır; ağ arka planda doldurur.
"""

from __future__ import annotations

import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from backend.config import get_springer_api_key, reload_env
from backend.publisher_apis import _q6g, _springer_count, peek_springer_count
from backend.years import end_year, read_json, should_refresh, write_json
from data.eu_operators import TT_OPERATOR, countries_for_region

CACHE_PATH = Path(__file__).resolve().parents[1] / "data" / "cache" / "mno_pub_live.json"
STATUS_PATH = Path(__file__).resolve().parents[1] / "data" / "cache" / "mno_pub_status.json"

_lock = threading.Lock()
_work_lock = threading.Lock()
_threads: Dict[str, threading.Thread] = {}


def _topic_key(topic: Optional[str]) -> str:
    name = (topic or "").strip()
    return name or "all"


def _query(topic: Optional[str], search: str, country_en: str) -> str:
    base = _q6g(topic)
    firm = (search or "").strip()
    place = (country_en or "").strip()
    return f'{base} "{firm}" {place}'.strip()


def _place(country: Dict[str, Any]) -> str:
    if str(country.get("cc") or "") == "TR":
        return "Turkey"
    return str(country.get("name_en") or "")


def _jobs(topic: Optional[str]) -> List[Dict[str, str]]:
    """Avrupa ülkesi × kilitli 3 MNO + Türk Telekom (Türkiye). TR üçlüsü bu eksende yok."""
    out: List[Dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for country in countries_for_region("eu"):
        place = _place(country)
        cc = str(country.get("cc") or "")
        for op in country.get("operators") or []:
            if not isinstance(op, dict):
                continue
            search = str(op.get("search") or op.get("name") or "").strip()
            if not search or not place:
                continue
            key = (search.casefold(), place.casefold())
            if key in seen:
                continue
            seen.add(key)
            out.append(
                {
                    "cc": cc,
                    "op_id": str(op.get("id") or search),
                    "search": search,
                    "place": place,
                    "query": _query(topic, search, place),
                }
            )
    tt_search = str(TT_OPERATOR.get("search") or "Turk Telekom")
    tt_key = (tt_search.casefold(), "turkey")
    if tt_key not in seen:
        out.append(
            {
                "cc": "TR",
                "op_id": "tt",
                "search": tt_search,
                "place": "Turkey",
                "query": _query(topic, tt_search, "Turkey"),
            }
        )
    return out


def peek_op_count(topic: Optional[str], search: str, country_en: str) -> Optional[int]:
    return peek_springer_count(_query(topic, search, country_en), None)


def _status_set(**fields: Any) -> None:
    data = read_json(STATUS_PATH)
    data.update(fields)
    data["at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    write_json(STATUS_PATH, data)


def prefetch_status() -> Dict[str, Any]:
    st = read_json(STATUS_PATH)
    return {
        "running": bool(st.get("running")),
        "done": int(st.get("done") or 0),
        "total": int(st.get("total") or 0),
        "error": str(st.get("error") or ""),
        "fetched_at": str(st.get("fetched_at") or ""),
        "year_end": st.get("year_end"),
    }


def _work(topic: Optional[str]) -> None:
    with _work_lock:
        reload_env()
        jobs = _jobs(topic)
        total = max(len(jobs), 1)
        done = 0
        _status_set(running=True, done=0, total=total, error="", topic=_topic_key(topic))
        try:
            for job in jobs:
                _springer_count(job["query"], None, force=True)
                done += 1
                _status_set(running=True, done=done, total=total)
                time.sleep(0.12)
            stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
            _status_set(
                running=False,
                done=total,
                total=total,
                fetched_at=stamp,
                year_end=end_year(),
            )
            blob = read_json(CACHE_PATH)
            blob[_topic_key(topic)] = {"fetched_at": stamp, "year_end": end_year()}
            write_json(CACHE_PATH, blob)
        except Exception as exc:
            _status_set(
                running=False,
                error=str(exc)[:240],
                done=done,
                total=total,
                fetched_at=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
            )


def ensure_prefetch(topic: Optional[str] = None, *, force: bool = False) -> None:
    if not get_springer_api_key():
        return
    key = _topic_key(topic)
    jobs = _jobs(topic)
    complete = bool(jobs) and all(
        isinstance(peek_springer_count(job["query"], None), int) for job in jobs
    )
    blob = read_json(CACHE_PATH)
    meta = blob.get(key) if isinstance(blob.get(key), dict) else {}
    st = prefetch_status()
    stored = meta.get("year_end", st.get("year_end"))
    try:
        stored_end = int(stored) if stored is not None else None
    except (TypeError, ValueError):
        stored_end = None
    with _lock:
        alive = _threads.get(key)
        if alive is not None and alive.is_alive():
            return
        if not should_refresh(
            complete=complete,
            fetched_at=str(meta.get("fetched_at") or st.get("fetched_at") or ""),
            year_end=stored_end,
            force=force,
            running=False,
        ):
            return
        _status_set(running=True, done=0, total=max(len(jobs), 1), error="", topic=key)
        t = threading.Thread(target=_work, args=(topic,), daemon=True, name=f"mno-pub-{key}")
        _threads[key] = t
        t.start()


def _op_rows(country: Dict[str, Any], topic: Optional[str]) -> List[Dict[str, Any]]:
    place = _place(country)
    out: List[Dict[str, Any]] = []
    for op in country.get("operators") or []:
        if not isinstance(op, dict):
            continue
        search = str(op.get("search") or op.get("name") or "").strip()
        n = peek_op_count(topic, search, place) if search else None
        out.append(
            {
                "id": str(op.get("id") or ""),
                "name": str(op.get("name") or search),
                "search": search,
                "n": n,
                "is_tt": bool(op.get("is_tt") or op.get("id") == "tt"),
                "query": _query(topic, search, place),
            }
        )
    return out


def country_leader(country: Dict[str, Any], topic: Optional[str]) -> Optional[Dict[str, Any]]:
    measured = [r for r in _op_rows(country, topic) if isinstance(r.get("n"), int)]
    if not measured:
        return None
    lead = max(measured, key=lambda r: (int(r["n"]), r["name"]))
    return {
        "cc": country["cc"],
        "name_tr": country["name_tr"],
        "name_en": country["name_en"],
        "lead_name": lead["name"],
        "lead_n": int(lead["n"]),
        "is_tt": bool(lead.get("is_tt")),
        "query": lead["query"],
        "ops": _op_rows(country, topic),
    }


def tt_count(topic: Optional[str]) -> Optional[int]:
    search = str(TT_OPERATOR.get("search") or "Turk Telekom")
    return peek_op_count(topic, search, "Turkey")


def europe_leader_rows(topic: Optional[str] = None) -> List[Dict[str, Any]]:
    """Her Avrupa ülkesi: kilitli 3 MNO içinden en yüksek Springer sayısı."""
    rows: List[Dict[str, Any]] = []
    for country in countries_for_region("eu"):
        hit = country_leader(country, topic)
        if hit and int(hit.get("lead_n") or 0) > 0:
            rows.append(hit)
    rows.sort(key=lambda r: (-int(r["lead_n"]), str(r.get("cc") or "")))
    return rows


def tt_europe_place(topic: Optional[str] = None) -> Dict[str, Any]:
    """TT sayısı, Avrupa ülke liderleri arasında sıra. Rakip ölçülmediyse sıra yok."""
    leaders = europe_leader_rows(topic)
    tt_n = tt_count(topic)
    field = [int(r["lead_n"]) for r in leaders if isinstance(r.get("lead_n"), int)]
    rank = None
    if isinstance(tt_n, int) and field:
        better = sum(1 for n in field if n > tt_n)
        rank = better + 1
        field_n = len(field) + 1
    else:
        field_n = len(field)
    top = leaders[0] if leaders else None
    return {
        "tt_n": tt_n,
        "rank": rank,
        "field_n": field_n,
        "leaders": leaders,
        "top_name": None if not top else top.get("lead_name"),
        "top_cc": None if not top else top.get("cc"),
        "top_n": None if not top else top.get("lead_n"),
        "tt_query": _query(topic, str(TT_OPERATOR.get("search") or "Turk Telekom"), "Turkey"),
    }


def chart_rows(topic: Optional[str] = None) -> List[Dict[str, Any]]:
    """Ülke liderleri + Türk Telekom (Türkiye) aynı eksende."""
    rows: List[Dict[str, Any]] = []
    for hit in europe_leader_rows(topic):
        rows.append(
            {
                "cc": hit["cc"],
                "name_tr": hit["name_tr"],
                "name_en": hit["name_en"],
                "firm": hit["lead_name"],
                "n": hit["lead_n"],
                "is_tt": bool(hit.get("is_tt")),
                "query": hit.get("query") or "",
            }
        )
    tt_n = tt_count(topic)
    if isinstance(tt_n, int):
        rows.append(
            {
                "cc": "TR",
                "name_tr": "Türkiye",
                "name_en": "Türkiye",
                "firm": "Türk Telekom",
                "n": tt_n,
                "is_tt": True,
                "query": _query(topic, str(TT_OPERATOR.get("search") or "Turk Telekom"), "Turkey"),
            }
        )
    rows.sort(key=lambda r: (-int(r["n"]), str(r.get("cc") or "")))
    return rows
