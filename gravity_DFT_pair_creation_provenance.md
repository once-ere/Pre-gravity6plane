# Provenance of 'dirac16complex in the primordial, modern and future gravitational fields: Euler-Lagrange equations, Kohn-Sham DFT, and pair creation'

## 1. Sources

- **Pre-gravity6plane.nb** (P. L. Nash, (C) 2022, GPL): the real Dirac matrices $T^A = (T16^A)[A]$ (cell 308), $\sigma_{16} = T^0T^1T^2T^3$ (cell 306), $\Gamma = (T16^A)[8]$ (cell 309); the primordial vielbein, which the notebook displays in text cells 901 and 913 as $\mathrm{diag}(\tan 6Hx_0,\ e^{-a_4(Hx_4)}\sin^{-1/6}6Hx_0\ (\times3),\ 1,\ e^{a_4(Hx_4)}\sin^{-1/6}6Hx_0\ (\times3))$; the assumptions $\cot 6Hx_0>0$, $\sin 6Hx_0>0$ (cell 48), i.e. $0 < 6Hx_0 < \pi/2$; the commented-out curved Lagrangian with $\sqrt{\det g}$ and spin connection (cells 1052, 1062).
- **User instructions**: Euler-Lagrange equations for interaction with the primordial, modern and future gravitational fields; a DFT-motivated approximation with a Kohn-Sham fermion-gas thermodynamic effective potential employing ground- and first-excited-state computations; proof that universes of masses $`\{+m,-m\}`$ are created in pairs for each case. The user did not specify the modern and future fields or the inflationary function $a_4$: the choices $a_4(Hx_4) = Hx_4$ (primordial), $f = 1 - r_s/x_0$ (modern) and $f = 1 - r_s/x_0 - H_\Lambda^2x_0^2$ (future) are this work's definitions, chosen because the modern and future profiles possess static (Killing) horizons, the setting in which Einstein-Rosen bridges exist.
- **Standard physics and mathematics**: tetrad formalism and spin connection $`\omega_\mu{}^A{}_B = e^A{}_\nu(\partial_\mu E_B{}^\nu + \Gamma^\nu{}_{\mu\lambda}E_B{}^\lambda)`$; Kohn-Sham density-functional theory (W. Kohn and L. J. Sham, Phys. Rev. 140, A1133 (1965)) and its finite-temperature form (N. D. Mermin, Phys. Rev. 137, A1441 (1965)); the $`\Delta`$SCF method for excited states; the Nambu-Jona-Lasinio mean-field gap equation (Y. Nambu and G. Jona-Lasinio, Phys. Rev. 122, 345 (1961)); MIT bag boundary conditions; the Lambert function $W_0$ ($x_0 = r_s(1 + W_0(e^{\rho/r_s-1}))$ inverts $`\rho = x_0 + r_s\ln(x_0/r_s - 1)`$).

## 2. Computations (Wolfram Language 15.0.1, 2026-10-30)

| result | where computed |
|---|---|
| covariant constancy $`\partial_\mu\gamma^\nu + \Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + [\Omega_\mu,\gamma^\nu] = 0`$, sign of $\Omega_\mu$ | 6planes.nb Part 5, Out[23] (exact) |
| $\sqrt{\lvert g\rvert} = \sec 6Hx_0$, 1, 1 | Part 5, Out[23] |
| reality $\mathcal L^* = \mathcal L$ and EL equations $=\sqrt{\lvert g\rvert}\sigma_{16}(\gamma^\mu D_\mu\psi - m\psi - \lambda(\bar\psi\psi)\psi)$ in all three fields | Part 5, Out[23] (exact Grassmann algebra, 16 components, 8 coordinates) |
| spin-connection terms $-3H\cot^2 6Hx_0$, $\frac{r_s}{4\sqrt{x_0^3(x_0-r_s)}}$, $\frac{r_s - 2H_\Lambda^2x_0^3}{4\sqrt{x_0^3(x_0-r_s-H_\Lambda^2x_0^3)}}$ | Part 5, Out[23] |
| $\mathcal L_{m}[\Gamma\psi^*] = \mathcal L_{-m}[\psi]$, $`\mathcal L_m[T^1\psi(R_1x)] = \mathcal L_{-m}[\psi](R_1x)`$ | Part 5.1, Out[24] (exact) |
| algebra of $\alpha$, $\beta$, $K$, $T^0$ | Part 6.1, Out[25] (exact) |
| bag test $1.13204, 1.47963, 1.95318$ vs exact $1.13211, 1.47986, 1.95361$ | Part 6.2, Out[26] |
| table of Section 5 (V1, V2, $`\Delta`$SCF) | Part 6.3, Out[27] (machine precision; self-consistency tolerance $10^{-11}$; 51-55 iterations for V1) |
| $\Omega(T)$ table | Part 6.4, Out[29] |
| $\bar\psi\psi = S_+ - S_-$, $(\bar\psi\psi)^2 = S_+^2+S_-^2-2S_+S_-$, 232 monomials in $\lambda S_+S_-$, pair energy balance 0 | Part 7, Out[30] (exact) |

Independent prototypes of the curved-space and Kohn-Sham computations (scratch scripts grav_EL.wls and run_dft.wls) gave the same results before the notebook was assembled.

## 3. New in this work

The three gravitational fields as defined above; the complete Grassmann derivation of the curved Euler-Lagrange equations; the reduction of the Kohn-Sham problem to $h_{KS} = \alpha p + W\beta$ in tortoise coordinates with the exact $\pm$ symmetry and its staggered discretization; the two vacua $V_1$, $V_2$; Theorems 1-3 and their proofs.
