<div align="center">

# 6G Teknoloji Patent Zekâsı Platformu

**Türk Telekom 6G Technology, Patent Intelligence & Field Deployment Decision Platform**

![Streamlit](https://img.shields.io/badge/Streamlit-1.48+-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.18+-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

<p align="center">
  <strong>6G teknoloji keşfi, patent zekâsı, akademik literatür analizi ve saha karar desteği için tek portal.</strong>
</p>

**Author / Developer:** [Zeynep Ebrar Pala](https://github.com/zeynep-ebrar-pala)

**GitHub Repository:** [zeynep-ebrar-pala/6G-Teknoloji-Patent-Zekas--Platformu](https://github.com/zeynep-ebrar-pala/6G-Teknoloji-Patent-Zekas--Platformu)

</div>

---

## 1. Proje Adı

**6G Teknoloji Patent Zekâsı Platformu** (Türk Telekom 6G Ar-Ge Portalı)

## 2. Proje Amacı

6G kablosuz teknolojilerini yönetici ve Ar-Ge uzmanı perspektifinden sunmak; patent ve akademik literatür verilerini **doğrulanabilir kaynaklardan** toplayarak stratejik karar desteği sağlamak.

## 3. Projenin Kapsamı

- 7 temel 6G teknolojisinin TRL haritası ve detaylı keşif modülü
- Google Patents üzerinden doğrulanmış patent analitiği
- OpenAlex + DOI ile doğrulanmış akademik yayın analizi
- Türk Telekom saha dağıtım senaryo çözümleyici
- Groq / Gemini ile isteğe bağlı AI asistan (yalnızca doğrulanmış veri üzerinde yorum; uygulama anahtarsız açılır)

## 4. Temel Özellikler

| Özellik | Açıklama |
|---------|----------|
| Dual-Depth görünüm | Temel (nedir/neden/nasıl) + Uzman (denklem, varsayım); uzman temel katmanı atlamaz |
| Source-locked veri | Patent ve makale kayıtları gerçek source_url ile bağlı |
| Canlı OpenAlex trendleri | Statik uydurma sayı yok |
| Kaynakta Aç ↗ | Patent ve makaleler tarayıcıda gerçek kaynağa açılır |
| Groq / Gemini | Yalnızca AI Asistan; anahtar `.env` veya oturumda, frontend'e sızmaz |

## 5. Sistem Mimarisi

```text
Gerçek External Source (Google Patents, OpenAlex, DOI)
        ↓
Raw Data (data/patents.py, data/academic.py)
        ↓
Validation (backend/data_validator.py)
        ↓
Normalized Data
        ↓
Service Layer (backend/*_service.py)
        ↓
Analysis / LLM (yorumlama — veri icat etmez)
        ↓
Streamlit Frontend (components/*, app.py)
        ↓
"Kaynakta Aç ↗" → Gerçek tarayıcı navigasyonu
```

## 6. Modüller

| Modül | İçerik |
|-------|--------|
| Ana Sayfa | TRL radar, 7 teknoloji KPI kartları |
| 6G Teknolojileri | Kavramsal temel, formül kartları, karşılaştırma, TT senaryoları, kayıt sayımı |
| Patent Zekası | Yıl, konu, kelime bulutu, ağaç, yoğunluk, TF-IDF harita, Google Patents listesi |
| Yayın Trendleri | OpenAlex yıl / kurum / ülke; DOI-doğrulamalı makaleler |
| Türk Telekom Görünümü | Avrupa’daki yer (doğrulanmış harita) + bölge/yoğunluk/önceliğe göre mimari önerisi |
| AI Asistan | TF-IDF yerel geri getirme + isteğe bağlı Groq/Gemini |
| Hakkında | Amaç, yığın, sunum iskeleti |

## 7. Kullanılan Teknolojiler

- **Python 3.9+**, **Streamlit**, **Plotly**, **Pandas**, **Matplotlib**, **NetworkX**, **WordCloud**, **scikit-learn**
- **python-dotenv**, **groq**, **google-genai** (AI Asistan, isteğe bağlı)
- **OpenAlex REST API**, **Google Patents**, **DOI (IEEE / Springer / Elsevier)**

## 8. Frontend

Streamlit tabanlı tek sayfa uygulaması (`app.py`). UI bileşenleri `components/` altında:

- `auth_view.py` — isteğe bağlı Groq/Gemini (yalnızca AI Asistan)
- `patent_views.py`, `academic_views.py` — Patent Zekası / Yayın Trendleri
- `tt_scenarios.py` — Saha senaryo çözümleyici
- `about_view.py` — Hakkında
- `ui_helpers.py` — Kaynak linkleri, boş/hata durumları
- `charts.py`, `diagrams.py` — Grafikler

Ayrı bir React/npm build yoktur; `streamlit run app.py` frontend'i başlatır.

Adım adım kullanım: [USAGE_GUIDE.md](USAGE_GUIDE.md).

## 9. Backend

`backend/` servis katmanı:

| Dosya | Görev |
|-------|-------|
| `config.py` | `.env` yükleme |
| `auth_service.py` | Groq/Gemini API doğrulama |
| `data_validator.py` | Source-locked kayıt filtresi |
| `openalex_client.py` | Canlı OpenAlex sorguları |
| `patent_service.py` | Patent metrikleri (gerçek kayıtlardan) |
| `academic_service.py` | Akademik metrikler + DOI zenginleştirme |
| `scenario_engine.py` | TT saha senaryo motoru |
| `ai_assistant_service.py` | LLM yorumlama (veri icat etmez) |

## 10. Groq Entegrasyonu

- Ortam değişkeni: `GROQ_API_KEY`
- Giriş ekranında anahtar doğrulanır (`backend/auth_service.py`)
- AI asistan Groq modelleri ile doğrulanmış platform verisini yorumlar
- Anahtar kaynak kodda veya tarayıcı bundle'ında bulunmaz

## 11. Gemini Entegrasyonu

- Ortam değişkeni: `GEMINI_API_KEY`
- Giriş ekranında alternatif sağlayıcı olarak seçilebilir
- `DEFAULT_AI_PROVIDER=gemini` ile varsayılan yapılabilir

## 12. Environment Kurulumu

```bash
cp .env.example .env
```

## 13. `.env` Kurulumu

```env
GROQ_API_KEY=gsk_your_groq_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
DEFAULT_AI_PROVIDER=groq
```

- `.env` Git'e eklenmez (`.gitignore`)
- `.env.example` yalnızca placeholder içerir

## 14. Lokal Kurulum

```bash
git clone https://github.com/zeynep-ebrar-pala/6G-Teknoloji-Patent-Zekas--Platformu.git
cd 6G-Teknoloji-Patent-Zekas--Platformu
pip install -r requirements.txt
cp .env.example .env
# .env dosyasına API anahtarınızı girin
```

## 15. Frontend Çalıştırma

```bash
streamlit run app.py
```

Uygulama `http://localhost:8501` adresinde açılır.

## 16. Backend Çalıştırma

Bu proje ayrı bir HTTP API sunucusu kullanmaz. Backend, Streamlit uygulaması içinde Python servis katmanı olarak çalışır (`backend/`). Tüm modüller `app.py` üzerinden yüklenir.

## 17. API Yapısı

| Katman | Arayüz |
|--------|--------|
| Auth | `AuthService.validate_groq()` / `validate_gemini()` |
| Patent | `PatentService.get_summary()`, `get_top_patents()`, `get_network_edges()` |
| Akademik | `AcademicService.get_tech_publication_trends_df()`, `get_most_cited_papers()` |
| OpenAlex | `fetch_publication_trends()`, `fetch_work_by_doi()` |
| Senaryo | `ScenarioEngine.recommend()` |

## 18. Veri Doğrulama Yaklaşımı

1. Ham kayıt `data/` dosyalarında tutulur
2. `backend/data_validator.py` zorunlu alanları ve URL host'unu kontrol eder
3. Geçersiz kayıtlar production UI'da gösterilmez
4. `scripts/verify_sources.py` ile HTTP erişilebilirlik testi yapılabilir

## 19. Patent Veri Kaynakları

- [Google Patents](https://patents.google.com) — her patent kartında doğrudan patent sayfası
- USPTO publication number formatı (US*, WO*)

## 20. Akademik Veri Kaynakları

- [OpenAlex](https://openalex.org) — trend sayıları ve atıf güncellemesi
- DOI → IEEE Xplore / Crossref yayıncı sayfaları

## 21. Halüsinasyon Önleme Yaklaşımı

- LLM patent/makale/DOI/URL **icat etmez**
- LLM görevi: analiz, özetleme, sınıflandırma, karşılaştırma
- Tüm metrikler doğrulanmış kayıt kümesinden hesaplanır
- OpenAlex erişilemezse trend grafiği gizlenir; statik sayı kullanılmaz

## 22. Proje Klasör Yapısı

```text
MODUL1/
├── app.py                    # Ana giriş noktası
├── styles.py
├── requirements.txt
├── USAGE_GUIDE.md
├── .env.example
├── backend/
│   ├── config.py
│   ├── auth_service.py
│   ├── data_validator.py
│   ├── openalex_client.py
│   ├── patent_service.py
│   ├── academic_service.py
│   ├── scenario_engine.py
│   └── ai_assistant_service.py
├── components/
│   ├── auth_view.py
│   ├── ai_chat_view.py
│   ├── patent_views.py
│   ├── academic_views.py
│   ├── tt_scenarios.py
│   ├── about_view.py
│   ├── content_views.py
│   ├── ui_helpers.py
│   ├── charts.py
│   └── diagrams.py
├── data/
│   ├── technologies.py
│   ├── beginner_copy.py
│   ├── expert_depth.py
│   ├── glossary.py
│   ├── patents.py
│   └── academic.py
└── scripts/
    └── verify_sources.py
```

## 23. Güvenlik

- API anahtarları yalnızca `.env` ve oturum state'inde
- Frontend bundle'da secret yok
- `.env` `.gitignore`'da
- Hard-coded credential araması: `grep -r "gsk_" .` (yalnızca placeholder)

## 24. Kullanım Alanları

Telekom Ar-Ge, 6G standardizasyon, patent araştırması, rakip analizi, akademik literatür taraması, teknoloji trend analizi, stratejik karar destek, saha planlama, teknoloji olgunluğu (TRL) değerlendirmesi.

## 25. Uygulama Senaryoları

Modül 1'de her teknoloji için gerçek dünya senaryoları `{title, description}` formatında açıklanır. Sahte başarı oranı veya istatistik içermez.

## 26. GitHub Repository

https://github.com/zeynep-ebrar-pala/6G-Teknoloji-Patent-Zekas--Platformu

## 27. Yazar Bilgisi

**Zeynep Ebrar Pala** — Geliştirici / Yazar

© 2026 · Türk Telekom 6G Ar-Ge Staj Projesi

---

## Veri Doğrulama Testi

```bash
python scripts/verify_sources.py
```

Patent ve makale URL'lerinin HTTP erişilebilirliğini kontrol eder.

## Lisans

Bu platform Türk Telekom 6G Ar-Ge kapsamında geliştirilmiştir. Tüm hakları saklıdır.
