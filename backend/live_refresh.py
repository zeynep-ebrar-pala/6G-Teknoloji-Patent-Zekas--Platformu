"""
Lens.org ve Springer Nature — stale-while-revalidate.
Sayfa disk önbelleğinden açılır; API arka planda çalışır. Ağ UI thread’ini kilitlemez.
"""

from __future__ import annotations

from datetime import timedelta
from typing import Tuple

import streamlit as st

# Aynı oturumda widget rerun API’yi tekrar tetiklemesin.
_SESSION_FLAG = "_live_sources_kicked"


def kickoff_on_visit() -> None:
    """Her tarayıcı oturumunda bir kez: önbelleği göster, kaynakları arka planda yenile."""
    if st.session_state.get(_SESSION_FLAG):
        return
    st.session_state[_SESSION_FLAG] = True
    _start(force=True)


def _start(*, force: bool) -> None:
    from backend.config import get_lens_token, get_springer_api_key, reload_env

    reload_env()
    if get_springer_api_key():
        from backend.springer_live import ensure_prefetch

        ensure_prefetch(force=force)
    if get_lens_token():
        from backend.patent_prefetch import ensure_prefetch
        from data.patents import SPEC_COMPANIES

        ensure_prefetch(None, tuple(SPEC_COMPANIES), force=force)


def _springer_status() -> Tuple[bool, int, int, str]:
    from backend.springer_live import prefetch_status

    data = prefetch_status()
    return (
        bool(data.get("running")),
        int(data.get("done") or 0),
        int(data.get("total") or 0),
        str(data.get("error") or ""),
    )


def _lens_status() -> Tuple[bool, int, int, str]:
    from backend.patent_prefetch import snapshot
    from data.patents import SPEC_COMPANIES

    topic = st.session_state.get("_pat_topic")
    snap = snapshot(topic, tuple(SPEC_COMPANIES))
    return (
        bool(snap.get("running")),
        int(snap.get("done") or 0),
        int(snap.get("total") or 0),
        str(snap.get("error") or ""),
    )


@st.fragment(run_every=timedelta(seconds=10))
def _watch_fragment(source: str, wait_key: str) -> None:
    from i18n.core import format_int, t

    reader = {"springer": _springer_status, "lens": _lens_status, "mno": _mno_status}[source]
    now_running, now_done, now_total, err = reader()
    flag = f"_live_wait_{source}"
    if err:
        st.warning(t(f"{wait_key}.api_error", detail=str(err).replace("{", "(").replace("}", ")")))
    if now_running and now_total > 0:
        st.session_state[flag] = True
        shown = min(int(now_done), int(now_total))
        st.info(t(f"{wait_key}.bg_wait", done=format_int(shown), total=format_int(now_total)))
        st.progress(shown / max(int(now_total), 1))
        if source == "mno":
            seen = st.session_state.get("_mno_done_seen")
            if seen != shown:
                st.session_state["_mno_done_seen"] = shown
                if shown > 0:
                    st.rerun()
        return
    if st.session_state.pop(flag, False):
        st.rerun()


def _mno_status() -> Tuple[bool, int, int, str]:
    from backend.mno_pub_live import prefetch_status

    data = prefetch_status()
    return (
        bool(data.get("running")),
        int(data.get("done") or 0),
        int(data.get("total") or 0),
        str(data.get("error") or ""),
    )


def render_watch(source: str, wait_key: str) -> None:
    """Çalışırken 10 sn’de bir durum; bitince tek rerun. İlk boya ağ beklemez."""
    reader = {"springer": _springer_status, "lens": _lens_status, "mno": _mno_status}[source]
    running, _, _, _ = reader()
    flag = f"_live_wait_{source}"
    if not running and not st.session_state.get(flag):
        return
    if running:
        st.session_state[flag] = True
    _watch_fragment(source, wait_key)
