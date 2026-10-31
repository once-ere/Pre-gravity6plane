import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, 'dm_data.json')))
def mat(M):
    rows = [' & '.join(('-1' if int(x) == -1 else '\\phantom{-}%d' % int(x)) for x in r) for r in M]
    return '\\left(\\begin{smallmatrix}\n' + ' \\\\\n'.join(rows) + '\n\\end{smallmatrix}\\right)'
def disp(lhs, M):
    return '$$\n' + lhs + ' = ' + mat(M) + '\n$$\n'
eta = 'diag(+1,+1,+1,+1,-1,-1,-1,-1)'
checks = D['checks']
CONSTR = r"""
## 2. Construction (exactly as in Pre-gravity6plane.nb)

Index conventions: capital Latin indices $A, B, C, D \in \{0,1,\dots,7\}$ label the eight Cartesian directions $x_0,\dots,x_7$; the flat metric is

$$
\eta^{AB} = \eta_{AB} = \mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1).
$$

The spinor metric of the 8-component spinors is

$$
\sigma = \begin{pmatrix} 0 & I_4 \\ I_4 & 0 \end{pmatrix}, \qquad \sigma^T = \sigma, \qquad \sigma^2 = I_8 .
$$

For $h \in \{1,2,3\}$ and $p, q \in \{1,2,3,4\}$ define the two $4\times 4$ arrays

$$
(Q_a^{h})_{pq} = \epsilon_{h p q 4}, \qquad (Q_b^{h})_{pq} = \delta_{p4}\,\delta_{qh} - \delta_{ph}\,\delta_{q4},
$$

where $\epsilon$ is the totally antisymmetric symbol with $\epsilon_{1234} = +1$, and the self-dual and anti-self-dual antisymmetric matrices

$$
s_h = Q_a^{h} - Q_b^{h}, \qquad t_h = Q_a^{h} + Q_b^{h}, \qquad \tfrac12 \epsilon_{pqrs}(s_h)_{rs} = (s_h)_{pq}, \qquad \tfrac12 \epsilon_{pqrs}(t_h)_{rs} = -(t_h)_{pq}.
$$

The eight real $8\times 8$ matrices $\tau_A$ are

$$
\tau_0 = I_8,\quad \tau_h = \begin{pmatrix} 0 & s_h \\ s_h & 0 \end{pmatrix}\ (h=1,2,3),\quad \tau_{3+j} = \begin{pmatrix} 0 & t_{4-j} \\ -t_{4-j} & 0 \end{pmatrix}\ (j=1,2,3),\quad \tau_7 = \tau_1\tau_2\tau_3\tau_4\tau_5\tau_6 ,
$$

their partners are

$$
\bar\tau_A = \sigma\,(\sigma\,\tau_A)^T = \sigma\,\tau_A^T\,\sigma ,
$$

and they satisfy (checked for all 64 pairs)

$$
\tfrac12\left(\tau_A\bar\tau_B + \tau_B\bar\tau_A\right) = \eta_{AB}\, I_8 .
$$

The eight real $16\times 16$ Dirac matrices are the reduced Brauer-Weyl generators

$$
T^A \equiv (T16^A)[A] = \begin{pmatrix} 0 & \bar\tau_A \\ \tau_A & 0 \end{pmatrix}, \qquad A = 0,1,\dots,7 .
$$

Further objects built from them:

$$
\Gamma \equiv (T16^A)[8] = T^0T^1T^2T^3T^4T^5T^6T^7, \qquad \sigma_{16} = T^0T^1T^2T^3, \qquad P_L = \tfrac12(I_{16}-\Gamma), \qquad P_R = \tfrac12(I_{16}+\Gamma),
$$

$$
S^{AB} = \tfrac14\left(T^A T^B - T^B T^A\right).
$$
"""
md = []
md.append('# dirac matrices: proof that the eight real 16x16 Dirac matrices (T16^A)[0..7] of dirac16complex are correct\n')
md.append('This file is the provenance proof requested for the eight real-valued $16\\times 16$ Dirac ("gamma") matrices $(T16^A)[0], \\dots, (T16^A)[7]$ that are used for the second-quantized Pin(4,4) spinor field dirac16complex. It shows the construction, displays every matrix, proves that the matrices are real and satisfy the Clifford anticommutation relations, proves that the scaled commutators generate Spin(4,4) and, together with the matrices themselves, Pin(4,4), and displays the products and the chiral projection matrices. Every equation used is written out in this file.\n')
md.append('## 1. Summary of what is proved\n')
md.append('1. Every entry of every $T^A$ is a real integer in $\\{-1,0,1\\}$ (Theorem 1).\n2. $T^A T^B + T^B T^A = 2\\eta^{AB} I_{16}$ for all $A,B$ (Theorem 2).\n3. The 28 scaled commutators $S^{AB}=\\tfrac14[T^A,T^B]$ ($A<B$) are linearly independent and close into the Lie algebra so(4,4); they exponentiate to Spin(4,4), a double cover of the identity component of SO(4,4); adding the eight reflections $T^C$ generates Pin(4,4), a double cover of the full group O(4,4) (Theorem 3).\n4. The 256 ordered products of the $T^A$ are linearly independent, so the $T^A$ generate the whole real Clifford algebra Cl(4,4) = M(16, R) (Theorem 4).\n5. The matrices are identical, entry by entry, to the matrices stored in the output cells of Pre-gravity6plane.nb (Theorem 5).\n')
md.append(CONSTR)
md.append('## 3. The eight real 8x8 matrices tau_A\n')
for A in range(8): md.append(disp('\\tau_{%d}' % A, D['tau'][A]))
md.append('## 4. The eight real 16x16 Dirac matrices (T16^A)[0..7]\n')
for A in range(8): md.append(disp('T^{%d} = (T16^A)[%d]' % (A, A), D['T'][A]))
md.append('## 5. Theorem 1 (reality)\n')
md.append('**Statement.** Every $T^A$ is a real matrix; its entries belong to $\\{-1,0,1\\}$.\n\n**Proof.** The building blocks $\\sigma$, $Q_a^h$, $Q_b^h$, $s_h$, $t_h$ have entries in $\\{-1,0,1\\}$ by their definitions (Levi-Civita symbols and Kronecker deltas). Products and transposes of signed permutation matrices are signed permutation matrices, so $\\tau_A$ and $\\bar\\tau_A = \\sigma\\tau_A^T\\sigma$ are signed permutation matrices, and so is the block matrix $T^A$. The sixteen rows of each $T^A$ displayed in Section 4 contain exactly one non-zero entry $\\pm1$ each. No complex number enters the construction. $\\square$\n\nComputer check: `%s` gives `%s`.\n' % ('all entries of T16A[0..7] are real integers in {-1,0,1}', checks['01 all entries of T16A[0..7] are real integers in {-1,0,1}']))
md.append('## 6. Theorem 2 (anticommutation relations)\n')
md.append('**Statement.**\n\n$$\nT^A T^B + T^B T^A = 2\\,\\eta^{AB}\\, I_{16}, \\qquad A,B = 0,\\dots,7 .\n$$\n\n**Proof.** With the block form of $T^A$,\n\n$$\nT^A T^B = \\begin{pmatrix} \\bar\\tau_A\\tau_B & 0 \\\\ 0 & \\tau_A\\bar\\tau_B \\end{pmatrix}, \\qquad T^A T^B + T^B T^A = \\begin{pmatrix} \\bar\\tau_A\\tau_B + \\bar\\tau_B\\tau_A & 0 \\\\ 0 & \\tau_A\\bar\\tau_B + \\tau_B\\bar\\tau_A \\end{pmatrix}.\n$$\n\nThe lower block equals $2\\eta_{AB} I_8$ by the identity $\\tfrac12(\\tau_A\\bar\\tau_B + \\tau_B\\bar\\tau_A) = \\eta_{AB} I_8$. Upper block: for $A=B$ that identity gives $\\tau_A\\bar\\tau_A = \\eta_{AA} I_8$, hence $\\bar\\tau_A = \\eta_{AA}\\tau_A^{-1}$ and $\\bar\\tau_A\\tau_A = \\eta_{AA} I_8$ (a one-sided inverse of a square matrix is two-sided). For $A\\neq B$ it reads $\\tau_A\\bar\\tau_B = -\\tau_B\\bar\\tau_A$, i.e. $\\eta_{BB}\\tau_A\\tau_B^{-1} = -\\eta_{AA}\\tau_B\\tau_A^{-1}$; multiplying by $\\tau_A^{-1}$ on the left and by $\\tau_A$ on the right gives $X^{-1} = -\\eta_{AA}\\eta_{BB}X$ for $X = \\tau_A^{-1}\\tau_B$, and therefore\n\n$$\n\\bar\\tau_A\\tau_B + \\bar\\tau_B\\tau_A = \\eta_{AA}X + \\eta_{BB}X^{-1} = \\eta_{AA}X - \\eta_{AA}X = 0 .\n$$\n\nAll 64 relations were also verified by exact integer arithmetic. $\\square$\n\nConsequences (all verified exactly):\n\n$$\n(T^A)^2 = \\eta^{AA} I_{16}, \\qquad (T^A)^{-1} = \\eta^{AA} T^A, \\qquad (T^A)^T = \\eta^{AA} T^A, \\qquad T^A T^B = -T^B T^A\\ (A \\neq B).\n$$\n\nThus $T^0,\\dots,T^3$ are real symmetric with square $+I_{16}$ and $T^4,\\dots,T^7$ are real antisymmetric with square $-I_{16}$.\n')
md.append('Table of $\\tfrac12\\{T^A,T^B\\}$ in units of $I_{16}$ (row $A$, column $B$):\n\n| A\\B | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |\n|---|---|---|---|---|---|---|---|---|\n' + '\n'.join('| %d | ' % A + ' | '.join(str(D['eta'][A][B]) for B in range(8)) + ' |' for A in range(8)) + '\n')
md.append('## 7. Products of the Dirac matrices\n')
md.append('Because $T^BT^A = -T^AT^B$ for $A\\neq B$ and $T^AT^A = \\eta^{AA}I_{16}$, every product of two Dirac matrices is, up to sign, one of the 28 products $T^AT^B$ with $A<B$, which we display. They are related to the scaled commutators by $S^{AB} = \\tfrac12 T^AT^B$ ($A \\neq B$).\n')
for p in D['products']: md.append(disp('T^{%d}T^{%d}' % (p['A'], p['B']), p['M']))
md.append('The product of all eight (the chirality matrix) and the two products of four:\n')
md.append(disp('\\Gamma = (T16^A)[8] = T^0T^1T^2T^3T^4T^5T^6T^7', D['Gamma']))
md.append(disp('\\sigma_{16} = T^0T^1T^2T^3', D['sigma16']))
md.append(disp('T^4T^5T^6T^7', D['T4567']))
md.append('## 8. Chirality and the chiral projection matrices\n')
md.append('$$\n\\Gamma = \\begin{pmatrix} -I_8 & 0 \\\\ 0 & I_8 \\end{pmatrix}, \\qquad \\Gamma^2 = I_{16}, \\qquad \\Gamma^T = \\Gamma, \\qquad \\Gamma T^A = -T^A\\Gamma .\n$$\n\nThe chiral projection matrices are\n\n$$\nP_L = \\tfrac12(I_{16} - \\Gamma) = \\begin{pmatrix} I_8 & 0 \\\\ 0 & 0 \\end{pmatrix}, \\qquad P_R = \\tfrac12(I_{16} + \\Gamma) = \\begin{pmatrix} 0 & 0 \\\\ 0 & I_8 \\end{pmatrix},\n$$\n\n$$\nP_L^2 = P_L,\\quad P_R^2 = P_R,\\quad P_LP_R = P_RP_L = 0,\\quad P_L + P_R = I_{16},\\quad \\mathrm{rank}\\,P_L = \\mathrm{rank}\\,P_R = 8,\\quad P_L T^A = T^A P_R .\n$$\n\nThe first eight components of a 16-component spinor (left, $P_L$) are the type-1 spinor and the last eight (right, $P_R$) the type-2 spinor of Spin(4,4); each $T^A$ maps one type into the other.\n')
md.append(disp('P_L', D['PL'])); md.append(disp('P_R', D['PR']))
md.append('## 9. Theorem 3: the scaled commutators generate Spin(4,4); with the reflections they generate Pin(4,4)\n')
md.append(r"""**Definitions.** The real Clifford algebra Cl(4,4) is generated by eight elements $e^A$ with $e^Ae^B + e^Be^A = 2\eta^{AB}$. A vector is $v = v_A e^A$ with $v\cdot v = \eta^{AB}v_Av_B$; it is a unit vector if $v\cdot v = \pm 1$. Pin(4,4) is the group of all finite products of unit vectors; Spin(4,4) is the subgroup of products of an even number of unit vectors; O(4,4) is the group of real $8\times8$ matrices $L$ with $L\eta L^T = \eta$. The twisted adjoint action of an invertible Clifford element $g$ of parity $|g|\in\{0,1\}$ on vectors is $\rho(g)v = (-1)^{|g|} g\,v\,g^{-1}$. In our representation $e^A \mapsto T^A$, and we write $\rho(g)T^C = \Lambda(g)^C{}_D\, T^D$.

**Lemma 1 (vector action).**

$$
[S^{AB}, T^C] = \eta^{BC}T^A - \eta^{AC}T^B .
$$

Proof: $S^{AB} = \tfrac12T^AT^B$ for $A\neq B$; using $T^BT^C = -T^CT^B + 2\eta^{BC}$ twice gives $T^AT^BT^C - T^CT^AT^B = 2\eta^{BC}T^A - 2\eta^{AC}T^B$. Verified for all 512 index triples.

**Lemma 2 (so(4,4) relations).**

$$
[S^{AB}, S^{CD}] = \eta^{BC}S^{AD} - \eta^{AC}S^{BD} - \eta^{BD}S^{AC} + \eta^{AD}S^{BC} .
$$

Proof: apply Lemma 1 to $S^{CD} = \tfrac14[T^C,T^D]$ and the Leibniz rule for commutators. Verified for all 4096 index quadruples.

**Lemma 3 (independence).** The 28 matrices $S^{AB}$, $A<B$, are linearly independent (the $28\times256$ matrix of their entries has rank 28). Hence they span a 28-dimensional real Lie algebra, which by Lemma 2 has the structure constants of so(4,4); the map $S^{AB}\mapsto$ (the matrix $L^{AB}$ with $(L^{AB})^C{}_D = \eta^{BC}\delta^A_D - \eta^{AC}\delta^B_D$) is a Lie algebra isomorphism onto so(4,4) by Lemma 1.

**Lemma 4 (one-parameter subgroups).** For $A\neq B$,

$$
(S^{AB})^2 = -\tfrac14\,\eta^{AA}\eta^{BB}\, I_{16},
$$

so there are 12 compact generators ($\eta^{AA}\eta^{BB}=+1$: both indices in $\{0,1,2,3\}$ or both in $\{4,5,6,7\}$) and 16 non-compact ones, and

$$
e^{\theta S^{AB}} = \cos\tfrac\theta2\, I_{16} + 2\sin\tfrac\theta2\, S^{AB}\ \ (\text{compact}), \qquad e^{\theta S^{AB}} = \cosh\tfrac\theta2\, I_{16} + 2\sinh\tfrac\theta2\, S^{AB}\ \ (\text{non-compact}).
$$

Since $2S^{AB} = T^AT^B$, each $e^{\theta S^{AB}}$ is a product of two unit vectors of the $(A,B)$-plane:

$$
e^{\theta S^{AB}} = \eta^{AA}\,T^A\left(c\,T^A + \eta^{AA} s\,T^B\right), \qquad (c,s) = (\cos\tfrac\theta2, \sin\tfrac\theta2)\ \text{or}\ (\cosh\tfrac\theta2, \sinh\tfrac\theta2),
$$

where $T^A$ and $n = c\,T^A + \eta^{AA}s\,T^B$ are unit vectors ($n^2 = \eta^{AA}(c^2 \pm s^2) = \eta^{AA}$ with the sign fixed by $\eta^{BB} = \pm\eta^{AA}$); hence $e^{\theta S^{AB}}\in$ Spin(4,4).

**Lemma 5 (covering).** For every generator and every real $\theta$ the matrix $\Lambda = \Lambda(e^{\theta S^{AB}})$ satisfies $\Lambda\eta\Lambda^T = \eta$ and $\det\Lambda = 1$ (exact symbolic check of all 28 one-parameter groups), and for the 12 compact generators

$$
e^{2\pi S^{AB}} = -I_{16}, \qquad \Lambda(-I_{16}) = I_8 ,
$$

so the homomorphism $\Lambda$ is two-to-one on the group generated by the $e^{\theta S^{AB}}$.

**Lemma 6 (reflections).** For each $C$, the twisted adjoint action of $T^C$ is the reflection in the hyperplane orthogonal to the $C$-th axis:

$$
\rho(T^C)\,T^D = -T^C T^D (T^C)^{-1} = \begin{cases} -T^C & D = C \\ +T^D & D\neq C \end{cases}, \qquad \det\rho(T^C) = -1 .
$$

**Theorem 3.** (i) The group generated by $\{e^{\theta S^{AB}}\}$ is the identity component of Spin(4,4), and $\Lambda$ maps it two-to-one onto the identity component SO$^+$(4,4). (ii) The group generated by $\{e^{\theta S^{AB}}\}$ together with the eight matrices $T^C$ is Pin(4,4), and $\rho$ maps it two-to-one onto O(4,4).

**Proof.** (i) By Lemma 4 the generated group lies in Spin(4,4) and is connected. By Lemma 3 its Lie algebra is (isomorphic to) so(4,4), so its image under $\Lambda$ is a connected Lie subgroup of O(4,4) (Lemma 5) whose Lie algebra is all of so(4,4); a connected Lie group is generated by any neighbourhood of the identity, so the image is SO$^+$(4,4). The kernel contains $-I_{16}$ (Lemma 5) and is contained in $\{\pm I_{16}\}$ because an element commuting with all $T^A$ is a multiple of the identity (the $T^A$ generate all of M(16,R), Theorem 4). (ii) By the Cartan-Dieudonne theorem every element of O(4,4) is a product of at most eight reflections in non-degenerate hyperplanes, i.e. of reflections along unit vectors $n$; every unit vector is $n = \Lambda(g)$ applied to a coordinate unit vector with $g$ in the group of (i) (SO$^+$(4,4) acts transitively on each sphere $n\cdot n=+1$ and $n\cdot n=-1$), and $\rho(g\,T^C g^{-1}) = \Lambda(g)\rho(T^C)\Lambda(g)^{-1}$, so all reflections, hence all of O(4,4), are reached. The generated group consists of products of unit vectors, i.e. it is Pin(4,4). The four connected components of O(4,4) are reached by $I_{16}$, $T^0$, $T^4$ and $T^0T^4$: the signs of the determinants of the space block and time block of $\rho$ are $(+,+)$, $(-,+)$, $(+,-)$ and $(-,-)$ respectively. $\square$

**Invariant form.** The spinor metric $\sigma_{16}$ satisfies

$$
\sigma_{16}^T = \sigma_{16},\qquad \sigma_{16}^2 = I_{16},\qquad (\sigma_{16}T^A)^T = -\sigma_{16}T^A,\qquad (\sigma_{16}S^{AB})^T = -\sigma_{16}S^{AB},
$$

so $\bar\psi\psi = \psi^\dagger\sigma_{16}\psi$ is invariant under Spin(4,4), $\psi \mapsto e^{\frac12\omega_{AB}S^{AB}}\psi$, and $\bar\psi T^A\psi$ transforms as a vector. Under a reflection $\psi\mapsto T^C\psi$ one has $(T^C)^T\sigma_{16}T^C = -\eta^{CC}\sigma_{16}$: the mass term changes sign for the four space-like reflections, which is the origin of the $\{+m,-m\}$ pairing of dirac16complex.
""")
md.append('## 10. Theorem 4: the 256 products form a basis (Cl(4,4) = M(16,R))\n')
md.append('Let $B_I = T^{A_1}T^{A_2}\\cdots T^{A_k}$ with $I = \\{A_1<\\dots<A_k\\}\\subseteq\\{0,\\dots,7\\}$ ($B_\\emptyset = I_{16}$); there are $\\sum_{k=0}^{8}\\binom8k = 256 = 16^2$ of them. The $256\\times256$ matrix of their entries has rank 256 and\n\n$$\n\\mathrm{Tr}\\left(B_I B_J^{-1}\\right) = 16\\,\\delta_{IJ},\n$$\n\nso the $B_I$ are a basis of all real $16\\times16$ matrices: the $T^A$ generate the full real Clifford algebra Cl(4,4) $\\cong$ M(16, R), the representation is faithful and irreducible over the reals, and $S^{AB}$ restricted to the two $8\\times8$ blocks gives the two inequivalent 8-dimensional spinor representations (type 1 and type 2): $S^{AB} = \\mathrm{diag}(D_{(1)}^{AB}, D_{(2)}^{AB})$ with $4D_{(1)}^{AB} = \\bar\\tau_A\\tau_B - \\bar\\tau_B\\tau_A$ and $4D_{(2)}^{AB} = \\tau_A\\bar\\tau_B - \\tau_B\\bar\\tau_A$.\n')
md.append('## 11. Theorem 5: identity with Pre-gravity6plane.nb\n')
md.append('The stored output cells of Pre-gravity6plane.nb were parsed and compared with the matrices of Sections 3-8: output cell 494 equals $(T^0,\\dots,T^7)$, cell 310 equals $\\Gamma = (T16^A)[8]$, cell 312 equals $\\sigma_{16}$, and cells 379 and 381 equal $P_L$ and $P_R$, entry by entry.\n')
md.append('## 12. Complete list of exact computer checks\n')
md.append('All checks were run with exact (integer or symbolic) arithmetic in Wolfram Language 15.0.1 by the script `verify_dirac_matrices.wls`; the result of every check:\n\n| check | result |\n|---|---|\n' + '\n'.join('| %s | %s |' % (k.replace('|', '/'), v.replace('|', '/')) for k, v in checks.items()) + '\n')
open(os.path.join(HERE, '..', 'dirac matrices.md'), 'w').write('\n'.join(md))
print('written', sum(len(x) for x in md))
