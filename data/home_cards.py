"""Ana Sayfa kartları — Temel: herkesin anlayacağı dil; Uzman: tam cümleli teknik özet."""

HOME_CARDS_TR = {
    "isac": {
        "kicker": "Sorun: kule konuşur, çevreyi görmez",
        "blurb": (
            "Bugünkü baz istasyonu telefona veri gönderir; çevredeki aracı veya kişiyi ölçmez. "
            "Kamera sis ve karanlıkta yetersiz kalır. Ayrı bir radar kurmak ise ikinci bir sistem demektir. "
            "ISAC (Integrated Sensing and Communication — Entegre Algılama ve İletişim) "
            "aynı antenle hem konuşmayı hem de yansıyan sinyalden uzaklık ve hız bilgisini birlikte sağlar. "
            "Hazırlık seviyesi 4'tür: laboratuvarda doğrulanmıştır. Türk Telekom şebekesinde henüz yoktur."
        ),
        "blurb_expert": (
            "Baz istasyonu Shannon kanalında bit taşır; yansıyan enerjiden kinematik çıkarmaz. "
            "Ayrı radar ikinci spektrum lisansı ve ikinci RF zinciri ister. "
            "ISAC (Integrated Sensing and Communication — Entegre Algılama ve İletişim) "
            "aynı RF zincirinde hem iletişimi hem yankıyı işler: gecikme mesafeyi, Doppler hızı verir. "
            "Bugünkü olgunluk TRL 4’tür; 3GPP Rel-19 çalışma kalemi (TR 22.837) ve laboratuvar doğrulaması "
            "bu seviyeyi destekler. Türk Telekom şebekesinde henüz kullanılmamaktadır."
        ),
    },
    "ris": {
        "kicker": "Sorun: sinyal köşeyi dönemez",
        "blurb": (
            "Yüksek frekanslı sinyal düz gider; bina köşesinde zayıflar veya kesilir. "
            "Her boşluğa yeni kule kurmak pahalıdır ve kenti yorar. "
            "RIS (Reconfigurable Intelligent Surface — Yeniden Yapılandırılabilir Akıllı Yüzey) "
            "bina cephesine asılan ince bir paneldir. Panel, baz istasyonunun sinyalini "
            "telefonun bulunduğu yöne yansıtır; kendi başına güçlü bir verici değildir. "
            "Hazırlık seviyesi 5'tir: prototip aşamasındadır. Ticari şebeke dağıtımında değildir."
        ),
        "blurb_expert": (
            "Yüksek frekansta dalga köşeyi dönmez; her kör nokta için yeni gNB dikmek "
            "CAPEX (sermaye harcaması) ve kent yükünü artırır. "
            "RIS (Reconfigurable Intelligent Surface — Yeniden Yapılandırılabilir Akıllı Yüzey) "
            "cephedeki programlanabilir yansıtıcıdır: eleman fazı θ_n hüzmeyi kullanıcı ekipmanına (UE) çevirir. "
            "Olgunluk TRL 5’tir; ETSI RIS ISG ile 3GPP Rel-19/20 çalışma kalemleri bu aşamayı tanımlar. "
            "Türk Telekom şebekesinde henüz ölçülmemiştir."
        ),
    },
    "cell_free": {
        "kicker": "Sorun: hücre kenarında sinyal düşer",
        "blurb": (
            "Klasik şebekede her telefon bir kuleye bağlıdır. İki kule arasında sinyal zayıflar; "
            "geçiş sırasında bağlantı kopabilir. "
            "Hücresiz Massive MIMO (Multiple-Input Multiple-Output — çok antenli ortak yayın), "
            "sokak ve tavanlara yayılmış küçük antenlerin aynı anda size hizmet etmesidir. "
            "Kenar boşluğu böylece azalır. Bedeli, bu antenleri bağlayan hızlı fiber hattıdır. "
            "Hazırlık seviyesi 4'tür: araştırma prototipidir. Türk Telekom şebekesinde henüz yoktur."
        ),
        "blurb_expert": (
            "Hücre kenarında SINR (signal-to-interference-plus-noise ratio — sinyal–girişim–gürültü oranı) düşer; "
            "handover kopma riski taşır. Hücresiz Massive MIMO, yayılmış erişim noktalarının "
            "ortak ön kodlama ile aynı frekans–zamanda hizmet vermesidir. "
            "Olgunluk TRL 4’tür; 3GPP Rel-19/20 dağıtık MIMO çalışma kalemi bu sınıfı çerçeveler. "
            "Türk Telekom şebekesinde henüz kullanılmamaktadır."
        ),
    },
    "thz": {
        "kicker": "Sorun: veri yolu dar kalabilir",
        "blurb": (
            "Bazı bağlantılarda bugünkü frekanslar yeterli hız vermez. "
            "THz (terahertz), milimetre dalga ile kızılötesi ışık arasında kalan çok geniş bir frekans aralığıdır; "
            "daha fazla veri taşımaya adaydır. Buna karşılık sinyal kısa mesafede zayıflar. "
            "Hazırlık seviyesi 3'tür: laboratuvar kanıtı vardır. Saha şebekesinde kullanılmamaktadır. "
            "6G yalnızca THz demek değildir."
        ),
        "blurb_expert": (
            "Sub-6 GHz ve mmWave bantları bazı hop’larda Shannon kapasitesinin bant genişliği tavanını dar bırakır. "
            "THz spektrumu açar; kapasite önce bant genişliği B ile büyür, ancak serbest uzay kaybı (FSPL) "
            "ve moleküler emilim menzili kısaltır. Olgunluk TRL 3’tür (3GPP TR 38.807). "
            "6G yalnızca THz demek değildir."
        ),
    },
    "ai_ran": {
        "kicker": "Sorun: şebeke sabit kurala bağlıdır",
        "blurb": (
            "Şebeke bugün çoğu yerde önceden yazılmış kurallarla yönetilir. "
            "Dolu bir stadyum ile boş bir gece aynı kurala bağlanırsa kaynak israfı veya yetersizlik doğar. "
            "AI-RAN (Artificial Intelligence-Native RAN — yapay zekâ destekli radyo ağı) "
            "ölçüme bakarak kapasiteyi kısa sürede yeniden dağıtır. Bir sohbet uygulaması değildir. "
            "Hazırlık seviyesi 5'tir: deneme aşamasındadır. "
            "İnsansız işletim için saha doğrulaması henüz yoktur."
        ),
        "blurb_expert": (
            "Sabit RRM (radio resource management — radyo kaynak yönetimi) kuralı, "
            "dolu stadyum ile boş geceyi aynı tarifeyle yönetir. "
            "AI-RAN ölçüme göre milisaniye–saniye döngüsünde kaynak kaydırır. "
            "Olgunluk TRL 5’tir; 3GPP TR 38.843 ve O-RAN RIC deneme sınıfı bu aşamayı tanımlar. "
            "İnsansız işletim için saha doğrulaması yoktur."
        ),
    },
    "ntn": {
        "kicker": "Sorun: kule her yere yetişmez",
        "blurb": (
            "Şehirdeki kule yolları ve yerleşimi kapsar. Dağ, deniz ve afet bölgesinde kapsama boş kalabilir. "
            "NTN (Non-Terrestrial Network — Karasal Olmayan Ağ) uydu veya yüksek irtifadaki platformu "
            "kara şebekesine bağlar; telefon aynı abonelikle bu yoldan da hizmet alabilir. "
            "Gecikme karasal kuleye göre daha uzundur. "
            "Hazırlık seviyesi 6'dır: kamuya açık denemeler vardır. "
            "Şehir kulesinin yerine geçmez; onu tamamlar."
        ),
        "blurb_expert": (
            "Karasal gNB şehir ve yol ağını kapsar; dağ, deniz ve enkaz bölgesi boş kalabilir. "
            "NTN, LEO veya HAPS düğümlerini 3GPP Rel-17+ ile çekirdeğe bağlar; bedeli gecikme ve Doppler kaymasıdır. "
            "Olgunluk TRL 6’dır (TR 38.811); kamuya açık direct-to-cell denemeleri vardır. "
            "Karasal kuleye tamamlayıcıdır, onun yerine geçmez."
        ),
    },
    "ambient_iot": {
        "kicker": "Sorun: her nesneye pil değiştirilemez",
        "blurb": (
            "Koli, sera veya sayaç gibi çok sayıda nesnede pili tek tek değiştirmek maliyetlidir. "
            "Ambient IoT, ortamda zaten bulunan radyo dalgasından az enerji toplayan küçük bir etikettir. "
            "Kendi bataryası olmadan kısa bir kimlik sinyali verir; video veya ses taşımaz. "
            "Hazırlık seviyesi 4'tür: laboratuvarda doğrulanmıştır. Ticari şebeke dağıtımında değildir."
        ),
        "blurb_expert": (
            "Koli ve sera ölçeğinde pil değiştirmek ekonomik değildir. "
            "Ambient IoT ortam RF’sinden enerji toplayıp backscatter ile kısa kimlik bildirir; "
            "kendi güç yükselteci yoktur. Olgunluk TRL 4’tür (3GPP TR 38.848). "
            "Türk Telekom şebekesinde henüz ölçülmemiştir."
        ),
    },
}

HOME_CARDS_EN = {
    "isac": {
        "kicker": "Problem: the tower talks but does not see",
        "blurb": (
            "Today’s base station sends data to the phone; it does not measure a nearby vehicle or person. "
            "Cameras are weak in fog and darkness. A separate radar means a second system. "
            "ISAC (Integrated Sensing and Communication) uses the same antenna for communication "
            "and for range and speed from the reflected signal. "
            "Readiness level 4: validated in the laboratory. Not yet in the Türk Telekom network."
        ),
        "blurb_expert": (
            "A base station carries bits on a Shannon channel; it does not extract kinematics from reflected energy. "
            "A separate radar needs a second spectrum licence and a second RF chain. "
            "ISAC processes communication and echo on the same RF chain: delay gives range, Doppler gives speed. "
            "Maturity is TRL 4; 3GPP Rel-19 (TR 22.837) and laboratory validation support that level. "
            "Not yet used in the Türk Telekom network."
        ),
    },
    "ris": {
        "kicker": "Problem: the signal cannot turn the corner",
        "blurb": (
            "A high-frequency signal travels in a straight line; it weakens or stops at a building corner. "
            "A new tower for every gap is expensive and burdens the city. "
            "A RIS (Reconfigurable Intelligent Surface) is a thin panel on a façade. "
            "It reflects the base-station signal toward the phone; it is not a high-power transmitter itself. "
            "Readiness level 5: prototype stage. Not in commercial network deployment."
        ),
        "blurb_expert": (
            "At high frequency a wave does not turn the corner; a new gNB for every blind spot "
            "raises CAPEX and urban load. A RIS is a programmable façade reflector: "
            "element phase θ_n steers the beam toward the UE. Maturity is TRL 5 "
            "(ETSI RIS ISG and 3GPP Rel-19/20). Not yet measured on the Türk Telekom network."
        ),
    },
    "cell_free": {
        "kicker": "Problem: the signal drops at the cell edge",
        "blurb": (
            "In a classic network each phone attaches to one tower. Between towers the signal weakens "
            "and a handover may drop. Cell-free Massive MIMO lets many small antennas serve you together, "
            "so the edge gap shrinks. The cost is fast fibre between those antennas. "
            "Readiness level 4: research prototype. Not yet in the Türk Telekom network."
        ),
        "blurb_expert": (
            "SINR drops at the cell edge and handover can drop the link. "
            "Cell-free Massive MIMO is joint precoding across geographically distributed access points "
            "on the same time–frequency resources. Maturity is TRL 4 "
            "(3GPP Rel-19/20 distributed MIMO). Not yet used in the Türk Telekom network."
        ),
    },
    "thz": {
        "kicker": "Problem: the data path can stay narrow",
        "blurb": (
            "For some links today’s frequencies do not give enough speed. "
            "THz (terahertz) is a wide band between millimetre-wave and infrared and can carry more data. "
            "The signal also fades over short distance. "
            "Readiness level 3: laboratory evidence. Not used in a field network. "
            "6G does not mean THz alone."
        ),
        "blurb_expert": (
            "Sub-6 GHz and mmWave can leave Shannon bandwidth too narrow on some hops. "
            "THz opens spectrum; capacity grows first with bandwidth B, while FSPL and molecular "
            "absorption shorten range. Maturity is TRL 3 (3GPP TR 38.807). 6G is not THz alone."
        ),
    },
    "ai_ran": {
        "kicker": "Problem: the network follows a fixed rule",
        "blurb": (
            "Networks are often run with pre-written rules. "
            "A full stadium and an empty night under the same rule waste or starve capacity. "
            "AI-RAN (artificial-intelligence-native radio access network) redistributes capacity "
            "from measurement on a short timescale. It is not a chat app. "
            "Readiness level 5: trial stage. No field validation yet for unattended operation."
        ),
        "blurb_expert": (
            "A fixed RRM rule treats a full stadium and an empty night with the same tariff. "
            "AI-RAN shifts resources on a millisecond-to-second measurement loop. "
            "Maturity is TRL 5 (3GPP TR 38.843 and O-RAN RIC trial class). "
            "There is no field validation yet for unattended operation."
        ),
    },
    "ntn": {
        "kicker": "Problem: the tower does not reach everywhere",
        "blurb": (
            "A city tower covers roads and buildings. Mountain, sea, and disaster areas may stay empty. "
            "An NTN (non-terrestrial network) joins a satellite or high-altitude platform to the "
            "ground network so the same subscription can be served that way too. Delay is longer "
            "than on a terrestrial tower. "
            "Readiness level 6: public trials exist. It complements the city tower; it does not replace it."
        ),
        "blurb_expert": (
            "A terrestrial gNB covers the city and road network; mountain, sea, and debris zones may stay empty. "
            "NTN joins LEO or HAPS nodes to the core with 3GPP Rel-17+; the cost is delay and Doppler. "
            "Maturity is TRL 6 (TR 38.811), with public direct-to-cell trials. "
            "It complements the terrestrial site; it does not replace it."
        ),
    },
    "ambient_iot": {
        "kicker": "Problem: you cannot change every battery",
        "blurb": (
            "Changing batteries one by one on many parcels, greenhouse sensors, or meters is costly. "
            "Ambient IoT is a small tag that draws a little energy from radio waves already in the air. "
            "It sends a short identity without its own battery; it does not carry video or voice. "
            "Readiness level 4: laboratory-validated. Not in commercial network deployment."
        ),
        "blurb_expert": (
            "Battery swaps at parcel and greenhouse scale are uneconomic. "
            "Ambient IoT harvests ambient RF and reports a short identity by backscatter; "
            "it has no power amplifier of its own. Maturity is TRL 4 (3GPP TR 38.848). "
            "Not yet measured on the Türk Telekom network."
        ),
    },
}


def home_card(tech_id: str, *, beginner: bool = True) -> dict:
    from i18n.core import get_lang

    table = HOME_CARDS_EN if get_lang() == "en" else HOME_CARDS_TR
    row = table.get(tech_id) or HOME_CARDS_TR.get(tech_id) or {}
    if not row:
        return {}
    blurb = row.get("blurb") if beginner else (row.get("blurb_expert") or row.get("blurb"))
    return {
        "kicker": row.get("kicker") or "",
        "blurb": blurb or "",
    }
