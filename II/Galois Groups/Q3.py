from Q2 import GetCycleTypeModP


def FindDecompGroupModP(p, f, degf):
    cycleType = GetCycleTypeModP(p, f, degf)
    if (cycleType == False):
        print("[-], ", end="")
        return
    
    print("[", end="")
    if (cycleType == []):
        print("$e$", end="")
    else:
        print("$(", end="")
        for i in range(len(cycleType)):
            if (i != 0): print(", ", end="")
            print(cycleType[i], end="")
        print(")$", end="")
    print("], ", end="")


def ComputeDecompsOfPolys():

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    polys = [
            [41, 1, 1],
            [1, 2, 0, 1],
            [-1, -2, 1, 1],
            [4, 0, -2, 0, 1],
            [16, -4, 0, -1, 1],
            [5, 5, 0, -2, 1],
            [7, 6, 7, 0, 1],
            [7, -9, -6, 3, 1],
            [36, 0, 0, 0, 0, 1],
            [3, -5, 0, 0, 0, 1],
            [3, 0, -3, 1, 0, 1],
            [-11, 22, 0, -11, 0, 1],
            [1, 1, 0, 0, 0, 0, 1],
            [2, 2, 0, 0, 0, 0, -2, 1],
            [4, 8, -2, 0, 1, 0, 0, 1],
            [1, 5, 0, -1, -4, 1, 0, 1]
    ]
    degs = [2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 7, 7, 7]

    for p in primes:

        print("\n[" + str(p) + "], ", end="")
        for i in range(0, 8):
            FindDecompGroupModP(p, polys[i], degs[i])
    
    print()
    
    for p in primes:

        print("\n[" + str(p) + "], ", end="")
        for i in range(8, 16):
            FindDecompGroupModP(p, polys[i], degs[i])



if __name__ == "__main__":
    ComputeDecompsOfPolys()