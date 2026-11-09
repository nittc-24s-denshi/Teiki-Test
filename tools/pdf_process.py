#!/usr/bin/env python3
"""Split PDF pages, extract embedded images, rasterize pages, optional text extract.

Usage:
  python pdf_process.py --input RAW/a.pdf --out-dir pipeline --dpi 150
  python pdf_process.py --input RAW/a.pdf --out-dir pipeline --extract-text
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import pymupdf as fitz


def source_id_from_path(path: Path) -> str:
    stem = path.stem
    stem = re.sub(r"[^\w\-]+", "_", stem, flags=re.UNICODE)
    return stem.strip("_") or "source"


def ensure_dirs(out_dir: Path) -> dict[str, Path]:
    paths = {
        "pages": out_dir / "pages",
        "embedded": out_dir / "images" / "embedded",
        "page_images": out_dir / "images" / "pages",
        "transcripts": out_dir / "transcripts",
    }
    for p in paths.values():
        p.mkdir(parents=True, exist_ok=True)
    return paths


def process_pdf(
    input_path: Path,
    out_dir: Path,
    *,
    dpi: int = 150,
    extract_text: bool = False,
    source_id: str | None = None,
) -> dict:
    if not input_path.is_file():
        raise FileNotFoundError(input_path)

    sid = source_id or source_id_from_path(input_path)
    dirs = ensure_dirs(out_dir)
    doc = fitz.open(input_path)
    page_count = doc.page_count
    embedded_count = 0
    zoom = dpi / 72.0
    matrix = fitz.Matrix(zoom, zoom)

    page_files: list[str] = []
    image_files: list[str] = []
    text_files: list[str] = []

    for i in range(page_count):
        page_no = i + 1
        tag = f"{sid}_p{page_no:03d}"

        # single-page PDF
        single = fitz.open()
        single.insert_pdf(doc, from_page=i, to_page=i)
        page_pdf = dirs["pages"] / f"{tag}.pdf"
        single.save(page_pdf)
        single.close()
        page_files.append(str(page_pdf.relative_to(out_dir)))

        # page raster
        page = doc.load_page(i)
        pix = page.get_pixmap(matrix=matrix, alpha=False)
        png_path = dirs["page_images"] / f"{tag}.png"
        pix.save(png_path)
        image_files.append(str(png_path.relative_to(out_dir)))

        # embedded images
        for img_index, img in enumerate(page.get_images(full=True), start=1):
            xref = img[0]
            try:
                extracted = doc.extract_image(xref)
            except Exception:
                continue
            ext = extracted.get("ext") or "bin"
            emb_path = dirs["embedded"] / f"{tag}_img{img_index:02d}.{ext}"
            emb_path.write_bytes(extracted["image"])
            embedded_count += 1
            image_files.append(str(emb_path.relative_to(out_dir)))

        if extract_text:
            text = page.get_text("text").strip()
            md_path = dirs["transcripts"] / f"{tag}.md"
            body = text if text else "（空白ページ）"
            md_path.write_text(
                f"<!-- source: {input_path.name} page: {page_no} tool: pymupdf -->\n\n{body}\n",
                encoding="utf-8",
            )
            text_files.append(str(md_path.relative_to(out_dir)))

    doc.close()
    summary = {
        "source_id": sid,
        "input": str(input_path),
        "page_count": page_count,
        "embedded_images": embedded_count,
        "pages": page_files,
        "images": image_files,
        "transcripts": text_files,
    }
    (out_dir / "pdf_process_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Source PDF under RAW/")
    parser.add_argument("--out-dir", required=True, type=Path, help="pipeline/ output directory")
    parser.add_argument("--dpi", type=int, default=150)
    parser.add_argument("--extract-text", action="store_true")
    parser.add_argument("--source-id", default=None)
    args = parser.parse_args(argv)

    try:
        summary = process_pdf(
            args.input,
            args.out_dir,
            dpi=args.dpi,
            extract_text=args.extract_text,
            source_id=args.source_id,
        )
    except Exception as exc:  # noqa: BLE001 — CLI boundary
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(
        f"OK: {summary['page_count']} pages, "
        f"{summary['embedded_images']} embedded images → {args.out_dir}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
