<!-- Gemini transcript p.20; verify against page image -->

## p.20

**【例 3】** 1 つのサイコロを 5 回投げる時，3 の倍数の目がちょうど 2 回出る確率は？
全事象 $\Omega = \{(1, 1, 1, 1, 1), (1, 1, 1, 1, 2), \dots, (6, 6, 6, 6, 5), (6, 6, 6, 6, 6)\} \cdots n(\Omega) = 6^5$.
3 の倍数の目がちょうど 2 回でる事象を $A$ とおく．$i, j$ 回目が 3 の倍数，それ以外は 3 の倍数でない目が出る事象を $A_{ij}$ とおく．例えば，

$$\begin{aligned} A_{12} = \{&(3, 3, 1, 1, 1), (3, 3, 1, 1, 2), (3, 3, 1, 1, 4), \dots, (3, 3, 5, 5, 5), \\ &(3, 6, 1, 1, 1), (3, 6, 1, 1, 2), (3, 6, 1, 1, 4), \dots, (3, 6, 5, 5, 5), \\ &(6, 3, 1, 1, 1), (6, 3, 1, 1, 2), (6, 3, 1, 1, 4), \dots, (6, 3, 5, 5, 5), \\ &(6, 6, 1, 1, 1), (6, 6, 1, 1, 2), (6, 6, 1, 1, 4), \dots, (6, 6, 5, 5, 5)\} \end{aligned}$$


この時，

* どの $1 \le i < j \le 5$ についても，$n(A_{ij}) = 2^2 \cdot 4^3$


* $1 \le i < j \le 5$ となる $\{i, j\}$ の個数（何回目に 3 の倍数が出るかの場合の数）は，${}_5\text{C}_2$



$$\begin{aligned} \text{よって，}\qquad n(A) &= \sum_{1 \le i < j \le 5} n(A_{ij}) = {}_5\text{C}_2 \cdot 2^2 \cdot 4^3 \\ \text{であるから，求める確率は，}\qquad \frac{n(A)}{n(\Omega)} &= {}_5\text{C}_2 \cdot \frac{2^2 \cdot 4^3}{6^5} = {}_5\text{C}_2 \cdot \left( \frac{2}{6} \right)^2 \cdot \left( \frac{4}{6} \right)^3 = \frac{80}{243} \end{aligned}$$



**観察**：$p = \frac{1}{3}$，即ち，1 回サイコロを振った時に 3 の倍数が出る確率とすると，

$${}_5\text{C}_2 \cdot \left( \frac{2}{6} \right)^2 \cdot \left( \frac{4}{6} \right)^3 = {}_5\text{C}_2 \cdot p^2 \cdot (1 - p)^3$$



**定理 1.2: 反復試行の確率**
1 回の試行において事象 $A$ の確率が $p$ である時，$n$ 回の反復試行において，事象「$A$ がちょうど $k$ 回起こる」の確率は

$${}_n\text{C}_k \cdot p^k \cdot (1 - p)^{n-k}$$



**【演習 2】** 1 枚の硬貨を 5 回投げる時，表がちょうど 3 回出る確率を求めよ．
{{手書き: 

$${}_5\text{C}_3 \cdot \left( \frac{1}{2} \right)^3 \times \left( \frac{1}{2} \right)^2 = \frac{5 \times \overset{2}{\not{4}} \times \not{3}}{\not{3} \times \not{2} \times 1} = 10 \times \frac{1}{2^3} \times \frac{1}{2^2} = \frac{1}{2^4 \times \not{2}} \times \overset{5}{\not{10}} = \underline{\frac{5}{2^4}}$$

}}

**【演習 3】** ある工場で製造される製品は，1 個につき独立に確率 0.2 で不良品となる．7 個の製品を製造したとき，次の確率を求めよ．

(1) 不良品がちょうど 3 個となる確率．
{{手書き: 

$${}_7\text{C}_3 \cdot 0.2^3 \cdot 0.8^4 = \frac{7 \times \not{6} \times 5}{\not{3 \times 2} \times 1} \times \frac{1}{5^3} \times \frac{4^4}{5^4} = \underline{\frac{7 \times 4^4}{5^6}}$$

}}

(2) 不良品が 3 個以下となる確率．
{{手書き: 

$$\begin{aligned} & {}_7\text{C}_3 \cdot 0.2^3 \times 0.8^4 + {}_7\text{C}_2 \cdot 0.2^2 \times 0.8^5 + {}_7\text{C}_1 \cdot 0.2^1 \times 0.8^6 = \text{[判読不能（塗りつぶし）]} \\ &= \frac{7 \times 4^4}{5^6} + 21 \times \frac{1}{5^2} \times \frac{4^5}{5^5} = \frac{3 \times 4^5 \times 7}{5^7} + 7 \times \frac{1}{5} \times \frac{4^6}{5^6} = \frac{7 \times 4^6}{5^7} = \frac{7 \times 4^4 \times 5 + 3 \times 4^5 \times 7 + 7 \times 4^6}{5^7} \\ &\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad = \frac{7 \times 4^4 (5 + 3 \times 4 + 4^2)}{5^7} \\ &\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad = \frac{7 \times 4^4 (33)}{5^7} \qquad \begin{aligned} 12 + 16 + 5 \\ 61 \end{aligned} \end{aligned}$$

}}

2
