# TODO: Create Person with from_birth_year class method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        @classmethod
        def from_birth_year(cls, name, birth_year):
            #calculate age from birth year
            #use from datetime import datetime
            from datetime import datetime
            current_year = datetime.now().year
            age = current_year - birth_year
            return cls(name, age)

person = Person.from_birth_year("Alice", 2000)
print(f"{person.name} is {person.age} years old.")

# TODO: Load configuration from different sources
class Config:
    def __init__(self, host, port, debug):
        self.host = host
        self.port = port
        self.debug = debug
    
    @classmethod
    def from_json_string(cls, json_string):
        import json
        data = json.loads(json_string)
        return cls(data['host'], data['port'], data['debug'])
    
    @classmethod
    def default_config(cls):
        return cls("localhost", 8080, False)
    
# TODO: Create static email validation
class EmailValidator:
    @staticmethod
    def is_valid_email(email):
        import re
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def get_domain(email):
        if EmailValidator.is_valid_email(email):
            return email.split('@')[1]
        return None

# TODO: File helper static methods
class FileHelper:
    @staticmethod
    def get_extension(filename):
        return filename.split('.')[-1] if '.' in filename else ''
    @staticmethod
    def is_image_file(filename):
        image_extensions = {'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'}
        return FileHelper.get_extension(filename).lower() in image_extensions
    @staticmethod
    def make_safe_filename(filename):
        import re
        return re.sub(r'[^a-zA-Z0-9_.-]', '_', filename)



# TODO: Create class with all three types
class Temperature:
    #instance method
    def __init__(self, celsius):
        self.celsius = celsius
    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32
    #class method
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return cls(celsius)
    #static method
    @staticmethod
    def is_freezing(celsius):
        return celsius <= 0
    

# TODO: User management with mixed methods
class User:
    all_users = []
    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.all_users.append(self)
        
        #instance method
    def login(self):
        return f"{self.username} logged in."
    #class method
    @classmethod
    def get_active_users(cls):
        return [user.username for user in cls.all_users]
    
    #static method
    @staticmethod
    def is_valid_username(username):
        # Check: 3-20 chars, alphanumeric only
        return username.isalnum() and 3 <= len(username) <= 20



# TODO: Create animal factory
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type.lower() == 'dog':
            return Dog()
        elif animal_type.lower() == 'cat':
            return Cat()
        else:
            raise ValueError("Unknown animal type")
        

# TODO: Create connection based on database type
class DatabaseConnection:
    def connect(self):
        pass
class MySQLConnection(DatabaseConnection):
    def connect(self):
        return "Connected to MySQL database."
class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        return "Connected to PostgreSQL database."
class DatabaseConnectionFactory:
    @staticmethod
    def create_connection(db_type):
        if db_type.lower() == 'mysql':
            return MySQLConnection()
        elif db_type.lower() == 'postgresql':
            return PostgreSQLConnection()
        else:
            raise ValueError("Unsupported database type")

