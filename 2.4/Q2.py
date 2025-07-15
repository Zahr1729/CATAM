import matplotlib.pyplot as plt
import numpy as np
import random

n = 100
theta0 = 1.2


u = [random.uniform(0,1) for i in range(n)]
x = [0 for i in range(n)]

for i in range(n):
    x[i] = -np.log(1-u[i])/theta0



def g (x, m):
    return ( np.log(2) / m) * np.exp(- np.log(2) * x / m )

def getProd (x, m, n):
    prod = 1
    for i in range(n):
        prod *= g(x[i], m)

    return prod


m = [0.05*(i+3) for i in range(200)]

y = [ np.log(getProd(x, m[i], n)) for i in range(200)]

plt.plot(m, y)
plt.show()


print(u)
print(x)
