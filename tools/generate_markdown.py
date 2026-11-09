#!/usr/bin/env python3
"""Generate a human-readable Markdown summary from structured questions JSON."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def _pv(obj: Any) -> tuple[str, str]:
    if isinstance(obj, dict) and "value" in obj:
        return str(obj.get("value", "")), str(obj.get("status", ""))
    return str(obj or ""), ""


def _badge(status: str) -> str:
    if status == "inferred":
        return " `推定`"
    if status == "unverified":
        return " `未確認`"
    if status == "original":
        return " `原文`"
    return ""


def render(data: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append(f"# {data.get('subject', '')} — 構造化問題まとめ")
    lines.append("")
    lines.append(f"- 試験: `{data.get('exam', '')}`")
    lines.append(f"- schema: `{data.get('schema_version', '')}`")
    if data.get("notes"):
        lines.append(f"- 注記: {data['notes']}")
    lines.append("")
    lines.append("> このファイルは `tools/generate_markdown.py` により生成。既存ノートを置換しないこと。")
    lines.append("")

    for q in data.get("questions") or []:
        stem, stem_st = _pv(q.get("stem"))
        ans, ans_st = _pv(q.get("answer"))
        expl, expl_st = _pv(q.get("explanation"))
        lines.append(f"## {q.get('id', '?')} — {q.get('unit', '')}")
        lines.append("")
        lines.append(f"- 形式: `{q.get('form', '')}`")
        if q.get("tags"):
            lines.append(f"- タグ: {', '.join(q['tags'])}")
        sources = q.get("sources") or []
        if sources:
            src_bits = []
            for s in sources:
                bit = s.get("file", "")
                if s.get("page"):
                    bit += f" p.{s['page']}"
                src_bits.append(bit)
            lines.append(f"- 出典: {'; '.join(src_bits)}")
        lines.append("")
        lines.append(f"**問題**{_badge(stem_st)}")
        lines.append("")
        lines.append(stem)
        lines.append("")
        if q.get("choices"):
            lines.append("**選択肢**")
            lines.append("")
            for c in q["choices"]:
                text, st = _pv(c.get("text"))
                lines.append(f"- ({c.get('key', '?')}) {text}{_badge(st)}")
            lines.append("")
        lines.append(f"**解答**{_badge(ans_st)}")
        lines.append("")
        lines.append(ans)
        lines.append("")
        if expl:
            lines.append(f"**解説**{_badge(expl_st)}")
            lines.append("")
            lines.append(expl)
            lines.append("")
        if q.get("corrections"):
            lines.append("**訂正**")
            lines.append("")
            for corr in q["corrections"]:
                lines.append(
                    f"- `{corr.get('field')}`: {corr.get('before')!r} → "
                    f"{corr.get('after')!r}（{corr.get('reason')}）"
                )
            lines.append("")
        if q.get("conflicts"):
            lines.append("**食い違い (conflicts)**")
            lines.append("")
            for conf in q["conflicts"]:
                lines.append(f"- フィールド `{conf.get('field')}`: {conf.get('reason')}")
                for v in conf.get("values") or []:
                    lines.append(f"  - {v.get('source')}: {v.get('value')!r}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)

    data = json.loads(args.input.read_text(encoding="utf-8"))
    text = render(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    print(f"OK: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
