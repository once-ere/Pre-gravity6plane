# Provenance of 'dirac16complex: a second-quantized Pin(4,4) fermion field and the 6-planes it creates'

## 1. Sources

- **Pre-gravity6plane.nb** (P. L. Nash, (C) 2022, GPL), read in full. Used: coordinates $`X=\{x_0,\dots,x_7\}`$ (cell 45); $\eta=\mathrm{diag}(1,1,1,1,-1,-1,-1,-1)$ (cell 66); $\sigma$ (cell 73); $\tau_A$, $\bar\tau_A = \sigma(\sigma\tau_A)^T$ (cell 265); $`T^A=(T16^A)[A] = \begin{pmatrix}0&\bar\tau_A\\ \tau_A&0\end{pmatrix}`$ (cell 308); $\sigma_{16}=T^0T^1T^2T^3$ (cells 306, 333); the Universe wave function $\Psi_{16} = f16[k][x_0,x_4]$ (cell 78); the Lagrangian $L_a = \frac1H\Psi_{16}^T\sigma_{16}\sum_AT^A\partial_A\Psi_{16} + \frac{2M}H\Psi_{16}^T\sigma_{16}\Psi_{16}$ (cell 1057); its Euler-Lagrange equations eLa and the coupling sets $`\{0,5,8,13\},\{1,4,9,12\},\{2,7,10,15\},\{3,6,11,14\}`$ (cells 1072-1095); the variables $z = 6Hx_0$, $t = Hx_4$ (cell 61) and eLazt (cell 1099); the Maple exponential solutions with exponent $C(t+\frac z6) - \frac{M^2}{CH^2}(t-\frac z6)$ (cells 1172-1193); $z_{adv} = 6t+z$, $z_{ret}=6t-z$ and $\xi_{adv}=x_0-x_4$, $\xi_{ret}=x_0+x_4$ (cells 1203, 1246); vanishing bilinears of light-like quanta (cells 1208-1234); unit spinor $u = \frac1{\sqrt2}(1,0,0,0,1,0,0,0)$ (cells 783-801); frames $F_A{}^a$, $F_a{}^A$ (cells 888-893); vectorFormOfType1/Type2, the 7-planes $0 = V\cdot Z$, $M^6$ as their intersection and the count $\binom82 = 28$ (cells 1255-1294).
- **User instructions** (2026-10-30): define dirac16complex as a 16-component Pin(4,4) field with complex anticommuting Grassmann components, a second-quantized fermion field; use $(T16^A)[0..7]$ as Dirac matrices; add quadratic mass and quartic self-coupling terms (compare with Higgs couplings); mirror Pre-gravity6plane.nb and create 6-dimensional planes.
- **Standard physics** used: Grassmann (Berezin) calculus with left derivatives and order-reversing conjugation $`(\theta\eta)^* = \eta^*\theta^*`$; canonical quantization of fermions $`\{\psi_a(x),\pi_b(y)\} = i\delta_{ab}\delta(x-y)`$; Noether's theorem for $\psi\to e^{i\alpha}\psi$ giving $J^A = \bar\psi T^A\psi$; indefinite-metric (Krein space) quantization as used for example in Gupta-Bleuler quantization.

## 2. Computations (Wolfram Language 15.0.1, exact arithmetic, 2026-10-30)

All results quoted in the guide are outputs of 6planes.nb (generated from 6planes_src.txt by build_nb2.wls; 34 input cells, 0 messages):

| result | 6planes.nb |
|---|---|
| $T^A$ real, $`\{T^A,T^B\}=2\eta^{AB}I_{16}`$, $\sigma_{16}$ and $S^{AB}$ properties | Part 1, Out[3]-Out[6] |
| Grassmann engine checks | Part 2, Out[7] |
| $\mathcal L$ has 392 monomials, mass and quartic terms non-zero, $\mathcal L^*=\mathcal L$ | Part 3.2, Out[8] |
| EL equations equal $\sigma_{16}(T^A\partial_A\psi - m\psi - \lambda(\bar\psi\psi)\psi)$; conjugate equation | Part 3.3, Out[9]; component 0 in Out[10] |
| $\partial_AJ^A = 0$ on shell | Part 3.4, Out[11] |
| $K = -i\sigma_{16}T^4$ Hermitian, $K^2 = I$, spectrum $8\times(+1)$, $8\times(-1)$; $g_{45}^T\sigma_{16}T^4g_{45} = -\sigma_{16}T^4$; $\sigma_{16}=K\beta$ | Part 3.5, Out[12] |
| $[K,T^A]=0$ ($A\le4$), $`\{K,T^A\}=0`$ ($A\ge5$), no cross terms, $\pm$ sign of the two sectors | Part 3.6, Out[13] |
| eLa-analogue for dirac16complex depending on $x_0$, $x_4$, and its couplings | Part 4.1-4.2, Out[14]-Out[15] |
| exponential (Maple-family) solutions and plane waves solve the equation | Part 4.3, Out[16]-Out[17] |
| light-like quanta: $J^A = 0$, $\bar\psi\psi = 0$ | Part 4.4, Out[18] |
| $u^T\sigma u = 1$, $F_A{}^aF_a{}^A = I_8$ | Part 4.5, Out[19] |
| $M^6$: rank 2, 28 valid parameterizations, explicit $z_7$, $z_8$ | Part 4.6, Out[20] |
| pair 6-plane: rank 2 | Part 4.6, Out[21]-Out[22] |

The frames $F_A{}^a$, $F_a{}^A$ were also compared with the stored outputs (cells 889 and 891) of Pre-gravity6plane.nb: identical.

## 3. New in this work

The Grassmann-valued field, the order-reversing reality proof, the quartic term $-\frac\lambda2(\bar\psi\psi)^2$, the Krein-metric theorem with the explicit element $g_{45}=T^4T^5$, the mirror-sector decomposition $\mathcal L = \mathcal L_D[\psi_+] - \mathcal L_D[\psi_-] - \frac\lambda2(S_+-S_-)^2$, the identification of the old Maple solutions as the light-cone exponential family $(6p+q)(6p-q) = m^2/H^2$, the definition of $M^6$ through the real part of a complex Universe, and the pair 6-plane $M^6_{pair}$.
