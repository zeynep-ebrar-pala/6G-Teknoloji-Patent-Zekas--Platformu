"""
Uzman katmanı: formül kartları, karşılaştırmalar, kullanım alanı mekanizması.
technologies.py'deki HTML mimariye eklenir; uydurma sayı yok.
"""

from __future__ import annotations

EXPERT_DEPTH: dict[str, dict] = {
    "isac": {
        "formulas": [
            {
                "name": "Radar denkleminde SNR",
                "latex": r"\mathrm{SNR}_{radar}=\frac{P_t G_t G_r\lambda^2\sigma}{(4\pi)^3 R^4 k T_0 B L}",
                "symbols": [
                    {"symbol": r"P_t", "meaning": "Verici çıkış gücü", "unit": "W"},
                    {"symbol": r"G_t, G_r", "meaning": "Verici / alıcı anten kazancı (lineer)", "unit": "—"},
                    {"symbol": r"\lambda", "meaning": "Taşıyıcı dalga boyu", "unit": "m"},
                    {"symbol": r"\sigma", "meaning": "Hedefin radar kesiti (RCS)", "unit": "m²"},
                    {"symbol": r"R", "meaning": "Hedefe tek yön mesafe", "unit": "m"},
                    {"symbol": r"k T_0 B", "meaning": "Isıl gürültü gücü (Boltzmann × sıcaklık × bant)", "unit": "W"},
                    {"symbol": r"L", "meaning": "Sistem ve atmosfer kayıpları", "unit": "—"},
                ],
                "tells_us": (
                    "Yankının, alıcı gürültüsüne göre ne kadar 'görünür' olduğunu söyler. "
                    "Tespit olasılığı ve menzil çözünürlüğü bu oranın üzerine kurulur; bit hızı formülü değildir."
                ),
                "why_this_form": (
                    "Gidiş yolunda güç ~1/R² yayılır, dönüşte bir kez daha ~1/R²; çarpım R⁴ üretir. "
                    "λ² ve G, antenin etkin alanı ve yönlülüğünden gelir. σ hedefin 'ne kadar büyük bir ayna' "
                    "olduğudur. Paydadaki B: daha geniş bant daha çok gürültü (ve daha iyi menzil çözünürlüğü) demektir."
                ),
                "when_valid": (
                    "Nokta hedef, uzak alan (far-field), tek gidiş-dönüş, clutter yok sayılan monostatik radar. "
                    "Şehirde çoklu yansıma bu denklemi iyimser kılar."
                ),
                "if_variable_changes": (
                    "R iki katına çıkınca SNR ~16 kat düşer — bu yüzden baz istasyonu ISAC menzili "
                    "iletişim menzilinden kısa kalır. B artınca gürültü artar ama menzil çözünürlüğü ~c/(2B) incelir: "
                    "klasik iletişim-algılama ödünleşmesi. P_t artınca hem bit hem eko güçlenir; batarya ve EMC bedeli vardır."
                ),
                "assumptions": (
                    "Hedef RCS bilinir veya tahmin edilir; anten kazançları hüzme yönündedir; "
                    "alıcı gürültü ısıl kabul edilir. Santimetre hassasiyet bu denklemden otomatik çıkmaz; "
                    "B, SNR ve kestirim algoritması birlikte belirler. Bu platformda saha SNR ölçülmemiştir."
                ),
                "simple_example": (
                    "Aynı donanımda R'yi 2 katına çıkarmak, 12 dB daha fazla SNR kaybı demektir "
                    "(10 log10(16) ≈ 12). Bunu kapatmak için güç veya kazanç ~16 kat gerekir — "
                    "şehir içi EIRP tavanları bunu sınırlar."
                ),
            },
            {
                "name": "Cramér-Rao sınırı ve iletişim kapasitesi",
                "latex": r"\mathrm{CRB}(\theta)\ge\frac{1}{J(\theta)},\qquad C_{\mathrm{com}}=B\log_2\left(1+\frac{P_{\mathrm{com}}|h|^2}{\sigma_n^2}\right)",
                "symbols": [
                    {"symbol": r"\theta", "meaning": "Kestirilecek parametre (açı, gecikme, Doppler)", "unit": "rad, s veya Hz"},
                    {"symbol": r"J(\theta)", "meaning": "Fisher bilgisi — verinin θ hakkında ne kadar keskin olduğu", "unit": "1/birim²"},
                    {"symbol": r"C_{com}", "meaning": "Shannon kapasitesi (AWGN, bilinen kanal)", "unit": "bit/s"},
                    {"symbol": r"P_{com}", "meaning": "İletişime ayrılan güç", "unit": "W"},
                    {"symbol": r"h", "meaning": "Karmaşık kanal kazancı", "unit": "—"},
                    {"symbol": r"\sigma_n^2", "meaning": "Gürültü gücü", "unit": "W"},
                ],
                "tells_us": (
                    "Sol: yansız kestiricinin varyansı Fisher bilgisinin tersinden daha iyi olamaz. "
                    "Sağ: aynı bantta iletişime ayrılan gücün taşıyabileceği bit tavanı. "
                    "ISAC'de P ve B bu iki ifadeyi aynı anda besler."
                ),
                "why_this_form": (
                    "CRB istatistiksel kestirim teorisindendir; 'daha iyi radar' iddiasının teorik tabanıdır. "
                    "Shannon formülü AWGN ve sonsuz blok uzunluğu varsayar. Birlikte yazılmalarının nedeni "
                    "kaynak paylaşımıdır: P_com artınca C artar, algılamaya kalan enerji veya zaman azalır."
                ),
                "when_valid": (
                    "CRB: düzenli (regular) istatistiksel model, yüksek SNR'de yaklaşım iyi. "
                    "Shannon: Gaussian gürültü, kodlama gecikmesi yok sayılır. OTFS/OFDM pratikte buna yaklaşır, eşit değildir."
                ),
                "if_variable_changes": (
                    "Gözlem süresi veya SNR artınca J büyür, CRB küçülür (daha iyi açı/mesafe). "
                    "B artınca hem C hem (radar) menzil çözünürlüğü iyileşir ama gürültü ve işlem yükü artar."
                ),
                "assumptions": (
                    "Çoklu hedef ve clutter CRB'yi bozar. '1 cm' bu eşitsizlikten türetilmiş bir saha garantisi değildir."
                ),
            },
        ],
        "comparison": {
            "title": "ISAC neyle karıştırılmamalı?",
            "headers": ["Yaklaşım", "Temel amaç", "Nasıl çalışır?", "Avantaj", "Sınırlama", "Ne zaman tercih?"],
            "rows": [
                [
                    "Ayrı radar + ayrı şebeke",
                    "İki bağımsız görev",
                    "İki spektrum, iki anten, iki zamanlama",
                    "Olgun ürünler, zayıf ödünleşme",
                    "CAPEX, spektrum, EMI",
                    "Görev-kritik radar zaten varsa",
                ],
                [
                    "ISAC / DFRC / JCR",
                    "Tek kaynak, çift işlev",
                    "Ortak dalga şekli ve donanım",
                    "Spektrum ve anten tasarrufu adayı",
                    "Güç/zaman ödünleşmesi, clutter, gizlilik",
                    "Kule geometrisi zaten sahneyi görüyorsa",
                ],
                [
                    "Kamera / LiDAR",
                    "Görüntü veya nokta bulutu",
                    "Optik / lazer",
                    "Zengin sahne semantiği",
                    "Sis, gece, gizlilik, bakım",
                    "RF'nin yetmediği semantik işler",
                ],
            ],
        },
        "use_case_depth": [
            {
                "how": "Eko gecikmesi ve AoA ile kör noktadaki hedefin kinematiği çıkarılır; V2X mesajı ayrı bir kontrol kanalı olabilir.",
                "when_not": "Çoklu yansımalı kavşakta tek yol varsayımı kırılır; santimetre iddiası bu platformda ölçülmedi.",
            },
            {
                "how": "Alçak irtifa hedefin RCS'i küçük olabilir; çok statik (bistatik) geometri kesiti büyütür.",
                "when_not": "İşbirlikçi transponder yoksa kaçak dron ile kuş ayrımı analog radar kadar zordur.",
            },
            {
                "how": "Makro ölçekte yoğunluk haritası; birey kimliği yoktur, Doppler spektrumu yığın hareket verir.",
                "when_not": "Kişisel iz sürme düzenlemesi net değilse kamusal ürünleştirme durur.",
            },
            {
                "how": "İç mekânda çok yollu eko aslında harita zenginliği olabilir (ters problem).",
                "when_not": "LiDAR/görü füzyonu olmadan milimetre 'rota' abartıdır.",
            },
            {
                "how": "Göğüs duvarı mikro-Doppler solunum izi literatürde gösterildi; kamera yokluğu gizlilik avantajı değildir otomatik.",
                "when_not": "Tıbbi cihaz onayı ve rıza yoksa sağlık ürünü sayılmaz.",
            },
        ],
        "adv_why": [
            "Ayrı radar RF zinciri ve spektrum lisansı ödenmez; mevcut gNB geometrisi kullanılır.",
            "Menzil çözünürlüğü bant genişliğiyle ölçeklenir; açı çözünürlüğü dizi açıklığıyla — hedef literatürdür, saha garantisi değil.",
            "Optik sensörlerin kara-yağmur-sis zayıflığı RF'de daha hafiftir (frekansa bağlı).",
            "Aynı Hz hem bit hem eko taşır; spektral verimlilik artışı ödünleşme doğru yönetilirse.",
        ],
        "dis_why": [
            "Aynı P_t ve zaman hem C_com hem SNR_radar'ı besler; biri artınca diğeri fiziken sıkışır.",
            "Kentsel clutter Fisher bilgisini düşürür; CRB iyimser kalır.",
            "Yankıdan hareket çıkarmak kamerasız izlemedir; KVKK/ePrivacy tasarım sorusudur, yan etki değil.",
        ],
        "global_why": [
            "3GPP Rel-19 ISAC çalışma kalemi: özelliğin araştırma makalesinden şartname adayına geçiş kapısıdır.",
            "Hexa-X-II: Avrupa bayrak 6G mimarisinde algılama-iletişim birlikteliğinin yerini tarif eder.",
            "IEEE ComSoc girişimi: ortak terim ve ölçüt dili (DFRC, JCR) üretir.",
            "Satıcı test yatakları gösterimdir; 100 Gbps + 1 cm birlikte bu platformda doğrulanmış metrik değildir.",
        ],
        "tt_why": [
            "Boğaz: kıyı gNB geometrisi su yolunu keser; sis kamerayı körler, RF yankısı adaydır.",
            "Dron koridoru: alçak irtifa, karasal kule zaten yukarı bakar; ayrı UTM radarı pahalıdır.",
            "Enkaz: optik yok, duvar arkası RF literatürü var; arama-kurtarma ürün onayı ayrı iştir.",
        ],
    },
    "ris": {
        "formulas": [
            {
                "name": "RIS aracılı dar bant kanal",
                "latex": r"y=\big(\mathbf{h}_r^{H}\boldsymbol{\Phi}\mathbf{G}\big)x+n,\quad\boldsymbol{\Phi}=\mathrm{diag}(e^{j\theta_1},\ldots,e^{j\theta_N})",
                "symbols": [
                    {"symbol": r"x", "meaning": "Gönderilen karmaşık taban bant sembolü", "unit": "—"},
                    {"symbol": r"y", "meaning": "UE'de alınan sembol", "unit": "—"},
                    {"symbol": r"\mathbf{G}", "meaning": "Tx (gNB) → RIS elemanları MIMO kanalı", "unit": "—"},
                    {"symbol": r"\mathbf{h}_r", "meaning": "RIS → Rx (UE) kanal vektörü", "unit": "—"},
                    {"symbol": r"\theta_n", "meaning": "n. elemanın uyguladığı faz", "unit": "rad"},
                    {"symbol": r"n", "meaning": "Alıcı gürültüsü", "unit": "—"},
                ],
                "tells_us": (
                    "UE'nin gördüğü etkin kanal, RIS faz diyagonalinin iki hopu birleştirmesidir. "
                    "Φ'yi seçmek, 'ayna açısını' seçmektir. x'i üretmek hâlâ gNB'nin işidir."
                ),
                "why_this_form": (
                    "Dar bant, düz sönümlenme varsayımı: her eleman bir karmaşık çarpan. "
                    "Diyagonal: elemanlar birbirine bağlı yayınım yapmaz (ideal pasif model). "
                    "Hermit h_r^H sırayı Rx tarafında iç çarpım yapar."
                ),
                "when_valid": (
                    "Dar bant veya OFDM alt taşıyıcı başına; elemanlar karşılıklı kuplajsız; "
                    "kuantize faz (1–2 bit) bu sürekli θ modelini bozar."
                ),
                "if_variable_changes": (
                    "θ yanlışsa hüzme UE'den kaçar, |h_r^H Φ G| düşer. N artınca (aşağıdaki N²) "
                    "ideal hizalamada güç büyür; kestirim yükü de N ile büyür."
                ),
                "assumptions": (
                    "Kanalın Tx ve RIS tarafında bilindiği varsayılır. Pasif RIS ölçemez; "
                    "bu varsayım pratikte en büyük darboğazdır."
                ),
            },
            {
                "name": "N² güç ölçeği (ideal hizalama)",
                "latex": r"P_r \propto N^2\,|h_{\mathrm{Tx-RIS}}|^2\,|h_{\mathrm{RIS-Rx}}|^2",
                "symbols": [
                    {"symbol": r"N", "meaning": "RIS eleman sayısı", "unit": "—"},
                    {"symbol": r"h_{Tx-RIS}", "meaning": "Tek elemanlık Tx–RIS karmaşık kazanç (ölçek)", "unit": "—"},
                    {"symbol": r"h_{RIS-Rx}", "meaning": "Tek elemanlık RIS–Rx kazanç", "unit": "—"},
                    {"symbol": r"P_r", "meaning": "UE'de alınan güç", "unit": "W"},
                ],
                "tells_us": (
                    "İdeal faz hizalamasında N elemanın gerilim katkıları toplanır (~N), güç karesidir (~N²). "
                    "Aktif rölede güç genelde ~N (her eleman kendi PA'sı) ölçeklenir; bu yüzden RIS 'pasif dizi kazancı' vaadi taşır."
                ),
                "why_this_form": (
                    "Eş fazlı toplanan alan genliği N ile; detektördeki güç genliğin karesi. "
                    "İki hop çarpımı çift yol kaybını yazar: her hop FSPL taşır."
                ),
                "when_valid": (
                    "Mükemmel CSI, sürekli faz, uzak alan, elemanlar eş. "
                    "Yakın alan, kuantizasyon ve kestirim hatası üssü düşürür."
                ),
                "if_variable_changes": (
                    "N'yi 10'dan 100'e çıkarmak idealde ~20 dB güç; pratikte kanal kestirim payı yer. "
                    "Mesafe her hopta 2 katına çıkarsa o hop ~6 dB kaybeder; iki hopta daha ağır."
                ),
                "assumptions": (
                    "Çift yol kaybı, RIS'in 'kule yerine her yere yapıştır' çözümünü sınırlar. "
                    "%90 enerji tasarrufu aktif baz ile kaba karşılaştırmadır; bu platformda fatura yoktur."
                ),
            },
        ],
        "comparison": {
            "title": "RIS, röle ve küçük hücre",
            "headers": ["Yaklaşım", "Temel amaç", "Nasıl çalışır?", "Avantaj", "Sınırlama", "Ne zaman tercih?"],
            "rows": [
                [
                    "Yeni gNB / küçük hücre",
                    "Kapasite + kapsama",
                    "Kendi RF zinciri ve hücresi",
                    "Olgun, ölçülebilir SINR",
                    "CAPEX, site, geri bağlantı",
                    "Trafik gerçekten yeni sektör istiyorsa",
                ],
                [
                    "Aktif röle / tekrarlayıcı",
                    "Menzil uzatma",
                    "Alır, güçlendirir, basar",
                    "Tek hop kaybı daha az olabilir",
                    "Güç, gürültü yükseltme, girişim",
                    "Güç bütçesi ve site uygunsa",
                ],
                [
                    "Pasif/yarı-pasif RIS",
                    "Yolu şekillendirme",
                    "Faz diyagonali ile yansıtma",
                    "Düşük enerji, ince form",
                    "Çift yol kaybı, CSI, kontrol gecikmesi",
                    "N-LoS ve kule dikilemeyen cephe",
                ],
            ],
        },
        "use_case_depth": [
            {"how": "Φ, Tx–RIS–UE toplam fazını hizalar; doğrudan yol bina tarafından zaten ölüdür.", "when_not": "CSI yoksa rastgele faz, rastgele sönümleme üretir."},
            {"how": "Kıvrımda birden fazla panel çok sekmeli 'dalga kılavuzu' gibi dizilebilir.", "when_not": "Metal tünel çoklu yansıması modeli dar bant varsayımını zorlar."},
            {"how": "İç mekân mmWave/THz'de duvar yansıması zarar değil, kontrollü yol olur.", "when_not": "İnsan blockage hâlâ keser; RIS sihirli duvar değildir."},
            {"how": "Aktif PA sayısı azalır; enerji vaadi buradan gelir.", "when_not": "Kontrol işlemcisi ve kestirim pilotları enerjiyi geri yer. %90 ölçülmedi."},
            {"how": "Yansıma geometrisi AoA çeşitliliği ekler; ISAC ile füzyon araştırma konusudur.", "when_not": "RIS tek başına radar standardı değildir."},
        ],
        "adv_why": [
            "PA yokluğu mW mertebesi kontrol gücü demektir; aktif gNB ile kıyas hedefidir.",
            "Cephe/cam form faktörü site kirasını düşürür.",
            "Kendi başına EIRP basmaz; gelen dalgayı yönlendirir (EMC profili farklıdır).",
            "Eleman boyutu taşıyıcıya göre ölçeklenir; alt-6'dan THz'e tasarım ailesi vardır.",
        ],
        "dis_why": [
            "Pasif eleman alıcı değildir; pilot ve protokol olmadan Φ kördür.",
            "Tx→RIS ve RIS→Rx her ikisi FSPL taşır; N² bunu ancak hizalamayla telafi eder.",
            "Hareketli UE için Φ(t) güncellemesi işlem ve kontrol gecikmesi ister.",
        ],
        "global_why": [
            "ETSI ISG RIS: endüstri dilini ve kanal modellerini hizalar.",
            "IEEE görev gücü: akademik ölçüt (N², çift yol) ortaklaşır.",
            "Operatör PoC: cephe paneli gösterimi; emtia ürün rafı değil.",
            "RISE-6G: AB araştırma çerçevesi, standart değil.",
        ],
        "tt_why": [
            "Tarihi yarımada: yeni kule silüeti kısıtlı; cephe paneli arkeolojik ve imar olarak daha savunulabilir.",
            "Tünel: kıvrım N-LoS; pasif panel bakım ve güç açısından aktiften sade olabilir.",
            "Plaza camı: şeffaf RIS araştırması var; '10 Gbps+ her vagonda' bu platformda ölçülmedi.",
        ],
    },
    "cell_free": {
        "formulas": [
            {
                "name": "Kullanıcı k için SINR (ortak iletim)",
                "latex": r"\mathrm{SINR}_k=\frac{\left|\sum_{m=1}^{M}\mathbf{g}_{mk}^{H}\mathbf{w}_{mk}\right|^2}{\sum_{j\neq k}\left|\sum_{m=1}^{M}\mathbf{g}_{mk}^{H}\mathbf{w}_{mj}\right|^2+\sigma^2}",
                "symbols": [
                    {"symbol": r"M", "meaning": "Erişim noktası (AP) sayısı", "unit": "—"},
                    {"symbol": r"\mathbf{g}_{mk}", "meaning": "AP m ile kullanıcı k arasındaki kanal", "unit": "—"},
                    {"symbol": r"\mathbf{w}_{mk}", "meaning": "AP m'nin kullanıcı k için ön kodlama vektörü", "unit": "—"},
                    {"symbol": r"\sigma^2", "meaning": "Gürültü gücü", "unit": "W"},
                    {"symbol": r"j", "meaning": "Diğer kullanıcı indisi (parazit)", "unit": "—"},
                ],
                "tells_us": (
                    "Pay: tüm AP'lerin sizin sembolünüzde eş fazlı toplanması (faydalı güç). "
                    "Payda: aynı kanaldan sızan diğer kullanıcıların ön kodları + gürültü. "
                    "Hücre kenarı yok: 'komşu hücre' terimi yerine yalnızca kullanıcı paraziti vardır."
                ),
                "why_this_form": (
                    "Toplam m üzerinden: hizmet dağıtıktır. j≠k toplamı: spektrum paylaşılır. "
                    "Klasik hücrede payda ayrıca diğer kulelerin 'yabancı' gücünü içerir; burada o güç "
                    "koordine edilip w ile şekillendirilir."
                ),
                "when_valid": (
                    "Düz sönüm / tek taşıyıcı anlık; mükemmele yakın CSI; fronthaul gecikmesi yok. "
                    "Pilot kirliliği (pilot contamination) payı şişirir."
                ),
                "if_variable_changes": (
                    "M artınca çeşitlilik ve toplam açıklık artar, SINR adaleti iyileşir — fronthaul ve CPU lineer/üstel pahalılaşır. "
                    "w MMSE seçilirse parazit paydası küçülür; ZF daha agresif sıfırlar, gürültüyü yükseltebilir."
                ),
                "assumptions": (
                    "Senkron nanosaniye mertebesi. 5x–10x spektral kazanç seçilmiş senaryo literatürüdür, "
                    "şehir geneli garanti değil."
                ),
            },
        ],
        "comparison": {
            "title": "Hücresiz MIMO ve komşuları",
            "headers": ["Yaklaşım", "Temel amaç", "Nasıl çalışır?", "Avantaj", "Sınırlama", "Ne zaman tercih?"],
            "rows": [
                [
                    "Makro hücre",
                    "Geniş alan kapsama",
                    "Bir kule, sektör, handover",
                    "Olgun, düşük fronthaul",
                    "Kenar SINR, adaletsizlik",
                    "Seyrek trafik, kırsal",
                ],
                [
                    "Küçük hücre ormanı",
                    "Kapasite sıkıştırma",
                    "Hâlâ hücre + handover",
                    "Site yakınlığı",
                    "Kenar ve girişim durur",
                    "Sıcak nokta, geri bağlantı varsa",
                ],
                [
                    "Hücresiz Massive MIMO",
                    "Kenarsız adalet",
                    "Çok AP, ortak w, tek kullanıcı kümesi",
                    "Düzgün SINR, az kopma",
                    "Fronthaul, CPU, senkron",
                    "Stadyum, terminal, fabrika",
                ],
            ],
        },
        "use_case_depth": [
            {"how": "Tribün AP'leri aynı kullanıcı kümesine hizmet; kenar tribün 'komşu hücre' olmaz.", "when_not": "Fronthaul yoksa dağıtık MIMO değil, dağınık small cell olur."},
            {"how": "Yürüyen UE'nin serving kümesi kayar; sert handover yerine ağırlık değişir.", "when_not": "CPU gecikmesi faz kaydırır, hüzme bozulur."},
            {"how": "Düşük gecikme için AP-UE mesafesi kısa; kontrol döngüsü kenar bulutta.", "when_not": "Emniyet SIL gereksinimi hücresiz araştırma koduna emanet edilmez."},
            {"how": "Spektral verimlilik kullanıcı başına adil pay ile tanımlanır, tepe hız ile değil.", "when_not": "Seyrek cadde: fiber maliyeti kazancı yer."},
        ],
        "adv_why": [
            "Tasarımda cell-edge kullanıcısı yoktur; SINR dağılımının kuyruğu kısalır.",
            "İşbirlikçi w paraziti faydaya çevirir; spektral kazanç senaryoya bağlıdır.",
            "Makro kule silüeti azalır; estetik ve site kiralama.",
            "Handover başarısızlığı hedef olarak sıfıra yaklaşır (sert hücre sınırı yok).",
        ],
        "dis_why": [
            "Her AP I/Q veya sıkıştırılmış örnek merkeze; fiber ve eCPRI boyutu makro hücrenin katıdır.",
            "MMSE/ZF matris boyutu kullanıcı×anten ile büyür.",
            "Kazı ve kira, radyo donanımından pahalı olabilir.",
        ],
        "global_why": [
            "Dağıtık MIMO teorisinin akademik omurgası (Linköping ekolü ve türevi literatür).",
            "IEEE özel sayıları ölçüt ve fronthaul modellerini toplar.",
            "3GPP Rel-19/20 dağıtık MIMO: şartnameye giden yol.",
            "Ericsson/Nokia gösterimleri laboratuvar; stadyum ürün SKU'su değildir.",
        ],
        "tt_why": [
            "Stadyum: aynı anda yüksek yük + adalet; klasik makro tribün kenarını aç bırakır.",
            "İGA: yürüyüş handover kopması; serving kümesi kaydırması aday mekanizmadır.",
            "Sanayi: AGV hücre sınırında durmasın diye kısa hop + ortak taşıma.",
        ],
    },
    "thz": {
        "formulas": [
            {
                "name": "THz yol kaybı (FSPL × moleküler emilim)",
                "latex": r"L(f,d)=L_{\mathrm{fs}}(f,d)\,L_{\mathrm{abs}}(f,d)=\left(\frac{4\pi f d}{c}\right)^2 e^{K(f)d}",
                "symbols": [
                    {"symbol": r"f", "meaning": "Taşıyıcı frekans", "unit": "Hz"},
                    {"symbol": r"d", "meaning": "Link mesafesi", "unit": "m"},
                    {"symbol": r"c", "meaning": "Işık hızı", "unit": "m/s"},
                    {"symbol": r"K(f)", "meaning": "Frekansa bağlı emilim katsayısı (su buharı vb.)", "unit": "1/m"},
                    {"symbol": r"L", "meaning": "Toplam güç kaybı çarpanı (>1)", "unit": "—"},
                ],
                "tells_us": (
                    "İlk çarpan geometrik yayılma: f ve d büyüdükçe kayıp karesel artar. "
                    "İkinci çarpan spektral pencereler: bazı f'de K sıçrar, link 'kör frekans' olur."
                ),
                "why_this_form": (
                    "Friis / FSPL küresel dalga yüzeyinden. Emilim Beer–Lambert: yoğunluk e^{-K d} "
                    "(burada L_abs = e^{K d} kayıp çarpanı). THz'de K ihmal edilemez; mmWave'de çoğu zaman ikincildir."
                ),
                "when_valid": (
                    "Görüş hattı, homojen atmosfer, yağmur/sis ayrı model. Engelleme (el, gövde) bu formülde yoktur."
                ),
                "if_variable_changes": (
                    "f iki kat → yalnız FSPL +6 dB. d iki kat → FSPL +6 dB ve emilim e^{K d} daha da ağır. "
                    "K(f) çizgisinde birkaç GHz kaymak kaybı onlarca dB değiştirebilir — bu yüzden 'pencere' seçilir."
                ),
                "assumptions": (
                    "K(f) standart atmosfer modellerine bağlıdır (ITU-R). "
                    "<100–500 m menzil kuralı kaba; EIRP ve yağmura göre değişir."
                ),
            },
            {
                "name": "Shannon kapasitesi (AWGN)",
                "latex": r"C=B\log_2\left(1+\frac{P_t G_t G_r}{L(f,d)\,N_0 B}\right)",
                "symbols": [
                    {"symbol": r"C", "meaning": "Kanal kapasitesi tavanı", "unit": "bit/s"},
                    {"symbol": r"B", "meaning": "Bant genişliği", "unit": "Hz"},
                    {"symbol": r"N_0", "meaning": "Gürültü spektral yoğunluğu", "unit": "W/Hz"},
                    {"symbol": r"P_t G_t G_r / L", "meaning": "Alınan güç (Friis)", "unit": "W"},
                ],
                "tells_us": (
                    "C önce B ile (neredeyse lineer, yüksek SNR'de), SNR ile logaritmik büyür. "
                    "THz'in vaadi B ~ onlarca GHz açmaktır. L(f,d) SNR'yi yerse B tek başına Tbps üretmez."
                ),
                "why_this_form": (
                    "Shannon–Hartley. Paydadaki B: daha geniş bant daha çok gürültü (N_0 B). "
                    "Bu yüzden 'B'yi sonsuz aç' SNR'yi de düşürür; optimum bant vardır."
                ),
                "when_valid": (
                    "Gaussian gürültü, düz kanal veya OFDM alt taşıyıcı, sonsuz kod gecikmesi. "
                    "Gerçek ADC çözünürlüğü ve PA doğrusalsızlığı C'nin altındadır."
                ),
                "if_variable_changes": (
                    "B 10× → idealde C ~10× eğer SNR yüksek kalırsa. L 100× (20 dB) → SNR düşer, "
                    "log terimi çöker; hortum geniş ama basınç kaçmıştır."
                ),
                "assumptions": (
                    "B ≈ 50 GHz örnek mertebedir, tahsis edilmiş Türkiye spektrumu değildir. "
                    "1 Tbps hedef/literatür; bu uygulamada ölçülmedi."
                ),
            },
        ],
        "comparison": {
            "title": "THz komşu spektrumlar",
            "headers": ["Yaklaşım", "Temel amaç", "Nasıl çalışır?", "Avantaj", "Sınırlama", "Ne zaman tercih?"],
            "rows": [
                [
                    "Sub-6 GHz",
                    "Kapsama",
                    "İyi kırınım, orta B",
                    "Duvar, menzil",
                    "Spektrum sıkışık",
                    "Makro 5G/6G katmanı",
                ],
                [
                    "mmWave (ör. 28–60 GHz)",
                    "Kapasite + kısa hop",
                    "Dar hüzme, orta emilim",
                    "Olgun 5G ürün",
                    "Blockage, site",
                    "Şehir sıcak nokta",
                ],
                [
                    "Sub-THz / THz",
                    "Aşırı B, kablosuz fiber",
                    "Çok dar hüzme, yüksek K(f)",
                    "Tbps adayı, spektrum bol",
                    "Menzil, donanım, TRL 3",
                    "Raf, salon, kule köprüsü",
                ],
            ],
        },
        "use_case_depth": [
            {"how": "Raf arası d kısa, L yönetilebilir; kablo yığını azalır.", "when_not": "Toz, hizalama ve EMC raf standardı ayrı iştir. 1 Tbps ölçülmedi."},
            {"how": "Hologram/VR bit hızı Shannon'da B ister; gecikme hop sayısına bağlı.", "when_not": "Cep telefonu THz varsayılan bant değildir."},
            {"how": "Fiber kazılamayan kısa hopta FSPL + hüzme backhaul adayı.", "when_not": "Yağmur ve salınım (kule) linki düşürür; çeşitlilik gerekir."},
            {"how": "Kısa dalga boyu küçük anten; vücut içi araştırma ucu.", "when_not": "Tıbbi güvenlik ve soğurma; ticari 6G özelliği değil."},
            {"how": "THz spektroskopi malzeme çizgilerini görür; iletişimden ayrı mod.", "when_not": "Güvenlik tarayıcı iddiası standart şebeke KPI'sı değildir."},
        ],
        "adv_why": [
            "B onlarca GHz açılabilirse C Shannon'da sıçrar — hedef aralık 100 Gbps–1 Tbps literatürdür.",
            "Kısa sembol süresi düşük gecikme adayıdır; kuyruk hâlâ MAC'tedir.",
            "Çok dar hüzme dinlemeyi zorlaştırır; 'imkânsız hack' abartıdır, fiziksel yaklaşıklık yeter.",
            "THz tahsisi henüz kalabalık değildir (düzenleme evrilir).",
        ],
        "dis_why": [
            "L(f,d) menzili onlarca–yüzlerce metreye iter.",
            "Blockage: el ve gövde optiğe yakın keser.",
            "InP/GaN ve hızlı ADC maliyeti CMOS mmWave'den yüksek.",
        ],
        "global_why": [
            "IEEE 802.15.3d: kısa menzil THz PHY şartnamesi.",
            "ITU-R WRC: spektrumun yasal varlığı olmadan şebeke olmaz.",
            "Araştırma programları cihaz fiziği (kaynak, detektör).",
            "Satıcı 140 GHz gösterimi Sub-THz'dir; 10 THz ürün değildir.",
        ],
        "tt_why": [
            "Veri merkezi: d küçük, fiber yorgunluğu; yine de hizalama ve ısı var.",
            "Kule köprüsü: kazı yok; yağmur yedek hop ister.",
            "Holografik stüdyo: kontrollü iç mekân, abone sokağı değil.",
        ],
    },
    "ai_ran": {
        "formulas": [
            {
                "name": "Uçtan uca otokodlayıcı kaybı",
                "latex": r"\mathcal{L}(\theta,\phi)=\mathbb{E}_{s,n}\big[\|s-f_D(f_E(s;\theta)+n;\phi)\|^2\big]",
                "symbols": [
                    {"symbol": r"s", "meaning": "Gönderilmek istenen sembol / bit vektörü", "unit": "—"},
                    {"symbol": r"f_E(\cdot;\theta)", "meaning": "Öğrenilmiş verici (kodlayıcı) ağı", "unit": "—"},
                    {"symbol": r"f_D(\cdot;\phi)", "meaning": "Öğrenilmiş alıcı (kod çözücü) ağı", "unit": "—"},
                    {"symbol": r"n", "meaning": "Kanal gürültüsü / bozulma", "unit": "—"},
                    {"symbol": r"\theta,\phi", "meaning": "Ağ ağırlıkları", "unit": "—"},
                ],
                "tells_us": (
                    "Amaç, kanalın içinden geçtikten sonra s'yi geri getirme hatasını küçültmektir. "
                    "Klasik QAM+LDPC yerine 'nasıl dalga basılır' da öğrenilebilir. "
                    "Bu, RIC'te trafik ışığı ayarlamaktan farklı bir katmandır (PHY)."
                ),
                "why_this_form": (
                    "Otokodlayıcı: darboğaz (kanal) ile ayrılmış iki ağ. MSE, Gaussian gürültüde "
                    "maksimum olabilirlikle ilişkilidir; BER kaybı da kullanılabilir."
                ),
                "when_valid": (
                    "Eğitim dağılımı saha kanalına yakınsa. Dağılım kayarsa (sim→saha) L yalan söyler. "
                    "3GPP uyumluluk ve açıklanabilirlik çoğu operatörde hâlâ klasik PHY ister."
                ),
                "if_variable_changes": (
                    "SNR düşerse (n büyür) aynı mimaride L artar; ağ daha fazla artıklık öğrenmeye zorlanır. "
                    "θ,φ aşırı uyum (overfit) simülasyon kanalına kilitlenirse sahada BER patlar."
                ),
                "assumptions": (
                    "Diferansiyellenebilir kanal modeli veya vekil. Gerçek PA doğrusalsızlığı unutulursa laboratuvar yanılır."
                ),
            },
            {
                "name": "Q-öğrenme güncellemesi (RRM)",
                "latex": r"Q(s,a)\leftarrow Q(s,a)+\alpha\big[r+\gamma\max_{a'}Q(s',a')-Q(s,a)\big]",
                "symbols": [
                    {"symbol": r"s", "meaning": "Durum (yük, SINR, enerji…)", "unit": "—"},
                    {"symbol": r"a", "meaning": "Eylem (PRB, uyku, hüzme)", "unit": "—"},
                    {"symbol": r"r", "meaning": "Anlık ödül (kapasite, kesinti, watt)", "unit": "—"},
                    {"symbol": r"\alpha", "meaning": "Öğrenme adımı", "unit": "—"},
                    {"symbol": r"\gamma", "meaning": "İskonto (gelecek ödülün ağırlığı)", "unit": "—"},
                ],
                "tells_us": (
                    "Trafik polisi 'bu durumda şu eylemin uzun vadeli değeri Q' diye tablo veya ağ tutar. "
                    "Near-RT xApp bu döngünün hızlı sürümü, rApp yavaş sürümüdür."
                ),
                "why_this_form": (
                    "Bellman denkleminin örneklemeli hali. Parantez içi TD hatası: beklenen değer ile gerçekleşen dönüş farkı."
                ),
                "when_valid": (
                    "Markov varsayımı (gelecek, s ve a ile özetlenir). Ödül yanlış seçilirse 'kurnaz' politika "
                    "(ölçütü oyunlaştırma) doğar. Canlı şebekede keşif (exploration) tehlikelidir."
                ),
                "if_variable_changes": (
                    "α büyük → hızlı unutur, salınır. γ≈1 → uzun vadeli enerji; kısa kesintiyi görmezden gelebilir. "
                    "r yalnızca kapasite ise enerji faturası patlar."
                ),
                "assumptions": (
                    "Simülatör ≠ saha. %50–70 enerji tasarrufu seçilmiş uyku senaryosu literatür/hedeftir."
                ),
            },
        ],
        "comparison": {
            "title": "Kural tabanlı RAN, SON ve AI-RAN",
            "headers": ["Yaklaşım", "Temel amaç", "Nasıl çalışır?", "Avantaj", "Sınırlama", "Ne zaman tercih?"],
            "rows": [
                [
                    "Sabit tarife / eşik",
                    "Öngörülebilirlik",
                    "İnsan kuralı",
                    "Açıklanabilir, denetlenebilir",
                    "Geç kalır, yerel optimum",
                    "Sakin, iyi anlaşılmış hücre",
                ],
                [
                    "Klasik SON",
                    "Öz-yapılandırma",
                    "Sezgisel + istatistik",
                    "Olgun satıcı özellikleri",
                    "Sınırlı öğrenme",
                    "Bugünkü 4G/5G işletme",
                ],
                [
                    "AI-RAN / RIC xApp-rApp",
                    "Ölçüme dayalı uyarlama",
                    "ML politika + isteğe nöral PHY",
                    "Değişken yük ve enerji",
                    "Kara kutu, veri, GPU enerjisi",
                    "O-RAN denemesi, stadyum, yeşil hedef",
                ],
            ],
        },
        "use_case_depth": [
            {"how": "Durum s spektrum doluluğu; eylem a PRB paylaşımı; ödül girişim+kapasite.", "when_not": "Komşu operatör modeli yoksa 'akıllı' politika dışarıyı ezer."},
            {"how": "Öncül alarm: sıcaklık, VSWR, hata sayacı zaman serisi sınıflandırılır.", "when_not": "Eti ket yok pozitif yedeklemeyi yorar; insan onayı kalır."},
            {"how": "r enerji + SLA; a uyku derinliği. Deep sleep uyanma gecikmesi SLA'yı kırabilir.", "when_not": "Tasarruf GPU'nun kendisiyle netlenmeden iddia edilmez."},
            {"how": "Near-RT döngü hüzme indeksini günceller; keşif üretimde kısıtlıdır.", "when_not": "Handover yanlış öğrenmesi toplu koparma yapar."},
        ],
        "adv_why": [
            "Uyku ve yük kaydırma watt-saat keser — oran sahaya göre değişir, %50–70 hedef/seçilmiş senaryodur.",
            "Zero-touch hedefi işletme OPEX'ini düşürür; 'sıfır insan' iddiası TRL 5 ile çelişir.",
            "Kanal dağılımı kayınca klasik tablo kırılır; öğrenen PHY uyum vaadi taşır.",
            "O-RAN çok tedarikçi: politika yazılımı donanımdan ayrılır.",
        ],
        "dis_why": [
            "Kararın nedeni denetçiye anlatılamazsa kabul edilmez.",
            "NPU/GPU hem CAPEX hem watt; net yeşil hesap şart.",
            "Etiketli arıza ve kanal izi olmadan model uydurur.",
        ],
        "global_why": [
            "AI-RAN Alliance: satıcı-operatör dilini hizalar, 3GPP yerine geçmez.",
            "O-RAN WG2/10: xApp/rApp iş akışı.",
            "3GPP TR 38.843: hava arayüzünde AI/ML'nin şartnameye girip girmeyeceği.",
            "NVIDIA Aerial vb. SDK'dır; standart değildir.",
        ],
        "tt_why": [
            "Gece makro uyku: ölçüm varsa watt-saat; yoksa senaryo motoru kuralıdır.",
            "Maç günü: yük s, eylem komşu hücreden PRB; keşif kapalı tutulur.",
            "Kestirimci bakım: yanlış pozitif saha ekibini yakmamalı.",
        ],
    },
    "ntn": {
        "formulas": [
            {
                "name": "LEO Doppler kayması",
                "latex": r"f_d=f_c\cdot\frac{v_{\mathrm{sat}}}{c}\cos(\theta(t))",
                "symbols": [
                    {"symbol": r"f_d", "meaning": "Alınan frekansın taşıyıcıdan sapması", "unit": "Hz"},
                    {"symbol": r"f_c", "meaning": "Taşıyıcı frekans", "unit": "Hz"},
                    {"symbol": r"v_{sat}", "meaning": "Uydunun yere göre hız büyüklüğü", "unit": "m/s"},
                    {"symbol": r"c", "meaning": "Işık hızı", "unit": "m/s"},
                    {"symbol": r"\theta(t)", "meaning": "Hız vektörü ile görüş doğrultusu arası açı", "unit": "rad"},
                ],
                "tells_us": (
                    "LEO ufukta yaklaşırken f_d pozitif, tepeden geçerken ~0, uzaklaşırken negatif. "
                    "PHY bu kaymayı önceden kestirip düzeltmezse OFDM alt taşıyıcıları kayar, PRACH tutmaz."
                ),
                "why_this_form": (
                    "Klasik boylamsal Doppler: yalnızca görüş hattı hız bileşeni. "
                    "v_sat / c ~ 2,5×10⁻⁵ (≈7,5 km/s); f_c = 2 GHz iken f_d onlarca kHz mertebesine çıkar."
                ),
                "when_valid": (
                    "Özel görelilik ve gravitasyonel kayma ihmal; tek yol. "
                    "Gerçekte yörünge ephemeris ve UE hareketi eklenir."
                ),
                "if_variable_changes": (
                    "f_c 2× → f_d 2× (S-band vs Ka). v daha yüksek LEO (düşük irtifa) daha agresif Doppler. "
                    "θ=90° (tepe) anında kayma sıfır, eğim maksimumdur — handover tam o bölgede sıklaşır."
                ),
                "assumptions": (
                    "27 000 km/h mertebesi popüler yuvarlamadır (~7,5 km/s). "
                    "Direct-to-cell, bu düzeltmenin ucuz UE'de sığmasını varsayar."
                ),
            },
            {
                "name": "Serbest uzay yol kaybı",
                "latex": r"\mathrm{FSPL}=\left(\frac{4\pi d f}{c}\right)^2",
                "symbols": [
                    {"symbol": r"d", "meaning": "Eğik menzil (UE–uydu)", "unit": "m"},
                    {"symbol": r"f", "meaning": "Taşıyıcı", "unit": "Hz"},
                ],
                "tells_us": (
                    "600–1000 km d, karasal 1 km makrodan ~60 dB fazla geometrik kayıp demektir "
                    "(kaba: 20 log10(d2/d1)). Link bütçesi bu yüzden uydu EIRP'si ve UE gürültü rakamı ister."
                ),
                "why_this_form": (
                    "Friis. Engel yok; yağmur ve iyonosfer ayrı eklenir. GEO'da d ~36 000 km, FSPL daha ağır, "
                    "bu yüzden direct-to-cell önce LEO konuşulur."
                ),
                "when_valid": (
                    "Görüş hattı, uzak alan. İç mekân ve ağaç ek kayıp. HAPS'ta d ~20 km, FSPL LEO'dan hafif."
                ),
                "if_variable_changes": (
                    "d 2× → +6 dB. f 2× → +6 dB. Ka-band kapasite verir, yağmur ve FSPL cezası yer."
                ),
                "assumptions": (
                    "10–30 ms LEO gecikmesi yayılma + işlem kaba aralığıdır; bu uygulamada ping ölçülmedi. "
                    "GEO ~250 ms RTT mertebesi konuşmayı zorlar."
                ),
            },
        ],
        "comparison": {
            "title": "NTN katmanları",
            "headers": ["Yaklaşım", "Temel amaç", "Nasıl çalışır?", "Avantaj", "Sınırlama", "Ne zaman tercih?"],
            "rows": [
                [
                    "Karasal gNB",
                    "Kapasite ve düşük gecikme",
                    "Kısa d, handover yavaş",
                    "Olgun, ucuz hop",
                    "Kapsama deliği, afet kırılganlığı",
                    "Şehir, yol, bina",
                ],
                [
                    "LEO NTN",
                    "Küresel boşluk + düşük gecikme (GEO'ya göre)",
                    "Direct-to-cell veya gateway",
                    "TRL 6, afet yedek",
                    "Doppler, takım, CAPEX",
                    "Kırsal, deniz, acil",
                ],
                [
                    "GEO / HAPS",
                    "Sabit kapsama / bölgesel katman",
                    "Az uydu veya stratosfer",
                    "Az handover (GEO), daha düşük d (HAPS)",
                    "GEO gecikme; HAPS süreklilik",
                    "Yayın, IoT, bölgesel yama",
                ],
            ],
        },
        "use_case_depth": [
            {"how": "Eğik menzil açık denizde tek yol; FSPL + dalga sönümü. Servis sınıfı dar bant olabilir.", "when_not": "Gemide VSAT zaten varsa iş modeli çakışır."},
            {"how": "Uçak gövdesi + yüksek irtifa; kabin içi dağıtım ayrı.", "when_not": "Havayolu IFC sözleşmesi 3GPP NTN ile otomatik aynı değildir."},
            {"how": "Karasal çekirdek ayakta, RAN ölü; uydu hücre acil kayıt.", "when_not": "Yer kapısı da depremdeyse çoklu gateway coğrafyası şart."},
            {"how": "IoT seyrek, gecikme toleranslı; GEO de aday.", "when_not": "Gerçek zamanlı drone komuta LEO gecikmesiyle sınırlı."},
        ],
        "adv_why": [
            "Kule ekonomisi biten yerde kapsama. '%100 sıfır boşluk' düzenleme ve iç mekân ile sınırlıdır.",
            "Karasal RAN yıkılınca yedek yol — çekirdek ve gateway ayaktaysa.",
            "Kırsal fiber kazısını erteleyebilir; kapasite vaadi makro 6G değildir.",
            "Rel-17+ UE yolu özel çanak envanterini düşürür (cihaz sınıfına bağlı).",
        ],
        "dis_why": [
            "Yayılma gecikmesi d/c + işlem; URLLC birincil yol değil.",
            "LEO görünürlüğü dakikalar; sık hücre değişimi.",
            "Fırlatma ve takım yenileme CAPEX'i karasal siteden farklı risk taşır.",
        ],
        "global_why": [
            "3GPP Rel-17 NTN: ilk hücresel uydu şartname paketi.",
            "Direct-to-cell ticari denemeler (farklı takımlar, farklı iş modelleri).",
            "AST vb. büyük faz dizi yaklaşımı link bütçesini UE tarafında tutar.",
            "ESA 6G uzay bileşeni: Avrupa sistem çalışması.",
        ],
        "tt_why": [
            "Afet: karasal gNB ölür, kimlik aynı kalır — operatör stratejisi, saha garantisi değil.",
            "Filo: açık deniz FSPL + Direct-to-cell cihaz sınıfı.",
            "Dağ: site yok; kapasite değil, bağlantı.",
        ],
    },
    "ambient_iot": {
        "formulas": [
            {
                "name": "RF enerji hasadı (Friis × rectenna)",
                "latex": r"P_{\mathrm{rec}}=P_{tx}G_{tx}G_{rx}\left(\frac{\lambda}{4\pi d}\right)^2\eta_{\mathrm{rectenna}}",
                "symbols": [
                    {"symbol": r"P_{tx}", "meaning": "Aydınlatıcı / gNB çıkış gücü", "unit": "W"},
                    {"symbol": r"G_{tx}, G_{rx}", "meaning": "Aydınlatıcı ve etiket anten kazancı", "unit": "—"},
                    {"symbol": r"\lambda", "meaning": "Dalga boyu", "unit": "m"},
                    {"symbol": r"d", "meaning": "Aydınlatıcı–etiket mesafesi", "unit": "m"},
                    {"symbol": r"\eta_{rectenna}", "meaning": "RF→DC dönüşüm verimi (0–1)", "unit": "—"},
                ],
                "tells_us": (
                    "Etiketin yaşayacağı DC güç kırıntısı. d² (aslında Friis d² paydada) menzili sert keser. "
                    "η < 1 ve düşük P_tx (EMC/EIRP tavanı) yüzünden onlarca metreden öte 'sürekli yayın' zorlaşır."
                ),
                "why_this_form": (
                    "Friis alınan RF gücü; η diyot/doğrultucu gerçekliği. "
                    "Kapasitör bu gücü entegre eder; mesaj ancak eşik joule birikince çıkar."
                ),
                "when_valid": (
                    "Görüş hattı, tek aydınlatıcı, dar bant. Çok yollu iç mekân bazen yardımcı, bazen sönümler. "
                    "<10–50 m kaba pratik aralıktır, anten ve EIRP'ye bağlı."
                ),
                "if_variable_changes": (
                    "d 2× → P_rec 4× düşer. f yükselince λ küçülür, Friis cezası artar ama anten küçülür. "
                    "η 0,3→0,6 iki kat enerji; soğuk ve düşük güçte diyot η çöker."
                ),
                "assumptions": (
                    "EIRP yasal tavanı P_tx G_tx'i kilitler. 'Sınırsız ömür' elektronik yaşlanması ve "
                    "RF kıtlığını yok sayar."
                ),
            },
            {
                "name": "Geri saçılım (backscatter) gözlemi",
                "latex": r"y(t)=\alpha\, x(t)\, b(t)+n(t)",
                "symbols": [
                    {"symbol": r"x(t)", "meaning": "Okuyucunun gönderdiği taşıyıcı", "unit": "—"},
                    {"symbol": r"b(t)", "meaning": "Etiketin bilgi dizisi (genelde ±1 veya 0/1 empedans)", "unit": "—"},
                    {"symbol": r"\alpha", "meaning": "Yuvarlak yol zayıflaması ve saçılım katsayısı", "unit": "—"},
                    {"symbol": r"n(t)", "meaning": "Gürültü + öz-girişim", "unit": "—"},
                ],
                "tells_us": (
                    "Etiket PA açmaz; x'i b ile çarparak yansıtır. Okuyucu kendi x'ini bildiği için "
                    "(en azından kısmen) ayırır. |α| çok küçük olduğu için menzil ve bit hızı düşüktür."
                ),
                "why_this_form": (
                    "Çarpımsal kanal: enerji ve referans x'ten, bilgi b'den. "
                    "RFID'nin hücresel soyutlamasıdır."
                ),
                "when_valid": (
                    "Dar bant, yavaş b(t) (saat x'ten çok düşük). Okuyucu öz-girişim iptali iyi değilse "
                    "α x terimi alıcıyı doyurur."
                ),
                "if_variable_changes": (
                    "α d⁻⁴ benzeri (gidiş-dönüş) düşer — radar denklemiyle aynı geometri. "
                    "b hızlanırsa SNR/bit düşer; video imkânsıza yaklaşır."
                ),
                "assumptions": (
                    "Kbps sınıfı senör telemetrisi. Trilyon adres 3GPP çalışma hedefidir, saha envanteri değil."
                ),
            },
        ],
        "comparison": {
            "title": "Pilsiz etiket ve komşuları",
            "headers": ["Yaklaşım", "Temel amaç", "Nasıl çalışır?", "Avantaj", "Sınırlama", "Ne zaman tercih?"],
            "rows": [
                [
                    "NB-IoT / RedCap",
                    "Hücresel IoT",
                    "Pilli modem, kendi Tx",
                    "Menzil, standart şebeke",
                    "Pil lojistiği, maliyet",
                    "Sayaç, araç, km menzil",
                ],
                [
                    "Pasif RFID",
                    "Kapı/raf okuma",
                    "Backscatter, özel okuyucu",
                    "Olgun, ucuz",
                    "Hücresel kimlik yok, kısa menzil",
                    "Depo kapısı, perakende",
                ],
                [
                    "Ambient IoT (3GPP)",
                    "Hücresel pilsiz iz",
                    "Hasat + backscatter + gNB okuyucu",
                    "Pil yok, TT IoT'ye akış adayı",
                    "RF kıtlığı, kbps, TRL 4",
                    "Palet, sera, yapı içi kısa hop",
                ],
            ],
        },
        "use_case_depth": [
            {"how": "Palet d okuyucuya yakın; b(t) ID+sıcaklık. Yıllarca pil yok.", "when_not": "Açık tır dorsesi RF zayıfsa susar."},
            {"how": "Toprak nemi seyrek örnek; enerji birikimi dakikalar alabilir.", "when_not": "Derin gömü Friis'i öldürür."},
            {"how": "Eşik alarmı az bit; soğuk zincir ihlali zaman damgası.", "when_not": "Sürekli analog izleme enerji eşiğini aşar."},
            {"how": "Beton içi nem yavaş değişir; bakım kazısı olmasın diye pilsiz.", "when_not": "Kalın beton α'yı yok eder; okuyucu yerleşimi tasarım işidir."},
        ],
        "adv_why": [
            "Pil SKU ve saha işçiliği kalkar — 'sıfır maliyet' abartı, silikon hâlâ vardır.",
            "Kimyasal batarya atığı yok; elektronik e-atık kalır.",
            "Hedef BOM düşük; '1 sent' hacim ve yıl varsayar, bugünün raf fiyatı değildir.",
            "Ömür pil kimyasıyla sınırlı değil; RF ve lehim ömrüyle sınırlı.",
        ],
        "dis_why": [
            "Gidiş-dönüş zayıflama + η; onlarca metre kaba tavan.",
            "α küçük → kbps; ses/görüntü yok.",
            "Depo köşesi karanlık (RF) ise etiket ölüdür.",
        ],
        "global_why": [
            "3GPP TR 38.848: hücresel Ambient IoT çalışma kalemi.",
            "IEEE backscatter özel sayıları fizik ve MAC.",
            "AB sıfır-güç IoT çerçeveleri araştırma.",
            "Wiliot vb. ticari etiket: 3GPP ile özdeş ürün olmayabilir.",
        ],
        "tt_why": [
            "Depo: okuyucu gNB veya gate; 10 yıl bakım vaadi hedef, saha değil.",
            "Sera: nem seyrek; toprak Friis'i tasarım kısıtı.",
            "Sayaç: RF'si olan şaft/bina; metal dolap öldürür.",
        ],
    },
}
