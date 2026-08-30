"""
Teknoloji başına performans KPI grafikleri — hız, gecikme, menzil, kazanç.
Değerler literatür / demo / şartname hedef sınıfıdır; Türk Telekom şebekesinde ölçülmedi.
Makale ve patent sayısı bu dosyada yoktur.
"""

from __future__ import annotations

from typing import Any, Dict, List

TECH_PERFORMANCE: Dict[str, Dict[str, Any]] = {
    "isac": {
        "caption_tr": (
            "ISAC paylaşımlı kaynakta iletişim ve algılama aynı güç bütçesini böler. "
            "Menzil ve gecikme laboratuvar ve Rel-19 çalışma sınıfıdır; santimetre hassasiyet "
            "bu platformda ölçülmedi."
        ),
        "caption_en": (
            "ISAC splits the same power budget between communication and sensing. "
            "Range and latency are laboratory and Rel-19 work-item class; centimetre accuracy "
            "was not measured on this platform."
        ),
        "charts": [
            {
                "type": "bar",
                "title_tr": "Menzil (laboratuvar / demo sınıfı)",
                "title_en": "Range (laboratory / demo class)",
                "unit_tr": "metre",
                "unit_en": "metres",
                "metrics": [
                    {
                        "label_tr": "Algılama menzili",
                        "label_en": "Sensing range",
                        "value": 200,
                        "display_tr": "200 m",
                        "display_en": "200 m",
                    },
                    {
                        "label_tr": "İletişim menzili (aynı band)",
                        "label_en": "Communication range (same band)",
                        "value": 500,
                        "display_tr": "500 m",
                        "display_en": "500 m",
                    },
                    {
                        "label_tr": "Menzil hatası (tipik lab)",
                        "label_en": "Range error (typical lab)",
                        "value": 1,
                        "display_tr": "1 m",
                        "display_en": "1 m",
                    },
                ],
            },
            {
                "type": "bar",
                "title_tr": "İşleme gecikmesi hedefi",
                "title_en": "Processing latency target",
                "unit_tr": "ms",
                "unit_en": "ms",
                "metrics": [
                    {
                        "label_tr": "Kenar sunucu özeti",
                        "label_en": "Edge summary",
                        "value": 8,
                        "display_tr": "8 ms",
                        "display_en": "8 ms",
                    },
                    {
                        "label_tr": "Uçtan uca algılama döngüsü",
                        "label_en": "End-to-end sensing loop",
                        "value": 15,
                        "display_tr": "15 ms",
                        "display_en": "15 ms",
                    },
                ],
            },
        ],
    },
    "ris": {
        "caption_tr": (
            "RIS kazancı faz hizalamasına bağlıdır; kuantize faz ve kestirim hatası saha değerini "
            "düşürür. dB değerleri ETSI ISG ve operatör PoC literatür sınıfıdır."
        ),
        "caption_en": (
            "RIS gain depends on phase alignment; quantised phase and estimation error reduce field "
            "values. dB figures are ETSI ISG and operator-PoC literature class."
        ),
        "charts": [
            {
                "type": "bar",
                "title_tr": "Kapsama kazancı (NLoS, ideal hizalama)",
                "title_en": "Coverage gain (NLoS, ideal alignment)",
                "unit_tr": "dB",
                "unit_en": "dB",
                "metrics": [
                    {
                        "label_tr": "Pasif RIS ile SNR artışı",
                        "label_en": "SNR boost with passive RIS",
                        "value": 20,
                        "display_tr": "20 dB",
                        "display_en": "20 dB",
                    },
                    {
                        "label_tr": "Aktif röle (referans)",
                        "label_en": "Active relay (reference)",
                        "value": 25,
                        "display_tr": "25 dB",
                        "display_en": "25 dB",
                    },
                    {
                        "label_tr": "Makro yalnız (NLoS)",
                        "label_en": "Macro only (NLoS)",
                        "value": 0,
                        "display_tr": "0 dB",
                        "display_en": "0 dB",
                    },
                ],
            },
            {
                "type": "bar",
                "title_tr": "Kontrol ve güncelleme",
                "title_en": "Control and update",
                "unit_tr": "ms",
                "unit_en": "ms",
                "metrics": [
                    {
                        "label_tr": "C-plane kontrol gecikmesi",
                        "label_en": "C-plane control latency",
                        "value": 5,
                        "display_tr": "5 ms",
                        "display_en": "5 ms",
                    },
                    {
                        "label_tr": "Faz güncelleme döngüsü",
                        "label_en": "Phase update cycle",
                        "value": 10,
                        "display_tr": "10 ms",
                        "display_en": "10 ms",
                    },
                ],
            },
        ],
    },
    "cell_free": {
        "caption_tr": (
            "Hücre kenarı hızı fiber fronthaul ve senkronizasyona bağlıdır. Mbps değerleri "
            "dağıtık MIMO literatür ve demo sınıfıdır; stadyum sahası TT ölçümü değildir."
        ),
        "caption_en": (
            "Cell-edge rate depends on fibre fronthaul and synchronisation. Mbps values are "
            "distributed-MIMO literature and demo class; not a TT stadium field measurement."
        ),
        "charts": [
            {
                "type": "bar",
                "title_tr": "Hücre kenarı veri hızı (demo sınıfı)",
                "title_en": "Cell-edge data rate (demo class)",
                "unit_tr": "Mbps",
                "unit_en": "Mbps",
                "metrics": [
                    {
                        "label_tr": "Tek makro kule (kenar)",
                        "label_en": "Single macro (edge)",
                        "value": 80,
                        "display_tr": "80 Mbps",
                        "display_en": "80 Mbps",
                    },
                    {
                        "label_tr": "Hücresiz MIMO kümesi",
                        "label_en": "Cell-free cluster",
                        "value": 250,
                        "display_tr": "250 Mbps",
                        "display_en": "250 Mbps",
                    },
                    {
                        "label_tr": "Merkez (makro)",
                        "label_en": "Centre (macro)",
                        "value": 400,
                        "display_tr": "400 Mbps",
                        "display_en": "400 Mbps",
                    },
                ],
            },
            {
                "type": "bar",
                "title_tr": "Geçiş ve gecikme",
                "title_en": "Handover and latency",
                "unit_tr": "ms",
                "unit_en": "ms",
                "metrics": [
                    {
                        "label_tr": "Klasik handover kesintisi",
                        "label_en": "Classic handover gap",
                        "value": 20,
                        "display_tr": "20 ms",
                        "display_en": "20 ms",
                    },
                    {
                        "label_tr": "Serving kümesi kaydırma hedefi",
                        "label_en": "Serving cluster shift target",
                        "value": 5,
                        "display_tr": "5 ms",
                        "display_en": "5 ms",
                    },
                ],
            },
        ],
    },
    "thz": {
        "caption_tr": (
            "THz menzil kısadır; hız bant genişliği ve SNR ile artar. Gbps–mesafe eğrisi "
            "laboratuvar ve satıcı demo sınıfıdır; sokak cep hızı senaryosu değildir."
        ),
        "caption_en": (
            "THz range is short; rate grows with bandwidth and SNR. The Gbps–distance curve is "
            "laboratory and vendor-demo class; not a street handset scenario."
        ),
        "charts": [
            {
                "type": "line",
                "title_tr": "Menzil–hız (sub-THz demo sınıfı)",
                "title_en": "Range–rate (sub-THz demo class)",
                "x_title_tr": "Mesafe",
                "x_title_en": "Distance",
                "y_title_tr": "Veri hızı",
                "y_title_en": "Data rate",
                "x_unit_tr": "m",
                "x_unit_en": "m",
                "y_unit_tr": "Gbps",
                "y_unit_en": "Gbps",
                "points": [
                    {"x": 5, "y": 500, "label_tr": "5 m", "label_en": "5 m"},
                    {"x": 10, "y": 200, "label_tr": "10 m", "label_en": "10 m"},
                    {"x": 30, "y": 50, "label_tr": "30 m", "label_en": "30 m"},
                    {"x": 50, "y": 10, "label_tr": "50 m", "label_en": "50 m"},
                ],
            },
            {
                "type": "bar",
                "title_tr": "Tepe hız — mesafeye göre (demo)",
                "title_en": "Peak rate by distance (demo)",
                "unit_tr": "Gbps",
                "unit_en": "Gbps",
                "metrics": [
                    {
                        "label_tr": "5 m mesafe",
                        "label_en": "5 m distance",
                        "value": 500,
                        "display_tr": "500 Gbps",
                        "display_en": "500 Gbps",
                    },
                    {
                        "label_tr": "50 m mesafe",
                        "label_en": "50 m distance",
                        "value": 10,
                        "display_tr": "10 Gbps",
                        "display_en": "10 Gbps",
                    },
                ],
            },
        ],
    },
    "ai_ran": {
        "caption_tr": (
            "RIC döngü süreleri O-RAN tanımıdır. Enerji yüzdesi literatür/hedef sınıfıdır; "
            "TT fatura ölçümü bu platformda yoktur. Netsia patentleri politika katmanını hedefler."
        ),
        "caption_en": (
            "RIC loop times follow the O-RAN definition. Energy percentages are literature/target "
            "class; no TT bill measurement on this platform. Netsia patents target the policy layer."
        ),
        "charts": [
            {
                "type": "bar",
                "title_tr": "RIC döngü süresi (O-RAN)",
                "title_en": "RIC loop time (O-RAN)",
                "unit_tr": "ms",
                "unit_en": "ms",
                "metrics": [
                    {
                        "label_tr": "Near-RT RIC (xApp)",
                        "label_en": "Near-RT RIC (xApp)",
                        "value": 10,
                        "display_tr": "10 ms",
                        "display_en": "10 ms",
                    },
                    {
                        "label_tr": "Non-RT RIC (rApp)",
                        "label_en": "Non-RT RIC (rApp)",
                        "value": 1000,
                        "display_tr": "1000 ms",
                        "display_en": "1000 ms",
                    },
                    {
                        "label_tr": "Klasik RRM döngüsü",
                        "label_en": "Classic RRM cycle",
                        "value": 100,
                        "display_tr": "100 ms",
                        "display_en": "100 ms",
                    },
                ],
            },
            {
                "type": "bar",
                "title_tr": "Enerji hedefi (literatür sınıfı)",
                "title_en": "Energy target (literature class)",
                "unit_tr": "%",
                "unit_en": "%",
                "metrics": [
                    {
                        "label_tr": "Makro derin uyku hedefi",
                        "label_en": "Macro deep-sleep target",
                        "value": 35,
                        "display_tr": "35 %",
                        "display_en": "35 %",
                    },
                    {
                        "label_tr": "Dinamik PRB kaydırma kazancı",
                        "label_en": "Dynamic PRB shift gain",
                        "value": 20,
                        "display_tr": "20 %",
                        "display_en": "20 %",
                    },
                ],
            },
        ],
    },
    "ntn": {
        "caption_tr": (
            "NTN gecikmesi yörünge ve işlemciden gelir; karasal kule ile aynı değildir. "
            "TT abone şebekesinde Rel-17 direct-to-cell ürünü bu platformda doğrulanmamıştır."
        ),
        "caption_en": (
            "NTN latency comes from orbit and processing; it is not the same as terrestrial towers. "
            "Rel-17 direct-to-cell on the TT retail network is not verified on this platform."
        ),
        "charts": [
            {
                "type": "bar",
                "title_tr": "Tek yön gecikme (literatür sınıfı)",
                "title_en": "One-way latency (literature class)",
                "unit_tr": "ms",
                "unit_en": "ms",
                "metrics": [
                    {
                        "label_tr": "Karasal 5G (şehir)",
                        "label_en": "Terrestrial 5G (urban)",
                        "value": 10,
                        "display_tr": "10 ms",
                        "display_en": "10 ms",
                    },
                    {
                        "label_tr": "LEO NTN",
                        "label_en": "LEO NTN",
                        "value": 25,
                        "display_tr": "25 ms",
                        "display_en": "25 ms",
                    },
                    {
                        "label_tr": "GEO RTT (referans)",
                        "label_en": "GEO RTT (reference)",
                        "value": 250,
                        "display_tr": "250 ms",
                        "display_en": "250 ms",
                    },
                ],
            },
            {
                "type": "bar",
                "title_tr": "Kapsama uzantısı",
                "title_en": "Coverage extension",
                "unit_tr": "km",
                "unit_en": "km",
                "metrics": [
                    {
                        "label_tr": "LEO görünürlük yarıçapı",
                        "label_en": "LEO visibility radius",
                        "value": 500,
                        "display_tr": "500 km",
                        "display_en": "500 km",
                    },
                    {
                        "label_tr": "HAPS stratosfer hücresi",
                        "label_en": "HAPS stratospheric cell",
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
            "Pilsiz etiket menzil ve veri hızı okuyucu gücüne bağlıdır. IoT platformu TT'de "
            "işletilir; Ambient IoT etiket dağıtımı abone şebekesinde doğrulanmamıştır."
        ),
        "caption_en": (
            "Battery-free tag range and rate depend on reader power. The IoT platform is operated "
            "by TT; Ambient IoT tag rollout is not verified on the retail network."
        ),
        "charts": [
            {
                "type": "bar",
                "title_tr": "Okuma menzili (demo sınıfı)",
                "title_en": "Read range (demo class)",
                "unit_tr": "metre",
                "unit_en": "metres",
                "metrics": [
                    {
                        "label_tr": "Depo / kapalı alan",
                        "label_en": "Warehouse / indoor",
                        "value": 15,
                        "display_tr": "15 m",
                        "display_en": "15 m",
                    },
                    {
                        "label_tr": "Açık alan (yüksek güç)",
                        "label_en": "Open area (high power)",
                        "value": 30,
                        "display_tr": "30 m",
                        "display_en": "30 m",
                    },
                ],
            },
            {
                "type": "bar",
                "title_tr": "Veri hızı (demo sınıfı)",
                "title_en": "Data rate (demo class)",
                "unit_tr": "kbps",
                "unit_en": "kbps",
                "metrics": [
                    {
                        "label_tr": "Etiket uplink",
                        "label_en": "Tag uplink",
                        "value": 1,
                        "display_tr": "1 kbps",
                        "display_en": "1 kbps",
                    },
                    {
                        "label_tr": "Sensör burst",
                        "label_en": "Sensor burst",
                        "value": 10,
                        "display_tr": "10 kbps",
                        "display_en": "10 kbps",
                    },
                ],
            },
        ],
    },
}


def get_tech_performance(tech_id: str) -> Dict[str, Any] | None:
    return TECH_PERFORMANCE.get(tech_id)
