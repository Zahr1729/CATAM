import matplotlib.pyplot as plt
import numpy
import HyperbolicTriangles as ht
import SphericalTriangles as st

def R1 (x, y):
    return x, -y

def R2 (x, y, p):
    X = x*numpy.cos(2*numpy.pi/p) + y*numpy.sin(2*numpy.pi/p)
    Y =x*numpy.sin(2*numpy.pi/p) - y*numpy.cos(2*numpy.pi/p)
    return X, Y

def R3 (a, b, r, x, y):
    x1, y1 = x - a, y - b
    norm = x1*x1 + y1*y1
    x2 = r*r*x1/norm
    y2 = r*r*y1/norm
    return x2 + a, y2 + b

# Mobius map version of R3
def R3Other(a, b, r, x, y):
    if (x == None): return a, b
    if (x == a and y == b): return None, None

    c1 = r*r - a*a - b*b
    z2 = x*x + y*y
    c2 = a*a - b*b
    c3 = 2*a*b
    sq = (x-a)*(x-a) + (y-b)*(y-b)

    re = (c1 * (x-a) + a*z2 - (c2*x +c3*y) )/sq
    im = (c1 * (y-b) + b*z2 - (c3*x - c2*y) )/sq
    return re, im

def S1(a, b, r, p, x, y):
    u, v = R3(a, b, r, x, y)
    w, z = R2(u, v, p)
    return w, z

def S2(a, b, r, p, x, y):
    u, v = R1(x, y)
    w, z = R3(a, b, r, u, v)
    return w, z
        
def S3(a, b, r, p, x, y):
    u, v = R2(x, y, p)
    w, z = R1(u, v)
    return w, z

def GenerateStartingTriangleData(p):
    if (p > 6): # Hyperbolic
        r = numpy.tanh(1/2 * numpy.arccosh(1/(numpy.sqrt(3)*numpy.tan(numpy.pi/p))))
        x, y = r*numpy.cos(2*numpy.pi/p), r*numpy.sin(2*numpy.pi/p)

        a, b, rad = ht.ComputeCircle(r, 0, x, y)

        mag2 = a*a + b*b
        l = 1 - (numpy.sqrt(mag2 - 1))/numpy.sqrt(mag2)
        x3, y3 = l*a, l*b
    else: # Spherical
        r = numpy.tan(1/2 * numpy.arccos(1/(numpy.sqrt(3)*numpy.tan(numpy.pi/p))))
        x, y = r*numpy.cos(2*numpy.pi/p), r*numpy.sin(2*numpy.pi/p)

        a, b, rad = st.ComputeCircle(r, 0, x, y)

        mag2 = a*a + b*b
        l = 1 - (numpy.sqrt(mag2 + 1))/numpy.sqrt(mag2)
        x3, y3 = l*a, l*b

    return 0, 0, r, 0, x3, y3, a, b, rad

def ComputeInitialTriangle(p):
    x1, y1, x2, y2, x3, y3, a, b, rad = GenerateStartingTriangleData(p)

    if (p > 6): # Hyp
        p1, q1 = ht.GenerateCirclePoints(None, None, None, x1, y1, x2, y2)
        p2, q2 = ht.GenerateCirclePoints(a, b, rad, x2, y2, x3, y3)
        p3, q3 = ht.GenerateCirclePoints(None, None, None, x3, y3, x1, y1)
    else: # Spherical
        p1, q1 = st.GenerateCirclePoints(None, None, None, x1, y1, x2, y2)
        p2, q2 = st.GenerateCirclePoints(a, b, rad, x2, y2, x3, y3)
        p3, q3 = st.GenerateCirclePoints(None, None, None, x3, y3, x1, y1)
    
    x = p1 + p2 + p3
    y = q1 + q2 + q3

    return x, y, a, b, rad

def DrawS1(x, y, p, a, b, rad):

    l = len(x)
    pX2 = [0 for i in range(l)]
    pY2 = [0 for i in range(l)]

    for i in range(l):
        pX2[i], pY2[i] = S1(a, b, rad, p, x[i], y[i])

    fig = plt.figure()
    ax = fig.add_subplot(aspect = 'equal')

    # Guidelines
    plt.plot([-100, 100], [0, 0], color = "green")
    plt.plot([-a*100, a*100], [-b*100, b*100], color = "orange")
    circle = plt.Circle((a, b), rad, edgecolor = 'red', facecolor = "none")
    ax.add_patch(circle)

    plt.plot(x, y, color = "black")
    ax.fill(x, y, color = "red")

    plt.plot(pX2, pY2, color = "black")
    ax.fill(pX2, pY2, color = "green")

    ax.set_xlim((-0.2, 1))
    ax.set_ylim((-0.2, 1))

    if (p == 3):
        ax.set_xlim((-0.5, 1))
        ax.set_ylim((-0.2, 1.5))

    plt.show()

def DrawS2(x, y, p, a, b, rad):
    l = len(x)
    pX2 = [0 for i in range(l)]
    pX3 = [0 for i in range(l)]
    pY2 = [0 for i in range(l)]
    pY3 = [0 for i in range(l)]

    for i in range(l):
        pX2[i], pY2[i] = S2(a, b, rad, p, x[i], y[i])
        pX3[i], pY3[i] = S2(a, b, rad, p, pX2[i], pY2[i])

    fig = plt.figure()
    ax = fig.add_subplot(aspect = 'equal')

    # Guidelines
    plt.plot([-100, 100], [0, 0], color = "green")
    plt.plot([-a*100, a*100], [-b*100, b*100], color = "orange")
    circle = plt.Circle((a, b), rad, edgecolor = 'red', facecolor = "none")
    ax.add_patch(circle)

    plt.plot(x, y, color = "black")
    ax.fill(x, y, color = "red")

    plt.plot(pX2, pY2, color = "black")
    ax.fill(pX2, pY2, color = "green")

    plt.plot(pX3, pY3, color = "black")
    ax.fill(pX3, pY3, color = "blue")

    ax.set_xlim((-0.2, 1))
    ax.set_ylim((-0.6, 0.6))

    if (p <= 4):
        ax.set_xlim((-0.2, 2.4))
        ax.set_ylim((-1.3, 1.3))

    plt.show()

def DrawS3(x, y, p, a, b, rad):

    l = len(x)
    pX = x
    pY = y

    fig = plt.figure()
    ax = fig.add_subplot(aspect = 'equal')

    # Guidelines
    plt.plot([-100, 100], [0, 0], color = "green")
    plt.plot([-a*100, a*100], [-b*100, b*100], color = "orange")
    circle = plt.Circle((a, b), rad, edgecolor = 'red', facecolor = "none")
    ax.add_patch(circle)

    plt.plot(x, y, color = "black")
    ax.fill(x, y)

    for j in range(p-1):
        for i in range(l):
            pX[i], pY[i] = S3(a, b, rad, p, pX[i], pY[i])

        plt.plot(pX, pY, color = "black")
        ax.fill(pX, pY)

    ax.set_xlim((-1, 1))
    ax.set_ylim((-1, 1))

    plt.show()

def DrawElement(x, y, p, a, b, rad, path, drawPath):

    l = len(x)
    pX = x
    pY = y

    fig = plt.figure()
    ax = fig.add_subplot(aspect = 'equal')

    # Guidelines
    plt.plot([-100, 100], [0, 0], color = "green")
    plt.plot([-a*100, a*100], [-b*100, b*100], color = "orange")
    circle = plt.Circle((a, b), rad, edgecolor = 'red', facecolor = "none")
    ax.add_patch(circle)

    m = len(path)
    if (m == 0):
        plt.plot(x, y, color = "black")
        ax.fill(x, y, color = "red")

    for j in range(m):
        move = path[j]
        i = 0
        while i < l:
            match move:
                case 1:
                    pX[i], pY[i] = S1(a, b, rad, p, pX[i], pY[i])
                case 2:
                    pX[i], pY[i] = S2(a, b, rad, p, pX[i], pY[i])
                case 3:
                    pX[i], pY[i] = S3(a, b, rad, p, pX[i], pY[i])
        
            i += 1

        if (drawPath or j == m-1):
            plt.plot(pX, pY, color = "black")
            ax.fill(pX, pY)

    ax.set_xlim((-4, 4))
    ax.set_ylim((-4, 4))

    if (p > 6):
        ax.set_xlim((-1, 1))
        ax.set_ylim((-1, 1))

    plt.show()

def Main(p):
    x, y, a, b, r = ComputeInitialTriangle(p)
    DrawS3(x, y, p, a, b, r)
    #DrawElement(x, y, p, a, b, r, [1, 2, 1, 2, 1])

Main(5)