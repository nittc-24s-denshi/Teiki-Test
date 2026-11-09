# 教材自動処理パイプライン

ユーザーが渡した PDF 等を、エージェントが取り込みからコミットまで一貫処理するための手順書集。

入口: [`AGENTS.md`](../../AGENTS.md)  
Skill: [`.cursor/skills/material-pipeline/SKILL.md`](../../.cursor/skills/material-pipeline/SKILL.md)

## ステップ一覧

| # | 文書 | 主な入出力 | 外部 AI |
|---|------|------------|---------|
| 0 | [00-overview.md](00-overview.md) | 全体像・ディレクトリ規約 | — |
| 1 | [01-pdf-split.md](01-pdf-split.md) | PDF → ページ PDF / 画像 | 不要（`tools/`） |
| 2 | [02-transcription.md](02-transcription.md) | 画像 → 文字起こし MD/JSON | Gemini 推奨 |
| 3 | [03-question-split.md](03-question-split.md) | 文字起こし → 問題単位 | エージェント可 |
| 4 | [04-fill-blanks.md](04-fill-blanks.md) | 空欄・未記入解答の補完 | ChatGPT / Gemini |
| 5 | [05-merge.md](05-merge.md) | 複数ソース統合・conflict | 不要（`tools/`） |
| 6 | [06-correct.md](06-correct.md) | 誤字・計算検算 | エージェント可 |
| 7 | [07-structure.md](07-structure.md) | Schema 準拠 JSON 化 | エージェント可 |
| 8 | [08-validate.md](08-validate.md) | Schema 検証 | 不要（`tools/`） |
| 9 | [09-commit.md](09-commit.md) | main へ直接コミット | — |

進捗ファイル: [status.md](status.md)  
外部 AI 方針: [external-ai.md](external-ai.md)

## 完了の定義（1 科目）

- `RAW/` に元 PDF が無加工で存在
- 構造化 JSON が `schema/questions.schema.json` を通過
- `original` / `inferred` / `unverified` が問題フィールドに付いている
- `status.json` が更新されている
- `main` にコミット済み（deploy しない）
