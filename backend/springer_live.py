"""
Springer Nature Meta API — yedi 6G konusu.
Yıl ve ülke: facet. Atıf: çekilen DOI + Crossref.
Sayı gelmezse None; uydurulmaz.
"""

from __future__ import annotations

import threading
import time
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from backend.config import get_springer_api_key, reload_env
from backend.paper_geo import EU_AFFIL, EU_CCS, affiliation_ccs
from backend.years import should_refresh
from backend.publisher_apis import _cache_put, _json, _q6g, _springer_count
from backend.topic_filter import filter_cited
from backend.years import end_year, read_json, trend_years, write_json, year_window

CACHE_PATH = Path(__file__).resolve().parents[1] / "data" / "cache" / "springer_live.json"
STATUS_PATH = Path(__file__).resolve().parents[1] / "data" / "cache" / "springer_prefetch_status.json"
AFF_CACHE_PATH = Path(__file__).resolve().parents[1] / "data" / "cache" / "crossref_aff.json"

TOPIC_ORDER = (
    "ISAC",
    "RIS",
    "Cell-Free",
    "THz",
    "AI-RAN",
    "NTN",
    "Ambient IoT",
)


def __getattr__(name: str):
    if name == "TREND_YEARS":
        return trend_years()
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


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
    "BELGIUM": "BE",
    "LUXEMBOURG": "LU",
    "POLAND": "PL",
    "VIETNAM": "VN",
    "TURKEY": "TR",
    "TURKIYE": "TR",
    "TÜRKIYE": "TR",
}

_lock = threading.Lock()
_work_lock = threading.Lock()
_thread: Optional[threading.Thread] = None


def _read(path: Path) -> Dict[str, Any]:
    return read_json(path)


def _write(path: Path, payload: Dict[str, Any]) -> None:
    write_json(path, payload)


def _status(**fields: Any) -> None:
    data = _read(STATUS_PATH)
    data.update(fields)
    data["at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    _write(STATUS_PATH, data)


def load_live() -> Dict[str, Any]:
    return _read(CACHE_PATH)


def _query(topic: str, extra: str = "") -> str:
    q = _q6g(topic)
    y0, y1 = year_window()
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
    out = {str(y): 0 for y in trend_years()}
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


def _affiliations_of(rec: Dict[str, Any]) -> List[str]:
    names: List[str] = []
    raw = rec.get("affiliations") or rec.get("affiliation") or []
    if isinstance(raw, str) and raw.strip():
        names.append(raw.strip())
    elif isinstance(raw, list):
        for item in raw:
            if isinstance(item, dict):
                label = str(item.get("name") or item.get("value") or "").strip()
            else:
                label = str(item or "").strip()
            if label:
                names.append(label)
    for creator in rec.get("creators") or []:
        if not isinstance(creator, dict):
            continue
        aff = creator.get("affiliation") or creator.get("affiliations") or []
        if isinstance(aff, str) and aff.strip():
            names.append(aff.strip())
        elif isinstance(aff, list):
            for item in aff:
                if isinstance(item, dict):
                    label = str(item.get("name") or "").strip()
                else:
                    label = str(item or "").strip()
                if label:
                    names.append(label)
    seen = set()
    out: List[str] = []
    for name in names:
        key = name.casefold()
        if key in seen:
            continue
        seen.add(key)
        out.append(name)
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
        date = str(rec.get("onlineDate") or rec.get("publicationDate") or "")[:10]
        url = f"https://doi.org/{doi}" if doi.startswith("10.") else ""
        abstract = str(rec.get("abstract") or rec.get("teaser") or "").strip()
        if len(abstract) > 1200:
            abstract = abstract[:1200]
        affiliations = _affiliations_of(rec)
        out.append(
            {
                "title": title,
                "authors": authors,
                "journal": journal,
                "year": year,
                "date": date,
                "doi": doi if doi.startswith("10.") else "",
                "citations": None,
                "abstract": abstract,
                "affiliations": affiliations,
                "ccs": affiliation_ccs(affiliations),
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


def crossref_citation_count(doi: str) -> Optional[int]:
    """Crossref is-referenced-by-count — çekilen DOI için atıf."""
    token = (doi or "").strip().removeprefix("https://doi.org/").removeprefix("http://doi.org/")
    if not token:
        return None
    cites = _crossref_work(token).get("cites")
    return int(cites) if isinstance(cites, int) else None


def _save_topic(name: str, patch: Dict[str, Any]) -> None:
    blob = load_live()
    topics = blob.get("topics") if isinstance(blob.get("topics"), dict) else {}
    row = topics.get(name) if isinstance(topics.get(name), dict) else {}
    row.update(patch)
    topics[name] = row
    blob["topics"] = topics
    blob["source"] = "Springer Nature Meta API"
    blob["fetched_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    blob["year_end"] = end_year()
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
                prev = live_topic_row(name)
                data = _meta(q, page=1, start=1, facet=True)
                if not data:
                    done += 3
                    _status(running=True, done=min(done, total_jobs), total=total_jobs)
                    continue
                facets = _facets(data)
                total = _total_of(data)
                if total is None and isinstance(prev.get("total"), int):
                    total = int(prev["total"])
                years = _year_map(facets.get("year") or [])
                if not any(years.values()) and isinstance(prev.get("years"), dict):
                    years = {str(y): int((prev["years"].get(str(y), 0) or 0)) for y in trend_years()}
                countries = _countries(facets.get("country") or [])
                turkey_n = _springer_count(_q6g(name), "Turkey", year_window(), force=True)
                if turkey_n is None and isinstance(prev.get("turkey_count"), int):
                    turkey_n = int(prev["turkey_count"])
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
                elif isinstance(prev.get("turkey_rank"), int):
                    turkey_rank = int(prev["turkey_rank"])
                _save_topic(
                    name,
                    {
                        "total": total,
                        "query": q,
                        "years": years,
                        "countries": countries or prev.get("countries") or [],
                        "turkey_count": turkey_n,
                        "turkey_rank": turkey_rank,
                    },
                )
                done += 1
                _status(running=True, done=done, total=total_jobs)
                rec_data = _meta(q, page=50, start=1, facet=False)
                papers = filter_cited(_records(rec_data, name), name, limit=50) if rec_data else []
                done += 1
                _status(running=True, done=done, total=total_jobs)
                if not papers:
                    papers = [p for p in (prev.get("cited") or []) if isinstance(p, dict)]
                    inst = []
                    _save_topic(
                        name,
                        {
                            "total": total,
                            "query": q,
                            "years": years,
                            "countries": countries or prev.get("countries") or [],
                            "institutions": inst[:10],
                            "cited": papers[:50],
                            "turkey_count": turkey_n,
                            "turkey_rank": turkey_rank,
                        },
                    )
                    done += 1
                    _status(running=True, done=done, total=total_jobs)
                    continue
                for paper in papers:
                    doi = str(paper.get("doi") or "")
                    if doi:
                        work = _crossref_work(doi)
                        if isinstance(work.get("cites"), int):
                            paper["citations"] = work["cites"]
                        aff = list(paper.get("affiliations") or [])
                        for name in work.get("aff") or []:
                            if name and name not in aff:
                                aff.append(name)
                        if aff:
                            paper["affiliations"] = aff
                            paper["ccs"] = affiliation_ccs(aff)
                        time.sleep(0.05)
                papers.sort(key=lambda p: (-int(p.get("citations") or 0), str(p.get("title") or "")))
                inst: List[Dict[str, Any]] = []
                _save_topic(
                    name,
                    {
                        "total": total,
                        "query": q,
                        "years": years,
                        "countries": countries,
                        "institutions": inst[:10],
                        "cited": papers[:50],
                        "turkey_count": turkey_n,
                        "turkey_rank": turkey_rank,
                    },
                )
                done += 1
                _status(running=True, done=done, total=total_jobs)
            _status(running=False, done=total_jobs, total=total_jobs, error="")
        except Exception as exc:
            _status(running=False, done=done, total=total_jobs, error=str(exc)[:240])


def _cache_complete(live: Dict[str, Any]) -> bool:
    topics = live.get("topics") if isinstance(live.get("topics"), dict) else {}
    if not all(isinstance((topics.get(n) or {}).get("total"), int) for n in TOPIC_ORDER):
        return False
    return all((topics.get(n) or {}).get("cited") for n in TOPIC_ORDER)


def ensure_prefetch(*, force: bool = False) -> None:
    if not get_springer_api_key():
        return
    global _thread
    with _lock:
        alive = _thread is not None and _thread.is_alive()
        if alive:
            return
        live = load_live()
        complete = _cache_complete(live)
        year_end = live.get("year_end")
        try:
            stored_end = int(year_end) if year_end is not None else None
        except (TypeError, ValueError):
            stored_end = None
        if not should_refresh(
            complete=complete,
            fetched_at=str(live.get("fetched_at") or ""),
            year_end=stored_end,
            force=force,
            running=False,
        ):
            return
        _status(running=True, done=0, total=len(TOPIC_ORDER) * 3, error="")
        _thread = threading.Thread(target=_work, daemon=True, name="springer-live")
        _thread.start()


def prefetch_status() -> Dict[str, Any]:
    st = _read(STATUS_PATH)
    alive = _thread is not None and _thread.is_alive()
    return {
        "running": alive,
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
        series[name] = {str(y): int(years.get(str(y), 0) or 0) for y in trend_years()}
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
    tpc = (topic or "").strip() or None
    cited_all = filter_cited(cited_all, tpc, limit=10)
    fetched = str(blob.get("fetched_at") or "")
    meta = {
        "chart_source": "springer",
        "fetched_at": fetched,
        "turkey_by_topic": turkey,
    }
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
            "cited": filter_cited(row.get("cited") or [], tpc, limit=10),
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


def _paper_affiliations(paper: Dict[str, Any]) -> List[str]:
    stored = paper.get("affiliations") if isinstance(paper.get("affiliations"), list) else []
    names = [str(x).strip() for x in stored if str(x).strip()]
    if names:
        return names
    doi = str(paper.get("doi") or "").strip()
    if not doi:
        return []
    blob = _read(AFF_CACHE_PATH)
    hit = blob.get(doi)
    if isinstance(hit, list):
        return [str(x).strip() for x in hit if str(x).strip()]
    aff = [str(x).strip() for x in (_crossref_work(doi).get("aff") or []) if str(x).strip()]
    blob[doi] = aff
    if aff:
        _write(AFF_CACHE_PATH, blob)
    return aff


def _europe_cited_for_topic(topic: str, *, max_cc: int = 5) -> List[Dict[str, Any]]:
    """Springer metin «ülke adı»: bağlılık alanı bu planda yok, ülke uydurulmaz."""
    from backend.topic_filter import filter_cited

    row = live_topic_row(topic)
    cached = row.get("europe_cited")
    if isinstance(cached, list) and cached:
        return [dict(p) for p in cached if isinstance(p, dict)]
    if not get_springer_api_key():
        return []
    from backend.paper_geo import EU_AFFIL, EU_CCS

    eu_rows = [
        c
        for c in (row.get("countries") or [])
        if isinstance(c, dict) and str(c.get("cc") or "") in EU_CCS
    ]
    if not eu_rows:
        eu_rows = [{"cc": cc} for cc in ("GB", "DE", "IT", "FR", "ES")]
    pool: List[Dict[str, Any]] = []
    seen = set()
    for item in eu_rows[:max_cc]:
        cc = str(item.get("cc") or "")
        name_en = EU_AFFIL.get(cc) or ""
        if not name_en:
            continue
        data = _meta(_query(topic, extra=name_en), page=12, start=1, facet=False)
        for paper in _records(data, topic):
            doi = str(paper.get("doi") or "").strip().lower()
            key = doi or str(paper.get("title") or "").casefold()
            if not key or key in seen:
                continue
            seen.add(key)
            paper["ccs"] = [cc]
            paper["affiliations"] = [name_en]
            pool.append(paper)
        time.sleep(0.05)
    papers = filter_cited(pool, topic, limit=40)
    for paper in papers:
        doi = str(paper.get("doi") or "")
        if not doi:
            continue
        work = _crossref_work(doi)
        if isinstance(work.get("cites"), int):
            paper["citations"] = work["cites"]
        time.sleep(0.03)
    papers.sort(
        key=lambda p: (
            -int(p.get("citations") or 0),
            -int(p.get("year") or 0),
            str(p.get("title") or ""),
        )
    )
    out = papers[:30]
    if out:
        _save_topic(topic, {"europe_cited": out})
    return [dict(p) for p in out]


_eu_year_cooldown_until = 0.0


def _europe_or_clause(topic: str, *, max_cc: int = 8) -> str:
    """Facet’teki Avrupa ülkelerinin İngilizce adı; tek OR, 4 ayrı istek değil."""
    row = live_topic_row(topic)
    eu_rows = [
        c
        for c in (row.get("countries") or [])
        if isinstance(c, dict) and str(c.get("cc") or "") in EU_CCS
    ]
    ccs = [str(c.get("cc") or "") for c in eu_rows[:max_cc]]
    if not ccs:
        ccs = ["GB", "DE", "IT", "FR", "ES", "NL", "SE", "FI"]
    parts: List[str] = []
    for cc in ccs:
        name_en = EU_AFFIL.get(cc) or ""
        if not name_en:
            continue
        parts.append(f'"{name_en}"' if " " in name_en else name_en)
    return "(" + " OR ".join(parts) + ")" if parts else "Germany"


def _europe_year_map(topic: str, *, max_cc: int = 8) -> Dict[str, int]:
    """Avrupa: tek sorguda ülke adı OR + year facet. Dünya serisi kullanılmaz."""
    global _eu_year_cooldown_until
    empty = {str(y): 0 for y in trend_years()}
    row = live_topic_row(topic)
    cached = row.get("europe_years")
    if isinstance(cached, dict) and any(int(cached.get(str(y), 0) or 0) for y in trend_years()):
        return {str(y): int(cached.get(str(y), 0) or 0) for y in trend_years()}
    if not get_springer_api_key():
        return empty
    if time.time() < _eu_year_cooldown_until:
        return empty
    extra = _europe_or_clause(topic, max_cc=max_cc)
    data = _meta(_query(topic, extra=extra), page=1, start=1, facet=True)
    if not data:
        _eu_year_cooldown_until = time.time() + 90.0
        return empty
    years = _year_map(_facets(data).get("year") or [])
    if any(years.values()):
        _save_topic(topic, {"europe_years": years})
    return years


def europe_year_charts(topic: Optional[str] = None) -> tuple[Dict[str, Dict[str, int]], Dict[str, int]]:
    tpc = (topic or "").strip() or None
    names = [tpc] if tpc and tpc in TOPIC_ORDER else list(TOPIC_ORDER)
    series: Dict[str, Dict[str, int]] = {}
    totals: Dict[str, int] = {}
    for name in names:
        years = _europe_year_map(name)
        series[name] = years
        n = sum(int(years.get(str(y), 0) or 0) for y in trend_years())
        if n:
            totals[name] = n
    return series, totals


def europe_trend_df(topic: Optional[str] = None):
    import pandas as pd

    series, _ = europe_year_charts(topic)
    axis = list(trend_years())
    keep = [name for name in TOPIC_ORDER if name in series]
    if topic:
        keep = [topic] if topic in series else []
    if not keep or not any(sum((series.get(n) or {}).values()) for n in keep):
        return None
    data: Dict[str, List[int]] = {"Years": axis}
    for name in keep:
        years = series.get(name) or {}
        data[name] = [int(years.get(str(y), 0) or 0) for y in axis]
    return pd.DataFrame(data)


def list_cited_papers(
    region: str = "both",
    topic: Optional[str] = None,
    *,
    limit: int = 30,
) -> List[Dict[str, Any]]:
    """Dünya: yıl yeniden→eski. Avrupa: atıf yüksek→düşük ve yalnız Avrupa bağlılığı."""
    from backend.topic_filter import paper_on_topic

    blob = load_live()
    topics = blob.get("topics") if isinstance(blob.get("topics"), dict) else {}
    tpc = (topic or "").strip() or None
    names = [tpc] if tpc and tpc in TOPIC_ORDER else list(TOPIC_ORDER)
    pool: List[Dict[str, Any]] = []
    seen = set()
    for name in names:
        row = topics.get(name) if isinstance(topics.get(name), dict) else {}
        for paper in row.get("cited") or []:
            if not isinstance(paper, dict):
                continue
            item = dict(paper)
            item["topic"] = item.get("topic") or name
            if not paper_on_topic(item, tpc):
                continue
            doi = str(item.get("doi") or "").strip().lower()
            key = doi or str(item.get("title") or "").casefold()
            if not key or key in seen:
                continue
            seen.add(key)
            pool.append(item)
    if region == "eu":
        kept: List[Dict[str, Any]] = []
        seen_eu = set()
        for name in names:
            for paper in _europe_cited_for_topic(name, max_cc=5 if tpc else 2):
                if not paper_on_topic(paper, tpc or name):
                    continue
                doi = str(paper.get("doi") or "").strip().lower()
                key = doi or str(paper.get("title") or "").casefold()
                if not key or key in seen_eu:
                    continue
                seen_eu.add(key)
                kept.append(paper)
        kept.sort(
            key=lambda p: (
                -int(p.get("citations") or 0),
                -int(p.get("year") or 0),
                str(p.get("title") or ""),
            )
        )
        return kept[:limit]
    pool.sort(
        key=lambda p: (
            int(p.get("year") or 0),
            str(p.get("date") or ""),
            int(p.get("citations") or 0),
            str(p.get("title") or ""),
        ),
        reverse=True,
    )
    return pool[:limit]

