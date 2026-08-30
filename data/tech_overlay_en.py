"""
English overlay for TECHNOLOGIES user-visible copy.
Keys match data/technologies.py. Does not replace id, acronym, icon, trl,
mathematical_foundation, references, or formulas.
TRL integers and published figures are those of the Turkish source; they are
literature/target values, not field measurements on this platform.
"""

TECH_OVERLAY_EN: dict = {
    "isac": {
        "title": "Integrated Sensing and Communication (ISAC)",
        "trl_desc": (
            "3GPP Rel-19 work item (TR 22.837). Laboratory validation; "
            "not measured on a Türk Telekom network."
        ),
        "card_summary": (
            "The site does not measure the scene; ISAC processes bits and echo on the same RF chain."
        ),
        "beginner_one_liner": (
            "The same carrier carries data and extracts range/speed from the echo; it is not a radar box."
        ),
        "highlights": [
            "Range from the echo",
            "Speed from Doppler",
            "TRL 4, not in the field",
        ],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Problem</strong><br>"
            "A classical gNB optimises only the communications channel. Cameras fail in fog and darkness; "
            "a separate radar wants a second spectrum and produces EMI.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Method</strong><br>"
            "ISAC (Integrated Sensing and Communication) jointly designs user-plane delivery and extraction of "
            "range, speed, and angle from reflected energy — on the same carrier, antennas, and often the same waveform. "
            "It is not a radar box bolted beside the site.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Limit</strong><br>"
            "Power and time are split from the same budget; the echo decays as R⁴. Centimetre accuracy is a literature target. "
            "TRL 4 — Rel-19 (TR 22.837); laboratory, not a Türk Telekom field."
        ),
        "beginner_principle": (
            "1. The gNB radiates the user frame; there is no separate radar hardware.<br>"
            "2. Delay is range, Doppler is speed, array phase difference is AoA.<br>"
            "3. Bits and echo share time/frequency/code. The same power budget feeds both tasks."
        ),
        "working_principle": (
            "<strong style='color: #00E5FF;'>Shared waveform and hardware (Joint Communication and Sensing — JCR):</strong><br>"
            "ISAC combines wireless communication waveforms (OFDM / OTFS / terahertz waveforms) with radar detection "
            "on the same frequency band, the same hardware, and a shared resource-allocation algorithm.<br><br>"
            "1. <strong style='color: #FFFFFF;'>Monostatic and bistatic sensing:</strong> The base-station transmitter (Tx) radiates. "
            "The echo from the target is captured either at the same site (monostatic) or at neighbouring sites "
            "(bistatic / multistatic).<br>"
            "2. <strong style='color: #FFFFFF;'>Angle of arrival (AoA) and Doppler estimation:</strong> Delay of the echo yields range; "
            "phase shift yields Doppler / speed; phase differences across the antenna array yield AoA/AoD. Together they give "
            "the object's 3D position, velocity, and heading.<br>"
            "3. <strong style='color: #FFFFFF;'>Avoiding signal collision:</strong> Orthogonal sharing in time, frequency, and code keeps "
            "communication data and the radar echo from degrading each other."
        ),
        "system_architecture": (
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>1. Physical layer and antenna hardware (PHY &amp; hardware):</strong><br>"
            "• Massive MIMO (Multiple-Input Multiple-Output) arrays and wideband RF transceivers.<br>"
            "• Dual-functional waveform design (DFRC — Dual-Functional Radar-Communication) and OTFS "
            "(Orthogonal Time Frequency Space) modulation combine communication symbols and radar probing on a single RF carrier.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>2. Protocol and signal-processing layer (MAC &amp; signal processing):</strong><br>"
            "• Advanced DSP, FPGA, and GPU units run Cramér-Rao Bound (CRB) sensing limits and FFT-based Doppler/AoA estimators.<br>"
            "• Dynamic radio resource management (RRM) maximises radar resolution in real time without collapsing the communication rate.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>3. Network and edge-cloud integration (O-RAN &amp; core):</strong><br>"
            "• On Open RAN (O-RAN), xApps on the Near-RT RIC (RAN Intelligent Controller) build sensing maps.<br>"
            "• Architecture aligned with 3GPP Release-19/20 delivers sensed 3D point-cloud data to Türk Telekom edge servers (Edge Cloud)."
        ),
        "use_cases": [
            {
                "title": "Autonomous vehicles and V2X traffic safety",
                "description": (
                    "The base station both carries data and acts as radar, detecting vehicles in blind spots "
                    "and fog, and feeding collision-avoidance systems with centimetre-level position."
                ),
            },
            {
                "title": "Low-altitude UAV/drone traffic management (UTM)",
                "description": (
                    "6G sites sense commercial and unauthorised drones over the city — even behind walls — "
                    "to keep air corridors safe and block illicit flights."
                ),
            },
            {
                "title": "Smart-city traffic and pedestrian-flow mapping",
                "description": (
                    "Without installing cameras, base-station signals map vehicle density and pedestrian "
                    "motion at intersections in real time and feed smart traffic-light optimisation."
                ),
            },
            {
                "title": "Industrial warehouse AGV navigation",
                "description": (
                    "Indoors, AGVs sense obstacles and other robots from ISAC signals without GPS or LiDAR, "
                    "and follow millimetre-accurate, collision-free paths."
                ),
            },
            {
                "title": "Healthcare and elderly care (camera-free monitoring)",
                "description": (
                    "In-home RF sensing detects breathing rhythm, heartbeat, and falls without a privacy-invasive camera; "
                    "an emergency notification can be triggered automatically."
                ),
            },
        ],
        "advantages": [
            "No second radar RF chain or spectrum licence; existing gNB geometry is used",
            "Range resolution scales with bandwidth, angle with array aperture (literature target, not a field guarantee)",
            "Optical sensors weaken in fog, rain, and night; RF is milder (frequency-dependent)",
            "The same hertz carries bits and echo; spectral efficiency rises if the trade-off is managed",
        ],
        "disadvantages": [
            "Power/reflection trade-off between communication rate and radar resolution",
            "Dense urban clutter and multipath interference",
            "Privacy and personal-data concerns (tracking risk even without cameras)",
        ],
        "global_research": [
            "3GPP Release-19 Study Item: Integrated Sensing and Communication",
            "EU Hexa-X II Project (flagship 6G initiative in Europe)",
            "IEEE ComSoc ISAC Emerging Technology Initiative",
            "Nokia Bell Labs and Huawei 6G ISAC testbed demonstrations (100+ Gbps plus 1 cm sensing)",
        ],
        "tt_scenarios": [
            "<strong>Ankara test centre — ISAC trial (2026):</strong> With InterDigital, a trial on preliminary 6G ISAC architecture using ETSI ISAC ISG baseline concepts, showing collaborative cellular and Wi-Fi sensing. Test-centre work, not a retail-network product.",
            "<strong>Retail network:</strong> ISAC is not verified as a commercial product on the Türk Telekom retail network on this platform. TRL 4 — laboratory and test-centre class.",
            "<strong>6G standards preparation:</strong> Ericsson R&D MoU signed at MWC Barcelona 2026 for 6G standards input; integrated sensing architecture is tracked in that frame.",
        ],
    },

    "ris": {
        "title": "Reconfigurable Intelligent Surfaces (RIS)",
        "trl_desc": (
            "ETSI RIS ISG and 3GPP Rel-19/20 work item; public operator-PoC class. "
            "Not a Türk Telekom field measurement."
        ),
        "card_summary": (
            "The wave does not turn the corner; RIS is a programmable reflector on the façade."
        ),
        "beginner_one_liner": (
            "Element phase θ_n steers the beam to the UE; the surface is not a high-power transmitter."
        ),
        "highlights": [
            "Phase-shifting surface",
            "No high-power Tx",
            "TRL 5, not commercial",
        ],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Problem</strong><br>"
            "At mmWave and above, the path drops or dies without LoS. A site per blind spot is CAPEX and EMC load.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Method</strong><br>"
            "A RIS (Reconfigurable Intelligent Surface) is a programmable reflector whose PIN/varactor elements "
            "shift incident phase over 0–2π. It does not generate internet; it steers the gNB transmission toward the intended UE.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Limit</strong><br>"
            "Double-path loss applies; gain collapses if the channel cannot be estimated. “90% energy saving” is literature/target. "
            "TRL 5 — ETSI RIS ISG and Rel-19/20; PoC class, not a Türk Telekom field."
        ),
        "beginner_principle": (
            "1. A thin reflector is mounted on the façade. This is not a base station.<br>"
            "2. Elements steer the beam to the UE via θ_n.<br>"
            "3. The gNB names the target on a low-rate control link. The bill is channel estimation and double-path loss."
        ),
        "working_principle": (
            "<strong style='color: #00E5FF;'>Phase control and metamaterial reflection:</strong><br>"
            "RIS is an electronic surface that hosts hundreds or thousands of passive or semi-active microscopic "
            "reflecting elements (PIN diodes, varactors, or varactor-loaded metamaterials).<br><br>"
            "1. <strong style='color: #FFFFFF;'>Phase shifting:</strong> Each metamaterial element independently shifts the phase of the "
            "incident electromagnetic wave between 0 and 2π.<br>"
            "2. <strong style='color: #FFFFFF;'>Beamforming:</strong> Combined phase shifts steer the incident signal not as a simple "
            "specular bounce (beyond Snell's law) but as a narrow beam focused onto the intended user device.<br>"
            "3. <strong style='color: #FFFFFF;'>Zero / ultra-low energy:</strong> There is no active transmitter (no RF chain); only a few "
            "milliwatts are used to switch diode states."
        ),
        "system_architecture": (
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>1. Surface and hardware layer (RIS hardware &amp; metamaterials):</strong><br>"
            "• Microscopic reflecting elements arrayed on a printed circuit board (PIN diode, MEMS, or liquid-crystal metamaterials).<br>"
            "• Ultra-low-power phase-shifter drivers and a passive reflection architecture with no RF power amplifier.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>2. Controller and software layer (RIS controller &amp; microcontroller):</strong><br>"
            "• An FPGA / ARM embedded controller sets metamaterial diode voltages and phase angles on commands from the base station.<br>"
            "• Real-time beam-steering algorithms track moving user devices.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>3. Network and operator interface (control link &amp; 3GPP RIS architecture):</strong><br>"
            "• An ultra-low-latency wireless or wired control link (C-plane) runs between the base station (gNB) and the RIS controller.<br>"
            "• Plug-and-play integration into the Türk Telekom network, aligned with ETSI RIS ISG and 3GPP Rel-19/20 specifications."
        ),
        "use_cases": [
            {
                "title": "NLoS urban coverage between buildings",
                "description": (
                    "On streets with no line of sight, the RIS surface reflects the signal onto the target device "
                    "and keeps a continuous 6G link without installing an extra base station."
                ),
            },
            {
                "title": "Tunnel, metro, and underground coverage",
                "description": (
                    "Signal that fades around tunnel bends is steered by passive RIS panels on the walls; "
                    "passengers' phones stay connected underground."
                ),
            },
            {
                "title": "Indoor mmWave / THz connectivity",
                "description": (
                    "Inside offices and factories, wall reflections focus the mmWave signal onto the target device, "
                    "delivering gigabit rates between rooms without pulling cable."
                ),
            },
            {
                "title": "Green communications",
                "description": (
                    "Passive RIS needs no active amplifier; fewer active base stations cut both energy use "
                    "and carbon footprint."
                ),
            },
            {
                "title": "Positioning support with ISAC",
                "description": (
                    "The RIS surface both boosts the signal and sharpens device location from the reflection geometry, "
                    "supporting ISAC-based indoor positioning services."
                ),
            },
        ],
        "advantages": [
            "Lower-energy candidate than an active relay (the surface carries no high-power RF chain)",
            "Can be mounted on façade, glass, or tunnel geometry; a coverage-hole candidate without a new tower",
            "Does not radiate actively; it steers the incident wave (Maxwell is not cancelled)",
            "Surfaces can be designed from sub-6 GHz to THz; channel estimation is a separate bill",
        ],
        "disadvantages": [
            "Channel-estimation difficulty (passive elements cannot measure the channel)",
            "Two-hop fading (double path-loss: Tx → RIS → Rx)",
            "High compute load for real-time phase control",
        ],
        "global_research": [
            "ETSI Industry Specification Group (ISG) RIS",
            "IEEE Wireless Communications Technical Committee RIS Task Force",
            "ZTE, Huawei, and NTT Docomo field trials (5G-Advanced and 6G RIS PoC)",
            "RISE-6G EU Project (Reconfigurable Intelligent Surfaces for 6G)",
        ],
        "tt_scenarios": [
            "<strong>Verified field pilot:</strong> No recorded RIS field pilot or retail-network installation for Türk Telekom on this platform. TRL 5 — industry prototype class.",
            "<strong>6G R&D frame:</strong> Ericsson 2026 R&D MoU; EUREKA DRIVING-6G (AI-native 6G, Türkiye lead) tracks 6G architecture; RIS is followed in literature.",
            "<strong>Patent footprint:</strong> Locked Netsia patents focus on programmable RAN and slicing; no RIS-specific Netsia dossier is listed on this platform.",
        ],
    },

    "cell_free": {
        "title": "Cell-Free Massive MIMO",
        "trl_desc": (
            "3GPP Rel-19/20 distributed-MIMO work item; literature prototype/simulation. "
            "Not a Türk Telekom field measurement."
        ),
        "card_summary": (
            "SINR drops at the cell edge; cell-free MIMO removes the edge as a design object."
        ),
        "beginner_one_liner": (
            "Distributed APs serve jointly on the same frequency with shared precoding; the bill is fronthaul."
        ),
        "highlights": [
            "Joint precoding",
            "Fronthaul is the bill",
            "TRL 4 stadium candidate",
        ],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Problem</strong><br>"
            "SINR drops at the cell edge; handover carries drop risk. One macro plus many users leaves one side of the stand starved.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Method</strong><br>"
            "Cell-free Massive MIMO is an architecture in which geographically spread APs serve jointly, on the same frequency, "
            "with central or semi-distributed processing. The cell boundary is designed out.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Limit</strong><br>"
            "Without fronthaul fibre and synchronisation, joint precoding cannot be written. 5×–10× spectral gain is a literature range. "
            "TRL 4 — Rel-19/20 distributed MIMO; not a Türk Telekom field."
        ),
        "beginner_principle": (
            "1. APs are placed densely; the design does not rest on one macro.<br>"
            "2. The UE attaches to several APs at once.<br>"
            "3. The processor on fronthaul applies MMSE-style precoding. The bill is fronthaul and compute."
        ),
        "working_principle": (
            "<strong style='color: #00E5FF;'>Distributed coordination and cell-free architecture:</strong><br>"
            "In conventional networks users attach to a given cellular sector (cell), and interference rises at the cell edge.<br><br>"
            "1. <strong style='color: #FFFFFF;'>Distributed access points (distributed APs):</strong> Many simple APs spread over a wide area "
            "connect over high-speed fronthaul to a central processing unit (CPU).<br>"
            "2. <strong style='color: #FFFFFF;'>Joint cooperative precoding:</strong> All APs serve the user at the same time and on the same "
            "frequency. The cell-edge notion disappears entirely.<br>"
            "3. <strong style='color: #FFFFFF;'>Interference suppression:</strong> Neighbour-cell interference is turned into useful signal "
            "power through cooperative processing."
        ),
        "system_architecture": (
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>1. Distributed radio and antenna layer (distributed access points):</strong><br>"
            "• Low-complexity APs and multi-antenna arrays distributed across the city and buildings.<br>"
            "• Each AP runs local transmit/receive functions and offloads heavy processing to the central units.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>2. Fronthaul network (high-speed fibre fronthaul):</strong><br>"
            "• High-bandwidth fibre and optical infrastructure based on eCPRI and RoF (Radio over Fiber) connecting all APs to the CPU.<br>"
            "• Time synchronisation (PTP IEEE 1588) aligns antennas at nanosecond accuracy.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>3. Central processing unit (CPU and edge cloud):</strong><br>"
            "• An edge-cloud server pool that computes MMSE (Minimum Mean Square Error) and zero-forcing precoding matrices.<br>"
            "• Fair, uniform quality of experience at terabit-class connectivity for all users."
        ),
        "use_cases": [
            {
                "title": "Stadiums and concert venues",
                "description": (
                    "When tens of thousands connect at once, cell-edge interference disappears; "
                    "every stand gets a uniform gigabit experience."
                ),
            },
            {
                "title": "Airport and rail-station interiors",
                "description": (
                    "Handover drop-outs while walking through the terminal disappear; "
                    "distributed access points follow the user without a break."
                ),
            },
            {
                "title": "Autonomous factory robot control",
                "description": (
                    "Industrial robots stay in sync at sub-millisecond latency without losing the signal at a cell boundary; "
                    "production-line stops fall."
                ),
            },
            {
                "title": "Dense downtown boulevards",
                "description": (
                    "On crowded streets, distributed mini-antennas raise spectral efficiency versus a single macro tower "
                    "and give each user a fair share of bandwidth."
                ),
            },
        ],
        "advantages": [
            "Cell-edge SINR collapse is designed out (a uniform-experience candidate)",
            "Spectral-efficiency gains are reported in the literature (5×–10× range; not measured on this platform)",
            "Distributed-AP candidate for indoor spaces that do not want a macro aesthetic",
            "Classical handover failures fall under joint service (fibre/sync required)",
        ],
        "disadvantages": [
            "Massive fronthaul load (every AP must connect to a central unit at high rate)",
            "High computational complexity at the central processing unit (CPU)",
            "High fibre-optic infrastructure cost",
        ],
        "global_research": [
            "Linköping University (work of Prof. Emil Björnson and Prof. Erik G. Larsson)",
            "IEEE Wireless Communications Letters — Cell-Free special issues",
            "3GPP Release-19/20 Distributed Massive MIMO working groups",
            "Ericsson and Nokia 6G distributed MIMO laboratory demonstrations",
        ],
        "tt_scenarios": [
            "<strong>Verified field pilot:</strong> No recorded cell-free MIMO field pilot for Türk Telekom on this platform. TRL 4 — fibre backhaul cost is an operational constraint.",
            "<strong>R&D publication footprint:</strong> TT R&D-affiliated papers track 6G network slicing and machine learning; distributed antenna architecture appears in that literature.",
            "<strong>6G project participation:</strong> DRIVING-6G and Ericsson MoU track distributed RAN architecture; no retail-network installation record on this platform.",
        ],
    },

    "thz": {
        "title": "Terahertz (THz) Communications",
        "trl_desc": (
            "3GPP TR 38.807 (NR beyond 52.6 GHz) plus laboratory spectrum studies. "
            "Not a street network."
        ),
        "card_summary": (
            "The wireless pipe can stay narrow; THz opens bandwidth, FSPL and absorption cut range."
        ),
        "beginner_one_liner": (
            "In Shannon, capacity grows first with B; THz wants a short hop and line of sight."
        ),
        "highlights": [
            "Bandwidth grows first",
            "FSPL + absorption",
            "TRL 3, not on the street",
        ],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Problem</strong><br>"
            "Sub-6 GHz and mmWave can stay narrow for intra-DC mesh and tower bridges. Fibre does not reach every geometry.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Method</strong><br>"
            "THz communication is the attempt to open tens of GHz of bandwidth in, roughly, 0.1–10 THz. "
            "Shannon: C = B log₂(1+SNR); B is the first term.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Limit</strong><br>"
            "FSPL and water-vapour absorption cut range. “1 Tbps to every subscriber” is marketing. "
            "TRL 3 — TR 38.807; laboratory, not a street network. 6G is not THz alone."
        ),
        "beginner_principle": (
            "1. Spectrum between mmWave and infrared opens; B grows.<br>"
            "2. Vapour, walls, and a hand add loss on top of FSPL.<br>"
            "3. A narrow beam offsets loss; range stays short. The right geometry is a rack, a hall, a tower hop."
        ),
        "working_principle": (
            "<strong style='color: #00E5FF;'>Sub-THz and THz spectrum physics:</strong><br>"
            "THz bands (0.1 THz to 10 THz) sit on the electromagnetic spectrum between mmWave (millimetre wave) "
            "and optical / infrared frequencies.<br><br>"
            "1. <strong style='color: #FFFFFF;'>Ultra-wide bandwidth (B &gt; 10–50 GHz):</strong> As frequency rises, usable bandwidth "
            "becomes enormous.<br>"
            "2. <strong style='color: #FFFFFF;'>Molecular absorption loss:</strong> THz waves are absorbed by water vapour and molecules "
            "in air. Special 'spectral windows' are therefore used.<br>"
            "3. <strong style='color: #FFFFFF;'>Ultra-narrow beamforming:</strong> Extremely narrow beams from thousands of microscopic "
            "antenna elements compensate for the path loss."
        ),
        "system_architecture": (
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>1. Semiconductor and RF front-end hardware (GaN / InP / graphene transceivers):</strong><br>"
            "• Gallium nitride (GaN), indium phosphide (InP), or graphene-based THz transistor and amplifier circuits.<br>"
            "• Antenna-on-chip / antenna-in-package (AiP) arrays in packages only a few millimetres across.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>2. High-rate sampling and modulation (sub-THz ultra-DSP):</strong><br>"
            "• Ultra-fast ADC/DAC integrated circuits sampling at 100+ giga-samples per second.<br>"
            "• DSSS and high-order QAM modulation with terabit-class processing capacity.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>3. Ultra-short-range and data-centre transmission architecture:</strong><br>"
            "• Wireless mesh links between servers in data centres and ultra-backhaul links between towers.<br>"
            "• Operates with 3GPP sub-THz (100–300 GHz) standardisation specifications."
        ),
        "use_cases": [
            {
                "title": "Wireless data centre (terabit backhaul)",
                "description": (
                    "THz links replace fibre between server racks so intra-data-centre traffic moves wirelessly "
                    "at terabits per second."
                ),
            },
            {
                "title": "Holographic and real-time 3D VR/AR",
                "description": (
                    "Holograms and immersive VR that need hundreds of gigabits per second are delivered without delay "
                    "over ultra-wideband THz beams."
                ),
            },
            {
                "title": "Short-range wireless backhaul / fronthaul",
                "description": (
                    "Where pulling fibre between towers or inside a building is hard, a THz link supplies "
                    "high-capacity backhaul."
                ),
            },
            {
                "title": "Medical nanosensor networks",
                "description": (
                    "In-body implants and nanosensors exchange data at ultra-low latency, taking advantage of "
                    "THz-band miniaturisation."
                ),
            },
            {
                "title": "THz spectroscopy and material sensing",
                "description": (
                    "In security screening and industrial quality control, THz waves analyse material composition "
                    "in a non-communications sensing mode."
                ),
            },
        ],
        "advantages": [
            "Large B grows Shannon capacity first with bandwidth (target order of magnitude is literature)",
            "Low-latency candidate on a short hop; a URLLC claim does not hold for a street macro",
            "A narrow beam makes eavesdropping harder; “impossible” is not a security guarantee",
            "Spectrum congestion is milder than at sub-6; devices and absorption are a separate bill",
        ],
        "disadvantages": [
            "Short range (typically &lt; 100–500 metres because of high atmospheric and molecular absorption)",
            "Extreme sensitivity to physical blockage (even a leaf or a human hand can cut the signal)",
            "Difficult RF hardware manufacturing and high semiconductor cost",
        ],
        "global_research": [
            "IEEE 802.15.3d Terahertz Standardisation Group",
            "ITU-R WRC (World Radiocommunication Conference) spectrum allocations",
            "DARPA (USA) and Max Planck Institute THz research programmes",
            "Samsung 6G White Paper and sub-THz (140 GHz) field-test demos",
        ],
        "tt_scenarios": [
            "<strong>Verified THz installation:</strong> No recorded THz field installation or retail-network measurement for Türk Telekom on this platform. TRL 3 — laboratory stage.",
            "<strong>Data-centre infrastructure:</strong> The group operates data centres in Ankara and Istanbul; inter-rack THz wireless was not measured on this platform.",
            "<strong>6G literature tracking:</strong> Ericsson MoU and DRIVING-6G track high-frequency bands in literature; no commercial THz product announcement in these sources.",
        ],
    },

    "ai_ran": {
        "title": "AI-Native Radio Access Network (AI-RAN)",
        "trl_desc": (
            "3GPP TR 38.843 (AI/ML for NR) and O-RAN RIC trial class. "
            "Unattended field proof is absent; not measured by this platform."
        ),
        "card_summary": (
            "A fixed RRM rule is not enough; AI-RAN shifts resource on a measurement loop."
        ),
        "beginner_one_liner": (
            "xApps/rApps on an O-RAN RIC produce policy from measurement; it is not a chatbot."
        ),
        "highlights": [
            "Resource from measurement",
            "Not a chatbot",
            "TRL 5, not unattended",
        ],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Problem</strong><br>"
            "A fixed RRM tariff treats a packed stadium and an empty night with the same rule. A human cannot write policy every second.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Method</strong><br>"
            "AI-native RAN designs parts of PHY/MAC and resource management to run on a learned model. "
            "Practical entry today is xApps/rApps on an O-RAN RIC; making the whole air interface a neural net is the research edge.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Limit</strong><br>"
            "“50–70% energy” and “zero human” are target/marketing. TRL 5 — TR 38.843 and O-RAN RIC trial class; no unattended field proof."
        ),
        "beginner_principle": (
            "1. Load, channel, energy, and drops are measured.<br>"
            "2. xApps/rApps on the RIC produce policy.<br>"
            "3. The outcome is watched; a rollback path is part of the design. Supervision does not disappear."
        ),
        "working_principle": (
            "<strong style='color: #00E5FF;'>Learned RRM and (at the research edge) neural PHY:</strong><br>"
            "AI-native RAN does not, in practice, delete PHY/MAC wholesale. Today's entry is resource management via "
            "xApps/rApps on an O-RAN RIC. Replacing the air interface with an autoencoder is the research edge (TR 38.843).<br><br>"
            "1. <strong style='color: #FFFFFF;'>Deep-learning physical layer (Deep PHY autoencoder):</strong> Modulation and coding "
            "are learned end-to-end with deep autoencoders instead of fixed closed-form algorithms.<br>"
            "2. <strong style='color: #FFFFFF;'>O-RAN RIC (RAN Intelligent Controller):</strong> Near-RT and Non-RT RIC units run xApps "
            "and rApps that manage radio resources (RRM) dynamically.<br>"
            "3. <strong style='color: #FFFFFF;'>Intelligent deep sleep:</strong> When there is no traffic, parts of the base station "
            "are put to sleep with millisecond precision, yielding large energy savings."
        ),
        "system_architecture": (
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>1. Deep-autoencoder physical layer (neural air-interface PHY):</strong><br>"
            "• Signal-processing steps (modulation, channel coding, estimation) are executed by artificial neural networks (ANNs).<br>"
            "• Neural modulation patterns that adapt instantly to changing channel conditions are generated.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>2. Open RAN intelligent-controller architecture (Near-RT &amp; Non-RT RIC):</strong><br>"
            "• xApps on the Near-RT RIC (10 ms loop) take millisecond-scale beam management and handover decisions.<br>"
            "• rApps on the Non-RT RIC (100 ms+ loop) handle longer-term traffic prediction and network energy optimisation.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>3. Hardware and accelerator layer (AI-accelerated RAN hardware):</strong><br>"
            "• On-site NVIDIA, Qualcomm, or domestic NPU/GPU accelerator chips in the base stations (gNB).<br>"
            "• Vendor-independent intelligent infrastructure aligned with AI-RAN Alliance standards."
        ),
        "use_cases": [
            {
                "title": "Dynamic spectrum sharing (DSS)",
                "description": (
                    "The AI model optimises frequency use from live traffic, sharing idle spectrum efficiently "
                    "and reducing interference."
                ),
            },
            {
                "title": "Predictive maintenance and self-healing network",
                "description": (
                    "Machine learning detects base-station hardware faults hours before they occur "
                    "and fails over automatically to a backup system."
                ),
            },
            {
                "title": "Intelligent power saving (deep sleep)",
                "description": (
                    "In low-traffic hours AI-RAN puts unused radio units to sleep with millisecond precision "
                    "and cuts network energy use substantially."
                ),
            },
            {
                "title": "Sub-second beam management",
                "description": (
                    "Beam-steering decisions for moving users are taken in under a second with no human in the loop; "
                    "handover delay is minimised."
                ),
            },
        ],
        "advantages": [
            "An energy target is tracked on a measurement loop; 50–70% saving is target/marketing",
            "Zero-touch is a research-edge claim; rollback and supervision stay on a live network",
            "Policy updates when the channel changes; a black box must still be explainable to a regulator",
            "The O-RAN interface enables a multi-vendor trial; O-RAN is not the same as AI",
        ],
        "disadvantages": [
            "AI models as a black box and the difficulty of explainability",
            "High NPU/GPU hardware cost and energy draw",
            "Need to collect vast data for model training",
        ],
        "global_research": [
            "AI-RAN Alliance (NVIDIA, SoftBank, Ericsson, Nokia founding membership)",
            "O-RAN Alliance Working Group 2 and Working Group 10 (AI/ML workflow)",
            "3GPP Release-18 Study on AI/ML for NR Air Interface",
            "NVIDIA Aerial 6G SDK and deep-learning RAN testbeds",
        ],
        "tt_scenarios": [
            "<strong>Netsia patents (2023–2025):</strong> Group affiliate Netsia received US patents on RAN capacity sharing (RANxChange), access+backhaul slicing, and RIC slice assurance. Google Patents records are listed on this platform.",
            "<strong>AI-for-6G publications:</strong> TT R&D-affiliated papers on AI for 6G, network slicing, and radio planning (IEEE, Springer; 2025–2026). Counted in the locked DOI set.",
            "<strong>Open RAN and standards partnerships:</strong> Net Insight GNSS-independent sync and Open RAN extension (2025); Ericsson 6G standards MoU at MWC Barcelona 2026. Autonomous field operation not verified on this platform.",
        ],
    },

    "ntn": {
        "title": "Non-Terrestrial Networks (NTN)",
        "trl_desc": (
            "3GPP Rel-17 NTN specification (TR 38.811) and Rel-17/18 work item; "
            "public Direct-to-Cell trials. Not a Türk Telekom field measurement."
        ),
        "card_summary": (
            "The tower does not reach everywhere; NTN joins a LEO/HAPS cell to the core with Rel-17+."
        ),
        "beginner_one_liner": (
            "Direct-to-cell: a standard UE sees the satellite cell; the bill is delay and Doppler."
        ),
        "highlights": [
            "Direct-to-cell",
            "Delay + Doppler",
            "TRL 6 complement",
        ],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Problem</strong><br>"
            "A terrestrial gNB covers the city and the asphalt; mountain, sea, and rubble stay empty. Rural CAPEX breaks the terrestrial model.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Method</strong><br>"
            "NTN joins LEO/GEO/HAPS nodes to the terrestrial core with 3GPP Rel-17+. "
            "Direct-to-cell: a standard UE seeing a satellite cell, not a dedicated dish.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Limit</strong><br>"
            "“100% global, zero gap” is marketing. Not the primary path for urban capacity or sub-millisecond URLLC. "
            "TRL 6 — TR 38.811; public trials. Complements the urban site; does not rival it."
        ),
        "beginner_principle": (
            "1. The city stays on towers. Empty geography uses LEO / HAPS.<br>"
            "2. The target is a 3GPP UE seeing the satellite cell.<br>"
            "3. PHY corrects Doppler and delay; it is not a promise of terrestrial-class latency."
        ),
        "working_principle": (
            "<strong style='color: #00E5FF;'>Space–air–ground integrated architecture:</strong><br>"
            "NTN is the 3GPP Rel-17/18/19 architecture that connects satellites — especially LEO satellites at "
            "500–1200 km altitude — directly to standard smartphones (direct-to-cell).<br><br>"
            "1. <strong style='color: #FFFFFF;'>Direct-to-cell satellite connectivity:</strong> Phones with a standard 6G modem chipset "
            "attach to a LEO satellite without a dedicated satellite handset.<br>"
            "2. <strong style='color: #FFFFFF;'>High Doppler and delay compensation:</strong> Satellites move at 27,000 km/h, so the "
            "huge Doppler shift and delay are corrected at the physical layer.<br>"
            "3. <strong style='color: #FFFFFF;'>Regenerative satellite payload:</strong> 6G gNB base-station software runs on the satellite "
            "and processes data in space."
        ),
        "system_architecture": (
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>1. Space and air-segment hardware (LEO/GEO &amp; HAPS):</strong><br>"
            "• Low Earth Orbit (LEO — 500–1200 km) satellites and stratospheric airship/HAPS (20 km) platforms.<br>"
            "• Inter-satellite laser links (ISL) for in-space data routing.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>2. Terrestrial earth stations and fibre gateway (ground stations):</strong><br>"
            "• Türk Telekom terrestrial earth stations that collect high-frequency feeder-link signals from the satellites.<br>"
            "• High-speed optical fibre into the terrestrial 6G core (5GC/6GC).<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>3. Standard user-equipment layer (unmodified direct-to-cell UEs):</strong><br>"
            "• 3GPP Rel-17/18 NTN protocol set that talks to ordinary handsets without a special antenna or large dish.<br>"
            "• Unbroken global access for rural areas, maritime, and aviation."
        ),
        "use_cases": [
            {
                "title": "Open-sea and ship communications",
                "description": (
                    "In mid-ocean, with no terrestrial coverage, standard phones keep continuous data and voice "
                    "over a LEO satellite."
                ),
            },
            {
                "title": "In-flight passenger internet",
                "description": (
                    "NTN integration lets passengers attach at 6G-class rates even at cruising altitude."
                ),
            },
            {
                "title": "Emergency communications after a disaster",
                "description": (
                    "If terrestrial towers are down after an earthquake or flood, the satellite link keeps "
                    "emergency calling and coordination alive."
                ),
            },
            {
                "title": "Rural and mountain IoT tracking",
                "description": (
                    "Sensors on farms and mine sites that fibre or towers never reach report to the centre over NTN."
                ),
            },
        ],
        "advantages": [
            "Coverage candidate where tower economics fail (“100% global” is marketing)",
            "Backup-path scenario when the terrestrial site falls; not a field guarantee",
            "Candidate for not paying rural fibre CAPEX in every hamlet",
            "Rel-17+ direct-to-cell targets a standard UE; every legacy device is not guaranteed",
        ],
        "disadvantages": [
            "Higher latency than terrestrial networks (10–30 ms for LEO)",
            "Frequent signal handovers because satellites move fast",
            "Satellite launch and on-orbit maintenance costs",
        ],
        "global_research": [
            "3GPP Release-17/18/19 NTN Enhancements Work Item",
            "Starlink (SpaceX) Direct-to-Cell initiative and T-Mobile partnership",
            "AST SpaceMobile and Vodafone / AT&T direct-to-phone satellite trials",
            "ESA (European Space Agency) 6G Space Component Initiative",
        ],
        "tt_scenarios": [
            "<strong>TTI wholesale network:</strong> TTI (Türk Telekom International) states on its official About page that it operates wholesale PoPs in 19 countries. Terrestrial wholesale, not an NTN satellite product.",
            "<strong>Rural coverage (terrestrial):</strong> Rural connectivity in Türkiye is delivered via the terrestrial network and fibre investment. Rel-17 direct-to-cell NTN is not verified on the retail network on this platform.",
            "<strong>6G standards preparation:</strong> Ericsson MoU tracks satellite integration in literature. Industry direct-to-cell trials exist; no Türk Telekom field record is listed on this platform.",
        ],
    },

    "ambient_iot": {
        "title": "Ambient IoT (Battery-Free Internet of Things)",
        "trl_desc": (
            "3GPP Rel-19 work item (TR 38.848). PoC class; not a shelf product. "
            "Not a Türk Telekom field measurement."
        ),
        "card_summary": (
            "Battery logistics do not scale; Ambient IoT reports identity by backscatter from ambient RF."
        ),
        "beginner_one_liner": (
            "Friis harvest × backscatter = a short identity; it does not carry video or replace a phone."
        ),
        "highlights": [
            "Backscatter identity",
            "Does not carry video",
            "TRL 4, not a shelf product",
        ],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Problem</strong><br>"
            "Replacing batteries at carton, greenhouse, and meter scale is uneconomic. NB-IoT and RedCap still want an energy source.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Method</strong><br>"
            "Ambient IoT is the class of tags with no battery, or a very small one, that harvest ambient RF "
            "and send a short status, mostly by backscatter.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Limit</strong><br>"
            "Range is short and bit-rate low. “One cent, a trillion objects” is target/marketing. "
            "TRL 4 — TR 38.848; PoC class, not a shelf product."
        ),
        "beginner_principle": (
            "1. A rectenna converts an RF scrap to DC.<br>"
            "2. There is no PA; the incoming carrier is modulated. Range is short.<br>"
            "3. A nearby reader separates the weak echo. It does not carry video."
        ),
        "working_principle": (
            "<strong style='color: #00E5FF;'>Energy harvesting and backscatter communications:</strong><br>"
            "Ambient IoT converts ambient electromagnetic waves (RF signals) to direct current (DC) with a rectifier "
            "antenna (rectenna).<br><br>"
            "1. <strong style='color: #FFFFFF;'>RF energy harvesting:</strong> Microwatt-level RF power radiated by the base station "
            "is collected and stored in a capacitor.<br>"
            "2. <strong style='color: #FFFFFF;'>Backscatter modulation:</strong> The tag does not run its own transmitter; it reflects "
            "the incoming RF wave by changing antenna impedance.<br>"
            "3. <strong style='color: #FFFFFF;'>Zero battery:</strong> Battery replacement and charging disappear entirely."
        ),
        "system_architecture": (
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>1. Battery-free tag hardware (ambient tag &amp; rectenna):</strong><br>"
            "• Battery-less ultra-low-power ASIC and a micro-capacitor.<br>"
            "• A high-efficiency rectifier antenna (rectenna) that turns RF waves into DC electricity.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>2. Power-provider and reader nodes (power nodes &amp; readers):</strong><br>"
            "• 6G base stations or auxiliary energy transmitters that continuously radiate RF into the environment to feed the tags.<br>"
            "• High-sensitivity 6G reader antenna arrays that detect the extremely weak modulated reflections.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.02rem;'>3. 3GPP Rel-19 network and software layer (3GPP Ambient IoT specs):</strong><br>"
            "• Addressing and MAC-layer protocols standardised under 3GPP Release-19 for a trillion-object scale.<br>"
            "• Direct, secure sensor data flow into the Türk Telekom IoT Cloud platform."
        ),
        "use_cases": [
            {
                "title": "Supply-chain and logistics tracking",
                "description": (
                    "Battery-free RFID-like tags on pallets and cartons report location and temperature for years "
                    "with no battery change."
                ),
            },
            {
                "title": "Smart-agriculture sensors",
                "description": (
                    "Battery-free soil-moisture sensors buried in the ground harvest RF energy from the 6G network "
                    "and feed irrigation systems automatically."
                ),
            },
            {
                "title": "Food and pharmaceutical cold-chain monitoring",
                "description": (
                    "Warehouse and transport temperature is measured continuously with battery-free tags; "
                    "a breach raises an instant alarm."
                ),
            },
            {
                "title": "Smart buildings and structural health",
                "description": (
                    "Battery-free sensors embedded in walls and concrete report moisture, cracks, and vibration "
                    "for years with no maintenance."
                ),
            },
        ],
        "advantages": [
            "Battery-replacement logistics disappear (energy depends on ambient RF; it is not guaranteed)",
            "No chemical battery waste; in an RF-weak pocket the tag falls silent",
            "The cost target is a cheap tag; “one cent” is marketing/target",
            "No battery-life cap; a readable bit still depends on Friis harvest",
        ],
        "disadvantages": [
            "Short communication range because of ultra-low power (&lt; 10–50 metres)",
            "Very low data rate (simple sensor data at kbps class)",
            "Dependence on ambient RF energy density",
        ],
        "global_research": [
            "3GPP Release-19 Study on Ambient IoT for NR",
            "IEEE RFID and IEEE Wireless Communications ambient backscatter special issues",
            "EU Zero-Power IoT Research Consortium",
            "Wiliot and Qualcomm battery-free smart-tag demos",
        ],
        "tt_scenarios": [
            "<strong>IoT platform (operational):</strong> The Türk Telekom IoT platform collects and manages sensor and device data. Battery-free 6G Ambient IoT tag rollout is not verified on the retail network on this platform.",
            "<strong>6G literature tracking:</strong> R&D teams track low-power IoT and 6G topics in publication and patent data. No Ambient IoT-specific field pilot record on this platform.",
            "<strong>Patent footprint:</strong> Locked Netsia patents focus on AI-RAN and slicing; no Ambient IoT-specific group patent on this list. TRL 4 — does not replace your phone.",
        ],
    },
}
