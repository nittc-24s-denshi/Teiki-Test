#!/usr/bin/env python3
"""Build examples/pipeline_sample end-to-end (PDF → structured → app data)."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]
TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))

from generate_app_data import generate  # noqa: E402
from generate_markdown import render  # noqa: E402
from merge_questions import merge_files  # noqa: E402
from pdf_process import process_pdf  # noqa: E402
from validate_schema import validate  # noqa: E402

SAMPLE = ROOT / "examples" / "pipeline_sample"
SCHEMA = ROOT / "schema" / "questions.schema.json"
APP_DATA = ROOT / "Web_App" / "Question_Bank" / "data"


def make_pdf(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    doc = fitz.open()
    p1 = doc.new_page()
    p1.insert_text(
        (50, 72),
        "仮・イーハトーブ sample print",
        fontsize=14,
    )
    p1.insert_text(
        (50, 110),
        "Q1. 白熊のような犬を連れた紳士は何人か。",
        fontsize=12,
    )
    p1.insert_text((50, 140), "Ans: 二人", fontsize=12)
    p2 = doc.new_page()
    p2.insert_text((50, 72), "仮 math page", fontsize=14)
    p2.insert_text((50, 110), "Q2. Compute 3+4.", fontsize=12)
    p2.insert_text((50, 140), "Ans: 7", fontsize=12)
    doc.save(path)
    doc.close()


def write_partial_questions(out_dir: Path) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    a = {
        "schema_version": "1.0.0",
        "exam": "2026/03",
        "subject": "サンプル科目（仮）",
        "questions": [
            {
                "id": "SAMPLE-IHATOV-001",
                "unit": "イーハトーブ文学（仮）",
                "form": "short_answer",
                "stem": {
                    "value": "仮：二人の若い紳士が連れていた、白熊のような動物は何か。",
                    "status": "original",
                },
                "answer": {"value": "犬", "status": "original"},
                "explanation": {
                    "value": "『注文の多い料理店』冒頭「白熊のような犬を二疋」。",
                    "status": "inferred",
                    "rationale": "青空文庫パブリックドメイン抜粋からの要約",
                    "tools": ["manual"],
                },
                "sources": [{"file": "RAW/sample_ihatov.pdf", "page": 1}],
                "tags": ["仮", "イーハトーブ"],
                "corrections": [
                    {
                        "field": "stem.value",
                        "before": "白熊の様な",
                        "after": "白熊のような",
                        "reason": "現代仮名遣いに統一",
                    }
                ],
            }
        ],
    }
    b = {
        "schema_version": "1.0.0",
        "exam": "2026/03",
        "subject": "サンプル科目（仮）",
        "questions": [
            {
                "id": "SAMPLE-IHATOV-001b",
                "unit": "イーハトーブ文学（仮）",
                "form": "short_answer",
                "stem": {
                    "value": "仮：二人の若い紳士が連れていた、白熊のような動物は何か。",
                    "status": "original",
                },
                "answer": {
                    "value": "犬（二疋）",
                    "status": "inferred",
                    "rationale": "別プリントでは頭数も解答に含めていた",
                    "tools": ["Gemini"],
                },
                "sources": [{"file": "RAW/sample_ihatov_alt.pdf", "page": 1}],
                "tags": ["仮", "イーハトーブ"],
            },
            {
                "id": "SAMPLE-MATH-001",
                "unit": "基礎計算（仮）",
                "form": "calculation",
                "stem": {
                    "value": "仮：次を計算せよ。 $3+4$",
                    "status": "original",
                },
                "answer": {"value": "$7$", "status": "original"},
                "explanation": {
                    "value": "整数の和。検算: $7-4=3$。",
                    "status": "original",
                },
                "sources": [{"file": "RAW/sample_ihatov.pdf", "page": 2}],
                "tags": ["仮", "math"],
            },
            {
                "id": "SAMPLE-MC-001",
                "unit": "基礎計算（仮）",
                "form": "multiple_choice",
                "stem": {
                    "value": "仮：$1+1$ の値はどれか。",
                    "status": "original",
                },
                "choices": [
                    {"key": "A", "text": {"value": "$0$", "status": "original"}},
                    {"key": "B", "text": {"value": "$1$", "status": "original"}},
                    {"key": "C", "text": {"value": "$2$", "status": "original"}},
                    {"key": "D", "text": {"value": "$3$", "status": "original"}},
                ],
                "answer": {"value": "C", "status": "original"},
                "sources": [{"file": "RAW/sample_ihatov.pdf", "page": 2}],
                "tags": ["仮", "math"],
            },
            {
                "id": "SAMPLE-EN-001",
                "unit": "語彙（仮）",
                "form": "flashcard",
                "stem": {"value": "Ihatov", "status": "original"},
                "answer": {"value": "イーハトーブ", "status": "original"},
                "sources": [{"file": "RAW/sample_ihatov.pdf", "page": 1}],
                "tags": ["仮", "english", "vocab"],
            },
            {
                "id": "SAMPLE-CLOZE-001",
                "unit": "イーハトーブ文学（仮）",
                "form": "cloze",
                "stem": {
                    "value": "仮：ぜんたい、ここらの山は{{怪しからん}}ね。",
                    "status": "original",
                },
                "answer": {
                    "value": "怪しからん",
                    "status": "unverified",
                },
                "sources": [{"file": "RAW/sample_ihatov.pdf", "page": 1}],
                "tags": ["仮", "cloze"],
            },
        ],
    }
    pa = out_dir / "partial_a.json"
    pb = out_dir / "partial_b.json"
    pa.write_text(json.dumps(a, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    pb.write_text(json.dumps(b, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return [pa, pb]


def main() -> int:
    raw_pdf = SAMPLE / "RAW" / "sample_ihatov.pdf"
    make_pdf(raw_pdf)

    pipeline_dir = SAMPLE / "pipeline"
    process_pdf(raw_pdf, pipeline_dir, dpi=100, extract_text=True, source_id="sample_ihatov")

    partials = write_partial_questions(SAMPLE / "pipeline" / "questions_raw")
    structured = SAMPLE / "structured" / "questions.json"
    merge_files(
        partials,
        structured,
        exam="2026/03",
        subject="サンプル科目（仮）",
    )

    # Stamp metadata without personal info
    data = json.loads(structured.read_text(encoding="utf-8"))
    data["generated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    data["notes"] = (
        "仮サンプル。本文は宮沢賢治『注文の多い料理店』（パブリックドメイン）由来の設問と自作の簡単な数式。"
    )
    structured.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    errors = validate(SCHEMA, structured)
    if errors:
        print("VALIDATION FAILED:", file=sys.stderr)
        for e in errors:
            print(" ", e, file=sys.stderr)
        return 1

    md_path = SAMPLE / "structured" / "まとめ_構造化.md"
    md_path.write_text(render(data), encoding="utf-8")

    app_dir = SAMPLE / "app_data"
    generate(data, app_dir)
    APP_DATA.mkdir(parents=True, exist_ok=True)
    generate(data, APP_DATA)

    status = {
        "exam": "2026/03",
        "subject": "サンプル科目（仮）",
        "updated": data["generated_at"],
        "pipeline": {
            "raw_ingested": True,
            "pages_split": True,
            "transcribed": True,
            "questions_split": True,
            "filled": True,
            "merged": True,
            "corrected": True,
            "structured": True,
            "validated": True,
        },
        "notes": "examples/pipeline_sample の通し実行結果。公式範囲ではない。",
    }
    (SAMPLE / "status.json").write_text(
        json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print("OK: sample pipeline complete")
    print(f"  structured: {structured}")
    print(f"  app data:   {APP_DATA}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
