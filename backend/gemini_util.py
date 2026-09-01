"""Gemini REST — UTF-8 güvenli; kota ve anahtar hataları ayrı."""

from __future__ import annotations

import json
import urllib.error
import urllib.parse
import urllib.request

_GEMINI_BASE = "https://generativelanguage.googleapis.com/v1beta"


class GeminiQuotaError(RuntimeError):
    """Ücretsiz kota veya model planı — anahtar geçerli olabilir."""


class GeminiAuthError(RuntimeError):
    """API anahtarı reddedildi."""


def safe_error_text(exc: BaseException, *, max_len: int = 80) -> str:
    raw = str(exc) or repr(exc)
    return raw.encode("ascii", errors="replace").decode("ascii")[:max_len]


def _api_error_quota(err: dict) -> bool:
    code = err.get("code")
    status = str(err.get("status") or "").upper()
    msg = str(err.get("message") or "").lower()
    return (
        code == 429
        or status == "RESOURCE_EXHAUSTED"
        or "quota" in msg
        or "rate limit" in msg
    )


def gemini_retryable_error(exc: Exception) -> bool:
    if isinstance(exc, GeminiQuotaError):
        return True
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
    if isinstance(exc, GeminiQuotaError):
        return True
    text = str(exc).lower()
    return "429" in text or "resource_exhausted" in text or "quota" in text


def gemini_error_summary(exc: Exception, *, max_len: int = 80) -> str:
    if gemini_quota_error(exc):
        return "quota"
    return safe_error_text(exc, max_len=max_len)


def _read_http_error(err: urllib.error.HTTPError) -> str:
    try:
        return err.read().decode("utf-8", errors="replace")
    except Exception:
        return str(err)


def _raise_for_http(err: urllib.error.HTTPError) -> None:
    detail = _read_http_error(err)
    if err.code == 429:
        raise GeminiQuotaError(detail) from err
    if err.code in (401, 403):
        raise GeminiAuthError(detail) from err
    try:
        payload = json.loads(detail)
        api_err = payload.get("error") if isinstance(payload, dict) else None
        if isinstance(api_err, dict):
            if _api_error_quota(api_err):
                raise GeminiQuotaError(detail) from err
            if api_err.get("code") in (401, 403):
                raise GeminiAuthError(detail) from err
    except (json.JSONDecodeError, TypeError):
        pass
    raise RuntimeError(f"HTTP {err.code}") from err


def gemini_list_models(api_key: str, *, timeout: float = 20.0) -> dict:
    url = f"{_GEMINI_BASE}/models?{urllib.parse.urlencode({'key': api_key})}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"}, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        _raise_for_http(err)
    err = data.get("error")
    if isinstance(err, dict):
        if _api_error_quota(err):
            raise GeminiQuotaError(json.dumps(err, ensure_ascii=False))
        if err.get("code") in (401, 403):
            raise GeminiAuthError(json.dumps(err, ensure_ascii=False))
    return data


def gemini_generate(api_key: str, model: str, prompt: str, *, timeout: float = 120.0) -> str:
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
        _raise_for_http(err)

    if data.get("error"):
        err = data["error"]
        if isinstance(err, dict) and _api_error_quota(err):
            raise GeminiQuotaError(json.dumps(err, ensure_ascii=False))
        if isinstance(err, dict) and err.get("code") in (401, 403):
            raise GeminiAuthError(json.dumps(err, ensure_ascii=False))
        raise RuntimeError("api_error")

    candidates = data.get("candidates") or []
    if not candidates:
        return ""
    parts = (candidates[0].get("content") or {}).get("parts") or []
    texts = [str(p.get("text") or "") for p in parts if isinstance(p, dict)]
    return "\n".join(t for t in texts if t).strip()
