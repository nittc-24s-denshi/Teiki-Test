# 02 — 文字起こし

## 入力

- `pipeline/images/pages/*.png`（および必要なら embedded 画像）

## 出力

- `pipeline/transcripts/<source_id>_pNNN.md`
  - 先頭 YAML または HTML コメントで `source`, `page`, `tool`, `confidence` を記録
  - 本文は可能な限り原文どおり。読めない箇所は `【未確認】` とマークし、後で `unverified` にする

## 外部 AI

- **推奨: Gemini**（画像・手書きに強い）
- 一時チャットを使い、個人情報を送らない
- 長い資料はページ単位で分割して依頼

## ローカル代替

印刷テキスト PDF なら `pymupdf` のテキスト抽出で足りる場合がある（`tools/pdf_process.py --extract-text`）。手書き・図中文字は外部 AI を使う。

## 完了条件

- 全ページに transcript がある（白紙は「（空白ページ）」と明示）
- 使用ツール名が各ファイルに記録されている
