import unittest
import calc

class TestCal(unittest.TestCase):
    def test_add(self):
        result = calc.add(5,5)
        self.assertEqual(result,10)

    def test_sub(self):
        result = calc.sub(5,5)
        self.assertEqual(result,0)

    def test_mult(self):
        result = calc.mult(5,5)
        self.assertEqual(result,25)

    def test_devide(self):
        result = calc.devide(5,5)
        self.assertEqual(result,1)

if __name__ == '__main__':
    unittest.main()