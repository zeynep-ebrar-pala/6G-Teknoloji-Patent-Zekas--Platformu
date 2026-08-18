"""
Expert layer — same heading order, different sentences.
Does not skip the foundation sequence; adds equations, assumptions, 3GPP, alternatives, limits.
"""

EXPERT_COPY = {
    "isac": {
        "problem": (
            "A gNB (next-generation Node B) optimises only the Shannon channel (C = B log₂(1+SNR)); "
            "it does not extract kinematics from reflected energy. A separate radar means a second spectrum "
            "licence and a second RF chain; the adjacent band produces EMI. "
            "Assumption: communication and sensing share the same P_t and B — they are not two independent tasks."
        ),
        "why_needed": (
            "Operator spectrum and urban site geometry are already paid for. A separate UTM/radar network "
            "doubles CAPEX and EMI. ISAC’s rationale is to spend part of the existing EIRP on estimation "
            "(delay, Doppler, AoA). The trade-off sits on a Pareto surface: raising P_com raises C and lowers "
            "SNR_radar. This platform has no field SNR."
        ),
        "what": (
            "ISAC / DFRC (Dual-Functional Radar-Communication) / JCR (Joint Communication and Sensing): "
            "joint design of the user plane and the reflected echo on the same carrier and array. "
            "Monostatic (same gNB Tx/Rx) or bistatic (neighbour gNB Rx). Parking a radar box beside the site "
            "is not ISAC; that is two systems, two clocks, two spectra."
        ),
        "mental_model": (
            "Outbound path ~1/R². Return via target RCS σ another ~1/R² → R⁴ in the radar equation. "
            "ΔR ≈ c/(2B) is range resolution; narrow B cannot yield centimetres. The CRB is the variance "
            "floor of an unbiased estimator; Shannon C shares the same P and B. Far-field, point target, "
            "no clutter — optimistic in a city."
        ),
        "how_steps": [
            "Waveform: the OFDM or OTFS user frame is also the radar probe; there is no chirp truck.",
            "Estimation: τ = 2R/c range, f_d Doppler speed, array phase difference AoA/AoD. FFT estimators approach the CRB at high SNR.",
            "Sharing: time/frequency/code orthogonality aims to keep bits and echo from corrupting each other; perfect orthogonality breaks in practice.",
            "Edge: a point cloud or track summary goes to a Near-RT RIC / edge cloud. Raw I/Q fronthaul is not a Rel-19 product assumption.",
        ],
        "analogy": (
            "Alternative 1: separate automotive/military radar + cellular — mature, expensive in CAPEX/EMI. "
            "Alternative 2: camera/LiDAR — rich semantics, weak in fog/night/privacy. "
            "ISAC is a third class: shared waveform, spectral-saving candidate, clutter and privacy constraints."
        ),
        "analogy_technical_map": (
            "Validity: far-field, single round-trip, regular statistical model. "
            "Doubling R drops SNR_radar by ~16× (~12 dB). Raising B refines both C and ΔR but grows noise and compute. "
            "3GPP Rel-19 work item TR 22.837 is the frame; 1 cm is not a field guarantee derived from the inequality."
        ),
        "when_used": (
            "When site geometry already cuts the scene (road, corridor, shore), optics are blind, and a dedicated radar band cannot be licensed. "
            "Bistatic geometry can enlarge a small RCS. V2X / UTM testbeds sit in this class."
        ),
        "when_not": (
            "A single-path assumption breaks at a multipath junction. Not a public-surveillance product without privacy law. "
            "Medical micro-Doppler is literature, not device approval. This platform has no field CRB/SNR."
        ),
        "not_to_confuse": (
            "A co-sited radar ≠ ISAC. Computer vision produces pixels; an RF echo does not. "
            "Ambient IoT (TR 38.848) is a cooperative tag; the ISAC target is often a non-cooperative reflector."
        ),
        "real_world": (
            "TR 22.837 Rel-19 SI, Hexa-X-II architecture reports, IEEE ComSoc ISAC ETI, vendor testbeds. "
            "Vendor ‘100 Gbps + 1 cm’ together is not a metric verified on this platform."
        ),
        "tt_impact": (
            "A Bosphorus coastal gNB cuts the waterway; a drone corridor uses the site azimuth; debris has no optics. "
            "TRL 4 — laboratory / Rel-19 SI. Candidacy; not measured on the subscriber network."
        ),
    },
    "ris": {
        "problem": (
            "At mmWave and above, missing LoS drops capacity via loss and blockage. "
            "An active relay carries its own RF chain, PA, and interference. Assumption: the channel is two hops "
            "(gNB→RIS→UE); single-hop Friis does not hold."
        ),
        "why_needed": (
            "A gNB per blind spot is CAPEX and EMC load. A RIS is a candidate to make the environment a controllable "
            "channel by programming the boundary condition. Energy saving versus an active relay is a claim; "
            "N² scaling holds only with channel estimation and phase coherence. 90% saving is literature/target; "
            "this platform has no field bill."
        ),
        "what": (
            "RIS (Reconfigurable Intelligent Surface): N tunable elements, PIN/varactor, θ_n ∈ [0, 2π). "
            "Effective channel h_rᴴ Φ G, Φ = diag(e^{jθ_n}). The surface does not generate internet; it steers "
            "the gNB illuminator toward the UE. ETSI RIS ISG + Rel-19/20 work item."
        ),
        "mental_model": (
            "Passive/semi-passive boundary: an element is not a receiver and cannot measure the channel alone. "
            "Double path-loss is the Tx→RIS→Rx product. Under ideal phase alignment N elements scale power ~N²; "
            "CSI delay or phase quantisation breaks that scale. If controller delay cannot track user speed, the beam slips."
        ),
        "how_steps": [
            "Surface: façade/glass/tunnel — PIN/MEMS/LC on PCB; no PA, or mW-class drivers.",
            "Phase write: FPGA/MCU updates Φ on a gNB C-plane command. The control link is low-rate.",
            "Channel estimation: a passive element does not measure; Φ is chosen from gNB/UE pilots. This step is the condition for gain.",
            "Beam: the array factor toward the UE. Steering ‘beyond Snell’ does not cancel Maxwell; only the boundary is programmed.",
        ],
        "analogy": (
            "Active relay / small cell: own transmitter, energy and interference. "
            "Passive reflector (flat mirror): phase not programmable. "
            "RIS: programmable boundary, shared gNB illuminator. The three are not the same CAPEX class."
        ),
        "analogy_technical_map": (
            "Validity: narrowband, slow fading, Φ update inside the coherence time. "
            "Gain scales theoretically as N²; the practical cap is estimation dimension and control delay. "
            "It can sit with ISAC; a RIS alone does not write a radar equation."
        ),
        "when_used": (
            "N-LoS urban canyon, tunnel bend, stand, heritage fabric where a tower is forbidden, indoor mmWave. "
            "Geometry that wants lower energy than an active relay, with channel estimation treated as solvable."
        ),
        "when_not": (
            "High mobility + a slow controller. No CSI. Long range where two-hop loss beats single-hop Friis. "
            "Not plug-and-play commodity on every façade. Not a TT field measurement (TRL 5, PoC class)."
        ),
        "not_to_confuse": (
            "Not a small cell. An ‘invisibility cloak’ claim oversells the metamaterial boundary. "
            "The Massive MIMO array sits at the gNB; the RIS is a separate surface."
        ),
        "real_world": (
            "ETSI ISG RIS, 3GPP Rel-19/20 RIS SI, RISE-6G, ZTE/Huawei/NTT PoCs. "
            "An operator field trial is not a default subscriber-network product."
        ),
        "tt_impact": (
            "Peninsula, tunnel, plaza glass: coverage without a new tower. TRL 5 — prototype in a relevant environment. "
            "No field promise without a control link and a CSI procedure."
        ),
    },
    "cell_free": {
        "problem": (
            "In a classical cell, edge SINR_k has neighbour-cell interference in the denominator. "
            "Handover drops when cell identity changes. Assumption: one serving gNB. "
            "That assumption breaks under stadium/terminal load."
        ),
        "why_needed": (
            "Distributed APs shorten the path and make interference jointly processable (joint precoding). "
            "The bill is fronthaul (eCPRI/RoF) capacity and sync (IEEE 1588 class). "
            "5×–10× spectral gain is a literature range; not measured on this platform."
        ),
        "what": (
            "Cell-free Massive MIMO: M geographic APs jointly serve K users in the same TTI and frequency. "
            "The cell edge is designed out. Rel-19/20 distributed-MIMO work item; CoMP is the ancestor "
            "but keeps cell identity."
        ),
        "mental_model": (
            "SINR_k numerator |Σ_m g_mkᴴ w_mk|², denominator other-user leakage + σ². "
            "w is written at the CPU by MMSE or ZF. Fronthaul delay or phase drift makes w wrong and reverses the gain. "
            "Without fibre, joint precoding is undefined."
        ),
        "how_steps": [
            "Placement: low-complexity APs; local DSP limited, heavy matrices at the CPU/edge.",
            "Fronthaul: eCPRI or RoF; sync loss eats beamforming gain.",
            "Estimation: joint uplink pilots; pilot contamination remains a constraint.",
            "Precoding: MMSE/ZF w_mk. The ‘no edge’ claim depends on the sync+fronthaul assumption.",
        ],
        "analogy": (
            "A small-cell forest: every cell still has an edge. "
            "Classical CoMP: joint processing, cell identity remains. "
            "Wi-Fi roaming: your symbol is not carried by several APs at once. "
            "Cell-free MIMO goes all the way to a ‘no cell’ assumption."
        ),
        "analogy_technical_map": (
            "Validity: good enough CSI, fronthaul delay inside coherence, phase-locked array. "
            "Fibre to every pole in sparse rural is CAPEX-nonsense — NTN/macro is the alternative."
        ),
        "when_used": (
            "High density + mobility + a fairness target: stadium, airport, production line, indoor. "
            "Geometry that does not want a macro aesthetic."
        ),
        "when_not": (
            "Sparse rural, a street without fibre. If CPU complexity misses real time. "
            "Terabit ‘per user’ was not measured here. TRL 4, literature prototype."
        ),
        "not_to_confuse": (
            "A DAS may be analogue distribution; cell-free MIMO is digital joint precoding. "
            "Massive MIMO grows the array on one site; cell-free is geographic distribution."
        ),
        "real_world": (
            "Björnson/Larsson literature, IEEE cell-free special issues, Rel-19/20 distributed MIMO, "
            "Ericsson/Nokia laboratory demonstrations. Not a city-wide product."
        ),
        "tt_impact": (
            "Airport, stadium, warehouse edge complaint. TRL 4. Dense venues first; fronthaul is a design constraint."
        ),
    },
    "thz": {
        "problem": (
            "In Shannon, C = B log₂(1+SNR). At sub-6 and mmWave, B can stay too narrow for intra-DC mesh "
            "and a tower hop. As frequency rises, FSPL ∝ (f d)² and molecular absorption e^{K(f)d} grow. "
            "Assumption: LoS, aligned beam, short d."
        ),
        "why_needed": (
            "Fibre does not reach every geometry. THz is a tens-of-GHz B candidate on the right hop. "
            "‘1 Tbps to every subscriber’ is marketing; if absorption collapses SNR, B is not enough. "
            "TRL 3 — TR 38.807; not a street network."
        ),
        "what": (
            "THz / sub-THz: roughly 0.1–10 THz; the practical 6G candidate is often the 100–300 GHz window "
            "(NR beyond 52.6 GHz, TR 38.807). 5G mmWave (28–39 GHz) is not this class. "
            "IEEE 802.15.3d is a separate WPAN track."
        ),
        "mental_model": (
            "L(f,d) = (4π f d / c)² · e^{K(f)d}. K(f) jumps on water-vapour lines. "
            "As B grows, C rises near-linearly, but N_0 B in the SNR denominator and absorption eat the log term. "
            "A narrow beam buys EIRP and raises blockage probability."
        ),
        "how_steps": [
            "Window: spectral windows where K(f) is low; not every THz hertz is usable.",
            "RF front-end: InP/GaN/graphene candidates; not mature CMOS — why TRL is low.",
            "ADC/DAC: high sample rate, power and heat. 100 GSa/s class is literature/target.",
            "Geometry: rack, hall, tower hop. A street macro sits outside this equation’s validity window.",
        ],
        "analogy": (
            "Wireless fibre: high B, short d, aligned. "
            "Free-space optics (laser): different wavelength, different fog/rain physics. "
            "A macro cellular carrier is not THz."
        ),
        "analogy_technical_map": (
            "Validity: LoS, narrow beam, d of tens to hundreds of metres, little rain or a short hop. "
            "A hand/leaf cuts the link (blockage). ‘Impossible to hack’ is not a security guarantee derived from beamwidth."
        ),
        "when_used": (
            "Data-centre mesh, short backhaul/fronthaul, controlled indoor, spectroscopy. "
            "If a backup LoS and a pointing budget exist."
        ),
        "when_not": (
            "Open-city macro, long rainy hops, phone-to-phone kilometres, medical nanosensors as a Rel-19 feature. "
            "6G is not THz alone. This platform did not measure Tbps."
        ),
        "not_to_confuse": (
            "mmWave ≠ THz. ISAC may use a THz waveform; THz is not by itself a sensing standard."
        ),
        "real_world": (
            "IEEE 802.15.3d, ITU-R WRC spectrum studies, TR 38.807, vendor sub-THz demonstrations. "
            "Not the default band in a subscriber handset."
        ),
        "tt_impact": (
            "Rack and a tower hop where fibre cannot be pulled. TRL 3, laboratory. Not a handset-speed claim."
        ),
    },
    "ai_ran": {
        "problem": (
            "A fixed RRM threshold sticks in a local optimum; traffic/channel/energy are non-stationary. "
            "A human cannot write policy every 10 ms. Assumption: measurement quality is high and rollback is defined. "
            "A black box cannot be explained to a regulator — a product constraint, not a style choice."
        ),
        "why_needed": (
            "Near-RT RIC (~10 ms, O-RAN definition) for beam/handover; Non-RT rApp at seconds+ for energy and prediction. "
            "A learning loop meets the need for measurement-driven adaptation. The GPU/NPU burns its own energy; "
            "without a measured net gain, ‘50–70%’ is target/marketing. TR 38.843 + O-RAN WG2/10."
        ),
        "what": (
            "AI-native RAN has two layers: (1) practical entry — RRM policy via xApp/rApp; "
            "(2) research edge — autoencoder PHY, a learned air-interface representation. "
            "O-RAN is an interface; AI is an application. The chat assistant is not AI-RAN."
        ),
        "mental_model": (
            "RL: state s (SINR, PRB, load), action a (RRM), reward r (capacity/energy/outage). "
            "Q(s,a) ← Q + α[r + γ max Q' − Q]. Autoencoder loss E[||s − f_D(f_E(s)+n)||²]. "
            "A wrong reward can lock the network; rollback is part of the design. Supervision does not disappear."
        ),
        "how_steps": [
            "Measure: load, SINR, PRB, energy, fault precursors — a model cannot exceed its data quality.",
            "Near-RT xApp: tens of ms for beam/handover. Non-RT rApp: seconds+ for sleep and prediction.",
            "Apply: policy is written to the gNB. Without rollback, an untrained model is not an autonomous pilot on a live network.",
            "Learn: if the reward is poor, update. Zero-touch (ZTN) is the research edge; no field proof (TRL 5).",
        ],
        "analogy": (
            "Classical SON: rule-based self-organising. "
            "AI-RAN RRM: learned policy, same loop, measurement required. "
            "Neural PHY: a separate layer, Rel-18/TR 38.843 study area, laboratory."
        ),
        "analogy_technical_map": (
            "Validity: non-i.i.d. traffic; distribution drift must be watched. "
            "Explainability (XAI) is a regulatory constraint. O-RAN ≠ a guarantee of multi-vendor AI; it is an interface standard."
        ),
        "when_used": (
            "Variable load, an energy target, predictive maintenance, a RIC trial. If measurement quality and rollback exist."
        ),
        "when_not": (
            "Untrained model, no field data, black box unacceptable. "
            "‘Zero human’ is marketing. This platform has no energy bill."
        ),
        "not_to_confuse": (
            "The platform chatbot ≠ AI-RAN. O-RAN is an open interface; AI may or may not sit on it as an xApp."
        ),
        "real_world": (
            "AI-RAN Alliance, O-RAN WG2/WG10, TR 38.843, NVIDIA Aerial testbeds, operator RIC PoCs. "
            "A fully neural air interface is laboratory."
        ),
        "tt_impact": (
            "Post-match resource, night sleep, a fault precursor. TRL 5, RIC trial class. Human supervision stays."
        ),
    },
    "ntn": {
        "problem": (
            "Terrestrial coverage is tower+fibre geometry. LEO ~500–1200 km, v ≈ 7.5 km/s → "
            "Doppler f_d = f_c (v/c) cosθ and frequent handover. GEO RTT ~250 ms class (literature). "
            "FSPL ∝ (d f)². Assumption: Rel-17+ NTN modem, feeder link, gateway."
        ),
        "why_needed": (
            "Rural CAPEX, sea, aviation, disaster (when the site falls) break the terrestrial model. "
            "The need is to close the gap with the same 3GPP identity. Not the primary path for urban capacity "
            "or URLLC. TRL 6 — TR 38.811, public Direct-to-Cell."
        ),
        "what": (
            "NTN: joining a LEO/GEO/HAPS node to the terrestrial core with Rel-17+. "
            "Direct-to-cell: a standard UE seeing a satellite cell; not a VSAT dish. "
            "HAPS is a stratospheric platform, not a satellite. Consumer LEO broadband (e.g. Starlink) "
            "need not be the same product as an NTN cell."
        ),
        "mental_model": (
            "Terrestrial is primary; NTN closes the coverage hole. Link budget is FSPL + atmosphere + antenna gain. "
            "Without PHY Doppler and delay pre-correction, PRACH will not hold. "
            "A regenerative payload runs a gNB on the satellite; a transparent payload hauls to the ground — not the same delay."
        ),
        "how_steps": [
            "Cell selection: gNB in the city; NTN cell in the gap. Terrestrial has priority.",
            "Feeder: satellite → gateway → 5GC/6GC. The gateway is operator presence.",
            "Compensate: f_d and timing advance; the Rel-17 NTN specification (TR 38.811) is the frame.",
            "Service class: emergency SMS/voice first. A terabit urban experience is not this equation’s output.",
        ],
        "analogy": (
            "VSAT: dish, a separate system. Direct-to-cell: handset antenna, Rel-17+ modem. "
            "HAPS: ~20 km class, not an orbit. ISAC ‘making the sky a radar’ is not NTN."
        ),
        "analogy_technical_map": (
            "Validity: visible satellite, sufficient EIRP, licensed spectrum. "
            "‘100% global, zero gap’ is marketing. This platform did not measure satellite delay in the field."
        ),
        "when_used": (
            "Where FSPL and site CAPEX beat a terrestrial hop: rural/mountain, maritime, aviation, "
            "and disaster when the gNB is down. Feeder + gateway must exist; regenerative vs transparent "
            "payload sets the delay class. Not a substitute for urban macro capacity."
        ),
        "when_not": (
            "Urban capacity, sub-ms URLLC as the primary path. Not every legacy device is a Rel-17 NTN guarantee."
        ),
        "not_to_confuse": (
            "Direct-to-cell ≠ VSAT. HAPS ≠ LEO. NTN is a complement, not a rival to the 6G macro."
        ),
        "real_world": (
            "TR 38.811, Rel-17/18/19 NTN WI, public Direct-to-Cell trials (operator–satellite partnerships). "
            "A disaster backup path is strategy, not a field guarantee."
        ),
        "tt_impact": (
            "Disaster, fleet, rural. TRL 6 — the most mature of the seven. A complement; it does not replace the city site."
        ),
    },
    "ambient_iot": {
        "problem": (
            "NB-IoT/RedCap still wants an energy source. Battery logistics at pallet/greenhouse scale is CAPEX+OPEX. "
            "Backscatter reflected power is weak; range is capped by Friis harvest × η_rectenna. "
            "Assumption: enough ambient RF, a nearby reader, a narrow bit."
        ),
        "why_needed": (
            "‘Where / how many degrees’ without a maintenance crew. The aim is sparse identity, not video. "
            "‘One cent, a trillion objects’ is target/marketing. TR 38.848 Rel-19 SI; not a shelf product."
        ),
        "what": (
            "Ambient IoT: a batteryless or micro-capacitor tag; rectenna RF→DC; communication mostly by "
            "backscatter (modulating the incoming carrier via antenna impedance, no PA). "
            "The reader is a gNB or a helper illuminator. ISAC measures a non-cooperative echo; this class is a cooperative tag."
        ),
        "mental_model": (
            "P_rec = P_tx G_tx G_rx (λ/4πd)² η. y(t) = α x(t) b(t) + n(t). "
            "In an RF-weak pocket the tag falls silent — zero battery cost is not an energy guarantee. "
            "RFID is the ancestor; the difference is a 3GPP cellular reader and a Rel-19 addressing target."
        ),
        "how_steps": [
            "Harvest: rectenna; efficiency η < 1, range falls with Friis.",
            "Modulation: b(t) is an impedance switch; no PA of its own, range is short (literature < 10–50 m class, geometry-dependent).",
            "Read: a high-sensitivity array separates the weak echo+bit. The protocol is narrow (kbps).",
            "Cloud: a narrow identity (‘carton, °C’). Video/telemetry does not fall out of this equation.",
        ],
        "analogy": (
            "Shop-door RFID: the ancestor, not a cellular multi-reader. "
            "A solar+battery harvesting sensor: a different class; Ambient IoT is not always a ‘zero battery’ claim. "
            "ISAC: a non-cooperative reflector."
        ),
        "analogy_technical_map": (
            "Validity: an illuminator is present, d is short, bits are sparse. "
            "Unbounded life still depends on a readable bit from harvest. Not a TT field (TRL 4)."
        ),
        "when_used": (
            "Pallet, cold chain, greenhouse, meter, structural health — short range, low bit-rate, long-life target."
        ),
        "when_not": (
            "Audio/video, kilometres, moving-vehicle telemetry, an RF-free corner. It does not replace a phone."
        ),
        "not_to_confuse": (
            "Shop-floor RFID ≠ Rel-19 Ambient IoT. An energy-harvesting (solar) sensor ≠ a backscatter tag."
        ),
        "real_world": (
            "TR 38.848, academic backscatter, Wiliot/Qualcomm batteryless-tag trials. "
            "Inflow to a TT IoT platform is a scenario; it is not on every shelf."
        ),
        "tt_impact": (
            "Warehouse pallet, greenhouse, meter candidate. TRL 4, PoC. Erasing battery logistics is not a field measurement."
        ),
    },
}
