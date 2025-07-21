"""
Package Usage Example
====================

This file demonstrates how to use the mypackage package.
"""

# Different ways to import from packages
from mypackage import Calculator, TextProcessor, FileHandler
from mypackage.utils import quick_math, quick_text, generate_password
import mypackage

def demonstrate_package_usage():
    """Demonstrate various ways to use the package"""
    print("PACKAGE USAGE DEMONSTRATION")
    print("=" * 50)
    
    # Show package info
    print("\n1. PACKAGE INFORMATION:")
    print(f"Package Info: {mypackage.get_package_info()}")
    print("Available modules:")
    for module in mypackage.list_modules():
        print(f"  - {module}")
    
    # Use Calculator class
    print("\n2. CALCULATOR CLASS:")
    calc = Calculator()
    print(f"Calculator: {calc}")
    
    # Perform calculations
    result1 = calc.add(10, 5)
    result2 = calc.multiply(result1, 2)
    result3 = calc.power(2, 8)
    
    print(f"10 + 5 = {result1}")
    print(f"{result1} * 2 = {result2}")
    print(f"2^8 = {result3}")
    
    # Show calculation history
    print("Calculation History:")
    for operation in calc.get_history():
        print(f"  {operation}")
    
    # Use TextProcessor class
    print("\n3. TEXT PROCESSOR CLASS:")
    text_proc = TextProcessor()
    print(f"Text Processor: {text_proc}")
    
    sample_text = "Hello, World! This is a SAMPLE text with numbers 123 and 456."
    
    cleaned = text_proc.clean_text(sample_text)
    words = text_proc.extract_words(sample_text)
    word_count = text_proc.count_words(sample_text)
    stats = text_proc.get_text_stats(sample_text)
    
    print(f"Original: {sample_text}")
    print(f"Cleaned: {cleaned}")
    print(f"Words: {words[:5]}...")  # Show first 5 words
    print(f"Word count: {dict(list(word_count.items())[:3])}...")  # Show first 3 word counts
    print(f"Stats: {stats}")
    
    # Use FileHandler class
    print("\n4. FILE HANDLER CLASS:")
    file_handler = FileHandler()
    print(f"File Handler: {file_handler}")
    
    # Create a sample file
    test_filename = "test_file.txt"
    test_content = "This is a test file created by the FileHandler class."
    
    try:
        file_handler.write_text_file(test_filename, test_content)
        print(f"Created file: {test_filename}")
        
        # Read the file back
        read_content = file_handler.read_text_file(test_filename)
        print(f"Read content: {read_content}")
        
        # Get file info
        file_info = file_handler.get_file_info(test_filename)
        print(f"File info: {file_info}")
        
        # Clean up
        file_handler.delete_file(test_filename)
        print(f"Deleted file: {test_filename}")
        
    except Exception as e:
        print(f"File operations error: {e}")
    
    # Use utility functions
    print("\n5. UTILITY FUNCTIONS:")
    
    # Quick math operations
    print("Quick Math:")
    print(f"  Add: {quick_math('add', 15, 25)}")
    print(f"  Multiply: {quick_math('multiply', 6, 7)}")
    print(f"  Average: {quick_math('average', 10, 20, 30, 40)}")
    
    # Quick text operations
    print("Quick Text:")
    test_text = "Hello World"
    print(f"  Original: {test_text}")
    print(f"  Upper: {quick_text('upper', test_text)}")
    print(f"  Reverse: {quick_text('reverse', test_text)}")
    print(f"  Length: {quick_text('length', test_text)}")
    
    # Generate password
    password = generate_password(12, include_special=True)
    print(f"Generated password: {password}")

def demonstrate_advanced_features():
    """Demonstrate advanced package features"""
    print("\n" + "=" * 50)
    print("ADVANCED PACKAGE FEATURES")
    print("=" * 50)
    
    # Advanced calculator features
    print("\n1. ADVANCED CALCULATOR:")
    calc = Calculator()
    
    # Trigonometric functions
    print(f"sin(30°) = {calc.sin(30):.4f}")
    print(f"cos(60°) = {calc.cos(60):.4f}")
    print(f"tan(45°) = {calc.tan(45):.4f}")
    
    # Memory operations
    calc.memory_store(42)
    print(f"Memory stored: {calc.memory_recall()}")
    
    # Square root and factorial
    print(f"√16 = {calc.sqrt(16)}")
    print(f"5! = {calc.factorial(5)}")
    
    # Advanced text processing
    print("\n2. ADVANCED TEXT PROCESSING:")
    text_proc = TextProcessor()
    
    sample_text = "The quick brown fox jumps over the lazy dog. This sentence contains every letter of the alphabet!"
    
    longest_word = text_proc.find_longest_word(sample_text)
    shortest_word = text_proc.find_shortest_word(sample_text)
    reversed_words = text_proc.reverse_words(sample_text)
    
    print(f"Longest word: {longest_word}")
    print(f"Shortest word: {shortest_word}")
    print(f"Reversed words: {reversed_words}")
    
    # Extract information
    email_text = "Contact us at support@example.com or admin@test.org"
    emails = text_proc.extract_emails(email_text)
    print(f"Extracted emails: {emails}")
    
    # Advanced utility functions
    print("\n3. ADVANCED UTILITIES:")
    from mypackage.utils import (
        hash_text, format_bytes, get_timestamp, 
        validate_email, chunk_list, remove_duplicates
    )
    
    # Hashing
    text_to_hash = "Hello, World!"
    print(f"Text: {text_to_hash}")
    print(f"SHA256 hash: {hash_text(text_to_hash)}")
    
    # Format bytes
    print(f"File size: {format_bytes(1024 * 1024 * 5)}")  # 5MB
    
    # Timestamp
    print(f"Current time: {get_timestamp('readable')}")
    
    # Email validation
    emails_to_test = ["valid@example.com", "invalid.email", "test@domain.co.uk"]
    for email in emails_to_test:
        print(f"Email '{email}' is valid: {validate_email(email)}")
    
    # List operations
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    chunks = chunk_list(numbers, 3)
    print(f"List chunks: {chunks}")
    
    duplicates = [1, 2, 2, 3, 3, 3, 4, 5, 5]
    unique = remove_duplicates(duplicates)
    print(f"Removed duplicates: {unique}")

def main():
    """Main function to run all demonstrations"""
    print("PYTHON PACKAGE DEMONSTRATION")
    print("=" * 60)
    
    demonstrate_package_usage()
    demonstrate_advanced_features()
    
    print("\n" + "=" * 60)
    print("Package demonstration complete!")
    print("You've learned how to:")
    print("- Create and organize packages")
    print("- Import classes and functions from packages")
    print("- Use package initialization files")
    print("- Create reusable, modular code")

if __name__ == "__main__":
    main()
