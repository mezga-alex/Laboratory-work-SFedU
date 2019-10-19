import numpy as np
import matplotlib.pyplot as plt


# Plotting
def build_plot(polygon):
    # Polygon
    p = plt.Polygon(polygon, color='red')
    plt.gca().add_patch(p)

    # Axes processing
    plt.axis('equal')
    plt.axhline(linewidth=2, color='black')
    plt.axvline(linewidth=2, color='black')
    plt.grid()

    plt.show()


# Check if the polygon is convex
# Vector product usage
def is_convex_polygon(polygon):
    num_of_angles = len(polygon)
    if num_of_angles < 3:
        return False

    prev_sign = -1.0
    zero_angle_times = 0
    for i in range(num_of_angles):
        j = (i + 1) % num_of_angles
        k = (i + 2) % num_of_angles

        ab_x = polygon[j, 0] - polygon[i, 0]
        ab_y = polygon[j, 1] - polygon[i, 1]

        bc_x = polygon[k, 0] - polygon[j, 0]
        bc_y = polygon[k, 1] - polygon[j, 1]

        # Direction of rotation
        sign = np.sign(ab_x * bc_y - ab_y * bc_x)

        if i == 0:
            prev_sign = sign

        if sign != prev_sign and sign != 0:
            return False
        if sign == 0:
            zero_angle_times += 1

    # Let degenerate polygons aren't convex
    if zero_angle_times == num_of_angles:
        return False
    else:
        return True


# The polygon area calculating
# Shoelace formula (Gauss's area formula)
def area(polygon):
    num_of_angles = len(polygon)
    S = 0
    for i in range(num_of_angles):
        j = (i + 1) % num_of_angles

        S += polygon[i, 0] * polygon[j, 1] - polygon[j, 0] * polygon[i, 1]
    S = abs(0.5 * S)
    return S


