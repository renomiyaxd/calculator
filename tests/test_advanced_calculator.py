# tests/test_advanced_calculator.py

import unittest
from calculator import add, subtract, multiply, divide


class TestAdvancedCalculator(unittest.TestCase):
    def test_add_floats(self):
        self.assertAlmostEqual(add(1.1, 2.2), 3.3)
        self.assertAlmostEqual(add(-1.1, 1.1), 0.0)
        self.assertAlmostEqual(add(-1.1, -1.1), -2.2)

    def test_subtract_floats(self):
        self.assertAlmostEqual(subtract(2.2, 1.1), 1.1)
        self.assertAlmostEqual(subtract(-1.1, -1.1), 0.0)
        self.assertAlmostEqual(subtract(-1.1, 1.1), -2.2)

    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply(2.0, 3.5), 7.0)
        self.assertAlmostEqual(multiply(-1.0, 1.5), -1.5)
        self.assertAlmostEqual(multiply(-1.2, -1.2), 1.44)

    def test_divide_floats(self):
        self.assertAlmostEqual(divide(7.0, 3.5), 2.0)
        self.assertAlmostEqual(divide(-1.0, 1.5), -0.6666667, places=6)
        self.assertAlmostEqual(divide(-1.5, -1.5), 1.0)
        with self.assertRaises(ValueError):
            divide(1.0, 0.0)


if __name__ == '__main__':
    unittest.main()

