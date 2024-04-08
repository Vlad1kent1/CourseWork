from copy import copy
from matplotlib import pyplot as plt

functions = [
    {"name": "A",
     "x": [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
     "y": [0.00000, 0.09983, 0.19866, 0.29552, 0.38941, 0.47942, 0.56464, 0.64421, 0.71735, 0.78332],
     "points": [0.052, 0.303, 0.891,
                0.445, 0.778, 0.801,
                0.115, 0.256, 0.669,
                0.224, 0.575, 0.832,
                0.033, 0.555, 0.782,
                0.226, 0.431, 0.669,
                0.114, 0.357, 0.802,
                0.335, 0.551, 0.844,
                0.011, 0.449, 0.723,
                0.225, 0.578, 0.805]
     },

    {"name": "B",
     "x": [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
     "y": [2.00000, 1.95533, 1.82533, 1.62160, 1.36235, 1.07073, 0.77279, 0.49515, 0.26260, 0.09592],
     "points": [0.122, 0.554, 0.812,
                0.054, 0.335, 0.774,
                0.221, 0.408, 0.681,
                0.084, 0.178, 0.455,
                0.351, 0.485, 0.804,
                0.108, 0.337, 0.687,
                0.224, 0.447, 0.771,
                0.066, 0.368, 0.623,
                0.311, 0.587, 0.776,
                0.188, 0.258, 0.691]
     },

    {"name": "C",
     "x": [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
     "y": [0.00000, 0.22140, 0.49182, 0.82211, 1.22554, 1.71828, 2.32011, 3.05519, 3.95303, 5.04964],
     "points": [0.221, 0.428, 0.681,
                0.128, 0.258, 0.691,
                0.224, 0.447, 0.771,
                0.172, 0.534, 0.832,
                0.331, 0.537, 0.716,
                0.012, 0.551, 0.808,
                0.284, 0.454, 0.633,
                0.087, 0.441, 0.777,
                0.405, 0.661, 0.822,
                0.216, 0.486, 0.714]
     }]
h = 0.1
n = 10


def find_diff(y):
    diff = [[]]
    diff[0] = copy(y)
    for i in range(1, len(y)):
        diff.append([])
        for j in range(len(diff[i - 1]) - 1):
            diff[i].append(diff[i - 1][j + 1] - diff[i - 1][j])
    return diff


def forward(diff, point, x0):
    s = (point - x0) / h
    L = diff[0][0]
    for i in range(1, len(x)):
        a = 1
        for j in range(1, i + 1):
            a *= (s - j + 1) / j
        L += a * diff[i][0]
    return L


def backward(diff, point, xn):
    s = (point - xn) / h
    L = diff[0][-1]
    for i in range(1, len(x)):
        a = 1
        for j in range(1, i + 1):
            a *= (s + j - 1) / j
        L += a * diff[i][-1]
    return L


for func in functions:
    name = func["name"]
    x = func["x"]
    y = func["y"]
    points = func["points"]
    diff = find_diff(y)

    print(f'\n\nФункція {name}:')
    forward_points = []
    print("\nІнтерполювання вперед: ")
    forward_points = [forward(diff, point, x[0]) for point in points]
    for point, forward_point in zip(points, forward_points):
        print(f"{point:.3f} : {forward_point:.20f}")

    backward_points = []
    print("\nІнтерполювання назад: ")
    backward_points = [backward(diff, point, x[-1]) for point in points]
    for point, backward_point in zip(points, backward_points):
        print(f"{point:.3f} : {backward_point:.20f}")

    plt.scatter(x, y, color='blue', label='Функція')
    plt.scatter(points, forward_points, color='red', label='Точки інтерполяції вперед')
    plt.title(f"Forward method for func {name}")
    plt.legend()
    plt.show()

    plt.scatter(x, y, color='blue', label='Функція')
    plt.scatter(points, backward_points, color='red', label='Точки інтерполяції назад')
    plt.title(f"Backward method for func {name}")
    plt.legend()
    plt.show()
