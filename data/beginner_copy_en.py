"""
Foundation layer — conceptual ground, native English overlay.
Jargon is allowed: expanded on first use. Expert equations live in technologies + expert_depth.
Each technology: what, why, problem, how, mental model, analogy→technical map,
when / when not, not to confuse, real world, Türk Telekom impact.
"""

BEGINNER_COPY = {
    "isac": {
        "card": (
            "On a fog-bound strait a tower can deliver internet, but it cannot answer "
            "whether a ship is out there; cameras go blind, and a separate radar truck is "
            "both expensive and pollutes the spectrum. "
            "Integrated Sensing and Communication (ISAC) counts the same radio wave as both "
            "conversation and echo: delay is range, Doppler shift is speed. "
            "For Türk Telekom this is a candidacy, not a neighbourhood product. "
            "Technology Readiness Level (TRL) 4 — laboratory-validated, not a live field network."
        ),
        "kicker": "Problem: the tower talks, it does not look",
        "what": (
            "Integrated Sensing and Communication (ISAC) is a radio architecture that jointly "
            "designs bit delivery to the user and extraction of range, speed, and angle from the "
            "environment — on the same frequency resource, the same antennas, and often the same "
            "waveform. It is not bolting on a separate “radar box”; it is treating the reflection "
            "of the communications wave as information as well."
        ),
        "why_needed": (
            "Spectrum and urban real estate are expensive. Traffic safety, a low-altitude drone "
            "corridor, and camera-free awareness would, if they required a separate radar network, "
            "grow both cost and electromagnetic interference (EMI). If the network is already "
            "pushing Radio Frequency (RF) energy everywhere, using that same energy as a second "
            "sense is a rational operator need."
        ),
        "problem": (
            "A classical base station carries data; it does not “see” the environment. Cameras go "
            "blind in fog, rain, and darkness, and privacy is costly too. Separate automotive or "
            "military radar produces adjacent-channel interference into the network spectrum. "
            "The outcome is either a remaining blind spot or paying for dual infrastructure."
        ),
        "how_steps": [
            "Transmit: the next-generation Node B (gNB) — the 5G/6G base station — radiates the Orthogonal Frequency-Division Multiplexing (OFDM) or Orthogonal Time Frequency Space (OTFS) waveform already bound for the user; there is no extra truck.",
            "Listen: echo returning from a vehicle, wall, or drone yields delay (range), Doppler (speed), and array phase difference as Angle of Arrival (AoA).",
            "Separate: orthogonal sharing in time, frequency, or code aims to keep conversation bits and the echo from corrupting each other.",
            "Forward: a point cloud or track summary goes to the edge server (traffic, Unmanned Traffic Management (UTM), debris/collapse scenarios).",
        ],
        "mental_model": (
            "Build the picture in your mind this way: the tower is not a flashlight; it is a bat — "
            "it both shouts and listens. The same “voice” reaches your ear (data) and returns from "
            "a wall to tell the tower the range. This is not two mouths; it is one mouth and two ears."
        ),
        "analogy": (
            "A bat does not see in the dark with eyes; it sees by the return of sound. An ISAC "
            "tower likewise transmits and listens to the echo — while continuing to talk to you "
            "at the same time."
        ),
        "analogy_technical_map": (
            "The technical mapping: RF carrier instead of ultrasound; “delay = 2R/c” is radar "
            "range; “shift of the sound” is Doppler shift; the “pair of ears” is multi-antenna "
            "AoA estimation. A bat is single-purpose; in ISAC, communications capacity and the "
            "sensing Cramér–Rao Bound (CRB) share the same power budget."
        ),
        "when_used": (
            "In scenarios where visibility fails (fog, night) and you do not want cameras (privacy); "
            "where existing tower geometry already overlooks a road, strait, or air corridor; "
            "on operator networks where a separate radar spectrum is expensive or politically difficult."
        ),
        "when_not": (
            "Not for a sub-centimetre “always, in every neighbourhood” promise — that is a literature "
            "target; this platform has no field measurement. Until dense multipath clutter and privacy "
            "regulation are resolved, it should not be presented as a public-surveillance product. "
            "Without bandwidth as wide as terahertz (THz), range resolution remains physically limited."
        ),
        "not_to_confuse": (
            "A classical radar plus a 5G tower placed beside it is not ISAC; that is two systems. "
            "It is also not camera-based computer vision: an RF echo does not produce image pixels. "
            "Ambient IoT backscatter is different as well: there a batteryless tag speaks on purpose; "
            "in ISAC the target is usually a non-cooperative reflector."
        ),
        "real_world": (
            "It appears in automotive Vehicle-to-Everything (V2X) research testbeds, low-altitude "
            "drone-management studies, the 3GPP Rel-19 ISAC work item, and European Hexa-X-II "
            "architecture reports. It is not a commercial “every tower is a radar” product."
        ),
        "tt_impact": (
            "Maritime traffic in strait fog, an urban drone corridor, motion under debris: candidacy "
            "on the existing tower grid. TRL 4: laboratory and early field; not in every subscriber "
            "neighbourhood."
        ),
        "principle_html": (
            "<p><strong>1. Transmit:</strong> "
            "The <strong>gNB</strong> (next-generation Node B, the 5G/6G base station) radiates the "
            "radio frame bound for the user. There is no new radar truck.</p>"
            "<p><strong>2. Listen:</strong> The signal bounces off a vehicle, wall, or drone. Delay is range, "
            "<strong>Doppler</strong> shift is speed, array phase difference is <strong>AoA</strong> "
            "(Angle of Arrival).</p>"
            "<p><strong>3. Separate:</strong> Software tries to keep your bits and the echo apart in "
            "time, frequency, or code. One is internet; the other is a map.</p>"
            "<p><strong>Result:</strong> One RF chain, two jobs. For the operator, a candidacy to save "
            "spectrum and antennas; for the city, awareness without planting cameras. The trade-off: "
            "the same power budget funds both bits and echo.</p>"
        ),
        "arch_html": (
            "<p><strong>Layer 1 — Radio and antennas (PHY):</strong> The existing base station both "
            "sends data and listens for echo. A massive Multiple-Input Multiple-Output (MIMO) array supplies phase difference for "
            "angle estimation.</p>"
            "<p><strong>Layer 2 — Resource sharing (MAC):</strong> Time, frequency, or code is partitioned "
            "so conversation and echo do not corrupt each other. This is not magic; it is a trade-off.</p>"
            "<p><strong>Layer 3 — Edge processing:</strong> A range/speed/angle summary goes to the "
            "Türk Telekom edge cloud (traffic, drones, debris). Raw I/Q is not always hauled to the "
            "core; the bandwidth is expensive.</p>"
            "<p>Waveform (OFDM/OTFS), CRB, and 3GPP Rel-19 sit in the expert layer on this page, "
            "in the formula cards.</p>"
        ),
    },
    "ris": {
        "card": (
            "At higher frequencies a wave tends to travel in a straight line; it does not turn the "
            "corner, and it dies in an elevator shaft. Building a new tower for every blind spot "
            "does not scale. "
            "A Reconfigurable Intelligent Surface (RIS) is an electronic mirror hung on a façade: "
            "each small element shifts phase, and the beam turns toward you. "
            "Because it is not a transmitter in its own right, it consumes only a scrap of energy. "
            "Technology Readiness Level (TRL) 5 — prototype / field trial, not a commercial tower."
        ),
        "kicker": "Problem: the signal cannot turn the corner",
        "what": (
            "A RIS is a surface of hundreds or thousands of tunable reflecting elements. "
            "The elements, switched by a PIN diode, varactor, or similar device, shift the phase of "
            "the incident wave over a 0–2π range. The surface does not generate internet on its own; "
            "it steers the existing gNB’s transmission toward the intended User Equipment (UE)."
        ),
        "why_needed": (
            "In millimetre-wave (mmWave) and higher bands, wall and corner loss is severe. A tower "
            "at every blind spot is a load on capital expenditure (CAPEX), urban aesthetics, and "
            "electromagnetic compatibility (EMC). A passive or semi-passive surface is the promise "
            "of closing a coverage hole cheaply by turning the path into an “intelligent environment.”"
        ),
        "problem": (
            "At high frequency a radio wave behaves like light: without line of sight (LoS), rate "
            "drops or the link breaks. Plaza glass, a courtyard, a tunnel bend — that is the physics "
            "behind “no coverage.” A relay (active repeater) brings its own RF chain, power, and "
            "interference."
        ),
        "how_steps": [
            "Place the surface: façade, glass, or tunnel wall — the surface is not a base station in its own right.",
            "Set the phase: each element applies a small phase shift; together they shape a beam (steering beyond Snell’s law).",
            "The tower commands: the gNB tells the RIS controller “look at this user”; the control link is thin and low-power.",
            "Result: a controlled reflection path forms in place of the blocked direct path.",
        ],
        "mental_model": (
            "Build the picture in your mind this way: in a dark corridor a flashlight cannot turn "
            "the corner. An adjustable mirror carries the light into the room. The mirror is not "
            "the lamp; it steers the lamp’s light. A RIS is not a transmitter either; it is a "
            "programmable reflector."
        ),
        "analogy": (
            "In a dark room a flashlight cannot light the far side of a wall. A mirror whose angle "
            "you set bends the light into the unseen room. A RIS is that adjustable mirror for radio."
        ),
        "analogy_technical_map": (
            "The technical mapping: “mirror angle” is each element’s phase θ_n; the “focused beam” "
            "is the array factor; the “lamp” is the Tx–RIS channel G; the “room” is the RIS–Rx "
            "channel h_r. A mirror attenuates light: cascaded path loss (Tx→RIS→Rx) is in force. "
            "With N elements acting together, under ideal conditions power scales as ~N²."
        ),
        "when_used": (
            "A non-line-of-sight (NLoS) street, a tunnel bend, a stadium stand, indoor mmWave in a "
            "plaza, a historic fabric where a tower cannot be sited. Places where energy and CAPEX "
            "are expected to stay below those of an active relay."
        ),
        "when_not": (
            "Expected gain falls where the surface cannot estimate the channel (a passive element "
            "is not a receiver) and where controller latency cannot keep up with user speed. "
            "Cascaded path loss means “stick a RIS everywhere instead of a tower” does not magically "
            "extend range. A 90% energy saving is a literature/target comparison; this platform has "
            "not measured a field energy bill."
        ),
        "not_to_confuse": (
            "It is not an active relay or a small cell — it has no high-power transmitter of its own. "
            "It is also not metamaterial “invisibility cloak” marketing; Maxwell’s laws still hold, "
            "only the boundary condition is programmed. It can be used together with ISAC, but a RIS "
            "alone is not a radar."
        ),
        "real_world": (
            "ETSI RIS Industry Specification Group (ISG), 3GPP Rel-19/20 work items, operator "
            "proofs of concept (PoC) (façade and indoor panels). Plug-and-play commercial commodity "
            "is not yet on every building."
        ),
        "tt_impact": (
            "Historic peninsula, tunnels, plaza glass: a coverage candidate without raising a tower. "
            "TRL 5 — prototype in a relevant environment; not a default part of the subscriber network."
        ),
        "principle_html": (
            "<p><strong>1. Hang the surface:</strong> A thin electronic reflector is applied to a building, "
            "glass, or wall. This is not a base station.</p>"
            "<p><strong>2. Shift the phase:</strong> Each small element changes the phase of the incident wave. "
            "Together they steer the beam toward your <strong>UE</strong>.</p>"
            "<p><strong>3. Tie it to the tower:</strong> The <strong>gNB</strong> tells the controller "
            "“look at this user.” The control link is thin and low-power.</p>"
            "<p><strong>Result:</strong> Directed reflection instead of a new tower. The blind spot closes; "
            "the price is channel estimation and cascaded path loss.</p>"
        ),
        "arch_html": (
            "<p><strong>Layer 1 — Surface:</strong> PIN/varactor elements on PCB or flexible film. "
            "There is no active RF chain, or only a very small one.</p>"
            "<p><strong>Layer 2 — Controller:</strong> An FPGA/microcontroller changes element voltages "
            "on the gNB’s command.</p>"
            "<p><strong>Layer 3 — Control link:</strong> A low-bit-rate C-plane between tower and surface. "
            "The surface does not generate “internet on its own.”</p>"
            "<p>Metamaterial, N² scaling, and the channel-estimation difficulty sit in the expert "
            "formula cards.</p>"
        ),
    },
    "cell_free": {
        "card": (
            "In a classical network every neighbourhood has a cell; as you approach the edge the "
            "signal drops, and when the serving tower changes (handover) you risk a drop. "
            "Cell-free Massive MIMO removes that boundary: access points as dense as street lamps "
            "carry you jointly, so there is no longer an “edge.” "
            "The bill is the fronthaul fibre that ties the antennas back to the centre. "
            "Technology Readiness Level (TRL) 4 — experimental; stadium and airport are the first candidates."
        ),
        "kicker": "Problem: drops at the cell edge",
        "what": (
            "Cell-free Massive MIMO (Multiple-Input Multiple-Output) is an architecture in which "
            "the user is not bound to a single cell. Many geographically distributed access points "
            "(APs) serve that user at the same time, on the same frequency, with central or "
            "semi-distributed processing. The cell boundary disappears as a design objective."
        ),
        "why_needed": (
            "Capacity and fairness collapse at the cell edge: your signal is weak, and the neighbour "
            "tower is interference. In a stadium or terminal everyone piles onto the same macro tower. "
            "Distributed antennas both shorten the path and give a way to turn interference into "
            "useful signal through cooperation."
        ),
        "problem": (
            "Cellular is a pie sliced into cells. At the slice edge, Signal-to-Interference-plus-Noise "
            "Ratio (SINR) falls. A walking subscriber performs handover; failure is a drop. "
            "One tower plus many users means one side of the stand is starved and the other is full."
        ),
        "how_steps": [
            "Distribute: low-complexity APs on ceilings, stands, streets — a macro tower does not carry the load alone.",
            "Connect: APs reach a central processing unit (CPU) / edge cloud over high-speed fronthaul; synchronisation is mandatory.",
            "Serve jointly: several APs apply precoding for you at the same time.",
            "Process the interference: energy headed for a neighbour user is suppressed, or turned to benefit, through cooperation.",
        ],
        "mental_model": (
            "Build the picture in your mind this way: with a single spotlight the edge of the stage "
            "stays dark. If many small lamps follow the actor together at every step, no shadow forms. "
            "The lamps are not separate “cells”; they are one lighting system."
        ),
        "analogy": (
            "A single spotlight leaves the edge dark. If many small lamps follow the actor together, "
            "no shadow forms. Cell-free MIMO is that lamp network."
        ),
        "analogy_technical_map": (
            "The technical mapping: lamp = AP; cable = fronthaul; joint tracking = joint precoding "
            "w_mk; shadow = cell-edge interference; “one system” = a Minimum Mean Square Error (MMSE) or zero-forcing (ZF) "
            "matrix at the CPU. Without fibre the lamp network is blind — computation has to reach "
            "the centre or a distributed cluster."
        ),
        "when_used": (
            "High user density, mobility, and a fairness need: stadium, airport, a line-production "
            "floor, a dense boulevard. Indoor spaces where a macro tower’s aesthetics are unwanted."
        ),
        "when_not": (
            "In sparse rural terrain, pulling fibre to every pole is CAPEX-nonsensical; NTN or macro "
            "4G/5G is more rational. If fronthaul latency and synchronisation break down, the "
            "“cell-free” gain reverses. A 5×–10× spectral-efficiency gain is a literature range; "
            "this platform has no field measurement."
        ),
        "not_to_confuse": (
            "It is not a forest of small cells: a small cell is still a cell, and it still has an edge. "
            "Classical Coordinated Multi-Point (CoMP) is an ancestor of cell-free MIMO but does not "
            "go as far as a “no cell” assumption. It is also not Wi-Fi roaming: here many APs carry "
            "your symbol at the same time."
        ),
        "real_world": (
            "Academic core (distributed MIMO literature), 3GPP distributed-MIMO working groups, "
            "vendor laboratory demonstrations. An operator stadium PoC candidate; not a city-wide product."
        ),
        "tt_impact": (
            "An airport walk, a stadium, an industrial warehouse: the edge complaint is the target. "
            "TRL 4. Dense venues first, because fibre is expensive."
        ),
        "principle_html": (
            "<p><strong>1. Distribute:</strong> Small access points are placed densely on the street, "
            "ceiling, and stand. You do not bet on a single giant tower.</p>"
            "<p><strong>2. Serve jointly:</strong> Your phone attaches to several APs at once. "
            "All of them speak for you.</p>"
            "<p><strong>3. Combine at the centre:</strong> A processor tied by fibre fronthaul uses "
            "<strong>MMSE</strong> (Minimum Mean Square Error) "
            "precoding to set what each AP will say.</p>"
            "<p><strong>Result:</strong> The “the tower changed” feeling while you walk disappears. "
            "Fairness rises; the bill is fronthaul and compute load.</p>"
        ),
        "arch_html": (
            "<p><strong>Layer 1 — Distributed APs:</strong> Low-complexity radios; local Tx/Rx, no heavy compute.</p>"
            "<p><strong>Layer 2 — Fronthaul:</strong> Fibre (eCPRI / Radio over Fibre). Without synchronisation, "
            "the joint beam collapses.</p>"
            "<p><strong>Layer 3 — CPU / edge cloud:</strong> Joint estimation and precoding. "
            "The cell-edge notion is removed by design.</p>"
            "<p>The SINR formula and MMSE assumptions sit in the expert cards.</p>"
        ),
    },
    "thz": {
        "card": (
            "5G is fast, but the wireless pipe is still narrow; inter-rack terabit or a real-time "
            "hologram will not fit down it. Terahertz (THz) is the spectrum between millimetre-wave "
            "and infrared; bandwidth explodes. The bill is physics: water vapour absorbs, walls cut, "
            "range shrinks. Technology Readiness Level (TRL) 3 — the laboratory is strong, the street network is not. "
            "6G is not THz in its entirety."
        ),
        "kicker": "Problem: the wireless pipe is still narrow",
        "what": (
            "THz communications is the attempt to open tens of GHz of bandwidth by using the "
            "spectrum that sits, roughly, in the 0.1–10 THz slice (hundreds of GHz and above), "
            "between millimetre-wave and optics. Shannon: capacity grows first with bandwidth B; "
            "SNR is the second term."
        ),
        "why_needed": (
            "Sub-6 GHz and even mmWave can stay too narrow for intra-datacentre mesh, ultra backhaul "
            "between towers, and, later, holographic / AR-VR bit rates. Fibre cannot be pulled to "
            "every rack aisle and every hilltop. THz is a “wireless fibre” candidate — at the right "
            "distance."
        ),
        "problem": (
            "As frequency rises, Free-Space Path Loss (FSPL) and molecular absorption grow. A hand, "
            "a leaf, or rain can break the link. Hardware (indium phosphide (InP), gallium nitride "
            "(GaN), analog-to-digital converter (ADC) speed) is expensive and is not mature. "
            "That is why TRL is low."
        ),
        "how_steps": [
            "Open the spectrum: windows above 100 GHz; the target is tens of GHz of B.",
            "Accept the loss: L(f,d) = FSPL × e^{K(f)d}; K(f) jumps on water-vapour lines.",
            "Narrow the beam: array gain offsets loss; alignment becomes exacting.",
            "Pick a short-range job: rack, hall, tower hop — not a city street.",
        ],
        "mental_model": (
            "Build the picture in your mind this way: you cannot fill a pool with a thin garden hose. "
            "THz is a fire hose — but the hose is short, and a leaf can close the nozzle. That is not "
            "a software bug; it is electromagnetics."
        ),
        "analogy": (
            "Thin hose / fire hose: THz carries a great deal of data, and it is short and fragile. "
            "It wants line of sight and dry air."
        ),
        "analogy_technical_map": (
            "The technical mapping: hose cross-section = bandwidth B; hose length = d; "
            "leaf = blockage; water vapour = K(f) absorption; pressure = Equivalent Isotropically "
            "Radiated Power (EIRP) and array gain. Shannon’s C = B log2(1+SNR) says making B 50 GHz "
            "is far more effective than logarithmic SNR — and if absorption eats the SNR, B alone "
            "is not enough."
        ),
        "when_used": (
            "Wireless datacentre, short-range backhaul/fronthaul, laboratory spectroscopy, "
            "controlled indoor space. Where line of sight can be provided and distance is tens to "
            "hundreds of metres."
        ),
        "when_not": (
            "An open-city macro, a long rainy hop, pocket-to-pocket kilometres. “1 Tbps to every "
            "subscriber” is a marketing sentence; it was not measured on this platform, and physics "
            "caps the range. The medical nanosensor promise is a research horizon, not a Rel-19 "
            "commercial feature."
        ),
        "not_to_confuse": (
            "5G mmWave (the 28–39 GHz band) is not THz; it is the lower neighbour. Free-space optics "
            "(laser) is different as well: THz is still close to the electronics/RF side. An ISAC "
            "waveform can use THz, but THz by itself is not a sensing standard."
        ),
        "real_world": (
            "IEEE 802.15.3d, ITU-R spectrum studies, 3GPP “NR beyond 52.6 GHz” reports, vendor "
            "sub-THz demonstrations (e.g. 140 GHz). Not a default band in a subscriber handset."
        ),
        "tt_impact": (
            "In the near term, not pocket speed; datacentre racks and a tower hop where fibre cannot "
            "be pulled. TRL 3. Honest placement: the laboratory."
        ),
        "principle_html": (
            "<p><strong>1. Speak at a higher pitch:</strong> The band between mmWave and infrared opens. "
            "Bandwidth grows, and more bits fit.</p>"
            "<p><strong>2. Accept the obstruction:</strong> Water vapour, a wall, a hand can cut the signal. "
            "That is a physics rule.</p>"
            "<p><strong>3. Use a narrow beam:</strong> To offset loss the beam is held as tight as a flashlight. "
            "Range stays short.</p>"
            "<p><strong>Result:</strong> In the right place (rack, hall, tower hop) a record-rate candidate; "
            "in the wrong place, useless. 6G is not THz alone.</p>"
        ),
        "arch_html": (
            "<p><strong>Layer 1 — RF front end:</strong> GaN/InP/graphene candidates, on-chip antenna. Not mature CMOS.</p>"
            "<p><strong>Layer 2 — Converter:</strong> Very high-speed ADC/DAC; power and heat are the problem.</p>"
            "<p><strong>Layer 3 — Usage geometry:</strong> Short hop, aligned beam, a spare line of sight.</p>"
            "<p>The L(f,d) and Shannon cards sit in the expert layer.</p>"
        ),
    },
    "ai_ran": {
        "card": (
            "A classical network recites the engineer’s tariff from memory: when a packed stadium "
            "and a deserted night share the same rule, you either waste resource or lose quality. "
            "An Artificial Intelligence–managed Radio Access Network (AI-RAN) measures the tower "
            "and shifts resource on a millisecond-to-second loop. It is not a chatbot. "
            "Technology Readiness Level (TRL) 5 — O-RAN RIC trials exist; “no human in the loop” is not field-proven."
        ),
        "kicker": "Problem: the network recites a memorised rule",
        "what": (
            "An AI-native RAN is the design of parts of PHY/MAC and resource management to run on "
            "learned models (autoencoder, reinforcement learning, prediction) instead of a fixed "
            "formula. In practice today most of the work starts with xApps/rApps on an O-RAN RAN "
            "Intelligent Controller (RIC); making the entire air interface a neural network is the "
            "research edge."
        ),
        "why_needed": (
            "Traffic, channel, and energy change with time. A fixed tariff is late to extra time in "
            "a match, to a concert emptying, to an earthquake. An idle tower still eats electricity. "
            "Faults are often visible only after they have happened. A learning loop meets the need "
            "for measurement-based adaptation."
        ),
        "problem": (
            "A human cannot write Radio Resource Management (RRM) every second. Classical threshold "
            "rules get stuck in a local optimum. Energy, capacity, and mobility pull at once. "
            "Without data the model fabricates; a black box cannot be explained to the regulator."
        ),
        "how_steps": [
            "Measure: load, SINR, Physical Resource Block (PRB) use, energy, fault precursors.",
            "Decide: Near-Real-Time RIC xApp (tens of ms) for beam/handover; Non-Real-Time rApp (seconds+) for energy and prediction.",
            "Apply: the policy is written to the gNB. Oversight does not switch off; a rollback path is required.",
            "Learn: if the reward (capacity, energy, outage) is poor, the policy is updated.",
        ],
        "mental_model": (
            "Build the picture in your mind this way: a fixed-time traffic light versus a light that "
            "sees the queue. AI-RAN is the second. The light does not “think”; it measures, applies "
            "a rule or a model, and watches the outcome. A light that learns wrongly can lock the "
            "junction — that is why engineer oversight is a design part."
        ),
        "analogy": (
            "Fixed traffic light / a light that sees the junction. AI-RAN extends green when the "
            "queue grows, and shortens an empty phase at night when nobody is there."
        ),
        "analogy_technical_map": (
            "The technical mapping: camera = RAN measurements; light programme = RRM policy; "
            "Near-RT = the junction’s instant loop (~10 ms order, O-RAN definition); Non-RT = the "
            "city’s night plan. In Q-learning, “extend green” is an action (a), queue is state s, "
            "reward r is capacity or energy. An autoencoder PHY is not the junction; it is learning "
            "how the horn is sounded — that is, the modulation itself."
        ),
        "when_used": (
            "Variable load (stadium, evening peak), an energy target, predictive maintenance, "
            "multi-vendor O-RAN trials. When measurement quality is high and a rollback procedure "
            "is defined."
        ),
        "when_not": (
            "You do not call an untrained model an “autonomous pilot” on a live network. A black-box "
            "decision is risky under regulator oversight. “50–70% energy” and “zero humans” claims "
            "are target/marketing; this platform has no field energy bill. The GPU itself eats "
            "energy — net gain must be measured."
        ),
        "not_to_confuse": (
            "The chat assistant on this page is not AI-RAN. Self-organizing network (SON) is an "
            "ancestor, but AI-native carries the claim of pushing learning down as far as the air "
            "interface. O-RAN is an open interface; AI is an application that runs on top of it — "
            "the two are not identical."
        ),
        "real_world": (
            "O-RAN WG2/WG10, 3GPP TR 38.843 (AI/ML for NR), AI-RAN Alliance. "
            "Operator RIC PoCs. A fully neural air interface is laboratory."
        ),
        "tt_impact": (
            "Post-match resource shift, night sleep, a fault precursor. TRL 5. "
            "Human oversight does not switch off."
        ),
        "principle_html": (
            "<p><strong>1. Measure:</strong> The tower reads load, heat, drops, and the channel.</p>"
            "<p><strong>2. Decide:</strong> On the <strong>RIC</strong> (RAN Intelligent Controller) "
            "an xApp/rApp says “shift capacity / sleep / warn.”</p>"
            "<p><strong>3. Apply and learn:</strong> If the outcome is good, the policy stays. "
            "A human rollback path is a design part, against black-box risk.</p>"
            "<p><strong>Result:</strong> The network adapts. Not magic; measurement + model + oversight.</p>"
        ),
        "arch_html": (
            "<p><strong>Layer 1 — Measurement and PHY:</strong> Classical signal processing, or neural PHY at the research edge.</p>"
            "<p><strong>Layer 2 — RIC:</strong> Near-RT xApp (fast), Non-RT rApp (slow / energy / prediction). "
            "<strong>O-RAN</strong> open interfaces carry this layer.</p>"
            "<p><strong>Layer 3 — Accelerator:</strong> An NPU/GPU may sit beside the gNB. Energy gain must be computed net.</p>"
            "<p>The loss function and Q-learning sit in the expert cards.</p>"
        ),
    },
    "ntn": {
        "card": (
            "Terrestrial towers cover the city and the asphalt; mountain, open sea, and debris "
            "fields stay empty. A Non-Terrestrial Network (NTN) joins Low Earth Orbit (LEO) "
            "satellites and High-Altitude Platform Stations (HAPS) to the 3GPP network: a standard "
            "phone falls back to the sky when there is no tower. The bill is latency and Doppler. "
            "Technology Readiness Level (TRL) 6 — the most mature of the seven; not a rival to urban 6G, a complement."
        ),
        "kicker": "Problem: the tower cannot reach everywhere",
        "what": (
            "NTN is the architecture that ties LEO, Geostationary Earth Orbit (GEO), and HAPS nodes "
            "into the terrestrial core with 3GPP Rel-17+ procedures. "
            "Direct-to-Cell: a standard UE seeing satellite cells, instead of a dedicated satellite phone."
        ),
        "why_needed": (
            "Coverage is only as far as tower and fibre reach. Rural CAPEX, the sea, aviation, and "
            "disaster (when the tower has fallen) break the terrestrial model. Satellite answers the "
            "need to close the gap with the same identity and number."
        ),
        "problem": (
            "Distance grows FSPL; LEO motion at ~7.5 km/s produces Doppler and frequent handover. "
            "GEO latency makes conversation hard. Spectrum, the ground gateway, and regulation are "
            "operator work, not “space magic.”"
        ),
        "how_steps": [
            "Terrestrial first: gNB in the city. Satellite/HAPS cell in the gap.",
            "Ground gateway: feeder link from the satellite to a Türk Telekom earth station, then into the core.",
            "Doppler/delay compensation: PHY time-frequency pre-correction; otherwise even the Physical Random Access Channel (PRACH) will not hold.",
            "Service class: emergency SMS/voice first; not a promise of a terabit city experience.",
        ],
        "mental_model": (
            "Build the picture in your mind this way: the terrestrial network is a street lamp — it "
            "lights the road, not the forest. NTN is a spotlight held from above. Where there is a "
            "lamp, use the lamp; where there is not, the spotlight. The spotlight is farther away; "
            "shadow and delay are different."
        ),
        "analogy": (
            "Street lamp / spotlight from the air. NTN holds the forest and the sea; it does not "
            "replace the street lamp."
        ),
        "analogy_technical_map": (
            "The technical mapping: lamp = gNB; spotlight = LEO beam; cable = feeder link "
            "+ core; shadow delay = propagation ~ d/c (tens of ms order on LEO, ~250 ms "
            "round-trip on GEO); sway in the wind = Doppler f_d = f_c (v/c) cosθ. Direct-to-Cell "
            "means fitting the phone antenna’s link budget, not a dish."
        ),
        "when_used": (
            "Rural and mountain, sea, aviation, a disaster backup path, IoT in tower-less terrain. "
            "Where terrestrial is not economic."
        ),
        "when_not": (
            "Not the primary path for inner-city capacity or sub-millisecond Ultra-Reliable "
            "Low-Latency Communication (URLLC). “100% global, zero gaps” is a marketing sentence; "
            "polar, indoor, and regulatory gaps remain. Satellite latency was not field-measured "
            "on this platform; the rule-based range is from the literature."
        ),
        "not_to_confuse": (
            "A classical Very Small Aperture Terminal (VSAT) dish ≠ Direct-to-Cell. Starlink "
            "consumer broadband is not the same product as an NTN 3GPP cell (protocol and business "
            "model can differ). HAPS is not a satellite; it is a stratosphere layer. ISAC “making "
            "the sky a radar” is not NTN."
        ),
        "real_world": (
            "3GPP TR 38.811 and Rel-17/18 NTN work items, Direct-to-Cell operator trials, "
            "ESA space-component studies. In Türkiye a disaster backup-path scenario is operator strategy."
        ),
        "tt_impact": (
            "A disaster path, a fishing fleet, rural Eastern Anatolia. TRL 6. "
            "A complement to the urban 5G/6G tower."
        ),
        "principle_html": (
            "<p><strong>1. Fill the gap:</strong> City and road stay with towers. In empty geography "
            "<strong>LEO</strong> or <strong>HAPS</strong> speaks.</p>"
            "<p><strong>2. Keep the same identity:</strong> The target is not a dedicated dish; it is a 3GPP UE seeing the satellite cell.</p>"
            "<p><strong>3. Manage the shift:</strong> The satellite is fast. PHY compensates Doppler and delay; "
            "it is still not as “instant” as a terrestrial tower.</p>"
            "<p><strong>Result:</strong> The coverage hole closes. Not a rival; a complement.</p>"
        ),
        "arch_html": (
            "<p><strong>Layer 1 — Space/air:</strong> A LEO constellation, HAPS on demand, rarely GEO for voice/IoT.</p>"
            "<p><strong>Layer 2 — Ground gateway:</strong> Feeder link → Türk Telekom gateway → core network.</p>"
            "<p><strong>Layer 3 — UE:</strong> A Rel-17+ NTN-capable modem; not every legacy phone is guaranteed.</p>"
            "<p>The Doppler and FSPL cards sit in the expert layer.</p>"
        ),
    },
    "ambient_iot": {
        "card": (
            "Every carton in the warehouse, every soil-moisture sensor in the field, still wants a "
            "battery today. When the battery dies the device dies; swapping millions of batteries "
            "does not scale. Ambient IoT harvests a scrap of ambient RF and says “I am here” by "
            "backscatter. It does not carry video. Technology Readiness Level (TRL) 4 — a 3GPP work item; it is not stuck to "
            "every shelf."
        ),
        "kicker": "Problem: you cannot put a battery on every object",
        "what": (
            "Ambient IoT is the IoT class in which tags with no battery, or a very small one, "
            "harvest energy from ambient RF (tower, Wi-Fi, a dedicated illuminator) and, most "
            "often by backscatter, send a short status message. The aim is cheap tracking at "
            "trillion scale."
        ),
        "why_needed": (
            "Battery logistics and chemical waste are not economic at carton/greenhouse/meter scale. "
            "Classical cellular IoT (NB-IoT, Reduced Capability (RedCap)) still wants an energy "
            "source. A batteryless tag is the need to solve “where / how many degrees” without a "
            "maintenance crew."
        ),
        "problem": (
            "Range is short and bit rate is low because reflected power is weak and ambient energy "
            "is not guaranteed. The reader must be sensitive and the protocol ultra-narrow. "
            "This is not “it replaces your phone.”"
        ),
        "how_steps": [
            "Harvest: a rectenna converts RF to DC; a scrap accumulates on a capacitor.",
            "Reflect: antenna impedance is switched to modulate the incoming carrier (no power amplifier of its own).",
            "Read: a nearby gNB/reader separates the weak echo + bit.",
            "Write to the cloud: “carton 14, 4 °C” — no video.",
        ],
        "mental_model": (
            "Build the picture in your mind this way: the solar panel on an old calculator. Radio "
            "waves, not light, are the “sun.” The device does not watch a film; it only reports a "
            "short status. If there is no sun (RF is weak), it falls silent."
        ),
        "analogy": (
            "A solar calculator: batteryless, lives off light. Ambient IoT uses a scrap of RF "
            "instead of light."
        ),
        "analogy_technical_map": (
            "The technical mapping: panel = rectenna efficiency η; light intensity = P_tx G_tx (λ/4πd)²; "
            "the calculator’s “equals” key = backscatter bit b(t); shade = an RF-weak zone. "
            "RFID is the ancestor; the difference is a 3GPP cellular reader and an addressing target."
        ),
        "when_used": (
            "Logistics pallet, cold chain, greenhouse humidity, meter, structural health — where "
            "you want short range, sparse, low bit rate, long life."
        ),
        "when_not": (
            "Voice, video, kilometre range, moving-vehicle telemetry. “Sub-one-cent, unlimited life, "
            "a trillion objects” is target/marketing; a Rel-19 work item is not a product on the shelf. "
            "In an RF-less warehouse corner the tag dies."
        ),
        "not_to_confuse": (
            "Classical passive RFID at a shop door is an ancestor of Ambient IoT, but the cellular "
            "standard and the multi-reader scenario are different. An energy-harvesting sensor "
            "(solar + battery) is a separate class as well. ISAC echo measurement is a non-cooperative "
            "target; Ambient IoT is an intentional tag."
        ),
        "real_world": (
            "3GPP TR 38.848, academic backscatter, commercial batteryless-tag trials. "
            "A flow onto the operator IoT platform is written as a scenario; it is not on every "
            "shelf in the field."
        ),
        "tt_impact": (
            "Warehouse pallet, greenhouse, meter: a monitoring candidate without a maintenance crew. "
            "TRL 4. It does not replace your phone."
        ),
        "principle_html": (
            "<p><strong>1. Harvest:</strong> The tag turns a scrap of airborne RF into electricity (rectenna). "
            "There is no battery bay, or it is only a backup.</p>"
            "<p><strong>2. Reflect:</strong> It does not fire its own transmitter. It changes the incoming wave "
            "into a yes/no. That is why range is short.</p>"
            "<p><strong>3. Read:</strong> A nearby tower or reader hears the weak echo and writes it to the cloud.</p>"
            "<p><strong>Result:</strong> Cheap, batteryless, sparse tracking. It does not carry video; it solves the right job.</p>"
        ),
        "arch_html": (
            "<p><strong>Layer 1 — Tag:</strong> ASIC + micro-capacitor + rectenna. No battery.</p>"
            "<p><strong>Layer 2 — Energy and reader:</strong> A 6G tower or an auxiliary illuminator; "
            "a high-sensitivity receiver.</p>"
            "<p><strong>Layer 3 — 3GPP Rel-19 and IoT cloud:</strong> Narrow addressing, Türk Telekom IoT platform.</p>"
            "<p>The Friis harvest and backscatter model sit in the expert cards.</p>"
        ),
    },
}
