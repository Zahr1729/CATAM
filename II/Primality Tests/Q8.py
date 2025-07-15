from Q1 import TrialDivisionTest
from Q5 import StrongTest
from Q7 import QuickPrimalityTest
import numpy as np

def TestStrongProbabilities(k, t, n):
    primeCount = 0
    passStrongCounts = [0 for j in range(t)]

    for i in range(n):
        # Get number
        num = np.random.randint(1 << k-1, 1 << k)
        if (num & 1 == 0):
            num += 1

        if (QuickPrimalityTest(num)):
            primeCount += 1
        
        passesStrong = [True for j in range(t)]
        for j in range(t):
            a = np.random.randint(2, num-1)
            if (not StrongTest(num, a)):
                for w in range(j, t):
                    passesStrong[w] = False
                break
        
        for j in range(t):
            if (passesStrong[j]):
                passStrongCounts[j] += 1
            
    print("$" + str(k) + "$, $" + str(primeCount) + "$, ", end="")
    
    for j in range(t):
        print("$" + str(passStrongCounts[j]) + "$, ", end="")
    for j in range(t):
        print("$" + str(primeCount/passStrongCounts[j]) + "$, ", end="")
    
    print("")



if __name__ == "__main__":
    
    for i in range(15, 28):
        TestStrongProbabilities(i, 4, 10000)
