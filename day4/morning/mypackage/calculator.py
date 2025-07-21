"""
Calculator Module - Part of MyPackage
=====================================

This module provides a Calculator class with various mathematical operations.
"""

import math

class Calculator:
    """A calculator class with history tracking"""
    
    def __init__(self):
        self.history = []
        self.memory = 0
    
    def add(self, a, b):
        """Add two numbers"""
        result = a + b
        self._record_operation(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract two numbers"""
        result = a - b
        self._record_operation(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        result = a * b
        self._record_operation(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self._record_operation(f"{a} / {b} = {result}")
        return result
    
    def power(self, base, exponent):
        """Calculate base raised to the power of exponent"""
        result = base ** exponent
        self._record_operation(f"{base} ^ {exponent} = {result}")
        return result
    
    def sqrt(self, n):
        """Calculate square root"""
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = math.sqrt(n)
        self._record_operation(f"√{n} = {result}")
        return result
    
    def factorial(self, n):
        """Calculate factorial"""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        result = math.factorial(n)
        self._record_operation(f"{n}! = {result}")
        return result
    
    def sin(self, angle_degrees):
        """Calculate sine of angle in degrees"""
        angle_radians = math.radians(angle_degrees)
        result = math.sin(angle_radians)
        self._record_operation(f"sin({angle_degrees}°) = {result}")
        return result
    
    def cos(self, angle_degrees):
        """Calculate cosine of angle in degrees"""
        angle_radians = math.radians(angle_degrees)
        result = math.cos(angle_radians)
        self._record_operation(f"cos({angle_degrees}°) = {result}")
        return result
    
    def tan(self, angle_degrees):
        """Calculate tangent of angle in degrees"""
        angle_radians = math.radians(angle_degrees)
        result = math.tan(angle_radians)
        self._record_operation(f"tan({angle_degrees}°) = {result}")
        return result
    
    def memory_store(self, value):
        """Store value in memory"""
        self.memory = value
        self._record_operation(f"Memory stored: {value}")
    
    def memory_recall(self):
        """Recall value from memory"""
        self._record_operation(f"Memory recalled: {self.memory}")
        return self.memory
    
    def memory_clear(self):
        """Clear memory"""
        self.memory = 0
        self._record_operation("Memory cleared")
    
    def get_history(self):
        """Get calculation history"""
        return self.history.copy()
    
    def clear_history(self):
        """Clear calculation history"""
        self.history = []
    
    def _record_operation(self, operation):
        """Record an operation in history"""
        self.history.append(operation)
    
    def __str__(self):
        """String representation of calculator"""
        return f"Calculator (Memory: {self.memory}, History: {len(self.history)} operations)"
