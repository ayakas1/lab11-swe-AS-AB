#https://github.com/ayakas1/lab11-swe-AS-AB
# Partner 1: Ayaka Shiomitsu
# Partner 2: Amelia Boobyer

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(3, -3), 0)
        self.assertEqual(add(-3, 4), 1)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(sub(4, 3), 1)
        self.assertEqual(sub(4, -3), 7)
        self.assertEqual(sub(-4, 3), -7)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(12, mul(4,3))
        self.assertEqual(10, mul(2,5))
        self.assertEqual(-30, mul(-15,2))



    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(15, div(4,60))
        self.assertAlmostEqual(-4, div(-2,8))
        self.assertAlmostEqual(6, div(-5,-30))
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
                div(0,5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(10,10), 1)
        self.assertEqual(log(2,8), 3)
        self.assertEqual(log(10,100), 2)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
                log(0,10)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        #call log function inside, example:
        with self.assertRaises(ValueError):
            log(5, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(5, hypotenuse(3,4))
        self.assertEqual(5, hypotenuse(-3,4))
        self.assertEqual(10, hypotenuse(8,-6))

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
           square_root(-10)
        self.assertEqual(2, square_root(4))
        self.assertEqual(3, square_root(9))

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()