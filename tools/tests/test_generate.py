import json
from pathlib import Path

from generate_app_data import generate
from generate_markdown import render


def test_generate_markdown_and_app_data(tmp_path: Path):
    data = {
        "schema_version": "1.0.0",
        "exam": "2026/03",
        "subject": "サンプル科目",
        "notes": "仮",
        "questions": [
            {
                "id": "EX-001",
                "unit": "イーハトーブ",
                "form": "short_answer",
                "stem": {
                    "value": "仮：『注文の多い料理店』の犬は何にたとえられるか。",
                    "status": "original",
                },
                "answer": {"value": "白熊", "status": "original"},
                "explanation": {
                    "value": "本文「白熊のような犬」。",
                    "status": "inferred",
                    "rationale": "青空文庫抜粋から要約",
                    "tools": ["manual"],
                },
                "sources": [{"file": "RAW/sample.pdf", "page": 1}],
                "tags": ["仮", "文学"],
            },
            {
                "id": "EX-002",
                "unit": "基礎数学",
                "form": "multiple_choice",
                "stem": {"value": "仮：図形なし。$1+1$ は？", "status": "original"},
                "choices": [
                    {"key": "A", "text": {"value": "1", "status": "original"}},
                    {"key": "B", "text": {"value": "2", "status": "original"}},
                ],
                "answer": {"value": "B", "status": "original"},
                "sources": [{"file": "RAW/sample.pdf", "page": 2}],
                "tags": ["仮", "math"],
            },
            {
                "id": "EX-003",
                "unit": "語彙",
                "form": "flashcard",
                "stem": {"value": "Ihatov", "status": "original"},
                "answer": {"value": "イーハトーブ", "status": "original"},
                "sources": [{"file": "RAW/sample.pdf", "page": 1}],
                "tags": ["english", "vocab", "仮"],
            },
        ],
    }
    md = render(data)
    assert "EX-001" in md
    assert "推定" in md

    out = tmp_path / "app_data"
    written = generate(data, out)
    assert (out / "flashcards.json").is_file()
    assert (out / "multiple_choice.json").is_file()
    assert (out / "words.csv").read_text(encoding="utf-8").splitlines()[0] == "word,japanese"
    assert "Ihatov" in (out / "words.csv").read_text(encoding="utf-8")
    assert json.loads(written["questions.json"].read_text(encoding="utf-8"))["subject"] == "サンプル科目"
