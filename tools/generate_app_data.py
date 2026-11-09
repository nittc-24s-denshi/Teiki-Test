#!/usr/bin/env python3
"""Generate app-facing datasets from structured questions JSON.

Outputs (into --out-dir):
  flashcards.json, multiple_choice.json, cloze.json, words.csv, questions.json (copy)
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any


_CLOZE_RE = re.compile(r"\{\{(.+?)\}\}|【(.+?)】|（\s*）|\(\s*\)")


def _pv(obj: Any) -> tuple[Any, str]:
    if isinstance(obj, dict) and "value" in obj:
        return obj.get("value"), str(obj.get("status", "original"))
    return obj, "original"


def generate(data: dict[str, Any], out_dir: Path) -> dict[str, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    questions = data.get("questions") or []

    flashcards = []
    multiple_choice = []
    cloze = []
    words_rows: list[dict[str, str]] = []

    for q in questions:
        stem, stem_st = _pv(q.get("stem"))
        ans, ans_st = _pv(q.get("answer"))
        expl, expl_st = _pv(q.get("explanation"))
        base = {
            "id": q.get("id"),
            "unit": q.get("unit"),
            "form": q.get("form"),
            "tags": q.get("tags") or [],
            "stem": stem,
            "stem_status": stem_st,
            "answer": ans,
            "answer_status": ans_st,
            "explanation": expl,
            "explanation_status": expl_st,
            "figures": q.get("figures") or [],
            "sources": q.get("sources") or [],
            "conflicts": q.get("conflicts") or [],
        }

        flashcards.append(
            {
                **base,
                "front": stem,
                "back": ans,
            }
        )

        if q.get("form") == "multiple_choice" or q.get("choices"):
            choices = []
            for c in q.get("choices") or []:
                text, st = _pv(c.get("text"))
                choices.append({"key": c.get("key"), "text": text, "status": st})
            multiple_choice.append({**base, "choices": choices})

        stem_s = str(stem or "")
        if q.get("form") == "cloze" or _CLOZE_RE.search(stem_s):
            cloze.append({**base, "template": stem_s})

        # English-ish flashcard → words.csv (word,japanese)
        tags = {t.lower() for t in (q.get("tags") or [])}
        if "english" in tags or "vocab" in tags or "単語" in (q.get("tags") or []):
            words_rows.append({"word": str(stem or ""), "japanese": str(ans or "")})

    written: dict[str, Path] = {}
    mapping = {
        "flashcards.json": flashcards,
        "multiple_choice.json": multiple_choice,
        "cloze.json": cloze,
    }
    for name, payload in mapping.items():
        path = out_dir / name
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        written[name] = path

    csv_path = out_dir / "words.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["word", "japanese"])
        writer.writeheader()
        writer.writerows(words_rows)
    written["words.csv"] = csv_path

    # Copy canonical structured file for the Question_Bank app
    qpath = out_dir / "questions.json"
    qpath.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    written["questions.json"] = qpath
    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument(
        "--also-copy-to",
        type=Path,
        default=None,
        help="Optional extra directory (e.g. Web_App/Question_Bank/data)",
    )
    args = parser.parse_args(argv)

    data = json.loads(args.input.read_text(encoding="utf-8"))
    written = generate(data, args.out_dir)
    if args.also_copy_to:
        args.also_copy_to.mkdir(parents=True, exist_ok=True)
        for path in written.values():
            shutil.copy2(path, args.also_copy_to / path.name)
    print(f"OK: wrote {len(written)} files → {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
