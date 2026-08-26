"""
Ortak teknik sözlük — ilk kullanımda açılım, sonra kısaltma.
Biçim: KISALTMA (English — Türkçe): tanım + neden önemli.
"""

from __future__ import annotations

from typing import Any

GLOSSARY: dict[str, dict[str, str]] = {
    "TRL": {
        "abbr": "TRL",
        "en": "Technology Readiness Level",
        "tr": "Teknoloji Hazırlık Seviyesi",
        "definition": (
            "Bir teknolojinin laboratuvar fikrinden gerçek saha koşullarında doğrulanmış "
            "olgun ürüne kadar hangi aşamada olduğunu 1–9 ölçeğinde gösteren ölçüttür."
        ),
        "why": (
            "Pazarlama vaadi ile saha olgunluğunu ayırır. Operatör, yatırım ve standart "
            "kararını 'ne kadar hazır?' sorusuna bağlar."
        ),
    },
    "ISAC": {
        "abbr": "ISAC",
        "en": "Integrated Sensing and Communication",
        "tr": "Entegre Algılama ve İletişim",
        "definition": (
            "Aynı radyo kaynağı, aynı dalga şekli ve çoğu zaman aynı donanım üzerinde "
            "hem veri iletimi hem çevre algılamanın (mesafe, hız, açı) birlikte tasarlanmasıdır."
        ),
        "why": "Ayrı radar spektrumu ve ayrı anten maliyeti olmadan şebekeye farkındalık katar.",
    },
    "RIS": {
        "abbr": "RIS",
        "en": "Reconfigurable Intelligent Surface",
        "tr": "Yeniden Yapılandırılabilir Akıllı Yüzey",
        "definition": (
            "Gelen elektromanyetik dalganın fazını (ve bazen genliğini) eleman eleman "
            "ayarlayarak yansıma yönünü kontrol eden, çoğu zaman aktif RF zinciri içermeyen yüzeydir."
        ),
        "why": "Yeni kule dikmeden kör noktayı kapatmak ve enerjiyi hedefe yönlendirmek için kullanılır.",
    },
    "NTN": {
        "abbr": "NTN",
        "en": "Non-Terrestrial Network",
        "tr": "Karasal Olmayan Ağ",
        "definition": (
            "LEO/GEO uydu, HAPS veya benzeri hava/uzay düğümlerini karasal 3GPP şebekesiyle "
            "tek sistem gibi işleten mimaridir."
        ),
        "why": "Kule ve fiberin yetişmediği coğrafya ile afet yedek hattını aynı protokol ailesine bağlar.",
    },
    "MIMO": {
        "abbr": "MIMO",
        "en": "Multiple-Input Multiple-Output",
        "tr": "Çoklu Giriş Çoklu Çıkış",
        "definition": (
            "Birden fazla verici ve alıcı anten kullanarak aynı anda birden fazla uzamsal "
            "akış taşıyan veya hüzme şekillendiren anten tekniğidir."
        ),
        "why": "Spektrumu çoğaltmadan kapasite ve bağlantı güvenilirliğini artırır.",
    },
    "MNO": {
        "abbr": "MNO",
        "en": "Mobile Network Operator",
        "tr": "Mobil Şebeke İşletmecisi",
        "definition": (
            "Kendi radyo spektrumu ve erişim şebekesiyle aboneye mobil hizmet veren lisanslı işletmecidir "
            "(sanal operatör MVNO değildir)."
        ),
        "why": (
            "Avrupa yayın grafiğinde ülke başına kilitli üç firmanın hangisinin 6G literatüründe "
            "daha görünür olduğunu karşılaştırmanın birimidir."
        ),
    },
    "OFDM": {
        "abbr": "OFDM",
        "en": "Orthogonal Frequency-Division Multiplexing",
        "tr": "Dik Frekans Bölmeli Çoğullama",
        "definition": (
            "Geniş bandı birbirine dik alt taşıyıcılara bölen çok taşıyıcılı modülasyondur; "
            "4G/5G hava arayüzünün temelidir."
        ),
        "why": "Frekans seçici sönümlenmeyi yönetilebilir kılar; 6G'de ISAC dalga şekli adaylarından biridir.",
    },
    "OTFS": {
        "abbr": "OTFS",
        "en": "Orthogonal Time Frequency Space",
        "tr": "Dik Zaman-Frekans Uzayı",
        "definition": (
            "Sembolleri gecikme-Doppler düzleminde yerleştiren, yüksek hareketliliğe "
            "karşı OFDM'e göre daha dayanıklı bir dalga şekli ailesidir."
        ),
        "why": "ISAC ve yüksek hızlı senaryolarda kanalın hem gecikme hem Doppler yapısını birlikte kullanır.",
    },
    "CRB": {
        "abbr": "CRB",
        "en": "Cramér-Rao Bound",
        "tr": "Cramér-Rao Sınırı",
        "definition": (
            "Yansız bir kestiricinin varyansı için teorik alt sınırdır; algılamada açı/mesafe/hız "
            "hassasiyetinin 'daha iyisi fiziken mümkün değil' tabanını verir."
        ),
        "why": "ISAC'de iletişim hızı ile algılama hassasiyeti arasındaki ödünleşimi niceler.",
    },
    "SNR": {
        "abbr": "SNR",
        "en": "Signal-to-Noise Ratio",
        "tr": "Sinyal-Gürültü Oranı",
        "definition": "İstenen sinyal gücünün gürültü gücüne oranıdır; birimsiz veya desibel (dB) ile verilir.",
        "why": "Hem bit hatasını hem radar tespit olasılığını sınırlayan temel kalite ölçütüdür.",
    },
    "SINR": {
        "abbr": "SINR",
        "en": "Signal-to-Interference-plus-Noise Ratio",
        "tr": "Sinyal-Parazit-artı-Gürültü Oranı",
        "definition": (
            "İstenen sinyal gücünün, diğer kullanıcıların paraziti ile ısıl gürültünün toplamına oranıdır."
        ),
        "why": "Hücresel ve hücresiz MIMO'da gerçek kapasiteyi SNR'den daha doğru temsil eder.",
    },
    "RF": {
        "abbr": "RF",
        "en": "Radio Frequency",
        "tr": "Radyo Frekansı",
        "definition": "Kablosuz haberleşmede kullanılan elektromanyetik spektrum dilimidir (kHz–yüzlerce GHz).",
        "why": "Anten, transiver ve spektrum düzenlemesinin ortak dilidir.",
    },
    "GHz": {
        "abbr": "GHz",
        "en": "Gigahertz",
        "tr": "Gigahertz",
        "definition": "Saniyede bir milyar salınım; 10⁹ Hz. 5G/6G taşıyıcı frekanslarının yaygın birimidir.",
        "why": "Frekans yükseldikçe bant genişliği artar, menzil ve duvar geçişi zorlaşır.",
    },
    "gNB": {
        "abbr": "gNB",
        "en": "next-generation Node B",
        "tr": "5G/6G baz istasyonu düğümü",
        "definition": "3GPP NR mimarisinde kullanıcı cihazına radyo bağlantısı sağlayan baz istasyonu varlığıdır.",
        "why": "Diyagram ve standart metinlerinde 'kule'nin resmi adıdır.",
    },
    "UE": {
        "abbr": "UE",
        "en": "User Equipment",
        "tr": "Kullanıcı Cihazı",
        "definition": "Telefon, modem veya 3GPP'ye bağlı uç cihazdır.",
        "why": "Standartlar aboneyi değil UE'yi konuşur; kapsama ve yetenek UE sınıfına bağlıdır.",
    },
    "AoA": {
        "abbr": "AoA",
        "en": "Angle of Arrival",
        "tr": "Geliş Açısı",
        "definition": "Alıcı anten dizisine gelen dalganın doğrultusudur; dizi faz farkından kestirilir.",
        "why": "ISAC konumlandırmada mesafe (gecikme) ile birlikte 2B/3B konumu tamamlar.",
    },
    "Doppler": {
        "abbr": "Doppler",
        "en": "Doppler shift",
        "tr": "Doppler kayması",
        "definition": (
            "Kaynak veya yansıtıcı hareket ettiğinde alınan frekansın taşıyıcıdan sapmasıdır; "
            "hızın radyal bileşeniyle orantılıdır."
        ),
        "why": "Radar hız ölçümü ve LEO uydu senkronizasyonu bu kaymayı okumak/düzeltmek zorundadır.",
    },
    "O-RAN": {
        "abbr": "O-RAN",
        "en": "Open Radio Access Network",
        "tr": "Açık Telsiz Erişim Ağı",
        "definition": (
            "RAN işlevlerini açık arayüzlerle ayıran, çok tedarikçili donanım/yazılım "
            "entegrasyonunu hedefleyen mimari çerçevedir."
        ),
        "why": "AI-RAN uygulamalarının (xApp/rApp) çalıştığı denetleyici katmanını standartlaştırır.",
    },
    "RIC": {
        "abbr": "RIC",
        "en": "RAN Intelligent Controller",
        "tr": "RAN Akıllı Denetleyici",
        "definition": (
            "O-RAN'da radyo kaynak politikalarını yazılım uygulamalarıyla yöneten denetleyicidir; "
            "Near-RT (yakın gerçek zaman) ve Non-RT (gerçek zaman dışı) döngüleri vardır."
        ),
        "why": "Şebeke ayarının 'insan tarife yazar' modelinden yazılım döngüsüne geçiş noktasıdır.",
    },
    "PHY": {
        "abbr": "PHY",
        "en": "Physical layer",
        "tr": "Fiziksel katman",
        "definition": "Bitlerin elektromanyetik dalgaya (modülasyon, kodlama, anten) dönüştüğü katmandır.",
        "why": "Dalga şekli, SNR ve algılama algoritmalarının yaşadığı yerdir.",
    },
    "MAC": {
        "abbr": "MAC",
        "en": "Medium Access Control",
        "tr": "Ortam Erişim Denetimi",
        "definition": "Kim, ne zaman, hangi kaynak bloğunu kullanır sorusunu çözen protokol katmanıdır.",
        "why": "ISAC kaynak paylaşımı ve hücresiz ön kodlama zamanlaması MAC ile PHY'nin kesişiminde durur.",
    },
    "KPI": {
        "abbr": "KPI",
        "en": "Key Performance Indicator",
        "tr": "Anahtar Performans Göstergesi",
        "definition": "Bir hedefin sayısal izleme ölçütüdür (hız, gecikme, kapsama, enerji).",
        "why": "Senaryo motorundaki sayılar saha ölçümü değil, kural tabanlı göstergedir; buna göre okunmalıdır.",
    },
    "CAPEX": {
        "abbr": "CAPEX",
        "en": "Capital Expenditure",
        "tr": "Sermaye Gideri",
        "definition": "Şebekeyi kurmak veya büyütmek için yapılan yatırım harcamasıdır (kule, fiber, uydu kapasitesi).",
        "why": "Operatör kararında OPEX (işletme gideri) ile birlikte teknolojinin 'neden pahalı/ucuz' cevabını verir.",
    },
    "DOI": {
        "abbr": "DOI",
        "en": "Digital Object Identifier",
        "tr": "Dijital Nesne Tanımlayıcı",
        "definition": "Bir akademik yayına kalıcı, çözümlenebilir kimlik veren uluslararası tanımlayıcıdır.",
        "why": "Makalenin 'gerçekten var ve tarayıcıda açılır' kanıtıdır; uydurma atıfın panzehiridir.",
    },
    "TF-IDF": {
        "abbr": "TF-IDF",
        "en": "Term Frequency–Inverse Document Frequency",
        "tr": "Terim Sıklığı–Ters Belge Sıklığı",
        "definition": (
            "Bir sözcüğün bir belgede ne kadar öne çıktığını, o sözcüğün derlemede ne kadar "
            "yaygın olduğuna göre ağırlıklandıran istatistiksel ölçüttür."
        ),
        "why": "Patent haritası ve AI asistan geri getirmesi bu skorla 'hangi kayıt bu soruya yakın?' der; anlam çıkarmaz.",
    },
    "3GPP": {
        "abbr": "3GPP",
        "en": "3rd Generation Partnership Project",
        "tr": "3. Nesil Ortaklık Projesi",
        "definition": (
            "2G'den 6G'ye mobil şebeke teknik şartnamelerini yazan uluslararası standartlaşma ortaklığıdır. "
            "Sürümler (Release) özellik paketleridir."
        ),
        "why": "Bir özelliğin 'araştırma fikri' mi 'şebekeye girebilir şartname' mi olduğunu ayırır.",
    },
    "LEO": {
        "abbr": "LEO",
        "en": "Low Earth Orbit",
        "tr": "Alçak Dünya Yörüngesi",
        "definition": "Yaklaşık 300–2000 km irtifadaki yörüngedir; 6G NTN'de sık anılan dilim ~500–1200 km'dir.",
        "why": "GEO'ya göre gecikme düşüktür ama uydu hızlı hareket eder; Doppler ve sık handover doğar.",
    },
    "GEO": {
        "abbr": "GEO",
        "en": "Geostationary Earth Orbit",
        "tr": "Yer Sabit Yörünge",
        "definition": "Ekvator üzerinde ~36 000 km'de, yerde sabit görünen yörüngedir.",
        "why": "Az uyduyla geniş kapsama verir; gecikme LEO'dan belirgin yüksektir, doğrudan cep için daha zordur.",
    },
    "HAPS": {
        "abbr": "HAPS",
        "en": "High-Altitude Platform Station",
        "tr": "Yüksek İrtifa Platform İstasyonu",
        "definition": "Stratosferde (tipik ~20 km) duran zeplin, uçak veya benzeri haberleşme platformudur.",
        "why": "Kule ile uydu arasında bir katman: bölgesel kapsama, uyduya göre daha düşük gecikme.",
    },
    "FSPL": {
        "abbr": "FSPL",
        "en": "Free-Space Path Loss",
        "tr": "Serbest Uzay Yol Kaybı",
        "definition": (
            "Engel ve atmosfer emilimi yokken, küresel yayılan dalganın mesafe ve frekansla "
            "geometrik olarak zayıflamasıdır."
        ),
        "why": "NTN ve THz menzil hesabının ilk terimidir; gerçek kanal buna emilim ve engel ekler.",
    },
    "MMSE": {
        "abbr": "MMSE",
        "en": "Minimum Mean Square Error",
        "tr": "Minimum Ortalama Kare Hata",
        "definition": (
            "Kestirim veya denkleştirmede beklenen karesel hatayı küçülten istatistiksel ölçüttür; "
            "hücresiz MIMO'da kanal kestirimi ve ön kodlamada yaygındır."
        ),
        "why": "Paraziti yok sayan kaba yöntemlere göre gürültü-parazit dengesini hesaba katar.",
    },
    "DFRC": {
        "abbr": "DFRC",
        "en": "Dual-Functional Radar-Communication",
        "tr": "Çift İşlevli Radar-Haberleşme",
        "definition": "Tek dalga şeklinin hem radar problama hem iletişim sembolü taşıyacak şekilde tasarlanmasıdır.",
        "why": "ISAC'in donanım/dalga şekli paylaşımını 'iki ayrı sistem yan yana' çözümünden ayırır.",
    },
    "JCR": {
        "abbr": "JCR",
        "en": "Joint Communication and Radar / Sensing",
        "tr": "Ortak Haberleşme ve Radar/Algılama",
        "definition": "Kaynak, dalga şekli ve işlemeyi iletişim ile algılama için birlikte optimize etme yaklaşımıdır.",
        "why": "Ayrı radar + ayrı şebeke yerine spektrum ve antenin çift kullanımını ifade eder.",
    },
    "EPO": {
        "abbr": "EPO",
        "en": "European Patent Office",
        "tr": "Avrupa Patent Ofisi",
        "definition": (
            "Avrupa Patent Sözleşmesi (EPC) üyeleri için tek başvuru ile bölgesel inceleme yapan ofistir. "
            "Verilen EP patenti, seçilen üye ülkelerde ayrıca yürürlüğe konur (validation)."
        ),
        "why": (
            "TR milli başvuru Almanya'yı korumaz; Avrupa'da hak için EP (veya her ülkede ayrı ulusal) yol gerekir. "
            "Türkiye EPO üyesidir; üyelik, otomatik EP tescili demek değildir."
        ),
    },
    "PCT": {
        "abbr": "PCT",
        "en": "Patent Cooperation Treaty",
        "tr": "Patent İşbirliği Anlaşması",
        "definition": (
            "WIPO nezdinde uluslararası başvuru (WO) yoludur. Tek başına tescil vermez; "
            "sonra ulusal/bölgesel faza (EP, US, TR…) girilir."
        ),
        "why": "WO numarası 'dünya patenti' değildir; hangi ofiste hak doğduğunu publication prefix söyler (EP, US, TR).",
    },
    "API": {
        "abbr": "API",
        "en": "Application Programming Interface",
        "tr": "Uygulama Programlama Arayüzü",
        "definition": "Bir yazılımın başka yazılımlara sunduğu kurallı çağrı yüzüdür.",
        "why": "Springer Nature Meta API, Lens.org ve isteğe bağlı LLM sağlayıcıları bu platforma API ile bağlanır.",
    },
    "SDK": {
        "abbr": "SDK",
        "en": "Software Development Kit",
        "tr": "Yazılım Geliştirme Kiti",
        "definition": "Bir platformda uygulama yazmak için kütüphane, araç ve belgeler paketidir.",
        "why": "AI-RAN ve RIC uygulamaları çoğu zaman satıcı SDK'sı üzerinde durur; standart değil araçtır.",
    },
    "AI": {
        "abbr": "AI",
        "en": "Artificial Intelligence",
        "tr": "Yapay Zekâ",
        "definition": "Veriden örüntü öğrenip karar veya kestirim üreten hesaplama yöntemleri ailesidir.",
        "why": "Bu platformda hem şebeke denetimi (AI-RAN) hem asistan yanıtı bağlamında geçer; ikisi farklı işlerdir.",
    },
    "ML": {
        "abbr": "ML",
        "en": "Machine Learning",
        "tr": "Makine Öğrenmesi",
        "definition": "Açıkça her kuralı kodlamak yerine örneklerden parametre öğrenen AI alt kümesidir.",
        "why": "3GPP 'AI/ML for NR' çalışma kalemleri ve RIC xApp'leri bu terimle anılır.",
    },
    "CAD": {
        "abbr": "CAD",
        "en": "Computer-Aided Design",
        "tr": "Bilgisayar Destekli Tasarım",
        "definition": "Donanım ve anten geometrisinin sayısal ortamda tasarlanmasıdır.",
        "why": "RIS elemanı ve THz paket anteni üretimden önce CAD ile çizilir; şebeke protokolü değildir.",
    },
    "EMC": {
        "abbr": "EMC",
        "en": "Electromagnetic Compatibility",
        "tr": "Elektromanyetik Uyumluluk",
        "definition": "Cihazın hem kendi yayınını yönetmesi hem başka cihazların yayınından bozulmamasıdır.",
        "why": "Yoğun kentsel 6G ve ISAC radar yan lobları spektrum komşularını bozmamalıdır.",
    },
    "EMI": {
        "abbr": "EMI",
        "en": "Electromagnetic Interference",
        "tr": "Elektromanyetik Girişim",
        "definition": "İstenmeyen elektromanyetik enerjinin bir sistemin işleyişini bozmasıdır.",
        "why": "EMC'nin düşmanıdır; ISAC yüksek güçlü radar ile haberleşme alıcısı aynı kutuda çarpışabilir.",
    },
    "FDTD": {
        "abbr": "FDTD",
        "en": "Finite-Difference Time-Domain",
        "tr": "Sonlu Farklar Zaman Domeni",
        "definition": "Maxwell denklemlerini zaman ve uzayda ızgara üzerinde adım adım çözen sayısal EM yöntemidir.",
        "why": "RIS metamalzeme ve THz paketinin laboratuvar öncesi elektromanyetik doğrulamasında kullanılır.",
    },
    "FEM": {
        "abbr": "FEM",
        "en": "Finite Element Method",
        "tr": "Sonlu Elemanlar Yöntemi",
        "definition": "Karmaşık geometrileri küçük elemanlara bölerek alan denklemlerini çözen sayısal yöntemdir.",
        "why": "Anten, paket ve soğutma tasarımında FDTD'ye tamamlayıcıdır; şebeke simülasyonu değildir.",
    },
    "CFD": {
        "abbr": "CFD",
        "en": "Computational Fluid Dynamics",
        "tr": "Hesaplamalı Akışkanlar Dinamiği",
        "definition": "Akış ve ısı taşınımını sayısal çözen yöntem ailesidir.",
        "why": "Baz istasyonu soğutması ve HAPS platform aerodinamiği için geçerlidir; radyo protokolü değildir.",
    },
    "AR": {
        "abbr": "AR",
        "en": "Augmented Reality",
        "tr": "Artırılmış Gerçeklik",
        "definition": "Gerçek görüntü üzerine dijital katman bindiren arayüz sınıfıdır.",
        "why": "THz/6G kapasite senaryolarında yüksek bit hızlı uç uygulama örneğidir; henüz saha metrik değildir.",
    },
    "VR": {
        "abbr": "VR",
        "en": "Virtual Reality",
        "tr": "Sanal Gerçeklik",
        "definition": "Tamamen sentetik üç boyutlu ortam sunan arayüz sınıfıdır.",
        "why": "Gecikme ve bit hızı ihtiyacı THz ve hücresiz MIMO gerekçelerinden biridir.",
    },
    "Meta API": {
        "abbr": "Meta API",
        "en": "Springer Nature Meta API",
        "tr": "Springer Nature Meta API",
        "definition": (
            "Springer Nature’ın yayın üstveri arayüzüdür. Bu sayfadaki yıl ve ülke grafikleri "
            "facet çıktısıdır; atıf çekilen kayıt + Crossref’tir."
        ),
        "why": "Yedi 6G konusu «6G {token}», 2020’den içinde bulunulan yıla kadar sayılır; konular toplanmaz. Pencere her yıl genişler.",
    },
}

TRL_SCALE: list[dict[str, str]] = [
    {"level": "1–2", "title": "Fikir ve kavram", "meaning": "Temel ilke veya uygulama kavramı; henüz laboratuvar doğrulaması yok."},
    {"level": "3", "title": "Laboratuvar kanıtı", "meaning": "Kritik işlev deneysel gösterildi; sokak şebekesi değil."},
    {"level": "4", "title": "Laboratuvar bileşeni", "meaning": "Alt sistem laboratuvarda doğrulandı; saha henüz sınırlı."},
    {"level": "5", "title": "İlgili ortam / prototip", "meaning": "Prototip gerçekçi ortamda denendi; ticari kule kadar olgun değil."},
    {"level": "6", "title": "İlgili ortamda sistem", "meaning": "Sistem prototipi ilgili ortamda gösterildi; erken ticari deneme mümkün."},
    {"level": "7–8", "title": "Operasyonel prototip / nitelikli sistem", "meaning": "Gerçek operasyon koşullarına yakın doğrulama."},
    {"level": "9", "title": "Saha ürünü", "meaning": "Gerçek görevde kanıtlanmış, satışa yakın veya satılan sistem."},
]


def _ui_lang() -> str:
    try:
        from i18n.core import get_lang

        return get_lang()
    except Exception:
        return "tr"


def localized_entry(key: str) -> dict[str, Any] | None:
    item = GLOSSARY.get(key)
    if not item:
        return None
    out = dict(item)
    if _ui_lang() == "en":
        from data.glossary_en import GLOSSARY_EN

        extra = GLOSSARY_EN.get(key, {})
        out["definition"] = extra.get("definition", item["definition"])
        out["why"] = extra.get("why", item["why"])
    return out


def trl_scale() -> list[dict[str, str]]:
    if _ui_lang() == "en":
        from data.glossary_en import TRL_SCALE_EN

        return TRL_SCALE_EN
    return TRL_SCALE


def format_term(key: str, *, first_use: bool = True) -> str:
    """İlk kullanımda tam biçim, sonrasında kısaltma."""
    item = localized_entry(key)
    if not item:
        return key
    if not first_use:
        return item["abbr"]
    if _ui_lang() == "en":
        return f"**{item['abbr']} ({item['en']}):** {item['definition']} {item['why']}"
    return (
        f"**{item['abbr']} ({item['en']} — {item['tr']}):** "
        f"{item['definition']} {item['why']}"
    )


def term_chip_html(key: str) -> str:
    item = GLOSSARY.get(key)
    if not item:
        return ""
    return (
        f"<span class='term-chip' title='{item['en']} — {item['tr']}'>"
        f"{item['abbr']}</span>"
    )


def glossary_plain_corpus() -> str:
    """AI geri getirme için düz metin derlemesi."""
    lang = _ui_lang()
    parts = []
    for key, item in GLOSSARY.items():
        loc = localized_entry(key) or item
        if lang == "en":
            parts.append(f"{item['abbr']} ({item['en']}): {loc['definition']} {loc['why']}")
        else:
            parts.append(
                f"{item['abbr']} ({item['en']} — {item['tr']}): "
                f"{loc['definition']} {loc['why']}"
            )
    return "\n".join(parts)


def get_term(key: str) -> dict[str, Any] | None:
    return GLOSSARY.get(key)
