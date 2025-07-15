# Forward Euler
import math
import matplotlib.pyplot as plt

h = 0.08
N = 27
y = [0 for i in range(N)]
x = [0 for i in range(N)]

y[0] = 0
x[0] = 0

def f(x, y):
    z = -8*y + 6 * ((math.e)**(-2*x))
    return z

def g(x):
    z = (math.e)**(-2*x) - (math.e)**(-8*x)
    return z

for i in range(0, N-1):
    print(str(i) + " & " + str(x[i]) + " & " + str(g(x[i])) + " & " + str(y[i]) + "\\\\")
    y[i+1] = y[i] + h*f(x[i], y[i])
    x[i+1] = x[i] + h


plt.plot(x, y)
w = [i*0.01 for i in range(200)]
z = [( g(i*0.01) ) for i in range(200)]
plt.plot(w, z)
plt.show()


