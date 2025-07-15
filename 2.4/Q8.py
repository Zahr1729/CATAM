import matplotlib.pyplot as plt
import numpy as np
import random

n = 10
N = 200
t0 = 2.2


def F (x, t):
    return 1 - (1 + x*t) * np.exp(-t * x)

def findX (u, i, uBound, lBound, t): # Function which attempts to find x given u by the bisection method
    m = (uBound + lBound) / 2
    uNew = F(m, t)

    if (i <= 0): return m

    if (uNew > u):
        return findX( u, i-1, m, lBound, t)
    elif (uNew < u):
        return findX( u, i-1, uBound, m, t)
    else:
        return m



def f (x, t):
    return t * t * x * np.exp(- t * x)

def getLog (x, t, n):
    S = 1
    for i in range(n):
        S += np.log(f(x[i], t))

    return S

data = [0 for i in range(N)]

for j in range(N):
    u = [random.uniform(0,1) for i in range(n)]
    x = [0 for i in range(n)]

    for i in range(n):
        x[i] = findX(u[i], 50, 20, 0, t0)

    data[j] = 2*n / sum(x, 0)


plt.hist(data, bins = 20)
plt.show()



