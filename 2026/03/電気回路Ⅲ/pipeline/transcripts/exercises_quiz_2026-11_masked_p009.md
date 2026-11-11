## p.9

**電気回路Ⅲ 解答**

**17.6** 例題 17.4 と同じ回路で，$\omega$ が半分である．例題 17.4 の結果と比較してみよう．

$$\begin{aligned} \dot{I} &= \frac{\dot{E}}{R + j\omega L + \frac{1}{j\omega C}} = \frac{40}{10 + j(10 - 20)} \\ &= \frac{4}{1 - j} = \frac{4}{\sqrt{2}\angle -45^\circ} = 2\sqrt{2}\angle 45^\circ\text{ [A]} \end{aligned}$$



$$\dot{V} = \frac{\dot{I}}{j\omega C} = \frac{2\sqrt{2}\angle 45^\circ}{0.05\angle 90^\circ} = 40\sqrt{2}\angle -45^\circ\text{ [V]}$$



[図: フェーザ図。水平右向きの基準ベクトル $\dot{E}$（$40\text{ V}$）に対し、反時計回り $45^\circ$ の方向に $\dot{I}$（$2\sqrt{2}\text{ A}$）、時計回り $-45^\circ$ の方向に $\dot{V}$（$40\sqrt{2}\text{ V}$）が描かれている]

**17.7**
**(1)** $\text{S}_1, \text{S}_2$ 開放時，$\dot{I}$ と $\dot{E}$ が同相ゆえ，インピーダンス $\dot{Z} = \text{実数 } R$．リアクタンス $\omega L - \frac{1}{\omega C} = 0$．

$$\therefore R = Z = \frac{E}{I} = \frac{150}{5} = 30\text{ [}\Omega\text{]}$$


$\text{S}_2$ 短絡時，$Z = \sqrt{R^2 + (\omega L)^2} = \frac{E}{I} = \frac{150}{3} = 50$．
$R = 30$ ゆえ $\omega L = 40 \rightarrow L = 0.4\text{ [H]} = 400\text{ [mH]}$

$$\omega L = \frac{1}{\omega C} \rightarrow C = \frac{1}{\omega^2 L} = \frac{1}{4000}\text{ [F]} = 250\text{ [}\mu\text{F]}$$



**(2)** $I = \frac{E}{\sqrt{R^2 + \left(\frac{1}{\omega C}\right)^2}} = \frac{E}{\sqrt{R^2 + (\omega L)^2}} = 3\text{ [A]}$

**(3)** $I = \frac{E}{R} = 5\text{ [A]}$

**17.8** $R, L, C$ のインピーダンスはそれぞれ，$10\sqrt{3}, j15, -j5\text{ [}\Omega\text{]}$ となるから，$\dot{Z} = 10\sqrt{3} + j15 - j5 = 10\sqrt{3} + j10 = 20\angle 30^\circ\text{ [}\Omega\text{]}$．

$$\dot{I} = \frac{40}{20\angle 30^\circ} = 2\angle -30^\circ\text{ [A]}$$



$$I = \vert{}\dot{I}\vert{} = 2\text{ [A]} \quad \theta = -30^\circ$$



[図: フェーザ図。水平右向きの $\dot{E}$（$40\text{ V}$）に対し、時計回り $-30^\circ$ の方向に $\dot{I}$（$2\text{ A}$）が描かれている]

**17.9** $\dot{Z} = 40 + j30\text{ [}\Omega\text{]}$ だから，

$$Z = \vert{}\dot{Z}\vert{} = \sqrt{40^2 + 30^2} = 50\text{ [}\Omega\text{]}\text{．}$$



$$I = \frac{E}{Z} = \frac{100}{50} = 2\text{ [A]}$$



[図: インピーダンス三角形。底辺 $40$、高さ $30$、斜辺 $50$（$\dot{Z} = 40 + j30$）の直角三角形]

**17.10** インピーダンス $\dot{Z} = 30 + j10\text{ [}\Omega\text{]}$ だから，
アドミタンス $\dot{Y} = \frac{1}{30 + j10} = \frac{30 - j10}{(30 + j10)(30 - j10)}$

$$= \frac{30 - j10}{30^2 + 10^2} = 0.03 - j0.01\text{ [S]} = 30 - j10\text{ [mS]}$$



$$\therefore G = 30\text{ [mS]} \quad B = -10\text{ [mS]}$$



---
