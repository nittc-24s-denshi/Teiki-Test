# 03 — 問題ごとの分割

## 入力

- `pipeline/transcripts/*.md`

## 出力

- `pipeline/questions_raw/<source_id>_qNNN.json`  
  各ファイルは Schema の `Question` に近い形。未確定フィールドは `unverified` または空でよい。

## 手順

1. 大問・小問の境界を検出（番号、罫線、「問」など）
2. 問題文・選択肢・図参照・出典ページを切り出す
3. 図は `figures` に `pipeline/images/...` への相対パスを入れる
4. 解答欄が空なら解答はまだ入れない（次ステップ）

## 完了条件

- 1 問題 1 ファイル（または 1 配列でも可だが、マージ前はファイル分割推奨）
- 各問題に `source`（元ファイル名とページ）がある
