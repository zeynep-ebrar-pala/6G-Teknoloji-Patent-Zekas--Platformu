"""
WoS Starter API — yedi 6G konusu. Analyze Results HTML kazınmaz.
Sayı gelmezse None. Arka plan doldurur; sayfa kilitlemesin.
"""

from __future__ import annotations

import json
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

CACHE_PATH = Path(__file__).resolve().parents[1] / "data" / "cache" / "wos_live.json"
STATUS_PATH = Path(__file__).resolve().parents[1] / "data" / "cache" / "wos_prefetch_status.json"
YEARS = tuple(range(2020, 2027))
TOPIC_ORDER = (
    "ISAC",
    "RIS",
    "Cell-Free",
    "THz",
    "AI-RAN",
    "NTN",
    "Ambient IoT",
)

WOS_TOPIC_TS: Dict[str, str] = {
    "ISAC": '(ISAC OR "integrated sensing and communication" OR "joint communication and sensing")',
    "RIS": '(RIS OR "reconfigurable intelligent surface" OR "intelligent reflecting surface")',
    "Cell-Free": '("cell-free massive MIMO" OR "cell-free MIMO" OR "cell free massive MIMO")',
    "THz": '(THz OR terahertz OR "THz communication" OR "terahertz communication")',
    "AI-RAN": '("AI-RAN" OR "AI-native RAN" OR "AI native RAN" OR "O-RAN" OR "Open RAN" OR "RAN Intelligent Controller")',
    "NTN": '(NTN OR "non-terrestrial network" OR "non terrestrial network")',
    "Ambient IoT": '("ambient IoT" OR "ambient internet of things")',
}

# WoS Countries/Regions adları. CU Starter’da yoksa prefetch hata yazar; sayı uydurulmaz.
WOS_CU_ROSTER: Tuple[Tuple[str, str, str], ...] = (
    ("CN", "PEOPLES R CHINA", 'CU=("PEOPLES R CHINA")'),
    ("US", "USA", "CU=(USA)"),
    ("GB", "ENGLAND", "CU=(ENGLAND)"),
    ("DE", "GERMANY", "CU=(GERMANY)"),
    ("KR", "SOUTH KOREA", "CU=(SOUTH KOREA)"),
    ("JP", "JAPAN", "CU=(JAPAN)"),
    ("IN", "INDIA", "CU=(INDIA)"),
    ("IT", "ITALY", "CU=(ITALY)"),
    ("CA", "CANADA", "CU=(CANADA)"),
    ("AU", "AUSTRALIA", "CU=(AUSTRALIA)"),
    ("FR", "FRANCE", "CU=(FRANCE)"),
    ("ES", "SPAIN", "CU=(SPAIN)"),
    ("SG", "SINGAPORE", "CU=(SINGAPORE)"),
    ("SE", "SWEDEN", "CU=(SWEDEN)"),
    ("TW", "TAIWAN", "CU=(TAIWAN)"),
    ("NL", "NETHERLANDS", "CU=(NETHERLANDS)"),
    ("CH", "SWITZERLAND", "CU=(SWITZERLAND)"),
    ("SA", "SAUDI ARABIA", 'CU=("SAUDI ARABIA")'),
    ("FI", "FINLAND", "CU=(FINLAND)"),
    ("GR", "GREECE", "CU=(GREECE)"),
    ("EG", "EGYPT", "CU=(EGYPT)"),
    ("BR", "BRAZIL", "CU=(BRAZIL)"),
    ("PL", "POLAND", "CU=(POLAND)"),
    ("BE", "BELGIUM", "CU=(BELGIUM)"),
    ("AT", "AUSTRIA", "CU=(AUSTRIA)"),
    ("PT", "PORTUGAL", "CU=(PORTUGAL)"),
    ("TR", "TURKEY", "CU=(Turkey OR Turkiye OR Türkiye)"),
)

_lock = threading.Lock()
_work_lock = threading.Lock()
_thread: Optional[threading.Thread] = None


def topic_query(topic: str, *, year: Optional[int] = None, extra: str = "") -> str:
    ts = WOS_TOPIC_TS.get(topic) or f'("{topic}")'
    py = f"PY={int(year)}" if year else "PY=2020-2026"
    q = f"TS=(6G) AND TS={ts} AND {py}"
    if extra:
        q = f"{q} AND {extra}"
    return q


def _read(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def _write(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _status(**fields: Any) -> None:
    data = _read(STATUS_PATH)
    data.update(fields)
    data["at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    _write(STATUS_PATH, data)


def load_live() -> Dict[str, Any]:
    return _read(CACHE_PATH)


def _save_topic(name: str, patch: Dict[str, Any]) -> None:
    blob = load_live()
    topics = blob.get("topics") if isinstance(blob.get("topics"), dict) else {}
    row = topics.get(name) if isinstance(topics.get(name), dict) else {}
    row.update(patch)
    topics[name] = row
    blob["topics"] = topics
    blob["source"] = "Web of Science Starter API"
    blob["fetched_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    _write(CACHE_PATH, blob)


def _hits(data: Optional[Dict[str, Any]]) -> List[Dict[str, Any]]:
    if not data:
        return []
    rows = data.get("hits") or data.get("data") or []
    return [r for r in rows if isinstance(r, dict)]


def _cited_from_hits(hits: List[Dict[str, Any]], topic: str) -> List[Dict[str, Any]]:
    from backend.data_validator import load_validated_papers

    raw: List[Dict[str, Any]] = []
    for rec in hits:
        ident = rec.get("identifiers") if isinstance(rec.get("identifiers"), dict) else {}
        doi = str(ident.get("doi") or rec.get("doi") or "").strip().lower()
        doi = doi.removeprefix("https://doi.org/").removeprefix("http://doi.org/")
        title = str(rec.get("title") or "").strip()
        names = rec.get("names") if isinstance(rec.get("names"), dict) else {}
        authors = names.get("authors") if isinstance(names.get("authors"), list) else []
        author_txt = ", ".join(
            str(a.get("displayName") or a.get("display_name") or "").strip()
            for a in authors[:8]
            if isinstance(a, dict) and (a.get("displayName") or a.get("display_name"))
        )
        src = rec.get("source") if isinstance(rec.get("source"), dict) else {}
        journal = str(src.get("sourceTitle") or src.get("source_title") or rec.get("sourceTitle") or "").strip()
        year = src.get("publishYear") or src.get("publish_year") or rec.get("publishYear")
        try:
            year_i = int(year) if year is not None else None
        except (TypeError, ValueError):
            year_i = None
        cites = rec.get("citations")
        n_cite: Optional[int] = None
        if isinstance(cites, list) and cites:
            item = cites[0] if isinstance(cites[0], dict) else {}
            try:
                n_cite = int(item.get("count") or item.get("value") or 0)
            except (TypeError, ValueError):
                n_cite = None
        elif isinstance(cites, dict):
            try:
                n_cite = int(cites.get("count") or 0)
            except (TypeError, ValueError):
                n_cite = None
        uid = str(rec.get("uid") or ident.get("uid") or "").strip()
        if not doi.startswith("10.") and not title:
            continue
        url = f"https://doi.org/{doi}" if doi.startswith("10.") else ""
        raw.append(
            {
                "title": title,
                "authors": author_txt,
                "journal": journal,
                "year": year_i,
                "doi": doi if doi.startswith("10.") else "",
                "citations": n_cite,
                "source": "Web of Science Core Collection",
                "source_url": url,
                "url": url,
                "topic": topic,
                "wos_ut": uid,
            }
        )
    if any(p.get("doi") for p in raw):
        validated = load_validated_papers([p for p in raw if p.get("doi")])
        by_doi = {str(p.get("doi")).lower(): p for p in raw}
        for item in validated:
            extra = by_doi.get(str(item.get("doi") or "").lower()) or {}
            item["wos_ut"] = extra.get("wos_ut") or ""
            item["citations"] = extra.get("citations")
        rest = [p for p in raw if not p.get("doi")]
        return validated + rest
    return raw


def _inst_from_hits(hits: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    counts: Dict[str, int] = {}
    for rec in hits:
        names = rec.get("names") if isinstance(rec.get("names"), dict) else {}
        for key in ("issuingOrganizations", "issuing_organizations", "corp"):
            rows = names.get(key) or []
            if not isinstance(rows, list):
                continue
            for item in rows:
                if not isinstance(item, dict):
                    continue
                name = str(item.get("displayName") or item.get("display_name") or "").strip()
                if name:
                    counts[name] = counts.get(name, 0) + 1
    out = [{"name": k, "count": v} for k, v in counts.items()]
    out.sort(key=lambda r: (-int(r["count"]), str(r["name"])))
    return out[:10]


def _work() -> None:
    from backend.config import reload_env
    from backend.publisher_apis import wos_documents, wos_last_error, wos_total

    with _work_lock:
        reload_env()
        jobs = 0
        for name in TOPIC_ORDER:
            jobs += 1 + len(YEARS) + 1 + len(WOS_CU_ROSTER)
        done = 0
        _status(running=True, done=0, total=jobs, error="")
        try:
            for name in TOPIC_ORDER:
                q = topic_query(name)
                total = wos_total(q)
                done += 1
                _status(running=True, done=done, total=jobs)
                years: Dict[str, Optional[int]] = {}
                for year in YEARS:
                    years[str(year)] = wos_total(topic_query(name, year=year))
                    done += 1
                    _status(running=True, done=done, total=jobs)
                    time.sleep(0.08)
                cited_data = wos_documents(q, limit=10, page=1, sort="TC+D")
                done += 1
                _status(running=True, done=done, total=jobs)
                cited = _cited_from_hits(_hits(cited_data), name)
                inst = _inst_from_hits(_hits(cited_data))
                countries: List[Dict[str, Any]] = []
                turkey_n: Optional[int] = None
                for cc, label, extra in WOS_CU_ROSTER:
                    n = wos_total(topic_query(name, extra=extra))
                    done += 1
                    _status(running=True, done=done, total=jobs)
                    time.sleep(0.08)
                    if not isinstance(n, int):
                        continue
                    countries.append({"cc": cc, "name": label, "count": n})
                    if cc == "TR":
                        turkey_n = n
                countries.sort(key=lambda r: (-int(r["count"]), str(r.get("cc") or "")))
                turkey_rank = None
                if isinstance(turkey_n, int):
                    for i, row in enumerate(countries, 1):
                        if row.get("cc") == "TR":
                            turkey_rank = i
                            break
                _save_topic(
                    name,
                    {
                        "total": total,
                        "query": q,
                        "years": {k: v for k, v in years.items() if isinstance(v, int)},
                        "cited": cited,
                        "institutions": inst,
                        "countries": countries,
                        "turkey_count": turkey_n,
                        "turkey_rank": turkey_rank,
                        "roster": len(WOS_CU_ROSTER),
                    },
                )
            err = wos_last_error()
            _status(running=False, done=jobs, total=jobs, error=err)
        except Exception as exc:
            _status(running=False, done=done, total=jobs, error=str(exc)[:240])


def ensure_prefetch() -> None:
    from backend.config import get_wos_api_key

    if not get_wos_api_key():
        return
    global _thread
    with _lock:
        if _thread is not None and _thread.is_alive():
            return
        live = load_live()
        topics = live.get("topics") if isinstance(live.get("topics"), dict) else {}
        if all(isinstance((topics.get(n) or {}).get("total"), int) for n in TOPIC_ORDER):
            return
        _thread = threading.Thread(target=_work, daemon=True, name="wos-live")
        _thread.start()


def prefetch_status() -> Dict[str, Any]:
    st = _read(STATUS_PATH)
    return {
        "running": bool(st.get("running")),
        "done": int(st.get("done") or 0),
        "total": int(st.get("total") or 0),
        "error": str(st.get("error") or ""),
    }


def live_topic_row(topic: str) -> Dict[str, Any]:
    blob = load_live()
    topics = blob.get("topics") if isinstance(blob.get("topics"), dict) else {}
    row = topics.get(topic) if isinstance(topics.get(topic), dict) else {}
    return row if isinstance(row, dict) else {}
