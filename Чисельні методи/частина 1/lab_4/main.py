import math

func = lambda x: 2 * math.cos(x / 2) - math.exp(x) + 1

def secant(a, b, E):
    iteration = 0
    x_next = 0
    while True:
        x_next = b - func(b) * (b - a) / (func(b) - func(a))
        residual = abs(x_next - b)
        a = b
        b = x_next
        iteration += 1
        if residual / a < E:
            break

    print("Root of the given equation =", x_next)
    print(f"Iteration {iteration}")
    print(f"Residual: {residual}")

def run_secant(a, b, tolerances):
    for tolerance in tolerances:
        print(f"\nWith tolerance {tolerance}:")
        secant(a, b, tolerance)

a = 0
b = 2
tolerances = [1e-5, 1e-6, 1e-8]

print("\nFor [0; 2]:")
run_secant(a, b, tolerances)

# a = -5
# b = -2
#
# print("\nFor [-5; -2]:")
# run_secant(a, b, tolerances)
