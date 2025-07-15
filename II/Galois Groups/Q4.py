from Q2 import GetCycleTypeModP
import numpy as np


def ComputeProbabilities():

    polys = [
            [41, 1, 1],
            [1, 2, 0, 1],
            [5, 5, 0, -2, 1],
    ]
    degs = [2, 3, 4]

    # This is an inefficient test but will do for now.
    def TrialDivisionTest(n):
        if (n <= 1): return False
        for i in range(2, int(np.sqrt(n)) + 1):
            if (n % i == 0):
                return False
        return True
    
    maxNum = [2000, 2000, 500]

    for i in range(0, 3):
        dictionary = {}
        keys = []
        for p in range(2, maxNum[i]):
            # Test Primality
            if (TrialDivisionTest(p) == False): continue

            cycleType = GetCycleTypeModP(p, polys[i], degs[i])
            if (cycleType == False):
                continue
            string = "("
            for cyc in cycleType:
                string += str(cyc) + ","
            string += ")"

            if (string in keys):
                dictionary[string] = dictionary[string] + 1
            else:
                dictionary[string] = 1
                keys.append(string)

        total = 0
        for key in keys:  
            total += dictionary[key]
        for key in keys:
            dictionary[key] = dictionary[key] / total
        
        print(dictionary)

if __name__ == "__main__":
    ComputeProbabilities()