# TODO: Create Vehicle base class and Car derived class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
def start(self):
    print(f"{self.brand} {self.model} is starting")
# TODO: Create Car class that inherits from Vehicle
class Car(Vehicle):
    def honk(self):
        # Print "Beep beep!"
        print("Beep beep!")
# Test:
my_car = Car("Toyota", "Camry")
my_car.start()  
my_car.honk()   

# TODO: Create multiple vehicle types
class Vehicle:
    def __init__(self, brand, model, wheels):
        self.brand = brand
        self.model = model
        self.wheels = wheels
    def start(self):
        print(f"{self.brand} {self.model} is starting")
class Car(Vehicle):
    def __init__(self, brand, model):
        # Cars have 4 wheels
        super().__init__(brand, model, 4)

class Motorcycle(Vehicle):
    def __init__(self, brand, model):
        # Motorcycles have 2 wheels
        super().__init__(brand, model, 2)
    def wheelie(self):
        # Only motorcycles can do this
        print(f"{self.brand} {self.model} is doing a wheelie")
        print(f"{self.brand} {self.model} is starting")


class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        return 0 # Base shape has no area
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    def area(self):
        # Override to return width * height
        area = self.width * self.height
        return area
    
# TODO: Different grading for different students
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def calculate_grade(self):
        # Regular grading
        if self.score >= 90: return "A"
        elif self.score >= 80: return "B"
        elif self.score >= 70: return "C"
        else: return "F"
class HonorsStudent(Student):
    def calculate_grade(self):
        # Harder grading for honors
        # A: 95+, B: 85+, C: 75+
        if self.score >= 95: return "A"
        elif self.score >= 85: return "B"
        elif self.score >= 75: return "C"
        else: return "F"



# TODO: Extend Car class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    def accelerate(self):
        self.speed += 10
        print(f"Speed: {self.speed} mph")
class SportsCar(Car):
    def __init__(self, brand, model, year, turbo):
        # Call parent init
        # Add turbo attribute
        super().__init__(brand, model, year)
        self.turbo = turbo

    def accelerate(self):
        # If turbo, speed += 20, else normal
        if self.turbo:
            self.speed += 20
        else:
            self.speed += 10
# Test:
ferrari = SportsCar("Ferrari", "488", 2023, True)
ferrari.accelerate()


# TODO: Student hierarchy
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []
        self.gpa = 0.0
    def enroll(self, course):
        self.courses.append(course)
        print(f"Enrolled in {course}")
class GraduateStudent(Student):
    def __init__(self, name, student_id, thesis_topic):
        # Initialize parent
        # Add thesis_topic
        # Add advisor attribute (starts None)
        super().__init__(name, student_id)
        self.thesis_topic = thesis_topic
        self.advisor = None
    def set_advisor(self, advisor_name):
        # Set the advisor
        self.advisor = advisor_name

    def enroll(self, course):
        # Grad students can only take 500+ level courses
        # Check if course number >= 500
        course_number = int(''.join(filter(str.isdigit, course)))
        if course_number >= 500:
            super().enroll(course)
        else:
            print("Graduate students can only enroll in 500+ level courses.")


# TODO: Person who is both student and employee
class Student:
    def __init__(self):
        self.student_id = "S12345"
        self.gpa = 3.5
    def study(self):
        print("Studying hard!")
class Employee:
    def __init__(self):
        self.employee_id = "E67890"
        self.salary = 20000
    def work(self):
        print("Working hard!")
class StudentEmployee(Student, Employee):
    def __init__(self, name):
        # Initialize both parents
        # Add name attribute
        Student.__init__(self)
        Employee.__init__(self)
        self.name = name
# Test:
person = StudentEmployee("Alex")
person.study()
person.work()



# TODO: Vehicle for land and water
class LandVehicle:
    def __init__(self):
        self.speed_on_land = 60
    def drive(self):
        print(f"Driving at {self.speed_on_land} mph")
class WaterVehicle:
    def __init__(self):
        self.speed_on_water = 30
    def sail(self):
        print(f"Sailing at {self.speed_on_water} knots")
class AmphibiousVehicle(LandVehicle, WaterVehicle):
    def __init__(self, name):
        # Initialize both
        # Track current mode
        LandVehicle.__init__(self)
        WaterVehicle.__init__(self)
        self.name = name

    def switch_mode(self):
        # Toggle between land and water
        if hasattr(self, 'on_land') and self.on_land:
            self.on_land = False
            print(f"{self.name} switched to water mode.")
        else:
            self.on_land = True
            print(f"{self.name} switched to land mode.")

