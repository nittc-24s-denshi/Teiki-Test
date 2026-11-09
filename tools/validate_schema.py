#!/usr/bin/env python3
"""Validate structured questions JSON against schema + provenance rules."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

# Allow running from tools/ without installing a package
sys.path.insert(0, str(Path(__file__).resolve().parent))
from teiki_pipeline.provenance import check_inferred  # noqa: E402


def load_json(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def validate(
    schema_path: Path,
    data_path: Path,
    *,
    check_files: bool = False,
    base_dir: Path | None = None,
) -> list[str]:
    schema = load_json(schema_path)
    data = load_json(data_path)
    errors: list[str] = []

    validator = Draft202012Validator(schema)
    for err in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        loc = "/".join(str(p) for p in err.path) or "(root)"
        errors.append(f"schema:{loc}: {err.message}")

    questions = data.get("questions") if isinstance(data, dict) else None
    if isinstance(questions, list):
        ids: set[str] = set()
        for i, q in enumerate(questions):
            if not isinstance(q, dict):
                continue
            qid = q.get("id")
            if isinstance(qid, str):
                if qid in ids:
                    errors.append(f"questions[{i}].id: duplicate id '{qid}'")
                ids.add(qid)
            check_inferred(q, f"questions[{i}]", errors)
            if check_files:
                root = base_dir or data_path.parent
                for j, fig in enumerate(q.get("figures") or []):
                    if not isinstance(fig, dict):
                        continue
                    rel = fig.get("path")
                    if not rel:
                        continue
                    path = Path(rel)
                    if not path.is_absolute():
                        path = root / path
                    if not path.is_file():
                        errors.append(
                            f"questions[{i}].figures[{j}].path: file not found: {rel}"
                        )
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schema", type=Path, required=True)
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--check-files", action="store_true")
    parser.add_argument(
        "--base-dir",
        type=Path,
        default=None,
        help="Base directory for relative figure paths",
    )
    args = parser.parse_args(argv)

    errors = validate(
        args.schema,
        args.data,
        check_files=args.check_files,
        base_dir=args.base_dir,
    )
    if errors:
        print(f"FAIL: {len(errors)} error(s)", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    print(f"OK: {args.data}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
