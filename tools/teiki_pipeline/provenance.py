"""Provenance / reliability helpers."""

from __future__ import annotations

from typing import Any


def is_provenance(obj: Any) -> bool:
    """Return True for ProvenanceValue objects (not conflict value rows)."""
    if not isinstance(obj, dict) or "value" not in obj or "status" not in obj:
        return False
    # conflict.values[] entries use value+source(+status) and are not ProvenanceValue
    if "source" in obj and "rationale" not in obj and "tools" not in obj:
        return False
    return True


def check_inferred(obj: Any, path: str, errors: list[str]) -> None:
    """Recursively ensure inferred values have rationale and tools."""
    if is_provenance(obj):
        if obj.get("status") == "inferred":
            if not obj.get("rationale"):
                errors.append(f"{path}: inferred value missing rationale")
            tools = obj.get("tools")
            if not isinstance(tools, list) or len(tools) < 1:
                errors.append(f"{path}: inferred value missing tools")
        return
    if isinstance(obj, dict):
        for key, value in obj.items():
            check_inferred(value, f"{path}.{key}", errors)
    elif isinstance(obj, list):
        for i, value in enumerate(obj):
            check_inferred(value, f"{path}[{i}]", errors)


def provenance_value(value: Any, status: str = "original", **kwargs: Any) -> dict[str, Any]:
    out: dict[str, Any] = {"value": value, "status": status}
    out.update(kwargs)
    return out
