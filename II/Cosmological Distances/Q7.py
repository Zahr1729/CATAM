from Q6 import *

def UpdatedGetVolumes(z, ff0, h = 0.72, Omega_m = 0.27, Omega_Lambda = 0.73):
    # Using Giga-Lightyears
    DH = h * 9.26 * 1.057

    DC0DH, DA0DH, DL0DH = ComputeValues(0.2, Omega_m=Omega_m, Omega_Lambda=Omega_Lambda)
    DC0 = DH * DC0DH
    DC1DH, DA1DH, DL1DH = ComputeValues(3, Omega_m=Omega_m, Omega_Lambda=Omega_Lambda)
    DC1 = DH * DC1DH

    V0 = 4 * np.pi / 3 * DC0**3
    V1 = 4 * np.pi / 3 * DC1**3

    V, Vmax = GetVolumes(z, ff0, h = 0.72, Omega_m = Omega_m, Omega_Lambda = Omega_Lambda)
    V -= V0
    Vmax -= V0
    Vmax = min(Vmax, V1 - V0)

    if (V > Vmax):
        print(z, ff0, V, Vmax)

    return V, Vmax


def UpdatedAveragePerUniverse(n, z, ff0, Omega_m):
    Omega_Lambda = 1 - Omega_m

    tot = 0
    for i in range(n):
        V, Vmax = UpdatedGetVolumes(z[i], ff0[i], Omega_m=Omega_m, Omega_Lambda=Omega_Lambda)
        VVmax = V/Vmax
        tot += (VVmax)

    avg = tot/n
    return avg


if __name__ == "__main__":
    n = 114

    z = []
    ff0 = []
    with open("quasar.csv", 'r') as file:
        csvreader = csv.reader(file)

        for row in csvreader:
            z.append(float(row[0]))
            ff0.append(float(row[1]))

    n = len(z)

    avgEin = UpdatedAveragePerUniverse(n, z, ff0, 1)
    avgPop = UpdatedAveragePerUniverse(n, z, ff0, 0.27)
    print("AVERAGE: ", avgEin, "Popular: ", avgPop)