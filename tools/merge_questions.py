#!/usr/bin/env python3
"""Merge multiple structured (or raw) question JSON files.

Detects duplicates by id or similar stems; conflicting answers go into conflicts.
"""

from __future__ import annotations

import argparse
import json
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from teiki_pipeline.normalize import stems_similar  # noqa: E402


def load_questions(path: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return {}, data
    if isinstance(data, dict) and "questions" in data:
        meta = {k: v for k, v in data.items() if k != "questions"}
        return meta, list(data.get("questions") or [])
    raise ValueError(f"Unrecognized JSON shape: {path}")


def _stem_text(q: dict[str, Any]) -> str:
    stem = q.get("stem")
    if isinstance(stem, dict):
        return str(stem.get("value", ""))
    return str(stem or "")


def _answer_value(q: dict[str, Any]) -> Any:
    ans = q.get("answer")
    if isinstance(ans, dict):
        return ans.get("value")
    return ans


def _source_label(q: dict[str, Any], fallback: str) -> str:
    sources = q.get("sources") or []
    if sources and isinstance(sources[0], dict):
        f = sources[0].get("file", fallback)
        p = sources[0].get("page")
        return f"{f}:p{p}" if p else str(f)
    return fallback


def merge_question_lists(
    batches: list[tuple[str, list[dict[str, Any]]]],
) -> list[dict[str, Any]]:
    merged: list[dict[str, Any]] = []

    for origin, questions in batches:
        for q in questions:
            q = deepcopy(q)
            matched_idx = None
            qid = q.get("id")
            for i, existing in enumerate(merged):
                if qid and existing.get("id") == qid:
                    matched_idx = i
                    break
                if stems_similar(_stem_text(existing), _stem_text(q)):
                    matched_idx = i
                    break

            if matched_idx is None:
                merged.append(q)
                continue

            existing = merged[matched_idx]
            a_old = _answer_value(existing)
            a_new = _answer_value(q)
            if a_old is not None and a_new is not None and a_old != a_new:
                conflicts = list(existing.get("conflicts") or [])
                conflicts.append(
                    {
                        "field": "answer",
                        "values": [
                            {
                                "value": a_old,
                                "source": _source_label(existing, "existing"),
                                "status": (existing.get("answer") or {}).get("status")
                                if isinstance(existing.get("answer"), dict)
                                else "unverified",
                            },
                            {
                                "value": a_new,
                                "source": _source_label(q, origin),
                                "status": (q.get("answer") or {}).get("status")
                                if isinstance(q.get("answer"), dict)
                                else "unverified",
                            },
                        ],
                        "reason": "同一または類似問題で解答が不一致",
                    }
                )
                existing["conflicts"] = conflicts

            # Prefer filling empty fields from the new copy
            for key in ("explanation", "unit", "form", "tags", "figures", "choices"):
                if not existing.get(key) and q.get(key):
                    existing[key] = deepcopy(q[key])
            if q.get("sources"):
                existing_sources = list(existing.get("sources") or [])
                for s in q["sources"]:
                    if s not in existing_sources:
                        existing_sources.append(s)
                existing["sources"] = existing_sources
            if q.get("corrections"):
                existing["corrections"] = list(existing.get("corrections") or []) + deepcopy(
                    q["corrections"]
                )

    return merged


def merge_files(paths: list[Path], output: Path, *, exam: str | None, subject: str | None) -> dict:
    batches: list[tuple[str, list[dict[str, Any]]]] = []
    meta: dict[str, Any] = {
        "schema_version": "1.0.0",
        "exam": exam or "2026/03",
        "subject": subject or "unknown",
        "notes": "merged by tools/merge_questions.py",
    }
    for path in paths:
        file_meta, questions = load_questions(path)
        for k, v in file_meta.items():
            if k in ("exam", "subject", "schema_version") and v:
                meta[k] = v
        batches.append((path.name, questions))

    if exam:
        meta["exam"] = exam
    if subject:
        meta["subject"] = subject

    meta["questions"] = merge_question_lists(batches)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return meta


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", nargs="+", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--exam", default=None)
    parser.add_argument("--subject", default=None)
    args = parser.parse_args(argv)

    try:
        result = merge_files(args.inputs, args.output, exam=args.exam, subject=args.subject)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    n_conflict = sum(1 for q in result["questions"] if q.get("conflicts"))
    print(
        f"OK: {len(result['questions'])} questions "
        f"({n_conflict} with conflicts) → {args.output}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
