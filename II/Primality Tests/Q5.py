import numpy as np
from Q1 import TrialDivisionTest
from Q2 import EvaluateBasePowerMod

def StrongTest(N, a):
    if (np.gcd(N,a) != 1):
        return False

    s = N - 1
    r = 0
    while (s & 1 == 0):
        r += 1
        s = s >> 1
    
    k = EvaluateBasePowerMod(a, s, N)
    if (k == 1 or k == (-1 % N)):
        return True
    for i in range(1, r):
        k = (k * k) % N
        if (k == (-1 % N)):
            return True

    return False


def FindStrongPseudoPrimesBase(a, upperBound=1000000, lowerBound=2):
    output = set()
    for i in range(lowerBound, upperBound + 1):
        if (StrongTest(i, a)):
            if (not TrialDivisionTest(i)):
                output.add(i)
    
    return output

def FindAbsoluteStrongPseudoPrimes(upperBound=1000000, lowerBound=2):
    twoPseudoPrimes = sorted(FindStrongPseudoPrimesBase(2, upperBound, lowerBound))
    #print(twoPseudoPrimes)

    absolutePseudoPrimes = set()
    breakingPoints = []

    for n in twoPseudoPrimes:
        isAbsPseudo = True
        for a in range(3, n):
            if (np.gcd(a,n) != 1):
                continue
            if (StrongTest(n, a)):
                continue
            # If needed
            breakingPoints.append([n,a])
            isAbsPseudo = False
            break
        
        if (isAbsPseudo):
            absolutePseudoPrimes.add(n)

    return absolutePseudoPrimes, breakingPoints


if __name__ == "__main__":
    print(sorted(FindStrongPseudoPrimesBase(2,1000000)))
    absPseudo, breakingPoints = FindAbsoluteStrongPseudoPrimes(1000000)

    print(sorted(absPseudo))
    print(breakingPoints)