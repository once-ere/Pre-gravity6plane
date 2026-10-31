(* ===== core definitions, reproduced verbatim (up to symbol names) from Pre-gravity6plane.nb ===== *)
X = {x0, x1, x2, x3, x4, x5, x6, x7};
eta4488 = ArrayFlatten[{{IdentityMatrix[4], 0}, {0, -IdentityMatrix[4]}}];
sigma = ArrayFlatten[{{ConstantArray[0, {4, 4}], IdentityMatrix[4]}, {IdentityMatrix[4], ConstantArray[0, {4, 4}]}}];
ID4 = IdentityMatrix[4]; ID8 = IdentityMatrix[8]; ID16 = IdentityMatrix[16];
Qa[h_, p_, q_] := Signature[{h, p, q, 4}];
Qb[h_, p_, q_] := ID4[[p, 4]]*ID4[[q, h]] - ID4[[p, h]]*ID4[[q, 4]];
s4by4[h_] := Table[Qa[h, p, q] - Qb[h, p, q], {p, 4}, {q, 4}];
t4by4[h_] := Table[Qa[h, p, q] + Qb[h, p, q], {p, 4}, {q, 4}];
sixAntiSymmetric8by8 = Flatten[{Table[ArrayFlatten[{{0, s4by4[h]}, {s4by4[h], 0}}], {h, 1, 3}],
    Table[ArrayFlatten[{{0, t4by4[h]}, {-t4by4[h], 0}}], {h, 3, 1, -1}]}, 1];
tau[0] = ID8; Do[tau[h] = sixAntiSymmetric8by8[[h]], {h, 1, 6}];
tau[7] = tau[1].tau[2].tau[3].tau[4].tau[5].tau[6];
Do[taubar[h] = sigma.Transpose[sigma.tau[h]], {h, 0, 7}];
Do[T16A[A] = ArrayFlatten[{{0, taubar[A]}, {tau[A], 0}}], {A, 0, 7}];
T16A[8] = Dot @@ Table[T16A[A], {A, 0, 7}];
sigma16 = T16A[0].T16A[1].T16A[2].T16A[3];
PL = (ID16 - T16A[8])/2; PR = (ID16 + T16A[8])/2;
SAB = Table[(T16A[A].T16A[B] - T16A[B].T16A[A])/4, {A, 0, 7}, {B, 0, 7}];
