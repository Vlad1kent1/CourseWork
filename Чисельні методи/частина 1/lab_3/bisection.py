import math

func = lambda x: 2 * math.cos(x / 2) - math.exp(x) + 1

def bisection_method(a, b, eps):
    xl = a  # Ліва границя відрізка
    xp = b  # Права границя відрізка
    iteration = 0
    roots = []

    while (xp - xl) / 2 > eps:
        xx = (xl + xp) / 2  # Середина відрізка

        print(f"Iteration {iteration}: xl = {xl}, xx = {xx}, xp = {xp}")

        if func(xx) == 0:
            roots.append(xx)

        if func(xl) * func(xx) < 0:
            xp = xx
        else:
            xl = xx

        iteration += 1

    if func(xl) * func(xp) <= 0:
        roots.append((xl + xp) / 2)

    for root in roots:
        residual = abs(func(root))
        print(f"Root: {root}, Residual: {residual}")


epsilont = 1e-3
bisection_method(0,2, epsilont)
# print("")
# bisection_method(-5, -2, epsilont)
