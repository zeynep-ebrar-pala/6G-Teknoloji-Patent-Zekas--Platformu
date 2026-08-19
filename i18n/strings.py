"""
Merkezi UI katalogları — TR ve EN anahtar ağacı birebir aynıdır.
İçerik (öğretim metinleri) data/*_en.py overlay’lerinde durur.
"""

UI = {
    "tr": {
        "lang": {"tr": "TR", "en": "EN"},
        "app": {
            "page_title": "Türk Telekom | 6G Teknoloji & Patent Zekası",
            "brand": "Türk Telekom",
            "product": "6G Ar-Ge Platformu",
            "badge": "Türk Telekom 6G Ar-Ge Platformu",
            "title": "Türk Telekom 6G Teknoloji &amp; Patent Zekası Platformu",
            "subtitle": "6G Teknolojileri, Patent Zekası ve Yayın Analitiği",
            "footer": "© 2026 Türk Telekom Ar-Ge",
            "ai_provider": "AI sağlayıcı: {provider}",
            "ai_logout": "AI oturumunu kapat",
            "provider_off": "kapalı",
        },
        "nav": {
            "home": "Ana Sayfa",
            "tech": "6G Teknolojileri",
            "patent": "Patent Zekası",
            "publications": "Yayın Trendleri",
            "tt": "Türk Telekom Görünümü",
            "ai": "AI Asistan",
            "about": "Hakkında",
        },
        "tt_page": {
            "view": "Türk Telekom görünümü",
            "section": {
                "footprint": "Avrupa’daki yeri",
                "scenario": "Saha senaryosu",
            },
        },
        "settings": {"language": "Dil", "language_help": "Arayüz ve yeni AI yanıtları seçilen dile geçer."},
        "depth": {
            "label": "Anlatım derinliği",
            "radio": "Derinlik",
            "beginner": "Temel",
            "expert": "Uzman",
            "caption": "Temel: problem → yöntem → çalışma modeli. Uzman: temel katman + denklem / 3GPP / varsayım.",
        },
        "home": {
            "intro_beginner": """<div class="home-intro">
<h4>6G nedir</h4>
<p>
<strong>6G</strong>, 5G'nin yalnızca bit taşıyan erişim mimarisine yeni görevler ekler.
Bugün kule konuşur; çevreyi ölçmez, köşeyi dönemez, kule olmayan coğrafyada susar.
Yedi girdi bu boşlukları kapatma adayıdır:
<strong>ISAC</strong> aynı RF zincirinde yankı işler;
<strong>RIS</strong> cepheyi programlanabilir yansıtıcı yapar;
<strong>hücresiz MIMO</strong> hücre kenarını tasarım nesnesi olmaktan çıkarır;
<strong>NTN</strong> Rel-17+ ile LEO/HAPS hücresini çekirdeğe bağlar;
<strong>AI-RAN</strong> RRM'i ölçüm döngüsüne alır;
<strong>Ambient IoT</strong> pilsiz backscatter etiketi hedefler;
<strong>THz</strong> kısa hopta bant açar.
</p>
<p class="home-intro-note">
Hepsi aynı rafta durmaz. Her biri kendi
<strong>TRL</strong> (Technology Readiness Level — Teknoloji Hazırlık Seviyesi) basamağındadır;
tam sayı 3GPP teknik raporu veya kamuya açık deneme sınıfına göre eşlenir.
</p>
</div>""",
            "intro_expert": """<div class="home-intro">
<h4>6G nedir — uzman okuma (temel katman atlanmaz)</h4>
<p>
<strong>Temel:</strong> 6G, 5G'nin iletişim-only mimarisine algılama, programlanabilir kanal,
dağıtık anten, uydu hücresi, öğrenen RRM ve pilsiz etiket adaylarını ekler.
<strong>Uzman:</strong> ISAC: ortak dalga şekli, R⁴, CRB–Shannon ödünleşmesi (TR 22.837).
RIS: Φ = diag(e^{jθ_n}), çift yol kaybı, CSI gecikmesi (ETSI RIS ISG).
Hücresiz MIMO: ortak ön kodlama, bedel fronthaul/senkron (Rel-19/20).
NTN: Rel-17 TR 38.811, Doppler f_d = f_c (v/c) cosθ, TRL 6.
AI-RAN: O-RAN RIC xApp/rApp, TR 38.843; nöral PHY araştırma ucu.
Ambient IoT: Friis hasadı × backscatter, TR 38.848.
THz: L(f,d) = FSPL · e^{K(f)d}, TR 38.807, TRL 3.
</p>
<p class="home-intro-note">
Yedi girdi tek bir ticari «6G ürünü» değildir; farklı olgunlukta standartlaşma girdileridir.
Denklem, varsayım ve geçerlilik penceresi <strong>6G Teknolojileri</strong> uzman katmanındadır.
</p>
</div>""",
            "cards_heading": "Yedi Yapı Taşı",
            "cards_caption": "Kartta önce sahadaki sorun, sonra çözüm vardır. Adım adım anlatım, formül ve Türk Telekom senaryosu için soldan «6G Teknolojileri» menüsüne geçin.",
            "card_cta": "Adım adım anlatım: 6G Teknolojileri → bu kartı seçin",
            "cards_heading_expert": "Yedi Yapı Taşı",
            "cards_caption_expert": "Kartta problem + teknik karşılık vardır. Shannon/CRB, 3GPP ve geçerlilik penceresi için «6G Teknolojileri»ne geçin.",
            "card_cta_expert": "Denklem ve 3GPP bağlamı: 6G Teknolojileri → bu kartı seçin",
            "radar_heading": "### TRL radar — 3GPP / kamuya açık deneme eşlemesi",
            "radar_caption": "Dilimler NASA/AB TRL 1–9 ölçeğidir; her tam sayı, 3GPP teknik raporu veya kamuya açık deneme sınıfına göre eşlenir.",
        },
        "trl": {
            "pill": "TRL {n}",
            "maturity": "TRL {n} Olgunluk Seviyesi",
            "explainer_title": "TRL nedir?",
            "explainer_lead": "{abbr} ({en} — {tr}): {definition} {why}",
            "explainer_body": "1 = temel ilke, 9 = gerçek görevde kanıtlanmış ürün. Sayılar TT sahasında ölçülmedi: NASA/AB 1–9 ölçeği, 3GPP şartname/çalışma kalemi ve kamuya açık deneme sınıfına göre eşlenir.",
            "explainer_ntn": "TRL 6 — Rel-17 NTN şartnamesi (TR 38.811) + kamuya açık direct-to-cell denemeleri",
            "explainer_ris": "TRL 5 — ETSI RIS ISG / Rel-19–20 çalışma kalemi ve O-RAN RIC deneme sınıfı (RIS, AI-RAN)",
            "explainer_lab": "TRL 4 — Rel-19 çalışma kalemi / laboratuvar: ISAC (TR 22.837), hücresiz MIMO, Ambient IoT (TR 38.848)",
            "explainer_thz": "TRL 3 — TR 38.807 + laboratuvar spektrumu: THz, sokak şebekesi değil",
            "scale_header": "Ölçek",
            "scale_title": "TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi)",
        },
        "teach": {
            "problem": "Hangi problem?",
            "why_needed": "Neden gerekli?",
            "what": "Ne işe yarar?",
            "tt_impact": "Türk Telekom ve TRL",
            "heading": "Temel katman — problem, ihtiyaç, yöntem. Denklem ve 3GPP uzman katmanındadır.",
            "heading_compact": "Tanım katmanı (özet)",
            "heading_expert": "Uzman katman — aynı sıra; denklem, varsayım, 3GPP ve alternatif. Cümleler Temel ile aynı değildir.",
            "rail_beginner": "1 Problem · 2 İhtiyaç · 3 Yöntem · 4 Mekanizma · 5 Sınır · 6 Uygulama",
            "rail_expert": "1 Problem · 2 İhtiyaç · 3 Yöntem · 4 Mekanizma · 5 Sınır · 6 Uygulama · denklem / 3GPP / alternatif",
            "mental_model": "Çalışma modeli",
            "analogy": "Karşılaştırma",
            "analogy_map": "Teknik karşılık",
            "when_used": "Ne zaman kullanılır?",
            "when_not": "Ne zaman kullanılmaz?",
            "not_to_confuse": "Neyle karıştırılmamalıdır?",
            "real_world": "Gerçekte nerede karşımıza çıkar?",
            "how_steps": "Nasıl çalışır? — adımlar",
            "formula_heading": "#### Matematiksel temel — sembol, birim, varsayım",
            "formula_caption": "Formül ezberletilmez: her sembolün fiziksel anlamı, neden bu biçim ve ne zaman geçerli olduğu yazılır.",
            "equation": "Denklem",
            "formula_fallback": "Formül",
            "symbol": "Sembol",
            "meaning": "Anlamı",
            "unit": "Birim",
            "tells_us": "Ne anlatır?",
            "why_this_form": "Neden bu biçim?",
            "when_valid": "Ne zaman geçerli?",
            "if_variable_changes": "Değişken artınca / azalınca",
            "assumptions": "Varsayımlar ve sınır",
            "simple_example": "Basit nicel örnek",
            "use_cases": "### Kullanım alanları — mekanizma ve sınır",
            "use_cases_caption": "Her kart bir gerçek dünya işidir. Temel: ne işe yarar. Uzman: nasıl çalışır ve ne zaman kullanılmaz.",
            "scenario_n": "Senaryo #{n}",
            "how": "Nasıl:",
            "when_not_short": "Ne zaman değil:",
            "advantages": "### Avantajlar — neden kazanç?",
            "disadvantages": "### Dezavantajlar — hangi problem doğurur?",
            "global": "### Dünyadaki çalışmalar",
            "global_caption": "Bunlar isim listesi değil: her satır, özelliğin neden standart/araştırma gündeminde olduğunu söyler.",
            "tt_scenarios": "### Türk Telekom senaryoları",
            "tt_caption": "Problem → neden bu teknoloji → beklenen sonuç. Saha ölçümü değildir.",
            "trl_assess": "### TRL değerlendirmesi",
            "diagram_terms": "Diyagram terimleri",
        },
        "tech": {
            "select": "İncelemek İstediğiniz 6G Teknolojisini Seçin:",
            "select_fmt": "{icon} {title} (TRL {trl})",
            "badge": "6G TEKNOLOJİLERİ",
            "section_label": "Teknoloji bölümü",
            "section": {
                "definition": "1. Teknoloji Tanımı",
                "principle": "2. Çalışma Prensibi & Blok Diyagram",
                "architecture": "3. Sistem Mimarisi",
                "use_cases": "4. Kullanım Alanları",
                "adv_dis": "5. Avantajlar & Dezavantajlar",
                "global_tt": "6. Dünyadaki Çalışmalar & TT Senaryoları",
                "performance": "7. Performans Grafikleri & Referanslar",
            },
            "def_heading": "### Teknoloji tanımı — problem, yöntem, sınır",
            "expert_def": "Karşılaştırma — alternatif, varsayım, geçerlilik",
            "principle_beginner": "Çalışma prensibi — adımlar",
            "principle_expert": "Çalışma prensibi (mekanizma + terim)",
            "principle_recall": "Temel adımlar (atlanmaz)",
            "diagram": "### Blok diyagram",
            "arch_heading": "### Sistem mimarisi ve matematiksel temel",
            "arch_layers": "Üç katman — kısaltmalar ilk kullanımda açık",
            "arch_expert": "Donanım / protokol / şebeke katmanları",
            "math_on_arch": "Denklem, sembol ve varsayım kartları 3. Sistem Mimarisi sekmesindedir.",
            "perf_heading": "### Performans — doğrulanmış kayıt sayımı",
            "perf_caption": "Temsili 5G/6G hedef barı yok. Aşağıdaki grafikler bu teknolojinin doğrulanmış patent kayıt sayısı ve (varsa) OpenAlex yayın trendidir.",
            "empty_patents": "«{domain}» için doğrulanmış patent kaydı yok.",
            "openalex_fail": "OpenAlex bu konu için yanıt vermedi; yayın trendi gizlendi.",
            "cell_free_oa": "Cell-Free, şartnamedeki akademik konu listesinde yoktur; OpenAlex serisi gösterilmez.",
            "refs": "### Referans Makaleler & Yayınlar",
            "refs_caption": "Bağlantılar DOI veya resmi 3GPP / proje sayfalarına gider.",
        },
        "patent": {
            "title": "Patent Zekası",
            "subtitle": "Küresel telekom firmalarının 6G patent kayıtları — tüm kayıtlar Google Patents üzerinden doğrulanabilir. Bu küme tam portföy değildir; yalnızca doğrulanmış örnek kayıtlardır. Kaynak: {source}",
            "filter": "Firma (şartname listesi: Nokia, Ericsson, Huawei, Samsung, Qualcomm, ZTE):",
            "all": "Tümü",
            "what_title": "Bu sayfa ne işe yarar?",
            "what_body": """<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.65;margin:8px 0 0 0;">
<strong>Patent</strong>, bir buluşun kamuya açıklanması karşılığında sınırlı süre tekel hakkıdır.
Burada baktığımız şey hukuki tavsiye değil; hangi firmanın hangi 6G konusunda koruma talebinde
bulunduğunun <em>örnek</em> haritasıdır. <strong>Assignee</strong> (hak sahibi) kaydı kimin
başvurduğunu söyler; o firmanın sahada ürünü olduğu anlamına gelmez.
</p>
<p style="color:#CBD5E1;font-size:0.88rem;line-height:1.6;margin:10px 0 0 0;">
<strong>TF-IDF (Term Frequency–Inverse Document Frequency — terim sıklığı–ters belge sıklığı):</strong>
özet metindeki sözcükleri, derlemede ne kadar ayırt edici olduklarına göre puanlar.
Harita anlam çıkarmaz; hangi kaydın hangi sözcüklere yakın durduğunu gösterir.
Özetler kaynakta kilitlidir — yeniden yazılmaz, uydurulmaz.
</p>
<p style="color:#94A3B8;font-size:0.84rem;margin:10px 0 0 0;">
Ne zaman yorumlanmaz: tek patent = pazar liderliği değildir. Yıl çubuğu başvuru/yayın yılıdır,
ticarileşme tarihi değildir.
</p>""",
            "empty_company": "«{company}» için doğrulanmış patent kaydı yok. Sayı uydurulmaz; Google Patents’te teyitli kayıt eklenene kadar grafik gizlenir.",
            "metric_total": "Doğrulanmış Patent Kaydı",
            "metric_leader": "En Fazla Kayıt (Assignee)",
            "metric_leader_delta": "{n} patent",
            "metric_domain": "Öne Çıkan Teknoloji Alanı",
            "metric_domain_delta": "{n} kayıt",
            "metric_source": "Kaynak",
            "open_gp": "Google Patents ana sayfasını aç ↗",
            "view": "Patent görünümü",
            "section": {
                "year": "Patent Sayısı / Yıl",
                "topics": "Konu Dağılımı & Kelime Bulutu",
                "tree": "Patent Ağacı & Yoğunluk",
                "map": "Teknoloji Haritası & Ağ",
                "list": "Patent Başlıkları",
                "tt_eu": "TT Avrupa izi",
            },
            "year_heading": "### Yıllara Göre Dağılım",
            "year_caption": "Her çubuk bir takvim yılıdır (ör. 2024, 2025). Kayıtlarda ay bilgisi olmadığı için 2024.2 gibi ara değer veya uydurma «2. Ay» dilimi yok.",
            "empty_trend": "Trend grafiği için yeterli patent verisi yok.",
            "companies_heading": "### En Çok Kayıtlı Firmalar",
            "empty_counts": "Firma sayımı için veri yok.",
            "empty_domain": "Domain dağılımı hesaplanamadı.",
            "empty_kw": "Anahtar kelime analizi için veri yok.",
            "wordcloud": "### Kelime Bulutu",
            "wordcloud_caption": "Yalnızca doğrulanmış patent başlıklarındaki kelime sıklığı.",
            "empty_wc": "Kelime bulutu için wordcloud/matplotlib yüklü değil veya kelime yok.",
            "density": "### Patent Yoğunluk Grafiği",
            "empty_density": "Yoğunluk haritası için veri yok.",
            "tree_heading": "### Patent Ağacı",
            "empty_tree": "Ağaç grafiği için veri yok.",
            "map_heading": "### Patent Teknoloji Haritası",
            "map_caption": "Koordinatlar patent başlıklarının TF-IDF vektörlerinin PCA ile 2 boyuta indirgenmesidir; uydurma konum yoktur.",
            "empty_map": "Harita için en az 2 patent ve scikit-learn gerekir.",
            "network": "### Assignee ↔ Alan Ağ Analizi",
            "empty_net": "Ağ grafiği için bağlantı verisi yok.",
            "list_heading": "### Doğrulanmış 6G Patent Listesi",
            "list_caption": "Kartlar yıla göre yeniden eskiye. Her kartta publication number, başlık, assignee, yıl ve Google Patents kaynak bağlantısı bulunur.",
            "assignee": "Assignee",
            "year": "Yıl",
            "open_record": "{pub} — Google Patents'te Aç ↗",
        },
        "pub": {
            "title": "Yayın Trendleri",
            "subtitle": "Bu sayfa önce DOI ile doğrulanmış makale setini gösterir. OpenAlex canlı sayımı gelirse küresel trend eklenir; gelmezse uydurma sayı yazılmaz. Kaynak: {source}",
            "what_title": "DOI, OpenAlex ve atıf ne anlama gelir?",
            "what_body": """<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.65;margin:8px 0 0 0;">
<strong>DOI (Digital Object Identifier — dijital nesne tanımlayıcı):</strong>
makaleye kalıcı kimlik verir; karttaki «Kaynakta Aç» bu kimliği çözümler.
Uydurma DOI üretmek bu platformda yasaktır.
</p>
<p style="color:#CBD5E1;font-size:0.88rem;line-height:1.6;margin:10px 0 0 0;">
<strong>OpenAlex:</strong> açık akademik graf API’sidir. Yıl/kurum/ülke sayıları bu API’den gelir;
erişilemezse grafik gizlenir, statik tablo uydurulmaz.
<strong>Atıf sayısı</strong> (<em>cited_by_count</em>) bir makalenin kaç kez referans verildiğidir —
kalite notu değildir; yeni makale düşük, tarama makalesi yüksek olabilir.
Google Scholar ayrı bir API sunmaz; sayılar OpenAlex’tendir.
</p>""",
            "empty": "Doğrulanmış makale kaydı bulunamadı.",
            "metric_doi": "Doğrulanmış makale (DOI)",
            "metric_oa_year": "OpenAlex {year} (6 konu)",
            "metric_topic": "En aktif OpenAlex konusu",
            "metric_cites": "En yüksek atıf (OpenAlex)",
            "open_oa": "OpenAlex kaynak sayfasını aç ↗",
            "snapshot": "Son başarılı OpenAlex önbelleği: {ts}",
            "view": "Yayın görünümü",
            "section": {
                "doi": "Doğrulanmış set (DOI)",
                "trend": "OpenAlex yıl trendi",
                "inst": "Kurumlar",
                "country": "Ülkeler",
                "papers": "Makaleler",
                "tt_eu": "TT Avrupa izi",
            },
            "doi_heading": "### DOI ile doğrulanmış 6G makaleleri",
            "doi_caption": "Çubuklar yalnızca platformda listelenen makalelerin yayın yılı ve konusudur. Her karttaki buton makaleyi DOI üzerinden açar.",
            "chart_year": "Doğrulanmış set — yayın yılı",
            "chart_year_x": "Takvim yılı",
            "chart_topic": "Doğrulanmış set — konu",
            "chart_publisher": "Doğrulanmış set — yayıncı",
            "empty_year": "Yıl dağılımı yok.",
            "oa_heading": "### 6G konularına göre yayın sayıları (OpenAlex)",
            "oa_caption": "Sayılar OpenAlex aramasındandır. API veya önbellek yoksa grafik çizilmez; statik küresel sayı uydurulmaz.",
            "oa_empty": "OpenAlex şu an canlı yanıt vermedi ve disk önbelleği de boş. Yukarıdaki DOI doğrulamalı set kullanılabilir. OpenAlex düzelince trend otomatik dolar.",
            "try_oa": "OpenAlex’i tarayıcıda dene ↗",
            "open_oa_counts": "Bu sayıları OpenAlex’te aç ↗",
            "inst_heading": "### En çok yayın yapan kurumlar",
            "oa_groupby": "OpenAlex group_by — 2020–2025, 6G konu araması.",
            "chart_inst": "Kurumlara göre yayın (OpenAlex)",
            "open_inst": "OpenAlex kurum filtresini aç ↗",
            "inst_fallback": "Canlı küresel sayım yok. Aşağıdaki liste yalnızca DOI setindeki OpenAlex yazar kurumlarıdır.",
            "chart_inst_fb": "Doğrulanmış 8 makale — yazar kurumları",
            "empty_inst": "Kurum listesi için OpenAlex yanıtı yok. Makale kartlarındaki DOI butonunu kullanın.",
            "cc_heading": "### En çok yayın yapan ülkeler",
            "chart_cc": "Ülkelere göre yayın (OpenAlex)",
            "open_cc": "OpenAlex ülke filtresini aç ↗",
            "cc_fallback": "Canlı küresel sayım yok. Aşağıdaki liste yalnızca DOI setindeki OpenAlex ülke kodlarıdır.",
            "chart_cc_fb": "Doğrulanmış 8 makale — ülke kodları",
            "empty_cc": "Ülke listesi için OpenAlex yanıtı yok. Makale kartlarındaki DOI butonunu kullanın.",
            "papers_heading": "### Doğrulanmış 6G makaleleri",
            "papers_caption": "Sıra: yıl yeniden eskiye; aynı yılda OpenAlex atıf yüksekten düşüğe. Atıf yoksa «—». Her kayıt DOI ile açılır.",
            "citations_n": "{n} atıf",
            "citations_na": "Atıf: —",
            "authors": "Yazarlar",
            "open_doi": "Makaleyi DOI ile Aç ↗",
        },
        "tt_eu": {
            "what_title": "Patent neden ülkeye bağlıdır?",
            "what_body": """<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.65;margin:8px 0 0 0;">
<strong>Patent ülkeseldir:</strong> TR milli başvuru yalnızca Türkiye’de hak doğurur.
<strong>EPO (European Patent Office — Avrupa Patent Ofisi):</strong> EPC üyeleri için tek inceleme;
verilen EP, seçilen ülkede ayrıca yürürlüğe konur. Türkiye EPO üyesidir; üyelik otomatik EP tescili değildir.
<strong>PCT (Patent Cooperation Treaty — Patent İşbirliği Anlaşması):</strong> WO numarası dünya patenti değildir.
</p>
<p style="color:#CBD5E1;font-size:0.88rem;line-height:1.6;margin:10px 0 0 0;">
Bu sekme Türk Telekom’un <em>Avrupa’daki yerini</em> üç ayrı şey olarak ayırır: (1) doğrulanmış patent ofisi,
(2) yazar bağlılıklı makale, (3) işbirliği / standart organı. İşbirliği = tescil değildir.
Firma filtresindeki Nokia–ZTE kümesi rakip örneklemdir; burası TT grubu örneğidir.
</p>""",
            "expert_title": "Bu kümede ne doğrulandı, ne doğrulanmadı?",
            "expert_body": """<p style="color:#E2E8F0;font-size:0.9rem;line-height:1.65;margin:8px 0 0 0;">
Google Patents’te bu platformun kilitlediği TT-grup 6G-komşu tesciller <strong>Netsia Inc.</strong> (USPTO) altındadır.
Netsia, Argela/Türk Telekom ABD Ar-Ge iştirakidir; hukuki assignee Netsia’dır.
<strong>EP yayın numarası bu örnekte 0’dır</strong> — gizlenmez, uydurulmaz.
Yayınlarda ham bağlılık «Türk Telekom, Ankara/İstanbul, Türkiye». OpenAlex kurum grafı
bazı kaydı DE/MY/CZ şirketine yanlış düşürebilir; ülke çubuğu o hatayı TT Avrupa yayını diye okumaz.
</p>""",
            "metric_pat": "TT-grup doğrulanmış patent",
            "metric_ep": "EPO (EP) kayıt",
            "metric_papers": "TT bağlılıklı makale (DOI)",
            "metric_touch": "Avrupa dokunuşu",
            "metric_named": "Adı geçen TTI ülkesi",
            "role_title": "Pazardaki yer: satıcı değil, operatör",
            "role_body": """<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.65;margin:8px 0 0 0;">
Türk Telekom <strong>Türkiye’de entegre operatördür</strong> (sabit, mobil, genişbant).
Avrupa 6G <em>ekipman</em> pazarında Nokia / Ericsson sınıfı RAN satıcısı değildir.
<strong>Türk Telekom International (TTI):</strong> %100 iştirak; CEE–Türkiye–Kafkasya–Ortadoğu toptan veri/ses.
Harita yalnızca adı kaynakta geçen ülkeleri boyar. Boyanmayan Avrupa ülkesi «yok» iddiası değil:
bu platformda o ülke adı kilitlenmedi.
</p>""",
            "map_heading": "### Avrupa haritası (kaynakta adı geçen ülkeler)",
            "map_caption": "Katmanlar ayrıdır: merkez, TTI toptan first-mover, 6G Ar-Ge ortağı, ETSI merkezi, MoU imza yeri. Abone/pazar payı değildir.",
            "map_fail": "Harita çizilemedi; aşağıdaki liste kaynakta adı geçen ülkelerin tam kümesidir.",
            "role_heading": "### Kanıt türü (kaç ülkede adı geçti)",
            "role_caption": "EP tescil çubuğu 0’dır. Toptan 6 ülke TTI About «first mover» listesidir; 19 veya 24’ün tamamı değildir.",
            "vs_heading": "### Bu platformun kilitli 6G örnek kümesi",
            "vs_caption": "Nokia–ZTE çubukları doğrulanmış 6G örnek kayıttır. TT çubuğu Netsia USPTO tescilleridir. Küresel SEP veya gelir payı değildir.",
            "office_heading": "### Patent ofisi (doğrulanmış küme)",
            "office_caption": "EP=0, bu örnekte Avrupa bölgesel tescil yok demektir. 921 milli başvuru iddiası çubuğa işlenmez.",
            "pat_list_heading": "### Netsia Inc. (Türk Telekom grubu) — Google Patents",
            "pat_list_caption": "Assignee Netsia Inc. Kartlar yıla göre yeniden eskiye. Rakip (Nokia–ZTE) kümesine karıştırılmaz.",
            "named_heading": "### Kaynakta adı geçen ülkeler (eksiksiz liste)",
            "named_caption": "Haritada boyanan ülkelerin tam kümesi budur. 19 veya 24 ülke adı raporda yok; eklenmez.",
            "named_col_place": "Ülke",
            "named_col_layer": "Katman",
            "presence_heading": "### 6G dokunuşları — işbirliği / standart / proje",
            "presence_caption": "Kart resmi duyurudur. Eşit yükseklikli «ülke başına 1» çubuk pazar payı gibi okunduğu için çizilmez.",
            "oa_heading": "### OpenAlex ülke grafını TT Avrupa’sı sanmayın",
            "oa_caption": "Üstteki «Ülkeler» sekmesi küresel 6G konu aramasıdır, TT portföyü değildir. Aşağıdaki makalelerin ham bağlılığı TR’dir.",
            "papers_heading": "### Türk Telekom Ar-Ge bağlılıklı makaleler",
            "papers_caption": "DOI kilitlidir. Sıra: yıl yeniden eskiye; aynı yılda OpenAlex atıf (cited_by_count) yüksekten düşüğe.",
            "open_touch": "Kaynak duyuruyu aç ↗",
            "open_press": "Milli başvuru açıklamasını aç ↗",
            "open_ir": "2024 entegre raporu PDF ↗",
            "open_tti": "TTI About sayfasını aç ↗",
            "overview_heading": "### Avrupa geneli — TT yayın ve patent sırası",
            "overview_caption": "Her ülke: kilitli 3 MNO + TT. Yayın = OpenAlex 6G araması veya (TT, TR) DOI kilitli bağlılık. Patent = bu platformun örnek kümesi (Netsia USPTO yalnız TR). 1. sıra en yüksek sayıdır. Abone payı değildir.",
            "overview_spin": "Ülke sıraları OpenAlex önbelleğinden / canlı sorgudan yükleniyor",
            "overview_pub_title": "TT yayın sayısı (ülke, yüksekten düşüğe)",
            "overview_pat_title": "TT patent örnek sayısı (ülke, yüksekten düşüğe)",
            "overview_tt_pub": "TT yayın",
            "overview_tt_pat": "TT patent",
            "overview_pub_lead": "Yayında 1. (adet)",
            "overview_pat_lead": "Patentte 1. (adet)",
            "rank_heading": "### Ülke detayı: 3 MNO (Mobile Network Operator — mobil şebeke işletmecisi) + Türk Telekom",
            "rank_caption": "Üç operatör Wikipedia Avrupa MNO listesindeki bu ülke satırından kilitlendi; abone/gelir «en yüksek 3» bu platformda ölçülmedi. Yayın sayısı OpenAlex 6G konu aramasıdır. Patent sayısı yalnızca bu platformun kilitli örnek kümesi (TT için EP=0; USPTO Netsia yalnız TR satırında). Küresel SEP veya pazar payı değildir.",
            "rank_country": "Avrupa ülkesi",
            "rank_pub_title": "Yayın sırası (OpenAlex, bu ülke)",
            "rank_pat_title": "Patent sırası (kilitli örnek küme)",
            "rank_pub_x": "OpenAlex yayın sayısı",
            "rank_pat_x": "Örnek küme patent kaydı",
            "rank_tt": "Türk Telekom bu ülkede: yayın {pub}. sıra ({pub_n} OpenAlex kaydı) · patent {pat}. sıra ({pat_n} örnek kayıt) — {n} firma",
            "rank_oa_fail": "OpenAlex bu ülke için yanıt vermedi; yayın çubuğu çizilmez.",
            "rank_col_rank_pub": "Yayın sırası",
            "rank_col_pub": "Yayın (OpenAlex)",
            "rank_col_rank_pat": "Patent sırası",
            "rank_col_pat": "Patent (örnek)",
            "rank_open_oa": "Bu ülke OpenAlex sorgusunu aç ↗",
            "rank_open_wiki": "Avrupa MNO listesini aç ↗",
            "rank_open_gp": "Google Patents assignee ↗",
            "layer": {
                "hq": "Merkez / operatör Ar-Ge",
                "wholesale": "TTI toptan (first-mover)",
                "rd_collab": "6G Ar-Ge ortaklığı",
                "standards": "Standart organı (ETSI)",
                "mou_venue": "MoU imza yeri",
                "ep_grant": "EPO (EP) tescil",
            },
        },
        "ui": {
            "source": "Kaynakta Aç ↗",
            "no_source": "Kaynak bağlantısı yok.",
        },
        "scenario": {
            "title": "Türk Telekom 6G Saha Dağıtım ve Senaryo Çözümleyici",
            "lead": "Türkiye coğrafyası, Türk Telekom altyapısı ve stratejik Ar-Ge hedeflerine göre 6G teknoloji eşleştirme motoru.",
            "kpi_body": """<p style="color:#E2E8F0;font-size:0.88rem;line-height:1.6;margin:0;">
<strong>KPI (Key Performance Indicator — anahtar performans göstergesi):</strong>
hız, gecikme, enerji gibi izleme sayılarıdır. Buradaki değerler saha ping’i değil;
kural tabanlı senaryo motorunun çıktısıdır.
<strong>CAPEX (Capital Expenditure — sermaye gideri):</strong> kule, fiber, uydu kapasitesi gibi
yatırım ölçeğinin kaba etiketidir; ihale fiyatı değildir.
</p>
<p style="color:#94A3B8;font-size:0.84rem;line-height:1.55;margin:8px 0 0 0;">
Varsayım: bölge + yoğunluk + öncelik üçlüsü bir teknoloji setini seçer. Sınır: yağmur, izin, spektrum
ve gerçek fiber topolojisi modele girmez. Sayıyı «ölçülmüş 6G performansı» diye okumayın.
</p>""",
            "params": "### Senaryo parametreleri",
            "region": "1. Uygulama bölgesi / senaryo alanı",
            "region_help": "Eşleştirilecek Türk Telekom saha veya altyapı bölgesi",
            "density": "2. Hedef kullanıcı / sensör yoğunluğu",
            "density_help": "Bölgedeki kilometrekare başına düşen cihaz ve sensör yoğunluğu",
            "priority": "3. Öncelikli stratejik hedef",
            "priority_help": "Bu dağıtımda hedeflenen birincil performans veya iş hedefi",
            "metrics_exp": "Detaylı performans ve metrik özeti",
            "capex_caption": "CAPEX (sermaye gideri) ölçeği — ihale fiyatı değil: **{value}**",
            "kpi_note": "KPI değerleri kural tabanlı senaryo motoru çıktısıdır; saha ölçümü değildir.",
            "result_heading": "### Önerilen Türk Telekom mimarisi ve KPI analizi",
            "techs": "**Önerilen 6G teknolojileri:** {techs}",
            "solution": "**Saha çözüm mimarisi:**",
            "priority_impact": "**Stratejik hedef etkisi:**",
            "density_profile": "**Yoğunluk profili:** {value}",
            "metric_speed": "Hız kapasitesi",
            "metric_latency": "Gecikme (latency)",
            "metric_energy": "Enerji skoru",
            "feasibility": "**Uygulanabilirlik ve saha uyumluluk skoru:** `{score}`",
            "region_bosphorus": "İstanbul Boğazı ve Marmara deniz sahili (ISAC + THz)",
            "region_stadium": "RAMS Park / stadyum ve yoğun etkinlik alanları (hücresiz MIMO)",
            "region_industry": "Marmara sanayi bölgesi / otonom fabrikalar (Ambient IoT + AI-RAN)",
            "region_disaster": "AFAD entegre deprem ve afet bölgesi (NTN + ISAC)",
            "region_historic": "Tarihi Yarımada / dar sokak kentsel alan (RIS + Sub-THz)",
            "region_datacenter": "Türk Telekom Ankara ve İstanbul veri merkezi (THz mesh)",
            "density_low": "Düşük (kırsal / açık)",
            "density_medium": "Orta (şehir içi)",
            "density_high": "Yüksek (stadyum / meydan)",
            "density_extreme": "Aşırı yoğun (trilyon sensör ölçeği)",
            "priority_coverage": "Kesintisiz kapsama (zero gap)",
            "priority_speed": "Ultra yüksek hız (terabit/s)",
            "priority_energy": "Düşük enerji / yeşil şebeke",
            "priority_resilience": "Afet dayanıklılığı",
            "title_bosphorus": "İstanbul Boğazı ve Marmara deniz sahili",
            "title_stadium": "RAMS Park / stadyum ve yoğun etkinlik alanları",
            "title_industry": "Marmara sanayi bölgesi / otonom fabrikalar",
            "title_disaster": "AFAD entegre deprem ve afet bölgesi",
            "title_historic": "Tarihi Yarımada / dar sokak kentsel alan",
            "title_datacenter": "Türk Telekom Ankara ve İstanbul veri merkezi",
            "sol_bosphorus": "Sahil 6G kulelerine entegre ISAC radar algılama + kuleler arası THz kablosuz fiber geri bağlantı.",
            "sol_stadium": "Tribün ve çatıya dağıtılmış 200+ mini AP ile hücresiz (cell-free) kapsama + AI-RAN dinamik yük dengeleme.",
            "sol_industry": "Fabrika içi pilsiz Ambient IoT etiketleri + duvar kaplaması pasif RIS yansıtıcılar.",
            "sol_disaster": "LEO uydulardan akıllı telefonlara Direct-to-Cell bağlantı + duvar arkası RF enkaz radar algılaması.",
            "sol_historic": "Tarihi dokuyu bozmadan bina dış yüzeylerine şeffaf pasif RIS kaplama.",
            "sol_datacenter": "Sunucu rafları arasında kablosuz THz mesh bağlantısı + AI-RAN derin uyku modları.",
            "year_bosphorus": "2028 saha pilotu",
            "year_stadium": "2027 prototip denemesi",
            "year_industry": "2026 endüstri PoC",
            "year_disaster": "3GPP Rel-18/19 entegrasyonu",
            "year_historic": "2027 kentsel pilot",
            "year_datacenter": "2026 laboratuvar demosu",
            "capex_mid_high": "Orta–yüksek",
            "capex_high": "Yüksek",
            "capex_low_opt": "Düşük–optimal",
            "capex_strategic": "Stratejik yatırım",
            "capex_low": "Düşük",
            "kpi_coverage": "Sıfır kör nokta (%99,999 güvenilirlik ve kapsama hedefi)",
            "kpi_speed": "1 Tbps tepe hız ve ultra geniş frekans bandı (literatür hedefi)",
            "kpi_energy": "Yeşil 6G — yüksek enerji verimliliği hedefi (AI-RAN derin uyku)",
            "kpi_resilience": "Karasal kule çökse bile uydudan acil iletişim yedek hattı",
            "dens_low": "Kırsal / geniş alan genişletilmiş kapsama",
            "dens_medium": "Dengeli şehir içi makro-mikro şebeke katmanı",
            "dens_high": "Yoğun şehir içi / stadyum çoklu hüzme (multi-beam) tahsisi",
            "dens_extreme": "Trilyon cihaz ölçeğinde pilsiz etiket ve ultra masif hücresiz ağ",
            "nodes_low": "500 cihaz / km²",
            "nodes_medium": "50.000 cihaz / km²",
            "nodes_high": "500.000 cihaz / km²",
            "nodes_extreme": "1.000.000+ sensör / km²",
            "nodes_default": "10.000 / km²",
            "impact": "**Seçilen bölge ({region})** için **{priority}** önceliği ve **{density}** hedefiyle özelleştirilmiş 6G mimarisi oluşturuldu.\n\n• **Kapasite ve hız:** {capacity} Gbps tepe akış\n• **Gecikme:** {latency} ms (ultra-güvenilir düşük gecikme hedefi)\n• **Şebeke yoğunluğu:** {nodes}\n• **Enerji verimliliği skoru:** %{energy}",
        },
        "auth": {
            "title": "AI Asistan için API anahtarı",
            "lead": "Anahtar yalnızca bu oturumda tutulur. Modül 1–3 ve Türk Telekom görünümü anahtarsız çalışır.",
            "provider": "AI sağlayıcı seçimi",
            "groq": "Groq (gsk_...)",
            "gemini": "Google Gemini (AIza...)",
            "key": "API anahtarı",
            "keys_help": "Anahtar almak için: [Groq Console](https://console.groq.com/keys) · [Google AI Studio](https://aistudio.google.com/apikey)",
            "env_info": "`.env` dosyasında `{provider}_API_KEY` tanımlı. Aşağıdaki butonla ortam anahtarını kullanabilirsiniz.",
            "open_env": "`.env` anahtarı ile AI'yı aç",
            "open": "AI Asistanı aç",
            "empty_key": "Lütfen geçerli bir API anahtarı girin.",
            "spinner": "API anahtarı doğrulanıyor...",
            "no_key_caption": "Anahtar yoksa asistan yine de TF-IDF ile doğrulanmış kayıtlardan kısa yanıt üretir.",
            "continue": "Anahtarsız devam et (yalnızca yerel geri getirme)",
            "empty": "API anahtarı boş olamaz.",
            "bad_provider": "Geçersiz sağlayıcı seçimi.",
            "groq_ok": "Groq API anahtarı doğrulandı.",
            "groq_missing": "Groq kütüphanesi yüklü değil. pip install groq",
            "groq_bad": "Groq anahtarı geçersiz: {exc}",
            "gemini_ok": "Gemini API anahtarı doğrulandı.",
            "gemini_missing": "Gemini kütüphanesi yüklü değil. pip install google-genai",
            "gemini_bad": "Gemini anahtarı geçersiz: {exc}",
        },
        "ai": {
            "title": "AI Asistan",
            "lead": "Yanıtlar sklearn TF-IDF ile seçilen teknoloji, patent, makale ve sözlük kayıtlarındandır. Dual-Depth kenar çubuğu anlatım kademesini belirler (Temel: problem ve çalışma modeli; Uzman: denklem + varsayım). Mod: <strong style=\"color:#00E5FF;\">{mode}</strong> · Sağlayıcı: <strong style=\"color:#00E5FF;\">{provider}</strong>",
            "mode_llm": "LLM + TF-IDF",
            "mode_local": "yalnızca TF-IDF (yerel)",
            "caption": "Bağlamda olmayan patent numarası, DOI veya atıf sayısı üretilmez.",
            "chip_ris": "RIS nedir?",
            "chip_diff": "NTN ile ISAC arasındaki fark",
            "chip_patents": "Patent veri özeti",
            "chip_patents_q": "Platformdaki doğrulanmış patent verilerini özetle.",
            "welcome": "Merhaba! Ben Türk Telekom 6G AI Asistanıyım. Yanıtlarım Modül 1–3’teki doğrulanmış kayıtlara dayanır; platformda olmayan bilgi uydurmam.",
            "placeholder": "6G teknolojisi, patent veya makale hakkında sorun...",
            "spinner": "Doğrulanmış kayıtlar üzerinden yanıt üretiliyor...",
            "empty_q": "Lütfen bir soru yazın.",
            "fallback_none": "### 6G Asistan (veri tabanlı mod)\n\nSorunuz platform veri kümesinde eşleşmedi. 6G Teknolojileri, Patent Zekası veya Yayın Trendleri sayfalarındaki doğrulanmış kaynakları inceleyin.",
            "related": "**İlgili doğrulanmış kayıtlar:**",
            "tfidf_note": "*Yanıt TF-IDF ile seçilen platform kayıtlarındandır; sayı uydurulmaz.*",
            "llm_fail": "*LLM yanıtı alınamadı: {exc}*",
            "glossary_title": "Teknik sözlük (ilk kullanım açılımı)",
            "cite_n": "{n} atıf",
            "cite_na": "atıf sayısı OpenAlex’ten alınamadı",
            "pedagogy": "Anlatım kuralı: önemli kavramda Nedir, Neden gerekli, Ne işe yarar, Nasıl çalışır, Ne zaman kullanılır, Ne zaman kullanılmaz, Neyle karıştırılmamalı, Gerçekte nerede çıkar. Kısaltmayı ilk geçişte «KISALTMA (English — Türkçe):» diye aç; sonra kısaltma kullan. Formül varsa sembol ve varsayımı söyle; ezberletme. Bağlamda olmayan sayı, patent ID, DOI, atıf uydurma. Emin değilsen «Platform verisinde bu bilgi yok» de.",
            "depth_beginner": "Seviye: TEMEL. Problem, ihtiyaç, yöntem, çalışma modeli, ne zaman/kullanılmaz ve neyle karıştırılmamalı ağırlıklı yaz. Çocuklaştırma. Denklem istersen sembolleri açıkla; varsayımı atlama.",
            "depth_expert": "Seviye: UZMAN. Kavramsal temeli atlama; ardından denklem, varsayım, sınır ve alternatif ekle.",
            "ctx_header": "=== DOĞRULANMIŞ 6G VERİ BAĞLAMI (TF-IDF ile seçilmiş parçalar) ===",
            "ctx_rule": "KURAL: Bu bağlamda olmayan sayı, patent ID veya makale uydurma. Emin değilsen 'Platform verisinde bu bilgi yok' de.",
            "system": "Türk Telekom 6G Ar-Ge asistanısın. Yalnızca verilen bağlamı kullan. Tahmin veya uydurma yapma. USER_LANGUAGE = tr. Yanıtı doğal, profesyonel Türkçe yaz; kelime kelime çeviri yapma. Teknik terimlerde yerleşik terminolojiyi kullan.",
            "user_wrap": "Kullanıcı sorusu: {question}",
        },
        "about": {
            "heading": "### Hakkında",
            "card": """<div class="glass-card" style="border-left: 5px solid #00E5FF;">
<h4 style="color:#00E5FF; margin-top:0;">6G Technology &amp; Patent Intelligence Platform</h4>
<p style="color:#E2E8F0; font-size:0.95rem; line-height:1.6; margin-bottom:0;">
Türk Telekom 6G Ar-Ge ekibinde kullanılmak üzere 6G teknolojileri, akademik yayınlar
ve patent trendlerini tek portalda sunan Streamlit uygulaması.
Geliştirici: <strong>Zeynep Ebrar Pala</strong>.
</p>
</div>""",
            "modules": "#### Modüller",
            "mod_left": """
- **Ana Sayfa** — 7 teknolojinin TRL radar haritası; Dual-Depth (Temel/Uzman) giriş metnini değiştirir
- **6G Teknolojileri** — kavramsal temel + uzman katman (formül, varsayım, karşılaştırma); tüm sekmeler anlatım derinliğini dinler
- **Patent Zekası** — Nokia, Ericsson, Huawei, Samsung, Qualcomm, ZTE; TT Avrupa izi; yıl, konu, kelime bulutu, ağaç, yoğunluk, harita; patent özetleri kaynakta kilitli
- **Yayın Trendleri** — OpenAlex yıl / kurum / ülke; DOI doğrulamalı makaleler; TT Avrupa izi
            """,
            "mod_right": """
- **Türk Telekom Görünümü** — saha senaryo çözümleyici
- **AI Asistan** — TF-IDF yerel geri getirme; isteğe bağlı Groq / Gemini
- **Hakkında** — bu sayfa (teslim / 15 dk sunum iskeleti)
            """,
            "stack": "#### Kullanılan teknolojiler",
            "stack_body": "Python, Streamlit, Pandas, Plotly, Matplotlib, NetworkX, WordCloud, scikit-learn. Opsiyonel: Groq API, Google Gemini API. Patent kaynağı: Google Patents. Akademik: OpenAlex + DOI (IEEE Xplore, Springer, Elsevier).",
            "standard": "#### Anlatım standardı",
            "standard_body": "Teknik içerik iki kademelidir: **Temel** (nedir / neden / nasıl / ne zaman) ve **Uzman** (denklem, varsayım, 3GPP). Uzman mod temel katmanı atlamaz. Kısaltmalar ilk geçişte açılır. Patent özeti, DOI ve sayı uydurulmaz.",
            "talk": "#### 15 dakikalık sunum iskeleti",
            "talk_body": """
1. Amaç ve kapsam (1 dk)
2. Ana Sayfa TRL radar (2 dk)
3. Bir teknoloji (ör. RIS) — prensip + diyagram + TT senaryosu (3 dk)
4. Patent Zekası — firma filtresi, yıl grafiği, TT Avrupa izi (3 dk)
5. Yayın Trendleri — OpenAlex yıl + kurum/ülke + TT bağlılıklı DOI (3 dk)
6. AI Asistan — «RIS nedir?» ve «NTN ile ISAC arasındaki fark» (2 dk)
7. Kaynak doğrulama kuralı: uydurma ID/sayı yok (1 dk)
        """,
            "usage": "Kullanım adımları için depodaki USAGE_GUIDE.md dosyasına bakın.",
        },
        "charts": {
            "year": "Takvim yılı",
            "trl_series": "TRL seviyesi",
            "trl_title": "TRL eşlemesi (3GPP / deneme sınıfı → 1–9)",
            "trl_hover": "%{theta}<br>TRL %{r}<br>%{customdata}<extra></extra>",
            "tech_counts": "Doğrulanmış {label} patent kayıt sayısı / yıl",
            "count": "Kayıt sayısı",
            "patent_year": "Yıllara göre 6G patent kayıt sayısı (doğrulanmış küme)",
            "patent_count": "Patent kayıt sayısı",
            "domain_radar": "Firma bazlı 6G teknoloji yetkinlik dağılımı (%)",
            "keywords": "Patent istemlerinde en sık geçen anahtar kelimeler",
            "kw_x": "Geçtiği istem sayısı",
            "academic_trend": "Akademik yayın sayıları trendi (OpenAlex, konu bazlı)",
            "pub_count": "Yayın sayısı",
            "db_default": "Doğrulanmış örnek set — yayıncı sayısı",
            "publisher": "Yayıncı",
            "paper_count": "Makale sayısı",
            "network": "Assignee ↔ teknoloji alanı ağ grafiği",
            "nx_missing": "NetworkX yüklü değil; ağ grafiği gösterilemiyor.",
            "company_counts": "En çok kayıtlı firmalar (doğrulanmış küme)",
            "company": "Firma",
            "density": "Patent yoğunluğu (firma × alan, kayıt sayısı)",
            "sunburst": "Patent ağacı (firma → alan → kayıt)",
            "tfidf": "Patent teknoloji haritası (TF-IDF + PCA, başlık vektörleri)",
            "oa_bar_x": "Yayın sayısı (OpenAlex)",
            "tt_office": "TT-grup patent ofisi (doğrulanmış küme)",
            "tt_office_x": "Ofis kodu (EP / US / TR)",
            "tt_europe": "TT Avrupa dokunuşu (işbirliği / standart / proje)",
            "tt_europe_x": "Doğrulanmış dokunuş sayısı",
            "tt_map": "TT Avrupa yeri — yalnızca adı kaynakta geçen ülkeler",
            "tt_role": "TT kanıt türü (ülke adı adedi)",
            "tt_role_x": "Adı geçen ülke / kayıt",
            "tt_vs_vendors": "Kilitli 6G örnek küme vs TT-grup (Netsia)",
        },
        "diagram": {
            "isac_ue": "Kullanıcı (UE)",
            "ris_tx": "6G Verici (Tx)",
            "ris_bldg": "Bina (engelleme)",
            "ris_surface": "Akıllı yüzey (RIS ayna)",
            "ris_rx": "Kullanıcı (Rx)",
            "cf_cpu": "Merkezi işlemci (CPU)",
            "cf_user": "Kullanıcı",
            "thz_rate": "1 terabit / saniye veri hızı",
            "thz_bw": "0,1–10 THz ultra geniş bant",
            "ai_enc": "Nöral kodlayıcı",
            "ai_enc_sub": "(derin öğrenmeli verici)",
            "ai_ch": "Fiziksel kanal",
            "ai_ch_sub": "+ gürültü ve sönümlenme",
            "ai_dec": "Nöral alıcı",
            "ai_dec_sub": "(derin öğrenmeli alıcı)",
            "ai_loss": "Uçtan uca geri besleme ve kayıp fonksiyonu (end-to-end loss)",
            "ntn_leo": "LEO uydu takımı (600 km)",
            "ntn_haps": "HAPS zeplin (20 km)",
            "ntn_gw": "TT uydu geçidi (gateway)",
            "ntn_phone": "Akıllı telefon",
            "iot_reader": "6G okuyucu",
            "iot_reader_sub": "(sinyal üreteci)",
            "iot_in": "Gelen taşıyıcı RF sinyali (enerji kaynağı)",
            "iot_out": "Yansıyan modüle veri (geri saçılım)",
            "iot_tag": "Pilsiz IoT etiketi",
            "iot_tag_sub": "(RF enerji hasadı)",
            "legend_isac": "<strong>gNB</strong> (next-generation Node B — baz istasyonu) hem veri basar hem eko dinler. <strong>UE</strong> (User Equipment — kullanıcı cihazı) iletişim ucudur. <strong>AoA</strong> (Angle of Arrival — geliş açısı) dizi fazından yön; <strong>Doppler</strong> hızın radyal bileşenidir. Tx/Rx: aynı kutuda verici ve alıcı.",
            "legend_ris": "<strong>Tx</strong> verici gNB, <strong>Rx</strong> kullanıcı UE. <strong>N-LoS</strong> (Non-Line-of-Sight — görüş hattı yok): bina doğrudan yolu keser; RIS faz kaydırarak alternatif yol açar. RIS kendi başına internet üretmez.",
            "legend_cell_free": "<strong>AP</strong> (Access Point — erişim noktası) sokaktaki küçük radyodur. <strong>CPU</strong> ortak ön kodlamayı hesaplar. Kesikli çizgi <strong>fronthaul</strong> (ön bağlantı) fiberidir; yoksa hücresiz kazanç doğmaz.",
            "legend_thz": "Soldan sağa spektrum: Sub-6 GHz kapsama, mmWave şehir kapasitesi, THz (0,1–10 THz) ultra geniş bant. Hortum genişler, menzil kısalır.",
            "legend_ai_ran": "Nöral kodlayıcı/alıcı <strong>PHY</strong> (Physical layer — fiziksel katman) araştırma ucudur. Üretimde çoğu iş <strong>RIC</strong> xApp/rApp döngüsüdür. Turuncu yay: uçtan uca kayıp geri beslemesi.",
            "legend_ntn": "<strong>LEO</strong> (Low Earth Orbit — alçak yörünge) ~500–1200 km. <strong>HAPS</strong> stratosfer (~20 km). Gateway yer kapısı; feeder link uyduyu karasal çekirdeğe bağlar. Direct-to-cell: çanak değil telefon.",
            "legend_ambient_iot": "Okuyucu <strong>RF</strong> taşıyıcı basar (enerji + referans). Etiket rectenna ile DC üretir, backscatter ile biti yansıtır. Pil yok; menzil kırıntı güce bağlıdır.",
            "wave_comm": "İletişim Dalgası (Veri Transferi)",
            "wave_radar": "Radar Yankısı (AoA / Doppler / Mesafe)",
            "cap_isac": "<strong>İnteraktif Sinyal Akışı:</strong> Mavi çizgi haberleşme verisini, yeşil-turuncu çizgi ise hedef algılama radar yankısını gösterir.",
            "cap_ris": "<strong>RIS Yansıma Prensipleri:</strong> Doğrudan yol bina ile engellenmişken, RIS gelen radyo dalgasının fazını kaydırarak sinyali kullanıcıya odaklar.",
            "cap_cf": "<strong>Hücresiz Yapı:</strong> Hücre sınırı yok. Tüm dağıtık AP'ler fiber ön bağlantı ile tek bir kullanıcıyı aynı anda besler.",
            "cap_thz": "<strong>Terahertz Spektrumu:</strong> Kızılötesi ile mmWave arasındaki ultra geniş bant alanını temsil eder.",
            "cap_ai": "<strong>Oto-Kodlayıcı Mimari:</strong> İnsan tasarımlı modülasyon yerine derin öğrenme ile öğrenilen katmanlar.",
            "cap_ntn": "<strong>Çok Katmanlı Ulaşım:</strong> Uydu -> HAPS -> Karasal Ağ entegrasyonu ile kesintisiz kapsama.",
            "cap_iot": "<strong>Geri Saçılım Prensibi:</strong> Cihaz pil içermez; gelen RF dalgasını modüle edip yansıtarak veri iletir.",
            "missing": "Diyagram bulunamadı.",
        },
    },
    "en": {
        "lang": {"tr": "TR", "en": "EN"},
        "app": {
            "page_title": "Türk Telekom | 6G Technology & Patent Intelligence",
            "brand": "Türk Telekom",
            "product": "6G R&D Platform",
            "badge": "Türk Telekom 6G R&D Platform",
            "title": "Türk Telekom 6G Technology &amp; Patent Intelligence Platform",
            "subtitle": "6G technologies, patent intelligence, and publication analytics",
            "footer": "© 2026 Türk Telekom R&D",
            "ai_provider": "AI provider: {provider}",
            "ai_logout": "End AI session",
            "provider_off": "off",
        },
        "nav": {
            "home": "Home",
            "tech": "6G Technologies",
            "patent": "Patent Intelligence",
            "publications": "Publication Trends",
            "tt": "Türk Telekom View",
            "ai": "AI Assistant",
            "about": "About",
        },
        "tt_page": {
            "view": "Türk Telekom view",
            "section": {
                "footprint": "Place in Europe",
                "scenario": "Field scenario",
            },
        },
        "settings": {"language": "Language", "language_help": "The interface and new AI answers switch to the selected language."},
        "depth": {
            "label": "Explanation depth",
            "radio": "Depth",
            "beginner": "Beginner",
            "expert": "Expert",
            "caption": "Foundation: problem → method → operating model. Expert: foundation + equation / 3GPP / assumption.",
        },
        "home": {
            "intro_beginner": """<div class="home-intro">
<h4>What is 6G</h4>
<p>
<strong>6G</strong> adds new jobs to 5G’s bit-carrying access architecture.
Today the site talks; it does not measure the scene, cannot turn a corner, and falls silent where there is no tower.
Seven inputs are candidates to close those gaps:
<strong>ISAC</strong> processes echo on the same RF chain;
<strong>RIS</strong> makes the façade a programmable reflector;
<strong>cell-free MIMO</strong> removes the cell edge as a design object;
<strong>NTN</strong> joins a LEO/HAPS cell to the core with Rel-17+;
<strong>AI-RAN</strong> puts RRM on a measurement loop;
<strong>Ambient IoT</strong> targets a batteryless backscatter tag;
<strong>THz</strong> opens bandwidth on a short hop.
</p>
<p class="home-intro-note">
They do not sit on the same shelf. Each sits on its own
<strong>TRL</strong> (Technology Readiness Level) rung;
the integer is mapped from a 3GPP technical report or a public trial class.
</p>
</div>""",
            "intro_expert": """<div class="home-intro">
<h4>What is 6G — expert reading (foundation is not skipped)</h4>
<p>
<strong>Foundation:</strong> 6G adds sensing, a programmable channel, distributed antennas, a satellite cell,
learned RRM and a batteryless tag as candidates on top of 5G’s communications-only architecture.
<strong>Expert:</strong> ISAC: shared waveform, R⁴, CRB–Shannon trade-off (TR 22.837).
RIS: Φ = diag(e^{jθ_n}), double-path loss, CSI delay (ETSI RIS ISG).
Cell-free MIMO: joint precoding; the bill is fronthaul/sync (Rel-19/20).
NTN: Rel-17 TR 38.811, Doppler f_d = f_c (v/c) cosθ, TRL 6.
AI-RAN: O-RAN RIC xApp/rApp, TR 38.843; neural PHY is the research edge.
Ambient IoT: Friis harvest × backscatter, TR 38.848.
THz: L(f,d) = FSPL · e^{K(f)d}, TR 38.807, TRL 3.
</p>
<p class="home-intro-note">
The seven inputs are not a single commercial “6G product”; they are standards inputs at different maturities.
Equations, assumptions and validity windows sit in the expert layer of <strong>6G Technologies</strong>.
</p>
</div>""",
            "cards_heading": "Seven Building Blocks",
            "cards_caption": "Each card states the field problem first, then the method. For the step-by-step walkthrough, equations, and the Türk Telekom scenario, open 6G Technologies in the sidebar.",
            "card_cta": "Step-by-step walkthrough: 6G Technologies → select this card",
            "cards_heading_expert": "Seven Building Blocks",
            "cards_caption_expert": "Each card states the problem plus the technical counterpart. For Shannon/CRB, 3GPP and the validity window, open 6G Technologies.",
            "card_cta_expert": "Equations and 3GPP context: 6G Technologies → select this card",
            "radar_heading": "### TRL radar — 3GPP / public-trial mapping",
            "radar_caption": "Slices use the NASA/EU TRL 1–9 scale; each integer is mapped from a 3GPP technical report or a public trial class.",
        },
        "trl": {
            "pill": "TRL {n}",
            "maturity": "TRL {n} Maturity Level",
            "explainer_title": "What TRL means",
            "explainer_lead": "{abbr} ({en}): {definition} {why}",
            "explainer_body": "1 is a basic principle; 9 is a product proven in an operational mission. These integers were not measured on a Türk Telekom network: the NASA/EU 1–9 scale is mapped from 3GPP specifications/work items and public trial class.",
            "explainer_ntn": "TRL 6 — Rel-17 NTN specification (TR 38.811) plus public Direct-to-Cell trials",
            "explainer_ris": "TRL 5 — ETSI RIS ISG / Rel-19–20 work item and O-RAN RIC trial class (RIS, AI-RAN)",
            "explainer_lab": "TRL 4 — Rel-19 work item / laboratory: ISAC (TR 22.837), cell-free MIMO, Ambient IoT (TR 38.848)",
            "explainer_thz": "TRL 3 — TR 38.807 plus laboratory spectrum: THz, not a street network",
            "scale_header": "Band",
            "scale_title": "Technology Readiness Level (TRL)",
        },
        "teach": {
            "problem": "Which problem?",
            "why_needed": "Why is it needed?",
            "what": "What does it do?",
            "tt_impact": "Türk Telekom and TRL",
            "heading": "Foundation layer — problem, need, method. Equations and 3GPP sit in the expert layer.",
            "heading_compact": "Definition layer (summary)",
            "heading_expert": "Expert layer — same sequence; equations, assumptions, 3GPP and alternatives. Sentences are not copies of Foundation.",
            "rail_beginner": "1 Problem · 2 Need · 3 Method · 4 Mechanism · 5 Limit · 6 Application",
            "rail_expert": "1 Problem · 2 Need · 3 Method · 4 Mechanism · 5 Limit · 6 Application · equation / 3GPP / alternative",
            "mental_model": "Operating model",
            "analogy": "Comparison",
            "analogy_map": "Technical counterpart",
            "when_used": "When to use it",
            "when_not": "When not to use it",
            "not_to_confuse": "What not to confuse it with",
            "real_world": "Where it actually shows up",
            "how_steps": "How it works — steps",
            "formula_heading": "#### Mathematical foundation — symbols, units, assumptions",
            "formula_caption": "Equations are not memorised: every symbol has a physical meaning, a reason for this form, and a validity window.",
            "equation": "Equation",
            "formula_fallback": "Formula",
            "symbol": "Symbol",
            "meaning": "Meaning",
            "unit": "Unit",
            "tells_us": "What it tells you",
            "why_this_form": "Why this form",
            "when_valid": "When it holds",
            "if_variable_changes": "If a variable rises or falls",
            "assumptions": "Assumptions and limits",
            "simple_example": "Simple quantitative example",
            "use_cases": "### Use cases — mechanism and limits",
            "use_cases_caption": "Each card is a real-world job. Foundation: what it is for. Expert: how it works and when it is the wrong tool.",
            "scenario_n": "Scenario #{n}",
            "how": "How:",
            "when_not_short": "When not:",
            "advantages": "### Advantages — where the gain comes from",
            "disadvantages": "### Disadvantages — which problems it creates",
            "global": "### Work worldwide",
            "global_caption": "This is not a name-drop list: each row says why the topic is on the standards or research agenda.",
            "tt_scenarios": "### Türk Telekom scenarios",
            "tt_caption": "Problem → why this technology → expected outcome. Not a field measurement.",
            "trl_assess": "### TRL assessment",
            "diagram_terms": "Diagram terms",
        },
        "tech": {
            "select": "Select the 6G Technology You Want to Inspect:",
            "select_fmt": "{icon} {title} (TRL {trl})",
            "badge": "6G TECHNOLOGIES",
            "section_label": "Technology section",
            "section": {
                "definition": "1. Technology Definition",
                "principle": "2. Operating Principle & Block Diagram",
                "architecture": "3. System Architecture",
                "use_cases": "4. Use Cases",
                "adv_dis": "5. Advantages & Disadvantages",
                "global_tt": "6. Global Work & TT Scenarios",
                "performance": "7. Performance Charts & References",
            },
            "def_heading": "### Technology definition — problem, method, limit",
            "expert_def": "Comparison — alternatives, assumptions, validity",
            "principle_beginner": "Operating principle — steps",
            "principle_expert": "Operating principle (mechanism + terms)",
            "principle_recall": "Foundation steps (not skipped)",
            "diagram": "### Block diagram",
            "arch_heading": "### System architecture and mathematical foundation",
            "arch_layers": "Three layers — abbreviations expanded on first use",
            "arch_expert": "Hardware / protocol / network layers",
            "math_on_arch": "Equation, symbol and assumption cards sit in section 3. System Architecture.",
            "perf_heading": "### Performance — verified record counts",
            "perf_caption": "There is no representative 5G/6G target bar. The charts below are this technology’s verified patent-record count and, when available, the OpenAlex publication trend.",
            "empty_patents": "No verified patent records for “{domain}”.",
            "openalex_fail": "OpenAlex did not return this topic; the publication trend is hidden.",
            "cell_free_oa": "Cell-free MIMO is not on the specification’s academic topic list; no OpenAlex series is shown.",
            "refs": "### Reference Papers & Publications",
            "refs_caption": "Links go to a DOI or an official 3GPP / project page.",
        },
        "patent": {
            "title": "Patent Intelligence",
            "subtitle": "6G patent records from global telecom vendors — every record is checkable on Google Patents. This set is not a full portfolio; it is a verified sample. Source: {source}",
            "filter": "Company (specification list: Nokia, Ericsson, Huawei, Samsung, Qualcomm, ZTE):",
            "all": "All",
            "what_title": "What this page is for",
            "what_body": """<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.65;margin:8px 0 0 0;">
A <strong>patent</strong> is a time-limited exclusive right in exchange for public disclosure of an invention.
This page is not legal advice. It is a <em>sample</em> map of which firms have filed in which 6G topics.
The <strong>assignee</strong> names who filed; it does not mean that firm has a product in the field.
</p>
<p style="color:#CBD5E1;font-size:0.88rem;line-height:1.6;margin:10px 0 0 0;">
<strong>TF-IDF (term frequency–inverse document frequency):</strong>
scores words in the abstract by how distinctive they are in the corpus.
The map does not extract meaning; it shows which records sit near which terms.
Abstracts are locked to the source — they are not rewritten or invented.
</p>
<p style="color:#94A3B8;font-size:0.84rem;margin:10px 0 0 0;">
Do not over-read: one patent is not market leadership. The year bar is filing/publication year,
not commercialisation date.
</p>""",
            "empty_company": "No verified patent records for “{company}”. Counts are not invented; charts stay hidden until a Google Patents-confirmed record is added.",
            "metric_total": "Verified patent records",
            "metric_leader": "Most records (assignee)",
            "metric_leader_delta": "{n} patents",
            "metric_domain": "Leading technology domain",
            "metric_domain_delta": "{n} records",
            "metric_source": "Source",
            "open_gp": "Open the Google Patents homepage ↗",
            "view": "Patent view",
            "section": {
                "year": "Patent Count / Year",
                "topics": "Topic Distribution & Word Cloud",
                "tree": "Patent Tree & Density",
                "map": "Technology Map & Network",
                "list": "Patent Titles",
                "tt_eu": "TT Europe footprint",
            },
            "year_heading": "### Distribution by year",
            "year_caption": "Each bar is a calendar year (e.g. 2024, 2025). Records have no month field, so there is no 2024.2 tick and no invented “Month 2” slice.",
            "empty_trend": "Not enough patent data for a trend chart.",
            "companies_heading": "### Companies with the most records",
            "empty_counts": "No data for a company count.",
            "empty_domain": "Domain mix could not be computed.",
            "empty_kw": "No data for keyword analysis.",
            "wordcloud": "### Word cloud",
            "wordcloud_caption": "Word frequency from verified patent titles only.",
            "empty_wc": "Word cloud needs wordcloud/matplotlib, or there are no tokens.",
            "density": "### Patent density chart",
            "empty_density": "No data for a density heatmap.",
            "tree_heading": "### Patent tree",
            "empty_tree": "No data for a tree chart.",
            "map_heading": "### Patent technology map",
            "map_caption": "Coordinates are TF-IDF title vectors reduced to 2-D with PCA; positions are not invented.",
            "empty_map": "The map needs at least two patents and scikit-learn.",
            "network": "### Assignee ↔ domain network",
            "empty_net": "No edge data for a network graph.",
            "list_heading": "### Verified 6G patent list",
            "list_caption": "Cards are newest to oldest by year. Each card has a publication number, title, assignee, year, and a Google Patents source link.",
            "assignee": "Assignee",
            "year": "Year",
            "open_record": "{pub} — open on Google Patents ↗",
        },
        "pub": {
            "title": "Publication Trends",
            "subtitle": "This page leads with the DOI-verified paper set. If a live OpenAlex count arrives, the global trend is added; if not, no invented number is shown. Source: {source}",
            "what_title": "What DOI, OpenAlex, and citations mean",
            "what_body": """<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.65;margin:8px 0 0 0;">
A <strong>DOI (Digital Object Identifier)</strong> is a persistent identity for a paper;
the “Open source” button on each card resolves that identity.
Inventing a DOI is forbidden on this platform.
</p>
<p style="color:#CBD5E1;font-size:0.88rem;line-height:1.6;margin:10px 0 0 0;">
<strong>OpenAlex</strong> is an open scholarly-graph API. Year / institution / country counts come from it;
if it is unreachable, the chart is hidden and no static global table is invented.
<strong>Citation count</strong> (<em>cited_by_count</em>) is how often a paper is referenced —
it is not a quality grade; a new paper can sit low, a review paper high.
Google Scholar does not expose a public API; the numbers here are from OpenAlex.
</p>""",
            "empty": "No verified paper records were found.",
            "metric_doi": "Verified papers (DOI)",
            "metric_oa_year": "OpenAlex {year} (6 topics)",
            "metric_topic": "Most active OpenAlex topic",
            "metric_cites": "Highest citation count (OpenAlex)",
            "open_oa": "Open the OpenAlex source page ↗",
            "snapshot": "Last successful OpenAlex cache: {ts}",
            "view": "Publication view",
            "section": {
                "doi": "Verified set (DOI)",
                "trend": "OpenAlex yearly trend",
                "inst": "Institutions",
                "country": "Countries",
                "papers": "Papers",
                "tt_eu": "TT Europe footprint",
            },
            "doi_heading": "### DOI-verified 6G papers",
            "doi_caption": "Bars are publication year and topic for papers listed on this platform. Each card’s button opens the paper via its DOI.",
            "chart_year": "Verified set — publication year",
            "chart_year_x": "Calendar year",
            "chart_topic": "Verified set — topic",
            "chart_publisher": "Verified set — publisher",
            "empty_year": "No year distribution.",
            "oa_heading": "### Publication counts by 6G topic (OpenAlex)",
            "oa_caption": "Counts come from an OpenAlex search. If the API and cache are empty, no chart is drawn and no static global number is invented.",
            "oa_empty": "OpenAlex did not respond live and the disk cache is empty. The DOI-verified set above remains usable. The trend fills automatically when OpenAlex recovers.",
            "try_oa": "Try OpenAlex in the browser ↗",
            "open_oa_counts": "Open these counts on OpenAlex ↗",
            "inst_heading": "### Institutions with the most publications",
            "oa_groupby": "OpenAlex group_by — 2020–2025, 6G topic search.",
            "chart_inst": "Publications by institution (OpenAlex)",
            "open_inst": "Open the OpenAlex institution filter ↗",
            "inst_fallback": "No live global count. The list below is OpenAlex author institutions from the DOI set only.",
            "chart_inst_fb": "Verified 8 papers — author institutions",
            "empty_inst": "No OpenAlex response for institutions. Use the DOI button on each paper card.",
            "cc_heading": "### Countries with the most publications",
            "chart_cc": "Publications by country (OpenAlex)",
            "open_cc": "Open the OpenAlex country filter ↗",
            "cc_fallback": "No live global count. The list below is OpenAlex country codes from the DOI set only.",
            "chart_cc_fb": "Verified 8 papers — country codes",
            "empty_cc": "No OpenAlex response for countries. Use the DOI button on each paper card.",
            "papers_heading": "### Verified 6G papers",
            "papers_caption": "Order: year newest to oldest; within a year, OpenAlex citations high to low. “—” if no citation count. Every record opens via DOI.",
            "citations_n": "{n} citations",
            "citations_na": "Citations: —",
            "authors": "Authors",
            "open_doi": "Open the paper via DOI ↗",
        },
        "tt_eu": {
            "what_title": "Why a patent is tied to a country",
            "what_body": """<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.65;margin:8px 0 0 0;">
A <strong>patent is territorial:</strong> a Turkish national filing creates a right only in Türkiye.
<strong>EPO (European Patent Office):</strong> one examination for EPC members; a granted EP is then validated in chosen states.
Türkiye is an EPO member; membership is not an automatic EP grant.
<strong>PCT (Patent Cooperation Treaty):</strong> a WO number is not a world patent.
</p>
<p style="color:#CBD5E1;font-size:0.88rem;line-height:1.6;margin:10px 0 0 0;">
This tab splits Türk Telekom’s <em>European place</em> into three things: (1) verified patent office,
(2) affiliation-locked papers, (3) collaboration / standards body. A partnership is not a grant.
The Nokia–ZTE filter is a vendor sample; this tab is the TT-group sample.
</p>""",
            "expert_title": "What this set verified — and what it did not",
            "expert_body": """<p style="color:#E2E8F0;font-size:0.9rem;line-height:1.65;margin:8px 0 0 0;">
Google Patents records locked here for the TT group sit under <strong>Netsia Inc.</strong> (USPTO).
Netsia is Argela/Türk Telekom’s US R&amp;D affiliate; the legal assignee is Netsia.
<strong>EP publication count in this sample is 0</strong> — it is shown, not invented.
Papers’ raw affiliation is “Türk Telekom, Ankara/Istanbul, Türkiye”. OpenAlex’s institution graph
can mis-map a record to a DE/MY/CZ company; the country bar on the global tab is not read as TT’s European output.
</p>""",
            "metric_pat": "TT-group verified patents",
            "metric_ep": "EPO (EP) records",
            "metric_papers": "TT-affiliated papers (DOI)",
            "metric_touch": "European touchpoints",
            "metric_named": "Named TTI countries",
            "role_title": "Market place: operator, not equipment vendor",
            "role_body": """<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.65;margin:8px 0 0 0;">
Türk Telekom is an <strong>integrated operator in Türkiye</strong> (fixed, mobile, broadband).
It is not a Nokia/Ericsson-class RAN vendor in the European 6G <em>equipment</em> market.
<strong>Türk Telekom International (TTI)</strong> is a 100% subsidiary for wholesale data/voice across
CEE–Türkiye–Caucasus–Middle East. The map paints only countries named in a locked source.
An unpainted European country is not a claim of absence — its name was not locked here.
</p>""",
            "map_heading": "### Europe map (countries named in a source)",
            "map_caption": "Layers are distinct: HQ, TTI wholesale first-mover, 6G R&amp;D partner, ETSI seat, MoU venue. Not subscriber or revenue share.",
            "map_fail": "The map could not be drawn; the list below is the complete set of countries named in a source.",
            "role_heading": "### Evidence type (how many named countries)",
            "role_caption": "The EP-grant bar is 0. Wholesale 6 is TTI About’s first-mover list, not the full 19 or 24.",
            "vs_heading": "### This platform’s locked 6G sample",
            "vs_caption": "Nokia–ZTE bars are verified 6G sample records. The TT bar is Netsia USPTO grants. Not global SEP or revenue share.",
            "office_heading": "### Patent office (verified set)",
            "office_caption": "EP=0 means no European regional grant in this sample. The 921 national-filing claim is not plotted.",
            "pat_list_heading": "### Netsia Inc. (Türk Telekom group) — Google Patents",
            "pat_list_caption": "Assignee is Netsia Inc. Cards are newest to oldest by year. These cards are not mixed into the Nokia–ZTE vendor set.",
            "named_heading": "### Countries named in a source (complete list)",
            "named_caption": "This is the full set painted on the map. The 19 or 24 country names are not in the report; they are not added.",
            "named_col_place": "Country",
            "named_col_layer": "Layer",
            "presence_heading": "### 6G touchpoints — collaboration / standards / project",
            "presence_caption": "Each card is an official announcement. Equal-height “1 per country” bars are not drawn; they read as market share.",
            "oa_heading": "### Do not read the OpenAlex country chart as TT-in-Europe",
            "oa_caption": "The Countries tab above is a global 6G topic search, not a TT portfolio. Raw affiliation on the papers below is TR.",
            "papers_heading": "### Papers with Türk Telekom R&amp;D affiliation",
            "papers_caption": "DOIs are locked. Order: year newest to oldest; within a year, OpenAlex citation count (cited_by_count) high to low.",
            "open_touch": "Open the source announcement ↗",
            "open_press": "Open the national-filing statement ↗",
            "open_ir": "2024 integrated report PDF ↗",
            "open_tti": "Open the TTI About page ↗",
            "overview_heading": "### Europe-wide — TT publication and patent rank",
            "overview_caption": "Each country: the locked 3 MNOs + TT. Publications = OpenAlex 6G search, or (TT in TR) DOI-locked affiliation. Patents = this platform’s sample (Netsia USPTO on the TR row only). Rank 1 is the highest count. Not subscriber share.",
            "overview_spin": "Loading country ranks from the OpenAlex cache / live query",
            "overview_pub_title": "TT publication count (country, high to low)",
            "overview_pat_title": "TT sample patent count (country, high to low)",
            "overview_tt_pub": "TT papers",
            "overview_tt_pat": "TT patents",
            "overview_pub_lead": "Pub. leader (n)",
            "overview_pat_lead": "Patent leader (n)",
            "rank_heading": "### Country detail: 3 MNOs (mobile network operators) + Türk Telekom",
            "rank_caption": "The three operators are locked from that country’s row in the Wikipedia European MNO list; subscriber/revenue “top 3” was not measured here. Publication counts are an OpenAlex 6G topic search. Patent counts are this platform’s locked sample only (EP=0 for TT; Netsia USPTO is counted on the TR row only). Not global SEP or market share.",
            "rank_country": "European country",
            "rank_pub_title": "Publication rank (OpenAlex, this country)",
            "rank_pat_title": "Patent rank (locked sample)",
            "rank_pub_x": "OpenAlex publication count",
            "rank_pat_x": "Sample patent records",
            "rank_tt": "Türk Telekom in this country: publications rank {pub} ({pub_n} OpenAlex records) · patents rank {pat} ({pat_n} sample records) — {n} firms",
            "rank_oa_fail": "OpenAlex did not answer for this country; the publication bars are not drawn.",
            "rank_col_rank_pub": "Pub. rank",
            "rank_col_pub": "Publications (OpenAlex)",
            "rank_col_rank_pat": "Patent rank",
            "rank_col_pat": "Patents (sample)",
            "rank_open_oa": "Open this country’s OpenAlex query ↗",
            "rank_open_wiki": "Open the European MNO list ↗",
            "rank_open_gp": "Google Patents assignee ↗",
            "layer": {
                "hq": "HQ / operator R&D",
                "wholesale": "TTI wholesale (first-mover)",
                "rd_collab": "6G R&D partnership",
                "standards": "Standards body (ETSI)",
                "mou_venue": "MoU signing venue",
                "ep_grant": "EPO (EP) grant",
            },
        },
        "ui": {
            "source": "Open Source ↗",
            "no_source": "No source link.",
        },
        "scenario": {
            "title": "Türk Telekom 6G field-deployment scenario engine",
            "lead": "A 6G technology-matching engine driven by Turkish geography, Türk Telekom infrastructure, and strategic R&D priorities.",
            "kpi_body": """<p style="color:#E2E8F0;font-size:0.88rem;line-height:1.6;margin:0;">
A <strong>KPI (key performance indicator)</strong> is a tracking number such as rate, latency, or energy.
Values here are not a field ping; they are the output of a rule-based scenario engine.
<strong>CAPEX (capital expenditure)</strong> is a coarse label for investment scale — towers, fibre, satellite capacity —
not a tender price.
</p>
<p style="color:#94A3B8;font-size:0.84rem;line-height:1.55;margin:8px 0 0 0;">
Assumption: the region + density + priority triple selects a technology set. Limit: rain, permits, spectrum,
and the real fibre topology are not in the model. Do not read the numbers as measured 6G performance.
</p>""",
            "params": "### Scenario parameters",
            "region": "1. Deployment region / scenario area",
            "region_help": "Türk Telekom field or infrastructure region to match",
            "density": "2. Target user / sensor density",
            "density_help": "Devices and sensors per square kilometre in the region",
            "priority": "3. Primary strategic objective",
            "priority_help": "The primary performance or business goal for this deployment",
            "metrics_exp": "Detailed performance and metric summary",
            "capex_caption": "CAPEX (capital expenditure) scale — not a tender price: **{value}**",
            "kpi_note": "KPI values are the rule-based scenario engine’s output; they are not field measurements.",
            "result_heading": "### Recommended Türk Telekom architecture and KPI analysis",
            "techs": "**Recommended 6G technologies:** {techs}",
            "solution": "**Field solution architecture:**",
            "priority_impact": "**Strategic-objective impact:**",
            "density_profile": "**Density profile:** {value}",
            "metric_speed": "Peak rate capacity",
            "metric_latency": "Latency",
            "metric_energy": "Energy score",
            "feasibility": "**Feasibility and field-fit score:** `{score}`",
            "region_bosphorus": "Istanbul Bosphorus and Marmara shoreline (ISAC + THz)",
            "region_stadium": "RAMS Park / stadium and dense event venues (cell-free MIMO)",
            "region_industry": "Marmara industrial zone / autonomous factories (Ambient IoT + AI-RAN)",
            "region_disaster": "AFAD-integrated earthquake and disaster zone (NTN + ISAC)",
            "region_historic": "Historic Peninsula / narrow-street urban fabric (RIS + sub-THz)",
            "region_datacenter": "Türk Telekom Ankara and Istanbul data centres (THz mesh)",
            "density_low": "Low (rural / open)",
            "density_medium": "Medium (urban)",
            "density_high": "High (stadium / plaza)",
            "density_extreme": "Extreme (trillion-sensor scale)",
            "priority_coverage": "Unbroken coverage (zero gap)",
            "priority_speed": "Ultra-high rate (terabit/s)",
            "priority_energy": "Low energy / green network",
            "priority_resilience": "Disaster resilience",
            "title_bosphorus": "Istanbul Bosphorus and Marmara shoreline",
            "title_stadium": "RAMS Park / stadium and dense event venues",
            "title_industry": "Marmara industrial zone / autonomous factories",
            "title_disaster": "AFAD-integrated earthquake and disaster zone",
            "title_historic": "Historic Peninsula / narrow-street urban fabric",
            "title_datacenter": "Türk Telekom Ankara and Istanbul data centres",
            "sol_bosphorus": "ISAC radar sensing integrated on shoreline 6G sites, plus inter-site THz wireless fibre-class backhaul.",
            "sol_stadium": "Cell-free coverage from 200+ mini access points on stands and roof, plus AI-RAN dynamic load balancing.",
            "sol_industry": "Battery-free Ambient IoT tags on the factory floor, plus passive RIS panels as wall cladding.",
            "sol_disaster": "LEO direct-to-cell to smartphones, plus through-wall RF rubble sensing.",
            "sol_historic": "Transparent passive RIS cladding on façades without breaking the historic fabric.",
            "sol_datacenter": "Wireless THz mesh between server racks, plus AI-RAN deep-sleep modes.",
            "year_bosphorus": "2028 field pilot",
            "year_stadium": "2027 prototype trial",
            "year_industry": "2026 industrial PoC",
            "year_disaster": "3GPP Rel-18/19 integration",
            "year_historic": "2027 urban pilot",
            "year_datacenter": "2026 laboratory demo",
            "capex_mid_high": "Medium–high",
            "capex_high": "High",
            "capex_low_opt": "Low–optimal",
            "capex_strategic": "Strategic investment",
            "capex_low": "Low",
            "kpi_coverage": "Zero dead zones (99.999% reliability and coverage target)",
            "kpi_speed": "1 Tbps peak rate and ultra-wide bandwidth (literature target)",
            "kpi_energy": "Green 6G — high energy-efficiency target (AI-RAN deep sleep)",
            "kpi_resilience": "Emergency satellite path if terrestrial towers fail",
            "dens_low": "Rural / wide-area extended coverage",
            "dens_medium": "Balanced urban macro–micro layer",
            "dens_high": "Dense urban / stadium multi-beam allocation",
            "dens_extreme": "Trillion-device-scale battery-free tags and ultra-massive cell-free",
            "nodes_low": "500 devices / km²",
            "nodes_medium": "50,000 devices / km²",
            "nodes_high": "500,000 devices / km²",
            "nodes_extreme": "1,000,000+ sensors / km²",
            "nodes_default": "10,000 / km²",
            "impact": "A 6G architecture was tailored for **{region}**, with priority **{priority}** and density target **{density}**.\n\n• **Capacity and rate:** {capacity} Gbps peak throughput\n• **Latency:** {latency} ms (ultra-reliable low-latency target)\n• **Network density:** {nodes}\n• **Energy-efficiency score:** {energy}%",
        },
        "auth": {
            "title": "API key for the AI Assistant",
            "lead": "The key stays in this session only. Modules 1–3 and the Türk Telekom view run without a key.",
            "provider": "AI provider",
            "groq": "Groq (gsk_...)",
            "gemini": "Google Gemini (AIza...)",
            "key": "API key",
            "keys_help": "Get a key: [Groq Console](https://console.groq.com/keys) · [Google AI Studio](https://aistudio.google.com/apikey)",
            "env_info": "`{provider}_API_KEY` is set in `.env`. Use the button below to open the assistant with the environment key.",
            "open_env": "Open AI with the `.env` key",
            "open": "Open the AI Assistant",
            "empty_key": "Please enter a valid API key.",
            "spinner": "Validating the API key…",
            "no_key_caption": "Without a key the assistant still returns short answers from verified records via TF-IDF.",
            "continue": "Continue without a key (local retrieval only)",
            "empty": "API key cannot be empty.",
            "bad_provider": "Invalid provider selection.",
            "groq_ok": "Groq API key validated.",
            "groq_missing": "The Groq library is not installed. pip install groq",
            "groq_bad": "Groq key is invalid: {exc}",
            "gemini_ok": "Gemini API key validated.",
            "gemini_missing": "The Gemini library is not installed. pip install google-genai",
            "gemini_bad": "Gemini key is invalid: {exc}",
        },
        "ai": {
            "title": "AI Assistant",
            "lead": "Answers are grounded in technology, patent, paper, and glossary records selected with sklearn TF-IDF. The dual-depth sidebar sets the explanation level (foundation: problem and operating model; expert: equation + assumption). Mode: <strong style=\"color:#00E5FF;\">{mode}</strong> · Provider: <strong style=\"color:#00E5FF;\">{provider}</strong>",
            "mode_llm": "LLM + TF-IDF",
            "mode_local": "TF-IDF only (local)",
            "caption": "Patent numbers, DOIs, or citation counts that are not in context are not invented.",
            "chip_ris": "What is RIS?",
            "chip_diff": "NTN vs ISAC",
            "chip_patents": "Patent data summary",
            "chip_patents_q": "Summarise the verified patent records on this platform.",
            "welcome": "Hello — I am the Türk Telekom 6G AI assistant. My answers rest on verified records in Modules 1–3; I do not invent facts that are not on the platform.",
            "placeholder": "Ask about a 6G technology, patent, or paper…",
            "spinner": "Generating an answer from verified records…",
            "empty_q": "Please enter a question.",
            "fallback_none": "### 6G assistant (retrieval mode)\n\nYour question did not match the platform corpus. Review the verified sources on 6G Technologies, Patent Intelligence, or Publication Trends.",
            "related": "**Related verified records:**",
            "tfidf_note": "*This answer is from platform records selected with TF-IDF; numbers are not invented.*",
            "llm_fail": "*The LLM did not return an answer: {exc}*",
            "glossary_title": "Technical glossary (first-use expansions)",
            "cite_n": "{n} citations",
            "cite_na": "citation count was not returned by OpenAlex",
            "pedagogy": "Teaching rule: for an important concept cover what it is, why it is needed, what it does, how it works, when to use it, when not to, what not to confuse it with, and where it shows up in the real world. On first use expand an abbreviation as ABBR (English expansion); then use the abbreviation. If you cite an equation, name the symbols and the assumption; do not drill memorisation. Do not invent numbers, patent IDs, DOIs, or citation counts that are not in context. If you are unsure, say the platform data does not contain that information.",
            "depth_beginner": "Level: FOUNDATIONAL. Lead with problem, need, method, operating model, when / when-not, and what not to confuse it with. Do not talk down. If an equation is needed, explain the symbols and keep the assumption.",
            "depth_expert": "Level: EXPERT. Do not skip the conceptual foundation; then add the equation, assumption, limit, and alternative.",
            "ctx_header": "=== VERIFIED 6G DATA CONTEXT (TF-IDF-selected passages) ===",
            "ctx_rule": "RULE: Do not invent a number, patent ID, or paper that is not in this context. If unsure, say the platform data does not contain that information.",
            "system": "You are the Türk Telekom 6G R&D assistant. Use only the given context. Do not guess or invent. USER_LANGUAGE = en. Write the answer directly in natural, professional English — do not translate from Turkish. Use established technical terminology.",
            "user_wrap": "User question: {question}",
        },
        "about": {
            "heading": "### About",
            "card": """<div class="glass-card" style="border-left: 5px solid #00E5FF;">
<h4 style="color:#00E5FF; margin-top:0;">6G Technology &amp; Patent Intelligence Platform</h4>
<p style="color:#E2E8F0; font-size:0.95rem; line-height:1.6; margin-bottom:0;">
A Streamlit portal for the Türk Telekom 6G R&amp;D team: 6G technologies, academic publications,
and patent trends in one place.
Developer: <strong>Zeynep Ebrar Pala</strong>.
</p>
</div>""",
            "modules": "#### Modules",
            "mod_left": """
- **Home** — TRL radar for the seven technologies; dual-depth (foundation/expert) switches the intro
- **6G Technologies** — conceptual foundation plus expert layer (equation, assumption, comparison); every section respects depth
- **Patent Intelligence** — Nokia, Ericsson, Huawei, Samsung, Qualcomm, ZTE; TT Europe footprint; year, topic, word cloud, tree, density, map; abstracts locked to the source
- **Publication Trends** — OpenAlex year / institution / country; DOI-verified papers; TT Europe footprint
            """,
            "mod_right": """
- **Türk Telekom View** — field scenario engine
- **AI Assistant** — local TF-IDF retrieval; optional Groq / Gemini
- **About** — this page (delivery / 15-minute talk outline)
            """,
            "stack": "#### Stack",
            "stack_body": "Python, Streamlit, Pandas, Plotly, Matplotlib, NetworkX, WordCloud, scikit-learn. Optional: Groq API, Google Gemini API. Patent source: Google Patents. Academic: OpenAlex + DOI (IEEE Xplore, Springer, Elsevier).",
            "standard": "#### Teaching standard",
            "standard_body": "Technical content is two-layer: **foundation** (what / why / how / when) and **expert** (equation, assumption, 3GPP). Expert mode does not skip the foundation. Abbreviations expand on first use. Patent abstracts, DOIs, and numbers are not invented.",
            "talk": "#### 15-minute talk outline",
            "talk_body": """
1. Purpose and scope (1 min)
2. Home TRL radar (2 min)
3. One technology (e.g. RIS) — principle + diagram + TT scenario (3 min)
4. Patent Intelligence — company filter, year chart, TT Europe footprint (3 min)
5. Publication Trends — OpenAlex year + institution/country + TT-affiliated DOI (3 min)
6. AI Assistant — “What is RIS?” and “NTN vs ISAC” (2 min)
7. Source rule: no invented IDs or counts (1 min)
        """,
            "usage": "See USAGE_GUIDE.md in the repository for walkthrough steps.",
        },
        "charts": {
            "year": "Calendar year",
            "trl_series": "TRL",
            "trl_title": "TRL mapping (3GPP / trial class → 1–9)",
            "trl_hover": "%{theta}<br>TRL %{r}<br>%{customdata}<extra></extra>",
            "tech_counts": "Verified {label} patent records / year",
            "count": "Record count",
            "patent_year": "6G patent records by year (verified set)",
            "patent_count": "Patent record count",
            "domain_radar": "Company 6G technology-domain mix (%)",
            "keywords": "Most frequent keywords in patent claims",
            "kw_x": "Claim occurrences",
            "academic_trend": "Academic publication trend (OpenAlex, by topic)",
            "pub_count": "Publication count",
            "db_default": "Verified sample set — publisher count",
            "publisher": "Publisher",
            "paper_count": "Paper count",
            "network": "Assignee ↔ technology-domain network",
            "nx_missing": "NetworkX is not installed; the network graph cannot be shown.",
            "company_counts": "Companies with the most records (verified set)",
            "company": "Company",
            "density": "Patent density (company × domain, record count)",
            "sunburst": "Patent tree (company → domain → record)",
            "tfidf": "Patent technology map (TF-IDF + PCA, title vectors)",
            "oa_bar_x": "Publication count (OpenAlex)",
            "tt_office": "TT-group patent office (verified set)",
            "tt_office_x": "Office code (EP / US / TR)",
            "tt_europe": "TT European touchpoints (collaboration / standards / project)",
            "tt_europe_x": "Verified touchpoint count",
            "tt_map": "TT in Europe — only countries named in a source",
            "tt_role": "TT evidence type (named-country count)",
            "tt_role_x": "Named countries / records",
            "tt_vs_vendors": "Locked 6G sample vs TT-group (Netsia)",
        },
        "diagram": {
            "isac_ue": "User equipment (UE)",
            "ris_tx": "6G transmitter (Tx)",
            "ris_bldg": "Building (blockage)",
            "ris_surface": "Intelligent surface (RIS mirror)",
            "ris_rx": "User (Rx)",
            "cf_cpu": "Central processor (CPU)",
            "cf_user": "User",
            "thz_rate": "1 terabit/s data rate",
            "thz_bw": "0.1–10 THz ultra-wide bandwidth",
            "ai_enc": "Neural encoder",
            "ai_enc_sub": "(deep-learning transmitter)",
            "ai_ch": "Physical channel",
            "ai_ch_sub": "+ noise and fading",
            "ai_dec": "Neural decoder",
            "ai_dec_sub": "(deep-learning receiver)",
            "ai_loss": "End-to-end feedback and loss function",
            "ntn_leo": "LEO satellite constellation (600 km)",
            "ntn_haps": "HAPS airship (20 km)",
            "ntn_gw": "TT satellite gateway",
            "ntn_phone": "Smartphone",
            "iot_reader": "6G reader",
            "iot_reader_sub": "(signal generator)",
            "iot_in": "Incoming RF carrier (energy source)",
            "iot_out": "Reflected modulated data (backscatter)",
            "iot_tag": "Battery-free IoT tag",
            "iot_tag_sub": "(RF energy harvesting)",
            "legend_isac": "<strong>gNB</strong> (next-generation Node B) both transmits data and listens for echoes. <strong>UE</strong> (user equipment) is the communication endpoint. <strong>AoA</strong> (angle of arrival) is direction from array phase; <strong>Doppler</strong> is the radial speed component. Tx/Rx: transmitter and receiver in the same box.",
            "legend_ris": "<strong>Tx</strong> is the transmitting gNB; <strong>Rx</strong> is the user UE. <strong>NLoS</strong> (non-line-of-sight): the building blocks the direct path; RIS opens an alternative path by shifting phase. RIS does not generate internet on its own.",
            "legend_cell_free": "An <strong>AP</strong> (access point) is a small street radio. The <strong>CPU</strong> computes joint precoding. The dashed line is <strong>fronthaul</strong> fibre; without it the cell-free gain does not appear.",
            "legend_thz": "Spectrum left to right: sub-6 GHz coverage, mmWave urban capacity, THz (0.1–10 THz) ultra-wide band. The hose gets wider; the range gets shorter.",
            "legend_ai_ran": "A neural encoder/decoder is a <strong>PHY</strong> (physical layer) research edge. In production most of the work is the <strong>RIC</strong> xApp/rApp loop. Orange arc: end-to-end loss feedback.",
            "legend_ntn": "<strong>LEO</strong> (low Earth orbit) is ~500–1200 km. <strong>HAPS</strong> sits in the stratosphere (~20 km). The gateway is the ground door; the feeder link ties the satellite to the terrestrial core. Direct-to-cell: a phone, not a dish.",
            "legend_ambient_iot": "The reader transmits an <strong>RF</strong> carrier (energy + reference). The tag makes DC with a rectenna and reflects the bit via backscatter. No battery; range tracks leftover power.",
            "wave_comm": "Communication wave (data transfer)",
            "wave_radar": "Radar echo (AoA / Doppler / range)",
            "cap_isac": "<strong>Interactive signal flow:</strong> The blue line is the communications payload; the green–orange line is the sensing echo.",
            "cap_ris": "<strong>RIS reflection:</strong> The direct path is blocked by the building; RIS shifts the phase of the incoming wave and focuses it toward the user.",
            "cap_cf": "<strong>Cell-free layout:</strong> No cell edge. Distributed APs jointly serve one user over fibre fronthaul.",
            "cap_thz": "<strong>Terahertz spectrum:</strong> The ultra-wide band between millimetre-wave and infrared.",
            "cap_ai": "<strong>Autoencoder architecture:</strong> Layers learned with deep learning instead of a hand-designed modulation.",
            "cap_ntn": "<strong>Multi-layer access:</strong> Satellite → HAPS → terrestrial network for continuous coverage.",
            "cap_iot": "<strong>Backscatter:</strong> The device has no battery; it modulates and reflects the incoming RF wave to send data.",
            "missing": "Diagram not found.",
        },
    },
}
