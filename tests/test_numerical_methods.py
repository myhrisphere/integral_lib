import unittest
from integral_lib.numerical_methods import trapezoidal_method, simpson_method

class TestNumericalMethods(unittest.TestCase):
    def test_trapezoidal(self):
        result = trapezoidal_method(lambda x: x**2, 0, 2, 100)
        self.assertAlmostEqual(result, 8/3, places=2)

    def test_simpson(self):
        result = simpson_method(lambda x: x**2, 0, 2, 100)
        self.assertAlmostEqual(result, 8/3, places=2)

    # Test funkcji stałej (całka powinna być równa powierzchni prostokąta)
    def test_trapezoidal_constant(self):
        result = trapezoidal_method(lambda x: 5, 0, 2, 100)
        self.assertAlmostEqual(result, 10, places=2)

    def test_simpson_constant(self):
        result = simpson_method(lambda x: 5, 0, 2, 100)
        self.assertAlmostEqual(result, 10, places=2)
