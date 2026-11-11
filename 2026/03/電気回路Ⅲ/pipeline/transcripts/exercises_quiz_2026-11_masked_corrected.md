<!-- 訂正済: マスク版PDFと照合。p.14 の VL 位相は 7π/6、VC は −5π/6（学生誤答・採点斜線）。氏名・クラスはマスク済みのみ。 -->
<!--
Gemini一時チャットによる文字起こし（2026-11-11 09:45〜10:03 JST、AI操作代行）
- モデル: 全ページを Gemini 4 Argon（アカウント2 /u/1）で文字起こし。上限の表示はなし。
  - p.1〜13: 09:45〜09:52 JST、5ページ・5ページ・3ページの3回に分けて送信。
  - p.14: 10:03 JST、再マスク済み masked/p-14.jpg のみを新しい一時チャットで追加送信。
- 使用したのは masked/p-01.jpg〜p-14.jpg のみ（source.pdf、pages/、raw_full/、_mask_backup/ は未使用）。
- p.14 は当初、氏名・出席番号欄の白マスクが下線の下まで届いていなかったため保留し、マスク延長後に追加した。送信前に再確認し、氏名・出席番号は見えないことを確認した。
- コピーボタンのMarkdownをそのまま保存。画面上の「p-0N.jpg」出典表示は、コピー本文には入っていない。
- 手書きの読み違いや式の誤りがありうるため、原本と照合してください。
- p.1〜13 に {{採点}} は出ていない。p.14 には赤ペンの点数・丸・チェック・斜線が {{採点}} として入っている。
- 個人情報: 送った各ページに氏名・学籍番号・出席番号は見当たらない（送信前に確認済み）。p.12 のクラス欄と p.14 の氏名・出席番号欄はマスク済み。
-->
## p.1

**電気回路Ⅲ 演習問題 1**

**[3]** 問図 3-2 のグラフで、正弦波交流電圧 $v_1$、$v_2$ の周波数 $f$ はいずれも $100\text{ [Hz]}$、時間差 $\Delta t$ は $\frac{5}{3}\text{ [ms]}$ である。電圧 $v_1$ は電圧 $v_2$ に対して何 $\text{[rad]}$ 進み、または遅れているか。

{{手書き: $2\pi \frac{\Delta t}{100}\text{ [rad]}$ 進み}}

[図: 問図 3-2。縦軸が電圧 $v\text{ [V]}$、横軸が時間 $t\text{ [s]}$ のグラフに2つの正弦波 $v_1$ と $v_2$ が描かれ、ゼロクロス点間の時間差 $\Delta t$ が示されている]

---

**[3]** 次の極座標表示の複素数を直角座標表示で表すとともに、ベクトル図を描け。

**(1)** $\dot{Z} = \sqrt{8} \angle \frac{3\pi}{4}$

{{手書き: $\sout{-2+2j}$}}
{{手書き: $-2+j2$}}

[図: ベクトル図。複素平面（横軸・縦軸 $j$、原点 $0$）の第2象限に原点から左上方向のベクトル {{手書き: 直線}} が描かれている]

**(2)** $\dot{Z} = 1 \angle \left(-\frac{2\pi}{3}\right)$

{{手書き: $-\frac{1}{2} - j\frac{\sqrt{3}}{2}$}}

[図: ベクトル図。複素平面（横軸・縦軸 $j$、原点 $0$）の第3象限に原点から左下方向のベクトル {{手書き: 直線}} が描かれている]

---

**[2]** 直角座標表示で表された電圧 $\dot{V} = -20 + j10\text{ [V]}$ について、フェーザ表示を求め、フェーザ図を問図 5-2 に描け。また、瞬時値を示せ。ただし、角周波数は $\omega\text{ [rad/s]}$ とする。

{{手書き: $10\sqrt{5} \exp\left(\pi - \tan^{-1}\frac{1}{2}\right)$}}

[図: 問図 5-2。複素平面（横軸・縦軸 $j$、原点 $0$）の第2象限に原点から左上方向のベクトル {{手書き: 直線}} が描かれている]

---

**[1]** $L = 0.2\text{ [H]}$ のインダクタンスの両端に、$\dot{V} = 100\angle 0\text{ [V]}$ の電圧を加えるとき、流れる電流 $\dot{I}$ をフェーザ表示、および直角座標表示にて求めよ。また、$\dot{I}$、$\dot{V}$ のフェーザ図を描け。さらに、$\dot{I}$ の瞬時値 $i\text{ [A]}$ の式を示せ。ただし、周波数 $f$ は $\frac{100}{\pi}\text{ [Hz]}$ とする。

{{手書き: $\dot{I} = \frac{\dot{V}}{j\omega L} = -j 2.5\text{ A}$}}

[図: フェーザ図。複素平面（横軸・縦軸 $j$、原点 $0$）上に、{{手書き: 正の横軸方向の矢印 $\dot{V}$ と、負の縦軸方向の矢印 $\dot{I}$}} が描かれている]

---

**[3]** $C = \frac{1}{\pi}\text{ [mF]}$ のキャパシタンスに、$\dot{V} = 50\angle\left(\frac{\pi}{6}\right)\text{ [V]}$ の電圧を加えるとき、キャパシタンス $C$ に流れる電流 $\dot{I}\text{ [A]}$ をフェーザ表示、および直角座標表示にて求めよ。ただし、角周波数は $100\pi\text{ [rad/s]}$ とする。次いで、$\dot{I}$、$\dot{V}$ のフェーザ図を描け。さらに、$\dot{I}$ の瞬時値 $i\text{ [A]}$ の式を示せ。

{{手書き: $\dot{I} = 5\angle \frac{2}{3}\pi\text{ [A]}$}}
{{手書き: $i = 5\sqrt{2}\sin\left(100\pi t + \frac{2}{3}\pi\right)\text{ [A]}$}}

[図: フェーザ図。複素平面（横軸・縦軸 $j$、原点 $0$）の座標軸のみ（書き込みなし）]

---

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

## p.3

{{手書き: 問題 4}}

{{手書き: 

$$\dot{I} = 10\exp\left(j\frac{\pi}{6}\right)$$

}}

{{手書き: 

$$\dot{V}_R = R\dot{I} = 50\exp\left(j\frac{\pi}{6}\right)$$

}}
{{手書き: 

$$v_R = 50\sqrt{2}\sin\left(100t + \frac{\pi}{6}\right)$$

}}

{{手書き: 

$$\begin{aligned} \dot{V}_L = X_L\dot{I} &= j 2\pi f \cdot 50\times 10^{-3} \times 10\exp\left(j\frac{\pi}{6}\right) \\ &= 0.1\pi f \exp\left(j\frac{\pi}{2}\right) \times 10\exp\left(j\frac{\pi}{6}\right) \\ &= \pi f \exp\left(j\frac{4}{6}\pi\right) = \underset{100\pi}{\sout{\pi f}} \exp\left(j\frac{2}{3}\pi\right) \end{aligned}$$

}}

{{手書き: 

$$v_L = \underset{100\pi}{\sout{[判読不能]}}\sin\left(100t + \frac{2}{3}\pi\right)$$

}}

{{手書き: 

$$\begin{aligned} \dot{V}_C = X_C\dot{I} &= \frac{1}{j 2\pi f \cdot 2\times 10^{-3}} \sout{\exp} \times 10\exp\left(j\frac{\pi}{6}\right) \\ &= -j\frac{1}{2\pi \times \frac{100}{2\pi} \times 2\times 10^{-3}} \times 10\exp\left(j\frac{\pi}{6}\right) \\ &= \frac{1}{4\pi} \times \exp\left(-j\frac{\pi}{2}\right) \times \sout{10}\exp\left(j\frac{\pi}{6}\right) \\ &= \frac{1}{4\pi}\exp\left(-j\frac{\pi}{3}\right) \end{aligned}$$

}}

{{手書き: 

$$v_C = \frac{1}{4\pi}\sin\left(100t - \frac{\pi}{3}\right)$$

}}

---

（※ページ下部に別紙の下端が写り込んでいる）
{{手書き: $16\sqrt{2}\exp\left(-j\frac{\pi}{4}\right)$}}  問図 5-39

---

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

## p.5

**電気回路Ⅲ 配布資料 4**

**・瞬時電力**
{{手書き: 

$$v = \sqrt{2}V\sin\omega t\text{ [V]}$$

}}
{{手書き: 

$$\begin{aligned} i &= \frac{\sqrt{2}V}{Z}\sin(\omega t - \theta)\text{ [A]} \\ &= \sqrt{2}I\sin(\omega t - \theta) \end{aligned}$$

}}

[図: (a) RLC 直列回路。交流電源に抵抗 $R\text{ [}\Omega\text{]}$、誘導性リアクタンス $X_L\text{ [}\Omega\text{]}$、容量性リアクタンス $X_C\text{ [}\Omega\text{]}$ が直列接続された回路。全体の電圧が $v\text{ [V]}$ と示されている]

**・平均電力**

**・力率・皮相電力・有効電力・無効電力**
{{手書き: $\text{V}$}}

[図: 電圧 $v$、電流 $i$、瞬時電力 $p$ の波形図（3段）。上段は $v, i, p$ の重畳波形、中段は有効電力成分 $VI\cos\theta$ の波形、下段は $-VI\cos(2\omega t - \theta)$ の振動成分の波形]

---

**問題1** 交流負荷の電圧，電流が $\dot{V} = 15\angle -10^\circ\text{ [V]}$，$\dot{I} = 110\angle -10^\circ\text{ [A]}$ のとき，この負荷の皮相電力，力率，有効電力，無効電力の値をそれぞれ求めよ．

{{手書き: 

$$S = VI = 1650\text{ [VA]}$$

}}
{{手書き: 

$$P = 1650\text{ [W]}$$

}}
{{手書き: 

$$Q = 0\text{ [var]}$$

}}

---

**問題2** ある回路に，瞬時値 $v = 100\sin\left(\pi t + \frac{\pi}{9}\right)\text{ [V]}$ の電圧を加えたところ，瞬時値 $i = 40\sin\left(\pi t - \frac{2\pi}{9}\right)\text{ [A]}$ の電流が流れた．皮相電力，力率，有効電力，無効電力の値をそれぞれ求めよ．

{{手書き: $\frac{3}{9}\pi$}}
{{手書き: 

$$S = VI = 100 \times 40 \div 2 = 2000\text{ [VA]}$$

}}
{{手書き: 

$$P = S\cdot\cos\frac{\pi}{3} = 1000\text{ [W]}$$

}}
{{手書き: 

$$Q = S\cdot\sin\frac{\pi}{3} = 1000\sqrt{3}\text{ [var]}$$

}}

---

**問題3** 回路に $100\text{ [V]}$ の電圧 $V$ を加えたところ，$40\text{ [A]}$ の電流 $I$ が流れた．電圧は，電流より $60^\circ$ 位相が進んでいる．この回路の皮相電力，力率，有効電力，無効電力の値をそれぞれ求めよ．

{{手書き: 

$$S = 4000\text{ [VA]}$$

}}
{{手書き: 

$$P = 2000\text{ [W]}$$

}}
{{手書き: 

$$Q = 2000\sqrt{3}\text{ [var]}$$

}}

---

**問題4** 交流回路で電圧が $\dot{V} = 100 + j100\sqrt{3}\text{ [V]}$，電流が $\dot{I} = 10\sqrt{3} + j10\text{ [A]}$ であるとき，この回路の有効電力，無効電力，力率をそれぞれ求めよ．

## p.6

**電気回路Ⅲ 配布資料 5**

**・複素数での電力**

**問題1** 抵抗 $R = 10\text{ [}\Omega\text{]}$ とキャパシタンス $C = \frac{10^3}{\pi}\text{ [}\mu\text{F]}$ の直列回路に，周波数 $50\text{ [Hz]}$，電圧交流負荷の電圧 $\dot{V} = 100\angle 0^\circ\text{ [V]}$ が加えられている．この回路の皮相電力，力率，有効電力，無効電力の値をそれぞれ求めよ．

{{手書き: 

$$\dot{Z} = 10 + \frac{1}{j 2\pi 50 \frac{10^{-3}}{\pi}} = 10$$

}}

**問題2** 遅れ力率 $0.9$ の負荷の有効電力が $1800\text{ [W]}$ であるとき，この負荷の皮相電力と無効電力を求めよ．

$$\boxed{\text{力率改善}\cdots\text{無効電力を減らして、力率を 1 に近づけること}}$$



**問題3** 図に示す RLC 回路の力率が $1$ となるような可変キャパシタンス $C\text{ [F]}$ を与える式を求めよ．

[図: 問図 6-3。抵抗 $R\text{ [}\Omega\text{]}$ とインダクタンス $L\text{ [H]}$ の直列枝と、可変キャパシタンス $C\text{ [F]}$ の枝が並列に接続された回路]

{{手書き: 

$$\dot{Z} = \left((R + j\omega L)^{-1} + \left(\frac{1}{j\omega C}\right)^{-1}\right)^{-1} = R$$

}}

---

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

## p.8

**問題 17.6** 角周波数 $\omega = 500\text{ [rad/s]}$ のとき，右の RLC 直列回路の電流 $\dot{I}$ と電圧 $\dot{V}$ を求め，フェーザ $\dot{E}, \dot{V}, \dot{I}$ を図示せよ．

[図: 交流電源 $\dot{E} = 40\angle 0^\circ\text{ [V]}$ に、抵抗 $10\text{ [}\Omega\text{]}$、インダクタンス $20\text{ [mH]}$、キャパシタンス $100\text{ [}\mu\text{F]}$ が直列接続された回路。流れる電流が $\dot{I}$、キャパシタンスの両端電圧が $\dot{V}$]

---

**問題 17.7** 右の回路は，電源電圧 $E = 150\text{ [V]}$，角周波数 $\omega = 100\text{ [rad/s]}$ である．スイッチ $\text{S}_1$ と $\text{S}_2$ を開いたとき電流 $I = 5\text{ [A]}$ で $\dot{I}$ は $\dot{E}$ と同相であり，$\text{S}_2$ のみを閉じたとき $I = 3\text{ [A]}$ であった．このとき，次の問に答えよ．

[図: 交流電源 $\dot{E}$ に抵抗 $R$、インダクタンス $L$、キャパシタンス $C$ が直列接続され、$L$ と並列にスイッチ $\text{S}_1$、$C$ と並列にスイッチ $\text{S}_2$ が接続された回路。回路に流れる電流が $\dot{I}$]

**(1)** $R, L, C$ の値を求めよ．

{{手書き: 

$$R = 30\text{ [}\Omega\text{]}$$

}}
{{手書き: 

$$L = 0.4\text{ [H]}$$

}}
{{手書き: 

$$C = \sout{400} 250\text{ [}\mu\text{F]}$$

}}

{{手書き: 

$$\left\{ \begin{aligned} \omega L &= \frac{1}{\omega C} \\ &\frac{1}{100 C} = 40 \implies C = \frac{1}{4000} = \frac{250}{\text{M}} = \frac{1}{4}\text{m} \end{aligned} \right.$$

}}
{{手書き: 

$$\vert{}X_{RL}\vert{} = 50\text{ [}\Omega\text{]}$$

}}
{{手書き: 

$$X_L = 40\text{ }\Omega$$

}}
[図: 手書きの直角三角形。斜辺に $50$、他の2辺に $30$ と $40$ と記されている]

**(2)** $\text{S}_1$ のみを閉じたときの $I$ を求めよ．
{{手書き: 

$$3\text{ [A]}$$

}}

**(3)** $\text{S}_1$ と $\text{S}_2$ を閉じたときの $I$ を求めよ．
{{手書き: 

$$5\text{ [A]}$$

}}

---

**問題 17.8** 右のように $L, C$ のリアクタンスが与えられている．インピーダンス $\dot{Z}$，電流 $\dot{I}$，$\dot{I}$ の実効値 $I$ と位相角 $\theta$ を求めよ．

[図: 交流電源 $\dot{E} = 40\angle 0^\circ\text{ [V]}$ に、抵抗 $10\sqrt{3}\text{ [}\Omega\text{]}$、インダクタンス $15\text{ [}\Omega\text{]}$、キャパシタンス $-5\text{ [}\Omega\text{]}$ が直列接続された回路。流れる電流が $\dot{I}$]

{{手書き: 

$$\begin{aligned} \dot{Z} &= \sqrt{(10\sqrt{3})^2 + (15 - 5)^2} = \sqrt{300 + 100} = 10\sqrt{4} \\ &= 20\text{ [}\Omega\text{]} \end{aligned}$$

}}
{{手書き: 

$$\dot{I} = 2\angle -\frac{\pi}{6}$$

}}
[図: 手書きの直角三角形。横辺に $10\sqrt{3}$、縦辺に $10$、斜辺に $20$、角度に $\frac{\pi}{6}$ と記されている]
{{手書き: $\frac{1}{20}\angle -30^\circ$}}

---

**問題 17.9** 抵抗 $40\text{ [}\Omega\text{]}$，リアクタンス $30\text{ [}\Omega\text{]}$ の負荷に電圧 $100\text{ [V]}$ を加えたときに流れる電流 $I$ を求めよ．

{{手書き: 

$$\dot{Z} = 40 + j30$$

}}
{{手書き: 

$$\dot{Z} = 50\angle \tan^{-1}\frac{3}{4}$$

}}
{{手書き: 

$$100 \div \dot{Z} = 2\angle -\tan^{-1}\frac{3}{4}\text{ [A]}$$

}}

---

**問題 17.10** 抵抗 $30\text{ [}\Omega\text{]}$，リアクタンス $10\text{ [}\Omega\text{]}$ のとき，コンダクタンス $G$ とサセプタンス $B$ を求めよ．

{{手書き: 

$$X = 30 + j10$$

}}
{{手書き: 

$$X^{-1} = \frac{30 - j10}{1000} = \frac{3 - j1}{100}$$

}}
{{手書き: 

$$G = \frac{3}{100}\text{ [S]} \qquad B = -\frac{1}{100}\text{ [S]}$$

}}

---

**チェック項目**

| チェック項目 | 月 日 | 月 日 |
| --- | --- | --- |
| LC 直列回路と RLC 直列回路の計算ができる． |  |  |

68

---

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

## p.10

**問題 19.4** 角周波数 $\omega = 100\text{ [rad/s]}$ のとき，右の回路の電流 $I, I_L, I_C$ がすべて $2\text{ [A]}$ となった．$\dot{E}$ を基準方向としてフェーザ $\dot{I}, \dot{I}_L, \dot{I}_C$ を描き，$R, L, C$ の値を求めよ．

[図: 交流電源 $\dot{E} = 4\text{ [V]}$（電流 $\dot{I}$）に対し、抵抗 $R$ とインダクタンス $L$ の直列枝（電流 $\dot{I}_L$）と、キャパシタンス $C$ の枝（電流 $\dot{I}_C$）が並列接続された回路]

---

**問題 19.5** 右図の回路 (a), (b) において，角周波数 $\omega = 100\text{ [rad/s]}$ のとき，次の問に答えよ．

[図: 回路 (a) は交流電源 $\dot{E} = 10\text{ [V]}$ に抵抗 $1\text{ [}\Omega\text{]}$ とインダクタンス $30\text{ [mH]}$ が直列接続された回路（電流 $\dot{I}_1$）。回路 (b) は回路 (a) の直列枝（電流 $\dot{I}_1$）と並列にキャパシタンス $C$（電流 $\dot{I}_2$）を接続した回路（電源からの全電流 $\dot{I}$）]

**(1)** 回路 (a) の電流 $\dot{I}_1$ とその実効値 $I_1$ を求めよ．

**(2)** 回路 (a) に並列に $C$ を接続した回路 (b) で，$C$ を変数として電流 $\dot{I}_2$ と $\dot{I}$ を求めよ．

**(3)** 電流 $I$ を最小にする $C$ を求め，このときの $\dot{I}_1, \dot{I}_2, \dot{I}$ のフェーザを描け．

---

**問題 19.6** 右の回路の出力電圧 $\dot{V}$ とその実効値 $V$ を，$\omega, R, L, E$ を使って表せ．また，$\omega = 0, \frac{R}{L}$，および $\infty$ のときの $\dot{V}$ を求めよ．

[図: 交流電源 $\dot{E} = E\angle 0^\circ$ に対し、インダクタンス $L$ と抵抗 $R$ の直列枝（中点が端子 B）と、抵抗 $R$ とインダクタンス $L$ の直列枝（中点が端子 A）が並列接続されたブリッジ回路。端子 B から端子 A への電位差が $\dot{V}$]

---

**問題 19.7** $L = CR^2$ が成り立つとき，右の回路の合成アドミタンス $\dot{Y}$ は，角周波数 $\omega$ に依存しない値となる．このときの $\dot{Y}$ および合成インピーダンス $\dot{Z}$ を求めよ．

[図: 抵抗 $R$ とインダクタンス $L$ の直列枝と、キャパシタンス $C$ と抵抗 $R$ の直列枝が並列接続された2端子回路]

---

**チェック項目**

| チェック項目 | 月 日 | 月 日 |
| --- | --- | --- |
| 直並列回路の計算ができる． |  |  |

76

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

## p.12

**ドリル no.23**  class

**問題 23.1** 交流電力に関して，下記の値を求めよ．

**(1)** 電圧 $\dot{V} = 100\angle -30^\circ\text{ [V]}$，電流 $\dot{I} = 2\angle 30^\circ\text{ [A]}$ のときの有効電力 $P$，無効電力 $P_r$，皮相電力 $P_a$ を求めよ．

{{手書き: 

$$\dot{P} = \dot{V}\overline{\dot{I}} = 50\angle -60^\circ\text{ [W]} \qquad P = 25\text{ W} \quad P_r = 43\text{ Var} \quad P_a = 50\text{ VA}$$

}}

**(2)** 電圧 $\dot{V} = 2 + j4\text{ [V]}$，電流 $\dot{I} = 2 + j1\text{ [A]}$ のときの有効電力 $P$，無効電力 $P_r$，皮相電力 $P_a$ を求めよ．

{{手書き: 

$$\dot{P} = \dot{V}\overline{\dot{I}} = \frac{8}{5} + j\frac{6}{5} = \overset{\sqrt{5}}{2}\angle 0.644 \qquad P = 1.6\text{ W} \quad P_r = 1.2\text{ Var} \quad P_a = 2\text{ VA}$$

}}

**(3)** 電圧 $V = 10\text{ [V]}$，インピーダンス $\dot{Z} = 3 + j1\text{ [}\Omega\text{]}$ のときの有効電力 $P$，無効電力 $P_r$，皮相電力 $P_a$ を求めよ．

**(4)** 電圧 $V = 10\text{ [V]}$，有効電力 $P = 16\text{ [W]}$，無効電力 $P_r = 12\text{ [var]}$ のときの力率 $\cos\theta$ と電流 $I$ を求めよ．

**(5)** 電流 $I = 2\text{ [A]}$，有効電力 $P = 60\text{ [W]}$，力率 $\cos\theta = 0.6$ のときの電圧 $V$ とインピーダンス $\dot{Z}$ を求めよ．ただし，$\dot{Z}$ は容量性とする．

---

**問題 23.2** 角周波数 $\omega = 100\text{ [rad/s]}$ のとき，次の回路の有効電力 $P$，無効電力 $P_r$，皮相電力 $P_a$ を求めよ．

**(1)**
[図: 交流電源 $\dot{E} = 20\text{ [V]}$ に、抵抗 $6\text{ [}\Omega\text{]}$ とインダクタンス $80\text{ [mH]}$ が直列接続された回路]

**(2)**
[図: 交流電源 $\dot{E} = 10\text{ [V]}$ に、抵抗 $10\text{ [}\Omega\text{]}$ とキャパシタンス $2\text{ [mF]}$ が並列接続された回路]

**(3)**
[図: 交流電源 $\dot{E} = 10\text{ [V]}$ に、抵抗 $1\text{ [}\Omega\text{]}$ とインダクタンス $30\text{ [mH]}$ の直列枝と、キャパシタンス $2\text{ [mF]}$ の枝が並列接続された回路]

---

**問題 23.3** 次の回路の負荷 $\dot{Z}$ は誘導性で力率 $0.8$，電力 $200\text{ [W]}$ である．電流 $I$，インピーダンス $\dot{Z}$，無効電力 $P_r$，皮相電力 $P_a$ を求めよ．

[図: 交流電源 $50\text{ [V]}$ にインピーダンス負荷 $\dot{Z}$ が接続され、電流 $I$ が流れている回路]

91

---

## p.13

**電気回路Ⅲ 解答**

**23.1**
**(1)** 位相差 $\theta = \theta_V - \theta_I = -30 - 30 = -60^\circ$

$$P = VI\cos\theta = 100 \times 2 \times \frac{1}{2} = 100\text{ [W]}$$



$$\begin{aligned} P_r &= VI\sin\theta = 100 \times 2 \times \left(-\frac{\sqrt{3}}{2}\right) = -100\sqrt{3} \\ &\fallingdotseq -173\text{ [var]} \quad P_a = VI = 200\text{ [VA]} \end{aligned}$$



**(2)** $\dot{P} = \dot{V}\overline{\dot{I}} = (2 + j4)(2 - j1) = 8 + j6$

$$P = \text{Re}(\dot{P}) = 8\text{ [W]} \quad P_r = \text{Im}(\dot{P}) = 6\text{ [var]}$$



$$P_a = \vert{}\dot{P}\vert{} = \sqrt{8^2 + 6^2} = 10\text{ [VA]}$$



**(3)** $Z = \vert{}\dot{Z}\vert{} = \sqrt{10}\text{ [}\Omega\text{]} \quad I = \frac{V}{Z} = \sqrt{10}\text{ [A]}$

$$P = RI^2 = 30\text{ [W]} \quad P_r = XI^2 = 10\text{ [var]}$$



$$P_a = VI = 10\sqrt{10} \fallingdotseq 31.6\text{ [VA]}$$



**(4)** $P_a = \sqrt{P^2 + P_r^2} = 20\text{ [VA]} \quad I = \frac{P_a}{V} = 2\text{ [A]}$

$$P = P_a\cos\theta \text{ より } \cos\theta = \frac{P}{P_a} = \frac{16}{20} = 0.8$$



**(5)** $P = VI\cos\theta \text{ より } V = \frac{P}{I\cos\theta} = \frac{60}{2 \times 0.6} = 50\text{ [V]}$

$$Z = \frac{V}{I} = \frac{50}{2} = 25\text{ [}\Omega\text{]} \quad \dot{Z}\text{ は容量性なので}$$



$$\theta < 0 \text{ だから，}\sin\theta = -\sqrt{1 - \cos^2\theta} = -0.8$$



$$\dot{Z} = Z\angle\theta = Z(\cos\theta + j\sin\theta) = 15 - j20\text{ [}\Omega\text{]}$$



---

**23.2**
**(1)** $\dot{Z} = R + j\omega L = 6 + j8\text{ [}\Omega\text{]} \quad Z = \vert{}\dot{Z}\vert{} = 10\text{ [}\Omega\text{]}$

$$I = \frac{E}{Z} = 2\text{ [A]} \quad P = RI^2 = 6 \times 4 = 24\text{ [W]}$$



$$P_r = XI^2 = 8 \times 4 = 32\text{ [var]} \quad P_a = EI = 40\text{ [VA]}$$



**(2)** $\dot{I} = \left(\frac{1}{R} + j\omega C\right)\dot{E} = (0.1 + j0.2) \times 10 = 1 + j2\text{ [A]}$

$$\dot{P} = \dot{E}\overline{\dot{I}} = 10(1 - j2) = 10 - j20 \ \therefore P = 10\text{ [W]}$$



$$P_r = -20\text{ [var]} \quad P_a = \vert{}\dot{P}\vert{} = 10\sqrt{5} \fallingdotseq 22.4\text{ [VA]}$$



**(3)** $\text{RL の電流 } \dot{I}_{RL} = \frac{\dot{E}}{R + j\omega L} = \frac{10}{1 + j3} = 1 - j3$

$$\text{C の電流 } \dot{I}_C = j\omega C\dot{E} = j0.2 \times 10 = j2$$



$$\dot{I} = \dot{I}_{RL} + \dot{I}_C = 1 - j1\text{ [A]} \quad \dot{P} = \dot{E}\overline{\dot{I}} = 10 + j10$$



$$\begin{aligned} \therefore P &= 10\text{ [W]} \quad P_r = 10\text{ [var]} \quad P_a = 10\sqrt{2} \\ &\fallingdotseq 14.1\text{ [VA]} \end{aligned}$$



---

**23.3** $\dot{Z}$ は誘導性なので，偏角 $\theta > 0$

$$\cos\theta = 0.8 \rightarrow \sin\theta = \sqrt{1 - \cos^2\theta} = 0.6$$



$$P = P_a\cos\theta \text{ より，} P_a = \frac{P}{\cos\theta} = \frac{200}{0.8} = 250\text{ [VA]}$$



$$P_r = P_a\sin\theta = 250 \times 0.6 = 150\text{ [var]} \quad I = \frac{P_a}{V} = \frac{250}{50}$$



$$= 5\text{ [A]} \quad Z = \frac{V}{I} = \frac{50}{5} = 10\text{ [}\Omega\text{]} \quad \dot{Z} = Z\angle\theta$$



$$= Z(\cos\theta + j\sin\theta) = 10(0.8 + j0.6) = 8 + j6\text{ [}\Omega\text{]}$$

## p.14

電気回路Ⅲ 小テスト No.1
{{採点: 38}}

【問題 1】次の複素数を極座標表示に直せ．

(1) $z = \frac{1}{1+j\sqrt{3}}$
{{手書き: $= \frac{1-j\sqrt{3}}{1+3} = \frac{1}{4} - \frac{j\sqrt{3}}{4} = \frac{2}{4}\exp(j\cdot -\frac{\pi}{3}) = \frac{1}{2}\exp(-j\frac{\pi}{3})$}}
{{採点: 丸}}

(2) $z = \frac{1}{1\angle -\frac{2\pi}{3}}$
{{手書き: $= (1\exp(-j\frac{2}{3}\pi))^{-1} = \exp(j\frac{2}{3}\pi)$}}
{{採点: 丸}}

{{手書き: [図: 座標軸と直角三角形のメモ（$\frac{\pi}{6}, 1, \sqrt{3}$）]}}
{{手書き: $e^{i\pi}+1=0$}}
{{採点: 20}}

---

【問題 2】 端子 ab 間の合成インピーダンス，合成アドミタンスを求めよ．その時，$R = 10\Omega, L = 0.1\text{H}, C = 500\mu\text{F}, \omega = 100\text{rad/s}$ とする．

{{手書き: $500 \times 10^{-6} = 5.00 \times 10^{-4}$}}

[図: 端子a, b間に抵抗 $R$、インダクタンス $L$、キャパシタンス $C$ が並列に接続された回路図]

{{手書き: インピーダンス $Z = \left( 10^{-1} + (j10)^{-1} + \left( \frac{1}{j 5.00 \times 10^{-2}} \right)^{-1} \right)^{-1} = 5 + j5 = 5\sqrt{2}\exp(j\frac{\pi}{4})$}}
{{手書き: $j 5.00 \times 10^{-2} = \frac{1}{20}j$}}
{{手書き: $5.00 \times 10^{-4}$}}
{{手書き: $Z = 7.07\ [\text{S}]$}} {{採点: 斜線}}

{{手書き: アドミタンス $A = Z^{-1} = \frac{1}{10} - j\frac{199}{2000}$}}
{{手書き: $A = 0.141\ [\text{S}^{-1}]$}} {{採点: 斜線}}

---

【問題 3】瞬時値で表した電流 $i = 0.2\sqrt{2}\sin\left(1000t + \frac{\pi}{6}\right) [\text{A}]$ について以下について示せ．

(1) 電流のフェーザを極座標表示で示せ
(2) この電流が R=50 [$\Omega$] の抵抗，L=20 [mH] のインダクタンス，C=5 [$\mu$F] のキャパシタンス，これら 3 つの素子を直列に接続した回路に，この電流が流れるときそれぞれの素子に生じる電圧を極座標表示で求めよ．
(3) (2) で求めたそれぞれの電圧を瞬時値の式でそれぞれ示せ．

{{手書き: [図: 縦軸にL、Cと記されたベクトル図のようなメモ]}}
{{手書き: $-\frac{j}{5 \times 10^{-6} \times 1 \times 10^3} = -j\frac{1}{5} \times 10^3$}}
{{採点: 18}}

{{手書き: (1) $\dot{I} = 0.2\exp(j\frac{\pi}{6})\ [\text{A}]$}} {{採点: 丸}}

{{手書き: (2) $\dot{V}_R = 10\exp(j\frac{\pi}{6})\ [\text{V}]$}} {{採点: 丸}}
{{手書き: $2.0 \times 10^{-2} \times 1000 = 20$}}
{{手書き: $\dot{V}_L = 4.0\exp(j\frac{7}{6}\pi)\ [\text{V}]$}} {{採点: 斜線}}
{{手書き: $\dot{V}_C = 40\exp(-j\frac{5}{6}\pi)\ [\text{V}]$}} {{採点: 斜線}}

{{手書き: (3) $v_R = 10\sqrt{2}\sin(1000t + \frac{\pi}{6})\ [\text{V}]$}} {{採点: チェック}}
{{手書き: $v_L = 4.0\sqrt{2}\sin(1000t + \frac{7}{6}\pi)\ [\text{V}]$}} {{採点: 斜線}}
{{手書き: $v_C = 40\sqrt{2}\sin(1000t - \frac{5}{6}\pi)\ [\text{V}]$}} {{採点: 斜線}}
