"""
    This module provides basic arithmetic operations: addition, subtraction, multiplication, and division.
    Functions:
        add(num1, num2): Returns the sum of num1 and num2.
        subtract(num1, num2): Returns the difference between num1 and num2.
        multiply(num1, num2): Returns the product of num1 and num2.
        divide(num1, num2): Returns the quotient of num1 divided by num2, or an error message if division by zero is attempted.
"""

def add(num1, num2):
    """Returns the sum of num1 and num2."""
    """Adds two numbers and returns the result."""
    return num1 + num2

def subtract(num1, num2):
    """Returns the difference between num1 and num2."""
    """Subtracts num2 from num1 and returns the result."""
    return num1 - num2

def multiply(num1, num2):
    """Returns the product of num1 and num2."""
    """Multiplies two numbers and returns the result."""
    """Multiplies num1 by num2 and returns the result."""
    return num1 * num2

def divide(num1, num2):
    """Returns the quotient of num1 divided by num2, or an error message if division by zero is attempted."""
    """Divides num1 by num2 and returns the result, or an error message if division by zero is attempted."""
    """Divides num1 by num2 and returns the result."""
    if num2 == 0:
        return "Error! Division by zero."
    return num1 / num2

