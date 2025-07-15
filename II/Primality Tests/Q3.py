import numpy as np
from Q2 import FermatTest
from Q1 import TrialDivisionTest

def FindFermatPseudoPrimesBase(a, upperBound=1000000, lowerBound=2):
    output = set()
    for i in range(lowerBound, upperBound + 1):
        if (FermatTest(i, a)):
            if (not TrialDivisionTest(i)):
                output.add(i)
    
    return output
    



def FindCarmichaelFermat (upperBound=1000000, lowerBound=2):
    twoPseudoPrimes = sorted(FindFermatPseudoPrimesBase(2, upperBound, lowerBound))
    #print(twoPseudoPrimes)

    carmichaelNumbers = set()

    for n in twoPseudoPrimes:
        isCarmichael = True
        for a in range(3, min(n, 20)):
            if (np.gcd(a,n) != 1):
                continue
            if (not TrialDivisionTest(a)):
                continue
            if (FermatTest(n, a)):
                continue
            # print gets data for when we found a base which breaks 
            print(a, n)
            isCarmichael = False
            break
        
        if (isCarmichael):
            carmichaelNumbers.add(n)
        

    return carmichaelNumbers



if __name__ == "__main__":
    print(sorted(FindFermatPseudoPrimesBase(2, 1000000)))
    print(sorted(FindCarmichaelFermat(1000000)))