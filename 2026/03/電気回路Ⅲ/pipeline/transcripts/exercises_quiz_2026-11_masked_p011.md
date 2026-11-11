## p.11

**電気回路Ⅲ 解答**

**19.4** $\dot{I}_C$ は $\dot{E}$ より $90^\circ$ 進むから，$\dot{I}_C, \dot{I}_L, \dot{I}$ は右図の正三角形を作る．

$$\therefore \dot{I}_C = 2\angle 90^\circ = j2, \ \dot{I}_L = 2\angle -30^\circ\text{．}$$


$\dot{I}_C = j\omega C\dot{E} = j400C$ より $C = 5\text{ [mF]}$．

$$R + j\omega L = \frac{\dot{E}}{\dot{I}_L} = \frac{4}{2\angle -30^\circ} = 2\angle 30^\circ$$



$$= \sqrt{3} + j1 \text{ より，} R = \sqrt{3}\text{ [}\Omega\text{]}, \ \omega L = 1\text{．} \rightarrow L = 10\text{ [mH]}$$



[図: フェーザ図。水平右向きの基準ベクトル $\dot{E}$ に対し、真上方向（$+90^\circ$）に長さ $2$ の $\dot{I}_C$、$-30^\circ$ 方向に長さ $2$ の $\dot{I}_L$、$+30^\circ$ 方向に長さ $2$ の合成電流 $\dot{I}$ が描かれ、正三角形を構成している]

---

**19.5**
**(1)** 

$$\begin{aligned} \dot{I}_1 &= \frac{\dot{E}}{R + j\omega L} = \frac{10}{1 + j3} = \frac{10(1 - j3)}{(1 + j3)(1 - j3)} \\ &= 1 - j3\text{ [A]} \quad I_1 = \vert{}\dot{I}_1\vert{} = \sqrt{10}\text{ [A]} \end{aligned}$$



**(2)** $\dot{I}_2 = j\omega C\dot{E} = j1000C\text{ [A]}$

$$\dot{I} = \dot{I}_1 + \dot{I}_2 = 1 + j(1000C - 3)\text{ [A]}$$



**(3)** $I = \vert{}\dot{I}\vert{} = \sqrt{1^2 + (1000C - 3)^2}$ は，$1000C = 3$ のとき最小になる．

$$\therefore C = 3\text{ [mF]} \quad \text{このとき，}$$



$$\dot{I}_2 = j3\text{ [A]} \quad \dot{I} = 1\text{ [A]}$$



[図: フェーザ図。水平右向きの $\dot{E}$ と同方向に長さ $1$ の $\dot{I} = 1$、真上方向に長さ $3$ の $\dot{I}_2 = j3$、第4象限方向に長さ $\sqrt{10}$ の $\dot{I}_1 = 1 - j3$ が描かれている]

---

**19.6** 点 A, B の電位 $\dot{V}_A, \dot{V}_B$ は分圧の式より，

$$\dot{V}_A = \frac{R}{R + j\omega L}\dot{E}, \ \dot{V}_B = \frac{j\omega L}{R + j\omega L}\dot{E} \quad \therefore \dot{V} = \dot{V}_A - \dot{V}_B$$



$$= \frac{R - j\omega L}{R + j\omega L}\dot{E}\text{．} \quad V = \vert{}\dot{V}\vert{} = \frac{\vert{}R - j\omega L\vert{}}{\vert{}R + j\omega L\vert{}}E = E\text{（一定値）}$$


$\omega = 0$ のとき，$\dot{V} = \dot{E} = E\angle 0^\circ$．$\omega = \frac{R}{L}$ のとき，

$$\dot{V} = \frac{R - jR}{R + jR}\dot{E} = \frac{1 - j}{1 + j}E = \frac{\sqrt{2}\angle -45^\circ}{\sqrt{2}\angle 45^\circ}E = E\angle -90^\circ$$



$$\omega \rightarrow \infty \text{ で，} \dot{V} = \frac{\frac{R}{\omega L} - j}{\frac{R}{\omega L} + j}\dot{E} \rightarrow \frac{1\angle -90^\circ}{1\angle 90^\circ}E = E\angle -180^\circ$$


$\vert{}\dot{V}\vert{}$ は電源電圧 $E$ に等しく，$\dot{V}$ の位相だけが $\omega$ とともに変化する．この回路を位相推移器と言う．

---

**19.7** $\dot{Y} = \frac{1}{R + j\omega L} + \frac{1}{R + \frac{1}{j\omega C}}$ に $L = CR^2$ を代入：

$$\dot{Y} = \frac{1}{R + j\omega CR^2} + \frac{j\omega C}{1 + j\omega CR} = \frac{1 + j\omega CR}{R(1 + j\omega CR)} = \frac{1}{R}\text{．}$$


$\dot{Z} = R$．このように，$L, C$ を含むのにインピーダンスが $\omega$ に依存せず，一定の抵抗値となる回路を定抵抗回路と言う．
$L = CR^2$ のとき，下図 (a), (b) はブリッジの平衡条件 $R \times R = j\omega L \times \frac{1}{j\omega C}$ を満たすので，ブリッジ部分に電流が流れず，これを除去した (c) と等価である．(c) は本問題の回路で，全インピーダンス $= R$．だから，$L = CR^2$ のとき，回路 (a), (b), (c) はどれも，全インピーダンス $= R$ の定抵抗回路である．

[図: 3つの回路図 (a), (b), (c)。上枝が抵抗 $R$ とインダクタンス $L$、下枝がキャパシタンス $C$ と抵抗 $R$ の並列回路において、(a) は上下の中点間にインピーダンス $\dot{Z}$ が接続された回路、(b) は上下の中点間が短絡された回路、(c) は上下の中点間が開放された回路]

---
