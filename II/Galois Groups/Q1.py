import numpy as np

def GetInverses (p):
    inv = [0 for i in range(p)]
    for i in range(1, p):
        if (inv[i] != 0): continue
        for j in range(1, p):
            if ((i*j) % p != 1): continue
            inv[i] = j
            inv[j] = i
            break

    return inv

# Work under assumption that deg f >= deg g
def NegatePoly(p, inv, f, degf):
    h = [-f[i] % p for i in range(degf + 1)]
    return h

def AddPolys(p, inv, f, degf, g, degg):
    h = [0 for i in range(degf + 1)]
    for i in range(degg + 1):
        h[i] = (f[i] + g[i]) % p
    
    for i in range(degg + 1, degf + 1):
        h[i] = f[i] % p
    
    return h

def SubProcedure(p, inv, f, degf, g, degg):
    q = f[degf] * inv[g[degg]] % p

    r = [f[i] for i in range(degf + 1)]
    for i in range(degg + 1):
        r[i + degf - degg] = (r[i + degf - degg] - q * g[i]) % p
    
    return q, r

def Reduce(f):
    d = 0
    for i in range(len(f)):
        if (f[i] != 0):
            d = i

    return f[:d+1], d

def GetQuotRem (p, inv, f, degf, g, degg):
    r = [f[i] for i in range(degf + 1)]
    q = [0 for i in range(degf - degg + 1)]
    
    for i in range(degf - degg + 1):
        q[degf - degg - i], r = SubProcedure(p, inv, r, degf - i, g, degg)
    
    r, degr = Reduce(r)

    return q, r, degr

def PolysHCF (p, inv, f, degf, g, degg):
    degh = degf
    h = [f[i] for i in range(degf+1)]
    degk = degg
    k = [g[i] for i in range(degg+1)]

    while (degk > 0 or k[0] != 0):
        q, r, degr = GetQuotRem(p, inv, h, degh, k, degk)
        h = k
        degh = degk
        k = r
        degk = degr
    
    for i in range(degh+1):
        h[i] = h[i] * inv[h[degh]] % p

    return h, degh


def GenRandPoly(p):
    deg = np.random.randint(1, 7)
    f = [1 for i in range(deg+1)]
    for i in range(0, deg):
        f[i] = np.random.randint(1, 100) % p
    return f, deg

def Test():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
    for i in range(5):
        p = primes[np.random.randint(0, len(primes))]
        inv = GetInverses(p)
        f, degf = GenRandPoly(p)
        g, degg = GenRandPoly(p)
        print(p, f, g, end=" ")
        print(GetQuotRem(p, inv, f, degf, g, degg), end=" ")
        print(PolysHCF(p, inv, f, degf, g, degg), end=" ")
        print()

if __name__ == "__main__":
    Test()
