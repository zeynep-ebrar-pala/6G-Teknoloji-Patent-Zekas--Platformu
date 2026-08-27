"""
Türk Telekom 6G Technology & Patent Intelligence Platform
Module 1: 6G Technologies Comprehensive Knowledge Base
Dual-Depth: Temel (kavramsal) beginner_copy.py + Uzman (denklem/karşılaştırma) expert_depth.py
Pazarlama sayıları hedef/literatürdür; saha ölçümü değildir.
"""

TECHNOLOGIES = {
    "isac": {
        "id": "isac",
        "title": "Entegre Algılama ve İletişim (ISAC)",
        "acronym": "ISAC",
        "icon": "📡",
        "trl": 4,
        "trl_desc": "3GPP Rel-19 çalışma kalemi (TR 22.837). Laboratuvar doğrulaması; TT şebekesinde ölçülmedi.",
        "card_summary": "Kule çevreyi ölçmez; ISAC aynı RF zincirinde bit ve yankıyı işler.",
        "beginner_one_liner": "Aynı taşıyıcı hem veri taşır hem yankıdan mesafe/hız çıkarır; ayrı radar kutusu değildir.",
        "highlights": ["Yankıdan mesafe", "Doppler'den hız", "TRL 4, saha değil"],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Problem</strong><br>"
            "Klasik gNB yalnızca haberleşme kanalını optimize eder. Kamera sis ve karanlıkta düşer; "
            "ayrı radar ikinci spektrum ve EMI üretir.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Yöntem</strong><br>"
            "ISAC (Integrated Sensing and Communication), aynı taşıyıcı, anten ve çoğu zaman aynı dalga şeklinde "
            "hem kullanıcı verisini hem yansıyan enerjiden mesafe, hız ve açı çıkarımını birlikte tasarlar. "
            "Yanına radar kutusu eklemek değildir.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Sınır</strong><br>"
            "Güç ve zaman aynı bütçeden bölünür; eko R⁴ ile zayıflar. Santimetre hassasiyeti literatür hedefidir. "
            "TRL 4 — Rel-19 (TR 22.837); laboratuvar doğrulaması. Türk Telekom şebekesinde henüz kullanılmamaktadır."
        ),
        "beginner_principle": (
            "1. gNB, kullanıcı çerçevesini basar; ayrı radar donanımı yoktur.<br>"
            "2. Gecikme mesafe, Doppler hız, dizi faz farkı AoA verir.<br>"
            "3. Bit ile yankı zaman/frekans/kodda paylaşılır. Aynı güç bütçesi iki görevi besler."
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
            {
                "title": "Otonom Araçlar & V2X Trafik Güvenliği",
                "description": "Baz istasyonu hem veri taşır hem yankı işler; sis ve kör noktada araç kinematiği adayıdır. Santimetre iddiası bu platformda ölçülmedi."
            },
            {
                "title": "Alçak İrtifa İHA/Dron Trafik Yönetimi (UTM)",
                "description": "Alçak irtifa hedefin RCS'i küçüktür; mevcut kule geometrisi koridoru kesiyorsa ayrı UTM radarı yerine adaydır. Duvar arkası 'her zaman' iddiası değildir."
            },
            {
                "title": "Akıllı Şehir Trafik & Yaya Akışı Haritalama",
                "description": "Kamera kurulmadan baz istasyonu sinyalleriyle kavşaklardaki araç yoğunluğu ve yaya hareketliliği gerçek zamanlı haritalanır; akıllı trafik ışığı optimizasyonu beslenir."
            },
            {
                "title": "Endüstriyel Depo Otonom Robot (AGV) Navigasyonu",
                "description": "İç mekânda çok yollu eko harita zenginliği olabilir. LiDAR füzyonu olmadan milimetre rota abartıdır."
            },
            {
                "title": "Sağlık & Yaşlı Bakımı (Kamerasız İzleme)",
                "description": "Ev içinde RF algılama ile nefes ritmi, kalp atışı ve düşme olayları gizlilik ihlali yapmadan tespit edilir; acil durum otomatik bildirimi tetiklenir."
            },
        ],
        "advantages": [
            "Ayrı radar RF zinciri ve spektrum lisansı ödenmez; mevcut gNB geometrisi kullanılır",
            "Menzil çözünürlüğü bantla, açı çözünürlüğü dizi açıklığıyla ölçeklenir (literatür hedefi, saha garantisi değil)",
            "Optik sensörlerin sis-yağmur-gece zayıflığı RF'de daha hafiftir (frekansa bağlı)",
            "Aynı Hz hem bit hem eko taşır; spektral verim ödünleşme doğru yönetilirse artar"
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
            {
                "text": "F. Liu et al., 'Integrated Sensing and Communications: Toward Dual-Functional Wireless Networks for 6G and Beyond', IEEE Journal on Selected Areas in Communications, 2022.",
                "url": "https://doi.org/10.1109/jsac.2022.3156632"
            },
            {
                "text": "3GPP TR 22.837: 'Study on Integrated Sensing and Communication', Rel-19.",
                "url": "https://www.3gpp.org/DynaReport/22837.htm"
            },
            {
                "text": "Hexa-X-II Deliverable D3.2: 'Initial architectural enablers'.",
                "url": "https://hexa-x-ii.eu/wp-content/uploads/2023/11/Hexa-X-II_D3.2_v1.0.pdf"
            }
        ]
    },

    "ris": {
        "id": "ris",
        "title": "Yeniden Yapılandırılabilir Akıllı Yüzeyler (RIS)",
        "acronym": "RIS",
        "icon": "🪞",
        "trl": 5,
        "trl_desc": "ETSI RIS ISG ve 3GPP Rel-19/20 çalışma kalemi; operatör deneme aşaması. Türk Telekom şebekesinde henüz ölçülmemiştir.",
        "card_summary": "Dalga köşeyi dönmez; RIS cephedeki programlanabilir yansıtıcıdır.",
        "beginner_one_liner": "Eleman fazı θ_n hüzmeyi UE'ye çevirir; yüzey yüksek güçlü verici değildir.",
        "highlights": ["Faz kaydıran yüzey", "Aktif verici yok", "TRL 5, ticari dağıtım değil"],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Problem</strong><br>"
            "mmWave ve üzeri bantlarda LoS yoksa yol kopar veya hız düşer. Her kör noktaya kule CAPEX ve EMC yüküdür.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Yöntem</strong><br>"
            "RIS (Reconfigurable Intelligent Surface), PIN/varaktör elemanlarla gelen dalganın fazını 0–2π kaydıran "
            "programlanabilir yansıtıcıdır. İnternet üretmez; gNB yayınını hedeflenen UE'ye yönlendirir.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Sınır</strong><br>"
            "Çift yol kaybı vardır; kanal kestirilemezse kazanç düşer. '%90 enerji' literatür/hedeftir. "
            "TRL 5 — ETSI RIS ISG ve Rel-19/20; operatör deneme aşaması. Türk Telekom şebekesinde henüz ölçülmemiştir."
        ),
        "beginner_principle": (
            "1. Cepheye ince yansıtıcı asılır. Bu bir baz istasyonu değildir.<br>"
            "2. Elemanlar θ_n ile hüzmeyi UE cihazına çevirir.<br>"
            "3. gNB düşük bit hızlı kontrol hattından hedefi bildirir. Bedeli kanal kestirimi ve çift yol kaybıdır."
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
            {
                "title": "N-LoS Şehir İçi Bina Arası Kapsama",
                "description": "Binalar arası görüş hattı olmayan sokaklarda RIS yüzeyi sinyali hedef cihaza yansıtarak ek baz istasyonu kurmadan kesintisiz 6G bağlantısı sağlar."
            },
            {
                "title": "Tünel, Metro & Yeraltı Kapsama",
                "description": "Tünel kıvrımlarında sönümlenen sinyal, duvarlara monte edilen pasif RIS panelleriyle yönlendirilir; yolcu telefonları yeraltında kopmadan kalır."
            },
            {
                "title": "İç Mekan mmWave / THz Bağlantısı",
                "description": "Ofis ve fabrika içinde duvar yansımalarıyla mmWave sinyali hedef cihaza odaklanır; kablo çekmeden odalar arası gigabit hız sunulur."
            },
            {
                "title": "Yeşil Haberleşme (Green Communications)",
                "description": "Aktif güçlendirici gerektirmeyen pasif RIS, aktif baz istasyonu sayısını azaltarak hem enerji tüketimini hem karbon ayak izini düşürür."
            },
            {
                "title": "ISAC ile Konumlandırma Desteği",
                "description": "RIS yansıtıcı yüzeyi hem sinyal güçlendirir hem yansıma açısından cihaz konumunu hassaslaştırarak ISAC tabanlı iç mekan konum servislerini destekler."
            },
        ],
        "advantages": [
            "Aktif röleden düşük enerji adayıdır (yüzey yüksek güçlü RF zinciri taşımaz)",
            "Cephe/cam/tünel geometrisine asılabilir; yeni kule dikmeden kapsama deliği adayı",
            "Aktif radyasyon üretmez; gelen dalgayı yönlendirir (Maxwell iptal olmaz)",
            "Alt-6 GHz'den THz'e kadar yüzey tasarlanabilir; kanal kestirimi ayrı bedeldir"
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
            {
                "text": "Q. Wu and R. Zhang, 'Towards Smart and Reconfigurable Environment: Intelligent Reflecting Surface Aided Wireless Network', IEEE Communications Magazine, 2020.",
                "url": "https://doi.org/10.1109/mcom.001.1900107"
            },
            {
                "text": "C. Pan et al., 'Reconfigurable Intelligent Surfaces for 6G Systems: Principles, Applications, and Research Directions', IEEE Communications Magazine, 2021.",
                "url": "https://doi.org/10.1109/mcom.001.2001076"
            },
            {
                "text": "H. Liu et al., 'DRL-Based Joint Beamforming and Reflection Design for Secure RIS-Aided ISAC Systems', Telecommunication Systems, 2025.",
                "url": "https://doi.org/10.1007/s11235-025-01374-z"
            }
        ]
    },

    "cell_free": {
        "id": "cell_free",
        "title": "Hücresiz Masif MIMO (Cell-Free Massive MIMO)",
        "acronym": "Hücresiz MIMO",
        "icon": "📶",
        "trl": 4,
        "trl_desc": "3GPP Rel-19/20 dağıtık MIMO çalışma kalemi; literatür prototip/simülasyon. TT sahası ölçülmedi.",
        "card_summary": "Hücre kenarında SINR düşer; hücresiz MIMO kenarı tasarım nesnesi olmaktan çıkarır.",
        "beginner_one_liner": "Yayılmış AP'ler aynı frekansta ortak ön kodlama ile hizmet verir; bedel fronthaul'dur.",
        "highlights": ["Ortak ön kodlama", "Fronthaul bedeli", "TRL 4 stadyum adayı"],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Problem</strong><br>"
            "Hücre kenarında SINR düşer; handover kopma riski taşır. Tek makro + çok kullanıcı tribünün bir yanını tok bırakır.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Yöntem</strong><br>"
            "Hücresiz Massive MIMO, coğrafyaya yayılmış AP'lerin aynı frekansta, merkezi veya yarı-dağıtık işlemle "
            "birlikte hizmet verdiği mimaridir. Hücre sınırı tasarım olarak kalkar.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Sınır</strong><br>"
            "Fronthaul fiber ve senkron yoksa ortak hüzme yazılamaz. 5×–10× spektral kazanç literatür aralığıdır. "
            "TRL 4 — Rel-19/20 dağıtık MIMO; literatür prototipi. Türk Telekom şebekesinde henüz kullanılmamaktadır."
        ),
        "beginner_principle": (
            "1. AP'ler sık yerleştirilir; tek makro kuleye bel bağlanmaz.<br>"
            "2. UE aynı anda birkaç AP'ye bağlanır.<br>"
            "3. Fronthaul üzerindeki işlemci MMSE tipi ön kodlama uygular. Fatura fronthaul ve hesaptır."
        ),
        "working_principle": (
            "<strong style='color: #00E5FF;'>Dağıtık Koordinasyon ve Hücresiz Mimari:</strong><br>"
            "Geleneksel ağlarda kullanıcılar belirli bir hücresel sektöre (Cell) bağlıdır ve hücre kenarlarında (Cell Edge) parazit (Interference) artar.<br><br>"
            "1. <strong style='color: #FFFFFF;'>Dağıtık Erişim Noktaları (Distributed APs):</strong> Coğrafi olarak geniş alana dağıtılmış çok sayıda basit erişim noktası (AP), yüksek hızlı ön-bağlantı (Fronthaul) ile Merkezi İşleme Birimine (CPU) bağlanır.<br>"
            "2. <strong style='color: #FFFFFF;'>Ortak İşbirlikçi Ön Kodlama (Coordinated Precoding):</strong> Tüm AP'ler kullanıcıya aynı anda ve aynı frekansta hizmet verir. Hücre kenarı tasarım nesnesi olarak kalkar; senkron ve fronthaul yoksa kazanç tersine döner.<br>"
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
            "• Kenar bulut üzerinde MMSE ve Zero-Forcing ön kodlama matrislerini hesaplayan sunucu havuzu.<br>"
            "• Adil QoE hedefi literatürdür; terabit 'her kullanıcı' bu platformda ölçülmedi."
        ),
        "mathematical_foundation": (
            "Kullanıcı k için Sinyal-Gürültü ve Parazit Oranı (SINR):\n"
            "$$SINR_k = \\frac{\\left| \\sum_{m=1}^M \\mathbf{g}_{mk}^H \\mathbf{w}_{mk} \\right|^2}{\\sum_{j \\neq k} \\left| \\sum_{m=1}^M \\mathbf{g}_{mk}^H \\mathbf{w}_{mj} \\right|^2 + \\sigma^2}$$\n\n"
            "MMSE (Minimum Mean Square Error) Kanal Kestirimi ve Ortak Kapsama Formülasyonu."
        ),
        "use_cases": [
            {
                "title": "Stadyum & Konser Alanları",
                "description": "Yoğun tribünde yük tek makroya yığılmaz; ortak ön kodlama kenar parazitini işler. 'Eşit gigabit' saha garantisi değildir."
            },
            {
                "title": "Havaalanı & Tren Garı İç Mekan",
                "description": "Yolcu terminalinde hareket halindeyken handover kopması yaşanmaz; dağıtık erişim noktaları kullanıcıyı kesintisiz takip eder."
            },
            {
                "title": "Otonom Fabrika Robot Kontrolü",
                "description": "Endüstriyel robotlar hücre sınırında sinyal kaybetmeden milisaniye altı gecikmeyle senkronize çalışır; üretim hattı duruşları azalır."
            },
            {
                "title": "Şehir Merkezi Yoğun Bulvarlar",
                "description": "Kalabalık caddelerde tek dev kule yerine dağıtık mini antenler spektral verimliliği artırır ve kullanıcı başına adil bant genişliği sağlar."
            },
        ],
        "advantages": [
            "Hücre kenarı SINR çöküşü tasarım nesnesi olarak kalkar (uniform deneyim adayı)",
            "Spektral verim artışı literatürde raporlanır (5×–10× aralık; bu platformda ölçülmedi)",
            "Makro kule estetiği istenmeyen iç mekânda dağıtık AP adayı",
            "Klasik handover başarısızlığı ortak hizmetle azalır (fiber/senkron şart)"
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
            {
                "text": "S. Elhoushy et al., 'Cell-Free Massive MIMO: A Survey', IEEE Communications Surveys & Tutorials, 2022.",
                "url": "https://doi.org/10.1109/comst.2021.3123267"
            }
        ]
    },

    "thz": {
        "id": "thz",
        "title": "Terahertz (THz) İletişimi",
        "acronym": "THz İletişimi",
        "icon": "⚡",
        "trl": 3,
        "trl_desc": "3GPP TR 38.807 (NR beyond 52.6 GHz) + laboratuvar spektrum çalışmaları. Sokak şebekesi değil.",
        "card_summary": "Kablosuz boru dar kalabilir; THz bant açar, FSPL ve emilim menzili keser.",
        "beginner_one_liner": "Shannon'da kapasite önce B ile büyür; THz kısa hop ve görüş hattı ister.",
        "highlights": ["Bant büyür", "FSPL + emilim", "TRL 3, sokak değil"],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Problem</strong><br>"
            "Sub-6 GHz ve mmWave, veri merkezi içi mesh ve kule köprüsü için dar kalabilir. Fiber her geometriye gitmez.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Yöntem</strong><br>"
            "THz iletişimi, kabaca 0,1–10 THz diliminde onlarca GHz bant açma adayıdır. "
            "Shannon: C = B log₂(1+SNR); B birinci terimdir.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Sınır</strong><br>"
            "FSPL ve su buharı emilimi menzili keser. '1 Tbps her aboneye' pazarlamadır. "
            "TRL 3 — TR 38.807; laboratuvar. Saha şebekesinde kullanılmamaktadır. 6G yalnızca THz değildir."
        ),
        "beginner_principle": (
            "1. mmWave ile kızılötesi arasındaki spektrum açılır; B büyür.<br>"
            "2. Su buharı, duvar ve el FSPL'ye ek kayıp basar.<br>"
            "3. Dar hüzme kaybı telafi eder; menzil kısa kalır. Doğru geometri raf, salon, kule köprüsüdür."
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
            {
                "title": "Kablosuz Veri Merkezi (Terabit Backhaul)",
                "description": "Sunucu rafları arasındaki fiber kabloların yerine THz bağlantı kurularak veri merkezi içi trafik saniyede terabit hızında kablosuz taşınır."
            },
            {
                "title": "Holografik & 3D Gerçek Zamanlı VR/AR",
                "description": "Saniyede yüzlerce gigabit holografi/VR iddiası literatür hedefidir; bu platformda ölçülmedi. Kısa LoS hop şarttır."
            },
            {
                "title": "Kısa Menzil Kablosuz Backhaul / Fronthaul",
                "description": "Kuleler arası veya bina içi fiber çekimin zor olduğu noktalarda THz link devreye girerek yüksek kapasiteli geri bağlantı sağlar."
            },
            {
                "title": "Tıbbi Nanosensör Ağları",
                "description": "Vücut içi nanosensör araştırma ufkudur; Rel-19 ticari özellik değildir."
            },
            {
                "title": "THz Spektroskopi & Malzeme Algılama",
                "description": "Güvenlik taraması ve endüstriyel kalite kontrolünde THz dalgaları malzeme bileşimini iletişim dışı algılama modunda analiz eder."
            },
        ],
        "advantages": [
            "Yüksek B, Shannon'da kapasiteyi önce bantla büyütür (hedef mertebe literatürdür)",
            "Kısa hopta düşük gecikme adayı; URLLC vaadi sokak makrosu için geçerli değildir",
            "Dar hüzme dinlemeyi zorlaştırır; 'imkânsız' iddiası güvenlik garantisi değildir",
            "Spektrum sıkışıklığı Sub-6'ya göre rahattır; cihaz ve emilim bedeli ayrıdır"
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
            {
                "text": "I. F. Akyildiz et al., 'TeraHertz Band Communication: An Old Problem Revisited and Research Directions for the Next Decade', IEEE Transactions on Communications, 2022.",
                "url": "https://doi.org/10.1109/tcomm.2022.3171800"
            },
            {
                "text": "3GPP TR 38.807: 'Study on requirements for NR beyond 52.6 GHz'.",
                "url": "https://www.3gpp.org/DynaReport/38807.htm"
            }
        ]
    },

    "ai_ran": {
        "id": "ai_ran",
        "title": "Yapay Zeka Tabanlı Telsiz Erişim Ağı (AI-Native RAN)",
        "acronym": "AI-RAN",
        "icon": "🧠",
        "trl": 5,
        "trl_desc": "3GPP TR 38.843 (AI/ML for NR) ve O-RAN RIC deneme sınıfı. Insansız saha kanıtı yok; TT ölçmedi.",
        "card_summary": "Sabit RRM kuralı yetersiz kalır; AI-RAN ölçüm döngüsünde kaynak kaydırır.",
        "beginner_one_liner": "O-RAN RIC üzerindeki xApp/rApp ölçüme göre politika üretir; sohbet botu değildir.",
        "highlights": ["Ölçümle kaynak", "Sohbet botu değil", "TRL 5, insansız değil"],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Problem</strong><br>"
            "Sabit RRM tarife dolu stadyum ile boş geceyi aynı kurala bağlar. İnsan her saniye politika yazamaz.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Yöntem</strong><br>"
            "AI-native RAN, PHY/MAC ve kaynak yönetiminin bir kısmını öğrenilmiş modele alır. "
            "Bugün pratik giriş O-RAN RIC üzerindeki xApp/rApp'tir; hava arayüzünün tamamını sinir ağı yapmak araştırma ucudur.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Sınır</strong><br>"
            "'%50–70 enerji' ve 'sıfır insan' hedef/pazarlamadır. TRL 5 — TR 38.843 ve O-RAN RIC deneme sınıfı; "
            "insansız işletim için saha doğrulaması bulunmamaktadır."
        ),
        "beginner_principle": (
            "1. Yük, kanal, enerji, kopma ölçülür.<br>"
            "2. RIC üzerinde xApp/rApp politika üretir.<br>"
            "3. Sonuç izlenir; geri alma yolu tasarımın parçasıdır. Denetim kalkmaz."
        ),
        "working_principle": (
            "<strong style='color: #00E5FF;'>Öğrenen RRM ve (araştırma ucunda) nöral PHY:</strong><br>"
            "AI-native RAN, pratikte PHY/MAC'in tamamını silmez. Bugünkü giriş O-RAN RIC üzerindeki xApp/rApp ile "
            "kaynak yönetimidir. Hava arayüzünü otokodlayıcıyla ikame etmek araştırma ucudur (TR 38.843).<br><br>"
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
            {
                "title": "Dinamik Spektrum Paylaşımı (DSS)",
                "description": "AI modeli frekans kullanımını anlık trafik verisine göre optimize ederek boş spektrumu verimli paylaştırır ve paraziti azaltır."
            },
            {
                "title": "Kestirimci Bakım & Self-Healing Ağ",
                "description": "Makine öğrenmesi baz istasyonu donanım arızalarını oluşmadan saatler önce tespit eder ve otomatik yedek sisteme geçiş yapar."
            },
            {
                "title": "Akıllı Güç Tasarrufu (Deep Sleep)",
                "description": "Trafik düşük saatlerde AI-RAN gereksiz radyo birimlerini milisaniye hassasiyetinde uyutarak şebeke enerji tüketimini ciddi oranda düşürür."
            },
            {
                "title": "Saniye Altı Hüzme Yönetimi",
                "description": "Hareketli kullanıcılar için hüzme yönlendirme kararları insan müdahalesi olmadan saniyenin altında alınır; handover gecikmesi minimize edilir."
            },
        ],
        "advantages": [
            "Enerji hedefi ölçüm döngüsüyle izlenir; %50–70 tasarruf hedef/pazarlamadır",
            "Zero-touch iddiası araştırma ucudur; canlı şebekede geri alma ve denetim kalır",
            "Kanal değişince politika güncellenir; kara kutu düzenleyiciye açıklanmalıdır",
            "O-RAN arayüzü çok tedarikçili denemeyi mümkün kılar; O-RAN ≠ AI değildir"
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
            {
                "text": "3GPP TR 38.843: 'Study on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface'.",
                "url": "https://www.3gpp.org/DynaReport/38843.htm"
            }
        ]
    },

    "ntn": {
        "id": "ntn",
        "title": "Karasal Olmayan Ağlar (NTN - Uydu Entegrasyonu)",
        "acronym": "NTN Uyduları",
        "icon": "🛰️",
        "trl": 6,
        "trl_desc": "3GPP Rel-17 NTN şartnamesi (TR 38.811) ve Rel-17/18 iş kalemi; kamuya açık direct-to-cell denemeleri. Türk Telekom şebekesinde henüz ölçülmemiştir.",
        "card_summary": "Kule her yere yetişmez; NTN Rel-17+ ile LEO/HAPS hücresini çekirdeğe bağlar.",
        "beginner_one_liner": "Direct-to-cell: standart UE uydu hücresini görür; bedel gecikme ve Doppler'dir.",
        "highlights": ["Direct-to-cell", "Gecikme + Doppler", "TRL 6 tamamlayıcı"],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Problem</strong><br>"
            "Karasal gNB şehir ve asfaltı kapsar; dağ, deniz ve enkaz boş kalır. Kırsal CAPEX karasal modeli kırar.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Yöntem</strong><br>"
            "NTN, LEO/GEO/HAPS düğümlerini karasal çekirdeğe 3GPP Rel-17+ ile bağlar. "
            "Direct-to-cell: özel çanak yerine standart UE'nin uydu hücresini görmesi.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Sınır</strong><br>"
            "'%100 küresel sıfır boşluk' pazarlamadır. Şehir içi kapasite ve milisaniye altı URLLC için birincil yol değildir. "
            "TRL 6 — TR 38.811; kamuya açık denemeler. Rakip değil, tamamlayıcı."
        ),
        "beginner_principle": (
            "1. Şehir kulede kalır. Boş coğrafyada LEO / HAPS.<br>"
            "2. Hedef 3GPP UE'nin uydu hücresini görmesidir.<br>"
            "3. PHY Doppler ve gecikmeyi düzeltir; yer kulesi kadar düşük gecikme vaadi değildir."
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
            {
                "title": "Açık Deniz & Gemi İletişimi",
                "description": "Okyanus ortasında karasal kapsama olmadan LEO uydusu üzerinden standart telefonlarla kesintisiz veri ve ses iletişimi sağlanır."
            },
            {
                "title": "Havacılık Yolcu İnterneti",
                "description": "Uçuş sırasında NTN entegrasyonu sayesinde yolcular yüksek irtifada bile 6G hızında internete bağlanabilir."
            },
            {
                "title": "Afet Anında Acil İletişim",
                "description": "Deprem veya sel sonrası karasal kuleler devre dışı kalsa bile uydu bağlantısı acil arama ve koordinasyon hattını ayakta tutar."
            },
            {
                "title": "Kırsal & Dağlık Alan IoT Takibi",
                "description": "Fiber veya kule altyapısının ulaşmadığı tarım ve maden sahalarındaki sensörler NTN üzerinden merkeze veri iletir."
            },
        ],
        "advantages": [
            "Kule ekonomisinin işlemediği coğrafyada kapsama adayı (küresel '%100' pazarlamadır)",
            "Karasal site düştüğünde yedek yol senaryosu; saha garantisi değil",
            "Kırsal fiber çekme CAPEX'ini her mezrada ödememe adayı",
            "Rel-17+ direct-to-cell: standart UE hedefi; her eski cihaz garanti değildir"
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
            {
                "text": "M. Giordani and M. Zorzi, 'Non-Terrestrial Networks in the 6G Era: Challenges and Opportunities', IEEE Network, 2021.",
                "url": "https://doi.org/10.1109/mnet.011.2000493"
            },
            {
                "text": "F. Wang et al., 'Non-Terrestrial Networking for 6G: Evolution, Opportunities, and Future Directions', Engineering, 2025.",
                "url": "https://doi.org/10.1016/j.eng.2025.05.013"
            },
            {
                "text": "3GPP TR 38.811: 'Study on New Radio (NR) to support non-terrestrial networks'.",
                "url": "https://www.3gpp.org/DynaReport/38811.htm"
            }
        ]
    },

    "ambient_iot": {
        "id": "ambient_iot",
        "title": "Pilsiz Nesnelerin İnterneti (Ambient IoT)",
        "acronym": "Pilsiz IoT",
        "icon": "🔋",
        "trl": 4,
        "trl_desc": "3GPP Rel-19 çalışma kalemi (TR 38.848). Erken deneme aşaması. Türk Telekom şebekesinde henüz ölçülmemiştir.",
        "card_summary": "Pil lojistiği ölçeklenmez; Ambient IoT ortam RF'sinden backscatter kimlik bildirir.",
        "beginner_one_liner": "Rectenna hasadı × backscatter = kısa kimlik; video taşımaz, telefonun yerini almaz.",
        "highlights": ["Backscatter kimlik", "Video taşımaz", "TRL 4, ticari dağıtım değil"],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Problem</strong><br>"
            "Koli, sera ve sayaç ölçeğinde pil değiştirmek ekonomik değildir. NB-IoT ve RedCap hâlâ bir enerji kaynağı ister.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Yöntem</strong><br>"
            "Ambient IoT, pili olmayan veya çok küçük olan etiketlerin ortam RF'sinden enerji toplayıp "
            "çoğunlukla backscatter ile kısa durum mesajı verdiği IoT sınıfıdır.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Sınır</strong><br>"
            "Menzil kısa, bit hızı düşüktür. '1 sent, trilyon nesne' hedef/pazarlamadır. "
            "TRL 4 — TR 38.848; erken deneme aşaması. Türk Telekom şebekesinde henüz ölçülmemiştir."
        ),
        "beginner_principle": (
            "1. Rectenna RF kırıntısını DC'ye çevirir.<br>"
            "2. Kendi PA'sı yoktur; gelen taşıyıcı modüle edilir. Menzil kısadır.<br>"
            "3. Yakın okuyucu zayıf yankıyı ayırır. Video taşımaz."
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
            {
                "title": "Tedarik Zinciri & Lojistik Takibi",
                "description": "Pilsiz RFID benzeri etiketler palet ve koli üzerinde yıllarca pil değiştirmeden konum ve sıcaklık verisi iletir."
            },
            {
                "title": "Akıllı Tarım Sensörleri",
                "description": "Toprağa gömülü pilsiz nem sensörleri 6G ağından RF enerji alarak sulama sistemlerine otomatik veri sağlar."
            },
            {
                "title": "Gıda & İlaç Soğuk Zincir İzleme",
                "description": "Depo ve nakliye sıcaklığı pilsiz etiketlerle sürekli ölçülür; ihlal anında anlık alarm üretilir."
            },
            {
                "title": "Akıllı Bina & Yapı Sağlığı",
                "description": "Duvar ve beton içine gömülü pilsiz sensörler nem, çatlak ve titreşimi yıllarca bakım gerektirmeden raporlar."
            },
        ],
        "advantages": [
            "Pil değiştirme lojistiği kalkar (enerji ortam RF'sine bağlıdır, garanti değildir)",
            "Kimyasal pil atığı üretmez; RF zayıf köşede etiket susar",
            "Hedef maliyet düşük etikettir; '1 sent' pazarlama/hedeftir",
            "Pil ömrü sınırı yoktur; okunabilir bit Friis hasadına bağlıdır"
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
            {
                "text": "3GPP TR 38.848: 'Study on Ambient IoT (Internet of Things) in RAN'.",
                "url": "https://www.3gpp.org/DynaReport/38848.htm"
            }
        ]
    }
}
