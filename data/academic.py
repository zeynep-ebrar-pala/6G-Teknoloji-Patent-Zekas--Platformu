"""
Akademik yayın veri kümesi — DOI ile doğrulanabilir kayıtlar.
Kaynak hücreleri WoS ve Springer.
"""

ACADEMIC_DATA_SOURCE = (
    "Toplam adet: WoS Core Collection + Springer Meta API (yan yana, toplanmaz). "
    "Yıl / kurum / ülke / atıf: WoS Analyze Results, TS=(6G) AND konu, PY=2020-2026."
)

ACADEMIC_SOURCES = ["WoS", "Springer"]

# DOI ile doğrulanmış makaleler — uydurma atıf sayısı yok
MOST_CITED_PAPERS = [
    {
        "title": "Integrated Sensing and Communications: Toward Dual-Functional Wireless Networks for 6G and Beyond",
        "authors": "F. Liu, Y. Cui, C. Masouros, et al.",
        "journal": "IEEE Journal on Selected Areas in Communications",
        "year": 2022,
        "doi": "10.1109/jsac.2022.3156632",
        "topic": "ISAC",
        "source": "DOI",
        "source_url": "https://doi.org/10.1109/jsac.2022.3156632",
        "url": "https://doi.org/10.1109/jsac.2022.3156632",
    },
    {
        "title": "Towards Smart and Reconfigurable Environment: Intelligent Reflecting Surface Aided Wireless Network",
        "authors": "Q. Wu, R. Zhang",
        "journal": "IEEE Communications Magazine",
        "year": 2020,
        "doi": "10.1109/mcom.001.1900107",
        "topic": "RIS",
        "source": "DOI",
        "source_url": "https://doi.org/10.1109/mcom.001.1900107",
        "url": "https://doi.org/10.1109/mcom.001.1900107",
    },
    {
        "title": "Cell-Free Massive MIMO: A Survey",
        "authors": "S. Elhoushy, M. Ibrahim, W. Hamouda",
        "journal": "IEEE Communications Surveys & Tutorials",
        "year": 2022,
        "doi": "10.1109/comst.2021.3123267",
        "topic": "Cell-Free",
        "source": "DOI",
        "source_url": "https://doi.org/10.1109/comst.2021.3123267",
        "url": "https://doi.org/10.1109/comst.2021.3123267",
    },
    {
        "title": "Terahertz Band Communication: An Old Problem Revisited and Research Directions for the Next Decade",
        "authors": "I. F. Akyildiz, C. Han, Z. Hu, et al.",
        "journal": "IEEE Transactions on Communications",
        "year": 2022,
        "doi": "10.1109/tcomm.2022.3171800",
        "topic": "THz",
        "source": "DOI",
        "source_url": "https://doi.org/10.1109/tcomm.2022.3171800",
        "url": "https://doi.org/10.1109/tcomm.2022.3171800",
    },
    {
        "title": "Non-Terrestrial Networks in the 6G Era: Challenges and Opportunities",
        "authors": "M. Giordani, M. Zorzi",
        "journal": "IEEE Network",
        "year": 2021,
        "doi": "10.1109/mnet.011.2000493",
        "topic": "NTN",
        "source": "DOI",
        "source_url": "https://doi.org/10.1109/mnet.011.2000493",
        "url": "https://doi.org/10.1109/mnet.011.2000493",
    },
    {
        "title": "Reconfigurable Intelligent Surfaces for 6G Systems: Principles, Applications, and Research Directions",
        "authors": "C. Pan, H. Ren, K. Wang, et al.",
        "journal": "IEEE Communications Magazine",
        "year": 2021,
        "doi": "10.1109/mcom.001.2001076",
        "topic": "RIS",
        "source": "DOI",
        "source_url": "https://doi.org/10.1109/mcom.001.2001076",
        "url": "https://doi.org/10.1109/mcom.001.2001076",
    },
    {
        "title": "DRL-Based Joint Beamforming and Reflection Design for Secure RIS-Aided ISAC Systems",
        "authors": "H. Liu, L. Zheng, C. Zhai, et al.",
        "journal": "Telecommunication Systems",
        "year": 2025,
        "doi": "10.1007/s11235-025-01374-z",
        "topic": "RIS",
        "source": "Springer",
        "source_url": "https://doi.org/10.1007/s11235-025-01374-z",
        "url": "https://doi.org/10.1007/s11235-025-01374-z",
    },
    {
        "title": "Non-Terrestrial Networking for 6G: Evolution, Opportunities, and Future Directions",
        "authors": "F. Wang, S. Zhang, H. Yang, T. Q. S. Quek",
        "journal": "Engineering",
        "year": 2025,
        "doi": "10.1016/j.eng.2025.05.013",
        "topic": "NTN",
        "source": "DOI",
        "source_url": "https://doi.org/10.1016/j.eng.2025.05.013",
        "url": "https://doi.org/10.1016/j.eng.2025.05.013",
    },
]
