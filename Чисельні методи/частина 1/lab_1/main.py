import numpy as np

coefficients = np.array([
    [0.43, 0.045, -0.02, 0.03, -0.02],
    [0.12, 0.37, 0.02, 0, -0.01],
    [0.01, 0.032, 0.356, -0.02, 0.05],
    [0.12, -0.11, 0, 0.49, 0.112],
    [-0.05, 0, 0.025, -0.01, 0.294]
])

constants = np.array([0.78, -0.38, 1.91, -1.464, 2.362]).transpose()
epsilon = 1e-2

def check(x_n, x_n1):
    x = abs(x_n - x_n1)
    max = x[0]
    for i in range(len(x) - 1):
        if x[i] <= x[i+1]:
            max = x[i+1]
    return max

def simple_iteration(epsilon):
    x_current = np.zeros(len(constants)).transpose()
    x_next = np.zeros(len(constants)).transpose()
    iteration_count = 0

    while True:
        for i in range(len(constants)):
            x_next[i] = x_current[i] - np.dot(coefficients[i], x_current) + constants[i]
        iteration_count += 1
        if check(x_next, x_current) < epsilon:
            break
        x_current = x_next.copy()
    residuals = np.dot(coefficients, x_next) - constants

    print(f'Solution: {x_next}\nIterations: {iteration_count}\nResiduals: {residuals}')


for i in range(3):
    print(f'For epsilon: {epsilon}')
    simple_iteration(epsilon)
    epsilon *= epsilon
