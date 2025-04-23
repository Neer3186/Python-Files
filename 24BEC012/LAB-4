#1
for i in range(65, 91):
    print(chr(i), end=' ')
print()
for i in range(97, 123):
    print(chr(i), end=' ')

#2
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#3
string = input("Enter a string: ")
alphabets = 0
digits = 0
for char in string:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
print(f"Alphabets: {alphabets}, Digits: {digits}")

#4
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

n = int(input("Enter a number: "))
divisor_sum = 0
for i in range(1, n):
    if n % i == 0:
        divisor_sum += i
if divisor_sum == n:
    print(n, "is a perfect number")
else:
    print(n, "is not a perfect number")

num = int(input("Enter a number: "))
num_str = str(num)
length = len(num_str)
sum = 0
for digit in num_str:
    sum += int(digit) ** length
if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

n = int(input("Enter a number: "))
if str(n) == str(n)[::-1]:
    print(n, "is a palindrome")
else:
    print(n, "is not a palindrome")

n = int(input("Enter a number: "))
square = n ** 2
str_n = str(n)
str_square = str(square)
if str_square.endswith(str_n):
    print(n, "is an automorphic number.")
else:
    print(n, "is not an automorphic number.")

#5
limit = 30
triplets = []
for a in range(1, limit + 1):
    for b in range(a, limit + 1):
        for c in range(b, limit + 1):
            if a ** 2 + b ** 2 == c ** 2:
                triplets.append((a, b, c))
print("Pythagorean Triplets (Brute Force):")
for triplet in triplets:
    print(triplet)

#6
for h in range(1, 12):
    print(f"{h} AM")
print("12 Noon")
for h in range(1, 12):
    print(f"{h} PM")
print("12 Midnight")

#7
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter n: "))
r = int(input("Enter r: "))
nCr = factorial(n) // (factorial(r) * factorial(n - r))
nPr = factorial(n) // factorial(n - r)
print(f"nCr: {nCr}, nPr: {nPr}")

import math
n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
print(f"{n}C{r} (Combination) = {math.comb(n, r)}")
print(f"{n}P{r} (Permutation) = {math.perm(n, r)}")

#8
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"The factorial of {number} is {factorial}")

#9
n = int(input("Enter N: "))
for i in range(n, 0, -1):
    print(i, end=' ')

#10
n = int(input("Enter the number of terms: "))
a, b = 0, 1
print(a, b, end=' ')
for _ in range(n - 2):
    a, b = b, a + b
    print(b, end=' ')

#11
import math
x_deg = float(input("Enter angle in degrees: "))
x = x_deg * (math.pi / 180)
sin_x = 0
for i in range(10):
    term = ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
    sin_x += term
print(f"sin({x_deg}°) ≈ {sin_x}")
