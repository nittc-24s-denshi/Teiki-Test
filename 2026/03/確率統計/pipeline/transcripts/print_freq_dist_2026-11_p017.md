<!-- Gemini transcript p.17; verify against page image -->

## p.17

### [ 3 ] 確率の性質



$\Omega$ が有限であることを仮定していたことを思い出そう．確率は以下の基本原理（実は定義）を満たす：

**【定理 1】**

$$\begin{aligned} &(1)\ 0 \le P(A) \le 1 && (3)\ P(A \cup B) = P(A) + P(B) - P(A \cap B) \\ &(2)\ P(\emptyset) = 0, P(\Omega) = 1 && \quad \bullet \text{ 特に，$A$ と $B$ が排反 ($A \cap B = \emptyset$) の時，} \\ &(3)\ P(A) + P(\overline{A}) = 1 && \qquad P(A \cup B) = P(A) + P(B) \end{aligned}$$



**【例 3】** [例題 3.2] 1 から 100 までの数字が書かれた 100 枚のカードから 1 枚のカードを引く時，

* $A \cdots$ 引いたカードの数字が 3 の倍数である事象


* $B \cdots$ 引いたカードの数字が 5 の倍数である事象



とする．$n(\Omega) = 100$ である．以下の事象の確率を求めよう．

(1) $A \cdots n(A) = n(\{3k \mid 1 \le k \le 33\}) = 33$ より，$P(A) = \frac{33}{100}$

(2) $B \cdots n(B) = n(\{5k \mid 1 \le k \le 20\}) = 20$ より，$P(B) = \frac{20}{100} = \frac{1}{5}$

(3) $A \cap B \cdots$ これは 3 の倍数かつ 5 の倍数である事象，即ち 15 の倍数である事象だから，$n(A \cap B) = n(\{15k \mid 1 \le k \le 6\}) = 6$ より，$P(A \cap B) = \frac{6}{100} = \frac{3}{50}$．

(4) $A \cup B \cdots 3$ の倍数または 5 の倍数... これは数えづらい！性質を使おう．

$$P(A \cup B) = P(A) + P(B) - P(A \cap B) = \frac{33 + 20 - 6}{100} = \frac{47}{100}$$



(5) $\overline{A \cup B} \cdots$ 「3 の倍数または 5 の倍数」でない，即ち 3 の倍数でも 5 の倍数でもない事象... やはり数えづらいので性質を使おう．

$$P(\overline{A \cup B}) = 1 - P(A \cup B) = \frac{100 - 47}{100} = \frac{53}{100}.$$



**【演習 3】** [問 3.4] 1 から 8 までの数字が書かれた 8 枚のカードから 2 枚を同時に取り出すとき，取り出した 2 枚のカードの数の積が奇数となる事象を $A$，取り出した 2 枚のカードの数の和が 6 の倍数となる事象を $B$ とする．次の確率を求めよ：

(1) $A$ {{手書き: $= \{1, 3, 5, 7\}^2$}}
{{手書き: 

$$\begin{aligned} n(A) &= {}_4\text{C}_2 = 6 \\ n(\Omega) &= {}_8\text{C}_2 = 28 \\ P(A) &= \frac{6}{28} = \frac{3}{14} \end{aligned}$$

}}

(2) $B$ {{手書き: $= \{\{1, 5\}, \{2, 4\}, \{4, 8\}, \{5, 7\}\}$}}
{{手書き: 

$$\begin{aligned} n(B) &= 4 \\ P(B) &= \frac{4}{28} = \frac{1}{7} \end{aligned}$$

}}

(3) $A \cap B$ {{手書き: $= \{\{1, 5\}, \{5, 7\}\}$}}
{{手書き: 

$$\begin{aligned} n(A \cap B) &= 2 \\ P(A \cap B) &= \frac{2}{28} = \frac{1}{14} \end{aligned}$$

}}

(4) $A \cup B$ {{手書き: $=$}}
{{手書き: 

$$\begin{aligned} P(A \cup B) &= P(A) + P(B) - P(A \cap B) \\ &= \frac{3}{14} + \frac{2}{14} - \frac{1}{14} = \frac{4}{14} = \frac{2}{7} \end{aligned}$$

}}

(5) $\overline{A \cup B}$ {{手書き: $= \overline{A} \cap \overline{B}$}}
{{手書き: 

$$1 - \frac{2}{7} = \frac{5}{7}$$

}}

3

---
