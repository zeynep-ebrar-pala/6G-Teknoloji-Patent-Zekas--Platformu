"""Gemini REST istemcisi — UTF-8 güvenli; google-genai ASCII hatasından kaçınır."""

from __future__ import annotations

import json
import urllib.error
import urllib.parse
import urllib.request

_GEMINI_BASE = "https://generativelanguage.googleapis.com/v1beta"


def safe_error_text(exc: BaseException, *, max_len: int = 120) -> str:
    raw = str(exc) or repr(exc)
    return raw.encode("ascii", errors="replace").decode("ascii")[:max_len]


def gemini_retryable_error(exc: Exception) -> bool:
    """404 veya kota — sonraki modele geç."""
    text = str(exc).lower()
    if (
        "404" in text
        or "not_found" in text
        or "not found" in text
        or "no longer available" in text
    ):
        return True
    return (
        "429" in text
        or "resource_exhausted" in text
        or "quota" in text
        or "rate limit" in text
        or "rate_limit" in text
    )


def gemini_quota_error(exc: Exception) -> bool:
    text = str(exc).lower()
    return "429" in text or "resource_exhausted" in text or "quota" in text


def gemini_error_summary(exc: Exception, *, max_len: int = 120) -> str:
    if gemini_quota_error(exc):
        return safe_error_text(
            Exception("Free-tier quota exhausted or model not on plan; trying Flash.")
        )
    return safe_error_text(exc, max_len=max_len)


def _read_http_error(err: urllib.error.HTTPError) -> str:
    try:
        return err.read().decode("utf-8", errors="replace")
    except Exception:
        return str(err)


def gemini_list_models(api_key: str, *, timeout: float = 20.0) -> dict:
    """Models list — anahtar doğrulama."""
    url = f"{_GEMINI_BASE}/models?{urllib.parse.urlencode({'key': api_key})}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"}, method="GET")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def gemini_generate(api_key: str, model: str, prompt: str, *, timeout: float = 120.0) -> str:
    """generateContent — prompt UTF-8 JSON."""
    model_id = model if model.startswith("models/") else f"models/{model}"
    url = (
        f"{_GEMINI_BASE}/{model_id}:generateContent?"
        f"{urllib.parse.urlencode({'key': api_key})}"
    )
    payload = json.dumps(
        {"contents": [{"parts": [{"text": prompt}]}]},
        ensure_ascii=False,
    ).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        detail = _read_http_error(err)
        raise RuntimeError(f"HTTP {err.code}: {detail}") from err

    if data.get("error"):
        raise RuntimeError(json.dumps(data["error"], ensure_ascii=False))

    candidates = data.get("candidates") or []
    if not candidates:
        return ""
    parts = (candidates[0].get("content") or {}).get("parts") or []
    texts = [str(p.get("text") or "") for p in parts if isinstance(p, dict)]
    return "\n".join(t for t in texts if t).strip()
