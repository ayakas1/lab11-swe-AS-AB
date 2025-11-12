"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def add(a, b): 
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    try:
        return b/a
    except ZeroDivisionError as error:
        print("Caught zero division error: ", str(error))

def log(a,b):
    try:
        return math.log(b, a)
    except ValueError as error:
        print("Caught value error: ", str(error))

def exp(a,b):
    return a**b