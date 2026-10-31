# Symbols used in the README of Pre-gravity6plane

| symbol | definition |
|---|---|
| $x_0..x_7$ | coordinates: hidden, space (1-3), time (4), superluminal time (5-7) |
| $\eta$ | $\mathrm{diag}(1,1,1,1,-1,-1,-1,-1)$ |
| $\tau_A$, $\bar\tau_A$ | real 8x8 matrices of Pre-gravity6plane.nb, $\bar\tau_A = \sigma\tau_A^T\sigma$, $\sigma = \begin{pmatrix}0&I_4\\ I_4&0\end{pmatrix}$ |
| $T^A = (T16^A)[A]$ | $\begin{pmatrix}0&\bar\tau_A\\ \tau_A&0\end{pmatrix}$, real Dirac matrices |
| $S^{AB}$ | $\frac14[T^A,T^B]$ |
| $\Gamma$, $P_{L,R}$, $\sigma_{16}$ | $T^0\cdots T^7$; $\frac12(I_{16}\mp\Gamma)$; $T^0T^1T^2T^3$ |
| $\psi$, $\bar\psi$ | dirac16complex (complex Grassmann 16-spinor), $\bar\psi = \psi^\dagger\sigma_{16}$ |
| $\mathcal L$, $m$, $\lambda$ | Lagrangian, mass, quartic coupling |
| $K$ | $-i\sigma_{16}T^4$ |
| $\psi_\pm$, $S_\pm$, $\mathcal L_D$ | $K\psi_\pm = \pm\psi_\pm$; $S_\pm = \psi_\pm^\dagger(-iT^4)\psi_\pm$; $\mathcal L_D[\chi] = \chi^\dagger(-iT^4)(T^A\partial_A - m)\chi$ |
| $M$, $H$ | mass and Hubble parameters of Pre-gravity6plane.nb; $m = -2M$ |
| $z$, $t$, $p$, $q$ | $z = 6Hx_0$, $t = Hx_4$, mode $e^{pz+qt}u$ |
| $F_A{}^a$, $F_a{}^A$, $V_1$, $V_2$ | triality frames and vector forms: $V_1 = \eta(\psi_1^T\sigma F_A{}^a)$, $V_2 = F_a{}^A\psi_2$ |
| $n_k$, $Z$, $M^6$ | $n_k = V_k[\mathrm{Re}\,\psi]$; $Z\in\mathbb R^8$; $M^6 = \{Z : n_1\cdot Z = n_2\cdot Z = 0\}$ |
| $f$, $r_s$, $H_\Lambda$ | $1-r_s/x_0$ (modern), $1-r_s/x_0-H_\Lambda^2x_0^2$ (future) |
| $\gamma^\mu$, $D_\mu$ | $E_A{}^\mu T^A$; $\partial_\mu + \frac14\omega_\mu{}^A{}_BT_AT^B$ |
| $\rho_s$, $h_{KS}$, $\alpha$, $\beta$, $p$, $B$ | Kohn-Sham density, $\alpha p + BM\beta$, $-T^4T^0$, $-iT^4$, $-i\,d/d\rho$, lapse $e_4$ |
| $\Omega(T)$ | Kohn-Sham grand potential at temperature $T$ |
| $R_1$ | $x_1\mapsto-x_1$ |
| $R$, $\kappa$, $T_H$, $\epsilon$ | scalar curvature, surface gravity, $\kappa/2\pi$, Killing energy |
| $I_n$ | $n\times n$ identity matrix |
| $g_{jj}$, $b_{jj}$, $a$ | deflating metric functions $g_{jj} = b_{jj}e^{-ax_4}$ ($j = 5, 6, 7$), $a > 0$, $b_{jj} > 0$ |
| $w$, $y_j$ | coordinates of the deflating block: $w = \frac2ae^{ax_4/2}$, $y_j = \sqrt{b_{jj}}\,x_j$ |
| $\mathbb R^4$ | flat 4-space of $x_0, x_1, x_2, x_3$ |
| $\ell$, $p_5$, $x_4^*$ | affine parameter; $p_5 = -g_{55}\,dx_5/d\ell$; turning point $\frac1a\ln(b_{55}/p_5^2)$ |
| $\omega$, $k_0..k_3$, $q_5, q_6, q_7$ | frequency and wave numbers of a universe $e^{i(k_0x_0 + \dots + q_7x_7 - \omega x_4)}u$ (the indexed $q_j$ are wave numbers, not the exponent $q$); $u$ a constant spinor |
| $a_c$ | critical deflation rate $2H$ |
| $\chi$, $M$, $c_A$ | mode spinor with $\chi' = d\chi/dx_4 = M\chi$; $M = T^4(i\sum_{A\ne4}c_AT^A - m)$; real coefficients $c_A$ |
| $P_\pm$ | $\chi^\dagger\frac12(I_{16} \pm K)\chi$, weights of the +mass and -mass sectors |
