# TODO: Create Car with make, model, year
class Car:
    def __init__(self, make, model, year): #self if the parameter that refers to the instance being created
        self.make = make
        self.model = model
        self.year = year
# Test:
my_car = Car("Toyota", "Camry", 2020) #instance variable: my_car
print(f"{my_car.year} {my_car.make} {my_car.model}") #.year is an access to the instance variable year


# TODO: Add mileage and drive() method
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0
    def drive(self, miles):
    # Add miles to mileage
    # Print total mileage
        self.mileage += miles
        print(f"Total mileage: {self.mileage} miles")



# TODO: Add fuel tank and consumption
class Car:
    def __init__(self, make, model, year, mpg):
        # Your code here
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_tank = 10
        self.mpg = 35  # miles per gallon
    def drive(self, miles):
        # Calculate fuel needed
        # Check if enough fuel
        # Update mileage and fuel
        fuel_needed = miles / self.mpg
        if fuel_needed > self.fuel_tank:
            print("Not enough fuel to drive that distance.")
        else:
            self.mileage += miles
            self.fuel_tank -= fuel_needed
            print(f"Drove {miles} miles. Total mileage: {self.mileage} miles. Fuel left: {self.fuel_tank} gallons.")


#__init__ is a constructor method that initializes instance variables when an object is created.


# TODO: Create Teacher class that holds students
class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []
    # Add method to add a student
    def add_students(self, student_name):
        self.students.append(student_name)
# Test:
teacher = Teacher("Mr. Johnson")
teacher.add_student("Alice")
print(teacher.students)


# TODO: Add remove_student method
class Teacher:
    def __init__(self, name):
        # Your code
        self.name = name
        self.students = []
    def add_student(self, student_name):
        # Your code
        self.students.append(student_name)
    def remove_student(self, student_name):
        # Check if student exists first
        # Remove if found
        if student_name in self.students:
            self.students.remove(student_name)
        else:
            print(f"Student {student_name} not found.")


# TODO: Track grades for each student
class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = {} # Dictionary: name -> grade

    def add_student(self, name, initial_grade=0):
        # Your code
        self.students[name] = initial_grade

    def grade_student(self, name, grade):
        # Update grade if student exists
        if name in self.students:
            self.students[name] = grade

        
    def class_average(self):
        # Calculate and return average grade
        if self.students != {}:
            total = sum(self.students.values())
            return total / len(self.students)