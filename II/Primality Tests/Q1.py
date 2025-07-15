import numpy as np

def TrialDivisionTest(n):
    if (n <= 1): return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True

if __name__ == "__main__":
    for i in range(188000, 188201):
        if (TrialDivisionTest(i)):
            print(i, end=" ")

    print("")
    k = 1000000000
    for i in range(k, k + 201):
        if (TrialDivisionTest(i)):
            print("10^{9}+" + str(i-k), end=" ")