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
            "subtitle": "6G Teknoloji Rehberi · Patent Zekası · Akademik Yayın Analizi",
            "footer": "© 2026 Türk Telekom Ar-Ge",
            "ai_provider": "AI sağlayıcı: {provider}",
            "ai_logout": "AI oturumunu kapat",
            "provider_off": "kapalı",
        },
        "nav": {
            "home": "Ana Sayfa",
            "tech": "6G Teknoloji Rehberi",
            "patent": "Patent Zekası",
            "publications": "Akademik Yayın Analizi",
            "tt": "Türk Telekom Görünümü",
            "ai": "AI Asistanı",
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
Denklem, varsayım ve geçerlilik penceresi <strong>6G Teknoloji Rehberi</strong> uzman katmanındadır.
</p>
</div>""",
            "cards_heading": "Yedi Yapı Taşı",
            "cards_caption": "Kartta önce sahadaki sorun, sonra çözüm vardır. Adım adım anlatım, formül ve Türk Telekom senaryosu için soldan «6G Teknoloji Rehberi» menüsüne geçin.",
            "card_cta": "Adım adım anlatım: 6G Teknoloji Rehberi → bu kartı seçin",
            "cards_heading_expert": "Yedi Yapı Taşı",
            "cards_caption_expert": "Kartta problem + teknik karşılık vardır. Shannon/CRB, 3GPP ve geçerlilik penceresi için «6G Teknoloji Rehberi»ne geçin.",
            "card_cta_expert": "Denklem ve 3GPP bağlamı: 6G Teknoloji Rehberi → bu kartı seçin",
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
            "badge": "6G TEKNOLOJİ REHBERİ",
            "section_label": "Teknoloji bölümü",
            "section": {
                "definition": "1. Tanım",
                "principle": "2. Çalışma prensibi ve blok diyagram",
                "architecture": "3. Sistem mimarisi",
                "use_cases": "4. Kullanım alanları",
                "adv_dis": "5. Avantajlar ve dezavantajlar",
                "global_tt": "6. Dünyadaki çalışmalar ve TT senaryoları",
                "performance": "7. Performans grafikleri ve referans makaleler",
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
            "perf_caption": "Temsili 5G/6G hedef barı yok. Aşağıdaki grafikler bu teknolojinin doğrulanmış patent kayıt sayısı ve (varsa) Crossref 6G başlık yayın trendidir.",
            "empty_patents": "«{domain}» için doğrulanmış patent kaydı yok.",
            "pub_fail": "Bu konu için yayın yılı serisi yok; grafik gizlenir.",
            "cell_free_pub": "Cell-Free, şartnamedeki akademik konu listesinde yoktur; konu serisi gösterilmez.",
            "refs": "### Referans Makaleler & Yayınlar",
            "refs_caption": "Bağlantılar DOI veya resmi 3GPP / proje sayfalarına gider.",
        },
        "patent": {
            "title": "Patent Zekası",
            "subtitle": "Nokia, Ericsson, Huawei, Samsung, Qualcomm, ZTE, NEC, NICT, Intel — yedi 6G konusu (ISAC, RIS, Cell-Free, THz, AI-RAN, NTN, Ambient IoT). Kaynak: {source}",
            "filter": "Firma (Nokia, Ericsson, Huawei, Samsung, Qualcomm, ZTE, NEC, NICT, Intel):",
            "all": "Tümü",
            "what_title": "Bu sayfa ne işe yarar?",
            "what_body": """<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.65;margin:8px 0 0 0;">
<strong>Patent Zekası</strong> rakip portföyü <strong>6G Technology Explorer</strong> yedilisinden çeker:
<strong>ISAC</strong> (Integrated Sensing and Communication — bütünleşik sezim ve haberleşme),
<strong>RIS</strong> (Reconfigurable Intelligent Surfaces — yeniden yapılandırılabilir akıllı yüzeyler),
<strong>Cell-Free Massive MIMO</strong> (hücresiz çok-antennli erişim),
<strong>THz</strong> (terahertz haberleşme),
<strong>AI-Native RAN</strong> (yapay zekâ yerlisi radyo erişim ağı),
<strong>NTN</strong> (Non-Terrestrial Networks — yer-dışı ağlar),
<strong>Ambient IoT</strong> (ortam enerjili nesnelerin interneti).
</p>
<p style="color:#CBD5E1;font-size:0.88rem;line-height:1.6;margin:10px 0 0 0;">
Dokuz applicant: Nokia, Ericsson, Huawei, Samsung, Qualcomm, ZTE, NEC, NICT (National Institute of Information and Communications Technology — Japonya ulusal BİT enstitüsü), Intel.
Firma çubuğu bu yedi konunun Lens <code>total</code> değeridir — ham «6G» kelimesi değildir (telefon/6G gürültüsü karışmaz).
Diğer grafikler çekilen kayıttır (başlık + yayın no + yıl). İki katman toplanmaz. Yüzde yok.
</p>
<p style="color:#94A3B8;font-size:0.84rem;margin:10px 0 0 0;">
Bir kayıt sayfaya ancak yedi sorgudan birine düşünce girer; etiket o sorgunun konusudur. <strong>Unclassified yoktur</strong> — eşleşmeyen satır düşer, uydurulmaz.
<strong>Applicant</strong> kimin başvurduğunu söyler; sahada ürün değildir. Tek patent = pazar liderliği değildir. Yıl = yayın yılıdır.
</p>""",
            "access_title": "Veri nereden geliyor?",
            "access_body": """<p style="color:#E2E8F0;font-size:0.88rem;line-height:1.6;margin:8px 0 0 0;">
Bu sayfa yalnızca <strong>Lens.org</strong> patent API’sini kullanır (<code>POST /patent/search</code>).
Siteye giriş yetmez; profildeki Access Token gerekir (<code>LENS_TOKEN</code> veya bu sayfadaki kutu).
Toplam: JSON <code>total</code>. Kartlar ve diğer grafikler <code>data</code> satırıdır.
HTML kazınmaz. Yanıt yoksa hücre —.
</p>""",
            "expert_title": "Çekilen kayıt ve sınır",
            "expert_body": """<p style="color:#E2E8F0;font-size:0.88rem;line-height:1.65;margin:8px 0 0 0;">
Firma çubuğu: yedi konu DSL’inin OR’u × <code>applicant.name</code> (Lens <code>total</code>).
Çekilen satır: konu başı en fazla 100, dokuz firma OR süzülür. Aynı yayın no iki konuya düşerse listedeki ilk konu kalır (ISAC → … → Ambient IoT).
Radar / yoğunluk / ağaç ekseni kayıt sayısıdır (yüzde değil). Başlık yeniden yazılmaz.
429 olursa <code>x-rate-limit-retry-after-seconds</code> kadar beklenir.
</p>""",
            "key_gp": "Lens.org ↗",
            "key_lens": "Lens.org — API ve Data (token) ↗",
            "key_espacenet": "Lens.org ↗",
            "key_wipo": "Lens.org ↗",
            "key_uspto": "Lens.org ↗",
            "token_label": "Lens Access Token",
            "token_missing": "api.lens.org/patent/search tarayıcıda açılmaz; 401 (Missing Authorization) normaldir. Token, giriş yaptığınız Lens hesabında API ve Data → plan onayı → Create Token ile üretilir. Buraya veya .env LENS_TOKEN= satırına yapıştırın. Token sohbete yazılmasın.",
            "token_help": "Staj için Trial / Academic planını seçin. Onay mailinden sonra Access Token oluşur. HTML kazınmaz; uygulamayı yenileyin.",
            "api_error": "Lens API yanıt vermedi ({detail}). Sayı uydurulmaz.",
            "live_gp_heading": "### Lens.org — hak sahibi (örnek küme değil)",
            "live_gp_spin": "Lens.org tam sayılar arka planda soruluyor (ilk sefer birkaç dakika; sonra önbellek)",
            "bg_wait": "Sayılar arka planda doluyor ({done}/{total}). Sol menüden Yayınlar’a geçebilirsiniz; bu sayfa kilitlenmez.",
            "bg_partial": "Gelen tam sayılar çizilir. Henüz gelmeyen hücre boş kalır; sayı uydurulmaz.",
            "live_gp_caption": "Aynı konu sorgusu + applicant.name. Yanıt yoksa —. Bu sayılar kilitli örnek çubuklarla toplanmaz.",
            "live_gp_metric": "Lens.org (hak sahibi)",
            "live_gp_empty": "Lens bu sorgu için toplam vermedi; sayı uydurulmaz.",
            "live_col_firm": "Firma",
            "live_col_n": "API toplam",
            "live_col_sample": "Örnek küme",
            "empty_company": "«{company}» için Lens.org kayıt döndürmedi. Sayı uydurulmaz.",
            "empty_topic": "Bu konuda Lens kayıt yok. Sayı uydurulmaz. Ofis düğmeleri aynı sorguyu sitede açar.",
            "metric_total": "Çekilen kayıt",
            "metric_pulled": "Çekilen kayıt",
            "pulled_caption": "Kartlar ve kelime bulutu çekilen satırdır. Firma / yıl / konu / radar / ağaç / yoğunluk çubukları Lens total (tam sayı); 100 tavanı yok. İki katman toplanmaz.",
            "metric_leader": "En Fazla Kayıt (Applicant)",
            "metric_leader_delta": "{n} patent",
            "metric_domain": "Öne Çıkan Teknoloji Alanı",
            "metric_domain_delta": "{n} kayıt",
            "metric_source": "Kaynak",
            "open_gp": "Lens.org patent aramasını aç ↗",
            "view": "Bölüm",
            "section": {
                "charts": "Rakip patent grafikleri",
                "tt_eu": "Türk Telekom patent izi",
            },
            "year_heading": "### Patent sayısı / yıl",
            "year_caption": "Lens year_published tam sayısı, firma × yıl. Yuvarlama yok. 2026 eksik yıldır.",
            "empty_trend": "Trend grafiği için yeterli patent verisi yok.",
            "companies_heading": "### En çok çalışan firmalar",
            "companies_caption": "Lens.org total: yedi 6G konusu (OR) + applicant. Ham «6G» değil. 0 = bu sorguda kayıt yok; çubuk durur, sayı uydurulmaz.",
            "topic_mix_heading": "### Patent konusu dağılımı",
            "topic_mix_caption": "Lens total: yedi konu × dokuz applicant (OR). 100 tavanı / yuvarlama yok. Unclassified yok.",
            "radar_heading": "### Radar grafiği",
            "radar_caption": "Firma × konu Lens total. Eksen yüzde değil; 100 tavanı yok.",
            "empty_counts": "Firma sayımı için veri yok.",
            "empty_domain": "Domain dağılımı hesaplanamadı.",
            "empty_kw": "Anahtar kelime analizi için veri yok.",
            "wordcloud": "### Kelime Bulutu",
            "wordcloud_caption": "Çekilen patent başlıklarındaki kelime sıklığı (tam sayı).",
            "empty_wc": "Kelime bulutu için wordcloud/matplotlib yüklü değil veya kelime yok.",
            "density": "### Patent Yoğunluk Grafiği",
            "density_caption": "Hücre = Lens total (tam sayı). Renk ölçeği aynı tam sayıdır.",
            "empty_density": "Yoğunluk haritası için veri yok.",
            "tree_heading": "### Patent Ağacı",
            "tree_caption": "Treemap: dış kutu firma, iç kutu 6G konusu. Alan = Lens total. İsim tekrar etmez; yayın numarası yok.",
            "empty_tree": "Ağaç grafiği için veri yok.",
            "map_heading": "### Patent Teknoloji Haritası",
            "map_caption": "Koordinatlar çekilen başlıkların TF-IDF vektörlerinin PCA ile 2 boyuta indirgenmesidir; konum uydurulmaz.",
            "empty_map": "Harita için en az 2 patent ve scikit-learn gerekir.",
            "network": "### Assignee ↔ Alan Ağ Analizi",
            "empty_net": "Ağ grafiği için bağlantı verisi yok.",
            "list_heading": "### Çekilen 6G patent listesi",
            "list_caption": "Kartlar Lens data satırıdır, yıla göre yeniden eskiye. Aynı yayın no Lens.org’da açılır.",
            "assignee": "Applicant (başvuru sahibi)",
            "year": "Yıl",
            "open_record": "{pub} — Lens.org’da Aç ↗",
        },
        "pub": {
            "title": "Akademik Yayın Analizi",
            "subtitle": "WoS Core Collection + Springer Meta API. ISAC, RIS, NTN, AI-RAN, THz, Ambient IoT. Yıl / kurum / ülke / atıf: WoS. Kaynak: {source}",
            "what_title": "Bu sayfa neyi sayıyor?",
            "what_body": """<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.65;margin:8px 0 0 0;">
<strong>Akademik Yayın Analizi</strong> altı 6G konusunda yayını sayar:
ISAC, RIS, NTN, AI-RAN, THz, Ambient IoT.
<strong>Toplam adet:</strong> WoS Core Collection ile Springer Meta API yan yana. Hover’da ikisi de görünür. Tek birleşik külliyat yoktur (örtüşme düşülmedi).
<strong>Grafikler:</strong> yıllara göre yayın, en çok yayın yapan kurumlar, en çok yayın yapan ülkeler, en çok atıf alan makaleler, trend analizi.
</p>
<p style="color:#CBD5E1;font-size:0.88rem;line-height:1.6;margin:10px 0 0 0;">
Yıl / kurum / ülke / atıf: WoS Analyze Results (<code>TS=(6G) AND konu AND PY=2020-2026</code>).
WoS küresel Core Collection’dır. Springer konu çubuğu da küresel Meta API’dir. Altı konu ve iki kaynak toplanmaz.
</p>""",
            "expert_title": "API adı, filtre, sınır",
            "expert_body": """<p style="color:#E2E8F0;font-size:0.88rem;line-height:1.65;margin:8px 0 0 0;">
<strong>WoS Core Collection Analyze Results:</strong>
<code>TS</code> (Topic Search — konu araması) + <code>PY</code> (Publication Year — yayın yılı) 2020–2026.
Yıl = Publication Years; kurum = Affiliations; ülke = Countries/Regions (Results count).
Atıf = Times Cited, yüksekten düşüğe.
<strong>Springer Nature Meta API:</strong> konu toplamı; Basic planda bağlılık filtresi yok.
Anahtar yoksa hücre —. Sayı uydurulmaz.
</p>""",
            "access_title": "Anahtar nerede gerekir?",
            "access_body": """<p style="color:#E2E8F0;font-size:0.88rem;line-height:1.6;margin:8px 0 0 0;">
Bu sayfa <strong>WoS</strong> ve <strong>Springer</strong> kullanır.
</p>
<ul style="color:#CBD5E1;font-size:0.86rem;line-height:1.65;margin:8px 0 0 1.1rem;padding:0;">
<li><strong>Springer</strong> — bireysel e-posta yeterli.</li>
<li><strong>WoS (Clarivate)</strong> — kurumsal / kütüphane. Bireysel Gmail pratikte yetmez.</li>
</ul>""",
            "empty": "Yayın kaydı yok.",
            "empty_topic": "«{topic}» için ölçülen kayıt yok. Sayı uydurulmaz. Düğmeler aynı konuyu dış sitede arar.",
            "metric_doi": "Türkiye 6G (başlık)",
            "metric_ieee": "WoS",
            "metric_scholar": "Springer",
            "metric_springer": "Springer (TR)",
            "metric_elsevier": "Springer",
            "metric_wos": "WoS",
            "metric_wos_core": "WoS Core (konu)",
            "metric_tr": "Türkiye 6G başlık",
            "metric_top_cc": "WoS ilk 10 ülke",
            "metric_tr_springer": "Türkiye (Springer, 2022–2026)",
            "metric_tr_springer_cap": "Springer Meta metin «Turkey»; WoS Countries/Regions sırası değildir. Altı konu toplanmaz.",
            "metric_tr_wos_rank": "Türkiye WoS sırası",
            "metric_tr_wos_rank_n": "{n}.",
            "metric_tr_wos_out": "ilk 10’da yok",
            "metric_tr_wos_out_delta": "10. ülke {tenth} kayıt",
            "metric_tr_wos_all_delta": "İlk 10’da olan konu sayısı / 6 konu. Tam sıra uydurulmaz.",
            "cc_col_rank": "Sıra",
            "cc_col_country": "Ülke",
            "cc_col_count": "WoS kayıt",
            "cc_col_topic": "Konu",
            "cc_col_tr_rank": "Türkiye WoS sırası",
            "cc_col_tenth": "10. ülke",
            "cc_col_springer": "Springer TR 2022–2026",
            "cc_tr_rank_gt10": ">10",
            "cc_ellipsis": "…",
            "cc_tr_list_label": ">10. Türkiye",
            "cc_tr_not_measured": "ölçülmedi",
            "cc_rank_caption": "İlk 10 ülke, sonra …, sonra Türkiye sırası. Tam WoS sırası bu önbellekte yoksa >10 yazılır; 0 veya uydurma sıra basılmaz.",
            "cc_overview_caption": "Her konuda aynı düzen: ilk 10 → … → Türkiye sırası. Altı konu toplanmaz. Springer metin Turkey ≠ WoS CU sırası.",
            "tr_in_top10": "Türkiye bu konunun WoS ilk 10 ülkesinde var. Springer Meta «6G {topic} Turkey» 2022–2026: **{n}** (WoS sırası değildir).",
            "tr_not_top10": "WoS Analyze Results «{topic}»: Türkiye ilk 10 ülkede yok. 10. ülkenin kayıt sayısı **{tenth}**. Tam sıra bu platformda ölçülmedi (tam ülke listesi yok). Springer Meta «6G {topic} Turkey», 2022–2026: **{n}**. Metin Turkey ≠ WoS CU sırası; iki katman toplanmaz.",
            "tr_not_top10_all": "Türkiye WoS ilk 10 listesinde yok. Springer (2022–2026, metin Turkey): {springer}. Konular toplanmaz.",
            "metric_oa_year": "{year} (6 konu)",
            "metric_peak_year": "Türkiye — en çok makale yılı",
            "metric_peak_year_wos": "WoS — tepe yıl",
            "metric_peak_delta": "{n} makale",
            "metric_topic": "Konu",
            "metric_topic_delta": "{n} makale",
            "metric_cites": "Atıf (DOI kaydı)",
            "source_metric_caption": "Sayı o sitenin resmi API’sidir. Anahtar yoksa —.",
            "keys_help": "WoS / Springer sayımı resmi geliştirici anahtarı ister.",
            "key_ieee": "IEEE API ↗",
            "key_springer": "Springer API ↗",
            "key_elsevier": "Springer API ↗",
            "key_wos": "WoS (Clarivate) API ↗",
            "key_scholar": "Springer ↗",
            "scholar_metric_caption": "Anahtar yoksa hücre —; sayı uydurulmaz.",
            "open_oa": "WoS’u aç ↗",
            "snapshot": "Son başarılı önbellek: {ts}",
            "view": "Grafik",
            "region_label": "Bölge",
            "region": {
                "both": "Türkiye + Avrupa",
                "tr": "Türkiye",
                "eu": "Avrupa",
            },
            "section": {
                "year": "Yıllara göre yayın",
                "inst": "En çok yayın yapan kurumlar",
                "country": "En çok yayın yapan ülkeler",
                "cited": "En çok atıf alan makaleler",
                "trend": "Trend analizi",
                "tt_eu": "Türk Telekom yayın izi",
            },
            "year_heading": "### Yıllara göre yayın",
            "year_caption": "Başlığında 6G geçen dergi ve bildiri, 2020–2026. Türkiye: bağlılıkta Turkey. Avrupa çizgisi: Almanya, Fransa, İtalya, İspanya, Birleşik Krallık, Finlandiya, Yunanistan, Çekya (ayrı seri; toplanmaz).",
            "year_caption_wos": "WoS Core Collection, TS=(6G) AND konu. Yıl ekseni son 5 yıl: 2022–2026 (2026 eksik yıl). Tümü görünümünde altı seri ayrıdır; toplanmaz.",
            "inst_caption": "Türkiye 6G kayıtlarındaki bağlılık dizgesi (en sık 10). Avrupa kurum listesi bu önbellekte yok; ülke grafiğine bakın.",
            "inst_caption_wos": "Analyze Results → Affiliations, Results count (alfabetik değil). Seçili konu. Ortak yazarlı makale birden fazla kurumda sayılır; çubuklar toplanmaz.",
            "inst_caption_wos_all": "Tümü: her konu kendi WoS Analyze Results → Affiliations listesidir (önbellek). Altı konu toplanmaz (aynı makale birden fazla TS sorgusunda çıkar). Springer Meta Basic kurum facet vermez.",
            "cc_caption": "Bağlılık metninde ülke adı geçen, başlığında 6G olan kayıt. Ortak yazarlı makale birden fazla ülkede sayılır; çubuklar toplanmaz.",
            "cc_caption_wos": "Analyze Results → Countries/Regions, Results count, ilk 10 ülke (sıra 1–10; kim 1. olursa o). WoS «ENGLAND» burada Birleşik Krallık (İngiltere dilimi). Ortak yazarlı makale birden fazla ülkede sayılır; çubuklar toplanmaz. Ülke listesi PY=2020-2026 (yıllık ülke dilimi yok). Yıl/trend grafikleri son 5 yıl: 2022–2026. Konu: şartnamedeki altı 6G konusu.",
            "cc_caption_wos_all": "Her konuda: WoS ilk 10 ülke, sonra …, sonra Türkiye sırası. Altı konu toplanmaz. Tam sıra yoksa >10; Springer 2022–2026 metin Turkey ayrı durur.",
            "cited_heading": "### En çok atıf alan makaleler",
            "cited_caption": "Sıra: DOI kaydındaki is-referenced-by-count, yüksekten düşüğe. Kartlar canlı listedir.",
            "cited_caption_wos": "Sıra: WoS Times Cited (atıf sayısı), yüksekten düşüğe. Crossref is-referenced-by-count değildir. UT (Unique Identifier — benzersiz kayıt no) varsa tam kayıt açılır. Geniş 6G taramaları konu kelimesi geçtiği için üstte çıkabilir.",
            "trend_heading": "### Trend analizi",
            "trend_caption": "Türkiye ve seçilen Avrupa ülkelerinde başlık 6G, yıllara göre. Toplam Avrupa tek sayı değildir (çift sayım olmasın diye toplanmaz).",
            "trend_caption_wos": "Aynı WoS sorgusu, yıllara göre. Yıl ekseni son 5 yıl: 2022–2026. Konu serileri toplanmaz. 2026 yılı devam eden yıldır; önceki yıllarla kıyas tek başına olgunluk kanıtı değildir.",
            "empty_cited": "Atıf sıralı kayıt yok.",
            "volume_heading": "### 6G literatür hacmi",
            "volume_caption": "Başlığında 6G geçen dergi ve bildiri, Türkiye / Avrupa bağlılığı, 2020–2026.",
            "doi_heading": "### Yıl ve konu",
            "doi_caption": "DOI öneki. WoS atıf sırası Times Cited’dır.",
            "chart_year": "Yıllara göre yayın — başlık 6G",
            "chart_year_wos": "Yıllara göre yayın — WoS Core Collection",
            "chart_year_x": "Takvim yılı",
            "chart_topic": "Türkiye — başlık 6G AND konu",
            "chart_topic_wos": "WoS Core Collection — TS=(6G) AND konu",
            "chart_wos_springer": "Toplam yayın — WoS Core Collection vs Springer Meta API",
            "chart_trend_wos": "WoS Core Collection — yıllara göre konu serisi (toplanmaz)",
            "series_wos": "WoS Core Collection",
            "series_springer": "Springer Meta API",
            "hover_wos_springer": "%{{y}}<br>{wos}: <b>%{{customdata[0]}}</b> {unit}<br>{springer}: <b>%{{customdata[1]}}</b> {unit}<extra></extra>",
            "wos_springer_caption": "Hover’da her konu için WoS ve Springer ayrı yazılır. İki çubuk toplanıp «tek külliyat» yapılmaz: aynı makale her iki indekste de çıkabilir, örtüşme ölçülmedi. WoS: TS=(6G) AND konu AND PY=2020-2026. Springer: Meta API metin «6G {token}», 2020–2026, küresel. Üstteki Springer (TR) hücresi bu grafik değildir. Ambient IoT’de Springer serbest metin WoS tırnaklı sorgudan geniş kalır.",
            "chart_publisher": "DOI öneki (WoS / Springer)",
            "empty_year": "Yıl serisi yok (önbellek boş). Sayı uydurulmaz.",
            "oa_heading": "### 6G konularına göre yayın",
            "oa_caption": "Konu çubuğu Türkiye 6G + konu token. Avrupa ülke grafiği ayrı sekmededir.",
            "oa_empty": "Sayım yok; uydurulmaz.",
            "try_oa": "WoS’ta dene ↗",
            "open_oa_counts": "WoS’ta aç ↗",
            "scholar_heading": "### Trend + dış arama",
            "scholar_caption": "WoS / Springer düğmesi sorguyu yeni sekmede açar; sonuç sayısını buraya yazmayız.",
            "inst_heading": "### En çok yayın yapan kurumlar",
            "oa_groupby": "Bağlılık dizgesi, Türkiye 6G.",
            "chart_inst": "Kurumlara göre yayın (Türkiye, 6G)",
            "chart_inst_wos": "Kurumlara göre yayın — WoS Affiliations",
            "chart_inst_wos_all": "Kurumlara göre yayın — WoS Affiliations (konu ayrı, toplanmaz)",
            "open_inst": "Kurum aramasını aç ↗",
            "inst_fallback": "Türkiye bağlılık dizgesi.",
            "chart_inst_fb": "Kurumlar (makale adedi)",
            "empty_inst": "Kurum adı çıkmadı. Avrupa için ülke sekmesini kullanın.",
            "empty_inst_wos": "Kurum listesi Analyze Results önbelleğinde yok. Sayı uydurulmaz.",
            "cc_heading": "### En çok yayın yapan ülkeler",
            "chart_cc": "Ülkelere göre yayın — başlık 6G, bağlılık",
            "chart_cc_wos": "İlk 10 ülke — WoS Countries/Regions",
            "chart_cc_wos_all": "İlk 10 ülke — WoS Countries/Regions (konu ayrı, toplanmaz)",
            "open_cc": "Ülke aramasını aç ↗",
            "cc_fallback": "Bağlılıkta ülke adı.",
            "chart_cc_fb": "Ülke (makale adedi)",
            "empty_cc": "Ülke sayısı yok.",
            "empty_cc_wos": "Ülke listesi Analyze Results önbelleğinde yok. Sayı uydurulmaz.",
            "papers_heading": "### En çok atıf alan 6G makaleleri",
            "papers_caption": "Canlı DOI listesi; kilitli örnek seti değil. Atıf: DOI is-referenced-by-count.",
            "citations_n": "{n} atıf",
            "citations_na": "Atıf: —",
            "authors": "Yazarlar",
            "open_doi": "Makaleyi DOI ile Aç ↗",
            "cc": {
                "TR": "Türkiye",
                "DE": "Almanya",
                "FR": "Fransa",
                "IT": "İtalya",
                "ES": "İspanya",
                "GB": "Birleşik Krallık",
                "FI": "Finlandiya",
                "SE": "İsveç",
                "NL": "Hollanda",
                "BE": "Belçika",
                "AT": "Avusturya",
                "CH": "İsviçre",
                "NO": "Norveç",
                "DK": "Danimarka",
                "PL": "Polonya",
                "PT": "Portekiz",
                "GR": "Yunanistan",
                "IE": "İrlanda",
                "CZ": "Çekya",
                "HU": "Macaristan",
                "RO": "Romanya",
                "BG": "Bulgaristan",
                "HR": "Hırvatistan",
                "SK": "Slovakya",
                "SI": "Slovenya",
                "LT": "Litvanya",
                "LV": "Letonya",
                "EE": "Estonya",
                "LU": "Lüksemburg",
                "MT": "Malta",
                "CY": "Kıbrıs",
                "IS": "İzlanda",
                "CN": "Çin",
                "US": "ABD",
                "KR": "Güney Kore",
                "CA": "Kanada",
                "AU": "Avustralya",
                "SG": "Singapur",
                "IN": "Hindistan",
                "JP": "Japonya",
                "SA": "Suudi Arabistan",
                "EG": "Mısır",
            },
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
Google Patents’te bu platformun kilitlediği TT-grup 6G-komşu tesciller <strong>Netsia Inc.</strong> altındadır.
Netsia, Argela/Türk Telekom ABD Ar-Ge iştirakidir; hukuki assignee Netsia’dır.
<strong>EP yayın numarası bu örnekte 0’dır</strong> — gizlenmez, uydurulmaz.
Yayınlarda ham bağlılık «Türk Telekom, Ankara/İstanbul, Türkiye». Kurum grafı
bazı kaydı DE/MY/CZ şirketine yanlış düşürebilir; ülke çubuğu o hatayı TT Avrupa yayını diye okumaz.
</p>""",
            "metric_pat": "TT-grup doğrulanmış patent",
            "metric_ep": "Avrupa Patent Ofisi",
            "metric_us": "ABD Patent ve Marka Ofisi",
            "metric_tr": "Türkiye Patent ve Marka Kurumu",
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
            "map_caption": "Katmanlar ayrıdır: merkez, TTI (Türk Telekom International) toptan ilk giren pazar, 6G Ar-Ge (Araştırma ve Geliştirme) ortağı, ETSI (European Telecommunications Standards Institute — Avrupa Telekomünikasyon Standartları Enstitüsü) merkezi, MoU (Memorandum of Understanding — mutabakat zaptı) imza yeri. Abone/pazar payı değildir.",
            "map_fail": "Harita çizilemedi; aşağıdaki liste kaynakta adı geçen ülkelerin tam kümesidir.",
            "role_heading": "### Kanıt türü (kaç ülkede adı geçti)",
            "role_caption": "EP (European Patent — Avrupa patenti) tescil çubuğu 0’dır. Toptan 6 ülke TTI About «ilk giren pazar» listesidir; 19 veya 24’ün tamamı değildir.",
            "vs_heading": "### Bu platformun kilitli 6G örnek kümesi",
            "vs_caption": "Çubuklar bu platformun kilitli 6G örnek kaydıdır (Google Patents). Ericsson 5, Qualcomm 4, ZTE 4, Nokia 3, TT-grup (Netsia) 3, Huawei 2, Samsung 1. Küresel SEP, gelir veya Avrupa ofis payı değildir. Sıra kayıt adedine göredir.",
            "office_heading": "### Patent ofisi (doğrulanmış küme)",
            "office_caption": "Çubuklar kilitli Netsia tescilleridir (Google Patents). Anadolu Ajansı milli başvuru sıralaması (921, «Türkiye zirvede») bu grafik değildir ve bu bölümde açılmaz. Türkiye Patent ve Marka Kurumu bu örnekte 0 — ABD Patent ve Marka Ofisi’nde 3 tescil var, Avrupa Patent Ofisi’nde yok.",
            "office_lock_all": "Konu taraması: tüm konular. Avrupa Patent Ofisi {ep} · ABD Patent ve Marka Ofisi {us} · Türkiye Patent ve Marka Kurumu {tr}.",
            "office_lock_one": "Konu taraması kilitledi: «{topic}». Avrupa Patent Ofisi {ep} · ABD Patent ve Marka Ofisi {us} · Türkiye Patent ve Marka Kurumu {tr}.",
            "empty_topic": "Kilitli Netsia kümesinde «{topic}» tescili yok; üç ofis çubuğu 0’dır. Konu taramasındaki ofis düğmeleri aynı sorguyu dış sitede açar.",
            "pat_list_heading": "### Netsia Inc. (Türk Telekom grubu) — Google Patents",
            "pat_list_caption": "Hak sahibi (assignee): Netsia Inc. Kartlar yıla göre yeniden eskiye (2025 → 2023). Rakip (Nokia–ZTE) kümesine karıştırılmaz.",
            "named_heading": "### Kaynakta adı geçen ülkeler (eksiksiz liste)",
            "named_caption": "Haritada boyanan ülkelerin tam kümesi budur. 19 veya 24 ülke adı raporda yok; eklenmez.",
            "named_col_place": "Ülke",
            "named_col_layer": "Katman",
            "presence_heading": "### 6G dokunuşları — işbirliği / standart / proje",
            "presence_caption": "Kart resmi duyurudur. Eşit yükseklikli «ülke başına 1» çubuk pazar payı gibi okunduğu için çizilmez.",
            "oa_heading": "### Ülke grafını TT Avrupa’sı sanmayın",
            "oa_caption": "Üstteki «Ülkeler» sekmesi küresel 6G konu aramasıdır, TT portföyü değildir. Aşağıdaki makalelerin ham bağlılığı TR’dir.",
            "papers_heading": "### Türk Telekom Ar-Ge bağlılıklı makaleler",
            "papers_caption": "DOI kilitlidir. Sıra: yıl yeniden eskiye; aynı yılda atıf (cited_by_count) yüksekten düşüğe. WoS UT’si bilinen kayıtta tam kayıt düğmesi açılır.",
            "open_touch": "Kaynak duyuruyu aç ↗",
            "open_press": "Milli başvuru açıklamasını aç ↗",
            "open_ir": "2024 entegre raporu PDF ↗",
            "open_tti": "TTI About sayfasını aç ↗",
            "position_heading": "### Türk Telekom Avrupa’da nerededir? (bu platformun ölçümü)",
            "position_m_pub": "TR yayın sırası",
            "position_m_pub_help": "6G konu + 3 MNO ve TT; {n} kayıt",
            "position_m_pat": "TR patent sırası",
            "position_m_pat_help": "Kilitli ABD Patent ve Marka Ofisi örnek kümesi; {n} Netsia kaydı",
            "position_m_ep": "Avrupa Patent Ofisi tescili",
            "position_m_us": "ABD Patent ve Marka Ofisi (Netsia)",
            "position_m_out": "TR dışı TT yayın ülkesi",
            "position_m_pat_out": "TR dışı TT patent ülkesi",
            "position_body": """<div class="glass-card" style="border-left:6px solid #E20074;margin-bottom:12px;">
<p style="color:#F8FAFC;font-size:0.95rem;line-height:1.65;margin:0;">
<strong>Türkiye:</strong> 6G-bitişik yayında <em>{pub_rank}. sıra</em> ({pub_n} yayın kaydı; 3 MNO + TT).
Örnek Google Patents kaydında <em>{pat_rank}. sıra</em> ({pat_n} Netsia kaydı).
</p>
<p style="color:#F8FAFC;font-size:0.95rem;line-height:1.65;margin:8px 0 0 0;">
<strong>Avrupa geneli:</strong> Yayın veya EP patent lideri değildir.
TR dışı kilitli ülkede TT bağlılıklı yayın &gt;0 olan ülke sayısı: {pub_out}.
EP (Avrupa patenti) tescil bu kümede <strong>{ep}</strong>. Netsia Google Patents: {us} kayıt — yalnız TR satırında sayılır.
TR dışı örnek patent ülkesi: {pat_out}.
Ülkeler ayrı ligdir; tek bir «Avrupa kaçıncısı» sayısı üretilmez.
</p>
<p style="color:#C8D1DC;font-size:0.88rem;line-height:1.55;margin:8px 0 0 0;">
<strong>Aynı ülkelerin yayın 1.’leri (yüksekten düşüğe):</strong> {leaders}
</p>
<p style="color:#94A3B8;font-size:0.82rem;margin:8px 0 0 0;">
Bu abone/gelir payı veya EPO PATSTAT tam taraması değildir. 0 kayıt sıra almaz (—).
</p>
</div>""",
            "position_body_pat": """<div class="glass-card" style="border-left:6px solid #E20074;margin-bottom:12px;">
<p style="color:#F8FAFC;font-size:0.95rem;line-height:1.65;margin:0;">
<strong>Türkiye:</strong> kilitli Google Patents kümesinde <em>{pat_rank}. sıra</em> ({pat_n} Netsia kaydı; 3 MNO + TT).
<strong>Avrupa:</strong> EP tescil bu kümede <strong>{ep}</strong> — EP patent lideri değildir.
Netsia Google Patents {us} kayıt yalnız TR satırında sayılır. TR dışı örnek patent ülkesi: {pat_out}.
Ülkeler ayrı ligdir; tek bir Avrupa sıra sayısı üretilmez.
</p>
<p style="color:#94A3B8;font-size:0.82rem;margin:8px 0 0 0;">
Bu EPO PATSTAT taraması veya abone payı değildir. 0 kayıt sıra almaz (—). Yayın tabloları Akademik Yayın Analizi sayfasındadır.
</p>
</div>""",
            "position_body_pub": """<div class="glass-card" style="border-left:6px solid #E20074;margin-bottom:12px;">
<p style="color:#F8FAFC;font-size:0.95rem;line-height:1.65;margin:0;">
<strong>Türkiye:</strong> 6G-bitişik yayında <em>{pub_rank}. sıra</em> ({pub_n} kayıt; 3 MNO + TT).
<strong>Avrupa:</strong> yayın lideri değildir. TR dışı kilitli ülkede TT bağlılıklı yayın &gt;0 olan ülke: {pub_out}.
Ülkeler ayrı ligdir; tek bir Avrupa sıra sayısı üretilmez.
</p>
<p style="color:#C8D1DC;font-size:0.88rem;line-height:1.55;margin:8px 0 0 0;">
<strong>Aynı ülkelerin yayın 1.’leri (yüksekten düşüğe):</strong> {leaders}
</p>
<p style="color:#94A3B8;font-size:0.82rem;margin:8px 0 0 0;">
Bu abone/gelir payı değildir. 0 kayıt sıra almaz (—). Patent tabloları Patent Zekası sayfasındadır.
</p>
</div>""",
            "what_title_pub": "Yayın bağlılığı ülke sırasını nasıl kurar?",
            "what_body_pub": """<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.65;margin:8px 0 0 0;">
<strong>DOI / bağlılık</strong> kurum kimliği veya bağlılık dizesiyle 6G konu yayınlarını sayar.
Türk Telekom satırı TR dışı ülkede TR kurum ID’si ile şişirilmez; o ülkede DOI-kilitli bağlılık yoksa sayı 0’dır.
</p>
<p style="color:#CBD5E1;font-size:0.88rem;line-height:1.6;margin:10px 0 0 0;">
1./2./3. Wikipedia Avrupa MNO listesindeki üç işletmecinin kendi iç sıralamasıdır; abone payı değildir.
Patent ofisleri bu sayfada yoktur — Patent Zekası’ndadır.
</p>""",
            "overview_heading": "### Avrupa geneli — 3 operatör + Türk Telekom",
            "overview_heading_pat": "### Avrupa geneli — patent (kilitli örnek küme)",
            "overview_heading_pub": "### Avrupa geneli — yayın",
            "overview_caption": "Her ülkede Wikipedia MNO listesindeki 3 işletmeci, 6G konu aramasında kurum kimliği (veya bağlılık dizesi) ile sayıldı. 1./2./3. bu üç firmanın kendi iç sıralamasıdır; abone payı değildir. TT ayrı sütundadır. Ölçülmüş 0 (kurum bulundu, konu kaydı yok) 0’dır. Sorgulanamayan sayı — olarak kalır, uydurulmaz. Patent sütunu bu platformun kilitli örnek kümesidir (EPO PATSTAT taraması değil).",
            "overview_caption_pat": "Kilitli örnek kümede en az bir patenti olan ülkeler. 0’lık 2./3. operatör sütunu yok; yayın sütunu bu sayfada yok. Netsia Google Patents yalnız TR. 0 kayıt sıra almaz (—).",
            "overview_caption_pub": "Her ülkede Wikipedia MNO listesindeki 3 işletmeci, 6G konu aramasında kurum kimliği (veya bağlılık dizesi) ile sayıldı. 1./2./3. bu üç firmanın kendi iç sıralamasıdır; abone payı değildir. TT ayrı sütundadır. Ölçülmüş 0, 0’dır. Sorgulanamayan sayı — olarak kalır.",
            "overview_spin": "Operatör yayın sayıları yükleniyor (önbellek varsa beklenmez)",
            "overview_spin_pat": "Kilitli patent örnek kümesi yükleniyor",
            "overview_empty_pat": "Kilitli örnek kümede Avrupa satırında patent yok. Sayı uydurulmaz.",
            "overview_hits_pat": "Kayıtlı firma (örnek küme)",
            "overview_pub_title": "Ülkede yayın 1. operatör (>0)",
            "overview_pat_title": "Ülkede patent 1. (kilitli örnek, >0)",
            "overview_vs_title": "Yayın: ülkede 1. operatör vs Türk Telekom",
            "overview_vs_title_pat": "Patent: ülkede 1. (örnek) vs Türk Telekom",
            "overview_pub_lead_short": "1. operatör",
            "overview_pat_lead_short": "1. (örnek)",
            "overview_tt_pub": "TT yayın",
            "overview_tt_pat": "TT patent (örnek)",
            "overview_pub_lead": "Yayında 1. (adet)",
            "overview_pat_lead": "Patentte 1. (adet)",
            "overview_pub_1": "Yayın 1.",
            "overview_pub_2": "Yayın 2.",
            "overview_pub_3": "Yayın 3.",
            "overview_pat_1": "Patent 1. (örnek)",
            "overview_pat_2": "Patent 2. (örnek)",
            "overview_pat_3": "Patent 3. (örnek)",
            "rank_heading": "### Ülke detayı: 3 MNO (Mobile Network Operator — mobil şebeke işletmecisi) + Türk Telekom",
            "rank_heading_pat": "### Ülke detayı — patent (3 MNO + Türk Telekom)",
            "rank_heading_pub": "### Ülke detayı — yayın (3 MNO + Türk Telekom)",
            "rank_caption": "Üç operatör Wikipedia Avrupa MNO listesindeki bu ülke satırından kilitlendi; abone/gelir «en yüksek 3» bu platformda ölçülmedi. Yayın = 6G konu + kurum ID (yoksa bağlılık dizesi). Patent = Google Patents (Netsia yalnız TR). 0 kayıt sıra almaz (—). Küresel SEP veya pazar payı değildir.",
            "rank_caption_pat": "Bu ülkede Wikipedia’daki 3 MNO + TT. Patent = Google Patents (Netsia yalnız TR). Operatör yayın API’si yok. 0 kayıt sıra almaz (—). Kartlarda Google Patents açılır.",
            "rank_caption_pub": "Üç operatör Wikipedia Avrupa MNO listesinden kilitlendi. Yayın = 6G konu + kurum ID. 0 kayıt sıra almaz (—). Patent ofis sütunu bu sayfada yok.",
            "rank_country": "Avrupa ülkesi",
            "rank_spin": "Ülke sıralaması yükleniyor",
            "rank_col_firm": "Firma",
            "rank_pub_title": "Yayın sırası (bu ülke)",
            "rank_pat_title": "Patent sırası (kilitli örnek küme)",
            "rank_pub_x": "Yayın sayısı",
            "rank_pat_x": "Örnek küme patent kaydı",
            "rank_tt": "Türk Telekom bu ülkede: yayın {pub}. sıra ({pub_n} yayın kaydı) · patent {pat}. sıra ({pat_n} örnek kayıt) — {n} firma",
            "rank_tt_pat": "Türk Telekom bu ülkede: patent {pat}. sıra ({pat_n} örnek kayıt) — {n} firma",
            "rank_tt_pub": "Türk Telekom bu ülkede: yayın {pub}. sıra ({pub_n} yayın kaydı) — {n} firma",
            "rank_oa_fail": "Bu ülke için yayın yanıtı gelmedi; yayın çubuğu çizilmez.",
            "rank_col_rank_pub": "Yayın sırası",
            "rank_col_pub": "Yayın",
            "rank_col_rank_pat": "Patent sırası",
            "rank_col_pat": "Patent (örnek)",
            "rank_open_oa": "WoS’ta bu ülke 6G aramasını aç ↗",
            "rank_open_wiki": "Avrupa MNO listesini aç ↗",
            "rank_open_gp": "Google Patents hak sahibi (assignee) ↗",
            "layer": {
                "hq": "Merkez / operatör Ar-Ge (Araştırma ve Geliştirme)",
                "wholesale": "TTI (Türk Telekom International) toptan — ilk giren pazar (first-mover)",
                "rd_collab": "6G Ar-Ge (Araştırma ve Geliştirme) ortaklığı",
                "standards": "Standart organı: ETSI (European Telecommunications Standards Institute — Avrupa Telekomünikasyon Standartları Enstitüsü)",
                "mou_venue": "MoU (Memorandum of Understanding — mutabakat zaptı) imza yeri",
                "ep_grant": "EPO (European Patent Office — Avrupa Patent Ofisi) EP tescil",
            },
            "map_col_layer": "Katman",
            "map_col_note": "Açıklama",
        },
        "ui": {
            "source": "Kaynakta Aç ↗",
            "no_source": "Kaynak bağlantısı yok.",
        },
        "sources": {
            "patent_heading": "### Patent kaynağı",
            "patent_caption": "Bu sayfa Lens.org patent API’sini kullanır. Kart ve grafikler JSON kaydıdır. Aynı yayın no Lens.org’da açılır.",
            "pub_heading": "### Yayın kaynağı",
            "pub_caption": "Bu sayfa WoS Core Collection ve Springer kullanır. Kartta DOI + (varsa) Springer + WoS tam kayıt açılır.",
            "patent_metric": "Lens.org",
            "assignee_caption": "«{company}» başvuru sahibi (applicant) araması — sonuç sayısını buraya yazmayız; sitede doğrulayın.",
            "topic_search": "Konu taraması (şartname: ISAC, RIS, NTN, AI-RAN, THz, Ambient IoT)",
            "topic_all": "Tümü",
            "topic_all_caption": "Kartlar ve grafikler Lens.org kaydıdır. Konu seçince sorgu o alana iner.",
            "topic_all_caption_pub": "Kartlar kilitli DOI setinin tamamıdır. Bir konu seçince bu sayfadaki sayılar o alana iner.",
            "topic_caption": "Sorgu: «{q}». Bağlantı arama sayfasını açar.",
            "topic_result_caption": "Bu sayfadaki kartlar ve çubuklar kilitli kümede «{topic}» kayıtlarıdır. Ofis butonları aynı sorguyu («{q}») sitede açar.",
            "topic_result_caption_pub": "Bu sayfadaki kartlar kilitli DOI setinde «{topic}» kayıtlarıdır. Yayın butonları aynı sorguyu («{q}») sitede açar.",
            "open_google_patents": "Lens.org ↗",
            "open_lens": "Lens.org ↗",
            "open_espacenet": "Lens.org ↗",
            "open_wipo": "Lens.org ↗",
            "open_uspto": "Lens.org ↗",
            "open_ieee": "WoS ↗",
            "open_scholar": "Springer ↗",
            "open_springer": "Springer ↗",
            "open_elsevier": "Springer ↗",
            "open_wos": "WoS ↗",
            "open_doi": "DOI ↗",
            "open_crossref": "Crossref ↗",
            "mix_heading": "### Mix tarama (şartname siteleri)",
            "mix_caption": "Aynı 6G konusu: yayın (WoS, Springer) + patent (Lens.org).",
            "mix_pub_row": "Yayın taraması",
            "mix_pat_row": "Patent taraması (Lens.org)",
            "topic_pat_heading": "### Konu taraması — bu sayfa + Lens.org",
            "topic_pat_caption": "Açılır kutu sorguyu kilitler. Kartlar ve altı grafik Lens.org kaydıdır. Düğme aynı sorguyu Lens.org’da açar.",
            "topic_pub_heading": "### Konu taraması — bu sayfa + WoS / Springer",
            "topic_pub_caption": "Açılır kutu ISAC–Ambient IoT konusunu kilitler. Grafikler WoS Core Collection (küresel). Düğmeler WoS ve Springer aramasını yeni sekmede açar.",
            "topic_buttons_hint": "Bu düğmeler dış aramadır (yeni sekme). Sayfa içi sayılar yalnızca üstteki açılır kutudan değişir.",
            "topic_buttons_hint_pub": "Bu düğmeler dış aramadır (yeni sekme). Sayfa içi makale sayıları yalnızca üstteki açılır kutudan değişir.",
            "topic_live_all": "Lens.org (yedi 6G konusu): **{n}**. Çekilen kayıt: **{pulled}**. Toplanmaz. Ham «6G» değildir.",
            "topic_live_one": "Lens.org «{topic}» (`{q}`): **{n}**. Çekilen kayıt: **{pulled}**. Toplanmaz.",
            "topic_live_all_pub": "WoS Core Collection: TS=(6G) AND konu, PY=2020-2026. Altı konu çubuğu ayrıdır; toplanmaz. Türkiye başlık-6G önbelleği: **{n}** (küresel WoS değildir).",
            "topic_live_one_pub": "WoS Core Collection «{topic}»: **{n}** kayıt. Sorgu: `{q}`. Türkiye başlık-6G: {tr} (Crossref önbelleği; WoS küresel sayım değildir).",
            "totals_caption_pat": "Aynı sorgu, Lens.org patent/search. Yanıt yoksa —. Toplam, çekilen kayıtlarla toplanmaz.",
            "totals_caption_pub": "WoS ve Springer: o sitenin API’si (anahtar varsa). Anahtar yoksa —.",
            "total_col_db": "Veritabanı",
            "total_col_n": "Toplam",
            "total_col_how": "Nasıl sayıldı",
            "total_col_open": "Aramayı aç",
            "total_open_text": "Aç",
            "method_gp": "Google Patents xhr (bu sayfada kullanılmıyor)",
            "method_none": "Herkese açık JSON sayım API’si yok",
            "method_need_key": "Bireysel API anahtarı yok (hücre —)",
            "method_api_empty": "Anahtar var; ofis toplam vermedi — uydurulmaz",
            "method_native_lens": "Lens.org patent/search (aynı sorgu)",
            "method_native_espacenet": "EPO OPS (bu sayfada kullanılmıyor)",
            "method_native_uspto": "PatentsView (bu sayfada kullanılmıyor)",
            "method_native_ieee": "WoS Core Collection",
            "method_native_springer": "Springer Meta API: metin 6G, 2020–2026",
            "method_native_elsevier": "Springer Meta API",
            "method_native_wos": "Clarivate WoS Starter API / Analyze Results",
            "method_native_scholar": "WoS Core Collection",
            "method_crossref_ieee": "Crossref query.title=6G + önek 10.1109",
            "method_crossref_springer": "Crossref query.title=6G + önek 10.1007",
            "method_crossref_elsevier": "Crossref query.title=6G + önek 10.1016",
            "method_crossref_title": "Crossref query.title=6G, dergi, 2020–2026",
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
            "fallback_none": "### 6G Asistan (veri tabanlı mod)\n\nSorunuz platform veri kümesinde eşleşmedi. 6G Teknoloji Rehberi, Patent Zekası veya Akademik Yayın Analizi sayfalarındaki doğrulanmış kaynakları inceleyin.",
            "related": "**İlgili doğrulanmış kayıtlar:**",
            "tfidf_note": "*Yanıt TF-IDF ile seçilen platform kayıtlarındandır; sayı uydurulmaz.*",
            "llm_fail": "*LLM yanıtı alınamadı: {exc}*",
            "glossary_title": "Teknik sözlük (ilk kullanım açılımı)",
            "cite_n": "{n} atıf",
            "cite_na": "atıf sayısı kaynaktan alınamadı",
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
- **6G Teknoloji Rehberi** — tanım, çalışma prensibi, blok diyagram, mimari, kullanım, avantaj/dezavantaj, dünya çalışmaları, TT senaryoları, TRL
- **Patent Zekası** — Nokia–Intel (9 firma); yedi 6G konusu; Lens.org; grafik: firma, yıl, konu, radar, bulut, ağaç, yoğunluk, harita
- **Akademik Yayın Analizi** — WoS Core Collection + Springer; yıl / kurum / ülke / atıf / trend
            """,
            "mod_right": """
- **Türk Telekom Görünümü** — saha senaryo çözümleyici
- **AI Asistanı** — TF-IDF yerel geri getirme; isteğe bağlı Groq / Gemini
- **Hakkında** — bu sayfa (teslim / 15 dk sunum iskeleti)
            """,
            "stack": "#### Kullanılan teknolojiler",
            "stack_body": "Python, Streamlit, Pandas, Plotly, Matplotlib, NetworkX, WordCloud, scikit-learn. Opsiyonel: Groq API, Google Gemini API. Patent: Lens.org. Yayın: WoS, Springer.",
            "standard": "#### Anlatım standardı",
            "standard_body": "Teknik içerik iki kademelidir: **Temel** (nedir / neden / nasıl / ne zaman) ve **Uzman** (denklem, varsayım, 3GPP). Uzman mod temel katmanı atlamaz. Kısaltmalar ilk geçişte açılır. Patent özeti, DOI ve sayı uydurulmaz.",
            "talk": "#### 15 dakikalık sunum iskeleti",
            "talk_body": """
1. Amaç ve kapsam (1 dk)
2. Ana Sayfa TRL radar (2 dk)
3. Bir teknoloji (ör. RIS) — prensip + diyagram + TT senaryosu (3 dk)
4. Patent Zekası — firma filtresi, yıl grafiği, TT Avrupa izi (3 dk)
5. Akademik Yayın Analizi — WoS / Springer + TT bağlılıklı DOI (3 dk)
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
            "patent_year": "Yıllara göre 6G patent kayıt sayısı (çekilen Lens satırları)",
            "patent_count": "Patent kayıt sayısı",
            "domain_radar": "Firma × 6G konu — çekilen kayıt sayısı",
            "topic_mix": "Patent konusu dağılımı (çekilen kayıt)",
            "topic_axis": "Konu",
            "keywords": "Patent başlıklarında en sık geçen kelimeler",
            "kw_x": "Başlıkta geçme sayısı",
            "academic_trend": "Başlık 6G — yıllara göre makale adedi (Türkiye / Avrupa)",
            "pub_count": "Makale sayısı",
            "db_default": "Doğrulanmış örnek set — yayıncı sayısı",
            "publisher": "Yayıncı",
            "paper_count": "Makale sayısı",
            "hover_v": "%{{x}}<br><b>%{{y}}</b> {unit}<extra></extra>",
            "hover_h": "%{{y}}<br><b>%{{x}}</b> {unit}<extra></extra>",
            "network": "Assignee ↔ teknoloji alanı ağ grafiği",
            "nx_missing": "NetworkX yüklü değil; ağ grafiği gösterilemiyor.",
            "company_counts": "En çok çalışan firmalar (Lens.org total)",
            "company": "Firma",
            "density": "Patent yoğunluğu (firma × alan, kayıt sayısı)",
            "sunburst": "Patent ağacı (firma → konu, Lens total)",
            "tfidf": "Patent teknoloji haritası (TF-IDF + PCA, başlık vektörleri)",
            "oa_bar_x": "Makale sayısı",
            "tt_office": "TT-grup — hangi patent ofisinde tescil var (kilitli küme)",
            "tt_office_x": "Patent ofisi",
            "office_epo": "Avrupa Patent Ofisi",
            "office_uspto": "ABD Patent ve Marka Ofisi",
            "office_turkpatent": "Türkiye Patent ve Marka Kurumu",
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
            "subtitle": "6G Technology Explorer · Patent Intelligence · Academic Publication Analysis",
            "footer": "© 2026 Türk Telekom R&D",
            "ai_provider": "AI provider: {provider}",
            "ai_logout": "End AI session",
            "provider_off": "off",
        },
        "nav": {
            "home": "Home",
            "tech": "6G Technology Explorer",
            "patent": "Patent Intelligence",
            "publications": "Academic Publication Analysis",
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
Equations, assumptions and validity windows sit in the expert layer of <strong>6G Technology Explorer</strong>.
</p>
</div>""",
            "cards_heading": "Seven Building Blocks",
            "cards_caption": "Each card states the field problem first, then the method. For the step-by-step walkthrough, equations, and the Türk Telekom scenario, open 6G Technology Explorer in the sidebar.",
            "card_cta": "Step-by-step walkthrough: 6G Technology Explorer → select this card",
            "cards_heading_expert": "Seven Building Blocks",
            "cards_caption_expert": "Each card states the problem plus the technical counterpart. For Shannon/CRB, 3GPP and the validity window, open 6G Technology Explorer.",
            "card_cta_expert": "Equations and 3GPP context: 6G Technology Explorer → select this card",
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
            "badge": "6G TECHNOLOGY EXPLORER",
            "section_label": "Technology section",
            "section": {
                "definition": "1. Definition",
                "principle": "2. Operating principle and block diagram",
                "architecture": "3. System architecture",
                "use_cases": "4. Use cases",
                "adv_dis": "5. Advantages and disadvantages",
                "global_tt": "6. Global work and TT scenarios",
                "performance": "7. Performance charts and reference papers",
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
            "perf_caption": "There is no representative 5G/6G target bar. The charts below are this technology’s verified patent-record count and, when available, the Crossref 6G-title publication trend.",
            "empty_patents": "No verified patent records for “{domain}”.",
            "pub_fail": "No publication-year series for this topic; the chart is hidden.",
            "cell_free_pub": "Cell-free MIMO is not on the specification’s academic topic list; no topic series is shown.",
            "refs": "### Reference Papers & Publications",
            "refs_caption": "Links go to a DOI or an official 3GPP / project page.",
        },
        "patent": {
            "title": "Patent Intelligence",
            "subtitle": "Nokia, Ericsson, Huawei, Samsung, Qualcomm, ZTE, NEC, NICT, Intel — seven 6G topics (ISAC, RIS, Cell-Free, THz, AI-RAN, NTN, Ambient IoT). Source: {source}",
            "filter": "Company (Nokia, Ericsson, Huawei, Samsung, Qualcomm, ZTE, NEC, NICT, Intel):",
            "all": "All",
            "what_title": "What this page is for",
            "what_body": """<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.65;margin:8px 0 0 0;">
<strong>Patent Intelligence</strong> pulls rival filings from the <strong>6G Technology Explorer</strong> seven:
<strong>ISAC</strong> (Integrated Sensing and Communication),
<strong>RIS</strong> (Reconfigurable Intelligent Surfaces),
<strong>Cell-Free Massive MIMO</strong>,
<strong>THz</strong> (terahertz communication),
<strong>AI-Native RAN</strong> (radio access network),
<strong>NTN</strong> (Non-Terrestrial Networks),
<strong>Ambient IoT</strong>.
</p>
<p style="color:#CBD5E1;font-size:0.88rem;line-height:1.6;margin:10px 0 0 0;">
Nine applicants: Nokia, Ericsson, Huawei, Samsung, Qualcomm, ZTE, NEC, NICT (National Institute of Information and Communications Technology, Japan), Intel.
Firm bars are Lens <code>total</code> for these seven topics — not a raw «6G» keyword (handset noise is excluded).
The other charts are pulled rows (title + publication number + year). The two layers are not summed. No percents.
</p>
<p style="color:#94A3B8;font-size:0.84rem;margin:10px 0 0 0;">
A record appears only if it matched one of the seven queries; the label is that query’s topic. <strong>There is no Unclassified</strong> — unmatched rows are dropped, not invented.
The <strong>applicant</strong> is who filed, not a fielded product. One patent is not market leadership. Year is publication year.
</p>""",
            "access_title": "Where the data comes from",
            "access_body": """<p style="color:#E2E8F0;font-size:0.88rem;line-height:1.6;margin:8px 0 0 0;">
This page uses the <strong>Lens.org</strong> patent API only (<code>POST /patent/search</code>).
A website login is not enough; you need an Access Token from your profile (<code>LENS_TOKEN</code> or the box on this page).
Totals: JSON <code>total</code>. Cards and the other charts are <code>data</code> rows.
HTML is not scraped. No answer → —.
</p>""",
            "expert_title": "Pulled rows and limit",
            "expert_body": """<p style="color:#E2E8F0;font-size:0.88rem;line-height:1.65;margin:8px 0 0 0;">
Firm bars: OR of the seven topic DSLs × <code>applicant.name</code> (Lens <code>total</code>).
Pulled rows: up to 100 per topic, nine-firm OR. If a publication hits two topics, the first in list order is kept (ISAC → … → Ambient IoT).
Radar / density / tree axes are record counts, not percents. Titles are not rewritten.
On 429 the client waits <code>x-rate-limit-retry-after-seconds</code>.
</p>""",
            "key_gp": "Lens.org ↗",
            "key_lens": "Lens.org — API & Data (token) ↗",
            "key_espacenet": "Lens.org ↗",
            "key_wipo": "Lens.org ↗",
            "key_uspto": "Lens.org ↗",
            "token_label": "Lens Access Token",
            "token_missing": "Do not open api.lens.org/patent/search in a browser; 401 (Missing Authorization) is expected. The token is created in your Lens account: API & Data → plan approval → Create Token. Paste it here or as LENS_TOKEN= in .env. Do not paste the token in chat.",
            "token_help": "For the internship pick Trial / Academic. After the approval email, create an Access Token. HTML is not scraped; reload the app.",
            "api_error": "Lens API did not respond ({detail}). Counts are not invented.",
            "live_gp_heading": "### Lens.org — applicant (not the sample)",
            "live_gp_spin": "Asking Lens.org for integer totals in the background (first load can be long; then cached)",
            "bg_wait": "Totals are filling in the background ({done}/{total}). You can leave this page for Publications; the menu is not locked.",
            "bg_partial": "Charts use integer totals as they arrive. Empty cells stay empty; counts are not invented.",
            "live_gp_caption": "Same topic query + applicant.name. No answer → —. These numbers are not summed with locked sample bars.",
            "live_gp_metric": "Lens.org (applicant)",
            "live_gp_empty": "Lens did not return a total for this query; the count is not invented.",
            "live_col_firm": "Firm",
            "live_col_n": "API total",
            "live_col_sample": "Locked sample",
            "empty_company": "Lens.org returned no rows for “{company}”. Counts are not invented.",
            "empty_topic": "Lens returned no rows for this topic. Counts are not invented. Office buttons open the same query on the site.",
            "metric_total": "Pulled records",
            "metric_pulled": "Pulled records",
            "pulled_caption": "Cards and the word cloud are pulled rows. Firm / year / topic / radar / tree / density bars are Lens totals (integers, no 100 cap). The two layers are not summed.",
            "metric_leader": "Most records (applicant)",
            "metric_leader_delta": "{n} patents",
            "metric_domain": "Leading technology domain",
            "metric_domain_delta": "{n} records",
            "metric_source": "Source",
            "open_gp": "Open Lens.org patent search ↗",
            "view": "Section",
            "section": {
                "charts": "Rival patent charts",
                "tt_eu": "Türk Telekom patent footprint",
            },
            "year_heading": "### Patent count / year",
            "year_caption": "Lens year_published totals, firm × year. No rounding. 2026 is an incomplete year.",
            "empty_trend": "Not enough patent data for a trend chart.",
            "companies_heading": "### Firms with the most filings",
            "companies_caption": "Lens.org total: seven 6G topics (OR) + applicant. Not raw «6G». 0 = none for this query; the bar stays, the count is not invented.",
            "topic_mix_heading": "### Patent topic mix",
            "topic_mix_caption": "Lens total: seven topics × nine applicants (OR). No 100 cap and no rounding. No Unclassified.",
            "radar_heading": "### Radar chart",
            "radar_caption": "Firm × topic Lens totals. The axis is not a percent; there is no 100 cap.",
            "empty_counts": "No data for a company count.",
            "empty_domain": "Domain mix could not be computed.",
            "empty_kw": "No data for keyword analysis.",
            "wordcloud": "### Word cloud",
            "wordcloud_caption": "Word frequency in pulled patent titles (integers).",
            "empty_wc": "Word cloud needs wordcloud/matplotlib, or there are no tokens.",
            "density": "### Patent density chart",
            "density_caption": "Each cell is a Lens total (integer). The colour scale is the same integer.",
            "empty_density": "No data for a density heatmap.",
            "tree_heading": "### Patent tree",
            "tree_caption": "Treemap: outer box = firm, inner box = 6G topic. Area = Lens total. Names do not repeat; no publication numbers.",
            "empty_tree": "No data for a tree chart.",
            "map_heading": "### Patent technology map",
            "map_caption": "Coordinates are TF-IDF vectors of pulled titles reduced to 2-D with PCA; positions are not invented.",
            "empty_map": "The map needs at least two patents and scikit-learn.",
            "network": "### Assignee ↔ domain network",
            "empty_net": "No edge data for a network graph.",
            "list_heading": "### Pulled 6G patent list",
            "list_caption": "Cards are Lens data rows, newest year first. The same publication number opens on Lens.org.",
            "assignee": "Applicant (rights holder)",
            "year": "Year",
            "open_record": "{pub} — open on Lens.org ↗",
        },
        "pub": {
            "title": "Academic Publication Analysis",
            "subtitle": "WoS Core Collection + Springer Meta API. ISAC, RIS, NTN, AI-RAN, THz, Ambient IoT. Year / institution / country / cited: WoS. Source: {source}",
            "what_title": "What this page counts",
            "what_body": """<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.65;margin:8px 0 0 0;">
<strong>Academic Publication Analysis</strong> counts papers on six 6G topics:
ISAC, RIS, NTN, AI-RAN, THz, Ambient IoT.
<strong>Totals:</strong> WoS Core Collection beside Springer Meta API. Hover shows both. There is no single unique corpus (overlap was not subtracted).
<strong>Charts:</strong> publications by year, top institutions, top countries, most-cited papers, trend analysis.
</p>
<p style="color:#CBD5E1;font-size:0.88rem;line-height:1.6;margin:10px 0 0 0;">
Year / institution / country / cited: WoS Analyze Results (<code>TS=(6G) AND topic AND PY=2020-2026</code>).
WoS is global Core Collection. Springer topic bars are also global Meta API. The six topics and the two sources are not summed.
</p>""",
            "expert_title": "API name, filter, limit",
            "expert_body": """<p style="color:#E2E8F0;font-size:0.88rem;line-height:1.65;margin:8px 0 0 0;">
<strong>WoS Core Collection Analyze Results:</strong>
<code>TS</code> (Topic Search) + <code>PY</code> (Publication Year) 2020–2026.
Year = Publication Years; institution = Affiliations; country = Countries/Regions (Results count).
Citations = Times Cited, high to low.
<strong>Springer Nature Meta API:</strong> topic totals; the Basic plan has no affiliation filter.
No key → —. Counts are not invented.
</p>""",
            "access_title": "Where a key is needed",
            "access_body": """<p style="color:#E2E8F0;font-size:0.88rem;line-height:1.6;margin:8px 0 0 0;">
This page uses <strong>WoS</strong> and <strong>Springer</strong>.
</p>
<ul style="color:#CBD5E1;font-size:0.86rem;line-height:1.65;margin:8px 0 0 1.1rem;padding:0;">
<li><strong>Springer</strong> — personal email is enough.</li>
<li><strong>WoS (Clarivate)</strong> — institutional / library. A personal Gmail almost never works.</li>
</ul>""",
            "empty": "No publication records.",
            "empty_topic": "No measured records for “{topic}”. Counts are not invented. The buttons search the same topic on the external site.",
            "metric_doi": "Türkiye 6G (title)",
            "metric_ieee": "WoS",
            "metric_scholar": "Springer",
            "metric_springer": "Springer (TR)",
            "metric_elsevier": "Springer",
            "metric_wos": "WoS",
            "metric_wos_core": "WoS Core (topic)",
            "metric_tr": "Türkiye 6G-in-title",
            "metric_top_cc": "WoS top 10 countries",
            "metric_tr_springer": "Türkiye (Springer, 2022–2026)",
            "metric_tr_springer_cap": "Springer Meta text “Turkey”; not a WoS Countries/Regions rank. The six topics are not summed.",
            "metric_tr_wos_rank": "Türkiye WoS rank",
            "metric_tr_wos_rank_n": "{n}.",
            "metric_tr_wos_out": "not in top 10",
            "metric_tr_wos_out_delta": "10th country {tenth} records",
            "metric_tr_wos_all_delta": "Topics where Türkiye is in the top 10 / 6 topics. Exact rank is not invented.",
            "cc_col_rank": "Rank",
            "cc_col_country": "Country",
            "cc_col_count": "WoS records",
            "cc_col_topic": "Topic",
            "cc_col_tr_rank": "Türkiye WoS rank",
            "cc_col_tenth": "10th country",
            "cc_col_springer": "Springer TR 2022–2026",
            "cc_tr_rank_gt10": ">10",
            "cc_ellipsis": "…",
            "cc_tr_list_label": ">10. Türkiye",
            "cc_tr_not_measured": "not measured",
            "cc_rank_caption": "Top 10 countries, then …, then Türkiye’s rank. If the exact WoS rank is not in this cache, the label is >10; a fake rank or a 0 bar is not drawn.",
            "cc_overview_caption": "Same layout on every topic: top 10 → … → Türkiye’s rank. The six topics are not summed. Springer text-Turkey ≠ WoS CU rank.",
            "tr_in_top10": "Türkiye is in this topic’s WoS top 10. Springer Meta “6G {topic} Turkey” 2022–2026: **{n}** (not a WoS rank).",
            "tr_not_top10": "WoS Analyze Results “{topic}”: Türkiye is not in the top 10 countries. The 10th country has **{tenth}** records. The exact rank was not measured here (no full country list). Springer Meta “6G {topic} Turkey”, 2022–2026: **{n}**. Text Turkey ≠ WoS CU rank; the two layers are not summed.",
            "tr_not_top10_all": "Türkiye is not in the WoS top 10. Springer (2022–2026, text Turkey): {springer}. Topics are not summed.",
            "metric_oa_year": "{year} (6 topics)",
            "metric_peak_year": "Türkiye — peak year",
            "metric_peak_year_wos": "WoS — peak year",
            "metric_peak_delta": "{n} papers",
            "metric_topic": "Topic",
            "metric_topic_delta": "{n} papers",
            "metric_cites": "Citations (DOI record)",
            "source_metric_caption": "Counts come from that site’s official API. No key → —.",
            "keys_help": "WoS / Springer counts need an official developer key.",
            "key_ieee": "IEEE API ↗",
            "key_springer": "Springer API ↗",
            "key_elsevier": "Springer API ↗",
            "key_wos": "WoS (Clarivate) API ↗",
            "key_scholar": "Springer ↗",
            "scholar_metric_caption": "No key → —; counts are not invented.",
            "open_oa": "Open WoS ↗",
            "snapshot": "Last successful cache: {ts}",
            "view": "Chart",
            "region_label": "Region",
            "region": {
                "both": "Türkiye + Europe",
                "tr": "Türkiye",
                "eu": "Europe",
            },
            "section": {
                "year": "Publications by year",
                "inst": "Top publishing institutions",
                "country": "Top publishing countries",
                "cited": "Most cited papers",
                "trend": "Trend analysis",
                "tt_eu": "Türk Telekom publication footprint",
            },
            "year_heading": "### Publications by year",
            "year_caption": "Journal and proceedings with 6G in the title, 2020–2026. Türkiye: affiliation contains Turkey. Europe lines: Germany, France, Italy, Spain, United Kingdom, Finland, Greece, Czechia (separate series; not summed).",
            "year_caption_wos": "WoS Core Collection, TS=(6G) AND topic. Year axis is the last 5 years: 2022–2026 (2026 is incomplete). In the all-topics view the six series are separate and not summed.",
            "inst_caption": "Affiliation strings on Türkiye 6G records (top 10). A Europe institution list is not in this cache; use the country chart.",
            "inst_caption_wos": "Analyze Results → Affiliations, Results count (not alphabetical). Selected topic. A co-authored paper can count at more than one institution; bars are not summed.",
            "inst_caption_wos_all": "All topics: each topic is its own WoS Analyze Results → Affiliations list (cache). The six topics are not summed (the same paper can match more than one TS query). Springer Meta Basic has no institution facet.",
            "cc_caption": "Records with 6G in the title whose affiliation string contains the country name. A co-authored paper can count in more than one country; bars are not summed.",
            "cc_caption_wos": "Analyze Results → Countries/Regions, Results count, top 10 countries (ranks 1–10; whoever is first). WoS “ENGLAND” is shown here as United Kingdom (England slice). A co-authored paper can count in more than one country; bars are not summed. Country list window: PY=2020-2026 (no yearly country slice). Year/trend charts use the last 5 years: 2022–2026. Topics: the six specification 6G topics.",
            "cc_caption_wos_all": "On every topic: WoS top 10 countries, then …, then Türkiye’s rank. The six topics are not summed. If the exact rank is missing, the label is >10. Springer 2022–2026 text-Turkey sits separately.",
            "cited_heading": "### Most cited papers",
            "cited_caption": "Ranked by the DOI record’s is-referenced-by-count, high to low. These cards are a live list.",
            "cited_caption_wos": "Ranked by WoS Times Cited, high to low. Not Crossref is-referenced-by-count. A UT (Unique Identifier) opens the full record when present. Broad 6G surveys can rank at the top because the topic token appears in the record.",
            "trend_heading": "### Trend analysis",
            "trend_caption": "Title-6G by year for Türkiye and selected European countries. There is no single Europe total (it would double-count).",
            "trend_caption_wos": "The same WoS query by year. Year axis is the last 5 years: 2022–2026. Topic series are not summed. 2026 is an incomplete year; it is not, by itself, a maturity proof against earlier years.",
            "empty_cited": "No citation-ranked records.",
            "volume_heading": "### 6G literature volume",
            "volume_caption": "Journal and proceedings with 6G in the title, Türkiye / Europe affiliation, 2020–2026.",
            "doi_heading": "### Year and topic",
            "doi_caption": "DOI prefix. WoS rank is Times Cited.",
            "chart_year": "Publications by year — title 6G",
            "chart_year_wos": "Publications by year — WoS Core Collection",
            "chart_year_x": "Calendar year",
            "chart_topic": "Türkiye — title 6G AND topic",
            "chart_topic_wos": "WoS Core Collection — TS=(6G) AND topic",
            "chart_wos_springer": "Total papers — WoS Core Collection vs Springer Meta API",
            "chart_trend_wos": "WoS Core Collection — topic series by year (not summed)",
            "series_wos": "WoS Core Collection",
            "series_springer": "Springer Meta API",
            "hover_wos_springer": "%{{y}}<br>{wos}: <b>%{{customdata[0]}}</b> {unit}<br>{springer}: <b>%{{customdata[1]}}</b> {unit}<extra></extra>",
            "wos_springer_caption": "Hover shows WoS and Springer separately for each topic. The two bars are not added into one “unique corpus”: the same paper can appear in both indexes, and overlap was not measured. WoS: TS=(6G) AND topic AND PY=2020-2026. Springer: Meta API text “6G {token}”, 2020–2026, global. The Springer (TR) cell above is not this chart. For Ambient IoT, Springer free text is wider than the quoted WoS query.",
            "chart_publisher": "DOI prefix (WoS / Springer)",
            "empty_year": "No year series (cache empty). Counts are not invented.",
            "oa_heading": "### Publications by 6G topic",
            "oa_caption": "Topic bars are Türkiye 6G + topic token. The Europe country chart is a separate tab.",
            "oa_empty": "No count; it is not invented.",
            "try_oa": "Try WoS in the browser ↗",
            "open_oa_counts": "Open on WoS ↗",
            "scholar_heading": "### Trend + external search",
            "scholar_caption": "A WoS / Springer button opens the query in a new tab; the hit count is not copied here.",
            "inst_heading": "### Top publishing institutions",
            "oa_groupby": "Affiliation string, Türkiye 6G.",
            "chart_inst": "Publications by institution (Türkiye, 6G)",
            "chart_inst_wos": "Publications by institution — WoS Affiliations",
            "chart_inst_wos_all": "Publications by institution — WoS Affiliations (topics separate, not summed)",
            "open_inst": "Open an institution search ↗",
            "inst_fallback": "Türkiye affiliation strings.",
            "chart_inst_fb": "Institutions (paper count)",
            "empty_inst": "No institution name. For Europe use the country tab.",
            "empty_inst_wos": "No institution list in the Analyze Results cache. Counts are not invented.",
            "cc_heading": "### Top publishing countries",
            "chart_cc": "Publications by country — title 6G, affiliation",
            "chart_cc_wos": "Top 10 countries — WoS Countries/Regions",
            "chart_cc_wos_all": "Top 10 countries — WoS Countries/Regions (topics separate, not summed)",
            "open_cc": "Open a country search ↗",
            "cc_fallback": "Country name in the affiliation.",
            "chart_cc_fb": "Country (paper count)",
            "empty_cc": "No country counts.",
            "empty_cc_wos": "No country list in the Analyze Results cache. Counts are not invented.",
            "papers_heading": "### Most cited 6G papers",
            "papers_caption": "Live DOI list, not a locked sample. Citations: DOI is-referenced-by-count.",
            "citations_n": "{n} citations",
            "citations_na": "Citations: —",
            "authors": "Authors",
            "open_doi": "Open the paper via DOI ↗",
            "cc": {
                "TR": "Türkiye",
                "DE": "Germany",
                "FR": "France",
                "IT": "Italy",
                "ES": "Spain",
                "GB": "United Kingdom",
                "FI": "Finland",
                "SE": "Sweden",
                "NL": "Netherlands",
                "BE": "Belgium",
                "AT": "Austria",
                "CH": "Switzerland",
                "NO": "Norway",
                "DK": "Denmark",
                "PL": "Poland",
                "PT": "Portugal",
                "GR": "Greece",
                "IE": "Ireland",
                "CZ": "Czechia",
                "HU": "Hungary",
                "RO": "Romania",
                "BG": "Bulgaria",
                "HR": "Croatia",
                "SK": "Slovakia",
                "SI": "Slovenia",
                "LT": "Lithuania",
                "LV": "Latvia",
                "EE": "Estonia",
                "LU": "Luxembourg",
                "MT": "Malta",
                "CY": "Cyprus",
                "IS": "Iceland",
                "CN": "China",
                "US": "United States",
                "KR": "South Korea",
                "CA": "Canada",
                "AU": "Australia",
                "SG": "Singapore",
                "IN": "India",
                "JP": "Japan",
                "SA": "Saudi Arabia",
                "EG": "Egypt",
            },
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
Google Patents records locked here for the TT group sit under <strong>Netsia Inc.</strong>.
Netsia is Argela/Türk Telekom’s US R&amp;D affiliate; the legal assignee is Netsia.
<strong>EP publication count in this sample is 0</strong> — it is shown, not invented.
Papers’ raw affiliation is “Türk Telekom, Ankara/Istanbul, Türkiye”. The institution graph
can mis-map a record to a DE/MY/CZ company; the country bar on the global tab is not read as TT’s European output.
</p>""",
            "metric_pat": "TT-group verified patents",
            "metric_ep": "European Patent Office",
            "metric_us": "U.S. Patent and Trademark Office",
            "metric_tr": "Turkish Patent and Trademark Office",
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
            "vs_caption": "Bars are this platform’s locked 6G sample (Google Patents). Ericsson 5, Qualcomm 4, ZTE 4, Nokia 3, TT-group (Netsia) 3, Huawei 2, Samsung 1. Not global SEP, revenue, or European-office share. Rank is by record count.",
            "office_heading": "### Patent office (verified set)",
            "office_caption": "Bars are locked Netsia grants (Google Patents). The Anadolu Ajansı national-filing ranking (921, “Türkiye on top”) is not this chart and is not opened in this section. Turkish Patent and Trademark Office is 0 in this sample — three grants sit at the U.S. Patent and Trademark Office, none at the European Patent Office.",
            "office_lock_all": "Topic search: all topics. European Patent Office {ep} · U.S. Patent and Trademark Office {us} · Turkish Patent and Trademark Office {tr}.",
            "office_lock_one": "Topic search locked to “{topic}”. European Patent Office {ep} · U.S. Patent and Trademark Office {us} · Turkish Patent and Trademark Office {tr}.",
            "empty_topic": "The locked Netsia set has no “{topic}” grant; all three office bars are 0. The office buttons in Topic search open the same query on the external site.",
            "pat_list_heading": "### Netsia Inc. (Türk Telekom group) — Google Patents",
            "pat_list_caption": "Assignee: Netsia Inc. Cards are newest to oldest (2025 → 2023). These cards are not mixed into the Nokia–ZTE vendor set.",
            "named_heading": "### Countries named in a source (complete list)",
            "named_caption": "This is the full set painted on the map. The 19 or 24 country names are not in the report; they are not added.",
            "named_col_place": "Country",
            "named_col_layer": "Layer",
            "presence_heading": "### 6G touchpoints — collaboration / standards / project",
            "presence_caption": "Each card is an official announcement. Equal-height “1 per country” bars are not drawn; they read as market share.",
            "oa_heading": "### Do not read the country chart as TT-in-Europe",
            "oa_caption": "The Countries tab above is a global 6G topic search, not a TT portfolio. Raw affiliation on the papers below is TR.",
            "papers_heading": "### Papers with Türk Telekom R&amp;D affiliation",
            "papers_caption": "DOIs are locked. Order: year newest to oldest; within a year, citation count (cited_by_count) high to low. Cards with a known WoS UT open the Core Collection full record.",
            "open_touch": "Open the source announcement ↗",
            "open_press": "Open the national-filing statement ↗",
            "open_ir": "2024 integrated report PDF ↗",
            "open_tti": "Open the TTI About page ↗",
            "position_heading": "### Where is Türk Telekom in Europe? (this platform’s measurement)",
            "position_m_pub": "TR publication rank",
            "position_m_pub_help": "6G topic + 3 MNOs and TT; {n} records",
            "position_m_pat": "TR patent rank",
            "position_m_pat_help": "Locked U.S. Patent and Trademark Office sample; {n} Netsia records",
            "position_m_ep": "European Patent Office grants",
            "position_m_us": "U.S. Patent and Trademark Office (Netsia)",
            "position_m_out": "Non-TR countries with TT papers",
            "position_m_pat_out": "Non-TR countries with TT patents",
            "position_body": """<div class="glass-card" style="border-left:6px solid #E20074;margin-bottom:12px;">
<p style="color:#F8FAFC;font-size:0.95rem;line-height:1.65;margin:0;">
<strong>Türkiye:</strong> 6G-adjacent publications rank <em>{pub_rank}</em> ({pub_n} records among 3 MNOs + TT).
Sample Google Patents records rank <em>{pat_rank}</em> ({pat_n} Netsia records).
</p>
<p style="color:#F8FAFC;font-size:0.95rem;line-height:1.65;margin:8px 0 0 0;">
<strong>Europe-wide:</strong> TT is not the publication or EP-patent leader.
Locked countries outside TR with TT-affiliated papers &gt;0: {pub_out}.
EP (European patent) grants in this set: <strong>{ep}</strong>. Netsia Google Patents: {us} records — counted on the TR row only.
Sample-patent countries outside TR: {pat_out}.
Countries are separate leagues; a single pan-Europe “TT rank” is not invented.
</p>
<p style="color:#C8D1DC;font-size:0.88rem;line-height:1.55;margin:8px 0 0 0;">
<strong>Publication leaders in those countries (high to low):</strong> {leaders}
</p>
<p style="color:#94A3B8;font-size:0.82rem;margin:8px 0 0 0;">
This is not subscriber/revenue share or a full EPO PATSTAT extract. A zero count is unranked (—).
</p>
</div>""",
            "position_body_pat": """<div class="glass-card" style="border-left:6px solid #E20074;margin-bottom:12px;">
<p style="color:#F8FAFC;font-size:0.95rem;line-height:1.65;margin:0;">
<strong>Türkiye:</strong> locked Google Patents sample rank <em>{pat_rank}</em> ({pat_n} Netsia records among 3 MNOs + TT).
<strong>Europe:</strong> EP grants in this set: <strong>{ep}</strong> — TT is not the EP-patent leader.
Netsia Google Patents {us} records are counted on the TR row only. Sample-patent countries outside TR: {pat_out}.
Countries are separate leagues; a pan-Europe rank is not invented.
</p>
<p style="color:#94A3B8;font-size:0.82rem;margin:8px 0 0 0;">
This is not an EPO PATSTAT extract or subscriber share. A zero count is unranked (—). Publication tables sit on Publication Trends.
</p>
</div>""",
            "position_body_pub": """<div class="glass-card" style="border-left:6px solid #E20074;margin-bottom:12px;">
<p style="color:#F8FAFC;font-size:0.95rem;line-height:1.65;margin:0;">
<strong>Türkiye:</strong> 6G-adjacent publications rank <em>{pub_rank}</em> ({pub_n} records among 3 MNOs + TT).
<strong>Europe:</strong> TT is not the publication leader. Locked countries outside TR with TT-affiliated papers &gt;0: {pub_out}.
Countries are separate leagues; a pan-Europe rank is not invented.
</p>
<p style="color:#C8D1DC;font-size:0.88rem;line-height:1.55;margin:8px 0 0 0;">
<strong>Publication leaders in those countries (high to low):</strong> {leaders}
</p>
<p style="color:#94A3B8;font-size:0.82rem;margin:8px 0 0 0;">
This is not subscriber/revenue share. A zero count is unranked (—). Patent tables sit on Patent Intelligence.
</p>
</div>""",
            "what_title_pub": "How affiliation builds the country ranking",
            "what_body_pub": """<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.65;margin:8px 0 0 0;">
<strong>DOI / affiliation</strong> counts 6G-topic papers by institution ID or affiliation string.
The Türk Telekom row is not inflated on a non-TR country with the TR institution ID; if that country has no DOI-locked affiliation, the count is 0.
</p>
<p style="color:#CBD5E1;font-size:0.88rem;line-height:1.6;margin:10px 0 0 0;">
1st/2nd/3rd rank the three MNOs from the Wikipedia European list, not subscriber share.
Patent-office tables are not on this page — they sit on Patent Intelligence.
</p>""",
            "overview_heading": "### Europe-wide — 3 operators + Türk Telekom",
            "overview_heading_pat": "### Europe-wide — patents (locked sample)",
            "overview_heading_pub": "### Europe-wide — publications",
            "overview_caption": "In each country the three MNOs from the Wikipedia list are counted via a 6G topic search on institution IDs (or affiliation strings). 1st/2nd/3rd rank those three firms, not subscriber share. TT is a separate column. A measured 0 (institution found, no topic hits) stays 0. A count that could not be queried stays — and is not invented. Patent columns are this platform’s locked sample, not an EPO PATSTAT extract.",
            "overview_caption_pat": "Only countries with at least one patent in the locked sample. No empty 2nd/3rd operator columns; publication columns are not on this page. Netsia Google Patents is counted on TR only. A zero count is unranked (—).",
            "overview_caption_pub": "In each country the three Wikipedia MNOs are counted via a 6G topic search. 1st/2nd/3rd rank those firms, not subscriber share. TT is a separate column. A measured 0 stays 0. A count that could not be queried stays —.",
            "overview_spin": "Loading operator publication counts (skipped when cached)",
            "overview_spin_pat": "Loading the locked patent sample",
            "overview_empty_pat": "The locked sample has no patents on the Europe rows. Counts are not invented.",
            "overview_hits_pat": "Firms with records (sample)",
            "overview_pub_title": "Publication leader in-country (>0)",
            "overview_pat_title": "Patent leader in-country (locked sample, >0)",
            "overview_vs_title": "Publications: in-country leader vs Türk Telekom",
            "overview_vs_title_pat": "Patents: in-country leader (sample) vs Türk Telekom",
            "overview_pub_lead_short": "Leader",
            "overview_pat_lead_short": "Leader (sample)",
            "overview_tt_pub": "TT papers",
            "overview_tt_pat": "TT patents (sample)",
            "overview_pub_lead": "Pub. leader (n)",
            "overview_pat_lead": "Patent leader (n)",
            "overview_pub_1": "Pub. 1st",
            "overview_pub_2": "Pub. 2nd",
            "overview_pub_3": "Pub. 3rd",
            "overview_pat_1": "Patent 1st (sample)",
            "overview_pat_2": "Patent 2nd (sample)",
            "overview_pat_3": "Patent 3rd (sample)",
            "rank_heading": "### Country detail: 3 MNOs (mobile network operators) + Türk Telekom",
            "rank_heading_pat": "### Country detail — patents (3 MNOs + Türk Telekom)",
            "rank_heading_pub": "### Country detail — publications (3 MNOs + Türk Telekom)",
            "rank_caption": "The three operators are locked from that country’s row in the Wikipedia European MNO list; subscriber/revenue “top 3” was not measured here. Publication counts are a 6G topic search. Patent counts are Google Patents (Netsia on TR only). A zero count is unranked (—); zeros are not labelled “2nd”. Not global SEP or market share.",
            "rank_caption_pat": "The three Wikipedia MNOs + TT in this country. Patents = Google Patents (Netsia on TR only). There is no operator publication API on this tab. A zero count is unranked (—). Cards open Google Patents.",
            "rank_caption_pub": "The three operators are locked from the Wikipedia European MNO list. Publications are a 6G topic search. A zero count is unranked (—). Patent-office columns are not on this page.",
            "rank_country": "European country",
            "rank_spin": "Loading the country ranking",
            "rank_col_firm": "Firm",
            "rank_pub_title": "Publication rank (this country)",
            "rank_pat_title": "Patent rank (locked sample)",
            "rank_pub_x": "Publication count",
            "rank_pat_x": "Sample patent records",
            "rank_tt": "Türk Telekom in this country: publications rank {pub} ({pub_n} publication records) · patents rank {pat} ({pat_n} sample records) — {n} firms",
            "rank_tt_pat": "Türk Telekom in this country: patents rank {pat} ({pat_n} sample records) — {n} firms",
            "rank_tt_pub": "Türk Telekom in this country: publications rank {pub} ({pub_n} publication records) — {n} firms",
            "rank_oa_fail": "No publication answer for this country; the publication bars are not drawn.",
            "rank_col_rank_pub": "Pub. rank",
            "rank_col_pub": "Publications",
            "rank_col_rank_pat": "Patent rank",
            "rank_col_pat": "Patents (sample)",
            "rank_open_oa": "Open this country’s 6G search on WoS ↗",
            "rank_open_wiki": "Open the European MNO list ↗",
            "rank_open_gp": "Google Patents assignee ↗",
            "layer": {
                "hq": "HQ / operator R&amp;D (research and development)",
                "wholesale": "TTI (Türk Telekom International) wholesale — first-mover",
                "rd_collab": "6G R&amp;D (research and development) partnership",
                "standards": "Standards body: ETSI (European Telecommunications Standards Institute)",
                "mou_venue": "MoU (memorandum of understanding) signing venue",
                "ep_grant": "EPO (European Patent Office) EP grant",
            },
            "map_col_layer": "Layer",
            "map_col_note": "Note",
        },
        "ui": {
            "source": "Open Source ↗",
            "no_source": "No source link.",
        },
        "sources": {
            "patent_heading": "### Patent source",
            "patent_caption": "This page uses the Lens.org patent API. Cards and charts are JSON records. The same publication number opens on Lens.org.",
            "pub_heading": "### Publication source",
            "pub_caption": "This page uses WoS Core Collection and Springer. Each card opens DOI + (if any) Springer + the WoS full record.",
            "patent_metric": "Lens.org",
            "assignee_caption": "Applicant search for “{company}” — we do not copy the hit count here; verify on the site.",
            "topic_search": "Topic search (spec: ISAC, RIS, NTN, AI-RAN, THz, Ambient IoT)",
            "topic_all": "All",
            "topic_all_caption": "Cards and charts are Lens.org records. Pick a topic and the query drops to that domain.",
            "topic_all_caption_pub": "Cards are the full locked DOI set. Pick a topic and the counts on this page drop to that topic.",
            "topic_caption": "Query: “{q}”. The link opens the search page.",
            "topic_result_caption": "Cards and bars on this page are locked-sample “{topic}” records. The office buttons open the same query (“{q}”).",
            "topic_result_caption_pub": "Cards on this page are locked DOI-set “{topic}” records. The publication buttons open the same query (“{q}”).",
            "open_google_patents": "Lens.org ↗",
            "open_lens": "Lens.org ↗",
            "open_espacenet": "Lens.org ↗",
            "open_wipo": "Lens.org ↗",
            "open_uspto": "Lens.org ↗",
            "open_ieee": "WoS ↗",
            "open_scholar": "Springer ↗",
            "open_springer": "Springer ↗",
            "open_elsevier": "Springer ↗",
            "open_wos": "WoS ↗",
            "open_doi": "DOI ↗",
            "open_crossref": "Crossref ↗",
            "mix_heading": "### Mixed search (spec databases)",
            "mix_caption": "The same 6G topic: papers (WoS, Springer) + patents (Lens.org).",
            "mix_pub_row": "Publication search",
            "mix_pat_row": "Patent search (Lens.org)",
            "topic_pat_heading": "### Topic search — this page + Lens.org",
            "topic_pat_caption": "The drop-down locks the query. Cards and the six charts are Lens.org records. The button opens the same query on Lens.org.",
            "topic_pub_heading": "### Topic search — this page + WoS / Springer",
            "topic_pub_caption": "The drop-down locks ISAC–Ambient IoT. Charts are WoS Core Collection (global). Buttons open WoS and Springer in a new tab.",
            "topic_buttons_hint": "These buttons are external search (new tab). On-page counts change only from the drop-down above.",
            "topic_buttons_hint_pub": "These buttons are external search (new tab). On-page paper counts change only from the drop-down above.",
            "topic_live_all": "Lens.org (seven 6G topics): **{n}**. Pulled rows: **{pulled}**. Not summed. Not raw «6G».",
            "topic_live_one": "Lens.org “{topic}” (`{q}`): **{n}**. Pulled rows: **{pulled}**. Not summed.",
            "topic_live_all_pub": "WoS Core Collection: TS=(6G) AND topic, PY=2020-2026. The six topic bars are separate and not summed. Türkiye title-6G cache: **{n}** (not the global WoS count).",
            "topic_live_one_pub": "WoS Core Collection “{topic}”: **{n}** records. Query: `{q}`. Türkiye title-6G: {tr} (Crossref cache; not the global WoS count).",
            "totals_caption_pat": "Same query, Lens.org patent/search. No answer → —. The total is not summed with pulled rows.",
            "totals_caption_pub": "WoS and Springer: that site’s API when a key is set. No key → —.",
            "total_col_db": "Database",
            "total_col_n": "Total",
            "total_col_how": "How counted",
            "total_col_open": "Open search",
            "total_open_text": "Open",
            "method_gp": "Google Patents xhr (not used on this page)",
            "method_none": "No public JSON count API",
            "method_need_key": "No personal API key (cell —)",
            "method_api_empty": "Key present; office returned no total — not invented",
            "method_native_lens": "Lens.org patent/search (same query)",
            "method_native_espacenet": "EPO OPS (not used on this page)",
            "method_native_uspto": "PatentsView (not used on this page)",
            "method_native_ieee": "WoS Core Collection",
            "method_native_springer": "Springer Meta API: text 6G, 2020–2026",
            "method_native_elsevier": "Springer Meta API",
            "method_native_wos": "Clarivate WoS Starter API / Analyze Results",
            "method_native_scholar": "WoS Core Collection",
            "method_crossref_ieee": "Crossref query.title=6G + prefix 10.1109",
            "method_crossref_springer": "Crossref query.title=6G + prefix 10.1007",
            "method_crossref_elsevier": "Crossref query.title=6G + prefix 10.1016",
            "method_crossref_title": "Crossref query.title=6G, journal, 2020–2026",
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
            "fallback_none": "### 6G assistant (retrieval mode)\n\nYour question did not match the platform corpus. Review the verified sources on 6G Technology Explorer, Patent Intelligence, or Academic Publication Analysis.",
            "related": "**Related verified records:**",
            "tfidf_note": "*This answer is from platform records selected with TF-IDF; numbers are not invented.*",
            "llm_fail": "*The LLM did not return an answer: {exc}*",
            "glossary_title": "Technical glossary (first-use expansions)",
            "cite_n": "{n} citations",
            "cite_na": "citation count was not returned by the source",
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
- **6G Technology Explorer** — definition, operating principle, block diagram, architecture, use cases, advantages/disadvantages, global work, TT scenarios, TRL
- **Patent Intelligence** — Nokia–Intel (9 firms); seven 6G topics; Lens.org; charts: firms, year, topic, radar, cloud, tree, density, map
- **Academic Publication Analysis** — WoS Core Collection + Springer; year / institution / country / cited / trend
            """,
            "mod_right": """
- **Türk Telekom View** — field scenario engine
- **AI Assistant** — local TF-IDF retrieval; optional Groq / Gemini
- **About** — this page (delivery / 15-minute talk outline)
            """,
            "stack": "#### Stack",
            "stack_body": "Python, Streamlit, Pandas, Plotly, Matplotlib, NetworkX, WordCloud, scikit-learn. Optional: Groq API, Google Gemini API. Patents: Lens.org. Papers: WoS, Springer.",
            "standard": "#### Teaching standard",
            "standard_body": "Technical content is two-layer: **foundation** (what / why / how / when) and **expert** (equation, assumption, 3GPP). Expert mode does not skip the foundation. Abbreviations expand on first use. Patent abstracts, DOIs, and numbers are not invented.",
            "talk": "#### 15-minute talk outline",
            "talk_body": """
1. Purpose and scope (1 min)
2. Home TRL radar (2 min)
3. One technology (e.g. RIS) — principle + diagram + TT scenario (3 min)
4. Patent Intelligence — company filter, year chart, TT Europe footprint (3 min)
5. Academic Publication Analysis — WoS / Springer + TT-affiliated DOI (3 min)
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
            "patent_year": "6G patent records by publication year (pulled Lens rows)",
            "patent_count": "Patent record count",
            "domain_radar": "Firm × 6G topic — pulled record count",
            "topic_mix": "Patent topic mix (pulled rows)",
            "topic_axis": "Topic",
            "keywords": "Most frequent keywords in patent claims",
            "kw_x": "Title occurrences",
            "academic_trend": "Title 6G — papers by year (Türkiye / Europe)",
            "pub_count": "Paper count",
            "db_default": "Verified sample set — publisher count",
            "publisher": "Publisher",
            "paper_count": "Paper count",
            "hover_v": "%{{x}}<br><b>%{{y}}</b> {unit}<extra></extra>",
            "hover_h": "%{{y}}<br><b>%{{x}}</b> {unit}<extra></extra>",
            "network": "Assignee ↔ technology-domain network",
            "nx_missing": "NetworkX is not installed; the network graph cannot be shown.",
            "company_counts": "Firms with the most filings (Lens.org total)",
            "company": "Company",
            "density": "Patent density (company × domain, record count)",
            "sunburst": "Patent tree (firm → topic, Lens total)",
            "tfidf": "Patent technology map (TF-IDF + PCA, title vectors)",
            "oa_bar_x": "Paper count",
            "tt_office": "TT-group — which patent office granted the locked records",
            "tt_office_x": "Patent office",
            "office_epo": "European Patent Office",
            "office_uspto": "U.S. Patent and Trademark Office",
            "office_turkpatent": "Turkish Patent and Trademark Office",
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
