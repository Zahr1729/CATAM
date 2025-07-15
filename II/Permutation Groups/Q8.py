from Q7 import GetStabiliserGenerators
from Q5 import GetOrbitWitness
from Q3 import SimplifyArray, ReduceGenerators

def ComputeGroupOrder(n, perms):
    order = 1
    perms = ReduceGenerators(n, perms)

    for i in range(n):
        if (len(perms) == 0): break
        T = GetOrbitWitness(n, i, perms)
        orbitSize = len(SimplifyArray([T]))
        order *= orbitSize
        #print (order, end= " ")
        perms = GetStabiliserGenerators(n, i, perms, T)
    #print()

    # remove hashtags before this to get subgroup data
        
    return order

def PrintQ8Data(n, gens):
    order = ComputeGroupOrder(n, gens)
    print(n, gens, order)

if __name__ == "__main__":

    # Main Data
    
    PrintQ8Data(6, [[0,1,2,3,4,5]])
    PrintQ8Data(3, [[1,2,0], [2,0,1]])
    PrintQ8Data(3, [[1,2,0], [0,2,1]])
    PrintQ8Data(4, [[1,0,3,2], [2,3,0,1]])
    PrintQ8Data(5, [[1,2,3,4,0], [1,0,2,3,4]])
    PrintQ8Data(5, [[1,2,3,4,0], [1,0,3,2,4]])
    PrintQ8Data(11, [[1,2,3,4,5,6,7,8,9,10,0], [1,0,2,3,4,5,6,7,8,9,10]])

    # Do Subgroups
    print()

    # If you want to run this part and get the data you need to take the print statements
    # out of comments in ComputeGroupOrder Function

    #ComputeGroupOrder(4, [[1,0,3,2], [2,3,0,1]])
    #ComputeGroupOrder(3, [[1,2,0], [0,2,1]])
    #ComputeGroupOrder(5, [[1,2,3,4,0], [1,0,3,2,4]])
    #ComputeGroupOrder(6, [[1,2,3,4,5,0], [1,0,2,3,4,5]])
    #ComputeGroupOrder(6, [[1,0,2,3,4,5], [0,1,3,2,5,4], [0,1,4,5,2,3]])

    # I am speeeeeeeed for S_20
    print

    PrintQ8Data(20, [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,0], [1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]])