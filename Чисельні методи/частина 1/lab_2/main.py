import numpy as np
import numpy as np

coeff_matrix = np.array([
    [0.43, 0.045, -0.02, 0.03, -0.02],
    [0.12, 0.37, 0.02, 0, -0.01],
    [0.01, 0.032, 0.356, -0.02, 0.05],
    [0.12, -0.11, 0, 0.49, 0.112],
    [-0.05, 0, 0.025, -0.01, 0.294]
])

constants = np.array([0.78, -0.38, 1.91, -1.464, 2.362]).transpose()
epsilon = 1e-2


def solve_equation(eps):
    x_current = np.zeros(len(constants)).transpose()
    x_next = np.zeros(len(constants)).transpose()
    iteration_count = 0

    while True:
        for i in range(len(constants)):
            first_sum = sum(coeff_matrix[i][j] / coeff_matrix[i][i] * x_current[j] for j in range(i))
            second_sum = sum(coeff_matrix[i][j] / coeff_matrix[i][i] * x_current[j] for j in range(i + 1, len(constants)))
            x_next[i] = - first_sum - second_sum + constants[i] / coeff_matrix[i][i]
        iteration_count += 1
        if np.linalg.norm(x_next - x_current) < eps:
            break
        x_current = x_next.copy()
    residuals = np.dot(coeff_matrix, x_next) - constants

    print(f'Solution: {x_next}\nIterations: {iteration_count}\nResiduals: {residuals}')


for i in range(3):
    print(f'For epsilon: {epsilon}')
    solve_equation(epsilon)
    epsilon *= epsilon
