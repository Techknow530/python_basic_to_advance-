"""
Utils Module - Part of MyPackage
================================

This module provides quick utility functions for common tasks.
"""

import random
import string
import hashlib
from datetime import datetime, timedelta

def quick_math(operation, *args):
    """Quick math operations without creating a Calculator instance"""
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y if y != 0 else "Error: Division by zero",
        'power': lambda x, y: x ** y,
        'max': lambda *nums: max(nums),
        'min': lambda *nums: min(nums),
        'average': lambda *nums: sum(nums) / len(nums) if nums else 0
    }
    
    if operation not in operations:
        return f"Error: Unknown operation '{operation}'"
    
    try:
        return operations[operation](*args)
    except Exception as e:
        return f"Error: {str(e)}"

def quick_text(operation, text, *args):
    """Quick text operations without creating a TextProcessor instance"""
    operations = {
        'upper': lambda t: t.upper(),
        'lower': lambda t: t.lower(),
        'title': lambda t: t.title(),
        'reverse': lambda t: t[::-1],
        'length': lambda t: len(t),
        'words': lambda t: len(t.split()),
        'replace': lambda t, old, new: t.replace(old, new),
        'startswith': lambda t, prefix: t.startswith(prefix),
        'endswith': lambda t, suffix: t.endswith(suffix),
        'contains': lambda t, substring: substring in t
    }
    
    if operation not in operations:
        return f"Error: Unknown operation '{operation}'"
    
    try:
        return operations[operation](text, *args)
    except Exception as e:
        return f"Error: {str(e)}"

def generate_random_string(length=10, include_digits=True, include_special=False):
    """Generate a random string"""
    chars = string.ascii_letters
    if include_digits:
        chars += string.digits
    if include_special:
        chars += "!@#$%^&*"
    
    return ''.join(random.choice(chars) for _ in range(length))

def generate_password(length=12, include_uppercase=True, include_lowercase=True, 
                     include_digits=True, include_special=True):
    """Generate a secure password"""
    chars = ""
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_lowercase:
        chars += string.ascii_lowercase
    if include_digits:
        chars += string.digits
    if include_special:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if not chars:
        return "Error: No character types selected"
    
    return ''.join(random.choice(chars) for _ in range(length))

def hash_text(text, algorithm='sha256'):
    """Hash text using specified algorithm"""
    algorithms = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha256': hashlib.sha256,
        'sha512': hashlib.sha512
    }
    
    if algorithm not in algorithms:
        return f"Error: Unknown algorithm '{algorithm}'"
    
    hash_func = algorithms[algorithm]()
    hash_func.update(text.encode('utf-8'))
    return hash_func.hexdigest()

def format_bytes(bytes_count):
    """Format bytes into human-readable format"""
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    size = bytes_count
    unit_index = 0
    
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1
    
    return f"{size:.2f} {units[unit_index]}"

def format_duration(seconds):
    """Format seconds into human-readable duration"""
    if seconds < 60:
        return f"{seconds:.1f} seconds"
    elif seconds < 3600:
        minutes = seconds / 60
        return f"{minutes:.1f} minutes"
    elif seconds < 86400:
        hours = seconds / 3600
        return f"{hours:.1f} hours"
    else:
        days = seconds / 86400
        return f"{days:.1f} days"

def get_timestamp(format_type='iso'):
    """Get current timestamp in various formats"""
    now = datetime.now()
    
    formats = {
        'iso': now.isoformat(),
        'readable': now.strftime('%Y-%m-%d %H:%M:%S'),
        'date': now.strftime('%Y-%m-%d'),
        'time': now.strftime('%H:%M:%S'),
        'unix': int(now.timestamp())
    }
    
    return formats.get(format_type, now.isoformat())

def add_days(date_str, days):
    """Add days to a date string"""
    try:
        date_obj = datetime.fromisoformat(date_str)
        new_date = date_obj + timedelta(days=days)
        return new_date.isoformat()
    except ValueError:
        return "Error: Invalid date format"

def days_between(date1_str, date2_str):
    """Calculate days between two dates"""
    try:
        date1 = datetime.fromisoformat(date1_str)
        date2 = datetime.fromisoformat(date2_str)
        return (date2 - date1).days
    except ValueError:
        return "Error: Invalid date format"

def validate_email(email):
    """Simple email validation"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone):
    """Simple phone number validation"""
    import re
    # Remove all non-digits
    digits = re.sub(r'\D', '', phone)
    # Check if it's a valid length (10 or 11 digits)
    return len(digits) in [10, 11]

def clean_filename(filename):
    """Clean filename by removing invalid characters"""
    import re
    # Remove invalid characters
    cleaned = re.sub(r'[<>:"/\\|?*]', '', filename)
    # Remove leading/trailing spaces and dots
    cleaned = cleaned.strip(' .')
    return cleaned

def get_file_extension(filename):
    """Get file extension from filename"""
    import os
    return os.path.splitext(filename)[1].lower()

def is_valid_url(url):
    """Simple URL validation"""
    import re
    pattern = r'^https?://[^\s/$.?#].[^\s]*$'
    return bool(re.match(pattern, url))

def truncate_middle(text, max_length, separator='...'):
    """Truncate text in the middle, keeping start and end"""
    if len(text) <= max_length:
        return text
    
    if max_length <= len(separator):
        return separator[:max_length]
    
    # Calculate lengths for start and end
    available_length = max_length - len(separator)
    start_length = available_length // 2
    end_length = available_length - start_length
    
    return text[:start_length] + separator + text[-end_length:]

def chunk_list(lst, chunk_size):
    """Split a list into chunks of specified size"""
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def flatten_list(nested_list):
    """Flatten a nested list"""
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

def remove_duplicates(lst):
    """Remove duplicates from a list while preserving order"""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def get_random_choice(choices):
    """Get a random choice from a list"""
    return random.choice(choices) if choices else None

def get_random_sample(population, k):
    """Get k random samples from a population"""
    return random.sample(population, min(k, len(population)))

# Convenience functions that combine multiple operations
def create_secure_id(length=16):
    """Create a secure random ID"""
    return generate_random_string(length, include_digits=True, include_special=False)

def format_file_size(filename):
    """Get formatted file size"""
    try:
        import os
        size = os.path.getsize(filename)
        return format_bytes(size)
    except FileNotFoundError:
        return "File not found"

def get_current_time_info():
    """Get comprehensive current time information"""
    now = datetime.now()
    return {
        'iso': now.isoformat(),
        'readable': now.strftime('%Y-%m-%d %H:%M:%S'),
        'date': now.strftime('%Y-%m-%d'),
        'time': now.strftime('%H:%M:%S'),
        'unix': int(now.timestamp()),
        'weekday': now.strftime('%A'),
        'month': now.strftime('%B'),
        'year': now.year
    }
