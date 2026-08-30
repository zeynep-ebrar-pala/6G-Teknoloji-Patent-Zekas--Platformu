"""Temel mod yüz metinleri — başlık + açıklama biçiminde render."""

from html import escape


def render_surface_item(item, *, accent: str = "#00C2FF") -> str:
    if isinstance(item, dict):
        title = str(item.get("title") or "").strip()
        body = str(item.get("body") or "").strip()
        if not title and not body:
            return ""
        title_html = (
            f"<strong style='color:#FFFFFF;'>{escape(title)}</strong>" if title else ""
        )
        body_html = (
            f"<div style='color:#CBD5E1;font-size:0.88rem;margin-top:6px;line-height:1.55;'>"
            f"{escape(body)}</div>"
            if body
            else ""
        )
        return (
            f"<li style='margin-bottom:14px;line-height:1.5;'>"
            f"<span style='color:{accent};'>🔹</span> {title_html}{body_html}</li>"
        )
    text = str(item).strip()
    if not text:
        return ""
    return (
        f"<li style='margin-bottom:10px;line-height:1.5;'>"
        f"<span style='color:{accent};'>🔹</span> "
        f"<strong style='color:#FFFFFF;'>{escape(text)}</strong></li>"
    )


def render_surface_block(item, *, border: str = "") -> str:
    if isinstance(item, dict):
        title = str(item.get("title") or "").strip()
        body = str(item.get("body") or "").strip()
        if not title and not body:
            return ""
        title_html = (
            f"<strong style='color:#FFB020;'>{escape(title)}</strong>" if title else ""
        )
        body_html = (
            f"<span style='display:block;color:#CBD5E1;font-size:0.88rem;margin-top:6px;line-height:1.55;'>"
            f"{escape(body)}</span>"
            if body
            else ""
        )
        return (
            f"<p style='margin-bottom:14px;line-height:1.5;font-size:0.9rem;color:#E2E8F0;'>"
            f"{title_html}{body_html}</p>"
        )
    text = str(item).strip()
    if not text:
        return ""
    return (
        f"<p style='margin-bottom:12px;line-height:1.5;font-size:0.9rem;color:#E2E8F0;'>"
        f"{escape(text)}</p>"
    )
