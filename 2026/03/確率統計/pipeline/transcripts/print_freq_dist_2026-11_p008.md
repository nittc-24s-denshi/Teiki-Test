<!-- Gemini transcript p.8; verify against page image -->

## p.8

平均は

$$\bar{x} = {{手書き: 6}}$$


である．
各値について，平均との差およびその 2 乗を求め，次の表を完成させよ．

| $x_i$ | $f_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ | $f_i(x_i - \bar{x})^2$ |
| --- | --- | --- | --- | --- |
| 3 | 1 | {{手書き: $-3$}} | {{手書き: 9}} | {{手書き: 9}} |
| 5 | 3 | {{手書き: $-1$}} | {{手書き: 1}} | {{手書き: 3}} |
| 6 | 2 | {{手書き: 0}} | {{手書き: 0}} | {{手書き: 0}} |
| 8 | 1 | {{手書き: 2}} | {{手書き: 4}} | {{手書き: 4}} |
| 10 | 1 | {{手書き: 4}} | {{手書き: 16}} | {{手書き: 16}} |
| 計 | 8 | {{手書き: 2}} | {{手書き: 30}} | {{手書き: 32}} |

よって，

$$\begin{aligned} \text{レンジ：}\quad & {{手書き: 7}} \\ \text{分散：}\quad & {{手書き: 4}} \\ \text{標準偏差：}\quad & {{手書き: 2}} \end{aligned}$$



### [ 2 ] 分散と平均の関係



データ $x_1, \dots, x_n$ の平均 $\bar{x}$ と分散 $v_x$ には次の関係がある：

$$v_x = \frac{1}{n} \sum_{i=1}^{n} x_i^2 - \bar{x}^2 \tag{1}$$


即ち，

$$(\text{分散}) = (\text{2 乗の平均}) - (\text{平均の 2 乗}) \tag{2}$$



*Proof.*

$$\begin{aligned} v_x &= \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2 \\ &= \frac{1}{n} \sum_{i=1}^{n} (x_i^2 - 2x_i\bar{x} + \bar{x}^2) \\ &= \frac{1}{n} \sum_{i=1}^{n} x_i^2 - \frac{1}{n} \sum_{i=1}^{n} 2x_i\bar{x} + \frac{1}{n} \sum_{i=1}^{n} \bar{x}^2 \\ &= \frac{1}{n} \sum_{i=1}^{n} x_i^2 - 2\bar{x} \cdot \frac{1}{n} \sum_{i=1}^{n} x_i + \frac{1}{n} \cdot n\bar{x}^2 \\ &= \frac{1}{n} \sum_{i=1}^{n} x_i^2 - 2\bar{x}^2 + \bar{x}^2 = \frac{1}{n} \sum_{i=1}^{n} x_i^2 - \bar{x}^2 \end{aligned}$$


$\square$

また，度数分布表において $x_1, \dots, x_N$ の度数がそれぞれ $f_1, \dots, f_N$ の時，

$$v_x = \frac{1}{n} \sum_{i=1}^{n} f_i x_i^2 - \bar{x}^2 \tag{3}$$



2

---
