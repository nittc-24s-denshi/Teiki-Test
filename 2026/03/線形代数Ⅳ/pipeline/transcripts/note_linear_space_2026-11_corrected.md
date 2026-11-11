<!--
照合済み文字起こし（2026-11-11）。起点: gemini_transcript_source.md（Gemini 4 Argon）。
- ページ画像と照合し、数式は検算。大きな読み違いは corrections_log.json。
- p.5左上の別紙切れ込み（【状 / 【問）は本文ではないため未収録。
- 全文手書きのため {{手書き}} マークなし（設計どおり）。
-->

## p.1

### 線型空間



**線型空間**
ある集合 $V$，数からなるある集合 $K$ について，$\forall \boldsymbol{x}, \boldsymbol{y}, \boldsymbol{z} \in V, \forall d, e \in K$ に対して，

$$(*) \quad d\boldsymbol{x} + e\boldsymbol{y} \in V$$


であり，かつ
(1) $(\boldsymbol{x} + \boldsymbol{y}) + \boldsymbol{z} = \boldsymbol{x} + (\boldsymbol{y} + \boldsymbol{z})$ ：加法についての結合律
(2) $\boldsymbol{x} + \boldsymbol{0} = \boldsymbol{0} + \boldsymbol{x} = \boldsymbol{x}$ を満たす $\boldsymbol{0} \in V$ がただ1つ存在する：零元の存在
(3) $\boldsymbol{x} + (-\boldsymbol{x}) = (-\boldsymbol{x}) + \boldsymbol{x} = \boldsymbol{0}$ を満たす $-\boldsymbol{x} \in V$ がただ1つ存在する：逆元の存在
(4) $\boldsymbol{x} + \boldsymbol{y} = \boldsymbol{y} + \boldsymbol{x}$ ：加法についての交換律
(5) $(de)\boldsymbol{x} = d(e\boldsymbol{x})$ ：スカラー倍についての結合律
(6) $1\boldsymbol{x} = \boldsymbol{x}1 = \boldsymbol{x}$ ：単位元の存在
(7) $\begin{cases} d(\boldsymbol{x} + \boldsymbol{y}) = d\boldsymbol{x} + d\boldsymbol{y} \\ (d + e)\boldsymbol{x} = d\boldsymbol{x} + e\boldsymbol{x} \end{cases}$ ：スカラー倍についての分配律
を満たすものとする．このとき，集合 $V$ を，$K$ 上の線型空間（$K$ 上のベクトル空間）といい，線型空間 $V$ の元をベクトル，集合 $K$ の元をスカラーという．

* $K = \mathbb{R}$ であるとき，実線型空間 $V$，$K = \mathbb{C}$ であるとき，複素線型空間 $V$ ということもある．


* $m \times n$ 型行列 $A_{mn}$ の集合 $M_{mn}$ は線型空間である．特に，$M_{m1}$ を，$K - m$ 次元数ベクトル空間といい，$K^m$ で表す．$K^m$ の元 $\boldsymbol{a}$ を，$K - m$ 次元数ベクトル（$K - m$ 次元列ベクトル）といい，$\boldsymbol{0} \in K^m$ を零ベクトルという．$K - m$ 次元数ベクトルは，図示して視覚的（図形的）に扱うことができるので，一般のベクトルと区別して，幾何ベクトルということもある．
（例）$\boldsymbol{a} = \begin{pmatrix} 1 \\ 2 \end{pmatrix} \in \mathbb{R}^2$ ， $\boldsymbol{b} = \begin{pmatrix} 1+i \\ 2-i \\ 3i \end{pmatrix} \in \mathbb{C}^3$


* $n$ 次以下の多項式の集合 $V = \{ d_0 + d_1 x + \cdots + d_n x^n \mid d_0, d_1, \cdots, d_n \in K \}$ は線型空間である．


* 定数関数および三角関数の集合


$$V = \left\{ c_0 + \sum_{n=1}^N (a_n \cos nx + b_n \sin nx) \;\middle\vert{}\; c_0, a_1, \cdots, a_N, b_1, \cdots, b_N \in K \right\}$$



は線型空間である．



---

**線型部分空間**
$K$ 上の線型空間 $V$ の部分集合 $W$ について，$\forall \boldsymbol{x}, \boldsymbol{y} \in W, \forall d, e \in K$ に対して，

$$(*) \quad d\boldsymbol{x} + e\boldsymbol{y} \in W$$


を満たすとき，集合 $W$ を，線型空間 $V$ の（線型）部分空間という．

* $(\text{線型部分空間}) = (\text{部分集合}) \text{ かつ } (\text{線型空間})$ である．
（例）$W = \{ (x, y) \mid y \ge 0 \} \subset \mathbb{R}^2$ は $\mathbb{R}^2$ の部分空間ではない．


* $\{ \boldsymbol{0} \}$，$V$ 自身は，線型空間 $V$ の部分空間である．これら2つを，線型空間 $V$ の自明な部分空間という．



線型空間 $V$ の部分空間 $W_1, W_2$ に対して，

$$\begin{aligned} W_1 \cap W_2 &= \{ \boldsymbol{a} \mid \boldsymbol{a} \in W_1, \boldsymbol{a} \in W_2 \} \\ W_1 + W_2 &= \{ \boldsymbol{a} + \boldsymbol{b} \mid \boldsymbol{a} \in W_1, \boldsymbol{b} \in W_2 \} \\ W_1 \oplus W_2 &= \{ \boldsymbol{a} + \boldsymbol{b} \mid \boldsymbol{a} \in W_1, \boldsymbol{b} \in W_2, W_1 \cap W_2 = \{ \boldsymbol{0} \} \} \end{aligned}$$


もまた，線型空間 $V$ の部分空間である．部分空間 $W_1 + W_2$ を，部分空間 $W_1$ と $W_2$ の和，部分空間 $W_1 \oplus W_2$ を，部分空間 $W_1$ と $W_2$ の直和という．
（注）$W_1 + W_2$（和）$\neq W_1 \cup W_2$（合併集合）
（例）$W_1 = \left\{ \boldsymbol{a} \;\middle\vert{}\; \boldsymbol{a} = \begin{pmatrix} a \\ 0 \end{pmatrix}, a \in \mathbb{R} \right\}, W_2 = \left\{ \boldsymbol{b} \;\middle\vert{}\; \boldsymbol{b} = \begin{pmatrix} 0 \\ b \end{pmatrix}, b \in \mathbb{R} \right\}$
$\boldsymbol{w}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \in W_1, \boldsymbol{w}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \in W_2$ をとるとき，
$W_1 + W_2 \ni \boldsymbol{w}_1 + \boldsymbol{w}_2 = \begin{pmatrix} 1 \\ 1 \end{pmatrix} \notin W_1 \cup W_2$ ．

* 合併集合 $W_1 \cup W_2$ は，一般には，線型空間にならない（$(*)$ を満たさない）．


* $V = W_1 \oplus W_2 \iff \forall \boldsymbol{x} \in V$ について，$\boldsymbol{x} = \boldsymbol{x}_1 + \boldsymbol{x}_2, \boldsymbol{x}_1 \in W_1, \boldsymbol{x}_2 \in W_2$ と一意に表される（分解される）．



---

## p.2

### 線型空間の基底と次元



**基底**
$K$ 上の線型空間 $V \neq \{ \boldsymbol{0} \}$ の $l$ コのベクトル $\boldsymbol{a}_1, \cdots, \boldsymbol{a}_l$ について，
(1) $l$ コのベクトル $\boldsymbol{a}_1, \cdots, \boldsymbol{a}_l$ は1次独立
(2) 線型空間 $V$ の任意のベクトル $\boldsymbol{b} \in V$ は，$l$ コのベクトル $\boldsymbol{a}_1, \cdots, \boldsymbol{a}_l$ の1次結合で表すことができる（$(l+1)$ コのベクトル $\boldsymbol{a}_1, \cdots, \boldsymbol{a}_l, \boldsymbol{b}$ は1次従属）
を満たすとき，$l$ コのベクトル $\boldsymbol{a}_1, \cdots, \boldsymbol{a}_l$ の組を，線型空間 $V$ の基底といい，$\{ \boldsymbol{a}_1, \cdots, \boldsymbol{a}_l \}$ と表す．

* $V = \{ \boldsymbol{0} \}$ のときは，基底は存在しない．


* $n$ 次元数ベクトル空間 $K^n$ の $n$ コのベクトル $\boldsymbol{e}_1 = \begin{pmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}, \boldsymbol{e}_2 = \begin{pmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{pmatrix}, \cdots, \boldsymbol{e}_n = \begin{pmatrix} 0 \\ \vdots \\ 0 \\ 1 \end{pmatrix}$ は，$n$ 次元数ベクトル空間 $K^n$ の基底である．この $n$ コのベクトル $\boldsymbol{e}_1, \cdots, \boldsymbol{e}_n$ を，特に，$n$ 次元数ベクトル空間 $K^n$ の標準基底（単位ベクトル，基本ベクトル）という．
（例）$V = \mathbb{R}^2 \cdots \boldsymbol{e}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \boldsymbol{e}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \quad \to \mathbb{R}^2 \ni \forall \boldsymbol{x} = \begin{pmatrix} x \\ y \end{pmatrix} = x\boldsymbol{e}_1 + y\boldsymbol{e}_2$ ．
$V = \mathbb{R}^3 \cdots \boldsymbol{e}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \boldsymbol{e}_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \boldsymbol{e}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \to \mathbb{R}^3 \ni \forall \boldsymbol{x} = \begin{pmatrix} x \\ y \\ z \end{pmatrix} = x\boldsymbol{e}_1 + y\boldsymbol{e}_2 + z\boldsymbol{e}_3$ ．



必ずしも1次独立でない $m$ コのベクトル $\boldsymbol{x}_1, \cdots, \boldsymbol{x}_m \in V$ に対して，

$$\langle \boldsymbol{x}_1, \cdots, \boldsymbol{x}_m \rangle = K\boldsymbol{x}_1 + \cdots + K\boldsymbol{x}_m := \{ d_1 \boldsymbol{x}_1 + \cdots + d_m \boldsymbol{x}_m \mid \boldsymbol{x}_i \in V, d_i \in K, 1 \le i \le m \}$$


を，$m$ コのベクトル $\boldsymbol{x}_1, \cdots, \boldsymbol{x}_m$ によって張られた（生成された）部分空間という．$\{ \boldsymbol{a}_1, \cdots, \boldsymbol{a}_l \}$ が線型空間 $V$ の基底であるとき，$V = \langle \boldsymbol{a}_1, \cdots, \boldsymbol{a}_l \rangle$ と書くこともある．
（例）$\mathbb{R}^2 = \langle \boldsymbol{e}_1, \boldsymbol{e}_2 \rangle = \left\langle \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \end{pmatrix} \right\rangle = \left\langle \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 2 \\ 1 \end{pmatrix}, \begin{pmatrix} 3 \\ 3 \end{pmatrix} \right\rangle = \cdots$
実際，$\mathbb{R}^2 \ni \boldsymbol{x} = \begin{pmatrix} x \\ y \end{pmatrix} = x\boldsymbol{e}_1 + y\boldsymbol{e}_2$

$$\begin{aligned} &= \begin{pmatrix} x-y \\ 0 \end{pmatrix} + \begin{pmatrix} y \\ y \end{pmatrix} = (x-y)\begin{pmatrix} 1 \\ 0 \end{pmatrix} + y\begin{pmatrix} 1 \\ 1 \end{pmatrix} \\ &= \begin{pmatrix} x+y \\ 0 \end{pmatrix} + \begin{pmatrix} -4y \\ -2y \end{pmatrix} + \begin{pmatrix} 3y \\ 3y \end{pmatrix} = (x+y)\begin{pmatrix} 1 \\ 0 \end{pmatrix} + (-2y)\begin{pmatrix} 2 \\ 1 \end{pmatrix} + y\begin{pmatrix} 3 \\ 3 \end{pmatrix} . \end{aligned}$$

**基底と次元**
$K$ 上の線型空間 $V \neq \{ \boldsymbol{0} \}$ の基底の取り方は1通りではないが，基底の個数は一定である．この基底の個数を，線型空間 $V$ の次元といい，$\dim V$ と表す．

* $V = \{ \boldsymbol{0} \}$ のときは，$\dim V = 0$ とする．


* $\dim V = n$ であるとき，線型空間 $V$ を，$V^n$ と表すこともある．
（例）
$V = \mathbb{R}^2 \quad \cdots \text{標準基底 } \boldsymbol{e}_1, \boldsymbol{e}_2 \quad \to \dim \mathbb{R}^2 = 2$ ．
$V = M_{mn} \quad \cdots \text{行列単位 } E_{ij} = \begin{pmatrix} & \vdots & \\ \cdots & 1 & \cdots \\ & \vdots & \end{pmatrix} \begin{matrix} \\ \leftarrow i\text{行目} \\ \end{matrix} \quad \to \dim M_{mn} = mn$ ．（列の下に「$\uparrow j\text{列目}$」の注記あり）
$V = \langle 1, x, \cdots, x^n \rangle \cdots \text{基底 } a_i = x^{i-1} \quad \to \dim V = n+1$ ．



---

**行列の階数と次元**
$n$ 次元数ベクトル空間 $K^n$ の，必ずしも1次独立でない $l$ コのベクトル $\boldsymbol{x}_1, \cdots, \boldsymbol{x}_l$ に対して，$A = (\boldsymbol{x}_1 \cdots \boldsymbol{x}_l) \in M_{nl}$ とおくとき，$\operatorname{rank} A = \dim \langle \boldsymbol{x}_1, \cdots, \boldsymbol{x}_l \rangle$ ．

（例）$\boldsymbol{x}_1 = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}, \boldsymbol{x}_2 = \begin{pmatrix} 4 \\ 5 \\ 6 \end{pmatrix}, \boldsymbol{x}_3 = \begin{pmatrix} 7 \\ 8 \\ 9 \end{pmatrix}$
$A = \begin{pmatrix} 1 & 4 & 7 \\ 2 & 5 & 8 \\ 3 & 6 & 9 \end{pmatrix}$ とおくと，$A = \begin{pmatrix} 1 & 4 & 7 \\ 2 & 5 & 8 \\ 3 & 6 & 9 \end{pmatrix} \begin{matrix} \to \\ \times(-2) \\ \times(-3) \end{matrix} \to \begin{pmatrix} 1 & 4 & 7 \\ 0 & -3 & -6 \\ 0 & -6 & -12 \end{pmatrix} \begin{matrix} \\ \to \\ \times(-2) \end{matrix} \to \begin{pmatrix} \framebox{1} & 4 & 7 \\ 0 & \framebox{-3} & -6 \\ 0 & 0 & 0 \end{pmatrix}$ より，
$\operatorname{rank} A = 2$ ．一方，$\boldsymbol{x}_1$ と $\boldsymbol{x}_2$ とは1次独立，$\boldsymbol{x}_3 = -\boldsymbol{x}_1 + 2\boldsymbol{x}_2$ と書けるので，$\dim \langle \boldsymbol{x}_1, \boldsymbol{x}_2, \boldsymbol{x}_3 \rangle = 2$ ．

線型空間の基底と次元について，

$$\left. \begin{aligned} \dim V &= l \\ \boldsymbol{a}_1, \cdots, \boldsymbol{a}_l \in V &\text{ は1次独立} \end{aligned} \right\} \iff \{ \boldsymbol{a}_1, \cdots, \boldsymbol{a}_l \} \text{ は線型空間 } V \text{ の基底}$$


であるから，$K$ 上の線型空間 $V^n (\dim V = n < \infty)$ の部分空間 $W^l (\dim W = l \le n)$ の基底 $\{ \boldsymbol{a}_1, \cdots, \boldsymbol{a}_l \}$ に適当に $(n-l)$ コのベクトル $\boldsymbol{b}_{l+1}, \cdots, \boldsymbol{b}_n \in V$ を付け加えて，線型空間 $V$ の基底とすることができる．
（例）$V = \mathbb{R}^3, \quad V \supset W = \left\{ \begin{pmatrix} x \\ y \\ 0 \end{pmatrix} \;\middle\vert{}\; x, y \in \mathbb{R} \right\}$
$W$ の基底として，$\left\{ \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} \right\}$ を取る．このとき，$\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \in V$ を付け加えれば，$\left\{ \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \right\}$ は $V$ の基底である．

* $W_2 = \langle \boldsymbol{b}_{l+1}, \cdots, \boldsymbol{b}_n \rangle$ とおけば，$V = W \oplus W_2$ である．
（注）線型空間 $V$ が有限次元 $(\dim V < \infty)$ であるときに限る．



**次元公式**
$K$ 上の線型空間 $V$ の部分空間 $W_1, W_2 \ (\dim W_1 < \infty, \dim W_2 < \infty)$ に対して，

$$\dim(W_1 + W_2) + \dim(W_1 \cap W_2) = \dim W_1 + \dim W_2 .$$

（例）$V = \mathbb{R}^3, \quad W_1 = \left\{ \begin{pmatrix} x \\ y \\ z \end{pmatrix} \in \mathbb{R}^3 \;\middle\vert{}\; x+y+z=0 \right\}, W_2 = \left\{ \begin{pmatrix} x \\ y \\ z \end{pmatrix} \in \mathbb{R}^3 \;\middle\vert{}\; 2x+3y-z=0 \right\}$
$W_1 = \left\langle \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix} \right\rangle \to \dim W_1 = 2$ ，
$W_2 = \left\langle \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 3 \end{pmatrix} \right\rangle \to \dim W_2 = 2$ ，
$W_1 \cap W_2 = \left\{ \begin{pmatrix} x \\ y \\ z \end{pmatrix} \in \mathbb{R}^3 \;\middle\vert{}\; x+y+z=0, 2x+3y-z=0 \right\} = \left\langle \begin{pmatrix} 4 \\ -3 \\ -1 \end{pmatrix} \right\rangle \to \dim(W_1 \cap W_2) = 1$
より，$\dim(W_1 + W_2) = \dim W_1 + \dim W_2 - \dim(W_1 \cap W_2) = 3$ ．

$$\left( \dim(W_1 + W_2) = \operatorname{rank} \begin{pmatrix} 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ -1 & -1 & 2 & 3 \end{pmatrix} = \operatorname{rank} \begin{pmatrix} \framebox{1} & 0 & 1 & 0 \\ 0 & \framebox{1} & 0 & 1 \\ 0 & 0 & \framebox{3} & 4 \end{pmatrix} = 3 \right)$$

---

## p.3

### 線型写像



**写像**
2つの集合 $V, W$ について，集合 $V$ の各元 $v$ に対して，集合 $W$ の元 $w$ を一意的に結びつける対応関係を，集合 $V$ から $W$ への写像といい，

$$\begin{aligned} f &: V \to W \quad (V \xrightarrow{f} W) \\ f &: v \mapsto w \quad (v \stackrel{f}{\mapsto} w, \ w = f(v)) \end{aligned}$$


などと表す．集合 $V$ を，写像 $f$ の定義域という．特に，集合 $V$ から $V$ 自身への写像 $f : V \to V$ を，変換という．
[図: 集合 $V$ の元 $v_1, v_2, v_3$ から集合 $W$ の元 $w_1, w_2$ への写像 $f$ の対応図]

* 関数 $y = f(x)$ は，$\mathbb{R}$ から $\mathbb{R}$ への写像（変換）である．



**線型写像**
$K$ 上の線型空間 $V$ から $K$ 上の線型空間 $W$ への写像 $f : V \to W$ が，$\forall \boldsymbol{x}, \boldsymbol{y} \in V, \forall d, e \in K$ に対して

$$(*) \quad f(d\boldsymbol{x} + e\boldsymbol{y}) = df(\boldsymbol{x}) + ef(\boldsymbol{y})$$


を満たすとき，写像 $f$ を，線型空間 $V$ から $W$ への $K$ 上の線型写像（1次写像）という．

* 任意の $m \times n$ 型行列 $A_{mn} : K^n \to K^m$ は線型写像である．特に，任意の $n$ 次正方行列 $A_n : K^n \to K^n$ は線型変換（1次変換）である．


* 線型写像 $f : V \to W, \boldsymbol{0}_V \in V, \boldsymbol{0}_W \in W$ に対して，$f(\boldsymbol{0}_V) = \boldsymbol{0}_W$ である．


* 関数の微分，定積分，不定積分（ただし，積分定数 $C = 0$ とする）は線型写像である．



**像と核**
写像 $f$ によって定義域 $V$ の元 $v$ に対応する集合 $W$ の元 $w$ を，写像 $f$ による元 $v$ の像という．写像による元 $v$ の像の全体の集合を，写像 $f$ の像（値域）といい，

$$\operatorname{Im} f := f(V) = \{ w \mid w = f(v), v \in V \} \subseteq W$$


と表す．$\operatorname{Im} f = W$ のとき，写像 $f$ は全射（上への写像）である，という．
[図: 集合 $V$ から集合 $W$ 内の部分集合 $\operatorname{Im} f$ への写像 $f$ の図]

一方，集合 $W$ の元 $w$ に対して，

$$f^{-1}(w) := \{ v \mid w = f(v) \} \subseteq V$$


を，写像 $f$ による元 $w$ の逆像（方程式 $f(v) = w$ の一般解）という．
特に，元 $\boldsymbol{0}_W$ の逆像を，写像 $f$ の核（斉次方程式 $f(v) = \boldsymbol{0}_W$ の一般解）といい，

$$\operatorname{Ker} f := f^{-1}(\boldsymbol{0}_W) = \{ v \mid f(v) = \boldsymbol{0}_W \} \subseteq V$$


と表す．$v_1, v_2 \in V, v_1 \neq v_2 \Rightarrow f(v_1) \neq f(v_2) \ (f(v_1) = f(v_2) \Rightarrow v_1 = v_2)$ のとき，写像 $f$ は単射（1対1写像）である，という．
[図: 集合 $V$ の部分集合 $f^{-1}(w)$ と $\operatorname{Ker} f$ が集合 $W$ の元 $w$ と $\boldsymbol{0}_W$ にそれぞれ写る図]

---

* 写像 $f$ が全射かつ単射であるとき，写像 $f$ は全単射（双射）である，という．このとき，写像 $f$ の逆写像


$$f^{-1} : W \to V \quad (f^{-1} : w \mapsto v, \ v = f^{-1}(w))$$



がただ1つ存在し，逆写像 $f^{-1}$ もまた全単射である．
[図: 集合 $V$ の元 $v_1, v_2$ と集合 $W$ の元 $w_1, w_2$ の間の写像 $f$ と逆写像 $f^{-1}$ の1対1対応図]



（例）$V = \mathbb{R}, W = [0, \infty], w = f(v) = v^2$
[図: 放物線 $w = v^2$ のグラフ（$v_1, v_2$ に対して同じ $w_1$ をとる）]
・線型写像でない
・全射である
・単射でない

（例）$V = \mathbb{R}, W = \mathbb{R}, w = f(v) = \frac{1}{2}v$
[図: 直線 $w = \frac{1}{2}v$ のグラフ（$v_1$ と $w_1$ が1対1に対応する）]
・線型写像（変換）である
・全単射である
このとき，$v = f^{-1}(w) = 2w$

* 線型写像 $f : V \to W$ が全単射であるとき，写像 $f$ は，線型空間 $V$ から $W$ への同型写像という．このとき，線型空間 $V$ と $W$ とは同型である，といい，$V \simeq W$ と表す．


* 全単射な変換を，置換という．



**線型写像の像と核の性質**
$K$ 上の線型空間 $V$ から $W$ への線型写像 $f : V \to W$ について，
(i) 像 $\operatorname{Im} f = f(V)$ は線型空間 $W$ の部分空間である．（特に，写像 $f$ が全射 $\iff \operatorname{Im} f = W$．）
(ii) 核 $\operatorname{Ker} f = f^{-1}(\boldsymbol{0}_W)$ は線型空間 $V$ の部分空間である．特に，写像 $f$ が単射 $\iff \operatorname{Ker} f = \{ \boldsymbol{0}_V \}$．

線型空間 $V$ の基底 $\{ \boldsymbol{a}_1, \cdots, \boldsymbol{a}_n \}$ に対して，$n$ 次元数ベクトル空間 $K^n$ から線型空間 $V$ への写像 $f$ を，

$$\begin{aligned} f : K^n &\to V \\ \begin{pmatrix} d_1 \\ \vdots \\ d_n \end{pmatrix} &\mapsto \boldsymbol{v} = d_1 \boldsymbol{a}_1 + \cdots + d_n \boldsymbol{a}_n \end{aligned}$$


と定めれば，写像 $f$ は線型写像であり，全射である．また，線型独立の定義と線型写像の核の性質から，写像 $f$ は単射でもある．すなわち，写像 $f$ は同型写像である．したがって，次の性質が成り立っている：

**定理 8**
$K$ 上の線型空間 $V^n (\dim V = n < \infty)$ は，$n$ 次元数ベクトル空間 $K^n$ と同型である．

* 線型空間 $V$ の元 $\boldsymbol{v} = d_1 \boldsymbol{a}_1 + \cdots + d_n \boldsymbol{a}_n$ に対応した，$n$ 次元数ベクトル $\begin{pmatrix} d_1 \\ \vdots \\ d_n \end{pmatrix} \in K^n$ を，線型空間 $V$ の基底 $\{ \boldsymbol{a}_1, \cdots, \boldsymbol{a}_n \}$ に関する，元 $\boldsymbol{v}$ の座標（ベクトル）という．



線型空間は，次の4つの形で現れることが多い．
① $l$ コのベクトル $\boldsymbol{a}_1, \cdots, \boldsymbol{a}_l \in V$ が生成するベクトル空間 $\langle \boldsymbol{a}_1, \cdots, \boldsymbol{a}_l \rangle$
② 集合 $V$ から数の集合 $K$ への関数全体の集合 $\mathcal{F}(V, K)$
③④ 線型写像 $f$ の像 $\operatorname{Im} f$ と核 $\operatorname{Ker} f$

---

## p.4

### 線型写像としての行列



$K$ 上の線型空間 $V^n$ の基底 $\{ \boldsymbol{a}_1, \cdots, \boldsymbol{a}_n \}$，$K$ 上の線型空間 $W^m$ の基底 $\{ \boldsymbol{b}_1, \cdots, \boldsymbol{b}_m \}$ を取る $(m, n < \infty)$．線型空間 $V^n$ から $W^m$ への線型写像 $f : V^n \to W^m$ の全体の集合を $\mathcal{L}_K(V^n, W^m)$ とおくとき，

[図: $V^n \xrightarrow{f} W^m$ と $K^n \xrightarrow{A} K^m$ の間の基底と座標ベクトルによる可換図式：
上段は $(\boldsymbol{a}_1 \cdots \boldsymbol{a}_n)\begin{pmatrix} d_1 \\ \vdots \\ d_n \end{pmatrix} = d_1 \boldsymbol{a}_1 + \cdots + d_n \boldsymbol{a}_n = \boldsymbol{v} \in V^n$ が $f$ により $(f(\boldsymbol{a}_1) \cdots f(\boldsymbol{a}_n))\begin{pmatrix} d_1 \\ \vdots \\ d_n \end{pmatrix} = (\boldsymbol{b}_1 \cdots \boldsymbol{b}_m)A\begin{pmatrix} d_1 \\ \vdots \\ d_n \end{pmatrix} = f(\boldsymbol{v}) = d_1 f(\boldsymbol{a}_1) + \cdots + d_n f(\boldsymbol{a}_n) = \boldsymbol{w} = e_1 \boldsymbol{b}_1 + \cdots + e_m \boldsymbol{b}_m = (\boldsymbol{b}_1 \cdots \boldsymbol{b}_m)\begin{pmatrix} e_1 \\ \vdots \\ e_m \end{pmatrix} \in W^m$ に写り，下段は $K^n$ の元 $\begin{pmatrix} d_1 \\ \vdots \\ d_n \end{pmatrix}$ が $A$ により $K^m$ の元 $\begin{pmatrix} e_1 \\ \vdots \\ e_m \end{pmatrix} = A\begin{pmatrix} d_1 \\ \vdots \\ d_n \end{pmatrix}$ に写る図]

$$(*) \quad f : (\boldsymbol{a}_1 \cdots \boldsymbol{a}_n) \mapsto (f(\boldsymbol{a}_1) \cdots f(\boldsymbol{a}_n)) = (\boldsymbol{b}_1 \cdots \boldsymbol{b}_m)A$$


を満たす様に定めることにより，次の定理を得る：

**定理 9**
$\mathcal{L}_K(V^n, W^m) \simeq M_{mn}$ である．すなわち，線型写像 $f_A$ は，行列 $A_f$ に置き換えることができる．

* $(*)$ で定められる線型写像 $f$ を，行列 $A$ によって定義される線型写像 $f_A$ といい，行列 $A$ を，線型空間 $V^n$ の基底 $\{ \boldsymbol{a}_1, \cdots, \boldsymbol{a}_n \}$ と線型空間 $W^m$ の基底 $\{ \boldsymbol{b}_1, \cdots, \boldsymbol{b}_m \}$ に関する，線型写像 $f$ の表現行列（行列表示）$A_f$ という．



線型代数学とは，線型空間 $V^n$ 上の線型写像 $f_A$ についての学問である．定理8，定理9より，線型代数学とは，$n$ 次元数ベクトル空間 $K^n$ 上の $m \times n$ 型行列 $A_f$ についての学問であるといえる．

線型写像 $f : V^n \to W^m$ の像 $\operatorname{Im} f$ の次元 $\dim(\operatorname{Im} f)$ を，線型写像 $f$ の階数といい，$\operatorname{rank} f$ と表す．また，核 $\operatorname{Ker} f$ の次元 $\dim(\operatorname{Ker} f)$ を，線型写像 $f$ の退化次数という．線型写像 $f$ の表現行列を $A_f = (\boldsymbol{a}_1 \cdots \boldsymbol{a}_n) \ (\boldsymbol{a}_i \in K^m, 1 \le i \le n)$ とおくと，線型空間 $V^n, W^m$ の標準基底に対して，$\boldsymbol{a}_i = A_f(\boldsymbol{e}_i) = f(\boldsymbol{e}_i) \ (1 \le i \le n)$ であるので，

$$\begin{aligned}
A_f : K^n &\longrightarrow K^m \\
\boldsymbol{x} = \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} &\longmapsto \boldsymbol{y} = \begin{pmatrix} y_1 \\ \vdots \\ y_m \end{pmatrix} = A_f \boldsymbol{x} = (\boldsymbol{a}_1 \cdots \boldsymbol{a}_n)\begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}
\end{aligned}$$

$$\operatorname{Im} f = \langle \boldsymbol{a}_1, \cdots, \boldsymbol{a}_n \rangle$$


である．したがって，$\dim(\operatorname{Im} f) = \operatorname{rank} A_f$ となる．このとき，以下の性質が成り立っている：

**線型写像の階数**
$\operatorname{rank} f := \dim(\operatorname{Im} f) = \operatorname{rank} A_f$ である．特に，
(i) $f$ は全射 $\iff W^m = \langle \boldsymbol{a}_1, \cdots, \boldsymbol{a}_n \rangle, \ \operatorname{rank} A_f = m \ (\le n)$
(ii) $f$ は単射 $\iff \boldsymbol{a}_1, \cdots, \boldsymbol{a}_n$ は線型独立，$\operatorname{rank} A_f = n \ (\le m)$
$\iff$ 斉次連立一次方程式 $A_f \boldsymbol{x} = \boldsymbol{0}_m$ の解は，$\boldsymbol{x} = \boldsymbol{0}_n$ のみ
(iii) $f$ は全単射 $\iff \operatorname{rank} A_f = m = n$
$\iff \det A_f \neq 0$

---

**次元定理**
$K$ 上の線型空間 $V \ (\dim V < \infty)$ から $W$ への線型写像 $f : V \to W$ について，

$$\dim V = \dim(\operatorname{Im} f) + \dim(\operatorname{Ker} f)$$

* 線型写像 $f : V^n \to W^m \ (\dim V = n < \infty, \dim W = m < \infty)$ の表現行列 $A_f$ について，$\operatorname{rank} A_f = r$ のとき，$\dim(\operatorname{Ker} f) = \dim V - \dim(\operatorname{Im} f) = n - r$ ．すなわち，斉次連立一次方程式 $A_f \boldsymbol{x} = \boldsymbol{0}_m$ の一般解 $\operatorname{Ker} f = \{ \boldsymbol{x} \in K^n \mid A_f \boldsymbol{x} = \boldsymbol{0}_m \}$ は，$K^n$ の $(n-r)$ 次元部分空間であり，$(n-r)$ コの基本解を持つ（$(n-r)$ コのパラメータを持つ）．



（例）$V = \mathbb{R}^3, W = \mathbb{R}^3, f : \begin{pmatrix} x \\ y \\ z \end{pmatrix} \longmapsto \begin{pmatrix} X \\ Y \\ Z \end{pmatrix} = \begin{pmatrix} x+y-z \\ 4x+y-2z \\ 2x-y \end{pmatrix}$
線型写像 $f$ の表現行列 $A_f = \begin{pmatrix} 1 & 1 & -1 \\ 4 & 1 & -2 \\ 2 & -1 & 0 \end{pmatrix}$ より，$\dim(\operatorname{Im} f) = \operatorname{rank} A_f = \operatorname{rank} \begin{pmatrix} \framebox{1} & 1 & -1 \\ 0 & \framebox{-3} & 2 \\ 0 & 0 & 0 \end{pmatrix} = 2$ ．
実際，

$$\begin{cases} x+y-z = X \\ 4x+y-2z = Y \\ 2x-y = Z \end{cases} \qquad \begin{cases} 3x \quad -z = -X+Y \\ \quad -3y+2z = -4X+Y \\ \qquad \framebox{$0 = 2X-Y+Z$} \end{cases}$$

$$\left(\begin{array}{ccc|ccc} 1 & 1 & -1 & 1 & 0 & 0 \\ 4 & 1 & -2 & 0 & 1 & 0 \\ 2 & -1 & 0 & 0 & 0 & 1 \end{array}\right) \begin{matrix} \to \\ \times(-4) \\ \times(-2) \end{matrix} \to \left(\begin{array}{ccc|ccc} 1 & 1 & -1 & 1 & 0 & 0 \\ 0 & -3 & 2 & -4 & 1 & 0 \\ 0 & -3 & 2 & -2 & 0 & 1 \end{array}\right) \begin{matrix} \times\left(\frac{1}{3}\right) \\ \to \\ \times(-1) \end{matrix} \to \left(\begin{array}{ccc|ccc} 1 & 0 & -\frac{1}{3} & -\frac{1}{3} & \frac{1}{3} & 0 \\ 0 & -3 & 2 & -4 & 1 & 0 \\ 0 & 0 & 0 & 2 & -1 & 1 \end{array}\right) \begin{matrix} \times 3 \\ \\ \\ \end{matrix} \to \left(\begin{array}{ccc|ccc} 3 & 0 & -1 & -1 & 1 & 0 \\ 0 & -3 & 2 & -4 & 1 & 0 \\ 0 & 0 & 0 & 2 & -1 & 1 \end{array}\right)$$


であるから，$\operatorname{Im} f = \left\{ \begin{pmatrix} X \\ Y \\ Z \end{pmatrix} \;\middle|\; 2X - Y + Z = 0 \right\}$（2次元平面）．
また，次元定理より，$\dim(\operatorname{Ker} f) = \dim V - \operatorname{rank} A_f = 3 - 2 = 1$ ．実際，

$$\begin{cases} x+y-z = 0 \\ 4x+y-2z = 0 \\ 2x-y = 0 \end{cases} \to \begin{cases} 3x \quad -z = 0 \\ \quad -3y+2z = 0 \\ \qquad 0 = 0 \end{cases} \text{ より，} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = t\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} \ (t \in \mathbb{R}) \text{ であるから，}$$


$\operatorname{Ker} f = \left\{ \begin{pmatrix} x \\ y \\ z \end{pmatrix} \;\middle|\; \frac{x}{1} = \frac{y}{2} = \frac{z}{3} \right\}$（1次元直線）．
$\dim V = 3 \neq \operatorname{rank} A_f = 2 \neq 3 = \dim W$ であるから，線型写像 $f$ は全射でも単射でも全単射でもない．

（別解）$\operatorname{rank} A_f = 2$ より，$\dim(\operatorname{Im} f) = \operatorname{rank} A_f = 2$ ，$\operatorname{Im} f = \left\langle \begin{pmatrix} 1 \\ 4 \\ 2 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix}, \begin{pmatrix} -1 \\ -2 \\ 0 \end{pmatrix} \right\rangle = \left\langle \begin{pmatrix} 1 \\ 4 \\ 2 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix} \right\rangle$ ．
次元定理より，$\dim(\operatorname{Ker} f) = \dim V - \operatorname{rank} A_f = 1$ ，$\operatorname{Ker} f = \left\langle \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} \right\rangle$ ．

---

## p.5

### 合成写像および逆写像の表現行列



線型写像 $f, g$ の表現行列を，それぞれ $A_f, B_g$ とする．線型写像 $f$ と $g$ の合成写像 $g \circ f$ について，以下の定理が成り立っている：

[図: $U \xrightarrow{f} V \xrightarrow{g} W$（上部に合成写像 $g \circ f$ の矢印）と $K^n \xrightarrow{A_f} K^m \xrightarrow{B_g} K^l$ の対応図：
$\begin{pmatrix} u_1 \\ \vdots \\ u_n \end{pmatrix} \longmapsto \begin{pmatrix} v_1 \\ \vdots \\ v_m \end{pmatrix} = A_f \begin{pmatrix} u_1 \\ \vdots \\ u_n \end{pmatrix} \longmapsto \begin{pmatrix} w_1 \\ \vdots \\ w_l \end{pmatrix} = B_g \begin{pmatrix} v_1 \\ \vdots \\ v_m \end{pmatrix} = \underset{A_{g \circ f}}{\underline{B_g A_f}} \begin{pmatrix} u_1 \\ \vdots \\ u_n \end{pmatrix}$]

**合成写像の表現行列**

$$A_{g \circ f} = B_g A_f$$


である．特に，線型写像 $f$ が全単射（同型写像）であるとき，

$$A_{f^{-1}} = A_f^{-1} .$$

[図: $U \underset{f^{-1}}{\overset{f}{\rightleftarrows}} V$ と $K^n \underset{A_{f^{-1}}}{\overset{A_f}{\rightleftarrows}} K^m$ の対応図：
$\begin{pmatrix} u_1 \\ \vdots \\ u_n \end{pmatrix} \longleftrightarrow \begin{pmatrix} v_1 \\ \vdots \\ v_m \end{pmatrix} = A_f \begin{pmatrix} u_1 \\ \vdots \\ u_n \end{pmatrix}$，左下に $\begin{pmatrix} u_1 \\ \vdots \\ u_n \end{pmatrix} = A_{f^{-1}}\begin{pmatrix} v_1 \\ \vdots \\ v_m \end{pmatrix} = \underset{E}{\underline{A_{f^{-1}} A_f}}\begin{pmatrix} u_1 \\ \vdots \\ u_n \end{pmatrix}$]

（例）$A_f = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \ B_g = \begin{pmatrix} 3 & 1 \\ 4 & 2 \\ 5 & 0 \end{pmatrix}$

$$\begin{aligned}
A_{g \circ f} &= B_g A_f = \begin{pmatrix} 3 & 1 \\ 4 & 2 \\ 5 & 0 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix} 6 & 10 \\ 10 & 16 \\ 5 & 10 \end{pmatrix} , \\
A_{f^{-1}} &= A_f^{-1} = \frac{1}{-2} \begin{pmatrix} 4 & -2 \\ -3 & 1 \end{pmatrix} = \begin{pmatrix} -2 & 1 \\ \frac{3}{2} & -\frac{1}{2} \end{pmatrix} .
\end{aligned}$$

---

### いろいろな線型写像



$\mathbb{R}^2$ から $\mathbb{R}^2$ への線型写像（線型変換）には，以下の様なものがある：

1. 折り返し行列
1.1 $x$ 軸に関する折り返し（$x$ 軸に関して対称移動）


$$A_x = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$



1.2 $y$ 軸に関する折り返し（$y$ 軸に関して対称移動）


$$A_y = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$$



1.3 $x$ 軸に関して折り返して $y$ 軸に関して折り返し（原点に関して対称移動）


$$A_0 = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = A_x A_y = A_y A_x$$



[図: $xy$ 平面上の点 $\begin{pmatrix} x \\ y \end{pmatrix}$ が，$A_x$ で $\begin{pmatrix} x \\ -y \end{pmatrix}$，$A_y$ で $\begin{pmatrix} -x \\ y \end{pmatrix}$，$A_0$ で $\begin{pmatrix} -x \\ -y \end{pmatrix}$ にそれぞれ移動する図]


1.4 直線 $y = ax$ に関する折り返し（直線 $y = ax$ に関して対称移動）


$$L = \begin{pmatrix} \frac{1-a^2}{1+a^2} & \frac{2a}{1+a^2} \\ \frac{2a}{1+a^2} & \frac{a^2-1}{1+a^2} \end{pmatrix}$$



[図: $xy$ 平面上の直線 $y = ax$ に関して，点 $\begin{pmatrix} x \\ y \end{pmatrix}$ が点 $\begin{pmatrix} X \\ Y \end{pmatrix}$ に対称移動する図]


2. 回転行列
原点を中心に反時計回りに $\theta$ 回転


$$R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$


* 直線 $y = (\tan\theta)x$ に関する折り返しは


$$L = \begin{pmatrix} \cos 2\theta & \sin 2\theta \\ \sin 2\theta & -\cos 2\theta \end{pmatrix} = R_\theta A_x R_{-\theta}$$



と表すこともできる．
[図: $xy$ 平面上で原点からの角度 $\alpha$ の点 $\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} r\cos\alpha \\ r\sin\alpha \end{pmatrix}$ が，角度 $\theta$ 回転して $\begin{pmatrix} X \\ Y \end{pmatrix} = \begin{pmatrix} r\cos(\theta+\alpha) \\ r\sin(\theta+\alpha) \end{pmatrix}$ に移動する図]




3. 拡大行列
$x$ 方向に $a$ 倍，$y$ 方向に $b$ 倍


$$A_e = \begin{pmatrix} a & 0 \\ 0 & b \end{pmatrix}$$



[図: $xy$ 平面上の点 $(x, y)$ が，横方向に $\times a$，縦方向に $\times b$ されて点 $\begin{pmatrix} ax \\ by \end{pmatrix}$ に移動する図]
