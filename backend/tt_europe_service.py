"""
Türk Telekom Avrupa izi — doğrulanmış kayıtları UI ve grafik için hazırlar.
"""

from __future__ import annotations

from collections import Counter
from typing import Any, Dict, List

from backend.data_validator import load_validated_papers, load_validated_patents
from data.tt_europe import (
    TT_AFFILIATED_PAPERS,
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
        out.append(merged)
    return out


class TTEuropeService:
    @staticmethod
    def get_source() -> str:
        return TT_EUROPE_SOURCE

    @staticmethod
    def get_patents() -> List[Dict[str, Any]]:
        return _patents()

    @staticmethod
    def get_papers() -> List[Dict[str, Any]]:
        return _papers()

    @staticmethod
    def get_touchpoints() -> List[Dict[str, Any]]:
        return list(TT_EUROPE_TOUCHPOINTS)

    @staticmethod
    def get_press_claims() -> Dict[str, Any]:
        return dict(TT_PRESS_CLAIMS)

    @staticmethod
    def office_counts() -> Dict[str, int]:
        """Doğrulanmış TT-grup patent ofisleri. EP yoksa 0 olarak görünür; uydurulmaz."""
        counts: Counter = Counter()
        for p in _patents():
            office = next(
                (raw.get("office") for raw in TT_GROUP_PATENTS if raw["id"] == p.get("id")),
                "US",
            )
            counts[office] += 1
        if "EP" not in counts:
            counts["EP"] = 0
        if "TR" not in counts:
            counts["TR"] = 0
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
                "label_tr": "TTI toptan first-mover (resmi About)",
                "label_en": "TTI wholesale first-mover (official About)",
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
    def vendor_sample_vs_tt() -> Dict[str, int]:
        """Bu platformun kilitli 6G örnek kümesi vs TT-grup USPTO. Küresel SEP payı değildir."""
        from backend.patent_service import PatentService

        spec = PatentService.get_spec_companies()
        counts = PatentService.get_company_counts()
        out = {name: int(counts.get(name, 0)) for name in spec}
        out["Türk Telekom (Netsia)"] = len(_patents())
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
    def summary() -> Dict[str, Any]:
        patents = _patents()
        papers = _papers()
        offices = TTEuropeService.office_counts()
        return {
            "patent_n": len(patents),
            "paper_n": len(papers),
            "touch_n": len(TT_EUROPE_TOUCHPOINTS),
            "ep_n": offices.get("EP", 0),
            "us_n": offices.get("US", 0),
            "source": TT_EUROPE_SOURCE,
            "wholesale_named_n": len(TTI_WHOLESALE_FIRST_MOVER),
        }
