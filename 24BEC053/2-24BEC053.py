'''#CP1
x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))

if(x>y):
    print(x, "Is the largest number")
    print(y,"Is the smallest number")
elif(x==y):
    print("Both the values are same ")
else:
    print(x,"Is the smallest number")
    print(y,"Is the largest number")


#CP2
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))

if a>=b and a>=c :
    print(a,"is the largest number.")

elif b>=c and b>=c:
    print(b,"is the largest number.")
else:
    print(c,"is the largest number.")
    


#CP3
n=int(input("Enter a number:"))
if (n%2==0):
    print("The number is even.")
else:
    print("The number is odd.")

'''

#CP4
n=int(input("Enter a number:"))
if (n%10==0):
    print("The number is divisible by 10.")
else:
    print("The number is no tdivisible by 10.")

#CP5
age = int(input("Enter age: "))
    if age < 18:
        print("Minor")
    else:
        print("Major")

#CP6
n = int(input("Enter a number: "))
n = abs(n)
count = 0
    if n == 0:
        count = 1
    else:
        while n > 0:
            count += 1
            n //= 10
    print("Number of digits:", count)

#CP7
year = int(input("Enter a year: "))
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

#CP8

a1 = int(input("Enter angle 1: "))
a2 = int(input("Enter angle 2: "))
a3 = int(input("Enter angle 3: "))
    if a1 + a2 + a3 == 180:
        print("Valid Triangle")
    else:
        print("Invalid Triangle")

#CP9
n = int(input("Enter a number: "))
    if n < 0:
        print("Absolute value:", -n)
    else:
        print("Absolute value:", n)

#CP10

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
area = l * b
peri = 2 * (l + b)
    if area > peri:
        print("Area is greater")
    else:
        print("Perimeter is greater")
#CP11
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
x3 = int(input("x3: "))
y3 = int(input("y3: "))
    if (y2 - y1)(x3 - x1) == (y3 - y1)(x2 - x1):
        print("Points are collinear")
    else:
        print("Points are not collinear")
#CP12

import math
x = int(input("Enter x: "))
y = int(input("Enter y: "))
cx = int(input("Enter center x: "))
cy = int(input("Enter center y: "))
r = int(input("Enter radius: "))
d = math.sqrt((x - cx)*2 + (y - cy)*2)
    if d < r:
        print("Inside the circle")
    elif d == r:
        print("On the circle")
    else:
        print("Outside the circle")

#CP13
n = int(input("Enter number (0-19): "))
words = ["zero", "one", "two", "three", "four", "five", "six", "seven",
         "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
         "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
if 0 <= n <= 19:
    print(words[n])
else:
    print("Out of range")
#CP14
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
total = m1 + m2 + m3
avg = total / 3
print("Total:", total)
print("Average:", avg)
if m1 <= 39 or m2 <= 39 or m3 <= 39:
    print("Result: Fail")
else:
    print("Result: Pass")
for marks in [m1, m2, m3]:
    if marks == 0:
        print("Grade: NA")
    elif marks <= 39:
        print("Grade: F")
    elif marks <= 44:
        print("Grade: P")
    elif marks <= 49:
        print("Grade: C")
    elif marks <= 54:
        print("Grade: B")
    elif marks <= 59:
        print("Grade: B+")
    elif marks <= 69:
        print("Grade: A")
    elif marks <= 79:
        print("Grade: A+")
    elif marks <= 100:















