
p = 7;

% setup array
inverseArray = (1:p-1);


%core loop to find inverses
for i = 1:p-1
    for j = 1:p-1
        if (mod(i*j, p) == 1)
            inverseArray(i) = j;
            break;
        end
    end
end


%print out array
fprintf('%d, ', inverseArray(1:end))