"""
Polymorphism Exercise Solutions
==============================

Complete solutions to the polymorphism exercises.
Study these solutions to understand the concepts.
"""

from abc import ABC, abstractmethod

# SOLUTION 1: Employee Management System
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

class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, annual_salary):
        super().__init__(name, employee_id)
        self.annual_salary = annual_salary
    
    def calculate_pay(self):
        return self.annual_salary / 12
    
    def get_role(self):
        return "Full-time Employee"

class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked
    
    def get_role(self):
        return "Part-time Employee"

class Contractor(Employee):
    def __init__(self, name, employee_id, contract_amount):
        super().__init__(name, employee_id)
        self.contract_amount = contract_amount
    
    def calculate_pay(self):
        return self.contract_amount
    
    def get_role(self):
        return "Contractor"

# SOLUTION 2: Payment Processing System
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

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"
    
    def get_fee(self, amount):
        return amount * 0.029  # 2.9% fee

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"
    
    def get_fee(self, amount):
        return amount * 0.035  # 3.5% fee

class BankTransferProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Bank Transfer"
    
    def get_fee(self, amount):
        return 5.0  # Flat $5 fee

# SOLUTION 3: Media Player System
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

class AudioFile(MediaFile):
    def __init__(self, filename, duration_seconds):
        super().__init__(filename)
        self.duration_seconds = duration_seconds
    
    def play(self):
        return f"♪ Playing audio: {self.filename}"
    
    def get_duration(self):
        return self.duration_seconds
    
    def get_type(self):
        return "Audio"

class VideoFile(MediaFile):
    def __init__(self, filename, duration_seconds, resolution):
        super().__init__(filename)
        self.duration_seconds = duration_seconds
        self.resolution = resolution
    
    def play(self):
        return f"▶ Playing video: {self.filename} ({self.resolution})"
    
    def get_duration(self):
        return self.duration_seconds
    
    def get_type(self):
        return "Video"

class ImageFile(MediaFile):
    def __init__(self, filename, width, height):
        super().__init__(filename)
        self.width = width
        self.height = height
    
    def play(self):
        return f"🖼 Displaying image: {self.filename} ({self.width}x{self.height})"
    
    def get_duration(self):
        return 0  # Images don't have duration
    
    def get_type(self):
        return "Image"

# SOLUTION 4: Notification System
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

class EmailSender(NotificationSender):
    def send(self, message, recipient):
        return f"📧 Email sent to {recipient}: {message}"
    
    def get_delivery_status(self):
        return "Email delivered successfully"

class SMSSender(NotificationSender):
    def send(self, message, recipient):
        return f"📱 SMS sent to {recipient}: {message}"
    
    def get_delivery_status(self):
        return "SMS delivered successfully"

class PushNotificationSender(NotificationSender):
    def send(self, message, recipient):
        return f"🔔 Push notification sent to {recipient}: {message}"
    
    def get_delivery_status(self):
        return "Push notification delivered successfully"

# SOLUTION: UTILITY FUNCTIONS
def process_payroll(employees):
    """Process payroll for all employees using polymorphism"""
    print("=== PAYROLL PROCESSING ===")
    total_cost = 0
    
    for employee in employees:
        pay = employee.calculate_pay()
        total_cost += pay
        print(f"{employee.get_info()}")
        print(f"Role: {employee.get_role()}")
        print(f"Pay: ${pay:.2f}")
        print("-" * 30)
    
    return total_cost

def process_payments(processors, amount):
    """Process payments using different processors"""
    print(f"=== PROCESSING PAYMENT OF ${amount} ===")
    
    for processor in processors:
        processing_msg = processor.process_payment(amount)
        fee = processor.get_fee(amount)
        print(f"{processing_msg}")
        print(f"Processing fee: ${fee:.2f}")
        print(f"Total cost: ${amount + fee:.2f}")
        print("-" * 30)

def play_media_playlist(media_files):
    """Play a playlist of different media files"""
    print("=== PLAYING MEDIA PLAYLIST ===")
    
    for media in media_files:
        print(f"Type: {media.get_type()}")
        print(f"File: {media.filename}")
        print(f"Duration: {media.get_duration()} seconds")
        print(media.play())
        print("-" * 30)

def send_notifications(senders, message, recipient):
    """Send notifications using different senders"""
    print(f"=== SENDING NOTIFICATIONS ===")
    
    for sender in senders:
        send_msg = sender.send(message, recipient)
        status = sender.get_delivery_status()
        print(send_msg)
        print(f"Status: {status}")
        print("-" * 30)

# DEMONSTRATION FUNCTION
def demonstrate_solutions():
    """Demonstrate all solutions"""
    print("=" * 60)
    print("POLYMORPHISM EXERCISE SOLUTIONS")
    print("=" * 60)
    
    # Test Employee Management
    print("\n1. EMPLOYEE MANAGEMENT SYSTEM")
    employees = [
        FullTimeEmployee("Alice Johnson", 1001, 60000),
        PartTimeEmployee("Bob Smith", 1002, 15, 80),
        Contractor("Charlie Brown", 1003, 5000)
    ]
    total = process_payroll(employees)
    print(f"💰 Total payroll cost: ${total:.2f}")
    print("\n" + "="*50 + "\n")
    
    # Test Payment Processing
    print("2. PAYMENT PROCESSING SYSTEM")
    processors = [
        CreditCardProcessor(),
        PayPalProcessor(),
        BankTransferProcessor()
    ]
    process_payments(processors, 100)
    print("\n" + "="*50 + "\n")
    
    # Test Media Player
    print("3. MEDIA PLAYER SYSTEM")
    media_files = [
        AudioFile("favorite_song.mp3", 240),
        VideoFile("movie_trailer.mp4", 7200, "1080p"),
        ImageFile("vacation_photo.jpg", 1920, 1080)
    ]
    play_media_playlist(media_files)
    print("\n" + "="*50 + "\n")
    
    # Test Notification System
    print("4. NOTIFICATION SYSTEM")
    senders = [
        EmailSender(),
        SMSSender(),
        PushNotificationSender()
    ]
    send_notifications(senders, "Welcome to our service!", "user@example.com")

if __name__ == "__main__":
    demonstrate_solutions()
