# Provenance of ‘Deflating degrees of freedom: dirac16complex when $x_5, x_6, x_7$ deflate’ and of deflation.nb

## 1. The request

The user's instructions of 2026-10-30, verbatim:

```
next, study the case where x5, x6, and x7 are associated to metric components (call them g55, g66, g77) that each exponentially deflate (eg., g55 = b55*Exp[ - a*x4 ], where a>0 and b55>0. call   x5, x6, and x7  deflating degrees of freedom. Document your results, in entirety, in a new mathematica notebook named "deflation.nb".
```

```
'where x5, x6, and x7 are associated to metric components' means g55* (d x5 )^2 +g66* (d x6 )^2 +g77* (d x7 )^2 .
```

In the project $x_5, x_6, x_7$ are timelike. Asked whether they should stay timelike, the user answered:

```
-g55* (d x5 )^2 -g66* (d x6 )^2 -g77* (d x7 )^2 ; good catch of my error
```

and, asked what the remaining metric components should be:

```
Primordial field of 6planes.nb
```

Hence the line element used everywhere, with $z = 6Hx_0$:

$$
\begin{gathered}
ds^2 = \tan^2 z\,dx_0^2 + e^{-2Hx_4}\sin^{-1/3}z\,\left(dx_1^2 + dx_2^2 + dx_3^2\right) - dx_4^2 - g_{55}\,dx_5^2 - g_{66}\,dx_6^2 - g_{77}\,dx_7^2, \\
g_{jj} = b_{jj}\,e^{-ax_4}\ (j = 5, 6, 7),\quad a > 0,\quad b_{jj} > 0 .
\end{gathered}
$$

The standing rules of the project were followed: every document has a provenance file and a symbols file, each in Markdown, LaTeX and PDF, and each file contains every equation it uses.

## 2. Sources

- **Pre-gravity6plane.nb** (P. L. Nash, (C) 2022, GNU GPL). Used: the coordinates $X = \{x_0, \dots, x_7\}$ (cell 45); $\eta = \mathrm{diag}(1,1,1,1,-1,-1,-1,-1)$ (cell 66); $\sigma = \begin{pmatrix}0 & I_4\\ I_4 & 0\end{pmatrix}$ (cell 73); $\tau_A$ and $\bar\tau_A = \sigma(\sigma\tau_A)^T$ (cell 265), built from the self-dual and anti-self-dual $4\times4$ matrices and the six antisymmetric $8\times8$ matrices of the notebook; $T^A = (T16^A)[A] = \begin{pmatrix}0 & \bar\tau_A\\ \tau_A & 0\end{pmatrix}$ (cell 308); $\sigma_{16} = T^0T^1T^2T^3$ (cells 306, 333); the name "wave function for a Universe" for a mode function (cell 78); the vielbein of text cells 901 and 913, $\mathrm{diag}\left(\tan 6Hx_0,\ e^{-a_4(Hx_4)}\sin^{-1/6}6Hx_0\ (\times3),\ 1,\ e^{a_4(Hx_4)}\sin^{-1/6}6Hx_0\ (\times3)\right)$.
- **The primordial gravitational field of 6planes.nb** (this repository, 2026-10-30), chosen by the user: the vielbein above with $a_4(Hx_4) = Hx_4$, $\mathrm{diag}\left(\tan z,\ e^{-Hx_4}\sin^{-1/6}z\ (\times3),\ 1,\ e^{Hx_4}\sin^{-1/6}z\ (\times3)\right)$. In deflation.nb its last three entries are replaced by $e_j = \sqrt{b_{jj}}\,e^{-ax_4/2}$, so that $e_j^2 = g_{jj}$.
- **Code reused verbatim** from `code/6planes_src.txt`, the source of 6planes.nb: the construction of $T^A$ (Part 1.1), the exact Grassmann-algebra engine (Part 2), and the curved-space tools `spinConnection`, `covConst`, `christoffelG`, `riemannG`, `ricciG`, `einsteinG`, `kretschmannG` (Part 3). All other cells of deflation.nb were written for this work.
- **Standard results used** (textbook statements, not computed here):
  - Grassmann (Berezin) calculus with left derivatives and the order-reversing conjugation $(\theta\zeta)^* = \zeta^*\theta^*$ [F. A. Berezin, The Method of Second Quantization, Academic Press (1966)].
  - The tetrad (vielbein) formalism for spinors in curved space, and particle creation by time-dependent gravitational fields [L. Parker, Phys. Rev. 183, 1057 (1969); N. D. Birrell and P. C. W. Davies, Quantum Fields in Curved Space, Cambridge University Press (1982)].
  - The Poincare upper-half-space model $\frac{r^2}{w^2}(dw^2 + dy_5^2 + dy_6^2 + dy_7^2)$ of the hyperbolic 4-space of radius $r$, of constant sectional curvature $-1/r^2$ [J. G. Ratcliffe, Foundations of Hyperbolic Manifolds, Springer (1994)].
  - Indefinite (Krein) inner products [J. Bognar, Indefinite Inner Product Spaces, Springer (1974)].
  - The mean-field (Kohn-Sham) effective mass $m + \lambda\rho_s$ [W. Kohn and L. J. Sham, Phys. Rev. 140, A1133 (1965)].

## 3. Computations

All results are outputs of deflation.nb, produced with Wolfram Language 15.0.1 for Mac OS X ARM (64-bit) on 2026-10-30. The notebook is generated from `code/deflation_src.txt` (the concatenation of `code/deflation_head.txt` and `code/deflation_tail.txt`) by `code/build_deflation.wls`. The builder evaluates every input cell in the kernel with `EvaluationData` and writes the inputs, every message and every output into deflation.nb: 17 input cells, 0 messages, 28 s (log: `code/build_deflation.log`). Exact simplifications use the assumptions

$$
H > 0, \qquad 0 < x_0 < \frac{\pi}{12H}, \qquad a > 0, \qquad b_{55}, b_{66}, b_{77} > 0, \qquad x_0, \dots, x_7 \in \mathbb R, \qquad m, \lambda \in \mathbb R .
$$

### 3.1 Results and where they are computed

**Part 0, Out[1].** The diagonal of $\eta$ is $(1,1,1,1,-1,-1,-1,-1)$.

**Part 1.1, Out[2].** The eight matrices $T^A$, displayed.

**Part 1.2, Out[3]** (all True). The entries of $T^A$ are in $\{-1, 0, 1\}$; $T^0, \dots, T^3$ are symmetric and $T^4, \dots, T^7$ antisymmetric; and

$$
\begin{gathered}
T^AT^B + T^BT^A = 2\eta^{AB}I_{16}, \qquad \Gamma = T^0\cdots T^7 = \mathrm{diag}(-I_8, I_8), \qquad \sigma_{16} = \mathrm{diag}(-\sigma, \sigma), \\
(\sigma_{16}T^A)^T = -\sigma_{16}T^A, \qquad [S^{AB}, T^C] = \eta^{BC}T^A - \eta^{AC}T^B, \qquad S^{AB} = \tfrac14[T^A, T^B].
\end{gathered}
$$

**Part 2, Out[4]** (all True). $\psi_1\psi_2 + \psi_2\psi_1 = 0$, $\psi_1^2 = 0$, $(\psi_1^*\psi_1)^* = \psi_1^*\psi_1$.

**Part 3, Out[6]** (all True). For $K = -i\sigma_{16}T^4$, $\beta = -iT^4$ and $\Pi_\pm = \frac12(I_{16} \pm K)$: $K^\dagger = K$; $K^2 = I_{16}$; the eigenvalue $+1$ occurs 8 times and $-1$ occurs 8 times; $KT^A = T^AK$ ($A = 0..4$); $KT^A = -T^AK$ ($A = 5, 6, 7$); $\sigma_{16} = K\beta$. For $A = 0..4$, and also without $T^A$:

$$
\Pi_+\sigma_{16}T^A\Pi_- = 0, \qquad \Pi_+\sigma_{16}T^A\Pi_+ = \Pi_+\beta T^A\Pi_+, \qquad \Pi_-\sigma_{16}T^A\Pi_- = -\Pi_-\beta T^A\Pi_- .
$$

For $\psi = e^{-i\omega x_4}u$ with arbitrary complex $u$:

$$
\tfrac12\left(\bar\psi T^4\partial_4\psi - (\partial_4\bar\psi)T^4\psi\right) = \omega\,\psi^\dagger K\psi .
$$

**Part 4, Out[7].** With $e_0 = \tan z$, $e_{1,2,3} = e^{-Hx_4}\sin^{-1/6}z$, $e_4 = 1$, $e_j = \sqrt{b_{jj}}\,e^{-ax_4/2}$ and $g_{\mu\nu} = \eta_{AB}e^A{}_\mu e^B{}_\nu$: $e_j^2 = g_{jj}$ (True); $(\sqrt{\lvert g\rvert})^2 = \lvert\det g_{\mu\nu}\rvert$ (True); the entries of $g_{\mu\nu}$ for $\mu = 5, 6, 7$ equal $-g_{55}, -g_{66}, -g_{77}$ (True);

$$
g_{\mu\nu} = \mathrm{diag}\left(\tan^2 z,\ e^{-2Hx_4}\sin^{-1/3}z\ (\times3),\ -1,\ -b_{55}e^{-ax_4},\ -b_{66}e^{-ax_4},\ -b_{77}e^{-ax_4}\right),
$$

$$
\begin{gathered}
\sqrt{g_{55}} = \sqrt{b_{55}e^{-ax_4}}, \qquad \frac{d\ln\sqrt{g_{55}}}{dx_4} = -\frac a2, \qquad \sqrt{g_{55}g_{66}g_{77}} = \sqrt{b_{55}b_{66}b_{77}\,e^{-3ax_4}}, \\
\sqrt{\lvert g\rvert} = \sec z\,\sqrt{b_{55}b_{66}b_{77}\sin z}\;e^{-3(a+2H)x_4/2} .
\end{gathered}
$$

**Part 5, Out[8].** The full deflation field, with the Christoffel symbols, Riemann, Ricci and Einstein tensors

$$
\Gamma^\lambda{}_{\mu\nu} = \tfrac12 g^{\lambda\rho}(\partial_\mu g_{\rho\nu} + \partial_\nu g_{\rho\mu} - \partial_\rho g_{\mu\nu}), \qquad R^\kappa{}_{\lambda\mu\nu} = \partial_\mu\Gamma^\kappa{}_{\lambda\nu} - \partial_\nu\Gamma^\kappa{}_{\lambda\mu} + \Gamma^\kappa{}_{\mu\rho}\Gamma^\rho{}_{\lambda\nu} - \Gamma^\kappa{}_{\nu\rho}\Gamma^\rho{}_{\lambda\mu},
$$

$$
R_{\lambda\nu} = R^\kappa{}_{\lambda\kappa\nu}, \qquad R = g^{\lambda\nu}R_{\lambda\nu}, \qquad G_{\mu\nu} = R_{\mu\nu} - \tfrac12Rg_{\mu\nu}, \qquad R_{\kappa\lambda\mu\nu}R^{\kappa\lambda\mu\nu} = \sum \frac{g_{\kappa\kappa}}{g_{\lambda\lambda}g_{\mu\mu}g_{\nu\nu}}(R^\kappa{}_{\lambda\mu\nu})^2 ,
$$

gives

$$
R = \frac38\left[3(a^2 + 3aH - 32H^2) - 4(a^2 + 3aH + 32H^2)\cos 2z + a(a + 3H)\cos 4z\right]\csc^4 z ,
$$

$$
G^0{}_0 = -\frac3{16}\left[(a^2 + 3aH + 2H^2)(3 + \cos 4z) - 4(a^2 + 3aH + 6H^2)\cos 2z\right]\csc^4 z ,
$$

$$
G^i{}_i = -\frac3{16}\left[3a^2 + 6aH - 64H^2 - 4(a^2 + 2aH + 20H^2)\cos 2z + a(a + 2H)\cos 4z\right]\csc^4 z \quad (i = 1, 2, 3),
$$

$$
\begin{aligned}
G^4{}_4 &= \frac34(a^2 + 4H^2) - \frac3{16}\left[3(a^2 + 3aH - 32H^2) - 4(a^2 + 3aH + 32H^2)\cos 2z + a(a + 3H)\cos 4z\right]\csc^4 z \\
&= \frac34(a^2 + 4H^2) - \frac R2 ,
\end{aligned}
$$

$$
G^j{}_j = -\frac3{32}\left[3(a^2 + 4aH - 64H^2) - 4(a^2 + 4aH + 64H^2)\cos 2z + a(a + 4H)\cos 4z\right]\csc^4 z \quad (j = 5, 6, 7),
$$

$$
R_{04} = -3H^2\cot z \ \text{(the only non-zero } R_{\mu\nu},\ \mu < \nu\text{)}, \qquad G_{04} = R_{04}\ \text{(True)},
$$

$$
R_{\kappa\lambda\mu\nu}R^{\kappa\lambda\mu\nu} = \frac32\left[a^4 + 6a^2H^2 + 8H^4 + H^4(1245 + 108\cos 2z - \cos 4z)\cot^4 z\csc^4 z + 8H^4\cos^2 2z\,\csc^8 z\right].
$$

$R$, $G^\mu{}_\mu$, $R_{04}$ and the Kretschmann scalar do not contain $x_4$ (True), and

$$
\lim_{x_0 \to 0^+} x_0^4R = -\frac{7}{108H^2}, \qquad \lim_{x_0 \to 0^+} x_0^8\,R_{\kappa\lambda\mu\nu}R^{\kappa\lambda\mu\nu} = \frac{85}{69984H^4} .
$$

**Part 5, Out[9].** The pure deflation field $ds^2 = dx_0^2 + dx_1^2 + dx_2^2 + dx_3^2 - dx_4^2 - g_{55}dx_5^2 - g_{66}dx_6^2 - g_{77}dx_7^2$ gives $R = 3a^2$, $R_{\kappa\lambda\mu\nu}R^{\kappa\lambda\mu\nu} = 3a^4/2$, $G^\mu{}_\mu = -3a^2/2$ ($\mu = 0..3$) and $G^\mu{}_\mu = -3a^2/4$ ($\mu = 4..7$).

**Part 5, Out[10]** (all True). Every Riemann component of the pure deflation field with an index in $\{0,1,2,3\}$ vanishes. On the block $(x_4, x_5, x_6, x_7)$, $R_{\kappa\lambda\mu\nu} = \frac{a^2}{4}(g_{\kappa\mu}g_{\lambda\nu} - g_{\kappa\nu}g_{\lambda\mu})$ with $R_{\kappa\lambda\mu\nu} = g_{\kappa\rho}R^\rho{}_{\lambda\mu\nu}$. With $x_4 = \frac2a\ln\frac{aw}{2}$ and $x_j = y_j/\sqrt{b_{jj}}$, the metric of the block is $-\frac{4}{a^2w^2}I_4$ in the coordinates $(w, y_5, y_6, y_7)$, that is

$$
-dx_4^2 - g_{55}dx_5^2 - g_{66}dx_6^2 - g_{77}dx_7^2 = -\frac{4}{a^2}\,\frac{dw^2 + dy_5^2 + dy_6^2 + dy_7^2}{w^2} .
$$

**Part 6, Out[11].** For $p_5 = -g_{55}\dot x_5$, $\dot{} = d/d\ell$, and the normalization $-\dot x_4^2 - g_{55}\dot x_5^2 = -1$:

$$
\dot x_5 = -\frac{e^{ax_4}p_5}{b_{55}}, \qquad \dot x_4^2 = 1 - \frac{e^{ax_4}p_5^2}{b_{55}}, \qquad x_4^* = \frac1a\ln\frac{b_{55}}{p_5^2} .
$$

The following are True: $\frac12\,d(\dot x_4^2)/dx_4 = -\Gamma^4{}_{55}\dot x_5^2$; with $w = \frac2a e^{ax_4/2}$, $y_5 = \sqrt{b_{55}}x_5$ and $w_* = 2\sqrt{b_{55}}/(ap_5)$ ($p_5 > 0$), $(dw/dy_5)^2 = (w_*^2 - w^2)/w^2$; and $w(x_4^*) = w_*$.

**Part 7, Out[12].** With $\gamma^\mu = E_A{}^\mu T^A$, $D_\mu\psi = \partial_\mu\psi + \Omega_\mu\psi$, $\Omega_\mu = \frac14\omega_\mu{}^A{}_BT_AT^B$, $T_A = \eta_{AB}T^B$, $\omega_\mu{}^A{}_B = e^A{}_\nu(\partial_\mu E_B{}^\nu + \Gamma^\nu{}_{\mu\lambda}E_B{}^\lambda)$ and

$$
\mathcal L = \sqrt{\lvert g\rvert}\left[\tfrac12\left(\bar\psi\gamma^\mu D_\mu\psi - (D_\mu\bar\psi)\gamma^\mu\psi\right) - m\bar\psi\psi - \frac\lambda2(\bar\psi\psi)^2\right], \qquad D_\mu\bar\psi = \partial_\mu\bar\psi - \bar\psi\Omega_\mu ,
$$

the following are True:
- $\partial_\mu\gamma^\nu + \Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + [\Omega_\mu, \gamma^\nu] = 0$;
- $\mathcal L^* = \mathcal L$;
- $\partial^L\mathcal L/\partial\psi_a^* - \partial_\mu\,\partial^L\mathcal L/\partial(\partial_\mu\psi_a^*) = \left[\sqrt{\lvert g\rvert}\sigma_{16}(\gamma^\mu D_\mu\psi - m\psi - \lambda(\bar\psi\psi)\psi)\right]_a$ for all 16 components;
- $\mathcal L_m[\Gamma\psi^*] = \mathcal L_{-m}[\psi]$ and $\mathcal L_m[T^1\psi(R_1x)] = \mathcal L_{-m}[\psi](R_1x)$.

The computed values are

$$
\begin{gathered}
E_A{}^A = \left(\cot z,\ e^{Hx_4}\sin^{1/6}z\ (\times3),\ 1,\ e^{ax_4/2}/\sqrt{b_{55}},\ e^{ax_4/2}/\sqrt{b_{66}},\ e^{ax_4/2}/\sqrt{b_{77}}\right), \\
\gamma^\mu\Omega_\mu = -\frac32H\cot^2 z\,T^0 - \frac34(a + 2H)T^4 .
\end{gathered}
$$

**Part 8, Out[13].** True: $\gamma^\mu\partial_\mu F + F\gamma^\mu\Omega_\mu = 0$ for $F = \sin^{1/4}z\,e^{3(a+2H)x_4/4}$; $S^2 = \sum_{A\ne4}\eta_{AA}(c_Ak_A)^2I_{16}$ and $ST^4 + T^4S = 0$ for $S = \sum_{A\ne4}c_Ak_AT^A$, $c_A = 1/e_A$, $(k_A) = (k_0, k_1, k_2, k_3, 0, q_5, q_6, q_7)$. The dispersion relation is

$$
\omega^2 = m^2 - e^{ax_4}\left(\frac{q_5^2}{b_{55}} + \frac{q_6^2}{b_{66}} + \frac{q_7^2}{b_{77}}\right) + k_0^2\cot^2 z + e^{2Hx_4}(k_1^2 + k_2^2 + k_3^2)\sin^{1/3}z .
$$

With $\bar q^{\,2} = q_5^2/b_{55} + q_6^2/b_{66} + q_7^2/b_{77}$ the following are True: for $k_1 = k_2 = k_3 = 0$, $\omega^2 = m^2 + k_0^2\cot^2 z - e^{ax_4}\bar q^{\,2}$ and $d\omega^2/dx_4 = -ae^{ax_4}\bar q^{\,2}$; $\omega^2 = 0$ at $x_4^* = \frac1a\ln[(m^2 + k_0^2\cot^2 z)/\bar q^{\,2}]$; and at $a = 2H$, $\omega^2 = m^2 + k_0^2\cot^2 z + C_{2H}e^{2Hx_4}$ with the computed coefficient $C_{2H} = (k_1^2 + k_2^2 + k_3^2)\sin^{1/3}z - \bar q^{\,2}$. The exact limits $\lim_{x_4\to\infty}\omega^2$ for $H = 1$, $x_0 = 1/10$, $m = 1$, $k_0 = 0$, $k_1 = 1$, $k_2 = k_3 = 0$, $q_5 = 1$, $q_6 = q_7 = 0$, $b_{55} = b_{66} = b_{77} = 1$ are $-\infty$ ($a = 3$), $-\infty$ ($a = 2$) and $+\infty$ ($a = 1$).

**Part 8, Out[14].** True: in the pure deflation field $\gamma^\mu$ is covariantly constant and $\gamma^\mu\Omega_\mu = -\frac{3a}{4}T^4$; and for $\psi = e^{3ax_4/4}e^{i(k_1x_1 + q_5x_5)}\chi(x_4)$ with arbitrary $\chi$,

$$
\gamma^\mu D_\mu\psi - m\psi = e^{3ax_4/4}e^{i(k_1x_1 + q_5x_5)}\,T^4(\chi' - M\chi), \qquad M = T^4\left(ik_1T^1 + iq_5\frac{e^{ax_4/2}}{\sqrt{b_{55}}}T^5 - m\right).
$$

The numbers are listed in Section 3.2.

**Part 8, Out[15].** A figure with three panels: $N = \chi^\dagger\chi$ on a logarithmic scale with a dashed line at $x_4^* = \ln 8$; $P_-/N$; and $P_+$, $P_-$ on a logarithmic scale.

**Part 9, Out[16].** The matrix $(I_{16} + K)\sigma_{16}c_AT^A(I_{16} - K)$ vanishes for $A = 0, \dots, 4$ (True) and not for $A = 5, 6, 7$ (False, as expected). For $A = 5, 6, 7$ the absolute values of its entries are $0$ and $2e^{ax_4/2}/\sqrt{b_{jj}}$.

**Part 9, Out[17]** (all True). For real symbols $\kappa_A$ ($A \ne 4$) and $M = T^4(i\sum_{A\ne4}\kappa_AT^A - m)$:

$$
\sigma_{16}T^4 = iK, \qquad M^\dagger K + KM = 0, \qquad M^\dagger + M = 2iT^4(\kappa_5T^5 + \kappa_6T^6 + \kappa_7T^7), \qquad K(M^\dagger + M) + (M^\dagger + M)K = 0 .
$$

### 3.2 The numerical integration

The system $\chi' = T^4(ik_1T^1 + iq_5e^{ax_4/2}T^5/\sqrt{b_{55}} - m)\chi$ with $a = b_{55} = k_1 = m = 1$, $q_5 = 1/2$ was solved by the Wolfram Language function `NDSolve` on $-8 \le x_4 \le 5$ with `PrecisionGoal -> 10`, `AccuracyGoal -> 10`, `MaxSteps -> 10^6`. The initial vector $\chi(-8)$ is the normalized eigenvector of $\Pi_+h_0\Pi_+ + 10\,\Pi_-$, with $h_0 = -k_1T^4T^1 - imT^4$, whose eigenvalue is closest to $\sqrt{k_1^2 + m^2} = \sqrt2$. Because $h_0$ commutes with $K$, this matrix acts as $h_0$ on the $K = +1$ sector and as $10$ on the $K = -1$ sector, so $\chi(-8)$ is an eigenvector of $h_0$ with eigenvalue $\sqrt2$ in the $K = +1$ sector. The notebook confirms $\chi^\dagger h_0\chi = 1.4142135623730951$ and $\chi^\dagger\Pi_-\chi = 0$. Outputs, with $N = \chi^\dagger\chi$ and $P_\pm = \chi^\dagger\Pi_\pm\chi$:

- $x_4^* = \ln 8 = 2.0794415416798357$.
- $N$ at $x_4 = -8, 0, x_4^*, 3, 4, 5$: $1$, $1.067409453695482$, $1.9672504379730684$, $10.010160722635687$, $1198.1900459703008$, $1.0587953046760937\times10^{7}$.
- $P_-/N$ at $x_4 = -8, 0, x_4^*, 3, 5$: $1.232595164407831\times10^{-31}$, $0.03157622876752146$, $0.24583816482812526$, $0.45005076290732215$, $0.499999952776518$.
- $P_+$ at the same points: $1$, $1.033704688596978$, $1.4836252005444437$, $5.505080252588585$, $5.293977023380475\times10^{6}$.
- $P_-$ at the same points: $1.232595164407831\times10^{-31}$, $0.03370476509850364$, $0.4836252374286248$, $4.505080470047102$, $5.293976023380458\times10^{6}$.
- $Q = P_+ - P_-$ at the same points: $1$, $0.9999999234984744$, $0.999999963115819$, $0.999999782541483$, $1.0000000167638063$. The largest deviation from the exact value $1$ is $2.18\times10^{-7}$, the integration error.
- $\max_{x_4 = -8, -7, \dots, 5}\lvert P_-/N - (N - 1)/(2N)\rvert = 7.17543257486861\times10^{-7}$.

The guide quotes these numbers rounded, for example $1.067409$, $0.245838$, $5.293977\times10^6$ and $0.49999995$; the value $\sin^{1/3}(3/5) = 0.8265$ quoted with the limits was evaluated directly.

## 4. Derivations in the guide that combine computed identities

- $\Pi_-\sigma_{16}T^A\Pi_+ = 0$ is the Hermitian conjugate of $\Pi_+\sigma_{16}T^A\Pi_- = 0$, using $(\sigma_{16}T^A)^T = -\sigma_{16}T^A$, $\sigma_{16}^T = \sigma_{16}$ and $\Pi_\pm^\dagger = \Pi_\pm$.
- $(X + m)(X - m) = (\omega^2 - s^2 - m^2)I_{16}$ for $X = iS - i\omega T^4$ follows from $ST^4 + T^4S = 0$, $S^2 = s^2I_{16}$ and $(T^4)^2 = -I_{16}$; so non-zero $u$ with $(X - m)u = 0$ exist exactly when $\omega^2 = m^2 + s^2$.
- A frozen-coefficient mode obeys $\chi' = M\chi$ with $\kappa_A = c_Ak_A$: from $iS\chi + T^4\partial_4\chi = m\chi$ and $(T^4)^{-1} = -T^4$, $\partial_4\chi = T^4(iS - m)\chi$.
- $\frac{d}{dx_4}(\chi^\dagger K\chi) = \chi^\dagger(M^\dagger K + KM)\chi = 0$ and $\frac{d}{dx_4}(\chi^\dagger\chi) = \chi^\dagger(M^\dagger + M)\chi$; with $Q$ constant, $P_\pm = (N \pm Q)/2$ and $dP_+/dx_4 = dP_-/dx_4 = \frac12 dN/dx_4$.
- $\bar\psi\gamma^4\psi = \psi^\dagger\sigma_{16}T^4\psi = i\psi^\dagger K\psi$ because $E_4{}^4 = 1$ and $\sigma_{16}T^4 = iK$. In the pure deflation field $\sqrt{\lvert g\rvert} = \sqrt{b_{55}b_{66}b_{77}}\,e^{-3ax_4/2}$, so $\sqrt{\lvert g\rvert}\psi^\dagger K\psi = \sqrt{b_{55}b_{66}b_{77}}\,\chi^\dagger K\chi$ for $\psi = e^{3ax_4/4}e^{i(k_1x_1 + q_5x_5)}\chi$.
- $R = 12/(2/a)^2$ and $R_{\kappa\lambda\mu\nu}R^{\kappa\lambda\mu\nu} = 24/(2/a)^4$ are the values for a 4-dimensional space of constant curvature with $R_{\kappa\lambda\mu\nu} = \frac{a^2}{4}(g_{\kappa\mu}g_{\lambda\nu} - g_{\kappa\nu}g_{\lambda\mu})$: $R = 4\cdot3\cdot\frac{a^2}{4}$ and $R_{\kappa\lambda\mu\nu}R^{\kappa\lambda\mu\nu} = 2\cdot4\cdot3\cdot\left(\frac{a^2}{4}\right)^2$.
- The semicircles $(y_5 - y_{5c})^2 + w^2 = w_*^2$ solve $(dw/dy_5)^2 = (w_*^2 - w^2)/w^2$, since $dw/dy_5 = -(y_5 - y_{5c})/w$ on them.
- The friction-free form $\gamma^\mu D_\mu(F\chi) = F\gamma^\mu\partial_\mu\chi$ follows from $\gamma^\mu D_\mu(F\chi) = (\gamma^\mu\partial_\mu F + F\gamma^\mu\Omega_\mu)\chi + F\gamma^\mu\partial_\mu\chi$.

## 5. New in this work

The deflation field and its proper sizes; its exact Ricci, Einstein and Kretschmann curvature and their independence of $x_4$; the identification of the pure deflation block $(x_4, x_5, x_6, x_7)$ with an all-timelike hyperbolic 4-space of radius $2/a$; the turning point and semicircle geodesics; the field equation of dirac16complex in the deflation field; the exact friction-removing rescaling $F$; the dispersion relation with its turning point and the critical deflation rate $a_c = 2H$; the exact first-order equation $\chi' = M\chi$ and its numerical solution; and the pair-creation theorem from the conservation of the Krein charge.

## 6. Typesetting

The Markdown files are converted to LaTeX by `code/md2tex.py` (Python 3.14.7) and compiled with pdfTeX 3.141592653-2.6-1.40.29 (TeX Live 2026).
