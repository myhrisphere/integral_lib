import numpy as np

# Metoda trapezów
def trapezoidal_method(func, a, b, n):
    x = np.linspace(a, b, n)
    y = func(x)
    return np.trapz(y, x)

# Metoda Simpsona
def simpson_method(func, a, b, n):
    x = np.linspace(a, b, n)
    y = func(x)
    return np.sum((x[1] - x[0]) / 3 * (y[:-1] + 4 * y[1:-1:2] + y[2::2]))
