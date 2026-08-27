"""Ana Sayfa kartları — Temel (sahne dili) + Uzman (TRL / 3GPP kodu)."""

HOME_CARDS_TR = {
    "isac": {
        "kicker": "Sorun: kule konuşur, göremez",
        "blurb": (
            "Baz istasyonu veri taşır ama çevreyi görmez. Kamera sis ve karanlıkta zayıflar; "
            "ayrı bir radar ise ikinci frekans ve ikinci anten ister. "
            "ISAC (Integrated Sensing and Communication — Entegre Algılama ve İletişim) "
            "aynı radyo zincirinde hem konuşur hem yankıdan mesafe ve hız okur. "
            "TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi) 4: laboratuvarda doğrulanmış; "
            "Türk Telekom abone sahasında yok."
        ),
        "blurb_expert": (
            "Baz istasyonu veri taşır; çevreyi ölçmez. Kamera sis ve karanlıkta körleşir; "
            "ayrı radar ikinci spektrum ve ikinci anten ister. "
            "ISAC (Integrated Sensing and Communication — Entegre Algılama ve İletişim) "
            "aynı RF zincirinde hem bit hem yankı işler: gecikme mesafe, Doppler hız verir. "
            "TRL 4 — 3GPP Rel-19 çalışma kalemi (TR 22.837); laboratuvar, TT sahası değil."
        ),
    },
    "ris": {
        "kicker": "Sorun: dalga köşeyi dönemez",
        "blurb": (
            "Yüksek frekansta radyo dalgası köşeyi kolay dönmez. Her kör noktaya yeni kule dikmek "
            "hem pahalıdır hem kenti yorar. "
            "RIS (Reconfigurable Intelligent Surface — Yeniden Yapılandırılabilir Akıllı Yüzey) "
            "cepheye asılan programlanabilir bir yansıtıcıdır: küçük elemanlar fazı kaydırır ve "
            "hüzmeyi telefona çevirir; kendi yüksek güçlü vericisi yoktur. "
            "TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi) 5: ilgili ortamda prototip; "
            "market rafında ürün değil."
        ),
        "blurb_expert": (
            "Yüksek frekansta dalga köşeyi dönmez; her kör nokta için yeni gNB dikmek CAPEX ve kent yüküdür. "
            "RIS (Reconfigurable Intelligent Surface — Yeniden Yapılandırılabilir Akıllı Yüzey) "
            "cephedeki programlanabilir yansıtıcıdır: eleman fazı θ_n hüzmeyi UE'ye çevirir, "
            "kendi yüksek güçlü vericisi yoktur. "
            "TRL 5 — ETSI RIS ISG ve 3GPP Rel-19/20; operatör PoC (Proof of Concept — kavram kanıtı) sınıfı."
        ),
    },
    "cell_free": {
        "kicker": "Sorun: hücre sınırında zayıflar",
        "blurb": (
            "Hücre kenarında sinyal zayıflar; bir kuleden diğerine geçişte kopma riski vardır. "
            "Hücresiz Massive MIMO (Multiple-Input Multiple-Output — Çok Girişli Çok Çıkışlı), "
            "sokak ve tavana yayılmış küçük erişim noktalarının aynı anda, birlikte hizmet verdiği "
            "mimaridir: kenar tasarım olarak kalkar. Bedeli, bunları bağlayan hızlı fiber hattıdır. "
            "TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi) 4: literatür prototipi; "
            "TT sahası değil."
        ),
        "blurb_expert": (
            "Hücre kenarında SINR düşer; handover kopma riski taşır. "
            "Hücresiz Massive MIMO, yayılmış erişim noktalarının aynı anda ortak ön kodlama ile "
            "hizmet verdiği mimaridir: kenar tasarım hedefi olarak kalkar. Bedeli fronthaul fiberidir. "
            "TRL 4 — 3GPP Rel-19/20 dağıtık MIMO; literatür prototip, TT sahası değil."
        ),
    },
    "thz": {
        "kicker": "Sorun: veri borusu hâlâ dar",
        "blurb": (
            "Bugünkü frekanslar bazı köprü ve veri merkezi bağlantıları için dar kalabilir. "
            "THz (terahertz) milimetre dalga ile kızılötesi arasındaki bandı açar; boru genişler. "
            "Ama serbest uzay kaybı ve moleküler emilim menzili kısaltır. "
            "TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi) 3: laboratuvar kanıtı; "
            "sokak şebekesi değil. 6G yalnızca THz demek değildir."
        ),
        "blurb_expert": (
            "Sub-6 GHz ve mmWave, veri merkezi içi mesh ve kule köprüsü için dar kalabilir. "
            "THz (terahertz) milimetre dalga ile kızılötesi arasındaki spektrumu açar; "
            "Shannon'da kapasite önce B ile büyür. Bedeli FSPL ve moleküler emilimdir: menzil kısalır. "
            "TRL 3 — 3GPP TR 38.807; laboratuvar. 6G yalnızca THz değildir."
        ),
    },
    "ai_ran": {
        "kicker": "Sorun: şebeke sabit kural izler",
        "blurb": (
            "Sabit şebeke kuralı dolu stadyum ile boş geceyi aynı tarifeyle yönetir. "
            "AI-RAN (Artificial Intelligence-Native RAN — yapay zekâ tabanlı radyo erişim ağı) "
            "ölçüme bakarak kaynakları saniyeler içinde kaydırır. Sohbet botu değildir. "
            "TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi) 5: deneme sınıfı; "
            "insansız saha kanıtı yok."
        ),
        "blurb_expert": (
            "Sabit RRM kuralı dolu stadyum ile boş geceyi aynı tarifeyle yönetir. "
            "AI-RAN (Artificial Intelligence-Native RAN) ölçüme göre milisaniye–saniye döngüsünde "
            "kaynak kaydırır. Sohbet botu değildir. "
            "TRL 5 — 3GPP TR 38.843 ve O-RAN RIC deneme sınıfı; insansız saha kanıtı yok."
        ),
    },
    "ntn": {
        "kicker": "Sorun: kule her yere ulaşmaz",
        "blurb": (
            "Şehir kulesi asfaltı kapsar; dağ, deniz ve enkaz boş kalır. "
            "NTN (Non-Terrestrial Network — Karasal Olmayan Ağ) uydu ve yüksek irtifa platformunu "
            "karasal çekirdeğe bağlar. Bedeli gecikme ve hız kaymasıdır. "
            "TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi) 6: kamuya açık "
            "telefona-doğrudan denemeler var. Şehir kulesinin rakibi değil, tamamlayıcısıdır."
        ),
        "blurb_expert": (
            "Karasal gNB şehir ve asfaltı kapsar; dağ, deniz ve enkaz boş kalır. "
            "NTN (Non-Terrestrial Network — Karasal Olmayan Ağ) LEO ve HAPS düğümlerini "
            "3GPP Rel-17+ prosedürüyle çekirdeğe bağlar. Bedeli gecikme ve Doppler'dir. "
            "TRL 6 — TR 38.811; kamuya açık direct-to-cell denemeleri. Rakip değil, tamamlayıcı."
        ),
    },
    "ambient_iot": {
        "kicker": "Sorun: her nesneye pil değiştirilemez",
        "blurb": (
            "Koli ve sera ölçeğinde her etikete pil değiştirmek ekonomik değildir. "
            "Ambient IoT ortam radyo dalgasından enerji toplayıp backscatter "
            "(geri saçılım — gelen dalgayı zayıfça geri yansıtarak) kısa kimlik bildirir; video taşımaz. "
            "TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi) 4: kavram kanıtı sınıfı; "
            "market rafında ürün değil."
        ),
        "blurb_expert": (
            "Koli ve sera ölçeğinde pil değiştirmek ekonomik değildir. "
            "Ambient IoT ortam RF'sinden enerji toplayıp backscatter (geri saçılım) ile "
            "kısa kimlik bildirir; video taşımaz. "
            "TRL 4 — 3GPP TR 38.848; PoC (Proof of Concept — kavram kanıtı) sınıfı, raf ürünü değil."
        ),
    },
}

HOME_CARDS_EN = {
    "isac": {
        "kicker": "Problem: the tower talks, it cannot see",
        "blurb": (
            "A base station carries data but does not see the scene. Cameras weaken in fog and darkness; "
            "a separate radar wants a second frequency and a second antenna. "
            "ISAC (Integrated Sensing and Communication) talks and reads range/speed from the echo "
            "on the same radio chain. "
            "TRL (Technology Readiness Level) 4: lab-validated; not on a Türk Telekom subscriber field."
        ),
        "blurb_expert": (
            "A base station carries data; it does not measure the scene. Cameras fail in fog "
            "and darkness; a separate radar wants a second spectrum and a second antenna. "
            "ISAC (Integrated Sensing and Communication) processes bits and echo on the same RF "
            "chain: delay is range, Doppler is speed. "
            "TRL 4 — 3GPP Rel-19 work item (TR 22.837); laboratory, not a TT field."
        ),
    },
    "ris": {
        "kicker": "Problem: the wave cannot turn the corner",
        "blurb": (
            "At high frequency a radio wave does not turn the corner easily. A new tower for every "
            "blind spot is costly and burdens the city. "
            "A RIS (Reconfigurable Intelligent Surface) is a programmable façade reflector: "
            "tiny elements shift phase and steer the beam to the phone; it has no high-power "
            "transmitter of its own. "
            "TRL (Technology Readiness Level) 5: prototype in a relevant setting; not a shelf product."
        ),
        "blurb_expert": (
            "At high frequency a wave does not turn the corner; a new gNB for every blind spot is "
            "CAPEX and urban load. A RIS (Reconfigurable Intelligent Surface) is a programmable "
            "reflector on the façade: element phase θ_n steers the beam to the UE; it has no "
            "high-power transmitter of its own. "
            "TRL 5 — ETSI RIS ISG and 3GPP Rel-19/20; operator PoC (proof of concept) class."
        ),
    },
    "cell_free": {
        "kicker": "Problem: it weakens at the cell boundary",
        "blurb": (
            "At the cell edge the signal weakens; handovers risk drops. "
            "Cell-free Massive MIMO (multiple-input multiple-output) lets many small access points "
            "serve together so the edge is no longer the design object. The bill is fast fibre between them. "
            "TRL (Technology Readiness Level) 4: literature prototype; not a TT field."
        ),
        "blurb_expert": (
            "SINR drops at the cell edge; handover carries drop risk. Cell-free Massive MIMO "
            "is an architecture in which distributed access points serve jointly with shared "
            "precoding: the edge is removed as a design object. The bill is fronthaul fibre. "
            "TRL 4 — 3GPP Rel-19/20 distributed MIMO; literature prototype, not a TT field."
        ),
    },
    "thz": {
        "kicker": "Problem: the data pipe is still narrow",
        "blurb": (
            "Today's bands can stay narrow for some bridge and data-centre links. "
            "THz (terahertz) opens the band between millimetre-wave and infrared; the pipe widens. "
            "Free-space loss and molecular absorption then shorten range. "
            "TRL (Technology Readiness Level) 3: lab evidence; not a street network. "
            "6G is not THz alone."
        ),
        "blurb_expert": (
            "Sub-6 GHz and mmWave can stay narrow for intra-DC mesh and tower bridges. "
            "THz (terahertz) opens the spectrum between millimetre-wave and infrared; in Shannon, "
            "capacity grows first with B. The bill is FSPL and molecular absorption: range shrinks. "
            "TRL 3 — 3GPP TR 38.807; laboratory. 6G is not THz alone."
        ),
    },
    "ai_ran": {
        "kicker": "Problem: the network follows a fixed rule",
        "blurb": (
            "A fixed network rule treats a packed stadium and an empty night the same way. "
            "AI-RAN (artificial-intelligence-native radio access network) shifts resources from "
            "measurement on a seconds-scale loop. It is not a chatbot. "
            "TRL (Technology Readiness Level) 5: trial class; no unattended field proof."
        ),
        "blurb_expert": (
            "A fixed RRM rule treats a packed stadium and an empty night with the same tariff. "
            "AI-RAN (artificial-intelligence-native radio access network) shifts resource on a "
            "millisecond-to-second loop from measurement. It is not a chatbot. "
            "TRL 5 — 3GPP TR 38.843 and O-RAN RIC trial class; no unattended field proof."
        ),
    },
    "ntn": {
        "kicker": "Problem: the tower does not reach everywhere",
        "blurb": (
            "A city tower covers asphalt; mountain, sea, and rubble stay empty. "
            "An NTN (non-terrestrial network) joins satellites and high-altitude platforms to the "
            "terrestrial core. The bill is delay and Doppler. "
            "TRL (Technology Readiness Level) 6: public direct-to-phone trials exist. "
            "It complements the urban site; it does not replace it."
        ),
        "blurb_expert": (
            "A terrestrial gNB covers the city and the asphalt; mountain, sea, and rubble stay empty. "
            "An NTN (non-terrestrial network) joins LEO and HAPS nodes to the core with Rel-17+ "
            "procedures. The bill is delay and Doppler. "
            "TRL 6 — TR 38.811; public Direct-to-Cell trials. Complements the urban site; does not rival it."
        ),
    },
    "ambient_iot": {
        "kicker": "Problem: you cannot replace the battery on every object",
        "blurb": (
            "Replacing batteries at carton and greenhouse scale is uneconomic. "
            "Ambient IoT harvests ambient radio energy and reports a short identity by backscatter "
            "(weakly reflecting the incoming wave); it does not carry video. "
            "TRL (Technology Readiness Level) 4: proof-of-concept class; not a shelf product."
        ),
        "blurb_expert": (
            "Replacing batteries at carton and greenhouse scale is uneconomic. Ambient IoT harvests "
            "ambient RF and reports a short identity by backscatter; it does not carry video. "
            "TRL 4 — 3GPP TR 38.848; PoC (proof of concept) class, not a shelf product."
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
