from sympy import symbols, integrate

x, y, z = symbols('x y z')

# Całka oznaczona pojedyncza
def calculate(func, a, b):
    result = integrate(func(x), (x, a, b))
    return result

# Całka podwójna
def calculate_double_integral(func, x_range, y_range):
    result = integrate(
        integrate(func(x, y), (x, x_range[0], x_range[1])),
        (y, y_range[0], y_range[1])
    )
    return result

# Całka potrójna
def calculate_triple_integral(func, x_range, y_range, z_range):
    result = integrate(
        integrate(
            integrate(func(x, y, z), (x, x_range[0], x_range[1])),
            (y, y_range[0], y_range[1])
        ),
        (z, z_range[0], z_range[1])
    )
    return result
