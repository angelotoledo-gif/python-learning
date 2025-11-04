import re

text = "The dog barked at the mailman"
pattern = "dog" # Fill in the pattern
result = re.search(pattern, text)
if result:
    print("Found the dog!")


text = "The year 2024 will be exciting"
#search for "2024"
pattern = "2024"
#print where it starts in the text
result = re.search(pattern, text)
if result:
    print("Found 2024 at position:", result.start())

def word_exists(text, word):
    # Use re.search to check if word exists
    # Return True if found, False otherwise
    pattern = word
    result = re.search(pattern, text)
    return result is not None
print(word_exists("Hello world", "world"))  # Should return True
print(word_exists("Hello world", "Python")) # Should return False



text = "Hello World"
# Match any vowel (a, e, i, o, u) in the text
pattern = "[aeiou]"
result = re.search(pattern, text, re.IGNORECASE)
if result:
    print("Found a vowel at position:", result.start())

text = "Color code: #FF5A2B"
# Find all hexadecimal digits (0-9, A-F, a-f)
pattern = "[0-9A-Fa-f]"
result = re.findall(pattern, text)
print("Hexadecimal digits found:", result)

text = "Hello, World! 123"
# Extract all non-alphabetic characters from text
pattern = "[^a-zA-Z]"
result = re.findall(pattern, text)
print("Non-alphabetic characters found:", result)



text = "I have 2 cats and 3 dogs"
# Count all digits in the text
pattern = "\d"
result = re.findall(pattern, text)
print("Digits found:", result)
print("Number of digits found:", len(result))

text = "user@email.com has user_id=12345"
# Extract all "words" (continuous word characters)
pattern = "\w+"
result = re.findall(pattern, text)
print("Words found:", result)

text = "Hello! How are you? I'm fine... Thanks!"
# Clean text by removing all non-word characters except spaces
pattern = "[^\w\s]"
cleaned_text = re.sub(pattern, "", text)
print("Cleaned text:", cleaned_text)



texts = ["Python is fun", "I love Python", "Python"]
# Check if string starts with "Python"
pattern = "^Python"
for t in texts:
    if re.search(pattern, t):
        print(f'"{t}" starts with "Python"')

test_strings = ["12345", "123abc", "456"]
# Validate that a string contains ONLY digits
pattern = "^\d+$"
for s in test_strings:
    if re.search(pattern, s):
        print(f'"{s}" contains only digits')
    else:
        print(f'"{s}" does not contain only digits')

text = "The cat sat on the mat with a bat"
# Find all three-letter words ending in 'at'
pattern = r"\b\w{1}at\b"
result = re.findall(pattern, text)
print("Three-letter words ending in 'at':", result)



text = "Hello 123 world 456"
# Find all words (one or more letters)
pattern = r"[a-zA-Z]+"
result = re.findall(pattern, text)
print("Words found:", result)

phones = ["(555) 123-4567", "123-4567", "555-1234"]
# Match phone numbers with optional area code
# Format: (555) 123-4567 or 123-4567
pattern = r"(\(\d{3}\)\s)?\d{3}-\d{4}"
for phone in phones:
    if re.search(pattern, phone):
        print(f'Valid phone number: {phone}')
    else:
        print(f'Invalid phone number: {phone}')

text = 'He said "hello" and she said "goodbye" quickly'
# Extract content between quotes (non-greedy)
# Write pattern to extract text between quotes
pattern = r'"(.*?)"'
result = re.findall(pattern, text)
print("Text between quotes:", result)

