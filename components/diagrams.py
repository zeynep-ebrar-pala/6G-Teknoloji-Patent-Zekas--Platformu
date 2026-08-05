"""
 Türk Telekom 6G Platform - Interactive HTML/SVG Diagrams Module
 Provides custom animated signal propagation and architecture diagrams for 6G technologies.
"""

import streamlit as st

def render_technology_diagram(tech_id: str):
    """Renders animated interactive SVG block diagram based on tech_id."""
    
    css_style = "<style>html, body { margin: 0; padding: 0; background: transparent; overflow: hidden; box-sizing: border-box; font-family: sans-serif; }</style>"
    
    diagrams = {
        "isac": f"""
        {css_style}
        <div style="background: rgba(11, 19, 43, 0.95); border: 1.5px solid #00A8EC; border-radius: 12px; padding: 12px; text-align: center; box-sizing: border-box;">
            <svg width="100%" height="200" viewBox="0 0 700 200" xmlns="http://www.w3.org/2000/svg">
                <defs>
                    <linearGradient id="commWave" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" stop-color="#00A8EC" stop-opacity="0.8"/>
                        <stop offset="100%" stop-color="#0066B3" stop-opacity="0.2"/>
                    </linearGradient>
                    <linearGradient id="radarWave" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" stop-color="#10B981" stop-opacity="0.9"/>
                        <stop offset="100%" stop-color="#34D399" stop-opacity="0.2"/>
                    </linearGradient>
                </defs>
                <!-- Base Station Node -->
                <rect x="50" y="60" width="100" height="75" rx="10" fill="#001E50" stroke="#00A8EC" stroke-width="2"/>
                <text x="100" y="93" fill="#FFFFFF" font-family="sans-serif" font-weight="bold" font-size="14" text-anchor="middle">6G gNB</text>
                <text x="100" y="113" fill="#00A8EC" font-family="sans-serif" font-size="11" text-anchor="middle">(ISAC Tx/Rx)</text>
                
                <!-- Communication Link -->
                <path d="M 150 80 Q 300 50 440 80" fill="none" stroke="url(#commWave)" stroke-width="4" stroke-dasharray="8 4">
                    <animate attributeName="stroke-dashoffset" from="24" to="0" dur="1.5s" repeatCount="indefinite" />
                </path>
                <text x="300" y="55" fill="#38BDF8" font-size="12" font-weight="bold">İletişim Dalgası (Veri Transferi)</text>
                
                <!-- User Device Node -->
                <rect x="450" y="60" width="90" height="55" rx="8" fill="#1E293B" stroke="#38BDF8" stroke-width="2"/>
                <text x="495" y="93" fill="#FFFFFF" font-family="sans-serif" font-size="12" text-anchor="middle">Kullanıcı (UE)</text>
                
                <!-- Sensing Waveform (Tx) -->
                <path d="M 150 120 L 340 155" fill="none" stroke="#10B981" stroke-width="3" stroke-dasharray="6 3">
                    <animate attributeName="stroke-dashoffset" from="18" to="0" dur="1s" repeatCount="indefinite" />
                </path>
                
                <!-- Target Object (Drone/Vehicle) -->
                <circle cx="370" cy="160" r="20" fill="#0F172A" stroke="#10B981" stroke-width="2"/>
                <text x="370" y="164" fill="#10B981" font-size="15" text-anchor="middle">🛸</text>
                
                <!-- Echo Waveform (Rx Backscatter) -->
                <path d="M 360 150 L 155 110" fill="none" stroke="#F59E0B" stroke-width="3" stroke-dasharray="4 2">
                    <animate attributeName="stroke-dashoffset" from="0" to="12" dur="1s" repeatCount="indefinite" />
                </path>
                <text x="240" y="160" fill="#FCD34D" font-size="11">Radar Yankısı (AoA / Doppler / Mesafe)</text>
            </svg>
            <div style="color: #94A3B8; font-size: 0.82rem; margin-top: 4px;">
                <strong>İnteraktif Sinyal Akışı:</strong> Mavi çizgi haberleşme verisini, yeşil-turuncu çizgi ise hedef algılama radar yankısını gösterir.
            </div>
        </div>
        """,

        "ris": f"""
        {css_style}
        <div style="background: rgba(11, 19, 43, 0.95); border: 1.5px solid #00A8EC; border-radius: 12px; padding: 12px; text-align: center; box-sizing: border-box;">
            <svg width="100%" height="200" viewBox="0 0 700 200" xmlns="http://www.w3.org/2000/svg">
                <!-- Transmitter -->
                <rect x="40" y="120" width="90" height="55" rx="8" fill="#001E50" stroke="#00A8EC" stroke-width="2"/>
                <text x="85" y="153" fill="#FFF" font-weight="bold" font-size="13" text-anchor="middle">6G Verici (Tx)</text>

                <!-- Obstacle (Building) -->
                <rect x="220" y="100" width="80" height="90" fill="#1E293B" stroke="#475569" stroke-width="2"/>
                <text x="260" y="148" fill="#94A3B8" font-size="12" text-anchor="middle">Bina (Engelleme)</text>
                <path d="M 130 148 L 220 148" stroke="#EF4444" stroke-width="3" stroke-dasharray="4 4"/>
                <text x="175" y="138" fill="#FCA5A5" font-size="10">Engellendi (N-LoS)</text>

                <!-- RIS Surface -->
                <rect x="320" y="15" width="160" height="35" rx="6" fill="#0284C7" stroke="#38BDF8" stroke-width="2"/>
                <text x="400" y="37" fill="#FFF" font-weight="bold" font-size="13" text-anchor="middle">Akıllı Yüzey (RIS Ayna)</text>
                
                <!-- Incoming Beam to RIS -->
                <path d="M 130 130 L 340 50" fill="none" stroke="#00A8EC" stroke-width="3.5" stroke-dasharray="6 3">
                    <animate attributeName="stroke-dashoffset" from="18" to="0" dur="1.2s" repeatCount="indefinite" />
                </path>
                
                <!-- Reflected Beam to Receiver -->
                <path d="M 440 50 L 570 130" fill="none" stroke="#10B981" stroke-width="3.5" stroke-dasharray="6 3">
                    <animate attributeName="stroke-dashoffset" from="18" to="0" dur="1.2s" repeatCount="indefinite" />
                </path>
                
                <!-- Receiver -->
                <rect x="560" y="120" width="90" height="55" rx="8" fill="#001E50" stroke="#10B981" stroke-width="2"/>
                <text x="605" y="153" fill="#FFF" font-weight="bold" font-size="13" text-anchor="middle">Kullanıcı (Rx)</text>
            </svg>
            <div style="color: #94A3B8; font-size: 0.82rem; margin-top: 4px;">
                <strong>RIS Yansıma Prensipleri:</strong> Doğrudan yol bina ile engellenmişken, RIS gelen radyo dalgasının fazını kaydırarak sinyali kullanıcıya odaklar.
            </div>
        </div>
        """,

        "cell_free": f"""
        {css_style}
        <div style="background: rgba(11, 19, 43, 0.95); border: 1.5px solid #00A8EC; border-radius: 12px; padding: 12px; text-align: center; box-sizing: border-box;">
            <svg width="100%" height="200" viewBox="0 0 700 200" xmlns="http://www.w3.org/2000/svg">
                <!-- Central Cloud CPU -->
                <rect x="280" y="12" width="140" height="38" rx="19" fill="#0066B3" stroke="#00A8EC" stroke-width="2"/>
                <text x="350" y="36" fill="#FFF" font-weight="bold" font-size="13" text-anchor="middle">Merkezi İşlemci (CPU)</text>
                
                <!-- Access Points (AP 1, 2, 3) -->
                <circle cx="100" cy="100" r="20" fill="#001E50" stroke="#38BDF8" stroke-width="2"/>
                <text x="100" y="104" fill="#FFF" font-size="11" text-anchor="middle">AP 1</text>

                <circle cx="350" cy="100" r="20" fill="#001E50" stroke="#38BDF8" stroke-width="2"/>
                <text x="350" y="104" fill="#FFF" font-size="11" text-anchor="middle">AP 2</text>

                <circle cx="600" cy="100" r="20" fill="#001E50" stroke="#38BDF8" stroke-width="2"/>
                <text x="600" y="104" fill="#FFF" font-size="11" text-anchor="middle">AP 3</text>
                
                <!-- Fronthaul Fiber Links -->
                <line x1="290" y1="40" x2="115" y2="85" stroke="#00A8EC" stroke-width="2" stroke-dasharray="3 3"/>
                <line x1="350" y1="50" x2="350" y2="80" stroke="#00A8EC" stroke-width="2" stroke-dasharray="3 3"/>
                <line x1="410" y1="40" x2="585" y2="85" stroke="#00A8EC" stroke-width="2" stroke-dasharray="3 3"/>

                <!-- Coordinated Beams to Single User -->
                <path d="M 115 115 L 320 170" stroke="#34D399" stroke-width="3" stroke-dasharray="5 3">
                    <animate attributeName="stroke-dashoffset" from="15" to="0" dur="1s" repeatCount="indefinite" />
                </path>
                <path d="M 350 120 L 350 160" stroke="#34D399" stroke-width="3" stroke-dasharray="5 3">
                    <animate attributeName="stroke-dashoffset" from="15" to="0" dur="1s" repeatCount="indefinite" />
                </path>
                <path d="M 585 115 L 380 170" stroke="#34D399" stroke-width="3" stroke-dasharray="5 3">
                    <animate attributeName="stroke-dashoffset" from="15" to="0" dur="1s" repeatCount="indefinite" />
                </path>

                <!-- User Node -->
                <rect x="315" y="160" width="70" height="32" rx="6" fill="#1E293B" stroke="#34D399" stroke-width="2"/>
                <text x="350" y="181" fill="#FFF" font-weight="bold" font-size="12" text-anchor="middle">Kullanıcı</text>
            </svg>
            <div style="color: #94A3B8; font-size: 0.82rem; margin-top: 4px;">
                <strong>Hücresiz Yapı:</strong> Hücre sınırı yok. Tüm dağıtık AP'ler fiber ön bağlantı ile tek bir kullanıcıyı aynı anda besler.
            </div>
        </div>
        """,

        "thz": f"""
        {css_style}
        <div style="background: rgba(11, 19, 43, 0.95); border: 1.5px solid #00A8EC; border-radius: 12px; padding: 12px; text-align: center; box-sizing: border-box;">
            <svg width="100%" height="200" viewBox="0 0 700 200" xmlns="http://www.w3.org/2000/svg">
                <!-- Spectrum Bar -->
                <rect x="50" y="35" width="600" height="30" rx="6" fill="url(#spectrumGrad)" stroke="#334155"/>
                <defs>
                    <linearGradient id="spectrumGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" stop-color="#3B82F6"/>
                        <stop offset="40%" stop-color="#06B6D4"/>
                        <stop offset="70%" stop-color="#8B5CF6"/>
                        <stop offset="100%" stop-color="#EC4899"/>
                    </linearGradient>
                </defs>
                <text x="100" y="55" fill="#FFF" font-size="11" font-weight="bold">4G/5G (Sub-6GHz)</text>
                <text x="300" y="55" fill="#FFF" font-size="11" font-weight="bold">mmWave (28-60GHz)</text>
                <text x="540" y="55" fill="#FFF" font-size="12" font-weight="bold">6G THz Bandı (0.1-10 THz)</text>

                <!-- THz Data Pipe -->
                <rect x="150" y="100" width="400" height="65" rx="12" fill="#090D16" stroke="#8B5CF6" stroke-width="2"/>
                <path d="M 170 132 Q 270 110 370 132 T 530 132" fill="none" stroke="#EC4899" stroke-width="4">
                    <animate attributeName="stroke-dasharray" values="1,15; 15,15; 1,15" dur="1s" repeatCount="indefinite"/>
                </path>
                <text x="350" y="127" fill="#F472B6" font-weight="bold" font-size="15" text-anchor="middle">1 Terabit / saniye Veri Hızı</text>
                <text x="350" y="148" fill="#94A3B8" font-size="11" text-anchor="middle">0.1 - 10 THz Ultra Geniş Bant Genişliği</text>
            </svg>
            <div style="color: #94A3B8; font-size: 0.82rem; margin-top: 4px;">
                <strong>Terahertz Spektrumu:</strong> Kızılötesi ile mmWave arasındaki ultra geniş bant alanını temsil eder.
            </div>
        </div>
        """,

        "ai_ran": f"""
        {css_style}
        <div style="background: rgba(11, 19, 43, 0.95); border: 1.5px solid #00A8EC; border-radius: 12px; padding: 12px; text-align: center; box-sizing: border-box;">
            <svg width="100%" height="200" viewBox="0 0 700 200" xmlns="http://www.w3.org/2000/svg">
                <!-- Neural Encoder (Tx) -->
                <rect x="60" y="60" width="140" height="75" rx="10" fill="#001E50" stroke="#8B5CF6" stroke-width="2"/>
                <text x="130" y="93" fill="#FFF" font-weight="bold" font-size="13" text-anchor="middle">Nöral Kodlayıcı</text>
                <text x="130" y="113" fill="#A78BFA" font-size="11" text-anchor="middle">(Derin Öğrenmeli Verici)</text>

                <!-- Channel (Environment) -->
                <rect x="270" y="70" width="160" height="55" rx="8" fill="#1E293B" stroke="#475569" opacity="0.9"/>
                <text x="350" y="93" fill="#FFF" font-weight="bold" font-size="12" text-anchor="middle">Fiziksel Kanal</text>
                <text x="350" y="111" fill="#94A3B8" font-size="10" text-anchor="middle">+ Gürültü & Sönümlenme</text>

                <!-- Neural Decoder (Rx) -->
                <rect x="500" y="60" width="140" height="75" rx="10" fill="#001E50" stroke="#10B981" stroke-width="2"/>
                <text x="570" y="93" fill="#FFF" font-weight="bold" font-size="13" text-anchor="middle">Nöral Alıcı</text>
                <text x="570" y="113" fill="#34D399" font-size="11" text-anchor="middle">(Derin Öğrenmeli Alıcı)</text>

                <!-- Loss Feedback Loop -->
                <path d="M 570 135 Q 350 190 130 135" fill="none" stroke="#F59E0B" stroke-width="2.5" stroke-dasharray="6 3">
                    <animate attributeName="stroke-dashoffset" from="18" to="0" dur="1.5s" repeatCount="indefinite"/>
                </path>
                <text x="350" y="177" fill="#FCD34D" font-size="11" font-weight="bold" text-anchor="middle">Uçtan Uca Geri Besleme & Kayıp Fonksiyonu (End-to-End Loss)</text>
            </svg>
            <div style="color: #94A3B8; font-size: 0.82rem; margin-top: 4px;">
                <strong>Oto-Kodlayıcı Mimari:</strong> İnsan tasarımlı modülasyon yerine derin öğrenme ile öğrenilen katmanlar.
            </div>
        </div>
        """,

        "ntn": f"""
        {css_style}
        <div style="background: rgba(11, 19, 43, 0.95); border: 1.5px solid #00A8EC; border-radius: 12px; padding: 12px; text-align: center; box-sizing: border-box;">
            <svg width="100%" height="200" viewBox="0 0 700 200" xmlns="http://www.w3.org/2000/svg">
                <!-- LEO Satellite -->
                <text x="350" y="40" font-size="28" text-anchor="middle">🛰️</text>
                <text x="350" y="58" fill="#38BDF8" font-weight="bold" font-size="12" text-anchor="middle">LEO Uydu Takımı (600 km)</text>

                <!-- HAPS Stratosphere -->
                <text x="180" y="100" font-size="20" text-anchor="middle">🎈</text>
                <text x="180" y="117" fill="#FCD34D" font-size="11" text-anchor="middle">HAPS Zeplin (20 km)</text>

                <!-- Ground Station -->
                <rect x="520" y="140" width="100" height="40" rx="6" fill="#001E50" stroke="#00A8EC" stroke-width="2"/>
                <text x="570" y="165" fill="#FFF" font-weight="bold" font-size="11" text-anchor="middle">TT Uydu Gateway</text>

                <!-- Direct-to-Cell Device -->
                <rect x="80" y="150" width="70" height="32" rx="6" fill="#1E293B" stroke="#34D399" stroke-width="2"/>
                <text x="115" y="171" fill="#FFF" font-weight="bold" font-size="11" text-anchor="middle">Akıllı Tel</text>

                <!-- Beams -->
                <line x1="330" y1="45" x2="120" y2="150" stroke="#38BDF8" stroke-width="2.5" stroke-dasharray="4 2"/>
                <line x1="370" y1="45" x2="540" y2="140" stroke="#00A8EC" stroke-width="2.5" stroke-dasharray="4 2"/>
            </svg>
            <div style="color: #94A3B8; font-size: 0.82rem; margin-top: 4px;">
                <strong>Çok Katmanlı Ulaşım:</strong> Uydu -> HAPS -> Karasal Ağ entegrasyonu ile kesintisiz kapsama.
            </div>
        </div>
        """,

        "ambient_iot": f"""
        {css_style}
        <div style="background: rgba(11, 19, 43, 0.95); border: 1.5px solid #00A8EC; border-radius: 12px; padding: 12px; text-align: center; box-sizing: border-box;">
            <svg width="100%" height="200" viewBox="0 0 700 200" xmlns="http://www.w3.org/2000/svg">
                <!-- 6G Reader / gNB -->
                <rect x="60" y="60" width="120" height="75" rx="10" fill="#001E50" stroke="#00A8EC" stroke-width="2"/>
                <text x="120" y="93" fill="#FFF" font-weight="bold" font-size="13" text-anchor="middle">6G Okuyucu</text>
                <text x="120" y="113" fill="#00A8EC" font-size="11" text-anchor="middle">(Sinyal Üreteci)</text>

                <!-- Carrier RF Wave -->
                <path d="M 180 85 L 440 85" stroke="#00A8EC" stroke-width="3.5" stroke-dasharray="8 4">
                    <animate attributeName="stroke-dashoffset" from="24" to="0" dur="1s" repeatCount="indefinite"/>
                </path>
                <text x="310" y="75" fill="#38BDF8" font-size="11" font-weight="bold" text-anchor="middle">Gelen Taşıyıcı RF Sinyali (Enerji Kaynağı)</text>

                <!-- Backscattered Modulated Wave -->
                <path d="M 440 115 L 180 115" stroke="#34D399" stroke-width="3" stroke-dasharray="6 3">
                    <animate attributeName="stroke-dashoffset" from="0" to="18" dur="1s" repeatCount="indefinite"/>
                </path>
                <text x="310" y="133" fill="#34D399" font-size="11" font-weight="bold" text-anchor="middle">Yansıyan Modüle Veri (Geri Saçılım)</text>

                <!-- Ambient Passive Tag -->
                <rect x="450" y="65" width="150" height="65" rx="10" fill="#0F172A" stroke="#34D399" stroke-width="2"/>
                <text x="525" y="93" fill="#34D399" font-weight="bold" font-size="13" text-anchor="middle">🔋 Pilsiz IoT Etiketi</text>
                <text x="525" y="113" fill="#94A3B8" font-size="10" text-anchor="middle">(RF Enerji Hasadı)</text>
            </svg>
            <div style="color: #94A3B8; font-size: 0.82rem; margin-top: 4px;">
                <strong>Geri Saçılım Prensibi:</strong> Cihaz pil içermez; gelen RF dalgasını modüle edip yansıtarak veri iletir.
            </div>
        </div>
        """
    }

    diagram_code = diagrams.get(tech_id, "<p style='color: white;'>Diyagram bulunamadı.</p>")
    st.components.v1.html(diagram_code, height=380)
