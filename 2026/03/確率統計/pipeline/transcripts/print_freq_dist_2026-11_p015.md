<!-- Gemini transcript p.15; verify against page image -->

## p.15

# 確率統計 I 第4回



# 確率



### [ 1 ] 事象と試行



試行・事象などの言葉を以下のように使う．また，事象・全事象は集合で表すことができるのでそれも併記する．

**試行** サイコロを投げて出た目を調べる．
**事象**「素数の目が出た」$\rightarrow \{2, 3, 5\}$，「3 が出た」$\rightarrow \{3\}$, etc...
**根元事象**「1 が出た」$\rightarrow \{1\}$，「2 が出た」$\rightarrow \{2\}$, etc...
**全事象**「1 から 6 までの値が出た」$\rightarrow \{1, 2, 3, 4, 5, 6\}$
**試行** 3 枚のコインを投げて，出た面を調べる．（表 $\rightarrow \text{H}$，裏 $\rightarrow \text{T}$）
**事象**「全て表が出た」$\rightarrow \{(\text{H}, \text{H}, \text{H})\}$，「裏がちょうど 1 回」$\rightarrow \{(\text{H}, \text{H}, \text{T}), (\text{H}, \text{T}, \text{H}), (\text{T}, \text{H}, \text{H})\}$, etc...
**根元事象**「表，表，裏の順に出た」$\rightarrow \{(\text{H}, \text{H}, \text{T})\}$, etc...
**全事象** $\{(\text{H}, \text{H}, \text{H}), (\text{H}, \text{H}, \text{T}), (\text{H}, \text{T}, \text{H}), (\text{H}, \text{T}, \text{T}), (\text{T}, \text{H}, \text{H}), (\text{T}, \text{H}, \text{T}), (\text{T}, \text{T}, \text{H}), (\text{T}, \text{T}, \text{T})\}$

即ち，

**試行** ・・・観測や実験
**事象** ・・・試行によって起こる結果の集まり
**根元事象** ・・・一つの結果だけからなる事象
**全事象** ・・・起こりうる全ての結果を集めた事象

また，要素を持たない事象 $\emptyset$ を**空事象**という．
今回，全事象が有限であるものを扱う．よって，扱う全ての事象は有限集合とみなせる．
$\Omega$ を全事象とする．事象 $A, B \subset \Omega$ について，

**積事象**： $A \cap B = \{x \mid x \in A \text{ かつ } x \in B\}$.
**和事象**： $A \cup B = \{x \mid x \in A \text{ または } x \in B\}$.
**余事象**： $A^c = \{x \in \Omega \mid x \notin A\}$.
**$A$ と $B$ は排反**： $\Longleftrightarrow A \cap B = \emptyset$，即ち，$A$ と $B$ は同時に起こり得ない．
**事象 $A$ の要素数**： $n(A)$

**【例 1】** サイコロを投げる試行について，

* $A$ を 出目が 3 以上である事象，


* $B$ を 出目が素数である事象とする．



この時，集合の外延的記法で表すと，$A = \{3, 4, 5, 6\}, B = \{2, 3, 5\}$ である．またこの時，

**全事象** $\Omega = \{1, 2, 3, 4, 5, 6\}$.
**$A$ と $B$ の積事象** $A \cap B = \{3, 5\}$.
**$A$ と $B$ の和事象** $A \cup B = \{2, 3, 4, 5, 6\}$.
**$A$ の余事象** $\overline{A} = \{1, 2\}$.
**排反事象の例** $\{1, 3, 4\}$ と $\{2, 6\}$.
**$A$ の要素数** $n(A) = n(\{3, 4, 5, 6\}) = 4$.

1
