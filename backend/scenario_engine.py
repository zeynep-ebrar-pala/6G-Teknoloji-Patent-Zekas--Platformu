"""
Türk Telekom 6G Platform - Backend Scenario Engine
Kural tabanlı eşleştirme: bölge / yoğunluk / öncelik anahtarları dile bağlı değildir.
Gösterim metinleri i18n katmanındadır; sayısal hesap değişmez.
"""

from i18n.core import format_decimal, format_int, t

REGION_KEYS = ("bosphorus", "stadium", "industry", "disaster", "historic", "datacenter")
DENSITY_KEYS = ("low", "medium", "high", "extreme")
PRIORITY_KEYS = ("coverage", "speed", "energy", "resilience")

_REGIONAL = {
    "bosphorus": {"base_tech": ["ISAC", "THz"], "capex": "mid_high"},
    "stadium": {"base_tech": ["Cell-Free Massive MIMO", "AI-Native RAN"], "capex": "high"},
    "industry": {"base_tech": ["Ambient IoT", "RIS"], "capex": "low_opt"},
    "disaster": {"base_tech": ["NTN (satellite)", "ISAC"], "capex": "strategic"},
    "historic": {"base_tech": ["RIS", "Sub-THz"], "capex": "low"},
    "datacenter": {"base_tech": ["THz Communication", "AI-Native RAN"], "capex": "low"},
}


class ScenarioEngine:
    """Backend calculation engine for matching 6G technologies with Türk Telekom deployment requirements."""

    @classmethod
    def evaluate_scenario(cls, region_key: str, density_key: str, priority_key: str) -> dict:
        preset = _REGIONAL.get(region_key) or _REGIONAL["bosphorus"]
        region_key = region_key if region_key in _REGIONAL else "bosphorus"

        recommended_techs = list(preset["base_tech"])
        energy_score = 85
        feasibility_score = 90
        capacity_gbps = 100
        latency_ms = 1.0

        if priority_key == "coverage":
            if "RIS" not in recommended_techs:
                recommended_techs.append("RIS")
            priority_kpi = t("scenario.kpi_coverage")
            feasibility_score += 5
            energy_score += 8
            latency_ms = 0.8
        elif priority_key == "speed":
            if "THz" not in recommended_techs:
                recommended_techs.append("THz")
            priority_kpi = t("scenario.kpi_speed")
            capacity_gbps = 1000
            latency_ms = 0.1
            energy_score -= 10
        elif priority_key == "energy":
            if "Ambient IoT" not in recommended_techs and "AI-Native RAN" not in recommended_techs:
                recommended_techs.append("AI-Native RAN")
            priority_kpi = t("scenario.kpi_energy")
            energy_score = 98
            feasibility_score += 3
        else:
            if "NTN" not in recommended_techs and not any("NTN" in x for x in recommended_techs):
                recommended_techs.append("NTN")
            priority_kpi = t("scenario.kpi_resilience")
            feasibility_score += 4
            latency_ms = 5.0

        if density_key == "low":
            density_kpi = t("scenario.dens_low")
            active_nodes = t("scenario.nodes_low")
            feasibility_score = min(98, feasibility_score + 4)
        elif density_key == "medium":
            density_kpi = t("scenario.dens_medium")
            active_nodes = t("scenario.nodes_medium")
        elif density_key == "high":
            density_kpi = t("scenario.dens_high")
            active_nodes = t("scenario.nodes_high")
            capacity_gbps = int(capacity_gbps * 1.5)
        else:
            if "Cell-Free Massive MIMO" not in recommended_techs:
                recommended_techs.append("Cell-Free Massive MIMO")
            density_kpi = t("scenario.dens_extreme")
            active_nodes = t("scenario.nodes_extreme")
            capacity_gbps = int(capacity_gbps * 2.5)

        region_title = t(f"scenario.title_{region_key}")
        impact_summary = t(
            "scenario.impact",
            region=region_title,
            priority=t(f"scenario.priority_{priority_key}"),
            density=t(f"scenario.density_{density_key}"),
            capacity=format_int(capacity_gbps),
            latency=format_decimal(latency_ms, 1),
            nodes=active_nodes,
            energy=format_int(max(50, min(100, energy_score))),
        )

        return {
            "matched": True,
            "region_title": region_title,
            "recommended_tech": recommended_techs,
            "solution": t(f"scenario.sol_{region_key}"),
            "impact_summary": impact_summary,
            "target_year": t(f"scenario.year_{region_key}"),
            "capex_estimate": t(f"scenario.capex_{preset['capex']}"),
            "priority_kpi": priority_kpi,
            "density_kpi": density_kpi,
            "feasibility_score": min(99, max(60, feasibility_score)),
            "energy_score": max(50, min(100, energy_score)),
            "capacity_gbps": capacity_gbps,
            "latency_ms": latency_ms,
            "active_nodes": active_nodes,
        }
