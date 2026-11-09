import json
from pathlib import Path

from merge_questions import merge_files
from validate_schema import validate

REPO = Path(__file__).resolve().parents[2]
SCHEMA = REPO / "schema" / "questions.schema.json"


def _q(qid: str, stem: str, answer: str, status: str = "original", **extra):
    ans = {"value": answer, "status": status}
    if status == "inferred":
        ans["rationale"] = extra.pop("rationale", "test")
        ans["tools"] = extra.pop("tools", ["pytest"])
    return {
        "id": qid,
        "unit": "sample",
        "form": "short_answer",
        "stem": {"value": stem, "status": "original"},
        "answer": ans,
        "sources": [{"file": "RAW/a.pdf", "page": 1}],
        "tags": ["仮"],
        **extra,
    }


def test_validate_ok(tmp_path: Path):
    data = {
        "schema_version": "1.0.0",
        "exam": "2026/03",
        "subject": "サンプル",
        "questions": [_q("S-001", "問1", "答1")],
    }
    path = tmp_path / "q.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    assert validate(SCHEMA, path) == []


def test_validate_inferred_requires_rationale(tmp_path: Path):
    data = {
        "schema_version": "1.0.0",
        "exam": "2026/03",
        "subject": "サンプル",
        "questions": [
            {
                "id": "S-002",
                "unit": "sample",
                "form": "short_answer",
                "stem": {"value": "x", "status": "original"},
                "answer": {"value": "y", "status": "inferred"},
                "sources": [{"file": "a.pdf"}],
            }
        ],
    }
    path = tmp_path / "bad.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    errors = validate(SCHEMA, path)
    assert any("inferred" in e for e in errors)


def test_merge_records_conflict(tmp_path: Path):
    a = {
        "schema_version": "1.0.0",
        "exam": "2026/03",
        "subject": "サンプル",
        "questions": [_q("S-010", "イーハトーブの風は何を運ぶか", "夢")],
    }
    b = {
        "schema_version": "1.0.0",
        "exam": "2026/03",
        "subject": "サンプル",
        "questions": [_q("S-011", "イーハトーブの風は何を運ぶか", "光")],
    }
    pa = tmp_path / "a.json"
    pb = tmp_path / "b.json"
    pa.write_text(json.dumps(a), encoding="utf-8")
    pb.write_text(json.dumps(b), encoding="utf-8")
    out = tmp_path / "merged.json"
    result = merge_files([pa, pb], out, exam="2026/03", subject="サンプル")
    assert len(result["questions"]) == 1
    assert result["questions"][0]["conflicts"]
