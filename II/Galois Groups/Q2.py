from Q1 import *
import numpy as np
import time

def CheckSeperable(p, inv, f, degf):
    g, degg = Reduce([f[i+1]*(i+1) % p for i in range(degf)])
    hcf, d = PolysHCF(p, inv, f, degf, g, degg)
    return (d == 0)


def ReduceModP(p, f, degf):
    g, degg = Reduce([f[i] % p for i in range(degf+1)])
    return g, degg

def DecomposePolyModP(p, f, degf):
    inv = GetInverses(p)
    g, degg = ReduceModP(p, f, degf)
    isSep = CheckSeperable(p, inv, g, degg)
    if (not isSep): return False

    # Note we only need to check degrees up to floor(degf/2)
    # moreover if we are systematic once we find a factor we only need
    # to consider the poly divided out by said factor
    # to be even more efficient we only need to check irriducible polys
    # but that seems more difficult :/

    factors = []

    maxFactorDeg = int(degf/2)
    for j in range(1, maxFactorDeg + 1):

        maxNum = np.power(p, j)
        i = 0
        while(i < maxNum):
            # Use each of these numbers as a polynomial
            prelimh = [int(i/np.power(p, k)) % p for k in range(j)]
            prelimh.append(1)
            h, degh = Reduce(prelimh)
            
            q, r, degr = GetQuotRem(p, inv, g, degg, h, degh)
            
            i += 1

            if (degg <= degh):
                break

            if (r != [0]):
                continue
            
            g = q
            degg = degg - degh
            factors.append(h)
            
    factors.append(g)
    
    return factors

def PrintFactorisation(factors):
    for factor in factors:
        flag = False
        print("(", end="")
        for j in range(len(factor)):
            i = len(factor) - j - 1
            if (factor[i] == 0): continue
            if (flag): print(" + ", end="")
            
            if (i == 0):
                print(str(factor[i]), end="")
            elif (i == 1):
                if (factor[i] == 1):
                    print("X", end="")
                else:
                    print(str(factor[i]) + "X", end="")
            else:
                if (factor[i] == 1):
                    print("X^{" + str(i) + "}", end="")
                else:
                    print(str(factor[i]) + "X^{" + str(i) + "}", end="")
            
            flag = True
        print(")", end="")
    print("$ & ", end="")

def GetCycleTypeModP(p, f, degf):
    factors = DecomposePolyModP(p, f, degf)
    if (factors == False):
        return factors

    cycleType = []
    for i in range(len(factors)):
        ord = len(factors[i]) - 1
        if (ord != 1):
            cycleType.append(ord)
    
    return cycleType



def GetCycleTypeHCF(p, f, degf):

    inv = GetInverses(p)
    isSep = CheckSeperable(p, inv, f, degf)
    if (not isSep): return False

    cycleType = []
    sameOrderFactors = []
    i = 1
    while (i < int(np.floor(degf/2) + 1)):
        # Initialise phi
        ptoi = int(np.power(p, i))
        phi = [0 for i in range(1 + ptoi)]
        phi[1] = p - 1
        phi[ptoi] = 1


        hcf, degh = PolysHCF(p, inv, f, degf, phi, len(phi) - 1)
        if (degh > 0):
            sameOrderFactors.append(hcf)
            t = degh
            while (t > 0 and i != 1):
                cycleType.append(i)
                t -= i
            f, r, degr = GetQuotRem(p, inv, f, degf, hcf, degh)
            degf -= degh
    
        i += 1

    if (degf > 1):
        cycleType.append(degf)
    sameOrderFactors.append(f)

    return cycleType
        
        
        
if __name__ == "__main__":
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]#  61, 67, 71, 73, 79, 83, 89, 97]

    polys = [
            [41, 1, 1],
            [1, 2, 0, 1],
            [-1, -2, 1, 1],
            [4, 0, -2, 0, 1],
            [16, -4, 0, -1, 1],
            [5, 5, 0, -2, 1],
            [7, 6, 7, 0, 1],
            [7, -9, -6, 3, 1],
    ]
    degs = [2, 3, 3, 4, 4, 4, 4, 4]

    t = time.time()

    for p in primes:
        for i in range(0, 8):
            GetCycleTypeHCF(p, polys[i], degs[i])
            

    print(time.time() - t)
    t = time.time()

    for p in primes:
        for i in range(0, 8):
            GetCycleTypeModP(p, polys[i], degs[i])
            
    
    print(time.time() - t)
    t = time.time()