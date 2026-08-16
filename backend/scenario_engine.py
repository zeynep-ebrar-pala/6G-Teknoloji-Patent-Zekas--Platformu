"""
Türk Telekom 6G Platform - Backend Scenario Engine
Computes dynamic, highly reactive 6G technology matching based on regional, user density, and strategic priorities.
"""

class ScenarioEngine:
    """Backend calculation engine for matching 6G technologies with Türk Telekom deployment requirements."""

    REGIONAL_PRESETS = {
        "boğaz": {
            "title": "İstanbul Boğazı & Marmara Deniz Sahili",
            "base_tech": ["ISAC", "THz"],
            "base_solution": "Sahil 6G kulelerine entegre ISAC radar algılama + Kuleler arası THz kablosuz fiber geri bağlantı.",
            "target_year": "2028 Saha Pilotu",
            "base_capex": "Orta - Yüksek"
        },
        "stadyum": {
            "title": "RAMS Park / Stadyum & Yoğun Etkinlik Alanları",
            "base_tech": ["Cell-Free Massive MIMO", "AI-Native RAN"],
            "base_solution": "Tribün ve çatıya dağıtılmış 200+ mini AP ile hücresiz (Cell-Free) kapsama + AI-RAN dinamik yük dengeleme.",
            "target_year": "2027 Prototip Denemesi",
            "base_capex": "Yüksek"
        },
        "sanayi": {
            "title": "Marmara Sanayi Bölgesi / Otonom Fabrikalar",
            "base_tech": ["Ambient IoT", "RIS"],
            "base_solution": "Fabrika içi pilsiz Ambient IoT etiketleri + Duvar kaplaması pasif RIS yansıtıcılar.",
            "target_year": "2026 Endüstri PoC",
            "base_capex": "Düşük - Optimal"
        },
        "deprem": {
            "title": "AFAD Entegre Deprem & Afet Bölgesi",
            "base_tech": ["NTN (Uydu Entegrasyonu)", "ISAC"],
            "base_solution": "LEO Uydulardan akıllı telefonlara Direct-to-Cell bağlantı + Duvar arkası RF enkaz radar algılaması.",
            "target_year": "3GPP Rel-18/19 Entegrasyonu",
            "base_capex": "Stratejik Yatırım"
        },
        "tarihi": {
            "title": "Tarihi Yarımada / Dar Sokak Kentsel Alan",
            "base_tech": ["RIS", "Sub-THz"],
            "base_solution": "Tarihi dokuyu bozmadan bina dış yüzeylerine şeffaf pasif RIS kaplama.",
            "target_year": "2027 Kentsel Pilot",
            "base_capex": "Düşük"
        },
        "datacenter": {
            "title": "Türk Telekom Ankara & İstanbul Data Center",
            "base_tech": ["THz Communication", "AI-Native RAN"],
            "base_solution": "Sunucu rafları arasında 1 Tbps kablosuz THz mesh bağlantısı + AI-RAN derin uyku modları.",
            "target_year": "2026 Lab Demosu",
            "base_capex": "Düşük"
        }
    }

    @classmethod
    def evaluate_scenario(cls, region_input: str, density_input: str, priority_input: str) -> dict:
        """
        Dynamically calculates architecture recommendations, feasibility scores, KPIs, and deployment impact
        based on all 3 user input dimensions.
        """
        # 1. Match Region
        matched_preset = None
        for key, preset in cls.REGIONAL_PRESETS.items():
            if key in region_input.lower():
                matched_preset = preset
                break
        
        if not matched_preset:
            matched_preset = cls.REGIONAL_PRESETS["boğaz"]

        recommended_techs = list(matched_preset["base_tech"])
        
        # 2. Adjust based on Strategic Priority
        priority_kpi = ""
        energy_score = 85
        feasibility_score = 90
        capacity_gbps = 100
        latency_ms = 1.0

        if "Kesintisiz Kapsama" in priority_input:
            if "RIS" not in recommended_techs:
                recommended_techs.append("RIS")
            priority_kpi = "Sıfır Kör Nokta (%99.999 Güvenilirlik & Kapsama)"
            feasibility_score += 5
            energy_score += 8
            latency_ms = 0.8
        elif "Ultra Yüksek Hız" in priority_input:
            if "THz" not in recommended_techs:
                recommended_techs.append("THz")
            priority_kpi = "1 Tbps Peak Hız & Ultra Geniş Frekans Bandı"
            capacity_gbps = 1000
            latency_ms = 0.1
            energy_score -= 10
        elif "Düşük Enerji" in priority_input:
            if "Ambient IoT" not in recommended_techs and "AI-Native RAN" not in recommended_techs:
                recommended_techs.append("AI-Native RAN")
            priority_kpi = "Yeşil 6G — yüksek enerji verimliliği hedefi (AI-RAN derin uyku)"
            energy_score = 98
            feasibility_score += 3
        elif "Afet Dayanıklılığı" in priority_input:
            if "NTN" not in recommended_techs:
                recommended_techs.append("NTN")
            priority_kpi = "Karasal Kule Çökse Bile %100 Uydudan Acil İletişim"
            feasibility_score += 4
            latency_ms = 5.0

        # 3. Adjust based on User/Sensor Density
        density_kpi = ""
        active_nodes = "10.000 / km²"
        
        if "Düşük" in density_input:
            density_kpi = "Kırsal / Geniş Alan Genişletilmiş Kapsama"
            active_nodes = "500 cihaz / km²"
            feasibility_score = min(98, feasibility_score + 4)
        elif "Orta" in density_input:
            density_kpi = "Dengeli Şehir İçi Makro-Mikro Şebeke Katmanı"
            active_nodes = "50.000 cihaz / km²"
        elif "Yüksek" in density_input:
            density_kpi = "Yoğun Şehir İçi / Stadyum Çoklu Hüzme (Multi-beam) Tahsisi"
            active_nodes = "500.000 cihaz / km²"
            capacity_gbps = int(capacity_gbps * 1.5)
        elif "Aşırı Yoğun" in density_input:
            if "Cell-Free Massive MIMO" not in recommended_techs:
                recommended_techs.append("Cell-Free Massive MIMO")
            density_kpi = "Trilyon Cihaz Ölçeğinde Pilsiz Etiket & Ultra Masif Hücresiz Ağ"
            active_nodes = "1.000.000+ sensör / km²"
            capacity_gbps = int(capacity_gbps * 2.5)

        # 4. Formulate Detailed Impact & Strategic Action Plan
        impact_summary = (
            f"**Seçilen Bölge ({matched_preset['title']})** için **'{priority_input}'** önceliği "
            f"ve **'{density_input}'** hedefiyle özelleştirilmiş 6G mimarisi oluşturuldu.\n\n"
            f"• **Kapasite & Hız:** {capacity_gbps} Gbps Peak Akış\n"
            f"• **Gecikme Süresi:** {latency_ms} ms (Ultra-Reliable Low-Latency)\n"
            f"• **Şebeke Yoğunluğu:** {active_nodes}\n"
            f"• **Enerji Verimliliği Skoru:** %{energy_score}"
        )

        return {
            "matched": True,
            "region_title": matched_preset["title"],
            "recommended_tech": recommended_techs,
            "solution": matched_preset["base_solution"],
            "impact_summary": impact_summary,
            "target_year": matched_preset["target_year"],
            "capex_estimate": matched_preset["base_capex"],
            "priority_kpi": priority_kpi,
            "density_kpi": density_kpi,
            "feasibility_score": min(99, max(60, feasibility_score)),
            "energy_score": max(50, min(100, energy_score)),
            "capacity_gbps": capacity_gbps,
            "latency_ms": latency_ms,
            "active_nodes": active_nodes
        }
