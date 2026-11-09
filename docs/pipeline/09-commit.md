# 09 — コミット

## ルール

1. `git fetch origin main` し、最新を取り込む（rebase）。他者変更を上書きしない。
2. **教材データは PR せず `main` へ直接コミット**（科目単位）。
3. **deploy しない**（GitHub Pages への意図的デプロイ操作をしない）。
4. コミットメッセージ例: `Add structured questions for 2026/03 電磁気学Ⅱ`
5. 個人名・メール・秘密を差分に含めない。
6. push 直前に再 fetch。他者更新があれば rebase してから push。**force push 禁止**。
7. `main` への push が保護ルールで拒否された場合のみブランチ + PR を作り、マージは人間に任せる。

## status.json

コミット前に `pipeline.validated` と `pipeline.committed` 相当を更新する（[status.md](status.md)）。

## 完了条件

- `origin/main` に当該科目の成果が乗っている
- RAW が無加工のまま含まれている
