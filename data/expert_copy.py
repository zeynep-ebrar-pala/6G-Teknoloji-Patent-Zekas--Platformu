"""
Uzman katmanı — aynı başlık sırası, farklı cümleler.

Temel katman atlanmaz: problem → ihtiyaç → yöntem sırası korunur.
Üzerine denklem ilişkisi, varsayım, 3GPP referansı, alternatif ve sınır eklenir.
Anlatım telegraphic fragman değil; tam cümleli, terimli teknik prozedir.
"""

EXPERT_COPY = {
    "isac": {
        "problem": (
            "gNB (next-generation Node B — yeni nesil baz istasyonu) bugün yalnızca Shannon "
            "kanalını eniyiler: C = B log₂(1+SNR). Yansıyan enerjiden mesafe, hız veya açı "
            "çıkarmaz. Ayrı bir radar ikinci spektrum lisansı ve ikinci RF zinciri demektir; "
            "komşu bantlarda EMI (Electromagnetic Interference — elektromanyetik girişim) üretir. "
            "ISAC varsayımı şudur: haberleşme ile algılama aynı P_t ve B bütçesini paylaşır; "
            "iki bağımsız görev gibi davranmazlar."
        ),
        "why_needed": (
            "Operatör spektrumu ve kentsel site geometrisi zaten ödenmiştir. Ayrı bir UTM veya "
            "radar şebekesi CAPEX ile EMI yükünü ikiye katlar. ISAC’nin gerekçesi, mevcut EIRP’nin "
            "bir kısmını kestirim (gecikme, Doppler, geliş açısı) için kullanmaktır. Ödünleşme "
            "Pareto yüzeyindedir: iletişime ayrılan güç artınca kapasite yükselir, radar SNR’ı düşer. "
            "Bu platformda saha SNR ölçülmemiştir."
        ),
        "what": (
            "ISAC, DFRC (Dual-Functional Radar-Communication) ve JCR (Joint Communication and Sensing) "
            "aynı taşıyıcı ve dizi üzerinde kullanıcı düzlemi ile yansıyan ekonun ortak tasarımıdır. "
            "Mimari monostatik (aynı gNB hem Tx hem Rx) veya bistatik (komşu gNB Rx) olabilir. "
            "Yanına ayrı bir radar kutusu park etmek ISAC değildir; o durumda iki sistem, iki saat "
            "ve iki spektrum vardır."
        ),
        "mental_model": (
            "Gidiş yolunda güç serbest uzayda yaklaşık 1/R² ile yayılır; dönüşte hedef RCS "
            "(radar cross-section — radar kesiti, σ) üzerinden bir kez daha 1/R² zayıflama eklenir "
            "ve radar denkleminde R⁴ terimi doğar. Menzil çözünürlüğü ΔR ≈ c/(2B) ile verilir; "
            "bant dar ise santimetre çözünürlük fiziken çıkmaz. CRB (Cramér–Rao Bound) yansız "
            "kestiricinin varyans alt sınırıdır; Shannon kapasitesi C aynı güç ve bantı paylaşır. "
            "Uzak alan, nokta hedef ve clutter yok sayımı varsayımları kentte iyimser kalır."
        ),
        "how_steps": [
            "Dalga şekli olarak OFDM veya OTFS (Orthogonal Time Frequency Space) kullanıcı çerçevesi aynı zamanda radar probu işlevi görür; ayrı bir chirp kamyonu yoktur.",
            "Kestirimde τ = 2R/c menzili, f_d Doppler hızı, dizi faz farkı ise AoA/AoD’yi verir; FFT tabanlı kestirim yüksek SNR’de CRB’ye yaklaşır.",
            "Zaman, frekans veya kod dikliği bit ile ekonun birbirini bozmamasını hedefler; pratikte tam diklik çoğu zaman kırılır.",
            "Kenarda nokta bulutu veya iz özeti Near-RT RIC ya da kenar buluta gider; ham I/Q’nun fronthaul üzerinden taşınması Rel-19 ürün varsayımı değildir.",
        ],
        "analogy": (
            "Birinci alternatif, ayrı otomotiv veya askeri radar ile hücresel şebekenin yan yana "
            "çalışmasıdır: ürünler olgundur ama CAPEX ve EMI pahalıdır. İkinci alternatif kamera "
            "veya LiDAR’dır: semantik zengindir, sis, gece ve gizlilikte zayıftır. ISAC üçüncü "
            "sınıftır: ortak dalga şekli, spektrum tasarrufu adayı, clutter ve gizlilik kısıtı."
        ),
        "analogy_technical_map": (
            "Geçerlilik penceresi uzak alan, tek gidiş–dönüş ve düzenli istatistiksel modeldir. "
            "R iki katına çıkınca SNR_radar yaklaşık 16 kat (~12 dB) düşer. B artınca hem C hem "
            "ΔR incelir; buna karşılık gürültü ve işlem yükü büyür. 3GPP Rel-19 çalışma kalemi "
            "TR 22.837 çerçevedir; «1 cm» bu eşitsizlikten türetilmiş bir saha garantisi değildir."
        ),
        "when_used": (
            "Kule geometrisi sahneyi kestiğinde (yol, koridor, kıyı), optik kör kaldığında ve "
            "ayrı radar bandı lisanslanamadığında ISAC adaydır. Bistatik geometri küçük RCS’i "
            "büyütebilir. V2X ve UTM araştırma yatakları bu sınıfa girer."
        ),
        "when_not": (
            "Çoklu yansımalı kavşakta tek yol varsayımı kırılır. KVKK ve ePrivacy çözülmeden "
            "kamusal izleme ürünü değildir. Tıbbi mikro-Doppler literatürdür; cihaz onayı yoktur. "
            "Bu platformda saha CRB veya SNR ölçülmemiştir."
        ),
        "not_to_confuse": (
            "Aynı siteye konmuş ayrı radar, ISAC değildir. Bilgisayarlı görü piksel üretir; "
            "RF eko üretmez. Ambient IoT (TR 38.848) işbirlikçi etikettir; ISAC hedefi çoğu zaman "
            "işbirlikçi olmayan yansıtıcıdır."
        ),
        "real_world": (
            "TR 22.837 Rel-19 SI, Hexa-X-II mimari raporları, IEEE ComSoc ISAC ETI ve satıcı "
            "test yatakları bu izi taşır. Satıcıların «100 Gbps + 1 cm» iddiası bu platformda "
            "doğrulanmış bir metrik değildir."
        ),
        "tt_impact": (
            "Boğaz kıyı gNB’si su yolunu keser; dron koridoru kule azimutunu kullanır; enkazda "
            "optik yoktur. Olgunluk TRL 4’tür (laboratuvar / Rel-19 SI). Bu bir adaylıktır; "
            "abone şebekesinde ölçülmemiştir."
        ),
    },
    "ris": {
        "problem": (
            "mmWave ve üzeri bantlarda LoS (line of sight — görüş hattı) yoksa yol kaybı ve "
            "tıkanma kapasiteyi düşürür. Aktif röle kendi RF zincirini, güç yükseltecini ve "
            "girişimini taşır. RIS varsayımı kanalın iki hop’tan oluşmasıdır (gNB→RIS→UE); "
            "tek hop Friis modeli geçerli değildir."
        ),
        "why_needed": (
            "Kör nokta başına yeni gNB dikmek CAPEX ve EMC yüküdür. RIS, sınır koşulunu "
            "programlayarak ortamı kontrol edilebilir kanal yapma adayıdır. Enerji tasarrufu "
            "aktif röleye kıyasla bir iddiadır; N² ölçek ancak kanal kestirimi ve faz tutarlılığı "
            "varsa anlamlıdır. «%90 tasarruf» literatür veya hedeftir; bu platformda saha faturası yoktur."
        ),
        "what": (
            "RIS (Reconfigurable Intelligent Surface), N ayarlanabilir elemandan oluşur; "
            "PIN veya varaktör ile θ_n ∈ [0, 2π) aralığında faz yazılır. Etkin kanal "
            "h_rᴴ Φ G biçimindedir ve Φ = diag(e^{jθ_n})’dir. Yüzey internet üretmez; "
            "gNB aydınlatıcısını UE’ye (user equipment — kullanıcı ekipmanı) yönlendirir. "
            "ETSI RIS ISG ile Rel-19/20 çalışma kalemi bu sınıfı çerçeveler."
        ),
        "mental_model": (
            "Pasif veya yarı-pasif sınırda eleman alıcı değildir; kanalı kendi başına ölçemez. "
            "Çift yol kaybı (double path-loss) Tx→RIS→Rx çarpımıdır. İdeal faz hizasında N eleman "
            "güç kazancını yaklaşık N² ölçeğine taşır; CSI (channel state information — kanal "
            "durum bilgisi) gecikmesi veya faz kuantizasyonu bu ölçeği kırar. Denetleyici gecikmesi "
            "kullanıcı hızına yetmezse hüzme sapar."
        ),
        "how_steps": [
            "Yüzey cephe, cam veya tünelde PCB üzerinde PIN, MEMS veya LC elemanlarla kurulur; güç yükselteci yoktur veya sürücü miliwatt mertebesindedir.",
            "Faz yazımı FPGA veya MCU üzerinden yapılır; gNB C-plane komutu Φ’yi günceller ve kontrol hattı düşük bit hızlıdır.",
            "Pasif eleman ölçüm yapmadığı için Φ, gNB veya UE pilotlarından seçilir; bu adım kazancın koşuludur.",
            "Hüzme, dizi faktörü ile hedef UE’ye yönelir; «Snell ötesi» iddiası Maxwell yasalarını iptal etmez, yalnızca sınırı programlar.",
        ],
        "analogy": (
            "Aktif röle veya small cell kendi vericisini taşır; enerji ve girişim bedeli yüksektir. "
            "Pasif düz ayna faz programlanamaz. RIS programlanabilir bir sınırdır ve ortak "
            "aydınlatıcı gNB’dir. Üçü aynı CAPEX sınıfında değildir."
        ),
        "analogy_technical_map": (
            "Geçerlilik penceresi darbant, yavaş sönümlenme ve Φ güncellemesinin koherens "
            "süresinin altında kalmasıdır. N artınca teorik kazanç N²’ye gider; pratik kısıt "
            "kestirim boyutu ve kontrol gecikmesidir. RIS, ISAC ile birlikte kullanılabilir; "
            "tek başına radar denklemi yazmaz."
        ),
        "when_used": (
            "N-LoS kentsel kanyon, tünel kıvrımı, tribün, tarihi dokuda kule yasağı ve iç mekân "
            "mmWave geometrilerinde adaydır. Aktif röleden düşük enerji istenen ve kanal "
            "kestiriminin çözülebilir kabul edildiği senaryolarda tercih edilir."
        ),
        "when_not": (
            "Yüksek mobilite ile yavaş denetleyici bir arada olduğunda, CSI yoksa veya çift hop "
            "kaybının Friis tek hop’unu geçtiği uzun menzilde uygun değildir. Tak-çalıştır emtia "
            "her cephede yoktur. Türk Telekom şebekesinde henüz ölçülmemiştir (TRL 5, operatör denemesi)."
        ),
        "not_to_confuse": (
            "RIS small cell değildir. «Görünmez pelerin» pazarlaması metamalzeme sınırını abartır. "
            "Massive MIMO dizisi gNB’dedir; RIS ayrı bir yüzeydir."
        ),
        "real_world": (
            "ETSI ISG RIS, 3GPP Rel-19/20 RIS SI, RISE-6G ve ZTE/Huawei/NTT PoC’leri bu izi taşır. "
            "Operatör saha denemesi, abone şebekesinde varsayılan ürün anlamına gelmez."
        ),
        "tt_impact": (
            "Yarımada, tünel ve plaza camı: kule dikmeden kapsama adayıdır. Olgunluk TRL 5’tir "
            "(ilgili ortam prototipi). Kontrol hattı ve CSI prosedürü tasarlanmadan saha vaadi yazılmaz."
        ),
    },
    "cell_free": {
        "problem": (
            "Klasik hücresel dilimde kenar SINR_k paydası komşu hücrenin girişim terimidir. "
            "Handover, hücre kimliği değişince düşebilir. Varsayım tek serving gNB’dir; "
            "stadyum veya terminal yükünde bu varsayım kırılır."
        ),
        "why_needed": (
            "Dağıtık AP (access point — erişim noktası) yolu kısaltır ve girişimi ortak işlem "
            "(joint precoding) ile bastırılabilir kılar. Bedel fronthaul (eCPRI/RoF) kapasitesi "
            "ve senkronizasyondur (IEEE 1588 sınıfı). «5×–10× spektral kazanç» literatür aralığıdır; "
            "bu platformda ölçülmemiştir."
        ),
        "what": (
            "Cell-free Massive MIMO, M coğrafi AP’nin aynı TTI ve aynı frekansta K kullanıcıya "
            "ortak hizmet vermesidir. Hücre sınırı tasarım nesnesi olarak kalkar. Rel-19/20 "
            "dağıtık MIMO çalışma kalemi bu sınıfı çerçeveler; CoMP atasıdır ama hücre kimliğini tutmaz."
        ),
        "mental_model": (
            "SINR_k payı |Σ_m g_mkᴴ w_mk|², payda ise diğer kullanıcıların sızıntısı ile σ²’dir. "
            "Ağırlık vektörü w CPU’da MMSE veya ZF ile yazılır. Fronthaul gecikmesi veya faz "
            "kayması w’yi yanlış kılar ve kazanç tersine döner. Fiber yoksa ortak ön kodlama tanımsızdır."
        ),
        "how_steps": [
            "Yerleşimde düşük karmaşıklıklı AP’ler kullanılır; yerel DSP sınırlıdır, ağır matris işlemleri CPU veya kenarda yapılır.",
            "Fronthaul eCPRI veya RoF ile kurulur; senkron kaybı hüzme kazancını eritir.",
            "Ortak uplink pilot ile kanal kestirilir; pilot contamination hâlâ bir kısıttır.",
            "Ön kodlama MMSE veya ZF ile w_mk üretir; «kenar yok» iddiası senkron ve fronthaul varsayımına bağlıdır.",
        ],
        "analogy": (
            "Small-cell ormanı her hücrede kendi kenarını taşır. Klasik CoMP ortak işlem yapar "
            "ama hücre kimliği kalır. Wi-Fi roaming sembolü aynı anda çok AP’den taşımaz. "
            "Hücresiz MIMO, «hücre yok» varsayımına kadar gider."
        ),
        "analogy_technical_map": (
            "Geçerlilik için yeterince iyi CSI, fronthaul gecikmesinin koherens altında kalması "
            "ve faz kilitli dizi gerekir. Seyrek kırsalda her direğe fiber CAPEX açısından "
            "anlamsızdır; NTN veya makro alternatif kalır."
        ),
        "when_used": (
            "Yüksek yoğunluk, hareket ve adalet hedefi bir arada olduğunda (stadyum, havalimanı, "
            "üretim hattı, iç mekân) adaydır. Makro kule estetiğinin istenmediği geometride tercih edilir."
        ),
        "when_not": (
            "Seyrek kırsalda veya fiber olmayan caddede uygun değildir. CPU karmaşıklığı gerçek "
            "zamanı kaçırıyorsa kazanç tersine döner. «Her kullanıcıya terabit» bu platformda "
            "ölçülmemiştir. Olgunluk TRL 4’tür (literatür prototip)."
        ),
        "not_to_confuse": (
            "DAS (distributed antenna system) analog dağıtım olabilir; hücresiz MIMO dijital "
            "ortak ön kodlamadır. Massive MIMO tek sitede diziyi büyütmektir; cell-free coğrafi dağıtımdır."
        ),
        "real_world": (
            "Björnson/Larsson literatürü, IEEE cell-free özel sayıları, Rel-19/20 dağıtık MIMO "
            "ve Ericsson/Nokia laboratuvar gösterimleri bu izi taşır. Şehir geneli ürün değildir."
        ),
        "tt_impact": (
            "Havalimanı, stadyum ve depo kenar şikâyeti aday senaryolardır. Olgunluk TRL 4’tür. "
            "Önce yoğun mekân seçilir; fronthaul faturası tasarım kısıtıdır."
        ),
    },
    "thz": {
        "problem": (
            "Shannon’da C = B log₂(1+SNR) geçerlidir. Sub-6 ve mmWave’de B tavanı, veri merkezi "
            "içi mesh veya kule köprüsü için dar kalabilir. Frekans yükseldikçe FSPL ∝ (f d)² "
            "ve moleküler emilim e^{K(f)d} büyür. Varsayım LoS, hizalı hüzme ve kısa mesafedir."
        ),
        "why_needed": (
            "Fiber her geometriye gitmez. THz, doğru hop’ta onlarca GHz bant adayıdır. "
            "«Her aboneye 1 Tbps» pazarlamadır; emilimde SNR çökerse B yetmez. "
            "Olgunluk TRL 3’tür (TR 38.807); saha şebekesinde kullanılmamaktadır."
        ),
        "what": (
            "THz / sub-THz kabaca 0,1–10 THz aralığıdır; pratik 6G adayı çoğu zaman "
            "100–300 GHz penceresidir (NR beyond 52.6 GHz, TR 38.807). 5G mmWave "
            "(28–39 GHz) bu sınıf değildir. IEEE 802.15.3d ayrı bir WPAN izidir."
        ),
        "mental_model": (
            "Yol kaybı L(f,d) = (4π f d / c)² · e^{K(f)d} ile yazılır; K(f) su buharı "
            "çizgilerinde sıçrar. B büyüdükçe C neredeyse lineer artar, ancak SNR paydasındaki "
            "N_0 B ve emilim logaritmik terimi yer. Dar hüzme EIRP kazancı verir; blockage "
            "olasılığını yükseltir."
        ),
        "how_steps": [
            "Önce K(f)’nin düşük olduğu spektral pencereler seçilir; her THz hertz’i kullanılabilir değildir.",
            "RF ön uçta InP, GaN veya grafen adaydır; olgun CMOS bu bantta varsayılan çözüm değildir ve TRL’nin düşük kalmasının nedenidir.",
            "ADC/DAC yüksek örnekleme, güç ve ısı ister; 100 GSa/s sınıfı iddia literatür veya hedeftir.",
            "Geometri raf, salon veya kule hop’u ile sınırlıdır; makro sokak bu denklemin geçerlilik penceresi dışındadır.",
        ],
        "analogy": (
            "Kablosuz fiber benzetmesi yüksek B, kısa d ve hizalı hüzmeyi anlatır. "
            "Serbest uzay optiği (lazer) farklı dalga boyudur; sis ve yağmurda ayrı fizik "
            "geçerlidir. Makro hücresel taşıyıcı THz değildir."
        ),
        "analogy_technical_map": (
            "Geçerlilik LoS, dar hüzme, onlarca–yüzlerce metre mesafe ve yağmursuz veya kısa "
            "hop varsayar. El veya yaprak keser (blockage). «Hacklenmesi imkânsız» iddiası "
            "dar hüzmeden türetilmiş bir güvenlik garantisi değildir."
        ),
        "when_used": (
            "Veri merkezi mesh, kısa backhaul/fronthaul, kontrollü iç mekân ve spektroskopi "
            "adaydır. Yedek LoS ve hizalama bütçesi varsa anlamlıdır."
        ),
        "when_not": (
            "Açık şehir makrosu, uzun yağmurlu hop, cep–cep kilometre ve tıbbi nanosensör "
            "Rel-19 özelliği bu sınıf değildir. 6G yalnızca THz demek değildir. "
            "Bu platformda Tbps ölçülmemiştir."
        ),
        "not_to_confuse": (
            "mmWave, THz değildir. ISAC THz dalga şekli kullanabilir; THz tek başına "
            "algılama standardı değildir."
        ),
        "real_world": (
            "IEEE 802.15.3d, ITU-R WRC spektrum çalışmaları, TR 38.807 ve satıcı sub-THz "
            "gösterimleri bu izi taşır. Abone elsetinde varsayılan bant değildir."
        ),
        "tt_impact": (
            "Raf ve fiber çekilemeyen kule köprüsü adaydır. Olgunluk TRL 3’tür (laboratuvar). "
            "Cep hızı vaadi yazılmaz."
        ),
    },
    "ai_ran": {
        "problem": (
            "Sabit RRM eşiği yerel optimumda sıkışır; trafik, kanal ve enerji non-stationary’dir. "
            "İnsan her 10 ms’de politika yazamaz. Varsayım ölçüm kalitesinin yüksek ve geri "
            "almanın tanımlı olmasıdır. Kara kutu düzenleyiciye açıklanamaz; bu bir ürün "
            "kısıtıdır, stil tercihi değildir."
        ),
        "why_needed": (
            "Near-RT RIC (~10 ms, O-RAN tanımı) hüzme ve handover’ı; Non-RT rApp saniye ve "
            "üzerinde enerji ile kestirimi yönetir. Öğrenen döngü ölçüme bağlı uyarlama "
            "ihtiyacını karşılar. GPU/NPU kendi enerjisini yer; net kazanç ölçülmeden "
            "«%50–70» iddiası hedef veya pazarlamadır. Referanslar TR 38.843 ile O-RAN WG2/10’dur."
        ),
        "what": (
            "AI-native RAN iki kattır. Birinci kat pratik giriştir: xApp/rApp ile RRM politikası. "
            "İkinci kat araştırma ucudur: otokodlayıcı PHY ve hava arayüzünün öğrenilmiş temsili. "
            "O-RAN bir arayüzdür; AI uygulamadır. Sohbet asistanı AI-RAN değildir."
        ),
        "mental_model": (
            "Pekiştirmeli öğrenmede durum s (SINR, PRB, yük), eylem a (RRM kararı) ve ödül r "
            "(kapasite, enerji, kesinti) tanımlanır; güncelleme Q(s,a) ← Q + α[r + γ max Q′ − Q] "
            "biçimindedir. Otokodlayıcı kaybı E[||s − f_D(f_E(s)+n)||²] ile yazılır. "
            "Yanlış ödül şebekeyi kilitleyebilir; rollback tasarımın parçasıdır ve denetim kalkmaz."
        ),
        "how_steps": [
            "Önce yük, SINR, PRB, enerji ve arıza öncülü ölçülür; model verinin kalitesini aşamaz.",
            "Near-RT xApp onlarca milisaniyede hüzme ve handover’ı günceller; Non-RT rApp saniye ölçeğinde uyku ve tahmin uygular.",
            "Politika gNB’ye yazılır; geri alma yolu yoksa canlı şebekeye otonom pilot denmez.",
            "Ödül kötüyse öğrenme güncellenir; zero-touch (ZTN) araştırma ucudur ve saha kanıtı yoktur (TRL 5).",
        ],
        "analogy": (
            "Klasik SON kural tabanlı self-organizing’dir. AI-RAN RRM öğrenilmiş politika ile "
            "aynı döngüyü ölçüm şartına bağlar. Nöral PHY ayrı bir katmandır; Rel-18 / TR 38.843 "
            "çalışma alanıdır ve laboratuvardadır."
        ),
        "analogy_technical_map": (
            "Geçerlilik için i.i.d. olmayan trafik ve dağılım kayması (drift) izlenmelidir. "
            "Açıklanabilirlik (XAI) düzenleyici bir kısıttır. O-RAN çok tedarikçili AI garantisi "
            "değildir; arayüz standardıdır."
        ),
        "when_used": (
            "Değişken yük, enerji hedefi, kestirimci bakım ve RIC denemesinde adaydır. "
            "Ölçüm kalitesi ve rollback tanımlıysa anlamlıdır."
        ),
        "when_not": (
            "Eğitilmemiş model, saha verisi yokluğu veya kara kutunun kabul edilmediği "
            "ortamlarda uygun değildir. «Sıfır insan» pazarlamadır. Bu platformda enerji "
            "faturası ölçülmemiştir."
        ),
        "not_to_confuse": (
            "Platform sohbet botu AI-RAN değildir. O-RAN açık arayüzdür; AI onun üstünde "
            "xApp olabilir veya olmayabilir."
        ),
        "real_world": (
            "AI-RAN Alliance, O-RAN WG2/WG10, TR 38.843, NVIDIA Aerial test yatakları ve "
            "operatör RIC PoC’leri bu izi taşır. Tam nöral hava arayüzü laboratuvardadır."
        ),
        "tt_impact": (
            "Maç çıkışı kaynak kaydırma, gece uyku ve arıza öncülü aday senaryolardır. "
            "Olgunluk TRL 5’tir (RIC deneme sınıfı). İnsan denetimi kapanmaz."
        ),
    },
    "ntn": {
        "problem": (
            "Karasal kapsama kule ve fiber geometrisidir. LEO yaklaşık 500–1200 km irtifada "
            "v ≈ 7,5 km/s ile hareket eder; Doppler f_d = f_c (v/c) cosθ ve sık handover doğurur. "
            "GEO RTT yaklaşık 250 ms sınıfındadır (literatür). FSPL ∝ (d f)²’dir. Varsayım "
            "Rel-17+ NTN modem, feeder link ve gateway’dir."
        ),
        "why_needed": (
            "Kırsal CAPEX, deniz, havacılık ve afet (site düşünce) karasal modeli kırar. "
            "Aynı 3GPP kimliği ile boşluğu kapatma ihtiyacıdır. Şehir kapasitesi ve URLLC için "
            "birincil yol değildir. Olgunluk TRL 6’dır (TR 38.811, kamuya açık direct-to-cell)."
        ),
        "what": (
            "NTN, LEO, GEO veya HAPS düğümünün Rel-17+ ile karasal çekirdeğe bağlanmasıdır. "
            "Direct-to-cell, standart UE’nin uydu hücresini görmesidir; VSAT çanak değildir. "
            "HAPS stratosfer platformudur, uydu değildir. Tüketici LEO genişbantı ile NTN "
            "hücresi aynı ürün olmak zorunda değildir."
        ),
        "mental_model": (
            "Karasal birincildir; NTN kapsama deliğini kapatır. Link bütçesi FSPL, atmosfer "
            "ve anten kazancından oluşur. PHY’de Doppler ve gecikme ön düzeltmesi yoksa PRACH "
            "tutmaz. Regenerative payload uyduda gNB işler; transparent payload yere taşır — "
            "ikisi aynı gecikme sınıfında değildir."
        ),
        "how_steps": [
            "Hücre seçiminde şehirde gNB, boşlukta NTN hücresi tercih edilir; öncelik karasaldır.",
            "Feeder uydu → gateway → 5GC/6GC yolunu kurar; yer kapısı operatör varlığıdır.",
            "f_d ve timing advance telafi edilir; Rel-17 NTN şartnamesi (TR 38.811) çerçevedir.",
            "Servis sınıfında acil SMS/ses önce gelir; terabit şehir deneyimi bu denklemin çıktısı değildir.",
        ],
        "analogy": (
            "VSAT çanaklı ayrı bir sistemdir. Direct-to-cell elset anteni ve Rel-17+ modem kullanır. "
            "HAPS yaklaşık 20 km sınıfindadır ve uydu yörüngesi değildir. ISAC «gökyüzü radarı» "
            "NTN değildir."
        ),
        "analogy_technical_map": (
            "Geçerlilik görünür uydu, yeterli EIRP ve düzenlenmiş spektrum varsayar. "
            "«%100 küresel sıfır boşluk» pazarlamadır. Bu platformda uydu gecikmesi saha ölçülmemiştir."
        ),
        "when_used": (
            "FSPL ve saha CAPEX karasal hop’u geçersiz kıldığında (kırsal/dağ, deniz, havacılık, "
            "kule düşünce afet yedek) adaydır. Feeder ve gateway şarttır; regenerative ile "
            "transparent payload gecikme sınıfını belirler. Şehir makro kapasitesinin yerine geçmez."
        ),
        "when_not": (
            "Şehir içi kapasite ve sub-ms URLLC birincil yol olarak uygun değildir. "
            "Her eski cihaz Rel-17 NTN garantisi taşımaz."
        ),
        "not_to_confuse": (
            "Direct-to-cell VSAT değildir. HAPS LEO değildir. NTN tamamlayıcıdır; "
            "6G makrosunun rakibi değildir."
        ),
        "real_world": (
            "TR 38.811, Rel-17/18/19 NTN WI ve kamuya açık direct-to-cell denemeleri "
            "(operatör–uydu ortaklıkları) bu izi taşır. Afet yedek hattı stratejidir; "
            "saha garantisi değildir."
        ),
        "tt_impact": (
            "Afet, filo ve kırsal aday senaryolardır. Olgunluk TRL 6’dır — yedi dilimin en "
            "olgunu. Tamamlayıcıdır; şehir kulesinin yerine geçmez."
        ),
    },
    "ambient_iot": {
        "problem": (
            "NB-IoT veya RedCap hâlâ bir enerji kaynağı ister. Palet ve sera ölçeğinde pil "
            "lojistiği CAPEX ve OPEX’tir. Backscatter yansıyan gücü zayıftır; menzil Friis "
            "hasadı ile η_rectenna çarpımıyla sınırlıdır. Varsayım ortamda yeterli RF, yakın "
            "okuyucu ve dar bittir."
        ),
        "why_needed": (
            "«Nerede / kaç derece» işi bakım ekibi olmadan yapılmak istenir. Amaç video değil, "
            "seyrek kimliktir. «1 sent, trilyon nesne» hedef veya pazarlamadır. TR 38.848 "
            "Rel-19 SI’dir; ticari dağıtım aşamasında değildir."
        ),
        "what": (
            "Ambient IoT pilsiz veya mikro-kapasitörlü etikettir; rectenna RF’yi DC’ye çevirir "
            "ve iletişim çoğunlukla backscatter’tır (anten empedansı ile gelen taşıyıcıyı "
            "modüle eder, PA yoktur). Okuyucu gNB veya yardımcı aydınlatıcıdır. ISAC "
            "işbirlikçi olmayan eko ölçer; bu sınıf kasıtlı etikettir."
        ),
        "mental_model": (
            "Alınan güç P_rec = P_tx G_tx G_rx (λ/4πd)² η ile yazılır; gözlenen sinyal "
            "y(t) = α x(t) b(t) + n(t) biçimindedir. RF zayıf ceplede etiket susar — sıfır "
            "pil maliyeti enerji garantisi değildir. RFID atasıdır; fark 3GPP hücresel "
            "okuyucu ve Rel-19 adresleme hedefidir."
        ),
        "how_steps": [
            "Hasat rectenna ile yapılır; verim η < 1’dir ve mesafe Friis ile düşer.",
            "Modülasyon b(t) empedans anahtarıdır; kendi PA’sı yoktur ve menzil kısa kalır (literatürde çoğu zaman 10–50 m sınıfı, geometriye bağlı).",
            "Okuma yüksek hassasiyetli dizi ile zayıf eko ve biti ayırır; protokol dardır (kbps).",
            "Buluta dar kimlik gider («koli, °C»); video veya zengin telemetri bu denklemden çıkmaz.",
        ],
        "analogy": (
            "Mağaza kapısı RFID atasıdır ama hücresel çoklu okuyucu değildir. Güneş veya "
            "pilli hasatlı sensör ayrı bir sınıftır; Ambient IoT her zaman «sıfır pil» "
            "iddiası taşımaz. ISAC işbirlikçi olmayan yansıtıcıyı ölçer."
        ),
        "analogy_technical_map": (
            "Geçerlilik aydınlatıcının mevcut, mesafenin kısa ve bitin seyrek olmasını "
            "varsayar. Sınırsız ömür ancak okunabilir bit hasada bağlıdır. TT sahası "
            "ölçülmemiştir (TRL 4)."
        ),
        "when_used": (
            "Palet, soğuk zincir, sera, sayaç ve yapı sağlığı — kısa menzil, düşük bit "
            "ve uzun ömür hedefi bir arada olduğunda adaydır."
        ),
        "when_not": (
            "Ses veya görüntü, kilometre menzil, hareketli araç telemetrisi ve RF’siz "
            "köşe uygun değildir. Telefonun yerini almaz."
        ),
        "not_to_confuse": (
            "Shop-floor RFID, Rel-19 Ambient IoT değildir. Energy-harvesting (güneş) "
            "sensör backscatter etiket değildir."
        ),
        "real_world": (
            "TR 38.848, akademik backscatter ve Wiliot/Qualcomm pilsiz etiket denemeleri "
            "bu izi taşır. TT IoT platformuna akış senaryodur; her rafta değildir."
        ),
        "tt_impact": (
            "Depo paleti, sera ve sayaç adaydır. Olgunluk TRL 4’tür (PoC). "
            "Pil lojistiğini silme vaadi saha ölçümü değildir."
        ),
    },
}
