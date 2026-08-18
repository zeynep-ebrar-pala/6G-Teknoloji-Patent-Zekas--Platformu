"""Ana Sayfa kartları — kicker + gövde. Çipler UI'da kullanılmaz."""

HOME_CARDS_TR = {
    "isac": {
        "kicker": "Sorun: kule konuşur, göremez",
        "chips": ["Yankıdan mesafe", "Doppler'den hız", "TRL 4, saha değil"],
        "blurb": (
            "Baz istasyonu veri taşır; çevreyi ölçmez. Kamera sis ve karanlıkta körleşir; "
            "ayrı radar ikinci spektrum ve ikinci anten ister. "
            "ISAC (Integrated Sensing and Communication — Entegre Algılama ve İletişim) "
            "aynı RF zincirinde hem bit hem yankı işler: gecikme mesafe, Doppler hız verir. "
            "TRL 4 — Rel-19 (TR 22.837); laboratuvar doğrulaması, TT sahası değil."
        ),
    },
    "ris": {
        "kicker": "Sorun: dalga köşeyi dönemez",
        "chips": ["Faz kaydıran yüzey", "Aktif verici yok", "TRL 5, ticari değil"],
        "blurb": (
            "Yüksek frekansta dalga köşeyi dönmez; her kör nokta için yeni gNB dikmek CAPEX ve kent yüküdür. "
            "RIS (Reconfigurable Intelligent Surface — Yeniden Yapılandırılabilir Akıllı Yüzey) "
            "cephedeki programlanabilir yansıtıcıdır: eleman fazı θ_n hüzmeyi UE'ye çevirir, "
            "kendi yüksek güçlü vericisi yoktur. TRL 5 — ETSI RIS ISG ve Rel-19/20; PoC sınıfı."
        ),
    },
    "cell_free": {
        "kicker": "Sorun: hücre sınırında zayıflar",
        "chips": ["Ortak ön kodlama", "Fronthaul bedeli", "TRL 4 stadyum adayı"],
        "blurb": (
            "Hücre kenarında SINR düşer; handover kopma riski taşır. "
            "Hücresiz Massive MIMO, yayılmış erişim noktalarının aynı anda ortak ön kodlama ile "
            "hizmet verdiği mimaridir: kenar tasarım hedefi olarak kalkar. Bedeli fronthaul fiberidir. "
            "TRL 4 — Rel-19/20 dağıtık MIMO; literatür prototip, TT sahası değil."
        ),
    },
    "thz": {
        "kicker": "Sorun: veri borusu hâlâ dar",
        "chips": ["Bant büyür", "FSPL + emilim", "TRL 3, sokak değil"],
        "blurb": (
            "Sub-6 GHz ve mmWave, veri merkezi içi mesh ve kule köprüsü için dar kalabilir. "
            "THz (terahertz) milimetre dalga ile kızılötesi arasındaki spektrumu açar; "
            "Shannon'da kapasite önce B ile büyür. Bedeli FSPL ve moleküler emilimdir: menzil kısalır. "
            "TRL 3 — TR 38.807; laboratuvar. 6G yalnızca THz değildir."
        ),
    },
    "ai_ran": {
        "kicker": "Sorun: şebeke sabit kural izler",
        "chips": ["Ölçümle kaynak", "Sohbet botu değil", "TRL 5, insansız değil"],
        "blurb": (
            "Sabit RRM kuralı dolu stadyum ile boş geceyi aynı tarifeyle yönetir. "
            "AI-RAN (Artificial Intelligence-Native RAN) ölçüme göre milisaniye–saniye döngüsünde "
            "kaynak kaydırır. Sohbet botu değildir. "
            "TRL 5 — TR 38.843 ve O-RAN RIC deneme sınıfı; insansız saha kanıtı yok."
        ),
    },
    "ntn": {
        "kicker": "Sorun: kule her yere ulaşmaz",
        "chips": ["Direct-to-cell", "Gecikme + Doppler", "TRL 6 tamamlayıcı"],
        "blurb": (
            "Karasal gNB şehir ve asfaltı kapsar; dağ, deniz ve enkaz boş kalır. "
            "NTN (Non-Terrestrial Network — Karasal Olmayan Ağ) LEO ve HAPS düğümlerini "
            "Rel-17+ prosedürüyle çekirdeğe bağlar. Bedeli gecikme ve Doppler'dir. "
            "TRL 6 — TR 38.811; kamuya açık direct-to-cell denemeleri. Rakip değil, tamamlayıcı."
        ),
    },
    "ambient_iot": {
        "kicker": "Sorun: her nesneye pil değiştirilemez",
        "chips": ["Backscatter kimlik", "Video taşımaz", "TRL 4, raf ürünü değil"],
        "blurb": (
            "Koli ve sera ölçeğinde pil değiştirmek ekonomik değildir. "
            "Ambient IoT ortam RF'sinden enerji toplayıp backscatter (geri saçılım) ile "
            "kısa kimlik bildirir; video taşımaz. "
            "TRL 4 — TR 38.848; PoC sınıfı, raf ürünü değil."
        ),
    },
}

HOME_CARDS_EN = {
    "isac": {
        "kicker": "Problem: the tower talks, it cannot see",
        "chips": ["Range from the echo", "Speed from Doppler", "TRL 4, not in the field"],
        "blurb": (
            "A base station carries data; it does not measure the scene. Cameras fail in fog "
            "and darkness; a separate radar wants a second spectrum and a second antenna. "
            "ISAC (Integrated Sensing and Communication) processes bits and echo on the same RF "
            "chain: delay is range, Doppler is speed. "
            "TRL 4 — Rel-19 work item (TR 22.837); laboratory validation, not a Türk Telekom field."
        ),
    },
    "ris": {
        "kicker": "Problem: the wave cannot turn the corner",
        "chips": ["Phase-shifting surface", "No high-power Tx", "TRL 5, not commercial"],
        "blurb": (
            "At high frequency a wave does not turn the corner; a new gNB for every blind spot is "
            "CAPEX and urban load. A RIS (Reconfigurable Intelligent Surface) is a programmable "
            "reflector on the façade: element phase θ_n steers the beam to the UE; it has no "
            "high-power transmitter of its own. TRL 5 — ETSI RIS ISG and Rel-19/20; operator-PoC class."
        ),
    },
    "cell_free": {
        "kicker": "Problem: it weakens at the cell boundary",
        "chips": ["Joint precoding", "Fronthaul is the bill", "TRL 4 stadium candidate"],
        "blurb": (
            "SINR drops at the cell edge; handover carries drop risk. Cell-free Massive MIMO "
            "is an architecture in which distributed access points serve jointly, on the same "
            "frequency, with shared precoding: the edge is removed as a design object. The bill "
            "is fronthaul fibre. TRL 4 — Rel-19/20 distributed MIMO; literature prototype, not a TT field."
        ),
    },
    "thz": {
        "kicker": "Problem: the data pipe is still narrow",
        "chips": ["Bandwidth grows first", "FSPL + absorption", "TRL 3, not on the street"],
        "blurb": (
            "Sub-6 GHz and mmWave can stay narrow for intra-DC mesh and tower bridges. "
            "THz (terahertz) opens the spectrum between millimetre-wave and infrared; in Shannon, "
            "capacity grows first with B. The bill is FSPL and molecular absorption: range shrinks. "
            "TRL 3 — TR 38.807; laboratory, not a street network. 6G is not THz alone."
        ),
    },
    "ai_ran": {
        "kicker": "Problem: the network follows a fixed rule",
        "chips": ["Resource from measurement", "Not a chatbot", "TRL 5, not unattended"],
        "blurb": (
            "A fixed RRM rule treats a packed stadium and an empty night with the same tariff. "
            "AI-RAN (artificial-intelligence-native radio access network) shifts resource on a "
            "millisecond-to-second loop from measurement. It is not a chatbot. "
            "TRL 5 — TR 38.843 and O-RAN RIC trial class; no unattended field proof."
        ),
    },
    "ntn": {
        "kicker": "Problem: the tower does not reach everywhere",
        "chips": ["Direct-to-cell", "Delay + Doppler", "TRL 6 complement"],
        "blurb": (
            "A terrestrial gNB covers the city and the asphalt; mountain, sea, and rubble stay empty. "
            "An NTN (non-terrestrial network) joins LEO and HAPS nodes to the core with Rel-17+ "
            "procedures. The bill is delay and Doppler. "
            "TRL 6 — TR 38.811; public Direct-to-Cell trials. Complements the urban site; does not rival it."
        ),
    },
    "ambient_iot": {
        "kicker": "Problem: you cannot replace the battery on every object",
        "chips": ["Backscatter identity", "Does not carry video", "TRL 4, not a shelf product"],
        "blurb": (
            "Replacing batteries at carton and greenhouse scale is uneconomic. Ambient IoT harvests "
            "ambient RF and reports a short identity by backscatter; it does not carry video. "
            "TRL 4 — TR 38.848; PoC class, not a shelf product."
        ),
    },
}


def home_card(tech_id: str) -> dict:
    from i18n.core import get_lang

    table = HOME_CARDS_EN if get_lang() == "en" else HOME_CARDS_TR
    return table.get(tech_id) or HOME_CARDS_TR.get(tech_id) or {}
