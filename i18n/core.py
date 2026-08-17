"""
Merkezi i18n: dil durumu, t(key), locale biçimleme, eksik anahtar fallback.
Yeni dil eklemek: SUPPORTED_LANGS + i18n/strings.py içine katalog.
"""

from __future__ import annotations

import os
import sys
from typing import Any, Iterable

SESSION_KEY = "ui_lang"
SUPPORTED_LANGS: tuple[str, ...] = ("tr", "en")
DEFAULT_LANG = "tr"
FALLBACK_LANG = "tr"

_MISSING: set[tuple[str, str]] = set()
_FLAT: dict[str, dict[str, str]] | None = None


def flatten(data: dict[str, Any], prefix: str = "") -> dict[str, str]:
    out: dict[str, str] = {}
    for key, val in data.items():
        dotted = f"{prefix}.{key}" if prefix else str(key)
        if isinstance(val, dict):
            out.update(flatten(val, dotted))
        else:
            out[dotted] = str(val)
    return out


def _catalogs() -> dict[str, dict[str, str]]:
    global _FLAT
    if _FLAT is None:
        from i18n.strings import UI

        _FLAT = {lang: flatten(UI[lang]) for lang in SUPPORTED_LANGS}
    return _FLAT


def bootstrap_lang() -> str:
    """query_params + session_state. Widget'tan önce çağırın."""
    import streamlit as st

    raw = st.query_params.get("lang")
    if isinstance(raw, list):
        raw = raw[0] if raw else None
    if raw in SUPPORTED_LANGS and SESSION_KEY not in st.session_state:
        st.session_state[SESSION_KEY] = raw
    if SESSION_KEY not in st.session_state:
        st.session_state[SESSION_KEY] = DEFAULT_LANG
    lang = st.session_state[SESSION_KEY]
    if lang not in SUPPORTED_LANGS:
        lang = DEFAULT_LANG
        st.session_state[SESSION_KEY] = lang
    if st.query_params.get("lang") != lang:
        st.query_params["lang"] = lang
    return lang


def get_lang() -> str:
    try:
        import streamlit as st

        lang = st.session_state.get(SESSION_KEY)
        if lang in SUPPORTED_LANGS:
            return lang
        raw = st.query_params.get("lang")
        if isinstance(raw, list):
            raw = raw[0] if raw else None
        if raw in SUPPORTED_LANGS:
            return raw
    except Exception:
        pass
    return DEFAULT_LANG


def t(key: str, **kwargs: Any) -> str:
    """Çeviri anahtarı. Eksikte fallback dile, o da yoksa anahtarın kendisine düşer."""
    lang = get_lang()
    catalogs = _catalogs()
    text = catalogs.get(lang, {}).get(key)
    if text is None:
        _MISSING.add((lang, key))
        if os.environ.get("I18N_DEBUG"):
            print(f"[i18n] missing {lang}: {key}", file=sys.stderr)
        text = catalogs.get(FALLBACK_LANG, {}).get(key, key)
    if kwargs:
        try:
            text = text.format(**kwargs)
        except (KeyError, IndexError, ValueError):
            pass
    return text


def missing_keys() -> frozenset[tuple[str, str]]:
    return frozenset(_MISSING)


def catalog_key_set(lang: str) -> set[str]:
    return set(_catalogs().get(lang, {}))


def assert_catalog_parity() -> list[str]:
    """TR/EN (ve ileride diğer diller) anahtar farklarını döndürür."""
    catalogs = _catalogs()
    base = catalog_key_set(FALLBACK_LANG)
    problems: list[str] = []
    for lang in SUPPORTED_LANGS:
        keys = catalog_key_set(lang)
        missing = sorted(base - keys)
        extra = sorted(keys - base)
        for k in missing:
            problems.append(f"{lang} missing: {k}")
        for k in extra:
            problems.append(f"{lang} extra: {k}")
    return problems


def format_int(value: int | None) -> str:
    if value is None:
        return "—"
    if get_lang() == "tr":
        return f"{value:,}".replace(",", ".")
    return f"{value:,}"


def format_decimal(value: float, digits: int = 1) -> str:
    if get_lang() == "tr":
        return f"{value:.{digits}f}".replace(".", ",")
    return f"{value:.{digits}f}"


def iter_supported() -> Iterable[str]:
    return SUPPORTED_LANGS
