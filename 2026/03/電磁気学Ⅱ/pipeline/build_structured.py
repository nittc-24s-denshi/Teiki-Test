#!/usr/bin/env python3
"""Build corrected transcripts, questions_raw, structured/questions.json for EM2 print."""

from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # 電磁気学Ⅱ
PIPELINE = Path(__file__).resolve().parent
SOURCE = "RAW/print_dielectric_2026-11.pdf"
SID = "print_dielectric_2026-11"
EXAM = "2026/03"
SUBJECT = "電磁気学Ⅱ"

NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def pv(value, status="original", rationale=None, tools=None):
    obj = {"value": value, "status": status}
    if rationale is not None:
        obj["rationale"] = rationale
    if tools is not None:
        obj["tools"] = tools
    return obj


def corr(field, before, after, reason):
    return {"field": field, "before": before, "after": after, "reason": reason}


# ---------------------------------------------------------------------------
# Blank inventory (after image verification)
# ---------------------------------------------------------------------------
# Each blank: id, chapter-local number, page, unit, stem, answer, form, figures,
# corrections[], answer_status, rationale, tools, tags, notes

BLANKS: list[dict] = []


def add_blank(**kwargs):
    BLANKS.append(kwargs)


# --- Ch.4 Dielectrics ---
add_blank(
    local="①", page=1, unit="4. 誘電体 / 4.1 誘電体と比誘電率",
    stem="比誘電率 ε_r を、真空時の静電容量 C_0 と誘電体充填時の静電容量 C で表せ。",
    answer=r"$\varepsilon_r = \dfrac{C}{C_0}$",
    form="cloze", tags=["比誘電率", "穴埋め"],
)
add_blank(
    local="②", page=1, unit="4. 誘電体 / 4.1 誘電体と比誘電率",
    stem="平行平板コンデンサ（極板面積 S、間隔 d）の真空時静電容量 C_0 を表せ。",
    answer=r"$C_0 = \varepsilon_0 \dfrac{S}{d}$",
    form="cloze", tags=["静電容量", "穴埋め"],
)
add_blank(
    local="③", page=1, unit="4. 誘電体 / 4.1 誘電体と比誘電率",
    stem="極板間を誘電率 ε の誘電体で満たしたときの静電容量 C を表せ。",
    answer=r"$C = \varepsilon \dfrac{S}{d}$",
    form="cloze", tags=["静電容量", "穴埋め"],
)
add_blank(
    local="④", page=1, unit="4. 誘電体 / 4.1 誘電体と比誘電率",
    stem="誘電率 ε と比誘電率 ε_r、真空の誘電率 ε_0 の関係を書け。",
    answer=r"$\varepsilon = \varepsilon_r \varepsilon_0$",
    form="cloze", tags=["比誘電率", "穴埋め"],
)
add_blank(
    local="⑤", page=2, unit="4. 誘電体 / 4.2 誘電体の分極",
    stem="電界により原子が2つの極を持つようになった状態は、何を形成した状態か。",
    answer="電気双極子",
    form="cloze", tags=["分極", "穴埋め"],
    figures=[{"path": "pipeline/images/figures/fig4_1_electron_polarization.png", "page": 2,
              "caption": pv("図4.1a 電子分極", "original")}],
)
add_blank(
    local="⑥", page=2, unit="4. 誘電体 / 4.2 誘電体の分極",
    stem="原子が電界により双極子を形成することを何と呼ぶか。",
    answer="電子分極",
    form="cloze", tags=["分極", "穴埋め"],
)
add_blank(
    local="⑦", page=2, unit="4. 誘電体 / 4.2 誘電体の分極",
    stem="「導電体は⑦を流し，誘電体は⑧を流さない」の⑦に入る語句。",
    answer="自由な電流",
    form="cloze", tags=["誘電体", "導電体", "穴埋め"],
    corrections=[corr(
        "answer.value",
        "電気 / 電流",
        "自由な電流",
        "ページ画像照合。Gemini文字起こしの⑦読み違い（電気/電流）を訂正。手書きは「自由な電流」。",
    )],
)
add_blank(
    local="⑧", page=2, unit="4. 誘電体 / 4.2 誘電体の分極",
    stem="「導電体は⑦を流し，誘電体は⑧を流さない」の⑧に入る語句。",
    answer="ほとんど電流",
    form="cloze", tags=["誘電体", "導電体", "穴埋め"],
    corrections=[corr(
        "answer.value",
        "電気 / 電流",
        "ほとんど電流",
        "ページ画像照合。Gemini文字起こしの⑧読み違いを訂正。手書きは「ほとんど電流」。",
    )],
)
add_blank(
    local="⑨", page=2, unit="4. 誘電体 / 4.2 誘電体の分極",
    stem="「導電体は⑨を蓄えることができないが，誘電体は…⑨を蓄えることができる」の⑨。",
    answer="電荷",
    form="cloze", tags=["誘電体", "穴埋め"],
)
add_blank(
    local="⑩", page=3, unit="4. 誘電体 / 4.2.2 誘電体中の電界",
    stem="誘電体表面に ±σ_p が生じるとき、誘電体内の電界 E_p を σ, σ_p, ε_0 で表せ。",
    answer=r"$E_p = \dfrac{\sigma - \sigma_p}{\varepsilon_0}$",
    form="cloze", tags=["電界", "分極電荷", "穴埋め"],
    figures=[{"path": "pipeline/images/figures/fig4_2_apparent_charge.png", "page": 3,
              "caption": pv("図4.2 平行平板導体間の電界（見かけ電荷）", "original")}],
)
add_blank(
    local="⑪", page=3, unit="4. 誘電体 / 4.2.2 誘電体中の電界",
    stem="見かけの電荷密度を σ, σ_p で表せ。",
    answer=r"$\pm(\sigma - \sigma_p)$",
    form="cloze", tags=["見かけの電荷", "穴埋め"],
)
add_blank(
    local="⑫", page=3, unit="4. 誘電体 / 4.2.2 誘電体中の電界",
    stem="分極 P を分極率 χ（または比分極率 χ_r）と E_p で表せ（式4.6）。",
    answer=r"$P = \chi E_p = \varepsilon_0 \chi_r E_p$",
    form="cloze", tags=["分極", "穴埋め"],
)
add_blank(
    local="⑬", page=3, unit="4. 誘電体 / 4.2.2 誘電体中の電界",
    stem="電束密度 D を ε_0, E_p, P で表せ（式4.7）。",
    answer=r"$\mathbf{D} = \varepsilon_0 E_p + P$",
    form="cloze", tags=["電束密度", "穴埋め"],
)
add_blank(
    local="⑭", page=4, unit="4. 誘電体 / 電束とガウスの法則",
    stem="電荷 Q を覆う半径 r の球面の電束密度 D を表せ。",
    answer=r"$D = \dfrac{Q}{4\pi r^2}$",
    form="cloze", tags=["電束密度", "穴埋め"],
)
add_blank(
    local="⑮", page=4, unit="4. 誘電体 / 電束とガウスの法則",
    stem="電束に関するガウスの法則の一般形（単位 [C]）を書け。",
    answer="【未確認】空欄のまま（想定: $\\oint \\mathbf{D}\\cdot d\\mathbf{S} = Q$）",
    answer_status="unverified",
    form="cloze", tags=["ガウスの法則", "穴埋め", "未記入"],
    corrections=[corr(
        "answer.status",
        "（Geminiは空欄として未記載、一部読み取りで誤補完の疑い）",
        "unverified",
        "ページ画像照合の結果、⑮は未記入。穴埋め補完は別途外部AI運用のためここでは埋めない。",
    )],
)
add_blank(
    local="⑯", page=4, unit="4. 誘電体 / 電束とガウスの法則",
    stem="電束密度 D と電界 E の関係を書け。",
    answer=r"$D = \varepsilon E$",
    form="cloze", tags=["電束密度", "穴埋め"],
    explanation=pv(
        "手書き解答 $D=\\varepsilon E$ は関係式として正しい。印刷の単位 [V/m] は E の単位であり、"
        "D の単位 [C/m²] と不一致。プリント側の単位表記の誤りの可能性が高い。",
        "inferred",
        "単位の次元照合（D: C/m², E: V/m）",
        ["manual-dimensional-check"],
    ),
)
add_blank(
    local="⑰", page=4, unit="4. 誘電体 / 電束とガウスの法則",
    stem="電束数 Q=φ [C] について、周囲との関係を述べよ。",
    answer="周囲の影響は受けない",
    form="cloze", tags=["電束", "穴埋め"],
    corrections=[corr(
        "answer.value",
        "周囲の影響は受けない（Gemini）／周囲の物質は無関係（別読み）",
        "周囲の影響は受けない",
        "強調コントラスト画像で再読。手書きは「周囲の影響は受けない」と判定。",
    )],
)
add_blank(
    local="⑱", page=4, unit="4. 誘電体 / 電束とガウスの法則",
    stem="電気力線数 N=Q/ε [本] について、周囲との関係を述べよ。",
    answer="【未確認】判読不能・ほぼ空白（想定: 周囲の物質の影響を受ける）",
    answer_status="unverified",
    form="cloze", tags=["電気力線", "穴埋め", "判読不能"],
    corrections=[corr(
        "answer.value",
        "）",
        "【未確認】判読不能・ほぼ空白",
        "Gemini既知疑いどおり。強調画像でも明確な文字を確認できず unverified。",
    )],
)
add_blank(
    local="⑲", page=5, unit="4. 誘電体 / 4.3 誘電体のガウスの法則",
    stem="見かけの電荷を用いた微小面積 ΔS の電気力線の本数 N（式4.8）。",
    answer=r"$N = \dfrac{\Delta S(\sigma-\sigma_p)}{\varepsilon_0} = E_p\,\Delta S$",
    form="cloze", tags=["ガウスの法則", "穴埋め"],
    figures=[{"path": "pipeline/images/figures/fig4_3_field_flux.png", "page": 5,
              "caption": pv("図4.3 平行平板間の電界（見かけ電荷）", "original")}],
)
add_blank(
    local="⑳", page=5, unit="4. 誘電体 / 4.3 誘電体のガウスの法則",
    stem="平行平板全体の電気力線の数（式4.9）を書け。",
    answer=r"$\oint_S E_p\,\Delta S = \dfrac{Q-Q_p}{\varepsilon_0}$",
    form="cloze", tags=["ガウスの法則", "穴埋め"],
    explanation=pv(
        "プリント注記に $Q=\\Delta S\\sigma/\\varepsilon_0$ とあるが、真電荷は $Q=\\sigma\\Delta S$ が次元的に正しい。"
        "注記は印刷側の誤記候補（解答⑳の手書き本体は式4.9の形として採用）。",
        "inferred",
        "電荷密度σ[C/m²]×面積→電荷[C]。ε0で割ると次元が合わない。",
        ["manual-dimensional-check"],
    ),
)
add_blank(
    local="㉑", page=5, unit="4. 誘電体 / 4.3 誘電体のガウスの法則",
    stem="電束と真電荷の関係（式4.10）を書け。",
    answer=r"$\Delta S\,\sigma = \Delta S\,D$",
    form="cloze", tags=["電束", "穴埋め"],
)
add_blank(
    local="㉒", page=5, unit="4. 誘電体 / 4.3 誘電体のガウスの法則",
    stem="電束に関するガウスの法則（式4.11）を書け。",
    answer=r"$\oint_S D_n\cdot dS = Q$",
    form="cloze", tags=["ガウスの法則", "穴埋め"],
)
add_blank(
    local="㉓", page=6, unit="4. 誘電体 / 4.4 誘電体境界条件",
    stem="図4.5の電束密度の接線・法線成分の分解（θ は法線からの角）。",
    answer=r"$D_{1t}=D_1\sin\theta_1,\ D_{1n}=D_1\cos\theta_1,\ D_{2t}=D_2\sin\theta_2,\ D_{2n}=D_2\cos\theta_2$",
    form="cloze", tags=["境界条件", "穴埋め"],
    figures=[{"path": "pipeline/images/figures/fig4_5_boundary_components.png", "page": 6,
              "caption": pv("図4.5 異なる2つの誘電率を持つ境界面（㉓）", "original")}],
    corrections=[corr(
        "local_number",
        "欠落（Gemini既知誤り）",
        "㉓",
        "図4.5枠内左上の丸数字㉓と手書き成分分解を確認。transcriptから欠落していたため復元。",
    )],
    explanation=pv(
        "図4.4に生徒が μ₁, μ₂ と書き込んでいるが、文脈は誘電率 ε₁, ε₂。透磁率との取り違え候補。",
        "inferred",
        "図キャプション・本文は誘電率。μ は磁気の章の記号。",
        ["manual-physics-check"],
    ),
)
add_blank(
    local="㉔", page=6, unit="4. 誘電体 / 4.4 誘電体境界条件",
    stem="薄い円柱閉曲面に対する電束の収支（自由表面電荷なし）を書け。",
    answer=r"$\Delta S (D_{2n}-D_{1n})=0$",
    form="cloze", tags=["境界条件", "穴埋め"],
)
add_blank(
    local="㉕", page=6, unit="4. 誘電体 / 4.4 誘電体境界条件",
    stem="境界面における電束密度の法線成分についての結論を書け。",
    answer="境界面における電束密度の法線方向の成分は連続である",
    form="cloze", tags=["境界条件", "穴埋め"],
    corrections=[corr(
        "local_number",
        "㉥",
        "㉕",
        "Gemini既知誤り。画像上の丸数字は㉕。",
    )],
)
add_blank(
    local="㉖", page=7, unit="4. 誘電体 / 4.4 誘電体境界条件",
    stem="境界面近傍の閉曲線 abcd に対する電界の線積分（式4.13）。",
    answer=r"$\oint_{abcd}\mathbf{E}\cdot d\mathbf{l}=-E_{1t}|ab|+E_{2t}|cd|$",
    form="cloze", tags=["境界条件", "穴埋め"],
)
add_blank(
    local="㉗", page=7, unit="4. 誘電体 / 4.4 誘電体境界条件",
    stem="電束密度の法線連続から得られる角度関係（式4.14上段）。",
    answer=r"$D_1\cos\theta_1=D_2\cos\theta_2$",
    form="cloze", tags=["境界条件", "穴埋め"],
    corrections=[corr(
        "answer.value",
        r"$D_1\sin\theta_1=D_2\sin\theta_2$",
        r"$D_1\cos\theta_1=D_2\cos\theta_2$",
        "画像照合。法線成分は cos。sin は接線成分。Geminiがsinと誤記。",
    )],
)
add_blank(
    local="㉘", page=7, unit="4. 誘電体 / 4.4 誘電体境界条件",
    stem="電界の接線連続から得られる角度関係（式4.14下段）。",
    answer=r"$E_1\sin\theta_1=E_2\sin\theta_2$",
    form="cloze", tags=["境界条件", "穴埋め"],
)
add_blank(
    local="㉙", page=7, unit="4. 誘電体 / 4.4 誘電体境界条件",
    stem="tanθ₁/tanθ₂=ε₁/ε₂ を、電気力線と電束の何と呼ぶか。",
    answer="屈折の法則",
    form="cloze", tags=["屈折の法則", "穴埋め"],
)
add_blank(
    local="㉚", page=8, unit="4. 誘電体 / 4.5 エネルギーと力",
    stem="電束が管状になったものを何と呼ぶか（ファラデー管の直前の用語）。",
    answer="力管",
    form="cloze", tags=["ファラデー管", "穴埋め"],
    figures=[{"path": "pipeline/images/figures/fig4_6_faraday_tube.png", "page": 8,
              "caption": pv("図4.6 力管", "original")}],
    corrections=[corr(
        "local_number", "㉠", "㉚", "Gemini既知誤り（㉠〜㉣表記）。画像は㉚。",
    ), corr(
        "answer.value", "ファラデー管", "力管",
        "画像照合。手書きは「力管」。直後に「力管をファラデー管と呼ぶ」と続く。",
    )],
)
add_blank(
    local="㉛", page=8, unit="4. 誘電体 / 4.5 エネルギーと力",
    stem="ファラデー管（力管）の始点・終点の性質を述べよ。",
    answer="単位正の電荷から始まり、単位負の電荷に終わる",
    form="cloze", tags=["ファラデー管", "穴埋め"],
    corrections=[corr(
        "local_number", "㉡", "㉛", "Gemini既知誤り。画像は㉛。",
    ), corr(
        "answer.value",
        "正の電荷から発生し、負の電荷に終わる",
        "単位正の電荷から始まり、単位負の電荷に終わる",
        "画像照合。手書きに「単位」が付く。",
    )],
)
add_blank(
    local="㉜", page=8, unit="4. 誘電体 / 4.5.1 電界エネルギー",
    stem="エネルギー体積密度 w = (1/2)·(ΔV/Δl)·(1/ΔS) = (1/2)·□ （式4.19）。□を埋めよ。",
    answer=r"$ED$",
    form="cloze", tags=["エネルギー密度", "穴埋め"],
    corrections=[corr(
        "local_number", "㉢", "㉜", "Gemini既知誤り。画像は㉜。",
    ), corr(
        "answer.value", r"\frac{1}{2} E D", "ED",
        "印刷の 1/2 は箱の外。箱内手書きは ED。",
    )],
)
add_blank(
    local="㉝", page=8, unit="4. 誘電体 / 4.5.1 電界エネルギー",
    stem="w = (1/2)ED = (1/2)·□ （式4.20）。□を埋めよ。",
    answer=r"$\dfrac{D^2}{\varepsilon}$",
    form="cloze", tags=["エネルギー密度", "穴埋め"],
    corrections=[corr(
        "local_number", "㉣", "㉝", "Gemini既知誤り。画像は㉝。",
    ), corr(
        "answer.value", r"\frac{1}{2}\frac{D^2}{\varepsilon}", r"\dfrac{D^2}{\varepsilon}",
        "1/2 は箱の外。箱内は D²/ε。",
    )],
)
add_blank(
    local="㉞", page=10, unit="4. 誘電体 / 4.5.2 電極に働く力",
    stem="真空の平行平板で電極の単位面積に働く応力 F_0（式4.21）。",
    answer=r"$\dfrac{1}{2}DE$",
    form="cloze", tags=["応力", "穴埋め"],
    corrections=[corr(
        "local_number", "㉤", "㉞", "Gemini既知誤り。連番上㉞（画像の丸数字も34系）。",
    )],
)

# Example / problems chapter 4
add_blank(
    local="例題4.1", page=9, unit="4. 誘電体 / 4.5.1 電界エネルギー",
    stem="同軸二重円筒（内半径 a, 外半径 b, 誘電率 ε, 線電荷密度 ±λ）の単位長さあたり静電エネルギーを求めよ。",
    answer=r"$W=\dfrac{\lambda^2}{4\pi\varepsilon}\ln\dfrac{b}{a}\ [\mathrm{J/m}]$",
    form="calculation", tags=["例題", "同軸円筒", "エネルギー"],
    figures=[{"path": "pipeline/images/figures/fig_ex4_1_coaxial.png", "page": 9,
              "caption": pv("例題4.1 同軸二重円筒", "original")}],
    explanation=pv(
        "ガウスの法則より D=λ/(2πr)。w=D²/(2ε) を体積要素 2πr dr で a→b 積分。"
        "プリント解答中の w_e の単位表記 [C/m²] は誤記で、正しくは [J/m³]。",
        "inferred",
        "エネルギー密度の次元は J/m³ = N/m²。C/m² は電束密度の次元。",
        ["manual-dimensional-check"],
    ),
)
add_blank(
    local="問題4.2", page=10, unit="4. 誘電体 / 4.5.2 電極に働く力",
    stem="(a)真空 (b)真空+誘電体(各 d/2) (c)誘電体 の3条件で、同面積・同間隔・同電圧の＋電極単位面積あたりの力を求めよ。",
    answer="【未確認】完全解答なし。手書き部分: $F=\\frac{1}{2}\\varepsilon_0\\left(\\frac{2V_1}{d}\\right)^2$（(b)真空層側の途中式と推定）",
    answer_status="unverified",
    form="calculation", tags=["問題", "応力", "未完成"],
    figures=[{"path": "pipeline/images/figures/fig_prob4_2_capacitors.png", "page": 10,
              "caption": pv("問題4.2 3種の平行平板", "original")}],
    corrections=[corr(
        "answer.value",
        r"F=\frac{1}{2}\varepsilon_0(2V/d)^2",
        r"F=\frac{1}{2}\varepsilon_0(2V_1/d)^2（部分・Vに添字1）",
        "画像では V に添字1が見える。全体解答は未記入のため unverified。",
    )],
    explanation=pv(
        "完全解の候補（inferred・穴埋め別途）: "
        "(a) $F=\\frac{1}{2}\\varepsilon_0(V/d)^2$; "
        "(c) $F=\\frac{1}{2}\\varepsilon(V/d)^2$; "
        "(b) 直列で D 一定、真空層の E_0=σ/ε_0、力は電極側真空なら $\\sigma^2/(2\\varepsilon_0)$。"
        "生徒の (2V₁/d) は真空層厚さ d/2 のときの E=2V₁/d として形は妥当だが、"
        "V₁ と全電圧 V の関係・(a)(c) が未記載のため正解確定はしない。",
        "inferred",
        "応力公式 F=½DE と直列誘電体の境界条件から整理",
        ["manual-physics-check"],
    ),
    conflicts=[{
        "field": "answer",
        "values": [
            {"value": r"$F=\frac{1}{2}\varepsilon_0(2V_1/d)^2$（手書き部分）",
             "source": "RAW/print_dielectric_2026-11.pdf:p10", "status": "original"},
            {"value": "(a)(b)(c)の完全な力の式は資料上未記入",
             "source": "page-image-review", "status": "unverified"},
        ],
        "reason": "問題4.2の解答が部分記入のみ",
    }],
)

# --- Ch.5 Current (numbers restart) ---
add_blank(
    local="5-①", page=11, unit="5. 電流 / 5.1 電流と電流密度",
    stem="「ここでは，定常的に流れる①について検討する」の①。",
    answer="【未確認】空欄（想定: 電流 / 定常電流）",
    answer_status="unverified",
    form="cloze", tags=["電流", "未記入"],
)
add_blank(
    local="5-②", page=11, unit="5. 電流 / 5.1 電流と電流密度",
    stem="電流の定義 I（式5.1）。",
    answer=r"$I=\dfrac{dQ}{dt}$",
    form="cloze", tags=["電流", "穴埋め"],
    figures=[{"path": "pipeline/images/figures/fig5_1_current.png", "page": 11,
              "caption": pv("図5.1 電流", "original")}],
)
add_blank(
    local="5-③", page=11, unit="5. 電流 / 5.1 電流と電流密度",
    stem="電流密度 J の定義（式5.2）。",
    answer=r"$J=\dfrac{dI}{dS}$",
    form="cloze", tags=["電流密度", "穴埋め"],
)
add_blank(
    local="5-④", page=11, unit="5. 電流 / 5.1 電流と電流密度",
    stem="電流を電流密度の面積分で表せ（式5.3）。",
    answer=r"$I=\oint_S J\,dS$",
    form="cloze", tags=["電流密度", "穴埋め"],
)
add_blank(
    local="5-⑤", page=11, unit="5. 電流 / 5.1 電流と電流密度",
    stem="電荷密度 n・電荷 q・平均速度 v のときの電流密度（式5.4）。",
    answer=r"$J=nqv$",
    form="cloze", tags=["電流密度", "穴埋め"],
)
add_blank(
    local="例題5.1", page=12, unit="5. 電流 / 5.1 電流と電流密度",
    stem="導線に 2 A が流れている。1 C の移動に要する時間を求めよ。",
    answer=r"$t=Q/I=1/2=0.5\,\mathrm{s}$",
    form="calculation", tags=["例題", "電流"],
)
add_blank(
    local="5-⑥", page=12, unit="5. 電流 / 5.2 定常電流界",
    stem="定常電流の電荷保存則（式5.6）。",
    answer=r"$\oint_S\mathbf{J}\cdot d\mathbf{S}=\oint J_n\,dS=0$",
    form="cloze", tags=["電荷保存則", "穴埋め"],
    figures=[{"path": "pipeline/images/figures/fig5_2_current_continuity.png", "page": 12,
              "caption": pv("図5.2 電流の連続", "original")}],
)
add_blank(
    local="5-⑦", page=12, unit="5. 電流 / 5.2 定常電流界",
    stem="オームの法則 J=σE を用いた式（式5.7）。",
    answer=r"$\oint_S J_n\,dS=\sigma\oint_S E_n\,dS=0$",
    form="cloze", tags=["定常電流界", "穴埋め"],
)
add_blank(
    local="5-⑧", page=13, unit="5. 電流 / 境界条件",
    stem="境界面の電流連続（式5.9）。",
    answer=r"$\oint_S J_n\,dS=-J_{1n}\Delta S+J_{2n}\Delta S=0$",
    form="cloze", tags=["境界条件", "穴埋め"],
    figures=[{"path": "pipeline/images/figures/fig5_4_conductor_boundary.png", "page": 13,
              "caption": pv("図5.4 導体境界面の電流密度条件", "original")}],
)
add_blank(
    local="5-⑨", page=13, unit="5. 電流 / 境界条件",
    stem="境界面における電流密度の法線連続（式5.10）。",
    answer=r"$J_{1n}=J_{2n}$",
    form="cloze", tags=["境界条件", "穴埋め"],
)
add_blank(
    local="5-⑩", page=13, unit="5. 電流 / 境界条件",
    stem="定常電流界の接線成分に関する角度関係（式5.11）。",
    answer=r"$E_1\sin\theta_1=E_2\sin\theta_2$",
    form="cloze", tags=["境界条件", "穴埋め"],
)
add_blank(
    local="5-⑪", page=13, unit="5. 電流 / 境界条件",
    stem="電流密度法線を定常電流界で書いた式（式5.12）。",
    answer=r"$\sigma_1 E_1\cos\theta_1=\sigma_2 E_2\cos\theta_2$",
    form="cloze", tags=["境界条件", "穴埋め"],
)
add_blank(
    local="5-⑫", page=13, unit="5. 電流 / 境界条件",
    stem="定常電流界の接線成分の連続を式で書け（式5.13）。",
    answer="【未確認】空欄（想定: $E_{1t}=E_{2t}$ または $J_{1t}/\\sigma_1=J_{2t}/\\sigma_2$）",
    answer_status="unverified",
    form="cloze", tags=["境界条件", "未記入"],
)
add_blank(
    local="例題5.2", page=14, unit="5. 電流 / 漏れ電流",
    stem="平行板（S, d, 起電力 V, 媒質 ε, σ）の漏れ電流・漏れコンダクタンス G、および C と G の関係。",
    answer=r"$I=\sigma(V/d)S,\quad G=\sigma S/d,\quad C/G=\varepsilon/\sigma$",
    form="calculation", tags=["例題", "漏れコンダクタンス"],
    figures=[{"path": "pipeline/images/figures/fig_ex5_2_leaky_capacitor.png", "page": 14,
              "caption": pv("例題5.2 漏れのあるコンデンサ", "original")}],
    explanation=pv(
        "問題文は起電力を E[V] と書いているが解答は V を使用。記号の揺れに注意（原文維持）。",
        "inferred",
        "同一ページ内で E と V が混在",
        ["manual"],
    ),
)

# --- Ch.6 Magnetostatics ---
add_blank(
    local="6-①", page=15, unit="6. 真空中の静磁界 / 6.2 磁力線の特性",
    stem="磁力線の特性(3): 単位面積あたりの磁力線と磁界の関係。",
    answer="単位面積あたりの磁力線の数，すなわち磁力線密度，と磁界の強さは等しい",
    form="cloze", tags=["磁力線", "穴埋め"],
    figures=[{"path": "pipeline/images/figures/fig6_2_field_lines.png", "page": 15,
              "caption": pv("図6.2 磁力線", "original")}],
)
add_blank(
    local="6-②", page=15, unit="6. 真空中の静磁界 / 6.2 磁力線の特性",
    stem="磁力線の特性(4): 本数 N と磁荷 m・透磁率の関係（文章）。",
    answer="磁力線の本数 N は磁荷の強さ m を周囲の透磁率 μ₀ で割った値",
    form="cloze", tags=["磁力線", "穴埋め"],
)
add_blank(
    local="6-③", page=15, unit="6. 真空中の静磁界 / 6.2 磁力線の特性",
    stem="N と m, μ₀ の式。",
    answer=r"$N=\dfrac{m}{\mu_0}$",
    form="cloze", tags=["磁力線", "穴埋め"],
)
add_blank(
    local="6-④", page=16, unit="6. 真空中の静磁界 / 6.3 磁気の性質と強さ",
    stem="磁気に関するクーロンの法則（大きさ、式6.1）。",
    answer=r"$F=\dfrac{1}{4\pi\mu_0}\dfrac{m_1 m_2}{r^2}$",
    form="cloze", tags=["クーロンの法則", "穴埋め"],
)
add_blank(
    local="6-⑤", page=16, unit="6. 真空中の静磁界 / 6.3 磁気の性質と強さ",
    stem="F₁ を m₂ と磁界で表す途中式。",
    answer=r"$F_1=m_2\dfrac{1}{4\pi\mu_0}\dfrac{m_1}{r^2}$",
    form="cloze", tags=["磁界", "穴埋め"],
    figures=[{"path": "pipeline/images/figures/fig6_3_coulomb.png", "page": 17,
              "caption": pv("図6.3 磁気に関するクーロンの法則", "original")}],
)
add_blank(
    local="6-⑥", page=16, unit="6. 真空中の静磁界 / 6.3 磁気の性質と強さ",
    stem="磁荷 m₁ が距離 r に作る磁界 H（式6.3）。",
    answer=r"$H=\dfrac{1}{4\pi\mu_0}\dfrac{m_1}{r^2}$",
    form="cloze", tags=["磁界", "穴埋め"],
)
add_blank(
    local="6-⑦", page=17, unit="6. 真空中の静磁界 / 6.4 磁束の特性",
    stem="図6.4 磁石周辺の磁束（枠内⑦）。",
    answer="【未確認】図枠が空白（図の描画・説明未記入）",
    answer_status="unverified",
    form="other", tags=["磁束", "未記入"],
    figures=[{"path": "pipeline/images/figures/fig6_4_flux_blank.png", "page": 17,
              "caption": pv("図6.4 磁石周辺の磁束（空白）", "original")}],
)
add_blank(
    local="6-⑧", page=18, unit="6. 真空中の静磁界 / 6.5 磁束密度と磁界",
    stem="磁束密度 B の式（式6.8）。",
    answer=r"$B=\dfrac{\Phi}{S}=\mu_0\dfrac{N}{S}=\mu_0 H$",
    form="cloze", tags=["磁束密度", "穴埋め"],
)
add_blank(
    local="6-⑨", page=18, unit="6. 真空中の静磁界 / 6.5 磁束密度と磁界",
    stem="微小領域の磁束収支（式6.9）。",
    answer=r"$\Delta\phi_2-\Delta\phi_1=0$",
    form="cloze", tags=["磁束保存", "穴埋め"],
)
add_blank(
    local="6-⑩", page=18, unit="6. 真空中の静磁界 / 6.5 磁束密度と磁界",
    stem="磁束密度に関するガウスの法則（式6.10）。",
    answer=r"$\oint_S\mathbf{B}\cdot d\mathbf{S}=0$（手書きで印字 B を Φ と訂正した痕跡あり）",
    form="cloze", tags=["ガウスの法則", "穴埋め"],
    figures=[{"path": "pipeline/images/figures/fig6_5_flux_gauss.png", "page": 18,
              "caption": pv("図6.5 磁石周辺の磁束", "original")}],
    corrections=[corr(
        "answer.value",
        "BS → ∮ B·dS = 0",
        "∮ B·dS = 0（印字BをΦと斜線訂正の痕跡）",
        "画像で印字記号への手書き訂正を確認。法則としては磁束の閉曲面積分=0。",
    )],
)
add_blank(
    local="問題6.1", page=19, unit="6. 真空中の静磁界 / 問題",
    stem="磁極 ±m、長さ l の2本の棒磁石を同種極を相対させて距離 d 離したときの力。また r≪L のとき。",
    answer="【未確認】解答欄未記入",
    answer_status="unverified",
    form="calculation", tags=["問題", "磁力", "未記入"],
    figures=[{"path": "pipeline/images/figures/fig_prob6_1_magnets.png", "page": 19,
              "caption": pv("問題6.1 相対する棒磁石", "original")}],
)


def make_question(idx: int, item: dict) -> dict:
    qid = f"EM2-D{idx:03d}"
    status = item.get("answer_status", "original")
    ans = pv(item["answer"], status)
    if status == "inferred":
        ans["rationale"] = item.get("rationale", "推定")
        ans["tools"] = item.get("tools", ["manual"])
    q = {
        "id": qid,
        "unit": item["unit"],
        "form": item["form"],
        "stem": pv(f"[{item['local']}] {item['stem']}", "original"),
        "answer": ans,
        "sources": [{"file": SOURCE, "page": item["page"], "note": f"穴埋め/設問 {item['local']}"}],
        "tags": item.get("tags") or [],
    }
    if item.get("explanation"):
        q["explanation"] = item["explanation"]
    if item.get("figures"):
        q["figures"] = item["figures"]
    if item.get("corrections"):
        q["corrections"] = item["corrections"]
    if item.get("conflicts"):
        q["conflicts"] = item["conflicts"]
    return q


def write_corrected_transcripts():
    """Split gemini raw into per-page MD with correction header notes."""
    raw = (PIPELINE / "transcripts" / "gemini_transcript_raw.md").read_text(encoding="utf-8")
    # Keep raw; also write index of corrections applied at transcript level
    out_dir = PIPELINE / "transcripts"
    notes = {
        2: ["⑦⑧の手書きを「自由な電流」「ほとんど電流」に訂正"],
        4: ["⑮は空欄→unverified", "⑱は判読不能→unverified", "⑰は「周囲の影響は受けない」で確定"],
        6: ["㉓を図4.5から復元", "㉥→㉕"],
        7: ["㉗を D₁cosθ₁=D₂cosθ₂ に訂正（sin誤記）"],
        8: ["㉠〜㉣→㉚〜㉝", "㉚=力管", "㉛に「単位」を復元", "㉜㉝は係数1/2を箱外と整理"],
        9: ["例題4.1の w_e 単位[C/m²]は誤記候補（正: J/m³）"],
        10: ["㉤→㉞", "問題4.2は部分解答のみ"],
        11: ["5章①は空欄"],
        13: ["5章⑫は空欄"],
        17: ["図6.4⑦は空白"],
        19: ["問題6.1未記入"],
    }
    # Write a single corrected overview
    lines = [
        "<!--",
        f"source: {SOURCE}",
        "tool: Gemini (raw) + page-image manual correction",
        f"generated_at: {NOW}",
        "confidence: mixed (handwriting verified on key pages)",
        "-->",
        "",
        "# 訂正済み文字起こしメモ",
        "",
        "原本のページ単位 Gemini 文字起こしは `gemini_transcript_raw.md`。",
        "以下は画像照合で確定した訂正。構造化データ側の `corrections` と対応。",
        "",
    ]
    for p, ns in sorted(notes.items()):
        lines.append(f"## p.{p}")
        for n in ns:
            lines.append(f"- {n}")
        lines.append("")
    (out_dir / "corrections_notes.md").write_text("\n".join(lines), encoding="utf-8")
    # Also copy per-page extracted text stubs pointing to page images
    for i in range(1, 20):
        path = out_dir / f"{SID}_p{i:03d}.md"
        if path.exists() and "tool: pymupdf" in path.read_text(encoding="utf-8")[:200]:
            # replace empty pymupdf extracts with pointer
            body = (
                f"<!-- source: print_dielectric_2026-11.pdf page: {i} "
                f"tool: gemini+manual-review -->\n\n"
                f"スキャンPDFのため pymupdf テキストなし。"
                f"結合文字起こし: `gemini_transcript_raw.md` の p.{i}。"
                f"訂正: `corrections_notes.md`。\n"
                f"ページ画像: `../images/pages/{SID}_p{i:03d}.png`\n"
            )
            path.write_text(body, encoding="utf-8")


def main():
    questions = [make_question(i + 1, b) for i, b in enumerate(BLANKS)]

    # questions_raw
    qraw = PIPELINE / "questions_raw"
    qraw.mkdir(parents=True, exist_ok=True)
    for q in questions:
        (qraw / f"{q['id']}.json").write_text(
            json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

    # corrections log (flat)
    clog = []
    for q in questions:
        for c in q.get("corrections") or []:
            clog.append({"id": q["id"], **c})
    (PIPELINE / "corrections_log.json").write_text(
        json.dumps({"generated_at": NOW, "count": len(clog), "items": clog},
                   ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    unverified = [q for q in questions if q["answer"]["status"] == "unverified"]
    inferred_ans = [q for q in questions if q["answer"]["status"] == "inferred"]

    structured = {
        "schema_version": "1.0.0",
        "exam": EXAM,
        "subject": SUBJECT,
        "generated_at": NOW,
        "notes": (
            "授業プリント「4.誘電体」〜「6.真空中の静磁界」スキャン19頁。"
            "手書き解答は画像照合済み。空欄・判読不能は unverified（穴埋めは別途外部AI）。"
            "公式範囲表は未入手のため確定範囲としては扱わない。"
        ),
        "questions": questions,
    }

    sdir = ROOT / "structured"
    sdir.mkdir(parents=True, exist_ok=True)
    (sdir / "questions.json").write_text(
        json.dumps(structured, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    # human markdown summary (do not overwrite 確認ノート.md)
    md_lines = [
        f"# {SUBJECT} — 構造化まとめ（プリント誘電体〜静磁界）",
        "",
        f"- 試験フォルダ: `{EXAM}`",
        f"- 出典: `{SOURCE}`（19ページ）",
        f"- 問題数: {len(questions)}",
        f"- corrections: {len(clog)}",
        f"- unverified: {len(unverified)}",
        f"- 生成: {NOW}",
        "",
        "## 単元一覧",
        "",
    ]
    units = {}
    for q in questions:
        units.setdefault(q["unit"], []).append(q)
    for u, qs in units.items():
        md_lines.append(f"### {u}")
        md_lines.append("")
        for q in qs:
            st = q["answer"]["status"]
            md_lines.append(f"- `{q['id']}` ({st}) {q['stem']['value']}")
            md_lines.append(f"  - 答: {q['answer']['value']}")
        md_lines.append("")
    md_lines += [
        "## unverified 一覧",
        "",
    ]
    for q in unverified:
        md_lines.append(f"- `{q['id']}` p.{q['sources'][0]['page']}: {q['stem']['value']} → {q['answer']['value']}")
    md_lines += [
        "",
        "## 主な corrections",
        "",
    ]
    for c in clog:
        md_lines.append(f"- `{c['id']}` {c['field']}: {c['before']} → {c['after']}（{c['reason']}）")
    (sdir / "まとめ_構造化.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    # status
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
        },
        "counts": {
            "questions": len(questions),
            "corrections": len(clog),
            "unverified": len(unverified),
            "inferred_answers": len(inferred_ans),
        },
        "notes": (
            "進捗: 整備中。空欄穴埋めは未実施（filled=false / unverified 残）。"
            "公式範囲表は未入手。Question Bank 用 app_data を生成予定。"
        ),
    }
    (ROOT / "status.json").write_text(
        json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    write_corrected_transcripts()
    print(f"OK: {len(questions)} questions, {len(clog)} corrections, {len(unverified)} unverified")


if __name__ == "__main__":
    main()
