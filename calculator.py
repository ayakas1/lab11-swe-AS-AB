"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example


def square_root(a):
    if a < 0:
        raise ValueError("a is negative")
    else:
        return math.sqrt(a)

def hypotenuse(a,b):
    return math.hypot(a,b)

import math
def add(a,b):
    c = a+ b
    return c
def sub(a,b):
    c = a - b
    return c
def mul(a,b):
    c= a*b
    return c
def div(a,b):
    try:
       if a ==0:
        raise ZeroDivisionError("Error")
       else:
        c = b/a
        return c
    except ValueError as error:
        print("Caught ValueError:",str(error))
def log(a,b):
    try:
        if a <= 0:
            raise ValueError("Error")
        else:
            c= math.log(b,a)
            return c
    except ValueError as error:
        print("Caught ValueError:", str(error))
def exp(a,b):
    c = pow(a,b)
    return c

