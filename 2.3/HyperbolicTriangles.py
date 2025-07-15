import matplotlib.pyplot as plt
import numpy
import random


def CrossProd (x1, y1, x2, y2):
    return x1*y2 - x2*y1


def ComputeCircle (x1, y1, x2, y2):
    
    if (x1 == None or x2 == None or y1 == None or y2 == None): return None, None, None
    
    b1 = x1*x1 + y1*y1 + 1
    b2 = x2*x2 + y2*y2 + 1

    det = 4*CrossProd(x1, y1, x2, y2)

    if (det == 0): return None, None, None

    a1 = (2*y2*b1 - 2*y1*b2)/det
    a2 = (-2*x2*b1 + 2*x1*b2)/det

    r = numpy.sqrt(a1*a1 + a2*a2 - 1)

    return a1, a2, r


def ComputeArgFromCentre (x, y, b, c):
    X = x - b
    Y = y - c

    if (X == 0):
        if (Y == 0): return 0
        if (Y > 0): return numpy.pi/2
        if (Y < 0): return numpy.pi/2

    t = numpy.arctan(Y/X)

    if (X < 0):
        if (Y >= 0): t += numpy.pi
        else: t -= numpy.pi

    return t


def GenerateLinePoints (x1, y1, x2, y2):
    n = 100

    x = [x1 + (x2 - x1)*i/n for i in range(n+1)]
    y = [y1 + (y2 - y1)*i/n for i in range(n+1)]

    return x, y


def GenerateCirclePoints (b, c, r, x1, y1, x2, y2):

    # If Line then do line computations
    if (b == None): return GenerateLinePoints(x1, y1, x2, y2)
    
    # Generate points on the circle from z1 to z2
    a1 = ComputeArgFromCentre(x1, y1, b, c)
    a2 = ComputeArgFromCentre(x2, y2, b, c)

    # Use the cross product to determine which way to go, clock or anticlock.

    d = CrossProd(x1, y1, x2, y2)
    flag = numpy.sign(d)
    if (a2 < a1):
        a2 += 2*numpy.pi
    if (flag == 1):
        a2 -= 2*numpy.pi

    n = 100

    t = [a1 + (a2-a1)*i/n for i in range(n+1)]
    x = [b + r*numpy.cos(t[i]) for i in range(n+1)]
    y = [c + r*numpy.sin(t[i]) for i in range(n+1)]

    return x, y


def DrawHyperbolicTriangle (x1, y1, x2, y2, x3, y3):
    # If both are null we assume that means infinity

    # Generate Appropriate data of circles
    a1, a2, r1 = ComputeCircle(x1, y1, x2, y2)
    b1, b2, r2 = ComputeCircle(x2, y2, x3, y3)
    c1, c2, r3 = ComputeCircle(x3, y3, x1, y1)

    fig = plt.figure()
    ax = fig.add_subplot(aspect = 'equal')


    circle1 = plt.Circle((a1, a2), r1, edgecolor = 'black', facecolor = "none")
    circle2 = plt.Circle((b1, b2), r2, edgecolor = 'black', facecolor = "none")
    circle3 = plt.Circle((c1, c2), r3, edgecolor = 'black', facecolor = "none")

    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.add_patch(circle3)

    
    # Generate Points
    p1, q1 = GenerateCirclePoints(a1, a2, r1, x1, y1, x2, y2)
    p2, q2 = GenerateCirclePoints(b1, b2, r2, x2, y2, x3, y3)
    p3, q3 = GenerateCirclePoints(c1, c2, r3, x3, y3, x1, y1)

    x = p1 + p2 + p3
    y = q1 + q2 + q3

    plt.plot(x, y, color = "black")
    plt.fill(x, y, color = "pink")

    # One error about filling inside not outside when shape includes infinity
    # This is only thing that really needs to be finished up.
    
    circle = plt.Circle((0, 0), 1, linewidth = 1.5, edgecolor = 'red', facecolor = "none")
    ax.add_patch(circle)

    plt.plot(x1, y1, marker="o", markersize = 5, markerfacecolor = "red", markeredgecolor = "black")
    plt.plot(x2, y2, marker="o", markersize = 5, markerfacecolor = "green", markeredgecolor = "black")
    plt.plot(x3, y3, marker="o", markersize = 5, markerfacecolor = "blue", markeredgecolor = "black")
    
    
    ax.set_xlim((-1.5, 1.5))
    ax.set_ylim((-1.5, 1.5))
    
    plt.show()


def GenerateRandomTriangle():
    x = [0 for i in range(6)]
    for i in range(3):
        while True:
            a = random.uniform(-1,1)
            b = random.uniform(-1,1)
            if (a*a + b*b <= 1):
                x[2*i] = a
                x[2*i + 1] = b
                break

    DrawHyperbolicTriangle(x[0], x[1], x[2], x[3], x[4], x[5])
