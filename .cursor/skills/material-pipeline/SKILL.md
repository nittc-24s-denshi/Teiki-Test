---
name: material-pipeline
description: >-
  授業プリント・板書・問題集・過去問などの PDF を受け取り、分割・文字起こし・問題分割・穴埋め・統合・訂正・構造化・検証・main へのコミットまでを実行する。
  教材取り込み、RAW 追加、questions.json 生成、パイプライン実行の依頼で使う。
---

# 教材取り込みパイプライン skill

入口: [`AGENTS.md`](../../../AGENTS.md)  
手順書: [`docs/pipeline/README.md`](../../../docs/pipeline/README.md)

## いつ使うか

ユーザーが PDF（または画像束）を「取り込んで」「パイプライン回して」「構造化してコミットして」と頼んだとき。

## 事前確認

1. `git fetch origin main` → 最新 `main` を取得（他者変更を上書きしない）
2. 対象が筆記試験科目か（実験・体育・ものづくりは対象外）
3. 配置先 `YYYY/NN/科目/` を確認。無ければ既存慣習に合わせて作成
4. 個人情報（氏名・採点済み答案）が無いか確認。あれば本人確認まで中断

## 実行手順（漏れなく全部）

1. **RAW 保存（無加工）**  
   `YYYY/NN/科目/RAW/<source_id>.pdf`

2. **PDF 分割・画像**（ローカル）  
   `python3 tools/pdf_process.py --input .../RAW/x.pdf --out-dir .../pipeline --dpi 150 --extract-text`

3. **文字起こし**  
   手書き・図は **Gemini（一時チャット）**。印刷テキストは `--extract-text` で足りることがある。  
   出力: `pipeline/transcripts/`

4. **問題分割** → `pipeline/questions_raw/`

5. **穴埋め**  
   空欄・未記入は **ChatGPT または Gemini**。値は `inferred` + `rationale` + `tools`。不明なら `unverified`。

6. **統合**  
   `python3 tools/merge_questions.py --inputs ... --output .../structured/questions.json --exam YYYY/NN --subject ...`

7. **訂正**  
   誤字・計算検算。変更は `corrections` に残す。食い違いは `conflicts`。

8. **構造化仕上げ**  
   [`schema/questions.schema.json`](../../../schema/questions.schema.json) に合わせる。  
   シラバス予定を確定範囲として書かない。

9. **検証**  
   `python3 tools/validate_schema.py --schema schema/questions.schema.json --data .../structured/questions.json`

10. **status.json 更新**（[`docs/pipeline/status.md`](../../../docs/pipeline/status.md)）

11. **コミット**（PR せず `main` へ、科目単位、**deploy しない**）  
    push 前に再 fetch。他者更新があれば rebase。force push 禁止。

任意: Markdown まとめは `tools/generate_markdown.py`（既存ノートを上書きしない）。

## 完了条件

- RAW 無加工で残存
- Schema 検証 OK
- `original` / `inferred` / `unverified` が付いている
- `status.json` 更新
- `main` にコミット済み

## サンプル

`python3 tools/run_sample_pipeline.py` が `examples/pipeline_sample` の通し参考実装。
