import matplotlib.pyplot as plt
import numpy

r = 1.21
t = 0.43

fig = plt.figure()
ax = fig.add_subplot(aspect = 'equal')

circle = plt.Circle((0, 0), 1, linewidth = 1.5, edgecolor = 'red', facecolor = "none")
ax.add_patch(circle)

circle = plt.Circle((r*numpy.cos(t), r*numpy.sin(t)), numpy.sqrt(r*r- 1), linewidth = 1.5, edgecolor = 'blue', facecolor = "none")
ax.add_patch(circle)

x = [0, r*numpy.cos(t), numpy.cos(t + numpy.arccos(1/r)), 0]
y = [0, r*numpy.sin(t), numpy.sin(t + numpy.arccos(1/r)), 0]

plt.plot(x, y, color = "black")

plt.show()