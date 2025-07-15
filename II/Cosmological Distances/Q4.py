import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def SetupAxes (x, y, ytext = 'amogus', showGrid=True):

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
    plt.ylabel(ytext, color='white')
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


def ComputeValues(z, Omega_m = 0.27, Omega_Lambda = 0.73):
    Omega_k = 1 - Omega_m - Omega_Lambda

    DADH = 0

    def E(x):
        return np.sqrt(Omega_m * np.power((1+x),3) + Omega_k * np.power(1+x, 2) + Omega_Lambda)

    x = np.linspace(0, z, 1000)
    y = 1/ E(x)
    DCDH = np.trapz(y, dx=z * 0.001)
    if (Omega_k == 0):
        DADH = DCDH / (1+z)
    elif (Omega_k > 0):
        DADH = 1/ (np.sqrt(Omega_k) * (1+z)) * np.sinh(np.sqrt(Omega_k) * DCDH)
    else:
        DADH = 1/ (np.sqrt(Omega_k) * (1+z)) * np.sin(np.sqrt(Omega_k) * DCDH)

    DLDH = (1+z)**2 * DADH
    return DADH, DLDH

n=50
z = np.array(np.linspace(0, 7, n))

DADHs =[[0 for j in range(n)] for i in range(3)]
DLDHs =[[0 for j in range(n)] for i in range(3)]

for i in range(n):
    DADHs[0][i], DLDHs[0][i] = ComputeValues(z[i], Omega_m = 1, Omega_Lambda = 0)
    DADHs[1][i], DLDHs[1][i] = ComputeValues(z[i], Omega_m = 0.04, Omega_Lambda = 0)
    DADHs[2][i], DLDHs[2][i] = ComputeValues(z[i], Omega_m = 0.27, Omega_Lambda = 0.73)

fig1, ax1 = SetupAxes(z, DADHs, ytext='DA/DH')
for i in range(3):
    plt.plot(z, DADHs[i])
ax1.legend(['Einstein-de-Sitter', 'Baryon Dominated', 'Currently Popular'])

fig2, ax2 = SetupAxes(z, DLDHs, ytext='DL/DH')
for i in range(3):
    plt.plot(z, DLDHs[i])
ax2.legend(['Einstein-de-Sitter', 'Baryon Dominated', 'Currently Popular'])
plt.show()

z = [1, 1.25, 2, 4]

DADHs =[[0 for j in range(4)] for i in range(3)]
DLDHs =[[0 for j in range(4)] for i in range(3)]

for i in range(4):
    DADHs[0][i], DLDHs[0][i] = ComputeValues(z[i], Omega_m = 1, Omega_Lambda = 0)
    DADHs[1][i], DLDHs[1][i] = ComputeValues(z[i], Omega_m = 0.04, Omega_Lambda = 0)
    DADHs[2][i], DLDHs[2][i] = ComputeValues(z[i], Omega_m = 0.27, Omega_Lambda = 0.73)

for i in range(3):
    print(DADHs[i])
    print(DLDHs[i])
    print("\n")