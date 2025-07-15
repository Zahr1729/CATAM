from Q1 import Inverse, Product

def ReduceGenerators (n, gens):
    A = [[None for i in range(n)] for j in range(n)]
    for i in range(len(gens)):
        g = gens[i]
        for j in range(n):
            if (g[j] == j): continue
            f = A[j][g[j]]
            if (f != None):
                g = Product(Inverse(f), g)
                continue
            A[j][g[j]] = g
            break
    print(A)
    return SimplifyArray(A)

def SimplifyArray(A):
    arr = []
    for i in range(len(A)):
        for j in range(len(A[i])):
            if (A[i][j] != None):
                arr.append(A[i][j])
    return arr

if __name__ == "__main__":
    print(ReduceGenerators(5, [[0, 1, 2, 3, 4]]))
    print(ReduceGenerators(3, [[2,0,1], [2,1,0]]))
    print(ReduceGenerators(4, [[1,2,3,0]]))
    print(ReduceGenerators(5, [[1,0,2,3,4], [1,2,3,4,0], [1,3,0,2,4], [2,3,1,0,4]]))