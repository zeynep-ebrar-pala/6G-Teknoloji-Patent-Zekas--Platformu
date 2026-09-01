"""Gemini API hata sınıflandırması — ortak auth ve asistan."""

from __future__ import annotations


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
        return "Ücretsiz kota doldu veya bu model planda yok; Flash deneniyor."
    raw = str(exc).replace("{", "(").replace("}", ")")
    return raw[:max_len]
