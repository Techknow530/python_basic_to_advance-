"""
Math Utilities Module
====================

This module provides common mathematical operations and constants.
It demonstrates how to create a reusable module.
"""

import math

# Module-level constants
PI = 3.14159
E = 2.71828

# Module-level variables
calculation_history = []

def add(a, b):
    """Add two numbers and record the operation"""
    result = a + b
    calculation_history.append(f"{a} + {b} = {result}")
    return result

def subtract(a, b):
    """Subtract two numbers and record the operation"""
    result = a - b
    calculation_history.append(f"{a} - {b} = {result}")
    return result

def multiply(a, b):
    """Multiply two numbers and record the operation"""
    result = a * b
    calculation_history.append(f"{a} * {b} = {result}")
    return result

def divide(a, b):
    """Divide two numbers with error handling"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    result = a / b
    calculation_history.append(f"{a} / {b} = {result}")
    return result

def power(base, exponent):
    """Calculate base raised to the power of exponent"""
    result = base ** exponent
    calculation_history.append(f"{base} ^ {exponent} = {result}")
    return result

def factorial(n):
    """Calculate factorial of n"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = math.factorial(n)
    calculation_history.append(f"{n}! = {result}")
    return result

def circle_area(radius):
    """Calculate area of a circle"""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    result = PI * radius ** 2
    calculation_history.append(f"Circle area (r={radius}) = {result}")
    return result

def circle_circumference(radius):
    """Calculate circumference of a circle"""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    result = 2 * PI * radius
    calculation_history.append(f"Circle circumference (r={radius}) = {result}")
    return result

def get_history():
    """Return the calculation history"""
    return calculation_history.copy()

def clear_history():
    """Clear the calculation history"""
    global calculation_history
    calculation_history = []

# Module testing
if __name__ == "__main__":
    print("Testing Math Utilities Module")
    print("=" * 30)
    
    # Test basic operations
    print(f"Add: {add(5, 3)}")
    print(f"Subtract: {subtract(10, 4)}")
    print(f"Multiply: {multiply(6, 7)}")
    print(f"Divide: {divide(15, 3)}")
    print(f"Power: {power(2, 8)}")
    print(f"Factorial: {factorial(5)}")
    print(f"Circle area: {circle_area(5)}")
    print(f"Circle circumference: {circle_circumference(5)}")
    
    # Show history
    print("\nCalculation History:")
    for item in get_history():
        print(f"  {item}")
    
    # Test error handling
    try:
        divide(10, 0)
    except ValueError as e:
        print(f"Error caught: {e}")
    
    try:
        factorial(-1)
    except ValueError as e:
        print(f"Error caught: {e}")
