"""
Polymorphism Practice Exercises
===============================

Complete these exercises to master polymorphism concepts.
Each exercise builds on the previous ones.
"""

from abc import ABC, abstractmethod

# EXERCISE 1: Employee Management System
# Create a polymorphic employee management system

class Employee(ABC):
    """Abstract base class for all employees"""
    
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    
    @abstractmethod
    def calculate_pay(self):
        """Calculate employee pay - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def get_role(self):
        """Get employee role - must be implemented by subclasses"""
        pass
    
    def get_info(self):
        """Get basic employee information"""
        return f"Employee: {self.name} (ID: {self.employee_id})"

# TODO: Create these employee classes
class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, annual_salary):
        # TODO: Initialize parent class and set annual_salary
        pass
    
    def calculate_pay(self):
        # TODO: Return monthly salary (annual_salary / 12)
        pass
    
    def get_role(self):
        # TODO: Return "Full-time Employee"
        pass

class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        # TODO: Initialize parent class and set hourly_rate and hours_worked
        pass
    
    def calculate_pay(self):
        # TODO: Return hourly_rate * hours_worked
        pass
    
    def get_role(self):
        # TODO: Return "Part-time Employee"
        pass

class Contractor(Employee):
    def __init__(self, name, employee_id, contract_amount):
        # TODO: Initialize parent class and set contract_amount
        pass
    
    def calculate_pay(self):
        # TODO: Return contract_amount
        pass
    
    def get_role(self):
        # TODO: Return "Contractor"
        pass

# EXERCISE 2: Payment Processing System
# Create a polymorphic payment system

class PaymentProcessor(ABC):
    """Abstract base class for payment processors"""
    
    @abstractmethod
    def process_payment(self, amount):
        """Process payment - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def get_fee(self, amount):
        """Get processing fee - must be implemented by subclasses"""
        pass

# TODO: Create these payment processor classes
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # TODO: Return processing message for credit card
        pass
    
    def get_fee(self, amount):
        # TODO: Return 2.9% of amount as fee
        pass

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # TODO: Return processing message for PayPal
        pass
    
    def get_fee(self, amount):
        # TODO: Return 3.5% of amount as fee
        pass

class BankTransferProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # TODO: Return processing message for bank transfer
        pass
    
    def get_fee(self, amount):
        # TODO: Return flat $5 fee
        pass

# EXERCISE 3: Media Player System
# Create a polymorphic media player

class MediaFile(ABC):
    """Abstract base class for media files"""
    
    def __init__(self, filename):
        self.filename = filename
    
    @abstractmethod
    def play(self):
        """Play the media file"""
        pass
    
    @abstractmethod
    def get_duration(self):
        """Get media duration"""
        pass
    
    @abstractmethod
    def get_type(self):
        """Get media type"""
        pass

# TODO: Create these media file classes
class AudioFile(MediaFile):
    def __init__(self, filename, duration_seconds):
        # TODO: Initialize parent class and set duration
        pass
    
    def play(self):
        # TODO: Return play message for audio
        pass
    
    def get_duration(self):
        # TODO: Return duration in seconds
        pass
    
    def get_type(self):
        # TODO: Return "Audio"
        pass

class VideoFile(MediaFile):
    def __init__(self, filename, duration_seconds, resolution):
        # TODO: Initialize parent class and set duration and resolution
        pass
    
    def play(self):
        # TODO: Return play message for video with resolution
        pass
    
    def get_duration(self):
        # TODO: Return duration in seconds
        pass
    
    def get_type(self):
        # TODO: Return "Video"
        pass

class ImageFile(MediaFile):
    def __init__(self, filename, width, height):
        # TODO: Initialize parent class and set dimensions
        pass
    
    def play(self):
        # TODO: Return display message for image
        pass
    
    def get_duration(self):
        # TODO: Return 0 (images don't have duration)
        pass
    
    def get_type(self):
        # TODO: Return "Image"
        pass

# EXERCISE 4: Notification System
# Create a polymorphic notification system

class NotificationSender(ABC):
    """Abstract base class for notification senders"""
    
    @abstractmethod
    def send(self, message, recipient):
        """Send notification"""
        pass
    
    @abstractmethod
    def get_delivery_status(self):
        """Get delivery status"""
        pass

# TODO: Create these notification sender classes
class EmailSender(NotificationSender):
    def send(self, message, recipient):
        # TODO: Return email sending message
        pass
    
    def get_delivery_status(self):
        # TODO: Return email delivery status
        pass

class SMSSender(NotificationSender):
    def send(self, message, recipient):
        # TODO: Return SMS sending message
        pass
    
    def get_delivery_status(self):
        # TODO: Return SMS delivery status
        pass

class PushNotificationSender(NotificationSender):
    def send(self, message, recipient):
        # TODO: Return push notification message
        pass
    
    def get_delivery_status(self):
        # TODO: Return push notification status
        pass

# UTILITY FUNCTIONS TO COMPLETE

def process_payroll(employees):
    """Process payroll for all employees using polymorphism"""
    print("=== PAYROLL PROCESSING ===")
    total_cost = 0
    
    # TODO: Iterate through employees and calculate total payroll cost
    # Print each employee's info, role, and pay
    # Return total cost
    
    return total_cost

def process_payments(processors, amount):
    """Process payments using different processors"""
    print(f"=== PROCESSING PAYMENT OF ${amount} ===")
    
    # TODO: Use each processor to process the payment
    # Print processing message and fee for each processor
    
    pass

def play_media_playlist(media_files):
    """Play a playlist of different media files"""
    print("=== PLAYING MEDIA PLAYLIST ===")
    
    # TODO: Play each media file and show its information
    # Print type, filename, duration, and play message
    
    pass

def send_notifications(senders, message, recipient):
    """Send notifications using different senders"""
    print(f"=== SENDING NOTIFICATIONS ===")
    
    # TODO: Send message using each sender
    # Print send message and delivery status
    
    pass

# TEST FUNCTIONS (DO NOT MODIFY)
def test_exercises():
    """Test all exercises"""
    print("=" * 60)
    print("TESTING POLYMORPHISM EXERCISES")
    print("=" * 60)
    
    # Test Employee Management
    try:
        employees = [
            FullTimeEmployee("Alice", 1001, 60000),
            PartTimeEmployee("Bob", 1002, 15, 80),
            Contractor("Charlie", 1003, 5000)
        ]
        total = process_payroll(employees)
        print(f"Total payroll cost: ${total}")
        print("\n" + "="*40 + "\n")
    except Exception as e:
        print(f"Employee exercise needs completion: {e}")
    
    # Test Payment Processing
    try:
        processors = [
            CreditCardProcessor(),
            PayPalProcessor(),
            BankTransferProcessor()
        ]
        process_payments(processors, 100)
        print("\n" + "="*40 + "\n")
    except Exception as e:
        print(f"Payment exercise needs completion: {e}")
    
    # Test Media Player
    try:
        media_files = [
            AudioFile("song.mp3", 240),
            VideoFile("movie.mp4", 7200, "1080p"),
            ImageFile("photo.jpg", 1920, 1080)
        ]
        play_media_playlist(media_files)
        print("\n" + "="*40 + "\n")
    except Exception as e:
        print(f"Media exercise needs completion: {e}")
    
    # Test Notification System
    try:
        senders = [
            EmailSender(),
            SMSSender(),
            PushNotificationSender()
        ]
        send_notifications(senders, "Hello, World!", "user@example.com")
    except Exception as e:
        print(f"Notification exercise needs completion: {e}")

if __name__ == "__main__":
    test_exercises()
