import numpy as np
import matplotlib.pyplot as plt


class Triangle(object):
    def __init__(self, x_a=None, y_a=None, z_a=1.0, x_b=None, y_b=None, z_b=1.0, x_c=None, y_c=None, z_c=1.0):
        # Triangle coordinates
        self.x_a = x_a
        self.y_a = y_a
        self.z_a = z_a
        self.x_b = x_b
        self.y_b = y_b
        self.z_b = z_b
        self.x_c = x_c
        self.y_c = y_c
        self.z_c = z_c

    def print_value(self):
        print('x_a = ', self.x_a, ' y_a = ', self.y_a, 'z_a = ', self.z_a,
              ' x_b = ', self.x_b, ' y_b = ', self.y_b, 'z_b = ', self.z_b,
              ' x_c = ', self.x_c, ' y_c = ', self.y_c, 'z_c = ', self.z_c)

    def check_value(self):
        # Check if values are numbers
        if type(self.x_a) != float:
            return False
        if type(self.y_a) != float:
            return False
        if type(self.x_b) != float:
            return False
        if type(self.y_b) != float:
            return False
        if type(self.x_c) != float:
            return False
        if type(self.y_c) != float:
            return False
        return True


class Line(object):
    def __init__(self, k=None, b=None):
        self.k = k
        self.b = b

    def print_value(self):
        print('k = ', self.k, ' b = ', self.b)

    def check_value(self):
        if type(self.k) != float:
            return False
        if type(self.b) != float:
            return False
        return True


def create_reflection_triangle(triangle, line):
    # Triangle coordinates matrix
    C = np.array([[triangle.x_a, triangle.y_a, triangle.z_a],
                 [triangle.x_b, triangle.y_b, triangle.z_b],
                 [triangle.x_c, triangle.y_c, triangle.z_c]])

    # Transfer matrix
    T = np.array([[1, 0, 0],
                  [0, 1, 0],
                  [0, -line.b, 1]])

    # Get line angle
    angle = np.arctan(line.k)

    # Rotation matrix
    cos_angle = np.cos(angle)
    sin_angle = np.sin(angle)
    R = np.array([[cos_angle, -sin_angle, 0],
                  [sin_angle, cos_angle, 0],
                  [0, 0, 1]])

    # Mirroring matrix
    M = ([[1, 0, 0],
          [0, -1, 0],
          [0, 0, 1]])

    # Inverse matrices
    T_I = np.linalg.inv(T)
    R_I = np.linalg.inv(R)

    # Create Full Conversion (F_C) matrix
    F_C = (((T.dot(R)).dot(M)).dot(R_I)).dot(T_I)

    # New coordinates
    N_C = C.dot(F_C)

    # Return new triangle
    new_triangle = Triangle(N_C[0, 0], N_C[0, 1], N_C[0, 2],
                            N_C[1, 0], N_C[1, 1], N_C[1, 2],
                            N_C[2, 0], N_C[2, 1], N_C[2, 2])
    return new_triangle


def build_plot(triangle, reflected_triangle, line):
    # Set the range of the X axis
    x_max = abs(triangle.x_a)
    if x_max < abs(triangle.x_b):
        x_max = abs(triangle.x_b)
    if x_max < abs(triangle.x_c):
        x_max = abs(triangle.x_c)

    # Start triangle polygon
    T = np.array([[triangle.x_a, triangle.y_a],
                  [triangle.x_b, triangle.y_b],
                  [triangle.x_c, triangle.y_c]])
    t1 = plt.Polygon(T[:, :], color='red')
    plt.gca().add_patch(t1)

    # Reflected triangle polygon
    T2 = np.array([[reflected_triangle.x_a, reflected_triangle.y_a],
                   [reflected_triangle.x_b, reflected_triangle.y_b],
                   [reflected_triangle.x_c, reflected_triangle.y_c]])
    t2 = plt.Polygon(T2[:, :], color='green')
    plt.gca().add_patch(t2)

    # Line
    x = np.linspace(-x_max - 2, x_max + 2, 100)
    plt.plot(x, line.k * x + line.b, 'blue', label='y=' + str(line.k) + 'x' + '+' + str(line.b))
    plt.legend(loc='upper left')
    #
    plt.axhline(linewidth=2, color='black')
    plt.axvline(linewidth=2, color='black')
    plt.axis('equal')
    #
    plt.grid()
    plt.show()
