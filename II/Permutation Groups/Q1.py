
def Inverse(f):
    g = [0 for i in range(len(f))]
    for i in range(len(f)):
        g[f[i]] = i
    return g

def Product(f, g):
    h = [0 for i in range(len(f))]
    for i in range(len(f)):
        h[i] = f[g[i]]
    return h


if __name__ == "__main__":
    g = [1, 3, 4, 0, 2]
    h = [2, 4, 1, 3, 0]

    print(g, h)
    print(Inverse(g))
    print(Product(g, h))