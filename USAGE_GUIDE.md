# Kullanım Kılavuzu

Türk Telekom **6G Technology & Patent Intelligence Platform** — Streamlit uygulaması.

## 1. Kurulum

```bash
git clone https://github.com/zeynep-ebrar-pala/6G-Teknoloji-Patent-Zekas--Platformu.git
cd 6G-Teknoloji-Patent-Zekas--Platformu
pip install -r requirements.txt
```

İsteğe bağlı AI için `.env.example` dosyasını `.env` olarak kopyalayın ve Groq veya Gemini anahtarını yazın. Anahtar olmadan da Ana Sayfa, 6G Teknoloji Rehberi, Patent Zekası, Akademik Yayın Analizi ve Türk Telekom Görünümü açılır.

```bash
streamlit run app.py
```

Tarayıcıda `http://localhost:8501` açılır.

## 2. Menü

| Menü | Ne işe yarar |
|------|----------------|
| Ana Sayfa | 7 teknolojinin TRL radar haritası ve özet kartları |
| 6G Teknoloji Rehberi | Tanım, çalışma prensibi, blok diyagram, mimari, kullanım, avantaj/dezavantaj, dünya çalışmaları, TT senaryoları, TRL, kayıt sayımı grafikleri, referanslar |
| Patent Zekası | Nokia–Intel (9 firma), yedi 6G konusu; Lens.org analitiği |
| Akademik Yayın Analizi | WoS Core Collection + Springer Meta API; DOI kartları |
| Türk Telekom Görünümü | Saha senaryo çözümleyici |
| AI Asistan | «RIS nedir?» ve «NTN ile ISAC arasındaki fark» dahil sorular; TF-IDF + isteğe bağlı LLM |
| Hakkında | Amaç, yığın, 15 dakikalık sunum iskeleti |

Sol kenarda **Temel / Uzman** anlatım derinliği Ana Sayfa girişini ve **6G Teknolojileri**nin tüm sekmelerini etkiler.
Uzman mod kavramsal temeli gizlemez; üstüne formül kartı, varsayım ve karşılaştırma ekler.
Patent özetleri ve DOI kayıtları kaynakta kilitlidir (yeniden yazılmaz).

## 3. Patent Zekası

1. Üstteki firmayı seçin (`Tümü` veya Nokia, Ericsson, Huawei, Samsung, Qualcomm, ZTE, NEC, NICT, Intel).
2. Konu kutusu yedi 6G Technology Explorer alanıdır (ISAC, RIS, Cell-Free, THz, AI-RAN, NTN, Ambient IoT). Ham «6G» aranmaz.
3. Kayıt yoksa grafik 0 gösterir veya gizlenir; Unclassified yoktur; sayı uydurulmaz.
4. Grafikler: en çok çalışan firmalar (API total), patent sayısı / yıl, konu dağılımı, radar, kelime bulutu, patent ağacı, yoğunluk, teknoloji haritası; ayrıca **Türk Telekom patent izi**.
5. Her karttaki **Kaynakta Aç** Lens.org kayıt sayfasını açar.
6. **Türk Telekom patent izi:** TT Avrupa’da RAN satıcısı değil, Türkiye operatörü + TTI toptandır. Harita yalnızca adı kaynakta geçen ülkeleri boyar (TTI first-mover 6 ülke; 19/24 iddiası boyanmaz). Netsia Inc. Google Patents; 921 milli başvuru çubuğa işlenmez.

Bu küme tam küresel portföy değildir. Firma çubuğu yedi konu × applicant Lens `total` değeridir. Diğer grafikler çekilen kayıttır (konu başı en fazla 100). İki katman toplanmaz.

## 4. Akademik Yayın Analizi

- Toplam adet: WoS Core Collection + Springer Meta API (örtüşme düşülmez).
- Yıl / trend: son 5 yıl (2022–2026). 2026 eksik yıldır.
- Kurum / ülke: her konu için WoS Analyze Results ilk 10 (sıra 1–10), sonra …, sonra Türkiye sırası. Altı konu toplanmaz.
- Türkiye WoS sırası: ilk 10’da yoksa tam sıra uydurulmaz; 10. ülke eşiği ve Springer 2022–2026 metin Turkey ayrı durur. Ülke listesinin Analyze Results penceresi PY=2020-2026’dır (yıllık ülke dilimi yok).
- Anahtar yoksa hücre —.
- **Türk Telekom yayın izi** sekmesi: kilitli DOI (TT bağlılığı) + resmi harita; operatör yayın API’si yoktur.

## 5. AI Asistan

- İsteğe bağlı Groq veya Gemini anahtarı.
- Anahtar yoksa «Anahtarsız devam et» ile sklearn TF-IDF yerel yanıt kullanılır.
- Asistan yalnızca platformdaki teknoloji metinleri, doğrulanmış patentler ve DOI’li makalelerden parça seçer.

## 6. Kaynak doğrulama

```bash
python scripts/verify_sources.py
```

Patent ve makale URL’lerinin HTTP erişilebilirliğini kontrol eder. Geçersiz kayıtlar `backend/data_validator.py` tarafından arayüzden çıkarılır.

## 7. Güvenlik

- `.env` Git’e eklenmez.
- API anahtarı yalnızca oturum belleğindedir.
- Uygulamanın geri kalanı anahtarsız çalışır.
