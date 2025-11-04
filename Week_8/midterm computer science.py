#Grade Book System
def add_student(gradebook, name, grade):
    if 0 <= grade <= 100:
        gradebook[name] = grade
        return True
    else:
        return False

def get_class_average(gradebook):
    if not gradebook:
        return 0
    total = sum(gradebook.values())
    return (total / len(gradebook))

def get_passing_students(gradebook):
    passing_students = [name for name, grade in gradebook.items() if grade >= 60]
    return passing_students

if __name__ == "__main__":
    gradebook = {}
    add_student(gradebook, "Alice", 85)
    add_student(gradebook, "Bob", 150)
    add_student(gradebook, "Charlie", 45)
    
    print(f"Average: {get_class_average(gradebook):.2f}")
    print(f"Passing: {get_passing_students(gradebook)}")




#Problem 5, Regular Expressions
import re
def find_all_phones(text): 
    pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(pattern, text)

def find_all_prices(text):
    pattern = r'\$\d+\.\d{2}'
    return re.findall(pattern, text)

def extract_emails(text): 
    pattern = r'[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

def validate_student_id(student_id):
    pattern = r'^[A-Z]{2}\d{4}$'
    return bool(re.match(pattern, student_id))

if __name__ == "__main__":
    text = "For info, call 555-123-4567 or (555) 987-6543. Email us at info@school.edu or admin@college.com Course fee: $50.00 for materials, $150.50 for tuition."
    print("Phones:", find_all_phones(text))
    print("Prices:", find_all_prices(text))
    print("Emails:", extract_emails(text))

    print("Valid ID 'CS1234'?", validate_student_id("CS1234"))
    print("Valid ID '12ABCD'?", validate_student_id("12ABCD"))
    print("Valid ID 'AB12345'?", validate_student_id("AB12345"))