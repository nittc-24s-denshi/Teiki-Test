---
name: test-prep-app
description: >-
  構造化済み questions.json からテスト対策用アプリデータ（フラッシュカード・選択式・穴埋め・英単語 CSV）を生成し、
  Web_App/Question_Bank で使えるようにする。アプリ追加・問題データ生成の依頼で使う。
---

# テスト対策アプリ・問題データ生成 skill

入口: [`AGENTS.md`](../../../AGENTS.md)  
アプリ: [`Web_App/Question_Bank/`](../../../Web_App/Question_Bank/)  
生成ツール: [`tools/generate_app_data.py`](../../../tools/generate_app_data.py)

## いつ使うか

- 「この JSON からアプリ用データを作って」
- 「フラッシュカード / 四択 / 穴埋め CSV が欲しい」
- 「Question Bank に載せて」

## 前提

- 入力は [`schema/questions.schema.json`](../../../schema/questions.schema.json) を通った `structured/questions.json`
- 未検証なら先に `material-pipeline` の検証ステップを実行

## 手順

```bash
python3 tools/generate_app_data.py \
  --input YYYY/NN/科目/structured/questions.json \
  --out-dir YYYY/NN/科目/app_data \
  --also-copy-to Web_App/Question_Bank/data
```

出力:

| ファイル | 用途 |
|----------|------|
| `questions.json` | Question Bank 本体 |
| `flashcards.json` | 表裏カード |
| `multiple_choice.json` | 選択式 |
| `cloze.json` | 穴埋め |
| `words.csv` | `word,japanese`（既存 Grammar_Words 慣習） |

英単語だけ既存 UI で使う場合は、`words.csv` を `Web_App/Grammar_Words/` または科目の `単語テスト/` にコピーしてよい（既存ファイルを無闇に上書きしない）。

## アプリの使い方

1. `Web_App/Question_Bank/index.html` を開く（`fetch` のため、できればローカル静的サーバ）
2. 科目・単元・形式で絞り込み。`推定` / `未確認` バッジと conflict を確認しながら学習

ポータル (`Web_App/index.html`) からもリンクする。

## 注意

- 既存の `Grammar_Words` / `Oral_sentence` 等は壊さない
- 個人名・秘密をデータに入れない
- 仮データは「仮」タグとイーハトーブ系マーカーを維持
- アプリやデータ追加後も **deploy しない**（教材と同様、必要なら main へ直接コミットのみ）
