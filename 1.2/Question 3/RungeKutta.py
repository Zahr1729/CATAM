# Runge-Kutta

import math
import matplotlib.pyplot as plt

h = 0.08
N = 27

y = [0 for i in range(N)]
x = [0 for i in range(N)]


def f(x, y):
    z = -8*y + 6 * ((math.e)**(-2*x))
    return z

def g(x):
    z = (math.e)**(-2*x) - (math.e)**(-8*x)
    return z


for i in range(0, N-1):
    
    k1 = f(x[i], y[i])
    k2 = f(x[i] + 0.5 * h, y[i] + 0.5 * h * k1)
    k3 = f(x[i] + 0.5 * h, y[i] + 0.5 * h * k2)
    k4 = f(x[i] + h, y[i] + h * k3)
    y[i+1] = y[i] + h*( k1 + 2*k2 + 2*k3 + k4 ) / 6
    x[i+1] = x[i] + h


plt.plot(x, y)

plt.show()
