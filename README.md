# Pre-gravity6plane: the Pin(4,4) fermion field dirac16complex, its 6-planes, gravity, Kohn-Sham pair creation, Einstein-Rosen bridges and deflating degrees of freedom

This repository extends the Mathematica notebook Pre-gravity6plane.nb (P. L. Nash, (C) 2022, GNU General Public License) with a second-quantized fermion field, dirac16complex, and the calculations requested for it. Every equation and result stated below is computed with exact arithmetic (or a convergent numerical method where stated) in the notebooks 6planes.nb (Sections 1 to 4) and deflation.nb (Section 5).
This notebook is distributed as free software under the GNU General Public License.They are distributed in the hope that they will  be useful,but WITHOUT ANY WARRANTY;without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the GNU GPL for more details.

Please  cite  this  work  and this web page if you use it.

## 1. Setting

Coordinates $x_0,\dots,x_7$ ($x_0$ hidden space, $x_{1,2,3}$ space, $x_4$ time, $x_{5,6,7}$ superluminal time), metric $\eta = \mathrm{diag}(1,1,1,1,-1,-1,-1,-1)$. The eight real $16\times16$ Dirac matrices are those of Pre-gravity6plane.nb,

$$
T^A = (T16^A)[A] = \begin{pmatrix}0&\bar\tau_A\\ \tau_A&0\end{pmatrix},\qquad T^AT^B + T^BT^A = 2\eta^{AB}I_{16},\qquad S^{AB} = \tfrac14[T^A,T^B],
$$

with entries in $\{-1,0,1\}$; the $S^{AB}$ generate Spin(4,4) and, with the reflections $T^C$, Pin(4,4); $\Gamma = T^0\cdots T^7 = \mathrm{diag}(-I_8,I_8)$, $P_{L,R} = \frac12(I_{16}\mp\Gamma)$, $\sigma_{16} = T^0T^1T^2T^3$.

## 2. The field and its Lagrangian

dirac16complex $\psi = (\psi_0,\dots,\psi_{15})$ has complex anticommuting (Grassmann) components and is a second-quantized fermion field; $\bar\psi = \psi^\dagger\sigma_{16}$.

$$
\mathcal L = \tfrac12\left(\bar\psi T^A\partial_A\psi - (\partial_A\bar\psi)T^A\psi\right) - m\bar\psi\psi - \frac\lambda2(\bar\psi\psi)^2,\qquad T^A\partial_A\psi = (m + \lambda\bar\psi\psi)\psi .
$$

$\mathcal L$ is exactly real; the quadratic (mass) and quartic (self-coupling) terms are non-zero because the components are complex. Quantization with time $x_4$ gives $\{\psi_a,\psi_b^\dagger\} = K_{ab}\delta$, $K = -i\sigma_{16}T^4$, $K^2 = I$, with an (8,8) indefinite (Krein) metric, and an exact split into two mirror sectors of opposite energy: $\mathcal L = \mathcal L_D[\psi_+] - \mathcal L_D[\psi_-] - \frac\lambda2(S_+-S_-)^2$ for fields independent of $x_5,x_6,x_7$.

## 3. Mirror of Pre-gravity6plane.nb and the 6-planes

Restricted to configurations that depend only on $x_0$ and $x_4$, the analogue of the notebook's $\Psi_{16}(x_0,x_4)$ ($m = -2M$), the 16 field equations split into the four blocks $\{0,5,8,13\},\{1,4,9,12\},\{2,7,10,15\},\{3,6,11,14\}$, as in the old notebook; its exponential solutions $e^{pz+qt}u$ with $(6p+q)(6p-q) = m^2/H^2$, $z = 6Hx_0$, $t = Hx_4$, are exactly the Maple solutions of the old notebook. With the triality frames and vector forms $V_1 = \eta(\psi_1^T\sigma F_A{}^a)$, $V_2 = F_a{}^A\psi_2$, a Universe defines the 6-plane

$$
M^6 = \{Z\in\mathbb R^8 : n_1\cdot Z = 0,\ n_2\cdot Z = 0\},\qquad n_k = V_k[\mathrm{Re}\,\psi],
$$

with $\binom82 = 28$ parameterizations; a pair of universes of energies $\pm E$ creates the 6-plane $\{Z:\mathrm{Re}V_2\cdot Z = \mathrm{Im}V_2\cdot Z = 0\}$ by itself.

## 4. Gravity, Kohn-Sham DFT, pair creation, Einstein-Rosen bridges

Three gravitational fields (diagonal vielbeins): primordial $\mathrm{diag}(\tan6Hx_0,$ $e^{-Hx_4}\sin^{-1/6}6Hx_0\,(\times3),$ $1,$ $e^{Hx_4}\sin^{-1/6}6Hx_0\,(\times3))$ (the vielbein of Pre-gravity6plane.nb with $a_4 = Hx_4$); modern $\mathrm{diag}(f^{-1/2},1,1,1,f^{1/2},1,1,1)$ with $f = 1-r_s/x_0$; future the same with $f = 1 - r_s/x_0 - H_\Lambda^2x_0^2$. In each, the Euler-Lagrange equations derived from the Grassmann Lagrangian are $\gamma^\mu D_\mu\psi = (m+\lambda\bar\psi\psi)\psi$, e.g. (primordial)

$$
\begin{aligned}
&\cot(6Hx_0)T^0\partial_0\psi + e^{Hx_4}\sin^{\frac16}(6Hx_0)\sum_{i=1}^3T^i\partial_i\psi + T^4\partial_4\psi \\
&\qquad + e^{-Hx_4}\sin^{\frac16}(6Hx_0)\sum_{j=5}^7T^j\partial_j\psi - 3H\cot^2(6Hx_0)T^0\psi = (m+\lambda\bar\psi\psi)\psi .
\end{aligned}
$$

The quartic term is treated in a Kohn-Sham (DFT) approximation, $M = m + \lambda\rho_s$, with the Kohn-Sham Hamiltonian $h_{KS} = \alpha p + BM\beta$ ($\alpha = -T^4T^0$, $\beta = -iT^4$) in tortoise coordinates, ground and first-excited ($\Delta$SCF) states, and the finite-temperature thermodynamic effective potential $\Omega(T)$. Proven in each field: $\mathcal L_m[\Gamma\psi^*] = \mathcal L_{-m}[\psi]$ and $\mathcal L_m[T^1\psi(R_1x)] = \mathcal L_{-m}[\psi]$ (mass-sign pairing); $T^0h_{KS}T^0 = -h_{KS}$ and $h_{KS}^* = -h_{KS}$ (every level $\epsilon$ has a partner $-\epsilon$); in the zero-energy vacuum the creation of a $+$ universe pair together with a $-$ universe pair changes the energy by exactly 0, while single quanta and single-sign creation are forbidden by the conserved charges and energy: universes of masses $\{+m,-m\}$ are created in pairs. The 1935 Einstein-Rosen bridges are verified; the modern field has one and the future field two exact bridges (two congruent sheets, $g = 0$ on the bridge, finite curvature); the primordial field's degenerate hypersurface $x_0 = 0$ is a curvature singularity ($R \approx -\frac{31}{216H^2x_0^4}$); across a bridge the vacuum pairs universes of energy $+\epsilon$ and $-\epsilon$ with weight $1/(e^{\epsilon/T_H}+1)$, $T_H = \kappa/2\pi$.

## 5. Deflating degrees of freedom

In deflation.nb the superluminal times $x_5, x_6, x_7$ of the primordial field are replaced by deflating degrees of freedom ($z = 6Hx_0$):

$$
\begin{gathered}
ds^2 = \tan^2 z\,dx_0^2 + e^{-2Hx_4}\sin^{-1/3}z\,(dx_1^2 + dx_2^2 + dx_3^2) - dx_4^2 - g_{55}\,dx_5^2 - g_{66}\,dx_6^2 - g_{77}\,dx_7^2, \\
g_{jj} = b_{jj}e^{-ax_4},\quad a > 0,\ b_{jj} > 0 .
\end{gathered}
$$

Proper sizes along $x_5, x_6, x_7$ shrink as $\sqrt{b_{jj}}\,e^{-ax_4/2}$. The Ricci scalar, the Einstein tensor and the Kretschmann scalar depend on $x_0$ only, so deflation creates no curvature singularity at finite $x_4$. The pure deflation field $dx_0^2 + dx_1^2 + dx_2^2 + dx_3^2 - dx_4^2 - \sum_j g_{jj}dx_j^2$ is flat $\mathbb R^4$ times a hyperbolic 4-space of radius $2/a$ whose four directions are all timelike,

$$
-dx_4^2 - \sum_{j=5}^{7}g_{jj}\,dx_j^2 = -\frac{4}{a^2}\,\frac{dw^2 + dy_5^2 + dy_6^2 + dy_7^2}{w^2}, \qquad w = \frac2a\,e^{ax_4/2},\quad y_j = \sqrt{b_{jj}}\,x_j ,
$$

with $R = 3a^2$ and Kretschmann scalar $3a^4/2$. World lines with momentum $p_5 = -g_{55}\,dx_5/d\ell$ ($\ell$ an affine parameter) turn back in time at $x_4^* = \frac1a\ln(b_{55}/p_5^2)$. The field equation of dirac16complex, derived exactly from the Grassmann Lagrangian, is

$$
\begin{aligned}
&\cot z\,T^0\partial_0\psi + e^{Hx_4}\sin^{\frac16}z\sum_{i=1}^{3}T^i\partial_i\psi + T^4\partial_4\psi + e^{ax_4/2}\sum_{j=5}^{7}\frac{T^j\partial_j\psi}{\sqrt{b_{jj}}} \\
&\qquad - \frac32H\cot^2 z\,T^0\psi - \frac32\left(H + \frac a2\right)T^4\psi = (m + \lambda\bar\psi\psi)\psi .
\end{aligned}
$$

Its universes $e^{i(k_0x_0 + k_1x_1 + k_2x_2 + k_3x_3 + q_5x_5 + q_6x_6 + q_7x_7 - \omega x_4)}u$ (frozen coefficients) obey

$$
\omega^2 = m^2 + \cot^2 z\,k_0^2 + e^{2Hx_4}\sin^{1/3}z\,(k_1^2 + k_2^2 + k_3^2) - e^{ax_4}\sum_{j=5}^{7}\frac{q_j^2}{b_{jj}} ,
$$

so momentum along a deflating direction turns oscillation into exponential growth, and the critical deflation rate is $a_c = 2H$. Every mode equation $\chi' = d\chi/dx_4 = M\chi$ with $M = T^4(i\sum_{A\ne4}c_AT^A - m)$ and real $c_A$ satisfies $M^\dagger K + KM = 0$. So the Krein charge $\chi^\dagger K\chi = P_+ - P_-$ is conserved, where $P_\pm = \chi^\dagger\frac12(I_{16} \pm K)\chi$ are the weights of the +mass and -mass sectors, while only the deflating directions change the norm $P_+ + P_-$. Hence $P_+$ and $P_-$ grow by equal amounts: deflation creates {+mass, -mass} universes in pairs. In the exact numerical example the -mass fraction $P_-/(P_+ + P_-)$ grows from $1.2\times10^{-31}$ to $0.49999995$.

## 6. Assumptions and interpretations made in this work

1. The modern and future gravitational fields (not specified in the request) are defined as above; the primordial field is the notebook's vielbein with $a_4(Hx_4) = Hx_4$.
2. "Universe" means a mode function (c-number solution) of dirac16complex, as the notebook calls $\Psi_{16}$ the wave function of a Universe; its "mass" is its energy for translations of $x_4$ (or the mass parameter $m$ for the mass-sign theorem).
3. The theorems are exact statements about this model; they are not a proof about the physical universe.
4. In Section 5 the deflating components enter the line element as $-g_{jj}dx_j^2$ and all other components are those of the primordial field, as the user specified; the dispersion relation there uses frozen (adiabatic) coefficients.

## 7. Reproducing everything

```
cd code
wolframscript -file verify_dirac_matrices.wls ../Pre-gravity6plane.nb
wolframscript -file build_nb2.wls
wolframscript -file build_deflation.wls
python3 gen_dm.py
python3 md2tex.py <file>.md <file>.tex ; pdflatex <file>.tex
```

## 8. Repository inventory

| file | content |
|---|---|
| Pre-gravity6plane.nb | original notebook (P. L. Nash, GPL) |
| 6planes.nb | new notebook, evaluated, 34 input cells, no messages |
| deflation.nb | new notebook on the deflating degrees of freedom, evaluated, 17 input cells, no messages |
| README.md/.tex/.pdf | this overview |
| dirac matrices.md/.tex/.pdf | proofs and display of the eight real 16x16 Dirac matrices |
| dirac16complex_6planes.md/.tex/.pdf | the field, Lagrangian, quantization, mirror of the old notebook, 6-planes |
| gravity_DFT_pair_creation.md/.tex/.pdf | three gravitational fields, Euler-Lagrange equations, Kohn-Sham DFT, pair theorems |
| einstein_rosen_bridges.md/.tex/.pdf | Einstein-Rosen bridges |
| deflation.md/.tex/.pdf | deflating degrees of freedom: geometry, curvature, geodesics, field equation, universes, pair creation |
| *_provenance.md/.tex/.pdf | sources and computations behind each document |
| *_symbols.md/.tex/.pdf | definitions of all symbols of each document |
| code/ | core.wl, verify_dirac_matrices.wls (+ log), dm_data.json, gen_dm.py, md2tex.py, 6planes_src.txt, build_nb2.wls (+ log), deflation_head.txt, deflation_tail.txt, deflation_src.txt, build_deflation.wls (+ log) |

# Pre-Universe

[Whenever possible, we try to follow ROBERT L. BRYANT , 'SUBMANIFOLDS AND SPECIAL STRUCTURES ON THE OCTONIANS', J. DIFFERENTIAL GEOMETRY 17 (1982) 185-232; any ERRORS ARE DEFINITELY due to ME]

<!-- testing (please ignore):  $\bar{SO(4,4;\mathbb{R})}$ $\overline{SO(4,4;\mathbb{R})}$ $\overline{{SO(4,4;\mathbb{R})}}$ $\overline{[SO(4,4;\mathbb{R})]}$  -->



Let
$\mathbb{R}^{4,4}$
denote a real, eight-dimensional, pseudo-Euclidean vector space
endowed with  the $SO(4,4;\mathbb{R})$ invariant
quadratic form

$x0^{2} + x1^{2} + x2^{2} + x3^{2}
− x4^{2} - x5^{2} - x6^{2} - x7^{2}$,

which
defines the standard pseudo-Euclidean norm on $\mathbb{R}^{4,4}$ and associated non-degenerate indefinite
inner product.

Let $\overline{SO(4,4;\mathbb{R})}$
denote the universal cover  of $SO(4,4;\mathbb{R})$.

Spinor notation:

“left-handed” and
“right-handed” spin(8) spinors have
$\overline{SO(4,4;\mathbb{R})}$ counterparts
that are denoted as $\psi_1$ and $\psi_2$ in this repo.


<!-- ${\Large ***In this draft the phrase  'Pre-Universe' is intended to intimate***}$  -->

<span style="font-size: 30px;">***In this draft the phrase  'Pre-Universe'***</span>

<!--<span style="font-size: 2.5em;">***In this draft the phrase  'Pre-Universe' is intended to intimate***</span>-->



describes a conjectured 'Quantum construction' of a Pre-Big-Bang ***spacetime***,

built using 

the split octonion algebra $O_{4,4}$ 

and

the (pseudo-) Clifford algebra $C_{4,4}$
(with multiplicative identity id)
generated by a set of 8 elements 
$e^{4,4}_A, \space A = 1-1,...8-1$
that anticommute with each other
and have square equal to $\pm$ id.

Explicitly, the generators $e^{4,4}_A,\space A=0, 1, ..., 7$ satisfy 

$$e^{4,4}_A e^{4,4}_B + e^{4,4}_B e^{4,4}_A  = id \space g_{A B} , \space A, B = 0, 1, ..., 7$$

where

$$g_{A B}=diag(1,1,1,1,-1,-1,-1,-1)$$.

The (scaled) skew-symmetrized products of the $e^{4,4}_A$,
formed from an irreducible representation of the $e^{4,4}_A$, 
are the infinitesimal generators of a
$16 = 2^{8/2}$-dimensional ,  reducible, basic spinor representation of $\overline{SO(4,4;\mathbb{R})}$.


# Dynkin Diagram for $D_4$ [SO(8) ; Spin(8)]

                        (left-handed, Type 1 Spinor)
                               O
                              /
                             /
                            /
                           /
                          /
        O --------------- O  (Adjoint)
     (Vector)              \
                            \
                             \
                              \
                               \
                                O
                         (right-handed, Type 2 Spinor)


### Node Legend:
* **Central Node:** Adjoint representation
* **Left Node (180°):** Vector representation 
* **Top-Right Node (60°):** Type 1 Spinor (left-handed spinor) representation
* **Bottom-Right Node (-60°):** Type 2 Spinor (right-handed spinor) representation


We represent spinors in this
16-component basic spinor representation
as

$\psi \in \mathbb{R}^{16} = \\{\psi_1,\psi_2\\}$ ,

which are realized according to

$$\psi \in \mathbb{R}^{16} = \\{\psi_1\in \mathbb{R}^{8}  \oplus \psi_2\in \mathbb{R}^{8}\\}$$

$$\psi_1 = \psi_1^a ,  a = 0, 1, ..., 7$$

$$\psi_2 = \psi_2^{(a)},  (a) \to a = 0, 1, ..., 7$$

[see split octonions, $O_{4,4}$ = Os, below];

# A Lagrangian  
for $\psi$ is defined,

Euler-Lagrange equaions solved,

vector forms of $\psi_1$  and $\psi_2$ calculated (please see 'split octonions' , below),

two  7-planes, respectively dual to the preceding two vectors, are computed,

the 6-plane of their intersection identified;

todo:

associate 6-plane with 3 generations of Einstein-Rosen 2-planes.



# This 
study of a possible 'Quantum construction' of a Pre-Big-Bang ***spacetime*** 
is also carved out using the split octonion inner product algebra 

$O_{4,4}$ = Os  

and  Cartan's 'triality' .

Recall:

several properties of the
split octonion inner product algebra Os are::

$$1 \in Os$$;

non-degenerate indefinite inner product

$$< , > : Os \times Os \mapsto \mathbb{R}$$

and a multiplication $Os \times Os \mapsto Os$
with unit $1 \in Os$ such that 

$$\forall x, y \in Os, $$
< x y,  x y > =  <x, x> <y, y>.


<1, 1> = 1;

For convenience's sake we will identify $\mathbb{R}$ with the 1-dimensional subalgebra of Os generated by $1 \in Os$.


We define the orthogonal compliment of 1 to be $Im \space Os \in Os$. 
It is a
proper subspace and we have 
$$Os = \mathbb{R} \oplus Im \space Os$$.

Given $x \in Os$, we define the conjugate $x^*$ according to

$x \mapsto x^* = 2 <x, 1> - x$;

We denote <x, 1> by Re x 

and (x - Re x) by Im x. 

Clearly $x \in Im \space Os$ if and only if $x^* = -x$ or x = Im x or Re x = 0.


# Let

$e_A, \space A=0, 1, ..., 7$, 
comprise a Minkowski vector basis of Os.

We are using the convention that 

# $e_0 \space =  \space 1$ 

A 'Minkowski' vector realization of $x \in Os$ is 

$x = x^A e_A,  \space A=0, 1, ..., 7$ where

$x^A \in \mathbb{R}$.


(equivalent [by Cartan's triality] to each of the two independent spinor bases; 
explicit realizations of equivalence
are constructed in this repo's files),

and verify

$< e_A, e_B > = g_{A,B} = diag(1,1,1,1,-1,-1,-1,-1)$,


Os is endowed with a non-associative multiplication 
$Os \times Os \mapsto Os$  , which may be defined according to

$e_A \space e_B = e_C \space m^C_{A \space B}$.

In this repo we construct the multiplication constants $m^C_{A \space B}$
from 

[1] our irrep of the Clifford algebra $C_{4,4}$ generators ;
and 

[2] a type 1 spinor u,

verifying < u, u > = 1.



# SPLIT OCTONION MULTIPLICATION TABLE $\space  \space e_A \space e_B$


$$\begin{array}{ccccccccc}
 \text{A/B} & e_0 & e_1 & e_2 & e_3 & e_4 & e_5 & e_6 &
   e_7 \\
 e_0 & e_0 & e_1 & e_2 & e_3 & e_4 & e_5 & e_6 & e_7 \\
 e_1 & e_1 & -e_0 & -e_3 & e_2 & -e_5 & e_4 & e_7 & -e_6
   \\
 e_2 & e_2 & e_3 & -e_0 & -e_1 & -e_6 & -e_7 & e_4 & e_5
   \\
 e_3 & e_3 & -e_2 & e_1 & -e_0 & -e_7 & e_6 & -e_5 & e_4
   \\
 e_4 & e_4 & e_5 & e_6 & e_7 & e_0 & e_1 & e_2 & e_3 \\
 e_5 & e_5 & -e_4 & e_7 & -e_6 & -e_1 & e_0 & -e_3 & e_2
   \\
 e_6 & e_6 & -e_7 & -e_4 & e_5 & -e_2 & e_3 & e_0 & -e_1
   \\
 e_7 & e_7 & e_6 & -e_5 & -e_4 & -e_3 & -e_2 & e_1 & e_0
   \\
\end{array}$$





Let

$e^{1/2}_a, \space a=0, 1, ..., 7$ comprise a type 1 spinor basis of Os.

A type 1 spinor $\Psi_1 \in Os$ may be realized according to 

$\Psi_1 = \psi_1^a \space e^{1/2}_a,  a = 0, 1, ..., 7 $, where

$\psi_1^a \in \mathbb{R}$.

Similarly, a type 2 spinor $\Psi_2 \in Os$ may be realized according to 

$\Psi_2 = \psi_2^{(a)} \space e^{1/2}_{(a)}, \space (a) = (0), (1), ..., (7)$, where

$\psi_2^{(a)} \in \mathbb{R}$, and

and the $e^{1/2}_{(a)}, \space (a) = (0), (1), ..., (7)$ comprise a type 2 spinor basis of Os.



We restrict Spin(4,4) ( = $\overline{ SO(4,4) }$  ) transformations to the subgroups preserving
both $\mathbb{R}$  and Im Os,
i.e.,
restrict  to   Spin(3,4)

in which case $\Psi_1$  and  $\Psi_2$ transform the same way under 'allowed
Lorentz' transformations.

For brevity, understanding this restriction,
$\space (a) = (0), (1), ..., (7)  \space \to a = 0, 1, ..., 7$.



We are beginning to study 3-Generations of Einstein-Rosen 2-Plane-Bridges

BibTeX:
@article{Einstein Rosen 1935,author={Einstein,A.and Rosen,N.},title={The Particle Problem in the General Theory of Relativity},journal={Phys.Rev.},volume={48},issue={1},pages={73-- 77},year={1935},publisher={American Physical Society},doi={10.1103/PhysRev.48.73}},

for the case of
Einstein-Rosen 2-Plane-Bridges
$\in \space Os$

The origin of this calculation has its roots in 
"The Particle Problem in the General Theory of Relativity"
and
"A Remarkable Representation of the 3+2 de Sitter Group" by P.A.M.Dirac, J.Math.Phys.4,901\[Dash]909 (1963). 

The term "reduced Brauer\[Dash]Weyl generators",  refers to a specific set of irreducible generators for certain complex Clifford algebras, particularly in the context of mathematical physics and the study of Dirac spinors. These generators were introduced by E.A. Lord (E. A. Lord. "The Dirac spinor in six dimensions". Mathematical Proceedings of the Cambridge Philosophical Society, vol. 64, pp. 765\[Dash]778, 1968) and are described as "reduced" because they form an irreducible representation of the Clifford algebra   Subscript[\[ScriptCapitalC], 2 n]  from   Subscript[\[ScriptCapitalC], 2 (n-1)] .

Here,  we employ  Lord's  idea of reduced Brauer\[Dash]Weyl generators to extend Dirac's 4x4 gamma matrices into  this notebook's  real tau8  8x8 and  tau16   16x16 matrices,
which  are  employed  to write  down the 'Dirac Equation  for the Pre-Universe'
[remember, this is before  the  Big Bang,  and before  the particles  of  the  standard  model  exist ]
  formulated  in  terms  of a 16-component    Overscript[O(4,4), _] spinor \[CapitalPsi]16
(\[CapitalPsi]16  AKA 'WAVE FUNCTION OF  the UN-UNIVERSE,' which could possibly be named something more pompous).
This equation is used to  investigate EINSTEIN AND ROSEN's idea:
"If one tries to interpret the regular solution (5a)
in the space of r, 0, ø, t, one arrives at the following conclusion. The four-dimensional space is
described mathematically by two congruent
parts or "sheets," corresponding to u>0 and
u <0, which are joined by a hyperplane r= 2m or
u=0 in which g vanishes .2 We call such a connection between the two sheets a "bridge.""

PLEASE IGNORE, FOR NOW, THE FOLLOWING:

Notation:
$M_{4,4}$ = Minkowski spacetime,  signature = {4,4};

$O_{4,4}$ = Os =split octonion algebra;

with  vector  and spinor bases:
o\[Element]Subscript[\[DoubleStruckCapitalO], 4,4]; o =Subscript[eA, j] o^j=Subscript[ea\[Psi]1, j] o\[Psi]1^j=Subscript[ea\[Psi]2, j] (o\[Psi]2^j)   [Cartan's   triality]
=Subscript[\[Psi]1, j] ea^j=Subscript[ea, j] (\[Psi]2^j)  [restrict  to   Spin(3,4)];

<Subscript[ea, a],Subscript[ea, b]> = Subscript[\[Sigma], ab]
<Subscript[eA, A],Subscript[eA, B]> = Subscript[\[Eta], AB]
{X,EA}\[Element]Subscript[M, 4,4]\[CircleTimes]Subscript[\[DoubleStruckCapitalO], 4,4]
