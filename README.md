# Integral Library

The library allows for calculating definite and indefinite integrals using both analytical and numerical methods.

## Installation
```bash
pip install git+https://github.com/myhrisphere/integral_lib.git
````
## Usage exmaple
```python
from integral_lib.definite_integral import calculate as calculate_definite
from integral_lib.indefinite_integral import calculate as calculate_indefinite
from integral_lib.numerical_methods import trapezoidal_method, simpson_method, midpoint_method

# Example usage
result = calculate_definite(lambda x: x**2, 0, 2)
print(result) # Output: 8/3
```

## Features
 - **Calculating Definite Integrals:** Calculates the definite integral of a function between two points using symbolic computation.
 - **Calculating Indefinite Integrals:** Computes the indefinite integral (antiderivative) of a function symbolically.
 - **Trapezoidal Rule:** Approximates the integral using the trapezoidal rule.
 - **Simpson's Rule:** Approximates the integral using Simpson's rule for higher accuracy.
 - **Midpoint Rule:** Approximates the integral using the midpoint rule.
 - **Derivative Calculation:** Calculates the derivative of a function symbolically.
 - **Antiderivative Calculation:** Computes the antiderivative of a function symbolically.
 - **Function Plotting:** Plots the function and highlights the area under the curve for a visual representation of the integral.
