from components.tt_europe_views import render_tt_europe_patent_section
from components.tt_scenarios import render_tt_scenario_calculator
from components.ui_helpers import select_section
from i18n.core import get_lang, t

_TT_KEYS = ["footprint", "scenario"]
_labels = [t(f"tt_page.section.{k}") for k in _TT_KEYS]
_map = dict(zip(_labels, _TT_KEYS))
section = _map.get(
    select_section(t("tt_page.view"), _labels, key=f"tt_page_section_eu1_{get_lang()}"),
    _TT_KEYS[0],
)

if section == "scenario":
    render_tt_scenario_calculator()
else:
    render_tt_europe_patent_section()
