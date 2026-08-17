"""
Expert layer: formula cards, comparisons, use-case mechanisms.
Appended to the HTML architecture in technologies.py; no invented numbers.
"""

from __future__ import annotations

EXPERT_DEPTH: dict[str, dict] = {
    "isac": {
        "formulas": [
            {
                "name": "SNR in the radar equation",
                "latex": r"\mathrm{SNR}_{radar}=\frac{P_t G_t G_r\lambda^2\sigma}{(4\pi)^3 R^4 k T_0 B L}",
                "symbols": [
                    {"symbol": r"P_t", "meaning": "Transmitter output power", "unit": "W"},
                    {"symbol": r"G_t, G_r", "meaning": "Transmit / receive antenna gain (linear)", "unit": "—"},
                    {"symbol": r"\lambda", "meaning": "Carrier wavelength", "unit": "m"},
                    {"symbol": r"\sigma", "meaning": "Target radar cross section (RCS)", "unit": "m²"},
                    {"symbol": r"R", "meaning": "One-way range to the target", "unit": "m"},
                    {"symbol": r"k T_0 B", "meaning": "Thermal noise power (Boltzmann × temperature × bandwidth)", "unit": "W"},
                    {"symbol": r"L", "meaning": "System and atmospheric losses", "unit": "—"},
                ],
                "tells_us": (
                    "It says how 'visible' the echo is relative to the receiver noise. "
                    "Detection probability and range resolution are built on this ratio; it is not a bit-rate formula."
                ),
                "why_this_form": (
                    "On the outbound path power spreads as ~1/R²; on the return it does so again ~1/R²; the product yields R⁴. "
                    "λ² and G come from the antenna's effective area and directivity. σ is how large a 'mirror' "
                    "the target is. B in the denominator: a wider bandwidth means more noise (and better range resolution)."
                ),
                "when_valid": (
                    "Point target, far-field, single round trip, monostatic radar with clutter neglected. "
                    "Multipath in a city makes this equation optimistic."
                ),
                "if_variable_changes": (
                    "When R doubles, SNR drops by ~16× — that is why a base-station ISAC range stays "
                    "shorter than the communication range. When B increases, noise increases but range resolution thins to ~c/(2B): "
                    "the classic communication–sensing trade-off. When P_t increases, both bits and echo strengthen; there is a battery and EMC cost."
                ),
                "assumptions": (
                    "Target RCS is known or estimated; antenna gains are in the beam direction; "
                    "receiver noise is taken as thermal. Centimetre-level precision does not fall out of this equation automatically; "
                    "B, SNR and the estimation algorithm jointly determine it. Field SNR has not been measured on this platform."
                ),
                "simple_example": (
                    "On the same hardware, doubling R means ~12 dB more SNR loss "
                    "(10 log10(16) ≈ 12). Closing that gap requires ~16× more power or gain — "
                    "urban EIRP ceilings limit this."
                ),
            },
            {
                "name": "Cramér–Rao bound and communication capacity",
                "latex": r"\mathrm{CRB}(\theta)\ge\frac{1}{J(\theta)},\qquad C_{\mathrm{com}}=B\log_2\left(1+\frac{P_{\mathrm{com}}|h|^2}{\sigma_n^2}\right)",
                "symbols": [
                    {"symbol": r"\theta", "meaning": "Parameter to be estimated (angle, delay, Doppler)", "unit": "rad, s veya Hz"},
                    {"symbol": r"J(\theta)", "meaning": "Fisher information — how sharp the data is about θ", "unit": "1/birim²"},
                    {"symbol": r"C_{com}", "meaning": "Shannon capacity (AWGN, known channel)", "unit": "bit/s"},
                    {"symbol": r"P_{com}", "meaning": "Power allocated to communication", "unit": "W"},
                    {"symbol": r"h", "meaning": "Complex channel gain", "unit": "—"},
                    {"symbol": r"\sigma_n^2", "meaning": "Noise power", "unit": "W"},
                ],
                "tells_us": (
                    "Left: the variance of an unbiased estimator cannot be better than the inverse of Fisher information. "
                    "Right: the bit ceiling that power allocated to communication can carry in the same band. "
                    "In ISAC, P and B feed both expressions at once."
                ),
                "why_this_form": (
                    "The CRB comes from statistical estimation theory; it is the theoretical floor of any 'better radar' claim. "
                    "The Shannon formula assumes AWGN and infinite block length. They are written together because of "
                    "resource sharing: when P_com increases, C increases, and the energy or time left for sensing decreases."
                ),
                "when_valid": (
                    "CRB: regular statistical model; the approximation is good at high SNR. "
                    "Shannon: Gaussian noise, coding delay neglected. OTFS/OFDM approach this in practice; they are not equal to it."
                ),
                "if_variable_changes": (
                    "When observation time or SNR increases, J grows and the CRB shrinks (better angle/range). "
                    "When B increases, both C and (radar) range resolution improve, but noise and processing load increase."
                ),
                "assumptions": (
                    "Multiple targets and clutter degrade the CRB. '1 cm' is not a field guarantee derived from this inequality."
                ),
            },
        ],
        "comparison": {
            "title": "What ISAC must not be confused with",
            "headers": ["Approach", "Primary aim", "How does it work?", "Advantage", "Limitation", "When to prefer?"],
            "rows": [
                [
                    "Separate radar + separate network",
                    "Two independent missions",
                    "Two spectra, two antennas, two schedules",
                    "Mature products, weak trade-off",
                    "CAPEX, spectrum, EMI",
                    "When mission-critical radar already exists",
                ],
                [
                    "ISAC / DFRC / JCR",
                    "Single resource, dual function",
                    "Shared waveform and hardware",
                    "Candidate for spectrum and antenna savings",
                    "Power/time trade-off, clutter, privacy",
                    "When tower geometry already sees the scene",
                ],
                [
                    "Camera / LiDAR",
                    "Image or point cloud",
                    "Optical / laser",
                    "Rich scene semantics",
                    "Fog, night, privacy, maintenance",
                    "Semantic tasks where RF is not enough",
                ],
            ],
        },
        "use_case_depth": [
            {
                "how": "Target kinematics in a blind spot are extracted from echo delay and AoA; a V2X message may be a separate control channel.",
                "when_not": "The single-path assumption breaks at a multipath intersection; a centimetre claim was not measured on this platform.",
            },
            {
                "how": "A low-altitude target's RCS may be small; a multistatic (bistatic) geometry enlarges the cross section.",
                "when_not": "Without a cooperative transponder, telling a rogue drone from a bird is as hard as with analogue radar.",
            },
            {
                "how": "At macro scale a density map; there is no individual identity; the Doppler spectrum gives crowd motion.",
                "when_not": "If personal-tracking regulation is unclear, public-sector productisation stops.",
            },
            {
                "how": "Indoors, multipath echo can actually be map richness (an inverse problem).",
                "when_not": "Without LiDAR/vision fusion, a millimetre 'route' is an exaggeration.",
            },
            {
                "how": "Chest-wall micro-Doppler as a respiration trace has been shown in the literature; the absence of a camera is not automatically a privacy advantage.",
                "when_not": "Without medical-device approval and consent it does not count as a health product.",
            },
        ],
        "adv_why": [
            "A separate radar RF chain and spectrum licence are not paid for; existing gNB geometry is used.",
            "Range resolution scales with bandwidth; angular resolution with array aperture — the target is literature, not a field guarantee.",
            "The dark–rain–fog weakness of optical sensors is milder in RF (frequency-dependent).",
            "The same Hz carries both bits and echo; spectral-efficiency gain if the trade-off is managed correctly.",
        ],
        "dis_why": [
            "The same P_t and time feed both C_com and SNR_radar; when one increases the other is physically squeezed.",
            "Urban clutter lowers Fisher information; the CRB stays optimistic.",
            "Extracting motion from echo is camera-less tracking; it is a KVKK/ePrivacy design question, not a side effect.",
        ],
        "global_why": [
            "3GPP Rel-19 ISAC work item: the gateway from research paper to specification candidate.",
            "Hexa-X-II: describes where sensing–communication coexistence sits in Europe's flagship 6G architecture.",
            "IEEE ComSoc initiative: produces a shared term and metric language (DFRC, JCR).",
            "Vendor testbeds are demonstrations; 100 Gbps + 1 cm together is not a metric verified on this platform.",
        ],
        "tt_why": [
            "Bosphorus: coastal gNB geometry cuts the waterway; fog blinds the camera, RF echo is a candidate.",
            "Drone corridor: low altitude, the terrestrial tower already looks up; a separate UTM radar is expensive.",
            "Rubble: no optics, through-wall RF literature exists; search-and-rescue product approval is a separate job.",
        ],
    },
    "ris": {
        "formulas": [
            {
                "name": "RIS-aided narrowband channel",
                "latex": r"y=\big(\mathbf{h}_r^{H}\boldsymbol{\Phi}\mathbf{G}\big)x+n,\quad\boldsymbol{\Phi}=\mathrm{diag}(e^{j\theta_1},\ldots,e^{j\theta_N})",
                "symbols": [
                    {"symbol": r"x", "meaning": "Transmitted complex baseband symbol", "unit": "—"},
                    {"symbol": r"y", "meaning": "Symbol received at the UE", "unit": "—"},
                    {"symbol": r"\mathbf{G}", "meaning": "Tx (gNB) → RIS-element MIMO channel", "unit": "—"},
                    {"symbol": r"\mathbf{h}_r", "meaning": "RIS → Rx (UE) channel vector", "unit": "—"},
                    {"symbol": r"\theta_n", "meaning": "Phase applied by the n-th element", "unit": "rad"},
                    {"symbol": r"n", "meaning": "Receiver noise", "unit": "—"},
                ],
                "tells_us": (
                    "The effective channel seen by the UE is the RIS phase diagonal combining the two hops. "
                    "Choosing Φ is choosing the 'mirror angle'. Producing x is still the gNB's job."
                ),
                "why_this_form": (
                    "Narrowband, flat-fading assumption: each element is one complex multiplier. "
                    "Diagonal: the elements do not radiate into one another (ideal passive model). "
                    "The Hermitian h_r^H takes the inner product on the Rx side."
                ),
                "when_valid": (
                    "Narrowband or per OFDM subcarrier; elements mutually uncoupled; "
                    "quantised phase (1–2 bit) breaks this continuous-θ model."
                ),
                "if_variable_changes": (
                    "If θ is wrong the beam misses the UE and |h_r^H Φ G| drops. When N grows (N² below) "
                    "power grows under ideal alignment; estimation load also grows with N."
                ),
                "assumptions": (
                    "The channel is assumed known on the Tx and RIS sides. A passive RIS cannot measure; "
                    "in practice this assumption is the largest bottleneck."
                ),
            },
            {
                "name": "N² power scaling (ideal alignment)",
                "latex": r"P_r \propto N^2\,|h_{\mathrm{Tx-RIS}}|^2\,|h_{\mathrm{RIS-Rx}}|^2",
                "symbols": [
                    {"symbol": r"N", "meaning": "Number of RIS elements", "unit": "—"},
                    {"symbol": r"h_{Tx-RIS}", "meaning": "Per-element Tx–RIS complex gain (scale)", "unit": "—"},
                    {"symbol": r"h_{RIS-Rx}", "meaning": "Per-element RIS–Rx gain", "unit": "—"},
                    {"symbol": r"P_r", "meaning": "Power received at the UE", "unit": "W"},
                ],
                "tells_us": (
                    "Under ideal phase alignment the voltage contributions of N elements add (~N); power is the square (~N²). "
                    "In an active relay, power typically scales as ~N (each element has its own PA); that is why RIS carries a 'passive array-gain' promise."
                ),
                "why_this_form": (
                    "Coherently summed field amplitude scales with N; power at the detector is the square of amplitude. "
                    "The two-hop product writes the double path loss: each hop carries FSPL."
                ),
                "when_valid": (
                    "Perfect CSI, continuous phase, far-field, identical elements. "
                    "Near-field, quantisation and estimation error lower the exponent."
                ),
                "if_variable_changes": (
                    "Raising N from 10 to 100 is ideally ~20 dB of power; in practice the channel-estimation share eats into that. "
                    "If distance doubles on each hop, that hop loses ~6 dB; two hops weigh more."
                ),
                "assumptions": (
                    "Double path loss limits the 'stick it everywhere instead of a tower' RIS solution. "
                    "90% energy saving is a coarse comparison with an active base station; there is no bill on this platform."
                ),
            },
        ],
        "comparison": {
            "title": "RIS, relay and small cell",
            "headers": ["Approach", "Primary aim", "How does it work?", "Advantage", "Limitation", "When to prefer?"],
            "rows": [
                [
                    "New gNB / small cell",
                    "Capacity + coverage",
                    "Its own RF chain and cell",
                    "Mature, measurable SINR",
                    "CAPEX, site, backhaul",
                    "When traffic truly wants a new sector",
                ],
                [
                    "Active relay / repeater",
                    "Range extension",
                    "Receives, amplifies, forwards",
                    "Single-hop loss can be smaller",
                    "Power, noise amplification, interference",
                    "When the power budget and site allow it",
                ],
                [
                    "Passive / semi-passive RIS",
                    "Shaping the path",
                    "Reflection with a phase diagonal",
                    "Low energy, thin form factor",
                    "Double path loss, CSI, control delay",
                    "N-LoS and a facade where a tower cannot be sited",
                ],
            ],
        },
        "use_case_depth": [
            {"how": "Φ aligns the total Tx–RIS–UE phase; the direct path is already dead because of the building.", "when_not": "Without CSI, random phase produces random fading."},
            {"how": "Around a bend, several panels can be lined up like a multi-hop 'waveguide'.", "when_not": "Multipath in a metal tunnel stresses the model's narrowband assumption."},
            {"how": "Indoors at mmWave/THz, a wall reflection is not damage but a controlled path.", "when_not": "Human blockage still cuts the link; RIS is not a magic wall."},
            {"how": "The number of active PAs falls; the energy promise comes from that.", "when_not": "The control processor and estimation pilots put energy back. 90% was not measured."},
            {"how": "Reflection geometry adds AoA diversity; fusion with ISAC is a research topic.", "when_not": "RIS alone is not a radar standard."},
        ],
        "adv_why": [
            "Absence of a PA means control power on the order of milliwatts; comparison with an active gNB is the target.",
            "A facade/glass form factor lowers site rent.",
            "It does not radiate its own EIRP; it steers the incoming wave (the EMC profile is different).",
            "Element size scales with the carrier; there is a design family from sub-6 to THz.",
        ],
        "dis_why": [
            "A passive element is not a receiver; without pilots and protocol, Φ is blind.",
            "Both Tx→RIS and RIS→Rx carry FSPL; N² compensates only with alignment.",
            "For a moving UE, updating Φ(t) demands processing and control delay.",
        ],
        "global_why": [
            "ETSI ISG RIS: aligns industry language and channel models.",
            "IEEE task force: academic metrics (N², double path) are shared.",
            "Operator PoC: a facade-panel demonstration; not a commodity product on the shelf.",
            "RISE-6G: an EU research framework, not a standard.",
        ],
        "tt_why": [
            "Historic Peninsula: a new tower silhouette is constrained; a facade panel is more defensible archaeologically and under zoning.",
            "Tunnel: a bend is N-LoS; a passive panel can be simpler than an active one on maintenance and power.",
            "Plaza glass: transparent-RIS research exists; '10 Gbps+ in every carriage' was not measured on this platform.",
        ],
    },
    "cell_free": {
        "formulas": [
            {
                "name": "SINR for user k (joint transmission)",
                "latex": r"\mathrm{SINR}_k=\frac{\left|\sum_{m=1}^{M}\mathbf{g}_{mk}^{H}\mathbf{w}_{mk}\right|^2}{\sum_{j\neq k}\left|\sum_{m=1}^{M}\mathbf{g}_{mk}^{H}\mathbf{w}_{mj}\right|^2+\sigma^2}",
                "symbols": [
                    {"symbol": r"M", "meaning": "Number of access points (APs)", "unit": "—"},
                    {"symbol": r"\mathbf{g}_{mk}", "meaning": "Channel between AP m and user k", "unit": "—"},
                    {"symbol": r"\mathbf{w}_{mk}", "meaning": "Precoding vector at AP m for user k", "unit": "—"},
                    {"symbol": r"\sigma^2", "meaning": "Noise power", "unit": "W"},
                    {"symbol": r"j", "meaning": "Index of another user (interference)", "unit": "—"},
                ],
                "tells_us": (
                    "Numerator: coherent summing of all APs on your symbol (useful power). "
                    "Denominator: other users' precoders leaking through the same channel + noise. "
                    "There is no cell edge: instead of a 'neighbouring cell' term there is only user interference."
                ),
                "why_this_form": (
                    "The sum over m: service is distributed. The j≠k sum: the spectrum is shared. "
                    "In a classical cell the denominator also includes 'foreign' power from other towers; here that power "
                    "is coordinated and shaped with w."
                ),
                "when_valid": (
                    "Flat fading / instantaneous single carrier; near-perfect CSI; no fronthaul delay. "
                    "Pilot contamination inflates the denominator."
                ),
                "if_variable_changes": (
                    "When M increases, diversity and total aperture grow and SINR fairness improves — fronthaul and CPU become linearly/exponentially more expensive. "
                    "If w is chosen as MMSE, the interference denominator shrinks; ZF zeros more aggressively and can raise the noise."
                ),
                "assumptions": (
                    "Synchronisation on the order of nanoseconds. 5x–10x spectral gain is selected-scenario literature, "
                    "not a city-wide guarantee."
                ),
            },
        ],
        "comparison": {
            "title": "Cell-free MIMO and its neighbours",
            "headers": ["Approach", "Primary aim", "How does it work?", "Advantage", "Limitation", "When to prefer?"],
            "rows": [
                [
                    "Macro cell",
                    "Wide-area coverage",
                    "One tower, sector, handover",
                    "Mature, low fronthaul",
                    "Edge SINR, unfairness",
                    "Sparse traffic, rural",
                ],
                [
                    "Small-cell forest",
                    "Capacity densification",
                    "Still cells + handover",
                    "Site proximity",
                    "Edge and interference remain",
                    "Hotspot, if backhaul exists",
                ],
                [
                    "Cell-free Massive MIMO",
                    "Edgeless fairness",
                    "Many APs, joint w, one user set",
                    "Uniform SINR, fewer drops",
                    "Fronthaul, CPU, sync",
                    "Stadium, terminal, factory",
                ],
            ],
        },
        "use_case_depth": [
            {"how": "Stand APs serve the same user set; an edge stand does not become a 'neighbouring cell'.", "when_not": "Without fronthaul it is not distributed MIMO, it is scattered small cells."},
            {"how": "A walking UE's serving set slides; weights change instead of a hard handover.", "when_not": "CPU delay shifts phase and the beam breaks."},
            {"how": "AP–UE distance is short for low latency; the control loop sits in the edge cloud.", "when_not": "A safety SIL requirement is not entrusted to cell-free research code."},
            {"how": "Spectral efficiency is defined by a fair per-user share, not by peak rate.", "when_not": "Sparse street: fibre cost eats the gain."},
        ],
        "adv_why": [
            "By design there is no cell-edge user; the tail of the SINR distribution shortens.",
            "Cooperative w turns interference into useful power; spectral gain depends on the scenario.",
            "The macro-tower silhouette shrinks; aesthetics and site leasing.",
            "Handover failure as a target approaches zero (no hard cell boundary).",
        ],
        "dis_why": [
            "Every AP sends I/Q or compressed samples to the centre; fibre and eCPRI size is a multiple of a macro cell.",
            "MMSE/ZF matrix size grows with users × antennas.",
            "Trenching and rent can cost more than the radio hardware.",
        ],
        "global_why": [
            "Academic backbone of distributed-MIMO theory (Linköping school and derived literature).",
            "IEEE special issues collect metrics and fronthaul models.",
            "3GPP Rel-19/20 distributed MIMO: the path into the specification.",
            "Ericsson/Nokia demonstrations are laboratory; they are not a stadium product SKU.",
        ],
        "tt_why": [
            "Stadium: high load and fairness at once; a classical macro starves the stand edge.",
            "Istanbul Airport (IGA): walking-handover drops; sliding the serving set is a candidate mechanism.",
            "Industry: short hop + joint transport so an AGV does not stop at a cell boundary.",
        ],
    },
    "thz": {
        "formulas": [
            {
                "name": "THz path loss (FSPL × molecular absorption)",
                "latex": r"L(f,d)=L_{\mathrm{fs}}(f,d)\,L_{\mathrm{abs}}(f,d)=\left(\frac{4\pi f d}{c}\right)^2 e^{K(f)d}",
                "symbols": [
                    {"symbol": r"f", "meaning": "Carrier frequency", "unit": "Hz"},
                    {"symbol": r"d", "meaning": "Link distance", "unit": "m"},
                    {"symbol": r"c", "meaning": "Speed of light", "unit": "m/s"},
                    {"symbol": r"K(f)", "meaning": "Frequency-dependent absorption coefficient (water vapour etc.)", "unit": "1/m"},
                    {"symbol": r"L", "meaning": "Total power-loss factor (>1)", "unit": "—"},
                ],
                "tells_us": (
                    "The first factor is geometric spreading: as f and d grow, loss grows quadratically. "
                    "The second factor is spectral windows: at some f, K jumps and the link becomes a 'blind frequency'."
                ),
                "why_this_form": (
                    "Friis / FSPL from the spherical-wave surface. Absorption is Beer–Lambert: intensity e^{-K d} "
                    "(here L_abs = e^{K d} is the loss factor). At THz, K is not negligible; at mmWave it is often secondary."
                ),
                "when_valid": (
                    "Line of sight, homogeneous atmosphere; rain/fog is a separate model. Blockage (hand, torso) is not in this formula."
                ),
                "if_variable_changes": (
                    "f doubles → FSPL alone +6 dB. d doubles → FSPL +6 dB and absorption e^{K d} weighs even more. "
                    "Sliding a few GHz on the K(f) line can change loss by tens of dB — that is why a 'window' is chosen."
                ),
                "assumptions": (
                    "K(f) depends on standard atmosphere models (ITU-R). "
                    "The <100–500 m range rule is coarse; it varies with EIRP and rain."
                ),
            },
            {
                "name": "Shannon capacity (AWGN)",
                "latex": r"C=B\log_2\left(1+\frac{P_t G_t G_r}{L(f,d)\,N_0 B}\right)",
                "symbols": [
                    {"symbol": r"C", "meaning": "Channel-capacity ceiling", "unit": "bit/s"},
                    {"symbol": r"B", "meaning": "Bandwidth", "unit": "Hz"},
                    {"symbol": r"N_0", "meaning": "Noise spectral density", "unit": "W/Hz"},
                    {"symbol": r"P_t G_t G_r / L", "meaning": "Received power (Friis)", "unit": "W"},
                ],
                "tells_us": (
                    "C grows first with B (almost linearly at high SNR) and logarithmically with SNR. "
                    "THz's promise is to open B of tens of GHz. If L(f,d) eats the SNR, B alone does not produce Tbps."
                ),
                "why_this_form": (
                    "Shannon–Hartley. B in the denominator: a wider band means more noise (N_0 B). "
                    "That is why 'open B without bound' also lowers SNR; there is an optimum bandwidth."
                ),
                "when_valid": (
                    "Gaussian noise, flat channel or OFDM subcarrier, infinite coding delay. "
                    "Real ADC resolution and PA nonlinearity sit below C."
                ),
                "if_variable_changes": (
                    "B ×10 → ideally C ~10× if SNR stays high. L ×100 (20 dB) → SNR drops, "
                    "the log term collapses; the hose is wide but the pressure has leaked away."
                ),
                "assumptions": (
                    "B ≈ 50 GHz is an order-of-magnitude example, not allocated Turkish spectrum. "
                    "1 Tbps is a target/literature figure; it was not measured in this application."
                ),
            },
        ],
        "comparison": {
            "title": "THz neighbouring spectra",
            "headers": ["Approach", "Primary aim", "How does it work?", "Advantage", "Limitation", "When to prefer?"],
            "rows": [
                [
                    "Sub-6 GHz",
                    "Coverage",
                    "Good diffraction, moderate B",
                    "Walls, range",
                    "Spectrum is congested",
                    "Macro 5G/6G layer",
                ],
                [
                    "mmWave (e.g. 28–60 GHz)",
                    "Capacity + short hop",
                    "Narrow beam, moderate absorption",
                    "Mature 5G product",
                    "Blockage, site",
                    "Urban hotspot",
                ],
                [
                    "Sub-THz / THz",
                    "Extreme B, wireless fibre",
                    "Very narrow beam, high K(f)",
                    "Tbps candidate, spectrum abundant",
                    "Range, hardware, TRL 3",
                    "Rack, hall, tower bridge",
                ],
            ],
        },
        "use_case_depth": [
            {"how": "Inter-rack d is short, L is manageable; the cable pile shrinks.", "when_not": "Dust, alignment and EMC rack standards are a separate job. 1 Tbps was not measured."},
            {"how": "Hologram/VR bit rate wants B in Shannon; latency depends on hop count.", "when_not": "A handset THz band is not the default."},
            {"how": "On a short hop where fibre cannot be trenched, FSPL + beam is a backhaul candidate.", "when_not": "Rain and sway (tower) drop the link; diversity is needed."},
            {"how": "Short wavelength, small antenna; an in-body research edge.", "when_not": "Medical safety and absorption; not a commercial 6G feature."},
            {"how": "THz spectroscopy sees material lines; a mode separate from communication.", "when_not": "A security-scanner claim is not a standard network KPI."},
        ],
        "adv_why": [
            "If B of tens of GHz can be opened, C jumps in Shannon — the 100 Gbps–1 Tbps target range is literature.",
            "Short symbol duration is a low-latency candidate; the tail is still in the MAC.",
            "A very narrow beam makes eavesdropping harder; 'impossible to hack' is an exaggeration — physical proximity is enough.",
            "THz allocation is not yet crowded (regulation is evolving).",
        ],
        "dis_why": [
            "L(f,d) pushes range to tens–hundreds of metres.",
            "Blockage: hand and torso cut nearly as optics do.",
            "InP/GaN and fast-ADC cost is higher than CMOS mmWave.",
        ],
        "global_why": [
            "IEEE 802.15.3d: short-range THz PHY specification.",
            "ITU-R WRC: without lawful existence of the spectrum there is no network.",
            "Research programmes on device physics (source, detector).",
            "A vendor 140 GHz demonstration is Sub-THz; it is not a 10 THz product.",
        ],
        "tt_why": [
            "Data centre: d is small, fibre fatigue; alignment and heat are still there.",
            "Tower bridge: no trenching; rain wants a backup hop.",
            "Holographic studio: controlled indoor space, not a subscriber street.",
        ],
    },
    "ai_ran": {
        "formulas": [
            {
                "name": "End-to-end autoencoder loss",
                "latex": r"\mathcal{L}(\theta,\phi)=\mathbb{E}_{s,n}\big[\|s-f_D(f_E(s;\theta)+n;\phi)\|^2\big]",
                "symbols": [
                    {"symbol": r"s", "meaning": "Symbol / bit vector intended for transmission", "unit": "—"},
                    {"symbol": r"f_E(\cdot;\theta)", "meaning": "Learned transmitter (encoder) network", "unit": "—"},
                    {"symbol": r"f_D(\cdot;\phi)", "meaning": "Learned receiver (decoder) network", "unit": "—"},
                    {"symbol": r"n", "meaning": "Channel noise / distortion", "unit": "—"},
                    {"symbol": r"\theta,\phi", "meaning": "Network weights", "unit": "—"},
                ],
                "tells_us": (
                    "The aim is to shrink the error in recovering s after it has passed through the channel. "
                    "Instead of classical QAM+LDPC, 'how the wave is radiated' can also be learned. "
                    "This is a different layer from adjusting traffic lights in the RIC (PHY)."
                ),
                "why_this_form": (
                    "Autoencoder: two networks separated by a bottleneck (the channel). MSE, under Gaussian noise, "
                    "is related to maximum likelihood; a BER loss can also be used."
                ),
                "when_valid": (
                    "If the training distribution is close to the field channel. If the distribution shifts (sim→field), L lies. "
                    "3GPP compatibility and explainability still want classical PHY at most operators."
                ),
                "if_variable_changes": (
                    "If SNR drops (n grows), L rises on the same architecture; the network is forced to learn more redundancy. "
                    "If θ,φ overfit and lock onto the simulation channel, BER explodes in the field."
                ),
                "assumptions": (
                    "A differentiable channel model or a surrogate. If real PA nonlinearity is forgotten, the laboratory is wrong."
                ),
            },
            {
                "name": "Q-learning update (RRM)",
                "latex": r"Q(s,a)\leftarrow Q(s,a)+\alpha\big[r+\gamma\max_{a'}Q(s',a')-Q(s,a)\big]",
                "symbols": [
                    {"symbol": r"s", "meaning": "State (load, SINR, energy…)", "unit": "—"},
                    {"symbol": r"a", "meaning": "Action (PRB, sleep, beam)", "unit": "—"},
                    {"symbol": r"r", "meaning": "Instantaneous reward (capacity, outage, watts)", "unit": "—"},
                    {"symbol": r"\alpha", "meaning": "Learning step size", "unit": "—"},
                    {"symbol": r"\gamma", "meaning": "Discount (weight of future reward)", "unit": "—"},
                ],
                "tells_us": (
                    "The traffic cop keeps a table or network saying 'in this state the long-term value of that action is Q'. "
                    "A Near-RT xApp is the fast version of this loop; an rApp is the slow version."
                ),
                "why_this_form": (
                    "The sampled form of the Bellman equation. The term in brackets is the TD error: the gap between expected value and realised return."
                ),
                "when_valid": (
                    "Markov assumption (the future is summarised by s and a). If the reward is chosen wrongly, a 'clever' policy "
                    "(gaming the metric) is born. Exploration is dangerous on a live network."
                ),
                "if_variable_changes": (
                    "Large α → forgets fast, oscillates. γ≈1 → long-term energy; it can ignore a short outage. "
                    "If r is capacity only, the energy bill explodes."
                ),
                "assumptions": (
                    "A simulator ≠ the field. 50–70% energy saving is selected-sleep-scenario literature/target."
                ),
            },
        ],
        "comparison": {
            "title": "Rule-based RAN, SON and AI-RAN",
            "headers": ["Approach", "Primary aim", "How does it work?", "Advantage", "Limitation", "When to prefer?"],
            "rows": [
                [
                    "Fixed tariff / threshold",
                    "Predictability",
                    "Human rule",
                    "Explainable, auditable",
                    "Reacts late, local optimum",
                    "A quiet, well-understood cell",
                ],
                [
                    "Classical SON",
                    "Self-configuration",
                    "Heuristics + statistics",
                    "Mature vendor features",
                    "Limited learning",
                    "Today's 4G/5G operations",
                ],
                [
                    "AI-RAN / RIC xApp-rApp",
                    "Measurement-driven adaptation",
                    "ML policy + optional neural PHY",
                    "Variable load and energy",
                    "Black box, data, GPU energy",
                    "O-RAN trial, stadium, green target",
                ],
            ],
        },
        "use_case_depth": [
            {"how": "State s is spectrum occupancy; action a is PRB sharing; reward is interference+capacity.", "when_not": "Without a neighbouring-operator model the 'smart' policy crushes the outside."},
            {"how": "Precursor alarm: temperature, VSWR, error-counter time series are classified.", "when_not": "False positives exhaust spare inventory; human approval remains."},
            {"how": "r is energy + SLA; a is sleep depth. Deep-sleep wake-up delay can break the SLA.", "when_not": "Savings are not claimed until they are netted against the GPU itself."},
            {"how": "The Near-RT loop updates the beam index; exploration is constrained in production.", "when_not": "A wrongly learned handover causes mass drops."},
        ],
        "adv_why": [
            "Sleep and load shifting cut watt-hours — the ratio varies by field; 50–70% is a target/selected scenario.",
            "The zero-touch target lowers operations OPEX; a 'zero human' claim contradicts TRL 5.",
            "When the channel distribution shifts, a classical table breaks; a learning PHY carries an adaptation promise.",
            "O-RAN multi-vendor: policy software is separated from hardware.",
        ],
        "dis_why": [
            "If the reason for a decision cannot be told to an auditor, it is not accepted.",
            "NPU/GPU is both CAPEX and watts; a net green account is required.",
            "Without labelled faults and channel traces the model fabricates.",
        ],
        "global_why": [
            "AI-RAN Alliance: aligns vendor–operator language; it does not replace 3GPP.",
            "O-RAN WG2/10: xApp/rApp workflow.",
            "3GPP TR 38.843: whether AI/ML on the air interface will enter the specification.",
            "NVIDIA Aerial and similar are SDKs; they are not a standard.",
        ],
        "tt_why": [
            "Night-time macro sleep: watt-hours if there is a measurement; otherwise it is a scenario-engine rule.",
            "Match day: load s, action PRB from a neighbour cell; exploration is kept off.",
            "Predictive maintenance: a false positive must not burn the field team.",
        ],
    },
    "ntn": {
        "formulas": [
            {
                "name": "LEO Doppler shift",
                "latex": r"f_d=f_c\cdot\frac{v_{\mathrm{sat}}}{c}\cos(\theta(t))",
                "symbols": [
                    {"symbol": r"f_d", "meaning": "Deviation of the received frequency from the carrier", "unit": "Hz"},
                    {"symbol": r"f_c", "meaning": "Carrier frequency", "unit": "Hz"},
                    {"symbol": r"v_{sat}", "meaning": "Magnitude of the satellite's speed relative to the ground", "unit": "m/s"},
                    {"symbol": r"c", "meaning": "Speed of light", "unit": "m/s"},
                    {"symbol": r"\theta(t)", "meaning": "Angle between the velocity vector and the line of sight", "unit": "rad"},
                ],
                "tells_us": (
                    "As LEO approaches on the horizon f_d is positive, near overhead ~0, and negative as it recedes. "
                    "If the PHY does not predict and correct this shift, OFDM subcarriers slide and PRACH does not hold."
                ),
                "why_this_form": (
                    "Classical longitudinal Doppler: only the line-of-sight speed component. "
                    "v_sat / c ~ 2.5×10⁻⁵ (≈7.5 km/s); at f_c = 2 GHz, f_d reaches the order of tens of kHz."
                ),
                "when_valid": (
                    "Special relativity and gravitational shift neglected; single path. "
                    "In reality orbital ephemeris and UE motion are added."
                ),
                "if_variable_changes": (
                    "f_c ×2 → f_d ×2 (S-band vs Ka). Higher-v LEO (lower altitude) is more aggressive Doppler. "
                    "At the θ=90° (overhead) instant the shift is zero and the slope is maximum — handover densifies right in that region."
                ),
                "assumptions": (
                    "The 27 000 km/h order of magnitude is a popular rounding (~7.5 km/s). "
                    "Direct-to-cell assumes this correction fits in a cheap UE."
                ),
            },
            {
                "name": "Free-space path loss",
                "latex": r"\mathrm{FSPL}=\left(\frac{4\pi d f}{c}\right)^2",
                "symbols": [
                    {"symbol": r"d", "meaning": "Slant range (UE–satellite)", "unit": "m"},
                    {"symbol": r"f", "meaning": "Carrier", "unit": "Hz"},
                ],
                "tells_us": (
                    "d of 600–1000 km means ~60 dB more geometric loss than a terrestrial 1 km macro "
                    "(coarse: 20 log10(d2/d1)). That is why the link budget wants satellite EIRP and a UE noise figure."
                ),
                "why_this_form": (
                    "Friis. No obstacle; rain and ionosphere are added separately. At GEO, d ~36 000 km, FSPL is heavier, "
                    "which is why direct-to-cell is discussed for LEO first."
                ),
                "when_valid": (
                    "Line of sight, far-field. Indoor and trees add extra loss. At HAPS, d ~20 km, FSPL is lighter than LEO."
                ),
                "if_variable_changes": (
                    "d ×2 → +6 dB. f ×2 → +6 dB. Ka-band gives capacity; rain and FSPL penalties eat it."
                ),
                "assumptions": (
                    "10–30 ms LEO delay is a coarse range for propagation + processing; ping was not measured in this application. "
                    "GEO ~250 ms RTT order of magnitude makes conversation hard."
                ),
            },
        ],
        "comparison": {
            "title": "NTN layers",
            "headers": ["Approach", "Primary aim", "How does it work?", "Advantage", "Limitation", "When to prefer?"],
            "rows": [
                [
                    "Terrestrial gNB",
                    "Capacity and low latency",
                    "Short d, slow handover",
                    "Mature, cheap hop",
                    "Coverage hole, disaster fragility",
                    "City, road, building",
                ],
                [
                    "LEO NTN",
                    "Global gap-fill + low latency (vs GEO)",
                    "Direct-to-cell or gateway",
                    "TRL 6, disaster backup",
                    "Doppler, constellation, CAPEX",
                    "Rural, maritime, emergency",
                ],
                [
                    "GEO / HAPS",
                    "Fixed coverage / regional layer",
                    "Few satellites or stratosphere",
                    "Few handovers (GEO), lower d (HAPS)",
                    "GEO delay; HAPS continuity",
                    "Broadcast, IoT, regional patch",
                ],
            ],
        },
        "use_case_depth": [
            {"how": "Slant range is the only path on the open sea; FSPL + wave fading. The service class may be narrowband.", "when_not": "If the ship already has VSAT, the business model collides."},
            {"how": "Aircraft fuselage + high altitude; in-cabin distribution is separate.", "when_not": "An airline IFC contract is not automatically the same as 3GPP NTN."},
            {"how": "The terrestrial core is up, the RAN is dead; the satellite cell is emergency attach.", "when_not": "If the ground gateway is also hit by the earthquake, multi-gateway geography is required."},
            {"how": "IoT is sparse and delay-tolerant; GEO is also a candidate.", "when_not": "Real-time drone command is limited by LEO delay."},
        ],
        "adv_why": [
            "Coverage where the tower economy ends. '100% zero gap' is bounded by regulation and indoor.",
            "A backup path when terrestrial RAN collapses — if the core and gateway are up.",
            "It can defer rural fibre trenching; the capacity promise is not macro 6G.",
            "The Rel-17+ UE path reduces special-dish inventory (depends on device class).",
        ],
        "dis_why": [
            "Propagation delay is d/c + processing; not a primary URLLC path.",
            "LEO visibility is minutes; frequent cell changes.",
            "Launch and constellation replenishment CAPEX carries a different risk from a terrestrial site.",
        ],
        "global_why": [
            "3GPP Rel-17 NTN: the first cellular-satellite specification package.",
            "Direct-to-cell commercial trials (different constellations, different business models).",
            "AST and similar large phased-array approaches keep the link budget on the UE side.",
            "ESA 6G space component: a European system study.",
        ],
        "tt_why": [
            "Disaster: the terrestrial gNB dies, identity stays the same — an operator strategy, not a field guarantee.",
            "Fleet: open-sea FSPL + Direct-to-cell device class.",
            "Mountain: no site; connectivity, not capacity.",
        ],
    },
    "ambient_iot": {
        "formulas": [
            {
                "name": "RF energy harvesting (Friis × rectenna)",
                "latex": r"P_{\mathrm{rec}}=P_{tx}G_{tx}G_{rx}\left(\frac{\lambda}{4\pi d}\right)^2\eta_{\mathrm{rectenna}}",
                "symbols": [
                    {"symbol": r"P_{tx}", "meaning": "Illuminator / gNB output power", "unit": "W"},
                    {"symbol": r"G_{tx}, G_{rx}", "meaning": "Illuminator and tag antenna gain", "unit": "—"},
                    {"symbol": r"\lambda", "meaning": "Wavelength", "unit": "m"},
                    {"symbol": r"d", "meaning": "Illuminator–tag distance", "unit": "m"},
                    {"symbol": r"\eta_{rectenna}", "meaning": "RF→DC conversion efficiency (0–1)", "unit": "—"},
                ],
                "tells_us": (
                    "The DC-power crumb the tag will live on. d² (in fact Friis d² in the denominator) cuts range hard. "
                    "Because η < 1 and P_tx is low (EMC/EIRP ceiling), 'always-on broadcast' beyond tens of metres becomes hard."
                ),
                "why_this_form": (
                    "Friis received RF power; η is diode/rectifier reality. "
                    "A capacitor integrates this power; the message goes out only once a threshold of joules has accumulated."
                ),
                "when_valid": (
                    "Line of sight, single illuminator, narrowband. Indoor multipath sometimes helps, sometimes fades. "
                    "<10–50 m is a coarse practical range, depending on antenna and EIRP."
                ),
                "if_variable_changes": (
                    "d ×2 → P_rec drops 4×. As f rises, λ shrinks, the Friis penalty grows but the antenna shrinks. "
                    "η 0.3→0.6 is twice the energy; in the cold and at low power, diode η collapses."
                ),
                "assumptions": (
                    "The legal EIRP ceiling locks P_tx G_tx. 'Unlimited lifetime' ignores electronics ageing and "
                    "RF scarcity."
                ),
            },
            {
                "name": "Backscatter observation",
                "latex": r"y(t)=\alpha\, x(t)\, b(t)+n(t)",
                "symbols": [
                    {"symbol": r"x(t)", "meaning": "Carrier sent by the reader", "unit": "—"},
                    {"symbol": r"b(t)", "meaning": "Tag information sequence (typically ±1 or 0/1 impedance)", "unit": "—"},
                    {"symbol": r"\alpha", "meaning": "Round-trip attenuation and scattering coefficient", "unit": "—"},
                    {"symbol": r"n(t)", "meaning": "Noise + self-interference", "unit": "—"},
                ],
                "tells_us": (
                    "The tag does not turn on a PA; it reflects x by multiplying with b. Because the reader knows its own x "
                    "it can (at least partly) separate it. Because |α| is very small, range and bit rate are low."
                ),
                "why_this_form": (
                    "A multiplicative channel: energy and reference from x, information from b. "
                    "It is the cellular abstraction of RFID."
                ),
                "when_valid": (
                    "Narrowband, slow b(t) (clock much lower than x). If the reader's self-interference cancellation is not good "
                    "the α x term saturates the receiver."
                ),
                "if_variable_changes": (
                    "α falls similarly to d⁻⁴ (round trip) — the same geometry as the radar equation. "
                    "If b speeds up, SNR/bit drops; video approaches the impossible."
                ),
                "assumptions": (
                    "Kbps-class sensor telemetry. A trillion addresses is a 3GPP study target, not a field inventory."
                ),
            },
        ],
        "comparison": {
            "title": "Battery-free tags and their neighbours",
            "headers": ["Approach", "Primary aim", "How does it work?", "Advantage", "Limitation", "When to prefer?"],
            "rows": [
                [
                    "NB-IoT / RedCap",
                    "Cellular IoT",
                    "Battery modem, own Tx",
                    "Range, standard network",
                    "Battery logistics, cost",
                    "Meter, vehicle, km range",
                ],
                [
                    "Passive RFID",
                    "Door/shelf reading",
                    "Backscatter, dedicated reader",
                    "Mature, cheap",
                    "No cellular identity, short range",
                    "Warehouse door, retail",
                ],
                [
                    "Ambient IoT (3GPP)",
                    "Cellular battery-free trace",
                    "Harvest + backscatter + gNB reader",
                    "No battery; a candidate feed into TT IoT",
                    "RF scarcity, kbps, TRL 4",
                    "Pallet, greenhouse, short indoor hop",
                ],
            ],
        },
        "use_case_depth": [
            {"how": "Pallet d is close to the reader; b(t) is ID+temperature. No battery for years.", "when_not": "If RF is weak on an open truck trailer, it goes silent."},
            {"how": "Soil moisture is sampled sparsely; energy accumulation can take minutes.", "when_not": "Deep burial kills Friis."},
            {"how": "A threshold alarm is few bits; a cold-chain breach timestamp.", "when_not": "Continuous analogue monitoring exceeds the energy threshold."},
            {"how": "Moisture in concrete changes slowly; battery-free so there is no maintenance excavation.", "when_not": "Thick concrete wipes out α; reader placement is a design job."},
        ],
        "adv_why": [
            "Battery SKU and field labour go away — 'zero cost' is an exaggeration; silicon is still there.",
            "No chemical-battery waste; electronic e-waste remains.",
            "Target BOM is low; '1 cent' assumes volume and year, it is not today's shelf price.",
            "Lifetime is not limited by battery chemistry; it is limited by RF and solder life.",
        ],
        "dis_why": [
            "Round-trip attenuation + η; tens of metres is a coarse ceiling.",
            "Small α → kbps; no audio/video.",
            "If a warehouse corner is dark (RF), the tag is dead.",
        ],
        "global_why": [
            "3GPP TR 38.848: cellular Ambient IoT work item.",
            "IEEE backscatter special issues: physics and MAC.",
            "EU zero-power IoT frameworks: research.",
            "Wiliot and similar commercial tags: may not be an identical product to 3GPP.",
        ],
        "tt_why": [
            "Warehouse: the reader is a gNB or a gate; a 10-year maintenance promise is a target, not the field.",
            "Greenhouse: moisture is sparse; soil Friis is a design constraint.",
            "Meter: a shaft/building that has RF; a metal cabinet kills it.",
        ],
    },
}
