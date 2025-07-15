# Adams-Bashforth

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

# Forward Euler for first one
print("0 & " + str(x[0]) + " & " + str(g(x[0])) + " & " + str(y[0]) + "\\\\")
y[1] = y[0] + h*f(x[0], y[0])
x[1] = x[0] + h

# A-B now
for i in range(1, N-1):
    print(str(i) + " & " + str(x[i]) + " & " + str(g(x[i])) + " & " + str(y[i]) + "\\\\")
    y[i+1] = y[i] + h*( 1.5 * f(x[i], y[i]) - 0.5 * f(x[i-1], y[i-1]) )
    x[i+1] = x[i] + h


plt.plot(x, y)
w = [i*0.01 for i in range(200)]
z = [( g(i*0.01) ) for i in range(200)]
plt.plot(w, z)
plt.show()


