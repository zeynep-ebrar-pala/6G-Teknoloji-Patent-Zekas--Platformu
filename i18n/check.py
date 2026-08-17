"""Translation key parity checks for UI catalogs and content overlays."""

from __future__ import annotations

from typing import Any


def nested_keys(data: dict[str, Any], prefix: str = "") -> set[str]:
    out: set[str] = set()
    for key, val in data.items():
        dotted = f"{prefix}.{key}" if prefix else str(key)
        if isinstance(val, dict):
            out |= nested_keys(val, dotted)
        elif isinstance(val, list):
            out.add(f"{dotted}[]:{len(val)}")
            for i, item in enumerate(val):
                if isinstance(item, dict):
                    out |= nested_keys(item, f"{dotted}[{i}]")
        else:
            out.add(dotted)
    return out


def diff_keys(left: set[str], right: set[str], left_name: str, right_name: str) -> list[str]:
    problems: list[str] = []
    for k in sorted(left - right):
        problems.append(f"{right_name} missing: {k}")
    for k in sorted(right - left):
        problems.append(f"{right_name} extra: {k}")
    return problems


def check_ui_catalogs() -> list[str]:
    from i18n.core import assert_catalog_parity

    return assert_catalog_parity()


def check_beginner_copy() -> list[str]:
    from data.beginner_copy import BEGINNER_COPY as TR
    from data.beginner_copy_en import BEGINNER_COPY as EN

    return diff_keys(nested_keys(TR), nested_keys(EN), "tr", "en beginner_copy")


def check_expert_depth() -> list[str]:
    from data.expert_depth import EXPERT_DEPTH as TR
    from data.expert_depth_en import EXPERT_DEPTH as EN

    return diff_keys(nested_keys(TR), nested_keys(EN), "tr", "en expert_depth")


def check_tech_overlay() -> list[str]:
    from data.tech_overlay_en import TECH_OVERLAY_EN
    from data.technologies import TECHNOLOGIES

    fields = (
        "title",
        "trl_desc",
        "card_summary",
        "beginner_one_liner",
        "highlights",
        "executive_summary",
        "beginner_principle",
        "working_principle",
        "system_architecture",
        "use_cases",
        "advantages",
        "disadvantages",
        "global_research",
        "tt_scenarios",
    )
    problems: list[str] = []
    for tech_id, src in TECHNOLOGIES.items():
        extra = TECH_OVERLAY_EN.get(tech_id)
        if not extra:
            problems.append(f"en overlay missing tech: {tech_id}")
            continue
        for field in fields:
            if field not in extra:
                problems.append(f"{tech_id} overlay missing field: {field}")
                continue
            sv, ev = src.get(field), extra.get(field)
            if isinstance(sv, list) and isinstance(ev, list) and len(sv) != len(ev):
                problems.append(f"{tech_id}.{field} length {len(ev)} != TR {len(sv)}")
    return problems


def check_glossary_en() -> list[str]:
    from data.glossary import GLOSSARY
    from data.glossary_en import GLOSSARY_EN, TRL_SCALE_EN
    from data.glossary import TRL_SCALE

    problems = []
    for key in GLOSSARY:
        if key not in GLOSSARY_EN:
            problems.append(f"glossary_en missing: {key}")
        else:
            for field in ("definition", "why"):
                if field not in GLOSSARY_EN[key]:
                    problems.append(f"glossary_en.{key} missing {field}")
    if len(TRL_SCALE_EN) != len(TRL_SCALE):
        problems.append(f"TRL_SCALE_EN length {len(TRL_SCALE_EN)} != {len(TRL_SCALE)}")
    return problems


def run_all() -> list[str]:
    problems: list[str] = []
    problems += check_ui_catalogs()
    problems += check_beginner_copy()
    problems += check_expert_depth()
    problems += check_tech_overlay()
    problems += check_glossary_en()
    return problems
