products = {
'laptop': 899.99,
'mouse': 29.99,
'keyboard': 79.99,
'monitor': 299.99
}
# 1. Get all product names
for product in products.keys():
    print(product)
# 2. Calculate total inventory value
total_value = sum(products.values())
print(f"Total inventory value: ${total_value:.2f}")
# 3. Find the most expensive product
most_expensive = max(products, key=products.get)
print(f"Most expensive product: {most_expensive} at ${products[most_expensive]:.2f}")
# 4. Create a list of (product, price) tuples sorted by price
sorted_products = sorted(products.items(), key=lambda item: item[1])
print("Products sorted by price:")
for product, price in sorted_products:
    print(f"{product}: ${price:.2f}")


students = {
'Alice': {'courses': ['CS1350', 'MATH2010'], 'credits': 6},
'Bob': {'courses': ['CS1350', 'PHYS1410', 'ENGL1010'], 'credits': 9},
'Carol': {'courses': ['MATH2010', 'PHYS1410'], 'credits': 6}
}
# 1. Find all unique courses being taken
unique_courses = set()
for info in students.values():
    unique_courses.update(info['courses'])
print("Unique courses being taken:")
for course in unique_courses:
    print(course)
# 2. Calculate average credit load
total_credits = sum(info['credits'] for info in students.values())
average_credits = total_credits / len(students)
print(f"Average credit load: {average_credits:.2f} credits")

# 3. Find students taking more than 6 credits
heavy_load_students = [name for name, info in students.items() if info['credits'] > 6]
print("Students taking more than 6 credits:")
for student in heavy_load_students:
    print(student)

# 4. Create a course enrollment count dictionary
course_enrollment = {}
for info in students.values():
    for course in info['courses']:
        if course in course_enrollment:
            course_enrollment[course] += 1
        else:
            course_enrollment[course] = 1
print("Course enrollment counts:")
for course, count in course_enrollment.items():
    print(f"{course}: {count} students")




large_data = {f"item_{i}": i * 1.5 for i in range(100000)}
# Implement and time these operations:
# 1. Sum all values using values() view
import time
start_time = time.time()
total = sum(large_data.values())
end_time = time.time()
print(f"Sum using values(): {total}, Time taken: {end_time - start_time:.6f} seconds")

# 2. Sum all values by iterating over keys
start_time = time.time()
total = 0
for key in large_data.keys():
    total += large_data[key]
end_time = time.time()
print(f"Sum by iterating over keys: {total}, Time taken: {end_time - start_time:.6f} seconds")

# 3. Create a new dictionary with doubled values
start_time = time.time()
doubled_data = {key: value * 2 for key, value in large_data.items()}
end_time = time.time()
print(f"Created doubled_data dictionary, Time taken: {end_time - start_time:.6f} seconds")

# Which approach is fastest and why?
# The first approach (using values() view) is generally the fastest 
# because it avoids the overhead of key lookups in the second approach.