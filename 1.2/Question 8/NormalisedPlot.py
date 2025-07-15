# False position method
import math
import matplotlib.pyplot as plt
import numpy


# Compute the value of Y_N with step size h with p and alpha given with RK4.
def ComputeYn(h, N, p, alpha):
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


    return x, y


def Normalise(h, N, p, alpha, y):
    # integrate and divide by integral
    integral = 0

    for i in range(1, N):
        integral += h * ( (1 + i*h)**(-10) * (p * y[i])**2 )

    integral += h * ((p*y[0])**2) / 2
    integral += h * (2**(-10) * (p*y[N])**2) / 2

    for i in range(0, N+1):
        y[i] /= integral

    return y


p = 66.6632979369170

h = (2**(-10))
N = (2**10)
x, y = ComputeYn(h, N, p, 10)
z = Normalise(h, N, p, 10, y)

plt.plot(x,z)
plt.grid()
plt.show()
