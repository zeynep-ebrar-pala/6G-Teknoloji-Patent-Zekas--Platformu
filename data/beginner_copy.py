"""
Temel seviye anlatım — sıfır teknik bilgi.
Her teknoloji: sorun → çözüm → analoji → Türk Telekom'da ne işe yarar.
Uzman jargonu (OFDM, CRB, gNB, Rel-19) burada yok; o metinler technologies.py'de kalır.
"""

BEGINNER_COPY = {
    "isac": {
        "card": (
            "Bugün telefon kulesi yalnızca internet taşır. Sis, gece veya kameranın "
            "göremediği yerde bir aracı fark etmek için ayrı radar veya kamera gerekir. "
            "ISAC aynı kuleyi hem internet hem radar yapar: gönderilen sinyalin yankısından "
            "mesafe ve hız okunur. Türk Telekom için ek radar aracı dikmeden çevre farkındalığı demektir."
        ),
        "kicker": "Sorun: kule konuşur, bakmaz",
        "teach_html": (
            "<div class='teach-item'><div class='teach-label'>Bugünün sorunu</div>"
            "<p>Baz istasyonu veri taşır; çevreyi görmez. Sis, yağmur ve karanlıkta kamera körleşir. "
            "Ayrı radar kurmak pahalıdır ve şehirde yer kaplar.</p></div>"
            "<div class='teach-item'><div class='teach-label'>6G bunu nasıl çözer</div>"
            "<p>Aynı radyo sinyali hem telefonunuza internet götürür hem de duvardan, arabadan, "
            "dronlardan geri seken yankıyı dinler. Yankı ne kadar geç dönerse nesne o kadar uzaktır; "
            "sesi nasıl kayıyorsa o kadar hızlıdır.</p></div>"
            "<div class='teach-item'><div class='teach-label'>Analoji</div>"
            "<p>Yarasa karanlıkta gözle değil, sesin geri dönüşüyle 'görür'. ISAC kulesi de bağırır "
            "ve yankıyı dinler — ama aynı anda sizinle konuşmayı da sürdürür.</p></div>"
            "<div class='teach-item'><div class='teach-label'>Türk Telekom abonesi için ne değişir</div>"
            "<p>Boğaz'da sis, şehir içi dron koridoru, enkaz altı hareket: mevcut kule altyapısı "
            "radar kamyonu dikilmeden bu işlere aday olur. Olgunluk notu TRL 4'tür — laboratuvar "
            "doğrulandı, her mahallede henüz yok.</p></div>"
        ),
        "arch_html": (
            "<p><strong>Katman 1 — Kule ve anten:</strong> Mevcut baz istasyonu hem internet yollar hem yankı dinler. "
            "Ayrı radar kamyonu yoktur.</p>"
            "<p><strong>Katman 2 — Ayırıcı yazılım:</strong> Konuşma verisi ile yankı birbirine karışmasın diye "
            "zaman ve frekans paylaşılır.</p>"
            "<p><strong>Katman 3 — Kenar sunucu:</strong> Mesafe/hız haritası Türk Telekom kenar bulutuna gider "
            "(trafik, dron, enkaz senaryoları).</p>"
            "<p>Donanım kısaltmaları, 3GPP ve formül için soldan <strong>Uzman Seviyesi</strong> açın.</p>"
        ),
        "principle_html": (
            "<p><strong>1. Gönder:</strong> Kule, her zamanki gibi internet sinyalini yayınlar. "
            "Yeni bir 'radar kamyonu' yoktur.</p>"
            "<p><strong>2. Dinle:</strong> Sinyal araba, duvar veya drondan seker. Kule bu yankıyı "
            "alır. Gecikme = mesafe, kayma = hız.</p>"
            "<p><strong>3. Ayır:</strong> Yazılım, sizin konuşma verinizle yankıyı birbirine karıştırmaz. "
            "Biri internet, diğeri haritadır.</p>"
            "<p><strong>Sonuç:</strong> Tek anten, iki iş. Operatör için maliyet ve spektrum tasarrufu; "
            "şehir için kamera koymadan farkındalık.</p>"
        ),
    },
    "ris": {
        "card": (
            "Yüksek hızlı sinyal düz gider; köşe başı, asansör ve kalın duvar kör nokta kalır. "
            "Klasik çözüm yeni kule dikmektir — pahalı ve çirkin. RIS, bina cephesine asılan "
            "elektronik bir ayna gibidir: gelen sinyali sizin bulunduğunuz odaya çevirir, "
            "neredeyse elektrik harcamaz. Türk Telekom kör noktayı kule dikmeden kapatır."
        ),
        "kicker": "Sorun: sinyal köşeyi dönemez",
        "teach_html": (
            "<div class='teach-item'><div class='teach-label'>Bugünün sorunu</div>"
            "<p>Radyo dalgası ışık gibi davranır: duvarın arkasına ve keskin köşeye zor ulaşır. "
            "Plaza camı, asansör boşluğu ve avlu 'çekmiyor' şikâyetinin kaynağı budur. "
            "Her kör noktaya kule dikmek hem pahalıdır hem kent estetiğini bozar.</p></div>"
            "<div class='teach-item'><div class='teach-label'>6G bunu nasıl çözer</div>"
            "<p>Cepheye ince bir elektronik yüzey asılır. Yüzeyin her küçük parçası sinyali "
            "biraz döndürür; hepsi birlikte ışığı sizin telefona odaklar. Aktif verici yoktur, "
            "bu yüzden enerji tüketimi çok düşüktür.</p></div>"
            "<div class='teach-item'><div class='teach-label'>Analoji</div>"
            "<p>Karanlık odada el feneri duvarın arkasını aydınlatamaz. Açısı ayarlanan bir ayna "
            "ışığı büküp görünmeyen odaya taşır. RIS, radyo için o ayarlanabilir aynadır.</p></div>"
            "<div class='teach-item'><div class='teach-label'>Türk Telekom abonesi için ne değişir</div>"
            "<p>Plaza camı, stadyum tribünü, metro girişi: kapsama 'çekmiyor' yerine yönlendirilmiş "
            "sinyal olur. TRL 5 — prototip ve saha denemesi aşamasında, ticari kule kadar olgun değil.</p></div>"
        ),
        "arch_html": (
            "<p><strong>Katman 1 — Yüzey:</strong> Cam veya cepheye ince elektronik ayna asılır. "
            "Kendi başına internet üretmez.</p>"
            "<p><strong>Katman 2 — Küçük denetleyici:</strong> Her hücre sinyali biraz döndürür; "
            "hepsi birlikte hüzmeyi size çevirir.</p>"
            "<p><strong>Katman 3 — Kule emri:</strong> Baz istasyonu aynaya 'şu kullanıcıya bak' der. "
            "Kontrol hattı ince ve düşük güçlüdür.</p>"
            "<p>Metamalzeme, faz kaydırma ve 3GPP RIS için soldan <strong>Uzman Seviyesi</strong> açın.</p>"
        ),
        "principle_html": (
            "<p><strong>1. Yüzeyi as:</strong> Bina, cam veya duvara ince elektronik ayna kaplanır.</p>"
            "<p><strong>2. Açıyı ayarla:</strong> Her küçük hücre sinyali biraz döndürür. "
            "Hepsi birlikte hüzmeyi sizin cihaza çevirir.</p>"
            "<p><strong>3. Kuleye bağla:</strong> Baz istasyonu aynaya 'şu kullanıcıya bak' der. "
            "Ayna kendi başına internet üretmez; yalnızca yönlendirir.</p>"
            "<p><strong>Sonuç:</strong> Yeni kule yerine ucuz yüzey. Kör nokta kapanır, enerji faturası "
            "neredeyse artmaz.</p>"
        ),
    },
    "cell_free": {
        "card": (
            "Bugünkü şebekede her mahallenin bir 'hücresi' vardır. Hücre kenarında sinyal düşer, "
            "kule değişirken arama kopabilir. Hücresiz MIMO'da sokak lambası gibi sık küçük antenler "
            "sizi birlikte taşır; kenar diye bir yer kalmaz. Stadyum, havalimanı ve kalabalık caddede "
            "herkesin hızı daha adil olur."
        ),
        "kicker": "Sorun: hücre kenarında kopma",
        "teach_html": (
            "<div class='teach-item'><div class='teach-label'>Bugünün sorunu</div>"
            "<p>Şebeke, pastayı dilimlere ayırır: her dilim bir kule. Dilimin kenarında hem sizin "
            "sinyaliniz zayıftır hem komşu kule karışır. Yürürken kule değiştirmek (handover) kopma riskidir. "
            "Stadyumda herkes aynı kuleye yığılır, tribünün bir yanı aç kalır.</p></div>"
            "<div class='teach-item'><div class='teach-label'>6G bunu nasıl çözer</div>"
            "<p>Tek dev kule yerine onlarca küçük erişim noktası sizi aynı anda taşır. "
            "'Bu anten senin, şu anten komşunun' ayrımı kalkar. Yazılım hepsini tek sistem gibi yönetir.</p></div>"
            "<div class='teach-item'><div class='teach-label'>Analoji</div>"
            "<p>Tek projektörle sahneyi aydınlatırsanız kenar karanlık kalır. Birçok küçük lamba "
            "oyuncuyu her adımında birlikte takip ederse gölge oluşmaz. Hücresiz MIMO o lamba ağıdır.</p></div>"
            "<div class='teach-item'><div class='teach-label'>Türk Telekom abonesi için ne değişir</div>"
            "<p>Havalimanı yürüyüşü, stadyum maçı, yoğun bulvar: 'kenarda çekmiyor' şikâyeti hedeflenir. "
            "TRL 4 — deneysel; fiberle antenleri merkeze bağlamak pahalıdır, bu yüzden önce yoğun mekânlar adaydır.</p></div>"
        ),
        "arch_html": (
            "<p><strong>Katman 1 — Küçük antenler:</strong> Sokak, tavan, tribün: birçok erişim noktası sizi birlikte taşır.</p>"
            "<p><strong>Katman 2 — Fiber omurga:</strong> Antenler merkeze bağlanır; 'hangi anten ne söylesin' orada kararlaşır.</p>"
            "<p><strong>Katman 3 — Ortak beyin:</strong> Kenar bulut, kenar parazitini faydalı sinyale çevirir. "
            "Hücre kenarı kavramı kalkar.</p>"
            "<p>Fronthaul, MMSE ve ön kodlama için soldan <strong>Uzman Seviyesi</strong> açın.</p>"
        ),
        "principle_html": (
            "<p><strong>1. Dağıt:</strong> Küçük antenler sokağa, tavana, tribüne sık yerleştirilir. "
            "Tek dev kuleye bel bağlanmaz.</p>"
            "<p><strong>2. Ortak taşı:</strong> Telefonunuz birkaç antene aynı anda bağlanır. "
            "Hepsi sizin için konuşur.</p>"
            "<p><strong>3. Merkezde birleştir:</strong> Fiberle bağlı bir beyin, hangisinin ne söyleyeceğini "
            "ayarlar. Kenar paraziti faydalı sinyale dönüşür.</p>"
            "<p><strong>Sonuç:</strong> Yürürken 'kule değişti' hissi kaybolur. Herkes daha adil hız alır.</p>"
        ),
    },
    "thz": {
        "card": (
            "5G hızlıdır ama kablosuz 'boru' hâlâ dardır: hologram, kablosuz veri merkezi, "
            "saniyede film indirme bu boruya sığmaz. Terahertz, radyo ile ışık arasındaki "
            "çok yüksek tonda konuşur; boru çok genişler. Bedeli vardır: duvar, yağmur ve "
            "mesafe sinyali keser. Bu yüzden TRL 3'tür — laboratuvar güçlü, sokak henüz değil."
        ),
        "kicker": "Sorun: kablosuz boru hâlâ dar",
        "teach_html": (
            "<div class='teach-item'><div class='teach-label'>Bugünün sorunu</div>"
            "<p>4G köy yolu, 5G otobandır. Yine de bir veri merkezinin rafları arası trafik veya "
            "gerçek zamanlı hologram, bugünkü kablosuz banta sığmaz. Fiber her yere çekilemez.</p></div>"
            "<div class='teach-item'><div class='teach-label'>6G bunu nasıl çözer</div>"
            "<p>Çok daha tiz bir radyo kullanılır. Frekans yükseldikçe aynı anda taşınabilen veri "
            "miktarı patlar. Hedef: saniyede yüzlerce gigabit, hatta terabit mertebesi.</p></div>"
            "<div class='teach-item'><div class='teach-label'>Analoji</div>"
            "<p>İnce bir bahçe hortumuyla havuz dolduramazsınız. THz, yangın hortumu gibidir — "
            "ama hortum kısadır ve bir yaprak bile ağzını kapatabilir. Bu yüzden kısa mesafe ve "
            "görüş hattı ister.</p></div>"
            "<div class='teach-item'><div class='teach-label'>Türk Telekom abonesi için ne değişir</div>"
            "<p>Kısa vadede cebinizdeki hız değil; veri merkezi rafları arası kablosuz köprü ve "
            "fiber çekilemeyen kuleler arası yedek hattır. Abone deneyimine inmesi yıllar sürer. "
            "Dürüst olgunluk: TRL 3, laboratuvar.</p></div>"
        ),
        "arch_html": (
            "<p><strong>Katman 1 — Çok yüksek tonlu radyo:</strong> Boru genişler; hedef saniyede yüzlerce gigabit / terabittir.</p>"
            "<p><strong>Katman 2 — Dar ışın:</strong> Sinyal el feneri gibi tutulur. Duvar, yağmur, el kesebilir.</p>"
            "<p><strong>Katman 3 — Kısa mesafe işi:</strong> Raf arası, salon, kule köprüsü. Şehir sokağı için değildir.</p>"
            "<p>GaN/InP, emilim denklemi ve Sub-THz spektrum için soldan <strong>Uzman Seviyesi</strong> açın.</p>"
        ),
        "principle_html": (
            "<p><strong>1. Daha tiz konuş:</strong> Radyo ile kızılötesi ışık arasındaki bant açılır. "
            "Boru genişler, daha çok veri sığar.</p>"
            "<p><strong>2. Engeli kabul et:</strong> Su buharı, duvar, hatta bir el sinyali kesebilir. "
            "Bu fizik kuralıdır, yazılımla sihirlenmez.</p>"
            "<p><strong>3. Dar ışın kullan:</strong> Kaybı telafi için sinyal el feneri gibi dar tutulur. "
            "Menzil kısa kalır.</p>"
            "<p><strong>Sonuç:</strong> Doğru yerde (raf arası, salon, kule köprüsü) rekor hız; "
            "yanlış yerde (açık şehir, yağmur) işe yaramaz. Bu yüzden 6G'nin tamamı THz değildir.</p>"
        ),
    },
    "ai_ran": {
        "card": (
            "Bugünkü şebeke, mühendislerin önceden yazdığı kuralları uygular: gece-gündüz, "
            "maç saati-sakin saat aynı ezber. AI-RAN, kuleyi öğrenen bir trafik polisi yapar: "
            "kim nerede sıkıştıysa kaynağı oraya kaydırır, boş kuleyi uyutur. Sonuç: daha az "
            "kesinti, daha düşük elektrik faturası. Karar hâlâ ölçüme dayanır, sihir değildir."
        ),
        "kicker": "Sorun: şebeke ezber kural okur",
        "teach_html": (
            "<div class='teach-item'><div class='teach-label'>Bugünün sorunu</div>"
            "<p>Klasik şebeke 'saat 02:00 ise kapasiteyi düşür' gibi sabit tarifelerle yürür. "
            "Maç uzarsa, konser biterse, deprem olursa tarife geç kalır. Boş kuleler gece de "
            "elektrik yer. Arıza çoğu zaman olduktan sonra fark edilir.</p></div>"
            "<div class='teach-item'><div class='teach-label'>6G bunu nasıl çözer</div>"
            "<p>Yazılım canlı trafiği izler ve milisaniyede ayar değiştirir: sıkışan mahalleye "
            "kaynak, boş kuleye uyku, arızaya erken uyarı. Yapay zekâ burada 'sohbet botu' değil; "
            "kule ayarlarını yöneten bir karar motorudur.</p></div>"
            "<div class='teach-item'><div class='teach-label'>Analoji</div>"
            "<p>Sabit zamanlı trafik ışığı vs. kavşağı kamerayla gören akıllı ışık. AI-RAN ikincisidir: "
            "kuyruk uzayınca yeşili uzatır, gece kimse yoksa kırmızıda bekletmez.</p></div>"
            "<div class='teach-item'><div class='teach-label'>Türk Telekom abonesi için ne değişir</div>"
            "<p>Maç çıkışı çekmeme, gece elektrik israfı, arızanın aboneyi vurması: bunların hedefidir. "
            "TRL 5 — Open RAN denemeleri var, 'hiç insan yok' iddiası henüz sahada kanıtlanmış değildir.</p></div>"
        ),
        "arch_html": (
            "<p><strong>Katman 1 — Ölçüm:</strong> Kule canlı trafiği, ısınmayı ve kopmayı okur.</p>"
            "<p><strong>Katman 2 — Karar yazılımı:</strong> Sıkışan mahalleye kaynak, boş kuleye uyku, "
            "arıza belirtisine erken uyarı.</p>"
            "<p><strong>Katman 3 — Uygulama:</strong> Ayar milisaniyede kuleye yazılır. "
            "İnsan her saniye tarife yazmaz; denetim kalkmaz.</p>"
            "<p>O-RAN RIC, xApp/rApp ve otokodlayıcı PHY için soldan <strong>Uzman Seviyesi</strong> açın.</p>"
        ),
        "principle_html": (
            "<p><strong>1. Ölç:</strong> Kule kimlerin nerede sıkıştığını, hangi antenin ısındığını "
            "sürekli okur.</p>"
            "<p><strong>2. Karar ver:</strong> Yazılım 'bu mahalleye kapasite', 'şu kuleyi uyut', "
            "'şu donanım bozulmak üzere' der. İnsan her saniye kural yazmaz.</p>"
            "<p><strong>3. Uygula ve öğren:</strong> Sonuç iyiyse politika kalır, kötüyse düzeltilir. "
            "Enerji ve hız birlikte hedeflenir.</p>"
            "<p><strong>Sonuç:</strong> Şebeke otonom trafik polisi olur. Yine de model yanlış öğrenmesin "
            "diye mühendis denetimi kalkmaz — kara kutu riski dezavantajlar sekmesinde durur.</p>"
        ),
    },
    "ntn": {
        "card": (
            "Karasal kule şehir ve yolu kapsar; dağ, açık deniz ve enkaz bölgesi boş kalır. "
            "NTN, alçak yörünge uydusunu aynı telefon şebekesine bağlar: özel uydu telefonu "
            "şart değildir. Depremde kule yıkılsa bile arama yolu gökten açık kalabilir. "
            "Bedeli: yer kulesine göre biraz daha gecikme. TRL 6 — yedi teknolojinin en olgunu."
        ),
        "kicker": "Sorun: kule her yere yetişmez",
        "teach_html": (
            "<div class='teach-item'><div class='teach-label'>Bugünün sorunu</div>"
            "<p>Kapsama, kule ve fiberin ulaştığı yer kadardır. Mezra, gemi, uçak ve afet sahası "
            "bu haritanın dışında kalır. Klasik uydu telefonu ayrı cihaz, ayrı abonelik ister.</p></div>"
            "<div class='teach-item'><div class='teach-label'>6G bunu nasıl çözer</div>"
            "<p>Alçak yörünge uyduları (ve yüksek irtifa platformları) karasal şebekeyle tek sistem "
            "gibi çalışır. Hedef: standart telefonun, kule yokken göğe bağlanması. Şehirde kule "
            "önceliklidir; boşlukta uydu devreye girer.</p></div>"
            "<div class='teach-item'><div class='teach-label'>Analoji</div>"
            "<p>Karasal şebeke sokak lambasıdır — yolu aydınlatır, ormanı değil. NTN yukarıdan "
            "tutan bir projektördür. Lambanın olduğu yerde lamba kullanılır; lamba yoksa projektör.</p></div>"
            "<div class='teach-item'><div class='teach-label'>Türk Telekom abonesi için ne değişir</div>"
            "<p>Afet hattı, balıkçı filosu, Doğu Anadolu kırsalı: kapsama vaadi buradadır. "
            "TRL 6 — standartlaşma ve ticari deneme en ileride olan teknolojidir. Yine de uydu "
            "gecikmesi yer kulesinden fazladır; şehir içi 6G'nin yerini almaz.</p></div>"
        ),
        "arch_html": (
            "<p><strong>Katman 1 — Gök:</strong> Alçak yörünge uydusu veya yüksek irtifa platformu boş coğrafyayı tutar.</p>"
            "<p><strong>Katman 2 — Yer kapısı:</strong> Uydu sinyali Türk Telekom yer istasyonuna iner, karasal çekirdeğe bağlanır.</p>"
            "<p><strong>Katman 3 — Sizin telefon:</strong> Hedef özel çanak değil, mevcut SIM ile göğe düşebilmektir. "
            "Şehirde kule önceliklidir.</p>"
            "<p>Doppler, feeder link ve Rel-17 NTN için soldan <strong>Uzman Seviyesi</strong> açın.</p>"
        ),
        "principle_html": (
            "<p><strong>1. Yeri doldur:</strong> Şehir ve yol kulelerle kalır. Boş coğrafyada "
            "uydu veya yüksek irtifa platformu konuşur.</p>"
            "<p><strong>2. Aynı numarayı koru:</strong> Hedef, özel çanak antenli uydu telefonu değil; "
            "mevcut SIM ve telefonla göğe düşebilmektir.</p>"
            "<p><strong>3. Gecikmeyi yönet:</strong> Uydu uzaktadır ve hızlı hareket eder. "
            "Şebeke bu kaymayı telafi eder; yine de yer kulesi kadar 'anında' olmaz.</p>"
            "<p><strong>Sonuç:</strong> Kapsama deliği kapanır, afet hattı yedeklenir. "
            "Bu, şehirdeki 5G/6G kulesinin rakibi değil tamamlayıcısıdır.</p>"
        ),
    },
    "ambient_iot": {
        "card": (
            "Depodaki her koli, tarladaki her nem ölçer, sayaçtaki her düğme bugün pil ister. "
            "Pil bitince cihaz ölür; milyonlarca pili değiştirmek imkânsızdır. Pilsiz IoT, "
            "havadaki radyo dalgasından kırıntı enerji toplayıp 'buradayım' der. Türk Telekom "
            "için lojistik, tarım ve sayaç: bakım ekibi göndermeden izleme."
        ),
        "kicker": "Sorun: her nesneye pil takılmaz",
        "teach_html": (
            "<div class='teach-item'><div class='teach-label'>Bugünün sorunu</div>"
            "<p>Nesnelerin interneti pille yürür. Milyon koli, sera ve sayaçta pili değiştirmek "
            "işçilik ve atık demektir. Pahalı sensör de her ürüne yapıştırılmaz.</p></div>"
            "<div class='teach-item'><div class='teach-label'>6G bunu nasıl çözer</div>"
            "<p>Etiketin kendi pili yoktur. Havadaki kule veya Wi-Fi dalgasından kırıntı elektrik "
            "toplar; bu enerjiyle kısa bir 'buradayım / sıcaklık normal' mesajı yollar. "
            "Kendi vericisini tam güç çalıştırmaz, gelen dalgayı hafifçe yansıtarak konuşur.</p></div>"
            "<div class='teach-item'><div class='teach-label'>Analoji</div>"
            "<p>Eski hesap makinelerindeki güneş paneli: pilsiz, ışıktan yaşar. Ambient IoT aynı "
            "fikirdir; ışık yerine radyo dalgasını 'güneş' kabul eder. Film izlemez, yalnızca "
            "kısa durum bildirir.</p></div>"
            "<div class='teach-item'><div class='teach-label'>Türk Telekom abonesi için ne değişir</div>"
            "<p>Depo paleti, sera nemi, su sayacı: yıllarca bakım ekibi gitmeden izlenebilir. "
            "TRL 4 — menzil kısa, veri yavaştır; telefonunuzun yerini almaz. Trilyon nesne vaadi "
            "standartlaşma (çalışma kalemi) aşamasındadır, sahada her rafa yapışmış değildir.</p></div>"
        ),
        "arch_html": (
            "<p><strong>Katman 1 — Pilsiz etiket:</strong> Koli, sera, sayaç: ucuz etiket pil yuvası taşımaz.</p>"
            "<p><strong>Katman 2 — Enerji kırıntısı:</strong> Kule veya Wi-Fi dalgası elektriğe çevrilir; "
            "etiket gelen dalgayı hafifçe yansıtarak konuşur.</p>"
            "<p><strong>Katman 3 — Okuyucu ve bulut:</strong> Yakın kule zayıf yankıyı duyar; "
            "Türk Telekom IoT platformuna 'nerede / kaç derece' yazar.</p>"
            "<p>Rectenna, backscatter ve Rel-19 Ambient IoT için soldan <strong>Uzman Seviyesi</strong> açın.</p>"
        ),
        "principle_html": (
            "<p><strong>1. Topla:</strong> Etiket havadaki radyo kırıntısını elektriğe çevirir. "
            "Pil yuvası yoktur.</p>"
            "<p><strong>2. Yansıt:</strong> Kendi vericisini yakmaz. Gelen dalgayı 'evet/hayır' "
            "diye hafifçe değiştirerek konuşur. Bu yüzden menzil kısadır.</p>"
            "<p><strong>3. Oku:</strong> Yakındaki kule veya okuyucu bu zayıf yankıyı duyar ve "
            "buluta 'koli 14, 4 °C' diye yazar.</p>"
            "<p><strong>Sonuç:</strong> Ucuz, pilsiz, uzun ömürlü iz. Video veya ses taşımaz; "
            "doğru işi (nerede / kaç derece) çözer.</p>"
        ),
    },
}
