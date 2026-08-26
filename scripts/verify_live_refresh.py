#!/usr/bin/env python3
"""Lens + Springer canlı yenilemenin doğru sonuç verdiğini ölçer. Anahtar basılmaz."""

from __future__ import annotations

import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _ok(name: str, cond: bool, detail: str = "") -> bool:
    mark = "PASS" if cond else "FAIL"
    extra = f" — {detail}" if detail else ""
    print(f"[{mark}] {name}{extra}")
    return cond


def main() -> int:
    from backend.config import get_lens_token, get_springer_api_key, reload_env
    from backend.patent_apis import _lens_count, lens_explorer_dsl, peek_lens_count
    from backend.publisher_apis import _q6g, _springer_count, peek_springer_count
    from backend.springer_live import TOPIC_ORDER, ensure_prefetch, live_topic_row, load_live, prefetch_status
    from backend.years import should_refresh, span_label, year_window

    reload_env()
    failed = 0

    y0, y1 = year_window()
    if not _ok("year window includes current year", y0 == 2020 and y1 >= 2026, span_label()):
        failed += 1

    live = load_live()
    fetched = str(live.get("fetched_at") or "")
    complete = all(isinstance((live.get("topics") or {}).get(n, {}).get("total"), int) for n in TOPIC_ORDER)
    want = should_refresh(complete=complete, fetched_at=fetched, force=True)
    if not _ok("stale cache must refresh on visit", want, f"fetched_at={fetched or 'none'}"):
        failed += 1

    springer_key = bool(get_springer_api_key())
    lens_key = bool(get_lens_token())
    _ok("SPRINGER_API_KEY present", springer_key)
    _ok("LENS_TOKEN present", lens_key)
    if not springer_key:
        print("SKIP live Springer API (no key)")
        failed += 1
    if not lens_key:
        print("SKIP live Lens API (no token)")
        failed += 1

    t0 = time.perf_counter()
    cached_isac = peek_springer_count(_q6g("ISAC"), None)
    peek_ms = (time.perf_counter() - t0) * 1000
    if not _ok("Springer peek is disk-only and fast", peek_ms < 500, f"{peek_ms:.0f} ms, n={cached_isac}"):
        failed += 1

    t0 = time.perf_counter()
    cached_lens = peek_lens_count(lens_explorer_dsl())
    peek_ms = (time.perf_counter() - t0) * 1000
    if not _ok("Lens peek is disk-only and fast", peek_ms < 500, f"{peek_ms:.0f} ms, n={cached_lens}"):
        failed += 1

    if springer_key:
        disk_row = live_topic_row("ISAC")
        disk_n = disk_row.get("total") if isinstance(disk_row.get("total"), int) else cached_isac
        t0 = time.perf_counter()
        live_n = _springer_count(_q6g("ISAC"), None, force=True)
        api_s = time.perf_counter() - t0
        if not _ok("Springer Meta returns an integer total", isinstance(live_n, int), f"{live_n} in {api_s:.1f}s"):
            failed += 1
        elif isinstance(disk_n, int):
            # Yeni yıl kayıtları toplamı küçültmez; eşit veya artar. API dalgalanması için %5 tolerans.
            if not _ok(
                "Springer live total is not a frozen drop",
                live_n >= int(disk_n * 0.95),
                f"disk={disk_n} live={live_n}",
            ):
                failed += 1
        t0 = time.perf_counter()
        ensure_prefetch(force=True)
        kick_ms = (time.perf_counter() - t0) * 1000
        st = prefetch_status()
        if not _ok(
            "Springer prefetch does not block the UI thread",
            kick_ms < 800,
            f"{kick_ms:.0f} ms, running={st.get('running')}",
        ):
            failed += 1

    if lens_key:
        dsl = lens_explorer_dsl()
        t0 = time.perf_counter()
        live_lens = _lens_count(dsl, force=True)
        api_s = time.perf_counter() - t0
        if not _ok("Lens patent/search returns an integer total", isinstance(live_lens, int), f"{live_lens} in {api_s:.1f}s"):
            failed += 1
        elif isinstance(cached_lens, int):
            if not _ok(
                "Lens live total is not a frozen drop",
                live_lens >= int(cached_lens * 0.95),
                f"disk={cached_lens} live={live_lens}",
            ):
                failed += 1

        from backend.patent_prefetch import ensure_prefetch as lens_prefetch, snapshot
        from data.patents import SPEC_COMPANIES

        t0 = time.perf_counter()
        lens_prefetch(None, tuple(SPEC_COMPANIES), force=True)
        kick_ms = (time.perf_counter() - t0) * 1000
        snap = snapshot(None, tuple(SPEC_COMPANIES))
        if not _ok(
            "Lens prefetch does not block the UI thread",
            kick_ms < 800,
            f"{kick_ms:.0f} ms, running={snap.get('running')}",
        ):
            failed += 1

    print("RESULT", "OK" if failed == 0 else f"{failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
