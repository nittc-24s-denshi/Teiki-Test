<!-- Gemini transcript p.10; verify against page image -->

## p.10

### [ 3 ] 一次変換の平均・分散・標準偏差



変数 $X$ が $x_1, \dots, x_n$ の時，$f(x_1), \dots, f(x_n)$ をとる変数を $f(X)$ とかく．特に，$a, b$ を定数とするとき，変数 $aX + b$ のとる値は $ax_1 + b, \dots, ax_n + b$ である．
変数 $X$ の平均，分散，標準偏差をそれぞれ $\bar{x}, v_x, s_x$ とすると一次変換 $Y = aX + b\ (y_1, \dots, y_n)$ について次が成り立つ：

$$\begin{aligned} \text{平均：}\quad \bar{y} &= a\bar{x} + b, \tag{4} \\ \text{分散：}\quad v_y &= a^2 v_x, \tag{5} \\ \text{標準偏差：}\quad s_y &= \vert{}a\vert{} s_x. \tag{6} \end{aligned}$$



すなわち，すべてのデータに同じ値 $b$ を加えても分散・標準偏差は変化せず，すべてのデータを $a$ 倍すると，分散は $a^2$ 倍，標準偏差は $\vert{}a\vert{}$ 倍になる．

*Proof.*

**平均**

$$\begin{aligned} \bar{y} &= \frac{1}{n} \sum_{i=1}^{n} (ax_i + b) \\ &= a \frac{1}{n} \sum_{i=1}^{n} x_i + b \\ &= a\bar{x} + b. \end{aligned}$$



**分散**

$$\begin{aligned} v_y &= \frac{1}{n} \sum_{i=1}^{n} \{(ax_i + b) - (a\bar{x} + b)\}^2 \\ &= \frac{1}{n} \sum_{i=1}^{n} \{a(x_i - \bar{x})\}^2 \\ &= a^2 \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2 \\ &= a^2 v_x. \end{aligned}$$



**標準偏差**

$$\begin{aligned} s_y &= \sqrt{v_y} \\ &= \sqrt{a^2 v_x} \\ &= \vert{}a\vert{} \sqrt{v_x} \\ &= \vert{}a\vert{} s_x. \end{aligned}$$


$\square$

変数 $X$ の平均を $\bar{x}$，標準偏差を $s_x$ とおく．

**【例 3】**

$$Z = \frac{X - \bar{x}}{s_x}$$


とした時，平均 $Z$ の平均 $\bar{z}$ は $0$，標準偏差 $s_z$ は $1$ となる．この変換を**標準化**という．

**【演習 3】** 次の変数を**偏差値**という．

$$T = 50 + 10 \cdot \frac{X - \bar{x}}{s_x}$$


偏差値の平均 $\bar{t}$，標準偏差 $s_t$ を求めよ．また，平均点が 68 点，標準偏差が 12 点の試験で 74 点を取った時の偏差値を求めよ．

{{手書き: 

$$\begin{aligned} \bar{t} &= 50 \\ s_t &= 10 \end{aligned} \qquad \frac{74 - 68}{12} = 0.5$$

}}

{{手書き: 

$$50 + 10 \times 0.5 = \underline{55}$$

}}

4
