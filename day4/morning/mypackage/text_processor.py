"""
Text Processor Module - Part of MyPackage
=========================================

This module provides a TextProcessor class for text manipulation.
"""

import re
import string
from collections import Counter

class TextProcessor:
    """A text processor class with various text manipulation methods"""
    
    def __init__(self):
        self.processed_texts = []
    
    def clean_text(self, text):
        """Clean text by removing extra whitespace and converting to lowercase"""
        cleaned = re.sub(r'\s+', ' ', text.strip().lower())
        self._record_processing(f"Cleaned text: '{text}' -> '{cleaned}'")
        return cleaned
    
    def remove_punctuation(self, text):
        """Remove punctuation from text"""
        cleaned = text.translate(str.maketrans('', '', string.punctuation))
        self._record_processing(f"Removed punctuation: '{text}' -> '{cleaned}'")
        return cleaned
    
    def extract_words(self, text):
        """Extract words from text"""
        words = re.findall(r'\b\w+\b', text.lower())
        self._record_processing(f"Extracted {len(words)} words from text")
        return words
    
    def count_words(self, text):
        """Count word frequency in text"""
        words = self.extract_words(text)
        word_count = Counter(words)
        self._record_processing(f"Counted words in text: {len(word_count)} unique words")
        return dict(word_count)
    
    def find_longest_word(self, text):
        """Find the longest word in text"""
        words = self.extract_words(text)
        if not words:
            return None
        longest = max(words, key=len)
        self._record_processing(f"Found longest word: '{longest}'")
        return longest
    
    def find_shortest_word(self, text):
        """Find the shortest word in text"""
        words = self.extract_words(text)
        if not words:
            return None
        shortest = min(words, key=len)
        self._record_processing(f"Found shortest word: '{shortest}'")
        return shortest
    
    def reverse_text(self, text):
        """Reverse the text"""
        reversed_text = text[::-1]
        self._record_processing(f"Reversed text: '{text}' -> '{reversed_text}'")
        return reversed_text
    
    def reverse_words(self, text):
        """Reverse the order of words in text"""
        words = text.split()
        reversed_words = ' '.join(reversed(words))
        self._record_processing(f"Reversed words: '{text}' -> '{reversed_words}'")
        return reversed_words
    
    def capitalize_text(self, text, mode='title'):
        """Capitalize text in different modes"""
        if mode == 'title':
            result = text.title()
        elif mode == 'upper':
            result = text.upper()
        elif mode == 'lower':
            result = text.lower()
        elif mode == 'sentence':
            result = text.capitalize()
        else:
            raise ValueError("Mode must be 'title', 'upper', 'lower', or 'sentence'")
        
        self._record_processing(f"Capitalized ({mode}): '{text}' -> '{result}'")
        return result
    
    def extract_numbers(self, text):
        """Extract numbers from text"""
        numbers = re.findall(r'\d+\.?\d*', text)
        self._record_processing(f"Extracted numbers: {numbers}")
        return [float(num) if '.' in num else int(num) for num in numbers]
    
    def extract_emails(self, text):
        """Extract email addresses from text"""
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(pattern, text)
        self._record_processing(f"Extracted emails: {emails}")
        return emails
    
    def extract_urls(self, text):
        """Extract URLs from text"""
        pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        urls = re.findall(pattern, text)
        self._record_processing(f"Extracted URLs: {urls}")
        return urls
    
    def replace_text(self, text, old, new):
        """Replace text with new text"""
        result = text.replace(old, new)
        count = text.count(old)
        self._record_processing(f"Replaced '{old}' with '{new}' ({count} occurrences)")
        return result
    
    def truncate_text(self, text, max_length, suffix="..."):
        """Truncate text to specified length"""
        if len(text) <= max_length:
            return text
        result = text[:max_length - len(suffix)] + suffix
        self._record_processing(f"Truncated text to {max_length} characters")
        return result
    
    def get_text_stats(self, text):
        """Get comprehensive statistics about text"""
        words = self.extract_words(text)
        word_count = len(words)
        char_count = len(text)
        char_count_no_spaces = len(text.replace(' ', ''))
        sentence_count = len(re.findall(r'[.!?]+', text))
        paragraph_count = len(text.split('\n\n'))
        
        stats = {
            'characters': char_count,
            'characters_no_spaces': char_count_no_spaces,
            'words': word_count,
            'sentences': sentence_count,
            'paragraphs': paragraph_count,
            'average_word_length': sum(len(word) for word in words) / word_count if words else 0
        }
        
        self._record_processing(f"Generated text statistics: {word_count} words, {char_count} characters")
        return stats
    
    def get_processing_history(self):
        """Get history of text processing operations"""
        return self.processed_texts.copy()
    
    def clear_history(self):
        """Clear processing history"""
        self.processed_texts = []
    
    def _record_processing(self, operation):
        """Record a processing operation"""
        self.processed_texts.append(operation)
    
    def __str__(self):
        """String representation of text processor"""
        return f"TextProcessor (Processed: {len(self.processed_texts)} operations)"
