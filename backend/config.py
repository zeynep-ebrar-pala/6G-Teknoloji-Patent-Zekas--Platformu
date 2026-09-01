"""Ortam değişkenleri (.env) yükleyici ve API anahtarı erişimi."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Literal, Optional

from dotenv import load_dotenv

_ROOT = Path(__file__).resolve().parent.parent


def reload_env() -> None:
    """Her okumada .env'i yeniden yükle. Boş LENS_TOKEN eski süreci kilitlemesin."""
    path = _ROOT / ".env"
    if path.is_file():
        load_dotenv(path, override=True)


reload_env()

Provider = Literal["groq", "gemini"]

def _secret(name: str) -> Optional[str]:
    reload_env()
    value = (os.getenv(name) or "").strip().strip('"').strip("'")
    if value:
        return value
    try:
        import streamlit as st

        raw = st.secrets.get(name)
        if raw is None:
            return None
        text = str(raw).strip()
        return text or None
    except Exception:
        return None


def get_ieee_api_key() -> Optional[str]:
    return _secret("IEEE_API_KEY")


def get_springer_api_key() -> Optional[str]:
    return _secret("SPRINGER_API_KEY")


def get_elsevier_api_key() -> Optional[str]:
    return _secret("ELSEVIER_API_KEY")


def get_elsevier_inst_token() -> Optional[str]:
    """Scopus kurum aboneliği. Yoksa ülke süzgeçli arama boş kalabilir."""
    return _secret("ELSEVIER_INST_TOKEN")


def get_serpapi_key() -> Optional[str]:
    """Google Scholar resmi API yoktur. SerpAPI üçüncü taraf, isteğe bağlı."""
    return _secret("SERPAPI_KEY")


def get_lens_token() -> Optional[str]:
    """Lens.org patent API — .env veya oturum. Site girişi tek başına yetmez."""
    env = _secret("LENS_TOKEN") or _secret("LENS_API_TOKEN")
    if env:
        return env
    try:
        import streamlit as st

        sess = str(st.session_state.get("lens_token") or "").strip()
        return sess or None
    except Exception:
        return None


def get_patentsview_api_key() -> Optional[str]:
    """USPTO PatentsView — bireysel API anahtarı."""
    return _secret("PATENTSVIEW_API_KEY") or _secret("USPTO_API_KEY")


def get_epo_ops_key() -> Optional[str]:
    """EPO OPS (Espacenet) consumer key — bireysel kayıt."""
    return _secret("EPO_OPS_KEY") or _secret("EPO_CONSUMER_KEY")


def get_epo_ops_secret() -> Optional[str]:
    return _secret("EPO_OPS_SECRET") or _secret("EPO_CONSUMER_SECRET")


def get_groq_api_key() -> Optional[str]:
    return _secret("GROQ_API_KEY")


def get_gemini_api_key() -> Optional[str]:
    return _secret("GEMINI_API_KEY")


def get_gemini_auth_probe_models() -> tuple[str, ...]:
    """Ücretsiz katman — giriş doğrulaması ve öncelikli yanıt."""
    return (
        "gemini-2.5-flash",
        "gemini-3-flash-preview",
        "gemini-flash-latest",
    )


def get_gemini_chat_models() -> tuple[str, ...]:
    """Yalnızca Flash — Pro ücretsiz planda kota 0."""
    override = (_secret("GEMINI_CHAT_MODEL") or os.getenv("GEMINI_CHAT_MODEL") or "").strip()
    if override and "3.1-pro" not in override:
        return (override,)
    return get_gemini_auth_probe_models()


def get_default_ai_provider() -> Provider:
    raw = (os.getenv("DEFAULT_AI_PROVIDER") or "groq").strip().lower()
    return "gemini" if raw == "gemini" else "groq"
