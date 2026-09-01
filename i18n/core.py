"""
Merkezi i18n: dil durumu, t(key), locale biçimleme, eksik anahtar fallback.
Yeni dil eklemek: SUPPORTED_LANGS + i18n/strings.py içine katalog.
"""

from __future__ import annotations

import os
import sys
from typing import Any, Iterable


class _FormatDict(dict):
    """Eksik yer tutucu kırılmasın: {token} belgelerde olduğu gibi kalsın."""

    def __missing__(self, key: str) -> str:
        return "{" + key + "}"

SESSION_KEY = "ui_lang"
SUPPORTED_LANGS: tuple[str, ...] = ("tr", "en")
DEFAULT_LANG = "tr"
FALLBACK_LANG = "tr"

_MISSING: set[tuple[str, str]] = set()
_FLAT: dict[str, dict[str, str]] | None = None
_FLAT_MTIME: int = 0
_UI_ROOT: dict[str, Any] | None = None
_UI_ROOT_MTIME: int = 0


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
    """strings.py değişince eski metin kilitlenmesin (Streamlit süreç içi önbellek)."""
    global _FLAT, _FLAT_MTIME
    import importlib
    from pathlib import Path

    import i18n.strings as strings_mod

    mtime = Path(strings_mod.__file__).stat().st_mtime_ns
    if _FLAT is None or _FLAT_MTIME != mtime:
        strings_mod = importlib.reload(strings_mod)
        _FLAT = {lang: flatten(strings_mod.UI[lang]) for lang in SUPPORTED_LANGS}
        _FLAT_MTIME = mtime
    return _FLAT


def bootstrap_lang() -> str:
    """query_params okur, session_state yazar. URL yazılmaz: Cloud iframe rerun döngüsü olmasın."""
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


def _year_fields() -> dict[str, Any]:
    try:
        from backend.years import format_fields

        return format_fields()
    except Exception:
        y = 2026
        return {"y0": 2020, "y1": y, "l0": y - 4, "l1": y, "end": y}


def _ui_root() -> dict[str, Any]:
    """strings.UI — liste/dict yapıları flatten edilmeden."""
    global _UI_ROOT, _UI_ROOT_MTIME
    import importlib
    from pathlib import Path

    import i18n.strings as strings_mod

    mtime = Path(strings_mod.__file__).stat().st_mtime_ns
    if _UI_ROOT is None or _UI_ROOT_MTIME != mtime:
        strings_mod = importlib.reload(strings_mod)
        _UI_ROOT = strings_mod.UI
        _UI_ROOT_MTIME = mtime
    return _UI_ROOT


def t_value(key: str) -> Any:
    """İç içe katalog değeri (liste, dict, str). Düz metin için t()."""
    lang = get_lang()
    parts = key.split(".")

    def _walk(catalog: dict[str, Any] | None) -> Any:
        if not catalog:
            return None
        node: Any = catalog
        for part in parts:
            if not isinstance(node, dict):
                return None
            node = node.get(part)
            if node is None:
                return None
        return node

    val = _walk(_ui_root().get(lang))
    if val is None and lang != FALLBACK_LANG:
        val = _walk(_ui_root().get(FALLBACK_LANG))
    return val


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
    if "{" not in text:
        return text
    try:
        text = text.format_map(_FormatDict({**_year_fields(), **kwargs}))
    except (KeyError, IndexError, ValueError):
        pass
    return text


def topic_label(name: str) -> str:
    """Grafik/menü konu adı — arayüz dilinde; anahtar yoksa ham ad."""
    raw = (name or "").strip()
    if not raw:
        return raw
    key = f"pub.topic.{raw}"
    labeled = t(key)
    return raw if labeled == key else labeled


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
