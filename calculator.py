"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example

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



def add(a, b): 
    return a+b

def sub(a,b):
    return a-b


def mul(a,b):
    return a*b


def log(a,b):
    if b <= 0:
        raise ValueError("b is less than or equal to 0")
    elif a <=0:
        raise ValueError("a is less than or equal to 0")
    else:
        return math.log(b, a)

def exp(a,b):
    return a**b