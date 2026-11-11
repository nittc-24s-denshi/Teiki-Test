## p.7

**電気回路Ⅲ 配布資料 6**

**・最大電力供給条件**

[図: 図 6-23。破線で囲まれた交流電源（起電力 $\dot{V}_0\text{ [V]}$、内部インピーダンス $\dot{Z}_0 = R_0 + jX_0\text{ [}\Omega\text{]}$）の端子 a-b に、可変インピーダンス負荷 $\dot{Z} = R + jX\text{ [}\Omega\text{]}$ が接続され、電流 $\dot{I}\text{ [A]}$ が流れている回路]

{{手書き: 

$$\begin{aligned} \dot{I} = \frac{\dot{V}_0}{\dot{Z}_0 + \dot{Z}} &= \frac{\dot{V}_0}{R_0 + jX_0 + R + jX} \\ &= \frac{\dot{V}_0}{(R_0 + R) + j(X_0 + X)} \end{aligned}$$

}}

{{手書き: 

$$\begin{aligned} P &= \vert{}\dot{I}\vert{}^2 R \\ &= \frac{\vert{}\dot{V}_0\vert{}^2}{(R_0 + R)^2 + (X_0 + X)^2} \cdot R \end{aligned}$$

}}

{{手書き: $R$ は一定とする。}}
{{手書き: $X_0 + X$ が最小 $\Leftrightarrow$ 分母が最小 $\Leftrightarrow P$ が最大}}
{{手書き: $X_0 + X = 0 \quad \therefore X = -X_0$}}
{{手書き: このとき、$P = \frac{\vert{}\dot{V}_0\vert{}^2 R}{(R_0 + R)^2}$}}

**問題1** 図のように電源電圧が $\vert{}\dot{V}_0\vert{}\text{ [V]}$，内部インピーダンスが抵抗 $r_0\text{ [}\Omega\text{]}$ とキャパシタンス $C\text{ [F]}$ の並列回路からなる交流電圧源があるとする．この電圧源に，負荷として抵抗 $R_L\text{ [}\Omega\text{]}$ とインダクタンス $L\text{ [H]}$ が直列接続されている．$R_L$ の消費電力が最大となるような，$R_L$ と $L$ の値を，整合条件によって求めよ．また，この時の最大消費電力を求めよ。角周波数は $\omega = 10^3\text{ [rad/s]}$ とする．

[図: 問図 6-6。破線で囲まれた交流電源（電圧 $\vert{}\dot{V}_0\vert{} = 100\text{ [V]}$、および $r_0 = 10^3\text{ [}\Omega\text{]}$ と $C = 1\text{ [}\mu\text{F]}$ の並列回路）に、破線で囲まれた負荷（可変抵抗 $R_L\text{ [}\Omega\text{]}$ と可変インダクタンス $L\text{ [H]}$ の直列回路）が接続された回路]

{{手書き: 

$$Z_0 = 1\times 10^{-3} + j 1\times 10^{-3}$$

}}

**問題2** 図のように電源電圧が $\dot{V}_0 = 60\text{ [V]}$，内部インピーダンス $\dot{Z}_0 = 0.3 + j0.9\text{ [}\Omega\text{]}$ の交流電圧源に，負荷として抵抗 $R_L\text{ [}\Omega\text{]}$ とキャパシタンス $C\text{ [F]}$ が並列接続されている．$R_L$ の消費電力が最大となるような，$R_L$ と $C$ の値を，整合条件によって求めよ．また，この時の最大消費電力を求めよ。角周波数は $\omega = 10^3\text{ [rad/s]}$ とする．

{{手書き: 

$$R_L = 0.3\text{ [}\Omega\text{]} \qquad X_C = -0.9\text{ [}\Omega\text{]}$$

}}
{{手書き: 

$$C = 1.11\text{ [mF]}$$

}}
{{手書き: 

$$(100\sout{[判読不能]})^2 \cdot 0.3 = 3000\text{ [W]}$$

}}

---
