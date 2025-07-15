import random
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from Q8 import ComputeGroupOrder

def SetupAxes (x, y, showGrid=True):

    x = np.array(x)
    y = np.array(y)
    xMax = np.max(x) + 0.5
    xMin = 4.5
    yMax = 1
    yMin = 0

    fig, ax = plt.subplots()
    plt.xlabel('n', color='white')
    plt.ylabel('Pn', color='white')
    fig.set_facecolor("black")
    ax.set_facecolor("black")
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.tick_params(colors='white')
    ax.set_xlim(xMin, xMax)
    ax.set_ylim(yMin, yMax)
    if (showGrid):
        ax.grid(color='white', linewidth=0.4, alpha=0.3, zorder=0)
    return fig, ax


def GenerateRandomPermutation(n):

    values = [i for i in range(n)]
    perm = [-1 for i in range(n)]

    for i in range(n):
        t = random.randint(0,n-i-1)
        perm[i] = values[t]
        values = values[:t] + values[t+1:]

    return perm

def PairCheck(n):
    g = GenerateRandomPermutation(n)
    h = GenerateRandomPermutation(n)
    ord = ComputeGroupOrder(n, [g,h])
    return (ord == np.math.factorial(n))

def GetSn2Probability(n, perms):
    l = len(perms)
    tot = 0
    for i in range(l):
        for j in range(l):
            ord = ComputeGroupOrder(n, [perms[i],perms[j]])
            tot += (ord == np.math.factorial(n))
    prob = tot / (l * l)
    return prob

def SmallProbabilities():
    perms2 = [[0,1], [1,0]]
    perms3 = [[0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,0,1], [2,1,0]]
    perms4 = [[0,1,2,3], [0,1,3,2], [0,2,1,3], [0,2,3,1], [0,3,1,2], [0,3,2,1],
              [1,0,2,3], [1,0,3,2], [1,2,0,3], [1,2,3,0], [1,3,0,2], [1,3,2,0],
              [2,0,1,3], [2,0,3,1], [2,1,0,3], [2,1,3,0], [2,3,0,1], [2,3,1,0],
              [3,0,1,2], [3,0,2,1], [3,1,0,2], [3,1,2,0], [3,2,0,1], [3,2,1,0]]
    
    print(GetSn2Probability(2, perms2))
    print(GetSn2Probability(3, perms3))
    print(GetSn2Probability(4, perms4))

def EstimatePn(n):
    k = 100
    total = 0
    for i in range(k):
        total += PairCheck(n)
    prob = total/k
    return(prob)

def GraphPn():
    m = 13
    ns = [i for i in range(5, m)]
    P = [0 for i in range(m)]
    
    for n in range(5, m):
        print(n)
        P[n] = EstimatePn(n)
    
    colours = [mpl.cm.hsv((i -5) * 0.8 / (m-6)) for i in range(5, m)]

    P = P[5:]

    fig, ax = SetupAxes(ns, P, showGrid=False)
    plt.bar(ns, P, color=colours)
    plt.show()
    

if __name__ == "__main__":
    SmallProbabilities()

    GraphPn()



