#!/usr/bin/env python3
"""Append 第6回 + 後期中間（参考） questions onto existing structured/questions.json."""

from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = "RAW/print_lec6_midterm_practice_2026-11.pdf"
SRC = {"file": RAW}
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
UNIT6 = "第6回 独立事象とベイズの定理"
UNIT_REF = "2026年度後期中間試験（参考）"
TOOLS_HW = ["gemini-transcript", "manual-page-image-check", "manual-calc-check"]


def pv(value, status="original", rationale=None, tools=None):
    out = {"value": value, "status": status}
    if rationale is not None:
        out["rationale"] = rationale
    if tools is not None:
        out["tools"] = tools
    return out


def hw_answer(value: str, page: int, extra: str = "") -> dict:
    rationale = (
        f"原本ページ画像 p.{page} の手書き記入を照合。"
        + (f" {extra}" if extra else "")
    )
    return pv(value, "inferred", rationale=rationale, tools=TOOLS_HW)


def q(
    id_,
    unit,
    form,
    stem,
    answer,
    page,
    tags,
    *,
    explanation=None,
    corrections=None,
    note=None,
    stem_status="original",
):
    item = {
        "id": id_,
        "unit": unit,
        "form": form,
        "stem": pv(stem, stem_status),
        "answer": answer if isinstance(answer, dict) else pv(answer),
        "sources": [{"file": RAW, "page": page, **({"note": note} if note else {})}],
        "tags": tags,
    }
    if explanation is not None:
        item["explanation"] = (
            explanation if isinstance(explanation, dict) else pv(explanation)
        )
    if corrections:
        item["corrections"] = corrections
    return item


NEW_CORRECTIONS = [
    {
        "field": "answer:PS-L6-E6.rounding",
        "before": "手書き 0.015",
        "after": "手書き 0.015 を原文のまま保持。指示は小数第4位四捨五入。厳密値≈0.01467→0.0147",
        "reason": "ページ画像照合・検算。指示と手書き丸めが不一致。本文・解答は書き換えない",
    },
    {
        "field": "answer:PS-L6-E5.rounding",
        "before": "手書き 0.188",
        "after": "手書き 0.188 を原文のまま保持。厳密値 6/32=0.1875",
        "reason": "検算。手書きは小数第3位への丸め",
    },
    {
        "field": "transcript:p7.score_group_ri_wa",
        "before": "（照合中）リ・ル と レ・ロ・ワ の配点分割の疑い",
        "after": "リ・ル・レ=6、ロ・ワ=6（Gemini起こしどおり。ページ画像で確認）",
        "reason": "解答用紙配点の照合。印刷された学科コード M/E/D/J/C は空欄マーク",
    },
]


def build_new_questions() -> list[dict]:
    return [
        q(
            "PS-L6-DEF-indep",
            UNIT6,
            "flashcard",
            "独立事象の定義を書け。また独立かつ $P(B)\\neq 0$ のとき $P(A\\mid B)$ はどうなるか。",
            "$P(A\\cap B)=P(A)\\cdot P(B)$ のとき独立。このとき $P(A\\mid B)=P(A)$（同様に $P(A\\mid\\overline{B})=P(A)$）。",
            1,
            ["定義", "独立事象"],
        ),
        q(
            "PS-L6-EX1",
            UNIT6,
            "short_answer",
            "【例1】サイコロ3回の「1回目偶数」と「2回目4以上」は独立か。また当たり3/10本くじの非復元2回で「1回目当たり」と「2回目当たり」は独立か。理由も。",
            "前者は独立（2回目は1回目に依らない）。後者は独立でない（非復元のため2回目の当たりやすさが1回目に依存）。",
            1,
            ["例", "独立事象"],
        ),
        q(
            "PS-L6-E1-1",
            UNIT6,
            "calculation",
            "【演習1(1)】1〜$n$のカードから1枚。$A$:3の倍数、$B$:5の倍数。$n=20$のとき $A$ と $B$ は独立か。",
            hw_answer(
                "{{手書き: $P(A\\cap B)=1/20$}}；"
                "{{手書き: $P(A)\\cdot P(B)=(6/20)\\cdot(4/20)=3/50$}}；"
                "{{手書き: 独立ではない}}",
                1,
                "検算: 積事象は15のみ。$6/20\\cdot4/20=3/50\\neq1/20$。",
            ),
            1,
            ["演習", "独立事象"],
        ),
        q(
            "PS-L6-E1-2",
            UNIT6,
            "calculation",
            "【演習1(2)】同上で $n=30$ のとき $A$ と $B$ は独立か。",
            hw_answer(
                "{{手書き: $P(A\\cap B)=2/30=1/15$}}；"
                "{{手書き: $P(A)\\cdot P(B)=(10/30)\\cdot(6/30)=1/15$}}；"
                "{{手書き: 独立}}",
                1,
                "検算: 15と30の2個。一致するため独立。",
            ),
            1,
            ["演習", "独立事象"],
        ),
        q(
            "PS-L6-E2",
            UNIT6,
            "calculation",
            "【演習2】[問3.11] ジョーカー除くトランプ1枚。$A$=偶数、$B$=ハート、$C$=絵札$\\{11,12,13\\}$。独立な事象の組を全て求めよ。",
            hw_answer("{{手書き: $(A,B),\\ (B,C),$}}", 2, "検算: $(A,C)$ は非独立（$P(A\\cap C)=4/52\\neq P(A)P(C)$）。"),
            2,
            ["演習", "独立事象", "トランプ"],
        ),
        q(
            "PS-L6-EX2-bayes",
            UNIT6,
            "flashcard",
            "【例2】袋X（赤4・白3）とY（赤3・白5）を無作為に選び玉を1つ。赤が出たとき袋Xだった確率 $P(X\\mid R)$ の結果（プリントの計算）は？",
            "$\\dfrac{32}{53}$（$P(X)=P(\\overline{X})=1/2$，$P(R\\mid X)=4/7$，$P(R\\mid\\overline{X})=3/8$）。",
            2,
            ["例", "ベイズの定理"],
        ),
        q(
            "PS-L6-E3",
            UNIT6,
            "calculation",
            "【演習3】例2と同じ状況で、白玉が出たとき選ばれた袋がYであった確率を求めよ。",
            hw_answer(
                "{{手書き: $X:Y=3/7:5/8$}}；"
                "{{手書き: $\\dfrac{5/8}{3/7+5/8}=0.593$}}",
                2,
                "検算: $35/59\\approx0.593$。袋の選択確率1/2は比で約分される。",
            ),
            2,
            ["演習", "ベイズの定理"],
        ),
        q(
            "PS-L6-DEF-bayes",
            UNIT6,
            "flashcard",
            "ベイズの定理（2事象および排反分割 $A_1\\cup\\cdots\\cup A_n=\\Omega$）の公式を書け。",
            "$P(A\\mid B)=\\dfrac{P(A)P(B\\mid A)}{P(A)P(B\\mid A)+P(\\overline{A})P(B\\mid\\overline{A})}$。"
            "一般に $P(A_i\\mid B)=\\dfrac{P(A_i)P(B\\mid A_i)}{\\sum_k P(A_k)P(B\\mid A_k)}$。",
            3,
            ["定義", "ベイズの定理"],
        ),
        q(
            "PS-L6-E4",
            UNIT6,
            "calculation",
            "【演習4】晴れ0.6・曇り0.3・雨0.1。遅刻確率は晴れ0.2・曇り0.1・雨0.4。遅刻したとき晴れている確率を求めよ。",
            hw_answer(
                "{{手書き: $\\dfrac{0.6\\times0.2}{0.6\\times0.2+0.3\\times0.1+0.1\\times0.4}\\fallingdotseq0.632$}}",
                3,
                "検算: $0.12/0.19\\approx0.6316\\fallingdotseq0.632$。",
            ),
            3,
            ["演習", "ベイズの定理", "事前確率", "事後確率"],
        ),
        q(
            "PS-L6-DEF-prior",
            UNIT6,
            "flashcard",
            "事前確率と事後確率とは何か（プリントの晴れ・遅刻の文脈）。",
            "元の $P(\\text{晴れ})$ が事前確率。結果（遅刻）のもとでの $P(\\text{晴れ}\\mid\\text{遅刻})$ が事後確率。",
            3,
            ["定義", "事前確率", "事後確率"],
        ),
        q(
            "PS-L6-E5",
            UNIT6,
            "calculation",
            "【演習5】[問3.13] 機械A,B,Cの個数比 $2:3:5$。不良率 3%,2%,4%。不良品1つがA製である確率を求めよ。",
            hw_answer(
                "{{手書き: $\\dfrac{(2/10)\\times3}{(2/10)\\times3+(3/10)\\times2+(5/10)\\times4}=0.188$}}",
                3,
                "検算: $6/32=0.1875$。手書きは0.188。",
            ),
            3,
            ["演習", "ベイズの定理"],
            corrections=[
                {
                    "field": "answer.rounding",
                    "before": "0.188（手書き）",
                    "after": "0.188（手書き保持）。厳密値0.1875",
                    "reason": "検算。丸め差のみ。解答本文は手書き原文のまま",
                }
            ],
        ),
        q(
            "PS-L6-E6",
            UNIT6,
            "calculation",
            "【演習6】[問3.14] 規格外確率0.1。規格内は0.97で合格、規格外でも0.13で合格。合格と判定されたとき規格外である確率（小数第4位四捨五入）。",
            hw_answer(
                "{{手書き: $\\dfrac{.1\\times.13}{.9\\times.97+.1\\times.13}=0.015$}}",
                4,
                "検算: 厳密値≈0.01467。小数第4位四捨五入なら0.0147。手書き0.015は指示と不一致のため原文のまま保持し corrections に記録。",
            ),
            4,
            ["演習", "ベイズの定理"],
            corrections=[
                {
                    "field": "answer.rounding",
                    "before": "0.015（手書き）",
                    "after": "0.015（手書き保持）。指示どおりなら≈0.0147",
                    "reason": "小数第4位四捨五入の指示と手書き丸めが不一致。本文は書き換えない",
                }
            ],
            explanation=pv(
                "注: プリント指示は小数第4位四捨五入。手書き解答0.015はそのまま残し、疑義は corrections に記録。",
                "original",
            ),
        ),
        q(
            "PS-L6-E7-1",
            UNIT6,
            "calculation",
            "【演習7(1)】モンティ・ホール。箱A指定後、司会者が箱Bを空けハズレと知らせた。司会者が指定外の箱を必ず無作為に1つ開ける場合、$P($箱Aが当たり$)$ を求めよ。",
            pv("（未記入・未確認）", "unverified"),
            4,
            ["演習", "モンティ・ホール", "未記入"],
            note="演習7(1) 未解き",
        ),
        q(
            "PS-L6-E7-2",
            UNIT6,
            "calculation",
            "【演習7(2)】同上。司会者が指定外のうちハズレの箱を必ず無作為に1つ開ける場合、$P($箱Aが当たり$)$ を求めよ。",
            pv("（未記入・未確認）", "unverified"),
            4,
            ["演習", "モンティ・ホール", "未記入"],
            note="演習7(2) 未解き",
        ),
        # --- 参考試験 ---
        q(
            "PS-REF-Q1",
            UNIT_REF,
            "cloze",
            "【1】通学時間の度数分布（0〜20:1, 20〜40:10, 40〜60:9, 60〜80:8, 80〜100:2、計30）。"
            "平均値は $\\fbox{アイ}$ 分、中央値が含まれる階級の階級値は $\\fbox{ウエ}$ 分、"
            "分散は $\\fbox{オカキ}$、標準偏差は $\\fbox{クケ}$。",
            pv("（未記入・未確認） アイ／ウエ／オカキ／クケ", "unverified"),
            5,
            ["参考試験", "度数分布", "代表値", "分散", "未記入"],
            note="公式範囲表ではない参考試験。空欄穴埋め未実施",
        ),
        q(
            "PS-REF-Q2",
            UNIT_REF,
            "cloze",
            "【2】8人の小テスト $(x,y)=(1,4),(2,2),(3,1),(4,7),(6,3),(7,9),(8,6),(9,8)$。"
            "共分散 $\\fbox{コ}$、相関係数 $\\fbox{サ}/\\fbox{シ}$、"
            "回帰直線 $y=(\\fbox{ス}/\\fbox{セ})x+(\\fbox{ソ}/\\fbox{タ})$。",
            pv("（未記入・未確認） コ／サシ／スセ／ソタ", "unverified"),
            5,
            ["参考試験", "共分散", "相関係数", "回帰", "未記入"],
        ),
        q(
            "PS-REF-Q3",
            UNIT_REF,
            "true_false",
            "【3】共分散・相関係数の正誤（正=1・誤=0）。"
            "(I) $x$のみ2倍すると共分散は2倍…$\\fbox{チ}$。"
            "(II) $x_i<x_j\\Rightarrow y_i<y_j$ なら $r=1$…$\\fbox{ツ}$。"
            "(III) 右上がり直線上に全点があれば $r=1$…$\\fbox{テ}$。",
            pv("（未記入・未確認） チ／ツ／テ", "unverified"),
            5,
            ["参考試験", "相関係数", "正誤", "未記入"],
        ),
        q(
            "PS-REF-Q4",
            UNIT_REF,
            "cloze",
            "【4】$X$の平均6・標準偏差2。$Y=-3X+10$ の平均 $\\fbox{トナ}$・標準偏差 $\\fbox{ニ}$。"
            "また $Z=(X-\\fbox{ヌ})/\\fbox{ネ}$ は平均0・標準偏差1。",
            pv("（未記入・未確認） トナ／ニ／ヌネ", "unverified"),
            5,
            ["参考試験", "標準化", "線形変換", "未記入"],
        ),
        q(
            "PS-REF-Q5",
            UNIT_REF,
            "cloze",
            "【5】$P(A)=0.5,P(B)=0.4,P(A\\cup B)=0.7$ のとき "
            "$P(A\\cap B)=0.\\fbox{ノ}$、$P(A\\cap\\overline{B})=0.\\fbox{ハ}$。",
            pv("（未記入・未確認） ノ／ハ", "unverified"),
            6,
            ["参考試験", "確率の性質", "未記入"],
        ),
        q(
            "PS-REF-Q6",
            UNIT_REF,
            "cloze",
            "【6】サイコロを4回振る時、$n$回目の出目が$n$の倍数である確率は $\\fbox{ヒ}/\\fbox{フヘ}$。",
            pv("（未記入・未確認） ヒ／フヘ", "unverified"),
            6,
            ["参考試験", "反復試行", "未記入"],
        ),
        q(
            "PS-REF-Q7",
            UNIT_REF,
            "cloze",
            "【7】原点の点P。サイコロで1,2なら$x$方向+1、それ以外なら$y$方向+1。"
            "5回後に$(2,3)$にある確率は $\\fbox{ホマ}/\\fbox{ミムメ}$。",
            pv("（未記入・未確認） ホマ／ミムメ", "unverified"),
            6,
            ["参考試験", "反復試行", "未記入"],
        ),
        q(
            "PS-REF-Q8",
            UNIT_REF,
            "cloze",
            "【8】サイコロ2個。出目の和が8という条件のもと、少なくとも1個が偶数である条件付き確率は $\\fbox{モ}/\\fbox{ヤ}$。",
            pv("（未記入・未確認） モ／ヤ", "unverified"),
            6,
            ["参考試験", "条件付き確率", "未記入"],
        ),
        q(
            "PS-REF-Q9",
            UNIT_REF,
            "cloze",
            "【9】当たり3/10本。A→Bの順に非復元で1本ずつ。AがはずれBが当たる確率は $\\fbox{ユ}/\\fbox{ヨラ}$。",
            pv("（未記入・未確認） ユ／ヨラ", "unverified"),
            6,
            ["参考試験", "乗法定理", "未記入"],
        ),
        q(
            "PS-REF-Q10",
            UNIT_REF,
            "true_false",
            "【10】サイコロ1個。$A$=奇数、$B$=3以下、$C$=3または4。"
            "独立なら1・でなければ0。(I)$A$と$B$…$\\fbox{リ}$ (II)$A$と$C$…$\\fbox{ル}$ (III)$B$と$C$…$\\fbox{レ}$。",
            pv("（未記入・未確認） リ／ル／レ", "unverified"),
            6,
            ["参考試験", "独立事象", "未記入"],
        ),
        q(
            "PS-REF-Q11",
            UNIT_REF,
            "cloze",
            "【11】天候: 晴0.5・曇0.3・雨0.2。遅延: 晴0.02・曇0.04・雨0.1。"
            "遅延したとき曇りである確率は $\\fbox{ロ}/\\fbox{ワ}$。",
            pv("（未記入・未確認） ロ／ワ", "unverified"),
            6,
            ["参考試験", "ベイズの定理", "未記入"],
        ),
        q(
            "PS-REF-ANSWER-SHEET",
            UNIT_REF,
            "other",
            "解答用紙（書式のみ）の記入項目と配点ブロックを要約せよ。"
            "氏名・組・番・得点・学科M/E/D/J/C・出席番号・解答マークはすべて空欄。"
            "M/E/D/J/Cは印刷された学科コード。",
            pv(
                "見出し: 確率統計Ⅰ 2026年度後期中間試験（参考）解答用紙。"
                "左: ア〜ケ(12), コ〜タ(12), チ〜テ(6), ト〜ネ(10)。"
                "右: ノハ(8), ヒフヘ(5), ホ〜メ(5), モヤ(5), ユヨラ(5), リルレ(6), ロワ(6)。"
                "全マーク・氏名欄は空欄。",
                "original",
            ),
            7,
            ["参考試験", "解答用紙", "書式"],
            note="書式のみ。個人情報欄・解答マークは空欄",
        ),
        {
            "id": "PS-META-LEC6-REF-QC",
            "unit": "メタ（第6回・参考試験 文字起こし訂正）",
            "form": "other",
            "stem": pv(
                "第6回打刷＋2026年度後期中間試験（参考）の文字起こし照合・訂正記録。"
            ),
            "answer": pv(
                "訂正ログ参照（pipeline/corrections_log.json および本問 corrections）。"
                "参考試験は公式範囲表ではない。"
            ),
            "sources": [{"file": RAW, "page": 1, "note": "メタ"}],
            "tags": ["meta", "corrections", "参考試験"],
            "corrections": NEW_CORRECTIONS,
        },
    ]


def main() -> None:
    structured = ROOT / "structured" / "questions.json"
    data = json.loads(structured.read_text(encoding="utf-8"))
    existing = data["questions"]
    existing_ids = {q["id"] for q in existing}
    assert len(existing) == 53, len(existing)

    new_qs = build_new_questions()
    for item in new_qs:
        if item["id"] in existing_ids:
            raise SystemExit(f"ID collision: {item['id']}")

    # Append new meta corrections note into old meta as pointer (non-destructive)
    for item in existing:
        if item["id"] == "PS-META-TRANSCRIPT-QC":
            item.setdefault("corrections", []).append(
                {
                    "field": "ingest:lec6_ref",
                    "before": "第1〜5回のみ",
                    "after": "第6回＋後期中間（参考）を追加。詳細は PS-META-LEC6-REF-QC",
                    "reason": "追加取込。既存問は削除しない",
                }
            )
            break

    data["questions"] = existing + new_qs
    data["generated_at"] = NOW
    data["notes"] = (
        "授業プリント『確率統計 I 第1〜5回』（度数分布〜反復試行・条件付き確率）に加え、"
        "第6回『独立事象とベイズの定理』および『2026年度後期中間試験（参考）』を追加。"
        "手書き解答は inferred（原本ページ画像照合）。未記入・参考試験空欄は unverified。"
        "空欄穴埋め未実施（filled=false）。参考試験は公式範囲表ではない。"
        "公式範囲表は未入手のため確定範囲としては扱わない。"
    )

    structured.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    # corrections log: keep old + append new
    clog_path = ROOT / "pipeline" / "corrections_log.json"
    clog = json.loads(clog_path.read_text(encoding="utf-8"))
    old_corr = list(clog.get("corrections") or [])
    # include the pointer correction once
    pointer = {
        "field": "ingest:lec6_ref",
        "before": "第1〜5回のみ",
        "after": "第6回＋後期中間（参考）を追加。詳細は PS-META-LEC6-REF-QC",
        "reason": "追加取込。既存問は削除しない",
    }
    all_corr = old_corr + [pointer] + NEW_CORRECTIONS
    # also per-question rounding corrections already inside questions; count them in status via scan

    n_inferred = sum(
        1
        for qq in data["questions"]
        if isinstance(qq.get("answer"), dict) and qq["answer"].get("status") == "inferred"
    )
    unverified_ids = [
        qq["id"]
        for qq in data["questions"]
        if isinstance(qq.get("answer"), dict) and qq["answer"].get("status") == "unverified"
    ]
    n_corr = sum(len(qq.get("corrections") or []) for qq in data["questions"])

    clog.update(
        {
            "source": (
                "print_freq_dist + print_lec6_midterm_practice; "
                "gemini transcripts vs page images"
            ),
            "updated": NOW,
            "corrections": all_corr,
            "counts": {
                "questions": len(data["questions"]),
                "corrections": n_corr,
                "unverified": len(unverified_ids),
                "inferred_answers": n_inferred,
            },
            "unverified_ids": unverified_ids,
            "notes": (
                "参考試験を受領したが公式範囲表ではない。"
                "空欄穴埋めは未実施（filled=false）。"
            ),
        }
    )
    clog_path.write_text(
        json.dumps(clog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    status = {
        "exam": "2026/03",
        "subject": "確率統計",
        "updated": NOW,
        "pipeline": {
            "raw_ingested": True,
            "pages_split": True,
            "transcribed": True,
            "questions_split": True,
            "filled": False,
            "merged": True,
            "corrected": True,
            "structured": True,
            "validated": True,
            "app_data": True,
        },
        "counts": {
            "questions": len(data["questions"]),
            "corrections": n_corr,
            "unverified": len(unverified_ids),
            "inferred_answers": n_inferred,
        },
        "unverified_ids": unverified_ids,
        "notes": (
            "進捗: 整備中。第1〜5回に加え第6回打刷と2026年度後期中間試験（参考）を追加取込。"
            "参考試験を受領、公式範囲表ではない。"
            "schema検証対象。空欄穴埋めは未実施（filled=false）。"
            "公式範囲表は未入手。Question Bank catalog に ps_2026_03。"
        ),
    }
    (ROOT / "status.json").write_text(
        json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    note = f"""# 確率統計（2026/03）確認ノート

出典:
- `RAW/print_freq_dist_2026-11.pdf`（確率統計 I 第1〜5回、23ページ）
- `RAW/print_lec6_midterm_practice_2026-11.pdf`（第6回＋2026年度後期中間試験（参考）、7ページ）

## 単元

1. **第1回** — 度数分布表，ヒストグラム，代表値
2. **第2回** — 分散と標準偏差
3. **第3回** — 散布図・共分散・相関係数・回帰直線
4. **第4回** — 確率（事象と試行）
5. **第5回** — 反復試行・条件付き確率と乗法定理（余談: マルコフ連鎖）
6. **第6回** — 独立事象とベイズの定理（演習1〜7。演習7モンティ・ホールは未解き）

## 参考試験（公式範囲表ではない）

- **2026年度後期中間試験（参考）** 大問1〜11（解答未記入）および解答用紙（書式のみ・全空欄）を受領。
- **公式の試験範囲表ではない。** 範囲表(内容).md / 範囲表(ページ).md には確定範囲として載せていない。シラバス週次も写していない。

## データ

- 構造化: `structured/questions.json`
- 文字起こし（第1〜5回・訂正済）: `pipeline/transcripts/print_freq_dist_2026-11_corrected.md`
- 文字起こし（第6回・参考試験）: `pipeline/transcripts/print_lec6_midterm_practice_2026-11_gemini.md`
- 訂正ログ: `pipeline/corrections_log.json`
- アプリ用: `app_data/`
- Question Bank: `ps_2026_03`

## 注意

- 手書き解答は `inferred`（原本ページ画像の手書きを根拠・検算）。原文のまま（`{{{{手書き: …}}}}`）。
- 未記入空欄は `unverified`（既存の演習表・条件付き演習に加え、演習7および参考試験空欄）。
- 演習6は小数第4位四捨五入指示に対し手書き0.015。疑義は corrections に残し本文は未改変。
- 参考試験を受領、公式範囲表ではない。公式試験範囲は未入手。範囲表には写していない。
- 空欄穴埋めは未実施（filled=false）。
"""
    (ROOT / "確認ノート.md").write_text(note, encoding="utf-8")

    # corrected transcript: gemini + correction header
    gem = (
        ROOT
        / "pipeline"
        / "transcripts"
        / "print_lec6_midterm_practice_2026-11_gemini.md"
    )
    corrected = (
        ROOT
        / "pipeline"
        / "transcripts"
        / "print_lec6_midterm_practice_2026-11_corrected.md"
    )
    header = f"""<!--
照合メモ ({NOW}):
- 出発: Gemini 4 Argon 起こし（p.1〜7）。
- ページ画像と照合。起こしと矛盾する場合は PDF/ページ画像を優先。
- 演習6手書き 0.015 は原文保持（指示どおりなら ≈0.0147）。corrections 参照。
- 解答用紙配点: リ・ル・レ=6、ロ・ワ=6 をページ画像で確認。
- 参考試験は公式範囲表ではない。穴埋め補完なし。
-->

"""
    corrected.write_text(header + gem.read_text(encoding="utf-8"), encoding="utf-8")

    # まとめ
    md = ROOT / "structured" / "まとめ_構造化.md"
    lines = [
        f"# 確率統計 構造化まとめ（2026/03）",
        "",
        f"生成: {NOW}",
        "",
        f"問数: {len(data['questions'])}（メタ含む）",
        f"unverified: {len(unverified_ids)}",
        f"inferred: {n_inferred}",
        f"corrections: {n_corr}",
        "",
        "参考試験は公式範囲表ではない。",
        "",
    ]
    for item in data["questions"]:
        ans = item["answer"]
        lines.append(f"## {item['id']} — {item['unit']}")
        lines.append("")
        lines.append(f"- form: {item['form']}")
        lines.append(f"- stem: {item['stem']['value']}")
        lines.append(f"- answer ({ans['status']}): {ans['value']}")
        if item.get("explanation"):
            lines.append(f"- explanation: {item['explanation']['value']}")
        lines.append("")
    md.write_text("\n".join(lines), encoding="utf-8")

    print(
        json.dumps(
            {
                "questions": len(data["questions"]),
                "added": len(new_qs),
                "corrections": n_corr,
                "unverified": unverified_ids,
                "inferred": n_inferred,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
