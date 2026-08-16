# Kullanım Kılavuzu

Türk Telekom **6G Technology & Patent Intelligence Platform** — Streamlit uygulaması.

## 1. Kurulum

```bash
git clone https://github.com/zeynep-ebrar-pala/6G-Teknoloji-Patent-Zekas--Platformu.git
cd 6G-Teknoloji-Patent-Zekas--Platformu
pip install -r requirements.txt
```

İsteğe bağlı AI için `.env.example` dosyasını `.env` olarak kopyalayın ve Groq veya Gemini anahtarını yazın. Anahtar olmadan da Ana Sayfa, 6G Teknolojileri, Patent Zekası, Yayın Trendleri ve Türk Telekom Görünümü açılır.

```bash
streamlit run app.py
```

Tarayıcıda `http://localhost:8501` açılır.

## 2. Menü

| Menü | Ne işe yarar |
|------|----------------|
| Ana Sayfa | 7 teknolojinin TRL radar haritası ve özet kartları |
| 6G Teknolojileri | Tanım, çalışma prensibi, blok diyagram, mimari, kullanım, avantaj/dezavantaj, dünya çalışmaları, TT senaryoları, TRL, kayıt sayımı grafikleri, referanslar |
| Patent Zekası | Nokia, Ericsson, Huawei, Samsung, Qualcomm filtreli patent analitiği |
| Yayın Trendleri | OpenAlex yıl / kurum / ülke grafikleri ve DOI doğrulamalı makaleler |
| Türk Telekom Görünümü | Saha senaryo çözümleyici |
| AI Asistan | «RIS nedir?» ve «NTN ile ISAC arasındaki fark» dahil sorular; TF-IDF + isteğe bağlı LLM |
| Hakkında | Amaç, yığın, 15 dakikalık sunum iskeleti |

Sol kenarda **Temel / Uzman** anlatım derinliği yalnızca 6G Teknolojileri sayfasını etkiler.

## 3. Patent Zekası

1. Üstteki firmayı seçin (`Tümü` veya şartnamedeki 5 firmadan biri).
2. Kayıt yoksa grafik çizilmez; sayı uydurulmaz.
3. Sekmeler: yıl trendi, konu + kelime bulutu, patent ağacı + yoğunluk, TF-IDF harita + ağ, patent listesi.
4. Her karttaki **Kaynakta Aç** Google Patents sayfasını açar.

Bu küme tam küresel portföy değildir; yalnızca Google Patents’ten doğrulanmış örnek kayıtlardır.

## 4. Yayın Trendleri

- Yıllık sayılar, kurumlar ve ülkeler OpenAlex API’den canlı gelir.
- API yanıt vermezse grafik gizlenir; statik tablo gösterilmez.
- Makale atıfları yalnızca OpenAlex `cited_by_count` alanındandır; yoksa «—» yazılır.
- OpenAlex, IEEE / Springer / Elsevier ve Google Scholar indeksli literatürü kapsar. Google Scholar ayrı bir API sunmaz.

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
