# Write a function called plot_func() that uses matplotlib.pyplot.plot to produce a plot of the functions
# f(t) = sin(π/t) when t != 0. If t = 0, f(0) = 0.
# g(t) = t*exp{-t^2}
# over the interval [-1.0, 1.0].
# Include labels for the x- and y-axes, and a legend.
# * x-label: "t-axes"
# * y-label: "y-axes"
# * Legend
#     * f(t)
#     * g(t)
# Make sure to use enough points that the curve is closed and appears smooth.
# Note: This part will be manually graded!

import matplotlib.pyplot as plt
import math
import numpy as np

t = np.arange(-1, 1, .01)
f_t = np.sin(math.pi/t)
g_t = t * np.exp(-(t**2))
plt.plot(t, f_t, color = 'blue', label = 'f(t)')
plt.plot(t, g_t, color = 'red', label = 'g(t)')
plt.xlabel('t-axes')
plt.ylabel('y-axes')
plt.legend()
plt.show()
