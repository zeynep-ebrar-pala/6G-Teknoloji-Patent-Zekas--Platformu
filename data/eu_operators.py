"""
Avrupa ülkesi başına kilitli üç MNO.
Abone/gelir «en yüksek 3» iddiası değildir: Wikipedia Avrupa MNO listesindeki
bu ülke girdilerinden kilitlendi. Yayın sayısı OpenAlex kurum kimliği / bağlılık
sorgusudur. Patent sayısı kilitli örnek küme + Google Patents doğrulama linki.
OpenAlex kurum ID’leri api.openalex.org/institutions canlı yanıtından kilitlendi.
"""

from __future__ import annotations

from typing import Any, Dict, List

EU_MNO_LIST_URL = "https://en.wikipedia.org/wiki/List_of_mobile_network_operators_of_Europe"

TT_OPERATOR = {
    "id": "tt",
    "name": "Türk Telekom",
    "patterns": ("türk telekom", "turk telekom", "turktelekom", "netsia"),
    "patents_url": "https://patents.google.com/?assignee=Netsia",
    "is_tt": True,
    "oa_ids": ("I4210092500",),
    "oa_affil": (),
}


def _op(
    op_id: str,
    name: str,
    patterns: tuple[str, ...],
    patents_q: str,
    *,
    oa_ids: tuple[str, ...] = (),
    oa_affil: tuple[str, ...] = (),
) -> Dict[str, Any]:
    q = patents_q.replace(" ", "+")
    return {
        "id": op_id,
        "name": name,
        "patterns": patterns,
        "patents_url": f"https://patents.google.com/?assignee={q}",
        "is_tt": False,
        "oa_ids": oa_ids,
        "oa_affil": oa_affil,
    }


EU_COUNTRY_MNOS: List[Dict[str, Any]] = [
    {
        "cc": "TR",
        "iso3": "TUR",
        "name_tr": "Türkiye",
        "name_en": "Türkiye",
        "operators": [
            _op("turkcell", "Turkcell", ("turkcell",), "Turkcell", oa_ids=("I4210154164",)),
            _op(
                "vodafone_tr",
                "Vodafone Türkiye",
                ("vodafone türkiye", "vodafone turkey", "vodafone telekomünikasyon"),
                "Vodafone Turkey",
                oa_affil=("Vodafone Turkey", "Vodafone Türkiye"),
            ),
            _op(
                "tt",
                "Türk Telekom",
                ("türk telekom", "turk telekom", "turktelekom", "netsia"),
                "Netsia",
                oa_ids=("I4210092500",),
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
                oa_ids=("I4210093367",),
            ),
            _op(
                "vodafone_de",
                "Vodafone Deutschland",
                ("vodafone gmbh", "vodafone deutschland", "vodafone germany"),
                "Vodafone Germany",
                oa_ids=("I245417339",),
            ),
            _op(
                "telefonica_de",
                "Telefónica Deutschland",
                ("telefónica deutschland", "telefonica deutschland", "o2 germany", "o2 deutschland"),
                "Telefonica Deutschland",
                oa_ids=("I4210099988",),
            ),
        ],
    },
    {
        "cc": "FR",
        "iso3": "FRA",
        "name_tr": "Fransa",
        "name_en": "France",
        "operators": [
            _op("orange", "Orange", ("orange",), "Orange", oa_ids=("I19370010",)),
            _op("sfr", "SFR", ("sfr", "altice france"), "SFR", oa_affil=("SFR",)),
            _op("bouygues", "Bouygues Telecom", ("bouygues",), "Bouygues Telecom", oa_ids=("I280199911",)),
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
                oa_ids=("I4210134591",),
            ),
            _op(
                "orange_es",
                "Orange España",
                ("orange espana", "orange españa", "orange spain"),
                "Orange Espana",
                oa_affil=("Orange España", "Orange Spain"),
            ),
            _op(
                "vodafone_es",
                "Vodafone España",
                ("vodafone espana", "vodafone españa", "vodafone spain"),
                "Vodafone Spain",
                oa_ids=("I2800993576",),
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
                oa_ids=("I137543953",),
            ),
            _op(
                "vodafone_it",
                "Vodafone Italia",
                ("vodafone italia", "vodafone italy"),
                "Vodafone Italia",
                oa_ids=("I4210094608",),
            ),
            _op(
                "windtre",
                "Wind Tre",
                ("wind tre", "windtre"),
                "Wind Tre",
                oa_affil=("Wind Tre",),
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
                oa_ids=("I1332878012",),
            ),
            _op(
                "vodafone_uk",
                "Vodafone UK",
                ("vodafone uk", "vodafone limited"),
                "Vodafone UK",
                oa_ids=("I74316835",),
            ),
            _op(
                "vmo2",
                "Virgin Media O2",
                ("virgin media", "vmo2", "telefónica uk", "telefonica uk", "o2 uk"),
                "Virgin Media O2",
                oa_affil=("Virgin Media", "Telefonica UK", "O2 UK"),
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
                oa_ids=("I170053871",),
            ),
            _op("tele2", "Tele2", ("tele2",), "Tele2", oa_affil=("Tele2",)),
            _op(
                "telenor_se",
                "Telenor Sverige",
                ("telenor sverige", "telenor sweden"),
                "Telenor Sweden",
                oa_affil=("Telenor Sverige", "Telenor Sweden"),
            ),
        ],
    },
    {
        "cc": "FI",
        "iso3": "FIN",
        "name_tr": "Finlandiya",
        "name_en": "Finland",
        "operators": [
            _op("elisa", "Elisa", ("elisa",), "Elisa", oa_ids=("I2801699569",)),
            _op("dna", "DNA", ("dna oyj", "dna plc"), "DNA Oyj", oa_affil=("DNA Oyj", "DNA Plc")),
            _op(
                "telia_fi",
                "Telia Finland",
                ("telia finland", "telia finnish"),
                "Telia Finland",
                oa_ids=("I4210163533",),
            ),
        ],
    },
    {
        "cc": "NL",
        "iso3": "NLD",
        "name_tr": "Hollanda",
        "name_en": "Netherlands",
        "operators": [
            _op("kpn", "KPN", ("kpn",), "KPN", oa_ids=("I4210109701",)),
            _op(
                "vziggo",
                "VodafoneZiggo",
                ("vodafoneziggo", "vodafone ziggo"),
                "VodafoneZiggo",
                oa_affil=("VodafoneZiggo", "Vodafone Ziggo"),
            ),
            _op(
                "odido",
                "Odido",
                ("odido", "t-mobile netherlands"),
                "Odido",
                oa_affil=("Odido", "T-Mobile Netherlands"),
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
                oa_affil=("Magyar Telekom",),
            ),
            _op(
                "yettel_hu",
                "Yettel Hungary",
                ("yettel hungary", "yettel magyar"),
                "Yettel Hungary",
                oa_affil=("Yettel Hungary",),
            ),
            _op(
                "vodafone_hu",
                "Vodafone Hungary",
                ("vodafone hungary", "vodafone magyar"),
                "Vodafone Hungary",
                oa_affil=("Vodafone Hungary",),
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
                oa_affil=("Orange Romania", "Orange România"),
            ),
            _op(
                "vodafone_ro",
                "Vodafone Romania",
                ("vodafone romania",),
                "Vodafone Romania",
                oa_affil=("Vodafone Romania",),
            ),
            _op(
                "digi",
                "Digi",
                ("digi communications", "rcs rds", "digi romania"),
                "Digi Romania",
                oa_affil=("Digi Romania", "RCS RDS"),
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
                oa_affil=("A1 Bulgaria",),
            ),
            _op(
                "yettel_bg",
                "Yettel Bulgaria",
                ("yettel bulgaria",),
                "Yettel Bulgaria",
                oa_affil=("Yettel Bulgaria",),
            ),
            _op("vivacom", "Vivacom", ("vivacom",), "Vivacom", oa_affil=("Vivacom",)),
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
                oa_ids=("I4210128241",),
            ),
            _op(
                "yettel_rs",
                "Yettel Serbia",
                ("yettel serbia", "yettel srbija"),
                "Yettel Serbia",
                oa_affil=("Yettel Serbia",),
            ),
            _op(
                "a1_rs",
                "A1 Srbija",
                ("a1 srbija", "a1 serbia"),
                "A1 Serbia",
                oa_affil=("A1 Srbija", "A1 Serbia"),
            ),
        ],
    },
    {
        "cc": "UA",
        "iso3": "UKR",
        "name_tr": "Ukrayna",
        "name_en": "Ukraine",
        "operators": [
            _op("kyivstar", "Kyivstar", ("kyivstar",), "Kyivstar", oa_affil=("Kyivstar",)),
            _op(
                "vodafone_ua",
                "Vodafone Ukraine",
                ("vodafone ukraine",),
                "Vodafone Ukraine",
                oa_affil=("Vodafone Ukraine",),
            ),
            _op("lifecell", "lifecell", ("lifecell",), "lifecell", oa_affil=("lifecell",)),
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
                oa_ids=("I53472387",),
            ),
            _op(
                "magenta",
                "Magenta Telekom",
                ("magenta telekom", "t-mobile austria"),
                "Magenta Telekom",
                oa_ids=("I272033418",),
            ),
            _op(
                "drei",
                "Drei",
                ("hutchison drei", "3 austria"),
                "Hutchison Drei",
                oa_affil=("Hutchison Drei", "Drei Austria"),
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
                oa_ids=("I126469861",),
            ),
            _op(
                "play",
                "Play",
                ("p4 play", "play poland"),
                "Play Poland",
                oa_affil=("Play Poland", "P4 Sp"),
            ),
            _op(
                "plus",
                "Plus",
                ("polkomtel", "plus poland"),
                "Plus Poland",
                oa_affil=("Polkomtel",),
            ),
        ],
    },
]


def country_choices() -> List[Dict[str, Any]]:
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
                op.setdefault("oa_ids", TT_OPERATOR["oa_ids"])
                op.setdefault("oa_affil", TT_OPERATOR["oa_affil"])
    return ops


def name_matches(inst_name: str, patterns: tuple[str, ...]) -> bool:
    text = (inst_name or "").lower()
    return any(p.lower() in text for p in patterns)
