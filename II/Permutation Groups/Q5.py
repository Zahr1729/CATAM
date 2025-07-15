from Q1 import Product
from Q3 import ReduceGenerators, SimplifyArray

def GetOrbitWitness (n, el, perms):
    perms = ReduceGenerators(n, perms)

    
    oldOrbit = [None for i in range(n)]
    orbit = [None for i in range(n)]
    orbit[el] = [i for i in range(n)]
    while (orbit != oldOrbit):
        # I KNEW THIS WOULD CAUSE some memory issue
        # oldOrbit = orbit
        for i in range(n): oldOrbit[i] = orbit[i]

        for k in range(len(perms)):
            g = perms[k]
            for j in range(n):
                if (not oldOrbit[j]): continue
                if (orbit[g[j]] == None):
                    orbit[g[j]] = Product(g, oldOrbit[j])

    
    return orbit


def PrintQ5Data(n, a, gens):
    print(n, a, gens, end=" ")
    data = (GetOrbitWitness(n, a, gens))
    for i in range(len(data)):
        if (data[i] != None):
            print(str(i) + ", " + str(data[i]), end=" ")
    
    print("")


if __name__ == "__main__":

    PrintQ5Data(3, 0, [[1,0,2]])
    PrintQ5Data(3, 2, [[1,0,2]])
    PrintQ5Data(4, 0, [[1, 0, 3, 2], [0, 1, 3, 2]])
    PrintQ5Data(5, 0, [[0, 3, 2, 4, 1], [4, 2, 0, 1, 3]])
    