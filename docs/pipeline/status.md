# 科目 status.json

各試験の科目フォルダに置く進捗ファイル。機械可読を優先する。

## 配置

`YYYY/NN/科目/status.json`

## スキーマ（ Informal ）

```json
{
  "exam": "2026/03",
  "subject": "電磁気学Ⅱ",
  "updated": "2026-11-09T00:00:00+09:00",
  "pipeline": {
    "raw_ingested": true,
    "pages_split": true,
    "transcribed": true,
    "questions_split": true,
    "filled": true,
    "merged": true,
    "corrected": true,
    "structured": true,
    "validated": true
  },
  "notes": "公式範囲は未入手。構造化データは仮サンプルのみ。"
}
```

## 規則

- 個人名を書かない
- シラバス推定を「範囲確定」と書かない
- フラグはブール。未着手は `false`
- アプリ用データまで作ったら `notes` か将来の `pipeline.app_data` で触れてよい
