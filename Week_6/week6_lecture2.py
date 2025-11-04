import re

print("="*40)
print("Exercise 1")
print("="*40)
# Exercise 1: Find all capital letters in text
text = "HTML and CSS are Not Programming Languages"
pattern = r"[A-Z]"  # Matches any single uppercase letter
capitals = re.findall(pattern, text)
print(f"Capital letters: {capitals}")

print("="*40)
print("Exercise 2")
print("="*40)
text = 'He said "hello" and she replied "hi there" quietly'
pattern = r'"(.*?)"'  # Match text between double quotes (non-greedy)
quoted_strings = re.findall(pattern, text)
print(f"Quoted strings: {quoted_strings}")

print("="*40)
print("Exercise 3")
print("="*40)
log = """
[INFO] 2024-01-15 10:30:15 - Server started
[ERROR] 2024-01-15 10:35:22 - Connection failed
[WARNING] 2024-01-15 10:40:00 - High memory usage
"""

pattern = r"\[(.*?)\]\s+(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (.+)"

entries = re.findall(pattern, log)
print(entries)

print("="*40)
print("Exercise 1")
print("="*40)
# Find all words and their positions
text = "The quick brown fox"
pattern = r"\w+"

# Use finditer to print each word and where it starts
for match in re.finditer(pattern, text):
    word = match.group()
    position = match.start()
    print(f"Word: '{word}' starts at position {position}")


print("="*40)
print("Exercise 2")
print("="*40)
text = "aaaa"
pattern = r"(?=(aa))"  # Lookahead to capture overlapping "aa"

for match in re.finditer(pattern, text):
    print(f"Found '{match.group(1)}' at position {match.start()}")

print("="*40)
print("Exercise 3")
print("="*40)

text = "the cat and the dog and the bird"
concordance = {}
pattern = r"\w+"

for match in re.finditer(pattern, text):
    word = match.group()
    position = match.start()
    if word not in concordance:
        concordance[word] = []
    concordance[word].append(position)

print(concordance)



# Replace all spaces with underscores
print("="*40)
print("Exercise 1")
print("="*40)
text = "Convert this to snake case"
pattern = r" " # Fill in pattern for space
replacement = "_" # Fill in replacement
result = re.sub(pattern, replacement, text)
print(f"Snake case: {result}")


print("="*40)
print("Exercise 2")
print("="*40)
# Mask email addresses (keep first letter and domain)
text = "Contact john@example.com or mary@company.org"
# Replace middle part with ***
# Expected: "Contact j***@example.com or m***@company.org"
pattern = r"\b(\w)(\w*)@([\w.-]+\.\w+)\b"

masked = re.sub(pattern, r"\1***@\3", text)
print(masked)


print("="*40)
print("Exercise 3")
print("="*40)
text = "Check [Google](https://google.com) and [GitHub](https://github.com)"
pattern = r"\[(.*?)\]\((.*?)\)"  # Group 1: link text, Group 2: URL

converted = re.sub(pattern, r'<a href="\2">\1</a>', text)
print(converted)