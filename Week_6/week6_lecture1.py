import re
text = "Born in 1995, graduated 2017, now it's 24"
#match years (exactly 4 digits)
years = re.findall(r'\b\d{4}\b', text)
print("Years found:", years)



colors = ["#FFF", "#FFFFFF", "#12AB56", "#GGG", "#12"]
# Validate hex color codes (#RGB or #RRGGBB)
# Write pattern for 3 or 6 hex digits after #
pattern = r'^#([0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})$'
valid_colors = [color for color in colors if re.match(pattern, color)]
print("Valid colors:", valid_colors)



text = "SSN: 123-45-6789, Invalid: 12-345-6789, 123-4-5678"
# Extract and validate US Social Security Numbers
# Format: XXX-XX-XXXX where X is a digit
ssns = re.findall(r'\b\d{3}-\d{2}-\d{4}\b', text)
print("Valid SSNs found:", ssns)



text = "It's very very important and really really cool"
# Match repeated words like "very very" or "really really"
pattern = r'\b(\w+)\s+\1\b'
matches = re.findall(pattern, text)
print("Repeated words found:", matches)



dates = ["12/25/2024", "01/01/2025", "13/40/2024"]
# Extract date components (MM/DD/YYYY)
date_pattern = r'(\d{2})/(\d{2})/(\d{4})'
for date in dates:
    match = re.match(date_pattern, date)
    if match:
        month, day, year = match.groups()
        print(f"Date: {date} => Month: {month}, Day: {day}, Year: {year}")
    else:
        print(f"Invalid date format: {date}")



urls = ["http://example.com/page", "https://site.org/path/to/file"]
# Parse URLs: protocol://domain/path
# Create groups for protocol, domain, and path
# Print each component separately
url_pattern = r'^(https?)://([\w.-]+)/?(.*)$'
for url in urls:
    match = re.match(url_pattern, url)
    if match:
        protocol, domain, path = match.groups()
        print(f"URL: {url} => Protocol: {protocol}, Domain: {domain}, Path: {path}")



text = "My name is Alice and I am 25 years old"
# Extract name and age from text
pattern = r'My name is (\w+) and I am (\d+) years old'

# Complete the code to print name and age separately
match = re.search(pattern, text)
if match:
    name, age = match.groups()
    print(f"Name: {name}, Age: {age}")



emails = ["john.doe@company.com", "alice_smith@university.edu"]
# Parse email addresses with named groups
# Write pattern with named groups for username and domain
# Pattern: (?P<user>...) @ (?P<domain>...)
email_pattern = r'(?P<user>[\w._%+-]+)@(?P<domain>[\w.-]+\.[a-zA-Z]{2,})'
for email in emails:
    match = re.match(email_pattern, email)
    if match:
        user = match.group('user')
        domain = match.group('domain')
        print(f"Email: {email} => User: {user}, Domain: {domain}")



text = "Hello there! Hi everyone. Hey you. Goodbye."
# Match different greetings
pattern = r'\b(Hello|Hi|Hey)\b'
matches = re.findall(pattern, text)
print("Greetings found:", matches)



files = ["report.doc", "image.jpg", "data.xlsx", "notes.txt"]
# Match .doc, .docx, .pdf, or .txt files
# Use alternation with proper grouping
pattern = r'.*\.(docx?|pdf|txt)$'
matched_files = [file for file in files if re.match(pattern, file)]
print("Matched files:", matched_files)



text = "The temperature is 72 degrees"
# Find a number and print its position
pattern = r'\b\d+\b'
match = re.search(pattern, text)
if match:
    print(f"Number found: {match.group()} at position {match.start()}-{match.end()}")



url = "https://www.example.com/path/to/page"
# Extract URL components and their positions
# Extract URL components and their positions
pattern = r'^(https?)://([\w.-]+)(/.*)?$'

# Use the match object to extract:
# - Protocol (http or https)
# - Domain
# - Path
# - Position of each component

match = re.match(pattern, url)
if match:
    protocol, domain, path = match.groups()
    print(f"Protocol: {protocol} (Position: {match.start(1)}-{match.end(1)})")
    print(f"Domain: {domain} (Position: {match.start(2)}-{match.end(2)})")
    if path:
        print(f"Path: {path} (Position: {match.start(3)}-{match.end(3)})")
    else:
        print("Path: None")



texts = ["Hello World", "Say Hello", "Hello", "HELLO"]
# Check if string starts with "Hello"
pattern = r'^Hello'
for text in texts:
    if re.match(pattern, text):
        print(f"'{text}' starts with 'Hello'")
    else:
        print(f"'{text}' does not start with 'Hello'")



# Validate phone number format from start of string
# Format: (XXX) XXX-XXXX or XXX-XXX-XXXX
phones = ["(555) 123-4567", "555-123-4567", "Call 555-1234", "123-4567"]
# Write validation using re.match
phone_pattern = r'^(\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})$'
for phone in phones:
    if re.match(phone_pattern, phone):
        print(f"Valid phone number: {phone}")
    else:
        print(f"Invalid phone number: {phone}")



assignments = ["x = 10", "name = 'John'", "flag = True", "= invalid", "no equals"]
# Write pattern to match and extract variable name and value
# Pattern should match from start: variable_name = value
assignment_pattern = r'^\s*([a-zA-Z_]\w*)\s*=\s*(.+)$'
for assignment in assignments:
    match = re.match(assignment_pattern, assignment)
    if match:
        var_name, value = match.groups()
        print(f"Variable: {var_name}, Value: {value}")
    else:
        print(f"Invalid assignment: {assignment}")

