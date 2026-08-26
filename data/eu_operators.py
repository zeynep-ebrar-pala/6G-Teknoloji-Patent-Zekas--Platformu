"""
Avrupa ülkesi başına kilitli üç MNO.
Abone/gelir «en yüksek 3» iddiası değildir: Wikipedia Avrupa MNO listesindeki
bu ülke girdilerinden kilitlendi. Patent sayısı kilitli örnek küme + Google Patents.
Yayın sayısı: Akademik Yayın Analizi Avrupa yüzünde Springer Meta metin
«6G {firma} {ülke}». Bağlılık facet değildir. TT bağlılıklı DOI kümesi ayrıdır.
"""

from __future__ import annotations

from typing import Any, Dict, List

EU_MNO_LIST_URL = "https://en.wikipedia.org/wiki/List_of_mobile_network_operators_of_Europe"

TT_OPERATOR = {
    "id": "tt",
    "name": "Türk Telekom",
    "search": "Turk Telekom",
    "patterns": ("türk telekom", "turk telekom", "turktelekom", "netsia"),
    "patents_url": "https://patents.google.com/?assignee=Netsia",
    "is_tt": True,
}


def _op(
    op_id: str,
    name: str,
    patterns: tuple[str, ...],
    patents_q: str,
    search: str | None = None,
) -> Dict[str, Any]:
    q = patents_q.replace(" ", "+")
    return {
        "id": op_id,
        "name": name,
        "search": (search or patents_q).strip(),
        "patterns": patterns,
        "patents_url": f"https://patents.google.com/?assignee={q}",
        "is_tt": op_id == "tt",
    }


EU_COUNTRY_MNOS: List[Dict[str, Any]] = [
    {
        "cc": "TR",
        "iso3": "TUR",
        "name_tr": "Türkiye",
        "name_en": "Türkiye",
        "operators": [
            _op("turkcell", "Turkcell", ("turkcell",), "Turkcell"),
            _op(
                "vodafone_tr",
                "Vodafone Türkiye",
                ("vodafone türkiye", "vodafone turkey", "vodafone telekomünikasyon"),
                "Vodafone Turkey",
            ),
            _op(
                "tt",
                "Türk Telekom",
                ("türk telekom", "turk telekom", "turktelekom", "netsia"),
                "Netsia",
                search="Turk Telekom",
            ),
        ],
    },
    {
        "cc": "DE",
        "iso3": "DEU",
        "name_tr": "Almanya",
        "name_en": "Germany",
        "operators": [
            _op(
                "dt",
                "Deutsche Telekom",
                ("deutsche telekom", "telekom deutschland"),
                "Deutsche Telekom",
            ),
            _op(
                "vodafone_de",
                "Vodafone Deutschland",
                ("vodafone gmbh", "vodafone deutschland", "vodafone germany"),
                "Vodafone Germany",
            ),
            _op(
                "telefonica_de",
                "Telefónica Deutschland",
                ("telefónica deutschland", "telefonica deutschland", "o2 germany", "o2 deutschland"),
                "Telefonica Deutschland",
            ),
        ],
    },
    {
        "cc": "FR",
        "iso3": "FRA",
        "name_tr": "Fransa",
        "name_en": "France",
        "operators": [
            _op("orange", "Orange", ("orange",), "Orange"),
            _op("sfr", "SFR", ("sfr", "altice france"), "SFR"),
            _op("bouygues", "Bouygues Telecom", ("bouygues",), "Bouygues Telecom"),
        ],
    },
    {
        "cc": "ES",
        "iso3": "ESP",
        "name_tr": "İspanya",
        "name_en": "Spain",
        "operators": [
            _op(
                "telefonica",
                "Telefónica",
                ("telefónica", "telefonica", "movistar"),
                "Telefonica",
            ),
            _op(
                "orange_es",
                "Orange España",
                ("orange espana", "orange españa", "orange spain"),
                "Orange Espana",
            ),
            _op(
                "vodafone_es",
                "Vodafone España",
                ("vodafone espana", "vodafone españa", "vodafone spain"),
                "Vodafone Spain",
            ),
        ],
    },
    {
        "cc": "IT",
        "iso3": "ITA",
        "name_tr": "İtalya",
        "name_en": "Italy",
        "operators": [
            _op(
                "tim",
                "TIM",
                ("telecom italia", "tim s.p.a", "tim spa"),
                "Telecom Italia",
            ),
            _op(
                "vodafone_it",
                "Vodafone Italia",
                ("vodafone italia", "vodafone italy"),
                "Vodafone Italia",
            ),
            _op(
                "windtre",
                "Wind Tre",
                ("wind tre", "windtre"),
                "Wind Tre",
            ),
        ],
    },
    {
        "cc": "GB",
        "iso3": "GBR",
        "name_tr": "Birleşik Krallık",
        "name_en": "United Kingdom",
        "operators": [
            _op(
                "bt",
                "BT Group / EE",
                ("bt group", "british telecom", "ee limited"),
                "BT Group",
            ),
            _op(
                "vodafone_uk",
                "Vodafone UK",
                ("vodafone uk", "vodafone limited"),
                "Vodafone UK",
            ),
            _op(
                "vmo2",
                "Virgin Media O2",
                ("virgin media", "vmo2", "telefónica uk", "telefonica uk", "o2 uk"),
                "Virgin Media O2",
            ),
        ],
    },
    {
        "cc": "SE",
        "iso3": "SWE",
        "name_tr": "İsveç",
        "name_en": "Sweden",
        "operators": [
            _op(
                "telia_se",
                "Telia",
                ("telia company", "telia sverige", "telia sweden"),
                "Telia",
            ),
            _op("tele2", "Tele2", ("tele2",), "Tele2"),
            _op(
                "telenor_se",
                "Telenor Sverige",
                ("telenor sverige", "telenor sweden"),
                "Telenor Sweden",
            ),
        ],
    },
    {
        "cc": "FI",
        "iso3": "FIN",
        "name_tr": "Finlandiya",
        "name_en": "Finland",
        "operators": [
            _op("elisa", "Elisa", ("elisa",), "Elisa"),
            _op("dna", "DNA", ("dna oyj", "dna plc"), "DNA Oyj"),
            _op(
                "telia_fi",
                "Telia Finland",
                ("telia finland", "telia finnish"),
                "Telia Finland",
            ),
        ],
    },
    {
        "cc": "NL",
        "iso3": "NLD",
        "name_tr": "Hollanda",
        "name_en": "Netherlands",
        "operators": [
            _op("kpn", "KPN", ("kpn",), "KPN"),
            _op(
                "vziggo",
                "VodafoneZiggo",
                ("vodafoneziggo", "vodafone ziggo"),
                "VodafoneZiggo",
            ),
            _op(
                "odido",
                "Odido",
                ("odido", "t-mobile netherlands"),
                "Odido",
            ),
        ],
    },
    {
        "cc": "HU",
        "iso3": "HUN",
        "name_tr": "Macaristan",
        "name_en": "Hungary",
        "operators": [
            _op(
                "magyar",
                "Magyar Telekom",
                ("magyar telekom",),
                "Magyar Telekom",
            ),
            _op(
                "yettel_hu",
                "Yettel Hungary",
                ("yettel hungary", "yettel magyar"),
                "Yettel Hungary",
            ),
            _op(
                "vodafone_hu",
                "Vodafone Hungary",
                ("vodafone hungary", "vodafone magyar"),
                "Vodafone Hungary",
            ),
        ],
    },
    {
        "cc": "RO",
        "iso3": "ROU",
        "name_tr": "Romanya",
        "name_en": "Romania",
        "operators": [
            _op(
                "orange_ro",
                "Orange Romania",
                ("orange romania", "orange românia"),
                "Orange Romania",
            ),
            _op(
                "vodafone_ro",
                "Vodafone Romania",
                ("vodafone romania",),
                "Vodafone Romania",
            ),
            _op(
                "digi",
                "Digi",
                ("digi communications", "rcs rds", "digi romania"),
                "Digi Romania",
            ),
        ],
    },
    {
        "cc": "BG",
        "iso3": "BGR",
        "name_tr": "Bulgaristan",
        "name_en": "Bulgaria",
        "operators": [
            _op(
                "a1_bg",
                "A1 Bulgaria",
                ("a1 bulgaria", "a1 bulgar"),
                "A1 Bulgaria",
            ),
            _op(
                "yettel_bg",
                "Yettel Bulgaria",
                ("yettel bulgaria",),
                "Yettel Bulgaria",
            ),
            _op("vivacom", "Vivacom", ("vivacom",), "Vivacom"),
        ],
    },
    {
        "cc": "RS",
        "iso3": "SRB",
        "name_tr": "Sırbistan",
        "name_en": "Serbia",
        "operators": [
            _op(
                "mts",
                "Telekom Srbija",
                ("telekom srbija", "telekom srbije"),
                "Telekom Srbija",
            ),
            _op(
                "yettel_rs",
                "Yettel Serbia",
                ("yettel serbia", "yettel srbija"),
                "Yettel Serbia",
            ),
            _op(
                "a1_rs",
                "A1 Srbija",
                ("a1 srbija", "a1 serbia"),
                "A1 Serbia",
            ),
        ],
    },
    {
        "cc": "UA",
        "iso3": "UKR",
        "name_tr": "Ukrayna",
        "name_en": "Ukraine",
        "operators": [
            _op("kyivstar", "Kyivstar", ("kyivstar",), "Kyivstar"),
            _op(
                "vodafone_ua",
                "Vodafone Ukraine",
                ("vodafone ukraine",),
                "Vodafone Ukraine",
            ),
            _op("lifecell", "lifecell", ("lifecell",), "lifecell"),
        ],
    },
    {
        "cc": "AT",
        "iso3": "AUT",
        "name_tr": "Avusturya",
        "name_en": "Austria",
        "operators": [
            _op(
                "a1_at",
                "A1 Telekom Austria",
                ("a1 telekom", "telekom austria"),
                "A1 Telekom Austria",
            ),
            _op(
                "magenta",
                "Magenta Telekom",
                ("magenta telekom", "t-mobile austria"),
                "Magenta Telekom",
            ),
            _op(
                "drei",
                "Drei",
                ("hutchison drei", "3 austria"),
                "Hutchison Drei",
            ),
        ],
    },
    {
        "cc": "PL",
        "iso3": "POL",
        "name_tr": "Polonya",
        "name_en": "Poland",
        "operators": [
            _op(
                "orange_pl",
                "Orange Polska",
                ("orange polska", "orange poland"),
                "Orange Polska",
            ),
            _op(
                "play",
                "Play",
                ("p4 play", "play poland"),
                "Play Poland",
            ),
            _op(
                "plus",
                "Plus",
                ("polkomtel", "plus poland"),
                "Plus Poland",
            ),
        ],
    },
]


def country_choices() -> List[Dict[str, Any]]:
    return list(EU_COUNTRY_MNOS)


def countries_for_region(region: str) -> List[Dict[str, Any]]:
    """tr → Türkiye MNO’ları; eu → diğer Avrupa; both → hepsi."""
    code = (region or "both").lower()
    if code == "tr":
        return [row for row in EU_COUNTRY_MNOS if row["cc"] == "TR"]
    if code == "eu":
        return [row for row in EU_COUNTRY_MNOS if row["cc"] != "TR"]
    return list(EU_COUNTRY_MNOS)


def country_by_cc(cc: str) -> Dict[str, Any] | None:
    code = (cc or "").upper()
    return next((row for row in EU_COUNTRY_MNOS if row["cc"] == code), None)


def operators_with_tt(country: Dict[str, Any]) -> List[Dict[str, Any]]:
    ops = [dict(op) for op in country["operators"]]
    if not any(op.get("is_tt") or op["id"] == "tt" for op in ops):
        ops.append(dict(TT_OPERATOR))
    else:
        for op in ops:
            if op["id"] == "tt":
                op["is_tt"] = True
    return ops


def name_matches(inst_name: str, patterns: tuple[str, ...]) -> bool:
    text = (inst_name or "").lower()
    return any(p.lower() in text for p in patterns)
