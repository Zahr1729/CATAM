import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def SetupAxes (x, y, showGrid=True):

    x = np.array(x)
    y = np.array(y)
    xMax = np.max(x)
    xMin = 0
    yMax = np.max(y)
    yMin = 0
    dx = (xMax - xMin) / 20
    dy = (yMax - yMin) / 20

    fig, ax = plt.subplots()
    plt.xlabel('Redshift', color='white')
    plt.ylabel('Lookback Time', color='white')
    fig.set_facecolor("black")
    ax.set_facecolor("black")
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.tick_params(colors='white')
    ax.set_xlim(xMin, xMax+dx)
    ax.set_ylim(yMin, yMax+dy)
    if (showGrid):
        ax.grid(color='white', linewidth=0.4, alpha=0.3, zorder=0)
    return fig, ax


def ComputeLookbackTime (z, h = 0.72, Omega_m = 0.27, Omega_Lambda = 0.73, n = 10000):
    Omega_k = 1 - Omega_m - Omega_Lambda
    tH = 3.0856 * 10**17 / (10**8 * 60 * 60 * 24 * 365 * h)

    def E(x):
        return np.sqrt(Omega_m * np.power((1+x),3) + Omega_k * np.power(1+x, 2) + Omega_Lambda)
    
    x = np.linspace(0, z, n)
    y = 1/ ((x + 1) * E(x))
    integral = tH * np.trapz(y, dx=z/n)
    return integral





zs = np.array([0.1, 1.0, 2.0, 4.0, 6.7])
times =[[0 for j in range(5)] for i in range(4)]

for i in range(5):
    times[0][i] = ComputeLookbackTime(zs[i], Omega_m = 1, Omega_Lambda = 0)
    times[1][i] = ComputeLookbackTime(zs[i], Omega_m = 2, Omega_Lambda = 0)
    times[2][i] = ComputeLookbackTime(zs[i], Omega_m = 0.04, Omega_Lambda = 0)
    times[3][i] = ComputeLookbackTime(zs[i], Omega_m = 0.27, Omega_Lambda = 0.73)
print(times)

n = 100
zs = np.linspace(0, 8, n)
times =[[0 for j in range(n)] for i in range(4)]


for i in range(n):
    times[0][i] = ComputeLookbackTime(zs[i], Omega_m = 1, Omega_Lambda = 0)
    times[1][i] = ComputeLookbackTime(zs[i], Omega_m = 2, Omega_Lambda = 0)
    times[2][i] = ComputeLookbackTime(zs[i], Omega_m = 0.04, Omega_Lambda = 0)
    times[3][i] = ComputeLookbackTime(zs[i], Omega_m = 0.27, Omega_Lambda = 0.73)


fig, ax = SetupAxes(zs, times)

for i in range(4):
    plt.plot(zs, times[i])
ax.legend(['Einstein-de-Sitter', 'Classical Closed', 'Baryon Dominated', 'Currently Popular'])
plt.show()

print(ComputeLookbackTime(10000, Omega_m = 1, Omega_Lambda = 0, n= 100000))
print(ComputeLookbackTime(10000, Omega_m = 2, Omega_Lambda = 0, n= 100000))
print(ComputeLookbackTime(10000, Omega_m = 0.04, Omega_Lambda = 0, n= 100000))
print(ComputeLookbackTime(10000, Omega_m = 0.27, Omega_Lambda = 0.73, n= 100000))