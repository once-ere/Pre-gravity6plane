# Symbols used in ‘Deflating degrees of freedom: dirac16complex when $x_5, x_6, x_7$ deflate’ and in deflation.nb

## 1. Coordinates, metric and deflation

| symbol | meaning | definition |
|---|---|---|
| $x_0, \dots, x_7$ | coordinates | $x_0$ hidden space; $x_1, x_2, x_3$ 3-space; $x_4$ time; $x_5, x_6, x_7$ superluminal time, here the deflating degrees of freedom |
| $i$; $j$ | index ranges | $i = 1, 2, 3$; $j = 5, 6, 7$ |
| $A, B, C$ | frame indices | $0, \dots, 7$ |
| $\mu, \nu, \kappa, \lambda, \rho$ | coordinate indices | $0, \dots, 7$; a $\lambda$ carrying no index position is the quartic coupling of Section 4 |
| $\eta_{AB}$, $\eta^{AB}$ | flat metric | $\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$ |
| $H$ | Hubble parameter of the primordial field | $H > 0$ |
| $z$ | scaled hidden coordinate | $z = 6Hx_0$, $0 < z < \pi/2$, i.e. $0 < x_0 < \pi/(12H)$ |
| $a_4(Hx_4)$ | function in the vielbein of Pre-gravity6plane.nb | $a_4(Hx_4) = Hx_4$ for the primordial field |
| $a$ | deflation constant | $a > 0$ |
| $b_{55}, b_{66}, b_{77}$ | deflation amplitudes | $b_{jj} > 0$ |
| $g_{55}, g_{66}, g_{77}$ | deflating metric functions (positive) | $g_{jj} = b_{jj}e^{-ax_4}$ |
| $e^A{}_\mu$, $e_A$ | vielbein | $\mathrm{diag}(e_0, \dots, e_7)$: $e_0 = \tan z$, $e_{1,2,3} = e^{-Hx_4}\sin^{-1/6}z$, $e_4 = 1$, $`e_j = \sqrt{b_{jj}}\,e^{-ax_4/2}`$ |
| $E_A{}^\mu$ | inverse vielbein | $E_A{}^\mu = \delta_A^\mu/e_A$ |
| $g_{\mu\nu}$, $g^{\mu\nu}$ | metric tensor and its inverse | $`g_{\mu\nu} = \eta_{AB}e^A{}_\mu e^B{}_\nu`$ $= \mathrm{diag}(\tan^2 z,$ $e^{-2Hx_4}\sin^{-1/3}z$ (three times), $-1, -g_{55}, -g_{66}, -g_{77})$ |
| $ds^2$ | line element | $g_{\mu\nu}dx^\mu dx^\nu$ |
| $\sqrt{\lvert g\rvert}$ | volume element | $e_0\cdots e_7$ $= \sqrt{b_{55}b_{66}b_{77}}\tan z\sin^{-1/2}z$ $\times e^{-3(H+a/2)x_4}$; $(\sqrt{\lvert g\rvert})^2 = \lvert\det g_{\mu\nu}\rvert$ |
| $L_j$ | proper size of $\Delta x_j$ | $`L_j = \sqrt{g_{jj}}\,\Delta x_j`$; $d\ln L_j/dx_4 = -a/2$ |
| pure deflation field | deflation alone | $ds^2 = dx_0^2 + dx_1^2 + dx_2^2 + dx_3^2$ $- dx_4^2 - g_{55}dx_5^2 - g_{66}dx_6^2 - g_{77}dx_7^2$ |

## 2. Dirac matrices, the field and its sectors

| symbol | meaning | definition |
|---|---|---|
| $I_n$ | identity matrix | $n\times n$ |
| $\delta_{pq}$, $\delta_A^\mu$ | Kronecker symbol | $1$ if the indices are equal, else $0$ |
| $\epsilon_{hpq4}$ | Levi-Civita symbol | totally antisymmetric, $\epsilon_{1234} = 1$ |
| $\sigma$ | 8x8 spinor metric | $`\begin{pmatrix}0 & I_4\\ I_4 & 0\end{pmatrix}`$ |
| $s_h$, $t_h$ ($h = 1,2,3$) | self-dual, anti-self-dual 4x4 matrices | $`(s_h)_{pq} = \epsilon_{hpq4} - \delta_{p4}\delta_{qh} + \delta_{ph}\delta_{q4}`$, $`(t_h)_{pq} = \epsilon_{hpq4} + \delta_{p4}\delta_{qh} - \delta_{ph}\delta_{q4}`$ |
| $\tau_A$ | real 8x8 matrices | $\tau_0 = I_8$; $`\tau_h = \begin{pmatrix}0 & s_h\\ s_h & 0\end{pmatrix}`$; $`\tau_4, \tau_5, \tau_6 = \begin{pmatrix}0 & t_k\\ -t_k & 0\end{pmatrix}`$ with $k = 3, 2, 1$; $\tau_7 = \tau_1\cdots\tau_6$ |
| $\bar\tau_A$ | barred matrices | $\bar\tau_A = \sigma(\sigma\tau_A)^T = \sigma\tau_A^T\sigma$ |
| $T^A = (T16^A)[A]$ | real 16x16 Dirac matrices | $`\begin{pmatrix}0 & \bar\tau_A\\ \tau_A & 0\end{pmatrix}`$, $T^AT^B + T^BT^A = 2\eta^{AB}I_{16}$ |
| $T_A$ | lowered Dirac matrices | $T_A = \eta_{AB}T^B$ |
| $\Gamma$ (no indices) | chirality matrix | $T^0T^1\cdots T^7 = \mathrm{diag}(-I_8, I_8)$ |
| $P_L$, $P_R$ | chiral projectors | $\frac12(I_{16} - \Gamma)$, $\frac12(I_{16} + \Gamma)$ |
| $\sigma_{16}$ | Dirac-adjoint matrix | $T^0T^1T^2T^3 = \mathrm{diag}(-\sigma, \sigma)$, symmetric, $(\sigma_{16}T^A)^T = -\sigma_{16}T^A$ |
| $S^{AB}$ | Spin(4,4) generators | $\frac14[T^A, T^B]$, $[S^{AB}, T^C] = \eta^{BC}T^A - \eta^{AC}T^B$ |
| $\psi$ = dirac16complex | 16-component complex Grassmann spinor field (second quantized) | $\psi = (\psi_0, \dots, \psi_{15})^T$, $\psi_a\psi_b = -\psi_b\psi_a$, $\psi_a\psi_b^* = -\psi_b^*\psi_a$ |
| $\theta$, $\zeta$ | arbitrary Grassmann elements | $`(\theta\zeta)^* = \zeta^*\theta^*`$ |
| $\psi^*$, $\psi^\dagger$ | complex conjugate, conjugate transpose | componentwise conjugation; $\psi^\dagger = (\psi^*)^T$ |
| $\bar\psi$ | Dirac adjoint | $\psi^\dagger\sigma_{16}$ |
| universe | mode function | a c-number solution of the linear field equation |
| $K$ | Krein operator | $-i\sigma_{16}T^4$, $K^\dagger = K$, $K^2 = I_{16}$, $\sigma_{16}T^4 = iK$ |
| $\beta$ | Hermitian involution | $-iT^4$; $\sigma_{16} = K\beta$ |
| $\Pi_\pm$ | sector projectors | $\frac12(I_{16} \pm K)$ |
| $\psi_\pm$ | mirror sectors | $\Pi_\pm\psi$; $K = +1$: +mass sector, $K = -1$: -mass sector |
| $\omega$ | frequency | mode $\propto e^{-i\omega x_4}$; energy density of a mode $\omega\psi^\dagger K\psi$ |
| $u$ | constant spinor | amplitude of a mode |

## 3. Curvature and geodesics

| symbol | meaning | definition |
|---|---|---|
| $\Gamma^\lambda{}_{\mu\nu}$ | Christoffel symbols | $\frac12g^{\lambda\rho}(\partial_\mu g_{\rho\nu} + \partial_\nu g_{\rho\mu} - \partial_\rho g_{\mu\nu})$ |
| $R^\kappa{}_{\lambda\mu\nu}$ | Riemann tensor | $`\partial_\mu\Gamma^\kappa{}_{\lambda\nu} - \partial_\nu\Gamma^\kappa{}_{\lambda\mu}`$ $`+ \Gamma^\kappa{}_{\mu\rho}\Gamma^\rho{}_{\lambda\nu} - \Gamma^\kappa{}_{\nu\rho}\Gamma^\rho{}_{\lambda\mu}`$ |
| $R_{\kappa\lambda\mu\nu}$ | lowered Riemann tensor | $g_{\kappa\rho}R^\rho{}_{\lambda\mu\nu}$ |
| $R_{\lambda\nu}$ | Ricci tensor | $R^\kappa{}_{\lambda\kappa\nu}$ |
| $R$ | Ricci scalar | $g^{\lambda\nu}R_{\lambda\nu}$ |
| $G_{\mu\nu}$, $G^\mu{}_\nu$ | Einstein tensor | $R_{\mu\nu} - \frac12Rg_{\mu\nu}$; $`G^\mu{}_\nu = g^{\mu\rho}G_{\rho\nu}`$ |
| $R_{\kappa\lambda\mu\nu}R^{\kappa\lambda\mu\nu}$ | Kretschmann scalar | diagonal metric: $\sum\frac{g_{\kappa\kappa}}{g_{\lambda\lambda}g_{\mu\mu}g_{\nu\nu}}(R^\kappa{}_{\lambda\mu\nu})^2$ |
| $\mathbb R^4$ | flat 4-space | spanned by $x_0, \dots, x_3$ in the pure deflation field |
| $H^4$ | hyperbolic 4-space of radius $2/a$ | metric $\frac{4}{a^2}\frac{dw^2 + dy_5^2 + dy_6^2 + dy_7^2}{w^2}$, $w > 0$ |
| $w$, $y_j$ | Poincare coordinates of the block $(x_4, \dots, x_7)$ | $w = \frac2ae^{ax_4/2}$, $`y_j = \sqrt{b_{jj}}\,x_j`$ |
| $\ell$ | affine parameter of a world line | $\dot x = dx/d\ell$ |
| $p_5$ | conserved momentum | $p_5 = g_{5\mu}\dot x^\mu = -g_{55}\dot x_5$ |
| $x_4^*$ | turning point | world line: $\frac1a\ln\frac{b_{55}}{p_5^2}$; universe: $`\frac1a\ln\frac{m^2 + \cot^2 z\,k_0^2}{\bar q^{\,2}}`$; numerical example: $\ln 8$ |
| $w_*$, $y_{5c}$ | radius and centre of a semicircle | $w_* = \frac{2\sqrt{b_{55}}}{a\lvert p_5\rvert}$; $(y_5 - y_{5c})^2 + w^2 = w_*^2$ |

## 4. Field equation, universes and pairs

| symbol | meaning | definition |
|---|---|---|
| $\gamma^\mu$ | curved-space Dirac matrices | $E_A{}^\mu T^A$ |
| $\omega_\mu{}^A{}_B$ | spin-connection coefficients | $`e^A{}_\nu(\partial_\mu E_B{}^\nu + \Gamma^\nu{}_{\mu\lambda}E_B{}^\lambda)`$ |
| $\Omega_\mu$ | spinor connection | $`\frac14\omega_\mu{}^A{}_BT_AT^B`$; here $`\gamma^\mu\Omega_\mu = -\frac32H\cot^2 z\,T^0 - \frac34(a + 2H)T^4`$ |
| $D_\mu$ | covariant derivative | $D_\mu\psi = \partial_\mu\psi + \Omega_\mu\psi$, $D_\mu\bar\psi = \partial_\mu\bar\psi - \bar\psi\Omega_\mu$ |
| $\mathcal L$, $\mathcal L_m$ | Lagrangian density (with mass $m$) | $\sqrt{\lvert g\rvert}[\frac12(\bar\psi\gamma^\mu D_\mu\psi - (D_\mu\bar\psi)\gamma^\mu\psi)$ $- m\bar\psi\psi - \frac\lambda2(\bar\psi\psi)^2]$ |
| $m$ | mass | real constant |
| $\lambda$ | quartic self-coupling | real constant |
| $\partial^L/\partial\psi_a^*$ | left Grassmann derivative | removes $\psi_a^*$ from the left; sign $(-1)^{\text{position} - 1}$ |
| $\mathcal C$ | mass-sign map | $`\mathcal C\psi = \Gamma\psi^*`$; $`\mathcal L_m[\Gamma\psi^*] = \mathcal L_{-m}[\psi]`$ |
| $P_1$, $R_1$ | mass-sign map, reflection | $P_1\psi(x) = T^1\psi(R_1x)$, $R_1: x_1 \mapsto -x_1$ |
| $\rho_s$ | mean-field scalar density | $\langle\bar\psi\psi\rangle$; effective mass $m + \lambda\rho_s$ |
| $F$ | friction-removing factor | $`\sin^{1/4}z\,e^{3(a+2H)x_4/4}`$, $\gamma^\mu\partial_\mu F + F\gamma^\mu\Omega_\mu = 0$ |
| $\chi$, $\chi'$ | rescaled spinor, its $x_4$-derivative | $\psi = F\chi$ (full field), $\psi = e^{3ax_4/4}e^{i(k_1x_1 + q_5x_5)}\chi$ (pure field); $\chi' = d\chi/dx_4$ |
| $k_0, \dots, k_3$; $q_5, q_6, q_7$; $k_A$ | wave numbers | mode $e^{i(k_0x_0 + \dots + q_7x_7 - \omega x_4)}u$; $k_5, k_6, k_7 \equiv q_5, q_6, q_7$, $k_4 = 0$ |
| $c_A$ | frozen coefficients | $c_A = E_A{}^A = 1/e_A$ |
| $S$, $s^2$ | spatial Dirac operator, its square | $S = \sum_{A\ne4}c_Ak_AT^A$, $S^2 = s^2I_{16}$, $s^2 = \sum_{A\ne4}\eta_{AA}(c_Ak_A)^2$ |
| $X$ | mode matrix | $iS - i\omega T^4$ |
| $`\bar q^{\,2}`$ | deflating momentum squared | $\frac{q_5^2}{b_{55}} + \frac{q_6^2}{b_{66}} + \frac{q_7^2}{b_{77}}$ |
| $a_c$ | critical deflation rate | $a_c = 2H$ |
| $C_{2H}$ | late-time coefficient at $a = 2H$ | $`(k_1^2 + k_2^2 + k_3^2)\sin^{1/3}z - \bar q^{\,2}`$ |
| $c(x_4)$ | coupling of the deflating direction $x_5$ | $e^{ax_4/2}/\sqrt{b_{55}}$ |
| $\kappa_A$ | real coefficients | $\kappa_A = c_Ak_A$ (frozen modes); $\kappa_1 = k_1$, $\kappa_5 = q_5c(x_4)$ (pure field) |
| $M$ | evolution matrix | $T^4(i\sum_{A\ne4}\kappa_AT^A - m)$; pure field: $T^4(ik_1T^1 + iq_5c(x_4)T^5 - m)$; $\chi' = M\chi$ |
| $h_0$ | Hamiltonian at $c = 0$ | $-k_1T^4T^1 - imT^4$, $\chi' = -ih_0\chi$ at $c = 0$ |
| $N$ | norm | $\chi^\dagger\chi = P_+ + P_-$ |
| $P_\pm$ | weights of the +mass and -mass sectors | $\chi^\dagger\Pi_\pm\chi$ |
| $Q$ | Krein charge | $\chi^\dagger K\chi = P_+ - P_-$, conserved: $M^\dagger K + KM = 0$ |
| $\bar\psi\gamma^4\psi$ | $x_4$-component of the U(1) current | $\psi^\dagger\sigma_{16}T^4\psi = i\psi^\dagger K\psi$ |

## 5. Names used in deflation.nb

| notebook name | symbol | definition |
|---|---|---|
| `X`, `eta4488` | $(x_0, \dots, x_7)$, $\eta_{AB}$ | coordinates; $\mathrm{diag}(1,1,1,1,-1,-1,-1,-1)$ |
| `ID4`, `ID8`, `ID16` | $I_4$, $I_8$, $I_{16}$ | identity matrices |
| `sigma`, `s4by4[h]`, `t4by4[h]` | $\sigma$, $s_h$, $t_h$ | Section 2 above |
| `Qa`, `Qb` | parts of $s_h$, $t_h$ | $\epsilon_{hpq4}$; $\delta_{p4}\delta_{qh} - \delta_{ph}\delta_{q4}$; $s_h = Qa - Qb$, $t_h = Qa + Qb$ |
| `sixAntiSymmetric8by8` | $\tau_1, \dots, \tau_6$ | Section 2 above |
| `tau[A]`, `taubar[A]` | $\tau_A$, $\bar\tau_A$ | Section 2 above |
| `T16A[A]` ($A = 0..7$) | $T^A$ | the matrices (T16^A)[A] of Pre-gravity6plane.nb |
| `T16A[8]`, `Gamma5` | $\Gamma$ | $T^0\cdots T^7$ |
| `sigma16`, `PL`, `PR`, `SAB` | $\sigma_{16}$, $P_L$, $P_R$, $S^{AB}$ | Section 2 above |
| `gen["psi", a, d]`, `gen["psiS", a, d]` | $\partial_d\psi_a$, $\partial_d\psi_a^*$ | Grassmann generators; `d` is the sorted list of derivative indices |
| `psi`, `psiS`, `dpsi[mu]`, `dpsiS[mu]` | $\psi$, $`\psi^*`$, $`\partial_\mu\psi`$, $`\partial_\mu\psi^*`$ | vectors of generators |
| `gClean`, `gSortSign`, `gFromMono` | bookkeeping | drop zero coefficients; sort generators with the sign of the permutation (zero if a generator repeats); build a monomial |
| `gAdd`, `gScale`, `gMul`, `gGen`, `gNum` | algebra operations | sum, multiplication by a number, Grassmann product, a generator, a number |
| `gDL`, `gDR` | left, right derivative | remove a generator at position $p$ of $k$ with sign $(-1)^{p-1}$, resp. $(-1)^{k-p}$ |
| `gDx[mu, x, X]` | total derivative $d/dx_\mu$ | Leibniz rule; a generator with derivative list $d$ goes to $`d \cup \{\mu\}`$ |
| `gConj` | complex conjugation | $`(c\,\theta_1\cdots\theta_k)^* = c^*\theta_k^*\cdots\theta_1^*`$ |
| `gBil[u, M, v]`, `gMatVec`, `gVecAdd`, `gVecScale` | bilinear form and vector operations | $\sum_{ab}u_aM_{ab}v_b$; $Mv$; $u + v$; $cu$ |
| `gZeroQ`, `gSimplify`, `gLinSub` | tests and substitution | element is zero; simplify coefficients; substitute each generator by a linear combination |
| `Sbil` | $\bar\psi\psi$ | `gBil[psiS, sigma16, psi]` |
| `K`, `betaKS`, `Pp`, `Pm` | $K$, $\beta$, $\Pi_+$, $\Pi_-$ | Section 2 above |
| `uv`, `om`, `psiM`, `enM` | $u$, $\omega$, $e^{-i\omega x_4}u$, mode energy density | $u$ = `ur` + i `ui` with real components |
| `spinConnection[e, X]` | $\Omega_\mu$, $`\Gamma^\lambda{}_{\mu\nu}`$, $`\gamma^\mu`$, $`g_{\mu\nu}`$ | for a diagonal vielbein `e` |
| `covConst` | covariant constancy test | $`\partial_\mu\gamma^\nu + \Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + [\Omega_\mu, \gamma^\nu] = 0`$ |
| `christoffelG`, `riemannG`, `ricciG`, `einsteinG`, `kretschmannG` | $`\Gamma^\lambda{}_{\mu\nu}`$, $`R^\kappa{}_{\lambda\mu\nu}`$, $R_{\lambda\nu}$, $G_{\mu\nu}$, $R_{\kappa\lambda\mu\nu}R^{\kappa\lambda\mu\nu}$ | Section 3 above (`kretschmannG` general metric) |
| `kretschmannDiag` | Kretschmann scalar | diagonal-metric formula of Section 3 above |
| `z0`, `gjj`, `eDefl`, `gDefl` | $z$, $(g_{55}, g_{66}, g_{77})$, $(e_0, \dots, e_7)$, $g_{\mu\nu}$ | Section 1 above |
| `assumD` | assumptions | $H > 0$, $0 < x_0 < \pi/(12H)$, $a > 0$, $b_{jj} > 0$, real coordinates, real $m$ and $\lambda$ |
| `sqrtgD` | $\sqrt{\lvert g\rvert}$ | $e_0\cdots e_7$ |
| `RicD`, `RsD`, `GmixD`, `KD` | $R_{\mu\nu}$, $R$, $G^\mu{}_\mu$, Kretschmann scalar | full deflation field |
| `gPure`, `RicP`, `RsP` | pure deflation metric, its $R_{\mu\nu}$ and $R$ | $\mathrm{diag}(1,1,1,1,-1,-g_{55},-g_{66},-g_{77})$ |
| `Y4`, `g4`, `RP`, `R4`, `R4low` | block coordinates and metric, Riemann tensors | $(x_4, x_5, x_6, x_7)$, $\mathrm{diag}(-1,-g_{55},-g_{66},-g_{77})$; $`R^\kappa{}_{\lambda\mu\nu}`$ of the pure field and of the block; $`R_{\kappa\lambda\mu\nu}`$ of the block |
| `xOfY`, `JacY`, `gW`, `w`, `y5`, `y6`, `y7` | Poincare map | $x_4 = \frac2a\ln\frac{aw}{2}$, $x_j = y_j/\sqrt{b_{jj}}$; Jacobian; block metric in $(w, y_5, y_6, y_7)$ |
| `p5`, `x5dot`, `x4dot2`, `Gam45` | $p_5$, $\dot x_5$, $\dot x_4^2$, Christoffel symbols of $(x_4, x_5)$ | Section 3 above |
| `wOf`, `wstar` | $w(x_4)$, $w_*$ | $\frac2ae^{ax_4/2}$, $2\sqrt{b_{55}}/(ap_5)$ |
| `scD`, `OmD`, `gamD`, `spinD` | spin connection data, $\Omega_\mu$, $\gamma^\mu$, $\gamma^\mu\Omega_\mu$ | full deflation field |
| `LD`, `realRuleD` | $\mathcal L$, reality rules | `realRuleD` sets $m^* = m$, $\lambda^* = \lambda$, $H^* = H$, $a^* = a$, $b_{jj}^* = b_{jj}$, $x_0^* = x_0$, $x_4^* = x_4$ |
| `ELD`, `DpsiD`, `expectedD` | Euler-Lagrange expressions, $\gamma^\mu D_\mu\psi$, expected form | expected form $\sqrt{\lvert g\rvert}\sigma_{16}(\gamma^\mu D_\mu\psi - m\psi - \lambda(\bar\psi\psi)\psi)$ |
| `ruleC`, `ruleP` | substitutions for $\mathcal C$ and $P_1$ | $`\psi_a \mapsto \Gamma_{ab}\psi_b^*`$, $`\psi_a^* \mapsto \Gamma_{ab}\psi_b`$; $\psi_a \mapsto T^1_{ab}\psi_b$ with $\partial_1 \mapsto -\partial_1$ |
| `FD`, `cD`, `kv`, `Sslash`, `omega2` | $F$, $c_A$, $k_A$, $S$, $\omega^2$ | Section 4 above |
| `qq`, `om0`, `x4starD`, `om2H`, `C2H` | $`\bar q^{\,2}`$, $\omega^2$ at $k_1 = k_2 = k_3 = 0$, $x_4^*$, $\omega^2$ at $a = 2H$, $C_{2H}$ | Section 4 above |
| `sampleD` | sample values | $H = 1$, $x_0 = 1/10$, $m = 1$, $k_0 = 0$, $k_1 = 1$, $k_2 = k_3 = 0$, $q_5 = 1$, $q_6 = q_7 = 0$, $b_{jj} = 1$ |
| `ePure`, `scP` | pure-field vielbein and spin connection | $(1, 1, 1, 1, 1,$ $\sqrt{b_{55}}e^{-ax_4/2},$ $\sqrt{b_{66}}e^{-ax_4/2},$ $\sqrt{b_{77}}e^{-ax_4/2})$ |
| `chiS`, `phaseP`, `psiP`, `DpsiP`, `Mchi` | $\chi$, phase, $\psi$, $\gamma^\mu D_\mu\psi - m\psi$, $M$ | phase $e^{3ax_4/4}e^{i(k_1x_1 + q_5x_5)}$ |
| `aN`, `bN`, `kN`, `mN`, `qN`, `x4star` | $a$, $b_{55}$, $k_1$, $m$, $q_5$, $x_4^*$ in the example | $1, 1, 1, 1, 1/2$; $\ln 8$ |
| `h0`, `Kp`, `Km`, `vals0`, `vecs0`, `start` | $h_0$, $\Pi_+$, $\Pi_-$, eigen-data, $\chi(-8)$ | eigenvector of $\Pi_+h_0\Pi_+ + 10\Pi_-$ with eigenvalue $\sqrt2$ |
| `cf`, `chiF`, `eqs`, `solChi`, `chiAt` | numerical $\chi$ | components, equations $\chi' = M\chi$, `NDSolve` solution, $\chi(x_4)$ |
| `normAt`, `minusFrac`, `plusW`, `minusW` | $N$, $P_-/N$, $P_+$, $P_-$ | Section 4 above |
| `crossD[A]` | sector cross term of direction $A$ | $(I_{16} + K)\sigma_{16}c_AT^A(I_{16} - K)$ |
| `kapA`, `Mdef`, `MdefH` | $\kappa_A$, $M$, $M^\dagger$ | $M = T^4(i\sum_{A\ne4}\kappa_AT^A - m)$ |
