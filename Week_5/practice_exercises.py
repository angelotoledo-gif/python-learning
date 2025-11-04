"""
CS1350 Computer Science II
Week 5 Lecture 1: Advanced String Operations
Student Skeleton Code
Name: Angel Toledo
Date: September 18, 2025
"""
# ============================================================
# UNIT 1: String Methods - Changing Case and Cleaning
# ============================================================
def practice_1a_beginner():
    """
    Beginner: Clean up a messy name
    """
    print("\n" + "="*50)
    print("EXERCISE 1A: Clean the Name (Beginner)")
    print("="*50)
    # Messy name from user input
    messy_name = " jOhN sMiTh "
    print(f"Messy name: '{messy_name}'")
    # TODO 1: Remove spaces from both ends
    no_spaces = messy_name.strip() # Replace None with your code
    # TODO 2: Convert to title case (John Smith)
    clean_name = no_spaces.title() # Replace None with your code
    print(f"After removing spaces: '{no_spaces}'")
    print(f"Final clean name: '{clean_name}'")
    # Check your work
    if clean_name == "John Smith":
        print(" Perfect! You cleaned the name correctly!")
    else:
        print(" Not quite right. Try again!")
practice_1a_beginner()

def practice_1b_intermediate():
    """
    Intermediate: Standardize email addresses
    """
    print("\n" + "="*50)
    print("EXERCISE 1B: Email Standardizer (Intermediate)")
    print("="*50)
    emails = [
        " JOHN@GMAIL.COM",
        "Alice@Yahoo.com ",
        " Bob@HOTMAIL.COM "
    ]
    print("Messy emails:")
    for email in emails:
        print(f" '{email}'")
    cleaned_emails = []
    for email in emails:
        # TODO 1: Remove spaces
        cleaned = email.strip() # Replace None
        # TODO 2: Convert to lowercase
        cleaned = cleaned.lower() # Replace None
        # TODO 3: Add to cleaned_emails list
        cleaned_emails.append(cleaned) # Remove this pass and add your code
    print("\nCleaned emails:")
    for email in cleaned_emails:
        print(f" {email}")
practice_1b_intermediate()

def practice_1c_advanced():
    """
    Advanced: Process multiple data fields
    """
    print("\n" + "="*50)
    print("EXERCISE 1C: Data Processor (Advanced)")
    print("="*50)
    user_data = {
        "name": " JANE DOE ",
        "email": " Jane@Email.COM ",
        "username": " JaNe_DoE_123 ",
        "country": "united states"
    }
    print("Original data:")
    for key, value in user_data.items():
        print(f" {key}: '{value}'")
    cleaned_data = {}
    # TODO: Clean all fields appropriately
    # Name: strip spaces and use title case
    cleaned_data["name"] = user_data["name"].strip().title() # Replace None
    # Email: strip spaces and lowercase
    cleaned_data["email"] = user_data["email"].strip().lower() # Replace None
    # Username: strip spaces and lowercase
    cleaned_data["username"] = user_data["username"].strip().lower() # Replace None
    # Country: strip spaces and title case
    cleaned_data["country"] = user_data["country"].strip().title() # Replace None
    print("\nCleaned data:")
    for key, value in cleaned_data.items():
        print(f" {key}: '{value}'")
practice_1c_advanced()

# ============================================================
# UNIT 2: String Searching and Checking
# ============================================================
def practice_2a_beginner():
    """
    Beginner: Find words in a sentence
    """
    print("\n" + "="*50)
    print("EXERCISE 2A: Find Words (Beginner)")
    print("="*50)
    sentence = "Python programming is really fun and programming is useful"
    print(f"Sentence: {sentence}")
    # TODO 1: Check if "Python" is in the sentence
    has_python = sentence.find("Python") # Replace None
    # TODO 2: Count how many times "programming" appears
    prog_count = sentence.count("programming") # Replace None
    # TODO 3: Find the position of "fun"
    fun_position = sentence.find("fun") # Replace None
    print(f"Contains 'Python': {has_python}")
    print(f"'programming' appears: {prog_count} times")
    print(f"'fun' starts at position: {fun_position}")
practice_2a_beginner()

def practice_2b_intermediate():
    """
    Intermediate: Check password strength
    """
    print("\n" + "="*50)
    print("EXERCISE 2B: Password Checker (Intermediate)")
    print("="*50)
    passwords = ["abc123", "PASSWORD", "Pass123!", "12345678"]
    for password in passwords:
        print(f"\nChecking: {password}")
        # TODO 1: Check if password has any digits
        has_digit = password.isdigit() # Replace with appropriate check
        # TODO 2: Check if password has any uppercase
        has_upper = password.isupper() # Replace with appropriate check
        # TODO 3: Check if password has any lowercase
        has_lower = password.islower() # Replace with appropriate check
        # TODO 4: Check if length is at least 8
        long_enough = password.count("8")
        print(f" Has digit: {has_digit}")
        print(f" Has uppercase: {has_upper}")
        print(f" Has lowercase: {has_lower}")
        print(f" Length >= 8: {long_enough}")
        # Check if strong (all requirements met)
        if all([has_digit, has_upper, has_lower, long_enough]):
            print("PASSWORD")
        else:
            print("WEAK PASSWORD")
practice_2b_intermediate()

