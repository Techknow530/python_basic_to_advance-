"""
Main Module - Demonstrating Module Imports
==========================================

This module shows how to import and use other modules.
"""

# Different ways to import modules
import math_utils
from string_utils import reverse_string, is_palindrome, count_words
from math_utils import add, multiply, PI

def demonstrate_imports():
    """Demonstrate different ways to import and use modules"""
    print("DEMONSTRATING MODULE IMPORTS")
    print("=" * 40)
    
    # Using fully qualified module names
    print("\n1. Using fully qualified module names:")
    result1 = math_utils.add(10, 5)
    result2 = math_utils.multiply(4, 7)
    print(f"math_utils.add(10, 5) = {result1}")
    print(f"math_utils.multiply(4, 7) = {result2}")
    print(f"Pi constant: {math_utils.PI}")
    
    # Using directly imported functions
    print("\n2. Using directly imported functions:")
    result3 = add(20, 15)  # Direct import
    result4 = multiply(3, 9)  # Direct import
    print(f"add(20, 15) = {result3}")
    print(f"multiply(3, 9) = {result4}")
    print(f"Pi constant: {PI}")
    
    # Using imported string utilities
    print("\n3. Using string utilities:")
    text = "Hello World"
    print(f"Original text: {text}")
    print(f"Reversed: {reverse_string(text)}")
    print(f"Word count: {count_words(text)}")
    print(f"Is palindrome: {is_palindrome(text)}")
    
    # Show calculation history
    print("\n4. Calculation history:")
    history = math_utils.get_history()
    for item in history:
        print(f"  {item}")

def calculator_demo():
    """Create a simple calculator using imported functions"""
    print("\nSIMPLE CALCULATOR DEMO")
    print("=" * 25)
    
    # Clear previous history
    math_utils.clear_history()
    
    # Perform calculations
    operations = [
        ("Addition", lambda: add(15, 25)),
        ("Subtraction", lambda: math_utils.subtract(50, 20)),
        ("Multiplication", lambda: multiply(6, 8)),
        ("Division", lambda: math_utils.divide(100, 4)),
        ("Power", lambda: math_utils.power(3, 4)),
        ("Factorial", lambda: math_utils.factorial(6)),
        ("Circle Area", lambda: math_utils.circle_area(10))
    ]
    
    results = {}
    for name, operation in operations:
        try:
            result = operation()
            results[name] = result
            print(f"{name}: {result}")
        except Exception as e:
            print(f"{name}: Error - {e}")
    
    return results

def text_processor_demo():
    """Demonstrate text processing with string utilities"""
    print("\nTEXT PROCESSING DEMO")
    print("=" * 25)
    
    # Import more string utilities
    from string_utils import (
        capitalize_words, remove_punctuation, 
        extract_numbers, slugify, truncate_text
    )
    
    sample_text = "Hello, World! This is a GREAT example with numbers 123 and 456."
    
    print(f"Original: {sample_text}")
    print(f"Reversed: {reverse_string(sample_text)}")
    print(f"Capitalized: {capitalize_words(sample_text)}")
    print(f"No punctuation: {remove_punctuation(sample_text)}")
    print(f"Numbers: {extract_numbers(sample_text)}")
    print(f"Slug: {slugify(sample_text)}")
    print(f"Truncated: {truncate_text(sample_text, 30)}")
    print(f"Word count: {count_words(sample_text)}")

def main():
    """Main function to run all demonstrations"""
    print("PYTHON MODULES DEMONSTRATION")
    print("=" * 50)
    
    demonstrate_imports()
    calculator_demo()
    text_processor_demo()
    
    print("\n" + "=" * 50)
    print("Module demonstration complete!")

if __name__ == "__main__":
    main()
