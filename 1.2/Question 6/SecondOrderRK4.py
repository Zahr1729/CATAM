# Runge-Kutta on second order

import math
import matplotlib.pyplot as plt
import numpy


def ye(x):
    a = (4 * p**2 - 1)**0.5
    b = (2/a) * ((1+x)**0.5) * math.sin(numpy.log(1+x)*a/2)
    return b

def ComputeYn(h, N):
    global alpha
    global p
    alpha = 2
    p = 5

    x = [0 for i in range(N+1)]
    y = [0 for i in range(N+1)]
    z = [0 for i in range(N+1)]

    z[0] = 1


    def f(x, y, z):
        return z

    def g(x, y, z):
        return -(p**2) * ((1+x)**(-alpha)) * y



    for i in range(0, N):

        x[i+1] = x[i] + h
        
        k1 = f(x[i], y[i], z[i])
        t1 = g(x[i], y[i], z[i])
        
        k2 = f(x[i] + 0.5 * h, y[i] + 0.5 * h * k1, z[i] + 0.5 * h * t1)
        t2 = g(x[i] + 0.5 * h, y[i] + 0.5 * h * k1, z[i] + 0.5 * h * t1)
        
        k3 = f(x[i] + 0.5 * h, y[i] + 0.5 * h * k2, z[i] + 0.5 * h * t2)
        t3 = g(x[i] + 0.5 * h, y[i] + 0.5 * h * k2, z[i] + 0.5 * h * t2)
        
        k4 = f(x[i] + h, y[i] + h * k3, z[i] + h * t3)
        t4 = g(x[i] + h, y[i] + h * k3, z[i] + h * t3)
        
        y[i+1] = y[i] + h*( k1 + 2*k2 + 2*k3 + k4 ) / 6 
        z[i+1] = z[i] + h*( t1 + 2*t2 + 2*t3 + t4 ) / 6


    #plt.plot(x, y)

    return y[N]


# Actual program
x = [0 for i in range(13)]
y = [0 for i in range(13)]
E = [0 for i in range(13)]



for k in range(13):
    h = 0.1 / (2**k)
    N = 10 * (2**k)
    
    x[k] = h
    y[k] = ComputeYn(h,N)
    E[k] = y[k] - ye(1)

    if (k != 0):
        print(str(k) + " & " + str(x[k]) + " & " + str(y[k]) + " & " + str(E[k]) + " & " + str(E[k-1]/E[k]) + " \\\\")
    else:
        print(str(k) + " & " + str(x[k]) + " & " + str(y[k]) + " & " + str(E[k]) + " & \\\\")


#plt.plot(x, y)
plt.plot(x, E)

plt.show()
