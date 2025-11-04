def practice_1_beginner():
    """
    Beginner: Understanding why we need files
    """
    print("\n" + "="*50)
    print("EXERCISE 1.1: Save Your Name")
    print("="*50)
    # TODO 1: Get user's name
    name = input("Enter your name: ")
    # TODO 2: Open a file called "myname.txt" for writing
    # Hint: Use open("myname.txt", "w")
    file = open("myname.txt", "w") # Replace None with open() function
    # TODO 3: Write the name to the file
    file.write(name)
    # Hint: Use file.write(name)
    # TODO 4: Close the file
    # Hint: Use file.close()
    file.close()
    print(f"Name '{name}' saved to myname.txt!")
    # TODO 5: Read it back
    # Open the file for reading with "r" mode
    file = open("myname.txt", "r") # Replace with open() for reading
    # Read the content
    saved_name = file.read() # Replace with file.read()
    # Close the file
    file.close
    print(f"Read back: '{saved_name}'")
    # Run the exercise
practice_1_beginner()




def practice_2_beginner():
    """
    Beginner: Work with file objects
    """
    print("\n" + "="*50)
    print("EXERCISE 2.1: File Object Basics")
    print("="*50)
    # TODO 1: Create a text file with 3 lines
    number_text = open("numbers.txt", "w")
    # Write three numbers, each on a new line
    number_text.write("10\n")
    # TODO: Write 20 and 30
    number_text.close()
    # TODO 2: Open the file and check its properties
    number_text = open("numbers.txt", "r")
    # Print file name
    print(f"File name: {number_text.name}")
    # TODO: Print file mode
    # Hint: Use file.mode
    # TODO: Check if file is closed
    # Hint: Use file.closed
    # TODO 3: Read one line at a time until EOF
    while True:
        line = number_text.readline()
        if line == "": # Check for EOF
            print("Reached end!")
            break
    print(f"Read: {line.strip()}")
    number_text.close()
    # Run the exercise
practice_2_beginner()


def practice_3_beginner():
    """
    Beginner: Basic file operations
    """
    print("\n" + "="*50)
    print("EXERCISE 3.1: Student Grades File")
    print("="*50)

    # TODO 1: Write student grades to file
    grades_file = open("grades.txt", "w")
    # Write these grades (each on new line):
    # Alice: 90
    # Bob: 85
    # Charlie: 92
    grades_file.write("Alice: 90\n")

    # TODO: Write Bob and Charlie
    grades_file.write("Bob: 85\n")
    grades_file.write("Charlie: 92\n")
    grades_file.close()
    print("Grades written!")

    # TODO 2: Read the file using read()
    grades_file = open("grades.txt", "r")
    content = grades_file.read()
    print(f"\nAll grades:\n{content}")
    grades_file.close()

    # TODO 3: Read line by line
    print("\nReading line by line:")
    grades_file = open("grades.txt", "r")

    # TODO: Use readline() three times
    line1 = grades_file.readline() # First student
    line2 = grades_file.readline() # Second student
    line3 = grades_file.readline() # Third student
    print(f"Student 1: {line1}")
    print(f"Student 2: {line2}")
    print(f"Student 3: {line3}")
    grades_file.close()
    # Run the exercise
practice_3_beginner()


def practice_4_beginner():
    """
    Beginner: Convert to with statements    
    """
    print("\n" + "="*50)
    print("EXERCISE 4.1: Using With Statement")
    print("="*50)

    # TODO 1: Rewrite using 'with'
    # Old way:
    # file = open("hello.txt", "w")
    # file.write("Hello World!")
    # file.close()


    # New way with 'with':
    with open("hello.txt", "w") as hello_file:
        # TODO: Write "Hello World!"
        file.write()
    
    print("File written with 'with'!")


    # TODO 2: Read using 'with'
    # Complete this:
    with open("hello.txt", "r") as hello_file:
        content = None # Replace with file.read()
    print(f"Content: {content}")


    # TODO 3: Append using 'with'
    with open("hello.txt", "a") as hello_file:
        # TODO: Add " Python is fun!"
        file.write()
    print("Python is fun")
        
    # TODO 4: Verify the complete content
    with open("hello.txt", "r") as hello_file:
    # TODO: Read and print everything
        content = file.read()
    print(f"Final Content: {content}")

    # Run the exercise
practice_4_beginner()


def practice_5_beginner():
    """
    Beginner: Simple contact list
    """
    print("\n" + "="*50)
    print("EXERCISE 5.1: Contact List")
    print("="*50)

    # TODO 1: create contact file
    with open("contacts.txt", "w") as contacts:
        contacts.write("My Contacts\n")
        contacts.write("-" * 20 + "\n")
    
    #TODO 2: Add 3 contacts
    with open("contacts.txt", "a") as contacts:
        contacts.write("Alice: 123-456-7890\n")
        contacts.write("Bob: 987-654-3210\n")
        contacts.write("Charlie: 555-555-5555\n")

    with open("contacts.txt", "r") as contacts:
        #TODO: write all contacts
        content = contacts.read()
    print(f"\nContacts List:\n{content}")

    with open("contacts.txt", "r") as contacts:
        #TODO: read and display all contacts
        print("Reading contacts line by line:")
        while True:
            line = contacts.readline()
            if line == "":
                break
            print(f"Contact: {line.strip()}")
    
    #Search for a contact
    search_name = "Bob"
    found = False
    with open("contacts.txt", "r") as contacts:
        while True:
            line = contacts.readline()
            if line == "":
                break
            if search_name in line:
                print(f"Found contact: {line.strip()}")
                found = True
                break
    if not found:
        print(f"{search_name} not found in contacts.")
    # Run the exercise
practice_5_beginner()
