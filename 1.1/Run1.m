
A = [1 0 1 2 0;
    0 1 1 2 0;
    0 0 0 0 1];

rows = 3;
columns = 5;

B = GaussianElimination(A, 1, 1, rows, columns);

C = KernelBasis(B, rows, columns);
