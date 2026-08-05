# 🇹🇷 Türk Telekom 6G Technology & Patent Intelligence Platform
## Modül 1 — 6G Technology Explorer

Bu proje, **Türk Telekom 6G Ar-Ge ekibinde ve yönetici sunumlarında** kullanılmak üzere tasarlanmış, 6G teknolojilerini hem 0 seviye hakimiyetteki kişilerin kolayca kavrayabileceği hem de 6G uzmanlarının akademik/teknik beklentilerini karşılayacak **çift katmanlı (Dual-Depth)** interaktif bir web platformudur.

---

## 🌳 Proje Ağacı (Directory Tree)

```text
MODUL1/
├── app.py                      # Ana Streamlit Giriş Noktası & Sayfa Yönlendirici (Frontend Entry)
├── styles.py                   # Türk Telekom Kurumsal Tasarım Kimliği & CSS Tema Katmanı
├── README.md                   # Proje Kılavuzu ve Ağaç Mimarisi Dokümantasyonu
│
├── data/
│   └── technologies.py         # 7 Temel 6G Teknolojisinin (ISAC, RIS, THz vb.) Veri Tabanı & Formülleri
│
├── backend/                    # ⚙️ BACKEND (Servis ve Hesaplama Katmanı)
│   ├── data_service.py         # Veri Erişim, Arama ve Filtreleme Servisleri (Data Access Service)
│   └── scenario_engine.py      # Türk Telekom Saha Dağıtım Hesaplama Motoru (Evaluation Engine)
│
└── components/                 # 🎨 FRONTEND (Görsel Arayüz Bileşenleri)
    ├── diagrams.py             # Canlı SVG/HTML Animasyonlu Sinyal ve Blok Diyagramları
    ├── charts.py               # Plotly Etkileşimli TRL Radar & Performans Grafikleri
    └── tt_scenarios.py         # Türk Telekom Senaryo Çözümleyici Kullanıcı Arayüzü
```

---

## 🏗️ Mimari Yapı (Frontend - Backend Ahengi)

Sistem modüler ve clean-architecture ilkelerine uygun şekilde ayrıştırılmıştır:

- **Frontend Katmanı (`app.py`, `styles.py`, `components/`)**:
  - Türk Telekom'un kurumsal renk paleti (Lacivert `#001E50`, Turkuaz `#00A8EC`) ile tasarlanmış Glassmorphism arayüz.
  - Sinyal akışlarını gösteren animasyonlu blok diyagramlar (`diagrams.py`) ve Plotly grafikleri (`charts.py`).
  - Çift katmanlı bilgi seçeneği (Temel Seviye / Uzman Modu).

- **Backend Katmanı (`backend/`, `data/`)**:
  - `data_service.py`: Teknolojileri filtrelere ve aramalara göre getiren servis katmanı.
  - `scenario_engine.py`: Kullanıcının seçtiği bölge, yoğunluk ve önceliğe göre en optimal Türk Telekom 6G mimari çözümlerini üreten motor.

---

## 🚀 Çalıştırma ve Kurulum

### 1. Gerekli Kütüphanelerin Yüklenmesi
```bash
pip install streamlit plotly pandas
```

### 2. Uygulamanın Başlatılması
```bash
streamlit run app.py
```

Uygulama başlatıldığında varsayılan olarak `http://localhost:8501` adresinde çalışacaktır.

---

## 📑 Kapsanan 7 Temel 6G Teknolojisi
1. **ISAC** (Integrated Sensing and Communication) - TRL 4
2. **RIS** (Reconfigurable Intelligent Surfaces) - TRL 5
3. **Cell-Free Massive MIMO** - TRL 4
4. **THz Communication** - TRL 3
5. **AI-Native RAN** - TRL 5
6. **NTN** (Non-Terrestrial Networks) - TRL 6
7. **Ambient IoT** (Zero-Energy Devices) - TRL 4

© 2026 Türk Telekom Ar-Ge Ekibi — Tüm Hakları Saklıdır.
