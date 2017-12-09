import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def test_add(self):
        calculator = SimpleCalculator()
        self.assertEqual(calculator.add(2,3), 5)
        with self.assertRaises(TypeError):
            calculator.add(2,3,4)

    def test_subtract(self):
        calculator = SimpleCalculator()
        self.assertEqual(calculator.subtract(5,2), 3)
        self.assertEqual(calculator.subtract(2,5), -3)
        with self.assertRaises(TypeError):
            calculator.subtract(2,3,4)

    def test_multiply(self):
        calculator = SimpleCalculator()
        self.assertEqual(calculator.multiply(5,3), 15)
        self.assertEqual(calculator.multiply(-5,-4), 20)
        self.assertEqual(calculator.multiply(4, -2), -8)
        self.assertEqual(calculator.multiply(-4, 8), -32)
        with self.assertRaises(TypeError):
            calculator.multiply(2,3,4)

if __name__ == '__main__':
    unittest.main()
