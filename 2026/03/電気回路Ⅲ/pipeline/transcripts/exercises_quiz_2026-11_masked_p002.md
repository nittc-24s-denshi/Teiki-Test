## p.2

**電気回路Ⅲ 配布資料 1**

**問題1** 図1において $v_c = V_c \sin\omega t\text{ [V]}$ である．
（1）この時の電源電圧 $v$ を，$v = V_m \sin(\omega t + \theta)\text{ [V]}$ の形式で求めよ．
{{手書き: $v =$}}
（2）$\frac{V_c}{V_m}$ の式を $R$，$C$，$\omega$ を適切に用いて求めよ．
（3）（2）で得られた式を用い，$C = 1\text{ [}\mu\text{F]}$，$R = 1\text{ [k}\Omega\text{]}$，周波数を問表 3-1 の値としたときの $\frac{V_c}{V_m}$ を計算せよ（小数点以下3桁とすること）．また，グラフで示せ．
（4）この結果から，この回路はローパスフィルタかハイパスフィルタか示せ．

{{手書き: $\dot{V}_c = \frac{\dot{V}_c}{V_c}$}}

[図: 図1。交流電源 $v\text{ [V]}$（角周波数 $\omega\text{ [rad/s]}$）に抵抗 $R\text{ [}\Omega\text{]}$ とキャパシタンス $C\text{ [F]}$ が直列接続された回路。キャパシタンスの両端電圧が $v_c\text{ [V]}$ と示されている]

**問表 3-1**

| 周波数 $f\text{ [kHz]}$ | $V_c / V_m$ |
| --- | --- |
| $0.01$ |  |
| $0.1$ |  |
| $0.3$ |  |
| $1$ |  |
| $10$ |  |

[図: 縦軸が電圧比 $\frac{V_c}{V_m}$（目盛り $0, 0.5, 1.0$）、横軸が周波数 $f\text{ [kHz]}$（対数目盛り $0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10$）の片対数グラフ用紙（書き込みなし）。右下に {{手書き: [判読不能]}} の薄い書き込み]

---

**問題2** 次の複素数を極座標表示と直交座標表示で表せ．

**(1)** $\dot{Z} = \left(6\angle\frac{\pi}{6}\right)\left(3\angle -\frac{2\pi}{3}\right)$

{{手書き: $= 18\angle -\frac{3}{6}\pi = 18\angle -\frac{1}{2}\pi$}}
{{手書き: $= 18(0 - j)$}}
{{手書き: $= -18j$}}

**(2)** $\dot{Z} = (1 + j\sqrt{3})\times\sqrt{3}\angle\left(-\frac{\pi}{4}\right)$

{{手書き: $2\angle\frac{\pi}{3}$}}
{{手書き: $= 2\angle\frac{\pi}{3} \times \sqrt{3}\angle -\frac{\pi}{4}$}}
{{手書き: $= 2\sqrt{3}\angle\frac{1}{12}\pi$}}
{{手書き: $= 2\sqrt{3}\left(\cos\frac{\pi}{12} + j\sin\frac{\pi}{12}\right)$}}

---

**問題3** 正弦波交流電圧 $v = 10\sqrt{2}\sin\left(\omega t - \frac{\pi}{3}\right)\text{ [V]}$ について以下について示せ．
{{手書き: （特に断りのない限り、以下の問いの単位は $\text{V}$ とする）}}

（1）極座標表示 $\dot{V}$ と直交座標表示 $\dot{V}$ を示せ．
（2）この $\dot{V}$ についての $j\dot{V}$，$-j\dot{V}$ を与える極座標表示を求めよ．
（3）$\dot{V}$，$j\dot{V}$，$-j\dot{V}$ のフェーザ図を描け．

{{手書き: (1) $\dot{V} = 10\exp\left(-j\frac{\pi}{3}\right) = 10\sin -\frac{\pi}{3} + 10j\cos -\frac{\pi}{3}$}}
{{手書き: $= 5 - j5\sqrt{3}$}}

{{手書き: (2) $j\dot{V} = 10\exp\left(j\frac{1}{6}\pi\right)$}}
{{手書き: $-j\dot{V} = 10\exp\left(j\frac{5}{6}\pi\right)$}}

{{手書き: (3)}}
[図: 手書きのフェーザ図。横軸 $\text{Re}$、縦軸 $\text{Im}$ の複素平面に、第4象限の矢印 $\dot{V}$、第1象限の矢印 $j\dot{V}$、第3象限の矢印 $j\dot{V}$（または $-j\dot{V}$）が描かれている]

---

**問題4** 瞬時値で表した電流 $i = 10\sqrt{2}\sin\left(100t + \frac{\pi}{6}\right)$ の極座標表示 $\dot{I}$ を示したのち，この電流が $R = 5\text{ [}\Omega\text{]}$ の抵抗，$L = 50\text{ [mH]}$ のインダクタンス，$C = 2\text{ [mF]}$ のキャパシタンスに流れるとき，それぞれの素子に生じる電圧を極座標表示 $\dot{V}_R\text{ [V]}$，$\dot{V}_L\text{ [V]}$，$\dot{V}_C\text{ [V]}$ を求めよ．また，それぞれの電圧の瞬時値 $v_R$，$v_L$，$v_C$ の式をそれぞれ示せ．さらに $\dot{I}$，$\dot{V}_R$，$\dot{V}_L$，$\dot{V}_C$，のフェーザ図を描け．

---
