"""
Foundation layer — conceptual ground, native English overlay.
Jargon is allowed: expanded on first use. Expert equations live in expert_depth.
Flow: problem → need → method → mechanism → result → application.
"""

BEGINNER_COPY = {
    "isac": {
        "card": (
            "A base station carries data; it does not measure the scene. Cameras fail in fog "
            "and darkness; a separate radar wants a second spectrum and a second antenna. "
            "ISAC (Integrated Sensing and Communication) processes bits and echo on the same RF "
            "chain: delay is range, Doppler is speed. "
            "TRL 4 — Rel-19 work item (TR 22.837); laboratory validation, not a Türk Telekom field."
        ),
        "kicker": "Problem: the tower talks, it cannot see",
        "what": (
            "ISAC (Integrated Sensing and Communication) is a radio architecture that jointly "
            "designs user-plane delivery and extraction of range, speed, and angle from reflected "
            "energy — on the same carrier, the same antennas, and often the same waveform. "
            "It is not a radar box bolted beside the site."
        ),
        "why_needed": (
            "Spectrum and urban real estate are expensive. Traffic, a low-altitude drone corridor, "
            "and camera-free awareness would, as a separate radar network, grow both CAPEX and "
            "EMI (electromagnetic interference). If the network already radiates RF, using that "
            "energy for a second task is a rational operator need."
        ),
        "problem": (
            "A classical gNB (next-generation Node B — 5G/6G base station) optimises only the "
            "communications channel. Cameras fail in rain and fog; privacy is costly. Adjacent "
            "automotive or military radar injects interference. The outcome is a remaining blind "
            "spot or paying for dual infrastructure."
        ),
        "how_steps": [
            "Radiate: the gNB transmits the OFDM or OTFS frame already bound for the user; there is no radar truck.",
            "Echo: return from a vehicle, wall, or drone yields delay (range), Doppler (speed), and array phase difference as AoA (angle of arrival).",
            "Share: orthogonal time, frequency, or code aims to keep bits and echo from corrupting each other.",
            "Edge: a range/speed/angle summary goes to the edge; raw I/Q is not always hauled to the core.",
        ],
        "mental_model": (
            "One RF chain, two tasks. The outbound path is a Shannon channel; the return path is "
            "a radar equation. Power and time are split from the same budget: more energy for "
            "communication lowers echo SNR. Sensing range stays shorter than communications range "
            "because the echo decays as R⁴."
        ),
        "analogy": (
            "A monostatic radar echo chain sharing the cellular downlink carrier. "
            "Not two independent systems standing side by side."
        ),
        "analogy_technical_map": (
            "Delay τ = 2R/c is range; Doppler is speed; multi-antenna phase difference is AoA. "
            "The CRB (Cramér–Rao bound) is the theoretical floor on estimator variance; Shannon "
            "capacity shares the same P and B. Clutter and privacy sit outside the equation."
        ),
        "when_used": (
            "Where visibility fails (fog, night), cameras are unwanted, the existing site already "
            "cuts the road or corridor, and a dedicated radar band is expensive or hard to license."
        ),
        "when_not": (
            "Not for a ‘sub-centimetre everywhere’ claim — that is a literature target; this "
            "platform has no field measurement. Dense multipath and privacy rules block a public "
            "surveillance product. Narrow B keeps range resolution physically coarse."
        ),
        "not_to_confuse": (
            "A 5G site with a radar parked next to it is not ISAC; that is two systems. It is not "
            "computer vision: an RF echo is not a pixel. Ambient IoT backscatter is a cooperative "
            "tag; the ISAC target is often a non-cooperative reflector."
        ),
        "real_world": (
            "3GPP Rel-19 ISAC work item (TR 22.837), Hexa-X-II architecture reports, V2X and "
            "low-altitude drone testbeds. Not a commercial ‘every site is a radar’ product."
        ),
        "tt_impact": (
            "Fog-bound strait traffic, urban drone corridor, motion under debris: existing site "
            "geometry is the candidate. TRL 4 — laboratory; not in every subscriber neighbourhood."
        ),
        "principle_html": (
            "<p><strong>1. Radiate:</strong> the <strong>gNB</strong> (next-generation Node B) "
            "transmits the user frame. There is no separate radar hardware.</p>"
            "<p><strong>2. Echo:</strong> delay is range, <strong>Doppler</strong> is speed, "
            "array phase difference is <strong>AoA</strong> (angle of arrival).</p>"
            "<p><strong>3. Share:</strong> bits and echo are split in time/frequency/code. "
            "The same power budget feeds both tasks.</p>"
            "<p><strong>Result:</strong> a spectrum- and antenna-saving candidate. The bill is R⁴ loss and clutter.</p>"
        ),
        "arch_html": (
            "<p><strong>Layer 1 — PHY:</strong> the existing array both sends data and listens for echo. "
            "Massive MIMO phase difference supports angle estimation.</p>"
            "<p><strong>Layer 2 — MAC:</strong> resources are shared so conversation and echo do not "
            "destroy each other. That is a trade-off, not magic.</p>"
            "<p><strong>Layer 3 — Edge:</strong> a range/speed/angle summary goes to Türk Telekom edge cloud. "
            "Raw I/Q is not always hauled to the core.</p>"
            "<p>Waveform, CRB, and Rel-19 formula cards sit in the expert layer.</p>"
        ),
    },
    "ris": {
        "card": (
            "At high frequency a wave does not turn the corner; a new gNB for every blind spot is "
            "CAPEX and urban load. A RIS (Reconfigurable Intelligent Surface) is a programmable "
            "reflector on the façade: element phase θ_n steers the beam to the UE; it has no "
            "high-power transmitter of its own. TRL 5 — ETSI RIS ISG and Rel-19/20; operator-PoC "
            "class, not a Türk Telekom field."
        ),
        "kicker": "Problem: the wave cannot turn the corner",
        "what": (
            "A RIS (Reconfigurable Intelligent Surface) is a surface of hundreds or thousands of "
            "tunable elements. A PIN diode or varactor shifts the incident phase over 0–2π. "
            "The surface does not generate internet; it steers the gNB transmission toward the "
            "intended UE (user equipment)."
        ),
        "why_needed": (
            "At mmWave and above, wall and corner loss is severe. A site per blind spot is CAPEX "
            "and EMC load. A passive or semi-passive surface is a candidate to close a coverage "
            "hole at lower energy than an active relay by making the environment a controllable channel."
        ),
        "problem": (
            "At high frequency the path drops or dies without line of sight (LoS). Plaza glass, "
            "courtyards, and tunnel bends are that physics in the field. An active relay carries "
            "its own RF chain, power, and interference."
        ),
        "how_steps": [
            "Surface: façade, glass, or tunnel wall — a RIS is not a base station.",
            "Phase: each element applies θ_n; the array factor shapes the beam.",
            "Command: the gNB tells the controller the target UE; the control link is low-rate.",
            "Result: a controlled reflection path replaces the blocked direct path.",
        ],
        "mental_model": (
            "A RIS is not a transmitter; it programs a boundary condition. The channel is two hops: "
            "gNB→RIS→UE. Double-path loss applies; under ideal conditions N elements scale power "
            "as ~N². If the channel cannot be estimated, the phase table is wrong and the gain collapses."
        ),
        "analogy": (
            "A passive phased array: each element is a delay, with a shared illuminator (the gNB). "
            "It is not an active relay or a small cell."
        ),
        "analogy_technical_map": (
            "θ_n is element phase, Φ = diag(e^{jθ_n}) the surface, G the Tx–RIS channel, h_r the "
            "RIS–UE channel. The effective channel is h_rᴴ Φ G. Double-path loss is the Tx→RIS→Rx "
            "product; it does not magically extend range."
        ),
        "when_used": (
            "N-LoS streets, tunnel bends, stands, indoor mmWave, historic fabric where a tower "
            "cannot be planted. Geometry that wants lower energy and CAPEX than an active relay."
        ),
        "when_not": (
            "Gain falls if the surface cannot estimate the channel (a passive element is not a "
            "receiver) and controller delay cannot track user speed. ‘90% energy saving’ is "
            "literature/target; this platform has no field bill."
        ),
        "not_to_confuse": (
            "Not an active relay or small cell — no high-power transmitter. A metamaterial "
            "‘invisibility cloak’ claim does not cancel Maxwell; only the boundary is programmed. "
            "It can sit with ISAC; a RIS alone is not a radar."
        ),
        "real_world": (
            "ETSI RIS ISG, 3GPP Rel-19/20 work items, façade and indoor operator PoCs. "
            "Not plug-and-play commodity on every building."
        ),
        "tt_impact": (
            "Peninsula, tunnel, plaza glass: coverage without a new tower. TRL 5 — prototype in a "
            "relevant environment; not a default part of the subscriber network."
        ),
        "principle_html": (
            "<p><strong>1. Surface:</strong> a thin reflector on the façade. This is not a base station.</p>"
            "<p><strong>2. Phase:</strong> elements steer the beam to the <strong>UE</strong> via θ_n.</p>"
            "<p><strong>3. Command:</strong> the <strong>gNB</strong> names the target on a low-rate control link.</p>"
            "<p><strong>Result:</strong> a controlled reflection. The bill is channel estimation and double-path loss.</p>"
        ),
        "arch_html": (
            "<p><strong>Layer 1 — Surface:</strong> PIN/varactor elements; little or no active RF chain.</p>"
            "<p><strong>Layer 2 — Controller:</strong> FPGA/MCU writes element phase on gNB command.</p>"
            "<p><strong>Layer 3 — C-plane:</strong> site–surface control link. The surface does not generate internet.</p>"
            "<p>N² scaling and channel estimation sit on the expert formula cards.</p>"
        ),
    },
    "cell_free": {
        "card": (
            "SINR drops at the cell edge; handover carries drop risk. Cell-free Massive MIMO "
            "(Multiple-Input Multiple-Output) is a architecture in which distributed access points "
            "serve jointly, on the same frequency, with shared precoding: the edge is removed as a "
            "design object. The bill is fronthaul fibre. "
            "TRL 4 — Rel-19/20 distributed-MIMO work item; literature prototype, not a TT field."
        ),
        "kicker": "Problem: it weakens at the cell boundary",
        "what": (
            "Cell-free Massive MIMO serves the user from geographically spread access points (APs) "
            "at once, on the same frequency, with central or semi-distributed processing, instead of "
            "binding the user to one cell. The cell boundary is designed out."
        ),
        "why_needed": (
            "Capacity and fairness collapse at the edge: the wanted signal is weak, the neighbour "
            "is interference. In a stadium or terminal, load piles onto one macro. Distributed "
            "antennas shorten the path and make interference jointly processable."
        ),
        "problem": (
            "A cellular network is a pie. At the slice edge, SINR (signal-to-interference-plus-noise "
            "ratio) falls. Failed handover is a drop. One tower plus many users means one side of "
            "the stand is fed and the other is starved."
        ),
        "how_steps": [
            "Distribute: low-complexity APs on ceilings, stands, streets.",
            "Backhaul: high-rate fronthaul to a CPU/edge cloud; synchronisation is mandatory.",
            "Serve jointly: several APs apply precoding at once.",
            "Process interference: energy toward a neighbour is jointly suppressed.",
        ],
        "mental_model": (
            "There is no single cell; the user sits in a joint beam of several APs. Computation "
            "must reach a centre or a distributed cluster — without fibre, joint precoding cannot "
            "be written. Fronthaul delay and phase drift reverse the gain."
        ),
        "analogy": (
            "Coordinated multipoint (CoMP) is the ancestor; the difference is going all the way to "
            "a ‘no cell’ assumption. A small-cell forest still has cell edges."
        ),
        "analogy_technical_map": (
            "AP = distributed radio; fronthaul = eCPRI/RoF; w_mk = joint precoding; edge interference "
            "= the component to suppress. MMSE or ZF at the CPU. Sync loss eats beamforming gain."
        ),
        "when_used": (
            "High density, mobility, fairness: stadium, airport, production line, busy boulevard. "
            "Indoor spaces that do not want a macro aesthetic."
        ),
        "when_not": (
            "Fibre to every pole in sparse rural is CAPEX-nonsense; NTN or macro is more rational. "
            "5×–10× spectral gain is a literature range; this platform has no field measurement."
        ),
        "not_to_confuse": (
            "A small cell is still a cell. Classical CoMP jointly processes but keeps cell identity. "
            "Wi-Fi roaming is not several APs carrying your symbol at once."
        ),
        "real_world": (
            "Distributed-MIMO literature, 3GPP Rel-19/20 distributed-MIMO work item, vendor lab "
            "demonstrations. A stadium PoC candidate; not a city-wide product."
        ),
        "tt_impact": (
            "Airport, stadium, warehouse: the edge complaint. TRL 4. Dense venues first — fibre is expensive."
        ),
        "principle_html": (
            "<p><strong>1. Distribute:</strong> APs are placed densely; the design does not rest on one macro.</p>"
            "<p><strong>2. Serve jointly:</strong> the UE attaches to several APs at once.</p>"
            "<p><strong>3. Combine:</strong> the processor on fronthaul applies "
            "<strong>MMSE</strong> (minimum mean-square error) style precoding.</p>"
            "<p><strong>Result:</strong> the handover sensation disappears. The bill is fronthaul and compute.</p>"
        ),
        "arch_html": (
            "<p><strong>Layer 1 — AP:</strong> low-complexity radio; no heavy local compute.</p>"
            "<p><strong>Layer 2 — Fronthaul:</strong> fibre. Without sync, the joint beam breaks.</p>"
            "<p><strong>Layer 3 — CPU / edge:</strong> joint estimation and precoding.</p>"
            "<p>SINR and MMSE assumptions sit on the expert cards.</p>"
        ),
    },
    "thz": {
        "card": (
            "Sub-6 GHz and mmWave can stay narrow for intra-DC mesh and tower bridges. "
            "THz (terahertz) opens the spectrum between millimetre-wave and infrared; in Shannon, "
            "capacity grows first with B. The bill is FSPL and molecular absorption: range shrinks. "
            "TRL 3 — TR 38.807; laboratory, not a street network. 6G is not THz alone."
        ),
        "kicker": "Problem: the data pipe is still narrow",
        "what": (
            "THz communication is the attempt to open tens of GHz of bandwidth in, roughly, "
            "0.1–10 THz. Shannon: C = B log₂(1+SNR); B is the first term, SNR the second."
        ),
        "why_needed": (
            "It is a candidate for intra-DC mesh, a tower hop where fibre cannot be pulled, and "
            "later high-rate indoor use. Fibre does not reach every geometry. THz is a high-B "
            "wireless candidate at the right distance."
        ),
        "problem": (
            "As frequency rises, FSPL (free-space path loss) and water-vapour absorption grow. "
            "A hand, a leaf, or rain can cut the link. InP/GaN and ADC speed are not mature CMOS. "
            "That is why TRL is low."
        ),
        "how_steps": [
            "Spectrum: windows above 100 GHz; the target is tens of GHz of B.",
            "Loss: L(f,d) = FSPL × e^{K(f)d}; K(f) jumps on water-vapour lines.",
            "Beam: array gain offsets loss; pointing becomes critical.",
            "Geometry: rack, hall, tower hop — not a macro street.",
        ],
        "mental_model": (
            "As B grows, capacity rises near-linearly; if absorption eats SNR, the log term collapses. "
            "A narrow beam offsets loss but raises blockage probability. The right hop is short and LoS."
        ),
        "analogy": (
            "A wireless-fibre candidate: high B, short d, aligned beam. Not a macro cellular carrier."
        ),
        "analogy_technical_map": (
            "B = bandwidth; d = distance; K(f) = molecular absorption; EIRP and array gain offset loss. "
            "C = B log₂(1+SNR): tens of GHz of B dominate SNR — unless absorption drops SNR first."
        ),
        "when_used": (
            "Wireless data centre, short backhaul/fronthaul, controlled indoor, spectroscopy. "
            "Line of sight and tens to hundreds of metres."
        ),
        "when_not": (
            "Open-city macro, long rainy hops, phone-to-phone kilometres. ‘1 Tbps to every subscriber’ "
            "is marketing; this platform did not measure it. Medical nanosensors are a research "
            "horizon, not a Rel-19 commercial feature."
        ),
        "not_to_confuse": (
            "5G mmWave (28–39 GHz) is not THz. Free-space optics (laser) is a different class. "
            "ISAC may use a THz waveform; THz is not by itself a sensing standard."
        ),
        "real_world": (
            "IEEE 802.15.3d, ITU-R spectrum studies, 3GPP TR 38.807 (NR beyond 52.6 GHz), vendor "
            "sub-THz demonstrations. Not the default band in a subscriber handset."
        ),
        "tt_impact": (
            "Not handset speed in the near term; racks and tower hops where fibre cannot be pulled. "
            "TRL 3. Placement: the laboratory."
        ),
        "principle_html": (
            "<p><strong>1. Band:</strong> spectrum between mmWave and infrared opens; B grows.</p>"
            "<p><strong>2. Absorption:</strong> vapour, walls, and a hand add loss on top of FSPL.</p>"
            "<p><strong>3. Beam:</strong> a narrow beam offsets loss; range stays short.</p>"
            "<p><strong>Result:</strong> a high-B candidate in the right geometry. 6G is not THz alone.</p>"
        ),
        "arch_html": (
            "<p><strong>Layer 1 — RF front-end:</strong> GaN/InP candidates; not mature CMOS.</p>"
            "<p><strong>Layer 2 — Converter:</strong> high-speed ADC/DAC; power and heat.</p>"
            "<p><strong>Layer 3 — Geometry:</strong> short hop, aligned beam, backup LoS.</p>"
            "<p>L(f,d) and Shannon sit on the expert cards.</p>"
        ),
    },
    "ai_ran": {
        "card": (
            "A fixed RRM rule treats a packed stadium and an empty night with the same tariff. "
            "AI-RAN (artificial-intelligence-native radio access network) shifts resource on a "
            "millisecond-to-second loop from measurement. It is not a chatbot. "
            "TRL 5 — TR 38.843 and O-RAN RIC trial class; no unattended field proof."
        ),
        "kicker": "Problem: the network follows a fixed rule",
        "what": (
            "AI-native RAN is the design of parts of PHY/MAC and resource management to run on a "
            "learned model (autoencoder, reinforcement learning, prediction) instead of a fixed "
            "threshold. Practical entry today is xApps/rApps on an O-RAN RIC; making the whole "
            "air interface a neural net is the research edge."
        ),
        "why_needed": (
            "Traffic, channel, and energy change in time. A fixed tariff is late for extra time "
            "in a match and for a fault. An idle site still burns power. A learning loop meets "
            "the need for measurement-driven adaptation."
        ),
        "problem": (
            "A human cannot write RRM every second. Classical thresholds stick in local optima. "
            "Energy, capacity, and mobility compete. Without data the model invents; a black box "
            "cannot be explained to a regulator."
        ),
        "how_steps": [
            "Measure: load, SINR, PRB, energy, fault precursors.",
            "Decide: Near-RT RIC xApp (tens of ms) for beam/handover; Non-RT rApp (seconds+) for energy and prediction.",
            "Apply: policy is written to the gNB; a rollback path is part of the design.",
            "Learn: if the reward (capacity, energy, outage) is poor, the policy updates.",
        ],
        "mental_model": (
            "Closed loop: measure → policy → apply → reward. Near-RT is tens of milliseconds, "
            "Non-RT seconds+. Supervision does not disappear; a wrongly learned policy can lock "
            "the network. The GPU itself burns energy — net gain must be measured."
        ),
        "analogy": (
            "Classical SON (self-organising network) is the ancestor. The difference is the claim "
            "to push learning from RRM down (at the research edge) onto the air interface. "
            "O-RAN is an open interface; AI is the application on top of it."
        ),
        "analogy_technical_map": (
            "State s = RAN measurements; action a = RRM policy; reward r = capacity or energy. "
            "Near-RT ≈ 10 ms class (O-RAN definition). An autoencoder PHY is a separate learning layer from RRM."
        ),
        "when_used": (
            "Variable load, an energy target, predictive maintenance, a multi-vendor O-RAN trial. "
            "When measurement quality is high and a rollback procedure is defined."
        ),
        "when_not": (
            "An untrained model is not an autonomous pilot on a live network. ‘50–70% energy’ and "
            "‘zero human’ are target/marketing; this platform has no field bill."
        ),
        "not_to_confuse": (
            "The chat assistant on this platform is not AI-RAN. O-RAN ≠ AI: one is an interface, "
            "the other an application."
        ),
        "real_world": (
            "O-RAN WG2/WG10, 3GPP TR 38.843 (AI/ML for NR), AI-RAN Alliance, operator RIC PoCs. "
            "A fully neural air interface is laboratory."
        ),
        "tt_impact": (
            "Post-match resource shift, night sleep, a fault precursor. TRL 5. Human supervision stays."
        ),
        "principle_html": (
            "<p><strong>1. Measure:</strong> load, channel, energy, drops.</p>"
            "<p><strong>2. Decide:</strong> xApp/rApp on the <strong>RIC</strong> (RAN Intelligent Controller) produces policy.</p>"
            "<p><strong>3. Apply:</strong> the outcome is watched; rollback is part of the design.</p>"
            "<p><strong>Result:</strong> an adapting network. Measurement + model + supervision.</p>"
        ),
        "arch_html": (
            "<p><strong>Layer 1 — Measurement / PHY:</strong> classical signal processing, or neural PHY at the research edge.</p>"
            "<p><strong>Layer 2 — RIC:</strong> Near-RT xApp, Non-RT rApp. <strong>O-RAN</strong> carries this layer.</p>"
            "<p><strong>Layer 3 — Accelerator:</strong> NPU/GPU may sit beside the gNB; net energy gain must be computed.</p>"
            "<p>Loss functions and Q-learning sit on the expert cards.</p>"
        ),
    },
    "ntn": {
        "card": (
            "A terrestrial gNB covers the city and the asphalt; mountain, sea, and rubble stay empty. "
            "An NTN (non-terrestrial network) joins LEO and HAPS nodes to the core with Rel-17+ "
            "procedures. The bill is delay and Doppler. "
            "TRL 6 — TR 38.811; public Direct-to-Cell trials. Complements the urban site; does not rival it."
        ),
        "kicker": "Problem: the tower does not reach everywhere",
        "what": (
            "NTN is the architecture that joins LEO (low Earth orbit), GEO, and HAPS "
            "(high-altitude platform station) nodes to the terrestrial core with 3GPP Rel-17+. "
            "Direct-to-cell: a standard UE seeing a satellite cell, not a dedicated dish."
        ),
        "why_needed": (
            "Coverage is wherever towers and fibre reach. Rural CAPEX, sea, aviation, and disaster "
            "(when the site falls) break the terrestrial model. The need is to close the gap with "
            "the same identity and number."
        ),
        "problem": (
            "Distance grows FSPL; LEO at ~7.5 km/s produces Doppler and frequent handover. "
            "GEO delay makes speech hard. Spectrum, gateway, and regulation are operator work."
        ),
        "how_steps": [
            "Priority: gNB in the city; satellite/HAPS cell in the gap.",
            "Gateway: feeder link → gateway → core.",
            "Compensate: Doppler and delay pre-correction in PHY; otherwise PRACH will not hold.",
            "Service class: emergency SMS/voice first; not a terabit urban experience claim.",
        ],
        "mental_model": (
            "Terrestrial is the primary path; NTN closes the coverage hole. Delay is ~d/c "
            "(LEO tens of ms, GEO round-trip ~250 ms class, literature). Direct-to-cell is the "
            "handset antenna fitting the link budget — not a VSAT dish."
        ),
        "analogy": (
            "The same 3GPP identity, a different radio geometry. Consumer LEO broadband "
            "(e.g. Starlink) need not be the same product as an NTN cell."
        ),
        "analogy_technical_map": (
            "Feeder link + core = the ground side. Doppler f_d = f_c (v/c) cosθ. "
            "Link budget is FSPL + atmosphere + antenna gain. The Rel-17 NTN specification "
            "(TR 38.811) is the frame."
        ),
        "when_used": (
            "Rural, mountain, sea, aviation, disaster backup, tower-less IoT. Where terrestrial is uneconomic."
        ),
        "when_not": (
            "Not the primary path for urban capacity or sub-millisecond URLLC. "
            "‘100% global, zero gap’ is marketing. This platform did not measure satellite delay in the field."
        ),
        "not_to_confuse": (
            "A VSAT dish ≠ Direct-to-Cell. HAPS is not a satellite (stratosphere). "
            "ISAC ‘making the sky a radar’ is not NTN."
        ),
        "real_world": (
            "3GPP TR 38.811, Rel-17/18 NTN work item, public Direct-to-Cell trials. "
            "A disaster backup path is operator strategy, not a field guarantee."
        ),
        "tt_impact": (
            "Disaster path, fleet, rural. TRL 6 — the most mature of the seven. A complement."
        ),
        "principle_html": (
            "<p><strong>1. Priority:</strong> the city stays on towers. Empty geography uses <strong>LEO</strong> / <strong>HAPS</strong>.</p>"
            "<p><strong>2. Identity:</strong> the target is a 3GPP UE seeing the satellite cell.</p>"
            "<p><strong>3. Compensate:</strong> PHY corrects Doppler and delay; it is not a promise of terrestrial-class latency.</p>"
            "<p><strong>Result:</strong> the coverage hole closes. Complement, not rival.</p>"
        ),
        "arch_html": (
            "<p><strong>Layer 1 — Space/air:</strong> LEO constellation, HAPS on demand.</p>"
            "<p><strong>Layer 2 — Gateway:</strong> feeder link → Türk Telekom gateway → core.</p>"
            "<p><strong>Layer 3 — UE:</strong> Rel-17+ NTN modem; not every legacy device is guaranteed.</p>"
            "<p>Doppler and FSPL sit on the expert cards.</p>"
        ),
    },
    "ambient_iot": {
        "card": (
            "Replacing batteries at carton and greenhouse scale is uneconomic. Ambient IoT harvests "
            "ambient RF and reports a short identity by backscatter; it does not carry video. "
            "TRL 4 — TR 38.848; PoC class, not a shelf product."
        ),
        "kicker": "Problem: you cannot replace the battery on every object",
        "what": (
            "Ambient IoT is the class of tags with no battery, or a very small one, that harvest "
            "ambient RF (site, Wi-Fi, a helper illuminator) and send a short status, mostly by "
            "backscatter. The aim is cheap, sparse tracking."
        ),
        "why_needed": (
            "Battery logistics do not scale for cartons, greenhouses, and meters. NB-IoT and "
            "RedCap still want an energy source. A batteryless tag is the need to solve "
            "‘where / how many degrees’ without a maintenance crew."
        ),
        "problem": (
            "Reflected power is weak; range is short and bit-rate low. Ambient energy is not "
            "guaranteed. The reader must be sensitive and the protocol narrow. It does not replace a phone."
        ),
        "how_steps": [
            "Harvest: a rectenna converts RF to DC.",
            "Reflect: antenna impedance modulates the incoming carrier; there is no PA of its own.",
            "Read: a nearby gNB or reader separates the weak echo plus the bit.",
            "Write: ‘carton 14, 4 °C’ — no video.",
        ],
        "mental_model": (
            "Friis harvest × backscatter efficiency = a readable bit. In an RF-weak pocket the tag "
            "falls silent. RFID is the ancestor; the difference is a 3GPP cellular reader and an addressing target."
        ),
        "analogy": (
            "Passive RFID moved onto a cellular reader. An energy-harvesting (solar+battery) sensor is a different class."
        ),
        "analogy_technical_map": (
            "Rectenna efficiency η; incident power P_tx G_tx (λ/4πd)²; backscatter bit b(t). "
            "3GPP TR 38.848 is a Rel-19 work item, not a product on the shelf."
        ),
        "when_used": (
            "Pallet, cold chain, greenhouse, meter, structural health — short range, sparse, low bit-rate, long life."
        ),
        "when_not": (
            "Audio, video, kilometre range, moving-vehicle telemetry. ‘One cent, a trillion objects’ "
            "is target/marketing. In an RF-free corner the tag dies."
        ),
        "not_to_confuse": (
            "Shop-door RFID is the ancestor; a cellular multi-reader scenario is different. "
            "ISAC measures a non-cooperative echo; Ambient IoT is a cooperative tag."
        ),
        "real_world": (
            "3GPP TR 38.848, academic backscatter, commercial batteryless-tag trials. "
            "Inflow to a TT IoT platform is a scenario; it is not on every shelf."
        ),
        "tt_impact": (
            "Warehouse pallet, greenhouse, meter. TRL 4. It does not replace your phone."
        ),
        "principle_html": (
            "<p><strong>1. Harvest:</strong> a rectenna converts an RF scrap to DC.</p>"
            "<p><strong>2. Reflect:</strong> there is no PA; the incoming carrier is modulated. Range is short.</p>"
            "<p><strong>3. Read:</strong> a nearby reader separates the weak echo and writes to the cloud.</p>"
            "<p><strong>Result:</strong> cheap, batteryless, sparse tracking. It does not carry video.</p>"
        ),
        "arch_html": (
            "<p><strong>Layer 1 — Tag:</strong> ASIC + micro-capacitor + rectenna.</p>"
            "<p><strong>Layer 2 — Reader:</strong> gNB or helper illuminator; high sensitivity.</p>"
            "<p><strong>Layer 3 — Rel-19 / IoT cloud:</strong> narrow addressing, TT IoT platform.</p>"
            "<p>Friis harvest sits on the expert cards.</p>"
        ),
    },
}
