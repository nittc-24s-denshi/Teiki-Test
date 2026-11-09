"""Text normalization helpers for duplicate detection."""

from __future__ import annotations

import re
import unicodedata


_SPACE_RE = re.compile(r"\s+")
_PUNCT_RE = re.compile(r"[、。．，,.!！?？:：;；\"'「」『』（）()\[\]{}]")


def normalize_stem(text: str) -> str:
    """Normalize question stem for fuzzy duplicate comparison."""
    if text is None:
        return ""
    s = unicodedata.normalize("NFKC", str(text)).lower()
    s = _PUNCT_RE.sub("", s)
    s = _SPACE_RE.sub("", s)
    return s


def stems_similar(a: str, b: str, *, min_len: int = 12) -> bool:
    """Return True if normalized stems are equal or one contains the other."""
    na, nb = normalize_stem(a), normalize_stem(b)
    if not na or not nb:
        return False
    if na == nb:
        return True
    if len(na) >= min_len and len(nb) >= min_len and (na in nb or nb in na):
        return True
    return False
