import numpy as np
import matplotlib.pyplot as plt

functions = [
    {"name": "B",
     "x": [0.0, 0.1, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],
     "y": [2.00000, 1.95533, 1.62160, 1.36235, 1.07073, 0.77279, 0.49515, 0.26260]
     }
]


def approximation0(y):
    a1 = sum(y) / len(y)

    sum_squared_error = 0
    max_error = 0
    for yi in y:
        sum_squared_error += (yi - a1) ** 2
        err = abs(yi - a1)
        if err > max_error:
            max_error = err

    return a1


def approximation1(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum([x ** 2 for x in x])
    sum_xy = sum([y * x for x, y in zip(x, y)])
    denominator = n * sum_x2 - sum_x ** 2

    a_1 = (sum_x2 * sum_y - sum_x * sum_xy) / denominator
    a_2 = (n * sum_xy - sum_x * sum_y) / denominator

    return a_1, a_2


calculate_polynomial_values = lambda coefficients, x: [coefficients[0] + coefficients[1] * xi for xi in x]


def compute_error0(y):
    sum_squared_error = 0
    max_error = 0
    for yi in y:
        sum_squared_error += (yi - a1) ** 2
        err = abs(yi - a1)
        if err > max_error:
            max_error = err
    return max_error, sum_squared_error


def compute_error1(x, y):
    sum_squared_error = 0
    max_error = 0
    for xi, yi in zip(x, y):
        sum_squared_error += (yi - a2 * xi - a1) ** 2
        err = abs(yi - a2 * xi - a1)
        if err > max_error:
            max_error = err
    return max_error, sum_squared_error


# Sample usage
x_values = functions[0]["x"]
y_values = functions[0]["y"]

a1 = approximation0(y_values)

max_error, sum_of_squares = compute_error0(y_values)

print("Max Error:", max_error)
print("Sum of Squares of Residuals:", sum_of_squares)

a1, a2 = approximation1(x_values, y_values)

max_error, sum_of_squares = compute_error1(x_values, y_values)

print("Max Error:", max_error)
print("Sum of Squares of Residuals:", sum_of_squares)
plt.figure(figsize=(10, 8))
plt.scatter(x_values, y_values, color='blue', label='Input Data')

a1 = approximation0(y_values)
plt.plot(x_values, [a1] * len(x_values), color='red', label='Approximation 0')

a1, a2 = approximation1(x_values, y_values)
plt.plot(x_values, [a2 * xi + a1 for xi in x_values], color='green', label='Approximation 1')

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.title('Data and Approximations')
plt.show()
