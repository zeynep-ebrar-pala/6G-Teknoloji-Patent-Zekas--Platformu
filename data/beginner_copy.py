"""
Temel seviye — kavramsal temel.
Jargon yasak değil: ilk kullanımda açılır. Uzman denklemler technologies + expert_depth'te.
Her teknoloji: nedir, neden, problem, nasıl, zihinsel model, analoji→teknik karşılık,
ne zaman / ne zaman değil, neyle karıştırılmamalı, gerçek dünya, TT etkisi.
"""

BEGINNER_COPY = {
    "isac": {
        "card": (
            "Sisli bir boğazda kule internet verir ama «karşıda bir gemi var mı» diye bakamaz; "
            "kamera görüşünü kaybeder, ayrı radar kamyonu hem pahalıdır hem spektrumu kirletir. "
            "ISAC (Integrated Sensing and Communication — Entegre Algılama ve İletişim) "
            "aynı radyo dalgasını hem veri taşımak hem yankıdan ölçüm yapmak için kullanır: "
            "gecikme mesafeyi, Doppler kayması hızı verir. "
            "Bedeli, bu ölçümün laboratuvar dışında güvenilir kalmasıdır; "
            "Türk Telekom için adaylık budur, mahalle ürünü değil. "
            "TRL 4 seviyesindedir: yöntem laboratuvarda doğrulanmıştır, "
            "ancak sahada gerçek bir şebekede henüz denenmemiştir."
        ),
        "kicker": "Sorun: kule konuşur, göremez",
        "what": (
            "ISAC (Integrated Sensing and Communication — Entegre Algılama ve İletişim), "
            "aynı frekans kaynağı, aynı anten ve çoğu zaman aynı dalga şekli üzerinde hem "
            "kullanıcıya bit taşımayı hem çevreden mesafe/hız/açı çıkarmayı birlikte tasarlayan "
            "radyo mimarisidir. Ayrı bir 'radar kutusu' eklemek değil; haberleşme dalgasının "
            "yansımasını da bilgi saymaktır."
        ),
        "why_needed": (
            "Spektrum ve kent arazisi pahalıdır. Trafik güvenliği, alçak irtifa dron koridoru ve "
            "kamerasız farkındalık ayrı radar ağı isterse hem maliyet hem girişim (EMI) büyür. "
            "Şebeke zaten her yere RF (Radio Frequency — radyo frekansı) basıyorsa, aynı enerjiyi "
            "ikinci bir duyu olarak kullanmak operatör için rasyonel bir ihtiyaçtır."
        ),
        "problem": (
            "Klasik baz istasyonu veri taşır; çevreyi 'görmez'. Kamera sis, yağmur ve karanlıkta "
            "körleşir; gizlilik de pahalıdır. Ayrı otomotiv/askeri radar spektrumu şebeke spektrumuna "
            "komşu girişim üretir. Sonuç: ya kör nokta kalır ya da çift altyapı ödenir."
        ),
        "how_steps": [
            "Gönder: gNB (next-generation Node B — 5G/6G baz istasyonu) kullanıcıya giden OFDM veya OTFS dalga şeklini yayınlar; ekstra kamyon yoktur.",
            "Dinle: Araç, duvar veya drondan dönen eko gecikme (mesafe), Doppler (hız) ve dizi faz farkı AoA (Angle of Arrival — geliş açısı) verir.",
            "Ayır: Zaman, frekans veya kodda dik (orthogonal) paylaşım, konuşma bitleri ile yankının birbirini bozmamasını hedefler.",
            "Aktar: Nokta bulutu veya iz özeti kenar sunucuya gider (trafik, UTM, enkaz senaryoları).",
        ],
        "mental_model": (
            "Bunu zihninde şöyle kur: kule el feneri değil, yarasa gibi hem bağırır hem dinler. "
            "Aynı 'ses' hem sizin kulağınıza (veri) gider hem duvardan dönüp kuleye mesafe söyler. "
            "İki ayrı ağız değil, tek ağız, iki kulak işidir."
        ),
        "analogy": (
            "Yarasa karanlıkta gözle değil, sesin geri dönüşüyle 'görür'. ISAC kulesi de yayınlar "
            "ve yankıyı dinler — ama aynı anda sizinle konuşmayı da sürdürür."
        ),
        "analogy_technical_map": (
            "Bu analojinin teknik karşılığı: ultrason yerine RF taşıyıcı; 'gecikme = 2R/c' radar "
            "menzili; 'sesin kayması' Doppler kayması; 'kulak çifti' ise çok antenli AoA kestirimidir. "
            "Yarasa tek görevlidir; ISAC'de iletişim kapasitesi ile algılama CRB'si aynı güç bütçesini paylaşır."
        ),
        "when_used": (
            "Görüşün bozulduğu (sis, gece) ve kamera istemediğiniz (gizlilik) senaryolarda; "
            "mevcut kule geometrisinin zaten yolu, boğazı veya hava koridorunu gördüğü yerde; "
            "ayrı radar spektrumunun pahalı veya siyasi olarak zor olduğu operatör şebekelerinde."
        ),
        "when_not": (
            "Santimetre altı 'her zaman, her mahallede' vaadi için değil — bu literatür hedefidir, "
            "bu platformda saha ölçümü yoktur. Yoğun çoklu yansıma (clutter) ve gizlilik düzenlemesi "
            "çözülmeden kamusal izleme ürünü gibi sunulmamalıdır. THz kadar geniş bant yoksa "
            "menzil çözünürlüğü fiziken sınırlı kalır."
        ),
        "not_to_confuse": (
            "Klasik radar + yanına konmuş 5G kulesi ISAC değildir; o iki sistemdir. "
            "Kamerayla bilgisayarla görme de değildir: RF yankısı görüntü pikseli üretmez. "
            "Ambient IoT geri saçılımı da farklıdır: orada pilsiz etiket kasıtlı konuşur; "
            "ISAC'de hedef çoğu zaman işbirlikçi olmayan bir yansıtıcıdır."
        ),
        "real_world": (
            "Otomotiv V2X araştırma test yatakları, alçak irtifa dron yönetimi çalışmaları, "
            "3GPP Rel-19 ISAC çalışma kalemi ve Avrupa Hexa-X-II mimari raporlarında karşınıza çıkar. "
            "Ticari 'her kule radar' ürünü değildir."
        ),
        "tt_impact": (
            "Boğaz sisinde deniz trafiği, şehir içi dron koridoru, enkaz altı hareket: mevcut "
            "kule adaylığıdır. TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi) 4: "
            "laboratuvar ve erken saha; her abone mahallesinde yok."
        ),
        "principle_html": (
            "<p><strong>1. Gönder:</strong> "
            "<strong>gNB</strong> (next-generation Node B — 5G/6G baz istasyonu) kullanıcıya giden "
            "radyo çerçevesini yayınlar. Yeni bir radar kamyonu yoktur.</p>"
            "<p><strong>2. Dinle:</strong> Sinyal araç, duvar veya drondan seker. Gecikme mesafe, "
            "<strong>Doppler</strong> kayması hız, dizi faz farkı <strong>AoA</strong> "
            "(Angle of Arrival — geliş açısı) verir.</p>"
            "<p><strong>3. Ayır:</strong> Yazılım, sizin bitlerinizle yankıyı zaman/frekans/kodda "
            "ayırmaya çalışır. Biri internet, diğeri haritadır.</p>"
            "<p><strong>Sonuç:</strong> Tek RF zinciri, iki iş. Operatör için spektrum ve anten tasarrufu "
            "adaylığı; şehir için kamera koymadan farkındalık. Ödünleşme: aynı güç hem bit hem eko içindir.</p>"
        ),
        "arch_html": (
            "<p><strong>Katman 1 — Radyo ve anten (PHY):</strong> Mevcut baz istasyonu hem veri yollar "
            "hem eko dinler. Masif MIMO dizi, açı kestirimi için faz farkı sağlar.</p>"
            "<p><strong>Katman 2 — Kaynak paylaşımı (MAC):</strong> Konuşma ile yankı birbirini bozmasın "
            "diye zaman, frekans veya kod paylaştırılır. Bu 'sihir' değil, ödünleşmedir.</p>"
            "<p><strong>Katman 3 — Kenar işleme:</strong> Mesafe/hız/açı özeti Türk Telekom kenar bulutuna "
            "gider (trafik, dron, enkaz). Ham I/Q her zaman merkeze taşınmaz; bant pahalıdır.</p>"
            "<p>Dalga şekli (OFDM/OTFS), CRB ve 3GPP Rel-19 için uzman katmanı bu sayfada, "
            "formül kartlarında durur.</p>"
        ),
    },
    "ris": {
        "card": (
            "Yüksek frekanslı dalga düz gitmeye eğilimlidir; köşeyi dönmez, asansör boşluğunda kaybolur. "
            "Her kör nokta için yeni kule dikmek pahalı ve pratik değildir. "
            "RIS (Reconfigurable Intelligent Surface — Yeniden Yapılandırılabilir Akıllı Yüzey) "
            "cepheye asılan elektronik bir aynadır: yüzeydeki her küçük eleman dalganın fazını kaydırır, "
            "hüzme size döner. Kendi başına sinyal üretmediği için enerji tüketimi kırıntı kadardır. "
            "TRL 5 seviyesindedir: prototip üretilmiş ve saha denemeleri yapılmıştır, "
            "ancak henüz ticari bir kulede kullanılmamaktadır."
        ),
        "kicker": "Sorun: dalga köşeyi dönemez",
        "what": (
            "RIS, yüzlerce veya binlerce ayarlanabilir yansıtıcı elemandan oluşan bir yüzeydir. "
            "Elemanlar PIN diyot, varaktör veya benzeri anahtarla gelen dalganın fazını 0–2π aralığında "
            "kaydırır. Kendi başına internet üretmez; mevcut gNB'nin yayınını istenen UE'ye (User Equipment — "
            "kullanıcı cihazı) yönlendirir."
        ),
        "why_needed": (
            "mmWave ve daha yüksek bantlarda duvar ve köşe kaybı şiddetlidir. Her kör noktaya kule "
            "hem CAPEX hem kent estetiği hem EMC yüküdür. Pasif veya yarı-pasif bir yüzey, "
            "yolu 'akıllı ortam' haline getirerek kapsama deliğini ucuza kapatma vaadidir."
        ),
        "problem": (
            "Radyo dalgası yüksek frekansta ışığa benzer: görüş hattı (LoS) yoksa hız düşer veya bağ kopar. "
            "Plaza camı, avlu, tünel kıvrımı 'çekmiyor' şikâyetinin fiziğidir. Röle (aktif tekrarlayıcı) "
            "ise kendi RF zinciri, güç ve girişimini taşır."
        ),
        "how_steps": [
            "Yüzeyi yerleştir: cephe, cam veya tünel duvarı — yüzey kendi başına baz istasyonu değildir.",
            "Fazı ayarla: her eleman küçük bir faz kayması uygular; hepsi birlikte hüzme şekillendirir (Snell'in ötesinde yönlendirme).",
            "Kule komut verir: gNB, RIS denetleyicisine 'şu kullanıcıya bak' der; kontrol hattı ince ve düşük güçlüdür.",
            "Sonuç: engellenen doğrudan yol yerine kontrollü yansıma yolu oluşur.",
        ],
        "mental_model": (
            "Bunu zihninde şöyle kur: karanlık koridorda el feneri köşeyi dönemez. Ayarlanabilir bir ayna "
            "ışığı odaya taşır. Ayna lamba değildir; lambanın ışığını yönlendirir. RIS de verici değil, "
            "programlanabilir yansıtıcıdır."
        ),
        "analogy": (
            "Karanlık odada el feneri duvarın arkasını aydınlatamaz. Açısı ayarlanan ayna ışığı büküp "
            "görünmeyen odaya taşır. RIS, radyo için o ayarlanabilir aynadır."
        ),
        "analogy_technical_map": (
            "Bu analojinin teknik karşılığı: 'ayna açısı' her elemanın fazı θ_n; 'odaklanmış demet' "
            "dizi faktörü; 'lamba' Tx–RIS kanalı G; 'oda' RIS–Rx kanalı h_r. Ayna ışığı zayıflatır: "
            "çift yol kaybı (Tx→RIS→Rx) aktiftir. N eleman birlikte, ideal koşullarda güç ~N² ölçeklenir."
        ),
        "when_used": (
            "N-LoS sokak, tünel kıvrımı, stadyum tribünü, plaza içi mmWave, tarihi dokuya kule dikilemeyen "
            "alan. Enerji ve CAPEX'in aktif röleden düşük kalmasının istendiği yerler."
        ),
        "when_not": (
            "Yüzeyin kanalı kestiremediği (pasif eleman alıcı değildir) ve denetleyici gecikmesinin "
            "kullanıcı hızına yetmediği yerde beklenen kazanç düşer. Çift yol kaybı yüzünden 'kule yerine "
            "her yere RIS yapıştır' çözümü menzili sihirle uzatmaz. %90 enerji tasarrufu literatür/hedef "
            "karşılaştırmasıdır; bu platformda saha faturası ölçülmemiştir."
        ),
        "not_to_confuse": (
            "Aktif röle veya küçük hücre değildir — kendi yüksek güçlü vericisi yoktur. "
            "Metamalzeme 'görünmez pelerin' pazarlaması da değildir; Maxwell yasaları geçerlidir, "
            "yalnızca sınır koşulu programlanır. ISAC ile birlikte kullanılabilir ama RIS tek başına radar değildir."
        ),
        "real_world": (
            "ETSI RIS ISG, 3GPP Rel-19/20 çalışma kalemleri, operatör PoC'leri (cephe ve iç mekân panelleri). "
            "Tak-çalıştır ticari emtia henüz her binada yoktur."
        ),
        "tt_impact": (
            "Tarihi yarımada, tünel, plaza camı: kule dikmeden kapsama adayı. TRL 5 — ilgili ortamda "
            "prototip; abone şebekesinin varsayılan parçası değil."
        ),
        "principle_html": (
            "<p><strong>1. Yüzeyi as:</strong> Bina, cam veya duvara ince elektronik yansıtıcı kaplanır. "
            "Bu bir baz istasyonu değildir.</p>"
            "<p><strong>2. Fazı kaydır:</strong> Her küçük eleman gelen dalganın fazını değiştirir. "
            "Hepsi birlikte hüzmeyi sizin <strong>UE</strong> cihazınıza çevirir.</p>"
            "<p><strong>3. Kuleye bağla:</strong> <strong>gNB</strong> denetleyiciye 'şu kullanıcıya bak' der. "
            "Kontrol hattı ince ve düşük güçlüdür.</p>"
            "<p><strong>Sonuç:</strong> Yeni kule yerine yönlendirilmiş yansıma. Kör nokta kapanır; "
            "bedeli kanal kestirimi ve çift yol kaybıdır.</p>"
        ),
        "arch_html": (
            "<p><strong>Katman 1 — Yüzey:</strong> PCB veya esnek film üzerinde PIN/varaktör elemanlar. "
            "Aktif RF zinciri yoktur veya çok azdır.</p>"
            "<p><strong>Katman 2 — Denetleyici:</strong> FPGA/mikrodenetleyici, eleman voltajlarını "
            "gNB emrine göre değiştirir.</p>"
            "<p><strong>Katman 3 — Kontrol hattı:</strong> Kule ile yüzey arasında düşük bit hızlı C-düzlemi. "
            "Yüzey 'kendi başına internet' üretmez.</p>"
            "<p>Metamalzeme, N² ölçeği ve kanal kestirim zorluğu uzman formül kartlarındadır.</p>"
        ),
    },
    "cell_free": {
        "card": (
            "Klasik şebekede her mahallenin bir hücresi vardır; kenara yaklaşınca sinyal düşer, "
            "kule değişince (handover) kopma riski doğar. "
            "Hücresiz Masif MIMO (Multiple-Input Multiple-Output — Çok Girişli Çok Çıkışlı) "
            "bu sınırı kaldırır: sokak lambası sıklığındaki erişim noktaları sizi birlikte taşır, "
            "kenar diye bir yer kalmaz. Bedeli, antenleri merkeze bağlayan "
            "fronthaul (ön bağlantı) fiberidir. "
            "TRL 4 seviyesindedir, yani hâlâ deneysel aşamadadır; "
            "ilk uygulama alanı olarak stadyum ve havalimanı gibi yoğun mekânlar düşünülmektedir."
        ),
        "kicker": "Sorun: hücre sınırında zayıflar",
        "what": (
            "Hücresiz Massive MIMO (Multiple-Input Multiple-Output — çoklu giriş çoklu çıkış), "
            "kullanıcıyı tek bir hücreye bağlamak yerine coğrafyaya yayılmış birçok erişim noktasının "
            "(AP) aynı anda, aynı frekansta, merkezi veya yarı-dağıtık işlemle hizmet verdiği mimaridir. "
            "Hücre sınırı tasarım hedefi olarak ortadan kalkar."
        ),
        "why_needed": (
            "Kapasite ve adalet hücre kenarında çöker: sizin sinyaliniz zayıf, komşu kule parazittir. "
            "Stadyum ve terminalde herkes aynı makro kuleye yığılır. Dağıtık antenler hem yolu kısaltır "
            "hem paraziti işbirliğiyle faydalı sinyale çevirme imkânı verir."
        ),
        "problem": (
            "Hücresel pasta dilimleridir. Dilim kenarında SINR (Signal-to-Interference-plus-Noise Ratio — "
            "sinyal-parazit-artı-gürültü oranı) düşer. Yürüyen abone handover yapar; başarısızlık kopmadır. "
            "Tek kule + çok kullanıcı = tribünün bir yanı aç, diğer yanı tok."
        ),
        "how_steps": [
            "Dağıt: düşük karmaşıklıklı AP'ler tavan, tribün, cadde — makro kule tek başına taşımaz.",
            "Bağla: AP'ler yüksek hızlı fronthaul ile CPU/kenar buluta gider; senkronizasyon şarttır.",
            "Ortak taşı: birkaç AP sizin için aynı anda ön kodlama (precoding) yapar.",
            "Paraziti işle: komşu kullanıcıya giden enerji, işbirliğiyle bastırılır veya faydaya çevrilir.",
        ],
        "mental_model": (
            "Bunu zihninde şöyle kur: tek projektörle sahne kenarı karanlık kalır. Birçok küçük lamba "
            "oyuncuyu her adımında birlikte takip ederse gölge oluşmaz. Lambalar ayrı 'hücre' değildir; "
            "tek aydınlatma sistemidir."
        ),
        "analogy": (
            "Tek projektör kenarı karanlık bırakır. Birçok küçük lamba oyuncuyu birlikte takip ederse "
            "gölge oluşmaz. Hücresiz MIMO o lamba ağıdır."
        ),
        "analogy_technical_map": (
            "Bu analojinin teknik karşılığı: lamba = AP; kablo = fronthaul; ortak takip = ortak ön kodlama "
            "w_mk; gölge = hücre kenarı paraziti; 'tek sistem' = CPU'da MMSE veya sıfır zorlamalı (ZF) "
            "matris. Fiber yoksa lamba ağı kördür — hesap merkeze veya dağıtık kümeye gitmek zorundadır."
        ),
        "when_used": (
            "Yüksek kullanıcı yoğunluğu, hareket, adalet ihtiyacı: stadyum, havalimanı, dizi üretim hattı, "
            "yoğun bulvar. Makro kule estetiğinin istenmediği iç mekânlar."
        ),
        "when_not": (
            "Seyrek kırsalda her direğe fiber çekmek CAPEX olarak anlamsızdır; NTN veya makro 4G/5G "
            "daha rasyoneldir. Fronthaul gecikmesi ve senkron bozulursa 'hücresiz' kazanç tersine döner. "
            "5x–10x spektral kazanç literatür aralığıdır; bu platformda saha ölçümü yoktur."
        ),
        "not_to_confuse": (
            "Küçük hücre (small cell) ormanından farklıdır: small cell hâlâ hücredir, kenarı vardır. "
            "Klasik CoMP (koordineli çok nokta) hücresiz MIMO'nun atasıdır ama 'hücre yok' varsayımına "
            "kadar gitmez. Wi-Fi roaming de değildir: burada aynı anda çok AP sizin sembolünüzü taşır."
        ),
        "real_world": (
            "Akademik çekirdek (dağıtık MIMO literatürü), 3GPP dağıtık MIMO çalışma grupları, "
            "satıcı laboratuvar gösterimleri. Operatör stadyum PoC adayı; şehir geneli ürün değil."
        ),
        "tt_impact": (
            "Havalimanı yürüyüşü, stadyum, sanayi deposu: kenar şikâyeti hedeflenir. TRL 4. "
            "Önce yoğun mekân, çünkü fiber pahalıdır."
        ),
        "principle_html": (
            "<p><strong>1. Dağıt:</strong> Küçük erişim noktaları sokağa, tavana, tribüne sık yerleştirilir. "
            "Tek dev kuleye bel bağlanmaz.</p>"
            "<p><strong>2. Ortak taşı:</strong> Telefonunuz birkaç AP'ye aynı anda bağlanır. "
            "Hepsi sizin için konuşur.</p>"
            "<p><strong>3. Merkezde birleştir:</strong> Fiber fronthaul ile bağlı işlemci, "
            "<strong>MMSE</strong> (Minimum Mean Square Error — minimum ortalama kare hata) "
            "tipi ön kodlama ile hangisinin ne söyleyeceğini ayarlar.</p>"
            "<p><strong>Sonuç:</strong> Yürürken 'kule değişti' hissi kaybolur. Adalet artar; "
            "fatura fronthaul ve hesap yüküdür.</p>"
        ),
        "arch_html": (
            "<p><strong>Katman 1 — Dağıtık AP:</strong> Düşük karmaşıklıklı radyo; yerel Tx/Rx, ağır hesap yok.</p>"
            "<p><strong>Katman 2 — Fronthaul:</strong> Fiber (eCPRI / RoF). Senkron yoksa ortak hüzme bozulur.</p>"
            "<p><strong>Katman 3 — CPU / kenar bulut:</strong> Ortak kestirim ve ön kodlama. "
            "Hücre kenarı kavramı tasarım olarak kalkar.</p>"
            "<p>SINR formülü ve MMSE varsayımları uzman kartlarındadır.</p>"
        ),
    },
    "thz": {
        "card": (
            "5G hızlıdır ama kablosuz boru hâlâ dardır; sunucular arası terabit hızındaki aktarım "
            "veya gerçek zamanlı hologram bu boruya sığmaz. "
            "THz (terahertz) milimetre dalga ile kızılötesi arasındaki spektrumdur; "
            "bant genişliği katbekat artar. Bedeli fiziktir: su buharı emer, duvar keser, mesafe kısalır. "
            "TRL 3 seviyesindedir: laboratuvar sonuçları güçlüdür, "
            "ama sokaktaki bir şebekede henüz kullanılmamaktadır. "
            "Ayrıca 6G'nin tamamı THz teknolojisine dayanmamaktadır."
        ),
        "kicker": "Sorun: veri borusu hâlâ dar",
        "what": (
            "THz iletişimi, kabaca 0,1–10 THz (yüzlerce GHz üstü) diliminde, milimetre dalga ile "
            "optik arasında kalan spektrumu kullanarak onlarca GHz bant genişliği açma girişimidir. "
            "Shannon: kapasite önce bant genişliği B ile büyür; SNR ikinci terimdir."
        ),
        "why_needed": (
            "Sub-6 GHz ve hatta mmWave, veri merkezi içi mesh, kuleler arası ultra backhaul ve "
            "ileride holografik/AR-VR bit hızı için dar kalabilir. Fiber her raf arasına ve her "
            "tepeye çekilemez. THz, 'kablosuz fiber' adayıdır — doğru mesafede."
        ),
        "problem": (
            "Frekans yükseldikçe FSPL (Free-Space Path Loss — serbest uzay yol kaybı) ve moleküler "
            "emilim büyür. Bir el, yaprak, yağmur linki kesebilir. Donanım (InP, GaN, ADC hızı) pahalı "
            "ve olgundur değil. Bu yüzden TRL düşüktür."
        ),
        "how_steps": [
            "Spektrumu aç: 100 GHz üzeri pencereler; hedef onlarca GHz B.",
            "Kaybı kabul et: L(f,d) = FSPL × e^{K(f)d}; K(f) su buharı çizgilerinde sıçrar.",
            "Dar hüzme: dizi kazancı kaybı telafi eder; hizalama hassaslaşır.",
            "Kısa menzil işi seç: raf, salon, kule köprüsü — şehir sokağı değil.",
        ],
        "mental_model": (
            "Bunu zihninde şöyle kur: ince bahçe hortumuyla havuz dolduramazsınız. THz yangın hortumudur — "
            "ama hortum kısadır ve bir yaprak ağzını kapatabilir. Bu yazılım hatası değil, elektromanyetiktir."
        ),
        "analogy": (
            "İnce hortum / yangın hortumu: THz çok veri taşır, kısa ve kırılgandır. "
            "Görüş hattı ve kuru hava ister."
        ),
        "analogy_technical_map": (
            "Bu analojinin teknik karşılığı: hortum kesiti = bant genişliği B; hortum uzunluğu = d; "
            "yaprak = tıkanma (blockage); su buharı = K(f) emilim; basınç = EIRP ve dizi kazancı. "
            "Shannon C = B log2(1+SNR) der ki B'yi 50 GHz yapmak logaritmik SNR'den çok daha etkilidir — "
            "SNR'yi emilim yerse B tek başına yetmez."
        ),
        "when_used": (
            "Kablosuz veri merkezi, kısa menzil backhaul/fronthaul, laboratuvar spektroskopi, "
            "kontrollü iç mekân. Görüş hattı sağlanabilen, mesafenin onlarca–yüzlerce metre olduğu yer."
        ),
        "when_not": (
            "Açık şehir makrosu, yağmurlu uzun hop, cepten-cepte kilometre. '1 Tbps her aboneye' "
            "pazarlama cümlesidir; bu platformda ölçülmedi, fizik menzili sınırlar. Tıbbi nanosensör "
            "vaadi araştırma ufkudur, Rel-19 ticari özellik değildir."
        ),
        "not_to_confuse": (
            "5G mmWave (28–39 GHz bandı) THz değildir; alt komşudur. Serbest uzay optiği (lazer) "
            "de farklıdır: THz hâlâ elektronik/RF tarafına yakındır. ISAC THz dalga şekli kullanabilir "
            "ama THz tek başına algılama standardı değildir."
        ),
        "real_world": (
            "IEEE 802.15.3d, ITU-R spektrum çalışmaları, 3GPP 'NR beyond 52.6 GHz' raporları, "
            "satıcı Sub-THz (ör. 140 GHz) gösterimleri. Abone telefonunda varsayılan bant değil."
        ),
        "tt_impact": (
            "Kısa vadede cep hızı değil; veri merkezi rafları ve fiber çekilemeyen kule köprüsü. "
            "TRL 3. Dürüst konum: laboratuvar."
        ),
        "principle_html": (
            "<p><strong>1. Daha tiz konuş:</strong> mmWave ile kızılötesi arasındaki bant açılır. "
            "Bant genişliği büyür, daha çok bit sığar.</p>"
            "<p><strong>2. Engeli kabul et:</strong> Su buharı, duvar, el sinyali kesebilir. "
            "Bu fizik kuralıdır.</p>"
            "<p><strong>3. Dar ışın kullan:</strong> Kaybı telafi için hüzme el feneri gibi dar tutulur. "
            "Menzil kısa kalır.</p>"
            "<p><strong>Sonuç:</strong> Doğru yerde (raf, salon, kule köprüsü) rekor hız adayı; "
            "yanlış yerde işe yaramaz. 6G = yalnızca THz değildir.</p>"
        ),
        "arch_html": (
            "<p><strong>Katman 1 — RF ön uç:</strong> GaN/InP/grafen adayları, çip üstü anten. Olgun CMOS değil.</p>"
            "<p><strong>Katman 2 — Dönüştürücü:</strong> Çok yüksek hızlı ADC/DAC; güç ve ısı sorunu.</p>"
            "<p><strong>Katman 3 — Kullanım geometrisi:</strong> Kısa hop, hizalı hüzme, yedek görüş hattı.</p>"
            "<p>L(f,d) ve Shannon kartları uzman katmanındadır.</p>"
        ),
    },
    "ai_ran": {
        "card": (
            "Klasik şebeke sabit kuralı ezberden okur: dolu stadyum ile ıssız gece aynı kurala bakınca "
            "ya kaynak israf olur ya kalite düşer. "
            "AI-RAN (Artificial Intelligence-Native RAN — yapay zekâ tabanlı telsiz erişim ağı) "
            "kuleyi ölçer, milisaniye–saniye döngüsünde kaynak kaydırır. "
            "Sohbet botu değildir, ağı yöneten karar mekanizmasıdır. "
            "TRL 5 seviyesindedir: O-RAN RIC (RAN Intelligent Controller — RAN Akıllı Denetleyici) "
            "üzerinde denemeler yapılmıştır, ancak sahada tamamen insansız çalışma henüz kanıtlanmamıştır."
        ),
        "kicker": "Sorun: şebeke sabit kural izler",
        "what": (
            "AI-native RAN, PHY/MAC ve kaynak yönetiminin bir kısmının sabit formül yerine "
            "öğrenilmiş modellerle (otokodlayıcı, pekiştirmeli öğrenme, kestirim) çalışacak şekilde "
            "tasarlanmasıdır. Pratikte bugün çoğu iş O-RAN RIC üzerindeki xApp/rApp ile başlar; "
            "hava arayüzünün tamamını sinir ağı yapmak araştırma ucudur."
        ),
        "why_needed": (
            "Trafik, kanal ve enerji zamanla değişir. Sabit tarife maç uzamasına, konser bitişine, "
            "depreme geç kalır. Boş kule elektrik yer. Arıza çoğu zaman olduktan sonra görünür. "
            "Öğrenen döngü, ölçüme dayalı uyarlama ihtiyacını karşılar."
        ),
        "problem": (
            "İnsan her saniye RRM yazamaz. Klasik eşik kuralları yerel optimumda sıkışır. "
            "Enerji, kapasite ve hareket aynı anda çekişir. Veri yoksa model uydurur; kara kutu "
            "düzenleyiciye açıklanamaz."
        ),
        "how_steps": [
            "Ölç: yük, SINR, PRB kullanımı, enerji, arıza öncüleri.",
            "Karar: Near-RT RIC xApp (onlarca ms) hüzme/handover; Non-RT rApp (saniye+) enerji ve tahmin.",
            "Uygula: politika gNB'ye yazılır. Denetim kalkmaz; geri alma yolu gerekir.",
            "Öğren: ödül (kapasite, enerji, kesinti) kötüyse politika güncellenir.",
        ],
        "mental_model": (
            "Bunu zihninde şöyle kur: sabit zamanlı trafik ışığı vs. kuyruğu gören ışık. "
            "AI-RAN ikincisidir. Işık 'düşünmez'; ölçer, kural veya modeli uygular, sonucu izler. "
            "Yanlış öğrenen ışık kavşağı kilitleyebilir — bu yüzden mühendis denetimi tasarım parçasıdır."
        ),
        "analogy": (
            "Sabit trafik ışığı / kavşağı gören ışık. AI-RAN, kuyruk uzayınca yeşili uzatır, "
            "gece kimse yoksa boş fazı kısar."
        ),
        "analogy_technical_map": (
            "Bu analojinin teknik karşılığı: kamera = RAN ölçümleri; ışık programı = RRM politikası; "
            "Near-RT = kavşak anlık döngüsü (~10 ms mertebesi, O-RAN tanımı); Non-RT = şehrin gece "
            "planı. Q-learning'de 'yeşili uzat' bir eylemdir (a), kuyruk durumu s, ödül r kapasite veya "
            "enerjidir. Otokodlayıcı PHY ise kavşak değil, 'nasıl korna çalınır'ın (modülasyonun) öğrenilmesidir."
        ),
        "when_used": (
            "Değişken yük (stadyum, iş çıkışı), enerji hedefi, kestirimci bakım, çok tedarikçili "
            "O-RAN denemeleri. Ölçüm kalitesi yüksek, geri alma prosedürü tanımlı ise."
        ),
        "when_not": (
            "Eğitilmemiş modelle canlı şebekeye 'otonom pilot' denmez. Kara kutu karar düzenleyici "
            "denetiminde risklidir. '%50–70 enerji' ve 'sıfır insan' iddiaları hedef/pazarlamadır; "
            "bu platformda saha faturası yoktur. GPU'nun kendisi enerji yer — net kazanç ölçülmelidir."
        ),
        "not_to_confuse": (
            "Bu sayfadaki sohbet asistanı AI-RAN değildir. Self-organizing network (SON) atasıdır "
            "ama AI-native, öğrenmeyi hava arayüzüne kadar indirme iddiasını taşır. "
            "O-RAN açık arayüzdür; AI onun üstünde çalışan uygulamadır — ikisi özdeş değildir."
        ),
        "real_world": (
            "O-RAN WG2/WG10, 3GPP TR 38.843 (AI/ML for NR), AI-RAN Alliance. "
            "Operatör RIC PoC'leri. Tam nöral hava arayüzü laboratuvar."
        ),
        "tt_impact": (
            "Maç çıkışı kaynak kaydırma, gece uyku, arıza öncülü. TRL 5. "
            "İnsan denetimi kapanmaz."
        ),
        "principle_html": (
            "<p><strong>1. Ölç:</strong> Kule yük, ısınma, kopma ve kanalı okur.</p>"
            "<p><strong>2. Karar ver:</strong> <strong>RIC</strong> (RAN Intelligent Controller — RAN akıllı denetleyici) "
            "üzerinde xApp/rApp 'kapasite kaydır / uyu / uyar' der.</p>"
            "<p><strong>3. Uygula ve öğren:</strong> Sonuç iyiyse politika kalır. "
            "Kara kutu riski için insan geri alma yolu tasarımın parçasıdır.</p>"
            "<p><strong>Sonuç:</strong> Şebeke uyarlanır. Sihir değil; ölçüm + model + denetimdir.</p>"
        ),
        "arch_html": (
            "<p><strong>Katman 1 — Ölçüm ve PHY:</strong> Klasik sinyal işleme veya araştırma ucunda nöral PHY.</p>"
            "<p><strong>Katman 2 — RIC:</strong> Near-RT xApp (hızlı), Non-RT rApp (yavaş/enerji/tahmin). "
            "<strong>O-RAN</strong> açık arayüz bu katmanı taşır.</p>"
            "<p><strong>Katman 3 — Hızlandırıcı:</strong> gNB yanında NPU/GPU olabilir. Enerji kazancı net hesaplanmalıdır.</p>"
            "<p>Kayıp fonksiyonu ve Q-öğrenme uzman kartlarındadır.</p>"
        ),
    },
    "ntn": {
        "card": (
            "Karasal kule şehri ve asfaltı kapsar; dağ, açık deniz ve enkaz boş kalır. "
            "NTN (Non-Terrestrial Network — Karasal Olmayan Ağ) "
            "LEO (Low Earth Orbit — Alçak Dünya Yörüngesi) uydularını ve "
            "HAPS'ı (High-Altitude Platform Station — Yüksek İrtifa Platformu) "
            "3GPP şebekesiyle birleştirir: kule yokken telefon doğrudan göğe bağlanır. "
            "Bedeli, uzun mesafeden doğan gecikme ve uydu hareketinden gelen Doppler kaymasıdır. "
            "TRL 6 seviyesindedir ve yedi teknoloji arasında en olgun olanıdır; "
            "şehir içindeki 6G şebekesinin rakibi değil, onu tamamlayan bir çözümdür."
        ),
        "kicker": "Sorun: kule her yere ulaşmaz",
        "what": (
            "NTN, LEO (Low Earth Orbit — alçak dünya yörüngesi), GEO ve HAPS düğümlerini "
            "karasal çekirdeğe 3GPP Rel-17+ prosedürleriyle bağlayan mimaridir. "
            "Direct-to-cell: özel uydu telefonu yerine standart UE'nin uydu hücrelerini görmesi."
        ),
        "why_needed": (
            "Kapsama kule ve fiberin ulaştığı yer kadardır. Kırsal CAPEX, deniz, havacılık ve "
            "afet (kule yıkılınca) karasal modeli kırar. Uydu, aynı kimlik ve numara ile boşluğu kapatma "
            "ihtiyacına cevap verir."
        ),
        "problem": (
            "Mesafe FSPL'yi büyütür; LEO ~7,5 km/s hareket Doppler ve sık handover üretir. "
            "GEO gecikmesi konuşmayı zorlar. Spektrum, yer kapısı (gateway) ve düzenleme operatör "
            "işidir, 'uzay sihri' değil."
        ),
        "how_steps": [
            "Karasal öncelik: şehirde gNB. Boşlukta uydu/HAPS hücresi.",
            "Yer kapısı: feeder link uydudan TT yer istasyonuna, oradan çekirdeğe.",
            "Doppler/gecikme telafisi: PHY zaman-frekans ön düzeltmesi; aksi halde PRACH bile tutmaz.",
            "Servis sınıfı: acil SMS/ses önce; terabit şehir deneyimi vaadi değil.",
        ],
        "mental_model": (
            "Bunu zihninde şöyle kur: karasal şebeke sokak lambasıdır — yolu aydınlatır, ormanı değil. "
            "NTN yukarıdan tutan projektördür. Lambanın olduğu yerde lamba; yoksa projektör. "
            "Projektör daha uzaktır, gölge ve gecikme farklıdır."
        ),
        "analogy": (
            "Sokak lambası / havadan projektör. NTN ormanı ve denizi tutar; cadde lambasının yerini almaz."
        ),
        "analogy_technical_map": (
            "Bu analojinin teknik karşılığı: lamba = gNB; projektör = LEO hüzmesi; kablo = feeder link "
            "+ çekirdek; gölge gecikmesi = yayılma ~ d/c (LEO'da onlarca ms mertebesi, GEO'da ~250 ms "
            "gidiş-dönüş); rüzgârda sallanma = Doppler f_d = f_c (v/c) cosθ. Direct-to-cell, çanak değil "
            "telefon anteninin link bütçesine sığması demektir."
        ),
        "when_used": (
            "Kırsal ve dağ, deniz, havacılık, afet yedek hattı, IoT'nin kulesiz sahası. "
            "Karasalın ekonomik olmadığı yer."
        ),
        "when_not": (
            "Şehir içi kapasite ve milisaniye altı URLLC için birincil yol değildir. "
            "'%100 küresel, sıfır boşluk' pazarlama cümlesidir; kutup, iç mekân ve düzenleme boşluğu kalır. "
            "Bu platformda uydu gecikmesi saha ölçülmedi; kural tabanlı aralık literatürdendir."
        ),
        "not_to_confuse": (
            "Klasik VSAT çanak ≠ direct-to-cell. Starlink tüketici genişbantı NTN 3GPP hücresi ile "
            "aynı ürün değildir (farklı protokol ve iş modeli olabilir). HAPS uydu değildir; "
            "stratosfer katmanıdır. ISAC 'gökyüzünü radar yapmak' NTN değildir."
        ),
        "real_world": (
            "3GPP TR 38.811 ve Rel-17/18 NTN iş kalemleri, direct-to-cell operatör denemeleri, "
            "ESA uzay bileşeni çalışmaları. Türkiye'de afet yedek hattı senaryosu operatör stratejisidir."
        ),
        "tt_impact": (
            "Afet hattı, balıkçı filosu, Doğu Anadolu kırsalı. TRL 6. "
            "Şehir 5G/6G kulesinin tamamlayıcısı."
        ),
        "principle_html": (
            "<p><strong>1. Yeri doldur:</strong> Şehir ve yol kulelerle kalır. Boş coğrafyada "
            "<strong>LEO</strong> veya <strong>HAPS</strong> konuşur.</p>"
            "<p><strong>2. Aynı kimliği koru:</strong> Hedef özel çanak değil; 3GPP UE'nin uydu hücresini görmesidir.</p>"
            "<p><strong>3. Kaymayı yönet:</strong> Uydu hızlıdır. PHY Doppler ve gecikmeyi telafi eder; "
            "yine de yer kulesi kadar 'anında' olmaz.</p>"
            "<p><strong>Sonuç:</strong> Kapsama deliği kapanır. Rakip değil, tamamlayıcıdır.</p>"
        ),
        "arch_html": (
            "<p><strong>Katman 1 — Uzay/hava:</strong> LEO takımı, isteğe HAPS, nadiren GEO ses/IoT.</p>"
            "<p><strong>Katman 2 — Yer kapısı:</strong> Feeder link → Türk Telekom gateway → çekirdek şebeke.</p>"
            "<p><strong>Katman 3 — UE:</strong> Rel-17+ NTN yetenekli modem; her eski telefon garanti değildir.</p>"
            "<p>Doppler ve FSPL kartları uzman katmanındadır.</p>"
        ),
    },
    "ambient_iot": {
        "card": (
            "Depodaki her koli, tarladaki her nem sensörü bugün pil ister. "
            "Pil bitince cihaz susar; milyonlarca pili değiştirmek işlemez. "
            "Ambient IoT ortamdaki RF (Radio Frequency — radyo frekansı) kırıntısını toplayıp "
            "geri saçılımla (backscatter) «buradayım» der; video taşımaz, sadece kimlik bildirir. "
            "TRL 4 seviyesindedir: 3GPP bünyesinde aktif bir çalışma kalemidir, "
            "ancak henüz her rafa yapıştırılmış, yaygın kullanılan bir teknoloji değildir."
        ),
        "kicker": "Sorun: her nesneye pil değiştirilemez",
        "what": (
            "Ambient IoT, pili olmayan veya pili çok küçük olan etiketlerin, ortam RF'sinden "
            "(kule, Wi-Fi, özel aydınlatıcı) enerji toplayıp çoğunlukla backscatter (geri saçılım) "
            "ile kısa durum mesajı verdiği IoT sınıfıdır. Amaç trilyon ölçekte ucuz izlemedir."
        ),
        "why_needed": (
            "Pil lojistiği ve kimyasal atık, koli/sera/sayaç ölçeğinde ekonomik değildir. "
            "Klasik hücresel IoT (NB-IoT, RedCap) hâlâ bir enerji kaynağı ister. "
            "Pilsiz etiket, 'nerede / kaç derece' işini bakım ekibi olmadan çözme ihtiyacıdır."
        ),
        "problem": (
            "Menzil kısa, bit hızı düşüktür çünkü yansıyan güç zayıftır ve ortam enerjisi "
            "garanti değildir. Okuyucu hassas, protokol ultra dardır. 'Telefonunuzun yerini alır' değil."
        ),
        "how_steps": [
            "Topla: rectenna RF'yi DC'ye çevirir; kapasitörde kırıntı birikir.",
            "Yansıt: anten empedansı değiştirilerek gelen taşıyıcı modüle edilir (kendi PA'sı yok).",
            "Oku: yakındaki gNB/okuyucu zayıf eko + biti ayırır.",
            "Buluta yaz: 'koli 14, 4 °C' — video yok.",
        ],
        "mental_model": (
            "Bunu zihninde şöyle kur: eski hesap makinesinin güneş paneli. Işık yerine radyo dalgası "
            "'güneş'tir. Cihaz film izlemez; yalnızca kısa durum bildirir. Güneş yoksa (RF zayıfsa) susar."
        ),
        "analogy": (
            "Güneş panelli hesap makinesi: pilsiz, ışıktan yaşar. Ambient IoT ışık yerine RF kırıntısı kullanır."
        ),
        "analogy_technical_map": (
            "Bu analojinin teknik karşılığı: panel = rectenna verimi η; ışık şiddeti = P_tx G_tx (λ/4πd)²; "
            "hesap makinesinin 'eşittir' tuşu = backscatter biti b(t); gölge = RF zayıf bölge. "
            "RFID atasıdır; fark 3GPP hücresel okuyucu ve adresleme hedefidir."
        ),
        "when_used": (
            "Lojistik palet, soğuk zincir, sera nemi, sayaç, yapı sağlığı — kısa menzil, seyrek, "
            "düşük bit, uzun ömür istenen yer."
        ),
        "when_not": (
            "Ses, görüntü, kilometre menzil, hareketli araç telemetrisi. '1 sent altı, sınırsız ömür, "
            "trilyon nesne' hedef/pazarlamadır; Rel-19 çalışma kalemi ürün rafı değildir. "
            "RF'siz depo köşesinde etiket ölür."
        ),
        "not_to_confuse": (
            "Klasik pasif RFID mağaza kapısı Ambient IoT'nin atasıdır ama hücresel standart ve "
            "çoklu okuyucu senaryosu farklıdır. Enerji hasatlı sensor (güneş+pil) da ayrı sınıftır. "
            "ISAC eko ölçümü işbirlikçi olmayan hedeftir; Ambient IoT kasıtlı etikettir."
        ),
        "real_world": (
            "3GPP TR 38.848, akademik backscatter, ticari pilsiz etiket denemeleri. "
            "Operatör IoT platformuna akış senaryo olarak yazılır, sahada her rafta değildir."
        ),
        "tt_impact": (
            "Depo paleti, sera, sayaç: bakım ekibi olmadan izleme adayı. TRL 4. "
            "Telefonunuzun yerini almaz."
        ),
        "principle_html": (
            "<p><strong>1. Topla:</strong> Etiket havadaki RF kırıntısını elektriğe çevirir (rectenna). "
            "Pil yuvası yoktur veya yedektir.</p>"
            "<p><strong>2. Yansıt:</strong> Kendi vericisini yakmaz. Gelen dalgayı evet/hayır diye "
            "değiştirir. Bu yüzden menzil kısadır.</p>"
            "<p><strong>3. Oku:</strong> Yakındaki kule veya okuyucu zayıf yankıyı duyar ve buluta yazar.</p>"
            "<p><strong>Sonuç:</strong> Ucuz, pilsiz, seyrek iz. Video taşımaz; doğru işi çözer.</p>"
        ),
        "arch_html": (
            "<p><strong>Katman 1 — Etiket:</strong> ASIC + mikro kapasitör + rectenna. Batarya yok.</p>"
            "<p><strong>Katman 2 — Enerji ve okuyucu:</strong> 6G kulesi veya yardımcı aydınlatıcı; "
            "yüksek hassasiyetli alıcı.</p>"
            "<p><strong>Katman 3 — 3GPP Rel-19 ve IoT bulutu:</strong> Dar adresleme, TT IoT platformu.</p>"
            "<p>Friis hasadı ve backscatter modeli uzman kartlarındadır.</p>"
        ),
    },
}
