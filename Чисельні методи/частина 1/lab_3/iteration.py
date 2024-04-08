import math

func = lambda x: 2 * math.cos(x / 2) - math.exp(x) + 1
rho = lambda x: 1 / (2 * math.sin(x / 2) - math.exp(x))
phi = lambda x: x + rho(x) * func(x)

def simple_iteration(a, tol):
    x = a
    iteration = 0

    while True:
        x_next = phi(x)
        residual = abs(x_next - x)

        print(f"Iteration {iteration}: x_{iteration + 1} = {x_next}, Iterations: {iteration + 1}, Residual: {residual}")

        if residual < tol:
            break

        x = x_next
        iteration += 1

    return x_next


tolerance_5 = 1e-5
tolerance_6 = 1e-6
tolerance_8 = 1e-8

print("\nWith tolerance 10^-5:")
root_5 = simple_iteration(0.5, tolerance_5)
print("\nWith tolerance 10^-6:")
root_6 = simple_iteration(0.5, tolerance_6)
print("\nWith tolerance 10^-8:")
root_8 = simple_iteration(0.5, tolerance_8)

# print("\nWith tolerance 10^-5:")
# root_5 = simple_iteration(-4, tolerance_5)
# print("\nWith tolerance 10^-6:")
# root_6 = simple_iteration(-4, tolerance_6)
# print("\nWith tolerance 10^-8:")
# root_8 = simple_iteration(-4, tolerance_8)
