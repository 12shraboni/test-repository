def f(x):
    return x**3 - x - 1
def bisection_method(a, b, tol):
    if f(a) * f(b) >= 0:
        print("The bisection method requires that f(a) and f(b) have opposite signs.")
        return None
    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2.0
root = bisection_method(1, 2, 0.001)
print("Approximate Root:",root)
