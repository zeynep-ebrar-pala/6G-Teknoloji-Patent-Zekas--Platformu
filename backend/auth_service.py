"""
API key authentication for Groq and Google Gemini providers.
"""

from typing import Literal, Optional, Tuple

from i18n.core import t

Provider = Literal["groq", "gemini"]


def validate_api_key(provider: Provider, api_key: str) -> Tuple[bool, str]:
    """Validate provider API key with a minimal live request."""
    key = (api_key or "").strip()
    if not key:
        return False, t("auth.empty")

    if provider == "groq":
        return _validate_groq(key)
    if provider == "gemini":
        return _validate_gemini(key)
    return False, t("auth.bad_provider")


def _validate_groq(api_key: str) -> Tuple[bool, str]:
    try:
        from groq import Groq

        client = Groq(api_key=api_key)
        client.models.list()
        return True, t("auth.groq_ok")
    except ImportError:
        return False, t("auth.groq_missing")
    except Exception as exc:
        return False, t("auth.groq_bad", exc=exc)


def _validate_gemini(api_key: str) -> Tuple[bool, str]:
    from backend.gemini_util import gemini_list_models, safe_error_text

    try:
        data = gemini_list_models(api_key)
        if data.get("error"):
            return False, t("auth.gemini_bad", exc=safe_error_text(Exception(str(data["error"]))))
        return True, t("auth.gemini_ok")
    except Exception as exc:
        from backend.gemini_util import gemini_quota_error, gemini_retryable_error

        if gemini_retryable_error(exc) or gemini_quota_error(exc):
            return True, t("auth.gemini_ok_quota")
        return False, t("auth.gemini_bad", exc=safe_error_text(exc))


def resolve_stored_key(provider: Provider) -> Optional[str]:
    from backend.config import get_gemini_api_key, get_groq_api_key

    if provider == "groq":
        return get_groq_api_key()
    return get_gemini_api_key()
