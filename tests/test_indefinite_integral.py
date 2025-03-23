import unittest
from integral_lib.indefinite_integral import calculate, calculate_derivative, calculate_primitive
from sympy import symbols

x = symbols('x')

class TestIndefiniteIntegral(unittest.TestCase):
    def test_square(self):
        self.assertEqual(str(calculate(lambda x: x**2)), 'x**3/3')

    def test_derivative(self):
        self.assertEqual(str(calculate_derivative(lambda x: x**3)), '3*x**2')

    def test_primitive(self):
        self.assertEqual(str(calculate_primitive(lambda x: x**2)), 'x**3/3')

    # Test funkcji stałej (całka powinna być liniowa)
    def test_indefinite_constant(self):
        self.assertEqual(str(calculate(lambda x: 5)), '5*x')

    # Test pochodnej funkcji liniowej (powinna dać stałą)
    def test_derivative_linear(self):
        self.assertEqual(str(calculate_derivative(lambda x: 5*x + 3)), '5')
