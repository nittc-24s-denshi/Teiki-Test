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
    "validated": true,
    "app_data": true
  },
  "counts": {
    "questions": 0,
    "corrections": 0,
    "inferred": 0,
    "unverified": 0
  },
  "notes": "公式範囲は未入手。構造化データは仮サンプルのみ。"
}
```

## 規則

- 個人名を書かない
- シラバス推定を「範囲確定」と書かない
- フラグはブール。未着手は `false`
- PDF 以外（例: 暗記メーカー `/questions` JSON）では `pages_split` / `transcribed` を `false` にしてよい
- アプリ用データ（`app_data/` と Question Bank 登録）まで作ったら `pipeline.app_data: true`
- `counts` は任意。問数・corrections / inferred / unverified を残すと後続確認が楽
