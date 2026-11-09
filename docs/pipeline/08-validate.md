# 08 — 検証

## 入力

- `structured/questions.json`

## 手順（ローカル完結）

```bash
python3 tools/validate_schema.py \
  --schema schema/questions.schema.json \
  --data path/to/structured/questions.json
```

追加チェック（スクリプトが実施）:

- `inferred` に `rationale` / `tools` があるか
- `id` の一意性
- `figures[].path` の存在（オプション `--check-files`）

## 完了条件

- 終了コード 0
- エラー 0 件（警告のみならコミット可だが `status.json` に残す）
