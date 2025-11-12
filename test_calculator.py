import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(12, mul(4,3))
        self.assertEqual(10, mul(2,5))
        self.assertEqual(-30, mul(-15,2))



    def test_divide(self): # 3 assertions
        self.assertEqual(12, mul(4,60))
        with self.assertRaises(ZeroDivisionError):
            (mul(0,3))
        self.assertEqual(-4, mul(-2,8))
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        #call log function inside, example:
        with self.assertRaises(ValueError):
            log(0, 5)

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