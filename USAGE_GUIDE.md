# Türk Telekom 6G Technology & Patent Intelligence Platform
## Kullanım ve Canlıya Aktarım (Deployment) Kılavuzu

### 1. Yerel Kurulum & Çalıştırma (Local Setup)

1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install streamlit plotly pandas networkx scikit-learn
   ```

2. Uygulamayı başlatın:
   ```bash
   streamlit run app.py
   ```

3. **Giriş Ekranı (API Key Authentication)**:
   - Platform açıldığında kurumsal güvenlik kapısı sizden API Key isteyecektir.
   - Varsayılan Giriş Anahtarı: `TT-6G-2026-KEY` (veya kendi belirlenen API Key'iniz).

---

### 2. Streamlit Cloud ile Canlıya Aktarım (Deployment to Live)

1. Projeyi GitHub reponuza push edin:
   ```bash
   git init
   git add .
   git commit -m "Türk Telekom 6G Platform v2.0 Release"
   git remote add origin https://github.com/KULLANICI_ADI/6G-Intelligence-Platform.git
   git push -u origin main
   ```

2. [share.streamlit.io](https://share.streamlit.io) adresine gidin ve GitHub hesabınızla giriş yapın.
3. **"New app"** butonuna tıklayın:
   - **Repository:** `KULLANICI_ADI/6G-Intelligence-Platform`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. **Deploy!** butonuna basarak uygulamanızı canlıya alın.

---

### 3. Modül 1 — 6G Technology Explorer İçerik Haritası

Her teknoloji sayfasında staj projesinde istenen tüm bileşenler eksiksiz yer almaktadır:
- 📌 **Tanımı (Overview)**: Temel Seviye ve Uzman Seviyesi çift derinlikli özetler.
- ⚙️ **Çalışma prensibi**: Fiziksel ve RF sinyal işleme prensipleri.
- 🎨 **Blok diyagram animasyonu**: İnteraktif SVG / HTML5 animasyonlu mimari şemalar.
- 🏗️ **Sistem mimarisi**: PHY/MAC katmanları ve sinyal formülleri.
- 💡 **Kullanım alanları**: Otonom sürüş, dron takibi, akıllı şehirler, sağlık vb.
- ✅ **Avantajlar & ⚠️ Dezavantajlar**: Maddeler halinde teknik kıyaslamalar.
- 🌐 **Dünyadaki çalışmalar**: 3GPP Rel-18/19/20, Hexa-X II ve küresel testbed'ler.
- 🇹🇷 **Türk Telekom kullanım senaryoları**: İstanbul Boğazı deniz emniyeti, İHA koridorları, deprem RF enkaz algılama, kör nokta kapsama vb.
- 📊 **TRL Değerlendirmesi**: Teknoloji Hazırlık Seviyeleri (TRL 1-9).
- 📈 **Performans grafikleri**: Plotly interaktif 5G vs 6G kıyas grafikler.
- 🎬 **Kısa video**: Demonstrasyon & PoC simülasyon video Kartı.
- 📚 **Referans makaleler**: IEEE ve 3GPP standart belgeleri.
