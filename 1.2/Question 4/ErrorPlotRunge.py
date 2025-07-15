# Plot error
import math
import matplotlib.pyplot as plt

x = [0 for i in range(16)]
y = [0 for i in range(16)]

def GetError(h, n):
    N = n
    
    y = [0 for i in range(N+1)]
    x = [0 for i in range(N+1)]

    def f(x, y):
        z = -8*y + 6 * ((math.e)**(-2*x))
        return z

    def g(x):
        z = (math.e)**(-2*x) - (math.e)**(-8*x)
        return z

    for i in range(0, N):
        #print(str(i) + " & " + str(x[i]) + " & " + str(g(x[i])) + " & " + str(y[i]) + "\\\\")

        k1 = f(x[i], y[i])
        k2 = f(x[i] + 0.5 * h, y[i] + 0.5 * h * k1)
        k3 = f(x[i] + 0.5 * h, y[i] + 0.5 * h * k2)
        k4 = f(x[i] + h, y[i] + h * k3)
        y[i+1] = y[i] + h*( k1 + 2*k2 + 2*k3 + k4 ) / 6
        x[i+1] = x[i] + h

    #print(x[N])
    return y[N] - g(0.16)
    

for k in range(16):
    n = 2**k
    h = 0.16/n
    En = GetError(h, n)
    #print(En)
    x[k] = math.log(abs(h))
    y[k] = math.log(abs(En))

    try:
        print( (y[k] - y[k-1]) / (x[k] - x[k-1]) )
    except:
        pass

plt.plot(x,y)
plt.xlim(-13, 0)
plt.show()


