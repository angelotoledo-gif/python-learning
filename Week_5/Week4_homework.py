import numpy as np
np.random.seed(1350)

def problem1():
    # a) Create a 1D array of integers from 10 to 50 (inclusive) with step 5
    arr_1 = np.arange(10, 51, 5)
    print("Problem 1a:\n", arr_1)
    # b) Create a 2D array of shape (3, 4) with random integers between 0 and 20
    arr_2 = np.random.randint(0, 21, size=(3, 4))
    print("Problem 1b:\n", arr_2)
    # c) create a 3x3 identity matrix
    identity = np.eye(3)
    print("Problem 1c:\n", identity)
    # d) Create an array of 10 evenly spaced numbers between 0 and 5
    linspace_arr = np.linspace(0, 5, 10)
    print("Problem 1d:\n", linspace_arr)
    # e) Create a random array of shape (2, 5) with values between 0 and 1
    random_arr = np.random.rand(2, 5)
    print("Problem 1e:\n", random_arr)
    return arr_1, arr_2, identity, linspace_arr, random_arr
problem1()

def problem2():
    # Given arrays
    arr_a = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
    arr_b = np.array([10, 20, 30])
    # a) Add arr_b to each row of arr_a (using broadcasting)
    result_add = arr_a + arr_b
    print("Problem 2a:\n", result_add)
    # b) Multiply each column of arr_a by the corresponding element in arr_b
    result_multiply = arr_a * arr_b.reshape(3, 1)
    print("Problem 2b:\n", result_multiply)
    # c) Calculate the square of all elements in arr_a
    result_square = arr_a ** 2
    print("Problem 2c:\n", result_square)
    # d) Calculate the mean of each column in arr_a
    column_mean = np.mean(arr_a, axis=0)
    print("Problem 2d:\n", column_mean)
    # e) Subtract the column means from each element in the respective column
    centered_arr = arr_a - column_mean
    print("Problem 2e:\n", centered_arr)
    return result_add, result_multiply, result_square, column_mean, centered_arr
problem2()

def problem3():
    # Create a 5x5 array with values from 1 to 25
    arr = np.arange(1, 26).reshape(5, 5)
    print("Problem 3 - Original Array:\n", arr)
    # a) Extract the third row
    third_row = arr[2, :]
    print("Problem 3a - Third Row:\n", third_row)
    # b) Extract the last column
    last_column = arr[:, -1]
    print("Problem 3b - Last Column:\n", last_column)
    # c) Extract the 2x2 subarray from the center (rows 1-2, columns 1-2)
    center_subarray = arr[1:3, 1:3]
    print("Problem 3c - Center Subarray:\n", center_subarray)
    # d) Extract all elements greater than 15
    greater_than_15 = arr[arr > 15]
    print("Problem 3d - Elements Greater than 15:\n", greater_than_15)
    # e) Replace all even numbers with -1 (create a copy first)
    arr_copy = arr.copy()
    arr_copy[arr_copy % 2 == 0] = -1
    print("Problem 3e - Replace Even Numbers with -1:\n", arr_copy)
    return third_row, last_column, center_subarray, greater_than_15, arr_copy
problem3()

def problem4():
    # Student test scores (rows: students, columns: tests)
    scores = np.array([[85, 90, 78, 92],
                    [79, 85, 88, 91],
                    [92, 88, 95, 89],
                    [75, 72, 80, 78],
                    [88, 91, 87, 94]])
    
    # a) Calculate the average score for each student (across all tests)
    student_averages = np.mean(scores, axis=1)
    print("Problem 4a - Student Averages:\n", student_averages)
    # b) Calculate the average score for each test (across all students)
    test_averages = np.mean(scores, axis=0)
    print("Problem 4b - Test Averages:\n", test_averages)
    # c) Find the highest score in each test
    highest_scores = np.max(scores, axis=0)
    print("Problem 4c - Highest Scores:\n", highest_scores)
    # d) Find the standard deviation of scores for each test
    std_dev_scores = np.std(scores, axis=0)
    print("Problem 4d - Standard Deviation of Scores:\n", std_dev_scores)
    # e) Identify using boolean which students have an average score above 85
    above_85 = student_averages > 85
    print("Problem 4e - Students with Average Score Above 85:\n", above_85)
    return student_averages, test_averages, highest_scores, std_dev_scores, above_85
problem4()

def problem6():
    """
    Compare performance between NumPy arrays and Python lists.
    Complete the timing comparisons.
    """
    import time
    import numpy as np

    size = 100000

    # Create Python list and NumPy array with same data
    python_list = list(range(size))
    numpy_array = np.arange(size)

    # --- Python list approach ---
    start_time = time.time()
    list_result = [x ** 2 for x in python_list]  # square all elements using list comprehension
    list_time = time.time() - start_time

    # --- NumPy array approach ---
    start_time = time.time()
    array_result = numpy_array ** 2  # vectorized squaring
    numpy_time = time.time() - start_time

    # --- Calculate speedup ---
    speedup = list_time / numpy_time

    # Return results
    return {
        'list_time': list_time,
        'numpy_time': numpy_time,
        'speedup': speedup,
        'conclusion': f"NumPy is {speedup:.1f}x faster than Python lists for this operation"
    }
results = problem6()
print("Problem 6 - Performance Comparison:\n", results)