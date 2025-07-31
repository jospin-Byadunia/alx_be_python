import unittest
from simple_calculator import SimpleCalculator

class SimpleCalculatorTest(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(3,4),7)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10,8),2)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2,6),12)
    def test_division(self):
        self.assertEqual(self.calc.divide(10,2), 5)
    def test_divide_by_zero(self):
        self.assertEqual(self.calc.divide(12,0), None)