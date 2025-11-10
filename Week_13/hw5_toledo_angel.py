from abc import ABC, abstractmethod
import math

# =====================================
# Problem 1
# =====================================

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return f"This is a {self.__class__.__name__}"

    @staticmethod
    def validate_positive(value, name):
        if value > 0:
            return True
        print(f"{name} must be positive!")
        return False


class Circle(Shape):
    def __init__(self, radius):
        if not self.validate_positive(radius, "radius"):
            raise ValueError("Invalid radius")
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        if not (self.validate_positive(width, "width") and self.validate_positive(height, "height")):
            raise ValueError("Invalid dimensions")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        if not all(self.validate_positive(x, f"side{i+1}") for i, x in enumerate([side1, side2, side3])):
            raise ValueError("Invalid sides")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


class ShapeCollection:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def total_area(self):
        return sum(shape.area() for shape in self.shapes)

    def total_perimeter(self):
        return sum(shape.perimeter() for shape in self.shapes)


# =====================================
# Problem 2
# =====================================

class Pizza:
    price_list = {'small': 10, 'medium': 15, 'large': 20}
    topping_price = 2

    def __init__(self, size, toppings):
        if not self.validate_size(size):
            raise ValueError("Invalid pizza size")
        self.size = size
        self.toppings = toppings

    def calculate_price(self):
        return self.price_list[self.size] + self.topping_price * len(self.toppings)

    def __str__(self):
        return f"{self.size} pizza with {len(self.toppings)} toppings"

    @classmethod
    def create_margherita(cls, size):
        return cls(size, ['cheese', 'tomato', 'basil'])

    @classmethod
    def create_pepperoni(cls, size):
        return cls(size, ['cheese', 'pepperoni'])

    @classmethod
    def create_veggie(cls, size):
        return cls(size, ['cheese', 'mushrooms', 'peppers', 'onions'])

    @staticmethod
    def validate_size(size):
        return size in ['small', 'medium', 'large']


class PizzaOrder:
    total_orders = 0

    def __init__(self):
        PizzaOrder.total_orders += 1
        self.order_id = f"ORDER_{PizzaOrder.total_orders:03d}"
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def get_total(self):
        return sum(p.calculate_price() for p in self.pizzas)

    @classmethod
    def get_total_orders(cls):
        return cls.total_orders

    def __str__(self):
        return f"Order {self.order_id} - Total: ${self.get_total()}"


class OrderManager:
    @staticmethod
    def create_order_from_string(order_string):
        order = PizzaOrder()
        items = [item.strip() for item in order_string.split(",")]
        for item in items:
            size, kind = item.split()
            if kind.lower() == "margherita":
                pizza = Pizza.create_margherita(size)
            elif kind.lower() == "pepperoni":
                pizza = Pizza.create_pepperoni(size)
            elif kind.lower() == "veggie":
                pizza = Pizza.create_veggie(size)
            else:
                continue
            order.add_pizza(pizza)
        return order

    @staticmethod
    def format_receipt(order):
        lines = [
            "=== RECEIPT ===",
            f"Order: {order.order_id}",
            "Items:"
        ]
        for pizza in order.pizzas:
            lines.append(f"  {pizza} - ${pizza.calculate_price()}")
        lines.append(f"Total: ${order.get_total()}")
        lines.append("==============")
        return "\n".join(lines)


# =====================================
# Problem 3
# =====================================

class Duration:
    def __init__(self, hours=0, minutes=0, seconds=0):
        total = hours * 3600 + minutes * 60 + seconds
        if total < 0:
            total = 0
        self.hours = total // 3600
        remainder = total % 3600
        self.minutes = remainder // 60
        self.seconds = remainder % 60

    @property
    def total_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __str__(self):
        parts = []
        if self.hours:
            parts.append(f"{self.hours}h")
        if self.minutes:
            parts.append(f"{self.minutes}m")
        if self.seconds:
            parts.append(f"{self.seconds}s")
        return " ".join(parts) if parts else "0s"

    def __repr__(self):
        return f"Duration({self.hours}, {self.minutes}, {self.seconds})"

    def __add__(self, other):
        return Duration(seconds=self.total_seconds + other.total_seconds)

    def __sub__(self, other):
        diff = self.total_seconds - other.total_seconds
        return Duration(seconds=max(0, diff))

    def __mul__(self, multiplier):
        return Duration(seconds=self.total_seconds * multiplier)

    def __eq__(self, other):
        return self.total_seconds == other.total_seconds

    def __lt__(self, other):
        return self.total_seconds < other.total_seconds

    def __le__(self, other):
        return self.total_seconds <= other.total_seconds


# =====================================
# Test Script
# =====================================
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4, 5)

    print("Individual Shapes:")
    for s in [circle, rectangle, triangle]:
        print(f"  {s.describe()}")
        print(f"    Area: {s.area():.2f}")
        print(f"    Perimeter: {s.perimeter():.2f}")

    collection = ShapeCollection()
    for s in [circle, rectangle, triangle]:
        collection.add_shape(s)
    print(f"\nCollection Totals:")
    print(f"  Total Area: {collection.total_area():.2f}")
    print(f"  Total Perimeter: {collection.total_perimeter():.2f}")

    print("\nTesting validation:")
    try:
        bad_circle = Circle(-5)
    except:
        print("  Correctly rejected negative radius")
