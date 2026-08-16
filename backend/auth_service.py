"""
API key authentication for Groq and Google Gemini providers.
"""

from typing import Literal, Optional, Tuple

Provider = Literal["groq", "gemini"]


def validate_api_key(provider: Provider, api_key: str) -> Tuple[bool, str]:
    """Validate provider API key with a minimal live request."""
    key = (api_key or "").strip()
    if not key:
        return False, "API anahtarı boş olamaz."

    if provider == "groq":
        return _validate_groq(key)
    if provider == "gemini":
        return _validate_gemini(key)
    return False, "Geçersiz sağlayıcı seçimi."


def _validate_groq(api_key: str) -> Tuple[bool, str]:
    try:
        from groq import Groq

        client = Groq(api_key=api_key)
        client.models.list()
        return True, "Groq API anahtarı doğrulandı."
    except ImportError:
        return False, "Groq kütüphanesi yüklü değil. pip install groq"
    except Exception as exc:
        return False, f"Groq anahtarı geçersiz: {exc}"


def _validate_gemini(api_key: str) -> Tuple[bool, str]:
    try:
        from google import genai

        client = genai.Client(api_key=api_key)
        list(client.models.list())
        return True, "Gemini API anahtarı doğrulandı."
    except ImportError:
        return False, "Gemini kütüphanesi yüklü değil. pip install google-genai"
    except Exception as exc:
        return False, f"Gemini anahtarı geçersiz: {exc}"


def resolve_stored_key(provider: Provider) -> Optional[str]:
    from backend.config import get_gemini_api_key, get_groq_api_key

    if provider == "groq":
        return get_groq_api_key()
    return get_gemini_api_key()
