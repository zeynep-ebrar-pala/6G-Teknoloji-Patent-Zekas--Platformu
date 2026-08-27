"""Ana Sayfa kartları — Temel: resmi ve herkesin anlayacağı dil; Uzman: teknik kod."""

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
            "Baz istasyonu veri taşır; çevreyi ölçmez. Kamera sis ve karanlıkta körleşir; "
            "ayrı radar ikinci spektrum ve ikinci anten ister. "
            "ISAC (Integrated Sensing and Communication — Entegre Algılama ve İletişim) "
            "aynı RF zincirinde hem bit hem yankı işler: gecikme mesafe, Doppler hız verir. "
            "TRL 4 — 3GPP Rel-19 (TR 22.837); laboratuvar. Türk Telekom şebekesinde henüz kullanılmamaktadır."
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
            "Yüksek frekansta dalga köşeyi dönmez; her kör nokta için yeni gNB dikmek CAPEX ve kent yüküdür. "
            "RIS (Reconfigurable Intelligent Surface — Yeniden Yapılandırılabilir Akıllı Yüzey) "
            "cephedeki programlanabilir yansıtıcıdır: eleman fazı θ_n hüzmeyi UE'ye çevirir. "
            "TRL 5 — ETSI RIS ISG ve 3GPP Rel-19/20. Türk Telekom şebekesinde henüz ölçülmemiştir."
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
            "Hücre kenarında SINR düşer; handover kopma riski taşır. "
            "Hücresiz Massive MIMO, yayılmış erişim noktalarının ortak ön kodlama ile hizmetidir. "
            "TRL 4 — 3GPP Rel-19/20 dağıtık MIMO. Türk Telekom şebekesinde henüz kullanılmamaktadır."
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
            "Sub-6 GHz ve mmWave dar kalabilir. THz spektrumu açar; Shannon'da kapasite önce B ile büyür. "
            "Bedeli FSPL ve moleküler emilimdir. TRL 3 — 3GPP TR 38.807. 6G yalnızca THz değildir."
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
            "Sabit RRM kuralı dolu stadyum ile boş geceyi aynı tarifeyle yönetir. "
            "AI-RAN ölçüme göre milisaniye–saniye döngüsünde kaynak kaydırır. "
            "TRL 5 — 3GPP TR 38.843 ve O-RAN RIC. İnsansız işletim için saha doğrulaması yoktur."
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
            "Karasal gNB şehir ve asfaltı kapsar; dağ, deniz ve enkaz boş kalır. "
            "NTN LEO/HAPS düğümlerini 3GPP Rel-17+ ile çekirdeğe bağlar. Bedeli gecikme ve Doppler'dir. "
            "TRL 6 — TR 38.811; direct-to-cell denemeleri. Karasal kuleye tamamlayıcıdır."
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
            "Ambient IoT ortam RF'sinden enerji toplayıp backscatter ile kısa kimlik bildirir. "
            "TRL 4 — 3GPP TR 38.848. Türk Telekom şebekesinde henüz ölçülmemiştir."
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
            "A base station carries data; it does not measure the scene. "
            "ISAC processes bits and echo on the same RF chain. "
            "TRL 4 — 3GPP Rel-19 (TR 22.837). Not yet used in the Türk Telekom network."
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
            "At high frequency a wave does not turn the corner. "
            "RIS steers with element phase θ_n. TRL 5 — ETSI RIS ISG and 3GPP Rel-19/20."
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
            "SINR drops at the cell edge. Cell-free Massive MIMO uses joint precoding. "
            "TRL 4 — 3GPP Rel-19/20. Not yet used in the Türk Telekom network."
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
            "THz opens spectrum; FSPL and absorption shorten range. "
            "TRL 3 — 3GPP TR 38.807. 6G is not THz alone."
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
            "AI-RAN shifts resources on a millisecond-to-second loop. "
            "TRL 5 — 3GPP TR 38.843 and O-RAN RIC."
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
            "NTN joins LEO/HAPS with Rel-17+. TRL 6 — TR 38.811. Complements the terrestrial site."
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
            "Ambient IoT uses backscatter identity. TRL 4 — 3GPP TR 38.848. "
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
