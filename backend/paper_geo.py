"""
Yazar bağlılığından ülke kodu.
Bağlılık yoksa ülke uydurulmaz.
"""

from __future__ import annotations

import re
from typing import Any, Dict, Iterable, List, Sequence

EU_AFFIL: Dict[str, str] = {
    "DE": "Germany",
    "FR": "France",
    "IT": "Italy",
    "ES": "Spain",
    "GB": "United Kingdom",
    "FI": "Finland",
    "SE": "Sweden",
    "NL": "Netherlands",
    "BE": "Belgium",
    "AT": "Austria",
    "CH": "Switzerland",
    "NO": "Norway",
    "DK": "Denmark",
    "PL": "Poland",
    "PT": "Portugal",
    "GR": "Greece",
    "IE": "Ireland",
    "CZ": "Czech Republic",
    "HU": "Hungary",
    "RO": "Romania",
    "BG": "Bulgaria",
    "HR": "Croatia",
    "SK": "Slovakia",
    "SI": "Slovenia",
    "LT": "Lithuania",
    "LV": "Latvia",
    "EE": "Estonia",
    "LU": "Luxembourg",
    "MT": "Malta",
    "CY": "Cyprus",
    "IS": "Iceland",
}

EU_CCS = frozenset(EU_AFFIL.keys())

_ALIASES: Dict[str, str] = {
    "GERMANY": "DE",
    "DEUTSCHLAND": "DE",
    "FRANCE": "FR",
    "ITALY": "IT",
    "ITALIA": "IT",
    "SPAIN": "ES",
    "ESPANA": "ES",
    "ESPAÑA": "ES",
    "UNITED KINGDOM": "GB",
    "GREAT BRITAIN": "GB",
    "ENGLAND": "GB",
    "SCOTLAND": "GB",
    "WALES": "GB",
    "NORTHERN IRELAND": "GB",
    "UK": "GB",
    "FINLAND": "FI",
    "SUOMI": "FI",
    "SWEDEN": "SE",
    "SVERIGE": "SE",
    "NETHERLANDS": "NL",
    "HOLLAND": "NL",
    "THE NETHERLANDS": "NL",
    "BELGIUM": "BE",
    "BELGIQUE": "BE",
    "BELGIE": "BE",
    "AUSTRIA": "AT",
    "OSTERREICH": "AT",
    "ÖSTERREICH": "AT",
    "SWITZERLAND": "CH",
    "SCHWEIZ": "CH",
    "SUISSE": "CH",
    "NORWAY": "NO",
    "NORGE": "NO",
    "DENMARK": "DK",
    "DANMARK": "DK",
    "POLAND": "PL",
    "POLSKA": "PL",
    "PORTUGAL": "PT",
    "GREECE": "GR",
    "HELLAS": "GR",
    "IRELAND": "IE",
    "EIRE": "IE",
    "CZECH REPUBLIC": "CZ",
    "CZECHIA": "CZ",
    "HUNGARY": "HU",
    "ROMANIA": "RO",
    "BULGARIA": "BG",
    "CROATIA": "HR",
    "SLOVAKIA": "SK",
    "SLOVENIA": "SI",
    "LITHUANIA": "LT",
    "LATVIA": "LV",
    "ESTONIA": "EE",
    "LUXEMBOURG": "LU",
    "MALTA": "MT",
    "CYPRUS": "CY",
    "ICELAND": "IS",
}

_NAME_TO_CC: Dict[str, str] = {**_ALIASES, **{v.upper(): k for k, v in EU_AFFIL.items()}}
_NAME_RE = re.compile(
    r"\b(" + "|".join(re.escape(n) for n in sorted(_NAME_TO_CC, key=len, reverse=True)) + r")\b",
    re.I,
)


def _norm_names(values: Iterable[Any]) -> List[str]:
    out: List[str] = []
    for raw in values:
        if isinstance(raw, dict):
            text = str(raw.get("name") or raw.get("value") or "").strip()
        else:
            text = str(raw or "").strip()
        if text:
            out.append(text)
    return out


def affiliation_ccs(names: Sequence[Any] | None) -> List[str]:
    """Bağlılık metnindeki Avrupa ülke kodları. Eşleşme yoksa boş liste."""
    found: List[str] = []
    seen = set()
    blob = " | ".join(_norm_names(names or []))
    if not blob:
        return []
    for match in _NAME_RE.finditer(blob):
        cc = _NAME_TO_CC.get(match.group(1).upper())
        if cc in EU_CCS and cc not in seen:
            seen.add(cc)
            found.append(cc)
    return found


def paper_ccs(paper: Dict[str, Any]) -> List[str]:
    stored = paper.get("ccs")
    if isinstance(stored, list) and stored and all(isinstance(x, str) for x in stored):
        return [x for x in stored if x in EU_CCS]
    return affiliation_ccs(paper.get("affiliations") or [])


def paper_from_europe(paper: Dict[str, Any]) -> bool:
    return bool(paper_ccs(paper))
