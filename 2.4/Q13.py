import matplotlib.pyplot as plt
import Q10

def GenerateNChi(n, k):
    x = [0 for i in range(n)]
    for j in range(n):
        for i in range(k):
            y = Q10.generateNormal(0, 1)[0]
            x[j] += y*y

    return x

def DrawGraph(n, k):
    x = GenerateNChi(n, k)
    plt.hist(x, bins = 30)
    plt.show()

DrawGraph(100, 1)
DrawGraph(300, 1)
DrawGraph(500, 1)

DrawGraph(100, 5)
DrawGraph(300, 5)
DrawGraph(500, 5)

DrawGraph(100, 40)
DrawGraph(300, 40)
DrawGraph(500, 40)
