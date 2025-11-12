#https://github.com/ayakas1/lab11-swe-AS-AB
# Partner 1: Ayaka Shiomitsu
# Partner 2: Amelia Boobyer



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
    if a ==0:
        raise ZeroDivisionError("Error")
    else:
        c = b/a
        return c
def log(a,b):
        if a <= 0:
            raise ValueError("Error")
        else:
            c= math.log(b,a)
            return c

def exp(a,b):
    c = pow(a,b)
    return c

def logarithm(a,b):
    if a <= 0:
        raise ValueError("Error")
    else:
        c= math.log(b,a)
        return c


def subtract(a,b):
    c = a - b
    return c
