from components.tt_europe_views import render_tt_done_section
from components.tt_page_views import render_tt_roadmap_section
from components.ui_helpers import select_section
from i18n.core import get_lang, t

_TT_KEYS = ["done", "roadmap"]
_labels = [t(f"tt_page.section.{k}") for k in _TT_KEYS]
_map = dict(zip(_labels, _TT_KEYS))
section = _map.get(
    select_section(t("tt_page.view"), _labels, key=f"tt_page_section_v3_{get_lang()}"),
    _TT_KEYS[0],
)

if section == "done":
    render_tt_done_section()
else:
    render_tt_roadmap_section()
