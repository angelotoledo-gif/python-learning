def count_lines_with_word(filename, word):

    try:
        with open(filename, 'r') as file:
            count = sum(1 for line in file if word in line)
        return count
    except FileNotFoundError:
        return 0
    

class BankAccount:
    '''A simple bank account class.'''
    def __init__(self, Owner_Name, initial_balance=0):
        self.Owner_Name = Owner_Name
        self.balance = initial_balance
    def deposit(self, amount):
        '''Deposit money into the account.'''
        if amount > 0:
            self.balance += amount
        return self.balance
    def withdraw(self, amount):
        '''Withdraw money from the account'''
        if amount > self.balance:
            return f"Insufficient funds. Current balance: {self.balance}"
        else:
            self.balance -= amount
            return self.balance
    def get_balance(self):
        '''Return the current balance.'''
        return self.balance
print("Exercise2:")
account = BankAccount("John", 100)
print(account.deposit(50))
print(account.withdraw(30))
print(account.withdraw(200))


def safe_calculate(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Error: Invalid number"

    try:
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            return num1 / num2
        else:
            return "Error: invalid operation"
    except ZeroDivisionError:
        return "Error: Division by zero"

print("Exercise 3:")
print(safe_calculate(10, 5, '+'))
print(safe_calculate(10, 5, '-'))
print(safe_calculate(10, 0, '/'))
print(safe_calculate("abc", 5, '+'))

print("Exercise 4:")

def is_palindrome_recursive(s):
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])

print(is_palindrome_recursive("racecar"))
print(is_palindrome_recursive("hello"))
print(is_palindrome_recursive("A man a plan a canal Panama"))
print(is_palindrome_recursive(""))