#!/usr/bin/env python3
"""線形代数Ⅳ 手書きノート → questions_raw / structured / corrections / transcripts."""

from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = Path(__file__).resolve().parent
SOURCE = "RAW/note_linear_space_2026-11.pdf"
EXAM = "2026/03"
SUBJECT = "線形代数Ⅳ"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def pv(value, status="original", rationale=None, tools=None):
    obj = {"value": value, "status": status}
    if rationale is not None:
        obj["rationale"] = rationale
    if tools is not None:
        obj["tools"] = tools
    return obj


def fig(path, page, caption, status="original"):
    return {
        "path": path,
        "page": page,
        "caption": pv(caption, status),
    }


def src(page, note=None):
    d = {"file": SOURCE, "page": page}
    if note:
        d["note"] = note
    return d


QUESTIONS: list[dict] = []
CORRECTIONS_LOG: list[dict] = []


def add(q: dict):
    QUESTIONS.append(q)
    for c in q.get("corrections") or []:
        CORRECTIONS_LOG.append({"id": q["id"], **c})


def add_meta():
    add(
        {
            "id": "LA4-META-TRANSCRIPT-QC",
            "unit": "メタ（文字起こし照合）",
            "form": "other",
            "stem": pv("手書きノート文字起こしをページ画像と照合した記録。"),
            "answer": pv("訂正ログ参照（pipeline/corrections_log.json）。p.5左上の別紙切れ込み「【状」「【問」は本文外のため非取込。"),
            "sources": [src(1, "全5ページ照合")],
            "tags": ["meta", "corrections"],
            "corrections": [
                {
                    "field": "transcript:p5-edge",
                    "before": "（別紙切れ込み「【状」「【問」）",
                    "after": "（取込対象外・除外）",
                    "reason": "ページ画像照合。p.5左上の別紙断片は本ノート本文ではないため取り込みしない。",
                },
                {
                    "field": "transcript:p3-ex-domain",
                    "before": "W = [0, \\infty]（Gemini草稿どおり）",
                    "after": "W = [0, \\infty]（原文維持）",
                    "reason": "ページ画像でも閉じ区間記法に見える。数学的には f(v)=v^2 の像は [0,∞) が通常だが、原文を優先し解答側で注記。",
                },
            ],
        }
    )


# ---------- p.1 線型空間 / 線型部分空間 ----------
add_meta()

add(
    {
        "id": "LA4-DEF-linear-space",
        "unit": "線型空間",
        "form": "flashcard",
        "stem": pv("線型空間（ベクトル空間）の定義を述べよ（閉包条件と公理）。"),
        "answer": pv(
            r"集合 $V$ と数の集合 $K$ について、$\forall \boldsymbol{x},\boldsymbol{y},\boldsymbol{z}\in V,\ \forall d,e\in K$ に対し "
            r"$(\ast)\ d\boldsymbol{x}+e\boldsymbol{y}\in V$ であり、かつ"
            r"(1) 加法の結合律 (2) 零元の一意存在 (3) 逆元の一意存在 (4) 加法の交換律 "
            r"(5) スカラー倍の結合律 (6) $1\boldsymbol{x}=\boldsymbol{x}1=\boldsymbol{x}$（単位元） "
            r"(7) スカラー倍の分配律、を満たすとき $V$ を $K$ 上の線型空間という。"
            r"（ノート原文の (6) は $1\boldsymbol{x}=\boldsymbol{x}1=\boldsymbol{x}$ と記されている。）"
        ),
        "explanation": pv(
            r"$K=\mathbb{R}$ のとき実線型空間、$K=\mathbb{C}$ のとき複素線型空間ともいう。"
            r"$V$ の元をベクトル、$K$ の元をスカラーという。"
        ),
        "sources": [src(1, "定義枠")],
        "tags": ["線型空間", "定義", "公理"],
    }
)

add(
    {
        "id": "LA4-EX-matrix-Km",
        "unit": "線型空間",
        "form": "short_answer",
        "stem": pv(r"$m\times n$ 型行列の集合と $K^m$ について、線型空間としての要点を述べよ。"),
        "answer": pv(
            r"$M_{mn}$（$m\times n$ 型行列全体）は線型空間。"
            r"特に $M_{m1}$ を $K$-$m$ 次元数ベクトル空間といい $K^m$ で表す。"
            r"$K^m$ の元を $K$-$m$ 次元数ベクトル（列ベクトル）といい、幾何ベクトルとも呼ぶことがある。"
            r"（例）$\boldsymbol{a}=\begin{pmatrix}1\\2\end{pmatrix}\in\mathbb{R}^2$，"
            r"$\boldsymbol{b}=\begin{pmatrix}1+i\\2-i\\3i\end{pmatrix}\in\mathbb{C}^3$。"
        ),
        "sources": [src(1)],
        "tags": ["線型空間", "例", "数ベクトル空間"],
    }
)

add(
    {
        "id": "LA4-EX-poly-trig",
        "unit": "線型空間",
        "form": "short_answer",
        "stem": pv("多項式の集合と、定数関数＋三角関数の集合が線型空間になることを式で示せ。"),
        "answer": pv(
            r"$V=\{d_0+d_1 x+\cdots+d_n x^n\mid d_i\in K\}$（$n$ 次以下の多項式）は線型空間。"
            r"また "
            r"$V=\left\{c_0+\sum_{n=1}^{N}(a_n\cos nx+b_n\sin nx)\mid c_0,a_n,b_n\in K\right\}$ "
            r"も線型空間。"
        ),
        "sources": [src(1)],
        "tags": ["線型空間", "例", "多項式", "三角関数"],
    }
)

add(
    {
        "id": "LA4-DEF-subspace",
        "unit": "線型部分空間",
        "form": "flashcard",
        "stem": pv("線型部分空間の定義を述べよ。"),
        "answer": pv(
            r"$K$ 上の線型空間 $V$ の部分集合 $W$ が、"
            r"$\forall \boldsymbol{x},\boldsymbol{y}\in W,\ \forall d,e\in K$ に対し "
            r"$(\ast)\ d\boldsymbol{x}+e\boldsymbol{y}\in W$ を満たすとき、"
            r"$W$ を $V$ の（線型）部分空間という。"
            r"（線型部分空間）＝（部分集合）かつ（線型空間）。"
        ),
        "sources": [src(1, "線型部分空間")],
        "tags": ["線型部分空間", "定義"],
    }
)

add(
    {
        "id": "LA4-EX-not-subspace",
        "unit": "線型部分空間",
        "form": "short_answer",
        "stem": pv(r"$W=\{(x,y)\mid y\ge 0\}\subset\mathbb{R}^2$ は部分空間か。理由も述べよ。"),
        "answer": pv(
            r"部分空間ではない。"
            r"（例として閉包条件 $(\ast)$ を満たさない。半平面はスカラー倍・和で外へ出る。）"
        ),
        "sources": [src(1)],
        "tags": ["線型部分空間", "反例"],
    }
)

add(
    {
        "id": "LA4-DEF-trivial-subspace",
        "unit": "線型部分空間",
        "form": "flashcard",
        "stem": pv("自明な部分空間とは何か。"),
        "answer": pv(r"$\{\boldsymbol{0}\}$ および $V$ 自身。これらを線型空間 $V$ の自明な部分空間という。"),
        "sources": [src(1)],
        "tags": ["線型部分空間", "定義"],
    }
)

add(
    {
        "id": "LA4-DEF-sum-direct-sum",
        "unit": "線型部分空間",
        "form": "flashcard",
        "stem": pv(r"部分空間の和 $W_1+W_2$ と直和 $W_1\oplus W_2$ の定義を述べよ。"),
        "answer": pv(
            r"$W_1\cap W_2=\{\boldsymbol{a}\mid \boldsymbol{a}\in W_1,\boldsymbol{a}\in W_2\}$，"
            r"$W_1+W_2=\{\boldsymbol{a}+\boldsymbol{b}\mid \boldsymbol{a}\in W_1,\boldsymbol{b}\in W_2\}$，"
            r"$W_1\oplus W_2=\{\boldsymbol{a}+\boldsymbol{b}\mid \boldsymbol{a}\in W_1,\boldsymbol{b}\in W_2,\ W_1\cap W_2=\{\boldsymbol{0}\}\}$。"
            r"いずれも $V$ の部分空間。$W_1+W_2$ を和、$W_1\oplus W_2$ を直和という。"
            r"また $V=W_1\oplus W_2 \iff \forall\boldsymbol{x}\in V$ が $\boldsymbol{x}=\boldsymbol{x}_1+\boldsymbol{x}_2$ と一意に分解される。"
        ),
        "explanation": pv(
            r"ノートでは直和の定義に $W_1\cap W_2=\{\boldsymbol{0}\}$ を集合の条件として併記している。"
            r"注: $W_1+W_2\neq W_1\cup W_2$。合併は一般に線型空間にならない。"
        ),
        "sources": [src(1)],
        "tags": ["和", "直和", "定義"],
    }
)

add(
    {
        "id": "LA4-EX-sum-vs-union",
        "unit": "線型部分空間",
        "form": "calculation",
        "stem": pv(
            r"$W_1=\left\{\begin{pmatrix}a\\0\end{pmatrix}\mid a\in\mathbb{R}\right\}$，"
            r"$W_2=\left\{\begin{pmatrix}0\\b\end{pmatrix}\mid b\in\mathbb{R}\right\}$ において、"
            r"$\boldsymbol{w}_1+\boldsymbol{w}_2$ と $W_1\cup W_2$ の関係を示せ。"
        ),
        "answer": pv(
            r"$\boldsymbol{w}_1=\begin{pmatrix}1\\0\end{pmatrix}\in W_1$，"
            r"$\boldsymbol{w}_2=\begin{pmatrix}0\\1\end{pmatrix}\in W_2$ をとると "
            r"$W_1+W_2\ni \boldsymbol{w}_1+\boldsymbol{w}_2=\begin{pmatrix}1\\1\end{pmatrix}\notin W_1\cup W_2$。"
        ),
        "sources": [src(1)],
        "tags": ["和", "合併", "例"],
    }
)

# ---------- p.2 基底・次元・階数・次元公式 ----------
add(
    {
        "id": "LA4-DEF-basis",
        "unit": "基底と次元",
        "form": "flashcard",
        "stem": pv("線型空間の基底の定義を述べよ。"),
        "answer": pv(
            r"$V\neq\{\boldsymbol{0}\}$ の $l$ 個のベクトル $\boldsymbol{a}_1,\ldots,\boldsymbol{a}_l$ が"
            r"(1) 1次独立、(2) 任意の $\boldsymbol{b}\in V$ がそれらの1次結合で表せる（生成する）とき、"
            r"組 $\{\boldsymbol{a}_1,\ldots,\boldsymbol{a}_l\}$ を $V$ の基底という。"
            r"$V=\{\boldsymbol{0}\}$ のときは基底は存在しない。"
        ),
        "sources": [src(2, "基底")],
        "tags": ["基底", "定義"],
    }
)

add(
    {
        "id": "LA4-DEF-standard-basis",
        "unit": "基底と次元",
        "form": "flashcard",
        "stem": pv(r"$K^n$ の標準基底（単位ベクトル）とは何か。"),
        "answer": pv(
            r"$\boldsymbol{e}_1=\begin{pmatrix}1\\0\\\vdots\\0\end{pmatrix},\ldots,"
            r"\boldsymbol{e}_n=\begin{pmatrix}0\\\vdots\\0\\1\end{pmatrix}$。"
            r"これらは $K^n$ の基底であり、標準基底（単位ベクトル、基本ベクトル）という。"
        ),
        "sources": [src(2)],
        "tags": ["標準基底", "定義"],
    }
)

add(
    {
        "id": "LA4-DEF-span",
        "unit": "基底と次元",
        "form": "flashcard",
        "stem": pv(r"張られた（生成された）部分空間 $\langle \boldsymbol{x}_1,\ldots,\boldsymbol{x}_m\rangle$ の定義を述べよ。"),
        "answer": pv(
            r"$\langle \boldsymbol{x}_1,\ldots,\boldsymbol{x}_m\rangle = K\boldsymbol{x}_1+\cdots+K\boldsymbol{x}_m"
            r":=\{d_1\boldsymbol{x}_1+\cdots+d_m\boldsymbol{x}_m\mid d_i\in K\}$。"
            r"基底 $\{\boldsymbol{a}_1,\ldots,\boldsymbol{a}_l\}$ に対し $V=\langle\boldsymbol{a}_1,\ldots,\boldsymbol{a}_l\rangle$ とも書く。"
        ),
        "sources": [src(2)],
        "tags": ["生成", "部分空間", "定義"],
    }
)

add(
    {
        "id": "LA4-EX-span-R2",
        "unit": "基底と次元",
        "form": "calculation",
        "stem": pv(
            r"$\mathbb{R}^2=\langle\boldsymbol{e}_1,\boldsymbol{e}_2\rangle="
            r"\left\langle\begin{pmatrix}1\\0\end{pmatrix},\begin{pmatrix}1\\1\end{pmatrix}\right\rangle="
            r"\left\langle\begin{pmatrix}1\\0\end{pmatrix},\begin{pmatrix}2\\1\end{pmatrix},\begin{pmatrix}3\\3\end{pmatrix}\right\rangle$ "
            r"を、一般の $\boldsymbol{x}=\begin{pmatrix}x\\y\end{pmatrix}$ の表示で確かめよ。"
        ),
        "answer": pv(
            r"$\boldsymbol{x}=x\boldsymbol{e}_1+y\boldsymbol{e}_2$"
            r"$=(x-y)\begin{pmatrix}1\\0\end{pmatrix}+y\begin{pmatrix}1\\1\end{pmatrix}$"
            r"$=(x+y)\begin{pmatrix}1\\0\end{pmatrix}+(-2y)\begin{pmatrix}2\\1\end{pmatrix}+y\begin{pmatrix}3\\3\end{pmatrix}$。"
        ),
        "sources": [src(2)],
        "tags": ["生成", "例", "検算済"],
        "corrections": [
            {
                "field": "answer.value",
                "before": "（Gemini草稿の係数表示）",
                "after": "(x+y)(1,0)^T + (-2y)(2,1)^T + y(3,3)^T",
                "reason": "ページ画像照合・係数検算。$(x+y,-2y+3y)=(x,y)$ となり正しい。",
            }
        ],
    }
)

add(
    {
        "id": "LA4-DEF-dimension",
        "unit": "基底と次元",
        "form": "flashcard",
        "stem": pv(r"次元 $\dim V$ の定義を述べよ。"),
        "answer": pv(
            r"基底の取り方は一通りではないが個数は一定。その個数を $\dim V$ という。"
            r"$V=\{\boldsymbol{0}\}$ のときは $\dim V=0$。"
            r"$\dim V=n$ のとき $V^n$ と表すこともある。"
        ),
        "explanation": pv(
            r"（例）$\dim\mathbb{R}^2=2$；$\dim M_{mn}=mn$（行列単位 $E_{ij}$）；"
            r"$V=\langle 1,x,\ldots,x^n\rangle$ なら $\dim V=n+1$。"
        ),
        "sources": [src(2, "基底と次元")],
        "tags": ["次元", "定義"],
    }
)

add(
    {
        "id": "LA4-DEF-rank-dim",
        "unit": "行列の階数と次元",
        "form": "flashcard",
        "stem": pv(r"$\operatorname{rank} A$ と生成部分空間の次元の関係を述べよ。"),
        "answer": pv(
            r"$A=(\boldsymbol{x}_1\cdots\boldsymbol{x}_l)\in M_{nl}$ のとき "
            r"$\operatorname{rank} A=\dim\langle\boldsymbol{x}_1,\ldots,\boldsymbol{x}_l\rangle$。"
        ),
        "sources": [src(2, "行列の階数と次元")],
        "tags": ["階数", "次元", "定義"],
    }
)

add(
    {
        "id": "LA4-EX-rank-matrix",
        "unit": "行列の階数と次元",
        "form": "calculation",
        "stem": pv(
            r"$\boldsymbol{x}_1=\begin{pmatrix}1\\2\\3\end{pmatrix}$，"
            r"$\boldsymbol{x}_2=\begin{pmatrix}4\\5\\6\end{pmatrix}$，"
            r"$\boldsymbol{x}_3=\begin{pmatrix}7\\8\\9\end{pmatrix}$ に対し "
            r"$\operatorname{rank} A$ と $\dim\langle\boldsymbol{x}_1,\boldsymbol{x}_2,\boldsymbol{x}_3\rangle$ を求めよ。"
        ),
        "answer": pv(
            r"$A=\begin{pmatrix}1&4&7\\2&5&8\\3&6&9\end{pmatrix}$ を行基本変形すると "
            r"$\begin{pmatrix}1&4&7\\0&-3&-6\\0&0&0\end{pmatrix}$ より $\operatorname{rank} A=2$。"
            r"また $\boldsymbol{x}_3=-\boldsymbol{x}_1+2\boldsymbol{x}_2$ なので次元も $2$。"
        ),
        "sources": [src(2)],
        "tags": ["階数", "例", "検算済"],
        "corrections": [
            {
                "field": "answer.value",
                "before": "x3 = -x1 + 2 x2（草稿）",
                "after": "x3 = -x1 + 2 x2（確定）",
                "reason": "検算: -x1+2x2=(7,8,9)^T。行基本変形の結果とも一致。",
            }
        ],
    }
)

add(
    {
        "id": "LA4-PROP-basis-extend",
        "unit": "基底と次元",
        "form": "short_answer",
        "stem": pv("有限次元空間で、部分空間の基底を全体の基底へ延長できることを述べよ。"),
        "answer": pv(
            r"$\dim V=n<\infty$，$\dim W=l\le n$ のとき、$W$ の基底に $(n-l)$ 個のベクトルを付け加えて "
            r"$V$ の基底にできる。付け加えたベクトルが張る部分空間を $W_2$ とおけば $V=W\oplus W_2$。"
            r"（有限次元のときに限る。）"
        ),
        "sources": [src(2)],
        "tags": ["基底", "延長", "直和"],
    }
)

add(
    {
        "id": "LA4-THM-dim-formula",
        "unit": "次元公式",
        "form": "flashcard",
        "stem": pv("次元公式を述べよ。"),
        "answer": pv(
            r"有限次元部分空間 $W_1,W_2$ に対し "
            r"$\dim(W_1+W_2)+\dim(W_1\cap W_2)=\dim W_1+\dim W_2$。"
        ),
        "sources": [src(2, "次元公式")],
        "tags": ["次元公式", "定理"],
    }
)

add(
    {
        "id": "LA4-EX-dim-formula",
        "unit": "次元公式",
        "form": "calculation",
        "stem": pv(
            r"$V=\mathbb{R}^3$，$W_1: x+y+z=0$，$W_2: 2x+3y-z=0$ について "
            r"$\dim(W_1+W_2)$ を次元公式と行列の階数の両方で求めよ。"
        ),
        "answer": pv(
            r"$W_1=\left\langle\begin{pmatrix}1\\0\\-1\end{pmatrix},\begin{pmatrix}0\\1\\-1\end{pmatrix}\right\rangle$（$\dim=2$），"
            r"$W_2=\left\langle\begin{pmatrix}1\\0\\2\end{pmatrix},\begin{pmatrix}0\\1\\3\end{pmatrix}\right\rangle$（$\dim=2$），"
            r"$W_1\cap W_2=\left\langle\begin{pmatrix}4\\-3\\-1\end{pmatrix}\right\rangle$（$\dim=1$）より "
            r"$\dim(W_1+W_2)=2+2-1=3$。"
            r"また $\operatorname{rank}\begin{pmatrix}1&0&1&0\\0&1&0&1\\-1&-1&2&3\end{pmatrix}=3$ でも確認。"
        ),
        "sources": [src(2)],
        "tags": ["次元公式", "例", "検算済"],
        "corrections": [
            {
                "field": "answer.value",
                "before": "交わり基底 (4,-3,-1)",
                "after": "(4,-3,-1)（確定）",
                "reason": "x+y+z=0 と 2x+3y-z=0 より z=-x-y、代入で x+3y+(-x-y) 等を解くと方向ベクトル (4,-3,-1)。検算: 4-3-1=0、8-9-(-1)=0。",
            }
        ],
    }
)

# ---------- p.3 線型写像 ----------
add(
    {
        "id": "LA4-DEF-mapping",
        "unit": "線型写像",
        "form": "flashcard",
        "stem": pv("写像・定義域・変換の定義を述べよ。"),
        "answer": pv(
            r"集合 $V$ の各元に $W$ の元を一意に対応させる対応を写像 $f:V\to W$ という。"
            r"$V$ を定義域という。特に $f:V\to V$ を変換という。"
        ),
        "figures": [fig("pipeline/images/figures/fig_map_sets.png", 3, "写像の対応図")],
        "sources": [src(3, "写像")],
        "tags": ["写像", "定義"],
    }
)

add(
    {
        "id": "LA4-DEF-linear-map",
        "unit": "線型写像",
        "form": "flashcard",
        "stem": pv("線型写像（1次写像）の定義を述べよ。"),
        "answer": pv(
            r"$f:V\to W$ が $\forall\boldsymbol{x},\boldsymbol{y}\in V,\ \forall d,e\in K$ に対し "
            r"$f(d\boldsymbol{x}+e\boldsymbol{y})=df(\boldsymbol{x})+ef(\boldsymbol{y})$ を満たすとき線型写像という。"
            r"任意の $A_{mn}:K^n\to K^m$ は線型写像。正方行列による写像は線型変換。"
            r"また $f(\boldsymbol{0}_V)=\boldsymbol{0}_W$。微分・定積分・不定積分（$C=0$）も線型写像。"
        ),
        "sources": [src(3, "線型写像")],
        "tags": ["線型写像", "定義"],
    }
)

add(
    {
        "id": "LA4-DEF-im-ker",
        "unit": "像と核",
        "form": "flashcard",
        "stem": pv(r"像 $\operatorname{Im} f$ と核 $\operatorname{Ker} f$ の定義を述べよ。"),
        "answer": pv(
            r"$\operatorname{Im} f:=f(V)=\{w\mid w=f(v),v\in V\}\subseteq W$（$\operatorname{Im} f=W$ なら全射）。"
            r"$\operatorname{Ker} f:=f^{-1}(\boldsymbol{0}_W)=\{v\mid f(v)=\boldsymbol{0}_W\}\subseteq V$。"
            r"一般に $f^{-1}(w)=\{v\mid f(v)=w\}$ を逆像という。"
        ),
        "figures": [
            fig("pipeline/images/figures/fig_im_f.png", 3, "像 Im f の模式図"),
            fig("pipeline/images/figures/fig_ker_f.png", 3, "核 Ker f の模式図"),
        ],
        "sources": [src(3, "像と核")],
        "tags": ["像", "核", "定義"],
    }
)

add(
    {
        "id": "LA4-DEF-surj-inj-bij",
        "unit": "像と核",
        "form": "flashcard",
        "stem": pv("全射・単射・全単射（双射）と逆写像を述べよ。"),
        "answer": pv(
            r"全射: $\operatorname{Im} f=W$。単射: $f(v_1)=f(v_2)\Rightarrow v_1=v_2$。"
            r"全射かつ単射のとき全単射。このとき逆写像 $f^{-1}:W\to V$ がただ一つ存在し、それも全単射。"
        ),
        "figures": [fig("pipeline/images/figures/fig_bijection.png", 3, "全単射と逆写像")],
        "sources": [src(3)],
        "tags": ["全射", "単射", "全単射", "定義"],
    }
)

add(
    {
        "id": "LA4-EX-v2-map",
        "unit": "像と核",
        "form": "short_answer",
        "stem": pv(r"$V=\mathbb{R}$，$W=[0,\infty]$，$w=f(v)=v^2$ の性質を述べよ。"),
        "answer": pv(
            r"線型写像でない／全射である／単射でない。"
            r"（ノート原文の終域表記は $W=[0,\infty]$。数学的には像は通常 $[0,\infty)$ と書く。）"
        ),
        "figures": [fig("pipeline/images/figures/fig_ex_v2.png", 3, "w=v^2 のグラフ")],
        "sources": [src(3)],
        "tags": ["例", "全射", "単射"],
        "corrections": [
            {
                "field": "stem.value",
                "before": "W=[0,∞]（草稿）",
                "after": "W=[0,∞]（原文維持）+ 数学的注記",
                "reason": "ページ画像照合。閉じ括弧の記法は原文どおり。像の標準記法との差は answer に注記。",
            }
        ],
    }
)

add(
    {
        "id": "LA4-EX-half-v-map",
        "unit": "像と核",
        "form": "short_answer",
        "stem": pv(r"$f(v)=\frac{1}{2}v$（$V=W=\mathbb{R}$）の性質と逆写像を述べよ。"),
        "answer": pv(
            r"線型写像（変換）であり全単射。逆写像は $v=f^{-1}(w)=2w$。"
        ),
        "figures": [fig("pipeline/images/figures/fig_ex_half_v.png", 3, "w=(1/2)v のグラフ")],
        "sources": [src(3)],
        "tags": ["例", "全単射", "逆写像"],
    }
)

add(
    {
        "id": "LA4-DEF-isomorphism",
        "unit": "像と核",
        "form": "flashcard",
        "stem": pv("同型写像・同型・置換の定義を述べよ。"),
        "answer": pv(
            r"全単射な線型写像を同型写像といい、このとき $V\simeq W$（同型）。"
            r"全単射な変換を置換という。"
        ),
        "sources": [src(3)],
        "tags": ["同型", "置換", "定義"],
    }
)

add(
    {
        "id": "LA4-PROP-im-ker",
        "unit": "像と核",
        "form": "flashcard",
        "stem": pv("線型写像の像と核の基本性質を述べよ。"),
        "answer": pv(
            r"(i) $\operatorname{Im} f$ は $W$ の部分空間（全射 $\iff\operatorname{Im} f=W$）。"
            r"(ii) $\operatorname{Ker} f$ は $V$ の部分空間（単射 $\iff\operatorname{Ker} f=\{\boldsymbol{0}_V\}$）。"
        ),
        "sources": [src(3, "線型写像の像と核の性質")],
        "tags": ["像", "核", "性質"],
    }
)

add(
    {
        "id": "LA4-THM-8",
        "unit": "像と核",
        "form": "flashcard",
        "stem": pv("定理8を述べよ。"),
        "answer": pv(
            r"$K$ 上の線型空間 $V^n$（$\dim V=n<\infty$）は $K^n$ と同型である。"
            r"（基底による座標対応 $ (d_1,\ldots,d_n)^T \mapsto d_1\boldsymbol{a}_1+\cdots+d_n\boldsymbol{a}_n $ が同型写像。）"
        ),
        "explanation": pv(
            r"この対応で得られる $n$ 次元数ベクトルを、基底に関する座標（ベクトル）という。"
            r"線型空間の現れ方の例: ①生成空間 ②関数空間 $\mathcal{F}(V,K)$ ③④ $\operatorname{Im} f$ と $\operatorname{Ker} f$。"
        ),
        "sources": [src(3, "定理8")],
        "tags": ["定理8", "同型"],
    }
)

# ---------- p.4 表現行列・次元定理 ----------
add(
    {
        "id": "LA4-DEF-rep-matrix",
        "unit": "線型写像としての行列",
        "form": "flashcard",
        "stem": pv("表現行列（行列表示）の定義を述べよ。"),
        "answer": pv(
            r"基底 $\{\boldsymbol{a}_i\}$，$\{\boldsymbol{b}_j\}$ のもと "
            r"$(f(\boldsymbol{a}_1)\cdots f(\boldsymbol{a}_n))=(\boldsymbol{b}_1\cdots\boldsymbol{b}_m)A$ "
            r"を満たす行列 $A$ を表現行列 $A_f$ といい、対応する写像を $f_A$ という。"
        ),
        "figures": [fig("pipeline/images/figures/fig_rep_matrix_comm.png", 4, "表現行列の可換図式")],
        "sources": [src(4)],
        "tags": ["表現行列", "定義"],
    }
)

add(
    {
        "id": "LA4-THM-9",
        "unit": "線型写像としての行列",
        "form": "flashcard",
        "stem": pv("定理9を述べよ。"),
        "answer": pv(
            r"$\mathcal{L}_K(V^n,W^m)\simeq M_{mn}$。"
            r"すなわち線型写像 $f_A$ は行列 $A_f$ に置き換えられる。"
        ),
        "explanation": pv(
            r"定理8・9より、線型代数学は $K^n$ 上の $m\times n$ 型行列についての学問ともいえる。"
        ),
        "sources": [src(4, "定理9")],
        "tags": ["定理9", "表現行列"],
    }
)

add(
    {
        "id": "LA4-DEF-rank-of-map",
        "unit": "線型写像としての行列",
        "form": "flashcard",
        "stem": pv("線型写像の階数・退化次数を述べよ。"),
        "answer": pv(
            r"$\operatorname{rank} f:=\dim(\operatorname{Im} f)$。"
            r"$\dim(\operatorname{Ker} f)$ を退化次数という。"
            r"表現行列 $A_f=(\boldsymbol{a}_1\cdots\boldsymbol{a}_n)$ なら $\operatorname{Im} f=\langle\boldsymbol{a}_1,\ldots,\boldsymbol{a}_n\rangle$ で "
            r"$\operatorname{rank} f=\operatorname{rank} A_f$。"
        ),
        "sources": [src(4)],
        "tags": ["階数", "退化次数", "定義"],
    }
)

add(
    {
        "id": "LA4-PROP-rank-criteria",
        "unit": "線型写像としての行列",
        "form": "flashcard",
        "stem": pv("表現行列の階数による全射・単射・全単射の判定を述べよ。"),
        "answer": pv(
            r"(i) 全射 $\iff\operatorname{rank} A_f=m\ (\le n)$。"
            r"(ii) 単射 $\iff\operatorname{rank} A_f=n\ (\le m)$ $\iff A_f\boldsymbol{x}=\boldsymbol{0}$ の解は $\boldsymbol{0}$ のみ。"
            r"(iii) 全単射 $\iff\operatorname{rank} A_f=m=n\iff\det A_f\neq 0$。"
        ),
        "sources": [src(4, "線型写像の階数")],
        "tags": ["階数", "全射", "単射"],
    }
)

add(
    {
        "id": "LA4-THM-dim-theorem",
        "unit": "次元定理",
        "form": "flashcard",
        "stem": pv("次元定理を述べよ。"),
        "answer": pv(
            r"有限次元 $V$ から $W$ への線型写像 $f$ について "
            r"$\dim V=\dim(\operatorname{Im} f)+\dim(\operatorname{Ker} f)$。"
            r"特に $\operatorname{rank} A_f=r$ なら $\dim(\operatorname{Ker} f)=n-r$（基本解が $n-r$ 個）。"
        ),
        "sources": [src(4, "次元定理")],
        "tags": ["次元定理", "定理"],
    }
)

add(
    {
        "id": "LA4-EX-dim-theorem",
        "unit": "次元定理",
        "form": "calculation",
        "stem": pv(
            r"$f:\mathbb{R}^3\to\mathbb{R}^3$，"
            r"$f\begin{pmatrix}x\\y\\z\end{pmatrix}=\begin{pmatrix}x+y-z\\4x+y-2z\\2x-y\end{pmatrix}$ について "
            r"$\operatorname{Im} f$，$\operatorname{Ker} f$，全射/単射性を求めよ。"
        ),
        "answer": pv(
            r"$A_f=\begin{pmatrix}1&1&-1\\4&1&-2\\2&-1&0\end{pmatrix}$，$\operatorname{rank} A_f=2$。"
            r"$\operatorname{Im} f=\{(X,Y,Z)^T\mid 2X-Y+Z=0\}$（2次元平面）。"
            r"$\dim(\operatorname{Ker} f)=3-2=1$，$\operatorname{Ker} f=\left\langle\begin{pmatrix}1\\2\\3\end{pmatrix}\right\rangle$"
            r"（$\frac{x}{1}=\frac{y}{2}=\frac{z}{3}$）。"
            r"$\dim V=3\neq 2=\operatorname{rank} A_f\neq 3=\dim W$ より全射でも単射でも全単射でもない。"
            r"別解: $\operatorname{Im} f=\left\langle\begin{pmatrix}1\\4\\2\end{pmatrix},\begin{pmatrix}1\\1\\-1\end{pmatrix}\right\rangle$。"
        ),
        "sources": [src(4)],
        "tags": ["次元定理", "例", "検算済"],
        "corrections": [
            {
                "field": "answer.value",
                "before": "制約 2X-Y+Z=0 / Ker 方向 (1,2,3)",
                "after": "同左（検算確定）",
                "reason": "拡大行列の行基本変形で第3行が 0=2X-Y+Z。斉次系から y=2x,z=3x。A_f(1,2,3)^T=0 を検算。",
            }
        ],
    }
)

# ---------- p.5 合成・逆・いろいろな写像 ----------
add(
    {
        "id": "LA4-THM-compose-inverse",
        "unit": "合成写像および逆写像の表現行列",
        "form": "flashcard",
        "stem": pv("合成写像・逆写像の表現行列の公式を述べよ。"),
        "answer": pv(
            r"$A_{g\circ f}=B_g A_f$。"
            r"特に $f$ が全単射（同型）なら $A_{f^{-1}}=A_f^{-1}$。"
        ),
        "figures": [
            fig("pipeline/images/figures/fig_compose_maps.png", 5, "合成写像と行列積"),
            fig("pipeline/images/figures/fig_inverse_maps.png", 5, "逆写像と逆行列"),
        ],
        "sources": [src(5)],
        "tags": ["合成写像", "逆写像", "表現行列"],
    }
)

add(
    {
        "id": "LA4-EX-compose-inverse",
        "unit": "合成写像および逆写像の表現行列",
        "form": "calculation",
        "stem": pv(
            r"$A_f=\begin{pmatrix}1&2\\3&4\end{pmatrix}$，$B_g=\begin{pmatrix}3&1\\4&2\\5&0\end{pmatrix}$ のとき "
            r"$A_{g\circ f}$ と $A_{f^{-1}}$ を求めよ。"
        ),
        "answer": pv(
            r"$A_{g\circ f}=B_g A_f=\begin{pmatrix}6&10\\10&16\\5&10\end{pmatrix}$。"
            r"$A_{f^{-1}}=A_f^{-1}=\dfrac{1}{-2}\begin{pmatrix}4&-2\\-3&1\end{pmatrix}"
            r"=\begin{pmatrix}-2&1\\\frac{3}{2}&-\frac{1}{2}\end{pmatrix}$。"
        ),
        "sources": [src(5)],
        "tags": ["合成写像", "逆行列", "例", "検算済"],
        "corrections": [
            {
                "field": "answer.value",
                "before": "行列積・逆行列（草稿）",
                "after": "同値を検算で確定",
                "reason": "3*1+1*3=6 等。det(Af)=1*4-2*3=-2。逆行列公式どおり。",
            }
        ],
    }
)

add(
    {
        "id": "LA4-DEF-reflections",
        "unit": "いろいろな線型写像",
        "form": "flashcard",
        "stem": pv(r"$\mathbb{R}^2$ の折り返し（対称移動）行列を列挙せよ。"),
        "answer": pv(
            r"$A_x=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$（$x$ 軸）、"
            r"$A_y=\begin{pmatrix}-1&0\\0&1\end{pmatrix}$（$y$ 軸）、"
            r"$A_0=\begin{pmatrix}-1&0\\0&-1\end{pmatrix}=A_x A_y=A_y A_x$（原点）、"
            r"$L=\begin{pmatrix}\frac{1-a^2}{1+a^2}&\frac{2a}{1+a^2}\\\frac{2a}{1+a^2}&\frac{a^2-1}{1+a^2}\end{pmatrix}$"
            r"（直線 $y=ax$）。"
        ),
        "figures": [
            fig("pipeline/images/figures/fig_reflect_axes.png", 5, "軸・原点に関する折り返し"),
            fig("pipeline/images/figures/fig_reflect_line.png", 5, "直線 y=ax に関する折り返し"),
        ],
        "sources": [src(5, "折り返し行列")],
        "tags": ["折り返し", "表現行列"],
    }
)

add(
    {
        "id": "LA4-DEF-rotation",
        "unit": "いろいろな線型写像",
        "form": "flashcard",
        "stem": pv("回転行列と、直線折り返しの回転表現を述べよ。"),
        "answer": pv(
            r"原点中心・反時計回り $\theta$ 回転: "
            r"$R_\theta=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}$。"
            r"直線 $y=(\tan\theta)x$ に関する折り返しは "
            r"$L=\begin{pmatrix}\cos 2\theta&\sin 2\theta\\\sin 2\theta&-\cos 2\theta\end{pmatrix}=R_\theta A_x R_{-\theta}$。"
        ),
        "figures": [fig("pipeline/images/figures/fig_rotation.png", 5, "回転の図")],
        "sources": [src(5, "回転行列")],
        "tags": ["回転", "折り返し", "表現行列"],
    }
)

add(
    {
        "id": "LA4-DEF-scaling",
        "unit": "いろいろな線型写像",
        "form": "flashcard",
        "stem": pv("拡大行列を述べよ。"),
        "answer": pv(
            r"$x$ 方向に $a$ 倍、$y$ 方向に $b$ 倍: $A_e=\begin{pmatrix}a&0\\0&b\end{pmatrix}$。"
        ),
        "figures": [fig("pipeline/images/figures/fig_scaling.png", 5, "拡大の図")],
        "sources": [src(5, "拡大行列")],
        "tags": ["拡大", "表現行列"],
    }
)


def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    # questions_raw (1 file per question)
    qdir = PIPELINE / "questions_raw"
    if qdir.exists():
        shutil.rmtree(qdir)
    qdir.mkdir(parents=True, exist_ok=True)
    for q in QUESTIONS:
        write_json(qdir / f"{q['id']}.json", q)

    structured = {
        "schema_version": "1.0.0",
        "exam": EXAM,
        "subject": SUBJECT,
        "generated_at": NOW,
        "notes": (
            "手書きノート5ページ（線型空間〜いろいろな線型写像）。"
            "Gemini草稿をページ画像と照合。穴埋め補完は未実施（filled=false）。"
            "p.5左上別紙切れ込みは本文外のため非取込。公式範囲表は未入手。"
        ),
        "questions": QUESTIONS,
    }
    write_json(ROOT / "structured" / "questions.json", structured)

    corr = {
        "generated_at": NOW,
        "count": len(CORRECTIONS_LOG),
        "items": CORRECTIONS_LOG,
    }
    write_json(PIPELINE / "corrections_log.json", corr)

    # corrected transcript: start from gemini source, prepend QC header
    src_md = (PIPELINE / "transcripts" / "gemini_transcript_source.md").read_text(encoding="utf-8")
    header = (
        "<!--\n"
        "照合済み文字起こし（2026-11-11）。起点: gemini_transcript_source.md（Gemini 4 Argon）。\n"
        "- ページ画像と照合し、数式は検算。大きな読み違いは corrections_log.json。\n"
        "- p.5左上の別紙切れ込み（【状 / 【問）は本文ではないため未収録。\n"
        "- 全文手書きのため {{手書き}} マークなし（設計どおり）。\n"
        "-->\n\n"
    )
    # Drop the original HTML comment block from gemini source to avoid duplication
    body = src_md
    if body.startswith("<!--"):
        end = body.find("-->")
        if end != -1:
            body = body[end + 3 :].lstrip("\n")
    (PIPELINE / "transcripts" / "note_linear_space_2026-11_corrected.md").write_text(
        header + body, encoding="utf-8"
    )

    # per-page stubs pointing to corrected
    for i in range(1, 6):
        (PIPELINE / "transcripts" / f"note_linear_space_2026-11_p{i:03d}.md").write_text(
            f"# p.{i}\n\n訂正済み全文: `note_linear_space_2026-11_corrected.md` の `## p.{i}` を参照。\n",
            encoding="utf-8",
        )

    unverified = []
    for q in QUESTIONS:
        for field in ("stem", "answer", "explanation"):
            obj = q.get(field)
            if isinstance(obj, dict) and obj.get("status") == "unverified":
                unverified.append(q["id"])
                break

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
            "corrections": len(CORRECTIONS_LOG),
            "unverified": len(unverified),
            "inferred_answers": 0,
        },
        "unverified_ids": unverified,
        "notes": (
            "進捗: 手書きノート取込済。schema検証・アプリ登録は後続ステップ。"
            "穴埋め補完は未実施（filled=false）。公式範囲表は未入手。"
        ),
    }
    write_json(ROOT / "status.json", status)

    print(
        f"OK: {len(QUESTIONS)} questions, {len(CORRECTIONS_LOG)} corrections, "
        f"{len(unverified)} unverified"
    )


if __name__ == "__main__":
    main()
