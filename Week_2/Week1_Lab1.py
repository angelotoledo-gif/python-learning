# Test your Python environment
print("CS1350 Dictionary Lab - Choose Your Challenge")
print("=" * 50)
# Quick introduction
student_name = input("Enter your name: ")
print(f"Welcome {student_name}!")
print("\\nToday's lab has activities from 'Let's Start With' to 'Most Challenged'")
print("Choose based on what feels challenging but achievable for you.")
print("You can try multiple approaches - there's no wrong choice!")

# Let's build a student profile step by step
print("=== Building Your First Dictionary ===")
# Start simple - create empty dictionary
my_profile = {}
print(f"Empty dictionary: {my_profile}")
print(f"Type: {type(my_profile)}")
# Add information one piece at a time
print("\\n--- Adding Information ---")
# Step 1: Add name
my_profile["name"] = "Angel" # Replace with your name
print(f"After adding name: {my_profile}")
# Step 2: Add age
my_profile["age"] = 20 # Use your age
print(f"After adding age: {my_profile}")
# Step 3: Add favorite subject
my_profile["favorite_subject"] = "Marketing"
print(f"After adding subject: {my_profile}")
# Practice accessing values
print("\\n--- Accessing Information ---")
print(f"Name: {my_profile['name']}")
print(f"Age: {my_profile['age']}")
print(f"Favorite subject: {my_profile['favorite_subject']}")
# Your turn: Add these fields to your profile
print("\\n--- Your Turn ---")
my_profile["hometown"] = input("Enter your hometown: ")
my_profile["hobby"] = input("Enter your hobby: ")
my_profile["year_in_school"] = input("Enter your year (Freshman/Sophomore/etc.): ")
print(f"Complete profile: {my_profile}")



# Learning safe ways to access dictionary information
student = {
"name": "Alex Student",
"id": 12345,
"courses": ["CS1350", "MATH2010"]
}
print("=== Learning Safe Access ===")
print(f"Student info: {student}")
# Method 1: Direct access (can cause errors)
print("\\n--- Direct Access ---")
print(f"Name: {student['name']}") # This works
print(f"ID: {student['id']}") # This works
# What happens with missing keys?
print("\\n--- What about missing information? ---")
# Uncomment the next line to see the error:
# print(f"Email: {student['email']}") # This will cause KeyError!
print("(We commented out the error line!)")
# Method 2: Check first, then access
print("\\n--- Safe Method 1: Check First ---")
if "email" in student:
    print(f"Email: {student['email']}")
else:
    print("Email: Not provided")
# Your turn - check for phone number
if "phone" in student:
    print(f"Phone: {student['phone']}")
else:
    print("Phone: Not provided")
# Method 3: Use get() method
print("\\n--- Safe Method 2: Use get() ---")
email = student.get("email")
print(f"Email using get(): {email}") # Returns None if not found
# Use get() with a default value
email = student.get("email", "No email provided")
print(f"Email with default: {email}")
print("\\n--- Practice Time ---")
gpa = student.get("gpa", 0.0)
phone = student.get("phone", "No phone")
graduation_year = student.get("graduation_year", "Unknown")
print(f"GPA: {gpa}")
print(f"Phone: {phone}")
print(f"Graduation year: {graduation_year}")
print("\\n--- Practice Time ---")
gpa = student.get("gpa", 0.0)
phone = student.get("phone", "No phone")
graduation_year = student.get("graduation_year", "Unknown")
print(f"GPA: {gpa}")
print(f"Phone: {phone}")
print(f"Graduation year: {graduation_year}")


# Learning to go through all items in a dictionary
grades = {
"Math": 85,
"Science": 92,
"English": 78,
"History": 88
}
print("=== Learning Dictionary Iteration ===")
# Method 1: Loop through keys (subject names)
print("\\n--- Method 1: Just the subjects ---")
for subject in grades:
    print(f"Subject: {subject}")
# Method 2: Loop through keys and get values
print("\\n--- Method 2: Subjects and grades ---")
for subject in grades:
    grade = grades[subject]
    print(f"{subject}: {grade}")
# Method 3: Loop through values only
print("\\n--- Method 3: Just the grades ---")
for grade in grades.values():
    print(f"Grade: {grade}")
# Method 4: Loop through both at once (most useful!)
print("\\n--- Method 4: Both together ---")
for subject, grade in grades.items():
    print(f"{subject}: {grade}")
# Practice: Let's do something useful with the data
print("\\n--- Practice: Calculate average ---")
total = 0
count = 0
for subject, grade in grades.items():
    total = total + grade # Add to total
    count = count + 1 # Count how many subjects
    print(f"Added {subject} ({grade}): Total so far = {total}")
average = total / count
print(f"\\nAverage grade: {average}")
# Practice: Find highest grade
print("\\n--- Practice: Find highest grade ---")
highest_grade = 0
best_subject = ""
for subject, grade in grades.items():
    if grade > highest_grade:
        highest_grade = grade
        best_subject = subject
print(f"Best subject: {best_subject} with grade {highest_grade}")
# Your turn: Find lowest grade
print("\\n--- Your Turn: Find lowest grade ---")
lowest_grade = 100 # Start high
worst_subject = ""
for subject, grade in grades.items():
    if grade < lowest_grade:
        lowest_grade = grade
        worst_subject = subject
print(f"Subject that needs work: {worst_subject} with grade {lowest_grade}")




# Collaborative Restaurant Order System
print("=== Collaborative Restaurant Challenge ===")
print("Everyone works together on the same system!")
print("Choose tasks that feel right for your skill level.")
# Shared data structure that everyone will work with
restaurant_orders = {}
def level1_basic_orders():
    """Let's Start With: Basic order entry and simple calculations."""
    print("\\n--- Let's Start With: Basic Order Management ---")
    # Simple order structure - anyone can work with this
    sample_orders = {
        "order_001": {
            "customer": "Alice",
            "items": ["burger", "fries", "soda"],
            "total": 12.50,
            "status": "completed"
        },
        "order_002": {
            "customer": "Bob",
            "items": ["pizza", "salad"],
            "total": 15.75,
            "status": "preparing"
        },
        "order_003": {
            "customer": "Carol",
            "items": ["sandwich", "chips", "water"],
            "total": 8.25,
            "status": "pending"
        }
    }
    restaurant_orders.update(sample_orders)

    # Task 1: Show all orders
    print("Current orders:")
    for order_id, order_info in restaurant_orders.items():
        customer = order_info["customer"]
        total = order_info["total"]
        status = order_info["status"]
        print(f" {order_id}: {customer}, ${total}, {status}")
    # Task 2: Calculate total sales
    total_sales = 0
    for order_id, order_info in restaurant_orders.items():
        total_sales += order_info["total"]
    print(f"\\nTotal sales today: ${total_sales}")
    # Task 3: Count orders by status
    status_counts = {}
    for order_id, order_info in restaurant_orders.items():
        status = order_info["status"]
        if status in status_counts:
            status_counts[status] += 1
        else:
            status_counts[status] = 1
    print(f"Orders by status: {status_counts}")
    return {"total_sales": total_sales, "status_counts": status_counts}