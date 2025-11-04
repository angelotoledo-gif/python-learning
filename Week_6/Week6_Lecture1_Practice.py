import re
'''
practice 1_a
'''
print("*"*40)

# Match years (exactly 4 digits)
text = "Born in 1995, graduated 2017, now it's 24"
pattern = r"\d{4}" # Fill in the repetition
matches = re.findall(pattern, text)
print(f"Years found: {matches}")
'''
practice 1_b
'''
print("*"*40)

# Validate hex color codes (#RGB or #RRGGBB)
colors = ["#FFF", "#FFFFFF", "#12AB56", "#GGG", "#12"]
# Write pattern for 3 or 6 hex digits after #
# Hint: [0-9A-Fa-f]{3} or {6}
pattern = r"^#([0-9A-Fa-f]{6})$"
valid_colors = [color for color in colors if re.match(pattern, color)]
print(f"Valid hex colors: {valid_colors}")
'''
practice 1_c
'''
print("*"*40)

# Extract and validate US Social Security Numbers
# Format: XXX-XX-XXXX where X is a digit
text = "SSN: 123-45-6789, Invalid: 12-345-6789, 123-4-5678"
# Write pattern using {n} for each section
pattern = r"\b\d{3}-\d{2}-\d{4}\b"

valid_ssns = re.findall(pattern, text)
print(f"Valid SSNs: {valid_ssns}")

'''
practice 2_a
'''
print("*"*40)

# Match repeated words like "very very" or "really really"
text = "It's very very important and really really cool"
pattern = r"(\w+) \1" # Fill in to match repeated words
matches = re.findall(pattern, text)
print(f"Repeated words: {matches}") 


'''
practice 2_b
'''
print("*"*40)

# Extract date components (MM/DD/YYYY)
dates = ["12/25/2024", "01/01/2025", "13/40/2024"]
# Write pattern with groups for month, day, year
# Validate and extract each component
pattern = r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{4})$"

for date in dates:
    match = re.match(pattern, date)
    if match:
        month, day, year = match.groups()
        print(f"Valid date: {date}")
    else:
        print(f"Invalid date: {date}")

'''
practice 2_c
'''
print("*"*40)
# Parse URLs: protocol://domain/path
urls = ["http://example.com/page", "https://site.org/path/to/file"]
# Create groups for protocol, domain, and path
# Print each component separately
pattern = r"^(https?)://([^/]+)(/.*)$"

for url in urls:
    match = re.match(pattern, url)
    if match:
        protocol, domain, path = match.groups()
        print(f"URL: {url}")
        print(f"  Protocol: {protocol}")
        print(f"  Domain:   {domain}")
        print(f"  Path:     {path}\n")

'''
practice 3_a
'''
print("*"*40)
# Extract name and age from text
text = "My name is Alice and I am 25 years old"
pattern = r"name is (\w+) and I am (\d+)"
# Complete the code to print name and age separately
match = re.search(pattern, text)
if match:
    name, age = match.groups()
# Print the captured groups
print("Name is: " , name)
print("Age is: " , age)

'''
practice 3_b
'''
print("*"*40)
# Parse email addresses with named groups
emails = ["john.doe@company.com", "alice_smith@university.edu"]
# Write pattern with named groups for username and domain
# Pattern: (?P<user>...) @ (?P<domain>...)
pattern = r"(?P<user>[\w\.]+)@(?P<domain>[\w\.]+)"

for email in emails:
    match = re.match(pattern, email)
    if match:
        user = match.group("user")
        domain = match.group("domain")
        print(f"Email: {email}")
        print(f"  Username: {user}")
        print(f"  Domain:   {domain}\n")
'''
practice 3_c
'''
print("*"*40)
# Extract and validate time in HH:MM:SS format
times = ["12:30:45", "25:00:00", "10:65:30", "09:15:22"]
# Write pattern with groups for hours, minutes, seconds
# Validate each component (hours: 00-23, minutes/seconds: 00-59)
pattern = r"^(?P<hour>[01]\d|2[0-3]):(?P<minute>[0-5]\d):(?P<second>[0-5]\d)$"

for time in times:
    match = re.match(pattern, time)
    if match:
        print(f"Valid time: {time} ")
    else:
        print(f"Invalid time: {time}")

'''
practice 4_a
'''
print("*"*40)
text = "Hello there! Hi everyone. Hey you. Goodbye."
pattern = r"\b(Hello|Hi|Hey)\b" # Fill in: Match Hello, Hi, or Hey
matches = re.findall(pattern, text)
print(f"Greetings: {matches}")


'''
practice 4_b
'''
print("*"*40)
# Validate file extensions for documents
files = ["report.doc", "image.jpg", "data.xlsx", "notes.txt"]
# Match .doc, .docx, .pdf, or .txt files
# Use alternation with proper grouping
pattern = r".+\.(doc|docx|pdf|txt)$"
valid_docs = [file for file in files if re.match(pattern, file)]
print(f"Valid document files: {valid_docs}")

'''
practice 4_c
'''
print("*"*40)
# Parse different date formats
dates = ["2024-01-15", "15/01/2024", "Jan 15, 2024", "January 15, 2024"]
# Write pattern to match:
# - YYYY-MM-DD
# - DD/MM/YYYY
# - Mon DD, YYYY
# Use alternation to handle all formats
pattern = r"^(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|[A-Za-z]{3,9} \d{1,2}, \d{4})$"

for date in dates:
    if re.match(pattern, date):
        print(f"Matched date: {date}")
    else:
        print(f"Invalid format: {date}")


'''
practice 5-a
'''
print("*"*40)
# Find a number and print its position
text = "The temperature is 72 degrees"
pattern = r"\d+"
match = re.search(pattern, text)
if match:
    number = match.group()
    start, end = match.span()
    print(f"Found number: {number}")
    print(f"Position: start={start}, end={end}")
# Print the number and where it was found
# Use match.group() and match.span()
    
'''
practice 5_b
'''
print("*"*40)
# Extract URL components and their positions
url = "https://www.example.com/path/to/page"
pattern = r"(https?)://([^/]+)(.*)"
# Use the match object to extract:
# - Protocol (http or https)
# - Domain
# - Path
# - Position of each component
match = re.match(pattern, url)
if match:
    protocol = match.group(1)
    domain = match.group(2)
    path = match.group(3)

    protocol_span = match.span(1)
    domain_span = match.span(2)
    path_span = match.span(3)

    print(f"Protocol: {protocol} at {protocol_span}")
    print(f"Domain:   {domain} at {domain_span}")
    print(f"Path:     {path} at {path_span}")
'''
practice 5_c
'''
print("*"*40)
# Build a function that returns match details as dictionary


#Return dictionary with:
#- 'found': Boolean
#- 'match': The matched text
#- 'groups': All captured groups
#- 'position': (start, end) tuple
#- 'before': Text before match
#- 'after': Text after match

# Implement this function

def get_match_info(text, pattern):
    """
    Return dictionary with:
    - 'found': Boolean
    - 'match': The matched text
    - 'groups': All captured groups
    - 'position': (start, end) tuple
    - 'before': Text before match
    - 'after': Text after match
    """
    match = re.search(pattern, text)
    if match:
        start, end = match.span()
        return {
            'found': True,
            'match': match.group(0),
            'groups': match.groups(),
            'position': (start, end),
            'before': text[:start],
            'after': text[end:]
        }
    else:
        return {
            'found': False,
            'match': None,
            'groups': (),
            'position': None,
            'before': None,
            'after': None
        }
# Test with: "Price: $19.99 (discounted)"
# Pattern: r"\$(\d+)\.(\d{2})"
text = "Price: $19.99 (discounted)"
pattern = r"\$(\d+)\.(\d{2})"
info = get_match_info(text, pattern)
print(info)


#practice 6_a

# Check if string starts with "Hello"
texts = ["Hello World", "Say Hello", "Hello", "HELLO"]
pattern = r"Hello"
# Use re.match to check if text starts with Hello
# Print whether it matches or not

for text in texts:
    if re.match(pattern, text):
        print(f"'{text}' starts with 'Hello'")
    else:
        print(f"'{text}' does NOT start with 'Hello'")

#practice 6_b

# Validate phone number format from start of string
# Format: (XXX) XXX-XXXX or XXX-XXX-XXXX
phones = ["(555) 123-4567", "555-123-4567", "Call 555-1234", "123-4567"]
# Write validation using re.match

pattern = r"^(\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})$"

for phone in phones:
    if re.match(pattern, phone):
        print(f"'{phone}' is a valid format")
    else:
        print(f"'{phone}' is NOT a valid format")


#practice 6_c

# Parse variable assignments (var = value)
assignments = ["x = 10", "name = 'John'", "flag = True", "= invalid", "no equals"]
# Write pattern to match and extract variable name and value
pattern = r"^(\w+)\s*=\s*(.+)$"

for line in assignments:
    match = re.match(pattern, line)
    if match:
        var_name = match.group(1)
        value = match.group(2)
        print(f"Variable: '{var_name}', Value: '{value}'")
    else:
        print(f"Invalid assignment: '{line}'")

