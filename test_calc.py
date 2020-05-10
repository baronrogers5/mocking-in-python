import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(5, 2), 7)
        self.assertEqual(calc.add(5, -2), 3)
        self.assertEqual(calc.add(0, 0), 0)
        self.assertEqual(calc.add(-2, -2), -4)
    
    def test_mult(self):
        self.assertEqual(calc.multiply(0, 5), 0)

    def test_divide(self):
        self.assertRaises(ZeroDivisionError, calc.divide, 3, 0)
        self.assertAlmostEqual(calc.divide(10, 3), 3.333, places=3) 
    

if __name__ == "__main__":
    unittest.main()