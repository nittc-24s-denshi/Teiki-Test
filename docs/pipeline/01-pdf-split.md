# 01 — PDF 分割・画像抽出・ページ画像化

## 入力

- `YYYY/NN/科目/RAW/<source_id>.pdf`（無加工の原本）

## 出力

- `pipeline/pages/<source_id>_pNNN.pdf` — 1 ページ 1 PDF
- `pipeline/images/embedded/` — PDF 内埋め込み画像
- `pipeline/images/pages/<source_id>_pNNN.png` — ページ全体のラスタ画像

## 手順（ローカル完結）

```bash
python3 tools/pdf_process.py \
  --input path/to/RAW/source.pdf \
  --out-dir path/to/pipeline \
  --dpi 150
```

外部 AI は不要。依存は `tools/requirements.txt`（pymupdf）。

## 完了条件

- 全ページ分の単ページ PDF とページ PNG がある
- RAW の原本が変更・削除されていない
- ページ数が元 PDF と一致する（スクリプトが報告）
