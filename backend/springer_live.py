"""
Springer Nature Meta API — yedi 6G konusu.
Yıl ve ülke: facet. Kurum / atıf: çekilen kayıtlardan (facet yok).
Sayı gelmezse None; uydurulmaz.
"""

from __future__ import annotations

import json
import threading
import time
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from backend.config import get_springer_api_key, reload_env
from backend.publisher_apis import TOPIC_TOKEN, UA, YEARS, _cache_get, _cache_put, _json, _q6g, _springer_count

CACHE_PATH = Path(__file__).resolve().parents[1] / "data" / "cache" / "springer_live.json"
STATUS_PATH = Path(__file__).resolve().parents[1] / "data" / "cache" / "springer_prefetch_status.json"

TOPIC_ORDER = (
    "ISAC",
    "RIS",
    "Cell-Free",
    "THz",
    "AI-RAN",
    "NTN",
    "Ambient IoT",
)
TREND_YEARS = list(range(2020, 2027))

COUNTRY_CC = {
    "CHINA": "CN",
    "INDIA": "IN",
    "MALAYSIA": "MY",
    "JORDAN": "JO",
    "UNITED KINGDOM": "GB",
    "UNITED STATES": "US",
    "GERMANY": "DE",
    "SAUDI ARABIA": "SA",
    "CANADA": "CA",
    "UNITED ARAB EMIRATES": "AE",
    "ITALY": "IT",
    "FRANCE": "FR",
    "FINLAND": "FI",
    "AUSTRALIA": "AU",
    "GREECE": "GR",
    "SINGAPORE": "SG",
    "SOUTH KOREA": "KR",
    "EGYPT": "EG",
    "PAKISTAN": "PK",
    "IRAQ": "IQ",
    "JAPAN": "JP",
    "SPAIN": "ES",
    "SWEDEN": "SE",
    "NETHERLANDS": "NL",
    "SWITZERLAND": "CH",
    "BRAZIL": "BR",
    "TURKEY": "TR",
    "TURKIYE": "TR",
    "TÜRKIYE": "TR",
}

_lock = threading.Lock()
_work_lock = threading.Lock()
_thread: Optional[threading.Thread] = None


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


def _query(topic: str, extra: str = "") -> str:
    q = _q6g(topic)
    y0, y1 = YEARS
    out = f"{q} onlinedatefrom:{y0}-01-01 onlinedateto:{y1}-12-31"
    if extra:
        out = f"{out} {extra}"
    return out


def _meta(query: str, *, page: int = 1, start: int = 1, facet: bool = False) -> Optional[Dict[str, Any]]:
    key = get_springer_api_key()
    if not key:
        return None
    params = {"q": query, "api_key": key, "p": str(page), "s": str(start)}
    if facet:
        params["facet"] = "true"
    url = "https://api.springernature.com/meta/v2/json?" + urllib.parse.urlencode(params)
    return _json(url, timeout=28)


def _total_of(data: Optional[Dict[str, Any]]) -> Optional[int]:
    if not data:
        return None
    result = data.get("result") or []
    raw = result[0].get("total") if isinstance(result, list) and result else data.get("total")
    try:
        return int(str(raw).replace(",", ""))
    except (TypeError, ValueError):
        return None


def _facets(data: Optional[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    out: Dict[str, List[Dict[str, Any]]] = {}
    if not data:
        return out
    for block in data.get("facets") or []:
        if not isinstance(block, dict):
            continue
        name = str(block.get("name") or "").strip()
        rows: List[Dict[str, Any]] = []
        for item in block.get("values") or []:
            if not isinstance(item, dict):
                continue
            label = str(item.get("value") or "").strip()
            try:
                n = int(str(item.get("count")).replace(",", ""))
            except (TypeError, ValueError):
                continue
            if label:
                rows.append({"name": label, "count": n})
        if name:
            out[name] = rows
    return out


def _year_map(rows: List[Dict[str, Any]]) -> Dict[str, int]:
    out = {str(y): 0 for y in TREND_YEARS}
    for row in rows:
        key = str(row.get("name") or "")
        if key in out:
            out[key] = int(row["count"])
    return out


def _countries(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for row in rows:
        name = str(row.get("name") or "").strip()
        cc = COUNTRY_CC.get(name.upper()) or ""
        out.append({"cc": cc, "name": name, "count": int(row["count"])})
    out.sort(key=lambda r: (-int(r["count"]), str(r.get("cc") or r["name"])))
    return out


def _year_of(rec: Dict[str, Any]) -> Optional[int]:
    for key in ("onlineDate", "publicationDate"):
        raw = str(rec.get(key) or "")[:4]
        try:
            y = int(raw)
        except ValueError:
            continue
        if 1990 <= y <= 2035:
            return y
    return None


def _records(data: Optional[Dict[str, Any]], topic: str) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for rec in (data or {}).get("records") or []:
        if not isinstance(rec, dict):
            continue
        doi = str(rec.get("doi") or "").strip()
        doi = doi.removeprefix("https://doi.org/").removeprefix("http://doi.org/")
        title = str(rec.get("title") or "").strip()
        creators = rec.get("creators") if isinstance(rec.get("creators"), list) else []
        authors = ", ".join(
            str(c.get("creator") or "").strip() for c in creators[:8] if isinstance(c, dict) and c.get("creator")
        )
        journal = str(rec.get("publicationName") or "").strip()
        year = _year_of(rec)
        url = f"https://doi.org/{doi}" if doi.startswith("10.") else ""
        out.append(
            {
                "title": title,
                "authors": authors,
                "journal": journal,
                "year": year,
                "doi": doi if doi.startswith("10.") else "",
                "citations": None,
                "source": "Springer",
                "source_url": url,
                "url": url,
                "topic": topic,
            }
        )
    return [p for p in out if p.get("title")]


def _crossref_work(doi: str) -> Dict[str, Any]:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    data = _json(url, timeout=12)
    cites: Optional[int] = None
    names: List[str] = []
    if not data:
        return {"cites": None, "aff": []}
    msg = data.get("message") if isinstance(data.get("message"), dict) else {}
    try:
        cites = int(msg.get("is-referenced-by-count"))
        _cache_put(f"cr:{doi}", cites)
    except (TypeError, ValueError):
        cites = None
    for author in msg.get("author") or []:
        if not isinstance(author, dict):
            continue
        for aff in author.get("affiliation") or []:
            if isinstance(aff, dict):
                label = str(aff.get("name") or "").strip()
            else:
                label = str(aff or "").strip()
            if label:
                names.append(label)
    return {"cites": cites, "aff": names}


def _save_topic(name: str, patch: Dict[str, Any]) -> None:
    blob = load_live()
    topics = blob.get("topics") if isinstance(blob.get("topics"), dict) else {}
    row = topics.get(name) if isinstance(topics.get(name), dict) else {}
    row.update(patch)
    topics[name] = row
    blob["topics"] = topics
    blob["source"] = "Springer Nature Meta API"
    blob["fetched_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    _write(CACHE_PATH, blob)


def _work() -> None:
    with _work_lock:
        reload_env()
        total_jobs = len(TOPIC_ORDER) * 3
        done = 0
        _status(running=True, done=0, total=total_jobs, error="")
        try:
            for name in TOPIC_ORDER:
                q = _query(name)
                data = _meta(q, page=1, start=1, facet=True)
                facets = _facets(data)
                total = _total_of(data)
                years = _year_map(facets.get("year") or [])
                countries = _countries(facets.get("country") or [])
                turkey_n = _springer_count(_q6g(name), "Turkey", YEARS)
                turkey_rank = None
                if isinstance(turkey_n, int):
                    merged = list(countries)
                    if not any(r.get("cc") == "TR" for r in merged):
                        merged.append({"cc": "TR", "name": "Turkey", "count": turkey_n})
                        merged.sort(key=lambda r: (-int(r["count"]), str(r.get("cc") or r["name"])))
                    for i, row in enumerate(merged, 1):
                        if row.get("cc") == "TR":
                            turkey_rank = i
                            break
                    countries = merged
                _save_topic(
                    name,
                    {
                        "total": total,
                        "query": q,
                        "years": years,
                        "countries": countries,
                        "turkey_count": turkey_n,
                        "turkey_rank": turkey_rank,
                    },
                )
                done += 1
                _status(running=True, done=done, total=total_jobs)
                rec_data = _meta(q, page=20, start=1, facet=False)
                papers = _records(rec_data, name)
                done += 1
                _status(running=True, done=done, total=total_jobs)
                inst_counts: Dict[str, int] = {}
                for paper in papers:
                    doi = str(paper.get("doi") or "")
                    if not doi:
                        continue
                    work = _crossref_work(doi)
                    if isinstance(work.get("cites"), int):
                        paper["citations"] = work["cites"]
                    for aff in work.get("aff") or []:
                        short = aff.split(",")[0].strip()
                        if len(short) < 4:
                            continue
                        inst_counts[short] = inst_counts.get(short, 0) + 1
                    time.sleep(0.05)
                papers.sort(key=lambda p: (-int(p.get("citations") or 0), str(p.get("title") or "")))
                inst = [{"name": k, "count": v} for k, v in inst_counts.items()]
                inst.sort(key=lambda r: (-int(r["count"]), str(r["name"])))
                _save_topic(
                    name,
                    {
                        "total": total,
                        "query": q,
                        "years": years,
                        "countries": countries,
                        "institutions": inst[:10],
                        "cited": papers[:10],
                        "turkey_count": turkey_n,
                        "turkey_rank": turkey_rank,
                    },
                )
                done += 1
                _status(running=True, done=done, total=total_jobs)
            _status(running=False, done=total_jobs, total=total_jobs, error="")
        except Exception as exc:
            _status(running=False, done=done, total=total_jobs, error=str(exc)[:240])


def ensure_prefetch() -> None:
    if not get_springer_api_key():
        return
    global _thread
    with _lock:
        if _thread is not None and _thread.is_alive():
            return
        live = load_live()
        topics = live.get("topics") if isinstance(live.get("topics"), dict) else {}
        if all(isinstance((topics.get(n) or {}).get("total"), int) for n in TOPIC_ORDER):
            if all((topics.get(n) or {}).get("cited") for n in TOPIC_ORDER):
                return
        _thread = threading.Thread(target=_work, daemon=True, name="springer-live")
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


def springer_overlay(topic: Optional[str] = None) -> Optional[Dict[str, Any]]:
    blob = load_live()
    topics = blob.get("topics") if isinstance(blob.get("topics"), dict) else {}
    if not topics:
        return None

    totals: Dict[str, int] = {}
    series: Dict[str, Dict[str, int]] = {}
    by_inst: Dict[str, List[Dict[str, Any]]] = {}
    by_cc: Dict[str, List[Dict[str, Any]]] = {}
    turkey: Dict[str, Dict[str, Any]] = {}
    cited_all: List[Dict[str, Any]] = []
    for name in TOPIC_ORDER:
        row = topics.get(name)
        if not isinstance(row, dict):
            continue
        if isinstance(row.get("total"), int):
            totals[name] = int(row["total"])
        years = row.get("years") if isinstance(row.get("years"), dict) else {}
        series[name] = {str(y): int(years.get(str(y), 0) or 0) for y in TREND_YEARS}
        inst = row.get("institutions") if isinstance(row.get("institutions"), list) else []
        cc = row.get("countries") if isinstance(row.get("countries"), list) else []
        if inst:
            by_inst[name] = [x for x in inst if isinstance(x, dict)]
        if cc:
            by_cc[name] = [x for x in cc if isinstance(x, dict)]
        turkey[name] = {
            "count": row.get("turkey_count") if isinstance(row.get("turkey_count"), int) else None,
            "rank": row.get("turkey_rank") if isinstance(row.get("turkey_rank"), int) else None,
        }
        for paper in row.get("cited") or []:
            if isinstance(paper, dict):
                cited_all.append(paper)
    if not totals:
        return None
    cited_all.sort(key=lambda p: (-int(p.get("citations") or 0), str(p.get("title") or "")))
    fetched = str(blob.get("fetched_at") or "")
    meta = {
        "chart_source": "springer",
        "fetched_at": fetched,
        "turkey_by_topic": turkey,
    }
    tpc = (topic or "").strip() or None
    if tpc:
        row = topics.get(tpc) if isinstance(topics.get(tpc), dict) else {}
        return {
            **meta,
            "total": int(row["total"]) if isinstance(row.get("total"), int) else None,
            "query": str(row.get("query") or ""),
            "topics": {tpc: totals[tpc]} if tpc in totals else {},
            "year_counts": series.get(tpc) or {},
            "year_series": {tpc: series[tpc]} if tpc in series else {},
            "institutions": by_inst.get(tpc) or [],
            "countries": by_cc.get(tpc) or [],
            "institutions_by_topic": {tpc: by_inst[tpc]} if tpc in by_inst else {},
            "countries_by_topic": {tpc: by_cc[tpc]} if tpc in by_cc else {},
            "cited": list(row.get("cited") or [])[:10],
            "turkey": turkey.get(tpc) or {},
        }
    return {
        **meta,
        "total": None,
        "query": "",
        "topics": totals,
        "year_counts": {},
        "year_series": series,
        "institutions": [],
        "countries": [],
        "institutions_by_topic": by_inst,
        "countries_by_topic": by_cc,
        "cited": cited_all[:10],
        "turkey": {},
    }
