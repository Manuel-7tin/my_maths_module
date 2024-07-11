def f(x, c1, e1, c2, e2, c3):
    return c1*(x**e1) + c2*(x**e2) + c3

def f_prime(x, c1, e1, c2, e2):
    de = e1-1
    c = c2*(x**e2)
    return e1*c1*(x**de) + c

def newton_raphson(x0, eqn, tolerance=1e-7, max_iterations=1000):
    x = x0
    for i in range(max_iterations):
        fx = f(x, eqn[0], eqn[1], eqn[2], eqn[3], eqn[4])
        fpx = f_prime(x, eqn[0], eqn[1], eqn[2], eqn[3])
        if abs(fpx) < tolerance:
            print("Derivative too small. Stopping iteration.")
            return None, None
        x_new = x - fx / fpx
        if abs(x_new - x) < tolerance:
            return x_new, 1000 - max_iterations
        x = x_new
    print("Exceeded maximum iterations. No solution found.")
    return None, None

# Initial guess
x0 = 2.0

# Create equations 1 and 2
# Eq1: x³ - x - 1 = 0
# Eq2: x³ - 2x - 5 = 0
equations = [(1, 3, -1, 1, -1), (1, 3, -2, 1, -5)]

for equation in equations:
    root, iteration = newton_raphson(x0, equation)
    
    if root is not None:
        print(f"Root found: x = {root:.7f}")
    else:
        print("No root found.")
