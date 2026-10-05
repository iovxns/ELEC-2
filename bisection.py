import math

def bisection(f, a, b, tol=1e-6, max_iter=100):
    """
    Finds a root of f(x) = 0 in interval [a, b] using the Bisection Method.
    Halts when half the interval width (b - a)/2 < tol.
    """
    fa = f(a)
    fb = f(b)

    if fa * fb >= 0:
        raise ValueError(f"Function must have opposite signs at endpoints a={a}, b={b}.")

    for _ in range(max_iter):
        c = (a + b) / 2.0
        fc = f(c)

        if fc == 0 or (b - a) / 2.0 < tol:
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return (a + b) / 2.0