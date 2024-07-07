# Code to Solve Algebraic and Transcendental Equations using Bisection method
print("Welcome to the BI-Section method")
print("--------------------------------")


def round_off(nm: float, y):
    """Round a number to a given precision in decimal digits.
        It works like the python round function but without the round-half-to-even method.
        Only works with floats and ints
        The return value has the same type as the number."""
    # Verify data type
    if type(nm) != float and type(y) != int:
        print("Error: Invalid data type!!")
        return None
    str_nm = str(nm)
    if len(str_nm) > 5:
        fix = float(f"0.{'0'*3}1")
        nm += fix if int(str_nm[2+y]) == 5 else 0
    return round(nm, y)


def f_of_x(equation, value):
    """Execute the given equation using 'value' as the unknown variable"""
    c1, e1, c2, e2 = equation.get("const-1"), equation.get("exp-1"), equation.get("const-2"), equation.get("exp-2")
    c3 = equation.get("const-3")
    return round_off(c1*(value**e1) + c2*(value**e2) + c3, 3)


def find_roots(equation):
    """Find the two roots of a given algebraic equation"""
    # Set required variables
    last_result = 0
    x = 2
    started = None
    attempts = 100
    decrement_value = 2
    decrement_sign_unsure = True

    # Create while loop to run until there's zero attempts left
    while attempts:
        # Solve equation and get result
        result = f_of_x(equation=equation, value=x)
        # Condition to check if 'x' and the last value of 'x' are not the roots
        if last_result * result >= 0:
            # This executes if it isn't the loop's first iteration,
            #   the decrement sign is unsure, and if we are going farther from the roots.
            # The decrement sign tells us whether to decrease or increase x
            if result >= last_result > 0 and started and decrement_sign_unsure:
                # Switch to decrement if we are going farther from the roots in the positive direction
                decrement_value *= -1
                decrement_sign_unsure = False
                last_result = result
            else:
                started = True
                last_result = result
                x += decrement_value
        # Otherwise if 'x' and the last value of 'x' are correct roots
        else:
            # Determine the sign to add to x to get the closest possible roots
            x_sign = int(x/abs(x)) if x != 0 else -1
            # Return x and the number before x if they are the exact roots
            if last_result * f_of_x(equation=equation, value=x + x_sign*-1) >= 0:
                root1 = x + x_sign*-1
                root2 = x
                return root1, root2
                # return x + x_sign*-1, x
            # Return the last two numbers before x if they are the exact roots
            else:
                root1 = x + x_sign*-2
                root2 = x + x_sign*-1
                return root1, root2
                # return x + x_sign *-2, x + x_sign *-1
        # Decrement available attempts by 1 with each failed iteration
        attempts -= 1
    print("roots out of reach")
    return None, None


equations = [
    {
        "const-1": 1,
        "exp-1": 3,
        "const-2": -1,
        "exp-2": 1,
        "const-3": -1
    },
    {
        "const-1": 1,
        "exp-1": 3,
        "const-2": -2,
        "exp-2": 1,
        "const-3": -5
    },
    {
        "const-1": 1,
        "exp-1": 3,
        "const-2": -2,
        "exp-2": 1,
        "const-3": 6
    },
    {
        "const-1": 1,
        "exp-1": 3,
        "const-2": -1,
        "exp-2": 1,
        "const-3": -70
    },
    {
        "const-1": 1,
        "exp-1": 3,
        "const-2": -2,
        "exp-2": 1,
        "const-3": -5
    }
]

# Set required variables
iterations = 0
tries = 100
select_equation = equations[3]
a, b = find_roots(equation=select_equation)
determinant_1 = 0
determinant_2 = 0

while tries:
    # Ensure that equation has roots
    if not a:
        print("Equation roots cannot be determined")
        break

    iterations += 1
    # Get the value of xr, the f(x) where x is a, b and xr, and the product of f(a) and f(xr)
    xr = round_off((a+b)/2, 3)
    f_of_a = f_of_x(select_equation, a)
    f_of_b = f_of_x(select_equation, b)
    f_of_xr = f_of_x(select_equation, xr)
    product_of_fs = round_off(f_of_a*f_of_xr, 3)

    # Check if correct value of xr has been determined
    if product_of_fs == 0:
        print("Hurray, Equation solved!!")
        print(f"a={a}, b={b}, xr={xr}, iterations={iterations}")
        break
    # Check if the last 2 products of f(xr).f(a) have already been set
    elif determinant_1 and determinant_2:
        # Check if the change in the last three products is between 0.005
        case1 = determinant_1-determinant_2
        case2 = determinant_2-product_of_fs
        if -0.006 < case1 < case2 < 0.006 or -0.006 < case2 < case1 < 0.006:
            print("Hurray, Equation solved!!")
            print(f"a={a}, b={b}, xr={xr}, iterations={iterations}")
            break
    # Reset a or b depending on product value
    if product_of_fs < 0:
        b = xr
    elif product_of_fs > 0:
        a = xr

    # Set last two product values
    determinant_1 = determinant_2
    determinant_2 = product_of_fs
    tries -= 1

# FOr the lecturer
# # Set required variables
# iterations = 0
# tries = 100
# select_equation = {
#         "const-1": 1,
#         "exp-1": 3,
#         "const-2": -1,
#         "exp-2": 1,
#         "const-3": -1
#     }
# a, b = 2, 1
# determinant_1 = 0
# determinant_2 = 0
#
# while tries:
#     # Ensure that equation has roots
#     if not a:
#         print("Equation roots cannot be determined")
#         break
#
#     iterations += 1
#     # Get the value of xr, the f(x) where x is a, b and xr, and the product of f(a) and f(xr)
#     xr = round_off((a+b)/2, 3)
#     f_of_a = f_of_x(select_equation, a)
#     f_of_b = f_of_x(select_equation, b)
#     f_of_xr = f_of_x(select_equation, xr)
#     product_of_fs = round_off(f_of_a*f_of_xr, 3)
#
#     # Check if correct value of xr has been determined
#     if product_of_fs == 0:
#         print("Hurray, Equation solved!!")
#         print(f"a={a}, b={b}, xr={xr}, iterations={iterations}")
#         break
#     # Check if the last 2 products of f(xr).f(a) have already been set
#     elif determinant_1 and determinant_2:
#         # Check if the change in the last three products is between 0.005
#         case1 = determinant_1-determinant_2
#         case2 = determinant_2-product_of_fs
#         if -0.006 < case1 < case2 < 0.006 or -0.006 < case2 < case1 < 0.006:
#             print("Hurray, Equation solved!!")
#             print(f"a={a}, b={b}, xr={xr}, iterations={iterations}")
#             break
#     # Reset a or b depending on product value
#     if product_of_fs < 0:
#         b = xr
#     elif product_of_fs > 0:
#         a = xr
#
#     # Set last two product values
#     determinant_1 = determinant_2
#     determinant_2 = product_of_fs
#     tries -= 1