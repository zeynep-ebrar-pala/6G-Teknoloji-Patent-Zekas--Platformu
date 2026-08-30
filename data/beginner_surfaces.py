"""
Temel mod — kullanım senaryoları, artı/eksi, araştırma ve TT örnekleri.
global_research ve tt_scenarios: {title, body} ile başlık + açıklama.
"""

BEGINNER_SURFACES = {
    "isac": {
        "trl_desc": (
            "Seviye 4: laboratuvarda doğrulandı. "
            "Türk Telekom şebekesinde henüz kullanılmıyor; bu sayfa hedef ve literatürü anlatır."
        ),
        "highlights": [
            "Aynı antenle veri ve algılama",
            "Kamera yerine radyo yankısı",
            "Seviye 4 — saha değil",
        ],
        "use_cases": [
            {
                "title": "Otonom araçlar ve trafik güvenliği",
                "description": (
                    "Baz istasyonu telefonunuza veri gönderirken çevreden dönen sinyalle "
                    "araçların uzaklığını ve hızını okuyabilir. Sis ve kör noktada kamera zayıflar; "
                    "bu yöntem adaydır. Santimetre hassasiyet burada ölçülmedi."
                ),
            },
            {
                "title": "Şehir içi dron koridoru",
                "description": (
                    "Alçak irtifada uçan dronları izlemek için ayrı radar ağı kurmak pahalıdır. "
                    "Mevcut kule geometrisi bu işe uygun olabilir. Her duvar arkasından görmek bir vaat değildir."
                ),
            },
            {
                "title": "Kavşak trafik yoğunluğu",
                "description": (
                    "Kamera kurmadan kavşaktaki araç sayısını tahmin etmek için sinyal yankıları "
                    "kullanılabilir. Akıllı trafik ışığı gibi uygulamalara veri sağlayabilir."
                ),
            },
            {
                "title": "Depo içi robot",
                "description": (
                    "İç mekânda çok yönlü yansıma vardır; rota planlaması zorlaşır. "
                    "Lazer sensör olmadan milimetre hassasiyet abartıdır."
                ),
            },
            {
                "title": "Kamerasız yaşlı bakımı",
                "description": (
                    "Ev içinde nefes ve düşme tespiti gizlilik tartışmalarını beraberinde getirir. "
                    "Ürün olarak henüz yaygın değildir."
                ),
            },
        ],
        "advantages": [
            "Yanına ayrı radar kutusu takmaya gerek kalmayabilir; mevcut kule kullanılır.",
            "Kamera sis ve karanlıkta zayıflar; radyo bu koşullarda daha dayanıklı olabilir.",
            "İkinci frekans lisansı ve ikinci anten maliyeti azalabilir.",
            "Aynı enerjiyle hem konuşma hem çevreyi dinleme hedeflenir.",
        ],
        "disadvantages": [
            "İletişim hızı ve algılama kalitesi aynı güçten paylaşılır; biri artarsa diğeri zayıflayabilir.",
            "Yoğun şehir yansımaları ölçümü zorlaştırır.",
            "Kişisel veri ve gizlilik kuralları çözülmeden kamusal izleme ürünü sayılmaz.",
        ],
        "global_research": [
            {
                "title": "Uluslararası standart çalışması (3GPP Release-19)",
                "body": (
                    "Dünyadaki operatörler ve üreticiler aynı dili konuşsun diye "
                    "entegre algılama standart gündemine girdi. Bu bir satış vaadi değil; "
                    "yol haritasının resmi adımıdır."
                ),
            },
            {
                "title": "Avrupa Hexa-X-II 6G programı",
                "body": (
                    "Avrupa'nın büyük 6G araştırma programı bu konuyu mimari raporlarında "
                    "ele alıyor. Laboratuvar ve simülasyon ağırlıklıdır."
                ),
            },
            {
                "title": "IEEE entegre algılama girişimi",
                "body": (
                    "Akademi ve endüstri bu alanda ortak çalışma grupları kurdu. "
                    "Amaç: iletişim ve algılamayı aynı radyo zincirinde birleştirmek."
                ),
            },
            {
                "title": "Üretici laboratuvar denemeleri",
                "body": (
                    "Büyük üreticiler test ortamlarında yüksek hız ve algılama birlikte "
                    "gösterilmeye çalışılıyor. 'Her kule radar' ticari ürün değildir; "
                    "laboratuvar iddiaları saha garantisi taşımaz."
                ),
            },
        ],
        "tt_scenarios": [
            {
                "title": "Boğaz ve Marmara'da sis altında deniz trafiği",
                "body": (
                    "Sis altında kamera işe yaramaz. Sahil baz istasyonları aynı sinyalle "
                    "gemilerin uzaklığını ve hızını okuyabilir. Senaryo araştırma aşamasındadır; "
                    "saha garantisi değildir."
                ),
            },
            {
                "title": "İstanbul ve Ankara'da dron koridoru güvenliği",
                "body": (
                    "Şehir içi teslimat dronları ve izinsiz dronlar için ayrı radar ağı "
                    "kurmak zordur. Mevcut kule geometrisi bu koridorlarda adaydır."
                ),
            },
            {
                "title": "Afet sonrası enkaz altında hareket arama",
                "body": (
                    "Deprem sonrası enkaz altında hareket aramak için kamera her yere giremez. "
                    "Radyo yankısı duvar arkası hareketi gösterebilir; gizlilik ve doğruluk "
                    "tartışmaları devam eder."
                ),
            },
        ],
    },
    "ris": {
        "trl_desc": (
            "Seviye 5: prototip ve deneme aşamasında. "
            "Türk Telekom şebekesinde henüz ölçülmedi."
        ),
        "highlights": [
            "Cepheye asılan yansıtıcı panel",
            "Kendi güçlü vericisi yok",
            "Seviye 5 — ticari dağıtım değil",
        ],
        "use_cases": [
            {
                "title": "Bina arası kapsama",
                "description": (
                    "Doğrudan görüş olmayan sokaklarda panel sinyali telefona yansıtır. "
                    "Her boşluğa yeni kule dikmek gerekmez."
                ),
            },
            {
                "title": "Tünel ve metro",
                "description": (
                    "Tünel kıvrımlarında zayıflayan sinyal duvar panelleriyle yönlendirilir. "
                    "Yer altında bağlantı kopması azalabilir."
                ),
            },
            {
                "title": "İç mekân yüksek frekans",
                "description": (
                    "Ofis ve fabrikada duvar yansımasıyla sinyal hedef cihaza odaklanır. "
                    "Her odaya kablo çekmek gerekmez."
                ),
            },
            {
                "title": "Düşük enerji kapsama",
                "description": (
                    "Aktif röle yerine pasif yüzey düşük enerjiyle boşluğu kapatmaya adaydır. "
                    "Kanal ölçümü ayrı iş gerektirir."
                ),
            },
            {
                "title": "ISAC ile konum desteği",
                "description": (
                    "Yansıma açısı iç mekân konumunu iyileştirebilir. "
                    "RIS tek başına radar değildir."
                ),
            },
        ],
        "advantages": [
            "Aktif röleden daha az enerji kullanabilir; yüzey kendi başına güçlü verici değildir.",
            "Cephe, cam ve tünele asılabilir; yeni kule şart olmayabilir.",
            "Kör noktaya kule dikmeden sinyal yönlendirilir.",
            "Düşük frekanstan yüksek frekansa yüzey tasarlanabilir.",
        ],
        "disadvantages": [
            "Kanal doğru ölçülmezse faz ayarı yanlış olur ve kazanç düşer.",
            "Sinyal önce panele, sonra telefona gider; iki kez yol kaybı vardır.",
            "Hızlı hareket eden kullanıcı için kontrol gecikmesi zorlayıcıdır.",
        ],
        "global_research": [
            {
                "title": "ETSI RIS endüstri grubu",
                "body": (
                    "Avrupa telekom standardı kuruluşu akıllı yüzeyler için ortak tanım "
                    "ve test yöntemleri geliştiriyor. Ürün değil, standart çalışmasıdır."
                ),
            },
            {
                "title": "IEEE akıllı yüzey çalışma grubu",
                "body": (
                    "Akademi ve endüstri yansıtıcı yüzeylerin şebekeye nasıl bağlanacağını "
                    "tartışıyor. Sahada her binada panel yoktur."
                ),
            },
            {
                "title": "Operatör saha denemeleri",
                "body": (
                    "Bazı operatörler cephe ve iç mekânda prototip paneller deniyor. "
                    "Tak-çalıştır ticari ürün henüz yaygın değildir."
                ),
            },
            {
                "title": "RISE-6G Avrupa projesi",
                "body": (
                    "Akıllı yüzeyleri 6G mimarisine bağlama araştırması. "
                    "Laboratuvar ve pilot saha ağırlıklıdır."
                ),
            },
        ],
        "tt_scenarios": [
            {
                "title": "Tarihi Yarımada dar sokak kapsaması",
                "body": (
                    "Yeni kule dikmek tarihi dokuya zarar verebilir. Cepheye ince panel "
                    "sinyali telefona yansıtır; prototip aşamasındadır."
                ),
            },
            {
                "title": "Avrasya Tüneli ve Marmaray",
                "body": (
                    "Tünel kıvrımlarında sinyal zayıflar. Duvara monte paneller yönlendirme "
                    "yapabilir; saha denemesi adayıdır."
                ),
            },
            {
                "title": "Plaza ve veri merkezi cam cepheleri",
                "body": (
                    "Yüksek frekansta cam ve iç mekân sorunları yaşanır. Şeffaf veya ince "
                    "kaplama iç kapsamayı iyileştirmeye adaydır."
                ),
            },
        ],
    },
    "cell_free": {
        "trl_desc": (
            "Seviye 4: laboratuvar prototipi. "
            "Türk Telekom şebekesinde henüz kullanılmıyor."
        ),
        "highlights": [
            "Birçok küçük anten birlikte",
            "Hücre kenarı zayıflaması azalır",
            "Seviye 4 — fiber bedeli var",
        ],
        "use_cases": [
            {
                "title": "Stadyum ve konser",
                "description": (
                    "Yoğun tribünde yük tek kuleye yığılmaz; birçok küçük anten birlikte hizmet verir. "
                    "Fiber bağlantı şarttır."
                ),
            },
            {
                "title": "Havalimanı ve tren garı",
                "description": (
                    "Yolcu terminalinde hareket halinde geçiş kopması azalabilir. "
                    "Dağıtık antenler takip eder."
                ),
            },
            {
                "title": "Fabrika robot kontrolü",
                "description": (
                    "Robotlar hücre kenarında sinyal kaybetmeden çalışmaya adaydır. "
                    "Merkezi işlem ve fiber altyapı gerekir."
                ),
            },
            {
                "title": "Yoğun şehir bulvarı",
                "description": (
                    "Tek dev kule yerine dağıtık antenler daha adil hız dağıtımına adaydır. "
                    "Kurulum maliyeti yüksektir."
                ),
            },
        ],
        "advantages": [
            "Hücre kenarı zayıflaması tasarım olarak azalır; kullanıcı birkaç antenin ortasında durur.",
            "Literatürde spektral verim artışı raporlanır; bu platformda ölçülmedi.",
            "Büyük makro kule estetiği istenmeyen iç mekânda uygun olabilir.",
            "Geçiş kopması birlikte hizmetle azalabilir.",
        ],
        "disadvantages": [
            "Tüm antenleri fiber ile bağlamak pahalıdır.",
            "Merkezi işlem yükü yüksektir.",
            "Seyrek kırsalda her direğe fiber maliyeti anlamsız olabilir.",
        ],
        "global_research": [
            {
                "title": "Linköping Üniversitesi çalışmaları",
                "body": (
                    "Hücresiz MIMO kavramının önde gelen akademik kaynağı. "
                    "Simülasyon ve laboratuvar ağırlıklıdır."
                ),
            },
            {
                "title": "IEEE özel yayın konuları",
                "body": (
                    "Dağıtık anten ve ortak ön kodlama literatürü hızla büyüyor. "
                    "Saha ölçümü sınırlıdır."
                ),
            },
            {
                "title": "3GPP dağıtık MIMO çalışma grupları",
                "body": (
                    "Standart kuruluşu dağıtık anten mimarisini gelecek sürümlerde "
                    "tartışıyor. Ticari ürün değildir."
                ),
            },
            {
                "title": "Ericsson ve Nokia laboratuvar gösterimleri",
                "body": (
                    "Üreticiler stadyum benzeri senaryolarda demo yapıyor. "
                    "Kent geneli dağıtım aşamasında değildir."
                ),
            },
        ],
        "tt_scenarios": [
            {
                "title": "RAMS Park yoğun tribün",
                "body": (
                    "On binlerce kişi aynı anda bağlandığında tek kule yetmeyebilir. "
                    "Dağıtık antenler yoğunluğu paylaştırmaya adaydır; fiber maliyeti vardır."
                ),
            },
            {
                "title": "İstanbul Havalimanı geniş terminal",
                "body": (
                    "Yolcular hareket ederken bağlantı kopması yaşanabilir. "
                    "Tavan ve kolonlara dağıtık anten senaryosu tartışılıyor."
                ),
            },
            {
                "title": "Akıllı depo ve üretim hatları",
                "body": (
                    "Otonom araçlar ve robotlar hücre kenarında zayıflayabilir. "
                    "Dağıtık anten bu ortamlarda adaydır."
                ),
            },
        ],
    },
    "thz": {
        "trl_desc": (
            "Seviye 3: laboratuvar kanıtı. "
            "Saha şebekesinde kullanılmıyor; 6G yalnızca THz değildir."
        ),
        "highlights": [
            "Çok geniş bant açılır",
            "Menzil kısalır",
            "Seviye 3 — sokak değil",
        ],
        "use_cases": [
            {
                "title": "Kablosuz veri merkezi",
                "description": (
                    "Sunucu rafları arasında fiber yerine kısa mesafe kablosuz bağlantı adayıdır. "
                    "Menzil onlarca metreyi geçmez."
                ),
            },
            {
                "title": "Holografik VR/AR",
                "description": (
                    "Çok yüksek hız iddiası literatür hedefidir; burada ölçülmedi. "
                    "Kısa mesafe ve doğrudan görüş şarttır."
                ),
            },
            {
                "title": "Kuleler arası kısa köprü",
                "description": (
                    "Fiber çekilemeyen noktalarda kuleler arası yüksek kapasiteli "
                    "kablosuz köprü adayıdır."
                ),
            },
            {
                "title": "Malzeme algılama",
                "description": (
                    "Güvenlik taraması ve kalite kontrolünde iletişim dışı algılama "
                    "modu kullanılabilir."
                ),
            },
        ],
        "advantages": [
            "Geniş bant kapasiteyi artırmaya adaydır.",
            "Kısa mesafede düşük gecikme hedeflenir.",
            "Dar hüzme dinlemeyi zorlaştırabilir.",
            "Alt frekanslara göre spektrum sıkışıklığı daha azdır.",
        ],
        "disadvantages": [
            "Menzil genelde yüzlerce metreyi geçmez.",
            "El, yaprak ve yağmur bağlantıyı keser.",
            "Donanım pahalıdır ve cep telefonu seviyesinde olgun değildir.",
        ],
        "global_research": [
            {
                "title": "IEEE terahertz standartlaşma grubu",
                "body": (
                    "Kısa mesafe ultra geniş bant için frekans ve protokol "
                    "tartışmaları yapılıyor."
                ),
            },
            {
                "title": "ITU-R spektrum tahsis çalışmaları",
                "body": (
                    "Uluslararası frekans tahsisi için bilimsel veri toplanıyor. "
                    "Abone telefonunda varsayılan bant değildir."
                ),
            },
            {
                "title": "DARPA ve Max Planck programları",
                "body": (
                    "Terahertz donanım ve kanal ölçümü araştırması. "
                    "Laboratuvar ağırlıklıdır."
                ),
            },
            {
                "title": "Samsung Sub-THz saha denemeleri",
                "body": (
                    "Üreticiler 140 GHz civarında demo yapıyor. "
                    "Açık şehir makrosu için tasarlanmadı."
                ),
            },
        ],
        "tt_scenarios": [
            {
                "title": "Veri merkezlerinde raf arası bağlantı",
                "body": (
                    "Binlerce fiber kablo yerine kısa mesafe kablosuz link düşünülüyor. "
                    "Laboratuvar ve pilot aşamasındadır."
                ),
            },
            {
                "title": "Zor coğrafyada kule köprüsü",
                "body": (
                    "Dağlık alanda fiber çekmek zor olduğunda kuleler arası kablosuz "
                    "köprü adayıdır. Menzil kısadır."
                ),
            },
            {
                "title": "Teknoloji merkezi sunum denemeleri",
                "body": (
                    "Yüksek çözünürlüklü canlı sunum ve holografik demo hedeflenir. "
                    "Günlük cep hızı senaryosu değildir."
                ),
            },
        ],
    },
    "ai_ran": {
        "trl_desc": (
            "Seviye 5: deneme aşamasında. "
            "İnsansız işletim için saha doğrulaması yok; insan denetimi kalkmaz."
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
                    "Yapay zekâ anlık trafiğe göre frekansı paylaştırır; parazit azalabilir. "
                    "Canlı şebekede geri alma prosedürü şarttır."
                ),
            },
            {
                "title": "Arıza önceden tahmin",
                "description": (
                    "Baz istasyonu arızası önceden gösterilebilir; yedek sisteme geçiş planlanır. "
                    "Veri kalitesi düşükse model yanıltır."
                ),
            },
            {
                "title": "Gece enerji tasarrufu",
                "description": (
                    "Trafiğin az olduğu saatlerde gereksiz radyo birimleri uyutulur. "
                    "Tasarruf vaatleri hedef veya pazarlamadır; burada ölçülmedi."
                ),
            },
            {
                "title": "Hızlı hüzme yönetimi",
                "description": (
                    "Hareketli kullanıcı için hüzme kararları otomatik alınır. "
                    "İnsan denetimi kalkmaz."
                ),
            },
        ],
        "advantages": [
            "Trafik değişince politika güncellenebilir; sabit kurala bağlı kalmaz.",
            "Enerji hedefi ölçüm döngüsüyle izlenebilir.",
            "Açık arayüz çok tedarikçili denemeyi kolaylaştırır.",
            "Arıza önceden görülebilir; bakım planlanabilir.",
        ],
        "disadvantages": [
            "Model kara kutu olabilir; düzenleyiciye açıklama zordur.",
            "İşlemci donanımı maliyet ve enerji yer.",
            "Eğitim için çok veri gerekir; veri yoksa model uydurur.",
        ],
        "global_research": [
            {
                "title": "AI-RAN Alliance",
                "body": (
                    "Üreticiler ve operatörler yapay zekâ destekli radyo ağını "
                    "ortak tanımlamaya çalışıyor. Deneme aşamasındadır."
                ),
            },
            {
                "title": "O-RAN yapay zekâ çalışma grupları",
                "body": (
                    "Açık radyo arayüzü üzerinde akıllı uygulamaların nasıl çalışacağı "
                    "yazılıyor. O-RAN yapay zekâ değildir; üzerinde uygulama çalışır."
                ),
            },
            {
                "title": "3GPP Release-18 yapay zekâ çalışması",
                "body": (
                    "Standart kuruluşu radyo arayüzünde makine öğrenmesini inceliyor. "
                    "Tam nöral hava arayüzü laboratuvar ucudur."
                ),
            },
            {
                "title": "NVIDIA derin öğrenme RAN testleri",
                "body": (
                    "GPU tabanlı test ortamlarında politika denemeleri yapılıyor. "
                    "Net enerji kazancı her saha için ölçülmelidir."
                ),
            },
        ],
        "tt_scenarios": [
            {
                "title": "Yeşil şebeke — gece enerji tasarrufu",
                "body": (
                    "Gece trafiği düşerken boş kuleler uyutulabilir. "
                    "Tasarruf hedefidir; saha faturası burada ölçülmedi."
                ),
            },
            {
                "title": "Maç günü dinamik kapasite",
                "body": (
                    "Stadyum çevresinde trafik patlar; kaynak otomatik kaydırılabilir. "
                    "İnsan denetimi ve geri alma yolu kalır."
                ),
            },
            {
                "title": "Kestirimci arıza önleme",
                "body": (
                    "Donanım arızası önceden görülüp yedek sisteme geçiş planlanabilir. "
                    "Yanlış alarm riski vardır."
                ),
            },
        ],
    },
    "ntn": {
        "trl_desc": (
            "Seviye 6: kamuya açık denemeler var. "
            "Şehir kulesinin yerine geçmez; boş coğrafyayı tamamlar."
        ),
        "highlights": [
            "Telefondan uydu bağlantısı",
            "Gecikme daha uzun",
            "Seviye 6 — tamamlayıcı",
        ],
        "use_cases": [
            {
                "title": "Açık deniz ve gemi",
                "description": (
                    "Okyanusta karasal kapsama yokken uydu üzerinden standart telefonla "
                    "iletişim adayıdır. Hız karasal kuleye göre düşük olabilir."
                ),
            },
            {
                "title": "Uçak içi internet",
                "description": (
                    "Yüksek irtifada uydu bağlantısıyla internet sağlanabilir. "
                    "Gecikme konuşmayı zorlayabilir."
                ),
            },
            {
                "title": "Afet acil iletişim",
                "description": (
                    "Deprem sonrası kuleler devre dışı kalsa bile uydu acil hat için "
                    "yedek yol olabilir. Garanti değil, senaryodur."
                ),
            },
            {
                "title": "Kırsal sensör takibi",
                "description": (
                    "Kule ve fiber ulaşmayan tarım ve maden sahalarında sensör verisi "
                    "uydu üzerinden iletilebilir."
                ),
            },
        ],
        "advantages": [
            "Kule ekonomisi işlemediği dağ, deniz ve kırsalda kapsama adayıdır.",
            "Karasal site düştüğünde yedek yol senaryosu sunar.",
            "Her mezrada fiber çekmek zorunda kalmayabilir.",
            "Aynı abonelik numarasıyla boşluğu kapatma hedeflenir.",
        ],
        "disadvantages": [
            "Karasal ağa göre gecikme daha uzundur.",
            "Uydu hızlı hareket eder; sık geçiş gerekir.",
            "Uydu fırlatma ve bakım maliyeti yüksektir.",
        ],
        "global_research": [
            {
                "title": "3GPP Release-17/18/19 NTN geliştirmeleri",
                "body": (
                    "Standart telefonun uydu hücresini görmesi için kurallar yazılıyor. "
                    "Her eski telefon otomatik uyumlu değildir."
                ),
            },
            {
                "title": "Starlink Direct to Cell",
                "body": (
                    "Alçak yörünge uydu ile doğrudan cep telefonu denemeleri kamuya açık "
                    "yapılıyor. Türkiye sahası ölçümü bu platformda yok."
                ),
            },
            {
                "title": "AST SpaceMobile saha testleri",
                "body": (
                    "Uydu üzerinden doğrudan telefon bağlantısı test ediliyor. "
                    "Kapasite ve gecikme karasal kuleyle aynı değildir."
                ),
            },
            {
                "title": "ESA 6G uzay bileşeni",
                "body": (
                    "Avrupa uzay ajansı 6G ile uydu entegrasyonunu araştırıyor. "
                    "Afet ve kırsal senaryolar öne çıkar."
                ),
            },
        ],
        "tt_scenarios": [
            {
                "title": "Afet dayanıklı acil iletişim",
                "body": (
                    "Depremde kule ve fiber zarar görebilir. Uydu acil SMS ve ses için "
                    "yedek yol olabilir; gecikme karasalden uzundur."
                ),
            },
            {
                "title": "Balıkçı ve gemi filoları",
                "body": (
                    "Açık denizde karasal kapsama yoktur. Aynı SIM ile uydu üzerinden "
                    "iletişim hedeflenir; hız sınırlı olabilir."
                ),
            },
            {
                "title": "Dağlık kırsal kapsama",
                "body": (
                    "Kule dikmek zor veya pahalı mezralarda uydu hücresi boşluğu "
                    "kapatmaya adaydır. '%100 sıfır boşluk' pazarlamadır."
                ),
            },
        ],
    },
    "ambient_iot": {
        "trl_desc": (
            "Seviye 4: laboratuvarda doğrulandı. "
            "Ticari şebeke dağıtımında değil; telefonun yerini almaz."
        ),
        "highlights": [
            "Pilsiz küçük etiket",
            "Geri saçılım kimlik",
            "Seviye 4 — video taşımaz",
        ],
        "use_cases": [
            {
                "title": "Lojistik ve palet takibi",
                "description": (
                    "Pilsiz etiket palet ve kolide yıllarca pil değiştirmeden "
                    "konum ve sıcaklık bildirebilir. Menzil kısadır."
                ),
            },
            {
                "title": "Akıllı tarım",
                "description": (
                    "Toprağa gömülü pilsiz nem sensörü ortam radyosundan enerji alarak "
                    "veri gönderebilir. Radyo zayıf bölgede susar."
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
            "Pil değiştirme lojistiği kalkar; ortam enerjisine bağlıdır.",
            "Kimyasal pil atığı üretmez.",
            "Hedef maliyet düşük etikettir; '1 sent' pazarlamadır.",
            "Video ve ses taşımaz; kimlik ve sıcaklık gibi kısa mesajlar için uygundur.",
        ],
        "disadvantages": [
            "İletişim menzili kısadır; onlarca metre mertebesinde.",
            "Veri hızı düşüktür.",
            "Ortam radyo gücü zayıfsa etiket çalışmaz.",
        ],
        "global_research": [
            {
                "title": "3GPP Release-19 Ambient IoT çalışması",
                "body": (
                    "Pilsiz etiketlerin hücresel ağda nasıl okunacağı standart "
                    "gündemine girdi. Ticari raf ürünü değildir."
                ),
            },
            {
                "title": "IEEE geri saçılım yayınları",
                "body": (
                    "Akademi enerji toplama ve geri saçılım iletişimini inceliyor. "
                    "Menzil ve güvenilirlik sınırlıdır."
                ),
            },
            {
                "title": "Avrupa sıfır güç IoT konsorsiyumu",
                "body": (
                    "Trilyon nesne hedefi araştırma ufkudur; lojistik ölçeğinde "
                    "pil değiştirmek ekonomik değildir."
                ),
            },
            {
                "title": "Wiliot ve Qualcomm pilsiz etiket demoları",
                "body": (
                    "Ticari pilot etiketler depo ve mağazada deneniyor. "
                    "Hücresel çoklu okuyucu senaryosu ayrı çalışma konusudur."
                ),
            },
        ],
        "tt_scenarios": [
            {
                "title": "Depo ve lojistik merkezi palet takibi",
                "body": (
                    "Binlerce paletin pilini değiştirmek mümkün değildir. "
                    "Pilsiz etiket 'nerede, kaç derece' sorularını yanıtlamaya adaydır."
                ),
            },
            {
                "title": "Akıllı tarım ve sera izleme",
                "body": (
                    "Sera ve tarlada nem ve sıcaklık pilsiz sensörle izlenebilir. "
                    "Kapsama alanı sınırlıdır."
                ),
            },
            {
                "title": "Soğuk zincir ve ilaç lojistiği",
                "body": (
                    "Sıcaklık ihlali anında alarm üretilebilir. "
                    "Telefon veya kamera yerine geçmez; etiket sınırlı veri taşır."
                ),
            },
        ],
    },
}
