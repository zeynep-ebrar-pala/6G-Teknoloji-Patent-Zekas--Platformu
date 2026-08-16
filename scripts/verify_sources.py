#!/usr/bin/env python3
"""Patent ve makale source_url doğrulama scripti."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import urllib.error
import urllib.request

from backend.data_validator import load_validated_patents, load_validated_papers
from data.academic import MOST_CITED_PAPERS
from data.patents import VERIFIED_PATENTS

USER_AGENT = "6G-Patent-Platform-Verify/1.0"


def check_url(url: str, timeout: int = 15) -> tuple[bool, str]:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            code = resp.getcode()
            if code and code < 400:
                return True, f"HTTP {code}"
            return False, f"HTTP {code}"
    except urllib.error.HTTPError as e:
        if e.code in (405, 403):
            req_get = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            try:
                with urllib.request.urlopen(req_get, timeout=timeout) as resp:
                    return resp.getcode() < 400, f"HTTP {resp.getcode()} (GET fallback)"
            except Exception as ex:
                return False, str(ex)
        return False, f"HTTP {e.code}"
    except Exception as e:
        return False, str(e)


def main() -> int:
    failed = 0
    print("=== Patent URL Doğrulama ===")
    patents = load_validated_patents(VERIFIED_PATENTS)
    print(f"Doğrulanmış patent: {len(patents)} / {len(VERIFIED_PATENTS)}")
    for p in patents:
        ok, msg = check_url(p["source_url"])
        status = "OK" if ok else "FAIL"
        print(f"  [{status}] {p['publication_number']} — {msg}")
        if not ok:
            failed += 1

    print("\n=== Makale URL Doğrulama ===")
    papers = load_validated_papers(MOST_CITED_PAPERS)
    print(f"Doğrulanmış makale: {len(papers)} / {len(MOST_CITED_PAPERS)}")
    for paper in papers:
        ok, msg = check_url(paper["source_url"])
        status = "OK" if ok else "FAIL"
        print(f"  [{status}] {paper['doi']} — {msg}")
        if not ok:
            failed += 1

    print(f"\nToplam hata: {failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
