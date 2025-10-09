# Feature: Added multiply and divide functions
# Feature: Added power and square_root functions
"""
Calculator module
Contains basic arithmetic functions.
"""


def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract two numbers"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Return a raised to the power of b"""
    return a**b


def square_root(a):
    """Return the square root of a"""
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return a**0.5
