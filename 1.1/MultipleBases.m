function [M1, M2, M3, M4] = MultipleBases (A, B, rowsA, rowsB, cols)
    M1 = GaussianElimination(A, 1, 1, rowsA, cols);
    M2 = GaussianElimination(B, 1, 1, rowsB, cols);

    C = vertcat(A, B);
    M3 = GaussianElimination(C, 1, 1, rowsA + rowsB, cols);

    D1 = KernelBasis(M1, rowsA, cols);
    D2 = KernelBasis(M2, rowsB, cols);

    E1 = transpose(D1);
    E2 = transpose(D2);

    F = vertcat(E1, E2);
    G = GaussianElimination(F, 1, 1, size(F,1), cols);
    H = transpose(KernelBasis(G, size(F,1), cols));
    M4 = GaussianElimination(H, 1, 1, size(H,1), size(H,2));
end