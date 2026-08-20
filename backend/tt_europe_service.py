"""
Türk Telekom Avrupa izi — doğrulanmış kayıtları UI ve grafik için hazırlar.
"""

from __future__ import annotations

from collections import Counter
from typing import Any, Dict, List, Optional

import streamlit as st

from backend.data_validator import load_validated_papers, load_validated_patents
from data.eu_operators import (
    EU_MNO_LIST_URL,
    country_by_cc,
    country_choices,
    name_matches,
    operators_with_tt,
)
from data.patents import VERIFIED_PATENTS
from data.tt_europe import (
    TT_AFFILIATED_PAPERS,
    TT_COUNTRY_COLORS,
    TT_EUROPE_SOURCE,
    TT_EUROPE_TOUCHPOINTS,
    TT_GROUP_PATENTS,
    TT_IR_2024_URL,
    TT_IR_WHOLESALE,
    TT_MAP_RD,
    TT_PRESS_CLAIMS,
    TTI_ABOUT_URL,
    TTI_WHOLESALE_FIRST_MOVER,
)


def _patents() -> List[Dict[str, Any]]:
    return load_validated_patents(TT_GROUP_PATENTS)


def _papers() -> List[Dict[str, Any]]:
    validated = load_validated_papers(TT_AFFILIATED_PAPERS)
    raw_by_doi = {p["doi"].lower(): p for p in TT_AFFILIATED_PAPERS}
    out = []
    for p in validated:
        extra = raw_by_doi.get(p["doi"].lower()) or {}
        merged = dict(p)
        merged["affiliation_country"] = extra.get("affiliation_country") or "TR"
        merged["note"] = extra.get("note") or ""
        merged["wos_ut"] = extra.get("wos_ut") or ""
        out.append(merged)
    return out


class TTEuropeService:
    @staticmethod
    def get_source() -> str:
        return TT_EUROPE_SOURCE

    @staticmethod
    def get_patents() -> List[Dict[str, Any]]:
        patents = _patents()
        return sorted(
            patents,
            key=lambda p: (
                -int(p.get("year") or 0),
                str(p.get("publication_number") or p.get("id") or ""),
            ),
        )

    @staticmethod
    def get_papers() -> List[Dict[str, Any]]:
        papers = _papers()
        enriched = []
        for paper in papers:
            merged = dict(paper)
            merged["citations"] = paper.get("citations")
            merged["citations_live"] = False
            enriched.append(merged)

        def _paper_sort(p: Dict[str, Any]) -> tuple:
            cites = p.get("citations")
            return (-int(p.get("year") or 0), -(cites if isinstance(cites, int) else -1))

        return sorted(enriched, key=_paper_sort)

    @staticmethod
    def ranked_countries() -> List[Dict[str, Any]]:
        return country_choices()

    @staticmethod
    def country_rank(cc: str, include_pubs: bool = True) -> Dict[str, Any]:
        """Kilitli 3 MNO + TT. Yayın: kilitli DOI (TT bağlılığı). Patent: kilitli örnek."""
        from backend.source_links import ieee_text_search_url

        country = country_by_cc(cc)
        if not country:
            return {"ok": False, "cc": cc}
        ops = operators_with_tt(country)
        sample_patents = load_validated_patents(VERIFIED_PATENTS) + _patents()
        ranked: List[Dict[str, Any]] = []
        pub_any = False
        for op in ops:
            patterns = tuple(op["patterns"])
            pub_n = 0
            pub_resolved = False
            pub_hits: List[str] = []
            if include_pubs and op.get("is_tt"):
                pub_n = sum(
                    1
                    for p in _papers()
                    if (p.get("affiliation_country") or "").upper() == country["cc"]
                )
                pub_resolved = True
                pub_any = pub_any or pub_n > 0
                if pub_n:
                    pub_hits = ["DOI-locked TT affiliation (this country)"]
            pat_n = 0
            pat_ids: List[str] = []
            for pat in sample_patents:
                if name_matches(pat.get("assignee") or "", patterns):
                    if op.get("is_tt") and country["cc"] != "TR":
                        continue
                    pat_n += 1
                    pat_ids.append(pat.get("publication_number") or pat.get("id") or "")
            ranked.append(
                {
                    "id": op["id"],
                    "name": op["name"],
                    "is_tt": bool(op.get("is_tt")),
                    "pub_n": pub_n,
                    "pub_resolved": pub_resolved,
                    "pat_n": pat_n,
                    "pub_hits": pub_hits[:3],
                    "pat_ids": pat_ids,
                    "patents_url": op["patents_url"],
                    "pub_search_url": ieee_text_search_url(f"6G {op['name']} {country['name_en']}"),
                }
            )

        def _with_rank(rows: List[Dict[str, Any]], key: str, dest: str) -> None:
            # 0 kayıt = sıra yok. 0 ile «2. sıra» yazmak Fransa/İspanya’da yanıltır.
            ordered = sorted(rows, key=lambda r: int(r[key] or 0), reverse=True)
            rank = 0
            prev = None
            seen = 0
            for row in ordered:
                val = int(row[key] or 0)
                if val == 0:
                    row[dest] = None
                    continue
                seen += 1
                if prev is None or val != prev:
                    rank = seen
                    prev = val
                row[dest] = rank

        _with_rank(ranked, "pub_n", "pub_rank")
        _with_rank(ranked, "pat_n", "pat_rank")
        tt_row = next((r for r in ranked if r["is_tt"]), None)
        return {
            "ok": True,
            "cc": country["cc"],
            "name_tr": country["name_tr"],
            "name_en": country["name_en"],
            "mno_source": EU_MNO_LIST_URL,
            "pub_search_url": ieee_text_search_url(f"6G {country['name_en']}"),
            "pub_ok": pub_any,
            "rows": ranked,
            "tt_pub_rank": None if not tt_row else tt_row["pub_rank"],
            "tt_pat_rank": None if not tt_row else tt_row["pat_rank"],
            "field_n": len(ranked),
        }

    @staticmethod
    def europe_overview(include_pubs: bool = True) -> List[Dict[str, Any]]:
        """Kilitli ülkelerin tamamı. Patent sekmesi include_pubs=False."""
        return _europe_overview_cached(include_pubs)

    @staticmethod
    def europe_position(include_pubs: bool = True) -> Dict[str, Any]:
        """TT'nin bu platformdaki ölçülen Avrupa yeri. Uydurma sıra yok."""
        overview = TTEuropeService.europe_overview(include_pubs=include_pubs)
        tr = next((r for r in overview if r["cc"] == "TR"), {})
        offices = TTEuropeService.office_counts()
        pub_out = [r for r in overview if r["cc"] != "TR" and int(r.get("tt_pub_n") or 0) > 0]
        pat_out = [r for r in overview if r["cc"] != "TR" and int(r.get("tt_pat_n") or 0) > 0]
        leaders = [
            {
                "cc": r["cc"],
                "name_tr": r["name_tr"],
                "name_en": r["name_en"],
                "lead": r.get("pub_lead"),
                "n": int(r.get("pub_lead_n") or 0),
            }
            for r in overview
            if r["cc"] != "TR" and int(r.get("pub_lead_n") or 0) > 0
        ]
        leaders.sort(key=lambda r: (-int(r["n"]), r["cc"]))
        return {
            "tr_pub_n": int(tr.get("tt_pub_n") or 0),
            "tr_pub_rank": tr.get("tt_pub_rank"),
            "tr_pat_n": int(tr.get("tt_pat_n") or 0),
            "tr_pat_rank": tr.get("tt_pat_rank"),
            "ep_n": int(offices.get("EP") or 0),
            "us_n": int(offices.get("US") or 0),
            "pub_outside_tr": len(pub_out),
            "pat_outside_tr": len(pat_out),
            "europe_pub_leaders": leaders,
        }

    @staticmethod
    def get_touchpoints() -> List[Dict[str, Any]]:
        return sorted(
            TT_EUROPE_TOUCHPOINTS,
            key=lambda r: int(r.get("year") or 0),
            reverse=True,
        )

    @staticmethod
    def get_press_claims() -> Dict[str, Any]:
        return dict(TT_PRESS_CLAIMS)

    @staticmethod
    def office_counts(domain: Optional[str] = None) -> Dict[str, int]:
        """Doğrulanmış TT-grup patent ofisleri. Konu seçildiyse yalnız o alan. EP/TR yoksa 0 görünür."""
        counts: Counter = Counter()
        for p in _patents():
            if domain and (p.get("domain") or "") != domain:
                continue
            office = next(
                (raw.get("office") for raw in TT_GROUP_PATENTS if raw["id"] == p.get("id")),
                "US",
            )
            counts[str(office)] += 1
        for key in ("EP", "US", "TR"):
            counts.setdefault(key, 0)
        return dict(counts)

    @staticmethod
    def get_ir_wholesale() -> Dict[str, Any]:
        payload = dict(TT_IR_WHOLESALE)
        payload["url"] = TT_IR_2024_URL
        payload["tti_url"] = TTI_ABOUT_URL
        return payload

    @staticmethod
    def map_rows() -> List[Dict[str, Any]]:
        """Harita katmanı: 6G Ar-Ge, yoksa TTI first-mover toptan. İki katman bir ülkede birleşmez uydurma sayıyla."""
        by_iso: Dict[str, Dict[str, Any]] = {}
        for row in TTI_WHOLESALE_FIRST_MOVER:
            by_iso[row["iso3"]] = {
                "iso3": row["iso3"],
                "layer": "wholesale",
                "name_tr": row["name_tr"],
                "name_en": row["name_en"],
                "label_tr": "TTI (Türk Telekom International) toptan; first-mover (ilk giren pazar, resmi About)",
                "label_en": "TTI (Türk Telekom International) wholesale; first-mover (official About)",
                "color": TT_COUNTRY_COLORS.get(row["iso3"], "#64748B"),
            }
        for row in TT_MAP_RD:
            prev = by_iso.get(row["iso3"])
            name_tr = next((w["name_tr"] for w in TTI_WHOLESALE_FIRST_MOVER if w["iso3"] == row["iso3"]), "")
            name_en = next((w["name_en"] for w in TTI_WHOLESALE_FIRST_MOVER if w["iso3"] == row["iso3"]), "")
            if row["iso3"] == "SWE":
                name_tr, name_en = "İsveç", "Sweden"
            elif row["iso3"] == "ESP":
                name_tr, name_en = "İspanya", "Spain"
            elif row["iso3"] == "FRA":
                name_tr, name_en = "Fransa", "France"
            elif row["iso3"] == "TUR":
                name_tr, name_en = "Türkiye", "Türkiye"
            # 6G katmanı toptanın üstüne yazılır; TR hem merkez hem toptan — merkez öncelikli
            by_iso[row["iso3"]] = {
                "iso3": row["iso3"],
                "layer": row["layer"],
                "name_tr": name_tr or (prev or {}).get("name_tr", row["iso3"]),
                "name_en": name_en or (prev or {}).get("name_en", row["iso3"]),
                "label_tr": row["label_tr"],
                "label_en": row["label_en"],
                "color": TT_COUNTRY_COLORS.get(row["iso3"], "#64748B"),
            }
        return list(by_iso.values())

    @staticmethod
    def role_kind_counts() -> List[Dict[str, Any]]:
        """Rol adedi: ülke boyamak değil, kanıt türü."""
        kinds = [
            {"id": "hq", "count": 1},
            {"id": "wholesale", "count": len(TTI_WHOLESALE_FIRST_MOVER)},
            {"id": "rd_collab", "count": sum(1 for r in TT_MAP_RD if r["layer"] == "rd_collab")},
            {"id": "standards", "count": sum(1 for r in TT_MAP_RD if r["layer"] == "standards")},
            {"id": "mou_venue", "count": sum(1 for r in TT_MAP_RD if r["layer"] == "mou_venue")},
            {"id": "ep_grant", "count": 0},
        ]
        return kinds

    @staticmethod
    def vendor_sample_vs_tt(domain: str | None = None) -> Dict[str, int]:
        """Bu platformun kilitli 6G örnek kümesi vs TT-grup USPTO. Küresel SEP payı değildir."""
        from backend.patent_service import PatentService

        spec = PatentService.get_spec_companies()
        counts = PatentService.get_company_counts(domain=domain)
        out = {name: int(counts.get(name, 0)) for name in spec}
        tt = _patents()
        if domain:
            tt = [p for p in tt if (p.get("domain") or "") == domain]
        out["Türk Telekom (Netsia)"] = len(tt)
        return out

    @staticmethod
    def country_touchpoint_counts() -> List[Dict[str, Any]]:
        counter: Counter = Counter()
        labels: Dict[str, Dict[str, str]] = {}
        for row in TT_EUROPE_TOUCHPOINTS:
            cc = row["country"]
            counter[cc] += 1
            labels[cc] = {
                "name_tr": row["country_name_tr"],
                "name_en": row["country_name_en"],
            }
        items = []
        for cc, n in counter.most_common():
            items.append(
                {
                    "code": cc,
                    "count": n,
                    "name_tr": labels[cc]["name_tr"],
                    "name_en": labels[cc]["name_en"],
                }
            )
        return items

    @staticmethod
    def summary(domain: Optional[str] = None) -> Dict[str, Any]:
        patents = [
            p for p in _patents() if not domain or (p.get("domain") or "") == domain
        ]
        papers = [
            p for p in _papers() if not domain or (p.get("topic") or "") == domain
        ]
        offices = TTEuropeService.office_counts(domain)
        return {
            "patent_n": len(patents),
            "paper_n": len(papers),
            "touch_n": len(TT_EUROPE_TOUCHPOINTS),
            "ep_n": offices.get("EP", 0),
            "us_n": offices.get("US", 0),
            "tr_n": offices.get("TR", 0),
            "source": TT_EUROPE_SOURCE,
            "wholesale_named_n": len(TTI_WHOLESALE_FIRST_MOVER),
        }


@st.cache_data(ttl=21600, show_spinner=False)
def _europe_overview_cached(include_pubs: bool = True) -> List[Dict[str, Any]]:
    """Kilitli ülkelerin tamamı. Her satır country_rank; sayı uydurulmaz."""
    out: List[Dict[str, Any]] = []
    for country in country_choices():
        payload = TTEuropeService.country_rank(country["cc"], include_pubs=include_pubs)
        if not payload.get("ok"):
            continue
        rows = payload["rows"]
        tt_row = next((r for r in rows if r.get("is_tt")), {})
        wiki_three = [
            r for r in rows if not (r.get("is_tt") and country["cc"] != "TR")
        ]
        pub_ordered = sorted(
            wiki_three,
            key=lambda r: (not r.get("pub_resolved"), -int(r.get("pub_n") or 0), r["name"]),
        )
        pat_ordered = sorted(
            wiki_three,
            key=lambda r: (-int(r.get("pat_n") or 0), r["name"]),
        )
        pub_positive = [r for r in rows if int(r.get("pub_n") or 0) > 0]
        pat_positive = [r for r in rows if int(r.get("pat_n") or 0) > 0]
        pub_lead = max(pub_positive, key=lambda r: int(r.get("pub_n") or 0)) if pub_positive else None
        pat_lead = max(pat_positive, key=lambda r: int(r.get("pat_n") or 0)) if pat_positive else None
        out.append(
            {
                "cc": country["cc"],
                "name_tr": country["name_tr"],
                "name_en": country["name_en"],
                "tt_pub_n": int(tt_row.get("pub_n") or 0),
                "tt_pub_resolved": bool(tt_row.get("pub_resolved")),
                "tt_pub_rank": tt_row.get("pub_rank"),
                "tt_pat_n": int(tt_row.get("pat_n") or 0),
                "tt_pat_rank": tt_row.get("pat_rank"),
                "field_n": payload.get("field_n") or len(rows),
                "pub_lead": None if not pub_lead else pub_lead.get("name"),
                "pub_lead_n": 0 if not pub_lead else int(pub_lead.get("pub_n") or 0),
                "pat_lead": None if not pat_lead else pat_lead.get("name"),
                "pat_lead_n": 0 if not pat_lead else int(pat_lead.get("pat_n") or 0),
                "pub_top3": [
                    {
                        "name": r["name"],
                        "n": int(r.get("pub_n") or 0),
                        "resolved": bool(r.get("pub_resolved")),
                    }
                    for r in pub_ordered[:3]
                ],
                "pat_top3": [
                    {"name": r["name"], "n": int(r.get("pat_n") or 0)}
                    for r in pat_ordered[:3]
                ],
                "pub_search_url": payload.get("pub_search_url"),
                "pub_ok": payload.get("pub_ok"),
            }
        )
    return sorted(
        out,
        key=lambda r: (r["pub_lead_n"], r["tt_pub_n"], r["tt_pat_n"], r["cc"]),
        reverse=True,
    )

