"""
File Handler Module - Part of MyPackage
=======================================

This module provides a FileHandler class for file I/O operations.
"""

import os
import json
import csv
from datetime import datetime

class FileHandler:
    """A file handler class for various file operations"""
    
    def __init__(self):
        self.operations_log = []
    
    def read_text_file(self, filename):
        """Read contents of a text file"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                self._log_operation(f"Read text file: {filename}")
                return content
        except FileNotFoundError:
            self._log_operation(f"File not found: {filename}")
            raise
        except Exception as e:
            self._log_operation(f"Error reading file {filename}: {str(e)}")
            raise
    
    def write_text_file(self, filename, content):
        """Write content to a text file"""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content)
                self._log_operation(f"Wrote text file: {filename}")
        except Exception as e:
            self._log_operation(f"Error writing file {filename}: {str(e)}")
            raise
    
    def append_text_file(self, filename, content):
        """Append content to a text file"""
        try:
            with open(filename, 'a', encoding='utf-8') as file:
                file.write(content)
                self._log_operation(f"Appended to text file: {filename}")
        except Exception as e:
            self._log_operation(f"Error appending to file {filename}: {str(e)}")
            raise
    
    def read_json_file(self, filename):
        """Read JSON data from a file"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self._log_operation(f"Read JSON file: {filename}")
                return data
        except FileNotFoundError:
            self._log_operation(f"JSON file not found: {filename}")
            raise
        except json.JSONDecodeError as e:
            self._log_operation(f"Invalid JSON in file {filename}: {str(e)}")
            raise
        except Exception as e:
            self._log_operation(f"Error reading JSON file {filename}: {str(e)}")
            raise
    
    def write_json_file(self, filename, data):
        """Write data to a JSON file"""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
                self._log_operation(f"Wrote JSON file: {filename}")
        except Exception as e:
            self._log_operation(f"Error writing JSON file {filename}: {str(e)}")
            raise
    
    def read_csv_file(self, filename):
        """Read CSV data from a file"""
        try:
            with open(filename, 'r', encoding='utf-8', newline='') as file:
                reader = csv.DictReader(file)
                data = list(reader)
                self._log_operation(f"Read CSV file: {filename} ({len(data)} rows)")
                return data
        except FileNotFoundError:
            self._log_operation(f"CSV file not found: {filename}")
            raise
        except Exception as e:
            self._log_operation(f"Error reading CSV file {filename}: {str(e)}")
            raise
    
    def write_csv_file(self, filename, data, fieldnames=None):
        """Write data to a CSV file"""
        try:
            if not data:
                raise ValueError("No data to write")
            
            if fieldnames is None:
                fieldnames = data[0].keys()
            
            with open(filename, 'w', encoding='utf-8', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
                self._log_operation(f"Wrote CSV file: {filename} ({len(data)} rows)")
        except Exception as e:
            self._log_operation(f"Error writing CSV file {filename}: {str(e)}")
            raise
    
    def file_exists(self, filename):
        """Check if a file exists"""
        exists = os.path.exists(filename)
        self._log_operation(f"File exists check: {filename} -> {exists}")
        return exists
    
    def get_file_size(self, filename):
        """Get file size in bytes"""
        try:
            size = os.path.getsize(filename)
            self._log_operation(f"File size: {filename} -> {size} bytes")
            return size
        except FileNotFoundError:
            self._log_operation(f"File not found for size check: {filename}")
            raise
    
    def get_file_info(self, filename):
        """Get comprehensive file information"""
        try:
            stat_info = os.stat(filename)
            info = {
                'filename': filename,
                'size': stat_info.st_size,
                'modified': datetime.fromtimestamp(stat_info.st_mtime).isoformat(),
                'created': datetime.fromtimestamp(stat_info.st_ctime).isoformat(),
                'is_file': os.path.isfile(filename),
                'is_directory': os.path.isdir(filename)
            }
            self._log_operation(f"Retrieved file info: {filename}")
            return info
        except FileNotFoundError:
            self._log_operation(f"File not found for info: {filename}")
            raise
    
    def delete_file(self, filename):
        """Delete a file"""
        try:
            os.remove(filename)
            self._log_operation(f"Deleted file: {filename}")
        except FileNotFoundError:
            self._log_operation(f"File not found for deletion: {filename}")
            raise
        except Exception as e:
            self._log_operation(f"Error deleting file {filename}: {str(e)}")
            raise
    
    def create_directory(self, directory_path):
        """Create a directory"""
        try:
            os.makedirs(directory_path, exist_ok=True)
            self._log_operation(f"Created directory: {directory_path}")
        except Exception as e:
            self._log_operation(f"Error creating directory {directory_path}: {str(e)}")
            raise
    
    def list_directory(self, directory_path):
        """List contents of a directory"""
        try:
            contents = os.listdir(directory_path)
            self._log_operation(f"Listed directory: {directory_path} ({len(contents)} items)")
            return contents
        except FileNotFoundError:
            self._log_operation(f"Directory not found: {directory_path}")
            raise
        except Exception as e:
            self._log_operation(f"Error listing directory {directory_path}: {str(e)}")
            raise
    
    def copy_file(self, source, destination):
        """Copy a file from source to destination"""
        try:
            import shutil
            shutil.copy2(source, destination)
            self._log_operation(f"Copied file: {source} -> {destination}")
        except Exception as e:
            self._log_operation(f"Error copying file {source} to {destination}: {str(e)}")
            raise
    
    def move_file(self, source, destination):
        """Move a file from source to destination"""
        try:
            import shutil
            shutil.move(source, destination)
            self._log_operation(f"Moved file: {source} -> {destination}")
        except Exception as e:
            self._log_operation(f"Error moving file {source} to {destination}: {str(e)}")
            raise
    
    def get_operations_log(self):
        """Get log of all file operations"""
        return self.operations_log.copy()
    
    def clear_operations_log(self):
        """Clear the operations log"""
        self.operations_log = []
    
    def _log_operation(self, operation):
        """Log a file operation with timestamp"""
        timestamp = datetime.now().isoformat()
        self.operations_log.append(f"[{timestamp}] {operation}")
    
    def __str__(self):
        """String representation of file handler"""
        return f"FileHandler (Operations: {len(self.operations_log)})"
