# 04 — 穴埋め（未記入解答・空欄の補完）

## 入力

- `pipeline/questions_raw/*.json`
- 必要なら元画像・transcript

## 出力

- 同じ JSON を更新。補完した値は必ず:

```json
{
  "value": "...",
  "status": "inferred",
  "rationale": "空欄だったため同類問題と公式から補完",
  "tools": ["ChatGPT", "manual-check"]
}
```

自信が無い場合は `unverified` にし、アプリではバッジ表示する。

## 外部 AI

- **ChatGPT または Gemini**
- 計算問題は途中式も残す（後の検算用）
- 元資料に無い「創作問題」は作らない（空欄補完と範囲内の解答推定に限る）

## 完了条件

- 空のまま放置した解答には `unverified` が付いている
- `inferred` には `rationale` と `tools` がある
