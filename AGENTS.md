# AGENTS.md — 全エージェント向け入口

このリポジトリは **東京高専 電子工学科 3年** の定期テスト対策教材置き場である。  
Cursor / Codex / Claude / Gemini / Muse など、どのエージェントからでも、まずこのファイルを読む。

## 最初に読むもの

| 優先 | ファイル | 内容 |
|------|----------|------|
| 1 | 本ファイル (`AGENTS.md`) | 構成・運用ルール・入口 |
| 2 | [`docs/pipeline/README.md`](docs/pipeline/README.md) | 教材自動処理パイプライン |
| 3 | [`.cursor/skills/material-pipeline/SKILL.md`](.cursor/skills/material-pipeline/SKILL.md) | 取り込みパイプライン skill |
| 4 | [`.cursor/skills/test-prep-app/SKILL.md`](.cursor/skills/test-prep-app/SKILL.md) | 対策アプリ・問題データ生成 skill |
| 5 | [`schema/questions.schema.json`](schema/questions.schema.json) | 問題データの JSON Schema |
| 6 | [`README.md`](README.md) / [`specification.md`](specification.md) | 既存アプリ概要 |

他エージェント用の短いエイリアス:

- [`CLAUDE.md`](CLAUDE.md) → 本ファイルを参照
- [`GEMINI.md`](GEMINI.md) → 本ファイルを参照

## リポジトリ構成（慣習）

```
YYYY/NN/科目/…          年度 / 年度内シリアル / 科目
  範囲表(内容).md       試験フォルダ直下（内容項目）
  範囲表(ページ).md     試験フォルダ直下（ページ）
  Schedule.json         試験日時
  科目/RAW/             元資料（無加工）
  科目/参考資料/        整理済み参考資料
  科目/*.md             ノート・まとめ
  科目/status.json      パイプライン進捗（任意・推奨）
Web_App/                静的 Web アプリ（GitHub Pages 想定）
docs/pipeline/          教材自動処理の手順書
schema/                 JSON Schema
tools/                  ローカル完結の Python ツール
examples/               通し動作サンプル（仮本文）
.cursor/skills/         エージェント skill（他ツールも参照可）
```

- パスは `YYYY/NN` のみ。年跨ぎ通し番号や期名をフォルダ名に入れない。
- 筆記試験のない科目（実験・体育・ものづくり）は対象外。
- 仮ノート先頭は `<!-- 仮・イーハトーブ -->`。本文は宮沢賢治（パブリックドメイン）または自作の簡単な数式。

## 運用ルール（必須）

1. **作業前に最新 `main` を取得**し、他者の変更を上書きしない。`git fetch origin main` → `git pull --rebase origin main`（作業ブランチなら rebase）。
2. **教材データは基本 PR を使わず `main` へ直接コミット**（科目単位のまとまりで）。**deploy はしない**。
3. **原文 (`original`) / 推定補完 (`inferred`) / 未確認 (`unverified`)** を常に区別する。推定には根拠と使用ツールを書く。
4. **シラバスの予定を確定出題範囲として書かない**。公式範囲表が届くまで範囲表へ週次を写さない。
5. **RAW は無加工で保存**。個人メモは公開可。採点済み答案・氏名など個人情報を含むものは都度本人確認。
6. **仮本文**はイーハトーブ（宮沢賢治）系のパブリックドメイン文で、「仮」マーカー付き。
7. **リポジトリに個人名・メール・秘密を書かない**。
8. 科目進捗は各試験フォルダ配下の科目に `status.json` を持つ（形式は [`docs/pipeline/status.md`](docs/pipeline/status.md)）。

## パイプライン概要

ユーザーがまとめて送る PDF（授業プリント・板書・問題集・過去問など）を、エージェントが次を **全部自動で行ってからコミット** する。

1. PDF 分割・画像抽出・ページ画像化  
2. 文字起こし  
3. 問題ごとの分割  
4. 穴埋め（未記入解答・空欄の補完）  
5. 複数教材の内容統合  
6. 内容の訂正（誤字・計算検算）  
7. データの構造化  
8. 検証  
9. コミット  

詳細手順・入出力・命名規則: [`docs/pipeline/`](docs/pipeline/)  
ローカルスクリプト（外部 AI 無しでも動く部分）: [`tools/`](tools/)

### 外部 AI の役割（推奨）

| 作業 | 推奨 |
|------|------|
| 文字起こし（画像・手書き） | Gemini |
| 穴埋め・空欄補完 | ChatGPT または Gemini |
| 長い一気通し作業 | Muse |
| 構造化・検証・コミット補助 | 作業中のエージェント |

- **一時チャット優先**（長期メモリに教材を残さない）。
- **個人情報・秘密は送らない**。
- リポジトリ内スクリプト（`tools/`）は外部 AI 無しでも動作すること。

## テスト対策アプリ

- 既存: `Web_App/Grammar_Words` など（壊さない）。
- 新規: [`Web_App/Question_Bank/`](Web_App/Question_Bank/) — 構造化 JSON を読む汎用問題アプリ。
- データ生成: skill [`test-prep-app`](.cursor/skills/test-prep-app/SKILL.md) と `tools/generate_app_data.py`。

## サンプル通し確認

```bash
cd tools && python3 -m pip install -r requirements.txt
python3 -m pytest tests/ -q
python3 run_sample_pipeline.py
# ブラウザで Web_App/Question_Bank/index.html を開く（fetch 用に静的サーバ推奨）
```
