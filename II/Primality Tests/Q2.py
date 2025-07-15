import numpy as np

def EvaluateBasePowerMod(a, M, N):
    # reduce to simpler case
    b = a % N
    pow = 0
    mod = 1
    i = 0
    while (M > 0):
        c = M & 1
        M -= c
        pow += c * (1 << i)
        M = M >> 1
        if (c):
            mod = (mod * b) % N

        # May have overflow in this ase
        b = (b * b) % N
        
        # Here is memory efficient case

        #prod = 0
        #d = b
        #while (d > 0):
            #if (d % 2 == 1):
                #prod = prod + b % N
            #b = 2*b % N
            #d /= 2

        #b = prod
            

        if (b == 1):
            break

        i += 1

    return (mod % N)


def FermatTest(N, a):
    return (EvaluateBasePowerMod(a, N-1, N) == 1)



if __name__ == "__main__":

    primeset = {188011, 188017, 188021, 188029, 188107, 188137, 188143, 188147, 188159, 188171, 188179, 188189, 188197}
    for j in range(2, 14):
        testPass = set()
        print(j, end=" ")
        for i in range(188000, 188201):
            if (FermatTest(i, j)):
                testPass.add(i)
        print(primeset.issubset(testPass), testPass.difference(primeset))

    print("")

    k = 1000000000
    primeset = {1000000007, 1000000009, 1000000021, 1000000033, 1000000087, 1000000093, 1000000097, 1000000103, 1000000123, 1000000181}
    for j in range(2, 14):
        testPass = set()
        print(j, end=" ")
        for i in range(k, k+201):
            if (FermatTest(i, j)):
                testPass.add(i)
        print(primeset.issubset(testPass), testPass.difference(primeset))

        