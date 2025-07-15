import numpy
import Q10

z = 1.28
n = 100

tot = 0

for i in range(500):
    x = Q10.generateN(n, 0, 1)
    S = 0
    for j in range(n):
        S += x[j]
    mean = S/n

    A = mean - z/numpy.sqrt(n)
    B = mean + z/numpy.sqrt(n)

    oz = 1
    if (A > 0): oz = 0
    if (B < 0): oz = 0

    tot += oz

    #print(str(mean) + " & " + str(A) + " & " + str(B) + " & " + str(oz))

    
print(tot)
