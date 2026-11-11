## p.4

**電気回路Ⅲ 配布資料 3**

**・アドミタンスの定義**

[図: 図 5-43。端子間に電圧 $\dot{V}\text{ [V]}$、流入する電流 $\dot{I}\text{ [A]}$、アドミタンス $\dot{Y}\text{ [S]}$ のブロック図]
[図: 図 5-44 $\dot{Y} = G + jB\text{ [S]}$ が表す回路。コンダクタンス $G\text{ [S]}$ とサセプタンス $B\text{ [S]}$ の並列回路]

**・回路要素のアドミタンス**

[図: 図 5-46。(a) 抵抗 $r\text{ [}\Omega\text{]}$ の素子図と、(b) 複素平面上の正の実軸に沿うベクトル $\dot{Y}$（大きさ $\frac{1}{r}$）]
[図: 図 5-48。(a) キャパシタンス $C\text{ [F]}$ の素子図と、(b) 空欄の複素平面]
[図: 図 5-47。(a) インダクタンス $L\text{ [H]}$ の素子図と、(b) 空欄の複素平面]

| 回路要素 | アドミタンス $\text{[S]}$ | コンダクタンス $\text{[S]}$ | サセプタンス $\text{[S]}$ |
| --- | --- | --- | --- |
| 抵抗 $r\text{ [}\Omega\text{]}$ |  |  |  |
| インダクタンス $L\text{ [H]}$ |  |  |  |
| キャパシタンス $C\text{ [F]}$ |  |  |  |

---

**問題1** 次の回路のアドミタンス $\dot{Y}\text{ [S]}$ を求めよ．その $G\text{ [S]}$，$B\text{ [S]}$，アドミタンスの絶対値 $\vert{}\dot{Y}\vert{}\text{ [S]}$，$\theta_Y\text{ [rad]}$ を求めよ．

{{手書き: 

$$\begin{aligned} \dot{Y} &= (1 + j3)^{-1} + \left(\frac{1}{-5j}\right) \\ &= \frac{1}{1+j3} + \frac{j}{5}\text{ [S]} \\ &= \frac{1-j3}{1+9} + \frac{j}{5} = \frac{1-j}{10}\text{ [S]} \end{aligned}$$

}}
{{手書き: 

$$G = \frac{1}{10}\text{ [S]}, \quad B = -\frac{1}{10}\text{ [S]}$$

}}
{{手書き: 

$$\vert{}\dot{Y}\vert{} = \frac{\sqrt{2}}{10}\text{ [S]}$$

}}
{{手書き: 

$$\theta_Y = -45^\circ$$

}}

[図: 問図 5-31。(a) $r = 1\text{ [}\Omega\text{]}$ と $X_L = 3\text{ [}\Omega\text{]}$ の直列枝と、$X_C = -5\text{ [}\Omega\text{]}$ の枝が並列接続された回路。(b) 複素平面の座標軸（書き込みなし）]

---

**問題2** 図の回路に流れる電流 $\dot{I}\text{ [A]}$ の極座標表示を求めよ．

{{手書き: 

$$\begin{aligned} X = \left(25^{-1} + (3+j4)^{-1}\right)^{-1} &= \left(\frac{3-j4}{25} + \frac{1}{25}\right)^{-1} \\ &= \frac{25}{4-j4} \\ &= \frac{25(4+j4)}{32} \end{aligned}$$

}}
{{手書き: 

$$\overset{4}{\sout{100}} \times \frac{4-j4}{\underset{2}{\sout{25}}} = 16 - j16 = 16\sqrt{2}\exp\left(-j\frac{\pi}{4}\right)$$

}}

[図: 問図 5-39。電圧源 $\dot{V} = 100\angle 0\text{ [V]}$ に対し、端子 a-b 間で抵抗 $r_2 = 25\text{ [}\Omega\text{]}$ の枝と、リアクタンス $X = 4\text{ [}\Omega\text{]}$（インダクタ）および抵抗 $r_1 = 3\text{ [}\Omega\text{]}$ の直列枝が並列に接続された回路。電源から端子 a へ流れる電流が $\dot{I}\text{ [A]}$ と示されている]

---
