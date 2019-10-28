import numpy as np
from scipy.special import comb
import matplotlib.pyplot as plt


def build_plot(bezier_start_points, curve_points):
    plt.plot(curve_points[0], curve_points[1])
    first_last_elements = np.array([[bezier_start_points[0][0], bezier_start_points[0][-1]],
                                   [bezier_start_points[1][0], bezier_start_points[1][-1]]])
    plt.plot(first_last_elements[0], first_last_elements[1], "ro-", linewidth=0.7)
    plt.plot(bezier_start_points[0], bezier_start_points[1], "ro-", linewidth=0.7)

    # Axes processing
    plt.axis('equal')
    plt.axhline(linewidth=1, color='black')
    plt.axvline(linewidth=1, color='black')
    plt.grid()

    plt.show()


def bernstein_poly(i, n, t):
    return comb(n, i) * (t**(n-i)) * (1 - t)**i


def bezier_curve(points, n_t=1000):
    n_points = len(points)
    x_points = np.array([p[0] for p in points])
    y_points = np.array([p[1] for p in points])

    t = np.linspace(0.0, 1.0, n_t)

    polynomial_array = np.array([bernstein_poly(i, n_points-1, t) for i in range(0, n_points)])

    xvals = np.dot(x_points, polynomial_array)
    yvals = np.dot(y_points, polynomial_array)

    return xvals, yvals
