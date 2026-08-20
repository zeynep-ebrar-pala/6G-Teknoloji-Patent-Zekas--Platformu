"""
Patent ofisi — Google Patents xhr.
Anahtar yoksa None (UI —). HTML kazınmaz.
"""

from __future__ import annotations

import base64
import json
import re
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
import time

import streamlit as st

from backend.config import (
    get_epo_ops_key,
    get_epo_ops_secret,
    get_lens_token,
    get_patentsview_api_key,
)

CACHE_PATH = Path(__file__).resolve().parents[1] / "data" / "cache" / "source_totals.json"
GP_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)
UA = "6G-Patent-Platform/1.3 (mailto:zeynep.ebrar.pala@example.com)"


def _gp_get(url: str, timeout: int = 18) -> Optional[Dict[str, Any]]:
    """Google Patents xhr. 503/429 olursa iki kez bekleyip dener. HTML kazınmaz."""
    req = urllib.request.Request(url, headers={"User-Agent": GP_UA, "Accept": "application/json"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            return data if isinstance(data, dict) else None
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 503) and attempt < 2:
                time.sleep(1.5 * (attempt + 1))
                continue
            return None
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, ValueError):
            return None
    return None

REGISTER = {
    "google_patents": "https://patents.google.com/",
    "lens": "https://www.lens.org/lens/user/subscriptions",
    "espacenet": "https://developers.epo.org/",
    "wipo": "https://www.wipo.int/patentscope/en/",
    "uspto": "https://patentsview.org/apis/api-registration",
}


def key_status() -> Dict[str, bool]:
    return {
        "lens": bool(get_lens_token()),
        "uspto": bool(get_patentsview_api_key()),
        "espacenet": bool(get_epo_ops_key() and get_epo_ops_secret()),
        "wipo": False,
        "google_patents": True,
    }


def key_fingerprint() -> str:
    return "|".join(f"{name}={int(ok)}" for name, ok in sorted(key_status().items()))


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
    *,
    headers: Optional[Dict[str, str]] = None,
    data: Optional[bytes] = None,
    timeout: int = 18,
) -> Optional[Any]:
    h = {"User-Agent": UA, "Accept": "application/json"}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, data=data, headers=h)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8")
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError):
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return raw


def google_patents_count(query: str) -> Optional[int]:
    q = (query or "").strip()
    if not q:
        return None
    cache_key = f"gp:{q}"
    hit = _cache_get(cache_key)
    if hit is not None:
        return hit
    inner = f"q={urllib.parse.quote_plus(q)}&num=1"
    url = f"https://patents.google.com/xhr/query?url={urllib.parse.quote(inner)}"
    data = _gp_get(url, timeout=8)
    if not data:
        return None
    total = (data.get("results") or {}).get("total_num_results")
    if not isinstance(total, int):
        return None
    _cache_put(cache_key, total)
    return total


def _lens_count(query: str) -> Optional[int]:
    token = get_lens_token()
    if not token:
        return None
    cache_key = f"lens:{query}"
    hit = _cache_get(cache_key)
    if hit is not None:
        return hit
    payload = json.dumps({"query": query, "size": 0}).encode("utf-8")
    data = _json(
        "https://api.lens.org/patent/search",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        data=payload,
    )
    if not isinstance(data, dict):
        return None
    total = data.get("total")
    if total is None:
        total = (data.get("results") or {}).get("total")
    try:
        n = int(total)
    except (TypeError, ValueError):
        return None
    _cache_put(cache_key, n)
    return n


def _patentsview_count(query: str) -> Optional[int]:
    key = get_patentsview_api_key()
    if not key:
        return None
    cache_key = f"uspto:{query}"
    hit = _cache_get(cache_key)
    if hit is not None:
        return hit
    qobj = json.dumps(
        {
            "_or": [
                {"_text_any": {"patent_title": query}},
                {"_text_any": {"patent_abstract": query}},
            ]
        }
    )
    url = (
        "https://search.patentsview.org/api/v1/patent/?"
        + urllib.parse.urlencode({"q": qobj, "o": json.dumps({"size": 1})})
    )
    data = _json(url, headers={"X-Api-Key": key})
    if not isinstance(data, dict):
        return None
    total = data.get("total_hits")
    if total is None:
        total = data.get("count")
    try:
        n = int(total)
    except (TypeError, ValueError):
        return None
    _cache_put(cache_key, n)
    return n


def _epo_ops_count(query: str) -> Optional[int]:
    consumer = get_epo_ops_key()
    secret = get_epo_ops_secret()
    if not consumer or not secret:
        return None
    cache_key = f"epo:{query}"
    hit = _cache_get(cache_key)
    if hit is not None:
        return hit
    basic = base64.b64encode(f"{consumer}:{secret}".encode("utf-8")).decode("ascii")
    token_raw = _json(
        "https://ops.epo.org/3.2/auth/accesstoken",
        headers={
            "Authorization": f"Basic {basic}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data=b"grant_type=client_credentials",
    )
    token = None
    if isinstance(token_raw, dict):
        token = token_raw.get("access_token")
    if not token:
        return None
    q = urllib.parse.quote(f'txt="{query}"')
    url = f"https://ops.epo.org/3.2/rest-services/published-data/search?q={q}&Range=1-1"
    req = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {token}", "Accept": "application/json", "User-Agent": UA},
    )
    try:
        with urllib.request.urlopen(req, timeout=18) as resp:
            body = resp.read().decode("utf-8")
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError):
        return None
    match = re.search(r'"total-result-count"\s*:\s*"?(\d+)"?', body) or re.search(
        r"total-result-count[^0-9]*(\d+)", body
    )
    if not match:
        return None
    n = int(match.group(1))
    _cache_put(cache_key, n)
    return n


def _iter_gp_patents(payload: Any) -> List[Dict[str, Any]]:
    cluster = ((payload or {}).get("results") or {}).get("cluster") or []
    out: List[Dict[str, Any]] = []
    for cl in cluster:
        if isinstance(cl, dict):
            items = cl.get("result") or []
        elif isinstance(cl, list):
            items = cl
        else:
            continue
        if isinstance(items, dict):
            items = [items]
        for item in items:
            if not isinstance(item, dict):
                continue
            patent = item.get("patent") if isinstance(item.get("patent"), dict) else item
            if isinstance(patent, dict):
                out.append(patent)
    return out


def _xhr_payload(query: str, num: int, page: int) -> Optional[Dict[str, Any]]:
    inner = f"q={urllib.parse.quote_plus(query)}&num={num}&page={page}"
    url = f"https://patents.google.com/xhr/query?url={urllib.parse.quote(inner)}"
    return _gp_get(url, timeout=18)


def _rows_from_patents(patents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for patent in patents:
        pub = str(patent.get("publication_number") or "").strip()
        title = str(patent.get("title") or "").strip()
        assignee = str(patent.get("assignee") or "").strip()
        published = str(patent.get("publication_date") or patent.get("filing_date") or "")
        year = None
        if len(published) >= 4 and published[:4].isdigit():
            year = int(published[:4])
        if not pub or not title or year is None:
            continue
        rows.append(
            {
                "publication_number": pub,
                "title": title,
                "assignee": assignee,
                "year": year,
                "abstract": str(patent.get("snippet") or "").strip(),
                "source": "Google Patents xhr",
            }
        )
    return rows


def google_patents_records(query: str, num: int = 10, pages: int = 3) -> List[Dict[str, Any]]:
    """Google Patents xhr sonuç satırları. HTML kazınmaz. Özet yoksa snippet."""
    q = (query or "").strip()
    if not q:
        return []
    n = max(1, min(int(num or 10), 20))
    pmax = max(1, min(int(pages or 1), 5))
    cache_key = f"gp_rec:{q}:{n}:{pmax}"
    disk = _load()
    recs = (disk.get("records") or {}).get(cache_key)
    if isinstance(recs, list) and recs:
        return recs
    rows: List[Dict[str, Any]] = []
    seen: set = set()
    for page in range(1, pmax + 1):
        data = _xhr_payload(q, n, page)
        if not data:
            break
        batch = _rows_from_patents(_iter_gp_patents(data))
        if not batch:
            break
        for row in batch:
            pub = row["publication_number"]
            if pub in seen:
                continue
            seen.add(pub)
            rows.append(row)
        time.sleep(0.15)
    if rows:
        payload = _load()
        records = payload.get("records") or {}
        records[cache_key] = rows
        payload["records"] = records
        _save(payload)
    return rows


@st.cache_data(ttl=21600, show_spinner=False)
def fetch_office_counts(query: str, _keys: str = "") -> Dict[str, Optional[int]]:
    """Aynı 6G/konu sorgusu. WIPO anahtarsız JSON toplam vermez."""
    q = (query or "6G").strip() or "6G"
    return {
        "google_patents": google_patents_count(q),
        "lens": _lens_count(q),
        "espacenet": _epo_ops_count(q),
        "wipo": None,
        "uspto": _patentsview_count(q),
    }


@st.cache_data(ttl=21600, show_spinner=False)
def live_assignee_counts(query: str, companies: tuple) -> Dict[str, Optional[int]]:
    """Google Patents xhr — hak sahibi + konu. Örnek küme ile toplanmaz."""
    q = (query or "6G").strip() or "6G"
    out: Dict[str, Optional[int]] = {}
    for name in companies:
        a = (name or "").strip()
        if not a:
            continue
        out[a] = google_patents_count(f'{q} assignee:"{a}"')
    return out
