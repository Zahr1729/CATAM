from Q5 import GetOrbitWitness
from Q3 import SimplifyArray, ReduceGenerators
from Q1 import Product, Inverse

def GetStabiliserGenerators(n, el, perms, T):

    def Phi(g):
        return T[g[el]]
    
    A = [[None for i in range(len(perms))] for j in range(n)]

    for i in range(n):
        t = T[i]
        if (not t): continue
        for j in range(len(perms)):
            y = perms[j]
            yt = Product(y, t)
            A[i][j] = Product(Inverse(Phi(yt)), yt)
    
    #print(len(SimplifyArray(A)), end=" ")
    return ReduceGenerators(n, SimplifyArray(A))

def PrintQ7Data(n, a, gens):
    T = GetOrbitWitness(n, a, gens)
    data = GetStabiliserGenerators(n, a, gens, T)
    print(n, a, gens, data)

if __name__ == "__main__":
    PrintQ7Data(3, 0, [[1,0,2]])
    PrintQ7Data(3, 2, [[1,0,2]])
    PrintQ7Data(4, 0, [[1, 0, 3, 2], [0, 1, 3, 2]])
    PrintQ7Data(5, 0, [[0, 3, 2, 4, 1], [4, 2, 0, 1, 3]])
    PrintQ7Data(5, 0, [[1,0,2,3,4], [1,2,3,4,0], [1,3,0,2,4], [2,3,1,0,4]])
