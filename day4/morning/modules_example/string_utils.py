"""
String Utilities Module
======================

This module provides string manipulation utilities.
Demonstrates module creation with various string operations.
"""

import re
import string

def reverse_string(text):
    """Reverse a string"""
    return text[::-1]

def is_palindrome(text):
    """Check if a string is a palindrome"""
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def count_words(text):
    """Count words in a string"""
    return len(text.split())

def count_characters(text, include_spaces=True):
    """Count characters in a string"""
    if include_spaces:
        return len(text)
    else:
        return len(text.replace(" ", ""))

def capitalize_words(text):
    """Capitalize first letter of each word"""
    return text.title()

def remove_punctuation(text):
    """Remove punctuation from a string"""
    return text.translate(str.maketrans("", "", string.punctuation))

def extract_numbers(text):
    """Extract all numbers from a string"""
    return re.findall(r'\d+', text)

def extract_emails(text):
    """Extract email addresses from a string"""
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

def slugify(text):
    """Convert text to URL-friendly slug"""
    # Convert to lowercase and replace spaces with hyphens
    slug = text.lower().replace(" ", "-")
    # Remove non-alphanumeric characters except hyphens
    slug = re.sub(r'[^a-z0-9\-]', '', slug)
    # Remove multiple consecutive hyphens
    slug = re.sub(r'-+', '-', slug)
    # Remove leading/trailing hyphens
    return slug.strip('-')

def truncate_text(text, max_length, suffix="..."):
    """Truncate text to specified length with optional suffix"""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix

def mask_sensitive_data(text, mask_char="*"):
    """Mask sensitive data like credit card numbers"""
    # Mask credit card numbers (keep first 4 and last 4 digits)
    cc_pattern = r'\b(\d{4})\d{8}(\d{4})\b'
    text = re.sub(cc_pattern, r'\1********\2', text)
    
    # Mask email addresses (keep first character and domain)
    email_pattern = r'\b(\w)[^@]*@([^@]+\.[^@]+)\b'
    text = re.sub(email_pattern, r'\1****@\2', text)
    
    return text

# Module testing
if __name__ == "__main__":
    print("Testing String Utilities Module")
    print("=" * 35)
    
    test_string = "Hello, World! This is a test string."
    
    print(f"Original: {test_string}")
    print(f"Reversed: {reverse_string(test_string)}")
    print(f"Word count: {count_words(test_string)}")
    print(f"Character count: {count_characters(test_string)}")
    print(f"Capitalized: {capitalize_words(test_string)}")
    print(f"No punctuation: {remove_punctuation(test_string)}")
    print(f"Palindrome check: {is_palindrome('racecar')}")
    print(f"Slugified: {slugify(test_string)}")
    print(f"Truncated: {truncate_text(test_string, 20)}")
    
    # Test with numbers and emails
    mixed_text = "Call me at 123-456-7890 or email me at user@example.com"
    print(f"\nMixed text: {mixed_text}")
    print(f"Numbers: {extract_numbers(mixed_text)}")
    print(f"Emails: {extract_emails(mixed_text)}")
    
    # Test sensitive data masking
    sensitive = "Credit card: 1234567890123456, email: john.doe@example.com"
    print(f"\nSensitive: {sensitive}")
    print(f"Masked: {mask_sensitive_data(sensitive)}")
