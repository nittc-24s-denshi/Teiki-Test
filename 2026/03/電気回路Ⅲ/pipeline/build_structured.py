#!/usr/bin/env python3
"""Build corrected transcript + structured/questions.json for 電気回路Ⅲ masked exercises/quiz."""

from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = Path(__file__).resolve().parent
SOURCE = "RAW/exercises_quiz_2026-11_masked.pdf"
EXAM = "2026/03"
SUBJECT = "電気回路Ⅲ"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
PAGE_IMG = "pipeline/images/pages/exercises_quiz_2026-11_masked_p{n:03d}.png"


def pv(value, status="original", rationale=None, tools=None):
    obj = {"value": value, "status": status}
    if rationale is not None:
        obj["rationale"] = rationale
    if tools is not None:
        obj["tools"] = tools
    return obj


def unverified(note="未記入。穴埋め補完は未実施（filled=false）。"):
    return pv(note, "unverified")


def corr(field, before, after, reason):
    return {"field": field, "before": before, "after": after, "reason": reason}


def fig(page, caption):
    return {
        "path": PAGE_IMG.format(n=page),
        "page": page,
        "caption": pv(caption, "original"),
    }


def src(page, note=None):
    o = {"file": SOURCE, "page": page}
    if note:
        o["note"] = note
    return o


def q(
    id_,
    unit,
    form,
    stem,
    answer,
    *,
    explanation=None,
    pages=None,
    note=None,
    tags=None,
    figures=None,
    corrections=None,
    conflicts=None,
):
    pages = pages or [1]
    item = {
        "id": id_,
        "unit": unit,
        "form": form,
        "stem": stem if isinstance(stem, dict) else pv(stem),
        "answer": answer if isinstance(answer, dict) else pv(answer),
        "sources": [src(p, note) for p in pages],
        "tags": tags or [],
    }
    if explanation is not None:
        item["explanation"] = (
            explanation if isinstance(explanation, dict) else pv(explanation)
        )
    if figures:
        item["figures"] = figures
    if corrections:
        item["corrections"] = corrections
    if conflicts:
        item["conflicts"] = conflicts
    return item


CORRECTIONS = [
    corr(
        "transcript:p14.q3.VL.phase",
        r"手書き VL = 4.0 exp(j 2π/3)、採点: 丸",
        r"手書き VL = 4.0 exp(j 7π/6) [V]、採点: 斜線（誤り）",
        "マスク版PDF照合。位相は 7π/6。正解仮説は π/6+π/2=2π/3",
    ),
    corr(
        "transcript:p14.q3.vL.phase",
        r"手書き vL … +2π/3、採点: チェック",
        r"手書き vL = 4.0√2 sin(1000t + 7π/6)、採点: 斜線系（誤り継承）",
        "マスク版PDF照合。瞬時値の位相も 7π/6",
    ),
    corr(
        "transcript:p14.q3.VC.phase",
        r"手書き VC = 40 exp(-j 5π/6)、採点: チェック",
        r"手書き VC = 40 exp(-j 5π/6) [V] を確認。採点は斜線（誤り）。正解仮説は π/6−π/2=−π/3",
        "マスク版PDF照合。学生誤答は原文のまま残す",
    ),
    corr(
        "transcript:p14.q3.vC.phase",
        r"手書き vC … −5π/6、採点: チェック",
        r"手書き vC = 40√2 sin(1000t − 5π/6) を確認。採点斜線。正解仮説 −π/3",
        "マスク版PDF照合",
    ),
    corr(
        "transcript:p14.q2.Z.unit",
        r"Z = 7.07 [S]",
        r"Z = 7.07 [S]（単位誤り・採点斜線）。インピーダンスなら Ω。並列RLCの検算仮説: Y=0.1−j0.05 → Z=8+j4",
        "マスク版PDF照合。学生の Z=5+j5=5√2 exp(jπ/4) は原文のまま",
    ),
    corr(
        "transcript:p14.q2.Y.fraction",
        r"A = 1/10 − j 199/2000、A = 0.141 [S^{−1}]",
        r"分数 1/10 と 199/2000 をPDFで確認。|A|≈0.141 および単位 [S^{−1}]（アドミタンスなら S）・採点斜線を確認",
        "マスク版PDF照合。1/10 と 199/2000 の読みを再確認済み",
    ),
    corr(
        "transcript:p14.q1.euler",
        "有無不明",
        r"余白メモ e^{iπ}+1=0 をPDFで確認（手書き）",
        "マスク版PDF照合",
    ),
    corr(
        "transcript:p14.scores",
        "38 / 20 / 18",
        "赤ペン点数 38・20・18 をPDFで確認。丸・斜線は採点",
        "マスク版PDF照合。p.1〜13 に {{採点}} なし",
    ),
    corr(
        "privacy:p12.class",
        "クラス欄の内容",
        "マスク済み",
        "復元・記録しない",
    ),
    corr(
        "privacy:p14.name_attendance",
        "氏名・出席番号欄の内容",
        "マスク済み（下線下まで白マスク）",
        "復元・記録しない",
    ),
    corr(
        "calc:p14.q2.parallel_RLC",
        "学生 Z=5+j5",
        "検算メモ（解答の書き換えではない）: Y=1/R+1/(jωL)+jωC=0.1−j0.05、Z=1/Y=8+j4",
        "学生誤答は原文として維持",
    ),
]


QUESTIONS: list[dict] = []

QUESTIONS.append(
    q(
        "EIC3-META-TRANSCRIPT-QC",
        "メタ（文字起こし訂正）",
        "other",
        "文字起こしをマスク済みページ画像と照合して訂正した記録。",
        "訂正ログ参照（pipeline/corrections_log.json および本問 corrections）",
        pages=[1],
        note="メタ",
        tags=["meta", "corrections"],
        corrections=CORRECTIONS,
    )
)

# ---- 演習問題 1 (p.1) ----
U_EX1 = "演習問題1（正弦波・フェーザ）"
QUESTIONS.extend(
    [
        q(
            "EIC3-EX1-PHASE",
            U_EX1,
            "calculation",
            r"[3] 問図3-2で v1,v2 の周波数 f=100[Hz]、時間差 Δt=5/3[ms]。v1 は v2 に対し何 [rad] 進み/遅れか。",
            r"手書き: $2\pi \Delta t/100$ [rad] 進み（書き込みのまま）",
            pages=[1],
            note="問図3-2",
            tags=["正弦波", "位相差"],
            figures=[fig(1, "問図3-2 および手書き解答（演習問題1）")],
            explanation="ページ画像上の手書き解答を原文として記録。計算式の Δt/T との対応は要確認。",
        ),
        q(
            "EIC3-EX1-POLAR-1",
            U_EX1,
            "calculation",
            r"[3](1) 極座標 $\dot{Z}=\sqrt{8}\angle 3\pi/4$ を直角座標で表しベクトル図を描け。",
            r"手書き: $-2+j2$（取り消し線付き $-2+2j$ あり）",
            pages=[1],
            tags=["複素数", "極座標"],
            figures=[fig(1, "ベクトル図（第2象限）")],
        ),
        q(
            "EIC3-EX1-POLAR-2",
            U_EX1,
            "calculation",
            r"[3](2) $\dot{Z}=1\angle(-2\pi/3)$ を直角座標で表しベクトル図を描け。",
            r"手書き: $-1/2 - j\sqrt{3}/2$",
            pages=[1],
            tags=["複素数", "極座標"],
        ),
        q(
            "EIC3-EX1-PHASOR-V",
            U_EX1,
            "calculation",
            r"[2] $\dot{V}=-20+j10$ [V] のフェーザ表示・フェーザ図・瞬時値（角周波数 ω）。",
            r"手書き: $10\sqrt{5}\exp(\pi - \tan^{-1}(1/2))$（書き込みのまま）",
            pages=[1],
            note="問図5-2",
            tags=["フェーザ"],
            figures=[fig(1, "問図5-2")],
        ),
        q(
            "EIC3-EX1-L",
            U_EX1,
            "calculation",
            r"[1] L=0.2[H] に $\dot{V}=100\angle 0$[V]、f=100/π[Hz]。$\dot{I}$ のフェーザ・直角座標・図・瞬時値。",
            r"手書き: $\dot{I}=\dot{V}/(j\omega L)=-j2.5$ A",
            pages=[1],
            tags=["インダクタンス", "フェーザ"],
        ),
        q(
            "EIC3-EX1-C",
            U_EX1,
            "calculation",
            r"[3] C=1/π[mF] に $\dot{V}=50\angle(\pi/6)$[V]、ω=100π[rad/s]。$\dot{I}$・図・瞬時値。",
            r"手書き: $\dot{I}=5\angle(2\pi/3)$[A]、$i=5\sqrt{2}\sin(100\pi t+2\pi/3)$[A]",
            pages=[1],
            tags=["キャパシタンス", "フェーザ"],
            explanation="フェーザ図の座標軸のみ（書き込みなし）。",
        ),
    ]
)

# ---- 配布資料 1 (p.2-3) ----
U_D1 = "配布資料1（RC・複素数・素子電圧）"
QUESTIONS.extend(
    [
        q(
            "EIC3-D1-Q1",
            U_D1,
            "calculation",
            r"問題1: vc=Vc sinωt のとき (1) 電源電圧 v (2) Vc/Vm の式 (3) 表3-1の数値計算とグラフ (4) LPF/HPF の判定。図1は R-C 直列、vc は C 両端。",
            unverified("（1）〜（4）および問表3-1は未記入・薄い判読不能書き込みのみ。穴埋め補完なし。"),
            pages=[2],
            note="問題1",
            tags=["RC直列", "フィルタ", "未記入"],
            figures=[fig(2, "図1・問表3-1・グラフ用紙")],
            explanation=r"断片手書き: $\dot{V}_c=\dot{V}_c/V_c$（意味不明のまま原文）。右下に判読不能の薄い書き込み。",
        ),
        q(
            "EIC3-D1-Q2-1",
            U_D1,
            "calculation",
            r"問題2(1) $\dot{Z}=(6\angle\pi/6)(3\angle-2\pi/3)$ を極座標・直交座標で。",
            r"手書き: $=18\angle-\pi/2=18(0-j)=-18j$",
            pages=[2],
            tags=["複素数"],
        ),
        q(
            "EIC3-D1-Q2-2",
            U_D1,
            "calculation",
            r"問題2(2) $\dot{Z}=(1+j\sqrt{3})\times\sqrt{3}\angle(-\pi/4)$。",
            r"手書き: $2\angle\pi/3$ から $2\sqrt{3}\angle(\pi/12)=2\sqrt{3}(\cos\pi/12+j\sin\pi/12)$",
            pages=[2],
            tags=["複素数"],
        ),
        q(
            "EIC3-D1-Q3",
            U_D1,
            "calculation",
            r"問題3: $v=10\sqrt{2}\sin(\omega t-\pi/3)$[V] について極座標・直交、$j\dot{V}$、$-j\dot{V}$、フェーザ図。",
            r"手書き: (1) $\dot{V}=10\exp(-j\pi/3)=5-j5\sqrt{3}$（途中式に sin/cos の取り違え書き込みあり） (2) $j\dot{V}=10\exp(j\pi/6)$、$-j\dot{V}=10\exp(j5\pi/6)$",
            pages=[2],
            tags=["フェーザ"],
            figures=[fig(2, "手書きフェーザ図")],
            explanation="単位メモ: 特に断りのない限り V。",
        ),
        q(
            "EIC3-D1-Q4",
            U_D1,
            "calculation",
            r"問題4: $i=10\sqrt{2}\sin(100t+\pi/6)$ が R=5Ω, L=50mH, C=2mF に流れるときの $\dot{I},\dot{V}_R,\dot{V}_L,\dot{V}_C$ と瞬時値・フェーザ図。",
            r"手書き(p.3): $\dot{I}=10\exp(j\pi/6)$、$\dot{V}_R=50\exp(j\pi/6)$、$v_R=50\sqrt{2}\sin(100t+\pi/6)$；$\dot{V}_L$ は πf 経由で $100\pi\exp(j2\pi/3)$ に訂正；$v_L$ 振幅は判読不能；$V_C$ 導出で $1/(4\pi)\exp(-j\pi/3)$、$v_C=(1/(4\pi))\sin(100t-\pi/3)$",
            pages=[2, 3],
            note="問題文p.2・解答手書きp.3",
            tags=["RLC", "素子電圧"],
            figures=[fig(3, "問題4 手書き解答")],
            explanation=r"ページ下部に別紙写り込みと $16\sqrt{2}\exp(-j\pi/4)$・問図5-39 の断片あり。",
        ),
    ]
)

# ---- 配布資料 3 (p.4) ----
U_D3 = "配布資料3（アドミタンス）"
QUESTIONS.extend(
    [
        q(
            "EIC3-D3-TABLE",
            U_D3,
            "cloze",
            "回路要素（r, L, C）のアドミタンス・コンダクタンス・サセプタンス表を埋めよ。",
            unverified("表は空欄のまま。穴埋め補完なし。"),
            pages=[4],
            tags=["アドミタンス", "未記入"],
            figures=[fig(4, "アドミタンス定義図・要素図・空欄表")],
        ),
        q(
            "EIC3-D3-Q1",
            U_D3,
            "calculation",
            r"問題1: 問図5-31 の $\dot{Y}$ と G,B,|Y|,θY。",
            r"手書き: $\dot{Y}=(1+j3)^{-1}+1/(-5j)=1/10 - j/10$ [S]；$G=1/10$, $B=-1/10$, $|Y|=\sqrt{2}/10$, $θ_Y=-45°$",
            pages=[4],
            tags=["アドミタンス"],
            figures=[fig(4, "問図5-31")],
        ),
        q(
            "EIC3-D3-Q2",
            U_D3,
            "calculation",
            r"問題2: 問図5-39（V=100∠0、r2=25 と r1=3+X=4 の並列）の電流 $\dot{I}$ の極座標。",
            r"手書き: 途中計算の後 $16-j16=16\sqrt{2}\exp(-j\pi/4)$",
            pages=[4],
            tags=["並列回路", "アドミタンス"],
            figures=[fig(4, "問図5-39")],
        ),
    ]
)

# ---- 配布資料 4 (p.5) ----
U_D4 = "配布資料4（電力）"
QUESTIONS.extend(
    [
        q(
            "EIC3-D4-Q1",
            U_D4,
            "calculation",
            r"問題1: $\dot{V}=15\angle-10°$[V], $\dot{I}=110\angle-10°$[A] の皮相・力率・有効・無効。",
            r"手書き: S=1650[VA], P=1650[W], Q=0[var]",
            pages=[5],
            tags=["電力"],
        ),
        q(
            "EIC3-D4-Q2",
            U_D4,
            "calculation",
            r"問題2: $v=100\sin(\pi t+\pi/9)$, $i=40\sin(\pi t-2\pi/9)$ の皮相・力率・有効・無効。",
            r"手書き: 位相差メモ 3π/9；$S=2000$[VA], $P=1000$[W], $Q=1000\sqrt{3}$[var]",
            pages=[5],
            tags=["電力"],
        ),
        q(
            "EIC3-D4-Q3",
            U_D4,
            "calculation",
            r"問題3: V=100[V], I=40[A], 電圧が電流より60°進み。皮相・力率・有効・無効。",
            r"手書き: S=4000[VA], P=2000[W], Q=2000√3[var]",
            pages=[5],
            tags=["電力"],
        ),
        q(
            "EIC3-D4-Q4",
            U_D4,
            "calculation",
            r"問題4: $\dot{V}=100+j100\sqrt{3}$[V], $\dot{I}=10\sqrt{3}+j10$[A] の有効・無効・力率。",
            unverified("未記入。穴埋め補完なし。"),
            pages=[5],
            tags=["電力", "未記入"],
        ),
    ]
)

# ---- 配布資料 5 (p.6) ----
U_D5 = "配布資料5（複素電力・力率改善）"
QUESTIONS.extend(
    [
        q(
            "EIC3-D5-Q1",
            U_D5,
            "calculation",
            r"問題1: R=10Ω と C=10^3/π[μF] 直列、f=50Hz、$\dot{V}=100\angle0°$。皮相・力率・有効・無効。",
            unverified(r"手書きは $\dot{Z}=10+\cdots=10$ までで途中。穴埋め補完なし。"),
            pages=[6],
            tags=["複素電力", "未記入"],
        ),
        q(
            "EIC3-D5-Q2",
            U_D5,
            "calculation",
            r"問題2: 遅れ力率0.9、有効電力1800[W] の皮相電力と無効電力。",
            unverified("未記入（力率改善の定義枠のみ印刷）。穴埋め補完なし。"),
            pages=[6],
            tags=["力率", "未記入"],
            explanation="印刷: 力率改善…無効電力を減らして力率を1に近づけること。",
        ),
        q(
            "EIC3-D5-Q3",
            U_D5,
            "calculation",
            r"問題3: 問図6-3（R+jωL と C 並列）の力率1となる可変 C の式。",
            unverified(r"手書きは $\dot{Z}=((R+j\omega L)^{-1}+(1/(j\omega C))^{-1})^{-1}=R$ まで。穴埋め補完なし。"),
            pages=[6],
            tags=["力率", "未記入"],
            figures=[fig(6, "問図6-3")],
        ),
    ]
)

# ---- 配布資料 6 (p.7) ----
U_D6 = "配布資料6（最大電力供給）"
QUESTIONS.extend(
    [
        q(
            "EIC3-D6-DERIV",
            U_D6,
            "calculation",
            r"図6-23 の最大電力条件の導出（$X=-X_0$ など）。",
            r"手書き: $\dot{I}=\dot{V}_0/((R_0+R)+j(X_0+X))$、$P=|\dot{V}_0|^2 R/((R_0+R)^2+(X_0+X)^2)$；R一定で $X=-X_0$ のとき最大、$P=|\dot{V}_0|^2 R/(R_0+R)^2$",
            pages=[7],
            tags=["整合", "最大電力"],
            figures=[fig(7, "図6-23")],
        ),
        q(
            "EIC3-D6-Q1",
            U_D6,
            "calculation",
            r"問題1: 問図6-6（|V0|=100、r0=10^3 と C=1μF 並列電源、負荷 RL+L 直列、ω=10^3）で最大電力となる RL,L と最大電力。",
            unverified(r"手書きは $Z_0=1\times10^{-3}+j1\times10^{-3}$ のみ。穴埋め補完なし。"),
            pages=[7],
            tags=["整合", "未記入"],
            figures=[fig(7, "問図6-6")],
        ),
        q(
            "EIC3-D6-Q2",
            U_D6,
            "calculation",
            r"問題2: V0=60、Z0=0.3+j0.9、負荷 RL∥C、ω=10^3。最大電力の RL,C と最大電力。",
            r"手書き: $R_L=0.3$Ω、$X_C=-0.9$Ω、$C=1.11$mF；最大電力メモ $(100\sout{[判読不能]})^2\cdot0.3=3000$[W]",
            pages=[7],
            tags=["整合"],
        ),
    ]
)

# ---- 問題 17.x (p.8-9) ----
U_17 = "問題17.6〜17.10（RLC直列）"
QUESTIONS.extend(
    [
        q(
            "EIC3-P176",
            U_17,
            "calculation",
            r"問題17.6: ω=500、E=40∠0、R=10、L=20mH、C=100μF 直列の $\dot{I},\dot{V}$（C両端）とフェーザ。",
            r"解答: $\dot{I}=2\sqrt{2}\angle45°$[A]、$\dot{V}=40\sqrt{2}\angle-45°$[V]",
            pages=[8, 9],
            note="問題p.8・解答p.9",
            tags=["RLC直列"],
            figures=[fig(8, "問題17.6 回路"), fig(9, "17.6 解答フェーザ")],
            explanation="p.8 に学生解答なし。解答ページの印刷解を原文として採用。",
        ),
        q(
            "EIC3-P177-1",
            U_17,
            "calculation",
            r"問題17.7(1): E=150、ω=100。S1,S2開で I=5 同相、S2のみ閉で I=3。R,L,C を求めよ。",
            r"手書き: R=30Ω、L=0.4H、C=250μF（400 を取り消し）。解答も R=30、L=0.4H、C=250μF",
            pages=[8, 9],
            tags=["RLC直列", "スイッチ"],
            figures=[fig(8, "問題17.7 回路")],
        ),
        q(
            "EIC3-P177-2",
            U_17,
            "calculation",
            r"問題17.7(2): S1のみ閉じたときの I。",
            r"手書き・解答: 3[A]",
            pages=[8, 9],
            tags=["RLC直列"],
        ),
        q(
            "EIC3-P177-3",
            U_17,
            "calculation",
            r"問題17.7(3): S1とS2を閉じたときの I。",
            r"手書き・解答: 5[A]",
            pages=[8, 9],
            tags=["RLC直列"],
        ),
        q(
            "EIC3-P178",
            U_17,
            "calculation",
            r"問題17.8: E=40∠0、R=10√3、XL=15、XC=-5 の Z,I,実効値,位相。",
            r"手書き: Z=20Ω、$\dot{I}=2\angle-\pi/6$（別記 $1/20\angle-30°$）。解答: $\dot{Z}=20\angle30°$、$\dot{I}=2\angle-30°$、I=2、θ=-30°",
            pages=[8, 9],
            tags=["RLC直列"],
            figures=[fig(8, "問題17.8 回路・三角形")],
        ),
        q(
            "EIC3-P179",
            U_17,
            "calculation",
            r"問題17.9: R=40、X=30、V=100 の電流 I。",
            r"手書き: Z=50∠tan^{-1}(3/4)、I=2∠-tan^{-1}(3/4)[A]。解答: I=2[A]",
            pages=[8, 9],
            tags=["インピーダンス"],
        ),
        q(
            "EIC3-P1710",
            U_17,
            "calculation",
            r"問題17.10: R=30、X=10 の G,B。",
            r"手書き: G=3/100[S], B=-1/100[S]。解答: G=30[mS], B=-10[mS]",
            pages=[8, 9],
            tags=["アドミタンス"],
        ),
    ]
)

# ---- 問題 19.x (p.10-11) ----
U_19 = "問題19.4〜19.7（直並列）"
QUESTIONS.extend(
    [
        q(
            "EIC3-P194",
            U_19,
            "calculation",
            r"問題19.4: ω=100、E=4、I=IL=IC=2[A] のフェーザと R,L,C。",
            r"解答: IC=j2、IL=2∠-30°；C=5[mF]、R=√3[Ω]、L=10[mH]",
            pages=[10, 11],
            tags=["並列回路"],
            figures=[fig(10, "問題19.4 回路"), fig(11, "19.4 解答フェーザ")],
            explanation="p.10 に学生解答なし。解答ページの印刷解を原文として採用。",
        ),
        q(
            "EIC3-P195-1",
            U_19,
            "calculation",
            r"問題19.5(1): 回路(a) E=10、R=1、L=30mH、ω=100 の I1。",
            r"解答: $\dot{I}_1=1-j3$[A]、$I_1=\sqrt{10}$[A]",
            pages=[10, 11],
            tags=["直列回路"],
            figures=[fig(10, "問題19.5 回路")],
        ),
        q(
            "EIC3-P195-2",
            U_19,
            "calculation",
            r"問題19.5(2): 回路(b) で C を変数とした I2,I。",
            r"解答: $\dot{I}_2=j1000C$、$\dot{I}=1+j(1000C-3)$",
            pages=[10, 11],
            tags=["並列回路"],
        ),
        q(
            "EIC3-P195-3",
            U_19,
            "calculation",
            r"問題19.5(3): I 最小の C とフェーザ。",
            r"解答: C=3[mF]、I2=j3、I=1",
            pages=[10, 11],
            tags=["並列回路"],
        ),
        q(
            "EIC3-P196",
            U_19,
            "calculation",
            r"問題19.6: ブリッジ位相推移器の出力 V と ω=0,R/L,∞ のとき。",
            r"解答: $\dot{V}=((R-j\omega L)/(R+j\omega L))\dot{E}$、|V|=E；ω=0で E∠0、ω=R/L で E∠-90°、ω→∞ で E∠-180°",
            pages=[10, 11],
            tags=["位相推移器"],
            figures=[fig(10, "問題19.6 回路")],
        ),
        q(
            "EIC3-P197",
            U_19,
            "calculation",
            r"問題19.7: L=CR^2 のとき合成アドミタンス・インピーダンス。",
            r"解答: Y=1/R、Z=R（定抵抗回路）",
            pages=[10, 11],
            tags=["定抵抗回路"],
            figures=[fig(10, "問題19.7 回路"), fig(11, "等価説明図")],
        ),
    ]
)

# ---- ドリル 23 (p.12-13) ----
U_DR = "ドリル no.23（交流電力）"
QUESTIONS.extend(
    [
        q(
            "EIC3-DR23-1-1",
            U_DR,
            "calculation",
            r"23.1(1) V=100∠-30°、I=2∠30° の P, Pr, Pa。",
            r"手書き: P=25W, Pr=43Var, Pa=50VA（$\dot{P}=50\angle-60°$）。解答: P=100[W], Pr=-100√3≒-173[var], Pa=200[VA]",
            pages=[12, 13],
            tags=["電力"],
            figures=[fig(12, "ドリル no.23（クラス欄はマスク済み）")],
            explanation="学生計算は VI/2 系の誤りを含む原文。class 欄はマスク済み。",
        ),
        q(
            "EIC3-DR23-1-2",
            U_DR,
            "calculation",
            r"23.1(2) V=2+j4、I=2+j1 の P, Pr, Pa。",
            r"手書き: P=1.6W, Pr=1.2Var, Pa=2VA。解答: $\dot{P}=8+j6$ → P=8[W], Pr=6[var], Pa=10[VA]",
            pages=[12, 13],
            tags=["電力"],
            explanation=r"学生は $\dot{P}$ を 8/5+j6/5 と誤記。原文として残す。",
        ),
        q(
            "EIC3-DR23-1-3",
            U_DR,
            "calculation",
            r"23.1(3) V=10、Z=3+j1 の P, Pr, Pa。",
            r"解答: Z=√10、I=√10、P=30[W], Pr=10[var], Pa=10√10≒31.6[VA]",
            pages=[12, 13],
            tags=["電力"],
            explanation="p.12 は未記入。解答ページの印刷解を原文として採用。",
        ),
        q(
            "EIC3-DR23-1-4",
            U_DR,
            "calculation",
            r"23.1(4) V=10、P=16、Pr=12 の力率と I。",
            r"解答: Pa=20[VA], I=2[A], cosθ=0.8",
            pages=[12, 13],
            tags=["力率"],
            explanation="p.12 は未記入。解答ページの印刷解を原文として採用。",
        ),
        q(
            "EIC3-DR23-1-5",
            U_DR,
            "calculation",
            r"23.1(5) I=2、P=60、cosθ=0.6、Zは容量性。V と Z。",
            r"解答: V=50[V], Z=25、$\dot{Z}=15-j20$[Ω]",
            pages=[12, 13],
            tags=["力率", "インピーダンス"],
            explanation="p.12 は未記入。解答ページの印刷解を原文として採用。",
        ),
        q(
            "EIC3-DR23-2-1",
            U_DR,
            "calculation",
            r"23.2(1) ω=100、E=20、R=6、L=80mH 直列の P,Pr,Pa。",
            r"解答: Z=6+j8、I=2、P=24[W], Pr=32[var], Pa=40[VA]",
            pages=[12, 13],
            tags=["電力"],
            figures=[fig(12, "23.2(1) 回路")],
            explanation="p.12 は未記入。解答ページの印刷解を原文として採用。",
        ),
        q(
            "EIC3-DR23-2-2",
            U_DR,
            "calculation",
            r"23.2(2) E=10、R=10∥C=2mF、ω=100 の P,Pr,Pa。",
            r"解答: P=10[W], Pr=-20[var], Pa=10√5≒22.4[VA]",
            pages=[12, 13],
            tags=["電力"],
            explanation="p.12 は未記入。解答ページの印刷解を原文として採用。",
        ),
        q(
            "EIC3-DR23-2-3",
            U_DR,
            "calculation",
            r"23.2(3) E=10、R=1+L=30mH と C=2mF 並列、ω=100。",
            r"解答: P=10[W], Pr=10[var], Pa=10√2≒14.1[VA]",
            pages=[12, 13],
            tags=["電力"],
            explanation="p.12 は未記入。解答ページの印刷解を原文として採用。",
        ),
        q(
            "EIC3-DR23-3",
            U_DR,
            "calculation",
            r"23.3: 50[V]、誘導性力率0.8、P=200[W] の I,Z,Pr,Pa。",
            r"解答: Pa=250[VA], Pr=150[var], I=5[A], $\dot{Z}=8+j6$[Ω]",
            pages=[12, 13],
            tags=["電力"],
            figures=[fig(12, "23.3 回路")],
            explanation="p.12 は未記入。解答ページの印刷解を原文として採用。",
        ),
    ]
)

# ---- 小テスト No.1 (p.14) ----
U_QZ = "小テスト No.1"
QUESTIONS.extend(
    [
        q(
            "EIC3-QZ1-Q1-1",
            U_QZ,
            "calculation",
            r"問題1(1) $z=1/(1+j\sqrt{3})$ を極座標表示に直せ。",
            r"手書き: $(1-j\sqrt{3})/4 = 1/2\exp(-j\pi/3)$",
            pages=[14],
            tags=["複素数", "小テスト"],
            figures=[fig(14, "小テスト No.1（氏名・出席番号欄はマスク済み）")],
            explanation=r"採点: 丸。余白に直角三角形メモと $e^{i\pi}+1=0$。赤点数 38（全体）。",
        ),
        q(
            "EIC3-QZ1-Q1-2",
            U_QZ,
            "calculation",
            r"問題1(2) $z=1/(1\angle -2\pi/3)$ を極座標表示に直せ。",
            r"手書き: $\exp(j 2\pi/3)$",
            pages=[14],
            tags=["複素数", "小テスト"],
            explanation="採点: 丸。赤点数 20（問題1付近）。",
        ),
        q(
            "EIC3-QZ1-Q2",
            U_QZ,
            "calculation",
            r"問題2: 端子ab間の並列 R,L,C（R=10Ω, L=0.1H, C=500μF, ω=100 rad/s）の合成インピーダンスと合成アドミタンス。",
            r"手書き（原文）: $Z=5+j5=5\sqrt{2}\exp(j\pi/4)$、$|Z|=7.07$[S]；$A=Z^{-1}=1/10 - j 199/2000$、$A=0.141$[S^{-1}]",
            pages=[14],
            tags=["アドミタンス", "小テスト", "学生誤答"],
            figures=[fig(14, "問題2 並列RLC図")],
            explanation=(
                "採点: 斜線（誤り）。単位 [S]/[S^{-1}] も誤り。"
                "検算メモ（解答の書き換えではない）: Y=1/R+1/(jωL)+jωC=0.1-j0.05、Z=8+j4。"
                "分数 1/10 と 199/2000 はPDFで再確認。"
            ),
            corrections=[
                corr(
                    "answer.student_Z_unit",
                    "7.07 [S]",
                    "原文のまま残し、単位誤りと採点斜線を explanation に分離",
                    "PDF照合",
                ),
                corr(
                    "calc.parallel_RLC",
                    "学生 Z=5+j5",
                    "検算仮説 Z=8+j4（学生解答は変更しない）",
                    "検算",
                ),
            ],
        ),
        q(
            "EIC3-QZ1-Q3-1",
            U_QZ,
            "calculation",
            r"問題3(1) $i=0.2\sqrt{2}\sin(1000t+\pi/6)$[A] のフェーザ（極座標）。",
            r"手書き: $\dot{I}=0.2\exp(j\pi/6)$[A]",
            pages=[14],
            tags=["フェーザ", "小テスト"],
            explanation="採点: 丸。赤点数 18（問題3付近）。",
        ),
        q(
            "EIC3-QZ1-Q3-2",
            U_QZ,
            "calculation",
            r"問題3(2) R=50Ω, L=20mH, C=5μF 直列に同電流が流れるときの VR,VL,VC（極座標）。",
            r"手書き（原文）: $\dot{V}_R=10\exp(j\pi/6)$[V]；$\dot{V}_L=4.0\exp(j 7\pi/6)$[V]；$\dot{V}_C=40\exp(-j 5\pi/6)$[V]",
            pages=[14],
            tags=["RLC直列", "小テスト", "学生誤答"],
            explanation=(
                "採点: VR は丸。VL・VC は斜線（誤り）。"
                "検算メモ: ωL=20 → VL=4∠(π/6+π/2)=4∠2π/3；"
                "1/(ωC)=200 → VC=40∠(π/6−π/2)=40∠(−π/3)。"
                "学生の 7π/6 と −5π/6 は原文として残す。"
            ),
            corrections=[
                corr(
                    "transcript.VL_phase",
                    "2π/3・採点丸",
                    "PDFは 7π/6・採点斜線",
                    "マスク版PDF照合",
                ),
                corr(
                    "calc.VC_phase",
                    "学生 −5π/6",
                    "正解仮説 −π/3（学生解答は変更しない）",
                    "検算",
                ),
            ],
        ),
        q(
            "EIC3-QZ1-Q3-3",
            U_QZ,
            "calculation",
            r"問題3(3) (2)の各電圧を瞬時値で示せ。",
            r"手書き（原文）: $v_R=10\sqrt{2}\sin(1000t+\pi/6)$；$v_L=4.0\sqrt{2}\sin(1000t+7\pi/6)$；$v_C=40\sqrt{2}\sin(1000t-5\pi/6)$",
            pages=[14],
            tags=["瞬時値", "小テスト", "学生誤答"],
            explanation="採点: 斜線系（(2)の位相誤りを継承）。正解仮説の位相は VL:2π/3、VC:−π/3。",
        ),
    ]
)


def write_corrected_transcript() -> None:
    src_path = PIPELINE / "transcripts" / "gemini_transcript_source.md"
    text = src_path.read_text(encoding="utf-8")
    # Apply key p.14 fixes in corrected transcript
    replacements = [
        (
            r"{{手書き: $\dot{V}_L = 4.0\exp(j\frac{2}{3}\pi)\ [\text{V}]$}} {{採点: 丸}}",
            r"{{手書き: $\dot{V}_L = 4.0\exp(j\frac{7}{6}\pi)\ [\text{V}]$}} {{採点: 斜線}}",
        ),
        (
            r"{{手書き: $v_L = 4.0\sqrt{2}\sin(1000t + \frac{2}{3}\pi)\ [\text{V}]$}} {{採点: チェック}}",
            r"{{手書き: $v_L = 4.0\sqrt{2}\sin(1000t + \frac{7}{6}\pi)\ [\text{V}]$}} {{採点: 斜線}}",
        ),
        (
            r"{{手書き: $\dot{V}_C = 40\exp(-j\frac{5}{6}\pi)\ [\text{V}]$}} {{採点: チェック}}",
            r"{{手書き: $\dot{V}_C = 40\exp(-j\frac{5}{6}\pi)\ [\text{V}]$}} {{採点: 斜線}}",
        ),
        (
            r"{{手書き: $v_C = 40\sqrt{2}\sin(1000t - \frac{5}{6}\pi)\ [\text{V}]$}} {{採点: チェック}}",
            r"{{手書き: $v_C = 40\sqrt{2}\sin(1000t - \frac{5}{6}\pi)\ [\text{V}]$}} {{採点: 斜線}}",
        ),
        (
            r"{{手書き: $v_R = 10\sqrt{2}\sin(1000t + \frac{\pi}{6})\ [\text{V}]$}} {{採点: チェック}}",
            r"{{手書き: $v_R = 10\sqrt{2}\sin(1000t + \frac{\pi}{6})\ [\text{V}]$}} {{採点: 丸/チェック系}}",
        ),
    ]
    for before, after in replacements:
        if before not in text:
            # already corrected or slightly different; continue
            continue
        text = text.replace(before, after)
    header = (
        "<!-- 訂正済: マスク版PDFと照合。p.14 の VL 位相は 7π/6、"
        "VC は −5π/6（学生誤答・採点斜線）。氏名・クラスはマスク済みのみ。 -->\n"
    )
    out = PIPELINE / "transcripts" / "exercises_quiz_2026-11_masked_corrected.md"
    out.write_text(header + text, encoding="utf-8")


def main() -> None:
    write_corrected_transcript()

    (PIPELINE / "corrections_log.json").write_text(
        json.dumps(CORRECTIONS, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    # questions_raw
    raw_dir = PIPELINE / "questions_raw"
    if raw_dir.exists():
        shutil.rmtree(raw_dir)
    raw_dir.mkdir(parents=True)
    for item in QUESTIONS:
        (raw_dir / f"{item['id']}.json").write_text(
            json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

    structured = {
        "schema_version": "1.0.0",
        "exam": EXAM,
        "subject": SUBJECT,
        "generated_at": NOW,
        "notes": (
            "採点済み課題・小テスト（マスク版14頁: 演習問題1、配布資料1/3〜6、"
            "問題17.6〜19.7、ドリルno.23、小テストNo.1）。"
            "手書き・印刷解答は original。空欄は unverified。"
            "穴埋め補完は未実施（filled=false）。公式範囲表は未入手。"
            "氏名・出席番号・クラスはマスク済み（復元しない）。"
        ),
        "questions": QUESTIONS,
    }
    struct_dir = ROOT / "structured"
    struct_dir.mkdir(parents=True, exist_ok=True)
    qpath = struct_dir / "questions.json"
    qpath.write_text(
        json.dumps(structured, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    unverified_ids = [
        item["id"]
        for item in QUESTIONS
        if (item.get("answer") or {}).get("status") == "unverified"
    ]
    n_corr = sum(len(item.get("corrections") or []) for item in QUESTIONS)
    n_inferred = sum(
        1
        for item in QUESTIONS
        if (item.get("answer") or {}).get("status") == "inferred"
    )

    status = {
        "exam": EXAM,
        "subject": SUBJECT,
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
            "validated": False,
            "app_data": False,
        },
        "counts": {
            "questions": len(QUESTIONS),
            "body_questions": len(QUESTIONS) - 1,
            "corrections": n_corr,
            "unverified": len(unverified_ids),
            "inferred_answers": n_inferred,
        },
        "unverified_ids": unverified_ids,
        "notes": (
            "進捗: 整備中。マスク済み exercises_quiz_2026-11_masked.pdf のみRAW。"
            "空欄穴埋めは未実施（filled=false）。公式範囲表は未入手。"
            "Question Bank: eic3_2026_03。"
        ),
    }
    (ROOT / "status.json").write_text(
        json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    note = f"""# 電気回路Ⅲ（2026/03）確認ノート

出典: `{SOURCE}`（採点済み課題・小テスト・マスク版、14ページ）

## 資料内訳

1. p.1 演習問題1
2. p.2〜3 配布資料1（問題4手書きは p.3）
3. p.4〜7 配布資料3〜6
4. p.8〜9 問題17.6〜17.10 と解答
5. p.10〜11 問題19.4〜19.7 と解答
6. p.12〜13 ドリル no.23 と解答（クラス欄はマスク済み）
7. p.14 小テスト No.1（赤ペン採点、氏名・出席番号欄はマスク済み）

## データ

- 構造化: `structured/questions.json`
- 文字起こし（訂正済）: `pipeline/transcripts/exercises_quiz_2026-11_masked_corrected.md`
- 訂正ログ: `pipeline/corrections_log.json`
- アプリ用: `app_data/`
- Question Bank: `eic3_2026_03`

## 注意

- 手書き・印刷解答は `original`。空欄は `unverified`（穴埋め補完なし / filled=false）。
- 学生誤答は原文のまま。採点マークと検算メモは explanation / corrections に分離。
- マスク欄の内容は「マスク済み」のみ。復元しない。
- 公式試験範囲は未入手。範囲表には写していない。
"""
    (ROOT / "確認ノート.md").write_text(note, encoding="utf-8")

    # Replace イーハトーブ placeholder notebook
    summary = """# 電気回路Ⅲ（2026/03）ノートまとめ

マスク版課題・小テスト（`RAW/exercises_quiz_2026-11_masked.pdf`）を取り込み済み。

- 正弦波・フェーザ・複素数表示
- アドミタンス、電力（有効・無効・皮相・力率）
- 最大電力供給（整合）
- RLC 直列・直並列の計算問題（17.x / 19.x）
- ドリル no.23（交流電力）
- 小テスト No.1（複素数・並列RLC・直列素子電圧）

詳細は `確認ノート.md` と `structured/questions.json` を参照。公式範囲表は未入手。
"""
    (ROOT / "ノートまとめ.md").write_text(summary, encoding="utf-8")

    md = struct_dir / "まとめ_構造化.md"
    lines = [
        f"# {SUBJECT} 構造化まとめ（{EXAM}）",
        "",
        f"生成: {NOW}",
        "",
        f"問数: {len(QUESTIONS)}（メタ含む） / 本文 {len(QUESTIONS)-1}",
        f"unverified: {len(unverified_ids)}",
        f"inferred: {n_inferred}",
        f"corrections: {n_corr}",
        "",
    ]
    for item in QUESTIONS:
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
                "questions": len(QUESTIONS),
                "body": len(QUESTIONS) - 1,
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
