"""English glossary prose — same keys as data.glossary.GLOSSARY."""

GLOSSARY_EN: dict[str, dict[str, str]] = {
    "TRL": {
        "definition": (
            "A 1–9 scale for how far a technology has moved from a laboratory idea to a product "
            "proven in real operational conditions."
        ),
        "why": "It separates marketing claims from field maturity and ties investment and standards decisions to readiness.",
    },
    "ISAC": {
        "definition": (
            "Joint design of data transmission and environmental sensing (range, velocity, angle) "
            "on the same radio resource, waveform, and often the same hardware."
        ),
        "why": "It adds awareness to the network without a separate radar band and antenna bill.",
    },
    "RIS": {
        "definition": (
            "A surface that steers the reflection of an incoming electromagnetic wave by tuning "
            "each element’s phase (and sometimes amplitude), usually without an active RF chain."
        ),
        "why": "It closes a dead zone and steers energy toward a user without raising a new tower.",
    },
    "NTN": {
        "definition": (
            "An architecture that treats LEO/GEO satellites, HAPS, or similar air/space nodes "
            "as part of the same 3GPP system as the terrestrial network."
        ),
        "why": "It puts geography beyond towers and fibre, and a disaster backup path, on the same protocol family.",
    },
    "MIMO": {
        "definition": (
            "An antenna technique that uses multiple transmit and receive antennas to carry several "
            "spatial streams at once or to form beams."
        ),
        "why": "It raises capacity and link reliability without multiplying spectrum.",
    },
    "OFDM": {
        "definition": (
            "A multi-carrier modulation that splits a wide band into mutually orthogonal subcarriers; "
            "it is the air-interface foundation of 4G/5G."
        ),
        "why": "It makes frequency-selective fading manageable; it is also an ISAC waveform candidate in 6G.",
    },
    "OTFS": {
        "definition": (
            "A waveform family that places symbols in the delay–Doppler plane and is more robust "
            "to high mobility than OFDM."
        ),
        "why": "In ISAC and high-speed scenarios it uses both the delay and Doppler structure of the channel.",
    },
    "CRB": {
        "definition": (
            "A theoretical lower bound on the variance of an unbiased estimator; in sensing it is the "
            "‘no estimator can beat this’ floor for angle/range/velocity accuracy."
        ),
        "why": "It quantifies the communication-rate versus sensing-accuracy trade-off in ISAC.",
    },
    "SNR": {
        "definition": "The ratio of desired signal power to noise power; dimensionless or in decibels (dB).",
        "why": "It is the basic quality metric that limits both bit error and radar detection probability.",
    },
    "SINR": {
        "definition": (
            "The ratio of desired signal power to the sum of other users’ interference plus thermal noise."
        ),
        "why": "In cellular and cell-free MIMO it represents real capacity more honestly than SNR.",
    },
    "RF": {
        "definition": "The slice of the electromagnetic spectrum used for wireless communications (kHz to hundreds of GHz).",
        "why": "It is the shared language of antennas, transceivers, and spectrum regulation.",
    },
    "GHz": {
        "definition": "A frequency unit: one billion cycles per second.",
        "why": "Cellular, mmWave, and the lower edge of THz are all quoted in GHz.",
    },
    "gNB": {
        "definition": "The 3GPP NR base-station entity that provides the radio link to user equipment.",
        "why": "It is the formal name for the ‘tower’ in diagrams and specifications.",
    },
    "UE": {
        "definition": "The end-user device in a 3GPP network (phone, CPE, industrial modem).",
        "why": "Link budgets, RIS paths, and NTN direct-to-cell all terminate at a UE.",
    },
    "AoA": {
        "definition": "The direction from which a wavefront arrives at an array, estimated from inter-element phase.",
        "why": "ISAC and beam management turn AoA into a location/heading cue.",
    },
    "Doppler": {
        "definition": "The frequency shift of a wave caused by relative radial motion between transmitter, target, and receiver.",
        "why": "It is the sensing observable for speed and a mobility stress test for OFDM/OTFS.",
    },
    "O-RAN": {
        "definition": (
            "An open radio-access architecture that splits the base station into interoperable units "
            "and exposes control via a RAN Intelligent Controller."
        ),
        "why": "AI-RAN xApps/rApps run on this control plane; it is not a new air interface by itself.",
    },
    "RIC": {
        "definition": (
            "The RAN Intelligent Controller in O-RAN: near-real-time (xApps) and non-real-time (rApps) "
            "software that tunes radio resources."
        ),
        "why": "Most production AI-RAN value sits in this loop, not in a neural PHY demo.",
    },
    "PHY": {
        "definition": "The physical layer: waveforms, modulation, coding, and the radio chain.",
        "why": "Neural transceivers are a PHY research edge; operators still live mostly above it.",
    },
    "MAC": {
        "definition": "The medium-access layer: who transmits when, on which resource, with which grant.",
        "why": "ISAC resource sharing and cell-free scheduling are MAC problems as much as PHY ones.",
    },
    "KPI": {
        "definition": "A tracking metric such as rate, latency, energy, or coverage used to judge a system.",
        "why": "On this platform scenario KPIs are rule-engine outputs, not field pings.",
    },
    "CAPEX": {
        "definition": "Capital expenditure: money spent on assets (sites, fibre, satellite capacity) rather than operations.",
        "why": "Scenario labels (low/high) are investment-scale tags, not tender prices.",
    },
    "DOI": {
        "definition": "A persistent identifier for a digital object, almost always a paper or dataset.",
        "why": "Every verified article on this platform opens through its DOI; invented DOIs are forbidden.",
    },
    "TF-IDF": {
        "definition": (
            "A lexical score: how often a term appears in a document, down-weighted by how common "
            "it is across the corpus."
        ),
        "why": "Patent maps and the AI assistant retrieve records with TF-IDF; they do not ‘understand’ text.",
    },
    "3GPP": {
        "definition": (
            "The international partnership that writes mobile-network technical specifications from 2G through 6G. "
            "Releases are feature packages."
        ),
        "why": "It separates a research idea from a specification that can enter a live network.",
    },
    "LEO": {
        "definition": "Low Earth orbit: typically a few hundred to about 1,200 km altitude.",
        "why": "Direct-to-cell 6G NTN designs mostly assume LEO constellations, not geostationary slots.",
    },
    "GEO": {
        "definition": "Geostationary orbit: about 36,000 km, appearing fixed over one longitude.",
        "why": "GEO still matters for broadcast and some backhaul; latency is much higher than LEO.",
    },
    "HAPS": {
        "definition": "High-altitude platform station: an airship or aircraft in the stratosphere (~20 km).",
        "why": "It sits between towers and LEO as a regional coverage and disaster-coverage candidate.",
    },
    "FSPL": {
        "definition": (
            "Geometric spreading loss of a spherical wave with distance and frequency, with no obstacle "
            "or atmospheric absorption."
        ),
        "why": "It is the first term in NTN and THz range budgets; a real channel adds absorption and blockage.",
    },
    "MMSE": {
        "definition": (
            "A statistical criterion that minimises expected squared error; common in cell-free MIMO "
            "channel estimation and precoding."
        ),
        "why": "Unlike crude interference-blind methods, it balances noise and interference.",
    },
    "DFRC": {
        "definition": "Design of a single waveform that both probes as radar and carries communication symbols.",
        "why": "It is what separates true ISAC hardware/waveform sharing from ‘two boxes side by side’.",
    },
    "JCR": {
        "definition": "Joint optimisation of resources, waveform, and processing for communication and sensing together.",
        "why": "It names dual use of spectrum and antennas instead of a separate radar plus a separate network.",
    },
    "EPO": {
        "definition": (
            "The office that examines a single application for European Patent Convention (EPC) states. "
            "A granted EP patent must then be validated in the chosen member countries."
        ),
        "why": (
            "A Turkish national filing does not cover Germany. European rights need an EP (or separate national) path. "
            "Türkiye is an EPO member; membership is not an automatic EP grant."
        ),
    },
    "PCT": {
        "definition": (
            "The WIPO international filing route (WO). It does not itself grant a patent; "
            "the case later enters national or regional phase (EP, US, TR…)."
        ),
        "why": "A WO number is not a ‘world patent’; the publication prefix (EP, US, TR) names the office.",
    },
    "API": {
        "definition": "A ruled call interface that one piece of software exposes to others.",
        "why": "The Springer Nature Meta API, Lens.org and optional LLM providers attach to this platform through APIs.",
    },
    "SDK": {
        "definition": "A package of libraries, tools, and docs for building on a platform.",
        "why": "AI-RAN and RIC apps often sit on a vendor SDK; that is a tool, not a standard.",
    },
    "AI": {
        "definition": "A family of computing methods that learn patterns from data and produce a decision or estimate.",
        "why": "On this platform it means both network control (AI-RAN) and the assistant — two different jobs.",
    },
    "ML": {
        "definition": "The subset of AI that learns parameters from examples instead of coding every rule.",
        "why": "3GPP ‘AI/ML for NR’ work items and RIC xApps use this term.",
    },
    "CAD": {
        "definition": "Designing hardware and antenna geometry in a numerical environment.",
        "why": "RIS elements and THz package antennas are drawn in CAD before fabrication; it is not a network protocol.",
    },
    "EMC": {
        "definition": "A device both managing its own emissions and remaining intact under others’ emissions.",
        "why": "Dense urban 6G and ISAC radar sidelobes must not disrupt spectrum neighbours.",
    },
    "EMI": {
        "definition": "Unwanted electromagnetic energy that disrupts a system’s operation.",
        "why": "It is EMC’s adversary; ISAC can collide a high-power radar with the communications receiver in one box.",
    },
    "FDTD": {
        "definition": "A numerical EM method that steps Maxwell’s equations on a space–time grid.",
        "why": "It is used to validate RIS metamaterials and THz packages before the lab bench.",
    },
    "FEM": {
        "definition": "A numerical method that splits complex geometries into small elements and solves field equations.",
        "why": "It complements FDTD in antenna, package, and cooling design; it is not a network simulation.",
    },
    "CFD": {
        "definition": "A family of methods that numerically solve flow and heat transport.",
        "why": "It applies to base-station cooling and HAPS aerodynamics; it is not a radio protocol.",
    },
    "AR": {
        "definition": "An interface class that overlays digital layers on a real view.",
        "why": "It is a high-bit-rate edge-app example in THz/6G capacity stories; not a field KPI here.",
    },
    "VR": {
        "definition": "An interface class that presents a fully synthetic 3-D environment.",
        "why": "Its latency and bit-rate needs are one of the arguments for THz and cell-free MIMO.",
    },
    "Meta API": {
        "definition": (
            "Springer Nature’s publication metadata API. Year and country charts on this page "
            "come from facets; institution and citation counts come from pulled records plus Crossref."
        ),
        "why": "The seven 6G topics are counted as «6G {token}» for 2020–2026; topics are not summed.",
    },
}

TRL_SCALE_EN = [
    {"level": "1–2", "title": "Idea and concept", "meaning": "Basic principle or application concept; no laboratory validation yet."},
    {"level": "3", "title": "Laboratory proof", "meaning": "A critical function was shown experimentally; not a street network."},
    {"level": "4", "title": "Laboratory component", "meaning": "A subsystem was validated in the lab; field use is still limited."},
    {"level": "5", "title": "Relevant environment / prototype", "meaning": "A prototype was tried in a realistic setting; not as mature as a commercial site."},
    {"level": "6", "title": "System in a relevant environment", "meaning": "A system prototype was shown in a relevant environment; an early commercial trial is possible."},
    {"level": "7–8", "title": "Operational prototype / qualified system", "meaning": "Validation close to real operating conditions."},
    {"level": "9", "title": "Fielded product", "meaning": "Proven in an operational mission; near sale or already sold."},
]
