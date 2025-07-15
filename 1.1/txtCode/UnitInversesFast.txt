
p = 11;

% setup array
inverseArray = zeros(1, p-1);

%core loop to find inverses
for i = 1:p-1
    if (inverseArray(i) ~= 0)
        continue
    end

    for j = 1:p-1
        if (mod(i*j, p) == 1)
            inverseArray(i) = j;
            inverseArray(j) = i;
            break;
        end
    end
end


%print out array
fprintf('%d, ', inverseArray(1:end))