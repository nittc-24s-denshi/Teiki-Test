# 06 — 内容の訂正（誤字・計算検算）

## 入力

- 統合後 JSON

## 出力

- 訂正適用済み JSON
- 各訂正は `corrections` 配列へ:

```json
{
  "field": "stem.value",
  "before": "電束密度",
  "after": "電束密度 D",
  "reason": "記号欠落"
}
```

原文を書き換える場合も、可能なら `original` の値は `corrections.before` に残す。

## 手順

1. 明らかな誤字脱字を修正
2. 数値・単位・公式を検算（外部 AI 可、最終はエージェントまたは人が確認）
3. 検算不能なものは `unverified` のまま

## 完了条件

- 変更点はすべて `corrections` に残っている
- 「正しそうだから」での黙殺削除をしていない
