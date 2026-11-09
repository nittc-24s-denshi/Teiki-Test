# tools — 教材パイプライン用スクリプト

外部 AI 無しで動くローカル処理。依存は `requirements.txt` のみ。

```bash
python3 -m pip install -r requirements.txt
python3 -m pytest tests/ -q
```

| スクリプト | 役割 |
|------------|------|
| `pdf_process.py` | ページ分割・埋め込み画像抽出・ページ画像化・テキスト抽出 |
| `validate_schema.py` | `questions.schema.json` 検証 + inferred チェック |
| `merge_questions.py` | 複数 JSON 統合・重複検出・conflict 記録 |
| `generate_markdown.py` | 構造化 JSON → Markdown まとめ |
| `generate_app_data.py` | フラッシュカード / 選択式 / 穴埋め / 英単語 CSV |
| `run_sample_pipeline.py` | `examples/pipeline_sample` 通し実行 |

詳細手順は [`docs/pipeline/`](../docs/pipeline/)。
