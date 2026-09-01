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
    try:
        from google import genai

        from backend.config import get_gemini_auth_probe_models
        from backend.gemini_util import gemini_quota_error, gemini_retryable_error

        client = genai.Client(api_key=api_key)
        list(client.models.list())

        quota_hit = False
        for model in get_gemini_auth_probe_models():
            try:
                response = client.models.generate_content(model=model, contents="ok")
                if getattr(response, "text", None):
                    return True, t("auth.gemini_ok")
            except Exception as exc:
                if gemini_retryable_error(exc):
                    if gemini_quota_error(exc):
                        quota_hit = True
                    continue
                return False, t("auth.gemini_bad", exc=str(exc)[:120])

        if quota_hit:
            return True, t("auth.gemini_ok_quota")
        return True, t("auth.gemini_ok")
    except ImportError:
        return False, t("auth.gemini_missing")
    except Exception as exc:
        return False, t("auth.gemini_bad", exc=str(exc)[:120])


def resolve_stored_key(provider: Provider) -> Optional[str]:
    from backend.config import get_gemini_api_key, get_groq_api_key

    if provider == "groq":
        return get_groq_api_key()
    return get_gemini_api_key()
