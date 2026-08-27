"""
Uzman katmanı — aynı başlık sırası, farklı cümle.
Temel katmanı atlamaz: problem→ihtiyaç→yöntem durur; üzerine denklem, varsayım, 3GPP, alternatif, sınır eklenir.
"""

EXPERT_COPY = {
    "isac": {
        "problem": (
            "gNB (next-generation Node B) yalnızca Shannon kanalını (C = B log₂(1+SNR)) eniyiler; "
            "yansıyan enerjiden kinematik çıkarmaz. Ayrı radar, ikinci spektrum lisansı ve ikinci RF zinciri "
            "demektir; komşu bant EMI (Electromagnetic Interference — elektromanyetik girişim) üretir. "
            "Varsayım: haberleşme ve algılama aynı P_t ve B bütçesini paylaşır — bağımsız iki görev değildir."
        ),
        "why_needed": (
            "Operatör spektrumu ve kentsel site geometrisi zaten ödenmiştir. Ayrı bir UTM/radar şebekesi "
            "CAPEX + EMI'yi ikiye katlar. ISAC'nin rasyoneli, mevcut EIRP'nin bir kısmını kestirim "
            "(delay, Doppler, AoA) için kullanmaktır. Ödünleşme Pareto yüzeyindedir: P_com artınca C artar, "
            "SNR_radar düşer. Bu platformda saha SNR ölçülmedi."
        ),
        "what": (
            "ISAC / DFRC (Dual-Functional Radar-Communication) / JCR (Joint Communication and Sensing): "
            "aynı taşıyıcı ve dizi üzerinde kullanıcı düzlemi ile yansıyan ekonun ortak tasarımı. "
            "Monostatik (aynı gNB Tx/Rx) veya bistatik (komşu gNB Rx) olabilir. Yanına radar kutusu "
            "park etmek ISAC değildir; o iki sistem, iki saat, iki spektrumdur."
        ),
        "mental_model": (
            "Gidiş: serbest uzay ~1/R². Dönüş: hedef RCS (radar cross-section, σ) üzerinden bir kez daha "
            "~1/R² → radar denkleminde R⁴. ΔR ≈ c/(2B) menzil çözünürlüğüdür; B dar ise santimetre fiziken "
            "çıkmaz. CRB (Cramér–Rao Bound) yansız kestiricinin varyans tabanıdır; Shannon C aynı P ve B'yi "
            "paylaşır. Far-field, nokta hedef, clutter yok sayılır — kentte bu varsayım iyimserdir."
        ),
        "how_steps": [
            "Dalga şekli: OFDM veya OTFS (Orthogonal Time Frequency Space) kullanıcı çerçevesi aynı zamanda radar probudur; ayrı chirp kamyonu yoktur.",
            "Kestirim: τ = 2R/c menzil, f_d Doppler hız, dizi faz farkı AoA/AoD. FFT tabanlı kestirim yüksek SNR'de CRB'ye yaklaşır.",
            "Kaynak paylaşımı: zaman/frekans/kod dikliği (orthogonal) bit ile ekonun birbirini bozmamasını hedefler; tam diklik pratikte kırılır.",
            "Kenar: nokta bulutu veya iz özeti Near-RT RIC / kenar buluta gider. Ham I/Q fronthaul'u Rel-19 ürün varsayımı değildir.",
        ],
        "analogy": (
            "Alternatif 1: ayrı otomotiv/askeri radar + hücresel şebeke — olgun, CAPEX/EMI pahalı. "
            "Alternatif 2: kamera/LiDAR — semantik zengin, sis/gece/gizlilik zayıf. "
            "ISAC üçüncü sınıf: ortak dalga şekli, spektrum tasarrufu adayı, clutter ve gizlilik kısıtı."
        ),
        "analogy_technical_map": (
            "Geçerlilik: uzak alan, tek gidiş-dönüş, düzenli istatistiksel model. "
            "R iki katına çıkınca SNR_radar ~16 kat (~12 dB) düşer. B artınca hem C hem ΔR incelir ama gürültü ve işlem büyür. "
            "3GPP Rel-19 çalışma kalemi TR 22.837 çerçevedir; 1 cm bu eşitsizlikten türetilmiş saha garantisi değildir."
        ),
        "when_used": (
            "Kule geometrisi sahneyi kesiyorsa (yol, koridor, kıyı), optik kör, ayrı radar bandı lisanslanamıyorsa. "
            "Bistatik geometri küçük RCS'i büyütebilir. V2X / UTM araştırma yatağı bu sınıfa girer."
        ),
        "when_not": (
            "Çoklu yansımalı kavşakta tek yol varsayımı kırılır. KVKK/ePrivacy çözülmeden kamusal izleme ürünü değildir. "
            "Tıbbi mikro-Doppler literatürdür, cihaz onayı yoktur. Bu platformda saha CRB/SNR ölçülmedi."
        ),
        "not_to_confuse": (
            "Co-sited radar ≠ ISAC. Computer vision piksel üretir; RF eko üretmez. "
            "Ambient IoT (TR 38.848) işbirlikçi etikettir; ISAC hedefi çoğu zaman non-cooperative yansıtıcıdır."
        ),
        "real_world": (
            "TR 22.837 Rel-19 SI, Hexa-X-II mimari raporları, IEEE ComSoc ISAC ETI, satıcı test yatağı. "
            "Satıcı '100 Gbps + 1 cm' birlikte bu platformda doğrulanmış metrik değildir."
        ),
        "tt_impact": (
            "Boğaz kıyı gNB'si su yolunu keser; dron koridoru kule azimutunu kullanır; enkaz optik yok. "
            "TRL 4 — laboratuvar / Rel-19 SI. Adaylık; abone şebekesinde ölçülmedi."
        ),
    },
    "ris": {
        "problem": (
            "mmWave ve üzeri bantlarda LoS (line of sight) yoksa yol kaybı ve tıkanma kapasiteyi düşürür. "
            "Aktif röle kendi RF zinciri, PA'sı ve girişimini taşır. Varsayım: kanal iki hoptur "
            "(gNB→RIS→UE); tek hop Friis geçerli değildir."
        ),
        "why_needed": (
            "Kör nokta başına gNB, CAPEX ve EMC yüküdür. RIS, sınır koşulunu programlayarak ortamı "
            "kontrol edilebilir kanal yapma adayıdır. Enerji tasarrufu, aktif röleye kıyasla iddiadır; "
            "N² ölçek ancak kanal kestirimi ve faz tutarlılığı varsa. %90 tasarruf literatür/hedef; "
            "bu platformda saha faturası yok."
        ),
        "what": (
            "RIS (Reconfigurable Intelligent Surface): N ayarlanabilir eleman, PIN/varaktör ile "
            "θ_n ∈ [0, 2π). Etkin kanal h_rᴴ Φ G, Φ = diag(e^{jθ_n}). Yüzey internet üretmez; "
            "gNB aydınlatıcısını UE'ye (user equipment) yönlendirir. ETSI RIS ISG + Rel-19/20 çalışma kalemi."
        ),
        "mental_model": (
            "Pasif/yarı-pasif sınır: eleman alıcı değildir, kanalı kendi başına ölçemez. "
            "Çift yol kaybı (double path-loss) Tx→RIS→Rx çarpımıdır. İdeal faz hizasında N eleman "
            "güç ~N²; CSI (channel state information) gecikmesi veya faz kuantizasyonu bu ölçeği kırar. "
            "Denetleyici gecikmesi kullanıcı hızına yetmezse hüzme sapar."
        ),
        "how_steps": [
            "Yüzey: cephe/cam/tünel — PCB üzerinde PIN/MEMS/LC eleman; PA yok veya mW mertebesi sürücü.",
            "Faz yazımı: FPGA/MCU, gNB C-plane komutuyla Φ'yi günceller. Kontrol hattı düşük bit hızlıdır.",
            "Kanal kestirimi: pasif eleman ölçmez; gNB/UE pilotlarından Φ seçilir. Bu adım kazancın koşuludur.",
            "Hüzme: dizi faktörü hedef UE'ye. Snell ötesi yönlendirme iddiası Maxwell'i iptal etmez; sınır programlanır.",
        ],
        "analogy": (
            "Aktif röle / small cell: kendi vericisi var, enerji ve girişim taşır. "
            "Pasif yansıtıcı (düz ayna): faz programlanamaz. "
            "RIS: programlanabilir sınır, ortak aydınlatıcı gNB. Üçü aynı CAPEX sınıfı değildir."
        ),
        "analogy_technical_map": (
            "Geçerlilik: darband, yavaş sönümlenme, Φ güncellemesi koherens süresinin altında. "
            "N artınca kazanç teoretik N²; pratik kısıt kestirim boyutu ve kontrol gecikmesidir. "
            "ISAC ile birlikte kullanılabilir; RIS tek başına radar denklemi yazmaz."
        ),
        "when_used": (
            "N-LoS kentsel kanyon, tünel kıvrımı, tribün, tarihi dokuda kule yasağı, iç mekân mmWave. "
            "Aktif röleden düşük enerji istenen geometri; kanal kestirimi çözülebilir kabul edilir."
        ),
        "when_not": (
            "Yüksek mobilite + yavaş denetleyici. CSI yok. Çift hop kaybının Friis tek hopu geçtiği uzun menzil. "
            "Tak-çalıştır emtia her cephede yoktur. Türk Telekom şebekesinde henüz ölçülmemiştir (TRL 5, operatör denemesi)."
        ),
        "not_to_confuse": (
            "Small cell değildir. 'Görünmez pelerin' pazarlaması metamalzeme sınırını abartır. "
            "Massive MIMO dizisi gNB'dedir; RIS ayrı bir yüzeydir."
        ),
        "real_world": (
            "ETSI ISG RIS, 3GPP Rel-19/20 RIS SI, RISE-6G, ZTE/Huawei/NTT PoC. "
            "Operatör saha denemesi ≠ abone şebekesinde varsayılan ürün."
        ),
        "tt_impact": (
            "Yarımada, tünel, plaza camı: kule dikmeden kapsama adayı. TRL 5 — ilgili ortam prototipi. "
            "Kontrol hattı ve CSI prosedürü tasarlanmadan saha vaadi yazılmaz."
        ),
    },
    "cell_free": {
        "problem": (
            "Klasik hücresel dilimde kenar SINR_k paydası komşu hücrenin girişim terimidir. "
            "Handover, hücre kimliği değişince düşer. Varsayım: tek serving gNB. "
            "Bu varsayım stadyum/terminal yükünde kırılır."
        ),
        "why_needed": (
            "Dağıtık AP (access point) yolu kısaltır ve girişimi ortak işlemle (joint precoding) "
            "bastırılabilir kılar. Bedel fronthaul (eCPRI/RoF) kapasitesi ve senkron (IEEE 1588 sınıfı). "
            "5×–10× spektral kazanç literatür aralığıdır; bu platformda ölçülmedi."
        ),
        "what": (
            "Cell-free Massive MIMO: M coğrafi AP, aynı TTI ve aynı frekansta K kullanıcıya ortak hizmet. "
            "Hücre sınırı tasarım nesnesi olarak kalkar. Rel-19/20 dağıtık MIMO çalışma kalemi; "
            "CoMP atasıdır ama hücre kimliğini tutmaz."
        ),
        "mental_model": (
            "SINR_k payı |Σ_m g_mkᴴ w_mk|², payda diğer kullanıcıların sızıntısı + σ². "
            "w CPU'da MMSE veya ZF ile yazılır. Fronthaul gecikmesi veya faz kayması w'yi yanlış kılar; "
            "kazanç tersine döner. Fiber yoksa ortak ön kodlama tanımsızdır."
        ),
        "how_steps": [
            "Yerleşim: düşük karmaşıklıklı AP; yerel DSP sınırlı, ağır matris CPU/kenarda.",
            "Fronthaul: eCPRI veya RoF; senkron kaybı hüzme kazancını eritir.",
            "Kestirim: ortak uplink pilot; pilot contamination hâlâ kısıttır.",
            "Ön kodlama: MMSE/ZF w_mk. Kenar 'yok' iddiası senkron+fronthaul varsayımına bağlıdır.",
        ],
        "analogy": (
            "Small-cell ormanı: her hücre kendi kenarını taşır. "
            "Klasik CoMP: ortak işlem, hücre kimliği kalır. "
            "Wi-Fi roaming: sembol aynı anda çok AP'den taşınmaz. "
            "Hücresiz MIMO: 'hücre yok' varsayımına kadar gider."
        ),
        "analogy_technical_map": (
            "Geçerlilik: mükemmel veya yeterince iyi CSI, fronthaul gecikmesi koherens altında, "
            "faz kilitli dizi. Seyrek kırsalda her direğe fiber CAPEX-anlamsızdır — NTN/makro alternatif."
        ),
        "when_used": (
            "Yüksek yoğunluk + hareket + adalet hedefi: stadyum, havalimanı, üretim hattı, iç mekân. "
            "Makro estetiğinin istenmediği geometri."
        ),
        "when_not": (
            "Seyrek kırsal, fiber olmayan cadde. CPU karmaşıklığı gerçek zamanı kaçırıyorsa. "
            "Terabit 'her kullanıcı' bu platformda ölçülmedi. TRL 4, literatür prototip."
        ),
        "not_to_confuse": (
            "DAS (distributed antenna system) analog dağıtım olabilir; hücresiz MIMO dijital ortak ön kodlamadır. "
            "Massive MIMO tek sitede dizi büyütmektir; cell-free coğrafi dağıtımdır."
        ),
        "real_world": (
            "Björnson/Larsson literatürü, IEEE cell-free özel sayıları, Rel-19/20 dağıtık MIMO, "
            "Ericsson/Nokia laboratuvar gösterimi. Şehir geneli ürün değil."
        ),
        "tt_impact": (
            "Havalimanı, stadyum, depo kenar şikâyeti. TRL 4. Önce yoğun mekân; fronthaul faturası tasarım kısıtıdır."
        ),
    },
    "thz": {
        "problem": (
            "Shannon'da C = B log₂(1+SNR). Sub-6 ve mmWave'de B tavanı intra-DC mesh ve kule köprüsü için "
            "dar kalabilir. Frekans yükseldikçe FSPL ∝ (f d)² ve moleküler emilim e^{K(f)d} büyür. "
            "Varsayım: LoS, hizalı hüzme, kısa d."
        ),
        "why_needed": (
            "Fiber her geometriye gitmez. THz, doğru hopta onlarca GHz B adayıdır. "
            "'1 Tbps her abone' pazarlamadır; C, SNR emilimde çökerse B yetmez. "
            "TRL 3 — TR 38.807; saha şebekesinde kullanılmamaktadır."
        ),
        "what": (
            "THz / sub-THz: kabaca 0,1–10 THz, pratik 6G adayı çoğu zaman 100–300 GHz penceresi "
            "(NR beyond 52.6 GHz, TR 38.807). 5G mmWave (28–39 GHz) bu sınıf değildir. "
            "IEEE 802.15.3d ayrı bir WPAN izidir."
        ),
        "mental_model": (
            "L(f,d) = (4π f d / c)² · e^{K(f)d}. K(f) su buharı çizgilerinde sıçrar. "
            "B büyüdükçe C neredeyse lineer artar ancak SNR paydasındaki N_0 B ve emilim log terimini yer. "
            "Dar hüzme EIRP kazancı verir, blockage olasılığını yükseltir."
        ),
        "how_steps": [
            "Pencere seçimi: K(f) düşük spektral pencereler; 'her THz Hertz' kullanılabilir değildir.",
            "RF ön uç: InP/GaN/grafen adayları; olgun CMOS değildir — TRL'nin düşük olmasının nedeni.",
            "ADC/DAC: yüksek örnekleme, güç ve ısı. 100 GSa/s sınıfı iddia literatür/hedeftir.",
            "Geometri: raf, salon, kule hop. Makro sokak bu denklemin geçerlilik penceresi dışındadır.",
        ],
        "analogy": (
            "Kablosuz fiber: yüksek B, kısa d, hizalı. "
            "Serbest uzay optiği (lazer): farklı dalga boyu, sis/yağmurda ayrı fizik. "
            "Makro hücresel taşıyıcı: THz değildir."
        ),
        "analogy_technical_map": (
            "Geçerlilik: LoS, dar hüzme, d onlarca–yüzlerce metre, yağmursuz veya kısa hop. "
            "El/yaprak keser (blockage). 'Hacklenmesi imkânsız' dar hüzmeden türetilmiş güvenlik garantisi değildir."
        ),
        "when_used": (
            "Veri merkezi mesh, kısa backhaul/fronthaul, kontrollü iç mekân, spektroskopi. "
            "Yedek LoS ve hizalama bütçesi varsa."
        ),
        "when_not": (
            "Açık şehir makrosu, uzun yağmurlu hop, cep-cep kilometre, tıbbi nanosensör Rel-19 özelliği. "
            "6G = yalnızca THz değildir. Bu platformda Tbps ölçülmedi."
        ),
        "not_to_confuse": (
            "mmWave ≠ THz. ISAC THz dalga şekli kullanabilir; THz tek başına algılama standardı değildir."
        ),
        "real_world": (
            "IEEE 802.15.3d, ITU-R WRC spektrum çalışmaları, TR 38.807, satıcı sub-THz gösterimleri. "
            "Abone elsetinde varsayılan bant değil."
        ),
        "tt_impact": (
            "Raf ve fiber çekilemeyen kule köprüsü adayı. TRL 3, laboratuvar. Cep hızı vaadi yazılmaz."
        ),
    },
    "ai_ran": {
        "problem": (
            "Sabit RRM eşiği yerel optimumda sıkışır; trafik/kanal/enerji non-stationary'dir. "
            "İnsan her 10 ms'de politika yazamaz. Varsayım: ölçüm kalitesi yüksek, geri alma tanımlı. "
            "Kara kutu düzenleyiciye açıklanamaz — bu bir ürün kısıtıdır, stil tercihi değil."
        ),
        "why_needed": (
            "Near-RT RIC (~10 ms, O-RAN tanımı) hüzme/handover; Non-RT rApp saniye+ enerji ve kestirim. "
            "Öğrenen döngü ölçüme bağlı uyarlama ihtiyacını karşılar. GPU/NPU kendi enerjisini yer; "
            "net kazanç ölçülmeden '%50–70' iddiası hedef/pazarlamadır. TR 38.843 + O-RAN WG2/10."
        ),
        "what": (
            "AI-native RAN iki kattır: (1) pratik giriş — xApp/rApp ile RRM politikası; "
            "(2) araştırma ucu — otokodlayıcı PHY, hava arayüzünün öğrenilmiş temsili. "
            "O-RAN arayüzdür; AI uygulama. Sohbet asistanı AI-RAN değildir."
        ),
        "mental_model": (
            "RL: durum s (SINR, PRB, yük), eylem a (RRM), ödül r (kapasite/enerji/kesinti). "
            "Q(s,a) ← Q + α[r + γ max Q' − Q]. Otokodlayıcı kaybı E[||s − f_D(f_E(s)+n)||²]. "
            "Yanlış ödül şebekeyi kilitler; rollback tasarımın parçasıdır. Denetim kalkmaz."
        ),
        "how_steps": [
            "Ölç: yük, SINR, PRB, enerji, arıza öncülü — model verinin kalitesini aşamaz.",
            "Near-RT xApp: onlarca ms hüzme/handover. Non-RT rApp: saniye+ uyku ve tahmin.",
            "Uygula: politika gNB'ye yazılır. Geri alma yolu yoksa canlı şebekeye otonom pilot denmez.",
            "Öğren: ödül kötüyse güncelle. Zero-touch (ZTN) araştırma ucudur, saha kanıtı yoktur (TRL 5).",
        ],
        "analogy": (
            "Klasik SON: kural tabanlı self-organizing. "
            "AI-RAN RRM: öğrenilmiş politika, aynı döngü, ölçüm şart. "
            "Nöral PHY: ayrı katman, Rel-18/TR 38.843 çalışma alanı, laboratuvar."
        ),
        "analogy_technical_map": (
            "Geçerlilik: i.i.d. olmayan trafik, dağılım kayması (drift) izlenmeli. "
            "Açıklanabilirlik (XAI) düzenleyici kısıt. O-RAN ≠ çok tedarikçili AI garantisi; arayüz standardıdır."
        ),
        "when_used": (
            "Değişken yük, enerji hedefi, kestirimci bakım, RIC denemesi. Ölçüm kalitesi ve rollback varsa."
        ),
        "when_not": (
            "Eğitilmemiş model, saha verisi yok, kara kutu kabul edilmiyor. "
            "'Sıfır insan' pazarlamadır. Bu platformda enerji faturası ölçülmedi."
        ),
        "not_to_confuse": (
            "Platform sohbet botu ≠ AI-RAN. O-RAN açık arayüz; AI onun üstünde xApp olabilir veya olmayabilir."
        ),
        "real_world": (
            "AI-RAN Alliance, O-RAN WG2/WG10, TR 38.843, NVIDIA Aerial test yatakları, operatör RIC PoC. "
            "Tam nöral hava arayüzü laboratuvar."
        ),
        "tt_impact": (
            "Maç çıkışı kaynak, gece uyku, arıza öncülü. TRL 5, RIC deneme sınıfı. İnsan denetimi kapanmaz."
        ),
    },
    "ntn": {
        "problem": (
            "Karasal kapsama kule+fiber geometrisidir. LEO ~500–1200 km, v ≈ 7,5 km/s → "
            "Doppler f_d = f_c (v/c) cosθ ve sık handover. GEO RTT ~250 ms sınıfı (literatür). "
            "FSPL ∝ (d f)². Varsayım: Rel-17+ NTN modem, feeder link, gateway."
        ),
        "why_needed": (
            "Kırsal CAPEX, deniz, havacılık, afet (site düşünce) karasal modeli kırar. "
            "Aynı 3GPP kimliği ile boşluğu kapatma ihtiyacıdır. Şehir kapasitesi ve URLLC için "
            "birincil yol değildir. TRL 6 — TR 38.811, kamuya açık direct-to-cell."
        ),
        "what": (
            "NTN: LEO/GEO/HAPS düğümünün Rel-17+ ile karasal çekirdeğe bağlanması. "
            "Direct-to-cell: standart UE'nin uydu hücresini görmesi; VSAT çanak değildir. "
            "HAPS stratosfer platformudur, uydu değildir. Tüketici LEO genişbantı (ör. Starlink) "
            "ile NTN hücresi aynı ürün olmak zorunda değildir."
        ),
        "mental_model": (
            "Karasal birincil; NTN kapsama deliği. Link bütçesi FSPL + atmosfer + anten kazancı. "
            "PHY Doppler ve gecikme ön düzeltmesi yoksa PRACH tutmaz. "
            "Regenerative payload uyduda gNB işler; transparent payload yere taşır — ikisi aynı gecikme değildir."
        ),
        "how_steps": [
            "Hücre seçimi: şehirde gNB; boşlukta NTN hücresi. Öncelik karasaldır.",
            "Feeder: uydu → gateway → 5GC/6GC. Yer kapısı operatör varlığıdır.",
            "Telafi: f_d ve timing advance; Rel-17 NTN şartnamesi (TR 38.811) çerçeve.",
            "Servis sınıfı: acil SMS/ses önce. Terabit şehir deneyimi bu denklemin çıktısı değildir.",
        ],
        "analogy": (
            "VSAT: çanak, ayrı sistem. Direct-to-cell: elset anteni, Rel-17+ modem. "
            "HAPS: 20 km sınıfı, uydu yörüngesi değil. ISAC 'gökyüzü radar' NTN değildir."
        ),
        "analogy_technical_map": (
            "Geçerlilik: görünür uydu, yeterli EIRP, düzenlenmiş spektrum. "
            "'%100 küresel sıfır boşluk' pazarlamadır. Bu platformda uydu gecikmesi saha ölçülmedi."
        ),
        "when_used": (
            "FSPL ve saha CAPEX karasal hopu geçersiz kıldığında: kırsal/dağ, deniz, havacılık, "
            "kule düşünce afet yedek. Feeder + gateway şarttır; regenerative vs transparent payload "
            "gecikme sınıfını belirler. Şehir makro kapasitesinin yerine geçmez."
        ),
        "when_not": (
            "Şehir içi kapasite, sub-ms URLLC birincil yol. Her eski cihaz Rel-17 NTN garantisi değildir."
        ),
        "not_to_confuse": (
            "Direct-to-cell ≠ VSAT. HAPS ≠ LEO. NTN tamamlayıcıdır, 6G makrosunun rakibi değil."
        ),
        "real_world": (
            "TR 38.811, Rel-17/18/19 NTN WI, kamuya açık direct-to-cell denemeleri (operatör-uydu ortaklıkları). "
            "Afet yedek hattı stratejidir, saha garantisi değil."
        ),
        "tt_impact": (
            "Afet, filo, kırsal. TRL 6 — yedi dilimin en olgunu. Tamamlayıcı; şehir kulesinin yerine geçmez."
        ),
    },
    "ambient_iot": {
        "problem": (
            "NB-IoT/RedCap hâlâ bir enerji kaynağı ister. Palet/sera ölçeğinde pil lojistiği CAPEX+OPEX'tir. "
            "Backscatter yansıyan gücü zayıftır; menzil Friis hasadı × η_rectenna ile sınırlıdır. "
            "Varsayım: ortamda yeterli RF, yakın okuyucu, dar bit."
        ),
        "why_needed": (
            "'Nerede / kaç derece' işi bakım ekibi olmadan. Amaç video değil, seyrek kimlik. "
            "'1 sent, trilyon nesne' hedef/pazarlamadır. TR 38.848 Rel-19 SI; ticari dağıtım aşamasında değildir."
        ),
        "what": (
            "Ambient IoT: pilsiz veya mikro-kapasitörlü etiket; rectenna RF→DC; iletişim çoğunlukla "
            "backscatter (anten empedansı ile gelen taşıyıcıyı modüle, PA yok). "
            "Okuyucu gNB veya yardımcı aydınlatıcı. ISAC non-cooperative eko ölçer; bu sınıf kasıtlı etikettir."
        ),
        "mental_model": (
            "P_rec = P_tx G_tx G_rx (λ/4πd)² η. y(t) = α x(t) b(t) + n(t). "
            "RF zayıf ceplede etiket susar — sıfır pil maliyeti enerji garantisi değildir. "
            "RFID atası; fark 3GPP hücresel okuyucu ve Rel-19 adresleme hedefi."
        ),
        "how_steps": [
            "Hasat: rectenna; verim η < 1, mesafe Friis ile düşer.",
            "Modülasyon: b(t) empedans anahtarı; kendi PA'sı yoktur, menzil kısa (literatür < 10–50 m sınıfı, geometriye bağlı).",
            "Okuma: yüksek hassasiyetli dizi zayıf eko+biti ayırır. Protokol dardır (kbps).",
            "Bulut: dar kimlik ('koli, °C'). Video/telemetri bu denklemden çıkmaz.",
        ],
        "analogy": (
            "Mağaza kapısı RFID: atası, hücresel çoklu okuyucu değil. "
            "Güneş+pilli hasatlı sensör: ayrı sınıf, Ambient IoT 'sıfır pil' iddiası değildir her zaman. "
            "ISAC: işbirlikçi olmayan yansıtıcı."
        ),
        "analogy_technical_map": (
            "Geçerlilik: aydınlatıcı mevcut, d kısa, bit seyrek. "
            "Sınırsız ömür ancak okunabilir bit hasada bağlıdır. TT sahası ölçülmedi (TRL 4)."
        ),
        "when_used": (
            "Palet, soğuk zincir, sera, sayaç, yapı sağlığı — kısa menzil, düşük bit, uzun ömür hedefi."
        ),
        "when_not": (
            "Ses/görüntü, kilometre, hareketli araç telemetrisi, RF'siz köşe. Telefonun yerini almaz."
        ),
        "not_to_confuse": (
            "Shop-floor RFID ≠ Rel-19 Ambient IoT. Energy-harvesting (güneş) sensor ≠ backscatter etiket."
        ),
        "real_world": (
            "TR 38.848, akademik backscatter, Wiliot/Qualcomm pilsiz etiket denemeleri. "
            "TT IoT platformuna akış senaryodur; her rafta değildir."
        ),
        "tt_impact": (
            "Depo paleti, sera, sayaç adayı. TRL 4, PoC. Pil lojistiğini silme vaadi saha ölçümü değildir."
        ),
    },
}
