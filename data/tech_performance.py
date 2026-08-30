"""
Teknoloji başına performans KPI grafikleri — hız, gecikme, menzil, kazanç.
Her grafik kaynak notu taşır; değer uydurulmaz. TT abone şebekesi ölçümü değildir.
"""

from __future__ import annotations

from typing import Any, Dict, List

TECH_PERFORMANCE: Dict[str, Dict[str, Any]] = {
    "isac": {
        "caption_tr": (
            "Menzil ve gecikme laboratuvar / Rel-19 (TR 22.837) sınıfıdır. Algılama menzili "
            "iletişimden kısadır (R⁴ yankı kaybı). Santimetre hassasiyet bu platformda ölçülmedi."
        ),
        "caption_en": (
            "Range and latency are laboratory / Rel-19 (TR 22.837) class. Sensing range is shorter "
            "than communication (R⁴ echo loss). Centimetre accuracy was not measured on this platform."
        ),
        "sources_tr": "3GPP TR 22.837; platform expert_depth ISAC notları",
        "sources_en": "3GPP TR 22.837; platform expert_depth ISAC notes",
        "charts": [
            {
                "type": "bar",
                "title_tr": "Menzil (lab / demo sınıfı)",
                "title_en": "Range (lab / demo class)",
                "unit_tr": "metre",
                "unit_en": "metres",
                "metrics": [
                    {
                        "label_tr": "Algılama menzili (tipik lab)",
                        "label_en": "Sensing range (typical lab)",
                        "value": 150,
                        "display_tr": "~150 m",
                        "display_en": "~150 m",
                    },
                    {
                        "label_tr": "İletişim menzili (makro, aynı band)",
                        "label_en": "Communication range (macro, same band)",
                        "value": 400,
                        "display_tr": "~400 m",
                        "display_en": "~400 m",
                    },
                    {
                        "label_tr": "Menzil hatası (metre sınıfı lab)",
                        "label_en": "Range error (metre-class lab)",
                        "value": 2,
                        "display_tr": "~2 m",
                        "display_en": "~2 m",
                    },
                ],
            },
            {
                "type": "bar",
                "title_tr": "İşleme gecikmesi (hedef)",
                "title_en": "Processing latency (target)",
                "unit_tr": "ms",
                "unit_en": "ms",
                "metrics": [
                    {
                        "label_tr": "Kenar özeti (hedef)",
                        "label_en": "Edge summary (target)",
                        "value": 10,
                        "display_tr": "~10 ms",
                        "display_en": "~10 ms",
                    },
                    {
                        "label_tr": "Uçtan uca algılama döngüsü (hedef)",
                        "label_en": "End-to-end sensing loop (target)",
                        "value": 20,
                        "display_tr": "~20 ms",
                        "display_en": "~20 ms",
                    },
                ],
            },
        ],
    },
    "ris": {
        "caption_tr": (
            "dB değerleri ideal faz hizalamasında literatür ölçeğidir (N² güç ölçeği; pratikte "
            "kestirim hatası düşürür). ETSI ISG RIS ve operatör PoC sınıfı; saha garantisi değil."
        ),
        "caption_en": (
            "dB values are literature-scale under ideal phase alignment (N² power scaling; "
            "estimation error lowers field results). ETSI ISG RIS and operator-PoC class; not a field guarantee."
        ),
        "sources_tr": "ETSI ISG RIS; expert_depth RIS N² notu",
        "sources_en": "ETSI ISG RIS; expert_depth RIS N² note",
        "charts": [
            {
                "type": "bar",
                "title_tr": "SNR kazancı (NLoS, ideal hizalama)",
                "title_en": "SNR gain (NLoS, ideal alignment)",
                "unit_tr": "dB",
                "unit_en": "dB",
                "metrics": [
                    {
                        "label_tr": "Pasif RIS (N≈100, ideal)",
                        "label_en": "Passive RIS (N≈100, ideal)",
                        "value": 20,
                        "display_tr": "~20 dB",
                        "display_en": "~20 dB",
                    },
                    {
                        "label_tr": "Aktif röle (referans)",
                        "label_en": "Active relay (reference)",
                        "value": 25,
                        "display_tr": "~25 dB",
                        "display_en": "~25 dB",
                    },
                    {
                        "label_tr": "Makro yalnız (NLoS referans)",
                        "label_en": "Macro only (NLoS reference)",
                        "value": 0,
                        "display_tr": "0 dB",
                        "display_en": "0 dB",
                    },
                ],
            },
            {
                "type": "bar",
                "title_tr": "Kontrol gecikmesi (hedef)",
                "title_en": "Control latency (target)",
                "unit_tr": "ms",
                "unit_en": "ms",
                "metrics": [
                    {
                        "label_tr": "C-plane hedefi",
                        "label_en": "C-plane target",
                        "value": 10,
                        "display_tr": "~10 ms",
                        "display_en": "~10 ms",
                    },
                    {
                        "label_tr": "Faz güncelleme (Near-RT sınıfı)",
                        "label_en": "Phase update (Near-RT class)",
                        "value": 10,
                        "display_tr": "~10 ms",
                        "display_en": "~10 ms",
                    },
                ],
            },
        ],
    },
    "cell_free": {
        "caption_tr": (
            "Kenar hızı örnek senaryodur (~100 MHz FR1, TR 38.848 dağıtık MIMO sınıfı). "
            "Mutlak Mbps bant genişliğine bağlıdır; fiber fronthaul şarttır."
        ),
        "caption_en": (
            "Cell-edge rates are an example scenario (~100 MHz FR1, TR 38.848 distributed-MIMO class). "
            "Absolute Mbps depends on bandwidth; fibre fronthaul is required."
        ),
        "sources_tr": "3GPP TR 38.848; dağıtık MIMO literatürü (~2–4× kenar kazancı)",
        "sources_en": "3GPP TR 38.848; distributed-MIMO literature (~2–4× edge gain)",
        "charts": [
            {
                "type": "bar",
                "title_tr": "Hücre kenarı hızı (örnek senaryo)",
                "title_en": "Cell-edge rate (example scenario)",
                "unit_tr": "Mbps",
                "unit_en": "Mbps",
                "metrics": [
                    {
                        "label_tr": "Tek makro (kenar)",
                        "label_en": "Single macro (edge)",
                        "value": 50,
                        "display_tr": "~50 Mbps",
                        "display_en": "~50 Mbps",
                    },
                    {
                        "label_tr": "Hücresiz küme (kenar)",
                        "label_en": "Cell-free cluster (edge)",
                        "value": 150,
                        "display_tr": "~150 Mbps",
                        "display_en": "~150 Mbps",
                    },
                    {
                        "label_tr": "Merkez (makro)",
                        "label_en": "Centre (macro)",
                        "value": 300,
                        "display_tr": "~300 Mbps",
                        "display_en": "~300 Mbps",
                    },
                ],
            },
            {
                "type": "bar",
                "title_tr": "Kenar kazancı (oran)",
                "title_en": "Edge gain (ratio)",
                "unit_tr": "×",
                "unit_en": "×",
                "metrics": [
                    {
                        "label_tr": "Makro kenar (referans)",
                        "label_en": "Macro edge (reference)",
                        "value": 1,
                        "display_tr": "1×",
                        "display_en": "1×",
                    },
                    {
                        "label_tr": "Hücresiz kenar (literatür)",
                        "label_en": "Cell-free edge (literature)",
                        "value": 3,
                        "display_tr": "~3×",
                        "display_en": "~3×",
                    },
                ],
            },
        ],
    },
    "thz": {
        "caption_tr": (
            "Samsung/UCSB: 6,2 Gbps @ 15 m (140 GHz, ICC 2021). LG: 500 m kentsel menzil rekoru "
            "(2023); hız bu duyuruda sayılmadı. Tbps hedefi literatür bandıdır, ölçülmedi."
        ),
        "caption_en": (
            "Samsung/UCSB: 6.2 Gbps at 15 m (140 GHz, ICC 2021). LG: 500 m urban range record "
            "(2023); rate was not stated in that release. Tbps is a literature band target, not measured."
        ),
        "sources_tr": "Samsung ICC 2021 DOI 10.1109/ICCWorkshops50388.2021.9473600; LG 2023 kentsel 500 m",
        "sources_en": "Samsung ICC 2021 DOI 10.1109/ICCWorkshops50388.2021.9473600; LG 2023 urban 500 m",
        "charts": [
            {
                "type": "bar",
                "title_tr": "Doğrulanmış demo — veri hızı",
                "title_en": "Verified demo — data rate",
                "unit_tr": "Gbps",
                "unit_en": "Gbps",
                "metrics": [
                    {
                        "label_tr": "Samsung/UCSB @ 15 m",
                        "label_en": "Samsung/UCSB at 15 m",
                        "value": 6,
                        "display_tr": "6,2 Gbps",
                        "display_en": "6.2 Gbps",
                    },
                    {
                        "label_tr": "Literatür hedef (kısa menzil)",
                        "label_en": "Literature target (short range)",
                        "value": 100,
                        "display_tr": "~100 Gbps hedef",
                        "display_en": "~100 Gbps target",
                    },
                ],
            },
            {
                "type": "bar",
                "title_tr": "Doğrulanmış demo — menzil",
                "title_en": "Verified demo — range",
                "unit_tr": "metre",
                "unit_en": "metres",
                "metrics": [
                    {
                        "label_tr": "Samsung/UCSB (ölçülen hız)",
                        "label_en": "Samsung/UCSB (measured rate)",
                        "value": 15,
                        "display_tr": "15 m",
                        "display_en": "15 m",
                    },
                    {
                        "label_tr": "LG/LG U+ kentsel (2023)",
                        "label_en": "LG/LG U+ urban (2023)",
                        "value": 500,
                        "display_tr": "500 m",
                        "display_en": "500 m",
                    },
                ],
            },
        ],
    },
    "ai_ran": {
        "caption_tr": (
            "RIC döngüleri O-RAN WG3: Near-RT 10 ms–1 s, Non-RT >1 s. Enerji yüzdeleri literatür "
            "hedefi; TT fatura ölçümü yok. %50–70 enerji pazarlaması bu grafikte yok."
        ),
        "caption_en": (
            "RIC loops per O-RAN WG3: Near-RT 10 ms–1 s, Non-RT >1 s. Energy percentages are "
            "literature targets; no TT bill measurement. 50–70% energy marketing is not on this chart."
        ),
        "sources_tr": "O-RAN WG3 RICARCH; TR 38.843 AI/ML for NR",
        "sources_en": "O-RAN WG3 RICARCH; TR 38.843 AI/ML for NR",
        "charts": [
            {
                "type": "bar",
                "title_tr": "RIC döngü süresi (O-RAN WG3)",
                "title_en": "RIC loop time (O-RAN WG3)",
                "unit_tr": "ms",
                "unit_en": "ms",
                "metrics": [
                    {
                        "label_tr": "Near-RT RIC (alt sınır)",
                        "label_en": "Near-RT RIC (lower bound)",
                        "value": 10,
                        "display_tr": "10 ms",
                        "display_en": "10 ms",
                    },
                    {
                        "label_tr": "Non-RT RIC (alt sınır)",
                        "label_en": "Non-RT RIC (lower bound)",
                        "value": 1000,
                        "display_tr": ">1000 ms",
                        "display_en": ">1000 ms",
                    },
                    {
                        "label_tr": "Klasik RRM döngüsü (tipik)",
                        "label_en": "Classic RRM cycle (typical)",
                        "value": 100,
                        "display_tr": "~100 ms",
                        "display_en": "~100 ms",
                    },
                ],
            },
            {
                "type": "bar",
                "title_tr": "Enerji hedefi (literatür)",
                "title_en": "Energy target (literature)",
                "unit_tr": "%",
                "unit_en": "%",
                "metrics": [
                    {
                        "label_tr": "Makro uyku modu hedefi",
                        "label_en": "Macro sleep-mode target",
                        "value": 30,
                        "display_tr": "~30 %",
                        "display_en": "~30 %",
                    },
                    {
                        "label_tr": "Dinamik kaynak kaydırma hedefi",
                        "label_en": "Dynamic resource-shift target",
                        "value": 15,
                        "display_tr": "~15 %",
                        "display_en": "~15 %",
                    },
                ],
            },
        ],
    },
    "ntn": {
        "caption_tr": (
            "Gecikme: TR 38.811 yayılma RTT (işlem yok). LEO 600 km, UE elevasyon 10°. "
            "Karasal satır tipik kullanıcı düzlemi RTT örneğidir (yayılma tek başına <1 ms)."
        ),
        "caption_en": (
            "Latency: TR 38.811 propagation RTT (no processing). LEO 600 km, UE elevation 10°. "
            "Terrestrial row is a typical user-plane RTT example (propagation alone <1 ms)."
        ),
        "sources_tr": "3GPP TR 38.811 Tablo 5.3.4.1; TR 38.821 Tablo 7.1.1",
        "sources_en": "3GPP TR 38.811 Table 5.3.4.1; TR 38.821 Table 7.1.1",
        "charts": [
            {
                "type": "bar",
                "title_tr": "Gidiş-dönüş gecikme (TR 38.811 yayılma)",
                "title_en": "Round-trip latency (TR 38.811 propagation)",
                "unit_tr": "ms RTT",
                "unit_en": "ms RTT",
                "metrics": [
                    {
                        "label_tr": "Karasal NR (tipik kullanıcı RTT)",
                        "label_en": "Terrestrial NR (typical user RTT)",
                        "value": 20,
                        "display_tr": "~20 ms",
                        "display_en": "~20 ms",
                    },
                    {
                        "label_tr": "LEO rejeneratif (600 km)",
                        "label_en": "LEO regenerative (600 km)",
                        "value": 13,
                        "display_tr": "12,9 ms",
                        "display_en": "12.9 ms",
                    },
                    {
                        "label_tr": "LEO şeffaf (600 km)",
                        "label_en": "LEO transparent (600 km)",
                        "value": 26,
                        "display_tr": "25,8 ms",
                        "display_en": "25.8 ms",
                    },
                    {
                        "label_tr": "GEO rejeneratif",
                        "label_en": "GEO regenerative",
                        "value": 271,
                        "display_tr": "270,7 ms",
                        "display_en": "270.7 ms",
                    },
                ],
            },
            {
                "type": "bar",
                "title_tr": "Hüzme ayak izi (TR 38.821)",
                "title_en": "Beam footprint (TR 38.821)",
                "unit_tr": "km çap",
                "unit_en": "km diameter",
                "metrics": [
                    {
                        "label_tr": "LEO max hüzme çapı",
                        "label_en": "LEO max beam diameter",
                        "value": 1000,
                        "display_tr": "1000 km",
                        "display_en": "1000 km",
                    },
                    {
                        "label_tr": "LEO min hüzme çapı",
                        "label_en": "LEO min beam diameter",
                        "value": 50,
                        "display_tr": "50 km",
                        "display_en": "50 km",
                    },
                ],
            },
        ],
    },
    "ambient_iot": {
        "caption_tr": (
            "Menzil ve hız okuyucu gücüne bağlıdır. TR 38.848 ambient/backscatter sınıfı; "
            "pilsiz etiket TT abone şebekesinde doğrulanmamıştır."
        ),
        "caption_en": (
            "Range and rate depend on reader power. TR 38.848 ambient/backscatter class; "
            "battery-free tags are not verified on the TT retail network."
        ),
        "sources_tr": "3GPP TR 38.848; ambient backscatter literatürü",
        "sources_en": "3GPP TR 38.848; ambient backscatter literature",
        "charts": [
            {
                "type": "bar",
                "title_tr": "Okuma menzili (demo sınıfı)",
                "title_en": "Read range (demo class)",
                "unit_tr": "metre",
                "unit_en": "metres",
                "metrics": [
                    {
                        "label_tr": "Kapalı alan / depo",
                        "label_en": "Indoor / warehouse",
                        "value": 10,
                        "display_tr": "~10 m",
                        "display_en": "~10 m",
                    },
                    {
                        "label_tr": "Açık alan (yüksek güç)",
                        "label_en": "Open area (high power)",
                        "value": 20,
                        "display_tr": "~20 m",
                        "display_en": "~20 m",
                    },
                ],
            },
            {
                "type": "bar",
                "title_tr": "Veri hızı (backscatter sınıfı)",
                "title_en": "Data rate (backscatter class)",
                "unit_tr": "kbps",
                "unit_en": "kbps",
                "metrics": [
                    {
                        "label_tr": "Etiket uplink (tipik)",
                        "label_en": "Tag uplink (typical)",
                        "value": 1,
                        "display_tr": "~1 kbps",
                        "display_en": "~1 kbps",
                    },
                    {
                        "label_tr": "Sensör burst (kısa)",
                        "label_en": "Sensor burst (short)",
                        "value": 10,
                        "display_tr": "~10 kbps",
                        "display_en": "~10 kbps",
                    },
                ],
            },
        ],
    },
}


def get_tech_performance(tech_id: str) -> Dict[str, Any] | None:
    return TECH_PERFORMANCE.get(tech_id)
