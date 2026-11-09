# 00 — 全体像・ディレクトリ規約

## 目的

試験フォルダ `YYYY/NN/科目/` に、元資料から検証済み問題データまでを再現可能な形で置く。

## 標準レイアウト（科目ごと）

```
YYYY/NN/科目/
├── RAW/                          # 元資料（無加工・必須）
│   └── <source_id>.pdf
├── 参考資料/                     # 人間が読む整理済み資料
├── pipeline/                     # パイプライン中間成果（任意だが推奨）
│   ├── pages/                    # 1ページ1PDF: <source_id>_p001.pdf
│   ├── images/                   # 埋め込み画像・ページ画像
│   │   ├── embedded/
│   │   └── pages/                # <source_id>_p001.png
│   ├── transcripts/              # 文字起こし
│   │   └── <source_id>_p001.md
│   ├── questions_raw/            # 問題分割直後（未統合）
│   │   └── <source_id>_q001.json
│   └── corrections_log.json      # 訂正履歴の作業メモ（任意）
├── structured/
│   └── questions.json            # Schema 準拠の最終成果
├── app_data/                     # アプリ用派生データ（任意）
│   ├── flashcards.json
│   ├── multiple_choice.json
│   ├── cloze.json
│   └── words.csv
├── status.json                   # 進捗
└── *.md                          # 既存のノート・まとめ（壊さない）
```

サンプル通しデータは `examples/pipeline_sample/` に同様の骨格を置く。

## 命名規則

| 対象 | 規則 | 例 |
|------|------|----|
| source_id | 英数字と `_` `-`、拡張子なし | `print_2026-11-01` |
| ページ番号 | 3桁ゼロ埋め `pNNN` | `p001` |
| 問題 ID | `{科目略号}-{単元略}-{連番3桁}` または UUID | `EM-gauss-001` |
| 画像 | `<source_id>_pNNN[_imgKK].ext` | `print_p003_img01.png` |

科目略号はフォルダ名から機械的に決めてよい（例: 電磁気学Ⅱ → `EM2`）。一貫していればよい。

## 値の信頼性（全ステップ共通）

各意味のある値は次のいずれかを持つ（Schema の `ProvenanceValue`）:

- `original` — 元資料に明示されている
- `inferred` — 補完・推定。`rationale` と `tools` 必須
- `unverified` — 未確認。解答を断定しない

教材間の食い違いは片方を捨てず `conflicts` に両方残す。

## 対象外

実験・体育・ものづくりなど、筆記試験のない科目。
