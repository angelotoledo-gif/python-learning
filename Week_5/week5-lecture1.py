def practice_1_a_beginner():
    print("\n" + "="*50)
    print("EXERCISE 1A")
    print("="*50)
    name = "   jOhn sMiTh   "
    print(f"Original name: '{name}'")
    #remove spaces from both ends
    name = name.strip()
    #capitalize first letter of each word
    name = name.title()
    print(f"Cleaned name: '{name}'")
practice_1_a_beginner()

def practice_1_b_intermediate():
    print("\n" + "="*50)
    print("EXERCISE 1B")
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
        #remove spaces and convert to lowercase
        cleaned_email = email.strip().lower()
        cleaned_emails.append(cleaned_email)
    print("\nCleaned emails:")
    for email in cleaned_emails:
        print(f" '{email}'")
practice_1_b_intermediate()


def practice_1_c_advanced():
    print("\n" + "="*50)
    print("EXERCISE 1C")
    print("="*50)
    # User registration data (messy!)
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
    # Name: strip spaces and use title case
    cleaned_data["name"] = user_data["name"].strip().title()
    # Email: strip spaces and convert to lowercase
    cleaned_data["email"] = user_data["email"].strip().lower()
    # Username: strip spaces and convert to lowercase
    cleaned_data["username"] = user_data["username"].strip().lower()
    # Country: strip spaces and use title case
    cleaned_data["country"] = user_data["country"].strip().title()
    print("\nCleaned data:")
    for key, value in cleaned_data.items():
        print(f" {key}: '{value}'")
practice_1_c_advanced()

def practice_2_a_beginner():
    print("\n" + "="*50)
    print("EXERCISE 2A")
    print("="*50)
    sentence = "Python programming is really fun and programming is useful"
    print(f"Sentence: {sentence}")

    # TODO 1: Check if "Python" is in the sentence
    contains_python = "Python" in sentence
    print(f"Contains 'Python': {contains_python}")
    # TODO 2: Count how many times "programming" appears
    programming_count = sentence.count("programming")
    print(f"'programming' count: {programming_count}")
    # TODO 3: Find the position of "fun"
    fun_position = sentence.find("fun")
    print(f"Position of 'fun': {fun_position}")
practice_2_a_beginner()

def practice_2_b_intermediate():
    print("\n" + "="*50)
    print("EXERCISE 2B")
    print("="*50)
    passwords = ["abc123", "PASSWORD", "Pass123!", "12345678"]
    for password in passwords:
        print(f"\nChecking: {password}")
    
        # TODO 1: Check if password has any digits
        has_digit = any(char.isdigit() for char in password)
        print(f" Contains digit: {has_digit}")
        # TODO 2: Check if password has any uppercase
        has_uppercase = any(char.isupper() for char in password)
        print(f" Contains uppercase: {has_uppercase}")
        # TODO 3: Check if password has any lowercase
        has_lowercase = any(char.islower() for char in password)
        print(f" Contains lowercase: {has_lowercase}")
        # TODO 4: Check if length is at least 8
        is_long_enough = len(password) >= 8
        print(f" Is at least 8 characters: {is_long_enough}")
practice_2_b_intermediate()

def practice_2_c_advanced():
    """
    Advanced: Detect and categorize file types
    """
    print("\n" + "="*50)
    print("EXERCISE 2C: File Type Detector (Advanced)")
    print("="*50)
    files = [
    "document.pdf",
    "image.jpg",
    "photo.PNG",
    "script.py",
    "data.CSV",
    "video.mp4",
    "archive.zip",
    "webpage.html"
    ]
    # Categories
    documents = []
    images = []
    code = []
    other = []
    for filename in files:
        # Convert to lowercase for checking
        lower_name = filename.lower()
        # TODO: Categorize files based on extension
        if lower_name.endswith(('.pdf', '.docx', '.txt')):
            documents.append(filename)
        elif lower_name.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            images.append(filename)
        elif lower_name.endswith(('.py', '.js', '.html', '.css')):
            code.append(filename)
        else:
            other.append(filename)
    print("Documents:", documents)
    print("Images:", images)
    print("Code Files:", code)
    print("Other Files:", other)
practice_2_c_advanced()

def practice_3_a_beginner():
    print("\n" + "="*50)
    print("EXERCISE 3A: Word Replacer (Beginner)")
    print("="*50)
    story = "The cat sat on the cat mat. The cat was happy."
    print(f"Original: {story}")
    # TODO 1: Replace "cat" with "dog"
    dog_story = story.replace("cat", "dog")
    print(f"Modified: {dog_story}")
    # TODO 2: Replace "mat" with "rug"
    final_story = dog_story.replace("mat", "rug")
    print(f"Final: {final_story}")
    # TODO 3: Split the story into sentences (split on ". ")
    sentences = final_story.split(". ")
    print("Sentences:", sentences)
practice_3_a_beginner()

def practice_4_a_intermediate():
    print("\n" + "="*50)
    print("EXERCISE 4A: Info Formatter (Beginner)")
    print("="*50)

    # Personal information
    name = "John Doe"
    age = 25
    height = 5.9 # feet
    weight = 170.5 # pounds

    # TODO 1: Create f-string with name and age
    # Format: "Name: John Doe, Age: 25"
    info_1 = f"Name: {name}, Age: {age}"
    print(info_1)
    
    # TODO 2: Format height to 1 decimal place
    # Format: "Height: 5.9 feet"
    info_2 = f"Height: {height:.1f} feet"
    print(info_2)

    # TODO 3: Format weight to no decimal places
    # Format: "Weight: 171 lbs"
    info_3 = f"Weight: {weight:.0f} lbs"
    print(info_3)
practice_4_a_intermediate()

def practice_4_b_intermediate():
    print("\n" + "="*50)
    print("EXERCISE 4B: Table Formatter (Advanced)")
    print("="*50)

    students = [
        {"name": "Alice", "score": 92.5, "grade": "A"},
        {"name": "Bob", "score": 78.3, "grade": "C"},
        {"name": "Charlie", "score": 85.7, "grade": "B"}
    ]

    print(f"{'Name':<15} {'Score':>10} {'Grade':>10}")
    print("-" * 35)

    for student in students:
        # TODO 1: Format name left-aligned in 15 characters
        name = f"{student['name']:<15}"
        # TODO 2: Format score right-aligned with 1 decimal
        score = f"{student['score']:>10.1f}"
        # TODO 3: Format grade right-aligned in 10 characters
        grade = f"{student['grade']:>10}"
        print(f"{name}{score}{grade}")
    
    # Calculate and display average
    avg_score = sum(s["score"] for s in students) / len(students)
    # TODO 5: Format average with 2 decimal places
    print("-" * 35)
    print(f"{'Average':<15} {avg_score:.2f}")
practice_4_b_intermediate()

def practice_5a_beginner():
    print("\n" + "="*50)
    print("EXERCISE 5A: String Extraction (Beginner)")
    print("="*50)

    # Full name
    full_name = "John Michael Smith"
    print(f"Full name: {full_name}")

    # TODO 1: Get the first name (first 4 characters)
    first_name = full_name[:4]
    print(f"First name: {first_name}")

    # TODO 2: Get the last name (last 5 characters)
    last_name = full_name[-5:]
    print(f"Last name: {last_name}")

    # Email address
    email = "user@example.com"
    print(f"\nEmail: {email}")

    # TODO 3: Get username (everything before @)
    # Find @ position first
    at_position = email.find("@")
    username = email[:at_position]
    print(f"Username: {username}")

    # TODO 4: Get domain (everything after @)
    domain = email[at_position + 1:]
    print(f"Domain: {domain}")
practice_5a_beginner()

def practice_5b_intermediate():
    print("\n" + "="*50)
    print("EXERCISE 5B: Credit Card Masker (Intermediate)")
    print("="*50)

    # Credit card numbers to mask
    cards = [
        "4532-1234-5678-9012",
        "5412 3456 7890 1234",
        "378234567890123"
    ]

    for card in cards:
        print(f"\nOriginal: {card}")

        # TODO 1: Remove spaces and dashes
        clean_card = card.replace(" ", "").replace("-", "")
        print(f"Cleaned: {clean_card}")

        # TODO 1: Get last 4 digits
        last4 = clean_card[-4:]
        print(f"Last 4 digits: {last4}")
        # TODO 2: Create masked version
        # Show only last 4 digits, mask the rest with *
        if len(clean_card) >= 4:
            masked = "*" * (len(clean_card) - 4) + last4
        
        formatted = ""
        for i in range(0, len(masked), 4):
            formatted += masked[i:i+4] + " "
        formatted = formatted.strip()
        print(f"Masked: {masked}")
        print(f"Formatted: {formatted}")
practice_5b_intermediate()

def practice_6a_beginner():
    print("\n" + "="*50)
    print("EXERCISE 6A: Text Analyzer (Beginner)")
    print("="*50)

    text = """
    Python is a great programming language.
    It is easy to learn and fun to use.
    Many people love Python!
    """
    print("Text to analyze:")
    print(text)

    # TODO 1: Count total characters (including spaces)
    total_chars = len(text)
    print(f"Total characters (including spaces): {total_chars}")
    # TODO 2: Count characters without spaces
    chars_no_spaces = len(text.replace(" ", "").replace("\n", ""))
    print(f"Total characters (excluding spaces): {chars_no_spaces}")
    # TODO 3: Count words (split by whitespace)
    words = text.split()
    total_words = len(words)
    print(f"Total words: {total_words}")
    # TODO 4: Count sentences (split by ".")
    sentences = [s for s in text.split(".") if s.strip()]
    total_sentences = len(sentences)
    print(f"Total sentences: {total_sentences}")
    # TODO 5: Find the longest word
    if words:
        longest_word = max(words, key=len)
        print(f"Longest word: {longest_word}")
    
practice_6a_beginner()

def practice_6b_intermediate():
    print("\n" + "="*50)
    print("EXERCISE 6B: URL Parser (Intermediate)")
    print("="*50)
    urls = [
    "https://www.example.com/page?id=123",
    "http://subdomain.site.org/path/to/page",
    "ftp://files.server.com/document.pdf",
    "www.invalid-url.com", # Missing protocol
    "https://localhost:8080/api/data"
    ]

    for url in urls:
        print(f"\nParsing: {url}")
        
        # TODO 1: Check if URL has protocol (http://, https://, ftp://)
        has_protocol = url.startswith(("http://", "https://", "ftp://"))
        print(f" Has protocol: {has_protocol}")

        if has_protocol:
            # TODO 2: Check if URL has protocol (http://, https://, ftp://)
            protocol_end = url.find("://")
            protocol = url[:protocol_end]
            print(f" Protocol: {protocol}")

            # TODO 3: Extract domain
            domain_start = protocol_end + 3
            domain_end = url.find("/", domain_start)
            if domain_end == -1:
                domain_end = len(url)
            domain = url[domain_start:domain_end]
            print(f" Domain: {domain}")

            # TODO 4: Extract path (if exists)
            if domain_end < len(url):
                path_start = domain_end
                path_end = url.find("?", path_start)
                if path_end == -1:
                    path_end = len(url)
                path = url[path_start:path_end]
                print(f" Path: {path}")
            else:
                path = "/"
        else:
            print(" Invalid URL format (missing protocol)")
practice_6b_intermediate()
