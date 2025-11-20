import time
import random
import string
from collections import Counter

def warmup_1():
    #Create sets from different sources
    # TODO: Create a set from the string "hello world"
    # Expected: {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}
    text = "hello world"
    char_set = set(text)
    # TODO: Create a set of even numbers from 0 to 20
    even_numbers = set(range(0, 21, 2))
    # TODO: Remove duplicates from this list using a set
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    unique = set(numbers)
    return char_set, even_numbers, unique
    # Test your solution
print(warmup_1())



def create_enrollment_data():
    """Create sample enrollment data"""
    # Course enrollments - each key is a course, value is set of students
    enrollments = {
    'CS1350': {'Alice', 'Bob', 'Carol', 'David', 'Eve'},
    'MATH2010': {'Alice', 'Carol', 'Frank', 'Grace'},
    'PHYS1410': {'Bob', 'David', 'Frank', 'Henry'},
    'ENGL1010': {'Eve', 'Grace', 'Henry', 'Ivy'},
    'CHEM1010': {'Alice', 'Bob', 'Ivy', 'Jack'},
    'CS2040': {'Carol', 'David', 'Eve', 'Jack'}
    }
    # Student schedules - each key is a student, value is set of courses
    student_courses = {
    'Alice': {'CS1350', 'MATH2010', 'CHEM1010'},
    'Bob': {'CS1350', 'PHYS1410', 'CHEM1010'},
    'Carol': {'CS1350', 'MATH2010', 'CS2040'},
    'David': {'CS1350', 'PHYS1410', 'CS2040'},
    'Eve': {'CS1350', 'ENGL1010', 'CS2040'},
    'Frank': {'MATH2010', 'PHYS1410'},
    'Grace': {'MATH2010', 'ENGL1010'},
    'Henry': {'PHYS1410', 'ENGL1010'},
    'Ivy': {'ENGL1010', 'CHEM1010'},
    'Jack': {'CHEM1010', 'CS2040'}
    }
    return enrollments, student_courses
    # Load the data
course_enrollments, student_schedules = create_enrollment_data()



def find_common_students(course1, course2, enrollments):
    """
    Find students enrolled in both courses.
    Args:
    course1: First course code
    course2: Second course code
    enrollments: Dictionary of course enrollments
    Returns:
    Set of students in both courses
    """
    # TODO: Implement this function
    students_course1 = enrollments.get(course1, set())
    students_course2 = enrollments.get(course2, set())
    return students_course1.intersection(students_course2)

def find_popular_combinations(student_schedules):
    """
    Find the most common course pairs taken together.
    Args:
    student_schedules: Dictionary of student course sets
    Returns:
    List of (course_pair, count) tuples, sorted by count
    """
    # TODO: Implement this function
    # Hint: For each student, find all pairs of courses they take
    pair_counter = Counter()
    for courses in student_schedules.values():
        course_list = list(courses)
        for i in range(len(course_list)):
            for j in range(i + 1, len(course_list)):
                pair = tuple(sorted((course_list[i], course_list[j])))
                pair_counter[pair] += 1
    return pair_counter.most_common()

def find_exclusive_students(course, enrollments):
    """
    Find students who ONLY take this one course.
    Args:
    course: Course code
    enrollments: Dictionary of course enrollments
    Returns:
    Set of students taking only this course
    """
    # TODO: Implement this function
    exclusive_students = set()
    target_students = enrollments.get(course, set())
    for student in target_students:
        # Check if the student is enrolled in any other course
        enrolled_courses = [c for c, students in enrollments.items() if student in students]
        if len(enrolled_courses) == 1:
            exclusive_students.add(student)
    return exclusive_students

def recommend_courses(student, student_schedules):
    """
    Recommend courses based on what similar students take.
    Args:
    student: Student name
    student_schedules: Dictionary of student course sets
    Returns:
    Set of recommended courses (not currently taken)
    """
    # TODO: Find students with overlapping courses
    # TODO: Recommend their courses that this student doesn't take
    current_courses = student_schedules.get(student, set())
    recommended_courses = set()
    for other_student, courses in student_schedules.items():
        if other_student != student and current_courses.intersection(courses):
            # Add courses taken by similar students
            recommended_courses.update(courses)
    recommended_courses.difference_update(current_courses)
    return recommended_courses



def test_enrollment_analysis():
    """Test all enrollment analysis functions"""
    print("=== Testing Enrollment Analysis ===")
    # Test 1: Common students
    common = find_common_students('CS1350', 'MATH2010', course_enrollments)
    print(f"Students in both CS1350 and MATH2010: {common}")
    assert common == {'Alice', 'Carol'}, "Common students test failed"
    # Test 2: Popular combinations
    popular = find_popular_combinations(student_schedules)
    print(f"Popular course combinations: {popular[:3]}") # Top 3
    # Test 3: Exclusive students
    exclusive = find_exclusive_students('CS1350', course_enrollments)
    print(f"Students taking only CS1350: {exclusive}")
    # Test 4: Course recommendations
    recommendations = recommend_courses('Frank', student_schedules)
    print(f"Recommended courses for Frank: {recommendations}")
    # Run tests
test_enrollment_analysis()



def process_text(text):
    """
    Process text into a set of words (lowercase, no punctuation).
    Args:
    text: String of text to process
    Returns:
    Set of unique words
    """
    # TODO: Remove punctuation, convert to lowercase, split into words
    # Hint: Use string methods and set comprehension
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()
    words = set(cleaned_text.split())
    return words

def calculate_similarity(text1, text2):
    """
    Calculate Jaccard similarity between two texts.
    Jaccard = |intersection| / |union|
    Args:
    text1: First text string
    text2: Second text string
    Returns:
    Float between 0 and 1 (1 = identical vocabulary)
    """
    # TODO: Process both texts and calculate Jaccard similarity
    words1 = process_text(text1)
    words2 = process_text(text2)
    intersection = words1.intersection(words2)
    union = words1.union(words2)
    if not union:
        return 0.0
    return len(intersection) / len(union)

def find_unique_words(text1, text2):
    """
    Find words unique to each text.
    Args:
    text1: First text string
    text2: Second text string
    Returns:
    Tuple of (words_only_in_text1, words_only_in_text2)
    """
    # TODO: Find words that appear in one text but not the other
    words1 = process_text(text1)
    words2 = process_text(text2)
    only_in_text1 = words1.difference(words2)
    only_in_text2 = words2.difference(words1)
    return only_in_text1, only_in_text2

def detect_common_phrases(texts, min_occurrences=3):
    """
    Find words that appear in at least min_occurrences texts.
    Args:
    texts: List of text strings
    min_occurrences: Minimum number of texts word must appear in
    Returns:
    Set of common words
    """
    # TODO: Find words appearing in multiple texts
    word_count = Counter()
    for text in texts:
        words = process_text(text)
        for word in words:
            word_count[word] += 1
    common_words = {word for word, count in word_count.items() if count >= min_occurrences}
    return common_words


# Sample texts for analysis
text_samples = {
'student1': """
Python is a powerful programming language. It has efficient
high-level data structures and a simple approach to object-oriented
programming. Python's elegant syntax and dynamic typing make it
an ideal language for scripting.
""",
'student2': """
Python is a high-level programming language. It features dynamic
typing and elegant syntax. Python has simple but effective approach
to object-oriented programming and powerful data structures.
""",
'student3': """
Java is a class-based, object-oriented programming language. It is
designed to have as few implementation dependencies as possible. Java
applications are typically compiled to bytecode.
""",
'original': """
Python is a high-level, general-purpose programming language. Its
design philosophy emphasizes code readability with the use of
significant indentation. Python is dynamically typed and garbage-collected.
"""
}



def plagiarism_check(submissions, threshold=0.7):
    """
    Check for potential plagiarism among submissions.
    Args:
    submissions: Dictionary of {student_id: text}
    threshold: Similarity threshold for flagging (0-1)
    Returns:
    List of (student1, student2, similarity) tuples above threshold
    """
    # TODO: Compare all pairs of submissions
    # TODO: Flag pairs with similarity above threshold
    flagged_pairs = []
    student_ids = list(submissions.keys())
    for i in range(len(student_ids)):
        for j in range(i + 1, len(student_ids)):
            student1 = student_ids[i]
            student2 = student_ids[j]
            sim = calculate_similarity(submissions[student1], submissions[student2])
            if sim >= threshold:
                flagged_pairs.append((student1, student2, sim))
    return flagged_pairs
def writing_style_analysis(text):
    """
    Analyze writing style characteristics.
    Args:
    text: Text to analyze
    Returns:
    Dictionary with style metrics:
    - vocabulary_size: Number of unique words
    - average_word_length: Average length of words
    - word_diversity: Ratio of unique words to total words
    """
    # TODO: Calculate various style metrics
    words = text.split()
    unique_words = process_text(text)
    vocabulary_size = len(unique_words)
    total_words = len(words)
    average_word_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0
    word_diversity = vocabulary_size / total_words if total_words > 0 else 0
    return {
    'vocabulary_size': vocabulary_size,
    'average_word_length': average_word_length,
    'word_diversity': word_diversity
    }

# Test the plagiarism detection
print("\n=== Plagiarism Detection Results ===")
results = plagiarism_check(text_samples, threshold=0.5)
for student1, student2, similarity in results:
    print(f"{student1} vs {student2}: {similarity:.2%} similar")

