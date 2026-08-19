"""OpenAlex operatör yayın sayılarını disk önbelleğine yazar. Sayı uydurulmaz."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from backend.openalex_client import (  # noqa: E402
    CACHE_PATH,
    fetch_operator_work_count,
    operator_openalex_url,
)
from data.eu_operators import country_choices, operators_with_tt  # noqa: E402

# Bu oturumda api.openalex.org meta.count olarak okunan kurum ID sayımları.
SEED = {
    "FR:orange": ("institution", 27, ("I19370010",), ""),
    "DE:dt": ("institution", 8, ("I4210093367",), ""),
    "ES:telefonica": ("institution", 28, ("I4210134591",), ""),
    "IT:tim": ("institution", 8, ("I137543953",), ""),
    "GB:bt": ("institution", 9, ("I1332878012",), ""),
    "NL:kpn": ("institution", 0, ("I4210109701",), ""),
    "SE:telia_se": ("institution", 0, ("I170053871",), ""),
    "FI:elisa": ("institution", 0, ("I2801699569",), ""),
    "TR:turkcell": ("institution", 2, ("I4210154164",), ""),
    "TR:tt": ("institution", 5, ("I4210092500",), ""),
    "PL:orange_pl": ("institution", 15, ("I126469861",), ""),
    "AT:a1_at": ("institution", 0, ("I53472387",), ""),
    "DE:vodafone_de": ("institution", 8, ("I245417339",), ""),
    "GB:vodafone_uk": ("institution", 2, ("I74316835",), ""),
    "ES:vodafone_es": ("institution", 1, ("I2800993576",), ""),
    "IT:vodafone_it": ("institution", 1, ("I4210094608",), ""),
    "DE:telefonica_de": ("institution", 4, ("I4210099988",), ""),
    "FR:bouygues": ("institution", 4, ("I280199911",), ""),
    "FI:telia_fi": ("institution", 0, ("I4210163533",), ""),
    "RS:mts": ("institution", 1, ("I4210128241",), ""),
    "AT:magenta": ("institution", 2, ("I272033418",), ""),
}

# raw_affiliation_strings.search + ülke filtresi (aynı oturumda ölçülen meta.count)
AFFIL_SEED = {
    "FR:sfr": ("affiliation", 1, "SFR"),
    "IT:windtre": ("affiliation", 1, "Wind Tre"),
    "RO:orange_ro": ("affiliation", 4, "Orange Romania"),
    "SE:tele2": ("affiliation", 0, "Tele2"),
    "FI:dna": ("affiliation", 0, "DNA Oyj"),
    "NL:vziggo": ("affiliation", 0, "VodafoneZiggo"),
    "HU:magyar": ("affiliation", 0, "Magyar Telekom"),
    "RO:vodafone_ro": ("affiliation", 0, "Vodafone Romania"),
    "TR:vodafone_tr": ("affiliation", 0, "Vodafone Turkey"),
    "GB:vmo2": ("affiliation", 1, "O2 UK"),
}


def _load() -> dict:
    if CACHE_PATH.exists():
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    return {}


def _save(cache: dict) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    cache["fetched_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    cache["source_url"] = "https://openalex.org/works"
    CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def seed_known() -> None:
    cache = _load()
    stored = cache.get("operator_works") or {}
    for key, (source, count, ids, affil) in SEED.items():
        if key in stored:
            continue
        stored[key] = {
            "count": count,
            "source": source,
            "ids": list(ids),
            "affil": affil,
            "url": operator_openalex_url(inst_ids=ids, affil=affil, country_code=key.split(":")[0]),
        }
        print("seed", key, count, flush=True)
    for key, (source, count, affil) in AFFIL_SEED.items():
        if key in stored:
            continue
        stored[key] = {
            "count": count,
            "source": source,
            "ids": [],
            "affil": affil,
            "url": operator_openalex_url(affil=affil, country_code=key.split(":")[0]),
        }
        print("seed-affil", key, count, flush=True)
    cache["operator_works"] = stored
    _save(cache)


def refresh_all() -> None:
    seed_known()
    for country in country_choices():
        for op in operators_with_tt(country):
            key = f"{country['cc']}:{op['id']}"
            row = fetch_operator_work_count(
                key,
                inst_ids=tuple(op.get("oa_ids") or ()),
                affil_terms=tuple(op.get("oa_affil") or ()),
                country_code=country["cc"],
            )
            print(key, row.get("count") if row else None, row.get("source") if row else "FAIL", flush=True)


if __name__ == "__main__":
    refresh_all()
