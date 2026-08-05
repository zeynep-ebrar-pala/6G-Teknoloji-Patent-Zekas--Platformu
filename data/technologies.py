"""
Türk Telekom 6G Technology & Patent Intelligence Platform
Module 1: 6G Technologies Comprehensive Knowledge Base
Dual-Depth Architecture (Beginner / Executive + Deep Technical / Academic)
"""

TECHNOLOGIES = {
    "isac": {
        "id": "isac",
        "title": "Entegre Algılama ve İletişim (ISAC)",
        "acronym": "ISAC",
        "icon": "📡",
        "trl": 4,
        "trl_desc": "Laboratuvar Doğrulaması & Saha Testleri Başlangıcı (TRL 4 - 3GPP Rel-19/20 Hedefi)",
        "card_summary": "Baz istasyonlarını akıllı birer radara dönüştürerek hem yüksek hızlı haberleşme hem de santimetre hassasiyetinde 3D nesne/araç algılama sağlar.",
        "highlights": ["🎯 1cm Radar Hassasiyeti", "📡 100+ Gbps Hız", "🛰️ V2X / Dron Takibi"],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>1 Cümlede Nedir?</strong><br>"
            "ISAC, baz istasyonlarının sadece cihazlara veri taşımasını değil, aynı zamanda tıpkı bir <strong style='color: #FFFFFF;'>görünmez radar</strong> gibi çevredeki araçları, insanları, dronları ve engelleri santimetre hassasiyetinde tespit etmesini sağlayan 6G teknolojisidir.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Basit Analoji:</strong><br>"
            "Sıradan bir baz istasyonu sadece 'konuşan' bir radyo kulesidir. ISAC özellikli 6G baz istasyonu ise hem konuşan hem de gözleriyle çevreyi tarayıp 3 boyutlu haritalandıran <strong style='color: #FFFFFF;'>akıllı bir gözcü kulesine</strong> dönüşür."
        ),
        "working_principle": (
            "<strong style='color: #00E5FF;'>Ortak Dalga Şekli ve Donanım Paylaşımı (Joint Communication and Sensing - JCR):</strong><br>"
            "ISAC, kablosuz haberleşme sinyalleri (OFDM / OTFS / Terahertz dalga şekilleri) ile radar tespiti sinyallerini aynı frekans bandında, aynı donanım üzerinde ve ortak bir kaynak tahsis algoritması ile birleştirir.<br><br>"
            "1. <strong style='color: #FFFFFF;'>Monostatik ve Bistatik Algılama:</strong> Baz istasyonu vericisi (Tx) sinyali gönderir. Hedef objeden yansıyan eko sinyali (Echo Signal) ya aynı istasyon (Monostatic) ya da komşu istasyonlar (Bistatic/Multistatic) tarafından yakalanır.<br>"
            "2. <strong style='color: #FFFFFF;'>Geliş Açısı (AoA) ve Doppler Kestirimi:</strong> Yansıyan sinyalin gecikme süresinden (Mesafe), faz kaymasından (Doppler / Hız) ve çoklu anten dizisi faz farklarından (Geliş Açısı - AoA/AoD) objenin 3D konumu, hızı ve yönü çıkarılır.<br>"
            "3. <strong style='color: #FFFFFF;'>Sinyal Çakışmasını Önleme:</strong> İletişim verisi ile radar yankısı birbirini bozmasın diye Zaman, Frekans ve Kod Alanında dik (Orthogonal) kaynak paylaşımı yapılır."
        ),
        "system_architecture": (
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>1. Fiziksel Katman ve Anten Donanımı (PHY & Hardware):</strong><br>"
            "• Masif Çoklu Giriş Çoklu Çıkış (Massive MIMO) anten dizileri ve geniş bant RF transiver birimleri kullanılır.<br>"
            "• Çift işlevli dalga şekli tasarımı (DFRC - Dual-Functional Radar-Communication) ve OTFS (Orthogonal Time Frequency Space) modülasyonu ile hem haberleşme sembolleri hem de radar problama sinyalleri tek bir radyo frekansında birleştirilir.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>2. Protokol ve Sinyal İşleme Katmanı (MAC & Signal Processing):</strong><br>"
            "• Gelişmiş DSP (Sinyal İşlemci), FPGA ve GPU üniteleri üzerinde çalışan Cramér-Rao Algılama Sınırı (CRB) ve FFT tabanlı Doppler/AoA kestirim algoritmaları entegredir.<br>"
            "• Dinamik kaynak tahsisi (RRM), haberleşme veri hızını düşürmeden radar çözünürlüğünü maksimuma çıkaracak şekilde gerçek zamanlı çalışır.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>3. Şebeke ve Kenar Bulut Entegrasyonu (O-RAN & Core Network):</strong><br>"
            "• Open RAN (O-RAN) mimarisinde Near-RT RIC (RAN Intelligent Controller) üzerinde çalışan xApps yazılımları ile algılama haritaları çıkarılır.<br>"
            "• 3GPP Release-19/20 standartlarına uyumlu olan bu mimarı, algılanan 3D nokta bulutu verilerini (Point Cloud Data) doğrudan Türk Telekom Kenar Sunucularına (Edge Cloud) iletir."
        ),
        "mathematical_foundation": (
            "Radar Denkleminde Sinyal-Gürültü Oranı (SNR):\n"
            "$$SNR_{radar} = \\frac{P_t G_t G_r \\lambda^2 \\sigma}{(4\\pi)^3 R^4 k T_0 B L}$$\n\n"
            "Ortak Kapasite ve Algılama Sınırı (Cramér-Rao Bound - CRB):\n"
            "$$CRB(\\theta) \\ge \\frac{1}{J(\\theta)}, \\quad C_{com} = B \\log_2 \\left(1 + \\frac{P_{com}|h|^2}{\\sigma_n^2}\\right)$$"
        ),
        "use_cases": [
            "Otonom Araçlar & V2X Trafik Güvenliği (Kör nokta ve sis içi nesne tespiti)",
            "Alçak İrtifa İHA/Dron Trafik Yönetimi (UTM) & İzinsiz Dron Engelleme",
            "Akıllı Şehirler & Trafik Yoğunluğu / Yaya Akışı Haritalama",
            "Endüstriyel Depo Otonom Robot (AGV) Navigasyonu",
            "Sağlık & Yaşlı Bakımı (Kamera kullanmadan nefes/kalp atışı ve düşme tespiti)"
        ],
        "advantages": [
            "Ek Radar Donanımı Maliyetini Sıfıra İndirme (Mevcut 6G şebekesi radar görevi görür)",
            "Yüksek Hassasiyet (Santimetre altı mesafe ve derece altı açı tespiti)",
            "Gece, Sis ve Kötü Hava Şartlarında Kesintisiz Çalışma (Kameraya kıyasla üstünlük)",
            "Frekans Spektrumunun Çift Kullanımı (Yüksek Spektral Verimlilik)"
        ],
        "disadvantages": [
            "İletişim Hızı ile Radar Çözünürlüğü Arasında Güç/Yansıma Çatışması (Trade-off)",
            "Yoğun Şehir İçi Çoklu Yansıma (Clutter / Multi-path) Parazitleri",
            "Gizlilik ve Kişisel Veri Güvenliği Endişeleri (Kameralı olmadan takip riski)"
        ],
        "global_research": [
            "3GPP Release-19 Study Item: Integrated Sensing and Communication",
            "EU Hexa-X II Project (Flagship 6G Initiative in Europe)",
            "IEEE ComSoc ISAC Emerging Technology Initiative",
            "Nokia Bell Labs, Huawei 6G ISAC Testbed Gösterimleri (100+ Gbps + 1cm algılama)"
        ],
        "tt_scenarios": [
            "<strong>İstanbul Boğazı & Marmara Deniz Seyir Güvenliği:</strong> Türk Telekom sahil baz istasyonları ile boğazdaki tüm deniz taşıtlarının sis altında gerçek zamanlı konum/hız takibi.",
            "<strong>İstanbul / Ankara İHA (Dron) Koridorları:</strong> Türk Telekom 6G kuleleri ile şehir içi teslimat dronlarının uçuş güvenliği ve kaçak dron tespiti.",
            "<strong>AFAD Entegre Deprem Enkaz Algılama:</strong> Deprem anında binaların enkaz altındaki hareketliliklerin duvar arkası RF algılama ile kameralar olmadan tespiti."
        ],
        "references": [
            "F. Liu et al., 'Integrated Sensing and Communications: Toward Dual-Functional Design for 6G', IEEE Transactions on Communications, 2022.",
            "3GPP TR 22.837: 'Feasibility Study on Integrated Sensing and Communication (ISAC) for 6G', Rel-19.",
            "Hexa-X Deliverable D3.2: 'Localization and sensing display in 6G environment'."
        ]
    },

    "ris": {
        "id": "ris",
        "title": "Yeniden Yapılandırılabilir Akıllı Yüzeyler (RIS)",
        "acronym": "RIS",
        "icon": "🪞",
        "trl": 5,
        "trl_desc": "Saha Denemeleri & Prototip Doğrulaması (TRL 5 - Düşük Güç Tüketimli Akıllı Yüzeyler)",
        "card_summary": "Binalara ve camlara yerleştirilen pasif metamalzeme yüzeylerle radyo dalgalarını akıllı bir ayna gibi bükerek kör noktaları kapsar.",
        "highlights": ["🪞 Akıllı Yansıtıcı Yüzey", "🌱 %90 Enerji Tasarrufu", "🏙️ Kör Nokta Kapsama"],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>1 Cümlede Nedir?</strong><br>"
            "RIS, binaların dış cephelerine, camlara veya duvarlara kaplanan ve gelen radyo sinyallerini istenen yöne bir <strong style='color: #FFFFFF;'>akıllı ayna</strong> gibi yansıtarak sinyal ulaşmayan kör noktaları kapsayan teknolojidir.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Basit Analoji:</strong><br>"
            "Karanlık bir odadasınız ve el feneri (baz istasyonu) duvarın arkasını aydınlatamıyor. Duvara yerleştirdiğiniz açıları ayarlanabilir bir ayna (RIS), fener ışığını bükerek görünmeyen odaya <strong style='color: #FFFFFF;'>odaklanmış ışık demeti</strong> olarak yönlendirir."
        ),
        "working_principle": (
            "<strong style='color: #00E5FF;'>Faz Kontrolü ve Metamalzeme Yansıma Prensibi:</strong><br>"
            "RIS, üzerinde yüzlerce/binlerce pasif veya yarı-aktif mikroskobik yansıtıcı eleman (PIN diyotlar, varaktörler veya varaktörlü metamalzemeler) barındıran elektronik bir yüzeydir.<br><br>"
            "1. <strong style='color: #FFFFFF;'>Faz Kaydırma Kontrolü (Phase Shifting):</strong> Her bir metamalzeme elemanı, üzerine düşen elektromanyetik dalganın fazını 0 ile 2π arasında bağımsız olarak kaydırır.<br>"
            "2. <strong style='color: #FFFFFF;'>Hüzme Şekillendirme (Beamforming):</strong> Tüm elemanların faz kaymaları birleştirilerek gelen sinyal aynen yansımak yerine (Snell Yasasının ötesinde) istenen kullanıcı cihazına odaklanmış dar bir hüzme olarak yönlendirilir.<br>"
            "3. <strong style='color: #FFFFFF;'>Sıfır/Ultra Düşük Enerji:</strong> Aktif verici (RF Chain) içermez; sadece diyotların durumunu değiştirmek için birkaç milliwatt elektrik tüketir."
        ),
        "system_architecture": (
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>1. Yüzey ve Donanım Katmanı (RIS Hardware & Metamaterials):</strong><br>"
            "• Baskılı devre kartı (PCB) üzerine dizilmiş mikroskobik yansıtıcı elemanlar (PIN diyot, MEMS veya Likit Kristal tabanlı metamalzemeler).<br>"
            "• Ultra düşük güçlü faz kaydırıcı sürücü devreleri ve RF güçlendirici içermeyen pasif yansıtma mimarisi.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>2. Kontrolör ve Yazılım Katmanı (RIS Controller & Microcontroller):</strong><br>"
            "• FPGA / ARM tabanlı yerleşik denetleyici kartı, baz istasyonundan gelen emir doğrultusunda metamalzeme diyotlarının voltajını ve faz açılarını ayarlar.<br>"
            "• Gerçek zamanlı hüzme yönlendirme algoritmaları ile hareketli kullanıcı cihazları takip edilir.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>3. Ağ ve Operatör Arabirimi (Control Link & 3GPP RIS Architecture):</strong><br>"
            "• Baz istasyonu (gNB) ile RIS Kontrolcüsü arasında ultra düşük gecikmeli kablosuz/kablolu kontrol hattı (C-plane Link) bulunur.<br>"
            "• ETSI RIS ISG ve 3GPP Rel-19/20 spesifikasyonlarına uygun olarak Türk Telekom şebekesine tak-çalıştır (Plug-and-Play) olarak entegre edilir."
        ),
        "mathematical_foundation": (
            "RIS Aracılı Sinyal Kanal Modeli ve Alınan Güç Formülü:\n"
            "$$y = \\left( \\mathbf{h}_r^H \\mathbf{\\Phi} \\mathbf{G} \\right) x + n, \\quad \\mathbf{\\Phi} = \\text{diag}(e^{j\\theta_1}, e^{j\\theta_2}, \\dots, e^{j\\theta_N})$$\n\n"
            "Kanal Kazancı (N elemanlı RIS için geleneksel röleye kıyasla $N^2$ scaling law):\n"
            "$$P_r \\propto N^2 \\cdot |h_{Tx-RIS}|^2 \\cdot |h_{RIS-Rx}|^2$$"
        ),
        "use_cases": [
            "Görüş Hattı Olmayan (N-LoS) Şehir İçi Binalar Arası Kapsama",
            "Tüneller, Metro İstasyonları ve Yeraltı Tesisleri Sinyal Güçlendirme",
            "İç Mekan (Home/Office) Ultra Yüksek Hızlı mmWave/THz Bağlantısı",
            "Yeşil Haberleşme (Green Communications) & Düşük Karbon Ayak İzi",
            "ISAC ile Entegre Konumlandırma & Yansıtmalı Konum Tespiti"
        ],
        "advantages": [
            "Çok Düşük Maliyet ve Enerji Tüketimi (Aktif Baz İstasyonuna Göre %90+ Tasarruf)",
            "Kolay Montaj (Duvarlara, camlara, binalara yapıştırılabilir esnek yapı)",
            "Çevre Dostu Yeşil Teknoloji (Aktif Radyasyon Yaymaz, Gelen Dalgayı Yönlendirir)",
            "Frekans Bandından Bağımsız Tasarlanabilme (Sub-6GHz'den THz'e)"
        ],
        "disadvantages": [
            "Kanal Kestirimi (Channel Estimation) Zorluğu (Pasif elemanlar kanal ölçemez)",
            "İki Kademeli Sönümlenme Kaybı (Double Path Loss Effect: Tx->RIS->Rx)",
            "Gerçek Zamanlı Faz Kontrolü İçin Yüksek Hesaplama Yükü"
        ],
        "global_research": [
            "ETSI Industry Specification Group (ISG) RIS",
            "IEEE Wireless Communications Technical Committee RIS Task Force",
            "ZTE, Huawei, NTT Docomo Saha Denemeleri (5G-Advanced & 6G RIS PoC)",
            "RISE-6G EU Project (Reconfigurable Intelligent Surfaces for 6G)"
        ],
        "tt_scenarios": [
            "<strong>Tarihi Yarımada & Dar Sokak Kapsaması (İstanbul):</strong> Tarihi dokuya zarar vermeden, yeni kule dikmeksizin bina yüzeylerine akıllı kaplama RIS ile kesintisiz 6G.",
            "<strong>Avrasya Tüneli & Marmaray Kesintisiz Kapsama:</strong> Tünel içi kıvrımlarda sinyal sönümlenmesini önleyen pasif RIS panelleri ile Türk Telekom abonelerine 10 Gbps+ hız.",
            "<strong>Türk Telekom Plaza & Veri Merkezleri Cam Kaplama:</strong> Plaza binalarının dış camlarına entegre şeffaf RIS kaplaması ile iç mekan mmWave kapsama sorununu çözme."
        ],
        "references": [
            "Q. Wu and R. Zhang, 'Towards Smart and Reconfigurable Environment: Intelligent Reflecting Surface Aided Wireless Network', IEEE Communications Magazine, 2020.",
            "ETSI GR RIS 001: 'Reconfigurable Intelligent Surfaces (RIS); Use Cases, Deployment Scenarios and Operational Requirements'.",
            "E. Basar et al., 'Wireless Communications Through Reconfigurable Intelligent Surfaces', IEEE Access, 2019."
        ]
    },

    "cell_free": {
        "id": "cell_free",
        "title": "Hücresiz Masif MIMO (Cell-Free Massive MIMO)",
        "acronym": "Hücresiz MIMO",
        "icon": "📶",
        "trl": 4,
        "trl_desc": "Deneysel Prototip ve Simülasyon Testleri (TRL 4 - Hücresiz Ağ Mimarisi)",
        "card_summary": "Geleneksel hücre sınırlarını ortadan kaldırarak kullanıcının etrafındaki yüzlerce erişim noktasını tek bir devasa anten gibi birleştirir.",
        "highlights": ["🔄 Kesintisiz Sinyal Bulutu", "⚡ Sıfır Hücre Sınırı", "📶 Eşit 1 Gbps+ Deneyim"],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>1 Cümlede Nedir?</strong><br>"
            "Hücresiz Masif MIMO, bilinen klasik 'hücre' (cell) sınırlarını ortadan kaldırarak yüzlerce küçük erişim noktasının (AP) tek bir devasa sistem gibi çalışıp her kullanıcıyı kesintisiz kuşatmasıdır.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Basit Analoji:</strong><br>"
            "Klasik hücresel sistemde kullanıcı bir baz istasyonundan diğerine geçerken sinyal düşer ve kopma riski oluşur. Hücresiz sistemde ise nerede olursanız olun etrafınızdaki onlarca mini anten sizi ortak bir <strong style='color: #FFFFFF;'>sinyal bulutu</strong> gibi takip eder."
        ),
        "working_principle": (
            "<strong style='color: #00E5FF;'>Dağıtık Koordinasyon ve Hücresiz Mimari:</strong><br>"
            "Geleneksel ağlarda kullanıcılar belirli bir hücresel sektöre (Cell) bağlıdır ve hücre kenarlarında (Cell Edge) parazit (Interference) artar.<br><br>"
            "1. <strong style='color: #FFFFFF;'>Dağıtık Erişim Noktaları (Distributed APs):</strong> Coğrafi olarak geniş alana dağıtılmış çok sayıda basit erişim noktası (AP), yüksek hızlı ön-bağlantı (Fronthaul) ile Merkezi İşleme Birimine (CPU) bağlanır.<br>"
            "2. <strong style='color: #FFFFFF;'>Ortak İşbirlikçi Ön Kodlama (Coordinated Precoding):</strong> Tüm AP'ler kullanıcıya aynı anda ve aynı frekansta hizmet verir. Hücre kenarı kavramı tamamen yok olur.<br>"
            "3. <strong style='color: #FFFFFF;'>Parazit Bastırma (Interference Cancellation):</strong> Komşu hücre paraziti, işbirlikçi sinyal işleme sayesinde faydalı sinyal gücüne dönüştürülür."
        ),
        "system_architecture": (
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>1. Dağıtık Radyo ve Anten Katmanı (Distributed Access Points):</strong><br>"
            "• Şehir ve binalara dağıtılmış düşük karmaşıklıktaki erişim noktaları (AP) ve çoklu anten dizileri.<br>"
            "• Her AP, yerel sinyal alma-gönderme fonksiyonlarını yürütür ve karmaşık işleme yükünü merkezi birimlere devreder.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>2. Ön Bağlantı Şebekesi (High-Speed Fiber Fronthaul):</strong><br>"
            "• Tüm AP'leri Merkezi İşleme Birimine (CPU) bağlayan eCPRI ve RoF (Radio over Fiber) tabanlı yüksek bant genişlikli fiber ve optik altyapı.<br>"
            "• Zaman senkronizasyonu (PTP IEEE 1588) ile nanosaniye hassasiyetinde anten eşzamanlaması sağlanır.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>3. Merkezi İşleme Birimi (Central Processing Unit - CPU & Edge Cloud):</strong><br>"
            "• Kenar bulut üzerinde çalışan MMSE (Minimum Mean Square Error) ve Zero-Forcing ön kodlama matrislerini hesaplayan sunucu havuzu.<br>"
            "• Tüm kullanıcılara eşit ve adil (Quality of Experience) Terabit seviyesinde bağlantı kalitesi sunulur."
        ),
        "mathematical_foundation": (
            "Kullanıcı k için Sinyal-Gürültü ve Parazit Oranı (SINR):\n"
            "$$SINR_k = \\frac{\\left| \\sum_{m=1}^M \\mathbf{g}_{mk}^H \\mathbf{w}_{mk} \\right|^2}{\\sum_{j \\neq k} \\left| \\sum_{m=1}^M \\mathbf{g}_{mk}^H \\mathbf{w}_{mj} \\right|^2 + \\sigma^2}$$\n\n"
            "MMSE (Minimum Mean Square Error) Kanal Kestirimi ve Ortak Kapsama Formülasyonu."
        ),
        "use_cases": [
            "Stadyumlar, Konser Alanları ve Yüksek Yoğunluklu Etkinlikler",
            "Havaalanları, Tren Garı ve Alışveriş Merkezleri İç Mekan İletişimi",
            "Endüstriyel Akıllı Fabrikalar (Gecikmesiz ve Kesintisiz Robot Kontrolü)",
            "Şehir Merkezi Yoğun Bulvarlar ve Meydanlar"
        ],
        "advantages": [
            "Hücre Kenarı Sorununun Tamamen Çözülmesi (Uniform User Experience)",
            "Çok Yüksek Spektral Verimlilik (Klasik MIMO'ya kıyasla 5x-10x artış)",
            "Makro Kule İhtiyacının Azalması (Daha estetik ve dağıtık mimari)",
            "Makro Kopmaların (Handover Failures) Sıfıra İnmesi"
        ],
        "disadvantages": [
            "Devasa Fronthaul Yükü (Tüm AP'lerin merkezi bir birime yüksek hızda bağlanma gereksinimi)",
            "Merkezi İşleme Biriminde (CPU) Yüksek Hesaplama Karmaşıklığı",
            "Yüksek Fiber Optik Altyapı Maliyeti"
        ],
        "global_research": [
            "Linköping Üniversitesi (Prof. Emil Björnson & Prof. Erik G. Larsson Çalışmaları)",
            "IEEE Wireless Communications Letters - Cell-Free Special Issues",
            "3GPP Release-19/20 Distributed Massive MIMO Çalışma Grupları",
            "Ericsson & Nokia 6G Distributed MIMO Laboratuvar Gösterimleri"
        ],
        "tt_scenarios": [
            "<strong>Türk Telekom RAMS Park / Şükrü Saracoğlu Stadyum Çözümü:</strong> 50.000+ taraftarın aynı anda canlı yayın yaptığı durumlarda stadyum çatısına ve tribünlere dağıtılmış Cell-Free AP'ler ile sıfır hız düşüşü.",
            "<strong>İstanbul Havalimanı İç Mekan Kapsaması:</strong> Dünyanın en büyük terminal alanlarından birinde yolcular hareket ederken hücresel geçiş kopması yaşamadan kesintisiz 6G bağlantısı.",
            "<strong>Marmara Bölgesi Akıllı Sanayi Depoları:</strong> Otonom transpalet ve robotların hücre kenarında sinyal kaybetmeden tam senkronize çalışması."
        ],
        "references": [
            "H. Q. Ngo et al., 'Cell-Free Massive MIMO Versus Small Cells', IEEE Transactions on Wireless Communications, 2017.",
            "E. Björnson and L. Sanguinetti, 'Making Cell-Free Massive MIMO Competitive With MMSE Processing', IEEE Transactions on Wireless Communications, 2019.",
            "3GPP TR 38.800 Series: 'Evolution of Distributed MIMO for 6G'."
        ]
    },

    "thz": {
        "id": "thz",
        "title": "Terahertz (THz) İletişimi",
        "acronym": "THz İletişimi",
        "icon": "⚡",
        "trl": 3,
        "trl_desc": "Konsept Kanıtlama & Laboratuvar Deneyleri (TRL 3 - 0.1 THz - 10 THz Spektrumu)",
        "card_summary": "0.1 THz - 10 THz frekans bantlarında Terabit/saniye seviyesinde ultra hızlı kablosuz bant genişliği ve mikro-saniye gecikme sunar.",
        "highlights": ["⚡ 1 Tbps Rekor Hız", "⏱️ Sub-Milisaniye Gecikme", "🖥️ Kablosuz Veri Merkezi"],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>1 Cümlede Nedir?</strong><br>"
            "THz İletişimi, radyo dalgaları ile kızılötesi ışık arasındaki ultra yüksek frekans bandını (100 GHz - 10 THz) kullanarak <strong style='color: #FFFFFF;'>saniyede 1 Terabit (1000 Gbps)</strong> hızında ışık hızında veri aktarımı sağlayan teknolojidir.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Basit Analoji:</strong><br>"
            "4G bir köy yolu, 5G geniş bir otoban ise, Terahertz iletişimi adeta bir <strong style='color: #FFFFFF;'>ışınlanma tüpüdür</strong>. Çok büyük veri hacimlerini (örneğin tüm bir 8K filmi saniyenin yüzde birinde) iletebilir."
        ),
        "working_principle": (
            "<strong style='color: #00E5FF;'>Sub-THz ve THz Spektrum Fiziği:</strong><br>"
            "THz bantları (0.1 THz ila 10 THz), elektromanyetik spektrumda mmWave (Milimetrik Dalga) ile Optik/Kızılötesi frekanslar arasında yer alır.<br><br>"
            "1. <strong style='color: #FFFFFF;'>Ultra Geniş Bant Genişliği (B > 10-50 GHz):</strong> Frekans arttıkça kullanılabilir bant genişliği devasa boyuta ulaşır.<br>"
            "2. <strong style='color: #FFFFFF;'>Moleküler Emilim Kaybı (Absorption Loss):</strong> THz dalgaları havadaki su buharı ve moleküller tarafından emilir. Bu nedenle özel 'spektral pencereler' kullanılır.<br>"
            "3. <strong style='color: #FFFFFF;'>Ultra Dar Hüzmeleme:</strong> Sinyal kaybını telafi etmek için binlerce mikroskobik anten elemanından oluşan son derece dar hüzmeler kullanılır."
        ),
        "system_architecture": (
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>1. Yarı İletken ve RF Ön Uç Donanımı (GaN / InP / Graphene Transceivers):</strong><br>"
            "• Galyum Nitrür (GaN), İndiyum Fosfiti (InP) veya Grafen tabanlı THz tranzistör ve amplifikatör devreleri.<br>"
            "• Çip üstü anten dizileri (Antenna-on-Chip / Antenna-in-Package - AiP) ile birkaç milimetrelik küçük paket yapısı.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>2. Yüksek Hızlı Örnekleme ve Modülasyon (Sub-THz Ultra-DSP):</strong><br>"
            "• Saniyede 100+ Giga-örnekleme yapabilen ultra hızlı ADC/DAC dönüştürücü entegreler.<br>"
            "• DSSS ve yüksek dereceli QAM modülasyonları ile terabit mertebesinde veri işleme kapasitesi.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>3. Ultra Kısa Menzil ve Veri Merkezi İletim Mimarisi:</strong><br>"
            "• Veri merkezlerinde sunucular arası kablosuz mesh bağlantıları ve kuleler arası ultra-backhaul hatları.<br>"
            "• 3GPP Sub-THz (100-300 GHz) standartlaşma spesifikasyonları ile entegre çalışır."
        ),
        "mathematical_foundation": (
            "THz Kanal Sönümlenmesi ve Moleküler Emilim Denklem Modeli:\n"
            "$$L(f, d) = L_{fs}(f, d) \\cdot L_{abs}(f, d) = \\left( \\frac{4\\pi f d}{c} \\right)^2 \\cdot e^{K(f)d}$$\n\n"
            "Bant Genişliği ve Shannon Kapasitesi:\n"
            "$$C = B \\log_2 \\left( 1 + \\frac{P_t G_t G_r}{L(f,d) N_0 B} \\right), \\quad B \\approx 50 \\text{ GHz}$$"
        ),
        "use_cases": [
            "Kablosuz Veri Merkezi (Data Center) Sunucu-Sunucu Arası Terabit Bağlantı",
            "Holografik İletişim (Hologram Teleportation) & 3D Gerçek Zamanlı VR/AR",
            "Kısa Menzilli Ultra Hızlı Kablosuz Geri Bağlantı (Wireless Backhaul/Fronthaul)",
            "Tıbbi Nanosensör Ağları (Vücut İçi Terahertz İletişim)",
            "Gelişmiş Malzeme ve Kimyasal Algılama (THz Spektroskopi)"
        ],
        "advantages": [
            "Terabit/sn Seviyesinde Rekor Veri Transfer Hızı (100 Gbps - 1 Tbps)",
            "Ultra Düşük Gecikme Süresi (Sub-millisecond / Microsecond seviyesi)",
            "Yüksek Güvenlik (Çok dar hüzme nedeniyle dinlenmesi/hacklenmesi imkansız)",
            "Devasa Spektrum Kaynağı (Frekans sıkışıklığı yaşanmaz)"
        ],
        "disadvantages": [
            "Kısa Menzil (Yüksek Atmosferik & Moleküler Emilim Kaybı nedeniyle genellikle < 100-500 metre)",
            "Fiziksel Engellere Karşı Aşırı Hassasiyet (Bir yaprak veya insan eli bile sinyali kesebilir)",
            "RF Donanım Üretim Zorluğu ve Yüksek Yarı İletken Maliyeti"
        ],
        "global_research": [
            "IEEE 802.15.3d Terahertz Standardisation Group",
            "ITU-R WRC (World Radiocommunication Conference) Spectrum Allocations",
            "DARPA (USA) & Max Planck Institute THz Research Programs",
            "Samsung 6G White Paper & Sub-THz (140 GHz) Field Test Demos"
        ],
        "tt_scenarios": [
            "<strong>Türk Telekom Veri Merkezleri Raflar Arası THz Mesh:</strong> Ankara ve İstanbul veri merkezlerinde sunucu rafları arasındaki binlerce fiber kabloyu kaldırıp 1 Tbps THz kablosuz bağlantı kurma.",
            "<strong>Türk Telekom 6G Kuleler Arası Ultra-Backhaul:</strong> Fiber çekmenin çok zor veya maliyetli olduğu dağlık/zorlu arazilerde kuleler arası Terabit kablosuz fiber köprü.",
            "<strong>Yüksek Çözünürlüklü Holografik Sunumlar:</strong> Türk Telekom teknoloji merkezlerinde 8K canlı holografik konferans ve iletişim."
        ],
        "references": [
            "I. F. Akyildiz et al., 'Terahertz communication tools for 6G: Challenges and opportunities', IEEE Communications Magazine, 2022.",
            "K. Riklinen et al., 'Sub-THz Wireless Communications for 6G', IEEE Wireless Communications, 2021.",
            "3GPP TR 38.807: 'Study on Sub-THz Spectrum and Propagation for 6G'."
        ]
    },

    "ai_ran": {
        "id": "ai_ran",
        "title": "Yapay Zeka Tabanlı Telsiz Erişim Ağı (AI-Native RAN)",
        "acronym": "AI-RAN",
        "icon": "🧠",
        "trl": 5,
        "trl_desc": "O-RAN RIC Denemeleri & Yapay Zeka Protokol Testleri (TRL 5 - AI-Native 6G)",
        "card_summary": "Fiziksel katmandan kaynak yönetimine kadar tüm telsiz erişim ağını yapay zeka ve derin öğrenme modelleriyle yerel olarak optimize eder.",
        "highlights": ["🧠 Yapay Zeka Tabanlı PHY", "📊 Dinamik Spektrum Tahsisi", "🌿 %60 Yeşil Şebeke"],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>1 Cümlede Nedir?</strong><br>"
            "AI-Native RAN, 6G telsiz erişim ağının (baz istasyonları ve radyo donanımları) sonradan eklenen bir yazılımla değil, en alt temel seviyeden itibaren <strong style='color: #FFFFFF;'>yapay zeka tarafından yönetilecek şekilde</strong> tasarlanmasıdır.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Basit Analoji:</strong><br>"
            "Klasik şebeke, sadece insan mühendislerin yazdığı katı kuralları uygulayan bir robot gibidir. AI-Native RAN ise trafiği ve kullanıcı davranışlarını izleyip kendi parametrelerini milisaniyeler içinde optimize eden <strong style='color: #FFFFFF;'>öğrenen otonom bir pilot</strong> gibidir."
        ),
        "working_principle": (
            "<strong style='color: #00E5FF;'>Uçtan Uca Derin Öğrenmeli Radyo Mimarisi:</strong><br>"
            "AI-Native RAN, geleneksel 3GPP protokol katmanlarını (PHY/MAC/RLC/PDCP) derin yapay zeka modelleri (Deep Learning, Reinforcement Learning, Transformer) ile ikame eder.<br><br>"
            "1. <strong style='color: #FFFFFF;'>Derin Öğrenmeli Fiziksel Katman (Deep PHY Autoencoder):</strong> Modülasyon ve kodlama algoritmaları sabit matematiksel formüller yerine Derin Otokodlayıcılar (Autoencoders) ile uçtan uca öğrenilir.<br>"
            "2. <strong style='color: #FFFFFF;'>O-RAN RIC (RAN Intelligent Controller):</strong> Gerçek zamanlı (Near-RT ve Non-RT) RIC birimleri, xApps ve rApps yapay zeka uygulamaları ile radyo kaynaklarını (RRM) dinamik yönetir.<br>"
            "3. <strong style='color: #FFFFFF;'>Akıllı Derin Uyku (Deep Sleep Mode):</strong> Trafik olmadığı anlarda baz istasyonu parçalarını milisaniyelik hassasiyetle uyutarak devasa enerji tasarrufu sağlar."
        ),
        "system_architecture": (
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>1. Derin Otokodlayıcı Fiziksel Katman (Neural Air Interface PHY):</strong><br>"
            "• Sinyal işleme adımları (modülasyon, kanal kodlama, kestirim) Yapay Sinir Ağları (ANN) tarafından yürütülür.<br>"
            "• Değişen kanal koşullarına göre anlık adapte olan nöral modülasyon desenleri üretilir.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>2. Open RAN Akıllı Kontrolör Mimarisi (Near-RT & Non-RT RIC):</strong><br>"
            "• Near-RT RIC (10ms döngü zamanı) üzerinde çalışan xApps ile milisaniyelik hüzme yönetimi ve handover kararları.<br>"
            "• Non-RT RIC (100ms+ döngü) üzerinde çalışan rApps ile uzun vadeli trafik tahmini ve şebeke enerji optimizasyonu.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>3. Donanım ve Hızlandırıcı Katmanı (AI-Accelerated RAN Hardware):</strong><br>"
            "• Baz istasyonlarında (gNB) yerleşik NVIDIA, Qualcomm veya yerli NPU/GPU hızlandırıcı yongalar kullanılır.<br>"
            "• AI-RAN Alliance standartlarına uygun olarak operatör bağımsız akıllı altyapı sunulur."
        ),
        "mathematical_foundation": (
            "Otokodlayıcı (Autoencoder) Uçtan Uca Kayıp Fonksiyonu (Loss Function):\n"
            "$$\\mathcal{L}(\\theta, \\phi) = \\mathbb{E}_{x, n} \\left[ || s - f_D(f_E(s; \\theta) + n; \\phi)||^2 \\right]$$\n\n"
            "Pekiştirmeli Öğrenme (Reinforcement Learning) Q-Learning Radyo Kaynak Tahsisi:\n"
            "$$Q(s, a) \\leftarrow Q(s, a) + \\alpha \\left[ r + \\gamma \\max_{a'} Q(s', a') - Q(s, a) \\right]$$"
        ),
        "use_cases": [
            "Dinamik Spektrum Paylaşımı (Dynamic Spectrum Sharing - DSS) ve Otonom Frekans Tahsisi",
            "Kestirimci Bakım ve Ağ Arıza Önleme (Predictive Self-Healing Network)",
            "Kullanıcı Yoğunluğuna Göre Akıllı Güç Tasarrufu & Yeşil Baz İstasyonları",
            "Saniye Altı Hüzme Yönetimi (Beam Management) ve Hücre Yönetimi"
        ],
        "advantages": [
            "Maksimum Enerji Verimliliği (%50-%70 Enerji Tasarrufu)",
            "Sıfır İnsan Müdahalesi ile Otonom Ağ Yönetimi (Zero-Touch Network - ZTN)",
            "Kanal Şartlarına Göre İdeal Modülasyonu Anlık Öğrenme",
            "O-RAN Entegrasyonu ile Operatör Bağımsız Altyapı Esnekliği"
        ],
        "disadvantages": [
            "Yapay Zeka Modellerinin Kara Kutu (Black Box) Olması ve Açıklanabilirlik Zorluğu",
            "Yüksek NPU/GPU Donanım Maliyeti ve Enerji Tüketimi",
            "Model Eğitimi İçin Devasa Veri Toplama Gereksinimi"
        ],
        "global_research": [
            "AI-RAN Alliance (NVIDIA, SoftBank, Ericsson, Nokia Kurucu Üyeliği)",
            "O-RAN Alliance Working Group 2 & Working Group 10 (AI/ML Workflow)",
            "3GPP Release-18 Study on AI/ML for NR Air Interface",
            "NVIDIA Aerial 6G SDK & Deep Learning RAN Testbeds"
        ],
        "tt_scenarios": [
            "<strong>Türk Telekom Yeşil Şebeke (Green Network) İnisiyatifi:</strong> Gece saatlerinde trafiğin düştüğü kulelerde AI-RAN derin uyku modu ile yılda gigawatt-saat mertebesinde elektrik tasarrufu.",
            "<strong>Süper Lig Maç Günleri Dinamik Akıllı Trafik Yönetimi:</strong> Maç saatinde stadyum çevresindeki kulelerin kaynaklarını yapay zeka ile milisaniyeler içinde taraftarlara otomatik kaydırma.",
            "<strong>Türk Telekom Şebekesi Kestirimci Arıza Önleme:</strong> Baz istasyonundaki donanım bozulmalarını arıza yaşanmadan saatler önce tespit edip yedek sisteme geçiş."
        ],
        "references": [
            "T. O’Shea and J. Hoydis, 'An Introduction to Deep Learning for the Physical Layer', IEEE Transactions on Cognitive Communications and Networking, 2017.",
            "AI-RAN Alliance Whitepaper: 'Transforming Telecom with AI-Native Radio Access Networks', 2024.",
            "3GPP TR 38.843: 'Study on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface'."
        ]
    },

    "ntn": {
        "id": "ntn",
        "title": "Karasal Olmayan Ağlar (NTN - Uydu Entegrasyonu)",
        "acronym": "NTN Uyduları",
        "icon": "🛰️",
        "trl": 6,
        "trl_desc": "3GPP Rel-17/18 Standartlaşması & Ticari Uydu Denemeleri (TRL 6 - Uydu Entegrasyonu)",
        "card_summary": "LEO/GEO uydularını ve HAPS platformlarını karasal 6G şebekesiyle entegre ederek doğrudan akıllı telefonlara küresel kesintisiz kapsama sağlar.",
        "highlights": ["🛰️ Direct-to-Cell Uydular", "🌍 %100 Küresel Kapsama", "🆘 Afet Dayanıklılığı"],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>1 Cümlede Nedir?</strong><br>"
            "NTN (Karasal Olmayan Ağlar), alçak irtifa uyduları (LEO), zeplinler ve insansız hava araçlarını (HAPS) karasal baz istasyonlarıyla tek bir ağda birleştirerek <strong style='color: #FFFFFF;'>dünyanın her noktasında kesintisiz 6G kapsama</strong> sağlayan teknolojidir.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Basit Analoji:</strong><br>"
            "Karasal şebeke sadece şehirlerde ve yollarda olan sokak lambaları gibidir. NTN ise tüm dünyayı yukarıdan aydınlatan <strong style='color: #FFFFFF;'>uzaydaki devasa bir projektördür</strong>; okyanusun ortasında da olsanız dağın başında da olsanız sinyal kopmaz."
        ),
        "working_principle": (
            "<strong style='color: #00E5FF;'>Uzay-Hava-Kara Entegre Mimari:</strong><br>"
            "NTN, uyduları (özellikle 500-1200 km irtifadaki LEO uydularını) doğrudan standart akıllı telefonlara (Direct-to-Cell) bağlayan 3GPP Rel-17/18/19 mimarisidir.<br><br>"
            "1. <strong style='color: #FFFFFF;'>Doğrudan Cihaza Uydu İletişimi (Direct-to-Cell):</strong> Özel uydu telefonu gerektirmeden standart 6G modem çipe sahip telefonlar LEO uydusuna bağlanır.<br>"
            "2. <strong style='color: #FFFFFF;'>Yüksek Doppler ve Gecikme Telafisi:</strong> Uydular saatte 27.000 km hızla hareket ettiği için oluşan devasa Doppler kayması ve gecikme fiziki katmanda düzeltilir.<br>"
            "3. <strong style='color: #FFFFFF;'>Rejenere Uydu Yükü (Regenerative Payload):</strong> Uydular üzerinde 6G gNB baz istasyonu yazılımı çalıştırarak veriyi doğrudan uzayda işler."
        ),
        "system_architecture": (
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>1. Uzay ve Hava Segmen donanımları (LEO/GEO & HAPS):</strong><br>"
            "• Alçak Dünya Yörüngesi (LEO - 500-1200 km) uyduları ve stratosferik zeplin/HAPS (20 km) platformları.<br>"
            "• Uydular arası lazer iletişim bağlantıları (ISL - Inter-Satellite Laser Links) ile uzay içi veri yönlendirme.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>2. Karasal Yer İstasyonları ve Fiber Gateway (Ground Stations):</strong><br>"
            "• Uydulardan gelen yüksek frekanslı Feeder Link sinyallerini toplayan Türk Telekom Karasal Yer İstasyonları.<br>"
            "• Karasal 6G Çekirdek Şebekesine (5GC/6GC) yüksek hızlı optik fiber bağlantısı.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>3. Standart Kullanıcı Cihazı Katmanı (Unmodified Direct-to-Cell UEs):</strong><br>"
            "• Özel anten veya büyük çanak gerektirmeden doğrudan cep telefonları ile iletişim kuran 3GPP Rel-17/18 NTN protokol seti.<br>"
            "• Kırsal alanlar, denizcilik ve havacılık için kesintisiz küresel erişim."
        ),
        "mathematical_foundation": (
            "LEO Uydusu Doppler Kayması Formülü:\n"
            "$$f_d = f_c \\cdot \\frac{v_{sat}}{c} \\cos(\\theta(t))$$\n\n"
            "Serbest Uzay Yol Kaybı (Free Space Path Loss - FSPL):\n"
            "$$FSPL = \\left( \\frac{4\\pi d f}{c} \\right)^2, \\quad d \\approx 600 - 1000 \\text{ km}$$"
        ),
        "use_cases": [
            "Okyanuslar, Denizler ve Uluslararası Gemi Rotalarında Kesintisiz İletişim",
            "Havacılık & Yolcu Uçaklarında 6G İnternet Hizmeti",
            "Deprem, Tsunami ve Doğal Afetlerde Karasal Kuleler Çökse Dahi Kesintisiz Acil Çağrı",
            "Kutuplar, Çöller ve Dağlık Arazilerde Madencilik ve Tarım IoT Takibi"
        ],
        "advantages": [
            "Coğrafi Kısıtlama Olmaksızın %100 Küresel Kapsama (Zero Coverage Gap)",
            "Afet Anlarında Karasal Altyapıdan Tamamen Bağımsız Çalışabilme",
            "Kırsal Bölgelere Fiber Çekme Maliyetini Ortadan Kaldırma",
            "Standart Akıllı Telefonlar İle Doğrudan Bağlantı İmkanı"
        ],
        "disadvantages": [
            "Karasal Ağlara Göre Daha Yüksek Gecikme Süresi (LEO için 10-30 ms)",
            "Hızlı Hareket Eden Uydular Nedeniyle Sık Sinyal Devri (Fast Handover)",
            "Uydu Fırlatma ve Yörünge Bakım Maliyetleri"
        ],
        "global_research": [
            "3GPP Release-17/18/19 NTN Enhancements Work Item",
            "Starlink (SpaceX) Direct to Cell Initiative & T-Mobile Ortaklığı",
            "AST SpaceMobile & Vodafone / AT&T Uydudan Doğrudan Telefon Testleri",
            "ESA (European Space Agency) 6G Space Component Initiative"
        ],
        "tt_scenarios": [
            "<strong>Türk Telekom Afet Dayanıklı Acil İletişim Şebekesi:</strong> Deprem anında karasal kuleler veya fiber hatlar zarar görse dahi tüm abonelerin LEO uyduları üzerinden AFAD ve yakınlarıyla kesintisiz haberleşmesi.",
            "<strong>Marmara ve Karadeniz Balıkçı / Gemi Filoları:</strong> Türk Telekom SIM kartlı cihazların açık denizde uydu üzerinden tam kapsamada kalması.",
            "<strong>Doğu ve Güneydoğu Anadolu Dağlık Kırsal Kapsama:</strong> Kule dikilmesi coğrafi olarak imkansız mezra ve dağ yollarında %100 kapsama."
        ],
        "references": [
            "3GPP TR 38.811: 'Study on New Radio (NR) to support non-terrestrial networks'.",
            "S. Cioni et al., 'Non-Terrestrial Networks in 6G: A Survey on Key Enablers and Open Challenges', IEEE Communications Surveys & Tutorials, 2023.",
            "AST SpaceMobile White Paper: 'Cellular Broadband Directly to Unmodified Smartphones from Space'."
        ]
    },

    "ambient_iot": {
        "id": "ambient_iot",
        "title": "Pilsiz Nesnelerin İnterneti (Ambient IoT)",
        "acronym": "Pilsiz IoT",
        "icon": "🔋",
        "trl": 4,
        "trl_desc": "3GPP Rel-19 Study Item & Pilsiz Etiket PoC (TRL 4 - Pilsiz Nesnelerin İnterneti)",
        "card_summary": "Çevredeki radyo frekanslarından (RF) enerji devşirerek pil gerektirmeden çalışan trilyonlarca ultra ucuz sensörü 6G ağına bağlar.",
        "highlights": ["🔋 Pilsiz Çalışma", "📦 RF Enerji Hasadı", "🌐 Trilyon Sensör Ölçeği"],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>1 Cümlede Nedir?</strong><br>"
            "Ambient IoT, içerisinde <strong style='color: #FFFFFF;'>hiçbir pil veya batarya bulunmayan</strong>, ihtiyaç duyduğu elektriği havadaki radyo dalgalarından (RF Energy Harvesting) elde ederek çalışan ultra ucuz akıllı etiketler teknolojisidir.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Basit Analoji:</strong><br>"
            "Eski radyo etiketleri pasiftir. Ambient IoT etiketleri ise küçük bir güneş paneli gibi havadaki Wi-Fi ve 6G sinyallerini emerek <strong style='color: #FFFFFF;'>kendi enerjisini üreten pilsiz minik akıllı sensörler</strong> gibidir."
        ),
        "working_principle": (
            "<strong style='color: #00E5FF;'>Enerji Hasadı ve Geri Saçılım İletişimi:</strong><br>"
            "Ambient IoT, ortamdaki elektromanyetik dalgaları (RF Sinyalleri) doğrultucu devresi (Rectenna) ile doğru akıma (DC) dönüştürerek çalışır.<br><br>"
            "1. <strong style='color: #FFFFFF;'>RF Enerji Hasadı (Energy Harvesting):</strong> Baz istasyonunun yaydığı mikro-watt seviyesindeki RF gücü toplanır ve kapasitörde depolanır.<br>"
            "2. <strong style='color: #FFFFFF;'>Geri Saçılım Modülasyonu (Backscatter):</strong> Etiket kendi vericisini çalıştırmaz; gelen RF dalgasının anten empedansını değiştirerek dalgayı yansıtır.<br>"
            "3. <strong style='color: #FFFFFF;'>Sıfır Batarya (Zero-Battery):</strong> Batarya değişimi veya şarj gereksinimi tamamen ortadan kalkar."
        ),
        "system_architecture": (
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>1. Pilsiz Etiket Donanımı (Ambient Tag & Rectenna):</strong><br>"
            "• Bataryasız ultra düşük güçlü ASIC entegre devre ve mikro-kapasitör birimi.<br>"
            "• RF dalgalarını doğru akım elektriğe çeviren yüksek verimli Doğrultucu Anten (Rectenna).<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>2. Enerji Sağlayıcı ve Okuyucu Düğümler (Power Nodes & Readers):</strong><br>"
            "• Etiketleri beslemek için sürekli ortama RF sinyali yayan 6G baz istasyonları veya yardımcı enerji vericileri.<br>"
            "• Yansıyan son derece zayıf modüle dalgaları tespit eden yüksek hassasiyetli 6G Okuyucu (Reader) anten dizileri.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>3. 3GPP Rel-19 Şebeke ve Yazılım Katmanı (3GPP Ambient IoT Specs):</strong><br>"
            "• 3GPP Release-19 kapsamında standartlaştırılan trilyon nesne destekli adresleme ve MAC katman protokolleri.<br>"
            "• Türk Telekom IoT Bulut platformuna doğrudan güvenli sensör veri akışı."
        ),
        "mathematical_foundation": (
            "RF Enerji Hasadı Alınan Güç Denklem Modeli:\n"
            "$$P_{rec} = P_{tx} G_{tx} G_{rx} \\left( \\frac{\\lambda}{4\\pi d} \\right)^2 \\eta_{rectenna}$$\n\n"
            "Geri Saçılım (Backscatter) Sinyal Modeli:\n"
            "$$y(t) = \\alpha \\cdot x(t) \\cdot b(t) + n(t)$$"
        ),
        "use_cases": [
            "Tedarik Zinciri, Lojistik ve Depo Otomasyonunda Trilyonlarca Pilsiz Ürün Takibi",
            "Akıllı Tarım & Toprak Nem / Sıcaklık Sensörleri (Toprağa gömülü pilsiz sensörler)",
            "Gıda ve İlaç Soğuk Hava Deposu Sıcaklık Takibi",
            "Akıllı Binalar, Duvar İçi Beton Nem ve Çatlak Takibi Sensörleri"
        ],
        "advantages": [
            "Sıfır Batarya Maliyeti ve Batarya Değiştirme İşçiliğinin Yok Olması",
            "Çevre Dostu Sıfır Atık (Batarya kimyasal atık kirliliği yaşanmaz)",
            "1 Sentin Altında Ultra Düşük Üretim Maliyeti",
            "Sınırsız Kullanım Ömrü (Batarya ömrüyle sınırlı değildir)"
        ],
        "disadvantages": [
            "Ultra Düşük Güç Nedeniyle Kısa İletişim Menzili (< 10-50 metre)",
            "Çok Düşük Veri Hızı (Kbps seviyesinde basit sensör verisi)",
            "Ortamdaki RF Enerji Yoğunluğuna Bağımlılık"
        ],
        "global_research": [
            "3GPP Release-19 Study on Ambient IoT for NR",
            "IEEE RFID & IEEE Wireless Communications Ambient Backscatter Special Issues",
            "EU Zero-Power IoT Research Consortium",
            "Wiliot & Qualcomm Battery-Free Smart Tag Demos"
        ],
        "tt_scenarios": [
            "<strong>Türk Telekom Lojistik ve Depo Dijital Dönüşümü:</strong> Türk Telekom'un binlerce tedarikçi ürününün ve saha teçhizatının bataryasız etiketlerle 10 yıl boyunca bakım yapmaksızın takibi.",
            "<strong>Türkiye Akıllı Tarım / Sera Entegrasyonu:</strong> Tarım arazilerine serpilen pilsiz 6G nem sensörleri ile Türk Telekom IoT platformu üzerinden sulama otomasyonu.",
            "<strong>Akıllı Şehir Sayaç Takibi:</strong> Su, doğalgaz ve elektrik sayaçlarının bataryasız Ambient IoT etiketleriyle otomatik okunması."
        ],
        "references": [
            "3GPP TR 38.848: 'Study on Ambient IoT in GERAN / NR'.",
            "V. Liu et al., 'Ambient backscatter: wireless communication out of thin air', ACM SIGCOMM, 2013.",
            "Wiliot Whitepaper: 'Battery-Free Ambient IoT: Connecting Trillions of Everyday Things'."
        ]
    }
}
