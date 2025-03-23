import unittest
from integral_lib.definite_integral import calculate, calculate_double_integral, calculate_triple_integral

class TestDefiniteIntegral(unittest.TestCase):
    def test_square(self):
        self.assertEqual(calculate(lambda x: x**2, 0, 2), 8/3)

    def test_double_integral(self):
        result = calculate_double_integral(lambda x, y: x * y, (0, 1), (0, 1))
        self.assertEqual(result, 0.25)

    def test_triple_integral(self):
        result = calculate_triple_integral(lambda x, y, z: x * y * z, (0, 1), (0, 1), (0, 1))
        self.assertEqual(result, 0.125)

    # Test krańcowy – całka z zera powinna dać zero
    def test_definite_zero(self):
        result = calculate(lambda x: 0, 0, 10)
        self.assertEqual(result, 0)

    # Test na symetrię (całka z -x od -a do a powinna dać 0)
    def test_definite_symmetry(self):
        result = calculate(lambda x: -x, -1, 1)
        self.assertEqual(result, 0)
