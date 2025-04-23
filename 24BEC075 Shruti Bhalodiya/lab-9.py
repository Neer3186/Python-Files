#Lab-9:Functions

# 1. Recursive function to obtain prime factors
def prime_factors(n, divisor=2):
    if n == 1:
        return []
    if n % divisor == 0:
        return [divisor] + prime_factors(n // divisor, divisor)
    else:
        return prime_factors(n, divisor + 1)

print("\n#1: Prime Factors using Recursion")
number = int(input("Enter a positive integer to find its prime factors: "))
print("Prime factors:", prime_factors(number))

# 2. Function to find binary equivalent of a number
def to_binary(n):
    if n == 0:
        return "0"
    else:
        return to_binary(n // 2) + str(n % 2)

print("\n#2: Binary Equivalent using Recursion")
num = int(input("Enter a positive integer to find its binary equivalent: "))
print(f"Binary equivalent of {num} is:", to_binary(num))

# 3. Recursive function to count vowels in a string
def count_vowels(s):
    if len(s) == 0:
        return 0
    elif s[0].lower() in 'aeiou':
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])

print("\n#3: Count Vowels in a String using Recursion")
input_string = input("Enter a string to count vowels: ")
print("Number of vowels:", count_vowels(input_string))

# 4. Recursive function to reverse a list
def reverse_list(lst):
    if len(lst) == 0:
        return []
    else:
        return [lst[-1]] + reverse_list(lst[:-1])

print("\n#4: Reverse a List using Recursion")
num_list = [int(x) for x in input("Enter numbers separated by spaces to reverse: ").split()]
print("Reversed list:", reverse_list(num_list))

# 5. Recursive function to calculate a^b (a raised to the power b)
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)

print("\n#5: Calculate a^b using Recursion")
base = int(input("Enter the base number a: "))
exponent = int(input("Enter the exponent b: "))
print(f"{base} raised to the power {exponent} is:", power(base, exponent))

# 6. Recursive function to sanitize a list by replacing negative numbers with 0
def sanitize_list(lst):
    if len(lst) == 0:
        return []
    else:
        sanitized_value = 0 if lst[0] < 0 else lst[0]
        return [sanitized_value] + sanitize_list(lst[1:])

print("\n#6: Sanitize List (replace negatives with 0) using Recursion")
mixed_list = [int(x) for x in input("Enter numbers separated by spaces (some negative, some positive): ").split()]
print("Sanitized list:", sanitize_list(mixed_list))

# 7. Recursive function to obtain average of all numbers in a list
def average(lst, total=0, count=0):
    if len(lst) == 0:
        return total / count if count != 0 else 0
    else:
        return average(lst[1:], total + lst[0], count + 1)

print("\n#7: Average of List using Recursion")
num_list = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
print("Average of the list:", average(num_list))

# 8. Recursive function to find the length of a string
def string_length(s):
    if len(s) == 0:
        return 0
    else:
        return 1 + string_length(s[1:])

print("\n#8: Length of String using Recursion")
input_string = input("Enter a string to find its length: ")
print("Length of the string:", string_length(input_string))
