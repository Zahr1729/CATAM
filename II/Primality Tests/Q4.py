import numpy as np
from Q1 import TrialDivisionTest
from Q2 import EvaluateBasePowerMod


def EvaluateJacobi (a, b):
    a = a % b
    result = 1
    while (a > 1):
        
        ## Factor out 4s
        while (a % 4 == 0):
            a = a >> 2

        # Check last 2
        if (a % 2 == 0):
            a = a >> 1
            if (int((b*b - 1)/8) % 2 == 1):
                result *= -1

        # Flip upsidedown and modulo out
        if (a != 1):
            c = b
            b = a
            a = c

            if (int((a-1)*(b-1) / 4) % 2 == 1):
                result *= -1

            a = a % b
    
    return result * a
    

def EulerTest (N, a):

    if (np.gcd(N,a) == 1 and np.gcd(N,2) == 1):
        return ((EvaluateJacobi(a, N) % N) == (EvaluateBasePowerMod(a, int((N-1) / 2), N) % N))
    return False


def FindEulerPseudoPrimesBase(a, upperBound=1000000, lowerBound=2):
    output = set()
    for i in range(lowerBound, upperBound + 1):
        if (EulerTest(i, a)):
            if (not TrialDivisionTest(i)):
                output.add(i)
    
    return output

def FindAbsoluteEulerPseudoPrimes(upperBound=1000000, lowerBound=2):
    
    twoPseudoPrimes = sorted(FindEulerPseudoPrimesBase(2, upperBound, lowerBound))

    absolutePseudoPrimes = set()

    for n in twoPseudoPrimes:
        isAbsPseudo = True
        for a in range(3, n):
            if (np.gcd(a,n) != 1):
                continue
            if (EulerTest(n, a)):
                continue
            # print gets data for when we found a base which breaks 
            print(a, n)
            isAbsPseudo = False
            break
        
        if (isAbsPseudo):
            absolutePseudoPrimes.add(n)

    return absolutePseudoPrimes


if __name__ == "__main__":
    print(sorted(FindEulerPseudoPrimesBase(2, 1000000)))
    print(FindAbsoluteEulerPseudoPrimes(1000000))