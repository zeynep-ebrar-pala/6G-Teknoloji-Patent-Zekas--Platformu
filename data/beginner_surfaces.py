"""
Temel mod — kullanım senaryoları, artı/eksi, araştırma ve TT örnekleri.
technologies.py uzman metinlerini değiştirmez; Temel modda bunlarla değiştirilir.
"""

BEGINNER_SURFACES = {
    "isac": {
        "trl_desc": (
            "Hazırlık seviyesi 4: laboratuvarda doğrulandı. "
            "Türk Telekom şebekesinde henüz kullanılmıyor."
        ),
        "highlights": [
            "Yankıdan mesafe okur",
            "Frekans kaymasından hız",
            "Seviye 4 — saha değil",
        ],
        "use_cases": [
            {
                "title": "Otonom araçlar ve trafik güvenliği",
                "description": (
                    "Baz istasyonu hem veri gönderir hem yankı dinler. "
                    "Siste ve kör noktada araç konumu için adaydır. "
                    "Santimetre hassasiyet burada ölçülmedi."
                ),
            },
            {
                "title": "Düşük irtifa dron koridoru",
                "description": (
                    "Alçak irtifada uçan dronları izlemek için ayrı radar yerine "
                    "mevcut kule geometrisi aday olabilir. "
                    "Her duvar arkasından görmek bir vaat değildir."
                ),
            },
            {
                "title": "Akıllı şehir trafik haritası",
                "description": (
                    "Kamera kurmadan kavşaktaki araç yoğunluğunu "
                    "sinyal yankılarıyla tahmin etmek mümkün olabilir."
                ),
            },
            {
                "title": "Depo içi otonom robot",
                "description": (
                    "İç mekânda çok yönlü yansıma olabilir. "
                    "Lazer sensör olmadan milimetre hassasiyetli rota abartıdır."
                ),
            },
            {
                "title": "Kamerasız yaşlı bakımı",
                "description": (
                    "Ev içinde nefes ve düşme tespiti gizlilik tartışmalarını "
                    "beraberinde getirir; ürün olarak henüz yaygın değildir."
                ),
            },
        ],
        "advantages": [
            "Ayrı radar altyapısı ve ikinci frekans lisansı gerekmez",
            "Kamera sis ve karanlıkta zayıflar; radyo bu koşullarda daha dayanıklı olabilir",
            "Mevcut kule geometrisi kullanılabilir",
            "Aynı frekansta hem veri hem algılama hedeflenir",
        ],
        "disadvantages": [
            "İletişim hızı ile algılama kalitesi aynı güçten paylaşılır",
            "Yoğun şehir yansımaları ölçümü zorlaştırır",
            "Kişisel veri ve gizlilik kuralları çözülmelidir",
        ],
        "global_research": [
            "3GPP Release-19 entegre algılama çalışma kalemi",
            "Avrupa Hexa-X-II 6G araştırma programı",
            "IEEE entegre algılama girişimi",
            "Büyük üreticilerin laboratuvar denemeleri",
        ],
        "tt_scenarios": [
            "Boğaz ve Marmara'da sis altında deniz trafiği izleme",
            "İstanbul ve Ankara'da şehir içi dron koridoru güvenliği",
            "Afet sonrası enkaz altında hareket arama senaryosu",
        ],
    },
    "ris": {
        "trl_desc": (
            "Hazırlık seviyesi 5: prototip ve deneme aşamasında. "
            "Türk Telekom şebekesinde henüz ölçülmedi."
        ),
        "highlights": [
            "Faz ayarlı yansıtıcı yüzey",
            "Kendi vericisi yok",
            "Seviye 5 — ticari dağıtım değil",
        ],
        "use_cases": [
            {
                "title": "Bina arası kapsama",
                "description": (
                    "Doğrudan görüş olmayan sokaklarda panel sinyali telefona yansıtır; "
                    "her boşluğa yeni kule dikmek gerekmez."
                ),
            },
            {
                "title": "Tünel ve metro",
                "description": (
                    "Tünel kıvrımlarında zayıflayan sinyal duvar panelleriyle "
                    "yönlendirilir; yer altında bağlantı kopması azalabilir."
                ),
            },
            {
                "title": "İç mekân yüksek frekans",
                "description": (
                    "Ofis ve fabrikada duvar yansımasıyla sinyal hedef cihaza odaklanır; "
                    "her odaya kablo çekmek gerekmez."
                ),
            },
            {
                "title": "Düşük enerji kapsama",
                "description": (
                    "Aktif röle yerine pasif yüzey düşük enerjiyle kapsama boşluğunu "
                    "kapatmaya adaydır; kanal ölçümü ayrı iş gerektirir."
                ),
            },
            {
                "title": "ISAC ile konum desteği",
                "description": (
                    "Yansıma açısı iç mekân konumunu iyileştirebilir; "
                    "RIS tek başına radar değildir."
                ),
            },
        ],
        "advantages": [
            "Aktif röleden daha az enerji kullanabilir",
            "Cephe, cam ve tünele asılabilir",
            "Yeni kule dikmeden kapsama boşluğu kapatılabilir",
            "Düşük frekanstan yüksek frekansa yüzey tasarlanabilir",
        ],
        "disadvantages": [
            "Kanal ölçümü zordur; pasif parçalar alıcı değildir",
            "Sinyal iki kez yol kaybı yaşar (kule → panel → telefon)",
            "Hızlı hareket eden kullanıcı için faz ayarı zorlayıcıdır",
        ],
        "global_research": [
            "ETSI RIS endüstri grubu",
            "IEEE akıllı yüzey çalışma grubu",
            "Üretici saha denemeleri",
            "RISE-6G Avrupa projesi",
        ],
        "tt_scenarios": [
            "Tarihi Yarımada: kule dikmeden dar sokak kapsaması",
            "Avrasya Tüneli ve Marmaray: tünel içi kesintisiz bağlantı",
            "Plaza ve veri merkezi cam cephelerinde iç mekân kapsaması",
        ],
    },
    "cell_free": {
        "trl_desc": (
            "Hazırlık seviyesi 4: laboratuvar prototipi. "
            "Türk Telekom şebekesinde henüz kullanılmıyor."
        ),
        "highlights": [
            "Birlikte ön kodlama",
            "Fiber bağlantı bedeli",
            "Seviye 4 — stadyum adayı",
        ],
        "use_cases": [
            {
                "title": "Stadyum ve konser",
                "description": (
                    "Yoğun tribünde yük tek kuleye yığılmaz; "
                    "birçok küçük anten birlikte hizmet verir."
                ),
            },
            {
                "title": "Havalimanı ve tren garı",
                "description": (
                    "Yolcu terminalinde hareket halinde geçiş kopması "
                    "azalabilir; dağıtık antenler takip eder."
                ),
            },
            {
                "title": "Fabrika robot kontrolü",
                "description": (
                    "Endüstriyel robotlar hücre kenarında sinyal kaybetmeden "
                    "çalışmaya adaydır; fiber altyapı şarttır."
                ),
            },
            {
                "title": "Yoğun şehir bulvarı",
                "description": (
                    "Kalabalık caddede tek dev kule yerine dağıtık antenler "
                    "daha adil hız dağıtımına adaydır."
                ),
            },
        ],
        "advantages": [
            "Hücre kenarı zayıflaması tasarım olarak azalır",
            "Literatürde spektral verim artışı raporlanır; burada ölçülmedi",
            "İç mekânda büyük kule estetiği gerekmez",
            "Geçiş kopması birlikte hizmetle azalabilir",
        ],
        "disadvantages": [
            "Tüm antenleri fiber ile bağlamak pahalıdır",
            "Merkezi işlem yükü yüksektir",
            "Fiber altyapı maliyeti büyüktür",
        ],
        "global_research": [
            "Linköping Üniversitesi hücresiz MIMO çalışmaları",
            "IEEE özel yayın konuları",
            "3GPP dağıtık MIMO çalışma grupları",
            "Ericsson ve Nokia laboratuvar gösterimleri",
        ],
        "tt_scenarios": [
            "RAMS Park: 50.000 kişilik yoğun tribün senaryosu",
            "İstanbul Havalimanı: geniş terminal iç kapsaması",
            "Marmara bölgesi akıllı depo ve robot hatları",
        ],
    },
    "thz": {
        "trl_desc": (
            "Hazırlık seviyesi 3: laboratuvar kanıtı. "
            "Saha şebekesinde kullanılmıyor."
        ),
        "highlights": [
            "Geniş bant açılır",
            "Menzil kısalır",
            "Seviye 3 — sokak değil",
        ],
        "use_cases": [
            {
                "title": "Kablosuz veri merkezi",
                "description": (
                    "Sunucu rafları arasında fiber yerine kısa mesafe "
                    "kablosuz bağlantı adayıdır; menzil kısadır."
                ),
            },
            {
                "title": "Holografik VR/AR",
                "description": (
                    "Çok yüksek hız iddiası literatür hedefidir; "
                    "burada ölçülmedi. Kısa mesafe ve doğrudan görüş şarttır."
                ),
            },
            {
                "title": "Kısa mesafe kule bağlantısı",
                "description": (
                    "Fiber çekilemeyen noktalarda kuleler arası "
                    "yüksek kapasiteli kablosuz köprü adayıdır."
                ),
            },
            {
                "title": "Tıbbi nanosensör",
                "description": (
                    "Vücut içi sensör araştırma ufkudur; "
                    "ticari özellik değildir."
                ),
            },
            {
                "title": "Malzeme algılama",
                "description": (
                    "Güvenlik taraması ve kalite kontrolünde "
                    "iletişim dışı algılama modu kullanılabilir."
                ),
            },
        ],
        "advantages": [
            "Geniş bant kapasiteyi artırmaya adaydır",
            "Kısa mesafede düşük gecikme hedeflenir",
            "Dar hüzme dinlemeyi zorlaştırabilir",
            "Frekans sıkışıklığı alt frekanslara göre rahattır",
        ],
        "disadvantages": [
            "Menzil genelde yüzlerce metreyi geçmez",
            "El, yaprak ve yağmur bağlantıyı keser",
            "Donanım pahalı ve olgun değildir",
        ],
        "global_research": [
            "IEEE terahertz standartlaşma grubu",
            "ITU-R spektrum tahsis çalışmaları",
            "DARPA ve Max Planck THz programları",
            "Samsung Sub-THz saha denemeleri",
        ],
        "tt_scenarios": [
            "Veri merkezlerinde raf arası kablosuz mesh",
            "Fiber zor coğrafyada kuleler arası kablosuz köprü",
            "Teknoloji merkezlerinde yüksek çözünürlüklü sunum denemeleri",
        ],
    },
    "ai_ran": {
        "trl_desc": (
            "Hazırlık seviyesi 5: deneme aşamasında. "
            "İnsansız işletim için saha doğrulaması yok."
        ),
        "highlights": [
            "Ölçümle kaynak kaydırma",
            "Sohbet botu değil",
            "Seviye 5 — denetim kalır",
        ],
        "use_cases": [
            {
                "title": "Dinamik frekans paylaşımı",
                "description": (
                    "Yapay zekâ anlık trafiğe göre frekansı paylaştırır; "
                    "parazit azalabilir."
                ),
            },
            {
                "title": "Arıza önceden tahmin",
                "description": (
                    "Makine öğrenmesi baz istasyonu arızasını önceden "
                    "gösterebilir; yedek sisteme geçiş planlanır."
                ),
            },
            {
                "title": "Akıllı uyku modu",
                "description": (
                    "Trafiğin az olduğu saatlerde gereksiz radyo birimleri "
                    "uyutulur; enerji tasarrufu hedeflenir."
                ),
            },
            {
                "title": "Hızlı hüzme yönetimi",
                "description": (
                    "Hareketli kullanıcı için hüzme kararları otomatik alınır; "
                    "insan denetimi kalkmaz."
                ),
            },
        ],
        "advantages": [
            "Enerji hedefi ölçüm döngüsüyle izlenebilir",
            "Otomatik yönetim iddiası araştırma aşamasındadır",
            "Kanal değişince politika güncellenebilir",
            "Açık arayüz çok tedarikçili denemeyi kolaylaştırır",
        ],
        "disadvantages": [
            "Model kara kutu olabilir; açıklama zordur",
            "İşlemci donanımı maliyet ve enerji yer",
            "Eğitim için çok veri gerekir",
        ],
        "global_research": [
            "AI-RAN Alliance",
            "O-RAN yapay zekâ çalışma grupları",
            "3GPP Release-18 yapay zekâ çalışması",
            "NVIDIA ve derin öğrenme RAN test ortamları",
        ],
        "tt_scenarios": [
            "Yeşil şebeke: gece saatlerinde enerji tasarrufu",
            "Süper Lig maç günü dinamik kapasite kaydırma",
            "Kestirimci arıza önleme ve yedek geçiş",
        ],
    },
    "ntn": {
        "trl_desc": (
            "Hazırlık seviyesi 6: kamuya açık denemeler var. "
            "Şehir kulesinin tamamlayıcısıdır."
        ),
        "highlights": [
            "Telefondan uydu",
            "Gecikme daha uzun",
            "Seviye 6 — tamamlayıcı",
        ],
        "use_cases": [
            {
                "title": "Açık deniz ve gemi",
                "description": (
                    "Okyanusta karasal kapsama yokken uydu üzerinden "
                    "standart telefonla iletişim adayıdır."
                ),
            },
            {
                "title": "Uçak içi internet",
                "description": (
                    "Yüksek irtifada uydu bağlantısıyla internet "
                    "sağlanabilir; hız karasal kuleye göre düşük olabilir."
                ),
            },
            {
                "title": "Afet acil iletişim",
                "description": (
                    "Deprem sonrası kuleler devre dışı kalsa bile "
                    "uydu acil hat için yedek yol olabilir."
                ),
            },
            {
                "title": "Kırsal IoT takibi",
                "description": (
                    "Kule ve fiber ulaşmayan tarım ve maden sahalarında "
                    "sensör verisi uydu üzerinden iletilebilir."
                ),
            },
        ],
        "advantages": [
            "Kule ekonomisi işlemediği coğrafyada kapsama adayıdır",
            "Karasal site düştüğünde yedek yol senaryosu sunar",
            "Her mezrada fiber çekmek zorunda kalmayabilir",
            "Standart telefon hedefi; her eski cihaz garanti değildir",
        ],
        "disadvantages": [
            "Karasal ağa göre gecikme daha uzundur",
            "Uydu hızlı hareket eder; sık geçiş gerekir",
            "Uydu fırlatma ve bakım maliyeti yüksektir",
        ],
        "global_research": [
            "3GPP Release-17/18/19 NTN geliştirmeleri",
            "Starlink Direct to Cell girişimi",
            "AST SpaceMobile saha testleri",
            "ESA 6G uzay bileşeni girişimi",
        ],
        "tt_scenarios": [
            "Afet dayanıklı acil iletişim şebekesi",
            "Marmara ve Karadeniz balıkçı ve gemi filoları",
            "Doğu ve Güneydoğu kırsal ve dağlık kapsama",
        ],
    },
    "ambient_iot": {
        "trl_desc": (
            "Hazırlık seviyesi 4: laboratuvarda doğrulandı. "
            "Ticari şebeke dağıtımında değil."
        ),
        "highlights": [
            "Geri saçılım kimlik",
            "Video taşımaz",
            "Seviye 4 — ticari değil",
        ],
        "use_cases": [
            {
                "title": "Lojistik ve tedarik zinciri",
                "description": (
                    "Pilsiz etiket palet ve kolide yıllarca pil değiştirmeden "
                    "konum ve sıcaklık bildirebilir."
                ),
            },
            {
                "title": "Akıllı tarım",
                "description": (
                    "Toprağa gömülü pilsiz nem sensörü ortam radyosundan "
                    "enerji alarak veri gönderebilir."
                ),
            },
            {
                "title": "Soğuk zincir izleme",
                "description": (
                    "Depo ve nakliye sıcaklığı pilsiz etiketle izlenir; "
                    "ihlal anında alarm üretilebilir."
                ),
            },
            {
                "title": "Yapı sağlığı",
                "description": (
                    "Duvar ve betona gömülü pilsiz sensör nem ve titreşimi "
                    "uzun süre bakım gerektirmeden raporlayabilir."
                ),
            },
        ],
        "advantages": [
            "Pil değiştirme lojistiği kalkar; ortam enerjisine bağlıdır",
            "Kimyasal pil atığı üretmez",
            "Hedef maliyet düşük etikettir",
            "Pil ömrü sınırı yoktur; menzil kısadır",
        ],
        "disadvantages": [
            "İletişim menzili kısadır (onlarca metre)",
            "Veri hızı düşüktür; video taşımaz",
            "Ortam radyo gücüne bağımlıdır",
        ],
        "global_research": [
            "3GPP Release-19 Ambient IoT çalışması",
            "IEEE geri saçılım özel yayınları",
            "Avrupa sıfır güç IoT konsorsiyumu",
            "Wiliot ve Qualcomm pilsiz etiket demoları",
        ],
        "tt_scenarios": [
            "Depo ve lojistik merkezlerinde palet takibi",
            "Akıllı tarım ve sera izleme",
            "Soğuk zincir ve ilaç lojistiği",
        ],
    },
}
