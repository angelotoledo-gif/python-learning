# TODO: Add __str__ method
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        # Return "Title by Author (X pages)"
        return f"{self.title} by {self.author} ({self.pages} pages)"
    
# Test: 
book = Book("Python 101", "Jane Doe", 350)
print(book) # Should print: Python 101 by Jane Doe (350 pages)



# TODO: Add __len__ and __bool__
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    def add_song(self, song):
        self.songs.append(song)
    def __str__(self):
        # Return "Playlist: name (X songs)"
        return f"Playlist: {self.name} ({len(self.songs)} songs)"
        
    def __len__(self):
        # Return number of songs
        return len(self.songs)
    def __bool__(self):
        # True if has songs
        return len(self.songs) > 0
# Test with empty and full playlist



# TODO: Matrix with both __str__ and __repr__
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0]*cols for _ in range(rows)]
    def __str__(self):
        # Return nice grid format
        # 0 0 0
        # 0 0 0
        return '\n'.join(' '.join(str(cell) for cell in row) for row in self.data)
    
    def __repr__(self):
        # Return "Matrix(rows, cols)"
        return f"Matrix({self.rows}, {self.cols})"
    def __len__(self):
        # Return total elements (rows * cols)
        return self.rows * self.cols



# TODO: Add money with + operator
class Money:
    def __init__(self, dollars):
        self.dollars = dollars
    def __str__(self):
        return f"${self.dollars:.2f}"
    def __add__(self, other):
        # Return new Money with sum
        return Money(self.dollars + other.dollars)
    
# Test:
m1 = Money(10.50)
m2 = Money(5.25)
m3 = m1 + m2
print(m3) # Should print: $15.75



# TODO: Fraction math
class Fraction:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator
    def __str__(self):
        return f"{self.num}/{self.den}"
    def __add__(self, other):
        # Add fractions: a/b + c/d = (a*d + b*c)/(b*d)
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
    def __mul__(self, other):
        # Multiply: a/b * c/d = (a*c)/(b*d)
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
# Test:
f1 = Fraction(1, 2) # 1/2
f2 = Fraction(1, 3) # 1/3
print(f1 + f2) # Should be 5/6



# TODO: Compare game scores
class Score:
    def __init__(self, points):
        self.points = points
    def __str__(self):
        return f"Score: {self.points}"
    def __eq__(self, other):
        # Return True if points equal
        return self.points == other.points
    def __lt__(self, other):
        # Return True if less points
        return self.points < other.points
# Test:
s1 = Score(100)
s2 = Score(85)
print(s1 > s2) # Should be True



# TODO: Compare dates
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __str__(self):
        return f"{self.month:02d}/{self.day:02d}/{self.year}"
    def __eq__(self, other):
        # Check if same date
        return (self.year == other.year and
                self.month == other.month and
                self.day == other.day)
    def __lt__(self, other):
        # Check if earlier date
        # Compare year, then month, then day
        if self.year != other.year:
            return self.year < other.year
# Test with different dates



# TODO: Items with priority for queue
class PriorityItem:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority # Higher = more important
    def __str__(self):
        return f"{self.data} (P:{self.priority})"
    def __lt__(self, other):
        # Higher priority comes first!
        # So reverse the comparison
        return self.priority > other.priority
    def __eq__(self, other):
        # Equal if same priority
        return self.priority == other.priority
# Test sorting by priority



# TODO: Basic indexing
class SimpleGrades:
    def __init__(self):
        self.grades = {}
    def __getitem__(self, name):
        # Return grade or 0 if not found
        return self.grades.get(name, 0)
    def __setitem__(self, name, grade):
        # Store the grade
        self.grades[name] = grade
# Test:
book = SimpleGrades()
book["Alice"] = 95
print(book["Alice"])



# TODO: Cache with limited size
class Cache:
    def __init__(self, max_size=3):
        self.data = {}
        self.max_size = max_size
    def __getitem__(self, key):
        # Return value or None
        return self.data.get(key, None)
    def __setitem__(self, key, value):
        # Add to cache
        # If full, remove oldest item
        if len(self.data) >= self.max_size:
            oldest_key = next(iter(self.data))
            del self.data[oldest_key]
    def __contains__(self, key):
        # Check if key in cache
        return key in self.data
    


# TODO: Matrix that saves memory
class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = {} # Only store non-zero values
    def __getitem__(self, pos):
        # pos is tuple (row, col)
        # Return value or 0
        return self.data.get(pos, 0)
    def __setitem__(self, pos, value):
        # Only store if value != 0
        if value != 0:
            self.data[pos] = value
        elif pos in self.data:
            del self.data[pos]
    def __str__(self):
        # Print as grid
        result = []
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                row.append(str(self[r, c]))
            result.append(' '.join(row))
        return '\n'.join(result)
        
# Test:
# matrix = SparseMatrix(3, 3)
# matrix[0, 0] = 5
# matrix[1, 1] = 10
# print(matrix[0, 0]) # 5
# print(matrix[2, 2]) # 0