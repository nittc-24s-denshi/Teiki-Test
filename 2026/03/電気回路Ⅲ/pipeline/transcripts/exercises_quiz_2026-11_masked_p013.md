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
