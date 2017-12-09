import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def test_add(self):
        calculator = SimpleCalculator()
        self.assertEqual(calculator.add(2,3), 5)
        with self.assertRaises(TypeError):
            calculator.add(2,3,4)

if __name__ == '__main__':
    unittest.main()
