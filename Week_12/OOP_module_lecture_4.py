
# -------------------------
# UNIT 1: Polymorphism
# -------------------------

# Beginner: Shapes drawing
class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        raise NotImplementedError("draw() must be implemented by subclasses")


class Circle(Shape):
    def draw(self):
        return f"Drawing a {self.color} circle"


class Square(Shape):
    def draw(self):
        return f"Drawing a {self.color} square"

# Intermediate: Payment processing
class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        raise NotImplementedError


class CreditCard(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = str(card_number)

    def process(self):
        last4 = self.card_number[-4:]
        return f"Processing ${self.amount:.2f} via credit card ending in {last4}"


class PayPal(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def process(self):
        return f"Processing ${self.amount:.2f} via PayPal account {self.email}"
    
# -------------------------
# UNIT 2: Abstract Base Classes
# -------------------------

from abc import ABC, abstractmethod

# Beginner: 
class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car engine starting..."

#Intermediate:
# TODO: Abstract database interface

class DatabaseConnection(ABC):
    def __init__(self, host):
        self.host = host
        self.connected = False
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass
    @abstractmethod
    def execute_query(self, query):
        pass
class MySQLConnection(DatabaseConnection):
# Implement all abstract methods
    def connect(self):
        self.connected = True
        return f"Connected to MySQL database at {self.host}"

class PostgresConnection(DatabaseConnection):
# Implement all abstract methods
    def connect(self):
        self.connected = True
        return f"Connected to PostgreSQL database at {self.host}"

# -------------------------
# UNIT 3: Duck Typing
# -------------------------

# Beginner:
# TODO: Create objects with compatible methods
class Calculator:
    def compute(self, x, y):
        return x + y
class ScientificCalculator: # No inheritance!
    def compute(self, x, y):
        # Return x * y instead
        return x * y
    def process_numbers(processor, a, b):
        # Works with anything that has compute()
        result = processor.compute(a, b)
        print(f"Result: {result}")


# -------------------------
# UNIT 4: Interface Design Patterns
# -------------------------

# Beginner: 
# TODO: Different notification methods
class NotificationStrategy:
    def notify(self, message):
        pass

class EmailNotification(NotificationStrategy):
    def notify(self, message):
        # Print "Email sent: [message]"
        print(f"Email sent: {message}")
        
class SMSNotification(NotificationStrategy):
    # Implement SMS notification
    def notify(self, message):
        print(f"SMS sent: {message}")
class App:
    def __init__(self, notifier):
        self.notifier = notifier
    def alert_user(self, message):
        # Use the notifier
        self.notifier.notify(message)