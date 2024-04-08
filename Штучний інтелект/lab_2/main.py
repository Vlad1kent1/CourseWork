import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2


def monte_carlo(f, a, b, n, build_graph):
    randX = np.random.uniform(a, b, n)
    Y = [f(randX[i]) for i in range(n)]
    maxY = max(Y)
    randY = np.random.uniform(0, max(Y), n)

    inside_points = []
    outside_poitns = []

    for i in range(n):
        if randY[i] < Y[i]:
            inside_points.append((randX[i], randY[i]))
        else:
            outside_poitns.append((randX[i], randY[i]))

    result = (b - a) * maxY * len(inside_points) / n

    if not build_graph:
        return result

    plt.figure(figsize=(10, 6))
    x_values = np.linspace(a, b, 1000)
    plt.plot(x_values, f(x_values), color='blue', label='Function Graph')
    plt.scatter(*zip(*outside_poitns), color='red', alpha=0.5)
    plt.scatter(*zip(*inside_points), color='yellow', alpha=0.5)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

    return result


test_function = lambda x: x * x * x
main_function = lambda x: np.exp(x ** 2)

exact_integral_test_function = lambda a, b: ((b ** 4) / 4) - ((a**4)/4)

n = 10000
a = 0
b = 2

print("метод Монте Карло: ")
I2 = monte_carlo(test_function, a, b, n, True)
print("Тестова функція: ", I2)
print("Головна функція: ", monte_carlo(main_function, a, b, n, True))

e = exact_integral_test_function(a, b)
print("Похибка вимірювання значення інтеграла Тестової функції методом Монте Карло")
print("Абсолютна похибка для Тестової функції: ", np.abs(e - I2))
print("Відносна похибка для Тестової функції: ", np.abs(e - I2) / I2 * 100, "%")

num_samples = 500
alpha = 0.05
samples = [monte_carlo(main_function, a, b, n, False) for _ in range(num_samples)]
mean = sum(v for v in samples) / num_samples
variance = sum((v - mean) ** 2 for v in samples) / num_samples
chi2_lower = chi2.ppf(alpha / 2, df=num_samples - 1)
chi2_upper = chi2.ppf(1 - alpha / 2, df=num_samples - 1)
lower_bound = np.sqrt((num_samples - 1) * variance / chi2_upper)
upper_bound = np.sqrt((num_samples - 1) * variance / chi2_lower)

print("Похибка вимірювання значення інтеграла Головної функції методом Монте Карло")
print("Довірчий інтервал для середньоквадратичного відхилення")
print(f"({lower_bound:.5f}; {upper_bound:.5f})")
