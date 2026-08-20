"""
WoS (Web of Science — Web of Science) Core Collection UT (Unique Identifier — benzersiz kayıt no).
Yalnız tarayıcıda açılmış tam kayıttan alınan numaralar. HTML kazınmaz; sayı uydurulmaz.
"""

from __future__ import annotations

# DOI → WOS:accession. Anahtar küçük harf.
WOS_UT_BY_DOI = {
    "10.1109/access.2026.3691411": "WOS:001767283200006",
    "10.1109/jsac.2022.3156632": "WOS:000797418900005",
    "10.1109/ojcoms.2020.3010270": "WOS:000723372400065",
    "10.1109/jiot.2023.3235618": "WOS:001018925700001",
    "10.1109/jsac.2020.3007211": "WOS:000579341000002",
    "10.1109/comst.2021.3075437": "WOS:000688449200005",
    "10.1007/s11432-020-2955-4": "WOS:000597333100001",
    "10.1109/ojcoms.2021.3057679": "WOS:001101785300001",
    "10.1109/mnet.011.2000493": "WOS:000638250600035",
    "10.1109/comst.2023.3239220": "WOS:001001620300015",
    "10.1109/access.2020.3010896": "WOS:000554362600001",
    "10.1109/jproc.2022.3169622": "WOS:000791718500001",
}


def ut_for_doi(doi: str) -> str:
    key = (doi or "").strip().lower()
    key = key.removeprefix("https://doi.org/").removeprefix("http://doi.org/")
    return WOS_UT_BY_DOI.get(key) or ""
