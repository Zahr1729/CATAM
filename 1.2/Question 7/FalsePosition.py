# False position method
import math
import matplotlib.pyplot as plt
import numpy

def y(p, x):
    a = (4 * p**2 - 1)**0.5
    b = (2/a) * ((1+x)**0.5) * math.sin(numpy.log(1+x)*a/2)
    return b

# Compute value of y_p(1) with associated step size.
def phi(p):
    h = (2**(-10))
    N = (2**10)
    #print("THONK")
    return ComputeYn(h, N, p, 2)
    

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

    return y[N]




def FindRoot (p1, p2, phi1, phi2, eps):
    ps = ( phi2 * p1 - phi1 * p2 )/( phi2 - phi1 )
    print(str(p1) + " & " + str(p2) + " & " + str(ps) + "\\\\")

    phis = phi(ps)
    if (abs(phis) < eps): return ps
    if (phis * phi1 > 0): return FindRoot(ps, p2, phis, phi2, eps)
    return FindRoot(p1, ps, phi1, phis, eps)



eps = 1 * 10**(-7)
p2 = 5
p1 = 4
p = FindRoot(p1, p2, phi(p1), phi(p2), eps)
true = (1/4 + (math.pi/numpy.log(2))**2)**0.5
print(p, phi(p), y(p, 1), true, p-true)
