"""
Temel seviye — kavramsal temel.
Jargon yasak değil: ilk kullanımda açılır. Uzman denklemler expert_depth'te.
Akış: problem → ihtiyaç → yöntem → mekanizma → sonuç → uygulama.
"""

BEGINNER_COPY = {
    "isac": {
        "card": (
            "Baz istasyonu veri taşır; çevreyi ölçmez. Kamera sis ve karanlıkta körleşir; "
            "ayrı radar ikinci spektrum ve ikinci anten ister. "
            "ISAC (Integrated Sensing and Communication — Entegre Algılama ve İletişim) "
            "aynı RF zincirinde hem bit hem yankı işler: gecikme mesafe, Doppler hız verir. "
            "TRL 4 — Rel-19 çalışma kalemi (TR 22.837); laboratuvar doğrulaması, TT sahası değil."
        ),
        "kicker": "Sorun: kule konuşur, göremez",
        "what": (
            "ISAC (Integrated Sensing and Communication — Entegre Algılama ve İletişim), "
            "aynı taşıyıcı, aynı anten ve çoğu zaman aynı dalga şekli üzerinde hem kullanıcıya "
            "veri iletmeyi hem yansıyan enerjiden mesafe, hız ve açı çıkarmayı birlikte tasarlayan "
            "radyo mimarisidir. Yanına radar kutusu eklemek değildir."
        ),
        "why_needed": (
            "Spektrum ve kent arazisi pahalıdır. Trafik, alçak irtifa dron koridoru ve kamerasız "
            "farkındalık ayrı bir radar şebekesi isterse CAPEX ve EMI (Electromagnetic Interference — "
            "elektromanyetik girişim) birlikte büyür. Şebeke zaten RF basıyorsa, aynı enerjiyi ikinci "
            "görev için kullanmak operatör için rasyonel bir ihtiyaçtır."
        ),
        "problem": (
            "Klasik gNB (next-generation Node B — 5G/6G baz istasyonu) yalnızca haberleşme kanalını "
            "optimize eder. Kamera yağmur ve siste düşer; gizlilik maliyeti yüksektir. Komşu "
            "otomotiv/askeri radar spektrumu şebekeye girişim basar. Sonuç: kör nokta kalır ya da "
            "çift altyapı ödenir."
        ),
        "how_steps": [
            "Yayın: gNB, kullanıcıya giden OFDM veya OTFS çerçevesini basar; ayrı radar kamyonu yoktur.",
            "Yankı: Araç, duvar veya drondan dönen eko gecikme (mesafe), Doppler (hız) ve dizi faz farkı AoA (Angle of Arrival — geliş açısı) verir.",
            "Paylaşım: Zaman, frekans veya kodda dik (orthogonal) ayırım, bit ile yankının birbirini bozmamasını hedefler.",
            "Kenar: Mesafe/hız/açı özeti kenar sunucuya gider; ham I/Q her zaman merkeze taşınmaz.",
        ],
        "mental_model": (
            "Tek RF zinciri, iki görev. Gidiş yolu Shannon kanalıdır; dönüş yolu radar denklemidir. "
            "Güç ve zaman aynı bütçeden bölünür: iletişime ayrılan enerji artınca yankının SNR'ı düşer. "
            "Menzil iletişim menzilinden kısa kalır, çünkü eko R⁴ ile zayıflar."
        ),
        "analogy": (
            "Monostatik radarın eko zinciri ile hücresel down-link'in aynı taşıyıcıyı paylaşması. "
            "İki bağımsız sistem yan yana değildir."
        ),
        "analogy_technical_map": (
            "Gecikme τ = 2R/c menzili, Doppler kayması hızı, çok antenli faz farkı AoA'yı verir. "
            "CRB (Cramér-Rao Bound — Cramér-Rao sınırı) kestirim varyansının teorik tabanıdır; "
            "Shannon kapasitesi aynı P ve B'yi paylaşır. Clutter ve gizlilik, denklem dışındaki tasarım kısıtıdır."
        ),
        "when_used": (
            "Görüşün bozulduğu geometride (sis, gece), kameranın istenmediği yerde, mevcut kule "
            "hattının yolu veya koridoru kestiği operatör şebekesinde; ayrı radar spektrumunun "
            "pahalı veya düzenleme olarak zor olduğu durumda."
        ),
        "when_not": (
            "Santimetre altı 'her mahallede' vaadi için değil — literatür hedefidir, bu platformda "
            "saha ölçümü yoktur. Yoğun çoklu yansıma ve KVKK çözülmeden kamusal izleme ürünü sayılmaz. "
            "B dar ise menzil çözünürlüğü fiziken kaba kalır."
        ),
        "not_to_confuse": (
            "Yanına radar konmuş 5G kulesi ISAC değildir; o iki sistemdir. Kamerayla bilgisayarla görme "
            "değildir: RF yankısı piksel üretmez. Ambient IoT geri saçılımı kasıtlı etikettir; "
            "ISAC hedefi çoğu zaman işbirlikçi olmayan yansıtıcıdır."
        ),
        "real_world": (
            "3GPP Rel-19 ISAC çalışma kalemi (TR 22.837), Hexa-X-II mimari raporları, V2X ve alçak irtifa "
            "dron araştırma yatakları. Ticari 'her kule radar' ürünü değildir."
        ),
        "tt_impact": (
            "Boğaz sisinde deniz trafiği, şehir içi dron koridoru, enkaz altı hareket: mevcut kule "
            "geometrisi adaydır. TRL 4 — laboratuvar; abone mahallesinde yok."
        ),
        "principle_html": (
            "<p><strong>1. Yayın:</strong> "
            "<strong>gNB</strong> (next-generation Node B — 5G/6G baz istasyonu) kullanıcı çerçevesini basar. "
            "Ayrı radar donanımı yoktur.</p>"
            "<p><strong>2. Yankı:</strong> Gecikme mesafe, <strong>Doppler</strong> hız, dizi faz farkı "
            "<strong>AoA</strong> (Angle of Arrival — geliş açısı) verir.</p>"
            "<p><strong>3. Paylaşım:</strong> Bit ile yankı zaman/frekans/kodda ayrılır. Aynı güç bütçesi "
            "iki görevi besler.</p>"
            "<p><strong>Sonuç:</strong> Spektrum ve anten tasarrufu adayı. Ödünleşme: R⁴ kaybı ve clutter.</p>"
        ),
        "arch_html": (
            "<p><strong>Katman 1 — PHY:</strong> Mevcut dizi hem veri yollar hem eko dinler. "
            "Masif MIMO faz farkı açı kestirimine yarar.</p>"
            "<p><strong>Katman 2 — MAC:</strong> Konuşma ile yankı birbirini bozmasın diye kaynak paylaştırılır. "
            "Bu ödünleşmedir, sihir değildir.</p>"
            "<p><strong>Katman 3 — Kenar:</strong> Mesafe/hız/açı özeti Türk Telekom kenar bulutuna gider. "
            "Ham I/Q her zaman merkeze taşınmaz.</p>"
            "<p>Dalga şekli, CRB ve Rel-19 formül kartları uzman katmanındadır.</p>"
        ),
    },
    "ris": {
        "card": (
            "Yüksek frekansta dalga köşeyi dönmez; her kör nokta için yeni gNB dikmek CAPEX ve kent "
            "yüküdür. RIS (Reconfigurable Intelligent Surface — Yeniden Yapılandırılabilir Akıllı Yüzey) "
            "cephedeki programlanabilir yansıtıcıdır: eleman fazı θ_n hüzmeyi UE'ye çevirir, kendi "
            "yüksek güçlü vericisi yoktur. TRL 5 — ETSI RIS ISG ve Rel-19/20; operatör PoC sınıfı, "
            "TT sahası değil."
        ),
        "kicker": "Sorun: dalga köşeyi dönemez",
        "what": (
            "RIS (Reconfigurable Intelligent Surface — Yeniden Yapılandırılabilir Akıllı Yüzey), "
            "yüzlerce veya binlerce ayarlanabilir elemandan oluşan bir yüzeydir. PIN diyot veya varaktör "
            "gelen dalganın fazını 0–2π aralığında kaydırır. Yüzey internet üretmez; gNB yayınını "
            "hedeflenen UE'ye (User Equipment — kullanıcı cihazı) yönlendirir."
        ),
        "why_needed": (
            "mmWave ve üzeri bantlarda duvar ve köşe kaybı şiddetlidir. Her kör noktaya kule hem CAPEX "
            "hem EMC yüküdür. Pasif veya yarı-pasif yüzey, ortamı kontrol edilebilir bir kanal haline "
            "getirerek kapsama deliğini aktif röleden düşük enerjiyle kapatma adayıdır."
        ),
        "problem": (
            "Yüksek frekansta yol, görüş hattı (LoS) yoksa kopar veya hız düşer. Plaza camı, avlu ve "
            "tünel kıvrımı bu fiziğin sahadaki karşılığıdır. Aktif röle kendi RF zinciri, güç kaynağı "
            "ve girişimini taşır."
        ),
        "how_steps": [
            "Yüzey: cephe, cam veya tünel duvarı — RIS baz istasyonu değildir.",
            "Faz: her eleman θ_n kayması uygular; dizi faktörü hüzmeyi şekillendirir.",
            "Komut: gNB denetleyiciye hedef UE'yi bildirir; kontrol hattı düşük bit hızlıdır.",
            "Sonuç: engellenen doğrudan yol yerine kontrollü yansıma yolu oluşur.",
        ],
        "mental_model": (
            "RIS verici değil, sınır koşulunu programlayan yansıtıcıdır. Kanal iki hoptur: "
            "gNB→RIS→UE. Çift yol kaybı vardır; N eleman ideal koşullarda güç ~N² ölçeklenir. "
            "Kanal kestirilemezse faz tablosu yanlış yazılır ve kazanç düşer."
        ),
        "analogy": (
            "Pasif faz dizisi: her eleman bir gecikme hattıdır, ortak bir aydınlatıcı (gNB) vardır. "
            "Aktif röle veya küçük hücre değildir."
        ),
        "analogy_technical_map": (
            "θ_n eleman fazı, Φ = diag(e^{jθ_n}) yüzey, G Tx–RIS kanalı, h_r RIS–UE kanalıdır. "
            "Etkin kanal h_rᴴ Φ G. Çift yol kaybı Tx→RIS→Rx çarpımıdır; menzili sihirle uzatmaz."
        ),
        "when_used": (
            "N-LoS sokak, tünel kıvrımı, tribün, plaza içi mmWave, kule dikilemeyen tarihi doku. "
            "Aktif röleden düşük enerji ve CAPEX istenen geometri."
        ),
        "when_not": (
            "Yüzey kanalı kestiremiyorsa (pasif eleman alıcı değildir) ve denetleyici gecikmesi "
            "kullanıcı hızına yetmiyorsa kazanç düşer. '%90 enerji tasarrufu' literatür/hedeftir; "
            "bu platformda saha faturası ölçülmemiştir."
        ),
        "not_to_confuse": (
            "Aktif röle veya small cell değildir — yüksek güçlü vericisi yoktur. "
            "Metamalzeme 'görünmez pelerin' iddiası Maxwell'i iptal etmez; yalnızca sınır koşulu "
            "programlanır. ISAC ile birlikte kullanılabilir; RIS tek başına radar değildir."
        ),
        "real_world": (
            "ETSI RIS ISG, 3GPP Rel-19/20 çalışma kalemleri, cephe ve iç mekân operatör PoC'leri. "
            "Tak-çalıştır ticari emtia her binada yoktur."
        ),
        "tt_impact": (
            "Yarımada, tünel, plaza camı: kule dikmeden kapsama adayı. TRL 5 — ilgili ortamda prototip; "
            "abone şebekesinin varsayılan parçası değil."
        ),
        "principle_html": (
            "<p><strong>1. Yüzey:</strong> Cepheye ince yansıtıcı asılır. Bu bir baz istasyonu değildir.</p>"
            "<p><strong>2. Faz:</strong> Elemanlar θ_n ile hüzmeyi <strong>UE</strong> cihazına çevirir.</p>"
            "<p><strong>3. Komut:</strong> <strong>gNB</strong> düşük bit hızlı kontrol hattından hedefi bildirir.</p>"
            "<p><strong>Sonuç:</strong> Kontrollü yansıma. Bedeli kanal kestirimi ve çift yol kaybıdır.</p>"
        ),
        "arch_html": (
            "<p><strong>Katman 1 — Yüzey:</strong> PIN/varaktör elemanlar; aktif RF zinciri yok veya çok az.</p>"
            "<p><strong>Katman 2 — Denetleyici:</strong> FPGA/mikrodenetleyici, eleman fazını gNB emrine yazar.</p>"
            "<p><strong>Katman 3 — C-düzlemi:</strong> Kule–yüzey kontrol hattı. Yüzey kendi başına internet üretmez.</p>"
            "<p>N² ölçeği ve kanal kestirimi uzman formül kartlarındadır.</p>"
        ),
    },
    "cell_free": {
        "card": (
            "Hücre kenarında SINR düşer; handover kopma riski taşır. "
            "Hücresiz Massive MIMO (Multiple-Input Multiple-Output — Çok Girişli Çok Çıkışlı) "
            "yayılmış erişim noktalarının aynı anda, aynı frekansta ortak ön kodlama ile hizmet "
            "verdiği mimaridir: kenar tasarım hedefi olarak kalkar. Bedeli fronthaul fiberidir. "
            "TRL 4 — Rel-19/20 dağıtık MIMO çalışma kalemi; literatür prototip, TT sahası değil."
        ),
        "kicker": "Sorun: hücre sınırında zayıflar",
        "what": (
            "Hücresiz Massive MIMO, kullanıcıyı tek hücreye bağlamak yerine coğrafyaya yayılmış "
            "erişim noktalarının (AP) aynı frekansta, merkezi veya yarı-dağıtık işlemle birlikte "
            "hizmet verdiği mimaridir. Hücre sınırı tasarım olarak ortadan kalkar."
        ),
        "why_needed": (
            "Kapasite ve adalet kenarda çöker: istenen sinyal zayıf, komşu kule parazittir. "
            "Stadyum ve terminalde yük tek makro kuleye yığılır. Dağıtık antenler yolu kısaltır "
            "ve paraziti işbirliğiyle işlenebilir hale getirir."
        ),
        "problem": (
            "Hücresel şebeke pasta dilimidir. Dilim kenarında SINR "
            "(Signal-to-Interference-plus-Noise Ratio — sinyal-parazit-artı-gürültü oranı) düşer. "
            "Handover başarısızlığı kopmadır. Tek kule + çok kullanıcı = tribünün bir yanı tok, diğeri açık."
        ),
        "how_steps": [
            "Dağıt: düşük karmaşıklıklı AP'ler tavan, tribün, cadde.",
            "Bağla: yüksek hızlı fronthaul CPU/kenar buluta gider; senkronizasyon şarttır.",
            "Ortak taşı: birkaç AP aynı anda ön kodlama (precoding) uygular.",
            "Paraziti işle: komşu kullanıcıya giden enerji işbirliğiyle bastırılır.",
        ],
        "mental_model": (
            "Tek hücre yok; kullanıcı birkaç AP'nin ortak hüzmesinde durur. "
            "Hesap merkeze veya dağıtık kümeye gitmek zorundadır — fiber yoksa ortak ön kodlama "
            "yazılamaz. Fronthaul gecikmesi ve faz kayması kazancı tersine çevirir."
        ),
        "analogy": (
            "Koordineli çok nokta (CoMP) hücresiz MIMO'nun atasıdır; fark 'hücre yok' varsayımına "
            "kadar gitmesidir. Small-cell ormanı hâlâ hücre kenarı taşır."
        ),
        "analogy_technical_map": (
            "AP = dağıtık radyo; fronthaul = eCPRI/RoF; w_mk = ortak ön kodlama; kenar paraziti = "
            " bastırılacak bileşen. CPU'da MMSE veya ZF matris. Senkron kaybı hüzme kazancını eritir."
        ),
        "when_used": (
            "Yüksek yoğunluk, hareket, adalet: stadyum, havalimanı, üretim hattı, yoğun bulvar. "
            "Makro kule estetiğinin istenmediği iç mekân."
        ),
        "when_not": (
            "Seyrek kırsalda her direğe fiber CAPEX olarak anlamsızdır; NTN veya makro daha rasyoneldir. "
            "5×–10× spektral kazanç literatür aralığıdır; bu platformda saha ölçümü yoktur."
        ),
        "not_to_confuse": (
            "Small cell hâlâ hücredir. Klasik CoMP ortak işlem yapar ama hücre kimliğini kaldırmaz. "
            "Wi-Fi roaming aynı anda çok AP'nin sizin sembolünüzü taşıması değildir."
        ),
        "real_world": (
            "Dağıtık MIMO literatürü, 3GPP Rel-19/20 dağıtık MIMO çalışma kalemi, satıcı laboratuvar "
            "gösterimleri. Stadyum PoC adayı; şehir geneli ürün değil."
        ),
        "tt_impact": (
            "Havalimanı, stadyum, depo: kenar şikâyeti. TRL 4. Önce yoğun mekân — fiber pahalıdır."
        ),
        "principle_html": (
            "<p><strong>1. Dağıt:</strong> AP'ler sık yerleştirilir; tek makro kuleye bel bağlanmaz.</p>"
            "<p><strong>2. Ortak taşı:</strong> UE aynı anda birkaç AP'ye bağlanır.</p>"
            "<p><strong>3. Birleştir:</strong> Fronthaul üzerindeki işlemci "
            "<strong>MMSE</strong> (Minimum Mean Square Error — minimum ortalama kare hata) "
            "tipi ön kodlama uygular.</p>"
            "<p><strong>Sonuç:</strong> Handover hissi kaybolur. Fatura fronthaul ve hesaptır.</p>"
        ),
        "arch_html": (
            "<p><strong>Katman 1 — AP:</strong> Düşük karmaşıklıklı radyo; ağır hesap yok.</p>"
            "<p><strong>Katman 2 — Fronthaul:</strong> Fiber. Senkron yoksa ortak hüzme bozulur.</p>"
            "<p><strong>Katman 3 — CPU / kenar:</strong> Ortak kestirim ve ön kodlama.</p>"
            "<p>SINR ve MMSE varsayımları uzman kartlarındadır.</p>"
        ),
    },
    "thz": {
        "card": (
            "Sub-6 GHz ve mmWave, veri merkezi içi mesh ve kule köprüsü için dar kalabilir. "
            "THz (terahertz) milimetre dalga ile kızılötesi arasındaki spektrumu açar; Shannon'da "
            "kapasite önce B ile büyür. Bedeli FSPL ve moleküler emilimdir: menzil kısalır. "
            "TRL 3 — TR 38.807; laboratuvar, sokak şebekesi değil. 6G yalnızca THz değildir."
        ),
        "kicker": "Sorun: veri borusu hâlâ dar",
        "what": (
            "THz iletişimi, kabaca 0,1–10 THz diliminde onlarca GHz bant genişliği açma girişimidir. "
            "Shannon: C = B log₂(1+SNR); B birinci terimdir, SNR ikinci."
        ),
        "why_needed": (
            "Veri merkezi rafları arası mesh, fiber çekilemeyen kule köprüsü ve ileride yüksek bit "
            "hızlı iç mekân adayıdır. Fiber her geometriye gitmez. THz, doğru mesafede kablosuz "
            "yüksek B adayıdır."
        ),
        "problem": (
            "Frekans yükseldikçe FSPL (Free-Space Path Loss — serbest uzay yol kaybı) ve su buharı "
            "emilimi büyür. El, yaprak, yağmur linki keser. InP/GaN ve ADC hızı olgun CMOS değildir. "
            "Bu yüzden TRL düşüktür."
        ),
        "how_steps": [
            "Spektrum: 100 GHz üzeri pencereler; hedef onlarca GHz B.",
            "Kayıp: L(f,d) = FSPL × e^{K(f)d}; K(f) su buharı çizgilerinde sıçrar.",
            "Hüzme: dizi kazancı kaybı telafi eder; hizalama hassaslaşır.",
            "Geometri: raf, salon, kule köprüsü — makro sokak değil.",
        ],
        "mental_model": (
            "B büyüdükçe kapasite lineere yakın artar; emilim SNR'yi yerse logaritmik terim çöker. "
            "Dar hüzme kaybı telafi eder ama tıkanma (blockage) olasılığını yükseltir. "
            "Doğru hop kısa ve görüş hattıdır."
        ),
        "analogy": (
            "Kablosuz fiber adayı: yüksek B, kısa d, hizalı hüzme. Makro hücresel taşıyıcı değildir."
        ),
        "analogy_technical_map": (
            "B = bant; d = mesafe; K(f) = moleküler emilim; EIRP ve dizi kazancı kaybı telafi eder. "
            "C = B log₂(1+SNR): B'yi onlarca GHz yapmak SNR'den etkilidir — SNR emilimde düşerse B yetmez."
        ),
        "when_used": (
            "Kablosuz veri merkezi, kısa backhaul/fronthaul, kontrollü iç mekân, spektroskopi. "
            "Görüş hattı ve onlarca–yüzlerce metre."
        ),
        "when_not": (
            "Açık şehir makrosu, yağmurlu uzun hop, cepten-cepte kilometre. '1 Tbps her aboneye' "
            "pazarlama cümlesidir; bu platformda ölçülmedi. Tıbbi nanosensör araştırma ufkudur, "
            "Rel-19 ticari özellik değildir."
        ),
        "not_to_confuse": (
            "5G mmWave (28–39 GHz) THz değildir. Serbest uzay optiği (lazer) ayrı sınıftır. "
            "ISAC THz dalga şekli kullanabilir; THz tek başına algılama standardı değildir."
        ),
        "real_world": (
            "IEEE 802.15.3d, ITU-R spektrum çalışmaları, 3GPP TR 38.807 (NR beyond 52.6 GHz), "
            "satıcı Sub-THz gösterimleri. Abone telefonunda varsayılan bant değil."
        ),
        "tt_impact": (
            "Kısa vadede cep hızı değil; raf ve fiber çekilemeyen kule köprüsü. TRL 3. Konum: laboratuvar."
        ),
        "principle_html": (
            "<p><strong>1. Bant:</strong> mmWave ile kızılötesi arasındaki spektrum açılır; B büyür.</p>"
            "<p><strong>2. Emilim:</strong> Su buharı, duvar, el FSPL'ye ek kayıp basar.</p>"
            "<p><strong>3. Hüzme:</strong> Dar hüzme kaybı telafi eder; menzil kısa kalır.</p>"
            "<p><strong>Sonuç:</strong> Doğru geometride yüksek B adayı. 6G = yalnızca THz değildir.</p>"
        ),
        "arch_html": (
            "<p><strong>Katman 1 — RF ön uç:</strong> GaN/InP adayları; olgun CMOS değil.</p>"
            "<p><strong>Katman 2 — Dönüştürücü:</strong> Yüksek hızlı ADC/DAC; güç ve ısı.</p>"
            "<p><strong>Katman 3 — Geometri:</strong> Kısa hop, hizalı hüzme, yedek LoS.</p>"
            "<p>L(f,d) ve Shannon uzman kartlarındadır.</p>"
        ),
    },
    "ai_ran": {
        "card": (
            "Sabit RRM kuralı dolu stadyum ile boş geceyi aynı tarifeyle yönetir. "
            "AI-RAN (Artificial Intelligence-Native RAN — yapay zekâ tabanlı telsiz erişim ağı) "
            "ölçüme göre milisaniye–saniye döngüsünde kaynak kaydırır. Sohbet botu değildir. "
            "TRL 5 — TR 38.843 ve O-RAN RIC deneme sınıfı; insansız saha kanıtı yok."
        ),
        "kicker": "Sorun: şebeke sabit kural izler",
        "what": (
            "AI-native RAN, PHY/MAC ve kaynak yönetiminin bir kısmının sabit eşik yerine öğrenilmiş "
            "modelle (otokodlayıcı, pekiştirmeli öğrenme, kestirim) çalışacak şekilde tasarlanmasıdır. "
            "Bugün pratik giriş O-RAN RIC üzerindeki xApp/rApp'tir; hava arayüzünün tamamını sinir ağı "
            "yapmak araştırma ucudur."
        ),
        "why_needed": (
            "Trafik, kanal ve enerji zamanla değişir. Sabit tarife maç uzamasına ve arızaya geç kalır. "
            "Boş kule elektrik yer. Öğrenen döngü, ölçüme dayalı uyarlama ihtiyacını karşılar."
        ),
        "problem": (
            "İnsan her saniye RRM yazamaz. Klasik eşik yerel optimumda sıkışır. Enerji, kapasite ve "
            "hareket çekişir. Veri yoksa model uydurur; kara kutu düzenleyiciye açıklanamaz."
        ),
        "how_steps": [
            "Ölç: yük, SINR, PRB, enerji, arıza öncüleri.",
            "Karar: Near-RT RIC xApp (onlarca ms) hüzme/handover; Non-RT rApp (saniye+) enerji ve tahmin.",
            "Uygula: politika gNB'ye yazılır; geri alma yolu tasarımın parçasıdır.",
            "Öğren: ödül (kapasite, enerji, kesinti) kötüyse politika güncellenir.",
        ],
        "mental_model": (
            "Kapalı döngü: ölç → politika → uygula → ödül. Near-RT onlarca milisaniye, Non-RT saniye+. "
            "Denetim kalkmaz; yanlış öğrenen politika şebekeyi kilitleyebilir. "
            "GPU'nun kendisi enerji yer — net kazanç ölçülmelidir."
        ),
        "analogy": (
            "Klasik SON (Self-Organizing Network) atasıdır. Fark, öğrenmenin RRM'den (araştırma ucunda) "
            "hava arayüzüne kadar indirilme iddiasıdır. O-RAN açık arayüzdür; AI onun üstündeki uygulamadır."
        ),
        "analogy_technical_map": (
            "Durum s = RAN ölçümü; eylem a = RRM politikası; ödül r = kapasite veya enerji. "
            "Near-RT ≈ 10 ms mertebesi (O-RAN tanımı). Otokodlayıcı PHY, RRM'den ayrı bir öğrenme katmanıdır."
        ),
        "when_used": (
            "Değişken yük, enerji hedefi, kestirimci bakım, çok tedarikçili O-RAN denemesi. "
            "Ölçüm kalitesi yüksek ve geri alma prosedürü tanımlı ise."
        ),
        "when_not": (
            "Eğitilmemiş modelle canlı şebekeye otonom pilot denmez. '%50–70 enerji' ve 'sıfır insan' "
            "hedef/pazarlamadır; bu platformda saha faturası yoktur."
        ),
        "not_to_confuse": (
            "Bu platformdaki sohbet asistanı AI-RAN değildir. O-RAN ≠ AI: biri arayüz, diğeri uygulamadır."
        ),
        "real_world": (
            "O-RAN WG2/WG10, 3GPP TR 38.843 (AI/ML for NR), AI-RAN Alliance, operatör RIC PoC. "
            "Tam nöral hava arayüzü laboratuvar."
        ),
        "tt_impact": (
            "Maç çıkışı kaynak kaydırma, gece uyku, arıza öncülü. TRL 5. İnsan denetimi kapanmaz."
        ),
        "principle_html": (
            "<p><strong>1. Ölç:</strong> Yük, kanal, enerji, kopma.</p>"
            "<p><strong>2. Karar:</strong> <strong>RIC</strong> (RAN Intelligent Controller) üzerinde "
            "xApp/rApp politika üretir.</p>"
            "<p><strong>3. Uygula:</strong> Sonuç izlenir; geri alma yolu tasarımın parçasıdır.</p>"
            "<p><strong>Sonuç:</strong> Uyarlanan şebeke. Ölçüm + model + denetim.</p>"
        ),
        "arch_html": (
            "<p><strong>Katman 1 — Ölçüm / PHY:</strong> Klasik sinyal işleme veya araştırma ucunda nöral PHY.</p>"
            "<p><strong>Katman 2 — RIC:</strong> Near-RT xApp, Non-RT rApp. <strong>O-RAN</strong> bu katmanı taşır.</p>"
            "<p><strong>Katman 3 — Hızlandırıcı:</strong> NPU/GPU olabilir; net enerji kazancı hesaplanmalıdır.</p>"
            "<p>Kayıp fonksiyonu ve Q-öğrenme uzman kartlarındadır.</p>"
        ),
    },
    "ntn": {
        "card": (
            "Karasal gNB şehir ve asfaltı kapsar; dağ, deniz ve enkaz boş kalır. "
            "NTN (Non-Terrestrial Network — Karasal Olmayan Ağ) LEO ve HAPS düğümlerini Rel-17+ "
            "prosedürüyle çekirdeğe bağlar. Bedeli gecikme ve Doppler'dir. "
            "TRL 6 — TR 38.811; kamuya açık direct-to-cell denemeleri. Şehir kulesinin rakibi değil, tamamlayıcısı."
        ),
        "kicker": "Sorun: kule her yere ulaşmaz",
        "what": (
            "NTN, LEO (Low Earth Orbit — alçak dünya yörüngesi), GEO ve HAPS "
            "(High-Altitude Platform Station — yüksek irtifa platformu) düğümlerini karasal çekirdeğe "
            "3GPP Rel-17+ ile bağlayan mimaridir. Direct-to-cell: özel çanak yerine standart UE'nin "
            "uydu hücresini görmesi."
        ),
        "why_needed": (
            "Kapsama kule ve fiberin ulaştığı yer kadardır. Kırsal CAPEX, deniz, havacılık ve afet "
            "(kule yıkılınca) karasal modeli kırar. Aynı kimlik ve numara ile boşluğu kapatma ihtiyacıdır."
        ),
        "problem": (
            "Mesafe FSPL'yi büyütür; LEO ~7,5 km/s Doppler ve sık handover üretir. GEO gecikmesi "
            "konuşmayı zorlar. Spektrum, yer kapısı ve düzenleme operatör işidir."
        ),
        "how_steps": [
            "Öncelik: şehirde gNB; boşlukta uydu/HAPS hücresi.",
            "Yer kapısı: feeder link → gateway → çekirdek.",
            "Telafi: PHY'de Doppler ve gecikme ön düzeltmesi; aksi halde PRACH tutmaz.",
            "Servis sınıfı: acil SMS/ses önce; terabit şehir deneyimi vaadi değil.",
        ],
        "mental_model": (
            "Karasal birincil yoldur; NTN kapsama deliğini kapatır. Gecikme ~d/c (LEO onlarca ms, "
            "GEO gidiş-dönüş ~250 ms mertebesi, literatür). Direct-to-cell, telefon anteninin link "
            "bütçesine sığmasıdır — VSAT çanak değildir."
        ),
        "analogy": (
            "Aynı 3GPP kimliği, farklı radyo geometrisi. Tüketici LEO genişbantı (ör. Starlink) "
            "ile NTN hücresi aynı ürün olmak zorunda değildir."
        ),
        "analogy_technical_map": (
            "Feeder link + çekirdek = yer tarafı. Doppler f_d = f_c (v/c) cosθ. "
            "Link bütçesi FSPL + atmosfer + anten kazancı. Rel-17 NTN şartnamesi (TR 38.811) çerçevedir."
        ),
        "when_used": (
            "Kırsal, dağ, deniz, havacılık, afet yedek hattı, kulesiz IoT. Karasalın ekonomik olmadığı yer."
        ),
        "when_not": (
            "Şehir içi kapasite ve milisaniye altı URLLC için birincil yol değildir. "
            "'%100 küresel sıfır boşluk' pazarlamadır. Bu platformda uydu gecikmesi saha ölçülmedi."
        ),
        "not_to_confuse": (
            "VSAT çanak ≠ direct-to-cell. HAPS uydu değildir (stratosfer). "
            "ISAC 'gökyüzünü radar yapmak' NTN değildir."
        ),
        "real_world": (
            "3GPP TR 38.811, Rel-17/18 NTN iş kalemi, kamuya açık direct-to-cell denemeleri. "
            "Afet yedek hattı operatör stratejisidir, saha garantisi değil."
        ),
        "tt_impact": (
            "Afet hattı, filo, kırsal. TRL 6 — yedi teknoloji arasında en olgun dilim. Tamamlayıcı."
        ),
        "principle_html": (
            "<p><strong>1. Öncelik:</strong> Şehir kulede kalır. Boş coğrafyada <strong>LEO</strong> / <strong>HAPS</strong>.</p>"
            "<p><strong>2. Kimlik:</strong> Hedef 3GPP UE'nin uydu hücresini görmesidir.</p>"
            "<p><strong>3. Telafi:</strong> PHY Doppler ve gecikmeyi düzeltir; yer kulesi kadar düşük gecikme vaadi değildir.</p>"
            "<p><strong>Sonuç:</strong> Kapsama deliği kapanır. Rakip değil, tamamlayıcı.</p>"
        ),
        "arch_html": (
            "<p><strong>Katman 1 — Uzay/hava:</strong> LEO takımı, isteğe HAPS.</p>"
            "<p><strong>Katman 2 — Gateway:</strong> Feeder link → Türk Telekom yer kapısı → çekirdek.</p>"
            "<p><strong>Katman 3 — UE:</strong> Rel-17+ NTN modem; her eski cihaz garanti değildir.</p>"
            "<p>Doppler ve FSPL uzman kartlarındadır.</p>"
        ),
    },
    "ambient_iot": {
        "card": (
            "Koli ve sera ölçeğinde pil değiştirmek ekonomik değildir. Ambient IoT ortam RF'sinden "
            "enerji toplayıp backscatter (geri saçılım) ile kısa kimlik bildirir; video taşımaz. "
            "TRL 4 — TR 38.848; PoC sınıfı, raf ürünü değil."
        ),
        "kicker": "Sorun: her nesneye pil değiştirilemez",
        "what": (
            "Ambient IoT, pili olmayan veya çok küçük olan etiketlerin ortam RF'sinden "
            "(kule, Wi-Fi, yardımcı aydınlatıcı) enerji toplayıp çoğunlukla backscatter ile kısa "
            "durum mesajı verdiği IoT sınıfıdır. Amaç ucuz, seyrek izlemedir."
        ),
        "why_needed": (
            "Pil lojistiği koli/sera/sayaç ölçeğinde işlemez. NB-IoT ve RedCap hâlâ bir enerji "
            "kaynağı ister. Pilsiz etiket, 'nerede / kaç derece' işini bakım ekibi olmadan çözme ihtiyacıdır."
        ),
        "problem": (
            "Yansıyan güç zayıftır; menzil kısa, bit hızı düşüktür. Ortam enerjisi garanti değildir. "
            "Okuyucu hassas, protokol dardır. Telefonun yerini almaz."
        ),
        "how_steps": [
            "Topla: rectenna RF'yi DC'ye çevirir.",
            "Yansıt: anten empedansı ile gelen taşıyıcı modüle edilir; kendi PA'sı yoktur.",
            "Oku: yakındaki gNB veya okuyucu zayıf eko + biti ayırır.",
            "Yaz: 'koli 14, 4 °C' — video yok.",
        ],
        "mental_model": (
            "Friis hasadı × backscatter verimi = okunabilir bit. RF zayıf bölgede etiket susar. "
            "RFID atasıdır; fark 3GPP hücresel okuyucu ve adresleme hedefidir."
        ),
        "analogy": (
            "Pasif RFID'nin hücresel okuyucuya taşınması. Enerji hasatlı (güneş+pil) sensör ayrı sınıftır."
        ),
        "analogy_technical_map": (
            "Rectenna verimi η; gelen güç P_tx G_tx (λ/4πd)²; backscatter biti b(t). "
            "3GPP TR 38.848 Rel-19 çalışma kalemidir, ürün rafı değildir."
        ),
        "when_used": (
            "Palet, soğuk zincir, sera, sayaç, yapı sağlığı — kısa menzil, seyrek, düşük bit, uzun ömür."
        ),
        "when_not": (
            "Ses, görüntü, kilometre menzil, hareketli araç telemetrisi. '1 sent, trilyon nesne' "
            "hedef/pazarlamadır. RF'siz köşede etiket ölür."
        ),
        "not_to_confuse": (
            "Mağaza kapısı RFID atasıdır; hücresel çoklu okuyucu senaryosu farklıdır. "
            "ISAC işbirlikçi olmayan eko ölçer; Ambient IoT kasıtlı etikettir."
        ),
        "real_world": (
            "3GPP TR 38.848, akademik backscatter, ticari pilsiz etiket denemeleri. "
            "TT IoT platformuna akış senaryodur; her rafta değildir."
        ),
        "tt_impact": (
            "Depo paleti, sera, sayaç. TRL 4. Telefonun yerini almaz."
        ),
        "principle_html": (
            "<p><strong>1. Topla:</strong> Rectenna RF kırıntısını DC'ye çevirir.</p>"
            "<p><strong>2. Yansıt:</strong> Kendi PA'sı yoktur; gelen taşıyıcı modüle edilir. Menzil kısadır.</p>"
            "<p><strong>3. Oku:</strong> Yakın okuyucu zayıf yankıyı ayırır ve buluta yazar.</p>"
            "<p><strong>Sonuç:</strong> Ucuz, pilsiz, seyrek iz. Video taşımaz.</p>"
        ),
        "arch_html": (
            "<p><strong>Katman 1 — Etiket:</strong> ASIC + mikro kapasitör + rectenna.</p>"
            "<p><strong>Katman 2 — Okuyucu:</strong> gNB veya yardımcı aydınlatıcı; yüksek hassasiyet.</p>"
            "<p><strong>Katman 3 — Rel-19 / IoT bulutu:</strong> Dar adresleme, TT IoT platformu.</p>"
            "<p>Friis hasadı uzman kartlarındadır.</p>"
        ),
    },
}
