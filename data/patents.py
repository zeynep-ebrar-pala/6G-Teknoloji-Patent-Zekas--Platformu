"""
Türk Telekom 6G Patent Intelligence Dataset
Contains company patent data, annual trends, topic distributions, keyword frequencies, and patent graph relationships.
"""

PATENT_COMPANIES = ["Huawei", "Qualcomm", "Samsung", "Ericsson", "Nokia", "ZTE", "NEC", "Intel"]

TECHNOLOGY_DOMAINS = [
    "ISAC (Integrated Sensing & Comm)",
    "RIS (Reconfigurable Surfaces)",
    "Cell-Free Massive MIMO",
    "THz & Sub-THz Communications",
    "AI-Native RAN & O-RAN",
    "NTN (Non-Terrestrial Networks)",
    "Ambient IoT & Energy Harvesting"
]

# Annual Patent Application Trends (2020 - 2026)
PATENT_TRENDS = {
    "Years": [2020, 2021, 2022, 2023, 2024, 2025, 2026],
    "Huawei": [450, 780, 1250, 1890, 2450, 3100, 3800],
    "Qualcomm": [380, 620, 1020, 1540, 2100, 2750, 3350],
    "Samsung": [310, 540, 890, 1380, 1850, 2400, 2950],
    "Ericsson": [280, 480, 760, 1150, 1600, 2050, 2500],
    "Nokia": [250, 430, 710, 1080, 1500, 1920, 2380],
    "ZTE": [190, 340, 580, 890, 1220, 1600, 1980],
    "NEC": [110, 210, 350, 520, 740, 980, 1250],
    "Intel": [90, 180, 290, 430, 610, 820, 1050]
}

# Patent Share by Technology Domain per Company
COMPANY_DOMAIN_DISTRIBUTION = {
    "Huawei": {"ISAC": 28, "RIS": 20, "Cell-Free": 15, "THz": 12, "AI-RAN": 15, "NTN": 7, "Ambient IoT": 3},
    "Qualcomm": {"ISAC": 22, "RIS": 15, "Cell-Free": 18, "THz": 18, "AI-RAN": 14, "NTN": 8, "Ambient IoT": 5},
    "Samsung": {"ISAC": 18, "RIS": 22, "Cell-Free": 14, "THz": 16, "AI-RAN": 16, "NTN": 9, "Ambient IoT": 5},
    "Ericsson": {"ISAC": 25, "RIS": 18, "Cell-Free": 20, "THz": 10, "AI-RAN": 17, "NTN": 6, "Ambient IoT": 4},
    "Nokia": {"ISAC": 24, "RIS": 24, "Cell-Free": 16, "THz": 8, "AI-RAN": 18, "NTN": 6, "Ambient IoT": 4},
    "ZTE": {"ISAC": 20, "RIS": 21, "Cell-Free": 17, "THz": 11, "AI-RAN": 15, "NTN": 10, "Ambient IoT": 6},
    "NEC": {"ISAC": 19, "RIS": 25, "Cell-Free": 15, "THz": 14, "AI-RAN": 13, "NTN": 8, "Ambient IoT": 6},
    "Intel": {"ISAC": 15, "RIS": 12, "Cell-Free": 12, "THz": 15, "AI-RAN": 28, "NTN": 10, "Ambient IoT": 8}
}

# Top Keywords and Frequency in 6G Patent Claims
PATENT_KEYWORDS = {
    "Beamforming": 1420,
    "Sensing Matrix": 1180,
    "Phase Shift Profile": 1050,
    "Deep Reinforcement Learning": 980,
    "Sub-THz Channel Estimation": 870,
    "Zero Energy Transceiver": 760,
    "Satellite Direct-to-Cell": 690,
    "Distributed MIMO Processing": 640,
    "Joint Waveform Design": 580,
    "Metamaterial Surface": 530,
    "Semantic Communications": 490,
    "O-RAN xApp/rApp": 440
}

# Sample Key Patents for Intelligence Feed
TOP_PATENTS_FEED = [
    {
        "id": "EP-4019283-B1",
        "title": "Integrated Sensing and Communications (ISAC) Waveform Optimization in Terahertz Bands",
        "assignee": "Huawei Technologies",
        "year": 2025,
        "domain": "ISAC & THz",
        "citations": 142,
        "abstract": "Methods and apparatuses for dual-functional radar-communication (DFRC) waveform generation leveraging spatio-temporal beamforming in sub-THz spectrum."
    },
    {
        "id": "US-11894921-B2",
        "title": "Active Reconfigurable Intelligent Surfaces (RIS) with Phase-Shift Self-Calibration",
        "assignee": "Qualcomm Inc.",
        "year": 2024,
        "domain": "RIS",
        "citations": 118,
        "abstract": "Self-optimizing active RIS architecture designed for dynamic NLOS blockage compensation in dense urban 6G micro-cells."
    },
    {
        "id": "WO-2025-089123-A1",
        "title": "Cell-Free Massive MIMO Joint Channel Estimation and Pilot Allocation via Federated Learning",
        "assignee": "Ericsson AB",
        "year": 2025,
        "domain": "Cell-Free MIMO",
        "citations": 95,
        "abstract": "Distributed processing nodes coordinating AP cluster selection and power allocation for ultra-dense cell-free deployments."
    },
    {
        "id": "US-11990155-B1",
        "title": "AI-Native RAN Scheduling and PHY-Layer Autoencoder Architecture",
        "assignee": "Nokia Solutions & Networks",
        "year": 2024,
        "domain": "AI-Native RAN",
        "citations": 88,
        "abstract": "End-to-end neural network transceiver adaptation using deep learning for non-linear power amplifier distortion correction."
    },
    {
        "id": "EP-4102933-A1",
        "title": "Ambient IoT Energy Harvesting and Backscatter Communication Protocol",
        "assignee": "Samsung Electronics",
        "year": 2025,
        "domain": "Ambient IoT",
        "citations": 76,
        "abstract": "Ultra-low power passive backscatter signaling using RF energy harvesting in ambient 6G sub-6GHz and mmWave signals."
    }
]
