#!/usr/bin/env python3
"""Build corrected transcript + structured/questions.json for 電子回路Ⅱ masked assignment."""

from __future__ import annotations

import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = Path(__file__).resolve().parent
SOURCE = "RAW/assignment_opamp_2026-11_masked.pdf"
EXAM = "2026/03"
SUBJECT = "電子回路Ⅱ"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

TOOLS = ["gemini-4-argon-transcript", "manual-page-image-check"]
TOOLS_CALC = TOOLS + ["manual-calc-check"]


def pv(value, status="original", rationale=None, tools=None):
    obj = {"value": value, "status": status}
    if rationale is not None:
        obj["rationale"] = rationale
    if tools is not None:
        obj["tools"] = tools
    return obj


def hand(value, *, calc=False, extra=None):
    rationale = "マスク済みページ画像の手書き解答を照合して読み取り。"
    if extra:
        rationale = rationale + " " + extra
    return pv(value, "inferred", rationale=rationale, tools=TOOLS_CALC if calc else TOOLS)


def corr(field, before, after, reason):
    return {"field": field, "before": before, "after": after, "reason": reason}


def fig(path, page, caption):
    return {
        "path": path,
        "page": page,
        "caption": pv(caption, "original"),
    }


def src(page, note=None):
    o = {"file": SOURCE, "page": page}
    if note:
        o["note"] = note
    return o


CORRECTIONS = [
    corr(
        "transcript:p1.q6.2.freq",
        "318 Hz（Gemini原文のまま）",
        "318 Hz（手書き・採点○）。検算注記: 横軸 0〜2π ms を1周期と読めば f≈159 Hz、π ms を1周期と読めば ≈318 Hz",
        "ページ画像照合で手書きは318 Hz・赤丸。周期解釈はグラフを要再確認",
    ),
    corr(
        "transcript:p1.q2.decimal",
        "{{手書き: 20√2 V}} {{採点: =28.28 V}} 等を混在表記",
        "手書きは 20√2 V / 10√2 V。小数は赤ペン採点側",
        "ページ画像照合。赤は採点、黒は解答",
    ),
    corr(
        "transcript:p1.q6.1.rms_decimal",
        "{{手書き: 2/√2 mV}} {{採点: =1.41 mV}}",
        "手書きは 2/√2 mV。≒1.41 mV は赤ペン採点",
        "ページ画像照合",
    ),
    corr(
        "transcript:p2.chip_name",
        "TL84CN",
        "TL084CN",
        "ページ画像照合。印刷見出しは TL084CN",
    ),
    corr(
        "transcript:p6.eq5.subscript",
        "{{手書き: 1}}（v2 添字訂正）",
        "{{採点: 1}}（赤ペンで第2項添字を 2→1 に訂正）",
        "ページ画像照合。赤は採点訂正、黒の下書きではない",
    ),
    corr(
        "transcript:p3.lecture_date",
        "10/16 を手書き扱い",
        "見出しの 10/16 は手書き記入、講義分は印刷",
        "ページ画像照合",
    ),
    corr(
        "transcript:stamp_names",
        "確認印に氏名らしき字",
        "確認印（日付のみ記録）。印から氏名を復元しない",
        "個人情報方針。採点側の印として日付のみ残す",
    ),
    corr(
        "calc:p1.q6.2",
        "手書き 318 Hz（採点○）",
        "検算メモ: T=2π×10^{-3} s なら f=1000/(2π)≈159.15 Hz",
        "学生解答は書き換えず併記。周期読み取り要確認",
    ),
]

# ---------------------------------------------------------------------------
# Questions
# ---------------------------------------------------------------------------
QUESTIONS: list[dict] = []


def add(q: dict):
    QUESTIONS.append(q)


add(
    {
        "id": "EC2-META-TRANSCRIPT-QC",
        "unit": "メタ（文字起こし訂正）",
        "form": "other",
        "stem": pv("文字起こしをマスク済みページ画像と照合して訂正した記録。"),
        "answer": pv("訂正ログ参照（pipeline/corrections_log.json および本問 corrections）"),
        "sources": [src(1, "メタ")],
        "tags": ["meta", "corrections"],
        "corrections": CORRECTIONS,
    }
)

# --- 10/2 lecture ---
UNIT_1002 = "オペアンプ基礎（10/2 講義分）"

add(
    {
        "id": "EC2-1002-Q1-1",
        "unit": UNIT_1002,
        "form": "true_false",
        "stem": pv("オペアンプの特徴: (1) 電圧利得が大きい。正しいものには○、誤っているものには×。"),
        "answer": hand("○"),
        "explanation": pv("採点: ○（赤丸）", "original"),
        "sources": [src(1, "問1(1)")],
        "tags": ["オペアンプ", "特徴", "○×"],
    }
)
add(
    {
        "id": "EC2-1002-Q1-2",
        "unit": UNIT_1002,
        "form": "true_false",
        "stem": pv("オペアンプの特徴: (2) 入力インピーダンスが小さい。正しいものには○、誤っているものには×。"),
        "answer": hand("×"),
        "explanation": pv("採点: ○（赤丸）。理想オペアンプの入力インピーダンスは大きい。", "original"),
        "sources": [src(1, "問1(2)")],
        "tags": ["オペアンプ", "特徴", "○×"],
    }
)
add(
    {
        "id": "EC2-1002-Q1-3",
        "unit": UNIT_1002,
        "form": "true_false",
        "stem": pv("オペアンプの特徴: (3) 差動増幅する。正しいものには○、誤っているものには×。"),
        "answer": hand("○"),
        "explanation": pv("採点: ○（赤丸）", "original"),
        "sources": [src(1, "問1(3)")],
        "tags": ["オペアンプ", "特徴", "○×"],
    }
)
add(
    {
        "id": "EC2-1002-Q1-4",
        "unit": UNIT_1002,
        "form": "true_false",
        "stem": pv("オペアンプの特徴: (4) 出力インピーダンスが小さい。正しいものには○、誤っているものには×。"),
        "answer": hand("○"),
        "explanation": pv("採点: ○（赤丸）", "original"),
        "sources": [src(1, "問1(4)")],
        "tags": ["オペアンプ", "特徴", "○×"],
    }
)

add(
    {
        "id": "EC2-1002-Q2-1",
        "unit": UNIT_1002,
        "form": "calculation",
        "stem": pv(
            r"正弦波電圧の実効値 $V_{rms}=10\,\mathrm{V}$ のとき、$V_{pp}$ を求めよ。"
        ),
        "answer": hand(r"$20\sqrt{2}\,\mathrm{V}$", calc=True),
        "explanation": hand(
            r"採点追記: $=28.28\,\mathrm{V}$（赤ペン）。関係: $V_{pp}=2\sqrt{2}\,V_{rms}$。",
            extra="赤ペン小数は採点側。",
        ),
        "sources": [src(1, "問2(1)")],
        "tags": ["実効値", "Vpp", "計算"],
    }
)
add(
    {
        "id": "EC2-1002-Q2-2",
        "unit": UNIT_1002,
        "form": "calculation",
        "stem": pv(
            r"正弦波電圧の実効値 $V_{rms}=10\,\mathrm{V}$ のとき、$V_{op}$ を求めよ。"
        ),
        "answer": hand(r"$10\sqrt{2}\,\mathrm{V}$", calc=True),
        "explanation": hand(
            r"採点追記: $=14.14\,\mathrm{V}$（赤ペン）。$V_{op}=\sqrt{2}\,V_{rms}$。",
            extra="赤ペン小数は採点側。",
        ),
        "sources": [src(1, "問2(2)")],
        "tags": ["実効値", "Vop", "計算"],
    }
)

add(
    {
        "id": "EC2-1002-Q3",
        "unit": UNIT_1002,
        "form": "calculation",
        "stem": pv(r"$2\,\mathrm{mV}$ 入力で $9\,\mathrm{mV}$ 出力のアンプのゲインは何 $\mathrm{dB}$ か。"),
        "answer": hand(r"$13.1\,\mathrm{dB}$", calc=True, extra=r"採点○。$20\log_{10}(9/2)\approx13.06$。"),
        "sources": [src(1, "問3")],
        "tags": ["ゲイン", "dB", "計算"],
    }
)
add(
    {
        "id": "EC2-1002-Q4",
        "unit": UNIT_1002,
        "form": "calculation",
        "stem": pv(r"$19\,\mathrm{V}$ 入力で $2\,\mathrm{V}$ 出力のアンプのゲインは何 $\mathrm{dB}$ か。"),
        "answer": hand(r"$-19.6\,\mathrm{dB}$", calc=True, extra=r"採点○。$20\log_{10}(2/19)\approx-19.55$。"),
        "sources": [src(1, "問4")],
        "tags": ["ゲイン", "dB", "計算"],
    }
)
add(
    {
        "id": "EC2-1002-Q5",
        "unit": UNIT_1002,
        "form": "calculation",
        "stem": pv(r"ゲイン $30\,\mathrm{dB}$ のとき、$1\,\mathrm{mV}$ 入力で何 $\mathrm{mV}$ 出力か。"),
        "answer": hand(r"$31.6\,\mathrm{mV}$", calc=True, extra="採点○。$10^{30/20}\\approx31.62$。"),
        "sources": [src(1, "問5")],
        "tags": ["ゲイン", "dB", "計算"],
    }
)

add(
    {
        "id": "EC2-1002-Q6-1",
        "unit": UNIT_1002,
        "form": "calculation",
        "stem": pv(r"図の波形 (a) の振幅 $V_{op}$ と実効値 $V_{rms}$ を答えよ。"),
        "answer": hand(
            r"$V_{op}=2\,\mathrm{mV}$,\ $V_{rms}=\dfrac{2}{\sqrt{2}}\,\mathrm{mV}$",
            calc=True,
        ),
        "explanation": hand(
            r"採点追記: $V_{rms}\fallingdotseq 1.41\,\mathrm{mV}$（赤ペン）。",
            extra="小数は採点側。",
        ),
        "figures": [
            fig(
                "pipeline/images/figures/fig_q6_waveforms.png",
                1,
                "波形 a（実線）と b（破線）",
            )
        ],
        "sources": [src(1, "問6(1)")],
        "tags": ["波形", "Vop", "Vrms"],
    }
)
add(
    {
        "id": "EC2-1002-Q6-2",
        "unit": UNIT_1002,
        "form": "calculation",
        "stem": pv(r"図の波形 (a)(b) の周波数 $f$ を答えよ。"),
        "answer": hand(
            r"$318\,\mathrm{Hz}$",
            calc=True,
            extra="採点○。検算: 横軸0〜2π msを1周期とすれば≈159 Hz。手書きは書き換えない。",
        ),
        "corrections": [
            corr(
                "answer",
                "検算候補 ≈159 Hz（T=2π ms）",
                "手書き 318 Hz を保持（採点○）",
                "周期の読み取りが曖昧なため原文優先。要再確認",
            )
        ],
        "figures": [
            fig(
                "pipeline/images/figures/fig_q6_waveforms.png",
                1,
                "波形 a・b",
            )
        ],
        "sources": [src(1, "問6(2)")],
        "tags": ["波形", "周波数"],
    }
)
add(
    {
        "id": "EC2-1002-Q6-3",
        "unit": UNIT_1002,
        "form": "calculation",
        "stem": pv(r"(a) を入力、(b) を出力としたときのゲインは何 $\mathrm{dB}$ か。"),
        "answer": hand(
            r"$G=20\log\dfrac{5}{2}\fallingdotseq 7.96\,\mathrm{dB}$",
            calc=True,
            extra="採点○（7.96 を赤丸）。",
        ),
        "figures": [
            fig(
                "pipeline/images/figures/fig_q6_waveforms.png",
                1,
                "波形 a・b",
            )
        ],
        "sources": [src(1, "問6(3)")],
        "tags": ["波形", "ゲイン", "dB"],
    }
)
add(
    {
        "id": "EC2-1002-Q6-4",
        "unit": UNIT_1002,
        "form": "calculation",
        "stem": pv(r"(a) の位相を $0\,\mathrm{rad}$ とすると、(b) の位相は何 $\mathrm{rad}$ か。"),
        "answer": hand(
            r"$+\dfrac{\pi}{6}\,\mathrm{rad}$",
            calc=True,
            extra="黒インク手書き＋赤丸。赤ペン新規記入ではない。",
        ),
        "figures": [
            fig(
                "pipeline/images/figures/fig_q6_waveforms.png",
                1,
                "波形 a・b",
            )
        ],
        "sources": [src(1, "問6(4)")],
        "tags": ["波形", "位相"],
    }
)

add(
    {
        "id": "EC2-1002-Q7-TL084",
        "unit": UNIT_1002,
        "form": "short_answer",
        "stem": pv("オペアンプ TL084CN のピン配置を調査せよ（14ピン DIP）。"),
        "answer": hand(
            "1:1OUT, 2:1IN-, 3:1IN+, 4:VCC+, 5:2IN+, 6:2IN-, 7:2OUT, "
            "8:3OUT, 9:3IN-, 10:3IN+, 11:VCC-, 12:4IN+, 13:4IN-, 14:4OUT"
        ),
        "explanation": pv("採点: ○（大赤丸）。確認印あり（日付のみ記録）。", "original"),
        "figures": [
            fig(
                "pipeline/images/figures/fig_q7_tl084cn_pins.png",
                2,
                "TL084CN ピン配置（手書き）",
            )
        ],
        "sources": [src(2, "問7 TL084CN")],
        "tags": ["ピン配置", "TL084CN"],
        "corrections": [
            corr("stem", "TL84CN", "TL084CN", "印刷見出し照合")
        ],
    }
)
add(
    {
        "id": "EC2-1002-Q7-LM741",
        "unit": UNIT_1002,
        "form": "short_answer",
        "stem": pv("オペアンプ LM741 のピン配置を調査せよ（8ピン DIP）。"),
        "answer": hand(
            "1:OFFSET NULL, 2:INVERTING INPUT, 3:NON-INVERTING INPUT, 4:V-, "
            "5:OFFSET NULL, 6:OUTPUT, 7:V+, 8:NC"
        ),
        "explanation": pv("採点: ○（大赤丸）。確認印あり（日付のみ記録）。", "original"),
        "figures": [
            fig(
                "pipeline/images/figures/fig_q7_lm741_pins.png",
                2,
                "LM741 ピン配置（手書き）",
            )
        ],
        "sources": [src(2, "問7 LM741")],
        "tags": ["ピン配置", "LM741"],
    }
)

# --- 10/16 ---
UNIT_1016 = "反転増幅（10/16 講義分）"

add(
    {
        "id": "EC2-1016-Q1",
        "unit": UNIT_1016,
        "form": "calculation",
        "stem": pv(
            r"What is the output voltage $v_o$ in the circuit, assuming an infinite open-loop gain $A_O$? "
            r"（反転増幅: $v_i=1.5\,\mathrm{V}$, $R_1=20\,\mathrm{k}\Omega$, $R_2=250\,\mathrm{k}\Omega$）"
        ),
        "answer": hand(
            r"$v_o=-18.75\,\mathrm{V}$（過程: $A_v=-250/20=-12.5$）",
            calc=True,
        ),
        "figures": [
            fig(
                "pipeline/images/figures/fig_1016_q1_inverting.png",
                3,
                "反転増幅回路（問1）",
            )
        ],
        "sources": [src(3, "問1")],
        "tags": ["反転増幅", "計算", "英語設問"],
    }
)
add(
    {
        "id": "EC2-1016-Q2",
        "unit": UNIT_1016,
        "form": "calculation",
        "stem": pv(
            r"What input voltage $v_i$ results in an output of $2\,\mathrm{V}$ in the circuit, "
            r"assuming an open-loop gain $A_O=\infty$? "
            r"（$R_1=20\,\mathrm{k}\Omega$, $R_2=1\,\mathrm{M}\Omega$）"
        ),
        "answer": hand(
            r"$v_i=-40\,\mathrm{mV}$（過程: $A_v=-50$）",
            calc=True,
            extra="図上に手書き 1000k（=1MΩ）あり。",
        ),
        "figures": [
            fig(
                "pipeline/images/figures/fig_1016_q2_inverting.png",
                3,
                "反転増幅回路（問2）",
            )
        ],
        "sources": [src(3, "問2")],
        "tags": ["反転増幅", "計算", "英語設問"],
    }
)
add(
    {
        "id": "EC2-1016-Q3",
        "unit": UNIT_1016,
        "form": "essay",
        "stem": pv(
            "Summarize the following text in Japanese.（反転増幅の KCL 導出英文: "
            r"$v_o=-(R_f/R_1)v_i$, $A_v=-R_f/R_1$）"
        ),
        "answer": hand(
            "この回路において、非反転入力は接地されている。"
            "$v_i$ は $R_1$ を介して反転入力に接続されている。また、帰還抵抗 $R_f$ は反転入力と出力の間を接続している。"
            "私たちの目標は、入力電圧 $v_i$ と出力電圧 $v_o$ の間の関係を得ることである。"
            "KCLを節点1に適用する。"
            "$i_1$ は $i_f$ と等しい。よって、$v_i$ から $v_1$ を引いたものを $R_1$ で割ったものは、"
            "$v_1$ から $v_o$ を引いたものを $R_f$ で割ったものと等しい。"
            "しかし、理想的な演算増幅器において $v_1$ と $v_2$ は等しくその値は 0 であることから、非反転端子は接地されている。"
            "ゆえに、$v_i/R_1=-v_o/R_f$ となり、"
            r"$v_o=-(R_f/R_1)v_i$、$A_v=v_o/v_i=-R_f/R_1$。"
        ),
        "explanation": pv("採点: 確認印（日付のみ）。要約中の挿入は手書き。", "original"),
        "figures": [
            fig(
                "pipeline/images/figures/fig_1016_q3_inverting_kcl.png",
                4,
                "反転増幅 KCL 図（手書き注記）",
            )
        ],
        "sources": [src(4, "問3 要約")],
        "tags": ["反転増幅", "要約", "英語"],
    }
)

# --- 10/23 ---
UNIT_1023 = "非反転増幅（10/23 講義分）"

add(
    {
        "id": "EC2-1023-Q1",
        "unit": UNIT_1023,
        "form": "essay",
        "stem": pv(
            "Summarize the following text in Japanese.（非反転増幅の導出: "
            r"$v_o=(1+R_f/R_1)v_i$, $A_v=1+R_f/R_1$）"
        ),
        "answer": hand(
            "この回路において、入力電圧 $v_i$ は非反転入力端子に直接入力されている。"
            "そして抵抗 $R_1$ は接地点と反転入力の間をつなげる。"
            "私たちは出力電圧 $v_o$ と電圧増幅率 $A_v$ に興味がある。"
            "キルヒホッフの電流則を反転入力に当てはめると、"
            r"$i_1=i_2$ すなわち $(0-v_1)/R_1=(v_1-v_o)/R_f$。"
            r"しかし $v_1=v_2=v_i$。よって $(-v_i)/R_1=(v_i-v_o)/R_f$ となり、"
            r"$v_o=(1+R_f/R_1)v_i$。電圧利得は $A_v=v_o/v_i=1+R_f/R_1$ であり、これは負ではない。"
        ),
        "figures": [
            fig(
                "pipeline/images/figures/fig_1023_q1_noninverting.png",
                5,
                "非反転増幅回路",
            )
        ],
        "sources": [src(5, "問1 要約")],
        "tags": ["非反転増幅", "要約", "英語"],
    }
)
add(
    {
        "id": "EC2-1023-Q2",
        "unit": UNIT_1023,
        "form": "calculation",
        "stem": pv(
            r"Calculate the output voltage $v_o$ of a noninverting amplifier for "
            r"$v_i=2\,\mathrm{V}$, $R_f=500\,\mathrm{k}\Omega$, $R_1=100\,\mathrm{k}\Omega$, $A_O=\infty$."
        ),
        "answer": hand(
            r"$v_o=\dfrac{2\,\mathrm{V}}{100\,\mathrm{k}\Omega}\cdot 500\,\mathrm{k}\Omega+2\,\mathrm{V}=12\,\mathrm{V}$",
            calc=True,
        ),
        "figures": [
            fig(
                "pipeline/images/figures/fig_1023_q2_noninverting.png",
                5,
                "非反転増幅（問2）",
            )
        ],
        "sources": [src(5, "問2")],
        "tags": ["非反転増幅", "計算"],
    }
)
add(
    {
        "id": "EC2-1023-Q3",
        "unit": UNIT_1023,
        "form": "calculation",
        "stem": pv(
            r"Calculate the voltage gain $A_v$ of a noninverting amplifier for "
            r"$R_f=200\,\mathrm{k}\Omega$, $R_1=10\,\mathrm{k}\Omega$, $A_O=\infty$."
        ),
        "answer": hand(r"$A_v=200/10+1=21$", calc=True),
        "explanation": pv("採点: 確認印（日付のみ）。", "original"),
        "figures": [
            fig(
                "pipeline/images/figures/fig_1023_q3_noninverting.png",
                5,
                "非反転増幅（問3）",
            )
        ],
        "sources": [src(5, "問3")],
        "tags": ["非反転増幅", "計算"],
    }
)

# --- 11/5 ---
UNIT_1105 = "差動増幅（11/5 講義分）"

add(
    {
        "id": "EC2-1105-Q1",
        "unit": UNIT_1105,
        "form": "essay",
        "stem": pv(
            "Summarize the following text in Japanese.（差動増幅の導出。"
            r"特別な場合 $R_1=R_3$, $R_2=R_4$ のとき $v_o=(R_2/R_1)(v_2-v_1)$。"
            "印刷式(5)の第2項添字は採点で 2→1 に訂正。）"
        ),
        "answer": hand(
            "理解しなさい。演算増幅回路は以下の図に示されている。気をつけろ。"
            "ゼロ電流が演算増幅端子に入力されている。"
            "節点aとbにキルヒホッフの電流則を適用しろ。"
            "（以降の要約本文は用紙上に見当たらず、冒頭の命令文調の訳のみ。）",
            extra="要約が冒頭のみで未完了の可能性。残部は unverified 扱いを別IDで記録。",
        ),
        "explanation": pv(
            "印刷式(5)はもともと $(v_2-v_2)$ で、赤ペンにより第2項添字を 1 へ訂正（採点）。"
            "手書き要約は冒頭数行のみ確認。",
            "original",
        ),
        "figures": [
            fig(
                "pipeline/images/figures/fig_1105_q1_differential.png",
                6,
                "差動増幅回路",
            )
        ],
        "sources": [src(6, "問1 要約")],
        "tags": ["差動増幅", "要約", "英語"],
        "corrections": [
            corr(
                "transcript:eq5",
                "{{手書き: 添字1}}",
                "{{採点: 添字1}}",
                "赤ペン訂正を再分類",
            )
        ],
    }
)
add(
    {
        "id": "EC2-1105-Q1-REST",
        "unit": UNIT_1105,
        "form": "essay",
        "stem": pv("差動増幅英文要約の続き（式(1)〜(5)の日本語化の残部）。"),
        "answer": pv(
            "（未記入または判読不能。冒頭以外の要約なし）",
            "unverified",
        ),
        "sources": [src(6, "問1 要約残部")],
        "tags": ["差動増幅", "要約", "未記入"],
    }
)
add(
    {
        "id": "EC2-1105-Q2",
        "unit": UNIT_1105,
        "form": "calculation",
        "stem": pv(
            r"Find $v_o$ given that $v_1=1\,\mathrm{V}$ and $v_2=2\,\mathrm{V}$。"
            r"（回路: 反転側 $2\,\mathrm{k}/30\,\mathrm{k}$、非反転側 $2\,\mathrm{k}/20\,\mathrm{k}$。"
            "抵抗比が不一致のため単純な $(R_2/R_1)(v_2-v_1)$ は使えない。）"
        ),
        "answer": pv("（未記入）", "unverified"),
        "figures": [
            fig(
                "pipeline/images/figures/fig_1105_q2_differential.png",
                6,
                "差動増幅数値回路（問2）",
            )
        ],
        "sources": [src(6, "問2（未記入）")],
        "tags": ["差動増幅", "計算", "未記入"],
    }
)


CORRECTED_TRANSCRIPT = '''<!--
訂正済み文字起こし（2026-11-11）
- 起点: Gemini 4 Argon 一時チャット文字起こし（マスク済みページ画像のみ）
- 照合: assignment_opamp_2026-11_masked.pdf から生成したページ PNG
- 方針: {{手書き}}=学生解答、{{採点}}=採点・訂正。氏名欄マスクは維持。確認印は日付のみ。
-->

## p.1（10/2 講義分）

電子回路Ⅱ 3 （10 / 2 講義分）※日付は手書き記入、氏名欄はマスク

1. オペアンプの特徴として正しいものには○，誤っているものには×を答えよ．
(1) 電圧利得が大きい．{{手書き: ○}} {{採点: ○}}
(2) 入力インピーダンスが小さい．{{手書き: ×}} {{採点: ○}}
(3) 差動増幅する．{{手書き: ○}} {{採点: ○}}
(4) 出力インピーダンスが小さい．{{手書き: ○}} {{採点: ○}}

2. 正弦波電圧の実効値 $V_{rms}=10\\mathrm{V}$ のとき，(1) $V_{pp}$，(2) $V_{op}$ を求めよ．
(1) {{手書き: $20\\sqrt{2}\\mathrm{V}$}} {{採点: $=28.28\\mathrm{V}$}}
(2) {{手書き: $10\\sqrt{2}\\mathrm{V}$}} {{採点: $=14.14\\mathrm{V}$}}

3. $2\\mathrm{mV}$ 入力 → $9\\mathrm{mV}$ 出力のゲイン [dB]
{{手書き: $13.1\\mathrm{dB}$}} {{採点: ○}}

4. $19\\mathrm{V}$ 入力 → $2\\mathrm{V}$ 出力のゲイン [dB]
{{手書き: $-19.6\\mathrm{dB}$}} {{採点: ○}}

5. ゲイン $30\\mathrm{dB}$，$1\\mathrm{mV}$ 入力の出力 [mV]
{{手書き: $31.6\\mathrm{mV}$}} {{採点: ○}}

6. 図の波形（a 実線振幅2mV / b 破線振幅5mV）
(1) {{手書き: $V_{op}=2\\mathrm{mV}$}} {{採点: ○}} {{手書き: $V_{rms}=2/\\sqrt{2}\\mathrm{mV}$}} {{採点: $\\fallingdotseq 1.41\\mathrm{mV}$}}
(2) {{手書き: $318\\mathrm{Hz}$}} {{採点: ○}} ※検算: T=2π ms なら≈159 Hz。周期解釈要確認
(3) {{手書き: $G=20\\log(5/2)\\fallingdotseq 7.96\\mathrm{dB}$}} {{採点: ○}}
(4) {{手書き: $+\\pi/6\\mathrm{rad}$}} {{採点: ○}} ※黒インク解答＋赤丸（赤ペン新規ではない）

---

## p.2（10/2 講義分・続き）

7. オペアンプ TL084CN と LM741 のピン配置を調査せよ．

TL084CN（14ピン）: 1OUT,1IN-,1IN+,VCC+,2IN+,2IN-,2OUT / 3OUT,3IN-,3IN+,VCC-,4IN+,4IN-,4OUT
{{採点: ○}}

LM741（8ピン）: OFFSET NULL, INVERTING INPUT, NON-INVERTING INPUT, V- / NC, V+, OUTPUT, OFFSET NULL
{{採点: ○}}
{{採点: 確認印（26.10.-9・日付のみ）}}

---

## p.3（10/16 講義分）

1. $v_o$（$A_O=\\infty$）: {{手書き: $v_o=-18.75\\mathrm{V}$, $A_v=-12.5$}}
2. $v_i$（$v_o=2\\mathrm{V}$）: {{手書き: $v_i=-40\\mathrm{mV}$, $A_v=-50$}}（$R_2=1\\mathrm{M}\\Omega$）

---

## p.4（10/16 続き）

3. 反転増幅英文の日本語要約（手書き全文は structured 参照）
{{採点: 確認印（26.10.23・日付のみ）}}

---

## p.5（10/23 講義分）

1. 非反転増幅英文の日本語要約（手書き全文は structured 参照）
2. {{手書き: $v_o=12\\mathrm{V}$}}
3. {{手書き: $A_v=21$}}
{{採点: 確認印（26.10.23・日付のみ）}}

---

## p.6（11/5 講義分）

1. 差動増幅英文。式(5)印刷は $(v_2-v_2)$ → {{採点: 添字を1へ訂正}}（旧Geminiは手書き扱い）
   手書き要約は冒頭のみ: 「理解しなさい。…節点aとbにキルヒホッフの電流則を適用しろ。」
2. Find $v_o$（$v_1=1\\mathrm{V}$, $v_2=2\\mathrm{V}$, 2k/30k/2k/20k）: {{未記入}} → unverified
'''


def write_questions_raw():
    out = PIPELINE / "questions_raw"
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    for q in QUESTIONS:
        (out / f"{q['id']}.json").write_text(
            json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )


def main() -> None:
    structured = ROOT / "structured"
    structured.mkdir(parents=True, exist_ok=True)

    data = {
        "schema_version": "1.0.0",
        "exam": EXAM,
        "subject": SUBJECT,
        "generated_at": NOW,
        "notes": (
            "採点済み課題（マスク版6頁: 10/2・10/16・10/23・11/5 講義分）。"
            "手書き解答は inferred（ページ画像照合）。採点・赤ペン訂正は explanation/corrections に分離。"
            "未記入は unverified。穴埋め本番は未実施（filled=false）。"
            "公式範囲表は未入手。氏名・学籍番号は含めない。"
        ),
        "questions": QUESTIONS,
    }

    qpath = structured / "questions.json"
    qpath.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    (PIPELINE / "corrections_log.json").write_text(
        json.dumps(
            {
                "source": "gemini-transcript vs masked page images",
                "updated": NOW,
                "corrections": CORRECTIONS,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    tdir = PIPELINE / "transcripts"
    tdir.mkdir(parents=True, exist_ok=True)
    raw_gemini = Path(
        "/home/ubuntu/.cursor/projects/agent-repos-Teiki-Test/uploads/gemini-transcript_7d16.md"
    ).read_text(encoding="utf-8")
    # 確認印の印字氏名はリポジトリに残さない（日付のみ）
    scrubbed = re.sub(
        r"(確認印（(?:\d{2}\.\d{2}\.-?\d{1,2}))\s+[^\s）]+）",
        r"\1）",
        raw_gemini,
    )
    (tdir / "gemini_transcript_source.md").write_text(scrubbed, encoding="utf-8")
    (tdir / "assignment_opamp_2026-11_masked_corrected.md").write_text(
        CORRECTED_TRANSCRIPT, encoding="utf-8"
    )
    (tdir / "gemini_source_meta.md").write_text(
        "\n".join(
            [
                "# Gemini 文字起こしメタ",
                "",
                "- 日時: 2026-11-11 09:36〜09:38 JST",
                "- モデル: Gemini 4 Argon",
                "- 入力: マスク済みページ画像のみ",
                "- 草稿をページ画像と照合し `assignment_opamp_2026-11_masked_corrected.md` に反映",
                "",
            ]
        ),
        encoding="utf-8",
    )

    write_questions_raw()

    unverified = [
        q["id"]
        for q in QUESTIONS
        if (q.get("answer") or {}).get("status") == "unverified"
    ]
    n_corr = sum(len(q.get("corrections") or []) for q in QUESTIONS)
    n_inferred = sum(
        1 for q in QUESTIONS if (q.get("answer") or {}).get("status") == "inferred"
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
            "corrections": n_corr,
            "unverified": len(unverified),
            "inferred_answers": n_inferred,
        },
        "unverified_ids": unverified,
        "notes": (
            "進捗: 整備中。マスク済み課題PDFのみRAW。"
            "空欄穴埋めは未実施（filled=false）。公式範囲表は未入手。"
        ),
    }
    (ROOT / "status.json").write_text(
        json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    note = f"""# 電子回路Ⅱ（2026/03）確認ノート

出典: `{SOURCE}`（採点済み課題・氏名マスク版、6ページ）

## 単元

1. **10/2 講義分** — オペアンプの特徴、実効値、$\\mathrm{{dB}}$ ゲイン、波形、ピン配置（TL084CN / LM741）
2. **10/16 講義分** — 反転増幅の計算と英文要約
3. **10/23 講義分** — 非反転増幅の英文要約と計算
4. **11/5 講義分** — 差動増幅の英文要約と計算（問2は未記入）

## データ

- 構造化: `structured/questions.json`
- 文字起こし（訂正済）: `pipeline/transcripts/assignment_opamp_2026-11_masked_corrected.md`
- 訂正ログ: `pipeline/corrections_log.json`
- アプリ用: `app_data/`
- Question Bank: `ec2_2026_03`

## 注意

- 手書き解答は `inferred`（マスク済みページ画像照合）。採点・赤ペンは explanation / corrections に分離。
- 未記入は `unverified`（差動増幅要約の残部・問2）。
- 氏名欄マスクは維持。確認印は採点側（日付のみ記録）。
- 公式試験範囲は未入手。範囲表には写していない。
"""
    (ROOT / "確認ノート.md").write_text(note, encoding="utf-8")

    print(
        json.dumps(
            {
                "questions": len(QUESTIONS),
                "corrections": n_corr,
                "unverified": unverified,
                "inferred": n_inferred,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
