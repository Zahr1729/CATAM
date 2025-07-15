import numpy
import random

def generateNormal (mu, sigma):
    A = random.uniform(0,1)
    B = random.uniform(0,1)

    U = 2*numpy.pi*A
    V = -2 * numpy.log(1-B)

    X = mu + sigma*numpy.sqrt(V)*numpy.cos(U)
    Y = mu + sigma*numpy.sqrt(V)*numpy.sin(U)

    return X, Y


def generateN (n, mu, sigma):
    x = [0 for i in range(n)]
    for i in range(n):
        x[i] = generateNormal(mu, sigma)[0]

    return x
