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
            "Laboratory validation and early field trials "
            "(TRL 4 — 3GPP Rel-19/20 target)"
        ),
        "card_summary": (
            "The tower talks; it does not look. ISAC uses the same wave "
            "for talk and for echo."
        ),
        "beginner_one_liner": (
            "The cell site no longer only talks; it also 'hears' the car "
            "behind the fog."
        ),
        "highlights": [
            "Range from the echo",
            "Speed from Doppler",
            "TRL 4, not in the field",
        ],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>What is it in one sentence?</strong><br>"
            "ISAC is the 6G technology that lets base stations carry data to devices "
            "and, like an <strong style='color: #FFFFFF;'>invisible radar</strong>, detect vehicles, people, "
            "drones, and obstacles in the surroundings at centimetre-level accuracy.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Plain analogy:</strong><br>"
            "An ordinary base station is a radio tower that only 'talks'. An ISAC-capable 6G site "
            "becomes a <strong style='color: #FFFFFF;'>smart watchtower</strong>: it talks and scans the scene "
            "into a three-dimensional map."
        ),
        "beginner_principle": (
            "1. The site both transmits an internet signal and listens for that signal bouncing back from cars or walls.<br>"
            "2. The later the echo returns, the farther the object; how the tone shifts tells you how fast it is moving.<br>"
            "3. The same antenna talks and looks. No extra radar truck is required."
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
            "Zero extra radar hardware cost (the existing 6G network performs the radar role)",
            "High accuracy (sub-centimetre range and sub-degree angle estimation)",
            "Uninterrupted operation at night, in fog, and in bad weather (advantage over cameras)",
            "Dual use of the frequency spectrum (high spectral efficiency)",
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
            "<strong>Istanbul Strait and Sea of Marmara navigation safety:</strong> Türk Telekom coastal base stations track all vessels in fog with real-time position and speed.",
            "<strong>Istanbul / Ankara UAV (drone) corridors:</strong> Türk Telekom 6G sites support urban delivery-drone flight safety and detection of unauthorised drones.",
            "<strong>AFAD-integrated earthquake debris sensing:</strong> After a quake, through-wall RF sensing detects motion under rubble without cameras.",
        ],
    },

    "ris": {
        "title": "Reconfigurable Intelligent Surfaces (RIS)",
        "trl_desc": (
            "Field trials and prototype validation "
            "(TRL 5 — low-power intelligent surfaces)"
        ),
        "card_summary": (
            "The signal cannot turn the corner; RIS is an electronic mirror on the façade."
        ),
        "beginner_one_liner": (
            "An electronic mirror is hung on the building so the signal is not lost on the wall; "
            "it turns the beam into the room you choose."
        ),
        "highlights": [
            "Phase-shifting mirror",
            "A scrap of energy",
            "TRL 5, not commercial",
        ],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>What is it in one sentence?</strong><br>"
            "RIS is a technology applied to façades, windows, or walls that reflects incoming radio signals "
            "toward a chosen direction like a <strong style='color: #FFFFFF;'>smart mirror</strong>, covering "
            "blind spots the signal never reached.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Plain analogy:</strong><br>"
            "You are in a dark room and the flashlight (the base station) cannot light the far side of the wall. "
            "An adjustable mirror on that wall (RIS) bends the beam and sends a "
            "<strong style='color: #FFFFFF;'>focused light pencil</strong> into the unseen room."
        ),
        "beginner_principle": (
            "1. A thin electronic mirror is mounted on the building façade.<br>"
            "2. Each tiny patch of the mirror rotates the signal a little; together they steer the beam onto your phone.<br>"
            "3. It draws almost no electricity; it covers a blind spot without raising a new tower."
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
            "Very low cost and energy use (90%+ saving versus an active base station)",
            "Easy installation (flexible form factor that can be applied to walls, glass, and buildings)",
            "Environmentally friendly green technology (does not radiate actively; it steers the incident wave)",
            "Designable across frequency bands (from sub-6 GHz to THz)",
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
            "<strong>Historic Peninsula and narrow-street coverage (Istanbul):</strong> Continuous 6G via intelligent RIS coatings on building surfaces, without harming historic fabric or raising new towers.",
            "<strong>Eurasia Tunnel and Marmaray continuous coverage:</strong> Passive RIS panels that counter in-tunnel fading, targeting 10 Gbps+ for Türk Telekom subscribers.",
            "<strong>Türk Telekom Plaza and data-centre glass coating:</strong> Transparent RIS films on plaza façades to solve indoor mmWave coverage.",
        ],
    },

    "cell_free": {
        "title": "Cell-Free Massive MIMO",
        "trl_desc": (
            "Experimental prototype and simulation tests "
            "(TRL 4 — cell-free network architecture)"
        ),
        "card_summary": (
            "A drop at the cell edge; cell-free MIMO erases that boundary."
        ),
        "beginner_one_liner": (
            "The signal does not drop when you change towers in the city; the small antennas beside you "
            "hold you hand in hand."
        ),
        "highlights": [
            "Handover disappears",
            "Fronthaul is the bill",
            "TRL 4 stadium candidate",
        ],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>What is it in one sentence?</strong><br>"
            "Cell-Free Massive MIMO removes the classical 'cell' boundaries so that hundreds of small access points (APs) "
            "act as one vast system and surround every user without a break.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Plain analogy:</strong><br>"
            "In a classical cellular system the signal drops — and a drop-out is likely — when a user moves from one "
            "base station to the next. In a cell-free system, wherever you are, dozens of mini-antennas around you "
            "follow you as a shared <strong style='color: #FFFFFF;'>signal cloud</strong>."
        ),
        "beginner_principle": (
            "1. Small antennas sit densely, like street lamps; there is no single giant tower.<br>"
            "2. Your phone attaches to several of them at once.<br>"
            "3. As you walk, the antennas hand you over silently; the 'cell-edge' feeling disappears."
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
            "Cell-edge problem solved outright (uniform user experience)",
            "Very high spectral efficiency (5×–10× versus classical MIMO)",
            "Less need for macro towers (a more aesthetic, distributed architecture)",
            "Macro drop-outs (handover failures) driven toward zero",
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
            "<strong>Türk Telekom RAMS Park / Şükrü Saracoğlu stadium solution:</strong> Cell-free APs distributed on the roof and stands so that 50,000+ fans streaming live at once see zero throughput drop.",
            "<strong>Istanbul Airport indoor coverage:</strong> Unbroken 6G while passengers move through one of the world's largest terminals, without cellular handover drop-outs.",
            "<strong>Marmara Region smart industrial warehouses:</strong> Autonomous pallet trucks and robots stay fully synchronised without losing the signal at a cell edge.",
        ],
    },

    "thz": {
        "title": "Terahertz (THz) Communications",
        "trl_desc": (
            "Proof of concept and laboratory experiments "
            "(TRL 3 — 0.1 THz–10 THz spectrum)"
        ),
        "card_summary": (
            "The wireless pipe is still narrow; THz opens bandwidth, physics cuts range."
        ),
        "beginner_one_liner": (
            "You talk at a very high pitch between radio and light; downloading a film takes a blink, not seconds."
        ),
        "highlights": [
            "Bandwidth many times over",
            "Vapour / walls cut range",
            "TRL 3, not on the street",
        ],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>What is it in one sentence?</strong><br>"
            "THz communications uses the ultra-high frequency band between radio waves and infrared light "
            "(100 GHz–10 THz) to move data at <strong style='color: #FFFFFF;'>1 terabit per second (1000 Gbps)</strong>, "
            "at the speed of light.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Plain analogy:</strong><br>"
            "If 4G is a country road and 5G a wide motorway, terahertz communications is a "
            "<strong style='color: #FFFFFF;'>teleportation tube</strong>. It can move huge volumes "
            "(for example an entire 8K film in a hundredth of a second)."
        ),
        "beginner_principle": (
            "1. A higher-pitched radio tone is used; the pipe is wider, so more data fits.<br>"
            "2. That tone struggles through walls and rain; it wants short range and line of sight.<br>"
            "3. That is why the TRL is low: the laboratory is strong, the field is still limited."
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
            "Record data rate at terabit/s class (100 Gbps–1 Tbps)",
            "Ultra-low latency (sub-millisecond / microsecond class)",
            "High security (extremely narrow beam makes eavesdropping / hacking effectively impossible)",
            "Vast spectrum resource (no frequency congestion)",
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
            "<strong>Türk Telekom data-centre inter-rack THz mesh:</strong> In Ankara and Istanbul data centres, replace thousands of inter-rack fibre cables with 1 Tbps THz wireless links.",
            "<strong>Türk Telekom 6G inter-site ultra-backhaul:</strong> A terabit wireless fibre bridge between towers in mountainous or otherwise difficult terrain where pulling fibre is too hard or too costly.",
            "<strong>High-resolution holographic presentations:</strong> Live 8K holographic conferencing and communications at Türk Telekom technology centres.",
        ],
    },

    "ai_ran": {
        "title": "AI-Native Radio Access Network (AI-RAN)",
        "trl_desc": (
            "O-RAN RIC trials and AI protocol tests "
            "(TRL 5 — AI-native 6G)"
        ),
        "card_summary": (
            "The network recites from memory; AI-RAN redistributes resource on a millisecond loop."
        ),
        "beginner_one_liner": (
            "Instead of reading memorised rules, the base station watches live traffic and decides in milliseconds."
        ),
        "highlights": [
            "Resource from measurement",
            "Not a chatbot",
            "TRL 5, not unattended",
        ],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>What is it in one sentence?</strong><br>"
            "AI-Native RAN means the 6G radio access network (base stations and radio hardware) is designed "
            "<strong style='color: #FFFFFF;'>from the lowest layer to be run by artificial intelligence</strong>, "
            "not patched afterwards with an add-on application.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Plain analogy:</strong><br>"
            "A classical network is a robot that only applies rigid rules written by human engineers. "
            "AI-Native RAN is a <strong style='color: #FFFFFF;'>learning autonomous pilot</strong> that watches traffic "
            "and user behaviour and retunes its own parameters within milliseconds."
        ),
        "beginner_principle": (
            "1. The site continuously measures who is congested and where.<br>"
            "2. Software decides on its own to 'raise capacity in this neighbourhood'.<br>"
            "3. Humans do not write a rule every second; the network stays green and fast by learning."
        ),
        "working_principle": (
            "<strong style='color: #00E5FF;'>End-to-end deep-learning radio architecture:</strong><br>"
            "AI-Native RAN replaces conventional 3GPP protocol layers (PHY/MAC/RLC/PDCP) with deep AI models "
            "(deep learning, reinforcement learning, transformers).<br><br>"
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
            "Maximum energy efficiency (50%–70% energy saving)",
            "Autonomous network management with zero human intervention (Zero-Touch Network — ZTN)",
            "Instant learning of the modulation that fits the channel",
            "Infrastructure flexibility independent of a single vendor via O-RAN integration",
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
            "<strong>Türk Telekom Green Network initiative:</strong> AI-RAN deep-sleep on low-traffic night-time sites, targeting gigawatt-hour-class annual electricity savings.",
            "<strong>Süper Lig match-day dynamic intelligent traffic management:</strong> Around kick-off, AI automatically shifts resources on nearby sites to fans within milliseconds.",
            "<strong>Türk Telekom network predictive fault prevention:</strong> Detect hardware degradation at the base station hours before an outage and fail over to backup.",
        ],
    },

    "ntn": {
        "title": "Non-Terrestrial Networks (NTN)",
        "trl_desc": (
            "3GPP Rel-17/18 standardisation and commercial satellite trials "
            "(TRL 6 — satellite integration)"
        ),
        "card_summary": (
            "The tower cannot reach everywhere; NTN opens the 3GPP network to the sky."
        ),
        "beginner_one_liner": (
            "When the city tower is not enough, the satellite overhead takes over; the phone stays the same."
        ),
        "highlights": [
            "To the sky, no tower",
            "Delay + Doppler",
            "TRL 6 complement",
        ],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>What is it in one sentence?</strong><br>"
            "NTN (Non-Terrestrial Networks) merges low-Earth-orbit satellites (LEO), airships, and high-altitude "
            "platform stations (HAPS) with terrestrial base stations into one network, delivering "
            "<strong style='color: #FFFFFF;'>unbroken 6G coverage at every point on Earth</strong>.<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Plain analogy:</strong><br>"
            "The terrestrial network is street lighting that exists only in cities and along roads. NTN is a "
            "<strong style='color: #FFFFFF;'>giant spotlight in space</strong> that lights the whole planet from above; "
            "the signal does not drop in mid-ocean or on a mountain summit."
        ),
        "beginner_principle": (
            "1. Ground sites cover the city and the road.<br>"
            "2. Where that leaves a gap, a low-Earth-orbit satellite or a high-altitude platform speaks.<br>"
            "3. Your phone does not have to be a special satellite handset; the network joins sky and ground."
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
            "100% global coverage with no geographic restriction (zero coverage gap)",
            "Ability to operate fully independent of terrestrial infrastructure in disasters",
            "Eliminates the cost of pulling fibre to rural regions",
            "Direct connectivity from standard smartphones",
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
            "<strong>Türk Telekom disaster-resilient emergency network:</strong> Even if terrestrial towers or fibre are damaged in an earthquake, all subscribers keep talking to AFAD and their families over LEO satellites.",
            "<strong>Marmara and Black Sea fishing / merchant fleets:</strong> Devices with Türk Telekom SIMs stay in full coverage at sea via satellite.",
            "<strong>Eastern and Southeastern Anatolia mountain-rural coverage:</strong> 100% coverage on hamlets and mountain roads where raising a tower is geographically impossible.",
        ],
    },

    "ambient_iot": {
        "title": "Ambient IoT (Battery-Free Internet of Things)",
        "trl_desc": (
            "3GPP Rel-19 study item and battery-free tag PoC "
            "(TRL 4 — battery-free Internet of Things)"
        ),
        "card_summary": (
            "You cannot put a battery on every object; Ambient IoT says “I am here” on RF scraps."
        ),
        "beginner_one_liner": (
            "A tag as cheap as packing tape takes power from a Wi-Fi or 6G wave and says 'I am here'."
        ),
        "highlights": [
            "Backscatter identity",
            "Does not carry video",
            "TRL 4, not on every shelf",
        ],
        "executive_summary": (
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>What is it in one sentence?</strong><br>"
            "Ambient IoT is the technology of ultra-cheap smart tags that contain "
            "<strong style='color: #FFFFFF;'>no cell or battery at all</strong> and draw the electricity they need "
            "from radio waves in the air (RF energy harvesting).<br><br>"
            "<strong style='color: #00E5FF; font-size: 1.05rem;'>Plain analogy:</strong><br>"
            "Legacy radio tags are passive. Ambient IoT tags are more like a tiny solar panel: they absorb "
            "Wi-Fi and 6G signals in the air and become "
            "<strong style='color: #FFFFFF;'>battery-free miniature smart sensors that generate their own energy</strong>."
        ),
        "beginner_principle": (
            "1. The tag has no battery; it gathers scraps of energy from radio waves in the air.<br>"
            "2. With that energy it sends a short 'I am here' message.<br>"
            "3. In warehouses, farms, and logistics, billions of objects can be tracked without batteries."
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
            "Zero battery cost and no battery-replacement labour",
            "Environmentally friendly zero waste (no battery chemical pollution)",
            "Ultra-low manufacturing cost under one cent",
            "Unbounded service life (not limited by battery lifetime)",
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
            "<strong>Türk Telekom logistics and warehouse digital transformation:</strong> Track thousands of supplier SKUs and field assets with battery-free tags for 10 years with no maintenance.",
            "<strong>Türkiye smart-agriculture / greenhouse integration:</strong> Battery-free 6G moisture sensors scattered on farmland, driving irrigation automation through the Türk Telekom IoT platform.",
            "<strong>Smart-city meter reading:</strong> Automatic reading of water, natural-gas, and electricity meters with battery-free Ambient IoT tags.",
        ],
    },
}
