from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(int(datetime.now().timestamp()))

inputs = np.random.uniform(-7, 7, size=(100, 2))
weights = np.array([[1, 2], [0, 0]])
b1 = 0


def neuron(inputs, weights, b):
    s = np.dot(weights, inputs)
    s = sum(s) + b

    if s > 0:
        return 1
    elif s < 0:
        return -1
    else:
        return 0


def plot_perceptron(inputs, weights, b):
    for input_point in inputs:
        output = neuron(input_point, weights, b)
        color = 'green' if output > 0 else 'yellow'
        plt.plot(input_point[0], input_point[1], marker='o', markersize=10, color=color)

    a = weights[0][0] + weights[1][0]
    b = weights[0][1] + weights[1][1]
    c = b1
    # paint the line
    x = np.linspace(-7, 7, 100)
    y = (-a * x - c) / b
    plt.plot(x, y)

    plt.xlabel('Input 1')
    plt.ylabel('Input 2')
    plt.title('Perceptron Decision Boundary with Inputs')
    plt.show()

    print(f"equation of the line of the neuron is:{a}p1+{b}p2+{b1}")


plot_perceptron(inputs, weights, b1)
