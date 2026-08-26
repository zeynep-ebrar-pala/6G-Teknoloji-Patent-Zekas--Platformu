"""
Şartname yayın kaynakları — yalnız bu sitelerin resmi API’si.
IEEE Xplore, Springer Nature, Elsevier Scopus.
Google Scholar resmi API yok; HTML kazınmaz. SERPAPI_KEY varsa üçüncü taraf.
Anahtar yoksa None (UI —).
"""

from __future__ import annotations

import json
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional

from backend.config import (
    get_elsevier_api_key,
    get_elsevier_inst_token,
    get_ieee_api_key,
    get_serpapi_key,
    get_springer_api_key,
)
from backend.years import last5_window, year_window

CACHE_PATH = Path(__file__).resolve().parents[1] / "data" / "cache" / "publisher_native.json"
UA = "6G-Patent-Platform/1.3 (mailto:zeynep.ebrar.pala@example.com)"


def YEARS() -> tuple[int, int]:
    return year_window()


def LAST5() -> tuple[int, int]:
    return last5_window()

TOPIC_TOKEN: Dict[str, str] = {
    "ISAC": "ISAC",
    "RIS": "RIS",
    "Cell-Free": "cell-free massive MIMO",
    "THz": "THz",
    "AI-RAN": "AI-RAN",
    "NTN": "NTN",
    "Ambient IoT": "ambient IoT",
}

REGISTER = {
    "ieee": "https://developer.ieee.org/getting_started",
    "springer": "https://dev.springernature.com/",
    "elsevier": "https://dev.elsevier.com/",
    "scholar": "https://scholar.google.com/",
}


def _load() -> Dict[str, Any]:
    if not CACHE_PATH.exists():
        return {}
    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def _save(payload: Dict[str, Any]) -> None:
    try:
        CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
        CACHE_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    except OSError:
        pass


def _cache_get(key: str) -> Optional[int]:
    item = (_load().get("counts") or {}).get(key)
    if isinstance(item, dict) and isinstance(item.get("n"), int):
        return int(item["n"])
    return None


def _cache_put(key: str, n: int) -> None:
    data = _load()
    counts = data.get("counts") or {}
    counts[key] = {"n": n, "at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")}
    data["counts"] = counts
    _save(data)


def _json(
    url: str,
    headers: Optional[Dict[str, str]] = None,
    timeout: int = 18,
) -> Optional[Dict[str, Any]]:
    h = {"User-Agent": UA, "Accept": "application/json"}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, headers=h)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError, ValueError):
        return None


def _q6g(topic: Optional[str]) -> str:
    token = TOPIC_TOKEN.get(topic or "", "")
    if token:
        return f'"6G" {token}'
    return '"6G"'


def key_status() -> Dict[str, bool]:
    return {
        "ieee": bool(get_ieee_api_key()),
        "springer": bool(get_springer_api_key()),
        "elsevier": bool(get_elsevier_api_key()),
        "scholar": bool(get_serpapi_key()),
    }


def key_fingerprint() -> str:
    """st.cache_data anahtar eklenince eski None’u kilitlemesin."""
    return "|".join(f"{name}={int(ok)}" for name, ok in sorted(key_status().items()))


def _ieee_count(query: str, affiliation: Optional[str], *, force: bool = False) -> Optional[int]:
    key = get_ieee_api_key()
    if not key:
        return None
    y0, y1 = year_window()
    cache_key = f"ieee:{affiliation or 'all'}:{query}:{y0}-{y1}"
    hit = _cache_get(cache_key)
    if hit is not None and not force:
        return hit
    params = {
        "apikey": key,
        "format": "json",
        "max_records": "1",
        "start_year": str(y0),
        "end_year": str(y1),
        "querytext": query,
    }
    if affiliation:
        params["affiliation"] = affiliation
    url = "https://ieeexploreapi.ieee.org/api/v1/search/articles?" + urllib.parse.urlencode(params)
    data = _json(url)
    if not data:
        return hit
    total = data.get("total_records")
    if total is None:
        total = data.get("totalfound")
    try:
        n = int(total)
    except (TypeError, ValueError):
        return hit
    _cache_put(cache_key, n)
    return n


def _springer_count(
    query: str,
    affiliation: Optional[str] = None,
    years: Optional[tuple] = None,
    *,
    force: bool = False,
) -> Optional[int]:
    key = get_springer_api_key()
    if not key:
        return None
    span = years or year_window()
    y0, y1 = int(span[0]), int(span[1])
    cache_key = f"springer:{affiliation or 'all'}:{query}:{y0}-{y1}"
    hit = _cache_get(cache_key)
    if hit is not None and not force:
        return hit
    q = f"{query} onlinedatefrom:{y0}-01-01 onlinedateto:{y1}-12-31"
    if affiliation:
        # Basic Meta: affiliation: alanı 403 (premium). Metin araması: 6G Turkey.
        q = f"{query} {affiliation} onlinedatefrom:{y0}-01-01 onlinedateto:{y1}-12-31"
    url = (
        "https://api.springernature.com/meta/v2/json?"
        + urllib.parse.urlencode({"q": q, "api_key": key, "p": "1", "s": "1"})
    )
    data = _json(url)
    if not data:
        return hit
    result = data.get("result") or []
    if isinstance(result, list) and result:
        total = result[0].get("total")
    elif isinstance(result, dict):
        total = result.get("total")
    else:
        total = data.get("total")
    try:
        n = int(str(total).replace(",", ""))
    except (TypeError, ValueError):
        return hit
    _cache_put(cache_key, n)
    return n


def peek_springer_count(
    query: str,
    affiliation: Optional[str] = None,
    years: Optional[tuple] = None,
) -> Optional[int]:
    span = years or year_window()
    y0, y1 = int(span[0]), int(span[1])
    return _cache_get(f"springer:{affiliation or 'all'}:{query}:{y0}-{y1}")


def _elsevier_count(query: str, affiliation: Optional[str], *, force: bool = False) -> Optional[int]:
    key = get_elsevier_api_key()
    if not key:
        return None
    y0, y1 = year_window()
    cache_key = f"elsevier:{affiliation or 'all'}:{query}:{y0}-{y1}"
    hit = _cache_get(cache_key)
    if hit is not None and not force:
        return hit
    headers = {"X-ELS-APIKey": key, "Accept": "application/json"}
    inst = get_elsevier_inst_token()
    if inst:
        headers["X-ELS-Insttoken"] = inst
    if affiliation:
        q = (
            f"TITLE({query}) AND AFFILCOUNTRY({affiliation}) "
            f"AND PUBYEAR > {y0 - 1} AND PUBYEAR < {y1 + 1}"
        )
        url = (
            "https://api.elsevier.com/content/search/scopus?"
            + urllib.parse.urlencode({"query": q, "count": "1", "httpAccept": "application/json"})
        )
    else:
        q = f"TITLE({query}) AND PUBYEAR > {y0 - 1} AND PUBYEAR < {y1 + 1}"
        url = (
            "https://api.elsevier.com/content/search/sciencedirect?"
            + urllib.parse.urlencode({"query": q, "count": "1"})
        )
    data = _json(url, headers=headers)
    if not data:
        return hit
    block = data.get("search-results") or data
    total = block.get("opensearch:totalResults")
    try:
        n = int(str(total))
    except (TypeError, ValueError):
        return hit
    _cache_put(cache_key, n)
    return n


def _scholar_count(query: str, affiliation: Optional[str], *, force: bool = False) -> Optional[int]:
    """Google Scholar HTML kazınmaz. Yalnız isteğe bağlı SerpAPI."""
    key = get_serpapi_key()
    if not key:
        return None
    q = query
    if affiliation:
        q = f"{query} {affiliation}"
    y0, y1 = year_window()
    cache_key = f"scholar:{affiliation or 'all'}:{q}:{y0}-{y1}"
    hit = _cache_get(cache_key)
    if hit is not None and not force:
        return hit
    params = {
        "engine": "google_scholar",
        "q": q,
        "as_ylo": str(y0),
        "as_yhi": str(y1),
        "num": "1",
        "api_key": key,
    }
    url = "https://serpapi.com/search.json?" + urllib.parse.urlencode(params)
    data = _json(url)
    if not data:
        return hit
    info = data.get("search_information") or {}
    total = info.get("total_results")
    try:
        n = int(str(total).replace(",", ""))
    except (TypeError, ValueError):
        return hit
    _cache_put(cache_key, n)
    return n


def fetch_springer_topic_totals(_keys: str = "") -> Dict[str, Optional[int]]:
    """Disk önbelleği — ağ yok. Arka plan doldurur."""
    return {name: peek_springer_count(_q6g(name), None) for name in TOPIC_TOKEN}


def fetch_springer_turkey_topics(_keys: str = "") -> Dict[str, Optional[int]]:
    """Disk: «6G {token} Turkey», son 5 takvim yılı. Ağ yok."""
    span = last5_window()
    return {name: peek_springer_count(_q6g(name), "Turkey", span) for name in TOPIC_TOKEN}


def fetch_native_counts(
    region: str = "tr",
    topic: Optional[str] = None,
    _keys: str = "",
) -> Dict[str, Optional[int]]:
    """IEEE / Springer / Elsevier / Scholar — yalnız disk. Anahtar yoksa veya önbellek yoksa None."""
    q = _q6g(topic)
    empty = {"ieee": None, "springer": None, "elsevier": None, "scholar": None}
    y0, y1 = year_window()
    if region == "eu":
        out = dict(empty)
        out["scholar"] = _cache_get(f"scholar:Europe:{q}:{y0}-{y1}")
        return out
    return {
        "ieee": _cache_get(f"ieee:Turkey:{q}:{y0}-{y1}"),
        "springer": peek_springer_count(q, "Turkey"),
        "elsevier": _cache_get(f"elsevier:turkey:{q}:{y0}-{y1}"),
        "scholar": _cache_get(f"scholar:Turkey:{q}:{y0}-{y1}"),
    }
