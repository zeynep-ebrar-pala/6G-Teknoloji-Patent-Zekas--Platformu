"""
Türk Telekom — Avrupa patent / yayın izi.
Yalnızca Google Patents, DOI veya resmi kurum sayfası ile kilitli kayıtlar.
TR milli başvuru toplamı (basın açıklaması) grafik sayısı olarak kullanılmaz.
EPO (EP) 6G yayın numarası bu kümede doğrulanmadı; boş ofis gizlenmez, uydurulmaz.
"""

from __future__ import annotations

TT_EUROPE_SOURCE = (
    "Google Patents + DOI + Springer Nature Meta API UT "
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
    "KKTC": "#E85A9A",
}

_TR_ALPHA = "abcçdefgğhıijklmnoöprsştuüvyz"
_TR_FOLD = str.maketrans(
    {
        "A": "a",
        "B": "b",
        "C": "c",
        "Ç": "ç",
        "D": "d",
        "E": "e",
        "F": "f",
        "G": "g",
        "Ğ": "ğ",
        "H": "h",
        "I": "ı",
        "İ": "i",
        "J": "j",
        "K": "k",
        "L": "l",
        "M": "m",
        "N": "n",
        "O": "o",
        "Ö": "ö",
        "P": "p",
        "R": "r",
        "S": "s",
        "Ş": "ş",
        "T": "t",
        "U": "u",
        "Ü": "ü",
        "V": "v",
        "Y": "y",
        "Z": "z",
    }
)


def place_sort_key(name: str, lang: str = "tr") -> tuple:
    """Ülke adı sıralaması. TR: Türk abece; EN: casefold."""
    raw = name or ""
    if lang != "tr":
        return (raw.casefold(),)
    folded = raw.translate(_TR_FOLD)
    idxs: list[int] = []
    for ch in folded:
        if ch in _TR_ALPHA:
            idxs.append(_TR_ALPHA.index(ch))
        elif ch == " ":
            idxs.append(-1)
        else:
            idxs.append(200 + ord(ch.lower()) if ch.isalpha() else 400 + ord(ch))
    return tuple(idxs)

# Hukuki assignee Netsia Inc. (Türk Telekom grubu ABD Ar-Ge iştiraki).
# Verdict.co.uk bu aileleri TT'ye atfeder; ofis USPTO, kart açılışı Lens.org.
# Liste yeniden eskiye (2025 → 2023).
TT_GROUP_PATENTS = [
    {
        "id": "US12243096B2",
        "title": "System and method for a RAN exchange",
        "assignee": "Netsia Inc.",
        "group": "Türk Telekom",
        "year": 2025,
        "office": "US",
        "office_label": "USPTO",
        "region": "ABD",
        "domain": "AI-RAN",
        "url": "https://www.lens.org/lens/patent/US_12243096_B2",
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
        "office_label": "USPTO",
        "region": "ABD",
        "domain": "AI-RAN",
        "url": "https://www.lens.org/lens/patent/US_12021560_B1",
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
        "office_label": "USPTO",
        "region": "ABD",
        "domain": "AI-RAN",
        "url": "https://www.lens.org/lens/patent/US_11765049_B2",
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
        "note": (
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
# Kart başlığında Türk Telekom adı açık yazılır; partner adı ikinci plandadır.
TT_EUROPE_TOUCHPOINTS = [
    {
        "country": "SE",
        "country_name_tr": "İsveç",
        "country_name_en": "Sweden",
        "kind": "collaboration",
        "title_tr": "Türk Telekom × Net Insight × Parallel Wireless — GNSS bağımsız senkron / Open RAN",
        "title_en": "Türk Telekom × Net Insight × Parallel Wireless — GNSS-independent sync / Open RAN",
        "detail_tr": (
            "Türk Telekom, İsveç merkezli Net Insight ve Parallel Wireless ile "
            "GPS/GNSS bağımsız senkronizasyonu Open RAN mimarisine taşıma işbirliğini duyurdu. "
            "Precision TimeNet overlay 5G sahada kullanılıyor; 6G standartlarına katkı hedefi "
            "ortak basın metninde yazılıdır. Bu bir EP patent tescili değildir."
        ),
        "detail_en": (
            "Türk Telekom announced a collaboration with Sweden-based Net Insight and Parallel Wireless "
            "to advance GPS/GNSS-independent synchronisation in Open RAN. Precision TimeNet is used "
            "on live 5G; the joint press text targets 6G standards input. This is not an EP grant."
        ),
        "url": "https://netinsight.net/turktelekom-netinsight-parallel-wireless-partner-6g-standard/",
        "year": 2025,
    },
    {
        "country": "ES",
        "country_name_tr": "İspanya",
        "country_name_en": "Spain",
        "kind": "collaboration",
        "title_tr": "Türk Telekom × Ericsson — 6G Ar-Ge / standart MoU (MWC Barcelona)",
        "title_en": "Türk Telekom × Ericsson — 6G R&D / standards MoU (MWC Barcelona)",
        "detail_tr": (
            "Türk Telekom ile Ericsson, 2026 MWC Barcelona’da 6G standardizasyon ve Network-AI "
            "için ortak çalışma grubu kurma mutabakatını imzaladı. İmza yeri İspanya’dır; "
            "çalışmalar Türk Telekom 6G Ar-Ge laboratuvarları ve Ericsson Araştırma Türkiye ile "
            "yürütülecektir. Bu bir EP patent tescili değildir."
        ),
        "detail_en": (
            "Türk Telekom and Ericsson signed an MoU at MWC Barcelona 2026 to form a joint working "
            "group on 6G standardisation and Network-AI. The venue is Spain; work is planned with "
            "Türk Telekom’s 6G R&D labs and Ericsson Research Türkiye. This is not an EP grant."
        ),
        "url": "https://www.ericsson.com/en/press-releases/5/2026/turk-telekom-partners-with-ericsson-to-shape-6g-standards",
        "year": 2026,
    },
    {
        "country": "FR",
        "country_name_tr": "Fransa",
        "country_name_en": "France",
        "kind": "standards",
        "title_tr": "Türk Telekom × InterDigital — ISAC denemesi (ETSI ISAC ISG kavramları)",
        "title_en": "Türk Telekom × InterDigital — ISAC trial (ETSI ISAC ISG concepts)",
        "detail_tr": (
            "Türk Telekom Ankara İnovasyon ve Test Merkezi’nde InterDigital ile "
            "hücresel + Wi-Fi ortak algılama (ön 6G ISAC mimarisi) denemesi duyuruldu. "
            "Mimari kavramlar ETSI ISAC ISG ilk sürümüne dayanır; ETSI merkezi Fransa "
            "(Sophia Antipolis). Deneme yeri Türkiye’dir — Fransa etiketi standart organı içindir."
        ),
        "detail_en": (
            "At Türk Telekom’s Innovation and Test Centre in Ankara, InterDigital and Türk Telekom "
            "announced a collaborative cellular + Wi-Fi sensing trial on a preliminary 6G ISAC "
            "architecture using ETSI ISAC ISG baseline concepts. ETSI is seated in Sophia Antipolis (FR); "
            "the trial site is Türkiye — the France label marks the standards body, not the lab."
        ),
        "url": (
            "https://ir.interdigital.com/news-events/press-releases/news-details/2026/"
            "InterDigital-and-Trk-Telekom-Achieve-Worlds-First-Collaborative-Cellular-and-Wi-Fi-Sensing-"
            "Using-Preliminary-6G-Architecture/default.aspx"
        ),
        "year": 2026,
    },
    {
        "country": "EU",
        "country_name_tr": "EUREKA / CELTIC-NEXT",
        "country_name_en": "EUREKA / CELTIC-NEXT",
        "kind": "project",
        "title_tr": "Türk Telekom — DRIVING-6G konsorsiyum ortağı (CELTIC-NEXT)",
        "title_en": "Türk Telekom — DRIVING-6G consortium partner (CELTIC-NEXT)",
        "detail_tr": (
            "CELTIC-NEXT projesi DRIVING-6G (C2024/2-7) konsorsiyumunda "
            "Türk Telekomünikasyon A.Ş. ortak olarak listelenir (Vestel ve InterDigital Europe ile birlikte). "
            "Proje koordinatörü Danimarka’daki CGC Aps’tir — «Türkiye yürütücülüğü» değildir. "
            "Durum: set-up (Temmuz 2026 – Aralık 2028). Ülke listesi proje sayfasındaki konsorsiyum satırından alınır."
        ),
        "detail_en": (
            "On the CELTIC-NEXT project DRIVING-6G (C2024/2-7), Türk Telekomünikasyon A.Ş. is listed "
            "as a consortium partner (with Vestel and InterDigital Europe among others). "
            "The project coordinator is CGC Aps in Denmark — not a Türkiye lead. "
            "Status: set-up (July 2026 – Dec 2028). Country names follow the consortium list on the project page."
        ),
        "url": "https://www.celticnext.eu/project-driving-6g/",
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

# KAP özel durum açıklaması (Temmuz 2025). ISO-3166-1’de KKTC kodu yok; CYP boyanmaz, KKTC özel GeoJSON ile.
TT_KKTC_SOURCE_URL = (
    "https://www.cnbce.com/borsa/turk-telekom-kktcde-sabit-altyapi-kurmak-icin-sirket-kurdu-h14897"
)
TT_KKTC_POINT = {
    "iso3": "KKTC",
    "geojson_id": "KKTC",
    "layer": "kktc_infra",
    "name_tr": "Kuzey Kıbrıs Türk Cumhuriyeti",
    "name_en": "Turkish Republic of Northern Cyprus",
    "label_tr": (
        "Ne yapıldı: KAP açıklamasına göre Türk Telekom grubu KKTC’de sabit altyapı / perakende "
        "hizmet için şirket kurma kararı aldı (Temmuz 2025; ~100 milyon USD yatırım hedefi duyuruldu). "
        "Bu haritada abone sayısı veya tamamlanmış fiber şebeke çizilmez; kaynak karar/yatırım duyurusudur. "
        "Güney Kıbrıs (CYP) bu kaynakta yoktur."
    ),
    "label_en": (
        "What was done: per KAP disclosure, the Türk Telekom group decided to form companies in "
        "Northern Cyprus for fixed infrastructure / retail services (July 2025; ~USD 100m investment "
        "target announced). This map does not draw subscriber counts or a finished fibre network — "
        "the source is the decision/investment notice. The Republic of Cyprus (CYP) is not in this source."
    ),
    "color": "#E85A9A",
    "source_url": TT_KKTC_SOURCE_URL,
}

# 6G Ar-Ge dokunuşları — harita ISO-3 (EUREKA ülke değil, boyanmaz)
TT_MAP_RD = [
    {
        "iso3": "TUR",
        "layer": "hq",
        "label_tr": (
            "Ne yapıldı: Türkiye, Türk Telekom’un operatör merkezi ve 6G Ar-Ge üssüdür. "
            "Abone şebekesi burada işletilir; kilitli DOI makalelerinde yazar bağlılığı da buraya yazılır."
        ),
        "label_en": (
            "What was done: Türkiye is Türk Telekom’s operator HQ and 6G R&D base. "
            "The retail network is run here; locked DOI papers with TT affiliation are counted here."
        ),
    },
    {
        "iso3": "SWE",
        "layer": "rd_collab",
        "label_tr": (
            "Ne yapıldı: İsveç merkezli Net Insight ile GNSS bağımsız senkron / Open RAN işbirliği duyuruldu. "
            "İsveç’te TT abone şebekesi olduğu anlamına gelmez — partner şirketin ülkesi boyanır."
        ),
        "label_en": (
            "What was done: collaboration with Sweden-based Net Insight on GNSS-independent sync / Open RAN. "
            "This does not mean TT runs a retail network in Sweden — the partner’s country is painted."
        ),
    },
    {
        "iso3": "ESP",
        "layer": "mou_venue",
        "label_tr": (
            "Ne yapıldı: Ericsson ile 6G Ar-Ge / standart MoU, MWC Barcelona’da imzalandı. "
            "Boyanan yer imza mekânıdır; İspanya’da TT abone şebekesi iddiası değildir."
        ),
        "label_en": (
            "What was done: 6G R&D / standards MoU with Ericsson signed at MWC Barcelona. "
            "The painted place is the signing venue — not a Spanish retail-network claim."
        ),
    },
    {
        "iso3": "FRA",
        "layer": "standards",
        "label_tr": (
            "Ne yapıldı: İlgili ISAC denemesi Ankara’dadır; Fransa, ETSI standart organının merkezidir "
            "(Sophia Antipolis). Fransa’da TT toptan first-mover veya abone şebekesi iddiası değildir."
        ),
        "label_en": (
            "What was done: the related ISAC trial is in Ankara; France is painted as ETSI’s seat "
            "(Sophia Antipolis). This is not a French wholesale first-mover or retail-network claim."
        ),
    },
]

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
