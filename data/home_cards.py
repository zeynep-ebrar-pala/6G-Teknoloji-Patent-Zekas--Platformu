"""Ana Sayfa kartları — Temel (resmi, anlaşılır) + Uzman (TRL / 3GPP kodu)."""

HOME_CARDS_TR = {
    "isac": {
        "kicker": "Sorun: kule konuşur, göremez",
        "blurb": (
            "Baz istasyonu veri taşır ancak çevreyi algılamaz. Kamera sis ve karanlıkta yetersiz kalır; "
            "ayrı bir radar ise ikinci frekans bandı ve ikinci anten gerektirir. "
            "ISAC (Integrated Sensing and Communication — Entegre Algılama ve İletişim) "
            "aynı radyo zincirinde hem veri iletir hem yankıdan mesafe ve hız çıkarır. "
            "TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi) 4: "
            "laboratuvar ortamında doğrulanmıştır; Türk Telekom şebekesinde henüz kullanılmamaktadır."
        ),
        "blurb_expert": (
            "Baz istasyonu veri taşır; çevreyi ölçmez. Kamera sis ve karanlıkta körleşir; "
            "ayrı radar ikinci spektrum ve ikinci anten ister. "
            "ISAC (Integrated Sensing and Communication — Entegre Algılama ve İletişim) "
            "aynı RF zincirinde hem bit hem yankı işler: gecikme mesafe, Doppler hız verir. "
            "TRL 4 — 3GPP Rel-19 çalışma kalemi (TR 22.837); laboratuvar doğrulaması. "
            "Türk Telekom şebekesinde henüz kullanılmamaktadır."
        ),
    },
    "ris": {
        "kicker": "Sorun: dalga köşeyi dönemez",
        "blurb": (
            "Yüksek frekansta radyo dalgası köşeyi kolay dönmez. Her kör noktaya yeni kule kurmak "
            "yüksek yatırım ve kentsel yük getirir. "
            "RIS (Reconfigurable Intelligent Surface — Yeniden Yapılandırılabilir Akıllı Yüzey) "
            "cepheye monte edilen programlanabilir bir yansıtıcıdır: küçük elemanlar fazı kaydırarak "
            "hüzmeyi kullanıcı cihazına yönlendirir; kendi yüksek güçlü vericisi yoktur. "
            "TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi) 5: "
            "ilgili ortamda prototip düzeyindedir; ticari dağıtım aşamasında değildir."
        ),
        "blurb_expert": (
            "Yüksek frekansta dalga köşeyi dönmez; her kör nokta için yeni gNB dikmek CAPEX ve kent yüküdür. "
            "RIS (Reconfigurable Intelligent Surface — Yeniden Yapılandırılabilir Akıllı Yüzey) "
            "cephedeki programlanabilir yansıtıcıdır: eleman fazı θ_n hüzmeyi UE'ye çevirir, "
            "kendi yüksek güçlü vericisi yoktur. "
            "TRL 5 — ETSI RIS ISG ve 3GPP Rel-19/20; operatör deneme (PoC) sınıfı. "
            "Türk Telekom şebekesinde henüz ölçülmemiştir."
        ),
    },
    "cell_free": {
        "kicker": "Sorun: hücre sınırında zayıflar",
        "blurb": (
            "Hücre kenarında sinyal zayıflar; bir kuleden diğerine geçişte bağlantı kopması riski vardır. "
            "Hücresiz Massive MIMO (Multiple-Input Multiple-Output — Çok Girişli Çok Çıkışlı), "
            "alana yayılmış erişim noktalarının aynı anda birlikte hizmet verdiği mimaridir; "
            "kenar, tasarım sorunu olmaktan çıkar. Bedeli, noktaları bağlayan yüksek hızlı fiber hattıdır. "
            "TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi) 4: "
            "literatür prototipi düzeyindedir; Türk Telekom şebekesinde henüz kullanılmamaktadır."
        ),
        "blurb_expert": (
            "Hücre kenarında SINR düşer; handover kopma riski taşır. "
            "Hücresiz Massive MIMO, yayılmış erişim noktalarının aynı anda ortak ön kodlama ile "
            "hizmet verdiği mimaridir: kenar tasarım hedefi olarak kalkar. Bedeli fronthaul fiberidir. "
            "TRL 4 — 3GPP Rel-19/20 dağıtık MIMO; literatür prototipi. "
            "Türk Telekom şebekesinde henüz kullanılmamaktadır."
        ),
    },
    "thz": {
        "kicker": "Sorun: veri borusu hâlâ dar",
        "blurb": (
            "Mevcut frekans bantları bazı köprü ve veri merkezi bağlantıları için yetersiz kalabilir. "
            "THz (terahertz) milimetre dalga ile kızılötesi arasındaki bandı açar; kapasite artar. "
            "Buna karşılık serbest uzay kaybı ve moleküler emilim menzili kısaltır. "
            "TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi) 3: "
            "laboratuvar kanıtı düzeyindedir; saha şebekesinde kullanılmamaktadır. "
            "6G yalnızca THz anlamına gelmez."
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
            "Sabit şebeke kuralları dolu stadyum ile boş geceyi aynı biçimde yönetir. "
            "AI-RAN (Artificial Intelligence-Native RAN — yapay zekâ tabanlı radyo erişim ağı) "
            "ölçüme göre kaynakları kısa süre içinde yeniden dağıtır. Bir sohbet uygulaması değildir. "
            "TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi) 5: "
            "deneme aşamasındadır; insansız işletim için saha doğrulaması bulunmamaktadır."
        ),
        "blurb_expert": (
            "Sabit RRM kuralı dolu stadyum ile boş geceyi aynı tarifeyle yönetir. "
            "AI-RAN (Artificial Intelligence-Native RAN) ölçüme göre milisaniye–saniye döngüsünde "
            "kaynak kaydırır. Sohbet botu değildir. "
            "TRL 5 — 3GPP TR 38.843 ve O-RAN RIC deneme sınıfı; "
            "insansız işletim için saha doğrulaması yoktur."
        ),
    },
    "ntn": {
        "kicker": "Sorun: kule her yere ulaşmaz",
        "blurb": (
            "Şehir kulesi yerleşim ve yolları kapsar; dağ, deniz ve afet bölgesi boş kalabilir. "
            "NTN (Non-Terrestrial Network — Karasal Olmayan Ağ) uydu ve yüksek irtifa platformunu "
            "karasal çekirdeğe bağlar. Bedeli gecikme ve hız kaymasıdır. "
            "TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi) 6: "
            "kamuya açık doğrudan-telefona denemeler vardır. "
            "Şehir kulesinin yerine geçmez; onu tamamlar."
        ),
        "blurb_expert": (
            "Karasal gNB şehir ve asfaltı kapsar; dağ, deniz ve enkaz boş kalır. "
            "NTN (Non-Terrestrial Network — Karasal Olmayan Ağ) LEO ve HAPS düğümlerini "
            "3GPP Rel-17+ prosedürüyle çekirdeğe bağlar. Bedeli gecikme ve Doppler'dir. "
            "TRL 6 — TR 38.811; kamuya açık direct-to-cell denemeleri. "
            "Karasal kuleye rakip değil, tamamlayıcıdır."
        ),
    },
    "ambient_iot": {
        "kicker": "Sorun: her nesneye pil değiştirilemez",
        "blurb": (
            "Koli ve sera ölçeğinde her etiketin pilini değiştirmek ekonomik değildir. "
            "Ambient IoT ortam radyo dalgasından enerji toplayarak backscatter "
            "(geri saçılım: gelen dalgayı zayıfça yansıtma) ile kısa kimlik bildirir; video iletmez. "
            "TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi) 4: "
            "laboratuvar doğrulaması düzeyindedir; ticari dağıtım aşamasında değildir."
        ),
        "blurb_expert": (
            "Koli ve sera ölçeğinde pil değiştirmek ekonomik değildir. "
            "Ambient IoT ortam RF'sinden enerji toplayıp backscatter (geri saçılım) ile "
            "kısa kimlik bildirir; video taşımaz. "
            "TRL 4 — 3GPP TR 38.848; erken deneme (PoC) sınıfı. "
            "Türk Telekom şebekesinde henüz ölçülmemiştir."
        ),
    },
}

HOME_CARDS_EN = {
    "isac": {
        "kicker": "Problem: the tower talks, it cannot see",
        "blurb": (
            "A base station carries data but does not sense the surroundings. Cameras are weak in fog "
            "and darkness; a separate radar requires a second frequency band and a second antenna. "
            "ISAC (Integrated Sensing and Communication) transmits data and extracts range and speed "
            "from the echo on the same radio chain. "
            "TRL (Technology Readiness Level) 4: validated in the laboratory; "
            "not yet used in the Türk Telekom network."
        ),
        "blurb_expert": (
            "A base station carries data; it does not measure the scene. Cameras fail in fog "
            "and darkness; a separate radar wants a second spectrum and a second antenna. "
            "ISAC (Integrated Sensing and Communication) processes bits and echo on the same RF "
            "chain: delay is range, Doppler is speed. "
            "TRL 4 — 3GPP Rel-19 work item (TR 22.837); laboratory validation. "
            "Not yet used in the Türk Telekom network."
        ),
    },
    "ris": {
        "kicker": "Problem: the wave cannot turn the corner",
        "blurb": (
            "At high frequency a radio wave does not turn the corner easily. Building a new tower "
            "for every blind spot brings high investment and urban load. "
            "A RIS (Reconfigurable Intelligent Surface) is a programmable reflector mounted on a "
            "façade: small elements shift phase and steer the beam to the user device; it has no "
            "high-power transmitter of its own. "
            "TRL (Technology Readiness Level) 5: prototype in a relevant environment; "
            "not at commercial deployment."
        ),
        "blurb_expert": (
            "At high frequency a wave does not turn the corner; a new gNB for every blind spot is "
            "CAPEX and urban load. A RIS (Reconfigurable Intelligent Surface) is a programmable "
            "reflector on the façade: element phase θ_n steers the beam to the UE; it has no "
            "high-power transmitter of its own. "
            "TRL 5 — ETSI RIS ISG and 3GPP Rel-19/20; operator trial (PoC) class. "
            "Not yet measured on the Türk Telekom network."
        ),
    },
    "cell_free": {
        "kicker": "Problem: it weakens at the cell boundary",
        "blurb": (
            "At the cell edge the signal weakens; handover risks a drop. "
            "Cell-free Massive MIMO (multiple-input multiple-output) lets distributed access points "
            "serve jointly so the edge is no longer the design problem. The cost is high-speed fibre "
            "between the points. "
            "TRL (Technology Readiness Level) 4: literature-prototype level; "
            "not yet used in the Türk Telekom network."
        ),
        "blurb_expert": (
            "SINR drops at the cell edge; handover carries drop risk. Cell-free Massive MIMO "
            "is an architecture in which distributed access points serve jointly with shared "
            "precoding: the edge is removed as a design object. The bill is fronthaul fibre. "
            "TRL 4 — 3GPP Rel-19/20 distributed MIMO; literature prototype. "
            "Not yet used in the Türk Telekom network."
        ),
    },
    "thz": {
        "kicker": "Problem: the data pipe is still narrow",
        "blurb": (
            "Current frequency bands can be insufficient for some bridge and data-centre links. "
            "THz (terahertz) opens the band between millimetre-wave and infrared; capacity grows. "
            "Free-space loss and molecular absorption then shorten range. "
            "TRL (Technology Readiness Level) 3: laboratory evidence; not used in a field network. "
            "6G does not mean THz alone."
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
            "Fixed network rules treat a packed stadium and an empty night the same way. "
            "AI-RAN (artificial-intelligence-native radio access network) redistributes resources "
            "from measurement on a short timescale. It is not a chat application. "
            "TRL (Technology Readiness Level) 5: trial stage; "
            "there is no field validation for unattended operation."
        ),
        "blurb_expert": (
            "A fixed RRM rule treats a packed stadium and an empty night with the same tariff. "
            "AI-RAN (artificial-intelligence-native radio access network) shifts resource on a "
            "millisecond-to-second loop from measurement. It is not a chatbot. "
            "TRL 5 — 3GPP TR 38.843 and O-RAN RIC trial class; "
            "no field validation for unattended operation."
        ),
    },
    "ntn": {
        "kicker": "Problem: the tower does not reach everywhere",
        "blurb": (
            "A city tower covers built-up areas and roads; mountain, sea, and disaster zones may stay empty. "
            "An NTN (non-terrestrial network) joins satellites and high-altitude platforms to the "
            "terrestrial core. The cost is delay and Doppler. "
            "TRL (Technology Readiness Level) 6: public direct-to-phone trials exist. "
            "It does not replace the city tower; it complements it."
        ),
        "blurb_expert": (
            "A terrestrial gNB covers the city and the asphalt; mountain, sea, and rubble stay empty. "
            "An NTN (non-terrestrial network) joins LEO and HAPS nodes to the core with Rel-17+ "
            "procedures. The bill is delay and Doppler. "
            "TRL 6 — TR 38.811; public Direct-to-Cell trials. "
            "Complements the terrestrial site; does not rival it."
        ),
    },
    "ambient_iot": {
        "kicker": "Problem: you cannot replace the battery on every object",
        "blurb": (
            "Replacing the battery on every tag at carton and greenhouse scale is uneconomic. "
            "Ambient IoT harvests ambient radio energy and reports a short identity by backscatter "
            "(weak reflection of the incoming wave); it does not carry video. "
            "TRL (Technology Readiness Level) 4: laboratory validation level; "
            "not at commercial deployment."
        ),
        "blurb_expert": (
            "Replacing batteries at carton and greenhouse scale is uneconomic. Ambient IoT harvests "
            "ambient RF and reports a short identity by backscatter; it does not carry video. "
            "TRL 4 — 3GPP TR 38.848; early trial (PoC) class. "
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
