from sympy import symbols, integrate, diff

x = symbols('x')

# Całka nieoznaczona
def calculate(func):
    result = integrate(func(x))
    return result

# Pochodna funkcji
def calculate_derivative(func):
    result = diff(func(x))
    return result

# Funkcja pierwotna (odwrotność pochodnej)
def calculate_primitive(func):
    result = integrate(func(x))
    return result
