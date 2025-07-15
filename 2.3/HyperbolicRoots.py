import matplotlib.pyplot as plt
import numpy
import HyperbolicTriangles as ht

def DrawRootsPolygon(r, n):

    # Maths

    a = [0 for i in range(n)]
    b = [0 for i in range(n)]
    rad = [0 for i in range(n)]

    fig = plt.figure()
    ax = fig.add_subplot(aspect = 'equal')

    x = [r*numpy.cos(2*i*numpy.pi/n) for i in range(n)]
    y = [r*numpy.sin(2*i*numpy.pi/n) for i in range(n)]

    p = []
    q = []

    for i in range(n):
        a[i], b[i], rad[i] = ht.ComputeCircle(x[i], y[i], x[(i+1) % n], y[(i+1) % n])
        p1, q1 = ht.GenerateCirclePoints(a[i], b[i], rad[i], x[i], y[i], x[(i+1) % n], y[(i+1) % n])
        p = p + p1
        q = q + q1

    mag2 = a[0]*a[0] + b[0]*b[0]
    l = 1- (numpy.sqrt(mag2 - 1))/numpy.sqrt(mag2)


    #Graphics

    circle = plt.Circle((0, 0), 1, edgecolor = 'red', facecolor = "none")
    ax.add_patch(circle)

    plt.plot(p, q, color = "black")
    ax.fill(p, q, color = "pink")

    for i in range(n):
        plt.plot([0, a[i]*l], [0, b[i]*l], color = "black")
        plt.plot([0, x[i]], [0, y[i]], color = "black")
        plt.plot(x[i], y[i], marker="o", markersize = 5, markerfacecolor = "red", markeredgecolor = "black")
        plt.plot(a[i]*l, b[i]*l, marker="o", markersize = 5, markerfacecolor = "blue", markeredgecolor = "black")
            

    ax.set_xlim((-1.2, 1.2))
    ax.set_ylim((-1.2, 1.2))

    plt.show()

def DrawAngleNgon(n):
    if (n <= 6): return
    r = numpy.tanh(1/2 * numpy.arccosh(1/(numpy.sqrt(3)*numpy.tan(numpy.pi/n))))
    print(r)
    DrawRootsPolygon(r, n)

DrawAngleNgon(17)