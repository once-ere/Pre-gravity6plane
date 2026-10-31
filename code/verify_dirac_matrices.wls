(* verify_dirac_matrices.wls : rebuilds (T16^A)[0..7] exactly as Pre-gravity6plane.nb does, proves every property
   quoted in 'dirac matrices.md', compares with the stored outputs of Pre-gravity6plane.nb, and exports JSON data. *)
Get["core.wl"];
nbFile = If[Length[$ScriptCommandLine] > 1, $ScriptCommandLine[[2]], "Pre-gravity6plane.nb"];
etaE[A_, B_] := eta4488[[A + 1, B + 1]]; Sab[A_, B_] := SAB[[A + 1, B + 1]]; G = T16A[8];
res = <||>;
res["01 all entries of T16A[0..7] are real integers in {-1,0,1}"] = And @@ Table[SubsetQ[{-1, 0, 1}, Union[Flatten[T16A[A]]]], {A, 0, 7}];
res["02 {T^A,T^B} = 2 eta^AB I16 (64 pairs)"] = And @@ Flatten@Table[T16A[A].T16A[B] + T16A[B].T16A[A] == 2 etaE[A, B] ID16, {A, 0, 7}, {B, 0, 7}];
res["03 (T^A)^T = eta^AA T^A"] = And @@ Table[Transpose[T16A[A]] == etaE[A, A] T16A[A], {A, 0, 7}];
res["04 (T^A)^2 = eta^AA I16"] = And @@ Table[T16A[A].T16A[A] == etaE[A, A] ID16, {A, 0, 7}];
res["05 T^A T^B = -T^B T^A (A != B)"] = And @@ Flatten@Table[If[A != B, T16A[A].T16A[B] == -T16A[B].T16A[A], True], {A, 0, 7}, {B, 0, 7}];
res["06 Gamma = T^0...T^7 = diag(-I8,I8)"] = (G == ArrayFlatten[{{-ID8, 0}, {0, ID8}}]);
res["07 Gamma^2 = I16, Gamma^T = Gamma"] = (G.G == ID16 && Transpose[G] == G);
res["08 {Gamma,T^A} = 0"] = And @@ Table[G.T16A[A] == -T16A[A].G, {A, 0, 7}];
res["09 P_L, P_R: idempotent, orthogonal, complete, rank 8"] = (PL.PL == PL && PR.PR == PR && PL.PR == 0 ID16 && PR.PL == 0 ID16 && PL + PR == ID16 && MatrixRank[PL] == 8 && MatrixRank[PR] == 8);
res["10 P_L T^A = T^A P_R"] = And @@ Table[PL.T16A[A] == T16A[A].PR, {A, 0, 7}];
res["11 sigma16 = T^0T^1T^2T^3 = diag(-sigma,sigma), symmetric, sigma16^2 = I"] = (sigma16 == ArrayFlatten[{{-sigma, 0}, {0, sigma}}] && Transpose[sigma16] == sigma16 && sigma16.sigma16 == ID16);
res["12 sigma16 T^A antisymmetric"] = And @@ Table[Transpose[sigma16.T16A[A]] == -sigma16.T16A[A], {A, 0, 7}];
res["13 sigma16 S^AB antisymmetric (invariance of psibar psi)"] = And @@ Flatten@Table[Transpose[sigma16.Sab[A, B]] == -sigma16.Sab[A, B], {A, 0, 7}, {B, 0, 7}];
res["14 [S^AB,S^CD] = eta^BC S^AD - eta^AC S^BD - eta^BD S^AC + eta^AD S^BC (4096 cases)"] = And @@ Flatten@Table[Sab[A, B].Sab[C, D] - Sab[C, D].Sab[A, B] == etaE[B, C] Sab[A, D] - etaE[A, C] Sab[B, D] - etaE[B, D] Sab[A, C] + etaE[A, D] Sab[B, C], {A, 0, 7}, {B, 0, 7}, {C, 0, 7}, {D, 0, 7}];
res["15 [S^AB,T^C] = eta^BC T^A - eta^AC T^B (512 cases)"] = And @@ Flatten@Table[Sab[A, B].T16A[C] - T16A[C].Sab[A, B] == etaE[B, C] T16A[A] - etaE[A, C] T16A[B], {A, 0, 7}, {B, 0, 7}, {C, 0, 7}];
res["16 rank of the 28 S^AB (A<B)"] = MatrixRank[Flatten /@ Flatten[Table[Sab[A, B], {A, 0, 6}, {B, A + 1, 7}], 1]];
res["17 (S^AB)^2 = -(1/4) eta^AA eta^BB I16 (A != B)"] = And @@ Flatten@Table[Sab[A, B].Sab[A, B] == -(1/4) etaE[A, A] etaE[B, B] ID16, {A, 0, 6}, {B, A + 1, 7}];
res["18 number of compact / non-compact generators"] = {Count[Flatten@Table[etaE[A, A] etaE[B, B], {A, 0, 6}, {B, A + 1, 7}], 1], Count[Flatten@Table[etaE[A, A] etaE[B, B], {A, 0, 6}, {B, A + 1, 7}], -1]};
LambdaOf[g_] := Table[Tr[g.T16A[C].Inverse[g].T16A[D]] etaE[D, D]/16, {C, 0, 7}, {D, 0, 7}];
res["19 exp(theta S^AB) = cos/cosh closed form"] = And @@ Flatten@Table[Simplify[MatrixExp[th Sab[A, B]] - If[etaE[A, A] etaE[B, B] == 1, Cos[th/2] ID16 + 2 Sin[th/2] Sab[A, B], Cosh[th/2] ID16 + 2 Sinh[th/2] Sab[A, B]]] == 0 ID16, {A, 0, 6}, {B, A + 1, 7}];
res["20 Lambda(exp(theta S^AB)) in SO(4,4): Lambda eta Lambda^T = eta, det = 1"] = And @@ Flatten@Table[With[{L = Simplify[LambdaOf[MatrixExp[th Sab[A, B]]], th \[Element] Reals]}, {Simplify[L.eta4488.Transpose[L]] == eta4488, Simplify[Det[L]] == 1}], {A, 0, 6}, {B, A + 1, 7}];
res["21 exp(2 Pi S^AB) = -I16 for the 12 compact generators (double cover)"] = And @@ Flatten@Table[If[etaE[A, A] etaE[B, B] == 1, MatrixExp[2 Pi Sab[A, B]] == -ID16, True], {A, 0, 6}, {B, A + 1, 7}];
refl[g_] := Table[Tr[-g.T16A[C].Inverse[g].T16A[D]] etaE[D, D]/16, {C, 0, 7}, {D, 0, 7}];
res["22 twisted adjoint of T^C is the reflection diag(1,..,-1_C,..,1)"] = And @@ Table[refl[T16A[C]] == ID8 - 2 Outer[Times, UnitVector[8, C + 1], UnitVector[8, C + 1]], {C, 0, 7}];
blockdets[L_] := {Det[L[[1 ;; 4, 1 ;; 4]]], Det[L[[5 ;; 8, 5 ;; 8]]]};
res["23 components of O(4,4) reached by I, T^0, T^4, T^0T^4 (signs of space/time block determinants)"] = {blockdets[refl[ID16] /. {} -> ID8], blockdets[refl[T16A[0]]], blockdets[refl[T16A[4]]], blockdets[LambdaOf[T16A[0].T16A[4]]]};
basis = Prepend[Table[Dot @@ (T16A /@ s), {s, Subsets[Range[0, 7], {1, 8}]}], ID16];
res["24 the 256 products T^{A1}...T^{Ak} are linearly independent (Cl(4,4) = M(16,R))"] = {Length[basis], MatrixRank[Flatten /@ basis]};
res["25 trace orthogonality Tr(B_I B_J^-1) = 16 delta_IJ"] = (Table[Tr[basis[[i]].Inverse[basis[[j]]]], {i, 256}, {j, 256}] == 16 IdentityMatrix[256]);
res["26 type-1/type-2 block form: S^AB = diag(D1^AB, D2^AB)"] = And @@ Flatten@Table[Sab[A, B][[1 ;; 8, 9 ;; 16]] == 0 ID8 && Sab[A, B][[9 ;; 16, 1 ;; 8]] == 0 ID8, {A, 0, 7}, {B, 0, 7}];
res["27 tau/taubar relation (1/2)(tau^A taubar^B + tau^B taubar^A) = eta^AB I8"] = And @@ Flatten@Table[(tau[A].taubar[B] + tau[B].taubar[A])/2 == etaE[A, B] ID8, {A, 0, 7}, {B, 0, 7}];
(* comparison with the stored outputs of Pre-gravity6plane.nb *)
If[FileExistsQ[nbFile],
  nb = Get[nbFile]; styles = {"Input","Output","Text","Section","Title","Subsubsection","Print","Message"};
  cells = Cases[nb, c:Cell[_, s_String /; MemberQ[styles, s], ___] :> c, Infinity];
  val[i_] := ReleaseHold[ToExpression[cells[[i, 1]], StandardForm, HoldComplete] /. {MatrixForm[x_, ___] :> x}] /. HoldComplete[x_] :> x;
  res["28 identical to Pre-gravity6plane.nb output cell 494 ((T16^A)[0..7])"] = (val[494] == Table[T16A[A], {A, 0, 7}]);
  res["29 identical to Pre-gravity6plane.nb output cell 310 ((T16^A)[8])"] = (val[310] == T16A[8]);
  res["30 identical to Pre-gravity6plane.nb output cell 312 (sigma16)"] = (val[312] == sigma16);
  res["31 identical to Pre-gravity6plane.nb output cells 379, 381 (P_L, P_R)"] = (val[379] == PL && val[381] == PR),
  Print["Pre-gravity6plane.nb not found: comparison skipped"]];
KeyValueMap[Print[#1, " : ", #2] &, res];
Export["dm_data.json", <|"T" -> Table[T16A[A], {A, 0, 7}], "Gamma" -> G, "sigma16" -> sigma16, "PL" -> PL, "PR" -> PR,
   "tau" -> Table[tau[A], {A, 0, 7}], "taubar" -> Table[taubar[A], {A, 0, 7}], "sigma" -> sigma, "eta" -> eta4488,
   "products" -> Flatten[Table[<|"A" -> A, "B" -> B, "M" -> T16A[A].T16A[B]|>, {A, 0, 6}, {B, A + 1, 7}], 1],
   "T4567" -> T16A[4].T16A[5].T16A[6].T16A[7], "checks" -> (ToString[#, InputForm] & /@ res)|>, "JSON"];
