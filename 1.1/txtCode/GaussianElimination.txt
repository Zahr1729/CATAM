function B = GaussianElimination(M, r, c, rows, columns)
    % r, c initial input are 1, rows, columns are dimensions of matrix
    if(r > rows || c > columns)
        B = M;
        return;
    end
    % Assuming in row echelon form for all rows less than r and columns
    % less than c. Turn next row/column into row echelon form
    
    % These values prechosen and precalculated for each choice of p
    inverseArray = [1, 4, 5, 2, 3, 6];
    p = 7;

    M = mod(M, p);

    zeroFlag = 1;
    if (M(r,c) == 0)
        % Find non zero entry in column
        for i = (r+1):(rows)
            if (M(i,c) ~= 0)
                for j = c:(columns)
                    M(r,j) = mod(M(r,j) + M(i,j), p);
                end
                zeroFlag = 0;
                break;
            end
        end
        if (zeroFlag == 1)
            B = GaussianElimination(M, r, c+1, rows, columns);
            return;
        end
    end
    

    % Basic Case
    M(r,c) = mod(M(r,c), p);
    if (M(r,c) == 0)
        inv = 0;
    else
        inv = inverseArray(M(r,c));
    end

    % Normalise top row
    for j = c:(columns)
        M(r,j) = mod(M(r,j) * inv, p);
    end

    % Subtract out
    for i = (r+1):(rows)
        a = M(i,c);
        for j = c:(columns)
            d = a * M(r, j);
            M(i,j) = mod(M(i,j) - d, p);
        end
    end

    % Complete row echelon below diagonal for the rest of matrix
    M = GaussianElimination(M, r+1, c+1, rows, columns);
    
    % Finally kill terms in rows above r in column c
    for i = (1):(r-1)
        a = M(i,c);
        for j = c:(columns)
            d = a * M(r, j);
            M(i,j) = mod(M(i,j) - d, p);
        end
    end
    B = M
end