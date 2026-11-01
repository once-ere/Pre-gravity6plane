# Einstein-Rosen bridges in the gravitational fields of dirac16complex

Einstein and Rosen (Phys. Rev. 48, 73, 1935) replaced the Schwarzschild radius $r$ by $u$ with $u^2 = r - 2m$. Space is then described by two congruent sheets ($u>0$ and $u<0$) joined by the hypersurface $u = 0$ on which the metric determinant $g$ vanishes: the bridge. This document proves the existence of such bridges, analyses them for the three gravitational fields used for dirac16complex, and shows how a bridge pairs universes of energy $+\epsilon$ and $-\epsilon$. Every equation used is written here; all results are exact computations in 6planes.nb, Part 8.

## 1. The two bridges of Einstein and Rosen (verified)

**Neutral bridge.** With $u^2 = r - 2m$ the Schwarzschild metric becomes

```math
ds^2 = -\frac{u^2}{u^2+2m}\,dt^2 + 4(u^2+2m)\,du^2 + (u^2+2m)^2\left(d\theta^2 + \sin^2\theta\,d\phi^2\right).
```

Proven by exact computation: (a) $R_{\mu\nu} = 0$ (vacuum Einstein equations) for all $u$; (b) $\det g = -4u^2(u^2+2m)^4\sin^2\theta$, which vanishes exactly on the bridge $u = 0$; (c) the metric is even in $u$: the sheets $u>0$ and $u<0$ are congruent; (d) the curvature is finite on the bridge,

$$
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma} = \frac{48m^2}{(u^2+2m)^6}\quad\xrightarrow{u\to0}\quad\frac{3}{4m^4};
$$

(e) the area $4\pi(u^2+2m)^2$ of the spheres $`u = `$ const is minimal at $u = 0$: the bridge is a throat.

**Charged bridge** ($m = 0$, field energy of the electric field taken with the reversed sign, as in Einstein-Rosen). With $r^2 = u^2 + q^2$:

```math
ds^2 = -\frac{u^2}{u^2+q^2}\,dt^2 + du^2 + (u^2+q^2)\left(d\theta^2+\sin^2\theta\,d\phi^2\right),\qquad F_{tr} = \frac{q}{r^2},
```

$$
G_{\mu\nu} + 8\pi T^{EM}_{\mu\nu} = 0,\qquad T^{EM}_{\mu\nu} = \frac1{4\pi}\left(F_{\mu\alpha}F_\nu{}^\alpha - \tfrac14g_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}\right),
$$

verified exactly; $\det g = 0$ at $u = 0$ and $R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}\to 56/q^4$ (finite). A bridge without mass needs negative field energy, which is exactly what the $-$ universes of dirac16complex provide (Section 4).

## 2. Bridges of the modern and future fields

The modern and future fields of dirac16complex have the $(x_0,x_4)$ metric

```math
ds_2^2 = \frac{dx_0^2}{f(x_0)} - f(x_0)\,dx_4^2,\qquad f_{modern} = 1 - \frac{r_s}{x_0},\qquad f_{future} = 1 - \frac{r_s}{x_0} - H_\Lambda^2x_0^2,
```

times the flat transverse metric $dx_1^2+dx_2^2+dx_3^2-dx_5^2-dx_6^2-dx_7^2$. A horizon is a simple root $x_h$ of $f$. **Einstein-Rosen substitution:** $`x_0 = x_h + s\,u^2`$ with $s = +1$ if $f'(x_h)>0$ (black-hole type) and $s = -1$ if $f'(x_h) < 0$ (cosmological type). Then

```math
g_{uu} = \frac{4u^2}{f(x_h + su^2)} \xrightarrow{u\to0} \frac{4}{s\,f'(x_h)} = \frac{4}{\lvert f'(x_h)\rvert}\ (\text{finite, non-zero}),\qquad g_{44} = -f(x_h+su^2) \xrightarrow{u\to0} 0,
```

the metric is even in $u$ (two congruent sheets), and the scalar curvature of the full 8-dimensional metric equals that of the 2-dimensional part, $R = -f''(x_0)$, finite on the bridge. Results (exact or 12-digit):

| bridge | $x_h$ | $g_{uu}(0)$ | $g_{44}(0)$ | $R(0) = -f''(x_h)$ | surface gravity $\kappa = \lvert f'(x_h)\rvert/2$ |
|---|---|---|---|---|---|
| modern | $r_s$ | $4r_s$ | 0 | $2/r_s^2$ | $1/(2r_s)$ |
| future, black-hole horizon ($r_s=1$, $H_\Lambda=0.1$) | 1.0103126 | 4.16891046302 | 0 | 1.95937912 | 0.479741654 |
| future, cosmological horizon ($r_s=1$, $H_\Lambda=0.1$) | 9.4564927 | 22.4785613104 | 0 | 0.0223650467 | 0.0889736657 |

The horizons of the future field are the positive roots of $x_0 - r_s - H_\Lambda^2x_0^3 = 0$; the values of $g_{uu}(0)$ are exact algebraic numbers (roots of $373y^3 - 160000y \pm 640000 = 0$), confirmed by evaluating $g_{uu}$ at $u = 10^{-6}$.

**Theorem 1.** The modern field has one Einstein-Rosen bridge and the future field has two (at the black-hole and at the cosmological horizon). Each joins two congruent sheets through a hypersurface on which $g$ vanishes, with finite curvature.

## 3. The primordial field: a degenerate but singular bridge

In the primordial field (the vielbein of Pre-gravity6plane.nb with $a_4 = Hx_4$), $g_{00} = \tan^2 6Hx_0$ vanishes at $x_0 = 0$, $\det g = \sec^2 6Hx_0$, and the metric is even in $x_0$ if $\sin$ is replaced by $\lvert\sin\rvert$; formally two sheets are joined where $g_{00} = 0$. But the scalar curvature

$$
R = -\frac{3H^2}{2}\left(57 + 64\cos 12Hx_0 + 3\cos 24Hx_0\right)\csc^4 6Hx_0 = -\frac{31}{216H^2x_0^4} + O(x_0^{-2})
$$

diverges at $x_0 = 0$. **Theorem 2.** The degenerate hypersurface $x_0 = 0$ of the primordial field is a curvature singularity, not a regular Einstein-Rosen bridge.

## 4. A bridge creates universes in $`\{+\epsilon, -\epsilon\}`$ pairs

Near a bridge (non-degenerate horizon with surface gravity $\kappa$) use the tortoise coordinate $\rho$, $d\rho = dx_0/f$, and Kruskal coordinates

$$
U = -e^{-\kappa(x_4 - \rho)},\qquad V = e^{\kappa(x_4+\rho)}\quad\text{on sheet I},\qquad U > 0\ \text{on the second sheet}.
$$

A Kohn-Sham universe of Killing energy $\epsilon$ on sheet I behaves as $e^{-i\epsilon(x_4-\rho)} = (-U)^{i\epsilon/\kappa}$. The combination analytic in the lower half $U$-plane, $(U - i0)^{i\epsilon/\kappa}$, continues to the second sheet with the factor

$$
\frac{(e^{-i\pi}U)^{i\epsilon/\kappa}}{U^{i\epsilon/\kappa}} = e^{-\pi\epsilon/\kappa},
$$

and the resulting Bogoliubov coefficients give the fermion occupation

$$
\lvert\beta_\epsilon\rvert^2 = \frac{e^{-2\pi\epsilon/\kappa}}{1 + e^{-2\pi\epsilon/\kappa}} = \frac{1}{e^{2\pi\epsilon/\kappa}+1} = \frac1{e^{\epsilon/T_H}+1},\qquad T_H = \frac{\kappa}{2\pi},
$$

verified symbolically. Because the Killing time $x_4$ runs in opposite directions on the two sheets, the bridge (Kruskal, Hartle-Hawking) vacuum is a superposition of pairs: a universe of Killing energy $+\epsilon$ on one sheet together with its partner of Killing energy $-\epsilon$ on the other, with total Killing energy $H_I - H_{II} = 0$. Each sheet separately looks like a Kohn-Sham fermion gas at the Hawking temperature $T_H$; for the modern bridge $T_H = 1/(4\pi r_s) = 0.0795775$ for $r_s=1$, the first temperature in the thermodynamic table of the Kohn-Sham calculation.

**Theorem 3.** Across every regular bridge of Theorem 1, the bridge vacuum pairs each universe of energy $+\epsilon$ on one sheet with a universe of energy $-\epsilon$ on the other, with thermal (Fermi-Dirac) weight $1/(e^{\epsilon/T_H}+1)$.

Together with the mirror sectors of dirac16complex (a $+$ sector and a $-$ sector of opposite energy, created together at zero total energy), the bridges give a geometric picture of the pairs: the two sheets of a bridge host the $+\epsilon$ and $-\epsilon$ universes of a pair.

## 5. Honest scope

Theorems 1-3 are exact statements about the metrics written above. The modern and future fields are fixed backgrounds of the stated form, not solutions of the 8-dimensional Einstein equations sourced self-consistently by dirac16complex. The bridges of Theorem 1 are, like the original neutral bridge, not traversable: $g_{44}$ vanishes on the bridge. The primordial field has no regular bridge (Theorem 2). Theorem 3 is the standard Unruh-Israel-Hartle-Hawking pairing, applied to the Kohn-Sham universes of dirac16complex.
