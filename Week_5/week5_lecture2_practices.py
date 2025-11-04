import re
def practice_1a():
    # Find the word "dog" in the text
    text = "The dog barked at the mailman"
    pattern = "dog" # Fill in the pattern
    result = re.search(pattern, text)
    if result:
        print("Found the dog!")
practice_1a()

def practice_1b():
    # Find "2024" in the text and print its position
    text = "The year 2024 will be exciting"
    pattern = '2024'
    result = re.search(pattern, text)
    if result:
        print(result.group())
practice_1b()


# Create a function that checks if a word exists in text
def word_exists(text, word):
    pattern = word
    result = re.search(pattern, text)
    return result is not None

def practice_1c():
    print(word_exists("Hello world", "world"))
    print(word_exists("Hello world", "python")) # Should print False


def practice_2a():
    #match any vowel
    text = "Hello World"
    pattern = "[aeiouAEIOU]"
    result = re.findall(pattern, text)
    print(result)

