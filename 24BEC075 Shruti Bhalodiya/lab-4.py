#Lab-4:Loop Structure in Python

# 1. Print all alphabets in upper case and lower case
def print_alphabets():
    print("\n1. Alphabets in lower case:")
    for i in range(97, 123):
        print(chr(i), end=' ')
    print("\nAlphabets in upper case:")
    for i in range(65, 91):
        print(chr(i), end=' ')
    print()

# 2. Print multiplication table of a given number
def multiplication_table():
    print("\n2. Multiplication Table")
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# 3. Count alphabets and digits in a given string
def count_alpha_digit():
    print("\n3. Count Alphabets and Digits")
    s = input("Enter a string: ")
    alpha = digit = 0
    for ch in s:
        if ch.isalpha():
            alpha += 1
        elif ch.isdigit():
            digit += 1
    print("Alphabets:", alpha, "Digits:", digit)

# 4. Check if a number is prime, perfect, Armstrong, palindrome, automorphic
def check_number_properties():
    print("\n4. Number Properties Check")
    n = int(input("Enter a number: "))

    # Prime
    is_prime = n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
    print("Prime:", is_prime)

    # Perfect
    is_perfect = sum(i for i in range(1, n) if n % i == 0) == n
    print("Perfect:", is_perfect)

    # Armstrong
    is_armstrong = sum(int(d)**len(str(n)) for d in str(n)) == n
    print("Armstrong:", is_armstrong)

    # Palindrome
    is_palindrome = str(n) == str(n)[::-1]
    print("Palindrome:", is_palindrome)

    # Automorphic
    is_automorphic = str(n**2).endswith(str(n))
    print("Automorphic:", is_automorphic)

# 5. Generate all Pythagorean Triplets with side length <= 30
def pythagorean_triplets():
    print("\n5. Pythagorean Triplets (sides <= 30):")
    for a in range(1, 31):
        for b in range(a, 31):
            c = (a**2 + b**2)**0.5
            if c == int(c) and c <= 30:
                print(f"{a}, {b}, {int(c)}")

# 6. Print 24 hours of the day with suffixes
def print_day_hours():
    print("\n6. 24 Hours with AM/PM/Noon/Midnight:")
    for h in range(24):
        if h == 0:
            print("12 Midnight")
        elif h == 12:
            print("12 Noon")
        elif h < 12:
            print(f"{h} AM")
        else:
            print(f"{h - 12} PM")

# 7. Print nCr and nPr
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def nCr_nPr():
    print("\n7. Calculate nCr and nPr")
    n = int(input("Enter n: "))
    r = int(input("Enter r: "))
    print(f"nCr = {factorial(n) // (factorial(r) * factorial(n - r))}")
    print(f"nPr = {factorial(n) // factorial(n - r)}")

# 8. Print factorial of a given number
def print_factorial():
    print("\n8. Factorial Calculation")
    n = int(input("Enter a number: "))
    print(f"Factorial of {n} is {factorial(n)}")

# 9. Print N natural numbers in reverse
def reverse_naturals():
    print("\n9. N Natural Numbers in Reverse")
    n = int(input("Enter N: "))
    for i in range(n, 0, -1):
        print(i, end=' ')
    print()

# 10. Generate N numbers of Fibonacci series
def fibonacci():
    print("\n10. Fibonacci Series")
    n = int(input("Enter how many numbers to generate: "))
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

# 11. Calculate sin(x) using Taylor Series
def sin_series():
    print("\n11. Calculate sin(x) using Taylor Series")
    x_deg = float(input("Enter angle in degrees: "))
    terms = int(input("Enter number of terms: "))
    x = x_deg * 3.14159 / 180
    sinx = 0
    for i in range(terms):
        sign = (-1) ** i
        power = 2 * i + 1
        term = sign * (x ** power) / factorial(power)
        sinx += term
    print(f"sin({x_deg}) ≈ {sinx}")

if __name__ == "__main__":
    print_alphabets()
    multiplication_table()
    count_alpha_digit()
    check_number_properties()
    pythagorean_triplets()
    print_day_hours()
    nCr_nPr()
    print_factorial()
    reverse_naturals()
    fibonacci()
    sin_series()
