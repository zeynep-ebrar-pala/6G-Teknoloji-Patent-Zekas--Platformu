"""
Türk Telekom — Avrupa patent / yayın izi.
Yalnızca Google Patents, DOI veya resmi kurum sayfası ile kilitli kayıtlar.
TR milli başvuru toplamı (basın açıklaması) grafik sayısı olarak kullanılmaz.
EPO (EP) 6G yayın numarası bu kümede doğrulanmadı; boş ofis gizlenmez, uydurulmaz.
"""

from __future__ import annotations

TT_EUROPE_SOURCE = (
    "Google Patents + DOI + WoS Core Collection UT "
    "(oturumda açılan tam kayıt) + resmi ortak duyuruları"
)

# Haritada her ülke ayrı renk (katman rengi değil).
TT_COUNTRY_COLORS = {
    "TUR": "#E20074",
    "HUN": "#3B82F6",
    "ROU": "#22C55E",
    "BGR": "#F97316",
    "SRB": "#A855F7",
    "UKR": "#EAB308",
    "SWE": "#818CF8",
    "ESP": "#14B8A6",
    "FRA": "#FFB020",
}

# Hukuki assignee Netsia Inc. (Türk Telekom grubu ABD Ar-Ge iştiraki).
# Verdict.co.uk bu aileleri TT'ye atfeder; Google Patents kaydı Netsia'dır.
# Liste yeniden eskiye (2025 → 2023).
TT_GROUP_PATENTS = [
    {
        "id": "US12243096B2",
        "title": "System and method for a RAN exchange",
        "assignee": "Netsia Inc.",
        "group": "Türk Telekom",
        "year": 2025,
        "office": "US",
        "office_label": "Google Patents",
        "region": "ABD",
        "domain": "AI-RAN",
        "url": "https://patents.google.com/patent/US12243096B2/en",
        "abstract": (
            "Kullanılmayan baz istasyonu kapasitesinin dilim olarak ilan/kiralanması (RANxChange); "
            "programlanabilir RAN (Radio Access Network — radyo erişim ağı)."
        ),
    },
    {
        "id": "US12021560B1",
        "title": "Apparatus and method for joint profile-based slicing of mobile access and optical backhaul",
        "assignee": "Netsia Inc.",
        "group": "Türk Telekom",
        "year": 2024,
        "office": "US",
        "office_label": "Google Patents",
        "region": "ABD",
        "domain": "AI-RAN",
        "url": "https://patents.google.com/patent/US12021560B1/en",
        "abstract": (
            "RAN (Radio Access Network — radyo erişim ağı) ve PON (Passive Optical Network — pasif optik ağ) "
            "denetleyicilerini ortak kesit (slice) profiline bağlayan erişim+backhaul dilimleme; "
            "5G/ötesi ağ dilimlemesi."
        ),
    },
    {
        "id": "US11765049B2",
        "title": "Slice assurance within a mobile network",
        "assignee": "Netsia Inc.",
        "group": "Türk Telekom",
        "year": 2023,
        "office": "US",
        "office_label": "Google Patents",
        "region": "ABD",
        "domain": "AI-RAN",
        "url": "https://patents.google.com/patent/US11765049B2/en",
        "abstract": (
            "RIC (RAN Intelligent Controller — RAN zekâ denetleyicisi) altında dilim güvence işlevi; "
            "SLA (Service Level Agreement — hizmet seviyesi anlaşması) sapınca kaynak yeniden dağıtımı."
        ),
    },
]

# Ham bağlılık metni Türk Telekom / Türkiye.
# Ülke kodu raw affiliation'dan TR (indeks grafı başka ülkeye düşmesin).
# Liste yeniden eskiye (2026 → 2025).
TT_AFFILIATED_PAPERS = [
    {
        "title": "Agentic AI-Based 5G and Beyond Radio Planning Framework",
        "authors": "M. G. Tezcan, A. Yazar, S. N. Karahan, M. S. Osmanca, H. O. Altun",
        "journal": "IEEE Access",
        "year": 2026,
        "doi": "10.1109/access.2026.3691411",
        "topic": "AI-RAN",
        "source": "DOI",
        "source_url": "https://doi.org/10.1109/access.2026.3691411",
        "url": "https://doi.org/10.1109/access.2026.3691411",
        "affiliation_country": "TR",
        "wos_ut": "WOS:001767283200006",
        "note": (
            "WoS Core Collection tam kayıt: WOS:001767283200006. "
            "Yazar bağlılığı Türk Telekom Ar-Ge (Ankara) + Boğaziçi Üniversitesi’dir."
        ),
    },
    {
        "title": "Artificial intelligence for next-generation 6G technologies and networks",
        "authors": "Y. E. Tok, A. G. Toprak, S. N. Karahan, Ö. B. Mercan, H. M. Aydin, M. Altintas",
        "journal": "Discover Networks",
        "year": 2026,
        "doi": "10.1007/s44354-026-00016-3",
        "topic": "AI-RAN",
        "source": "Springer",
        "source_url": "https://doi.org/10.1007/s44354-026-00016-3",
        "url": "https://doi.org/10.1007/s44354-026-00016-3",
        "affiliation_country": "TR",
        "note": "",
    },
    {
        "title": (
            "AI-Driven Network Slicing for F5G-A Networks: A Framework With Unsupervised Discovery, "
            "Temporal Dynamics, and Explainable AI"
        ),
        "authors": "S. N. Karahan, M. Güllü, S. Çimen, A. Yazar, M. S. Osmanca",
        "journal": "IEEE Open Journal of the Communications Society",
        "year": 2026,
        "doi": "10.1109/ojcoms.2026.3679199",
        "topic": "AI-RAN",
        "source": "DOI",
        "source_url": "https://doi.org/10.1109/ojcoms.2026.3679199",
        "url": "https://doi.org/10.1109/ojcoms.2026.3679199",
        "affiliation_country": "TR",
        "note": "",
    },
    {
        "title": (
            "Realistic Performance Assessment of Machine Learning Algorithms for 6G Network Slicing: "
            "A Dual-Methodology Approach with Explainable AI Integration"
        ),
        "authors": "S. N. Karahan, M. Güllü, D. Karhan, S. Çimen, M. S. Osmanca, N. Barışçı",
        "journal": "Electronics",
        "year": 2025,
        "doi": "10.3390/electronics14193841",
        "topic": "AI-RAN",
        "source": "MDPI / DOI",
        "source_url": "https://doi.org/10.3390/electronics14193841",
        "url": "https://doi.org/10.3390/electronics14193841",
        "affiliation_country": "TR",
        "note": "",
    },
    {
        "title": (
            "Independent Time Transfer in 5G Technology Over IP Core Networks Using PTN Overlay "
            "and Comparison With GPS/GNSS-Based Synchronization"
        ),
        "authors": "M. S. Osmanca, U. Keten, Y. İ. Demır, K. Zaim",
        "journal": "IEEE Access",
        "year": 2025,
        "doi": "10.1109/access.2025.3611321",
        "topic": "AI-RAN",
        "source": "DOI",
        "source_url": "https://doi.org/10.1109/access.2025.3611321",
        "url": "https://doi.org/10.1109/access.2025.3611321",
        "affiliation_country": "TR",
        "note": (
            "Yazar bağlılığı Ankara, Türk Telekom Ar-Ge'dir."
        ),
    },
]

# Avrupa ülkesi = işbirliği / standart organı / etkinlik. Patent ofisi sayısı değildir.
TT_EUROPE_TOUCHPOINTS = [
    {
        "country": "SE",
        "country_name_tr": "İsveç",
        "country_name_en": "Sweden",
        "kind": "collaboration",
        "title_tr": "Net Insight — GNSS bağımsız senkronizasyon / Open RAN",
        "title_en": "Net Insight — GNSS-independent sync / Open RAN",
        "detail_tr": (
            "Precision TimeNet overlay; 5G sahada, 6G Open RAN senkronizasyonu için Parallel Wireless ile genişletme. "
            "İsveç PTS’nin GNSS bağımsız senkron zorunluluğu vaka metninde bağlam olarak geçer."
        ),
        "detail_en": (
            "Precision TimeNet overlay; live 5G, extended toward 6G Open RAN sync with Parallel Wireless. "
            "The Swedish PTS GNSS-independence rule is cited as regulatory context in the case study."
        ),
        "url": "https://netinsight.net/turktelekom-netinsight-parallel-wireless-partner-6g-standard/",
        "year": 2025,
    },
    {
        "country": "ES",
        "country_name_tr": "İspanya",
        "country_name_en": "Spain",
        "kind": "collaboration",
        "title_tr": "Ericsson — 6G standart MoU (MWC Barcelona)",
        "title_en": "Ericsson — 6G standards MoU (MWC Barcelona)",
        "detail_tr": (
            "2026 MWC Barcelona’da imzalanan Ar-Ge mutabakatı: ikili projeler ve 6G standart katkısı. "
            "İmza yeri İspanya’dır; bu bir EP patent tescili değildir."
        ),
        "detail_en": (
            "R&D memorandum signed at MWC Barcelona 2026: bilateral projects and 6G standards input. "
            "The venue is Spain; it is not an EP grant."
        ),
        "url": "https://www.ericsson.com/en/press-releases/5/2026/turk-telekom-partners-with-ericsson-to-shape-6g-standards",
        "year": 2026,
    },
    {
        "country": "FR",
        "country_name_tr": "Fransa",
        "country_name_en": "France",
        "kind": "standards",
        "title_tr": "ETSI ISAC ISG — hücresel + Wi-Fi ortak algılama denemesi",
        "title_en": "ETSI ISAC ISG — collaborative cellular + Wi-Fi sensing trial",
        "detail_tr": (
            "InterDigital ile Ankara test merkezinde ön 6G ISAC mimarisi; ETSI ISAC ISG taban kavramları. "
            "ETSI merkezi Sophia Antipolis (FR). Deneme yeri Türkiye’dir."
        ),
        "detail_en": (
            "Trial with InterDigital at the Ankara test centre on preliminary 6G ISAC architecture, "
            "using ETSI ISAC ISG baseline concepts. ETSI is seated in Sophia Antipolis (FR). The trial site is Türkiye."
        ),
        "url": "https://www.marketscreener.com/news/interdigital-and-turk-telekom-achieve-world-s-first-collaborative-cellular-and-wi-fi-sensing-using-p-ce7e5dd2d18bf027",
        "year": 2026,
    },
    {
        "country": "EU",
        "country_name_tr": "EUREKA / CELTIC-NEXT",
        "country_name_en": "EUREKA / CELTIC-NEXT",
        "kind": "project",
        "title_tr": "DRIVING-6G — AI-native 6G (Türkiye yürütücülüğü)",
        "title_en": "DRIVING-6G — AI-native 6G (Türkiye lead)",
        "detail_tr": (
            "EUREKA CELTIC-NEXT kümesinde 8 ülkeden 12 kuruluş. Ülke tek tek listesi bu platformda "
            "proje sözleşmesinden doğrulanmadı; sayı uydurulmaz."
        ),
        "detail_en": (
            "EUREKA CELTIC-NEXT cluster: 12 organisations from 8 countries. Individual country names "
            "were not verified from the grant text on this platform; they are not invented."
        ),
        "url": "https://celticnext.eu/",
        "year": 2026,
    },
]

# TTI resmi sayfa: toptan CEE ilk pazarlar (ülke listesi bu cümleden; 19/24'ün kalanı boyanmaz).
# Kaynak: https://www.turktelekomint.com/about-us
TTI_WHOLESALE_FIRST_MOVER = [
    {"iso3": "HUN", "cc": "HU", "name_tr": "Macaristan", "name_en": "Hungary"},
    {"iso3": "ROU", "cc": "RO", "name_tr": "Romanya", "name_en": "Romania"},
    {"iso3": "BGR", "cc": "BG", "name_tr": "Bulgaristan", "name_en": "Bulgaria"},
    {"iso3": "SRB", "cc": "RS", "name_tr": "Sırbistan", "name_en": "Serbia"},
    {"iso3": "UKR", "cc": "UA", "name_tr": "Ukrayna", "name_en": "Ukraine"},
    {"iso3": "TUR", "cc": "TR", "name_tr": "Türkiye", "name_en": "Türkiye"},
]

TTI_ABOUT_URL = "https://www.turktelekomint.com/about-us"
TT_IR_2024_URL = "https://www.ttyatirimciiliskileri.com.tr/media/l10mbc5l/2024-integrated-annual-report.pdf"

# Entegre faaliyet raporu 2024 — ülke adları raporda yok; haritaya 24 ülke basılmaz.
TT_IR_WHOLESALE = {
    "pop_floor": 135,
    "countries_claimed": 24,
    "attribution_tr": (
        "TT 2024 Entegre Faaliyet Raporu: «135+ PoP, 24 ülke». Hangi 24 ülke yazılmadığı için "
        "haritada 24 ülke boyanmaz. TTI About: ağ 19 ülke; çelişen toplamlar ayrı kaynak, birleştirilmez."
    ),
    "attribution_en": (
        "TT 2024 Integrated Annual Report: “135+ PoPs in 24 countries”. The 24 names are not listed, "
        "so the map does not paint 24 countries. TTI About says 19 countries; the two totals stay separate."
    ),
}

# 6G Ar-Ge dokunuşları — harita ISO-3 (EUREKA ülke değil, boyanmaz)
TT_MAP_RD = [
    {
        "iso3": "TUR",
        "layer": "hq",
        "label_tr": "Merkez; operatör Ar-Ge (Araştırma ve Geliştirme)",
        "label_en": "HQ; operator R&D (research and development)",
    },
    {
        "iso3": "SWE",
        "layer": "rd_collab",
        "label_tr": "6G Ar-Ge (Araştırma ve Geliştirme) ortağı: Net Insight",
        "label_en": "6G R&D (research and development) partner: Net Insight",
    },
    {
        "iso3": "ESP",
        "layer": "mou_venue",
        "label_tr": "MoU (Memorandum of Understanding — mutabakat zaptı) imza yeri: MWC Barcelona",
        "label_en": "MoU (memorandum of understanding) signing venue: MWC Barcelona",
    },
    {
        "iso3": "FRA",
        "layer": "standards",
        "label_tr": "ETSI (European Telecommunications Standards Institute — Avrupa Telekomünikasyon Standartları Enstitüsü) merkezi; deneme Ankara’da",
        "label_en": "ETSI (European Telecommunications Standards Institute) seat; trial in Ankara",
    },
]

TT_PRESS_CLAIMS = {
    "tr_filings_2025": 921,
    "attribution_tr": (
        "Türk Telekom / Sanayi ve Teknoloji Bakanlığı 2025 açıklaması (milli patent başvurusu). "
        "Bu platform her TR dosyasını Google Patents’te tek tek doğrulamadı; çubuğa işlenmez."
    ),
    "attribution_en": (
        "Türk Telekom / Ministry of Industry and Technology 2025 statement (national filings). "
        "This platform did not verify each TR dossier on Google Patents; it is not plotted."
    ),
    "url": "https://www.aa.com.tr/tr/isdunyasi/bilisim/turk-telekom-patent-basvurusunda-zirvede/701271",
}
