import Numbers
import unittest

class numtest(unittest.TestCase):

    def test(self):
        num1 = 5
        num2 = 10
        total = 15
        res = Numbers.num().add(num1, num2)
        self.assertEqual(total, res)

    def dividetest(self):
        num1 = 10
        num2 = 2
        total = 5
        res = Numbers.num().divide(num1, num2)
        self.assertEqual(total, res)

if __name__ == "__main__":
    unittest.main()

