<!--
Gemini一時チャットによる文字起こし（2026-11-11 09:36〜09:38 JST、AI操作代行）
- モデル: 全6ページ Gemini 4 Argon（アカウント2 /u/1）。3ページずつ2回に分けて送信し、上限の表示はなし。
- 使用したのは masked/p-01.jpg〜p-06.jpg のみ（source.pdf や pages/ は未使用）。
- コピーボタンのMarkdownをそのまま保存。画面上の「p-0N.jpg」出典表示は、コピー本文には入っていない。
- 赤ペンの採点は {{採点: ...}}、手書き解答は {{手書き: ...}}。一部で混在・誤分類がある（例: p.6 の $v_2$ 添字訂正が {{手書き}} になっている）。式の崩れもありうる。原本と照合してください。推測では直していない。
- 個人情報: 氏名欄は黒塗りで、学籍番号・出席番号の記入は見当たらず、送らなかったページはない。p.2・p.4・p.5 などに赤い確認印があり、{{採点: 確認印（日付と印字）}} として残している（提出者の氏名ではなく、採点側の印と判断）。
-->

## p.1

電子回路Ⅱ 3 （{{手書き: 10}} / {{手書き: 2}} 講義分）

1. オペアンプの特徴として正しいものには○，誤っているものには×を答えよ．



(1) 電圧利得が大きい．{{手書き: ○}} {{採点: ○}}
(2) 入力インピーダンスが小さい．{{手書き: ×}} {{採点: ○}}
(3) 差動増幅する．{{手書き: ○}} {{採点: ○}}
(4) 出力インピーダンスが小さい．{{手書き: ○}} {{採点: ○}}

2. 正弦波電圧の振幅の実効値 $V_{rms} = 10\text{ V}$ のとき，(1) $V_{pp}$，(2) $V_{op}$ を求めよ．



(1) {{手書き: $20\sqrt{2}\text{ V}$}} {{採点: $= 28.28\text{ V}$}}

(2) {{手書き: $10\sqrt{2}\text{ V}$}} {{採点: $= 14.14\text{ V}$}}

3. $2\text{ mV}$ を入力したとき $9\text{ mV}$ 出力するアンプのゲインは何 $\text{dB}$ か答えよ．



{{手書き: $13.1\text{ dB}$}} {{採点: ○}}

4. $19\text{ V}$ を入力したとき $2\text{ V}$ 出力するアンプのゲインは何 $\text{dB}$ か答えよ．



{{手書き: $-19.6\text{ dB}$}} {{採点: ○}}

5. アンプのゲインが $30\text{ dB}$ のとき，$1\text{ mV}$ を入力すると何 $\text{mV}$ 出力されるか答えよ．



{{手書き: $31.6\text{ mV}$}} {{採点: ○}}

6. 図の波形を見て各問いに答えよ．



[図: 縦軸 $V\text{ mV}$（目盛り $-6, -4, -2, 0, 2, 4, 6$）、横軸 $t\text{ ms}$（目盛り $0, \frac{\pi}{2}, \pi, \frac{3\pi}{2}, 2\pi$）のグラフ。実線 a は振幅 $2\text{ mV}$・周期 $2\pi\text{ ms}$ の正弦波、破線 b は振幅 $5\text{ mV}$・周期 $2\pi\text{ ms}$ の正弦波]

(1) (a)の波形の振幅 $V_{op}$，実効値 $V_{rms}$ を答えよ．
{{手書き: $2\text{ mV}$}} {{採点: ○}} {{手書き: $\frac{2}{\sqrt{2}}\text{ mV}$}} {{採点: $= 1.41\text{ mV}$}}

(2) (a)(b)の波形の周波数 $f$ を答えよ．
{{手書き: $318\text{ Hz}$}} {{採点: ○}}

(3) (a)を入力，(b)を出力としたときのゲインは何 $\text{dB}$ か答えよ．
{{手書き: $G = 20\log \frac{5}{2} \fallingdotseq 7.96\text{ dB}$}} {{採点: ○}}

(4) (a)の位相を $0\text{ rad}$ とすると，(b)の位相は何 $\text{rad}$ か答えよ．
{{手書き: $+\frac{\pi}{6}\text{ rad}$}} {{採点: ○}}

---

## p.2

7. オペアンプ TL84CN と LM741 のピン配置を調査せよ．



TL084CN

[図: 14ピンDIPパッケージの枠図（左側に1〜7番ピン、右側に8〜14番ピンの端子枠）]

* 左側（上から下へ）：
* {{手書き: 1OUT}} {{手書き: 1}}


* {{手書き: 1IN-}} {{手書き: 2}}


* {{手書き: 1IN+}} {{手書き: 3}}


* {{手書き: VCC+}} {{手書き: 4}}


* {{手書き: 2IN+}} {{手書き: 5}}


* {{手書き: 2IN-}} {{手書き: 6}}


* {{手書き: 2OUT}} {{手書き: 7}}




* 右側（上から下へ）：
* {{手書き: 14}} {{手書き: 4OUT}}


* {{手書き: 13}} {{手書き: 4IN-}}


* {{手書き: 12}} {{手書き: 4IN+}}


* {{手書き: 11}} {{手書き: VCC-}}


* {{手書き: 10}} {{手書き: 3IN+}}


* {{手書き: 9}} {{手書き: 3IN-}}


* {{手書き: 8}} {{手書き: 3OUT}}





{{採点: ○}}

LM741

[図: 8ピンDIPパッケージの枠図（端子枠なしの長方形）]

* 左側（上から下へ）：
* {{手書き: OFFSET NULL}} {{手書き: 1}}


* {{手書き: INVERTING INPUT}} {{手書き: 2}}


* {{手書き: NON-INVERTING INPUT}} {{手書き: 3}}


* {{手書き: $V^-$}} {{手書き: 4}}




* 右側（上から下へ）：
* {{手書き: 8}} {{手書き: NC}}


* {{手書き: 7}} {{手書き: $V^+$}}


* {{手書き: 6}} {{手書き: OUTPUT}}


* {{手書き: 5}} {{手書き: OFFSET NULL}}





{{採点: ○}}
{{採点: 確認印（26.10.-9）}}

---

## p.3

電子回路Ⅱ 3 （{{手書き: 10}} / {{手書き: 16}} 講義分）

1. What is the output voltage $v_o$ in the circuit , assuming an infinite open-loop gain $A_O$?
（`voltage v_o` の下に {{手書き: 下線}}、`assuming` の下に {{手書き: とし}}）



{{手書き: 

$$V_o = -18.75\text{ V}$$

}}
{{手書き: 

$$A_v = -\frac{250}{20} = -12.5$$

}}

[図: 反転増幅回路。入力電圧 $v_i = 1.5\text{ V}$ が抵抗 $R_1$（$20\text{ k}\Omega$、電流 $i_1$）を介してオペアンプの反転入力端子（$-$）に接続。非反転入力端子（$+$）は接地。帰還抵抗 $R_2$（$250\text{ k}\Omega$、電流 $i_2$）が反転入力端子と出力端子 $v_o$ の間に接続されている]

2. What input voltage $v_i$ results in an output of $2\text{ V}$ in the circuit , assuming an open-loop gain $A_O = \infty$?



{{手書き: 

$$v_i = -40\text{ mV}$$

}}
{{手書き: 

$$A_v = -50$$

}}

[図: 反転増幅回路。入力端子 $v_i$ が抵抗 $R_1$（$20\text{ k}\Omega$、電流 $i_1$）を介してオペアンプの反転入力端子（$-$）に接続。非反転入力端子（$+$）は接地。帰還抵抗 $R_2$（$1\text{ M}\Omega$、上部に {{手書き: $1000\text{k}$}} の書き込み、電流 $i_2$）が反転入力端子と出力端子 $v_o = 2\text{ V}$ の間に接続されている]

## p.4

3. Summarize the following text in Japanese.



In this circuit, the noninverting input is grounded, $v_i$ is connected to the inverting input through $R_1$, and the feedback resistor $R_f$ is connected between the inverting input and output. Our goal is to obtain the relationship between the input voltage $v_i$ and the output voltage $v_o$. Applying KCL at node 1,
（`grounded` の上に {{手書き: GND}}、`,` の上に {{手書き: ①}} と `/`、`R_1,` の `,` に {{手書き: /}}、`R_f` の上に {{手書き: ③}}、`output.` の後に {{手書き: ④}} と `/`、`v_i` と `v_o` の下に {{手書き: 下線}}）

$$i_1 = i_f \Rightarrow \frac{v_i - v_1}{R_1} = \frac{v_1 - v_o}{R_f}$$



[図: 反転増幅回路。入力 $v_i$（丸囲み）から抵抗 $R_1$（電流 $i_1$）を介して節点1（電圧 $v_1$、オペアンプの$-$端子）へ接続（この部分を囲んで {{手書き: ②}}）。$+$端子（電圧 $v_2$）は接地（この部分を囲んで {{手書き: ①}}）。節点1から帰還抵抗 $R_f$（電流 $i_f$）を介して出力 $v_o$ へ接続。図の上部に {{手書き: ③ $V_1 \rightarrow R_f \rightarrow V_o$}}、オペアンプ内部に {{手書き: $i_1 = i_f + 0$}}、図の下部に {{手書き: ④ $f(v_i, v_o) = ?$}} の書き込み]

But $v_1 = v_2 = 0$ for an ideal op amp, since the noninverting terminal is grounded. Hence,

$$\frac{v_i}{R_1} = -\frac{v_o}{R_f}$$



or

$$v_o = -\frac{R_f}{R_1} v_i$$



The voltage gain is $A_v = v_o / v_i = -R_f / R_1$.

{{手書き: この回路において、非反転入力は接地されている。}}
{{手書き: $v_i$ は $R_1$ を介して、反転入力に接続されている。また、帰還抵抗 $R_f$ は}}
{{手書き: 反転入力と出力の間を接続している。}}
{{手書き: 私たちの目標は、入力電圧 $v_i$ と出力電圧 $v_o$ の間の関係を得ることである}}
{{手書き: KCLを節点1に適用する。}}
{{手書き: $i_1$ は $i_f$ と等しい。よって、$v_i$ から $v_1$ を引いたものを $R_1$ で割ったものは、}}
{{手書き: $v_1$ から $v_o$ を引いたものを $R_f$ で割ったものと等しい。}}
{{手書き: しかし、$v_1$ と $v_2$ は等しくその値は $0$ であることから、非反転端子は接地されている。}}
{{手書き: （`しかし、` と `$v_1$` の間に挿入記号で）理想的な演算増幅機において、}}
{{手書き: ゆえに、$v_i$ を $R_1$ で割ったものは $v_o$ を $R_f$ で割ったものの正負を反転させたものと}}
{{手書き: 等しく、$v_o$ は、$R_f$ を $R_1$ で割ったものと $v_i$ の積の正負を反転させたものと等しい。}}
{{手書き: この電圧増幅率は、$A_v$ であり、その値は $v_o$ を $v_i$ で割ったものと等しく、}}
{{手書き: その値は $R_f$ を $R_1$ で割ったものの正負を反転させたものと等しい。}}

{{採点: 確認印（26.10.23）}}

---

## p.5

電子回路Ⅱ 3 （{{手書き: 10}} / {{手書き: 23}} 講義分）

1. Summarize the following text in Japanese.



In this case, the input voltage $v_i$ is applied directly at the noninverting input terminal, and resistor $R_1$ is connected between the ground and the inverting terminal. We are interested in the output voltage $v_o$ and the voltage gain $A_v$. Application of KCL at the inverting terminal gives

$$i_1 = i_2 \Rightarrow \frac{0 - v_1}{R_1} = \frac{v_1 - v_o}{R_f} \quad (1)$$



[図: 非反転増幅回路。接地から抵抗 $R_1$（電流 $i_1$）を介してオペアンプの$-$端子（電圧 $v_1$）へ接続。$+$端子（電圧 $v_2$）には入力電圧 $v_i$ が直接印加。$-$端子と出力 $v_o$ の間に帰還抵抗 $R_f$（電流 $i_2$）が接続されている]

But $v_1 = v_2 = v_i$. The equation above becomes

$$\frac{-v_i}{R_1} = \frac{v_i - v_o}{R_f} \quad (2)$$



or

$$v_o = \left(1 + \frac{R_f}{R_1}\right) v_i \quad (3)$$



The voltage gain is $A_v = v_o / v_i = 1 + R_f / R_1$, which does not have a negative sign.

{{手書き: この回路において、入力電圧 $v_i$ は非反転入力端子に直接入力されている。}}
{{手書き: そして抵抗 $R_1$ は接地点と反転入力の間をつなげる。}}
{{手書き: 私たちは出力電圧 $v_o$ と電圧増幅率 $A_v$ に興味がある}}
{{手書き: キルヒホッフの電流則を反転入力に当てはめると、}}
{{手書き: $i_1$ は $i_2$ と等しい、つまり、$0$ と $v_1$ の差を $R_1$ で割った値は $v_1$ と $v_o$ の差を $R_f$ で割った値と等しい。}}
{{手書き: しかし、$v_1$ と $v_2$ と $v_i$ は等しい。よって、式は}}
{{手書き: 

$$\frac{-v_i}{R_1} = \frac{v_i - v_o}{R_f} \quad (2)$$

}}
{{手書き: となり、}}
{{手書き: 

$$v_o = \left(1 + \frac{R_f}{R_1}\right) v_i$$

}}
{{手書き: となる。電圧利得は $A_v = v_o / v_i = 1 + R_f / R_1$ であり、これは負ではない}}

2. Calculate the output voltage $v_o$ of a noninverting amplifier for values of $v_i = 2\text{ V}$, $R_f = 500\text{ k}\Omega$, $R_1 = 100\text{ k}\Omega$, $A_O = \infty$.



{{手書き: 

$$v_o = \frac{2\text{ V}}{100\text{ k}\Omega} \cdot 500\text{ k}\Omega + 2\text{ V}$$

}}
{{手書き: 

$$= 12\text{ V}$$

}}

[図: 非反転増幅回路。$R_1$ の上に {{手書き: $100\text{ k}\Omega$}}、$R_f$ の上に {{手書き: $500\text{ k}\Omega$}}、$v_i$ の下に {{手書き: $2\text{ V}$}}、オペアンプの下に {{手書き: $A_o = \infty$}} の書き込み]

3. Calculate the voltage gain $A_v$ of a noninverting amplifier for values of $R_f = 200\text{ k}\Omega$, $R_1 = 10\text{ k}\Omega$, $A_O = \infty$.



{{手書き: 

$$A_v = \frac{200}{10} + 1 = 20 + 1 = 21$$

}}

[図: 非反転増幅回路。$R_1$ の上に {{手書き: $10\text{ k}\Omega$}}、$R_f$ の上に {{手書き: $200\text{ k}\Omega$}}、オペアンプの下に {{手書き: $A_o = \infty$}} の書き込み]

{{採点: 確認印（26.10.23）}}

---

## p.6

電子回路Ⅱ （{{手書き: 11}} / {{手書き: 5}} 講義分）

1. Summarize the following text in Japanese.



Consider the op amp circuit shown in the figure. Keep in mind that zero currents enter the OP amp terminals. Applying KCL to node a and b,

$$\frac{v_1 - v_a}{R_1} = \frac{v_a - v_o}{R_2} \quad (1)$$



$$\frac{v_2 - v_b}{R_3} = \frac{v_b - 0}{R_4} \quad (2)$$



[図: 差動増幅回路。入力 $v_1$ が抵抗 $R_1$ を介して節点 $a$（電位 $v_a$、オペアンプの$-$端子）に接続され、節点 $a$ と出力 $v_o$ の間に抵抗 $R_2$ が接続されている。入力 $v_2$ が抵抗 $R_3$ を介して節点 $b$（電位 $v_b$、オペアンプの$+$端子）に接続され、節点 $b$ と接地の間に抵抗 $R_4$ が接続されている]

From Eq. (1) and (2), $v_a$ and $v_b$ are derived as follows, respectively.

$$v_a = \frac{R_1 v_o + R_2 v_1}{R_1 + R_2} \text{ , } v_b = \frac{R_4 v_2}{R_3 + R_4}$$



As $v_a$ is equal to $v_b$ for an ideal OP amp,

$$\frac{R_1 v_o + R_2 v_1}{R_1 + R_2} = \frac{R_4 v_2}{R_3 + R_4} \quad (3)$$



Therefore, we have the following equation.

$$v_o = \frac{R_1 + R_2}{R_1} \frac{R_4}{R_3 + R_4} v_2 - \frac{R_2}{R_1} v_1 \quad (4)$$



If $R_1 = R_3$ and $R_2 = R_4$ in Eq. (4), the output voltage $v_o$ is explained as

$$v_o = \frac{R_2}{R_1}(v_2 - v_2) \quad (5)$$


（右辺第2項の $v_2$ の添字 $2$ に重ねて {{手書き: $1$}}、その下に {{手書き: $1$}} の訂正書き込み）

{{手書き: 理解しなさい。演算増幅回路は以下の図に示されている。気をつけろ。ゼロ電流が演算増幅}}
{{手書き: 端子に入力されている。節点aとbにキルヒホッフの電流則を適用しろ。}}

2. Find $v_o$ given that $v_1 = 1\text{ V}$ and $v_2 = 2\text{ V}$.



[図: 差動増幅回路。入力 $v_1$ 側の抵抗が $2\text{k}$、帰還抵抗が $30\text{k}$、入力 $v_2$ 側の抵抗が $2\text{k}$、$+$端子と接地間の抵抗が $20\text{k}$、出力が $v_o$]
