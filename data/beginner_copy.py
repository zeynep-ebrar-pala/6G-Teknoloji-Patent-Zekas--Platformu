"""
Temel seviye — kavramsal temel.
Jargon yasak değil: ilk kullanımda açılır. Uzman denklemler expert_depth'te.
Akış: problem → ihtiyaç → yöntem → mekanizma → sonuç → uygulama.
"""

BEGINNER_COPY = {
    "isac": {
        "card": (
            "Baz istasyonu telefonunuza veri gönderir ama çevreyi göremez. Kamera sis ve karanlıkta "
            "işe yaramaz; ayrı radar ise pahalıdır ve frekans çakışması yapabilir. "
            "ISAC (Integrated Sensing and Communication — Entegre Algılama ve İletişim) "
            "aynı antenle hem veri taşır hem dönen sinyalle mesafe ve hız ölçer. "
            "TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi) 4: "
            "laboratuvarda doğrulandı; Türk Telekom şebekesinde henüz kullanılmıyor."
        ),
        "kicker": "Sorun: kule konuşur, göremez",
        "what": (
            "ISAC (Integrated Sensing and Communication — Entegre Algılama ve İletişim), "
            "baz istasyonunun aynı antenle iki işi birden yapmasıdır: telefonunuza veri gönderir "
            "ve çevreden dönen sinyalle mesafe, hız ve yön okur. "
            "Yanına ayrı bir radar kutusu takmak değildir."
        ),
        "why_needed": (
            "Yol trafiği, düşük irtifada uçan dronlar veya kamera olmayan alanları izlemek için "
            "ayrı bir radar ağı kurmak hem pahalı hem karmaşıktır. "
            "Kule zaten radyo sinyali yayınlıyorsa, aynı enerjiyle çevreyi de dinlemek "
            "operatör için mantıklı bir seçenektir."
        ),
        "problem": (
            "Bugünkü baz istasyonları (5G/6G kuleleri) yalnızca telefonla konuşmayı hedefler. "
            "Kamera sisli ve karanlık havada zayıflar; ayrı radar hem pahalıdır hem frekans "
            "çakışması yapabilir. Sonuç: ya bir yeri göremezsiniz ya da iki ayrı sisteme para harcarsınız."
        ),
        "how_steps": [
            "Baz istasyonu telefonunuza normal şekilde veri gönderir; ayrı bir radar kamyonu gerekmez.",
            "Araç, bina veya drondan dönen sinyalin gecikmesi mesafeyi, frekans kayması hızı, birden fazla anten arasındaki fark yönü gösterir.",
            "Veri ile yankı birbirine karışmaması için zaman veya frekans olarak ayrılır.",
            "Özet bilgi (mesafe, hız) yakındaki sunucuya gider; ham sinyal her zaman merkeze taşınmaz.",
        ],
        "mental_model": (
            "Tek bir radyo zinciri iki iş yapar: giden yol telefonunuza veri taşır, "
            "dönen yol çevreyi algılar. İletişime ayrılan güç artarsa algılama zayıflar. "
            "Algılama menzili iletişimden genelde kısa kalır çünkü yansıyan sinyal çok daha zayıf düşer."
        ),
        "analogy": (
            "El feneri gibi düşünün: hem yolu aydınlatır hem de ışığın duvardan geri dönüşünden "
            "önünde bir şey olduğunu anlarsınız. ISAC da aynı radyo hem konuşur hem dinler; "
            "iki ayrı cihaz yan yana değildir."
        ),
        "analogy_technical_map": (
            "Semboller, denklemler ve 3GPP referansları Uzman katmanında."
        ),
        "when_used": (
            "Sisli veya karanlık ortamda; kameranın uygun olmadığı yerlerde; "
            "mevcut kule hattının yolu veya koridoru kestiği şebekede; "
            "ayrı radar frekansı pahalı veya yasal olarak zor olan durumlarda."
        ),
        "when_not": (
            "Her mahallede santimetre hassasiyet henüz gerçekçi değildir — bu araştırma hedefidir "
            "ve burada ölçülmedi. Yoğun yansıma ve kişisel veri kuralları çözülmeden kamusal izleme "
            "ürünü sayılmaz. Bant dar ise menzil ölçümü kabalaşır."
        ),
        "not_to_confuse": (
            "Yanına radar takılmış 5G kulesi ISAC değildir — o iki ayrı sistemdir. "
            "Kamera veya yapay görme de değildir: radyo yankısı fotoğraf üretmez. "
            "Ambient IoT kasıtlı etiket okur; ISAC çoğu zaman doğal yansıtıcıları hedefler."
        ),
        "real_world": (
            "Uluslararası standart kuruluşlarında (3GPP Rel-19) çalışma konusu; "
            "araştırma konsorsiyumları ve otomotiv/dron testleri. "
            "Her kulede satılan ticari radar ürünü değildir."
        ),
        "tt_impact": (
            "InterDigital ile Ankara test merkezinde ETSI ISAC ISG taban kavramlarını kullanan "
            "ön 6G ISAC mimarisinde hücresel ve Wi-Fi algılamayı birlikte gösteren deneme duyuruldu (2026). "
            "Abone şebekesinde ISAC ürünü bu platformda doğrulanmamıştır; hazırlık seviyesi 4."
        ),
        "principle_html": (
            "<p><strong>1. Gönder:</strong> Baz istasyonu telefonunuza veri gönderir. "
            "Ayrı radar donanımı yoktur.</p>"
            "<p><strong>2. Dinle:</strong> Dönen sinyalin gecikmesi mesafeyi, frekans kayması hızı, "
            "antem farkı yönü gösterir.</p>"
            "<p><strong>3. Ayır:</strong> Veri ve yankı zaman veya frekansta ayrılır; "
            "aynı güç iki işi paylaşır.</p>"
            "<p><strong>Sonuç:</strong> Tek antenle iki görev. Bedeli: kısa algılama menzili "
            "ve yoğun yansıma.</p>"
        ),
        "arch_html": (
            "<p><strong>1. Radyo katmanı:</strong> Mevcut anten dizisi hem veri yollar hem yankı dinler.</p>"
            "<p><strong>2. Zamanlama katmanı:</strong> Konuşma ve algılama birbirini bozmaması için "
            "kaynak paylaşılır.</p>"
            "<p><strong>3. Kenar sunucu:</strong> Mesafe, hız ve yön özeti yakında işlenir; "
            "ham sinyal her zaman merkeze taşınmaz.</p>"
            "<p>Dalga şekli ve formül kartları Uzman katmanındadır.</p>"
        ),
    },
    "ris": {
        "card": (
            "Yüksek frekansta radyo dalgası duvar ve köşeden kolay geçmez. "
            "Her kör noktaya yeni kule dikmek hem pahalı hem şehri yorar. "
            "RIS (Reconfigurable Intelligent Surface — Yeniden Yapılandırılabilir Akıllı Yüzey) "
            "cepheye asılan programlanabilir bir yansıtıcıdır: sinyali telefona çevirir; "
            "kendi güçlü vericisi yoktur. "
            "TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi) 5: "
            "prototip ve deneme aşamasında; ticari dağıtım henüz yok."
        ),
        "kicker": "Sorun: dalga köşeyi dönemez",
        "what": (
            "RIS (Reconfigurable Intelligent Surface — Yeniden Yapılandırılabilir Akıllı Yüzey), "
            "yüzlerce küçük parçadan oluşan ince bir paneldir. "
            "Her parça gelen dalganın fazını ayarlar ve sinyali hedef telefona yönlendirir. "
            "Panel internet üretmez; baz istasyonunun yayınını yansıtır."
        ),
        "why_needed": (
            "Yüksek frekansta duvar ve köşe sinyali keser veya yavaşlatır. "
            "Her kör noktaya kule dikmek hem yatırım hem elektromanyetik yük getirir. "
            "Operatör, aktif röleden daha az enerjiyle kapsama boşluğunu kapatacak bir yüzey arar; "
            "RIS bu ihtiyaca adaydır."
        ),
        "problem": (
            "Yüksek frekansta doğrudan görüş yoksa bağlantı kopar veya hız düşer. "
            "Plaza camı, avlu ve tünel kıvrımı bunun şehirdeki örnekleridir. "
            "Aktif röle ise kendi radyo zincirini, güç kaynağını ve parazitini beraberinde taşır."
        ),
        "how_steps": [
            "İnce panel cepheye, cam veya tünel duvarına asılır — bu bir baz istasyonu değildir.",
            "Her parça fazı kaydırır; tüm yüzey sinyali şekillendirir.",
            "Baz istasyonu hedef telefonu bildirir; kontrol hattı düşük hızlıdır.",
            "Engellenen doğrudan yol yerine kontrollü bir yansıma yolu oluşur.",
        ],
        "mental_model": (
            "RIS verici değil, yansıma yüzeyidir. Sinyal önce panele, sonra telefona gider. "
            "İki kez yol kaybı vardır; yüzey büyüdükçe kazanç artabilir ama kanal doğru "
            "ölçülmezse faz ayarı yanlış olur ve kazanç düşer."
        ),
        "analogy": (
            "Duvara asılı, her parçası ayrı ayarlanabilen bir ayna düşünün. "
            "Işık kaynağı baz istasyonudur; ayna ışığı telefonunuza çevirir. "
            "Ayna kendi başına lamba değildir; aktif röle veya küçük hücre de değildir."
        ),
        "analogy_technical_map": (
            "Semboller, denklemler ve 3GPP referansları Uzman katmanında."
        ),
        "when_used": (
            "Doğrudan görüş olmayan sokak, tünel kıvrımı, tribün, plaza içi yüksek frekans ve "
            "kule dikilemeyen tarihi dokuda. Aktif röleden daha düşük enerji ve yatırım istenen yerde."
        ),
        "when_not": (
            "Yüzey kanalı doğru ölçülemezse (pasif parçalar alıcı değildir) ve kontrol gecikmesi "
            "kullanıcı hızına yetmezse kazanç düşer. Enerji tasarrufu vaatleri araştırma hedefidir; "
            "bu platformda saha faturası ölçülmedi."
        ),
        "not_to_confuse": (
            "Aktif röle veya küçük hücre değildir — yüksek güçlü vericisi yoktur. "
            "Metamalzeme 'görünmez pelerin' iddiası fizik yasalarını iptal etmez; "
            "yalnızca yansıma yüzeyi programlanır. ISAC ile birlikte kullanılabilir; "
            "RIS tek başına radar değildir."
        ),
        "real_world": (
            "ETSI RIS ISG, 3GPP Rel-19/20 çalışma kalemleri, cephe ve iç mekân operatör denemeleri. "
            "Tak-çalıştır ticari ürün her binada yoktur."
        ),
        "tt_impact": (
            "Bu platformda Türk Telekom adına doğrulanmış RIS saha pilotu veya abone şebekesi "
            "kurulumu kaydı yoktur. Grup, Ericsson ile 6G Ar-Ge mutabakatı ve EUREKA DRIVING-6G "
            "projesinde 6G mimarisini takip ediyor; hazırlık seviyesi 5."
        ),
        "principle_html": (
            "<p><strong>1. Yüzey:</strong> Cepheye ince yansıtıcı asılır. Bu bir baz istasyonu değildir.</p>"
            "<p><strong>2. Faz:</strong> Parçalar sinyali hedef telefona çevirir.</p>"
            "<p><strong>3. Komut:</strong> Baz istasyonu düşük hızlı kontrol hattından hedefi bildirir.</p>"
            "<p><strong>Sonuç:</strong> Kontrollü yansıma. Bedeli kanal ölçümü ve çift yol kaybıdır.</p>"
        ),
        "arch_html": (
            "<p><strong>1. Yüzey:</strong> Küçük parçalar; aktif radyo zinciri yok veya çok az.</p>"
            "<p><strong>2. Denetleyici:</strong> Parça fazını baz istasyonu emrine yazar.</p>"
            "<p><strong>3. Kontrol hattı:</strong> Kule–yüzey bağlantısı. Yüzey kendi başına internet üretmez.</p>"
            "<p>Kazanç ölçeği ve kanal ölçümü Uzman formül kartlarındadır.</p>"
        ),
    },
    "cell_free": {
        "card": (
            "Hücre kenarında sinyal zayıflar; geçiş kopma riski taşır. "
            "Hücresiz Massive MIMO (Multiple-Input Multiple-Output — Çok Girişli Çok Çıkışlı), "
            "şehre yayılmış küçük erişim noktalarının aynı anda, aynı frekansta birlikte "
            "hizmet verdiği mimaridir: kenar sorunu tasarım olarak kalkar. "
            "Bedeli fiber bağlantıdır. "
            "TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi) 4: "
            "laboratuvar prototipi; Türk Telekom şebekesinde henüz kullanılmıyor."
        ),
        "kicker": "Sorun: hücre sınırında zayıflar",
        "what": (
            "Hücresiz Massive MIMO, kullanıcıyı tek hücreye bağlamak yerine şehre yayılmış "
            "erişim noktalarının aynı frekansta, merkezi veya yarı dağıtık işlemle birlikte "
            "hizmet verdiği mimaridir. Hücre sınırı tasarım olarak ortadan kalkar."
        ),
        "why_needed": (
            "Kapasite ve adalet hücre kenarında çöker: istenen sinyal zayıf, komşu kule parazittir. "
            "Stadyum ve terminalde yük tek makro kuleye yığılır. Dağıtık antenler yolu kısaltır "
            "ve paraziti birlikte bastırılabilir hale getirir."
        ),
        "problem": (
            "Hücresel şebeke pasta dilimidir. Dilim kenarında sinyal-parazit oranı düşer. "
            "Geçiş başarısızlığı kopmadır. Tek kule ve çok kullanıcı: tribünün bir yanı tok, diğeri açık."
        ),
        "how_steps": [
            "Küçük erişim noktaları tavan, tribün ve caddeye dağıtılır.",
            "Yüksek hızlı fiber merkezi veya kenar sunucuya gider; zaman senkronu şarttır.",
            "Birkaç nokta aynı anda ortak ön kodlama uygular.",
            "Komşu kullanıcıya giden enerji birlikte bastırılır.",
        ],
        "mental_model": (
            "Tek hücre yok; kullanıcı birkaç noktanın ortak hüzmesinde durur. "
            "Hesap merkeze veya dağıtık kümeye gitmek zorundadır — fiber yoksa ortak ön kodlama "
            "yazılamaz. Fiber gecikmesi ve faz kayması kazancı tersine çevirir."
        ),
        "analogy": (
            "Koordineli çok nokta (CoMP) hücresiz MIMO'nun atasıdır; fark, hücre varsayımını "
            "tamamen kaldırmasıdır. Küçük hücre ormanı hâlâ hücre kenarı taşır."
        ),
        "analogy_technical_map": (
            "Semboller, denklemler ve 3GPP referansları Uzman katmanında."
        ),
        "when_used": (
            "Yüksek yoğunluk, hareket ve adalet gerektiğinde: stadyum, havalimanı, üretim hattı, "
            "yoğun bulvar. Makro kule estetiğinin istenmediği iç mekânda."
        ),
        "when_not": (
            "Seyrek kırsalda her direğe fiber maliyeti anlamsızdır; uydu veya makro kule daha rasyoneldir. "
            "Spektral kazanç vaatleri literatür aralığıdır; bu platformda saha ölçümü yoktur."
        ),
        "not_to_confuse": (
            "Küçük hücre hâlâ hücredir. Klasik CoMP ortak işlem yapar ama hücre kimliğini kaldırmaz. "
            "Wi-Fi roaming, aynı anda çok noktanın sembolünüzü taşıması değildir."
        ),
        "real_world": (
            "Dağıtık MIMO literatürü, 3GPP Rel-19/20 çalışma kalemi, satıcı laboratuvar gösterimleri. "
            "Stadyum denemesi adayıdır; kent geneli dağıtım aşamasında değildir."
        ),
        "tt_impact": (
            "Bu platformda Türk Telekom adına doğrulanmış hücresiz MIMO saha pilotu kaydı yoktur. "
            "Ar-Ge yayınlarında 6G ağ dilimleme ve dağıtık mimari konuları izlenir; "
            "hazırlık seviyesi 4; fiber maliyeti operasyonel kısıttır."
        ),
        "principle_html": (
            "<p><strong>1. Dağıt:</strong> Noktalar sık yerleştirilir; tek makro kuleye bel bağlanmaz.</p>"
            "<p><strong>2. Ortak taşı:</strong> Telefon aynı anda birkaç noktaya bağlanır.</p>"
            "<p><strong>3. Birleştir:</strong> Fiber üzerindeki işlemci ortak ön kodlama uygular.</p>"
            "<p><strong>Sonuç:</strong> Geçiş hissi kaybolur. Fatura fiber ve hesaptır.</p>"
        ),
        "arch_html": (
            "<p><strong>1. Erişim noktası:</strong> Düşük karmaşıklıklı radyo; ağır hesap yok.</p>"
            "<p><strong>2. Fiber:</strong> Senkron yoksa ortak hüzme bozulur.</p>"
            "<p><strong>3. Merkez / kenar:</strong> Ortak kestirim ve ön kodlama.</p>"
            "<p>Sinyal-parazit oranı ve ön kodlama varsayımları Uzman kartlarındadır.</p>"
        ),
    },
    "thz": {
        "card": (
            "Geleneksel frekanslar veri merkezi içi ve kule köprüsü için dar kalabilir. "
            "THz (terahertz), milimetre dalga ile kızılötesi arasındaki spektrumu açar; "
            "bant genişliği büyür ama menzil kısalır. "
            "TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi) 3: "
            "laboratuvar kanıtı; saha şebekesinde kullanılmıyor. "
            "6G yalnızca THz anlamına gelmez."
        ),
        "kicker": "Sorun: veri borusu hâlâ dar",
        "what": (
            "THz iletişimi, kabaca 0,1–10 THz diliminde onlarca GHz bant genişliği açma "
            "girişimidir. Kapasite önce bant genişliğiyle büyür; sinyal kalitesi ikinci plandadır."
        ),
        "why_needed": (
            "Veri merkezi rafları arası bağlantı, fiber çekilemeyen kule köprüsü ve ileride "
            "yüksek hızlı iç mekân adayıdır. Fiber her geometriye gitmez. "
            "THz, doğru mesafede kablosuz yüksek bant adayıdır."
        ),
        "problem": (
            "Frekans yükseldikçe yol kaybı ve su buharı emilimi büyür. "
            "El, yaprak ve yağmur bağlantıyı keser. Donanım olgun cep telefonu seviyesinde değildir. "
            "Bu yüzden hazırlık seviyesi düşüktür."
        ),
        "how_steps": [
            "100 GHz üzeri pencereler açılır; hedef onlarca GHz bant genişliği.",
            "Yol kaybı ve su buharı emilimi sinyali zayıflatır.",
            "Dar hüzme kaybı telafi eder; hizalama hassaslaşır.",
            "Raf, salon ve kule köprüsü — açık şehir makrosu değil.",
        ],
        "mental_model": (
            "Bant genişliği büyüdükçe kapasite artar; emilim sinyal kalitesini düşürürse kazanç azalır. "
            "Dar hüzme kaybı telafi eder ama engel olasılığını yükseltir. "
            "Doğru kullanım kısa mesafe ve doğrudan görüştedir."
        ),
        "analogy": (
            "Kablosuz fiber adayı: yüksek bant, kısa mesafe, hizalı hüzme. "
            "Makro hücresel taşıyıcı değildir."
        ),
        "analogy_technical_map": (
            "Semboller, denklemler ve 3GPP referansları Uzman katmanında."
        ),
        "when_used": (
            "Kablosuz veri merkezi, kısa arka bağlantı, kontrollü iç mekân, spektroskopi. "
            "Doğrudan görüş ve onlarca–yüzlerce metre."
        ),
        "when_not": (
            "Açık şehir makrosu, yağmurlu uzun mesafe, cepten-cepte kilometre. "
            "'Her aboneye 1 Tbps' pazarlama cümlesidir; bu platformda ölçülmedi. "
            "Tıbbi nanosensör araştırma ufkudur, ticari özellik değildir."
        ),
        "not_to_confuse": (
            "5G mmWave (28–39 GHz) THz değildir. Serbest uzay optiği (lazer) ayrı sınıftır. "
            "ISAC THz dalga şekli kullanabilir; THz tek başına algılama standardı değildir."
        ),
        "real_world": (
            "IEEE 802.15.3d, ITU-R spektrum çalışmaları, 3GPP TR 38.807, satıcı Sub-THz gösterimleri. "
            "Abone telefonunda varsayılan bant değil."
        ),
        "tt_impact": (
            "Bu platformda Türk Telekom adına doğrulanmış THz saha kurulumu veya abone şebekesi "
            "kayıdı yoktur. Ankara ve İstanbul veri merkezleri işletilir; THz mesh bu platformda "
            "ölçülmemiştir. Hazırlık seviyesi 3; laboratuvar aşaması."
        ),
        "principle_html": (
            "<p><strong>1. Bant:</strong> mmWave ile kızılötesi arasındaki spektrum açılır.</p>"
            "<p><strong>2. Emilim:</strong> Su buharı, duvar ve el ek kayıp basar.</p>"
            "<p><strong>3. Hüzme:</strong> Dar hüzme kaybı telafi eder; menzil kısa kalır.</p>"
            "<p><strong>Sonuç:</strong> Doğru geometride yüksek bant adayı. 6G = yalnızca THz değildir.</p>"
        ),
        "arch_html": (
            "<p><strong>1. Radyo ön uç:</strong> Özel yarı iletkenler; olgun cep telefonu seviyesinde değil.</p>"
            "<p><strong>2. Dönüştürücü:</strong> Yüksek hızlı dönüştürücü; güç ve ısı sorunu.</p>"
            "<p><strong>3. Geometri:</strong> Kısa mesafe, hizalı hüzme, yedek doğrudan görüş.</p>"
            "<p>Yol kaybı ve Shannon formülleri Uzman kartlarındadır.</p>"
        ),
    },
    "ai_ran": {
        "card": (
            "Sabit kural dolu stadyum ile boş geceyi aynı tarifeyle yönetir. "
            "AI-RAN (Artificial Intelligence-Native RAN — yapay zekâ tabanlı telsiz erişim ağı), "
            "ölçüme göre milisaniye–saniye döngüsünde kaynak kaydırır. Sohbet botu değildir. "
            "TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi) 5: "
            "deneme aşamasında; insansız işletim için saha doğrulaması yok."
        ),
        "kicker": "Sorun: şebeke sabit kural izler",
        "what": (
            "AI-native RAN, radyo erişim ağının bir kısmının sabit eşik yerine öğrenilmiş "
            "modelle çalışacak şekilde tasarlanmasıdır. "
            "Bugün pratik giriş O-RAN RIC üzerindeki uygulamalardır; "
            "hava arayüzünün tamamını sinir ağı yapmak araştırma ucudur."
        ),
        "why_needed": (
            "Trafik, kanal ve enerji zamanla değişir. Sabit tarife maç uzamasına ve arızaya geç kalır. "
            "Boş kule elektrik yer. Öğrenen döngü, ölçüme dayalı uyarlama ihtiyacını karşılar."
        ),
        "problem": (
            "İnsan her saniye kaynak yönetimi yazamaz. Klasik eşik yerel optimumda sıkışır. "
            "Enerji, kapasite ve hareket çekişir. Veri yoksa model uydurur; "
            "kara kutu düzenleyiciye açıklanamaz."
        ),
        "how_steps": [
            "Yük, sinyal kalitesi, kaynak blokları, enerji ve arıza öncüleri ölçülür.",
            "Hızlı döngüde hüzme ve geçiş; yavaş döngüde enerji ve tahmin kararları verilir.",
            "Politika baz istasyonuna yazılır; geri alma yolu tasarımın parçasıdır.",
            "Ödül (kapasite, enerji, kesinti) kötüyse politika güncellenir.",
        ],
        "mental_model": (
            "Kapalı döngü: ölç → politika → uygula → ödül. Hızlı döngü onlarca milisaniye, "
            "yavaş döngü saniye ve üzeri. Denetim kalkmaz; yanlış öğrenen politika şebekeyi "
            "kilitleyebilir. İşlemci gücü de enerji yer — net kazanç ölçülmelidir."
        ),
        "analogy": (
            "Klasik SON (Self-Organizing Network) atasıdır. Fark, öğrenmenin kaynak yönetiminden "
            "(araştırma ucunda) hava arayüzüne kadar indirilme iddiasıdır. "
            "O-RAN açık arayüzdür; yapay zekâ onun üstündeki uygulamadır."
        ),
        "analogy_technical_map": (
            "Semboller, denklemler ve 3GPP referansları Uzman katmanında."
        ),
        "when_used": (
            "Değişken yük, enerji hedefi, kestirimci bakım, çok tedarikçili O-RAN denemesi. "
            "Ölçüm kalitesi yüksek ve geri alma prosedürü tanımlı ise."
        ),
        "when_not": (
            "Eğitilmemiş modelle canlı şebekeye otonom pilot denmez. "
            "Enerji ve 'sıfır insan' vaatleri hedef veya pazarlamadır; "
            "bu platformda saha faturası yoktur."
        ),
        "not_to_confuse": (
            "Bu platformdaki sohbet asistanı AI-RAN değildir. "
            "O-RAN ≠ yapay zekâ: biri arayüz, diğeri uygulamadır."
        ),
        "real_world": (
            "O-RAN WG2/WG10, 3GPP TR 38.843, AI-RAN Alliance, operatör RIC denemeleri. "
            "Tam nöral hava arayüzü laboratuvar aşamasında."
        ),
        "tt_impact": (
            "Netsia (grup Ar-Ge iştiraki) programlanabilir RAN, dilimleme ve RIC güvencesi için "
            "ABD patentleri aldı; Ar-Ge ekipleri yapay zekâ destekli 6G yayınları üretti. "
            "Net Insight ile Open RAN senkronizasyonu ve Ericsson ile 6G standart mutabakatı "
            "imzalandı. Hazırlık seviyesi 5; insan denetimi kalkmaz."
        ),
        "principle_html": (
            "<p><strong>1. Ölç:</strong> Yük, kanal, enerji, kopma.</p>"
            "<p><strong>2. Karar:</strong> RIC üzerinde uygulama politika üretir.</p>"
            "<p><strong>3. Uygula:</strong> Sonuç izlenir; geri alma yolu tasarımın parçasıdır.</p>"
            "<p><strong>Sonuç:</strong> Uyarlanan şebeke. Ölçüm + model + denetim.</p>"
        ),
        "arch_html": (
            "<p><strong>1. Ölçüm / radyo:</strong> Klasik sinyal işleme veya araştırma ucunda nöral radyo.</p>"
            "<p><strong>2. RIC:</strong> Hızlı ve yavaş döngü uygulamaları. O-RAN bu katmanı taşır.</p>"
            "<p><strong>3. Hızlandırıcı:</strong> NPU/GPU olabilir; net enerji kazancı hesaplanmalıdır.</p>"
            "<p>Kayıp fonksiyonu ve öğrenme formülleri Uzman kartlarındadır.</p>"
        ),
    },
    "ntn": {
        "card": (
            "Karasal kule şehir ve asfaltı kapsar; dağ, deniz ve enkaz boş kalır. "
            "NTN (Non-Terrestrial Network — Karasal Olmayan Ağ), uydu ve yüksek irtifa "
            "platformlarını çekirdeğe bağlar. Bedeli gecikme ve frekans kaymasıdır. "
            "TRL 6 — TR 38.811; kamuya açık direct-to-cell denemeleri vardır. "
            "Şehir kulesinin rakibi değil, tamamlayıcısıdır."
        ),
        "kicker": "Sorun: kule her yere ulaşmaz",
        "what": (
            "NTN (Non-Terrestrial Network — Karasal Olmayan Ağ), alçak yörünge uydu, "
            "jeostasyon uydu ve yüksek irtifa platformlarını karasal çekirdeğe bağlayan "
            "mimariidir. Direct-to-cell, özel çanak yerine standart telefonun uydu hücresini "
            "görmesi demektir."
        ),
        "why_needed": (
            "Kapsama, kule ve fiberin ulaştığı yer kadardır. Kırsal yatırım, deniz, havacılık ve "
            "afet (kule yıkılınca) bu modeli kırar. Aynı kimlik ve numara ile boşluğu kapatmak gerekir."
        ),
        "problem": (
            "Mesafe sinyal kaybını büyütür. Alçak yörünge uydu hızlı hareket eder; "
            "frekans kayması ve sık geçiş üretir. Jeostasyon gecikmesi konuşmayı zorlar. "
            "Spektrum, yer kapısı ve düzenleme operatör işidir."
        ),
        "how_steps": [
            "Şehirde karasal kule; boş coğrafyada uydu veya yüksek irtifa hücresi.",
            "Yer kapısı: feeder link → gateway → çekirdek.",
            "Radyo katmanında frekans kayması ve gecikme düzeltilir; aksi halde bağlantı tutmaz.",
            "Acil SMS ve ses önce gelir; terabit şehir deneyimi vaadi değildir.",
        ],
        "mental_model": (
            "Karasal yol birincildir; NTN kapsama deliğini kapatır. "
            "Gecikme mesafeye bağlıdır (alçak yörünge onlarca ms; jeostasyon gidiş-dönüş ~250 ms). "
            "Direct-to-cell, telefon anteninin link bütçesine sığmasıdır — VSAT çanak değildir."
        ),
        "analogy": (
            "Şehirde yol asfalttır; dağda helikopter iner. NTN de öyledir: "
            "aynı abone kimliğiyle boş coğrafyaya uydu veya yüksek irtifa platformundan hizmet gelir. "
            "Bu, şehirdeki her kuleyi kaldırmak demek değildir."
        ),
        "analogy_technical_map": (
            "Semboller, denklemler ve 3GPP referansları Uzman katmanında."
        ),
        "when_used": (
            "Kırsal, dağ, deniz, havacılık, afet yedek hattı ve kulesiz IoT. "
            "Karasalın ekonomik olmadığı yerde."
        ),
        "when_not": (
            "Şehir içi kapasite ve milisaniye altı gecikme için birincil yol değildir. "
            "'%100 küresel sıfır boşluk' pazarlama dilidir. "
            "Bu platformda uydu gecikmesi saha ölçülmedi."
        ),
        "not_to_confuse": (
            "VSAT çanak, direct-to-cell değildir. Yüksek irtifa platformu uydu değildir (stratosfer). "
            "ISAC 'gökyüzünü radar yapmak' NTN değildir."
        ),
        "real_world": (
            "3GPP TR 38.811, Rel-17/18 NTN iş kalemi, kamuya açık direct-to-cell denemeleri. "
            "Afet yedek hattı operatör stratejisidir, saha garantisi değildir."
        ),
        "tt_impact": (
            "TTI (Türk Telekom International) toptan ağda 19 ülkede PoP işletir; kırsal kapsama "
            "karasal şebeke ile sağlanır. Abone şebekesinde Rel-17 direct-to-cell NTN ürünü "
            "bu platformda doğrulanmamıştır. Hazırlık seviyesi 6; endüstri denemeleri vardır."
        ),
        "principle_html": (
            "<p><strong>1. Öncelik:</strong> Şehir kulede kalır. Boş coğrafyada uydu / yüksek irtifa.</p>"
            "<p><strong>2. Kimlik:</strong> Hedef standart telefonun uydu hücresini görmesidir.</p>"
            "<p><strong>3. Telafi:</strong> Radyo katmanı frekans kayması ve gecikmeyi düzeltir; "
            "yer kulesi kadar düşük gecikme vaadi değildir.</p>"
            "<p><strong>Sonuç:</strong> Kapsama deliği kapanır. Rakip değil, tamamlayıcı.</p>"
        ),
        "arch_html": (
            "<p><strong>1. Uzay/hava:</strong> Alçak yörünge takımı, isteğe yüksek irtifa platformu.</p>"
            "<p><strong>2. Gateway:</strong> Feeder link → yer kapısı → çekirdek.</p>"
            "<p><strong>3. Telefon:</strong> Rel-17+ NTN modem; her eski cihaz garanti değildir.</p>"
            "<p>Frekans kayması ve yol kaybı Uzman kartlarındadır.</p>"
        ),
    },
    "ambient_iot": {
        "card": (
            "Koli ve sera ölçeğinde pil değiştirmek ekonomik değildir. Ambient IoT, ortam radyosundan "
            "enerji toplayıp geri saçılımla kısa kimlik bildirir; video taşımaz. "
            "TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi) 4: "
            "laboratuvar doğrulaması; ticari dağıtım henüz yok."
        ),
        "kicker": "Sorun: her nesneye pil değiştirilemez",
        "what": (
            "Ambient IoT, pili olmayan veya çok küçük olan etiketlerin ortam radyosundan "
            "(kule, Wi-Fi, yardımcı aydınlatıcı) enerji toplayıp çoğunlukla geri saçılımla kısa "
            "durum mesajı verdiği IoT sınıfıdır. Amaç ucuz, seyrek izlemedir."
        ),
        "why_needed": (
            "Pil lojistiği koli, sera ve sayaç ölçeğinde işlemez. NB-IoT ve RedCap hâlâ bir enerji "
            "kaynağı ister. Pilsiz etiket, 'nerede / kaç derece' işini bakım ekibi olmadan çözme ihtiyacıdır."
        ),
        "problem": (
            "Yansıyan güç zayıftır; menzil kısa, bit hızı düşüktür. Ortam enerjisi garanti değildir. "
            "Okuyucu hassas, protokol dardır. Telefonun yerini almaz."
        ),
        "how_steps": [
            "Rectenna ortam radyosunu elektriğe çevirir.",
            "Anten empedansı ile gelen taşıyıcı modüle edilir; kendi güçlü vericisi yoktur.",
            "Yakındaki baz istasyonu veya okuyucu zayıf yankı ve biti ayırır.",
            "'Koli 14, 4 °C' gibi kısa mesaj — video yok.",
        ],
        "mental_model": (
            "Ortam enerjisi × geri saçılım verimi = okunabilir bit. "
            "Radyo zayıf bölgede etiket susar. RFID atasıdır; fark hücresel okuyucu ve adresleme hedefidir."
        ),
        "analogy": (
            "Pasif RFID'nin hücresel okuyucuya taşınması. "
            "Enerji hasatlı (güneş+pil) sensör ayrı sınıftır."
        ),
        "analogy_technical_map": (
            "Semboller, denklemler ve 3GPP referansları Uzman katmanında."
        ),
        "when_used": (
            "Palet, soğuk zincir, sera, sayaç, yapı sağlığı — kısa menzil, seyrek, düşük hız, uzun ömür."
        ),
        "when_not": (
            "Ses, görüntü, kilometre menzil, hareketli araç telemetrisi. "
            "'1 sent, trilyon nesne' hedef veya pazarlamadır. Radyosuz köşede etiket ölür."
        ),
        "not_to_confuse": (
            "Mağaza kapısı RFID atasıdır; hücresel çoklu okuyucu senaryosu farklıdır. "
            "ISAC doğal yansımayı ölçer; Ambient IoT kasıtlı etikettir."
        ),
        "real_world": (
            "3GPP TR 38.848, akademik geri saçılım, ticari pilsiz etiket denemeleri. "
            "TT IoT platformuna akış senaryodur; her rafta değildir."
        ),
        "tt_impact": (
            "Türk Telekom IoT platformu operasyonel olarak cihaz ve sensör verisini toplar. "
            "Pilsiz 6G Ambient IoT etiket dağıtımı abone şebekesinde bu platformda "
            "doğrulanmamıştır. Hazırlık seviyesi 4; telefonun yerini almaz."
        ),
        "principle_html": (
            "<p><strong>1. Topla:</strong> Rectenna radyo kırıntısını elektriğe çevirir.</p>"
            "<p><strong>2. Yansıt:</strong> Kendi güçlü vericisi yoktur; gelen taşıyıcı modüle edilir. Menzil kısadır.</p>"
            "<p><strong>3. Oku:</strong> Yakın okuyucu zayıf yankıyı ayırır ve buluta yazar.</p>"
            "<p><strong>Sonuç:</strong> Ucuz, pilsiz, seyrek iz. Video taşımaz.</p>"
        ),
        "arch_html": (
            "<p><strong>1. Etiket:</strong> Çip + mikro kapasitör + rectenna.</p>"
            "<p><strong>2. Okuyucu:</strong> Baz istasyonu veya yardımcı aydınlatıcı; yüksek hassasiyet.</p>"
            "<p><strong>3. IoT bulutu:</strong> Dar adresleme, TT IoT platformu.</p>"
            "<p>Enerji hasadı formülleri Uzman kartlarındadır.</p>"
        ),
    },
}
