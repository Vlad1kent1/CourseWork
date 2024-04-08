import math

f = lambda x: 1 / (5 - 3 * math.cos(x))
a = 0
b = 2 * math.pi
eps = 1e-5
n = 8
p = 2


def midpoint_rule(a, b, n, p, eps):
    iteration = 0
    integral = 0
    h = (b - a) / n
    for i in range(0, n + 1):
        xi = a + h * (i - 0.5)
        fi = f(xi)
        integral += h * fi

    while (True):
        iteration += 1

        pre_integral = integral
        n *= 2
        h /= 2
        integral = h * sum([f(a + (2 * i - 1) / 2 * h) for i in range(n)])
        if abs(integral - pre_integral) < (2 ** p - 1) * eps:
            break
    return integral + (integral - pre_integral) / (2 ** p - 1), iteration


def trapezoidal_rule(a, b, n, p, eps):
    iteration = 0
    integral = 0
    h = (b - a) / n
    for i in range(1, n):
        xi = a + h * i
        fi = f(xi)
        integral += h * fi
    integral = h * 0.5 * (f(a) + f(b))

    while (True):
        iteration += 1

        pre_integral = integral
        n *= 2
        h /= 2
        integral = integral / 2 + sum([f(a + h * i) for i in range(1, n, 2)]) * h
        if abs(integral - pre_integral) < (2 ** p - 1) * eps:
            break

    return integral + (integral - pre_integral) / (2 ** p - 1), iteration


def simpson_rule(a, b, n, p, eps):
    iteration = 0
    integral = 0
    sum1 = 0
    sum2 = 0
    h = (b - a) / (2 * n)
    for i in range(1, n):
        xi = a + 2 * i * h
        fi = f(xi)
        if i % 2 != 0:
            sum1 += 2 * fi
        else:
            sum2 += 4 * fi
    integral += (h / 3) * (f(a) + f(b)) + (h / 3) * (sum1 + sum2)

    while (True):
        iteration += 1

        pre_integral = integral
        n *= 2
        h /= 2
        sum2 += sum1
        sum1 = 0
        for i in range(1, n + 1):
            sum1 += f(a + (2 * i - 1) * h)
        integral = (h / 3) * (4 * sum1 + 2 * sum2 + f(a) + f(b))
        if abs(integral - pre_integral) < (2 ** p - 1) * eps:
            break

    return integral + (integral - pre_integral) / (2 ** p - 1), iteration


result, iterations = midpoint_rule(a, b, n, p, eps)
print("Midpoint Rule:", result, "\tIterations:", iterations)

result, iterations = trapezoidal_rule(a, b, n, p, eps)
print("Trapezoidal Rule:", result, "\tIterations:", iterations)

result, iterations = simpson_rule(a, b, n, p, eps)
print("Simpson's Rule:", result, "\tIterations:", iterations)
