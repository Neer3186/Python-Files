#q1
def print_alphabets():
    print("Uppercase letters:")
    for i in range(65, 91):  # ASCII values for A-Z
        print(chr(i), end=' ')
    
    print("\nLowercase letters:")
    for i in range(97, 123):  # ASCII values for a-z
        print(chr(i), end=' ')

print_alphabets()

#q2
def multi_(n):
    for i in range(11):
        a = i * n
        print(n, "*", i, "=", a)

n = int(input("Enter the number: "))
multi_(n)

#q3
def count_alpha_digits(s):
    a = 0
    d = 0

    for char in s:
        if char.isalpha():
            a += 1
        elif char.isdigit():
            d += 1

    print("Number of alphabets:", a)
    print("Number of digits:", d)

s = input("Enter a string: ")
count_alpha_digits(s)


#q4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n <= 0:
        return False
    sum_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_divisors == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d**power for d in digits) == n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    square = n * n
    return str(square).endswith(str(n))

def check_number(n):
    print(f"Checking number: {n}")
    print("Prime:", is_prime(n))
    print("Perfect:", is_perfect(n))
    print("Armstrong:", is_armstrong(n))
    print("Palindrome:", is_palindrome(n))
    print("Automorphic:", is_automorphic(n))

n = int(input("Enter a number: "))
check_number(n)

#q5
def pythagoras_(l):
    print(f"Pythagorean triplets with side length ≤ {l}:")
    for a in range(1, l + 1):
        for b in range(a, l + 1):  
            c_sq = a*a + b*b
            c = int(c_sq**0.5)
            if c <= l and c*c == c_sq:
                print(f"({a}, {b}, {c})")

pythagoras_(30)

#q6
def print_24_hours():
    for hour in range(0, 24):
        if hour == 0:
            print("12:00 Midnight")
        elif hour == 12:
            print("12:00 Noon")
        elif hour < 12:
            print(f"{hour}:00 AM")
        else:
            print(f"{hour - 12}:00 PM")

print_24_hours()

#q7
import math

def nCr(n, r):
    return math.comb(n, r)  

def nPr(n, r):
    return math.perm(n, r)  

n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))

print(f"nCr = {nCr(n, r)}")
print(f"nPr = {nPr(n, r)}")

#q8
import math

def factorial(n):
    return math.factorial(n)

num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")

#q9
def print_reverse_natural_numbers(n):
    for i in range(n, 0, -1):
        print(i, end=" ")

n = int(input("Enter a number: "))
print_reverse_natural_numbers(n)

#10
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter the number of Fibonacci numbers you want: "))
fibonacci(n)

#q11
import math

def sin_approximation(x, terms=10):
    result = 0
    for n in range(terms):
        sign = (-1) ** n  
        power = 2 * n + 1  
        factorial = math.factorial(power)
        result += sign * (x ** power) / factorial
    return result


x_degree = float(input("Enter x in degrees: "))
x_radian = x_degree * (math.pi / 180)  
print(f"sin({x_degree} degrees) ≈ {sin_approximation(x_radian)}")



