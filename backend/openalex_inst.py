"""
Dünya kurum sıralaması — OpenAlex group_by institutions.
Yedi 6G konusu, başlık+özet «6G {token}», 2020–içinde bulunulan yıl.
Springer kurum facet’i yoktur; sayı OpenAlex bağlılığındandır. Konular toplanmaz.
"""

from __future__ import annotations

import threading
import time
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from backend.publisher_apis import TOPIC_TOKEN, UA, _json
from backend.springer_live import TOPIC_ORDER
from backend.years import end_year, read_json, should_refresh, write_json, year_window

CACHE_PATH = Path(__file__).resolve().parents[1] / "data" / "cache" / "openalex_inst.json"
STATUS_PATH = Path(__file__).resolve().parents[1] / "data" / "cache" / "openalex_inst_status.json"
MAIL = "zeynep.ebrar.pala@example.com"
SKIP_NAMES = frozenset({"unknown", "unaffiliated", "n/a", "na", "none", "null"})

_lock = threading.Lock()
_work_lock = threading.Lock()
_thread: Optional[threading.Thread] = None


def _query(topic: str) -> str:
    token = TOPIC_TOKEN.get(topic) or topic
    return f"6G {token}".strip()


def load_live() -> Dict[str, Any]:
    return read_json(CACHE_PATH)


def prefetch_status() -> Dict[str, Any]:
    st = read_json(STATUS_PATH)
    return {
        "running": bool(st.get("running")),
        "done": int(st.get("done") or 0),
        "total": int(st.get("total") or 0),
        "error": str(st.get("error") or ""),
    }


def _status(**fields: Any) -> None:
    data = read_json(STATUS_PATH)
    data.update(fields)
    data["at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    write_json(STATUS_PATH, data)


def _fetch_topic(topic: str) -> Dict[str, Any]:
    y0, y1 = year_window()
    q = _query(topic)
    filt = (
        f"title_and_abstract.search:{q},"
        f"from_publication_date:{y0}-01-01,to_publication_date:{y1}-12-31"
    )
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(
        {
            "filter": filt,
            "group_by": "authorships.institutions.id",
            "per_page": "10",
            "mailto": MAIL,
        }
    )
    data = _json(url, headers={"User-Agent": UA}, timeout=40)
    rows: List[Dict[str, Any]] = []
    total = None
    if not data:
        return {"query": q, "total": None, "institutions": []}
    meta = data.get("meta") if isinstance(data.get("meta"), dict) else {}
    try:
        total = int(meta.get("count"))
    except (TypeError, ValueError):
        total = None
    for item in data.get("group_by") or []:
        if not isinstance(item, dict):
            continue
        name = str(item.get("key_display_name") or "").strip()
        if not name or name.casefold() in SKIP_NAMES:
            continue
        try:
            n = int(item.get("count"))
        except (TypeError, ValueError):
            continue
        if n <= 0:
            continue
        rows.append({"name": name, "count": n, "id": str(item.get("key") or "")})
        if len(rows) >= 10:
            break
    return {"query": q, "total": total, "institutions": rows}


def _cache_complete(blob: Dict[str, Any]) -> bool:
    topics = blob.get("topics") if isinstance(blob.get("topics"), dict) else {}
    if not all(name in topics for name in TOPIC_ORDER):
        return False
    return all(isinstance((topics.get(n) or {}).get("institutions"), list) for n in TOPIC_ORDER)


def _work() -> None:
    with _work_lock:
        _status(running=True, done=0, total=len(TOPIC_ORDER), error="")
        blob = load_live()
        topics = blob.get("topics") if isinstance(blob.get("topics"), dict) else {}
        done = 0
        try:
            for name in TOPIC_ORDER:
                row = _fetch_topic(name)
                if row.get("institutions") or isinstance(row.get("total"), int):
                    topics[name] = row
                done += 1
                _status(running=True, done=done, total=len(TOPIC_ORDER))
                time.sleep(0.2)
            blob["topics"] = topics
            blob["source"] = "OpenAlex"
            blob["fetched_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
            blob["year_end"] = end_year()
            write_json(CACHE_PATH, blob)
            _status(running=False, done=len(TOPIC_ORDER), total=len(TOPIC_ORDER), error="")
        except Exception as exc:
            _status(running=False, done=done, total=len(TOPIC_ORDER), error=str(exc)[:240])


def ensure_prefetch(*, force: bool = False) -> None:
    global _thread
    with _lock:
        alive = _thread is not None and _thread.is_alive()
        if alive:
            return
        live = load_live()
        st = read_json(STATUS_PATH)
        if not should_refresh(
            complete=_cache_complete(live),
            fetched_at=str(live.get("fetched_at") or ""),
            year_end=live.get("year_end") if isinstance(live.get("year_end"), int) else None,
            force=force,
            running=bool(st.get("running")),
        ):
            return
        _status(running=True, done=0, total=len(TOPIC_ORDER), error="")
        _thread = threading.Thread(target=_work, daemon=True, name="openalex-inst")
        _thread.start()


def inst_payload(topic: Optional[str] = None) -> Dict[str, Any]:
    blob = load_live()
    topics = blob.get("topics") if isinstance(blob.get("topics"), dict) else {}
    by_inst: Dict[str, List[Dict[str, Any]]] = {}
    for name in TOPIC_ORDER:
        row = topics.get(name) if isinstance(topics.get(name), dict) else {}
        inst = [x for x in (row.get("institutions") or []) if isinstance(x, dict)]
        if inst:
            by_inst[name] = inst
    tpc = (topic or "").strip() or None
    if tpc:
        return {
            "institutions": by_inst.get(tpc) or [],
            "institutions_by_topic": {tpc: by_inst[tpc]} if tpc in by_inst else {},
            "fetched_at": str(blob.get("fetched_at") or ""),
        }
    return {
        "institutions": [],
        "institutions_by_topic": by_inst,
        "fetched_at": str(blob.get("fetched_at") or ""),
    }
