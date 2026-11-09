import json
from pathlib import Path

import pymupdf as fitz

from pdf_process import process_pdf


def _make_sample_pdf(path: Path) -> None:
    doc = fitz.open()
    page = doc.new_page(width=300, height=200)
    page.insert_text((40, 80), "Kari Ihatov sample page 1", fontsize=12)
    page2 = doc.new_page(width=300, height=200)
    page2.insert_text((40, 80), "page 2 math: E = mc^2", fontsize=12)
    doc.save(path)
    doc.close()


def test_process_pdf_splits_and_rasterizes(tmp_path: Path):
    pdf = tmp_path / "RAW" / "sample_ihatov.pdf"
    pdf.parent.mkdir(parents=True)
    _make_sample_pdf(pdf)
    out = tmp_path / "pipeline"
    summary = process_pdf(pdf, out, dpi=72, extract_text=True, source_id="sample_ihatov")

    assert summary["page_count"] == 2
    assert (out / "pages" / "sample_ihatov_p001.pdf").is_file()
    assert (out / "pages" / "sample_ihatov_p002.pdf").is_file()
    assert (out / "images" / "pages" / "sample_ihatov_p001.png").is_file()
    assert (out / "transcripts" / "sample_ihatov_p001.md").is_file()
    saved = json.loads((out / "pdf_process_summary.json").read_text(encoding="utf-8"))
    assert saved["page_count"] == 2
