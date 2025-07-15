import numpy as np
import csv
import matplotlib as mpl
import matplotlib.pyplot as plt

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
    plt.xlabel('(f/f_0)^(-3/2)', color='white')
    plt.ylabel('V/Vmax', color='white')
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
    return DCDH, DADH, DLDH

def GetVolumes(z, ff0, h = 0.72, Omega_m = 0.27, Omega_Lambda = 0.73):
    # Using Giga-Lightyears
    DH = h * 9.26 * 1.057

    DCDH, DADH, DLDH = ComputeValues(z, Omega_m=Omega_m, Omega_Lambda=Omega_Lambda)
    DC = DH * DCDH
    DL = DH * DLDH

    V = 4 * np.pi / 3 * DC**3

    DL0 = DL * np.sqrt(ff0)


    def E(x):
        return np.sqrt(Omega_m * np.power((1+x),3) + 0 * np.power(1+x, 2) + Omega_Lambda)

    # Find z0 (or z_max)

    # Use a bit of root finding methods to get z0

    a = DL0 / DH
    def BinarySearch(zmin, zmax):
        zmid = (zmax + zmin) / 2
        if (zmax - zmin < 10**-8): return zmid

        x = np.linspace(0,zmid, 1000)
        y = 1/E(x)
        b = (1+zmid) * np.trapz(y, dx = zmid/1000)

        if (a < b):
            return BinarySearch(zmin, zmid)
        elif (a > b):
            return BinarySearch(zmid, zmax)
        else:
            return zmid
    
    z0 = BinarySearch(z, 20)

    DC0DH, DA0DH, DL0DH = ComputeValues(z0, Omega_m=Omega_m, Omega_Lambda=Omega_Lambda)
    DC0 = DH * DC0DH

    Vmax = 4 * np.pi / 3 * DC0**3

    return  V, Vmax


def SmallRedShift():
    n = 500
    z = [np.random.rand() * 0.01 for i in range(n)]
    ff0 = [(1 + (np.random.rand() ** 2)*10) for i in range(n)]
    Omega_m = [np.random.rand() for i in range(n)]
    VVmax = [0 for i in range(n)]

    xData = [ff0[i] ** (-1.5) for i in range(n)]
    colours = [mpl.cm.rainbow(z[i]*100) for i in range(n)]

    for i in range(n):
        V, Vmax = GetVolumes(z[i], ff0[i], Omega_m=Omega_m[i], Omega_Lambda=(1-Omega_m[i]))
        VVmax[i] = V/Vmax


    fig, ax = SetupAxes(xData, VVmax)

    plt.scatter(xData, VVmax, c=colours)

    plt.show()

def AveragePerUniverse(n, z, ff0, Omega_m):
    Omega_Lambda = 1 - Omega_m

    tot = 0
    for i in range(n):
        V, Vmax = GetVolumes(z[i], ff0[i], Omega_m=Omega_m, Omega_Lambda=Omega_Lambda)
        VVmax = V/Vmax
        tot += VVmax

    avg = tot/n
    return avg



if __name__ == "__main__":
    SmallRedShift()

    n = 1

    z = [5]
    ff0 = [10]
    avg = AveragePerUniverse(n, z, ff0, 1)


    n = 114

    z = []
    ff0 = []
    with open("quasar.csv", 'r') as file:
        csvreader = csv.reader(file)
        
        for row in csvreader:
            z.append(float(row[0]))
            ff0.append(float(row[1]))

    n = len(z)

    avgEin = AveragePerUniverse(n, z, ff0, 1)
    avgPop = AveragePerUniverse(n, z, ff0, 0.27)
    print("Einstein De-Sitter: ", avgEin, "Popular: ", avgPop)