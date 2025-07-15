import numpy as np
from Q1 import TrialDivisionTest
from Q3 import FindFermatPseudoPrimesBase
from Q4 import FindEulerPseudoPrimesBase
from Q5 import FindStrongPseudoPrimesBase
from Q5 import StrongTest


def FindPrimesWithStrongBase2(upperBound=1000000, lowerBound=2):
    output = {2}
    for i in range(lowerBound, upperBound + 1):
        if (StrongTest(i, 2)):
            if (TrialDivisionTest(i)):
                output.add(i)
    
    return output


def GetPseudoPrimesBase(a, upperBound = 10000, lowerBound=2):
    fermat = FindFermatPseudoPrimesBase(a, upperBound, lowerBound)
    euler = FindEulerPseudoPrimesBase(a, upperBound, lowerBound)
    strong = FindStrongPseudoPrimesBase(a, upperBound, lowerBound)

    return fermat, euler, strong

if __name__ == "__main__":

    fermatOverlap = [[] for i in range(5)]
    eulerOverlap = [[] for i in range(5)]
    strongOverlap = [[] for i in range(5)]

    for k in range(5, 10):
        low = int(np.power(10, k))
        upp = low + 100000
        ferm2, eul2, strong2 = GetPseudoPrimesBase(2, upp, low)
        ferm3, eul3, strong3 = GetPseudoPrimesBase(3, upp, low)

        primes = sorted(FindPrimesWithStrongBase2(upp, low))

        print(len(ferm2), len(eul2), len(strong2), len(primes))
        
        fermatOverlap[k-5] = sorted(ferm2.intersection(ferm3))
        eulerOverlap[k-5] = sorted(eul2.intersection(eul3))
        strongOverlap[k-5] = sorted(strong2.intersection(strong3))


    print(fermatOverlap)
    print(eulerOverlap)
    print(strongOverlap)

