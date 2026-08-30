"""
Temel mod — kullanım senaryoları, artı/eksi, araştırma ve coğrafi örnekler.
global_research ve tt_scenarios: {title, body} — başlık sorunu, gövde açıklaması.
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
                "title": "Standart kuruluşu: iletişim ve algılama birlikte tanımlanıyor",
                "body": (
                    "3GPP Release-19 kapsamında dünya operatörleri ve üreticileri, "
                    "aynı antenle hem konuşma hem çevre algılamasının kurallarını yazmaya başladı. "
                    "Bu, yakında satışa çıkacak ürün demek değildir; ortak dil oluşturma adımıdır."
                ),
            },
            {
                "title": "Avrupa 6G programı: mimaride birlikte düşünülüyor",
                "body": (
                    "Hexa-X-II gibi Avrupa programları, iletişim ve algılamayı aynı mimaride "
                    "nasıl konumlandıracağımızı raporluyor. Ağırlık laboratuvar ve simülasyondadır."
                ),
            },
            {
                "title": "Akademi–endüstri ortak çalışma grupları",
                "body": (
                    "IEEE ve benzeri girişimler, iletişim ve algılamayı tek radyo zincirinde "
                    "birleştirmenin yollarını tartışıyor. Sahada her kulede radar yoktur."
                ),
            },
            {
                "title": "Üretici laboratuvar gösterimleri",
                "body": (
                    "Büyük üreticiler test ortamında yüksek hız ve algılamayı birlikte "
                    "göstermeye çalışıyor. Laboratuvar iddiası, şebeke garantisi değildir."
                ),
            },
        ],
        "tt_scenarios": [
            {
                "title": "Sis yüzünden gemiler görünmüyor",
                "body": (
                    "Boğaz ve Marmara'da sis kamerayı işe yaramaz hale getirir. "
                    "Sahildeki baz istasyonu, gönderdiği radyo sinyalinin geri dönüşünden "
                    "geminin uzakta ve hızlı olduğunu anlayabilir. Bu fikir araştırılıyor; "
                    "şebekede ürün olarak yoktur."
                ),
            },
            {
                "title": "Şehirde dronları kim güvenli izleyecek?",
                "body": (
                    "Teslimat dronları ve izinsiz uçuşlar için ayrı radar ağı kurmak pahalıdır. "
                    "Mevcut kule hattı, bu koridorlarda ek bir görev üstlenebilir mi diye "
                    "literatürde tartışılıyor."
                ),
            },
            {
                "title": "Enkaz altında insan var mı?",
                "body": (
                    "Deprem sonrası kamera her enkaza giremez. Radyo yankısı hareket ipucu "
                    "verebilir; ancak gizlilik, hata payı ve yasal sınırlar henüz net değildir."
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
                "title": "Standart kuruluşu: akıllı yüzeylerin tanımı yazılıyor",
                "body": (
                    "ETSI gibi kuruluşlar, cepheye asılan yansıtıcı panellerin nasıl test "
                    "edileceğini ve şebekeye nasıl bağlanacağını standartlaştırıyor. "
                    "Henüz her binada satılan ürün değildir."
                ),
            },
            {
                "title": "Akademi: yansıtıcı yüzeylerin fiziği",
                "body": (
                    "IEEE ve üniversite grupları, sinyali telefona çeviren ince panellerin "
                    "sınırlarını ve kayıplarını inceliyor."
                ),
            },
            {
                "title": "Operatörler: cephe ve tünelde prototip deniyor",
                "body": (
                    "Bazı operatörler plaza, tünel ve cephede panel prototipi kuruyor. "
                    "Ticari 'tak-çalıştır' ürün yaygın değildir."
                ),
            },
            {
                "title": "Avrupa RISE-6G projesi",
                "body": (
                    "Akıllı yüzeyleri 6G mimarisine nasıl bağlayacağımızı araştırıyor. "
                    "Laboratuvar ve pilot saha ağırlıklıdır."
                ),
            },
        ],
        "tt_scenarios": [
            {
                "title": "Dar sokakta telefon çekmiyor",
                "body": (
                    "Tarihi Yarımada gibi yerlerde yeni kule dikmek zor veya istenmez. "
                    "Cepheye asılan ince panel, baz istasyonunun sinyalini telefona "
                    "yansıtmaya adaydır; prototip aşamasındadır."
                ),
            },
            {
                "title": "Tünelde bağlantı kopuyor",
                "body": (
                    "Avrasya Tüneli ve Marmaray'da kıvrımlar sinyali zayıflatır. "
                    "Duvara monte panel sinyali yönlendirebilir; saha denemesi adayıdır."
                ),
            },
            {
                "title": "Plaza ve cam cephede içeride zayıf sinyal",
                "body": (
                    "Yüksek frekansta cam ve kalın duvar iç mekânda sinyali keser. "
                    "Şeffaf veya ince yüzey kaplaması iç kapsamayı iyileştirmeye adaydır."
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
                "title": "Akademi: hücre sınırı sorununu matematikle modelliyor",
                "body": (
                    "Linköping gibi merkezler, dağıtık antenlerin aynı anda hizmet "
                    "vermesini simülasyon ve laboratuvarda inceliyor."
                ),
            },
            {
                "title": "IEEE: dağıtık anten literatürü büyüyor",
                "body": (
                    "Yoğun ortamlarda tek kuleye yığılan yükü paylaştırma fikri "
                    "makale ve özel dergi konularında tartışılıyor."
                ),
            },
            {
                "title": "Standart kuruluşu: dağıtık MIMO gündemde",
                "body": (
                    "3GPP gelecek sürümlerde dağıtık anten mimarisini inceliyor. "
                    "Ticari şebeke ürünü henüz değildir."
                ),
            },
            {
                "title": "Üreticiler: stadyum benzeri demolar",
                "body": (
                    "Ericsson ve Nokia gibi firmalar yoğun mekân senaryolarında "
                    "laboratuvar gösterimi yapıyor; kent geneli dağıtım yoktur."
                ),
            },
        ],
        "tt_scenarios": [
            {
                "title": "Stadyumda herkes aynı anda bağlanıyor",
                "body": (
                    "On binlerce kişi tek kuleye yük bindirir; tribünün bir yanı hızlı, "
                    "diğer yanı yavaş kalabilir. Tavan ve tribüne dağıtık antenler "
                    "yükü paylaştırmaya adaydır; fiber maliyeti vardır."
                ),
            },
            {
                "title": "Havalimanında yürürken bağlantı kopuyor",
                "body": (
                    "Geniş terminalde geçişlerde sinyal düşebilir. Birçok küçük anten "
                    "birlikte hizmet vererek kopmayı azaltmaya adaydır."
                ),
            },
            {
                "title": "Depoda robot hücre kenarında zayıflıyor",
                "body": (
                    "Otonom araçlar ve robotlar depo köşelerinde sinyal kaybedebilir. "
                    "Dağıtık anten bu tür iç mekânlarda tartışılıyor."
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
                "title": "Standart kuruluşu: kısa mesafe ultra geniş bant",
                "body": (
                    "IEEE 802.15.3d gibi gruplar, çok yüksek frekansta kısa mesafe "
                    "bağlantının kurallarını yazıyor. Cep telefonu varsayılan bantı değildir."
                ),
            },
            {
                "title": "ITU: frekans tahsisi için veri toplanıyor",
                "body": (
                    "Uluslararası kuruluşlar, terahertz diliminin hangi koşullarda "
                    "kullanılabileceğine dair bilimsel rapor üretiyor."
                ),
            },
            {
                "title": "Kamu araştırma programları",
                "body": (
                    "DARPA ve Max Planck gibi merkezler donanım ve kanal ölçümü yapıyor. "
                    "Ağırlık laboratuvar ortamındadır."
                ),
            },
            {
                "title": "Üretici Sub-THz demoları",
                "body": (
                    "Samsung gibi firmalar 140 GHz civarında kısa mesafe demo yapıyor. "
                    "Açık şehirde cep hızı senaryosu değildir."
                ),
            },
        ],
        "tt_scenarios": [
            {
                "title": "Veri merkezinde kablo karmaşası",
                "body": (
                    "Sunucu rafları arasında binlerce fiber kablo yönetimi zordur. "
                    "Kısa mesafe kablosuz link bu ortamda düşünülüyor; menzil çok kısadır."
                ),
            },
            {
                "title": "Dağlık alanda kuleler arası fiber zor",
                "body": (
                    "Fiber çekmek maliyetli veya imkânsız coğrafyada kuleler arası "
                    "kısa kablosuz köprü adayıdır. Sokak boyunca cep hızı vaadi değildir."
                ),
            },
            {
                "title": "Canlı sunum ve demo salonu",
                "body": (
                    "Teknoloji merkezlerinde yüksek çözünürlüklü canlı yayın denemeleri "
                    "yapılabilir. Günlük abone deneyimi hedefi değildir."
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
                "title": "AI-RAN Alliance: ortak tanım aranıyor",
                "body": (
                    "Üreticiler ve operatörler, yapay zekâ destekli radyo ağının "
                    "sınırlarını birlikte yazmaya çalışıyor. Deneme aşamasındadır."
                ),
            },
            {
                "title": "O-RAN: akıllı uygulama katmanı",
                "body": (
                    "Açık radyo arayüzü üzerinde politika üreten uygulamaların "
                    "nasıl çalışacağı tanımlanıyor. O-RAN kendisi yapay zekâ değildir."
                ),
            },
            {
                "title": "3GPP: radyo arayüzünde makine öğrenmesi",
                "body": (
                    "Standart kuruluşu, öğrenen modellerin radyo katmanında nereye "
                    "oturabileceğini inceliyor. Tam otomatik şebeke henüz değildir."
                ),
            },
            {
                "title": "GPU tabanlı test ortamları",
                "body": (
                    "NVIDIA gibi firmalar laboratuvarda politika denemeleri yapıyor. "
                    "Net enerji kazancı her ortamda ölçülmelidir."
                ),
            },
        ],
        "tt_scenarios": [
            {
                "title": "Gece boş kuleler elektrik yiyor",
                "body": (
                    "Trafiğin az olduğu saatlerde gereksiz radyo birimleri çalışmaya "
                    "devam eder. Yapay zekâ hangi parçayı uyutacağını seçebilir; "
                    "tasarruf hedefidir, burada fatura ölçülmedi."
                ),
            },
            {
                "title": "Maç günü stadyum çevresi çöküyor",
                "body": (
                    "Ani trafik patlamasında sabit kural yetmeyebilir. Kaynak otomatik "
                    "kaydırılabilir; insan denetimi ve geri alma yolu kalır."
                ),
            },
            {
                "title": "Kule arızası geç fark ediliyor",
                "body": (
                    "Donanım bozulması önceden görülüp yedek plan yapılabilir. "
                    "Yanlış alarm ve kara kutu model riski vardır."
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
                "title": "Standart kuruluşu: telefon uydu hücresini görsün",
                "body": (
                    "3GPP Release-17 ve sonrası, standart telefonun uydu hücresine "
                    "bağlanma kurallarını yazıyor. Her eski telefon uyumlu değildir."
                ),
            },
            {
                "title": "Starlink Direct to Cell denemeleri",
                "body": (
                    "Alçak yörünge uydu ile doğrudan cep telefonu bağlantısı kamuya açık "
                    "test ediliyor. Karasal kule hızı ve gecikmesiyle aynı değildir."
                ),
            },
            {
                "title": "AST SpaceMobile saha testleri",
                "body": (
                    "Uydu üzerinden telefon bağlantısı deneniyor. Kapasite sınırlıdır; "
                    "şehir içi yoğunluk senaryosu değildir."
                ),
            },
            {
                "title": "Avrupa uzay ajansı 6G bileşeni",
                "body": (
                    "ESA, 6G ile uydu entegrasyonunu afet ve kırsal bağlamda araştırıyor."
                ),
            },
        ],
        "tt_scenarios": [
            {
                "title": "Depremde kuleler devre dışı kalıyor",
                "body": (
                    "Afet sonrası karasal şebeke zarar görebilir. Uydu üzerinden acil "
                    "SMS veya ses yedek yol olabilir; gecikme şehir kulesinden uzundur."
                ),
            },
            {
                "title": "Açık denizde telefon çekmiyor",
                "body": (
                    "Balıkçı ve gemi filoları karasal kapsama dışına çıkar. Aynı SIM ile "
                    "uydu bağlantısı hedeflenir; hız sınırlı olabilir."
                ),
            },
            {
                "title": "Mezrada kule dikmek imkânsız veya pahalı",
                "body": (
                    "Dağlık kırsalda her köye fiber ve kule ekonomik değildir. Uydu "
                    "boşluğu kapatmaya adaydır; '%100 kapsama' pazarlamadır."
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
                "title": "Standart kuruluşu: pilsiz etiket kuralları",
                "body": (
                    "3GPP Release-19, pilsiz etiketlerin hücresel ağda nasıl okunacağını "
                    "standart gündemine aldı. Ticari raf ürünü değildir."
                ),
            },
            {
                "title": "Akademi: geri saçılım ve enerji toplama",
                "body": (
                    "IEEE ve üniversiteler, ortam radyosundan çalışan etiketlerin "
                    "fizik sınırlarını inceliyor. Menzil kısadır."
                ),
            },
            {
                "title": "Avrupa sıfır güç IoT programları",
                "body": (
                    "Trilyon nesne hedefi araştırma ufkudur; pratik sorun binlerce "
                    "nesnede pil değiştirmenin maliyetidir."
                ),
            },
            {
                "title": "Ticari pilsiz etiket pilotları",
                "body": (
                    "Wiliot ve Qualcomm gibi firmalar depo ve mağazada pilot deniyor. "
                    "Hücresel çoklu okuyucu senaryosu ayrı konudur."
                ),
            },
        ],
        "tt_scenarios": [
            {
                "title": "Binlerce paletin pilini kim değiştirecek?",
                "body": (
                    "Lojistik merkezlerinde her palete pil takmak ekonomik değildir. "
                    "Ortam radyosundan çalışan etiket 'nerede, kaç derece' bildirmeye adaydır."
                ),
            },
            {
                "title": "Serada kablo ve pil lojistiği zor",
                "body": (
                    "Toprağa gömülü nem sensörü pilsiz çalışabilir; ortamda yeterli "
                    "radyo yoksa etiket susar. Kapsama alanı sınırlıdır."
                ),
            },
            {
                "title": "Soğuk zincirde sıcaklık kaçtı mı?",
                "body": (
                    "İlaç ve gıda taşımada sıcaklık ihlali pahalıdır. Pilsiz etiket "
                    "alarm üretebilir; video veya telefon yerine geçmez."
                ),
            },
        ],
    },
}
