"""
Polymorphism in Python - Practical Examples
===========================================

This file demonstrates polymorphism concepts with practical examples
that are commonly asked in job interviews.
"""

from abc import ABC, abstractmethod

# Example 1: Duck Typing - No inheritance needed
class Dog:
    def make_sound(self):
        return "Woof!"
    
    def move(self):
        return "Running on four legs"

class Cat:
    def make_sound(self):
        return "Meow!"
    
    def move(self):
        return "Sneaking silently"

class Bird:
    def make_sound(self):
        return "Tweet!"
    
    def move(self):
        return "Flying in the sky"

# Polymorphic function - works with any object that has make_sound() method
def animal_sounds(animals):
    """Demonstrate polymorphism with duck typing"""
    for animal in animals:
        print(f"{animal.__class__.__name__}: {animal.make_sound()}")
        print(f"Movement: {animal.move()}")
        print("-" * 30)

# Example 2: Vehicle hierarchy with polymorphism
class Vehicle(ABC):
    """Abstract base class for all vehicles"""
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    @abstractmethod
    def make_sound(self):
        """Abstract method that must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def start_engine(self):
        """Abstract method for starting engine"""
        pass
    
    def get_info(self):
        """Concrete method available to all vehicles"""
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
    
    def make_sound(self):
        return "Vroom vroom!"
    
    def start_engine(self):
        return "Engine started with key"
    
    def open_doors(self):
        return f"Opening {self.doors} doors"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, engine_size):
        super().__init__(brand, model)
        self.engine_size = engine_size
    
    def make_sound(self):
        return "Brrrr brrrr!"
    
    def start_engine(self):
        return "Engine started with kick/button"
    
    def wheelie(self):
        return "Performing a wheelie!"

class Truck(Vehicle):
    def __init__(self, brand, model, cargo_capacity):
        super().__init__(brand, model)
        self.cargo_capacity = cargo_capacity
    
    def make_sound(self):
        return "Rumble rumble!"
    
    def start_engine(self):
        return "Heavy engine started"
    
    def load_cargo(self):
        return f"Loading up to {self.cargo_capacity} tons"

# Example 3: Polymorphic functions
def vehicle_demo(vehicles):
    """Demonstrate polymorphism with Vehicle objects"""
    print("=== Vehicle Polymorphism Demo ===")
    for vehicle in vehicles:
        print(f"Vehicle: {vehicle.get_info()}")
        print(f"Sound: {vehicle.make_sound()}")
        print(f"Starting: {vehicle.start_engine()}")
        print("-" * 40)

def start_all_vehicles(vehicles):
    """Start all vehicles regardless of their specific type"""
    for vehicle in vehicles:
        print(f"Starting {vehicle.get_info()}: {vehicle.start_engine()}")

# Example 4: Method Overriding
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"
    
    def info(self):
        return f"This is {self.name}"

class Dog(Animal):
    def speak(self):  # Method overriding
        return f"{self.name} barks: Woof!"
    
    def fetch(self):
        return f"{self.name} fetches the ball"

class Cat(Animal):
    def speak(self):  # Method overriding
        return f"{self.name} meows: Meow!"
    
    def climb(self):
        return f"{self.name} climbs the tree"

# Example 5: Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Overload + operator"""
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Overload - operator"""
        return Point(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        """String representation"""
        return f"Point({self.x}, {self.y})"
    
    def __eq__(self, other):
        """Overload == operator"""
        return self.x == other.x and self.y == other.y

# Example 6: Interface-like behavior with ABC
class Shape(ABC):
    """Abstract base class for geometric shapes"""
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius
    
    def draw(self):
        return f"Drawing a circle with radius {self.radius}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def draw(self):
        return f"Drawing a rectangle {self.width}x{self.height}"

def demonstrate_polymorphism():
    """Main demonstration function"""
    print("=" * 50)
    print("POLYMORPHISM DEMONSTRATION")
    print("=" * 50)
    
    # Duck typing example
    print("\n1. DUCK TYPING EXAMPLE:")
    animals = [Dog(), Cat(), Bird()]
    animal_sounds(animals)
    
    # Vehicle hierarchy example
    print("\n2. VEHICLE HIERARCHY EXAMPLE:")
    vehicles = [
        Car("Toyota", "Camry", 4),
        Motorcycle("Harley", "Davidson", 1200),
        Truck("Ford", "F-150", 5)
    ]
    vehicle_demo(vehicles)
    
    # Method overriding example
    print("\n3. METHOD OVERRIDING EXAMPLE:")
    pets = [Dog("Buddy"), Cat("Whiskers")]
    for pet in pets:
        print(pet.speak())
        print(pet.info())
    
    # Operator overloading example
    print("\n4. OPERATOR OVERLOADING EXAMPLE:")
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    p3 = p1 + p2
    print(f"{p1} + {p2} = {p3}")
    
    # Shape polymorphism example
    print("\n5. SHAPE POLYMORPHISM EXAMPLE:")
    shapes = [Circle(5), Rectangle(4, 6)]
    for shape in shapes:
        print(f"{shape.draw()}")
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")
        print("-" * 30)

if __name__ == "__main__":
    demonstrate_polymorphism()
