"""
Patent ofisi — Lens.org patent/search (Bearer token).
Token yoksa None (UI —). HTML kazınmaz. Google Patents xhr yedek kalır, sayfa Lens kullanır.
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
_LAST_LENS: Dict[str, Any] = {"code": None, "detail": ""}


def lens_last_error() -> str:
    """Son patent/search HTTP hatası. 200 veya çağrı yoksa boş."""
    code = _LAST_LENS.get("code")
    if not code or code == 200:
        return ""
    return str(_LAST_LENS.get("detail") or f"HTTP {code}").strip()


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


def lens_topic_dsl(topic: str) -> str:
    """Yedi 6G konusundan biri — başlık / özet / istem. Ham «6G» değil."""
    from backend.source_links import SPEC_PUB_TOPICS, TOPIC_TERMS

    key = (topic or "").strip()
    terms = TOPIC_TERMS.get(key)
    if not terms:
        for name, phrase in SPEC_PUB_TOPICS.items():
            if key == phrase or key.lower() == name.lower():
                terms = TOPIC_TERMS.get(name)
                break
    if not terms:
        text = key.replace('"', " ").strip()
        terms = (text,) if text and text not in ("6G", "all", "Tümü", "All") else ()
    if not terms:
        return lens_explorer_dsl()
    clauses = [f'(title:("{t}") OR abstract:("{t}") OR claim:("{t}"))' for t in terms]
    return "(" + " OR ".join(clauses) + ")"


def lens_explorer_dsl() -> str:
    """Yedi 6G Technology Explorer konusu (OR). Samsung 6G telefon gürültüsü yok."""
    from backend.source_links import TOPIC_TERMS

    return "(" + " OR ".join(lens_topic_dsl(name) for name in TOPIC_TERMS) + ")"


def _applicant_clause(company: str) -> str:
    name = (company or "").replace('"', " ").strip()
    aliases = {
        "NICT": '(NICT OR "National Institute of Information and Communications Technology")',
        "NEC": "(NEC)",
        "Intel": "(Intel)",
    }
    inner = aliases.get(name, f"({name})")
    return f"applicant.name:{inner}"


def lens_assignee_dsl(topic: str, company: str) -> str:
    name = (company or "").replace('"', " ").strip()
    dsl = lens_topic_dsl(topic) if (topic or "").strip() else lens_explorer_dsl()
    if not name:
        return dsl
    return f"{dsl} AND {_applicant_clause(name)}"


def _as_list(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _lens_post(payload: Dict[str, Any], timeout: int = 30) -> Optional[Dict[str, Any]]:
    token = get_lens_token()
    if not token:
        _LAST_LENS["code"] = 401
        _LAST_LENS["detail"] = "Missing Authorization"
        return None
    body = json.dumps(payload).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": UA,
    }
    _LAST_LENS["code"] = None
    _LAST_LENS["detail"] = ""
    for attempt in range(3):
        req = urllib.request.Request(
            "https://api.lens.org/patent/search",
            data=body,
            headers=headers,
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            _LAST_LENS["code"] = 200
            _LAST_LENS["detail"] = ""
            return data if isinstance(data, dict) else None
        except urllib.error.HTTPError as exc:
            err_body = ""
            try:
                err_body = exc.read().decode("utf-8", errors="replace")[:240]
            except Exception:
                err_body = ""
            _LAST_LENS["code"] = exc.code
            _LAST_LENS["detail"] = err_body or f"HTTP {exc.code}"
            if exc.code == 404:
                return {"total": 0, "data": []}
            if exc.code == 429 and attempt < 2:
                wait = 2.0
                retry = exc.headers.get("x-rate-limit-retry-after-seconds") if exc.headers else None
                try:
                    wait = max(wait, float(retry))
                except (TypeError, ValueError):
                    pass
                time.sleep(min(wait, 45))
                continue
            return None
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, ValueError) as exc:
            _LAST_LENS["code"] = 0
            _LAST_LENS["detail"] = type(exc).__name__
            return None
    return None


def _lens_total(data: Dict[str, Any]) -> Optional[int]:
    total = data.get("total")
    if total is None:
        total = (data.get("results") or {}).get("total")
    try:
        return int(total)
    except (TypeError, ValueError):
        return None


def _pick_title(titles: Any) -> str:
    english = ""
    first = ""
    for item in _as_list(titles):
        if not isinstance(item, dict):
            continue
        text = str(item.get("text") or "").strip()
        if not text:
            continue
        if not first:
            first = text
        lang = str(item.get("lang") or "").lower()
        if lang.startswith("en"):
            english = text
            break
    return english or first


def _applicant_names(biblio: Dict[str, Any]) -> str:
    parties = biblio.get("parties") if isinstance(biblio.get("parties"), dict) else {}
    names: List[str] = []
    for item in _as_list(parties.get("applicants")):
        if not isinstance(item, dict):
            continue
        extracted = item.get("extracted_name")
        if isinstance(extracted, dict) and extracted.get("value"):
            names.append(str(extracted["value"]).strip())
            continue
        raw = item.get("applicant_name") or item.get("name")
        if isinstance(raw, str) and raw.strip():
            names.append(raw.strip())
            continue
        if isinstance(raw, dict):
            parts = [raw.get("name"), raw.get("first_name"), raw.get("last_name")]
            joined = " ".join(str(p).strip() for p in parts if p)
            if joined:
                names.append(joined)
    seen: set = set()
    unique: List[str] = []
    for name in names:
        key = name.lower()
        if key in seen:
            continue
        seen.add(key)
        unique.append(name)
    return "; ".join(unique)


def _pub_ref(biblio: Dict[str, Any], rec: Dict[str, Any]) -> Dict[str, Any]:
    refs = _as_list(biblio.get("publication_reference"))
    raw = refs[0] if refs and isinstance(refs[0], dict) else {}
    nested = raw.get("document_id") if isinstance(raw.get("document_id"), dict) else {}
    return {
        "country": (
            raw.get("country")
            or raw.get("jurisdiction")
            or nested.get("country")
            or nested.get("jurisdiction")
            or rec.get("country")
            or rec.get("jurisdiction")
        ),
        "doc_number": raw.get("doc_number") or nested.get("doc_number") or rec.get("doc_number"),
        "kind": raw.get("kind") or nested.get("kind") or rec.get("kind"),
        "date": raw.get("date") or nested.get("date") or rec.get("date_published") or rec.get("date_publ"),
    }


def _year_from(text: Any) -> Optional[int]:
    token = str(text or "").strip()
    if len(token) >= 4 and token[:4].isdigit():
        year = int(token[:4])
        if 1980 <= year <= 2035:
            return year
    return None


def _rows_from_lens(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for rec in _as_list(payload.get("data")):
        if not isinstance(rec, dict):
            continue
        biblio = rec.get("biblio") if isinstance(rec.get("biblio"), dict) else {}
        ref = _pub_ref(biblio, rec)
        country = str(ref.get("country") or rec.get("country") or "").strip().upper()
        number = str(ref.get("doc_number") or rec.get("doc_number") or "").strip()
        kind = str(ref.get("kind") or rec.get("kind") or "").strip().upper()
        pub = f"{country}{number}{kind}" if country and number else str(rec.get("doc_key") or "").replace("_", "")
        title = _pick_title(biblio.get("invention_title"))
        year = _year_from(ref.get("date")) or _year_from(rec.get("date_published") or rec.get("date_publ"))
        lens_id = str(rec.get("lens_id") or "").strip()
        assignee = _applicant_names(biblio)
        abstracts = biblio.get("abstract") or biblio.get("abstracts") or rec.get("abstract")
        abstract = ""
        for item in _as_list(abstracts):
            if isinstance(item, dict) and item.get("text"):
                abstract = str(item["text"]).strip()
                lang = str(item.get("lang") or "").lower()
                if lang.startswith("en") or not abstract:
                    if lang.startswith("en"):
                        break
            elif isinstance(item, str) and item.strip() and not abstract:
                abstract = item.strip()
        if isinstance(abstracts, str) and abstracts.strip() and not abstract:
            abstract = abstracts.strip()
        if not pub:
            pub = str(rec.get("lens_id") or "").replace("-", "")
        if not pub or not title or year is None:
            continue
        source_url = f"https://www.lens.org/lens/patent/{lens_id}" if lens_id else ""
        rows.append(
            {
                "publication_number": pub,
                "title": title,
                "assignee": assignee,
                "year": year,
                "abstract": abstract,
                "lens_id": lens_id,
                "source": "Lens.org",
                "source_url": source_url,
            }
        )
    return rows


def lens_search(query: str, size: int = 25) -> Optional[Dict[str, Any]]:
    """POST api.lens.org/patent/search. HTML kazınmaz."""
    q = (query or "").strip()
    if not q or not get_lens_token():
        return None
    n = max(0, min(int(size or 0), 100))
    payload: Dict[str, Any] = {
        "query": q,
        "size": n,
        "include": ["lens_id", "biblio", "date_published", "abstract"],
    }
    data = _lens_post(payload)
    if not isinstance(data, dict):
        return None
    return data


def lens_topic_count(topic: str) -> Optional[int]:
    """Konu taraması toplamı (firma süzülmeden). Token yoksa None."""
    return _lens_count(lens_topic_dsl(topic))


def lens_scope_count(topic: Optional[str] = None) -> Optional[int]:
    """Tümü = yedi Explorer konusu. Tek konu = o DSL."""
    dsl = lens_topic_dsl(topic) if topic else lens_explorer_dsl()
    return _lens_count(dsl)


def _lens_count(query: str) -> Optional[int]:
    token = get_lens_token()
    if not token:
        return None
    cache_key = f"lens:{query}"
    hit = _cache_get(cache_key)
    if hit is not None:
        return hit
    data = lens_search(query, size=0)
    if not data:
        return None
    n = _lens_total(data)
    if n is None:
        return None
    _cache_put(cache_key, n)
    return n


def peek_lens_count(query: str) -> Optional[int]:
    """Disk önbelleği — ağ yok. Sayfa kilitlemesin."""
    q = (query or "").strip()
    if not q:
        return None
    return _cache_get(f"lens:{q}")


def peek_lens_count_map() -> Dict[str, int]:
    """Tüm disk Lens sayıları (ağ yok)."""
    out: Dict[str, int] = {}
    for key, item in (_load().get("counts") or {}).items():
        if not isinstance(key, str) or not key.startswith("lens:"):
            continue
        if isinstance(item, dict) and isinstance(item.get("n"), int):
            out[key[5:]] = int(item["n"])
    return out


@st.cache_data(ttl=3600, show_spinner=False)
def lens_assignee_bundle(topic: str, company: str, _keys: str = "") -> Dict[str, Any]:
    """Bir firma: API toplamı + çekilen kayıt. İkisi toplanmaz."""
    name = (company or "").strip()
    if not name or not get_lens_token():
        return {"total": None, "rows": []}
    data = lens_search(lens_assignee_dsl(topic, name), size=25)
    time.sleep(0.25)
    if not data:
        return {"total": None, "rows": []}
    return {"total": _lens_total(data), "rows": _rows_from_lens(data)}


@st.cache_data(ttl=3600, show_spinner=False)
def lens_topic_vendor_bundle(topic: str, companies: tuple, _keys: str = "") -> Dict[str, Any]:
    """Bir 6G konusu + şartname firmaları (tek POST)."""
    from data.patents import SPEC_COMPANIES

    names = [str(n).strip() for n in (companies or SPEC_COMPANIES) if str(n).strip()]
    if not names or not get_lens_token():
        return {"total": None, "rows": []}
    applicant_or = " OR ".join(_applicant_clause(n) for n in names)
    dsl = f"{lens_topic_dsl(topic)} AND ({applicant_or})"
    data = lens_search(dsl, size=100)
    time.sleep(0.25)
    if not data:
        return {"total": None, "rows": []}
    return {"total": _lens_total(data), "rows": _rows_from_lens(data)}


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
    """Yalnızca Lens.org. Ham «6G» yerine Explorer DSL."""
    q = (query or "").strip()
    dsl = lens_topic_dsl(q) if q and q not in ("6G", "all") else lens_explorer_dsl()
    return {
        "google_patents": None,
        "lens": _lens_count(dsl),
        "espacenet": None,
        "wipo": None,
        "uspto": None,
    }


@st.cache_data(ttl=21600, show_spinner=False)
def live_assignee_counts(topic: str, companies: tuple, _keys: str = "") -> Dict[str, Optional[int]]:
    """Firma çubuğu: yedi konu (veya seçilen konu) × applicant. Çekilen satır değil."""
    names = [str(n).strip() for n in companies if str(n).strip()]
    dsl = lens_topic_dsl(topic) if (topic or "").strip() else lens_explorer_dsl()
    out: Dict[str, Optional[int]] = {}
    for name in names:
        n = _lens_count(f"{dsl} AND {_applicant_clause(name)}")
        out[name] = int(n) if isinstance(n, int) else None
    return out


@st.cache_data(ttl=21600, show_spinner=False)
def live_topic_or_counts(topics: tuple, companies: tuple, _keys: str = "") -> Dict[str, int]:
    """Konu çubuğu: Lens total (size=0). 100 tavanı yok."""
    names = [str(n).strip() for n in companies if str(n).strip()]
    if not names:
        return {str(t): 0 for t in topics}
    applicant_or = " OR ".join(_applicant_clause(n) for n in names)
    out: Dict[str, int] = {}
    for topic in topics:
        key = str(topic).strip()
        if not key:
            continue
        n = _lens_count(f"{lens_topic_dsl(key)} AND ({applicant_or})")
        out[key] = int(n) if isinstance(n, int) else 0
    return out


@st.cache_data(ttl=21600, show_spinner=False)
def live_company_topic_matrix(topics: tuple, companies: tuple, _keys: str = "") -> Dict[str, Dict[str, int]]:
    """Firma × konu Lens total. Yoğunluk / radar / ağaç. Çekilen 100 satır değil."""
    names = [str(n).strip() for n in companies if str(n).strip()]
    axes = [str(t).strip() for t in topics if str(t).strip()]
    out: Dict[str, Dict[str, int]] = {name: {t: 0 for t in axes} for name in names}
    for topic in axes:
        for name in names:
            n = _lens_count(lens_assignee_dsl(topic, name))
            out[name][topic] = int(n) if isinstance(n, int) else 0
    return out


@st.cache_data(ttl=21600, show_spinner=False)
def live_company_year_counts(
    topic: str, companies: tuple, years: tuple, _keys: str = ""
) -> Dict[str, Dict[int, int]]:
    """Yıl × firma Lens total. year_published tam sayı."""
    names = [str(n).strip() for n in companies if str(n).strip()]
    dsl = lens_topic_dsl(topic) if (topic or "").strip() else lens_explorer_dsl()
    out: Dict[str, Dict[int, int]] = {name: {} for name in names}
    for name in names:
        for year in years:
            try:
                y = int(year)
            except (TypeError, ValueError):
                continue
            n = _lens_count(f"{dsl} AND {_applicant_clause(name)} AND year_published:{y}")
            out[name][y] = int(n) if isinstance(n, int) else 0
    return out
