"""
My Package - A Complete Package Example
=======================================

This package demonstrates how to organize Python code into packages.
It includes multiple modules with different functionalities.
"""

# Package version
__version__ = "1.0.0"

# Package author
__author__ = "Your Name"

# Define what gets imported when someone does "from mypackage import *"
__all__ = [
    'Calculator',
    'TextProcessor',
    'FileHandler',
    'quick_math',
    'quick_text'
]

# Import key classes and functions for easy access
from .calculator import Calculator
from .text_processor import TextProcessor
from .file_handler import FileHandler
from .utils import quick_math, quick_text

# Package-level convenience functions
def get_package_info():
    """Get information about this package"""
    return {
        'name': 'mypackage',
        'version': __version__,
        'author': __author__,
        'description': 'A demonstration package for Python learning'
    }

def list_modules():
    """List all available modules in this package"""
    return [
        'calculator - Mathematical operations',
        'text_processor - Text manipulation utilities',
        'file_handler - File I/O operations',
        'utils - Quick utility functions'
    ]

# Package initialization message
print(f"Initializing MyPackage v{__version__}")
