# 05 — 複数教材の内容統合

## 入力

- 複数の `questions_raw` または部分 JSON

## 出力

- 統合途中 JSON（まだ最終でなくてよい）
- 重複は 1 問にまとめ、食い違いは `conflicts` に両方残す

## 手順（ローカル完結）

```bash
python3 tools/merge_questions.py \
  --inputs a.json b.json \
  --output merged.json
```

重複検出の目安: 正規化した問題文の類似、同一 `source`+ページ+番号、同一 `id`。

## 完了条件

- 同一内容の重複エントリが統合されている
- 矛盾する解答・解説は削除せず `conflicts` に記録
