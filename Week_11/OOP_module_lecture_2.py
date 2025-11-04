# TODO: Create Person class with private _age
class Person:
    def __init__(self, age):
        self._age = age
    
    def get_age(self):
        return self._age

person = Person(25)
print(person.get_age()) 

# TODO: Add set_age() with validation
class Person:
    def __init__(self, age):
        self._age = age
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age
#test
person = Person(25)
Person.set_age(30)
Person.set_age(-5) 

# TODO: Store SSN privately, show only last 4 digits
class Person:
    def __init__(self, age, ssn):
        self._age = age
        self._ssn = ssn
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age
    
    def get_ssn(self):
        return "XXX-XX-" + self._ssn[-4:]
    



# TODO: Make area a property (calculated)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def area(self):
        return self.width * self.height

# TODO: Extract domain from email
class Person:
    def __init__(self, age, ssn, email):
        self._age = age
        self._ssn = ssn
        self._email = email
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age
    
    def get_ssn(self):
        return "XXX-XX-" + self._ssn[-4:]
    
    def get_email_domain(self):
        return self._email.split('@')[-1]

# TODO: Calculate age from birthdate
from datetime import datetime
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    
    @property
    def age(self):
        current_year = datetime.now().year
        return current_year - self.birth_year
    
    @property
    def can_vote(self):
        return self.age >= 18
    


# TODO: Create Score class (0-100 range)
class Score:
    def __init__(self, value):
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        if not (0 <= val <= 100):
            raise ValueError("Score must be between 0 and 100")
        self._value = val

# TODO: Username with format checking
class Username:
    def __init__(self, name):
        self._name = ""
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value.isalnum() or len(value) < 3:
            raise ValueError("Username must be at least 3 characters long and alphanumeric")
        self._name = value



# TODO: Create Inventory with protected stock
class Inventory:
    def __init__(self, product_name):
        self.product_name = product_name
        self._stock = 0
    @property
    def stock(self):
        # Return current stock
        return self._stock
    def add_stock(self, quantity):
        # Add to stock if quantity > 0
        if quantity > 0:
            self._stock += quantity
    def remove_stock(self, quantity):
        # Remove if enough stock
        if 0 < quantity <= self._stock:
            self._stock -= quantity

# TODO: Add low stock warnings
class Inventory:
    def __init__(self, product_name, reorder_point=10):
        self.product_name = product_name
        self._stock = 0
        self.reorder_point = reorder_point
    @property
    def needs_reorder(self):
        # Return True if stock below reorder_point
        return self._stock < self.reorder_point
    
# TODO: Track all inventory changes
from datetime import datetime
class Inventory:
    def __init__(self, product_name):
        self.product_name = product_name
        self._stock = 0
        self._history = []
    @property
    def stock(self):
        return self._stock
    @property
    def history(self):
        # Return copy of history
        return self._history.copy()

    def add_stock(self, quantity, reason=""):
        # Add stock and record in history
        # Include timestamp, action, quantity, reason
        if quantity > 0:
            self._stock += quantity
            self._history.append({
                "timestamp": datetime.now(),
                "action": "add",
                "quantity": quantity,
                "reason": reason
            })

    def get_history_summary(self):
        # Return formatted history
        summary = []
        for record in self._history:
            summary.append(f"{record['timestamp']}: {record['action']} {record['quantity']} ({record['reason']})")

