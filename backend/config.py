"""Ortam değişkenleri (.env) yükleyici ve API anahtarı erişimi."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Literal, Optional

from dotenv import load_dotenv

_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_ROOT / ".env")

Provider = Literal["groq", "gemini"]


def get_groq_api_key() -> Optional[str]:
    value = (os.getenv("GROQ_API_KEY") or "").strip()
    return value or None


def get_gemini_api_key() -> Optional[str]:
    value = (os.getenv("GEMINI_API_KEY") or "").strip()
    return value or None


def get_default_ai_provider() -> Provider:
    raw = (os.getenv("DEFAULT_AI_PROVIDER") or "groq").strip().lower()
    return "gemini" if raw == "gemini" else "groq"
