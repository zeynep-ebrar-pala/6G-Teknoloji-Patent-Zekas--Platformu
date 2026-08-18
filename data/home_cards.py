"""Ana Sayfa kartları — kicker, gövde, üç çip. DataService katmanına bağlı değil."""

HOME_CARDS_TR = {
    "isac": {
        "kicker": "Sorun: kule konuşur, göremez",
        "chips": ["Yankıdan mesafe", "Doppler'den hız", "TRL 4, saha değil"],
        "blurb": (
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
    },
    "ris": {
        "kicker": "Sorun: dalga köşeyi dönemez",
        "chips": ["Faz kaydıran ayna", "Enerji kırıntısı", "TRL 5, ticari değil"],
        "blurb": (
            "Yüksek frekanslı dalga düz gitmeye eğilimlidir; köşeyi dönmez, asansör boşluğunda kaybolur. "
            "Her kör nokta için yeni kule dikmek pahalı ve pratik değildir. "
            "RIS (Reconfigurable Intelligent Surface — Yeniden Yapılandırılabilir Akıllı Yüzey) "
            "cepheye asılan elektronik bir aynadır: yüzeydeki her küçük eleman dalganın fazını kaydırır, "
            "hüzme size döner. Kendi başına sinyal üretmediği için enerji tüketimi kırıntı kadardır. "
            "TRL 5 seviyesindedir: prototip üretilmiş ve saha denemeleri yapılmıştır, "
            "ancak henüz ticari bir kulede kullanılmamaktadır."
        ),
    },
    "cell_free": {
        "kicker": "Sorun: hücre sınırında zayıflar",
        "chips": ["Handover kalkar", "Fronthaul bedeli", "TRL 4 stadyum adayı"],
        "blurb": (
            "Klasik şebekede her mahallenin bir hücresi vardır; kenara yaklaşınca sinyal düşer, "
            "kule değişince (handover) kopma riski doğar. "
            "Hücresiz Masif MIMO (Multiple-Input Multiple-Output — Çok Girişli Çok Çıkışlı) "
            "bu sınırı kaldırır: sokak lambası sıklığındaki erişim noktaları sizi birlikte taşır, "
            "kenar diye bir yer kalmaz. Bedeli, antenleri merkeze bağlayan "
            "fronthaul (ön bağlantı) fiberidir. "
            "TRL 4 seviyesindedir, yani hâlâ deneysel aşamadadır; "
            "ilk uygulama alanı olarak stadyum ve havalimanı gibi yoğun mekânlar düşünülmektedir."
        ),
    },
    "thz": {
        "kicker": "Sorun: veri borusu hâlâ dar",
        "chips": ["Bant katbekat artar", "Su buharı / duvar", "TRL 3, sokak değil"],
        "blurb": (
            "5G hızlıdır ama kablosuz boru hâlâ dardır; sunucular arası terabit hızındaki aktarım "
            "veya gerçek zamanlı hologram bu boruya sığmaz. "
            "THz (terahertz) milimetre dalga ile kızılötesi arasındaki spektrumdur; "
            "bant genişliği katbekat artar. Bedeli fiziktir: su buharı emer, duvar keser, mesafe kısalır. "
            "TRL 3 seviyesindedir: laboratuvar sonuçları güçlüdür, "
            "ama sokaktaki bir şebekede henüz kullanılmamaktadır. "
            "Ayrıca 6G'nin tamamı THz teknolojisine dayanmamaktadır."
        ),
    },
    "ai_ran": {
        "kicker": "Sorun: şebeke sabit kural izler",
        "chips": ["Ölçümle kaynak", "Sohbet botu değil", "TRL 5, insansız değil"],
        "blurb": (
            "Klasik şebeke sabit kuralı ezberden okur: dolu stadyum ile ıssız gece aynı kurala bakınca "
            "ya kaynak israf olur ya kalite düşer. "
            "AI-RAN (Artificial Intelligence-Native RAN — yapay zekâ tabanlı telsiz erişim ağı) "
            "kuleyi ölçer, milisaniye–saniye döngüsünde kaynak kaydırır. "
            "Sohbet botu değildir, ağı yöneten karar mekanizmasıdır. "
            "TRL 5 seviyesindedir: O-RAN RIC (RAN Intelligent Controller — RAN Akıllı Denetleyici) "
            "üzerinde denemeler yapılmıştır, ancak sahada tamamen insansız çalışma henüz kanıtlanmamıştır."
        ),
    },
    "ntn": {
        "kicker": "Sorun: kule her yere ulaşmaz",
        "chips": ["Kule yokken göğe", "Gecikme + Doppler", "TRL 6 tamamlayıcı"],
        "blurb": (
            "Karasal kule şehri ve asfaltı kapsar; dağ, açık deniz ve enkaz boş kalır. "
            "NTN (Non-Terrestrial Network — Karasal Olmayan Ağ) "
            "LEO (Low Earth Orbit — Alçak Dünya Yörüngesi) uydularını ve "
            "HAPS'ı (High-Altitude Platform Station — Yüksek İrtifa Platformu) "
            "3GPP şebekesiyle birleştirir: kule yokken telefon doğrudan göğe bağlanır. "
            "Bedeli, uzun mesafeden doğan gecikme ve uydu hareketinden gelen Doppler kaymasıdır. "
            "TRL 6 seviyesindedir ve yedi teknoloji arasında en olgun olanıdır; "
            "şehir içindeki 6G şebekesinin rakibi değil, onu tamamlayan bir çözümdür."
        ),
    },
    "ambient_iot": {
        "kicker": "Sorun: her nesneye pil değiştirilemez",
        "chips": ["Backscatter kimlik", "Video taşımaz", "TRL 4, rafa değil"],
        "blurb": (
            "Depodaki her koli, tarladaki her nem sensörü bugün pil ister. "
            "Pil bitince cihaz susar; milyonlarca pili değiştirmek işlemez. "
            "Ambient IoT ortamdaki RF (Radio Frequency — radyo frekansı) kırıntısını toplayıp "
            "geri saçılımla (backscatter) «buradayım» der; video taşımaz, sadece kimlik bildirir. "
            "TRL 4 seviyesindedir: 3GPP bünyesinde aktif bir çalışma kalemidir, "
            "ancak henüz her rafa yapıştırılmış, yaygın kullanılan bir teknoloji değildir."
        ),
    },
}

HOME_CARDS_EN = {
    "isac": {
        "kicker": "Problem: the tower talks, it cannot see",
        "chips": ["Range from the echo", "Speed from Doppler", "TRL 4, not in the field"],
        "blurb": (
            "On a fog-bound strait the tower delivers internet but cannot look and ask "
            "whether a ship is out there; the camera loses sight, and a separate radar truck "
            "is both expensive and pollutes the spectrum. "
            "ISAC (Integrated Sensing and Communication) uses the same radio wave both to carry data "
            "and to measure from the echo: delay gives range, Doppler shift gives speed. "
            "The bill is keeping that measurement reliable outside the laboratory; "
            "for Türk Telekom this is a candidacy, not a neighbourhood product. "
            "It is at TRL 4: the method has been validated in the lab, "
            "but it has not yet been tried in a live field network."
        ),
    },
    "ris": {
        "kicker": "Problem: the wave cannot turn the corner",
        "chips": ["Phase-shifting mirror", "A scrap of energy", "TRL 5, not commercial"],
        "blurb": (
            "A high-frequency wave tends to travel in a straight line; it does not turn the corner, "
            "and it vanishes in an elevator shaft. Planting a new tower for every blind spot "
            "is expensive and impractical. "
            "RIS (Reconfigurable Intelligent Surface) is an electronic mirror hung on the façade: "
            "each small element on the surface shifts the wave’s phase, and the beam turns toward you. "
            "Because it does not generate a signal of its own, energy use is a scrap. "
            "It is at TRL 5: a prototype has been built and field trials have been run, "
            "but it is not yet used on a commercial tower."
        ),
    },
    "cell_free": {
        "kicker": "Problem: it weakens at the cell boundary",
        "chips": ["Handover disappears", "Fronthaul is the bill", "TRL 4 stadium candidate"],
        "blurb": (
            "In a classical network every neighbourhood has a cell; as you approach the edge the signal drops, "
            "and when the serving tower changes (handover) drop risk appears. "
            "Cell-free Massive MIMO (Multiple-Input Multiple-Output) removes that boundary: "
            "access points as dense as street lamps carry you jointly, so there is no longer an “edge.” "
            "The bill is the fronthaul fibre that ties the antennas back to the centre. "
            "It is at TRL 4, still experimental; stadiums and airports are thought of as the first dense venues."
        ),
    },
    "thz": {
        "kicker": "Problem: the data pipe is still narrow",
        "chips": ["Bandwidth many times over", "Vapour / walls cut range", "TRL 3, not on the street"],
        "blurb": (
            "5G is fast, but the wireless pipe is still narrow; terabit transfer between servers "
            "or a real-time hologram will not fit down it. "
            "THz (terahertz) is the spectrum between millimetre-wave and infrared; "
            "bandwidth grows many times over. The bill is physics: water vapour absorbs, walls cut, range shrinks. "
            "It is at TRL 3: laboratory results are strong, but it is not yet used in a street network. "
            "6G as a whole also does not rest on THz."
        ),
    },
    "ai_ran": {
        "kicker": "Problem: the network follows a fixed rule",
        "chips": ["Resource from measurement", "Not a chatbot", "TRL 5, not unattended"],
        "blurb": (
            "A classical network recites a fixed rule from memory: when a packed stadium and a deserted night "
            "share the same rule, you either waste resource or lose quality. "
            "AI-RAN (Artificial Intelligence-Native RAN) measures the tower and shifts resource "
            "on a millisecond-to-second loop. It is not a chatbot; it is the decision mechanism that runs the network. "
            "It is at TRL 5: trials have been run on an O-RAN RIC (RAN Intelligent Controller), "
            "but fully unattended operation in the field has not yet been proven."
        ),
    },
    "ntn": {
        "kicker": "Problem: the tower does not reach everywhere",
        "chips": ["To the sky, no tower", "Delay + Doppler", "TRL 6 complement"],
        "blurb": (
            "A terrestrial tower covers the city and the asphalt; mountain, open sea, and rubble stay empty. "
            "NTN (Non-Terrestrial Network) joins LEO (Low Earth Orbit) satellites and "
            "HAPS (High-Altitude Platform Station) to the 3GPP network: "
            "when there is no tower the phone connects straight to the sky. "
            "The bill is delay from the long path and Doppler shift from satellite motion. "
            "It is at TRL 6 and the most mature of the seven; "
            "not a rival to the urban 6G network, but the complement that completes it."
        ),
    },
    "ambient_iot": {
        "kicker": "Problem: you cannot replace the battery on every object",
        "chips": ["Backscatter identity", "Does not carry video", "TRL 4, not on every shelf"],
        "blurb": (
            "Every carton in the warehouse, every soil-moisture sensor in the field, still wants a battery today. "
            "When the battery dies the device falls silent; swapping millions of batteries does not scale. "
            "Ambient IoT harvests a scrap of ambient RF (radio frequency) and says “I am here” by backscatter; "
            "it does not carry video, it only announces identity. "
            "It is at TRL 4: an active 3GPP work item, "
            "but not yet a technology stuck to every shelf and used at scale."
        ),
    },
}


def home_card(tech_id: str) -> dict:
    from i18n.core import get_lang

    table = HOME_CARDS_EN if get_lang() == "en" else HOME_CARDS_TR
    return table.get(tech_id) or HOME_CARDS_TR.get(tech_id) or {}
