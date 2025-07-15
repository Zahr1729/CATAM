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

    y[1] = y[0] + h*f(x[0], y[0])
    x[1] = x[0] + h

    # A-B now
    for i in range(1, N):
        #print(str(i) + " & " + str(x[i]) + " & " + str(g(x[i])) + " & " + str(y[i]) + "\\\\")
        y[i+1] = y[i] + h*( 1.5 * f(x[i], y[i]) - 0.5 * f(x[i-1], y[i-1]) )
        x[i+1] = x[i] + h

    return y[N] - g(0.16)
    

for k in range(16):
    n = 2**k
    h = 0.16/n
    En = GetError(h, n)
    print(En)
    x[k] = math.log(abs(h))
    y[k] = math.log(abs(En))

plt.plot(x,y)
plt.show()

