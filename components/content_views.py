"""
İki kademeli içerik gösterimi: temel katman, formül kartları, karşılaştırma, kullanım/TRL.
"""

from __future__ import annotations

from html import escape

import streamlit as st

from data.glossary import GLOSSARY, TRL_SCALE

_TEACH_LABELS = (
    ("problem", "Nedir / hangi problem?"),
    ("why_needed", "Neden gerekli?"),
    ("what", "Ne işe yarar?"),
    ("tt_impact", "Türk Telekom ve TRL"),
)


def is_beginner(view_mode: str) -> bool:
    return "Temel Seviye" in (view_mode or "")


def render_foundation_layer(tech: dict, *, compact: bool = False) -> None:
    """Temel kavramsal katman — uzman modda da atlanmaz."""
    fnd = tech.get("foundation") or {}
    if not fnd:
        return
    heading = "Kavramsal temel (sıkıştırılmış)" if compact else "Kavramsal temel — nedir, neden, nasıl"
    st.markdown(
        f"""<div class="dual-card-beginner">
<h4 style="margin-top:0;margin-bottom:14px;">{heading}</h4>
</div>""",
        unsafe_allow_html=True,
    )
    items = []
    for key, label in _TEACH_LABELS:
        text = fnd.get(key)
        if text:
            items.append(
                "<div class='teach-item'>"
                f"<div class='teach-label'>{escape(label)}</div>"
                f"<p>{escape(str(text))}</p></div>"
            )
    if items:
        st.markdown(f"<div class='teach-grid'>{''.join(items)}</div>", unsafe_allow_html=True)

    st.markdown(
        f"""<div class="glass-card">
<div class="teach-label">Zihinsel model</div>
<p style="color:#E2E8F0;line-height:1.65;margin:8px 0 0 0;">{escape(str(fnd.get('mental_model') or ''))}</p>
</div>""",
        unsafe_allow_html=True,
    )
    analogy = fnd.get("analogy")
    tech_map = fnd.get("analogy_technical_map")
    if analogy:
        st.markdown(
            f"""<div class="glass-card">
<div class="teach-label">Analoji</div>
<p style="color:#E2E8F0;line-height:1.65;margin:8px 0 12px 0;">{escape(str(analogy))}</p>
<div class="teach-label">Bu analojinin teknik karşılığı</div>
<p style="color:#CBD5E1;line-height:1.65;margin:8px 0 0 0;">{escape(str(tech_map or ''))}</p>
</div>""",
            unsafe_allow_html=True,
        )

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            f"""<div class="glass-card" style="border-left:4px solid #00C853;">
<div class="teach-label">Ne zaman kullanılır?</div>
<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.6;margin:8px 0 0 0;">{escape(str(fnd.get('when_used') or ''))}</p>
</div>""",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f"""<div class="glass-card" style="border-left:4px solid #FF5252;">
<div class="teach-label">Ne zaman kullanılmaz?</div>
<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.6;margin:8px 0 0 0;">{escape(str(fnd.get('when_not') or ''))}</p>
</div>""",
            unsafe_allow_html=True,
        )
    st.markdown(
        f"""<div class="glass-card">
<div class="teach-label">Neyle karıştırılmamalıdır?</div>
<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.65;margin:8px 0 12px 0;">{escape(str(fnd.get('not_to_confuse') or ''))}</p>
<div class="teach-label">Gerçekte nerede karşımıza çıkar?</div>
<p style="color:#CBD5E1;font-size:0.92rem;line-height:1.65;margin:8px 0 0 0;">{escape(str(fnd.get('real_world') or ''))}</p>
</div>""",
        unsafe_allow_html=True,
    )

    steps = fnd.get("how_steps") or []
    if steps and not compact:
        lis = "".join(f"<li style='margin-bottom:8px;line-height:1.55;'>{escape(str(s))}</li>" for s in steps)
        st.markdown(
            f"""<div class="glass-card">
<div class="teach-label">Nasıl çalışır? — adımlar</div>
<ol style="color:#E2E8F0;font-size:0.92rem;margin:10px 0 0 18px;padding:0;">{lis}</ol>
</div>""",
            unsafe_allow_html=True,
        )


def render_formula_cards(tech: dict) -> None:
    formulas = tech.get("formulas") or []
    if not formulas:
        legacy = tech.get("mathematical_foundation")
        if legacy:
            st.markdown(f"<div class='formula-box'>{legacy}</div>", unsafe_allow_html=True)
        return
    st.markdown("#### Matematiksel temel — sembol, birim, varsayım")
    st.caption(
        "Formül ezberletilmez: her sembolün fiziksel anlamı, neden bu biçim ve ne zaman geçerli olduğu yazılır."
    )
    for formula in formulas:
        st.markdown(
            f"""<div class="formula-card">
<div class="teach-label">Denklem</div>
<h4 style="color:#00E5FF;margin:6px 0 10px 0;">{escape(formula.get('name', 'Formül'))}</h4>
</div>""",
            unsafe_allow_html=True,
        )
        latex = formula.get("latex") or ""
        if latex:
            st.latex(latex)
        symbols = formula.get("symbols") or []
        if symbols:
            rows = "".join(
                "<tr>"
                f"<td class='sym'>{escape(s.get('symbol', ''))}</td>"
                f"<td>{escape(s.get('meaning', ''))}</td>"
                f"<td>{escape(s.get('unit', ''))}</td>"
                "</tr>"
                for s in symbols
            )
            st.markdown(
                f"""<table class="symbol-table">
<thead><tr><th>Sembol</th><th>Anlamı</th><th>Birim</th></tr></thead>
<tbody>{rows}</tbody>
</table>""",
                unsafe_allow_html=True,
            )
        blocks = (
            ("Ne anlatır?", formula.get("tells_us")),
            ("Neden bu biçim?", formula.get("why_this_form")),
            ("Ne zaman geçerli?", formula.get("when_valid")),
            ("Değişken artınca / azalınca", formula.get("if_variable_changes")),
            ("Varsayımlar ve sınır", formula.get("assumptions")),
            ("Basit nicel örnek", formula.get("simple_example")),
        )
        body = "".join(
            f"<p style='margin:0 0 10px 0;line-height:1.6;'><strong>{escape(title)}:</strong> {escape(str(text))}</p>"
            for title, text in blocks
            if text
        )
        if body:
            st.markdown(f"<div class='glass-card'>{body}</div>", unsafe_allow_html=True)


def render_comparison_table(tech: dict) -> None:
    cmp_ = tech.get("comparison") or {}
    rows = cmp_.get("rows") or []
    headers = cmp_.get("headers") or []
    if not rows or not headers:
        return
    st.markdown(f"#### {cmp_.get('title', 'Karşılaştırma')}")
    head = "".join(f"<th>{escape(h)}</th>" for h in headers)
    body = "".join(
        "<tr>" + "".join(f"<td>{escape(str(c))}</td>" for c in row) + "</tr>" for row in rows
    )
    st.markdown(
        f"""<div style="overflow-x:auto;">
<table class="compare-table">
<thead><tr>{head}</tr></thead>
<tbody>{body}</tbody>
</table>
</div>""",
        unsafe_allow_html=True,
    )


def render_use_cases(tech: dict, *, beginner: bool) -> None:
    st.markdown("### Kullanım alanları — mekanizma ve sınır")
    st.caption(
        "Her kart bir gerçek dünya işidir. Temel: ne işe yarar. Uzman: nasıl çalışır ve ne zaman kullanılmaz."
    )
    cols = st.columns(2)
    for idx, uc in enumerate(tech.get("use_cases") or []):
        if isinstance(uc, dict):
            title = uc.get("title", f"Senaryo #{idx+1}")
            desc = uc.get("description", "")
            how = uc.get("how", "")
            when_not = uc.get("when_not", "")
        else:
            title, desc, how, when_not = f"Senaryo #{idx+1}", str(uc), "", ""
        extra = ""
        if not beginner and (how or when_not):
            extra = (
                f"<p style='color:#94A3B8;font-size:0.84rem;margin:10px 0 0 0;line-height:1.5;'>"
                f"<strong style='color:#00E5FF;'>Nasıl:</strong> {escape(how)}</p>"
                if how
                else ""
            )
            if when_not:
                extra += (
                    f"<p style='color:#94A3B8;font-size:0.84rem;margin:8px 0 0 0;line-height:1.5;'>"
                    f"<strong style='color:#FFB020;'>Ne zaman değil:</strong> {escape(when_not)}</p>"
                )
        with cols[idx % 2]:
            st.markdown(
                f"""<div class="glass-card" style="margin-bottom:12px;border-left:4px solid #00E5FF;">
<h4 style="color:#00E5FF;margin:0 0 8px 0;">{escape(title)}</h4>
<p style="color:#E2E8F0;font-size:0.9rem;margin:0;line-height:1.55;">{escape(desc)}</p>
{extra}
</div>""",
                unsafe_allow_html=True,
            )


def render_adv_dis(tech: dict, *, beginner: bool) -> None:
    c_adv, c_dis = st.columns(2)
    adv_why = tech.get("adv_why") or []
    dis_why = tech.get("dis_why") or []
    with c_adv:
        st.markdown("### Avantajlar — neden kazanç?")
        items = []
        for i, adv in enumerate(tech.get("advantages") or []):
            why = adv_why[i] if (not beginner and i < len(adv_why)) else ""
            why_html = (
                f"<div style='color:#94A3B8;font-size:0.84rem;margin-top:4px;line-height:1.5;'>{escape(why)}</div>"
                if why
                else ""
            )
            items.append(
                f"<li style='margin-bottom:12px;line-height:1.5;'>"
                f"<strong style='color:#00C853;'>✓</strong> {escape(str(adv))}{why_html}</li>"
            )
        st.markdown(
            f"""<div class="glass-card" style="border-left:4px solid #00C853;">
<ul style="list-style:none;padding-left:0;margin:0;color:#E2E8F0;font-size:0.92rem;">
{''.join(items)}
</ul></div>""",
            unsafe_allow_html=True,
        )
    with c_dis:
        st.markdown("### Dezavantajlar — hangi problem doğurur?")
        items = []
        for i, dis in enumerate(tech.get("disadvantages") or []):
            why = dis_why[i] if (not beginner and i < len(dis_why)) else ""
            why_html = (
                f"<div style='color:#94A3B8;font-size:0.84rem;margin-top:4px;line-height:1.5;'>{escape(why)}</div>"
                if why
                else ""
            )
            items.append(
                f"<li style='margin-bottom:12px;line-height:1.5;'>"
                f"<strong style='color:#FF5252;'>✗</strong> {escape(str(dis))}{why_html}</li>"
            )
        st.markdown(
            f"""<div class="glass-card" style="border-left:4px solid #FF5252;">
<ul style="list-style:none;padding-left:0;margin:0;color:#E2E8F0;font-size:0.92rem;">
{''.join(items)}
</ul></div>""",
            unsafe_allow_html=True,
        )


def render_global_tt_trl(tech: dict, *, beginner: bool, trl_class: str) -> None:
    c_g, c_tt_box, c_t_level = st.columns([1, 1, 0.9])
    global_why = tech.get("global_why") or []
    tt_why = tech.get("tt_why") or []
    with c_g:
        st.markdown("### Dünyadaki çalışmalar")
        if beginner:
            st.caption("Bunlar isim listesi değil: her satır, özelliğin neden standart/araştırma gündeminde olduğunu söyler.")
        items = []
        for i, gr in enumerate(tech.get("global_research") or []):
            why = global_why[i] if i < len(global_why) else ""
            why_html = (
                f"<div style='color:#94A3B8;font-size:0.82rem;margin-top:4px;line-height:1.45;'>{escape(why)}</div>"
                if why
                else ""
            )
            items.append(
                f"<li style='margin-bottom:10px;line-height:1.5;'>"
                f"<span style='color:#00C2FF;'>🔹</span> <strong style='color:#FFFFFF;'>{escape(str(gr))}</strong>"
                f"{why_html}</li>"
            )
        st.markdown(
            f"""<div class="glass-card"><ul style="list-style:none;padding-left:0;margin:0;color:#E2E8F0;font-size:0.9rem;">
{''.join(items)}</ul></div>""",
            unsafe_allow_html=True,
        )
    with c_tt_box:
        st.markdown("### Türk Telekom senaryoları")
        st.caption("Problem → neden bu teknoloji → beklenen sonuç. Saha ölçümü değildir.")
        chunks = []
        for i, tt_sc in enumerate(tech.get("tt_scenarios") or []):
            why = tt_why[i] if i < len(tt_why) else ""
            why_html = (
                f"<span style='display:block;color:#94A3B8;font-size:0.82rem;margin-top:4px;'>{escape(why)}</span>"
                if why
                else ""
            )
            chunks.append(
                f"<p style='margin-bottom:12px;line-height:1.5;font-size:0.9rem;color:#E2E8F0;'>{tt_sc}{why_html}</p>"
            )
        st.markdown(
            f"""<div class="glass-card" style="border-left:4px solid #FFB020;">{''.join(chunks)}</div>""",
            unsafe_allow_html=True,
        )
    with c_t_level:
        st.markdown("### TRL değerlendirmesi")
        st.markdown(
            f"""<div class="glass-card" style="text-align:center;">
<span class="trl-pill {trl_class}" style="font-size:1.3rem;padding:10px 24px;">TRL {tech['trl']}</span>
<p style="color:#CBD5E1;font-size:0.88rem;margin-top:14px;line-height:1.5;text-align:left;">{escape(str(tech.get('trl_desc') or ''))}</p>
</div>""",
            unsafe_allow_html=True,
        )
        scale_rows = "".join(
            f"<tr><td style='white-space:nowrap;color:#00E5FF;font-weight:700;'>{escape(r['level'])}</td>"
            f"<td><strong>{escape(r['title'])}</strong> — {escape(r['meaning'])}</td></tr>"
            for r in TRL_SCALE
        )
        st.markdown(
            f"""<table class="symbol-table">
<thead><tr><th>Ölçek</th><th>{escape('TRL (Technology Readiness Level — Teknoloji Hazırlık Seviyesi)')}</th></tr></thead>
<tbody>{scale_rows}</tbody>
</table>""",
            unsafe_allow_html=True,
        )


def render_trl_explainer() -> None:
    trl = GLOSSARY["TRL"]
    st.markdown(
        f"""<div class="glass-card">
<h4 style="color:#00E5FF;margin-top:0;">TRL nedir?</h4>
<p style="font-size:0.92rem;color:#C8D1DC;line-height:1.65;">
<strong>{escape(trl['abbr'])} ({escape(trl['en'])} — {escape(trl['tr'])}):</strong>
{escape(trl['definition'])} {escape(trl['why'])}
</p>
<p style="font-size:0.88rem;color:#94A3B8;line-height:1.6;">
1 = temel ilke, 9 = gerçek görevde kanıtlanmış ürün. 6G yapı taşları aynı anda gelmez:
NTN diğerlerinden öndedir; THz hâlâ laboratuvardır. Notlar pazarlama vaadi değil, saha/standart olgunluğudur.
</p>
<ul style="font-size:0.88rem;color:#CBD5E1;padding-left:20px;line-height:1.7;">
<li><strong style="color:#00C853;">TRL 6 — sahaya en yakın:</strong> NTN — dağ, deniz, afet yedek hattı</li>
<li><strong style="color:#FFB020;">TRL 5 — prototip / ilgili ortam:</strong> RIS ve AI-RAN</li>
<li><strong style="color:#FF5252;">TRL 4 — laboratuvar bileşeni:</strong> ISAC, hücresiz MIMO, pilsiz IoT</li>
<li><strong style="color:#FF7043;">TRL 3 — kavram kanıtı:</strong> THz — rekor hız adayı, sokak şebekesi değil</li>
</ul>
</div>""",
        unsafe_allow_html=True,
    )


DIAGRAM_LEGENDS: dict[str, str] = {
    "isac": (
        "<strong>gNB</strong> (next-generation Node B — baz istasyonu) hem veri basar hem eko dinler. "
        "<strong>UE</strong> (User Equipment — kullanıcı cihazı) iletişim ucudur. "
        "<strong>AoA</strong> (Angle of Arrival — geliş açısı) dizi fazından yön; "
        "<strong>Doppler</strong> hızın radyal bileşenidir. Tx/Rx: aynı kutuda verici ve alıcı."
    ),
    "ris": (
        "<strong>Tx</strong> verici gNB, <strong>Rx</strong> kullanıcı UE. "
        "<strong>N-LoS</strong> (Non-Line-of-Sight — görüş hattı yok): bina doğrudan yolu keser; "
        "RIS faz kaydırarak alternatif yol açar. RIS kendi başına internet üretmez."
    ),
    "cell_free": (
        "<strong>AP</strong> (Access Point — erişim noktası) sokaktaki küçük radyodur. "
        "<strong>CPU</strong> ortak ön kodlamayı hesaplar. Kesikli çizgi <strong>fronthaul</strong> "
        "(ön bağlantı) fiberidir; yoksa hücresiz kazanç doğmaz."
    ),
    "thz": (
        "Soldan sağa spektrum: Sub-6 GHz kapsama, mmWave şehir kapasitesi, "
        "THz (0,1–10 THz) ultra geniş bant. Hortum genişler, menzil kısalır."
    ),
    "ai_ran": (
        "Nöral kodlayıcı/alıcı <strong>PHY</strong> (Physical layer — fiziksel katman) araştırma ucudur. "
        "Üretimde çoğu iş <strong>RIC</strong> xApp/rApp döngüsüdür. Turuncu yay: uçtan uca kayıp geri beslemesi."
    ),
    "ntn": (
        "<strong>LEO</strong> (Low Earth Orbit — alçak yörünge) ~500–1200 km. "
        "<strong>HAPS</strong> stratosfer (~20 km). Gateway yer kapısı; feeder link uyduyu karasal çekirdeğe bağlar. "
        "Direct-to-cell: çanak değil telefon."
    ),
    "ambient_iot": (
        "Okuyucu <strong>RF</strong> taşıyıcı basar (enerji + referans). Etiket rectenna ile DC üretir, "
        "backscatter ile biti yansıtır. Pil yok; menzil kırıntı güce bağlıdır."
    ),
}


def render_diagram_legend(tech_id: str) -> None:
    text = DIAGRAM_LEGENDS.get(tech_id)
    if not text:
        return
    st.markdown(
        f"""<div class="glass-card" style="margin-top:8px;">
<div class="teach-label">Diyagram terimleri</div>
<p style="color:#CBD5E1;font-size:0.88rem;line-height:1.6;margin:8px 0 0 0;">{text}</p>
</div>""",
        unsafe_allow_html=True,
    )
