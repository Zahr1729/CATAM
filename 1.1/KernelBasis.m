function S = KernelBasis(M, rows, columns)
    % First locate the special "1s"
    r = 1;
    rank = 0;

    Basis = [];

    diagOnes = [];
    for j = 1:columns
        if (M(r,j) == 1)
            rank = rank + 1;
            diagOnes(r) = j;
            r = r + 1;
            if (r > rows)
                break
            end
        end
    end

    vecNumber = 0;

    % Make sure there is a zero vector to be make other programs work
    Basis(1:columns, 1) = 0;

    for j = 1:columns
        if (ismember(j, diagOnes))
            continue;
        end
        vecNumber = vecNumber + 1;
        
        % Construct new basis vector
        vec(1:columns) = 0;
        vec(j) = 1;
        for i = 1:rows
            if (M(i,j) == 0)
                continue;
            end

            vec(diagOnes(i)) = -M(i,j);
        end
        
        for j = 1:columns
            Basis(j, vecNumber) = vec(j);
        end
    end


    disp(diagOnes);
    S = Basis;
end
