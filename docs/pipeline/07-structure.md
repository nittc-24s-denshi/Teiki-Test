# 07 — データの構造化

## 入力

- 訂正済みの問題リスト

## 出力

- `YYYY/NN/科目/structured/questions.json`（[`schema/questions.schema.json`](../../schema/questions.schema.json) 準拠）

必須トップレベル:

- `schema_version`
- `exam`（例: `2026/03`）
- `subject`
- `generated_at`（ISO 8601、個人名は入れない）
- `questions[]`

各問題: `id`, `unit`, `form`, `stem`, `answer`, `sources`, `tags`, および任意で `choices`, `explanation`, `figures`, `corrections`, `conflicts`。

## Markdown まとめ（任意）

```bash
python3 tools/generate_markdown.py \
  --input structured/questions.json \
  --output 確認ノート_構造化.md
```

既存の仮ノートや人間用ノートを上書きしない。別名で出力する。

## 完了条件

- Schema の必須フィールドを満たす
- 信頼性ステータスが付いている
