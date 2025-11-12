"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example

# def square_root(a):
#     if a < 0:
#         raise ValueError("a is negative")
#     else:
#         return math.sqrt(a)

# def hypotenuse(a,b):
#     return math.hypot(a,b)

def add(a, b): 
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError("a is 0")
    else:
        return b/a

def log(a,b):
    if b <= 0:
        raise ValueError("b is less than or equal to 0")
    elif a <=0:
        raise ValueError("a is less than or equal to 0")
    else:
        return math.log(b, a)

def exp(a,b):
    return a**b