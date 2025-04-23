#Lab-9A:Functional Programming

# 1. Define three functions and store them in a list, then call them one by one in a loop
def fun():
    print("This is fun() function.")

def disp():
    print("This is disp() function.")

def msg():
    print("This is msg() function.")

# Store functions in a list
functions = [fun, disp, msg]

# Call each function in the list
print("\n#1: Calling functions from a list:")
for func in functions:
    func()

# 2. Add corresponding elements of two lists using map and lambda
list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 5, 4, 3, 2, 1]

# Using map and lambda to add corresponding elements
sum_list = list(map(lambda x, y: x + y, list1, list2))

print("\n#2: List obtained by adding corresponding elements of two lists:")
print(sum_list)

# 3. Generate a list of 10 random numbers and create a new list of their squares
import random

# Generate 10 random numbers between -15 and 15
random_list = [random.randint(-15, 15) for _ in range(10)]
# Create a new list by squaring all numbers using map and lambda
squared_list = list(map(lambda x: x**2, random_list))

print("\n#3: List of random numbers and their squares:")
print("Random numbers:", random_list)
print("Squared numbers:", squared_list)

# 4. Find palindromes in a list of strings
lst = ['madam', 'Python', 'malayalam', 12321]

# Convert numbers to strings and filter for palindromes
palindromes = list(filter(lambda x: str(x) == str(x)[::-1], lst))

print("\n#4: Palindromes in the list:")
print(palindromes)

# 5. Filter out names with more than 8 characters
faculty_names = ['John Doe', 'Catherine', 'Alexandra', 'Mark', 'Benjamin']

# Using filter to find names with length greater than 8
long_names = list(filter(lambda name: len(name) > 8, faculty_names))

print("\n#5: Names with more than 8 characters:")
print(long_names)
