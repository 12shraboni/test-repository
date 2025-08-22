def f(x):
    return x**3 - x - 1
def regular_falsi_method(a, b, tol):
    if f(a) * f(b) >= 0:
        print("The regular falsi method requires that f(a) and f(b) have opposite signs.")
        return None
    c=a
    while True:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if abs(f(c)) < tol:
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
root = regular_falsi_method(1, 2, 0.001)
print("Approximate Root:", root)