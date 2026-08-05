"""
Türk Telekom 6G Academic Publication Trends Dataset
Contains paper counts, source breakdown (IEEE Xplore, Google Scholar, Springer, Elsevier), top research institutions, top publishing countries, and most cited papers.
"""

ACADEMIC_SOURCES = ["IEEE Xplore", "Google Scholar", "Springer", "Elsevier"]

PUBLICATION_TRENDS_BY_TECH = {
    "Years": [2020, 2021, 2022, 2023, 2024, 2025, 2026],
    "ISAC": [350, 720, 1450, 2600, 3900, 5200, 6800],
    "RIS": [420, 890, 1850, 3200, 4800, 6100, 7500],
    "NTN": [280, 510, 980, 1750, 2650, 3500, 4400],
    "AI-RAN": [310, 640, 1280, 2100, 3150, 4200, 5300],
    "THz": [210, 390, 740, 1320, 2050, 2800, 3600],
    "Ambient IoT": [140, 270, 530, 950, 1500, 2150, 2900]
}

PUBLICATIONS_BY_DATABASE = {
    "IEEE Xplore": 45,
    "Google Scholar": 25,
    "Springer": 18,
    "Elsevier": 12
}

TOP_RESEARCH_INSTITUTIONS = [
    {"name": "Tsinghua University", "country": "China", "papers": 1420, "citations": 28400},
    {"name": "Nanyang Technological University (NTU)", "country": "Singapore", "papers": 1180, "citations": 24100},
    {"name": "ETH Zurich", "country": "Switzerland", "papers": 950, "citations": 19800},
    {"name": "KTH Royal Institute of Technology", "country": "Sweden", "papers": 870, "citations": 17200},
    {"name": "University of Surrey (ICS)", "country": "UK", "papers": 810, "citations": 15900},
    {"name": "Princeton University", "country": "USA", "papers": 760, "citations": 16400},
    {"name": "Bilkent & METU Joint 6G Lab", "country": "Turkey", "papers": 340, "citations": 6200}
]

TOP_PUBLISHING_COUNTRIES = {
    "China": 38,
    "United States": 24,
    "European Union (Germany/Sweden/UK)": 20,
    "South Korea": 9,
    "Japan": 5,
    "Turkey (Türk Telekom Ar-Ge & Universities)": 4
}

MOST_CITED_PAPERS = [
    {
        "title": "Integrated Sensing and Communications: Towards Dual-Functional Wireless Networks for 6G",
        "authors": "F. Liu, C. Masouros, A. Li, et al.",
        "journal": "IEEE Transactions on Communications",
        "year": 2022,
        "citations": 1840,
        "url": "https://ieeexplore.ieee.org"
    },
    {
        "title": "Reconfigurable Intelligent Surfaces for 6G: Architectures, Applications, and Open Issues",
        "authors": "Q. Wu, R. Zhang",
        "journal": "IEEE Wireless Communications",
        "year": 2021,
        "citations": 2350,
        "url": "https://ieeexplore.ieee.org"
    },
    {
        "title": "A Survey on Cell-Free Massive MIMO: Technical Challenges and 6G Deployment Roadmap",
        "authors": "E. Nayebi, A. Ashikhmin, R. R. Muller",
        "journal": "IEEE Access",
        "year": 2022,
        "citations": 1120,
        "url": "https://ieeexplore.ieee.org"
    },
    {
        "title": "AI-Native RAN for 6G: Deep Learning Frameworks in PHY and MAC Layers",
        "authors": "H. He, S. Jin, C. K. Wen",
        "journal": "IEEE Journal on Selected Areas in Communications",
        "year": 2023,
        "citations": 980,
        "url": "https://ieeexplore.ieee.org"
    }
]
