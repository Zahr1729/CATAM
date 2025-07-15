
A = [1 0 0 0 3 0 0;
    0 5 0 1 6 3 0;
    0 0 5 0 2 0 0;
    2 4 0 0 0 5 1;
    4 3 0 0 6 2 6;];

C = GaussianElimination(A, 1, 1, 5, 7);

B = transpose(KernelBasis(C, 5, 7));

[M1, M2, M3, M4] = MultipleBases(A, B, size(A, 1), size(B, 1), size(A, 2));